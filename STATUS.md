# Super Keno Lab — status

Last updated: 2026-08-24

## Phase

`PHASE 3 — walk-forward empirical signal discovery`

## Completed foundation

- Dedicated repository: `Mikayilzade/super-keno-lab`; broad `loto-research` remains separate and untouched.
- Copied and validated **195** Azerbaijan Super Keno draws in four chronological CSV shards.
- Dataset: earliest **2022-12-21**, latest **2026-08-23**; structural errors 0, duplicate dates 0, duplicate 20-number combinations 0.
- Current official rules/payouts/ticket price and operational notes are snapshotted in `rules/SUPER_KENO_RULES_2026-08-24.md`.
- Configurable scorer/evaluator and deterministic baselines are implemented.
- Portfolio size **N is a free integer optimization variable**, not a round-number grid.

## Frozen evaluation split

- Train/design: first **120** accepted draws, 2022-12-21 .. 2026-05-22.
- Reused diagnostic block: next **40**, 2026-05-23 .. 2026-07-19.
- Final holdout: last **35**, 2026-07-20 .. 2026-08-23 — **still sealed / not scored**.

The 40-row block was exposed by Phase 1, so later use of it is diagnostic only and is not called an untouched test.

## Phase 1 — naive matrix anti-example

See `results/PHASE1_BASELINES.md`.

Naive matrix search selected **N=370** and achieved 120/120 profitable training draws with minimum training P/L **+137 AZN**, but collapsed on the next 40 rows:
- min payout/cost **0.2378**;
- average payout/cost **0.6136**;
- profitable draws **5%**.

Verdict: historical memorization / overfit, rejected as an edge.

## Phase 2 — robust complementary search

See `results/PHASE2_ROBUST.md`, `experiments/phase2_robust.py`, `src/robust_search.py`.

Frozen robust configuration:
- 6,000 deterministic candidate tickets, seed `20260824`;
- capped selection utility `15 AZN` to suppress rare 8+/9+/10-hit memorization;
- 3 perturbation variants per training draw, swapping 2 numbers;
- bottom 15% scenario targeting;
- chronological fold-stability prior;
- N free across all prefixes.

Training-only walk-forward configuration checks selected N=142 and N=270 on successive windows. Four leave-30-out checks selected N values **244, 292, 215, 192**, with omitted-block minimum payout/cost ratios **0.279, 0.366, 0.279, 0.333**.

Final Phase 2 fit on all 120 design rows selected **N=203**. Exact frozen tickets are saved in `results/phase2_candidate_203.csv`.

Training result, N=203:
- min payout/cost **0.5862**;
- p10 ratio **0.6256**;
- average ratio **1.1734**;
- worst P/L **-84 AZN**;
- profitable draws **42.5%**.

Reused 40-row diagnostic result:
- min payout/cost **0.2759**;
- p10 ratio **0.3719**;
- average ratio **0.7393**;
- worst P/L **-147 AZN**;
- average P/L **-52.93 AZN**;
- profitable draws **12.5%**.

This is materially better than Phase 1 on the reused diagnostic block but remains negative and is **NOT SUCCESS**.

A 500-draw uniform-random negative control showed Phase 2 behaves close to ordinary random same-size portfolios under a fair generator. Therefore portfolio geometry alone is not the missing edge.

## Holdout policy

The final **35 rows remain sealed**. Do not score them until a signal-conditioned method is frozen and materially stronger across past-only internal forward tests.

## NEXT ACTION

Run **Phase 3 empirical signal discovery**, using only information available before each target draw:

1. Build a walk-forward feature/evaluation framework; no future leakage.
2. Measure previous-draw and multi-lag overlap behavior versus fair/random controls.
3. Test rolling hot/cold signals with shrinkage rather than raw frequency chasing.
4. Test stable pair/triple co-occurrence signals with minimum-support controls.
5. Test range/parity/run/gap and rolling regime/change-point features.
6. Generate signal-conditioned candidate ticket pools, then use the Phase 2 robust portfolio layer to choose free N.
7. Require nested walk-forward improvement over random and Phase 2 controls before freezing any Phase 3 candidate.
8. Keep a ledger of failed signal families to avoid rediscovery.
9. Do **not** open the final 35-row holdout yet.

No autonomous recurring task is enabled for this repository.
