#!/usr/bin/env python3
"""Validate the minimum safe input schema for lead research."""

import csv
import sys
from pathlib import Path

REQUIRED_COLUMNS = {
    "lead_id",
    "company_name",
    "headquarters_country",
    "industry",
    "company_website",
}


def fail(message: str) -> None:
    print(f"INVALID: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: validate_lead_input.py <lead-list.csv>")

    csv_path = Path(sys.argv[1])
    if not csv_path.is_file():
        fail(f"file not found: {csv_path}")

    with csv_path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        columns = set(reader.fieldnames or [])
        missing = sorted(REQUIRED_COLUMNS - columns)
        if missing:
            fail("missing columns: " + ", ".join(missing))

        rows = list(reader)

    if not rows:
        fail("no lead rows found")

    for index, row in enumerate(rows, start=2):
        for field in REQUIRED_COLUMNS:
            if not (row.get(field) or "").strip():
                fail(f"row {index} is missing {field}")
        if row["headquarters_country"].strip().upper() not in {"KR", "KOR", "대한민국", "한국"}:
            fail(f"row {index} is not headquartered in Korea")

    print(f"VALID: {len(rows)} Korean-headquartered leads ready for public-source research")


if __name__ == "__main__":
    main()
