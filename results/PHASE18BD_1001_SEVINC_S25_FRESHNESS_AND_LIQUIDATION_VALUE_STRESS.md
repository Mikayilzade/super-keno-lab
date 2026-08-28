# Phase 18BD — S25 freshness + liquidation-value stress

Date: 2026-08-28

Status: **NOT YET SUCCESS — S25 remains bound but no fresh sold% was reacquired; valuation assumptions were materially tightened.**

## Freshness result

Targeted first-party searches for `Samsung Galaxy S25 Ultra Black` + `16.09.2026` + `Satıldı` did not return a fresh complete current-cycle record today. Therefore the older ~41% Misli observation remains **monitoring-only** and is not promoted back into execution input.

Current cycle itself is still live: Azerlotereya shows 11 draws dated 16.09.2026 (3 × 1 AZN, 8 × 0.5 AZN).

Sources:
- https://www.azerlotereya.com/lotereya/1001-sevinc/tirajlar
- https://www.azerlotereya.com/lotereya/1001-sevinc

## Fresh local liquidation-value evidence

Current Azerbaijan resale/discount-market references for Galaxy S25 Ultra 256 GB are materially below high retail anchors:
- `ucuztap.az` current crawl: around **1,998 AZN**, listing text also quotes ~1,949 AZN for S25 Ultra 256 GB;
- `qiymetleri.az` current crawl: examples around **2,050 AZN**, with other sellers higher.

Sources:
- https://ucuztap.az/elan/7657025-samsung-galaxy-s25-ultra-titanium-black-256gb-12gb
- https://qiymetleri.az/s25-ultra

For conservative execution modelling, use **2,000 AZN** as the primary liquidation anchor until a better exact-model current offer is observed.

## Cap sensitivity at V = 2,000 AZN and p = 0.5 AZN

Standing property-prize tax model:

`V_economic = h*V - 0.14*(V-p)`

Break-even total cap under sold fraction `s`:

`C_break_even = V_economic / (p*s)`

| sold fraction | 60% usable | 70% usable | 80% usable | 100% usable |
|---:|---:|---:|---:|---:|
| 35% | 5,258 | 6,400 | 7,543 | 9,829 |
| 40% | 4,600 | 5,600 | 6,600 | 8,600 |
| 41% | 4,488 | 5,464 | 6,439 | 8,391 |
| 45% | 4,089 | 4,978 | 5,867 | 7,645 |
| 50% | 3,680 | 4,480 | 5,280 | 6,880 |

Interpretation: S25 remains potentially stronger than a 1-AZN iPhone because of the 0.5-AZN ticket, but the edge is less tolerant than earlier high-retail-value estimates suggested. A future positive-EV call requires both a **fresh sold%** and an absolute **cap / remaining / sold count**.

## Decision

- Keep `drawId=10072 / S25 Ultra Black` fully bound.
- Do **not** use ~41% as a live sold input until reacquired as a fresh complete record.
- Replace optimistic retail anchors with ~2,000 AZN liquidation anchor for conservative execution work.
- Silver `10066` remains execution target #1 only because it still has a fresher complete sold observation; S25 can retake #1 immediately if fresh sold% is reacquired and its cap tolerance still dominates.

## Next action

1. Reacquire fresh first-party S25 sold%.
2. Seek absolute cap/remaining for `10072` and `10066` only through genuinely new rendered/account/client artifacts.
3. If S25 sold% is reacquired, rank it immediately against Silver using the 2,000-AZN liquidation anchor and 14% tax model.
