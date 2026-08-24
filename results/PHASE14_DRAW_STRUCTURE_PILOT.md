# Phase 14 — draw-level structure/regime prediction pilot

Date: 2026-08-25

Status: **VALID PREDICTORS NO EDGE; ORACLE STRUCTURE IS NEAR BREAK-EVEN AND JUSTIFIES DECOMPOSITION.**

## Setup

- Same fixed universe as Phases 12–13: **5,000 tickets**, seed `424242`.
- Strict walk-forward: 125 targets after warmup.
- N free: **19..400**, selected only from prior capped15 prefix curves.
- Structure vector of each draw/ticket includes:
  - four number-range/quadrant proportions;
  - odd share;
  - <=35 share;
  - normalized mean number;
  - dispersion;
  - adjacent-run density;
  - span;
  - gap dispersion.
- Three valid pre-target predictors:
  - multivariate ridge on lagged/rolling structure context;
  - rolling-20 structure mean;
  - k-nearest historical structure context.
- Each valid method compared against **20 matched-N random replicas** from the same fixed ticket universe.
- Separate `oracle_structure` diagnostic uses the true target structure only to measure the ceiling of this representation. It is **not** a valid strategy.

## Valid walk-forward results

| model | ROI | P/L (AZN) | random mean ROI | blocks > random | positive blocks |
|---|---:|---:|---:|---:|---:|
| ridge_structure | **0.49198** | **-13,709** | 0.55894 | 0/3 | 0/3 |
| rolling20_structure | **0.48420** | **-9,678** | 0.55325 | 0/3 | 0/3 |
| knn_structure | **0.54767** | **-11,576** | 0.55713 | 1/3 | 0/3 |

### Ridge structure
- N range: 19..396, median 299.
- Mean structure-prediction RMSE: 0.1153.
- All 20 random replicas beat the strategy overall.
- block ROIs: 0.5086 / 0.4774 / 0.4742.

### Rolling-20 structure
- N range: 19..400, median 52.
- Mean structure-prediction RMSE: 0.1026.
- All 20 random replicas beat the strategy overall.
- block ROIs: 0.5135 / 0.5156 / 0.4554.

### KNN structure
- N range: 19..392, median 187.
- Mean structure-prediction RMSE: 0.1062.
- ROI 0.5477 vs random mean 0.5571.
- block ROIs: **0.7789** / 0.4874 / 0.4629.
- First block beat random strongly; later blocks did not reproduce it.

## Oracle diagnostic — important boundary

`oracle_structure` receives only the true coarse structure of the target draw, **not the actual 20 numbers**.

Across 125 targets:
- cost: **10,202 AZN**
- payout: **9,785 AZN**
- P/L: **-417 AZN**
- ROI: **0.95913**
- capped15 ROI: **0.77387**
- profitable targets: **28%**
- N range: 19..232, median 77.

Chronological oracle blocks:
- block 1: ROI **0.91850**, P/L -323 AZN
- block 2: ROI **1.00157**, P/L **+5 AZN**
- block 3: ROI **0.96754**, P/L -99 AZN

## Interpretation

The valid structure predictors are not accurate enough and do not beat random persistently. However, the oracle result is qualitatively different from the earlier failed representations: knowing only coarse draw structure pushes the same execution layer from roughly fair/random territory to **~95.9% gross return**, with one chronological block just above break-even.

That does **not** prove a usable edge. It says the representation contains materially useful information if it can be forecast accurately enough.

## Decision

No valid Phase-14 model is promoted.

Do **not** tune the current ridge/KNN hyperparameters as the next action. Instead decompose the oracle advantage by structural dimension and regime:

1. run single-factor and grouped oracle tests (quadrants, parity, mean/sum, dispersion, runs/span, overlap-related structure);
2. identify which factors create most of the ~0.96 oracle ROI;
3. measure how accurately each factor can actually be predicted walk-forward;
4. prioritize only factors where both oracle payoff lift and forecastability coexist;
5. condition among deterministic portfolio components rather than scoring every ticket with all structure dimensions at once.
