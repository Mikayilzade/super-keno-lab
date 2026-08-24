# Phase 5 — video metadata and operational-regime checkpoint

Date: 2026-08-24

Status: **NO MACHINE-DEFINED EDGE CONFIRMED.** Public evidence improved enough to define the next metadata work without opening the final 35-row holdout.

## 1. Official media archive is usable

An official continuous Telegram media trail exists across **2026-06-01..2026-06-08**, exactly around the weak Phase-4 numerical change-point hint. Entries identify draws 26231, 26232, 26233, 26234, 26235, 26236, 26237 and 26241.

Official YouTube videos also exist around the January-2025 program transition, including draws 25017 (2025-01-05), 25025 (2025-01-10) and 25026 (2025-01-11).

This means future equipment-regime boundaries can be defined from independent visual evidence rather than from the numbers themselves. In this pass, frames were **not** reliably extracted/annotated, so machine appearance, ball-set identity and backup-machine use remain UNKNOWN.

Ledger: `research/PHASE5_VIDEO_METADATA_LEDGER.md`.

## 2. Exact machine/set configuration still missing

Evidence supports physical Akanis equipment and air-mix technology at the manufacturer family level. Public sources found so far do **not** establish:

- exact Super Keno machine model/serial;
- number of ball sets;
- ball-set rotation/replacement policy;
- whether Azerbaijan's unit uses RFID recognition;
- dates when backup equipment was substituted.

Therefore no equipment-specific number effect is claimed yet.

## 3. Better externally defined January-2025 boundary

The previous `2025-01-10` rule-registration boundary is still not accepted as a mechanical reset.

A more meaningful external operational boundary exists on **2025-01-07**: official Azərlotereya material says 2025-01-06 was the final 5/36 draw and Beşdə 5 replaced it the next day; the 2025-01-15 announcement documents a wider draw-lottery branding/site refresh.

This is a **program/studio-lineup boundary only**. It becomes a video-comparison target, not a machine-change label.

## 4. Draw-number semantics resolved

Reproducible audit: `experiments/phase5_operational_regime_audit.py`.
Raw output: `results/phase5_operational_regime_audit.json`.

For the first **160 already-exposed draws**, there are 107 rows with an official draw ID. **107/107** exactly match:

`YYWWD` = 2-digit ISO week-year + 2-digit ISO week number + ISO weekday.

Examples:
- 2025-01-10 -> 25025;
- 2026-06-01 -> 26231.

Consequence: apparent draw-number gaps are calendar coding, not evidence of skipped sequential draws. Cancellation/postponement hypotheses require separate official evidence.

## 5. Number-4 chronology does not identify a sharp June regime

Across consecutive 20-row blocks of the first 160 exposed draws, number 4 appeared:

`6, 2, 1, 2, 4, 1, 4, 4` times.

The strongest coldness occurs well before and through May 2026; after the weak June change-point it does **not** suddenly normalize or collapse. This weakens the idea that the Phase-4 #4 observation is explained by a single early-June machine switch.

It remains a physical-bias candidate requiring actual ball-set/machine metadata, not a strategy rule.

## 6. Simple weekday / shared-program rotation hypothesis weakened

Number 4 appearances by weekday in the first 160 exposed rows:

| Weekday | Draws | #4 appearances | Rate |
|---|---:|---:|---:|
| Mon | 21 | 1 | 4.8% |
| Tue | 21 | 2 | 9.5% |
| Wed | 24 | 5 | 20.8% |
| Thu | 23 | 2 | 8.7% |
| Fri | 24 | 6 | 25.0% |
| Sat | 24 | 3 | 12.5% |
| Sun | 23 | 5 | 21.7% |

For the later period where the current shared-program schedule is documented, a Tue/Fri (4+4 days) versus other-days frequency fingerprint was compared across the design and reused diagnostic blocks. The 70-number difference-vector correlation was **-0.0027**.

Per-weekday 70-number profile correlations between the design portion and diagnostic portion were all approximately **-0.152 to +0.027**.

Verdict: there is **no stable exposed-data fingerprint consistent with a simple fixed ball-set-by-weekday or fixed shared-program-day assignment**. Undocumented rotations remain possible, but this easy version of the hypothesis is not supported.

## 7. Schedule history is real, but not yet mechanical

- 2022 studio report: draw show at 20:30.
- official 2023 material: Super Keno daily 19:45; 4+4 Mon/Wed/Fri/Sat.
- current official schedule: Super Keno and Beşdə 5 daily 19:45; 4+4 Tue/Fri.

These are externally documented operational regimes. Without machine/ball-set evidence, they are not used to split number statistics as if they were mechanical regimes.

## 8. Hypothesis ledger update

- `H-PHY-01` persistent physical/ball-set bias (#4): **OPEN, weaker as a single-June-regime story**.
- `H-REG-01` early-June-2026 change: **OPEN FOR VIDEO CHECK ONLY; numbers alone do not support a persistent boundary**.
- `H-WDAY-01` stable weekday/shared-program ball-set fingerprint: **REJECTED in simple form on exposed data**.
- `H-JAN25-01` 2025-01-07 studio/program transition: **CONFIRMED operational boundary; mechanical status UNKNOWN**.
- `H-DRAWID-01` draw IDs are sequential counters whose gaps indicate missing/cancelled draws: **REJECTED**; IDs are calendar-coded YYWWD in all 107 exposed rows with known IDs.

## Holdout decision

**Final 35 draws remain sealed and unscored.** Phase 5 has not produced a machine-defined signal strong enough to spend them.

## NEXT ACTION — Phase 6

1. Obtain frame-level annotations from official June-2026 and January-2025 draw videos: machine body/chamber, ball appearance/font/color, loader/output path, reader/display, studio position.
2. Search public documents and older footage for exact machine model and ball-set handling/rotation/replacement evidence.
3. Expand older contiguous result blocks if obtainable, prioritizing periods with video coverage.
4. If a visual/equipment boundary is externally confirmed, rerun physical-frequency tests *within that predefined regime*.
5. If no equipment metadata can be recovered, pivot away from physical-number identity and test other operational information that is knowable before ticket purchase.
6. Do not open the final 35-row holdout until a frozen method survives independent past-only checks.
