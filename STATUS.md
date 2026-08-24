# Super Keno Lab — status

Last updated: 2026-08-24

## Phase

`PHASE 4 — operational/regime discovery before further portfolio optimization`

## Completed foundation

- Dedicated repository: `Mikayilzade/super-keno-lab`; broad `loto-research` remains separate and untouched.
- Copied and validated **195** Azerbaijan Super Keno draws in four chronological CSV shards.
- Dataset: earliest **2022-12-21**, latest **2026-08-23**; structural errors 0, duplicate dates 0, duplicate 20-number combinations 0.
- Current official rules/payouts/ticket price are snapshotted in `rules/SUPER_KENO_RULES_2026-08-24.md`.
- Configurable scorer/evaluator and deterministic baselines are implemented.
- Portfolio size **N is a free integer optimization variable**, not a round-number grid.

## Evaluation policy

- Original Phase 1 design: first **120** accepted draws.
- Reused diagnostic block: next **40**, 2026-05-23 .. 2026-07-19.
- Final holdout: last **35**, 2026-07-20 .. 2026-08-23 — **still sealed / not scored**.
- The 40-row block was exposed by Phase 1, so later use is diagnostic only.

### Current-rule regime correction

Official Super Keno registration shown on the current game page is **285 / 07.01.2025**, effective **10.01.2025–31.12.2027**.

The copied dataset contains **8 rows before 2025-01-10** (one 2022 row and 2025-01-01 through 2025-01-07). These rows are now treated as **legacy/pre-current-rule** and are excluded by default from current-regime signal fitting.

See `research/OPERATIONAL_MECHANICS_2026-08-24.md`.

## Phase 1 — naive matrix anti-example

See `results/PHASE1_BASELINES.md`.

Naive matrix search selected **N=370** and achieved 120/120 profitable training draws with minimum training P/L **+137 AZN**, then collapsed on the next 40 rows:
- min payout/cost **0.2378**;
- average payout/cost **0.6136**;
- profitable draws **5%**.

Verdict: historical memorization / overfit, rejected.

## Phase 2 — robust complementary search

See `results/PHASE2_ROBUST.md`, `experiments/phase2_robust.py`, `src/robust_search.py`.

Frozen robust search selected **N=203**.

Reused 40-row diagnostic result:
- min payout/cost **0.2759**;
- average payout/cost **0.7393**;
- worst P/L **-147 AZN**;
- average P/L **-52.93 AZN**;
- profitable draws **12.5%**.

A 500-draw uniform-random control showed this geometry behaves close to ordinary random same-size portfolios under a fair generator. Portfolio geometry alone is not the missing edge.

## Phase 3 — empirical signal audit

See `results/PHASE3_SIGNAL_AUDIT.md` and `experiments/phase3_signal_audit.py`.

Verdict: **NO SIGNAL GATE PASSED**.

### Previous-draw behavior

Current-regime design consecutive-day transitions: **95**.
- mean consecutive overlap **5.579**;
- P(next | number appeared previous day) **0.2789**;
- P(next | absent previous day) **0.2884**.

Diagnostic consecutive transitions: **39**.
- mean overlap **6.000**;
- P(next | appeared previous day) **0.3000**;
- P(next | absent previous day) **0.2800**.

Direction reverses. Simple repeat/avoid rules rejected.

### Hot/cold

Long-window cold ranking looked mildly positive inside design but did not reach a convincing diagnostic gate.

Cold-80 top-30:
- diagnostic mean hits **8.875** vs fair **8.571**;
- Monte Carlo one-sided fair-control p **0.165**.

Per-number frequency rankings are not stable:
- design-half frequency correlation **-0.109**;
- later design half vs diagnostic **0.021**.

### Pair context

Best weak lead: 20-draw contextual pair score using previous-day numbers.
- diagnostic mean top-30 hits **9.026** vs fair **8.571**;
- diagnostic AUC **0.5155**;
- Monte Carlo one-sided p **0.073**.

Interesting but below gate; not promoted to money strategy.

Fixed pair maps are unstable:
- design-half pair residual correlation **0.0286**;
- later design half vs diagnostic **0.0035**.

### Structural features

Most lag signals in range/parity/sum/runs reverse or disappear. Mild negative lag correlation for first-quarter count (1..17) persists descriptively, but no validated monetary edge exists.

## Operational clues discovered

Official sources currently create unresolved questions that may matter more than number-frequency fitting:

- current page calls Super Keno a **virtual numeric lottery** with 20 balls taken from a **lototron**;
- official explanatory material also discusses computer/virtual execution of online draw lotteries;
- official live schedule repeatedly states **19:45** every day;
- recent result metadata is stamped **18:45**;
- live broadcasts exist on Xəzər TV / Azərlotereya TV;
- technical issues may lead to cancellation/postponement.

These are clues/data-quality questions only, not claimed edges. See `research/OPERATIONAL_MECHANICS_2026-08-24.md`.

## Holdout policy

The final **35 real draws remain sealed**. Do not score or inspect them for strategy selection until a materially stronger, frozen signal-conditioned method exists.

## NEXT ACTION

Run **Phase 4 operational/regime discovery**:

1. Determine the actual Super Keno randomization mechanism from authoritative rules, technical/audit documentation or historical draw footage: physical ball machine vs software/RNG/virtual process.
2. Resolve the official **19:45 schedule vs 18:45 result timestamp** discrepancy; establish whether it is timezone/backend metadata or a genuine regime change.
3. Search official news/archive/broadcast evidence for equipment, software, studio, draw-process or schedule changes since 2022, especially around **2025-01-10**.
4. Collect cancellation/postponement/technical-exception dates if available.
5. Map official draw-number/date continuity and regime boundaries without inventing missing rows.
6. If documented regimes exist, rerun Phase 3 signal tests separately within homogeneous regimes.
7. Only if a regime-conditioned signal passes nested walk-forward gates should it feed the Phase 2 robust free-N portfolio layer.
8. Keep the final 35-row holdout sealed.

No autonomous recurring task is enabled for this repository.
