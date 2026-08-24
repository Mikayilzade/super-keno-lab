# Project rules

This repository is the dedicated laboratory for Azerbaijan Super Keno strategy research.

## Isolation

- `Mikayilzade/loto-research` is a separate broad lottery-research project.
- Do not delete, move, rewrite, or repurpose files in `loto-research` from this project.
- Data copied here is an independent working copy.
- All Super Keno strategy experiments, code, checkpoints and conclusions belong here.

## Objective

Search for a reproducible method where a portfolio of N Super Keno tickets has the strongest possible persistent net result, with special attention to methods that exploit empirical, structural, operational or implementation effects rather than relying only on textbook probability calculations.

The target is a portfolio/process whose net result remains positive across unseen draws. A claim of guaranteed profit requires stronger proof than historical backtesting.

## Evidence rules

- Never use future draws when building a rule that is claimed to predict an earlier draw.
- Separate training, validation and final holdout data chronologically.
- Report both average result and worst result; optimize the worst-case floor as a primary metric.
- Compare every strategy against random-ticket and simple-frequency baselines.
- Record failed approaches as well as successful ones to avoid repeating work.
- Do not label a historical fit as a guaranteed edge.
- Current official rules, ticket price and payout table must be web-verified before monetary backtests.

## Data integrity

Every accepted draw must contain exactly 20 unique integers in 1..70. Deduplicate by date, official draw number when present, and sorted 20-number combination. Conflicts are flagged, never guessed.
