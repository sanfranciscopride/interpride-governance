# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Downloads InterPride governing documents and resources discovered via the
InterPride WordPress REST API (https://www.interpride.org/wp-json/wp/v2/media)
into organized subdirectories under /Users/chris/Developer/interpride/governance/resources/.
"""

import json
import os
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MANIFEST_PATH = BASE_DIR / "resources_manifest.json"
OUTPUT_DIR = BASE_DIR / "resources"


def categorize_item(item: dict) -> str:
    fname = item["filename"]
    fl = fname.lower()
    if "enmienda" in fl:
        return "02_bylaw_amendments"
    if fl == "ar23.pdf" or "solidarity_3_yr" in fl:
        return "07_strategy_reports_and_990s"
    return item["category"]


def download_one(item: dict, include_other: bool = False) -> tuple[str, str, bool, str]:
    cat = categorize_item(item)
    if not include_other and cat == "08_other_media_pdfs":
        return (cat, item["filename"], True, "skipped (non-governance media)")

    cat_dir = OUTPUT_DIR / cat
    cat_dir.mkdir(parents=True, exist_ok=True)

    # Prefix with media ID or date if duplicate filename exists with different URL
    url = item["url"]
    fname = item["filename"]
    # Keep upload year/month in filename only if collision occurs
    target_path = cat_dir / fname
    if target_path.exists() and target_path.stat().st_size > 0:
        # Check if same filesize or if we need to disambiguate by WP media ID
        expected_size = item.get("filesize") or 0
        if expected_size and abs(target_path.stat().st_size - expected_size) > 1024:
            stem, ext = os.path.splitext(fname)
            target_path = cat_dir / f"{stem}_id{item['id']}{ext}"

    if target_path.exists() and target_path.stat().st_size > 0:
        return (cat, target_path.name, True, "already exists")

    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) InterPrideGovernanceSync/1.0"
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
        target_path.write_bytes(data)
        return (cat, target_path.name, True, f"downloaded ({len(data):,} bytes)")
    except Exception as e:
        return (cat, fname, False, f"ERROR: {e}")


def main() -> None:
    include_all = "--all" in sys.argv
    if not MANIFEST_PATH.exists():
        print(f"Manifest not found at {MANIFEST_PATH}", file=sys.stderr)
        sys.exit(1)

    items = json.loads(MANIFEST_PATH.read_text())
    # Re-save normalized categories
    for item in items:
        item["category"] = categorize_item(item)
    MANIFEST_PATH.write_text(json.dumps(items, indent=2))

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    target_items = [
        x for x in items if include_all or x["category"] != "08_other_media_pdfs"
    ]
    print(f"Downloading {len(target_items)} PDF documents into {OUTPUT_DIR} ...")

    success_count = 0
    fail_count = 0
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = [pool.submit(download_one, item, include_all) for item in target_items]
        for fut in as_completed(futures):
            cat, fname, ok, msg = fut.result()
            if ok:
                success_count += 1
                print(f"[OK] [{cat}] {fname}: {msg}")
            else:
                fail_count += 1
                print(f"[FAIL] [{cat}] {fname}: {msg}", file=sys.stderr)

    print(f"\nCompleted: {success_count} succeeded, {fail_count} failed.")


if __name__ == "__main__":
    main()
