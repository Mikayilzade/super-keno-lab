# Phase 18CJ — user-runtime full inventory breakthrough

Date: 2026-08-29

## Result

The long-standing absolute-denominator blocker for the current `1001 Sevinc` cycle is substantially resolved from authenticated/rendered user-runtime screenshots.

For every current prize modal inspected, the UI exposes `Biletlərin sayı` (specified total ticket count/cap), alongside draw ID, stated prize value, prize count and ticket price. The parent collection simultaneously exposes current integer `Satıldı` percentages.

Canonical snapshot is saved in:

- `results/phase18cj_user_runtime_full_inventory_snapshot_2026-08-29.csv`

## Current draw mapping and caps

| drawId | prize | prize qty | stated value each | card price | modal price | cap C | sold% |
|---:|---|---:|---:|---:|---:|---:|---:|
| 10065 | iPhone 17 Pro 256 GB Cosmic Orange | 1 | 3200 | 1.0 | 1.0 | 6400 | 45 |
| 10064 | iPhone 17 Pro 256 GB Deep Blue | 1 | 3200 | 1.0 | 1.0 | 6400 | 36 |
| 10066 | iPhone 17 Pro 256 GB Silver | 1 | 3200 | 1.0 | 1.0 | 6400 | 34 |
| 10072 | PlayStation 5 Slim 1TB | 1 | 1200 | 0.5 | 0.5 | 4000 | 57 |
| 10073 | Samsung Galaxy S25 Ultra Black | 1 | 2500 | **0.5** | **1.0** | 8800 | 44 |
| 10067 | 1000-AZN gift coupon | 3 | 1000 | 0.5 | 0.5 | 12000 | 17 |
| 10071 | iPad Air 13-inch M2 128GB | 1 | 1500 | 0.5 | 0.5 | 6000 | 27 |
| 10068 | Samsung refrigerator | 1 | 1200 | 0.5 | 0.5 | 4800 | 24 |
| 10069 | Samsung washing machine | 1 | 700 | 0.5 | 0.5 | 2800 | 33 |
| 10070 | Samsung dishwasher | 1 | 765 | 0.5 | 0.5 | 3000 | 36 |
| 10074 | Samsung TV OLED 55 | 1 | 1100 | 0.5 | 0.5 | 4000 | 28 |

### Important corrections

1. `10072` is **PS5 Slim**, not S25. The prior `10072 -> S25` mapping was wrong.
2. `10073` is **S25 Ultra Black**.
3. The S25 runtime has an internal price contradiction: the live parent card shows **0.5 AZN**, while the detail modal says **1 manat**. Do not treat S25 as executable until the actual checkout/network transactional price is resolved.
4. Silver has advanced from the previous 33% observation to **34% sold**.

## Current break-even screen

Standing conservative property-prize working model remains:

`V_net_per_prize(h) = h*V - 0.14*(V-p)`

where `h` is usable/liquidation value as a fraction of operator-stated value. For `q` prizes:

`Pool_net = q * V_net_per_prize`

With full cap `C` and ticket price `p`, the sold-share break-even threshold is:

`S_break_even = Pool_net / (p*C)`

The table below uses the modal price except S25, where calculations are only diagnostic under the **0.5-AZN card-price hypothesis**.

| draw | sold% | BE sold% @100% usable | implied current ROI @100% | BE sold% @80% usable | implied current ROI @80% |
|---|---:|---:|---:|---:|---:|
| Cosmic 10065 | 45 | 43.00 | 0.956 | 33.00 | 0.733 |
| Deep Blue 10064 | 36 | 43.00 | 1.195 | 33.00 | 0.917 |
| Silver 10066 | 34 | 43.00 | 1.265 | 33.00 | 0.971 |
| PS5 10072 | 57 | 51.60 | 0.905 | 39.60 | 0.695 |
| S25 10073 (`p=0.5` hypothesis only) | 44 | 48.87 | 1.111 | 37.50 | 0.852 |
| 3x1000 coupon 10067 | 17 | 43.00 | **2.530** | 33.00 | **1.941** |
| iPad 10071 | 27 | 43.00 | **1.593** | 33.00 | **1.222** |
| refrigerator 10068 | 24 | 43.00 | **1.792** | 33.00 | **1.375** |
| washer 10069 | 33 | 43.00 | 1.303 | 33.01 | ~1.000 |
| dishwasher 10070 | 36 | 43.86 | 1.218 | 33.66 | 0.935 |
| TV OLED 10074 | 28 | 47.30 | **1.689** | 36.30 | **1.297** |

These are **snapshot / if-the-pool-froze-now diagnostics**, not executable promises. Future sales dilute every already-purchased ticket until sales close or the pool sells out and the draw is moved forward.

## New candidate hierarchy

For further work, denominator hunting is no longer the bottleneck. Priority becomes final-sale monitoring + prize liquidation/tax validation.

1. **10067 — 3x1000-AZN gift coupons, 17% sold**. Largest visible headroom. Need coupon issuer, restrictions, transferability/resale and exact tax classification.
2. **10068 — refrigerator, 24% sold**. Strong headroom even under an 80% usable-value stress.
3. **10074 — TV OLED 55, 28% sold**. Strong 80%-usable headroom.
4. **10071 — iPad, 27% sold**. Still positive under 80%-usable stress at the current snapshot.
5. 10069 washer / 10066 Silver / 10064 Deep Blue / 10070 dishwasher are thinner and highly sensitive to liquidation value and further sales.
6. 10065 Cosmic and 10072 PS5 are already below break-even under the standing 100%-usable after-tax model at the displayed snapshot.
7. 10073 S25 is withheld from execution classification until the 0.5-vs-1.0 AZN transactional-price conflict is resolved.

## Free integer N

`N` remains free. If external sales froze at `M` and the user buys `N`, expected profit under a net prize pool `P` is approximately:

`EV_profit(N) = N*P/(M+N) - p*N`

so the continuous interior optimum is:

`N* = sqrt(P*M/p) - M`

when positive. In reality, future external sales `F` must be included as `M+F`, which is why buying early is dangerous. The execution plan should monitor close to the sales deadline (or before an announced early sellout) and recompute `N` from the latest state rather than lock in a current-looking edge weeks early.

## NEXT ACTION

1. Resolve the **S25 transactional ticket price** by non-purchase checkout preview or browser network data. Do not buy merely to test.
2. Fully identify the **10067 coupon terms** (issuer/store, transferability, expiry, exclusions, tax treatment). This is now the strongest candidate.
3. Build/extend a live finite-pool calculator that accepts `(drawId, value, qty, p, C, sold%, haircut, tax)` and reports current implied ROI, break-even sold%, execution buffer, and free-integer-N optimum under future-sales scenarios.
4. Monitor current sold% near closing; do not treat current positive snapshot ROI as locked in.
