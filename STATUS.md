# Super Keno Lab — status

Last updated: 2026-08-24

## Phase

`PHASE 13 — direct ticket-payoff / ranking models with deterministic execution`

## Core state

- Dedicated repo: `Mikayilzade/super-keno-lab`; broad `loto-research` remains separate and untouched.
- **195** validated Super Keno draws, 2022-12-21..2026-08-23.
- Portfolio size **N remains a free integer optimization variable**.
- Physical/video investigation is deprioritized; working assumption: lototron unchanged.
- All 195 historical rows are exposed. Future draws after a frozen method are the only truly fresh validation source.
- New mandatory rule: when strategy construction itself contains randomness, report the **strategy-seed distribution**, not only one favorable generation seed.

## Exact universal fixed-list result — CLOSED

Every fixed 10-number ticket has exact gross mean payout **0.5985557942634199 AZN per 1 AZN stake** across all possible 20-of-70 draws. Therefore no fixed N-ticket list can guarantee break-even/profit against every mathematically possible draw.

Track A fixed geometry was tested with historical greedy, robust/CVaR greedy, multi-witness cutting-plane, and LP/fractional maximin + rounding. Under fresh adversarial attack all materially converged close to random geometry. Track A remains only a robustness/component layer.

## Phase 10 — strict adaptive rolling walk-forward

See:
- `experiments/phase10_walkforward_adaptive.py`
- `results/phase10_walkforward_adaptive.json`
- `results/PHASE10_WALKFORWARD_ADAPTIVE.md`

125 strict one-step targets after a 70-draw warmup; every target uses only rows before it. N free over 19..320. Tested hot/cold, contextual pairs, group mean reversion, ensembles, recent-performance meta-selection and abstention.

Main result:
- meta without abstention ROI **0.4559**, P/L **-1967 AZN**;
- meta + abstention ROI **0.4366**, P/L **-360 AZN** on 17/125 plays;
- same play/abstain matched-random ROI **0.6839**;
- positive chronological blocks **0/3**.

Verdict: hard recent-winner switching and first abstention gate rejected.

## Phase 10B — frozen ensemble lead verification

See:
- `results/PHASE10B_ENSEMBLE_VERIFY.md`
- `results/phase10b_ensemble_verify_checkpoint.json`
- `experiments/phase10b_ensemble_verify.py`
- `experiments/phase10b_runner.py`

The original frozen `ensemble_b06` run:
- ROI **0.714730**;
- P/L **-825 AZN**;
- same-N random mean across 40 replicas **0.559509**;
- only **3/40** random replicas >= strategy;
- empirical one-sided p ≈ **0.09756**;
- above same-N random mean in **3/3** chronological blocks;
- positive-P/L blocks **0/3**.

This initially qualified only as a weak lead.

## Phase 11 — decomposition + strategy-seed robustness

See `results/PHASE11_SIGNAL_DECOMPOSITION.md`.

### Frozen-weight ablations

Original cold+pair+reversion blend: ROI **0.71473**.

Remove one component:
- cold+pair: **0.56242**;
- cold+reversion: **0.58480**;
- pair+reversion: **0.51649**.

Standalone in the original candidate-generation seed:
- pair-only: **0.65569**;
- cold-only: **0.58231**;
- reversion-only: **0.50147**.

Pair was the strongest single component, but that was not the decisive test.

### Strategy candidate-generation seed test — decisive

Same frozen `ensemble_b06`, only candidate-ticket generation seed changed:
- offset 7: **0.71473**;
- 11: **0.5444**;
- 19: **0.5388**;
- 31: **0.6591**;
- 43: **0.58203**.

Across five seeds:
- mean ROI ≈ **0.608**;
- median ≈ **0.582**;
- range ≈ **0.539..0.715**.

Pair-only also collapses under seed variation:
- 0.65569 / 0.64140 / 0.54539 / 0.50508;
- mean ≈ **0.5869**;
- median ≈ **0.5934**.

Verdict: the attractive Phase-10 result was materially helped by a favorable stochastic candidate-ticket realization. The current hot/cold/pair/reversion family is **closed as a primary edge route**. Do not retune beta/window constants to recover seed 7.

## Phase 12 — supervised per-number probability model + fixed ticket pool

See:
- `experiments/phase12_supervised_fixed_pool.py`
- `results/PHASE12_SUPERVISED_FIXED_POOL_PILOT.md`
- `results/phase12_supervised_fixed_pool_checkpoint.json`

Material change from Phase 10/11:
- one fixed deterministic universe of **5,000** tickets, seed `424242`;
- no per-target candidate-ticket sampling;
- ridge walk-forward model predicts each of 70 number probabilities from rolling frequency, gap, previous hit, contextual pair and group-reversion features;
- ticket ranks are deterministic sums of predicted probabilities;
- N free over **19..300**, chosen from trailing realized prefix curves only.

Result over 125 targets:
- strategy ROI **0.53423**, P/L **-4300 AZN**;
- matched-random ROI **0.56369**, P/L **-4028 AZN**;
- only middle chronological block marginally beats random;
- all blocks strongly negative in absolute P/L.

Verdict: simple supervised per-number probability prediction does **not** extract a usable edge. Do not spend the next phase tuning ridge constants or nearby feature windows.

## Strategic interpretation

The project has now rejected three broad mechanisms as primary routes:
1. fixed-list geometry alone;
2. heuristic rolling number signals with stochastic ticket sampling;
3. straightforward supervised per-number probability ranking with deterministic execution.

The next method must target the actual object we care about more directly: **ticket payoff / portfolio payoff**, not merely whether each number appears.

## NEXT ACTION — Phase 13

Build a deterministic, direct **ticket-payoff ranking** walk-forward model:

1. Use one fixed large ticket universe so strategy construction has no hidden favorable seed per target.
2. For each historical target, create ticket-level features available before that draw: sums/dispersion of rolling number scores, contextual pair interactions inside the ticket, overlap with previous draws, gap structure, range/parity/run structure, and portfolio-diversity features.
3. Train on historical **ticket payout / capped utility / ranking labels**, not on individual-number appearance. Rare 8/9/10-hit payouts must be handled with robust/capped objectives so one event cannot dominate training.
4. Refit strictly walk-forward. At target `t`, all training labels end at `t-1`.
5. Rank the fixed ticket universe deterministically and evaluate every prefix N; N remains free.
6. Select N only from prior realized walk-forward curves; never from the target being scored.
7. Compare against many matched-N random controls and, if any stochastic model component remains, across model/strategy seeds as well.
8. Report both real payout and capped/low-tier utility to detect dependence on rare 8+ hits.
9. Require repeated improvement in chronological blocks before any promotion.
10. If direct ticket-payoff modeling also converges to random/fair return, pivot next to predicting **draw-level regimes/structures** and condition among prebuilt robust portfolio components rather than continuing number-level feature engineering.

No autonomous recurring task is enabled for this repository.
