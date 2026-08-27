# Phase 18AV — 1001 Sevinc public client/endpoint surface exhaustion

Date: 2026-08-27

Status: **NO ABSOLUTE DENOMINATOR RECOVERED; PUBLIC CLIENT/API-STRING SEARCH CLOSED UNTIL A NEW SURFACE APPEARS.**

## Target

Current execution target remains:

- drawId `10065`;
- iPhone 17 Pro 256 GB Cosmic Orange;
- ticket price 1 AZN;
- draw date 16.09.2026.

## Fresh first-party snapshot

A fresh Azerlotereya search/render surface on 2026-08-27 still exposes Cosmic Orange at **43% sold** for the 16.09.2026 draw.

Source:
- https://www.azerlotereya.com/lotereya/1001-sevinc/tirajlar

The same fresh index also exposes iPhone 17 Pro 256 GB Silver at **33% sold**, up from the previously recovered 32% snapshot. This confirms sell-through is continuing and reinforces that any possible finite-pool edge decays as tickets sell.

## Materially different surface attempted

The project had already exhausted ordinary `drawId + qalan/satildi` and registration-number searches. This batch specifically targeted the public client/API layer by searching for:

- `drawId` + Azerlotereya / 1001 Sevinc;
- `ticketCount`;
- `remainingTickets`;
- `soldCount` / `remaining`;
- `10065` + `qalan bilet`;
- exact current prize + `qalan`.

No indexed first-party endpoint, JSON payload, static bundle string or field exposing absolute cap/sold/remaining was recovered. The public detail page still renders as a client shell to the available crawler.

A direct local HTTP fetch was also attempted only as a technical route to inspect public script bundles; the execution environment had no DNS access to the external site, so it did not yield evidence and is **not** interpreted as an operator-side blocker.

## Important non-result

Do **not** infer denominator from:

- raw chance IDs;
- sold percentage alone;
- stale Misli percentage snapshots;
- current card ordering except where the drawId mapping was already separately established;
- any guessed round cap.

The true execution gate for drawId 10065 still requires one of:

1. total predetermined ticket cap `C`;
2. absolute sold count `M`;
3. cap `C` plus remaining `R` so `M=C-R`.

Until then, a positive-EV claim is not justified.

## Current economics unchanged

At 43% sold, 1 AZN ticket price, retail benchmark 3,289 AZN and the conservative 14% property-prize tax model, approximate break-even total-cap ceilings remain:

- 60% usable value: 3,519 tickets;
- 70% usable value: 4,284;
- 80% usable value: 5,049;
- 100% usable value: 6,578.

Practical execution should use resale/liquidation value rather than retail ceiling and an additional sell-through buffer, so the true actionable ceiling is lower.

## Decision

The repetitive public `10065 + remaining/cap/API-field` search is now closed unless a materially new rendered/account/client surface appears.

The next finite-pool batch should broaden horizontally rather than repeat this query: rebuild the **full current 11-prize table** for the 16.09.2026 cycle with fresh `prize + price + sold% + timestamp` observations where available, then rank candidates by break-even-cap tolerance under conservative net-value assumptions. A lower-sold, high-value 0.5-AZN prize may be a better target for denominator recovery than Cosmic Orange.

Super-Keno modifier scans continue only for genuinely new zero-cost/free-entry offers explicitly scoped to `Lotereya`; rejected draw-history prediction branches remain closed.
