# Phase 18AT — 1001 Sevinc cross-surface cache divergence

Date: 2026-08-27

Status: **NO EXECUTABLE +EV YET; LIVE DATA INTEGRITY RULE TIGHTENED.**

## Target

Current finite-pool target remains:

- drawId: **10065**
- prize: **iPhone 17 Pro 256 GB Cosmic Orange**
- ticket price: **1 AZN**
- draw date: **16.09.2026**

## Fresh cross-surface observation

On 2026-08-27 the first-party Azerlotereya search surface freshly crawled the current draw card and returned:

- Cosmic Orange
- 1 AZN
- draw date 16.09.2026
- **Satıldı: 43%**

A first-party Misli search surface for the same prize + same 1-AZN price + same 16.09.2026 draw date returned **Satıldı: 35%**, but its crawl timestamp is older (about three days).

This is not evidence for two separate ticket pools. It is evidence that public indexed surfaces can be asynchronously cached/stale.

## Execution integrity rule

From now on every sell-through observation must be keyed as:

`(drawId, prize, price, draw_date, sold_percent, source_surface, crawl_timestamp)`

Never:
- average sold% across surfaces;
- combine a newer price/date with an older sold%;
- interpret a lower stale Misli percentage as a live rollback;
- treat search-index crawl time as transaction time.

For execution-quality calculations, use the **freshest reproducible first-party observation** for the fully bound draw record. As of this checkpoint that is Azerlotereya at **43% sold**.

## Current cap ceilings at 43% sold

Using retail benchmark 3,289 AZN, 1-AZN ticket price and the conservative 14% property-prize tax model already established in prior phases, break-even total-cap ceilings remain approximately:

- 60% usable value: **3,519 tickets**
- 70% usable value: **4,284**
- 80% usable value: **5,049**
- 100% usable value: **6,578**

No cap / absolute remaining / absolute sold count was recovered in this batch, so these remain diagnostic ceilings, not an executable edge.

## New conclusion

The finite-pool route remains alive, but live `Satıldı%` is demonstrably cache-sensitive across operator surfaces. Any future denominator must be bound to the same draw and observation source/time before ROI is computed.

## Next action

1. Continue targeting **drawId=10065** for absolute cap / remaining / sold count through materially different rendered/account/client surfaces.
2. Re-snapshot Azerlotereya Cosmic Orange and expire 43% immediately if a newer bound value appears.
3. If cap/remaining is recovered, compute buffered live ROI under 60/70/80/100% usable-value scenarios and 14% tax.
4. Do not use the stale Misli 35% value for execution.