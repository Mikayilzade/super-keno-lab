# Super Keno historical dataset

Current copied dataset: **195 validated draws**.

- Earliest recovered draw: `2022-12-21`
- Latest recovered draw: `2026-08-23`
- Schema: `date, official_draw, internal_draw, n1..n20, source, source_url, note`
- Structural validation errors at copy time: `0`
- Duplicate dates at copy time: `0`
- Duplicate 20-number combinations at copy time: `0`

## Files

The independent working copy is stored in four chronological shards:

- `super_keno_draws_part_001.csv` — 50 draws, 2022-12-21 through 2025-11-24
- `super_keno_draws_part_002.csv` — 50 draws, 2025-11-25 through 2026-04-29
- `super_keno_draws_part_003.csv` — 50 draws, 2026-04-30 through 2026-06-21
- `super_keno_draws_part_004.csv` — 45 draws, 2026-07-10 through 2026-08-23

Run `python src/data_loader.py` to validate all shards. Run `python src/data_loader.py --write-master data/super_keno_history_master.csv` to reconstruct one chronological master CSV.

The reconstructed master at migration time had SHA-256:

`d36ef577a5b3d3a7828b423bbd5474b504fe3a34f9a6fcbe900b14d44e41390c`

## Important gap

The copied history is **not continuous**. The main recent gap is `2026-06-22` through `2026-07-09`, and older historical gaps also exist. Experiments must not treat row adjacency as proof that calendar days are consecutive.

## Provenance

The data was copied from the Super Keno work accumulated in `Mikayilzade/loto-research` and the recovered 150-draw baseline. The source repository remains untouched and independent.
