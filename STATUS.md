# Super Keno Lab — status

Last updated: 2026-08-25

## Phase

`PHASE 15 — oracle structural-factor decomposition + forecastability/value intersection`

## Core state

- Dedicated repo: `Mikayilzade/super-keno-lab`; broad `loto-research` remains separate and untouched.
- **195** validated Super Keno draws, 2022-12-21..2026-08-23.
- Portfolio size **N remains a free integer optimization variable**.
- Working assumption: lototron unchanged; physical/video branch remains deprioritized.
- All 195 historical rows are exposed. Future draws after a frozen method are the only truly fresh validation source.
- Mandatory evidence rule: if strategy construction contains randomness, report the **strategy-seed distribution**, not one favorable seed.
- Same deterministic ticket universe seed `424242` is intentionally reused across Phases 12–14 to avoid favorable-universe selection.

## Exact universal fixed-list result — CLOSED

Every fixed 10-number ticket has exact gross mean payout **0.5985557942634199 AZN per 1 AZN stake** over all mathematically possible 20-of-70 draws.

Therefore no fixed list of distinct tickets at any N can guarantee break-even/profit against every possible draw. Fixed-geometry work remains only a robustness/component layer.

Track A tested historical maximin, adversarial cutting-plane, broad-tail/CVaR greedy and fractional LP + rounding. Under fresh adversarial attack all converge close to random geometry.

## Phase 10/11 — adaptive heuristic signals — CLOSED AS PRIMARY ROUTE

Strict rolling walk-forward tested hot/cold, contextual pairs, group mean reversion, ensembles, recent-winner meta-selection and abstention.

The attractive `ensemble_b06` run (ROI 0.7147) did not survive strategy candidate-generation seed variation:
- ensemble seed ROIs: 0.7147 / 0.5444 / 0.5388 / 0.6591 / 0.5820;
- mean ≈ 0.608, median ≈ 0.582;
- pair-only mean ≈ 0.587, median ≈ 0.593.

Verdict: current hot/cold/pair/reversion family is closed as a primary edge source. Do not retune beta/windows to recover favorable seed 7.

## Phase 12 — supervised per-number model — NO EDGE

See `results/PHASE12_SUPERVISED_FIXED_POOL_PILOT.md`.

Fixed universe 5,000 tickets, deterministic execution, supervised ridge probability model for each of 70 numbers, strict walk-forward, N free 19..300.

- strategy ROI **0.53423**, P/L **-4300 AZN**;
- matched-random ROI **0.56369**;
- all three chronological blocks negative in absolute P/L.

Verdict: straightforward per-number probability forecasting is not a usable route.

## Phase 13 — direct ticket-payoff ranking — NO EDGE

See:
- `experiments/phase13_direct_ticket_payoff.py`
- `results/PHASE13_DIRECT_TICKET_PAYOFF.md`
- `results/phase13_direct_ticket_payoff_checkpoint.json`

Material change: train/rank on **ticket payoff itself**, not number appearance.

Setup:
- same fixed 5,000-ticket universe, seed `424242`;
- 125 strict walk-forward targets;
- N free **19..400**;
- N chosen only from earlier capped-payoff prefix curves;
- 20 matched-N random replicas per method;
- four predeclared direct-payoff targets: cap15 ridge, cap5 ridge, profit-ticket ridge, expanding empirical cap15.

Results:

| model | ROI | P/L | random mean ROI | blocks > random |
|---|---:|---:|---:|---:|
| ridge_cap15 | 0.48423 | -16,320 | 0.56454 | 0/3 |
| ridge_cap5 | 0.48945 | -13,380 | 0.53920 | 0/3 |
| ridge_profit_ticket | 0.48882 | -13,209 | 0.53403 | 0/3 |
| empirical_cap15 | 0.51876 | -11,312 | 0.54457 | 2/3 |

All four have **0/3 positive-P/L blocks**. The three learned ridge rankings are consistently worse than random. Empirical cap15 beats random in the first two blocks but fails in the latest block and remains strongly negative overall.

