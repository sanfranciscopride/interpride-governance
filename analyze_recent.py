# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
import json
from collections import Counter
import re

def main():
    messages = []
    with open("emails_audit.jsonl", "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                try:
                    messages.append(json.loads(line))
                except Exception:
                    pass

    # The last 55 messages are the newly appended ones
    new_msgs = messages[-55:]
    print(f"Analyzing {len(new_msgs)} new messages...")

    senders = Counter()
    for m in new_msgs:
        senders[m.get("from", "Unknown")] += 1

    print("\n--- NEW SENDERS ---")
    for s, c in senders.most_common(10):
        print(f"{c:2d} | {s}")

    threads = Counter()
    for m in new_msgs:
        subj = m.get("subject", "No Subject")
        clean_subj = re.sub(r'^(Re:\s*|Fwd:\s*|Updated invitation:\s*|Invitation:\s*)+', '', subj, flags=re.I).strip()
        threads[clean_subj] += 1

    print("\n--- NEW THREADS ---")
    for t, c in threads.most_common(15):
        print(f"{c:2d} | {t}")

    print("\n--- NOTABLE HIGHLIGHTS & DECISIONS ---")
    for m in new_msgs:
        subj = m.get("subject", "")
        body = m.get("body", "")
        date = m.get("date", "")
        sender = m.get("from", "")
        text = f"{subj} {body}".lower()

        if any(w in text for w in ["election", "vote", "motion", "winner", "result", "worldpride", "bylaw", "urgent", "approved"]):
            lines = [l.strip() for l in body.split("\n") if l.strip() and not l.strip().startswith(">")]
            snippet = " ".join(lines[:2])[:160]
            print(f"- [{date}] {sender}: {subj}")
            print(f"  Snippet: {snippet}...\n")

if __name__ == "__main__":
    main()
