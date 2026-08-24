from __future__ import annotations

import argparse
import csv
from pathlib import Path

EXPECTED_NUMBER_FIELDS = [f"n{i}" for i in range(1, 21)]
REQUIRED_FIELDS = [
    "date",
    "official_draw",
    "internal_draw",
    *EXPECTED_NUMBER_FIELDS,
    "source",
    "source_url",
    "note",
]


def load_and_validate(data_dir: Path) -> list[dict[str, str]]:
    paths = sorted(data_dir.glob("super_keno_draws_part_*.csv"))
    if not paths:
        raise ValueError(f"No Super Keno data shards found in {data_dir}")

    rows: list[dict[str, str]] = []
    seen_dates: set[str] = set()
    seen_official: set[str] = set()
    seen_combos: set[tuple[int, ...]] = set()

    for path in paths:
        with path.open(newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames != REQUIRED_FIELDS:
                raise ValueError(f"Unexpected schema in {path}: {reader.fieldnames}")

            for line_no, row in enumerate(reader, start=2):
                date = row["date"].strip()
                if not date:
                    raise ValueError(f"Missing date in {path}:{line_no}")
                if date in seen_dates:
                    raise ValueError(f"Duplicate date {date} in {path}:{line_no}")

                numbers = [int(row[field]) for field in EXPECTED_NUMBER_FIELDS]
                if len(set(numbers)) != 20 or not all(1 <= n <= 70 for n in numbers):
                    raise ValueError(f"Invalid 20-number draw in {path}:{line_no}: {numbers}")

                combo = tuple(sorted(numbers))
                if combo in seen_combos:
                    raise ValueError(f"Duplicate 20-number combination at {date}")

                official = row["official_draw"].strip()
                if official:
                    normalized = str(int(float(official)))
                    if normalized in seen_official:
                        raise ValueError(f"Duplicate official draw id {normalized}")
                    row["official_draw"] = normalized
                    seen_official.add(normalized)

                internal = row["internal_draw"].strip()
                if internal:
                    row["internal_draw"] = str(int(float(internal)))

                seen_dates.add(date)
                seen_combos.add(combo)
                rows.append({field: row.get(field, "") for field in REQUIRED_FIELDS})

    rows.sort(key=lambda row: row["date"])
    return rows


def write_master(rows: list[dict[str, str]], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=REQUIRED_FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate and assemble Super Keno draw data")
    parser.add_argument("--data-dir", type=Path, default=Path("data"))
    parser.add_argument("--write-master", type=Path)
    args = parser.parse_args()

    rows = load_and_validate(args.data_dir)
    if args.write_master:
        write_master(rows, args.write_master)

    print(f"validated_draws={len(rows)}")
    print(f"earliest={rows[0]['date']}")
    print(f"latest={rows[-1]['date']}")


if __name__ == "__main__":
    main()
