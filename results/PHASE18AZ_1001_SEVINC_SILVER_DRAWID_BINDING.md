# Phase 18AZ — Silver drawId binding checkpoint

Date: 2026-08-28

Status: **MEANINGFUL PROGRESS — SILVER BOUND TO DRAWID 10066; ABSOLUTE DENOMINATOR STILL UNRESOLVED.**

## Result

The current first-party `1001 Sevinc` listing crawled on 2026-08-28 again reproduces the first three current 1-AZN iPhone cards in the current-cycle sequence. Search-cache text exposes `iPhone 17 Pro 256 GB Deep Blue` immediately followed by `iPhone 17 Pro 256 GB Silver`, with Silver at **33% sold**, all for the 16.09.2026 draw set.

Earlier in the same unchanged 16.09.2026 cycle, Phase 18AE recovered the clickable card/link order directly from the official parent page:

1. display card 1 -> `drawId=10065`
2. display card 2 -> `drawId=10064`
3. display card 3 -> `drawId=10066`

Phase 18AS already bound the first card to Cosmic Orange (`drawId=10065`) using the same display-order/link-order method. The current first-party listing continues to show the remaining two 1-AZN iPhone cards in sequence as Deep Blue then Silver. Therefore the current three-card binding is:

1. `drawId=10065` — iPhone 17 Pro 256 GB Cosmic Orange
2. `drawId=10064` — iPhone 17 Pro 256 GB Deep Blue
3. `drawId=10066` — iPhone 17 Pro 256 GB Silver

This is not an inference from a standalone search snippet: it combines the previously recovered official clickable-link order for the current draw cycle with the current first-party card-content order for that same cycle.

## Execution record promoted

Silver is now bound as:

`(drawId=10066, iPhone 17 Pro 256 GB Silver, 1 AZN, 16.09.2026, 33% sold, first-party Azerlotereya cache, observed 2026-08-28)`.

Deep Blue is correspondingly bound to `drawId=10064`, but today's snippet does not expose a fresh sold percentage for it, so it is not yet an execution-grade ROI input.

## Silver break-even cap tolerance

Using the standing approximate market-value input ~3,150 AZN, 14% property-prize tax model, 1-AZN ticket price and 33% sold:

- 60% usable/resale value: total cap must be below about **4,391 tickets**;
- 70%: below about **5,346**;
- 80%: below about **6,300**;
- 100%: below about **8,210**.

Silver therefore has materially better cap tolerance than bound Cosmic Orange at 43% sold and becomes the primary finite-pool denominator target.

## What remains missing

No public first-party artifact in this run exposed:
- predetermined total ticket cap `C`;
- absolute sold count `M`;
- absolute remaining count `R`.

Direct exact-URL searches for `drawId=10064` / `10066` and targeted searches for `10065 + qalan/remaining/Satıldı` did not reveal an indexed payload or denominator. The generic API/client-shell/registry/Trendyol/local-download paths remain closed as previously documented.

## Decision

Promote `drawId=10066 Silver` to finite-pool target #1 because it is now both bound and freshly lower-sold than Cosmic Orange.

Target hierarchy:
1. `drawId=10066` Silver — 1 AZN, 16.09.2026, 33% sold, fully bound;
2. `drawId=10065` Cosmic Orange — 1 AZN, 16.09.2026, 43% sold, fully bound;
3. `drawId=10064` Deep Blue — fully bound prize/price/date, fresh sold% unresolved;
4. unbound 0.5-AZN candidates only when a fresh complete current artifact appears.

Next action: seek absolute `cap / remaining / sold-count` specifically for `drawId=10066` through a materially different rendered/account/client artifact. If recovered, compute buffered live ROI immediately under 60/70/80/100% usable-value scenarios and the 14% property-prize tax model.
