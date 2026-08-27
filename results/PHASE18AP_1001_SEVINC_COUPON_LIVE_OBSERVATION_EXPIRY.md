# Phase 18AP — 1001 Sevinc coupon live-observation expiry

Date: 2026-08-27

Status: **MEANINGFUL DATA-INTEGRITY CORRECTION; COUPON 17% IS NO LONGER TREATED AS A LIVE EXECUTION INPUT.**

## Goal

Continue the highest-priority `1001 Sevinc` task: bind the current 1000-AZN gift coupon to one exact live draw record:

`(drawId, prize, ticket price, draw date, sold%, timestamp)`

and recover absolute cap / remaining if possible.

## Fresh first-party snapshot

Fresh 27-Aug-2026 crawl of the official `1001 Sevinc` surface still shows the current draw set:
- 11 draws;
- all dated 16.09.2026;
- 3 cards at 1 AZN;
- 8 cards at 0.5 AZN.

Fresh indexed `tirajlar` content currently exposes at least:
- `iPhone 17 Pro 256 GB Cosmic Orange`;
- ticket price 1 AZN;
- draw date 16.09.2026;
- `Satıldı: 43%`.

Official sources:
- https://www.azerlotereya.com/lotereya/1001-sevinc
- https://www.azerlotereya.com/lotereya/1001-sevinc/tirajlar

## Coupon re-observation attempt

Targeted fresh searches were run for combinations of:
- `1000 AZN hədiyyə kuponu`;
- `Satıldı: 17%`;
- `0.5 AZN` / `1 AZN`;
- draw date `16.09.2026`;
- current `1001 Sevinc`.

No fresh first-party indexed result reproduced a current coupon card with price + sold percentage + draw date in one observation.

The only coupon-related indexed material surfaced in the pass was historical / prior-cycle material and therefore cannot be bound to the current 16.09.2026 draw set.

## Data-integrity decision

The previously recovered `1000-AZN gift coupon — 17% sold` observation is retained as a historical snapshot in project notes, but **must not be used as a current live ROI input until re-observed**.

This means the former cap ceilings based on `sold = 17%` are now diagnostic only, not executable thresholds.

The same rule already used for ticket price is extended to sold percentage:

> A sell-through percentage is execution-valid only when prize + ticket price + draw date + timestamp are freshly co-observed or otherwise bound to one exact current drawId.

## What remains valid today

The Cosmic Orange observation is still reproducible on the fresh official index:
- prize: iPhone 17 Pro 256 GB Cosmic Orange;
- price: 1 AZN;
- draw date: 16.09.2026;
- sold: 43%.

Its exact drawId and absolute cap/remaining remain unresolved.

## Consequence for priorities

1. Do **not** spend further effort calculating coupon ROI from 17% until a fresh current coupon card is recovered.
2. Recover coupon prize→drawId→price→sold% as a single live record first.
3. In parallel, Cosmic Orange becomes the best currently reproducible finite-pool observation for an absolute denominator search.
4. Any cap / remaining observation must still be tied to exact drawId before a +EV claim.

## Result

No positive-EV opportunity is promoted in this batch.

The useful result is preventing a false live-EV conclusion from an expired/unreproducible sell-through snapshot. The finite-pool route remains open because the official client is known to expose remaining-ticket information operationally, but the crawler still does not reveal the absolute denominator.
