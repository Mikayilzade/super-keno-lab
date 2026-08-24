# Super Keno Lab — status

Last updated: 2026-08-25

## Phase

`PHASE 16 — discrete coarse-regime classification + probabilistic component selection`

## Core state

- Dedicated repo: `Mikayilzade/super-keno-lab`; broad `loto-research` remains separate and untouched.
- **195** validated Super Keno draws, 2022-12-21..2026-08-23.
- Portfolio size **N remains a free integer optimization variable**; round-number N values are controls only.
- Working assumption: lototron unchanged; physical/video branch is deprioritized.
- All 195 historical rows are exposed. Future draws after a frozen method are the only truly fresh validation source.
- Mandatory evidence rule: if any strategy construction step is stochastic, report its **strategy/universe-seed distribution**, not one favorable seed.

## Exact universal fixed-list result — CLOSED

Every fixed 10-number ticket has exact gross mean payout **0.5985557942634199 AZN per 1 AZN stake** across all mathematically possible 20-of-70 draws. Therefore no fixed list at any N can guarantee break-even/profit against every possible draw.

Fixed-geometry methods (historical maximin, adversarial cutting-plane, broad-tail/CVaR greedy, LP + rounding) all converge near random geometry under fresh adversarial attack. Track A remains only a robustness/component layer.

## Closed / rejected primary routes

1. Fixed-list geometry alone.
2. Hot/cold + contextual pairs + group mean reversion with stochastic ticket generation; attractive seed-7 result collapsed across strategy seeds.
3. Supervised per-number probability ranking with deterministic 5,000-ticket universe.
4. Direct ticket-payoff regression/ranking.
5. Generic continuous multivariate structure prediction (ridge / rolling / KNN) as currently formulated.

See prior phase reports in `results/` for exact seeds, controls and failures.

## Phase 13 — direct ticket-payoff — NO EDGE

See `results/PHASE13_DIRECT_TICKET_PAYOFF.md`.

125 strict walk-forward targets, fixed 5,000-ticket universe seed `424242`, N free 19..400, 20 matched-N random replicas.

- ridge cap15 ROI **0.48423** vs random **0.56454**;
- ridge cap5 **0.48945** vs **0.53920**;
- ridge profit-ticket **0.48882** vs **0.53403**;
- empirical cap15 **0.51876** vs **0.54457**.

No model has a positive-P/L chronological block set; learned ridge rankings are consistently worse than random.

## Phase 14 — full draw-structure pilot

See `results/PHASE14_DRAW_STRUCTURE_PILOT.md`.

Valid pre-target models:
- ridge structure ROI **0.49198**;
- rolling20 structure **0.48420**;
- KNN structure **0.54767**;
- matched-random around **0.55–0.56**.

No valid model promoted.

### Full-structure oracle ceiling

Using true future coarse structure only as a diagnostic, not actual numbers:
- ROI **0.95913**;
- P/L **-417 AZN**;
- block ROIs **0.91850 / 1.00157 / 0.96754**.

This showed that draw structure contains meaningful payoff information even though current forecasting is inadequate.

## Phase 15 — factor value × forecastability

See:
- `experiments/phase15_oracle_factor_decomposition.py`
- `results/phase15_oracle_factor_decomposition.json`
- `results/PHASE15_FACTOR_VALUE_FORECASTABILITY.md`
- `results/phase15b_oracle_combo_robustness_compact.json`

Five predeclared structural groups were separated into economic oracle value and strict walk-forward forecastability.

| factor | oracle ROI | random mean | oracle lift | best valid forecast skill vs expanding mean | positive skill blocks |
|---|---:|---:|---:|---:|---:|
| mean/location | **0.86403** | 0.55679 | **+0.30724** | 0.000 | 0/3 |
| quadrants | **0.83994** | 0.58714 | **+0.25279** | 0.000 | 0/3 |
| balance (odd + <=35) | **0.71605** | 0.58233 | **+0.13372** | 0.000 | 0/3 |
| runs | 0.68661 | 0.55544 | +0.13117 | -0.09068 | 1/3 |
| dispersion/span/gaps | 0.58655 | 0.54092 | +0.04563 | 0.000 | 0/3 |

No individual factor passes the predeclared `value × forecastability` gate.

### Important oracle combination

Diagnostic combination of the three high-value coarse groups — **mean/location + quadrants + balance** — produced on canonical universe seed `424242`:
- ROI **1.06045**;
- cost **10,339 AZN**;
- payout **10,964 AZN**;
- P/L **+625 AZN**;
- N range **19..357**, median **23**.

This is the first coarse-structure oracle in the project with positive aggregate historical P/L. It is **not a valid strategy**, because it uses true future regime information and the combination was selected diagnostically.

### Universe-seed robustness of the same oracle combination

Four independent 5,000-ticket universes:
- seed 424242: ROI **1.06045**, P/L +625;
- seed 10101: **1.00324**, +33;
- seed 20202: **0.97899**, -177;
- seed 30303: **0.93284**, -416.

Across universes:
- mean ROI **0.99388**;
- median ROI **0.99112**;
- positive P/L **2/4** seeds.

Interpretation: perfect knowledge of this coarse regime brings the execution layer approximately to break-even across different ticket universes. The result is not merely a favorable universe-seed artifact, but positive P/L is not robust enough to be called an edge by itself.

### Accuracy-sensitivity warning

On the canonical universe, shrinking the true regime toward its expanding historical mean gave approximate ROIs:
- 0% true-regime information: **0.60972**;
- 25%: **0.58789**;
- 50%: **0.78097**;
- 75%: **0.78246**;
- 100% exact oracle: **1.06045**.

A finer 0.80..0.975 interpolation remained below break-even (~0.78..0.87). This curve is not monotonic because regime states and ticket structures are discrete and N changes adaptively, but it shows that **small continuous prediction improvements are unlikely to be enough**. The next test must predict discrete useful states/classes, not tune continuous regression.

## Strategic interpretation

The valuable information is concentrated in three coarse dimensions:
1. draw mean/location;
2. allocation across the four number quadrants;
3. odd/even and low/high balance.

Continuous pre-target regression has essentially zero stable forecasting skill for these factors. Therefore the structure branch is not yet closed, but the next attempt must be materially different: **discrete regime classification / probabilistic state selection**.

## NEXT ACTION — Phase 16

1. Define discrete regime states for `mean/location + quadrants + balance` using only past-derived bin boundaries / counts; do not use future global quantiles for valid predictions.
2. Measure regime-state entropy, class frequencies and exact/near-state recurrence to avoid impossible ultra-sparse classes.
3. Test strict walk-forward predictors materially different from continuous regression:
   - Markov / transition frequencies from recent regime states;
   - shrinkage class priors conditioned on previous one/two states;
   - nearest-context class probability distribution;
   - simple ordinal/multiclass linear scoring if class counts are sufficient.
4. Do not require one exact point state: output a **probability distribution over states**.
5. Prebuild deterministic ticket-component rankings for regime states from a fixed universe. Combine component scores by predicted class probabilities; no fresh ticket pool per target.
6. Keep exact-regime oracle and class-prior/randomized-state baselines as ceilings/controls only.
7. N remains free and is selected only from earlier realized capped-payout curves.
8. Compare with many matched-N random controls and report chronological blocks.
9. Promotion requires positive aggregate P/L, beating random overall, and repeated block-level superiority; a single lucky state/seed is insufficient.
10. If discrete classification also has no predictive skill, close the structure-history branch and move to a genuinely new information source rather than feature/window tuning.

No autonomous recurring task is enabled for this repository.