Rare 8+ payouts explain only ~7–11% of total payout, so the failure is not simply one missing jackpot.

Verdict: **direct ticket-payoff ranking is closed as a primary route in this formulation.** Do not tune ridge constants/payout caps/nearby feature windows next.

## Phase 14 — draw-level structure/regime pilot

See:
- `experiments/phase14_draw_structure.py`
- `results/PHASE14_DRAW_STRUCTURE_PILOT.md`
- `results/phase14_draw_structure_checkpoint.json`

Instead of predicting numbers/ticket payoff, Phase 14 predicts the coarse structure of the next 20-number draw:
- four range/quadrant proportions;
- parity;
- <=35 share;
- mean number;
- dispersion;
- adjacent-run density;
- span;
- gap dispersion.

The same fixed 5,000-ticket universe is ranked by closeness to predicted structure. N remains free 19..400.

### Valid pre-target predictors

| predictor | ROI | P/L | random mean ROI | blocks > random |
|---|---:|---:|---:|---:|
| ridge_structure | 0.49198 | -13,709 | 0.55894 | 0/3 |
| rolling20_structure | 0.48420 | -9,678 | 0.55325 | 0/3 |
| knn_structure | 0.54767 | -11,576 | 0.55713 | 1/3 |

No valid predictor is promoted. KNN has one attractive early block (ROI 0.7789) but fails to reproduce it later.

### Oracle structure diagnostic — IMPORTANT

`oracle_structure` is **not a valid strategy**: it is deliberately given the true coarse structure of the target draw, but still not the actual numbers. It measures the information ceiling of this representation/execution layer.

Across 125 targets:
- cost **10,202 AZN**;
- payout **9,785 AZN**;
- P/L **-417 AZN**;
- ROI **0.95913**;
- capped15 ROI **0.77387**;
- profitable targets **28%**;
- N range 19..232, median 77.

Chronological oracle blocks:
- ROI **0.91850**, P/L -323;
- ROI **1.00157**, P/L **+5**;
- ROI **0.96754**, P/L -99.

This is qualitatively stronger than previous representations. Coarse structure alone, if known perfectly, pushes the same fixed-universe execution layer close to break-even and produces one slightly positive block.

Interpretation: **the structure representation contains material value; current forecasting of that structure is the bottleneck.**

## Strategic decision

Rejected primary mechanisms so far:
1. fixed-list geometry alone;
2. heuristic rolling number signals with stochastic ticket generation;
3. supervised per-number probability ranking;
4. direct ticket-payoff regression/ranking;
5. generic multivariate structure prediction as currently implemented.

However Phase 14 oracle testing identifies a new useful question: not “can we forecast the full structure vector?” but **which structural dimensions actually create the payoff lift, and are any of those dimensions forecastable enough?**

## NEXT ACTION — Phase 15

1. Decompose the oracle structure advantage into predeclared factor groups:
   - quadrants/range balance;
   - parity / <=35 balance;
   - mean/sum location;
   - dispersion/span/gaps;
   - adjacent-run structure;
   - combinations of the strongest groups.
2. For each factor/group, run an oracle ticket-ranking diagnostic with the same fixed universe and free-N historical policy. Record ROI lift over matched random.
3. Separately measure strict walk-forward forecastability of that factor using simple stable predictors (rolling/shrinkage, ordinal/classification, context-nearest-neighbor) without using target payout.
4. Build a **value × forecastability table**. Prioritize only factors that are both economically useful under oracle information and predictably better than naive baselines.
5. Convert the promising factor(s) into discrete regimes and prebuild deterministic portfolio components for each regime; do not generate a fresh random ticket pool per target.
6. Condition among those components before each target using only past information; N remains free.
7. Compare every conditioned choice with matched-N random distributions across chronological blocks.
8. Keep an oracle counterpart for each regime as a ceiling diagnostic, never as evidence of a playable strategy.
9. If no individual/grouped structural factor has both material oracle value and stable forecastability, close the structure branch and move to a new information source rather than feature tuning.
10. Save all failures, exact seeds and checkpoints in the repo.

No autonomous recurring task is enabled for this repository.
