# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Fetch emails for chris.robert@interpride.org via gog and encode needed follow-ups
as tasks in Taskwarrior (project: interpride.governance).

Usage via pipx:
  pipx run fetch_emails.py                    # Fetch new emails & sync follow-up tasks
  pipx run fetch_emails.py --dry-run          # Inspect detected tasks without adding to Taskwarrior
  pipx run fetch_emails.py --sync-tasks-only  # Process existing emails in emails_audit.jsonl
  pipx run fetch_emails.py --fetch-only       # Only pull emails without encoding tasks
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

OUTPUT_FILE = Path("emails_audit.jsonl")
STATE_FILE = Path(".email_tasks_state.json")
ACCOUNT = "chris.robert@interpride.org"
PROJECT = "interpride.governance"
DEFAULT_MODEL = "openrouter/openrouter/free"

# ----------------------------------------------------------------------
# Gmail Fetching Logic
# ----------------------------------------------------------------------

def fetch_page(page_token=None):
    cmd = [
        "gog", "gmail", "messages", "search", "in:anywhere",
        "-a", ACCOUNT,
        "--max=10",
        "--include-body",
        "--body-format=text",
        "--json"
    ]
    if page_token:
        cmd.extend(["--page", page_token])

    while True:
        try:
            res = subprocess.run(cmd, capture_output=True, text=True, check=False)
            if res.returncode == 0:
                data = json.loads(res.stdout)
                return data

            err = res.stderr or res.stdout
            if any(term in err for term in ["rateLimitExceeded", "403", "429"]):
                print("[Quota Exceeded] Gmail quota hit. Waiting 60s for reset...", file=sys.stderr)
                time.sleep(60)
                continue
            else:
                print(f"[Error] gog failed (exit {res.returncode}): {err.strip()}", file=sys.stderr)
                return None
        except Exception as e:
            print(f"[Exception] {e}. Waiting 15s...", file=sys.stderr)
            time.sleep(15)

def fetch_incremental_emails():
    """Fetch newly arrived emails and append them to emails_audit.jsonl."""
    print(f"Starting incremental email pull for {ACCOUNT}...")
    seen_ids = set()

    if OUTPUT_FILE.exists():
        with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        item = json.loads(line)
                        if "id" in item:
                            seen_ids.add(item["id"])
                    except Exception:
                        pass
        print(f"Found {len(seen_ids)} existing messages in {OUTPUT_FILE}.")

    page_token = None
    new_emails = []
    consecutive_seen = 0

    while True:
        data = fetch_page(page_token)
        if not data:
            print("Stopping pull.")
            break

        messages = data.get("messages", [])
        if not messages:
            print("No more messages found.")
            break

        batch_new = 0
        for msg in messages:
            msg_id = msg.get("id")
            if msg_id in seen_ids:
                consecutive_seen += 1
            else:
                consecutive_seen = 0
                seen_ids.add(msg_id)
                new_emails.append(msg)
                batch_new += 1
                with open(OUTPUT_FILE, "a", encoding="utf-8") as out:
                    out.write(json.dumps(msg, ensure_ascii=False) + "\n")

        print(f"Batch returned {len(messages)} messages ({batch_new} new).")

        if consecutive_seen >= 10:
            print("Encountered previously audited messages. Mailbox is fully up to date!")
            break

        page_token = data.get("nextPageToken")
        if not page_token:
            print("Reached end of mailbox.")
            break

        time.sleep(2)

    print(f"Incremental pull complete. {len(new_emails)} new messages captured.")
    return new_emails

# ----------------------------------------------------------------------
# Follow-up Analysis Logic
# ----------------------------------------------------------------------

def load_state():
    if STATE_FILE.exists():
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"Warning: could not read {STATE_FILE}: {e}", file=sys.stderr)
    return {}

