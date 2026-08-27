# Phase 18BA — Silver freshness + execution-buffer cap table

Date: 2026-08-28

Status: **NOT YET SUCCESS — denominator still unresolved; Silver remains the best fully bound target.**

## Fresh first-party observation

A fresh Azerlotereya search/cache surface crawled 2026-08-28 again exposes the current 16.09.2026 1-AZN iPhone sequence and explicitly shows:

- `iPhone 17 Pro 256 GB Deep Blue` — current 1 AZN / 16.09.2026 card;
- `iPhone 17 Pro 256 GB Silver` — `Satıldı: 33%`.

Source:
- https://www.azerlotereya.com/lotereya/1001-sevinc/tirajlar

This reconfirms the standing fully bound Silver record:

`drawId=10066 | iPhone 17 Pro 256 GB Silver | 1 AZN | 16.09.2026 | sold=33% | observed 2026-08-28`.

The crawler does **not** expose a safely attributable sold percentage for Deep Blue in the same fresh observation. Therefore `drawId=10064 Deep Blue` remains sold%-unresolved and is not promoted above Silver by inference.

## Execution-buffer cap table

Standing assumptions used only for sensitivity:

- market/economic reference value `V = 3,150 AZN`;
- ticket price `p = 1 AZN`;
- conservative property-prize tax model: `14% * (V - p)`;
- usable/resale fraction `h = 60/70/80/100%`;
- if total ticket cap is `C` and sold fraction at execution is `s`, expected ticket cost of all sold positions is proportional to `C*s`, so break-even cap ceiling is `V_net / (p*s)`.

| usable value | 33% sold (fresh) | 35% sold | 38% sold | 43% sold |
|---:|---:|---:|---:|---:|
| 60% | 4,391 | 4,140 | 3,814 | 3,370 |
| 70% | 5,346 | 5,040 | 4,642 | 4,103 |
| 80% | 6,300 | 5,940 | 5,471 | 4,835 |
| 100% | 8,210 | 7,740 | 7,129 | 6,300 |

Interpretation: if an absolute denominator is eventually recovered, execution must use the **current** sold fraction or a conservative forward buffer rather than the stale 33% observation. For example, a cap that only clears the 33% threshold may cease to be +EV after a few additional percentage points of sell-through.

## Decision

1. `drawId=10066 Silver` remains denominator target #1.
2. Do not infer a Deep Blue sold% from neighboring snippets/order; require an explicit fresh `(prize + sold% + date/price)` binding.
3. Absolute `cap / remaining / sold-count` remains the decisive missing variable.
4. When a denominator is recovered, evaluate at both observed sold% and a conservative execution-buffer sold% before calling a live opportunity positive-EV.
5. No Super-Keno modifier classification changes in this batch; the EV-modifier ledger is unchanged.
