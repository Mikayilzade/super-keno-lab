# Phase 18AQ — Cosmic Orange sell-through velocity

Date: 2026-08-27

Status: **NO EXECUTABLE +EV YET; FIRST BOUND MULTI-TIMESTAMP SELL-THROUGH PAIR FOR A CURRENT DRAW.**

## Why this batch matters

Phase 18AP retained `iPhone 17 Pro 256 GB Cosmic Orange` as the strongest currently reproducible finite-pool target because the current Azerlotereya index bound together:

- prize: iPhone 17 Pro 256 GB Cosmic Orange;
- ticket price: 1 AZN;
- draw date: 16.09.2026;
- sold share: 43%.

This batch found an older cached first-party Misli snapshot for the **same prize / same 1-AZN price / same 16.09.2026 draw date** showing sold share **34%**, crawled three days before the current Azerlotereya snapshot.

Sources:
- current Azerlotereya card: https://www.azerlotereya.com/lotereya/1001-sevinc/tirajlar
- cached Misli first-party card: https://www.misli.az/lotereya/1001-sevinc/tirajlar

These are not transferred across draw cycles: the binding fields match the current draw instance.

## Observed movement

Bound observations:

| surface | observation/crawl timing | prize | price | draw date | sold |
|---|---|---|---:|---|---:|
| Misli | ~3 days before current crawl | iPhone 17 Pro 256 GB Cosmic Orange | 1 AZN | 16.09.2026 | 34% |
| Azerlotereya | 2026-08-27 current crawl | iPhone 17 Pro 256 GB Cosmic Orange | 1 AZN | 16.09.2026 | 43% |

Observed index movement: **+9 percentage points over approximately three crawl-days**.

Do **not** treat this as a guaranteed linear sales rate. Search-engine crawl time is an observation timestamp, not proof of the exact underlying transaction timestamp, and sales can accelerate/decelerate. Its value is that it proves sell-through is materially moving during the current draw cycle.

## EV consequence

Current retail benchmark retained from the prior phase for iPhone 17 Pro 256GB: `V = 3,289 AZN`.

Conservative non-cash prize tax model:

`V_economic = h*V - 0.14*(V-p)`

with `p=1 AZN` ticket price and `h` the usable/resale-value fraction.

Break-even cap ceiling at sold fraction `s`:

`C_max = V_economic / (p*s)`.

| usable value h | after-tax economic value | C_max at 34% sold | C_max at 43% sold |
|---:|---:|---:|---:|
| 60% | 1,513.08 | 4,450 | **3,519** |
| 70% | 1,841.98 | 5,418 | **4,284** |
| 80% | 2,170.88 | 6,385 | **5,049** |
| 100% | 2,828.68 | 8,320 | **6,578** |

Therefore the unknown cap that would make Cosmic Orange +EV has already become materially stricter as sell-through rose from the older 34% snapshot to the current 43% snapshot.

At the conservative 60%-usable-value level, the allowable cap ceiling fell from about **4,450** to **3,519** tickets — a reduction of about **21%** in the admissible denominator ceiling.

## Decision

1. **No purchase / no +EV claim.** Absolute cap or remaining count is still missing.
2. Cosmic Orange remains the best execution-quality target because its prize, price, draw date and current sold percentage are freshly bound together.
3. The finite-pool route is now explicitly time-sensitive: even if a draw becomes +EV at one snapshot, rising sell-through can destroy the edge before execution.
4. Any eventual scanner must recompute ROI from a fresh sell-through snapshot immediately before purchase; a historical percentage is not execution-valid.
5. Coupon remains unresolved and the expired 17% coupon observation is not reused.

## Next action

- Recover exact Cosmic Orange `drawId` and predetermined cap / absolute remaining count from a materially different client/rendered surface.
- Re-snapshot the same bound Cosmic Orange card later and store the timestamp; use it to estimate a range of sell-through velocity, not a single linear forecast.
- If `cap` or `remaining` is recovered, calculate live ROI immediately under 60/70/80/100% value haircuts and add an execution buffer for sell-through between observation and purchase.
- Continue new Super-Keno modifier scans only when the offer explicitly names `Lotereya` or exposes a product-category label for the credited balance.
