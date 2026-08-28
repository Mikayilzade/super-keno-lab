# Phase 18BC — S25 drawId binding + current-cycle coupon price resolution

Date: 2026-08-28

Status: **NO EXECUTABLE +EV YET; ONE 0.5-AZN PRIZE IS NOW DRAW-ID BOUND, AND THE CURRENT COUPON PRICE CONFLICT IS RESOLVED.**

## New evidence

A Misli search-cache snapshot for the current 16.09.2026 `1001 Sevinc` cycle (crawl age ~4 days at observation) exposes the card order:

- `iPhone 17 Pro 256 GB Silver` — 1 AZN — 16.09.2026;
- immediately followed by `Samsung Galaxy S25 Ultra Black` — 0.5 AZN — 16.09.2026.

Source surface:
- https://www.misli.az/lotereya/1001-sevinc/tirajlar

The current official Azerlotereya parent page independently still shows the cycle structure as exactly three 1-AZN cards followed by eight 0.5-AZN cards, all dated 16.09.2026.

The already recovered clickable draw-link order for this unchanged current cycle is:

1. 10065
2. 10064
3. 10066
4. 10072
5. 10073
6. 10067
7. 10071
8. 10068
9. 10069
10. 10070
11. 10074

The first three are already bound:
- 10065 = Cosmic Orange;
- 10064 = Deep Blue;
- 10066 = Silver.

Because S25 is the card immediately after Silver and is explicitly 0.5 AZN in the same current-cycle cache, it is the first 0.5-AZN card.

## New binding

**`drawId=10072` = Samsung Galaxy S25 Ultra Black — 0.5 AZN — 16.09.2026.**

This is a structural binding from current-cycle card order, not a guess from prize similarity.

The cached sold percentage previously observed for S25 (~41%) is **not promoted to live execution input** because that snapshot is several days old. A fresh complete first-party `(prize + price + sold% + date)` record is still required before live ROI evaluation.

## Coupon price conflict resolved for the current cycle

A separate Misli cache fragment from the same 16.09.2026 cycle exposes:

- `PlayStation 5 Slim 1 TB` — 0.5 AZN — 16.09.2026;
- followed by `1000 AZN-lik Hədiyyə Kuponu` — **0.5 AZN** — 16.09.2026.

Therefore the current-cycle 1000-AZN gift coupon ticket price is now safely resolved as **0.5 AZN**. The earlier 1-AZN evidence came from an older cycle and remains invalid for this cycle.

The coupon is **not yet drawId-bound**, and its old 17% sold observation remains expired; neither value is reused for execution.

## Candidate state after this phase

1. `10066 Silver` — fully bound, 1 AZN, fresh sold 33%; still execution target #1 because it has a fresh complete sold record.
2. `10072 S25 Ultra Black` — newly drawId-bound, 0.5 AZN; potentially stronger economics, but current sold% must be freshly reacquired before promotion.
3. `10065 Cosmic Orange` — bound, 1 AZN, last complete first-party sold 43%.
4. `10064 Deep Blue` — bound, 1 AZN, fresh sold% unresolved.
5. `1000-AZN gift coupon` — current price now resolved 0.5 AZN; drawId and fresh sold% unresolved.

## Decision

The decisive missing variable remains absolute `cap / remaining / sold-count`. However, `drawId=10072` is now a concrete second denominator target rather than an unbound prize name.

Do not use stale S25 ~41% or expired coupon 17% as current execution inputs.

## Next action

1. Reacquire a fresh complete first-party sold percentage for `drawId=10072 / S25 Ultra Black`. If materially below Silver's 33% or if its 0.5-AZN economics dominate after valuation, promote it to denominator target #1.
2. Seek absolute `cap / remaining / sold-count` for `10066` and `10072` only through materially new rendered/account/client surfaces.
3. Use the newly resolved 0.5-AZN coupon price, but reacquire its fresh sold% and bind its drawId before any ROI calculation.
4. Preserve free integer N and do not reopen rejected history-prediction branches.
