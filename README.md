# Super Keno Lab

Dedicated research and experiment repository for Azerbaijan Super Keno.

## Purpose

Search for reproducible ticket-generation and portfolio-selection methods that improve persistent net performance across unseen draws, with special focus on empirical, structural, operational and implementation effects rather than only textbook probability calculations.

The practical target is a portfolio of N tickets whose worst unseen-draw result can be pushed toward and, if evidence permits, above break-even. Historical profitability alone is not treated as a guarantee.

## Separation from loto-research

This repository is an **independent copy/laboratory**. `Mikayilzade/loto-research` remains the broad all-lotteries research project and must not be modified as part of Super Keno lab work.

## Current data

- **195 validated draws** copied into `data/`.
- Earliest recovered draw: `2022-12-21`.
- Latest recovered draw: `2026-08-23`.
- Main recent gap: `2026-06-22..2026-07-09`.
- Every accepted row has exactly 20 unique numbers from 1 to 70.

The dataset is split into four chronological shards. Run:

```bash
python src/data_loader.py
```

to validate them, or:

```bash
python src/data_loader.py --write-master data/super_keno_history_master.csv
```

to rebuild one chronological master CSV.

## Repository map

- `PROJECT_RULES.md` — isolation, evidence and anti-overfitting rules.
- `STATUS.md` — current checkpoint and exact next action.
- `EXPERIMENT_PROTOCOL.md` — train/validation/holdout and portfolio metrics.
- `data/` — copied historical draws and provenance notes.
- `src/` — loaders, scorers, portfolio search and analysis code.
- `experiments/` — reproducible strategy runs and results (to be added).

## Research direction

The first laboratory cycle will establish current rules/payouts, a configurable scorer, random/simple baselines, chronological holdouts and then matrix/complementary portfolio searches with concrete worst-draw witnesses.
