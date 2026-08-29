# Super Keno Lab — status

Last updated: 2026-08-29

## Phase

`PHASE 18CJ — external EV modifiers / 1001 Sevinc finite-pool execution`

## Core state

- Dedicated repo: `Mikayilzade/super-keno-lab`; broad `loto-research` remains separate.
- **195** validated Super Keno draws, 2022-12-21..2026-08-23.
- Portfolio size **N remains a free integer optimization variable**.
- Base-game fixed-list universal guarantee is mathematically impossible.
- History-based predictive branches are closed as primary edge sources after strict walk-forward/seed testing: hot/cold/pairs/context/mean-reversion, supervised per-number ranking, payoff regression, continuous structure, discrete regime/Markov.
- Exact after-tax 1x Super Keno expected cash-return ratio: **0.5918070335**.
- Base-game break-even modifier thresholds: direct cash-equivalent subsidy **40.82%**; one-wager bonus **68.97%**.

## Current conclusion

No fully verified **guaranteed-profit** or repeatable executable +EV Super Keno strategy is yet declared.

However, the major `1001 Sevinc` execution blocker changed materially on 2026-08-29: user-runtime product modals expose the absolute specified ticket count (`Biletlərin sayı`) for current draws. We no longer need to reverse-engineer the denominator from search/API guesses.

Canonical new evidence/checkpoint:

- `results/phase18cj_user_runtime_full_inventory_snapshot_2026-08-29.csv`
- `results/PHASE18CJ_USER_RUNTIME_FULL_INVENTORY_BREAKTHROUGH.md`

## Modifier state

- `10→10`: `official_status_conflict_conditional_positive`; conditional Super-Keno ROI **1.183614067** if operational/eligible. Main terms say through **31 Aug 23:59**, FAQ still says **31 Jul 23:59**. Do not stake solely for this without current account/support/UI confirmation.
- RadioArena promo: revisit only on materially new product-scope/account evidence.
- Misli APL Fantasy: free-entry bonus pattern exists but `Lotereya` eligibility/wagering/expiry/withdrawal remains unresolved.
- Oley Oley: historical only unless renewed; do not treat June–July 2026 evidence as current.

## 1001 Sevinc — current 16.09.2026 cycle

User-runtime screenshots now bind current draw IDs, operator-stated prize values, ticket quantities/caps, prize counts and sold percentages.

| drawId | prize | qty | stated value each | live card price | modal price | cap C | sold% |
|---:|---|---:|---:|---:|---:|---:|---:|
| 10065 | iPhone 17 Pro 256GB Cosmic Orange | 1 | 3200 | 1.0 | 1.0 | 6400 | 45 |
| 10064 | iPhone 17 Pro 256GB Deep Blue | 1 | 3200 | 1.0 | 1.0 | 6400 | 36 |
| 10066 | iPhone 17 Pro 256GB Silver | 1 | 3200 | 1.0 | 1.0 | 6400 | 34 |
| 10072 | PlayStation 5 Slim 1TB | 1 | 1200 | 0.5 | 0.5 | 4000 | 57 |
| 10073 | Samsung Galaxy S25 Ultra Black | 1 | 2500 | **0.5** | **1.0** | 8800 | 44 |
| 10067 | 1000-AZN gift coupon | 3 | 1000 | 0.5 | 0.5 | 12000 | 17 |
| 10071 | iPad Air 13-inch M2 128GB | 1 | 1500 | 0.5 | 0.5 | 6000 | 27 |
| 10068 | Samsung refrigerator | 1 | 1200 | 0.5 | 0.5 | 4800 | 24 |
| 10069 | Samsung washing machine | 1 | 700 | 0.5 | 0.5 | 2800 | 33 |
| 10070 | Samsung dishwasher | 1 | 765 | 0.5 | 0.5 | 3000 | 36 |
| 10074 | Samsung TV OLED 55 | 1 | 1100 | 0.5 | 0.5 | 4000 | 28 |

### Critical corrections

- Prior mapping `10072 -> S25` was wrong. **10072 is PS5; 10073 is S25**.
- S25 has a live UI price conflict: parent card shows **0.5 AZN**, detail modal says **1 manat**. Do not execute S25 until checkout/network confirms actual transactional price.
- Silver advanced from the previous 33% observation to **34%**.
- The old parent-page characterization `3 x 1 AZN + 8 x 0.5 AZN` is not enough to resolve S25 because its own card/modal conflict is explicit.

## Finite-pool economics

Standing working model for a non-cash/property prize:

`V_net_per_prize(h) = h*V - 0.14*(V-p)`

