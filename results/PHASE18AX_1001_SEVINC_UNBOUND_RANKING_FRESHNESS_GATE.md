# Phase 18AX — 1001 Sevinc unbound-ranking freshness gate

Date: 2026-08-27

Status: **NO +EV YET; UNBOUND iPAD/S25 PRIORITY DEMOTED UNTIL FRESH REPRODUCTION.**

## Purpose

Phase 18AW ranked several current-cycle prize observations by break-even cap tolerance and provisionally promoted iPad Air 13 M2 and Galaxy S25 Ultra above the fully bound Cosmic Orange draw. This batch attempted the required next step: reproduce each candidate on a fresh first-party surface and bind it to a current drawId.

## Fresh first-party result

The current Azerlotereya `1001 Sevinc` parent page still exposes 11 draws dated 16.09.2026: three at 1 AZN and eight at 0.5 AZN.

A fresh targeted search/open of first-party Azerlotereya surfaces on 2026-08-27 did **not** reproduce a complete current record for either:
- `iPad Air 13 M2` with 0.5-AZN price + sold% + 16.09.2026 date; or
- `Samsung Galaxy S25 Ultra` with 0.5-AZN price + sold% + 16.09.2026 date.

The crawler-visible draw-detail route remains a client shell and does not expose prize name, sold%, cap or remaining count.

By contrast, the current first-party search surface continues to expose current-cycle iPhone cards (including Silver at 33% in the current indexed snippet), and prior work has already fully bound Cosmic Orange to `drawId=10065`, 1 AZN, 16.09.2026, 43% sold.

## Data-integrity decision

The Phase-18AW iPad/S25 values remain useful **historical ranking observations**, but they are not execution-grade records until freshly reproduced and bound.

Therefore an unbound candidate may not outrank a fully bound candidate solely because an older search snapshot had a lower sold percentage.

New execution-priority rule:

1. `bound + fresh` candidate;
2. `fresh but unbound` candidate;
3. `unbound and not freshly reproducible` observation.

Under that rule, `drawId=10065` Cosmic Orange returns to **execution target #1**, not because its economics are intrinsically best, but because it is the strongest currently bound/reproducible target.

The iPad/S25 route is not rejected. It is promoted again immediately if a new first-party/current-cycle artifact reproduces `(prize, price, draw date, sold%, timestamp)` and allows drawId binding.

## Current denominator blocker

No absolute `cap`, `sold count`, or `remaining count` was recovered in this batch. Hence no finite-pool draw is promoted to positive EV.

For any recovered denominator:

`ROI = V_net / (ticket_price * sold_tickets)`

with the standing 14% property-prize tax model, resale/usable-value haircut, and an execution buffer for sales occurring after observation.

## Next action

1. Seek absolute denominator for fully bound `drawId=10065` only through a materially new rendered/account/client artifact; do not reopen exhausted generic API/registry/Trendyol routes.
2. In parallel, watch for a newly indexed first-party iPad/S25 card; if one appears, bind it and re-rank immediately.
3. Recover other current 0.5-AZN candidates only from fresh current-cycle artifacts.
4. Keep Super-Keno modifier scan restricted to genuinely new zero-cost/free-entry offers with explicit `Lotereya` scope.