def save_state(state):
    try:
        with open(STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving {STATE_FILE}: {e}", file=sys.stderr)

SYSTEM_PROMPT = """You are an executive assistant for Chris Robert, Co-President and Governance leader of InterPride.
Analyze the email to decide if it requires human action, reply, follow-up, document review, decision-making, or task completion by Chris or the InterPride Governance team.

CRITERIA:
- Followup REQUIRED (has_followup: true):
  * Requests for Chris's approval, review, sign-off, or input
  * Outstanding questions or discussions requiring a reply
  * Governance motions, voting preparations, bylaw/standing rule proposals
  * Deadlines, meetings to schedule or prepare materials for
  * Disputes, ombudsperson concerns, compliance inquiries, or external requests
- Followup NOT required (has_followup: false):
  * Automated marketing, newsletters, spam, shipping/billing confirmations
  * Informational-only updates where Chris has no action items or reply needed
  * Threads where another party already closed the matter completely

OUTPUT FORMAT:
Return ONLY a valid JSON object (no markdown, no code block fences, no explanation):
{
  "has_followup": true or false,
  "tasks": [
    {
      "description": "Concise imperative action item (e.g. 'Review draft bylaw amendments from Marsha and reply with approval')",
      "priority": "H" | "M" | "L",
      "due": "YYYY-MM-DD" or null,
      "tags": ["bylaws", "review"]
    }
  ]
}
If has_followup is false, "tasks" must be an empty list [].
"""

def extract_followup_tasks(email, model=DEFAULT_MODEL):
    """Call llm to determine if follow-up is needed and extract tasks."""
    sender = email.get("from", "")
    subject = email.get("subject", "")
    date = email.get("date", "")
    body = email.get("body", "")

    # Truncate body if excessively long to keep prompt clean and within token budget
    truncated_body = body[:8000] if body else "(No text body)"

    prompt = f"""EMAIL DETAILS:
From: {sender}
Date: {date}
Subject: {subject}

Content:
{truncated_body}
"""
    cmd = ["llm", "prompt", "-s", SYSTEM_PROMPT, "-m", model]
    try:
        res = subprocess.run(cmd, input=prompt, capture_output=True, text=True, check=False)
        if res.returncode != 0:
            print(f"LLM execution warning (code {res.returncode}): {res.stderr.strip()}", file=sys.stderr)
            return {"has_followup": False, "tasks": []}

        out = res.stdout.strip()
        # Clean potential markdown fencing
        out = re.sub(r"^```(?:json)?\s*", "", out)
        out = re.sub(r"\s*```$", "", out)

        data = json.loads(out)
        return data
    except json.JSONDecodeError:
        # Fallback regex extraction of JSON block
        match = re.search(r"\{.*\}", out, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(0))
            except Exception:
                pass
        print(f"Could not parse LLM output as JSON: {out[:100]}...", file=sys.stderr)
        return {"has_followup": False, "tasks": []}
    except Exception as e:
        print(f"Exception during LLM analysis: {e}", file=sys.stderr)
        return {"has_followup": False, "tasks": []}

# ----------------------------------------------------------------------
# Taskwarrior Integration
# ----------------------------------------------------------------------

def add_task_to_taskwarrior(task_info, email, dry_run=False):
    """Add a task into Taskwarrior with project: interpride.governance and email metadata."""
    desc = task_info.get("description", "").strip()
    if not desc:
        return None

    priority = task_info.get("priority", "M")
    due = task_info.get("due")
    tags = task_info.get("tags", [])

    # Ensure baseline tags
    tag_set = {"email", "followup"}
    for t in tags:
        clean_tag = re.sub(r"[^a-zA-Z0-9_\-]", "", t.lower())
        if clean_tag:
            tag_set.add(clean_tag)

    cmd = ["task", "add", f"project:{PROJECT}"]
    if priority in ["H", "M", "L"]:
        cmd.append(f"priority:{priority}")
    if due:
        cmd.append(f"due:{due}")
    for t in sorted(tag_set):
        cmd.append(f"+{t}")
    cmd.append(desc)

    sender = email.get("from", "Unknown")
    subject = email.get("subject", "No Subject")
    date = email.get("date", "")
    msg_id = email.get("id", "")
    annotation = f"From: {sender} | Date: {date} | Subject: {subject} | Email-ID: {msg_id}"

    if dry_run:
        print(f"  [DRY-RUN] Command: {' '.join(cmd)}")
        print(f"  [DRY-RUN] Annotation: {annotation}")
        return "dry-run-uuid"

    res = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if res.returncode != 0:
        print(f"  [Error] Failed to add task in taskwarrior: {res.stderr.strip()}", file=sys.stderr)
        return None

    output = res.stdout.strip()
    # Taskwarrior 3.5 output example: "Created task 604."
    m = re.search(r"Created task (\d+)", output)
    task_id = m.group(1) if m else None

    # If task id detected, annotate it with email context
    if task_id:
        anno_cmd = ["task", task_id, "annotate", annotation]
        subprocess.run(anno_cmd, capture_output=True, text=True, check=False)
        print(f"  [Task Created] #{task_id}: {desc}")
        return task_id
    else:
        print(f"  [Task Created] Output: {output}")
        return "created"

# ----------------------------------------------------------------------
# Processing & Synchronization
# ----------------------------------------------------------------------

def process_emails_for_tasks(emails, state, dry_run=False, model=DEFAULT_MODEL):
    """Evaluate emails, extract needed follow-ups, and create Taskwarrior tasks."""
    created_count = 0
    now_iso = datetime.now(timezone.utc).isoformat()

    for idx, email in enumerate(emails, 1):
        msg_id = email.get("id")
        if not msg_id:
            continue

        if msg_id in state and not dry_run:
            continue

        subject = email.get("subject", "(No Subject)")
        sender = email.get("from", "(Unknown)")
        print(f"\n[{idx}/{len(emails)}] Analyzing: {subject[:60]} (From: {sender[:30]})")

        analysis = extract_followup_tasks(email, model=model)
        has_followup = analysis.get("has_followup", False)
        tasks = analysis.get("tasks", [])

        task_records = []
        if has_followup and tasks:
            print(f"  -> Found {len(tasks)} follow-up task(s) required:")
            for t in tasks:
                task_id = add_task_to_taskwarrior(t, email, dry_run=dry_run)
                if task_id:
                    task_records.append(task_id)
                    created_count += 1
        else:
            print("  -> No follow-up required.")

        if not dry_run:
            state[msg_id] = {
                "processed_at": now_iso,
                "has_followup": has_followup,
                "task_ids": task_records,
                "subject": subject
            }
            save_state(state)

    return created_count

# ----------------------------------------------------------------------
# Main CLI Entrypoint
# ----------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Capture InterPride emails and encode follow-ups into Taskwarrior."
    )
    parser.add_argument("--fetch-only", action="store_true", help="Only fetch new emails from Gmail without creating tasks.")
    parser.add_argument("--sync-tasks-only", "--backfill", dest="backfill", action="store_true", help="Backfill/sync tasks for historical unprocessed emails in emails_audit.jsonl.")
    parser.add_argument("--since", type=str, default=None, help="Only backfill emails on or after this date (format: YYYY-MM-DD).")
    parser.add_argument("--dry-run", action="store_true", help="Simulate task generation without modifying Taskwarrior or state.")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of emails to process for tasks (useful for testing).")
    parser.add_argument("--model", type=str, default=DEFAULT_MODEL, help=f"LLM model to use (default: {DEFAULT_MODEL}).")
    args = parser.parse_args()

    # Pre-check tools
    if not shutil.which("task"):
        print("[Error] 'task' (Taskwarrior) is not installed or not in PATH.", file=sys.stderr)
        sys.exit(1)
    if not shutil.which("llm") and not args.fetch_only:
        print("[Error] 'llm' CLI is not installed or not in PATH.", file=sys.stderr)
        sys.exit(1)

    state = load_state()

    # Mode 1: Fetch-only
    if args.fetch_only:
        fetch_incremental_emails()
        return

    # Mode 2: Backfill / Sync tasks from existing emails in emails_audit.jsonl
    if args.backfill:
        if not OUTPUT_FILE.exists():
            print(f"[Error] {OUTPUT_FILE} not found.", file=sys.stderr)
            sys.exit(1)

        print(f"Reading existing emails from {OUTPUT_FILE}...")
        emails = []
        with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    try:
                        emails.append(json.loads(line))
                    except Exception:
                        pass

        # Sort newest first if date or internalDateIso available
        emails.sort(key=lambda m: m.get("internalDateIso", m.get("date", "")), reverse=True)

        # Filter by --since if provided
        if args.since:
            emails = [m for m in emails if (m.get("date", "") >= args.since or m.get("internalDateIso", "") >= args.since)]
            print(f"Filtered to {len(emails)} email(s) on or after {args.since}.")

        # Filter out already processed if not dry-run
        unprocessed = [m for m in emails if m.get("id") not in state]
        print(f"Total matching emails: {len(emails)}. Unprocessed for tasks: {len(unprocessed)}.")

        target = unprocessed if not args.dry_run else emails
        if args.limit:
            target = target[:args.limit]

        created = process_emails_for_tasks(target, state, dry_run=args.dry_run, model=args.model)
        print(f"\nDone. Created {created} follow-up task(s) in Taskwarrior.")
        return

    # Mode 3: Default (Fetch incrementally + immediately encode follow-up tasks for new emails)
    new_emails = fetch_incremental_emails()
    if not new_emails:
        print("\nNo newly captured emails to process for tasks.")
        return

    if args.limit:
        new_emails = new_emails[:args.limit]

    print(f"\nAnalyzing {len(new_emails)} newly captured email(s) for follow-up tasks...")
    created = process_emails_for_tasks(new_emails, state, dry_run=args.dry_run, model=args.model)
    print(f"\nDone. Successfully generated {created} new Taskwarrior task(s).")

if __name__ == "__main__":
    main()
