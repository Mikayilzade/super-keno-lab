# Phase 18CJ — user runtime total-cap breakthrough

Date: 2026-08-29 (Asia/Baku)

## Result

A live authenticated/rendered `1001 Sevinc` browser surface supplied by the user exposes the denominator field that the public crawler could not recover.

For `drawId=10065` (iPhone 17 Pro 256 GB Cosmic Orange):
- draw date: 16.09.2026
- ticket price: 1 AZN
- operator `Təxmini dəyər`: 3,200 AZN
- **`Biletlərin sayı`: 6,400 tickets**
- live parent-card `Satıldı`: **45%**
- sales start: 01.07.2026 12:00
- scheduled sales end: 16.09.2026 19:00
- scheduled draw: 16.09.2026 21:00; draw may be moved earlier if tickets sell out.

For `drawId=10064` (iPhone 17 Pro 256 GB Deep Blue):
- draw date: 16.09.2026
- ticket price: 1 AZN
- operator `Təxmini dəyər`: 3,200 AZN
- **`Biletlərin sayı`: 6,400 tickets**
- live parent-card `Satıldı`: **36%**

The same live parent surface shows, contemporaneously:
- `10065` Cosmic Orange: 45%
- `10064` Deep Blue: 36%
- `10066` Silver: **34%** (not yet modal-confirmed for total cap/value in this checkpoint)
- PlayStation 5 Slim 1 TB: 57%, 0.5 AZN
- `10072` Samsung Galaxy S25 Ultra Black: 44%, 0.5 AZN
- 1000-AZN electronics gift coupon: 17%, 0.5 AZN
- iPad Air 13-inch (M2) Starlight 128GB: 27%
- Samsung refrigerator: 24%
- Samsung washing machine: 33%

## Why this matters

The principal denominator blocker is now broken for at least two current draws: `Biletlərin sayı` is the explicit total ticket target/cap `C`.

For the two confirmed iPhone draws, `C = 6,400` exactly. Therefore current sold ticket count `M` can be bounded directly from the displayed integer sold percentage without recovering an absolute remaining count.

Using the standing property-prize model

`V_economic = h*V - 0.14*(V-p)`

with `V=3200`, `p=1`, tax component = 447.86 AZN:
- full-value after-tax economic prize = 2,752.14 AZN;
- full-value break-even final sold fraction = 2,752.14 / 6,400 = **43.0022%**.

At the simple point estimates implied by the displayed percentages (before rounding uncertainty and future dilution):
- Cosmic 45% -> M≈2,880 -> ROI≈0.9556 even at h=1.00: already negative under the standing tax model;
- Deep Blue 36% -> M≈2,304 -> ROI≈1.1945 at h=1.00, but requires roughly >=86% realization of the 3,200-AZN operator value before tax to remain break-even at the current point estimate;
- Silver 34% would be M≈2,176 if `C=6,400` is independently modal-confirmed; at h=1.00 point-estimate ROI would be ≈1.2648, and break-even realization would be about 82% of operator value before tax. **Do not treat this as execution-grade until Silver's modal independently confirms its `Biletlərin sayı` and value.**

Useful final-sold break-even percentages for the 3,200-AZN / 1-AZN / C=6,400 structure under the standing model:
- h=1.00 -> 43.00%
- h=0.95 -> 40.50%
- h=0.90 -> 38.00%
- h=0.85 -> 35.50%
- h=0.82 -> 34.00%
- h=0.80 -> 33.00%
- h=0.70 -> 28.00%
- h=0.60 -> 23.00%

These are **final sold fractions**, not a lock-in at purchase time. Later ticket sales dilute any ticket bought now. Because current draw sales continue until 16 Sep unless the pool sells out earlier, present positive point-estimate EV does not by itself make a purchase executable.

## Immediate next action

1. Use the same live info modal to capture `Təxmini dəyər` + `Biletlərin sayı` for **10066 Silver** first.
2. Then capture the same two fields for **10072 S25**, **1000-AZN coupon**, **iPad Air**, and ideally all 11 current draws.
3. Build a single current-cycle table `(drawId, prize, price, C, sold%, V_operator, timestamp)` and rank every draw under tax + liquidation haircuts.
4. Once Silver is confirmed, replace the old denominator-recovery search priority with final-sell monitoring / execution-threshold analysis. Preserve N as a free integer.
5. Do not buy solely from the current percentage; model percentage rounding and future sales through the actual close/draw timing.
