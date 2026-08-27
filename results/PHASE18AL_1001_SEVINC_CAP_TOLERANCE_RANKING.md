# Phase 18AL — 1001 Sevinc live cap-tolerance ranking

Date: 2026-08-27

Status: **NO LIVE +EV CLAIM YET; ABSOLUTE CAP/REMAINING STILL MISSING. PRIORITY ORDER IMPROVED.**

## Objective

Use the current live `Satıldı%` observations together with current local retail/value benchmarks to rank which `1001 Sevinc` prize categories are most tolerant of a large predetermined ticket cap. This does **not** infer the cap. It only tells us where recovering the cap has the highest information value.

For a prize with net usable/resale value `V_net`, ticket price `p`, sold fraction `s`, and predetermined cap `C`, estimated sold tickets are `M = s*C` and single-ticket expected-value ratio is approximately:

`ROI = V_net / (p * s * C)`.

Therefore the maximum cap compatible with break-even is:

`C_break_even = V_net / (p * s)`.

The true cap must still be recovered from an explicit first-party/client/account surface before any +EV claim.

## Live observations used

Current first-party `1001 Sevinc` index snapshot (27 Aug 2026):
- iPhone 17 Pro 256 GB Cosmic Orange — ticket 1 AZN — draw 16.09.2026 — `Satıldı: 43%`.
- PlayStation 5 Slim 1 TB — ticket 0.5 AZN — draw 16.09.2026 — `Satıldı: 55%`.
- 1000-AZN gift coupon — ticket 0.5 AZN — draw 16.09.2026 — `Satıldı: 17%`.

First-party game/rules source:
- https://www.azerlotereya.com/lotereya/1001-sevinc
- https://www.azerlotereya.com/lotereya/1001-sevinc/tirajlar

The official 1001 Sevinc explainer confirms that the player can see how many tickets remain until a draw and that sales stop either at the scheduled cutoff or when the predetermined quantity is reached:
- https://www.azerlotereya.com/bloq/1001-sevinc-al-qazan-lotereyaya-neca-qosulmaq-olar-23

## Current value benchmarks

### iPhone 17 Pro 256 GB

Official Apple partner iSpace Azerbaijan currently lists iPhone 17 Pro 256 GB Deep Blue and Silver at **3,289 AZN**. The three current iPhone prize colors are the same model/storage, so 3,289 AZN is used as the retail benchmark for the Cosmic Orange cap-tolerance calculation.

Source:
- https://ispace.az/en/product/iphone-17-pro-256-gb-deep-blue-mg8j4zd-a

### PlayStation 5 Slim 1 TB

Kontakt currently lists PlayStation 5 Slim 1 TB at **1,449.99 AZN** cash price; Baku Electronics independently shows **1,449.99 AZN** for the same PS5 Slim Blue-Ray 1 TB model.

Sources:
- https://kontakt.az/playstation-5-slim-1tb
- https://www.bakuelectronics.az/mehsul/playstation-5-slim-blue-ray-201123

### 1000-AZN gift coupon

Face value is **1,000 AZN**. Because actual merchant restrictions/transferability are not yet bound to the current prize card, multiple value haircuts are retained rather than treating face value as guaranteed cash.

## Break-even cap ceilings

| prize | ticket | sold | retail/face benchmark | cap @60% net | cap @70% net | cap @80% net | cap @100% ceiling |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1000-AZN gift coupon | 0.5 | 17% | 1,000 | **7,059** | **8,235** | **9,412** | **11,765** |
| iPhone 17 Pro 256 GB Cosmic Orange | 1.0 | 43% | 3,289 | **4,589** | **5,354** | **6,119** | **7,649** |
| PlayStation 5 Slim 1 TB | 0.5 | 55% | 1,449.99 | **3,164** | **3,691** | **4,218** | **5,273** |

Rounded to the nearest whole ticket cap.

## Interpretation

### 1. The 1000-AZN coupon is currently the highest-priority denominator target

Despite its lower prize value than the iPhone, its combination of **0.5-AZN ticket price and only 17% sold** lets it tolerate the largest total cap. Even with a severe 40% haircut to face value (`V_net = 600 AZN`), break-even is still possible if the predetermined cap is below roughly **7.1k tickets**.

At an 80% usable-value assumption, the threshold is about **9.4k tickets**; at face value the ceiling is **11.8k**.

This is materially more forgiving than the current iPhone and PS5 cards. Therefore an absolute cap/remaining observation for the coupon now has the highest information value.

### 2. Cosmic Orange remains the strongest electronics target

At 43% sold and 1-AZN ticket price, the iPhone still permits a relatively high cap: about **4.6k tickets** even at only 60% net resale/usage value, rising to **6.1k** at 80% net value.

### 3. PS5 is less attractive despite the cheaper ticket

Its 0.5-AZN ticket helps, but **55% already sold** substantially reduces the cap ceiling. With 60% net value, the cap must be below only about **3.16k tickets**; even at full current retail value, below about **5.27k**.

This makes PS5 a lower-priority denominator target than the coupon and iPhone unless an explicit small cap is exposed.

## Additional first-party rule finding retained

The current official explainer explicitly says players can view **how many tickets remain until the draw** (`tirajın keçirilməsi üçün neçə bilet qaldığını görmək`). This is important because it confirms that an absolute remaining-count exists in the operator/client surface; failure of the public crawler to expose it is a rendering/access limitation rather than absence of the field.

## Decision

No purchase recommendation and no positive-EV classification is made in this phase. `Satıldı%` alone is insufficient.

Priority for denominator recovery is now:
1. **1000-AZN gift coupon**;
2. **iPhone 17 Pro 256 GB Cosmic Orange**;
3. PlayStation 5 Slim 1 TB;
4. other current categories only after their value/cap tolerance is comparable or an explicit denominator is surfaced.

A recovered cap should immediately be compared with the table above and then recalculated using exact current sold percentage, tax, resale/usage friction, and the exact prize terms.

## Next action

1. Target public/account/client artifacts containing `qalan bilet`, `neçə bilet qaldı`, or absolute remaining count for the **1000-AZN coupon first**.
2. Continue exact cap/remaining search for Cosmic Orange as second priority.
3. Re-snapshot sold percentages on a later date; do not reuse today's percentages after sales move.
4. If an absolute denominator appears, bind it to `(drawId, prize, ticket price, draw date, observed timestamp)` and calculate live ROI immediately.
