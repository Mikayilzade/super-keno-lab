# Super Keno Lab — status

Last updated: 2026-08-24

## Phase

`PHASE 2 — robust portfolio search after baseline/overfit calibration`

## Completed

- Dedicated repository confirmed: `Mikayilzade/super-keno-lab`; broad `loto-research` remains separate and untouched.
- Copied and validated **195** Azerbaijan Super Keno draws in four chronological CSV shards.
- Dataset: earliest **2022-12-21**, latest **2026-08-23**; structural errors 0, duplicate dates 0, duplicate 20-number combinations 0.
- Current official rules, payout table, ticket price, multipliers, tax wording and 125-ticket-per-game-room FAQ constraint were web-verified and snapshotted in `rules/SUPER_KENO_RULES_2026-08-24.md`.
- Added configurable scorer and exact portfolio evaluator: `src/rules.py`, `src/evaluator.py`.
- Added deterministic random/hot/cold/modular baselines: `src/baselines.py`.
- Scorer regression suite: **5/5 tests passed**.
- Explicitly changed project protocol so portfolio size **N is a free integer optimization variable**, not a round-number grid.

## Phase 1 frozen split

- Train: first **120** accepted draws, 2022-12-21 .. 2026-05-22.
- Validation: next **40**, 2026-05-23 .. 2026-07-19.
- Holdout: final **35**, 2026-07-20 .. 2026-08-23 — **still sealed / not scored**.

## Phase 1 result

See `results/PHASE1_BASELINES.md` and `experiments/phase1_baselines.py`.

Simple validation baselines were negative at all tested non-round control sizes (37, 83, 127, 211, 347, 509).

The first naive complementary/matrix optimizer used 12,000 deterministic candidate tickets and treated N as free across prefixes. It selected **N=370**.

Training (120 draws):
- worst payout = **507 AZN** on 370 AZN cost;
- worst P/L = **+137 AZN**;
- minimum payout/cost = **1.3703**;
- profitable draws = **120/120**.

Validation (next unseen 40):
- worst payout = **88 AZN**;
- worst P/L = **-282 AZN**;
- minimum payout/cost = **0.2378**;
- average P/L = **-142.98 AZN**;
- profitable draws = **2/40 (5%)**.

Verdict: **NOT SUCCESS**. The naive matrix method memorizes historical draw rows and is rejected as an edge. This negative result is now a required anti-overfitting regression benchmark.

## Data notes

- Main recent missing block in the archive remains 2026-06-22..2026-07-09; older gaps also exist.
- On the first 120 training rows, number frequencies ranged 16..44 appearances. Descriptive only; no predictive claim.
- Across 175 truly consecutive-calendar-day pairs in the full copied dataset, mean draw overlap was 5.766 numbers (range 1..11). Descriptive only.

## NEXT ACTION

Run **Phase 2 robust complementary search** without opening the 35-row holdout:

1. Work only inside the 120-row training block for method design.
2. Add chronological internal folds / leave-block-out stability so a ticket cannot be selected merely for one memorized draw.
3. Test selection utilities that cap or de-emphasize rare 8+/9+/10 training payouts, plus ticket intersection/diversity constraints.
4. Add empirical/synthetic perturbation draws and walk-forward training checks.
5. Treat N as free and record the best worst-case prefix at every meaningful N.
6. Freeze one Phase 2 method before any external evaluation; do not retroactively repair Phase 1.
7. Keep the final 35-draw holdout sealed until a genuinely stronger candidate is frozen.

No autonomous recurring task is enabled for this repository.
