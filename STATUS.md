# Super Keno Lab — status

Last updated: 2026-08-24

## Phase

`PHASE 11 — verify frozen ensemble lead, then redesign adaptive process`

## Core state

- Dedicated repo: `Mikayilzade/super-keno-lab`; broad `loto-research` remains separate and untouched.
- **195** validated Super Keno draws, 2022-12-21..2026-08-23.
- Portfolio size **N remains a free integer optimization variable**.
- Physical/video investigation is deprioritized; working assumption: lototron unchanged.
- All 195 historical rows are exposed. Future draws after a frozen method are the only truly fresh validation source.

## Exact universal fixed-list result — CLOSED

Every fixed 10-number ticket has exact gross mean payout **0.5985557942634199 AZN per 1 AZN stake** over all possible 20-of-70 draws. Therefore no fixed N-ticket list can guarantee break-even/profit against every mathematically possible draw.

Track A fixed geometry was tested with historical greedy, robust/CVaR greedy, multi-witness cutting-plane, and LP/fractional maximin + rounding. Under fresh adversarial attack all materially converged close to random geometry. Track A remains only a robustness/component layer.

## Phase 9 — LP/fractional maximin summary

Canonical final LP-rounded portfolio: **N=1106**.

- fractional finite-bank floor: **0.957675**;
- rounded real-195 / finite-bank minimum: **0.432188**;
- strong adversarial witnessed return: **0.225136**;
- random same-N controls: **0.221519 / 0.223327**;
- bottom-64 control: **0.219643**.

Verdict: no material fixed-geometry edge over random.

## Phase 10 — strict rolling walk-forward adaptive search

See:
- `experiments/phase10_walkforward_adaptive.py`
- `results/phase10_walkforward_adaptive.json`
- `results/PHASE10_WALKFORWARD_ADAPTIVE.md`

Protocol:
- warmup: first **70** accepted draws;
- scored targets: next **125** draws;
- at target `t`, every portfolio is built only from rows `< t`;
- nine materially different signal/config families: hot, cold, contextual pairs, group mean reversion, and two ensemble strengths;
- 320 signal-conditioned candidate tickets per family/target;
- actual portfolio N chosen freely from every prefix **19..320** using only a trailing 32-draw past calibration window;
- meta-family selection uses only earlier realized target outcomes;
- abstention uses only earlier realized outcomes;
- matched-random controls use the exact selected N/cost.

### Phase 10 overall result — NO GATE

Meta selector without abstention:
- cost **3615 AZN**;
- payout **1648 AZN**;
- net P/L **-1967 AZN**;
- ROI **0.4559**;
- profitable targets **7.2%**.

Meta selector + abstention:
- played **17 / 125** targets;
- cost **639 AZN**;
- payout **279 AZN**;
- net P/L **-360 AZN**;
- ROI **0.4366**;
- matched-random with the same play/abstain dates and cost: ROI **0.6839**, P/L **-202 AZN**.

Chronological block gate:
- 2026-02-22..2026-05-12: negative;
- 2026-05-13..2026-06-21: negative;
- 2026-07-10..2026-08-23: negative;
- positive blocks: **0 / 3**.

Verdict: recent-performance family switching and the first confidence/abstention gate are rejected. They do not extract a profitable regime and are worse than same-cost random.

## Weak lead retained from Phase 10

The best frozen individual family was **`ensemble_b06`** (cold-frequency + contextual-pair + group-mean-reversion blend with moderate signal strength):

- targets: **125**;
- cost **2892 AZN**;
- payout **2067 AZN**;
- net P/L **-825 AZN**;
- ROI **0.71473**;
- profitable targets **12.8%**;
- max drawdown **956 AZN**;
- max losing streak **19**;
- selected N range **19..45**, median **20**.

This is still substantially negative and is **not a strategy success**. However, its ROI is materially above the Phase-10 generic matched-random no-abstention control (0.5787), so it is retained as a **weak signal lead pending same-N multi-seed verification**.

`experiments/phase10b_ensemble_verify.py` has been added to freeze this exact family and compare it against many same-N random replicas, chronological blocks, and payout-tier concentration. Until that verification produces a recorded result, do not promote the ensemble beyond weak-lead status.

## What Phase 10 ruled out

- choosing whichever signal family recently had the best realized ROI;
- the first abstention threshold based on recent realized ratios;
- raw hot/cold or pair families as standalone adaptive profit strategies;
- treating a lower number of plays as automatically safer/profitable;
- using historical calibration fit as a substitute for repeated forward improvement.

## NEXT ACTION — Phase 11

1. Complete/fix the frozen `ensemble_b06` same-N multi-seed verification; determine whether its ~0.715 ROI is a reproducible separation from random or just sample luck / payout concentration.
2. If the separation does **not** survive, close the current signal blend and move to a qualitatively different adaptive class rather than retuning beta/window constants.
3. If it **does** survive, decompose the ensemble with nested past-only ablations and learn signal weights only from earlier forward blocks; keep parameters frozen on later blocks.
4. Replace recent-winner meta-selection with stable model averaging / shrinkage rather than hard switching.
5. Design abstention from predicted *edge uncertainty* rather than realized recent ROI; zero-play remains valid when uncertainty is high.
6. Let N remain continuous/free and tie exposure to calibrated edge strength, but compare every selected N against same-cost random distributions.
7. Evaluate cumulative P/L, ROI, drawdown, losing streak, chronological block consistency, and payout concentration (especially 8+ hit dependence).
8. Any candidate process that survives historical walk-forward becomes a frozen paper strategy for future genuinely unseen draws; do not call historical survival proof of future profit.

No autonomous recurring task is enabled for this repository.
