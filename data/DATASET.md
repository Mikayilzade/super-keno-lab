# Super Keno historical dataset

As of 2026-10-11, **248 structurally validated draws** are stored in five chronological CSV shards. This is a historical collection, not a complete record of every calendar day.

- Earliest saved: `2022-12-21`; latest saved: `2026-10-10` (official draw №26416).
- Schema: `date, official_draw, internal_draw, n1..n20, source, source_url, note`.
- Validation on 2026-10-11: 248 rows, 0 invalid number sets (20 unique integers in 1–70), 0 duplicate dates, 0 chronological order errors.
- Counts and ranges:
  - `super_keno_draws_part_001.csv`: 50, 2022-12-21–2025-11-24
  - `super_keno_draws_part_002.csv`: 50, 2025-11-25–2026-04-29
  - `super_keno_draws_part_003.csv`: 55, 2026-04-30–2026-06-26
  - `super_keno_draws_part_004.csv`: 49, 2026-07-10–2026-08-27
  - `super_keno_draws_part_005.csv`: 44, 2026-08-28–2026-10-10

Run `python src/data_loader.py` to validate; run `python src/data_loader.py --write-master data/super_keno_history_master.csv` to rebuild the chronological master. The previously published SHA-256 `d36ef577a5b3d3a7828b423bbd5474b504fe3a34f9a6fcbe900b14d44e41390c` describes the **old 195-draw migration snapshot**, not today's dataset.

## Coverage and provenance

The priority unresolved contiguous gap is **2026-06-27 through 2026-07-09** (13 dates). Other 2026 gaps are listed in [COLLECTION_LOG.md](COLLECTION_LOG.md). Absence of a row is not proof a draw did not occur. Do not fill gaps by extrapolation.

The initial 195-row dataset was copied from `Mikayilzade/loto-research`; later draws were collected in this repository. Sources and verification notes are recorded per CSV row, with additional check history in the collection log. Independent confirmation is not available for every draw.
