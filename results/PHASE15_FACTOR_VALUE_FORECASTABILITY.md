# Phase 15 — structural factor value × forecastability

Date: 2026-08-25

Status: **NO VALID FORECASTABLE EDGE; ORACLE COMBINATION IS NEAR BREAK-EVEN/SLIGHTLY POSITIVE AND DESERVES DISCRETE-REGIME TESTING.**

## Main decomposition

Same fixed 5,000-ticket universe (seed `424242`), strict 125-target walk-forward timeline, free N 19..400. Oracle tests deliberately use true target factor values only to measure information value. Forecastability tests use only pre-target information.

| factor group | oracle ROI | matched-random mean ROI | oracle lift | best valid predictor | forecast MSE skill vs expanding mean | positive-skill blocks |
|---|---:|---:|---:|---|---:|---:|
| mean/location | **0.86403** | 0.55679 | **+0.30724** | expanding mean | 0.000 | 0/3 |
| quadrants | **0.83994** | 0.58714 | **+0.25279** | expanding mean | 0.000 | 0/3 |
| balance (odd + <=35) | **0.71605** | 0.58233 | **+0.13372** | expanding mean | 0.000 | 0/3 |
| runs | 0.68661 | 0.55544 | +0.13117 | KNN | -0.09068 | 1/3 |
| dispersion/span/gaps | 0.58655 | 0.54092 | +0.04563 | expanding mean | 0.000 | 0/3 |

No group passes the predeclared promotion gate: material oracle value **and** positive forecast skill overall **and** positive skill in at least 2/3 chronological blocks.

## Oracle combinations

The two highest-value single groups were mean/location and quadrants.

- oracle `mean + quadrants`: ROI **0.93737**, P/L **-575 AZN**;
- oracle `mean + quadrants + balance`: ROI **1.06045**, P/L **+625 AZN** on the canonical universe seed.

The three-group result is the first coarse-structure oracle in this project to produce positive aggregate historical P/L. It is still **not playable evidence**, because it uses true future structure and the combination was selected diagnostically after factor decomposition.

## Ticket-universe seed robustness of the top oracle combination

The same exact oracle rule (`mean + quadrants + balance`) was replayed on four independent fixed 5,000-ticket universes:

| universe seed | ROI | P/L | block ROIs |
|---:|---:|---:|---|
| 424242 | **1.06045** | **+625** | 0.8193 / 1.4589 / 1.1448 |
| 10101 | **1.00324** | **+33** | 0.8090 / 1.3928 / 0.8736 |
| 20202 | 0.97899 | -177 | 0.8649 / 1.2443 / 0.9718 |
| 30303 | 0.93284 | -416 | 0.7347 / 0.9061 / 1.2553 |

Across the four universes:
- mean ROI **0.99388**;
- median ROI **0.99112**;
- range **0.93284..1.06045**;
- positive P/L on **2/4** universes.

Interpretation: the oracle effect is not a one-seed artifact. Perfect knowledge of this coarse regime brings the execution layer approximately to break-even across different ticket universes, but positive P/L is not robust enough to call the representation itself a guaranteed edge.

## Accuracy sensitivity diagnostic

On the canonical universe, linearly shrinking the true target regime toward the expanding historical mean gave:

- 0% target information: ROI **0.60972**;
- 25%: **0.58789**;
- 50%: **0.78097**;
- 75%: **0.78246**;
- 100% exact oracle: **1.06045**.

A finer 0.80..0.975 grid remained below break-even (roughly 0.78..0.87); only the exact-oracle endpoint crossed 1.0 in this diagnostic. The curve is not monotonic because ticket structures are discrete and the free-N policy changes with the ranked prefix, so this is a sensitivity warning, not a calibrated probability threshold.

## Decision

Phase 15 does **not** promote any valid forecasting model.

However it changes the next question. The useful information appears to live in a **discrete coarse regime** dominated by:
1. mean/location of the draw;
2. quadrant allocation;
3. odd / low-half balance.

Continuous ridge/rolling/KNN regression cannot forecast those factors better than the expanding mean. The next materially different test should therefore treat the regime as discrete states/classes instead of another continuous vector regression.

## Next direction — Phase 16

- discretize the three-factor regime using only past-derived bin boundaries;
- test ordinal/multiclass / nearest-state transition predictors strictly walk-forward;
- build deterministic portfolio components for regime states from the same fixed universe;
- use predicted class probabilities to average components instead of requiring an exact point forecast;
- keep an exact-regime oracle and a randomized-class baseline as ceilings/controls;
- N remains free and is selected only from past realized curves;
- require superiority to matched-N random in repeated chronological blocks before promotion.

See raw main decomposition in `results/phase15_oracle_factor_decomposition.json` and seed robustness in `results/phase15b_oracle_combo_robustness_compact.json`.
