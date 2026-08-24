# Phase 11 — signal decomposition and candidate-generation seed robustness

Date: 2026-08-24

Status: **THE PHASE-10 WEAK LEAD DOES NOT SURVIVE STRATEGY-SEED ROBUSTNESS. CURRENT HOT/COLD/PAIR/REVERSION CLASS IS CLOSED AS A PRIMARY ROUTE.**

## 1. Frozen Phase-10 ensemble verification

`ensemble_b06` was first frozen exactly as found in Phase 10 and checked against 40 same-N random replicas.

- strategy ROI: **0.714730**
- strategy P/L: **-825 AZN**
- same-N random mean ROI: **0.559509**
- random replicas >= strategy: **3 / 40**
- empirical one-sided p: **0.09756**
- strategy above random mean in chronological blocks: **3 / 3**
- positive-P/L blocks: **0 / 3**

This justified decomposition as a weak lead, not promotion to a profit strategy.

## 2. Frozen-weight ablation

All ablations kept the same walk-forward harness, beta 0.6 and candidate-generation seed schedule. No new weights were optimized.

### Pair removals

| variant | ROI | P/L | block ROIs |
|---|---:|---:|---|
| original cold+pair+reversion (0.35/0.45/0.20) | **0.71473** | -825 | 0.6521 / 0.8292 / 0.6686 |
| cold+pair | 0.56242 | -1381 | 0.4347 / 0.4712 / 0.7500 |
| cold+reversion | 0.58480 | -1060 | 0.5917 / 0.4247 / 0.7198 |
| pair+reversion | 0.51649 | -2009 | 0.4149 / 0.4826 / 0.6335 |

### Single components

Using a small deterministic same-N random ensemble as a diagnostic control:

- `pair_only`: ROI **0.65569**, random mean ~**0.5250**, above random mean in **3/3** blocks;
- `cold_only`: ROI **0.58231**, random mean ~**0.52527**, above random mean in **2/3** blocks;
- `reversion_only`: ROI **0.50147**, random mean ~**0.62460**, above random mean in **1/3** blocks.

The pair component is the strongest standalone component in the original seed. Reversion is not useful alone; its apparent contribution in the full ensemble is interaction-dependent and nonlinear through ticket sampling / prefix selection.

## 3. Critical strategy-seed robustness test

The same frozen `ensemble_b06` signals and N-selection rule were rerun with different deterministic candidate-generation seed offsets. Only the sampled candidate tickets changed.

| seed offset | ROI | P/L |
|---:|---:|---:|
| 7 (original Phase-10 seed) | **0.71473** | -825 |
| 11 | 0.5444 | -1328 |
| 19 | 0.5388 | -1373 |
| 31 | 0.6591 | -1001 |
| 43 | 0.58203 | -1228 |

Across these five strategy seeds:
- mean ROI ≈ **0.608**;
- median ROI ≈ **0.582**;
- range ≈ **0.539 .. 0.715**.

The original 0.715 run is therefore a favorable candidate-generation realization. Once strategy-side sampling variance is included, the apparent ensemble edge largely collapses toward the game's ~0.599 fair gross-return level.

## 4. Pair-only seed robustness

The strongest standalone lead was also rerun under multiple candidate-generation seeds:

- offset 7: ROI **0.65569**
- offset 11: **0.64140**
- offset 19: **0.54539**
- offset 31: **0.50508**

Mean ≈ **0.5869**, median ≈ **0.5934**.

So pair-only also loses its apparent edge once strategy candidate-generation randomness is varied.

## 5. Decision

Rejected as a primary edge source:
- raw hot/cold;
- contextual pair signal in the current formulation;
- group mean reversion;
- their current fixed blend;
- conclusions based on one favorable candidate-ticket generation seed.

New evidence rule: **every adaptive method that contains stochastic ticket construction must be evaluated across multiple strategy-generation seeds, not only against random control tickets.** The canonical score is the strategy-seed distribution, not the best seed.

## Next direction

Move to deterministic or seed-averaged execution layers and qualitatively different predictive models. Do not retune the existing signal weights/windows to recover the favorable seed-7 result.