where `h` is the fraction of operator-stated value that is actually usable/liquidatable. For `q` prizes:

`Pool_net = q * V_net_per_prize`.

Break-even final sold share:

`S_BE = Pool_net / (p*C)`.

Snapshot diagnostics using current displayed sold% (future sales are NOT locked):

| draw | sold% | BE @100% usable | ROI-now @100% | BE @80% usable | ROI-now @80% |
|---|---:|---:|---:|---:|---:|
| 10065 Cosmic | 45 | 43.00 | 0.956 | 33.00 | 0.733 |
| 10064 Deep Blue | 36 | 43.00 | 1.195 | 33.00 | 0.917 |
| 10066 Silver | 34 | 43.00 | 1.265 | 33.00 | 0.971 |
| 10072 PS5 | 57 | 51.60 | 0.905 | 39.60 | 0.695 |
| 10073 S25 (`p=0.5` hypothesis only) | 44 | 48.87 | 1.111 | 37.50 | 0.852 |
| 10067 3x1000 coupon | 17 | 43.00 | **2.530** | 33.00 | **1.941** |
| 10071 iPad | 27 | 43.00 | **1.593** | 33.00 | **1.222** |
| 10068 refrigerator | 24 | 43.00 | **1.792** | 33.00 | **1.375** |
| 10069 washer | 33 | 43.00 | 1.303 | 33.01 | ~1.000 |
| 10070 dishwasher | 36 | 43.86 | 1.218 | 33.66 | 0.935 |
| 10074 TV OLED | 28 | 47.30 | **1.689** | 36.30 | **1.297** |

These are **if-the-pool-froze-now** expected-value diagnostics, not a guarantee and not a recommendation to buy now. Sales continue until the scheduled close or early sellout, so later external purchases dilute tickets bought earlier.

### Current candidate hierarchy

1. **10067 — 3x1000-AZN gift coupons, 17% sold.** Largest headroom. Must resolve coupon issuer/restrictions/transferability/expiry and exact tax classification.
2. **10068 — refrigerator, 24% sold.** Strong headroom even under 80% usable-value stress.
3. **10074 — TV OLED 55, 28% sold.** Strong 80%-usable headroom.
4. **10071 — iPad, 27% sold.** Still positive under 80%-usable stress at snapshot.
5. 10069 washer, 10066 Silver, 10064 Deep Blue, 10070 dishwasher are thinner and sensitive to resale value + future sales.
6. 10065 Cosmic and 10072 PS5 are already below break-even under the standing 100%-usable after-tax model at current displayed sold%.
7. 10073 S25 is withheld from execution classification until price conflict is resolved.

## Free integer N

`N` remains free. If external sales froze at `M` and net prize pool is `P`, approximate expected profit after buying `N` tickets is:

`EV_profit(N) = N*P/(M+N) - p*N`.

The continuous interior optimum is:

`N* = sqrt(P*M/p) - M`

when positive. Real execution must include future external sales `F`, replacing `M` with `M+F`. Therefore the rational research direction is near-close monitoring and scenario analysis, not early purchase based on today's percentage.

This finite-pool route seeks **positive expected value**, not deterministic guaranteed profit. Owning only some remaining tickets does not guarantee a prize.

## Operational risks already established

- Repeated category-level early sellouts occur; `execution_closure_risk` is real.
- A March-2026 incident caused some purchased tickets not to enter scheduled draws; `operational_integrity_status` remains required before any final execution claim.
- Historical chance IDs are namespaced/offset and cannot be used as sold counts.
- Generic public search, Telemetr/direct Telegram plaintext, Trendyol public search, exact-ID search, registration-DOCX search, APK mirror guesses and ticket-checker guessing are bounded absent materially new evidence.

## NEXT ACTION — Phase 18CJ+

1. **Resolve 10073 S25 actual transactional price** without making a purchase: use checkout preview or browser DevTools/network. The parent card says 0.5 AZN; modal says 1 AZN.
2. **Research 10067 coupon terms**: issuing electronics retailer, where it can be used, expiry, transferability, cash-equivalent/resale value, exclusions and tax classification. This is now candidate #1.
3. Build a reusable live finite-pool calculator/watchlist taking `(drawId, V, qty, p, C, sold%, haircut, tax)` and outputting current implied ROI, break-even sold%, remaining headroom, future-sales scenarios, and optimal integer `N`.
4. Monitor sold% close to sales end / early-sellout events; never treat today's snapshot edge as locked.
5. Revisit `10→10` only on materially new current-account/support/UI evidence resolving the 31-Aug/31-Jul conflict.
6. Do not reopen rejected draw-history prediction branches without materially new information.
