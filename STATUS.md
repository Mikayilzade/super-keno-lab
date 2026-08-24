# Super Keno Lab — status

Last updated: 2026-08-24

## Phase

`PHASE 6 — frame-level equipment annotation / externally defined physical regimes`

## Core state

- Dedicated repo: `Mikayilzade/super-keno-lab`; broad `loto-research` remains separate and untouched.
- **195** validated Super Keno draws, 2022-12-21..2026-08-23.
- Final **35 draws (2026-07-20..2026-08-23) remain sealed / unscored**.
- Portfolio size **N is a free integer optimization variable**.
- Current official rules/payouts are snapshotted; scorer/evaluator, baselines and robust free-N search are reproducible.

## Phase 1 — naive matrix anti-example

Naive matrix selected N=370 and achieved 120/120 profitable design draws with minimum design P/L +137 AZN, then collapsed on the next 40 exposed rows: min return 0.2378, average return 0.6136, profitable 5%.

Verdict: historical memorization / overfit, rejected.

## Phase 2 — robust complementary portfolio

Frozen robust search selected N=203. Reused 40-row diagnostic: min return 0.2759, average return 0.7393, worst P/L -147 AZN, profitable 12.5%.

A 500-draw fair-generator control showed portfolio geometry alone is not the missing edge.

## Phase 3 — empirical signal audit

No signal gate passed. Previous-draw repeat/avoid, raw hot/cold, fixed pairs and simple structural persistence failed. Weak leads only: contextual pair score and mild group-level mean reversion.

## Phase 4 — physical mechanism audit

Evidence supports a **physical lototron / physical-ball process** for televised Super Keno and use of French Akanis Technologies equipment at the draw-lottery level. Exact Super Keno machine model, ball-set rotation, RFID configuration and backup-machine substitution dates remain unknown.

First 160 exposed rows: number 4 is coldest (24 appearances vs fair expectation 45.714); global distribution remains compatible with fair behavior. Independent next-40 check for #4 is directionally low but weak (8 vs expected 11.43; p≈0.15). Hard exclusion of #4 worsened overall monetary performance.

Weak numeric change-point near 2026-06-01→02 did not persist on longer windows.

## Phase 5 — video metadata / operational regimes

See:
- `research/PHASE5_VIDEO_METADATA_LEDGER.md`
- `results/PHASE5_VIDEO_AND_REGIME_LEDGER.md`
- `experiments/phase5_operational_regime_audit.py`
- `results/phase5_operational_regime_audit.json`

### Official media trail established

Official Telegram archive contains draw media continuously across **2026-06-01..06-08** (26231..26241 calendar-coded series), covering the Phase-4 weak change-point neighborhood.

Official Azərlotereya TV YouTube videos exist around January 2025, including 2025-01-05 (25017), 2025-01-10 (25025) and 2025-01-11 (25026).

Frames have not yet been reliably annotated in this workflow, so no machine/ball-set change is claimed from the videos yet.

### Better January operational boundary

Official material confirms 2025-01-06 was the final 5/36 draw and Beşdə 5 replaced it from 2025-01-07; a broader draw-lottery branding/site refresh was announced 2025-01-15.

`2025-01-07` is therefore an **externally documented program/studio-lineup boundary**, but remains mechanically UNKNOWN for Super Keno.

### Draw IDs resolved

Across the first 160 exposed rows, **107/107 known official draw IDs** equal calendar code `YYWWD` = two-digit ISO week-year + ISO week + ISO weekday.

Therefore apparent draw-number jumps are not sequential missing-draw evidence. Cancellation/postponement must be proven independently.

### #4 chronology / weekday sanity check

Number 4 counts across exposed 20-row blocks: `6, 2, 1, 2, 4, 1, 4, 4`. Coldness predates June 2026 and does not identify a sharp June machine regime.

Simple weekday/shared-program fingerprint is also unsupported. In the later documented current-schedule period, the Tue/Fri-vs-other-days 70-number frequency-difference correlation from design to reused diagnostic is **-0.0027**; individual weekday profile correlations are all roughly -0.152..+0.027.

Verdict: a simple fixed ball-set-by-weekday/shared-program explanation is rejected on exposed data.

## Current hypothesis ledger

- `H-MECH-01` pure software RNG: evidence against as working model; physical lototron better supported.
- `H-RULE-01` 2025-01-10 mechanical reset: rejected as unsupported.
- `H-TIME-01` Super-Keno-specific 18:45 shift: rejected; likely site-wide display/metadata behavior.
- `H-PHY-01` persistent physical/ball-set bias, especially #4: open but unconfirmed.
- `H-REG-01` early-June-2026 operational change: open only for independent video check; number evidence alone is weak.
- `H-WDAY-01` stable weekday/shared-program ball-set fingerprint: rejected in simple form.
- `H-JAN25-01` 2025-01-07 program/studio transition: confirmed operational boundary, mechanical status unknown.
- `H-DRAWID-01` draw-number gaps imply sequential missing draws: rejected; IDs are YYWWD calendar codes.

## Holdout policy

The final **35 real draws remain sealed**. Do not inspect/score them until a frozen signal-conditioned method is materially stronger on independent past-only checks.

## NEXT ACTION — Phase 6

1. Obtain frame-level annotations from official 2026-06-01..08 and January-2025 draw media: machine/chamber shape, loader/output path, ball color/font, reader/display, studio position and visible substitutions.
2. Extend the video ledger around 2026-05-20..06-15 and older 2022/2023 footage.
3. Search authoritative/public evidence for exact Akanis model, ball-set count, rotation/replacement policy, RFID mode and backup-machine use.
4. If an equipment boundary is externally confirmed, rerun physical-frequency tests only inside predefined homogeneous regimes.
5. Expand older contiguous draw history where video-covered periods can provide independent verification.
6. If machine metadata remains inaccessible, pivot from ball identity to other operational information knowable before ticket purchase rather than endlessly mining frequencies.
7. Only then feed a supported signal into robust free-N portfolio selection.
8. Keep failed hypotheses/results recorded and keep final 35 holdout sealed.

No autonomous recurring task is enabled for this repository.
