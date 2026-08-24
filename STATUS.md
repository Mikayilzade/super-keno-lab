# Super Keno Lab — status

Last updated: 2026-08-24

## Phase

`PHASE 5 — video/equipment-set metadata and independent physical-bias verification`

## Core project state

- Dedicated repository: `Mikayilzade/super-keno-lab`; broad `loto-research` remains separate and untouched.
- **195** validated Azerbaijan Super Keno draws, earliest 2022-12-21, latest 2026-08-23.
- Structural errors 0; duplicate dates 0; duplicate 20-number combinations 0.
- Portfolio size **N is a free integer optimization variable**.
- Final **35 draws (2026-07-20..2026-08-23) remain sealed / not scored**.
- The next 40 rows after original design were exposed in Phase 1 and are reused only as a diagnostic block.

## Phase 1 — naive matrix anti-example

See `results/PHASE1_BASELINES.md`.

Naive matrix selected **N=370** and created 120/120 profitable design draws, minimum design P/L **+137 AZN**, then collapsed on the next 40:
- min return 0.2378;
- average return 0.6136;
- profitable draws 5%.

Verdict: historical memorization / overfit, rejected.

## Phase 2 — robust complementary portfolio

See `results/PHASE2_ROBUST.md`.

Frozen robust search selected **N=203**.

Reused 40-row diagnostic:
- min return **0.2759**;
- average return **0.7393**;
- worst P/L **-147 AZN**;
- average P/L **-52.93 AZN**;
- profitable draws **12.5%**.

A 500-draw fair-generator control showed portfolio geometry alone is not the missing edge.

## Phase 3 — walk-forward empirical number signals

See `results/PHASE3_SIGNAL_AUDIT.md`.

Verdict: **NO SIGNAL GATE PASSED**.

Weak leads only:
- contextual pair score (20-draw window): diagnostic top-30 mean hits 9.026 vs fair 8.571, p≈0.073;
- mild first-quarter composition mean reversion.

### Important Phase 4 correction to Phase 3

Phase 3 provisionally treated the current-rule effective date **2025-01-10** as a regime boundary and excluded earlier rows for some current-regime signal checks.

That mechanical interpretation is now **superseded**. Official Azərlotereya TV draw numbering is continuous across Jan 9–12, 2025 (25024 → 25025 → 25026 → 25027), and Super Keno existed/broadcast earlier. The registration date alone is not evidence of a machine/ball-set change.

Do not exclude older rows from physical-regime work solely because of 2025-01-10.

## Phase 4 — operational mechanics + physical-bias audit

See:
- `research/OPERATIONAL_MECHANICS_2026-08-24.md`
- `results/PHASE4_OPERATIONAL_AND_PHYSICAL.md`
- `experiments/phase4_physical_regime_audit.py`
- `results/phase4_physical_regime_audit.json`
- `experiments/phase4_cold_exclusion_test.py`

### Mechanism finding

Evidence now strongly supports a **physical lototron / physical-ball process** for televised Super Keno rather than a pure software-RNG working model:

- Azerbaijani draw-lottery rules explicitly regulate lototron operation, equal ball/item weight/size/shape, transparent automatic mixing and sealed/closed storage;
- a 2022 studio media tour specifically covering Super Keno reports equipment testing, ball weighing, gloves, French **Akanis Technologies** machines and backup lototron/equipment;
- Akanis specializes in air-mix draw machines and ball sets.

Exact current machine model, ball-set rotation/replacement and RFID/automatic-recognition configuration are still unknown.

### 19:45 vs 18:45

Official TV schedule says **19:45**. Current results metadata says **18:45**, but the same 18:45 timestamp appears for Beşdə 5 and 4+4. Treat as likely site-wide metadata/timezone/display behavior, not a Super Keno-specific edge.

### Physical-frequency audit — first 160 exposed rows only

Expected appearances per number: **45.714**.

Observed:
- number **4**: only **24** appearances (coldest);
- number **45**: **58** appearances (hottest);
- max-min range 34, adjusted MC p≈**0.052**;
- maximum scanned single-number deviation, adjusted MC p≈**0.011**;
- global 70-number chi-like statistic p≈**0.909**.

So the global distribution is not abnormal, but number 4 is a legitimate follow-up outlier.

Independent diagnostic check for #4: **8 appearances in 40** vs expected ≈11.43; one-sided p≈**0.15**. Direction persists but does not pass the signal gate.

Hard-excluding #4 or the design-coldest groups from Phase-2 candidate tickets did **not** create an edge. Avoiding #4 improved the single worst diagnostic ratio to ~0.317 but reduced average return to ~0.494 and profitable draws to 2.5%.

Verdict: physical-cold hypothesis remains **unconfirmed; not a betting rule**.

### Change-point scan

Strongest 10-row hint is at **2026-06-01 → 2026-06-02**, adjusted MC p≈**0.070**. Longer 15/20/30-row windows weaken sharply (≈0.149 / 0.505 / 0.897).

Verdict: weak lead only; no statistical or documented regime boundary yet.

## Current hypothesis ledger

- `H-MECH-01` pure software RNG: **evidence against / not working model**.
- `H-RULE-01` Jan-10-2025 mechanical reset: **rejected as unsupported**.
- `H-TIME-01` Super-Keno-specific 18:45 shift: **rejected as game-specific clue**.
- `H-PHY-01` persistent ball/set-specific physical bias (#4 lead): **open, unconfirmed**.
- `H-REG-01` early-June-2026 operational change: **open weak lead, unconfirmed**.

## Holdout policy

The final **35 real draws remain sealed**. Do not inspect/score them for strategy selection until a physical/signal-conditioned method is frozen and materially stronger on independent past-only tests.

## NEXT ACTION — Phase 5

Build a **historical draw-video / equipment-set metadata ledger** before further portfolio tuning:

1. Inspect official Azərlotereya TV draw videos, prioritizing 2025-01-09..12 and 2026-05-20..06-15.
2. Record draw date/number, machine appearance/model clues, ball-set appearance, studio/layout, sequence, presenters and visible interruptions/substitutions.
3. Find authoritative evidence for exact Akanis model, number of ball sets, set rotation/replacement policy, RFID/number recognition and backup-machine use.
4. Search official news/reports for technical interruptions, equipment/studio changes and maintenance/substitution events.
5. Expand older **contiguous** Super Keno result history where possible; physical-bias verification needs more independent draws and known regimes.
6. Use externally identified equipment/regime boundaries to retest #4 and other ball identities; do not data-mine a boundary and then call it independent.
7. Only after a physical signal survives independent temporal checks should it feed the robust **free-N** portfolio layer.
8. Keep failed hypotheses/results in the repo and keep the final 35-row holdout sealed.

No autonomous recurring task is enabled for this repository.
