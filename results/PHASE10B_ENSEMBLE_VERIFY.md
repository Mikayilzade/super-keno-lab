# Phase 10B — frozen ensemble_b06 verification

Date: 2026-08-24

Status: **PROMOTE AS A WEAK SIGNAL LEAD, NOT A PROFIT STRATEGY.**

The exact Phase-10 `ensemble_b06` method was frozen without parameter retuning and replayed over the same 125 strict one-step walk-forward targets. At every target its selected N was compared against **40 deterministic same-N random portfolios**.

## Frozen strategy

- targets: **125**
- total cost: **2892 AZN**
- total payout: **2067 AZN**
- net P/L: **-825 AZN**
- ROI: **0.714730**
- profitable targets: **12.8%**
- N range: **19..45**, median **20**
- largest one-target payout: **177 AZN**

## Same-N random distribution

- mean ROI: **0.559509**
- ROI standard deviation: **0.172407**
- 5th–95th percentile: **0.447216 .. 1.087327**
- best random replicate: **1.157331**
- worst random replicate: **0.425657**
- random replicates with ROI >= strategy: **3 / 40**
- empirical one-sided p: **0.097561**

This is evidence of a weak separation from random, not proof of an edge. With only 40 replicates and an unprofitable strategy, the result is deliberately treated as a lead rather than a success.

## Chronological blocks

| block | strategy ROI | same-N random mean | strategy P/L | above random mean? |
|---|---:|---:|---:|---|
| 2026-02-22..2026-05-12 | 0.652079 | 0.544119 | -318 AZN | yes |
| 2026-05-13..2026-06-21 | 0.829189 | 0.534973 | -158 AZN | yes |
| 2026-07-10..2026-08-23 | 0.668566 | 0.594421 | -349 AZN | yes |

The frozen method beats the same-N random mean in **3/3 chronological blocks**, but positive-P/L blocks remain **0/3**.

## Payout concentration

Total payout by hit tier:
- 1 hit: 339 AZN
- 5 hits: 498 AZN
- 6 hits: 435 AZN
- 7 hits: 195 AZN
- 8 hits: 600 AZN
- 9/10 hits: 0 AZN

Payout from 8+ hits: **600 AZN = 29.0%** of total payout. The lead is therefore not a jackpot/9-or-10-hit artifact, but 8-hit events still contribute materially and must be controlled in follow-up tests.

## Decision

- strategy positive: **false**
- beats random overall mean: **true**
- chronological blocks above random mean: **3/3**
- positive-P/L blocks: **0/3**
- promote to targeted signal decomposition: **true**

Next step: freeze the same walk-forward harness and perform past-only ablations of the ensemble components. Do not optimize weights yet. Determine whether cold frequency, contextual pair structure, group mean reversion, or their interaction is responsible for the repeated separation from random.
