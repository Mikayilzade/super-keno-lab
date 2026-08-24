# Phase 1 — scorer, honest split, baselines and first matrix search

Date: 2026-08-24

Status: **NOT SUCCESS** — foundation validated; first naive matrix strategy is a clear historical overfit.

## What was built

- Configurable current-rules scorer for 10-number tickets.
- Exact ticket/draw validation and payout matrix calculation.
- Portfolio metrics including average P/L, worst P/L, minimum payout/cost ratio, profitable-draw share and concrete worst draw date.
- Deterministic random, hot-frequency, cold-frequency and modular balanced baselines.
- Chronological train/validation/holdout split.
- First complementary/matrix greedy search with **free N**: every selected prefix is evaluated; N is not restricted to 10/100/1000 or any round grid.

## Frozen split for Phase 1

- Training: 120 accepted draws, 2022-12-21 .. 2026-05-22.
- Validation: 40 accepted draws, 2026-05-23 .. 2026-07-19.
- Holdout: 35 accepted draws, 2026-07-20 .. 2026-08-23 — **not opened**.

The historical dataset contains date gaps; these are accepted-row chronological splits, not claims of continuous daily history.

## Baseline validation results

Selected non-round N values were used only to establish scale; later optimization treats N as free.

| N | Typical random min payout/cost | Typical random avg P/L | Best min payout/cost among tested simple baselines | Best simple baseline |
|---:|---:|---:|---:|---|
| 37 | 0.135 | -20.13 | 0.189 | cold frequency |
| 83 | 0.205 | -41.33 | 0.229 | cold frequency |
| 127 | 0.268 | -61.80 | 0.276 | random seed 47 |
| 211 | 0.280 | -104.50 | 0.355 | random seed 11 |
| 347 | 0.352 | -126.68 | 0.363 | random seed 11 |
| 509 | 0.356 | -253.55 | 0.407 | random seed 29 |

None of the simple baselines approaches persistent positive performance on validation.

## First matrix/complementary search

Candidate pool: 12,000 deterministic random unique tickets, seed `20260824`. The greedy search repeatedly targets the weakest training draws and tracks the minimum payout/cost after every prefix. It chose **N = 370** because that prefix had the strongest training minimum ratio.

### Training result (120 draws)

- Tickets: **370**
- Worst payout: **507 AZN**
- Worst P/L: **+137 AZN**
- Minimum payout/cost: **1.3703**
- Profitable draws: **120 / 120 (100%)**
- Worst training witness date: **2026-02-18**

This looks spectacular if judged only on history.

### Validation result (next 40 unseen draws)

- Tickets: **370**
- Worst payout: **88 AZN**
- Worst P/L: **-282 AZN**
- Minimum payout/cost: **0.2378**
- Average P/L: **-142.98 AZN**
- Profitable draws: **2 / 40 (5%)**
- Worst validation witness date: **2026-05-31**

Conclusion: the naive matrix optimizer is exploiting specific historical draw rows rather than finding a persistent edge. This is a useful negative result and a concrete guardrail for the next optimizer.

## Small structural observations (not predictive claims)

On the first 120 training rows:

- Number appearance counts ranged from **16 to 44**; the most frequent included 45 (44 appearances), 27 and 53 (41 each).
- Across 175 pairs of accepted draws that are truly consecutive calendar days in the full 195-row set, mean overlap was **5.766 numbers**, with observed range 1..11.

These are descriptive only. A future signal must work walk-forward and on unseen data before it matters.

## Holdout policy

The final 35 rows were not scored. They remain available for a later frozen candidate. Because Phase 1 validation has now been observed, improvements inspired by this result must be treated as a new experiment rather than retroactively “fixing” Phase 1.

## Next experiment direction

Build a robust complementary optimizer that cannot profit merely by memorizing individual training rows. Candidate mechanisms to test *inside training only* include capped selection utility for rare 8+/9+/10 matches, chronological internal folds, leave-block-out stability, empirical/synthetic perturbation draws, ticket diversity/intersection constraints and walk-forward selection. Freeze the method before the next external evaluation.
