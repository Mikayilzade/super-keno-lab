# Phase 18AO — 1001 Sevinc coupon price stale-source correction

Date: 2026-08-27

Status: **IMPORTANT CORRECTION — CURRENT COUPON PRICE REMAINS UNRESOLVED.**

## What changed

Phase 18AN treated a search/social surface showing `1000 AZN hədiyyə kuponu` at **1 AZN** as fresh evidence potentially tied to the current 16.09.2026 cycle.

A targeted re-audit shows that this 1-AZN evidence is from an **older campaign cycle**, not the current cycle:

- the Misli Telegram/search artifact says `Cəmi 1 manata!` and lists `Hədiyyə kuponu 1000 AZN`, but the same post also lists **iPhone 16 Pro Max**, AirPods Max and states that all prizes would be added **by 18 July**;
- the current 16.09.2026 parent page instead exposes exactly **11 live draws: 3 at 1 AZN and 8 at 0.5 AZN**, but does not map prize names to those price slots in crawler-visible HTML;
- therefore the historical 1-AZN coupon post must not be used to price the current coupon with observed `Satıldı: 17%`.

## Execution consequence

The current 1000-AZN coupon record must be represented as:

- prize: `1000 AZN gift coupon`;
- draw date: `16.09.2026` only if the 17%-sold observation is independently bound to the current cycle;
- sold percentage: `17%` (current indexed observation already captured by prior phases);
- **ticket price: unresolved (0.5 or 1.0 AZN candidate until exact drawId/prize mapping is recovered)**;
- drawId: unresolved among current live IDs until prize mapping is proven;
- cap / remaining / sold count: unresolved.

Do not use the old July 1-AZN post as current price evidence.

## Break-even cap sensitivity at 17% sold

Using the conservative property-prize model from Phase 18AM:

`V_economic = h*1000 - 0.14*(1000-p)`

and `sold tickets ≈ 0.17*C`, break-even cap is `C < V_economic / (p*0.17)`.

### If current ticket price is 0.5 AZN

- 60% usable value: ~5,413 tickets
- 70% usable value: ~6,589
- 80% usable value: ~7,766
- 100% face value: ~10,119

### If current ticket price is 1.0 AZN

- 60% usable value: ~2,707 tickets
- 70% usable value: ~3,295
- 80% usable value: ~3,883
- 100% face value: ~5,060

These remain diagnostic only. No positive-EV execution claim is permitted until the exact current coupon is bound to one `(drawId, prize, price, sold%, draw date, timestamp)` tuple and an absolute denominator is recovered.

## Additional current-page fact

On 2026-08-27 the official Azerlotereya parent page still exposes the current 16.09.2026 cycle as:

- 3 draws at 1 AZN;
- 8 draws at 0.5 AZN.

Click-through mapping confirms the first three cards are draw IDs `10065, 10064, 10066`, followed by 0.5-AZN IDs beginning `10072, 10073, 10067...`, but client-rendered prize names remain absent from crawler-visible draw pages.

## Decision

Phase 18AN's `current coupon = 1 AZN` interpretation is **retracted**. The safer current state is `price unresolved`.

This is a meaningful correction because it prevents rejecting a potentially favorable 0.5-AZN finite-pool draw based on stale historical pricing, while also preventing the opposite error of assuming 0.5 AZN without proof.

## Next action

1. Recover exact current prize→drawId mapping, preferably from a fresh first-party rendered/social artifact or client payload.
2. Once the coupon drawId is known, bind its price directly from the current card slot.
3. Recover absolute cap / remaining for that exact draw.
4. Compute live ROI under 60/70/80/100% value haircuts and the conservative tax model.
5. Continue to reject any observation that cannot be bound to the same current draw tuple.
