# Phase 18AN — 1001 Sevinc coupon price conflict and execution guard

Date: 2026-08-27

Status: **NO +EV CLAIM; PRICE/DRAW BINDING MUST BE RESOLVED BEFORE USING PRIOR CAP CEILINGS.**

## New evidence

A fresh official Azerlotereya Telegram/search surface currently exposes a `1000 AZN-lik Hədiyyə Kuponu` with ticket price **1 AZN**. This conflicts with the active project state, which had been carrying the current 16.09.2026 coupon as **0.5 AZN** together with a `Satıldı: 17%` observation.

Official-source evidence:
- https://t.me/s/Azerlotereya?before=2505
- https://t.me/s/Azerlotereya?before=2494

The official 1001 Sevinc explainer continues to state that users can see how many tickets remain until the draw, that ticket sales stop either one day before the scheduled draw or when the predetermined quantity is reached, and that prizes are property/non-cash prizes rather than cash payouts:
- https://www.azerlotereya.com/bloq/1001-sevinc-al-qazan-lotereyaya-neca-qosulmaq-olar-23

## Why this matters

For finite-pool ROI:

`ROI = V_net / (p * M)`

and when only cap `C` and sold fraction `s` are used:

`ROI ~= V_net / (p * s * C)`.

Therefore a ticket-price error from 0.5 AZN to 1 AZN halves the break-even cap ceiling.

Until the coupon's `(drawId, prize, price, draw date, sold%, observed timestamp)` are bound from a single current-cycle surface, prior Phase 18AM coupon ceilings are **diagnostic only and not execution-safe**.

## Conditional corrected ceilings if the same current coupon is 1 AZN and sold fraction is still 17%

Using the conservative property-prize tax model already established:

`V_economic = h*1000 - 0.14*(1000 - 1)`

with `s = 0.17`, `p = 1`:

| usable-value fraction h | V_economic AZN | break-even cap C |
|---:|---:|---:|
| 0.60 | 460.14 | **~2,707** |
| 0.70 | 560.14 | **~3,295** |
| 0.80 | 660.14 | **~3,883** |
| 1.00 | 860.14 | **~5,060** |

These values are conditional only. If the 17% observation belongs to a different 0.5-AZN coupon draw, the older thresholds remain mathematically relevant for that different draw but cannot be transferred to the 1-AZN coupon.

## Denominator search result this run

No first-party public search result exposing absolute `cap`, `remaining`, or `sold count` for the current 1000-AZN coupon was recovered. The official explainer confirms such remaining-ticket information exists in the client surface, but crawler-accessible pages still do not expose the absolute number.

## Decision

1. Do **not** use the prior 0.5-AZN coupon cap ceilings for staking decisions.
2. Highest priority is now to bind the current coupon's exact price and sold% to a specific drawId/date, then recover cap/remaining.
3. If price=1 AZN and sold%=17% are proven to belong to the same current draw, use the stricter ceilings above.
4. Continue property-prize tax treatment conservatively until coupon settlement/tax classification is explicitly proven otherwise.
