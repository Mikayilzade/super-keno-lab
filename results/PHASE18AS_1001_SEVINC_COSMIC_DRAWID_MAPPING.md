# Phase 18AS — Cosmic Orange drawId mapping checkpoint

Date: 2026-08-27

Status: **MEANINGFUL PROGRESS — COSMIC ORANGE MAPPED TO DRAWID 10065; ABSOLUTE DENOMINATOR STILL UNRESOLVED.**

## Result

The current first-party `1001 Sevinc` listing freshly reproduces the first visible current draw card as:

- prize: **iPhone 17 Pro 256 GB Cosmic Orange**;
- ticket price: **1 AZN**;
- draw date: **16.09.2026**;
- sold: **43%**.

Earlier in the same current 16.09.2026 cycle, Phase 18AE recovered the clickable draw-card order from the official parent page by following its current links:

1. `drawId=10065` — 1 AZN
2. `drawId=10064` — 1 AZN
3. `drawId=10066` — 1 AZN
4. `drawId=10072` — 0.5 AZN
5. `drawId=10073` — 0.5 AZN
6. `drawId=10067` — 0.5 AZN
7. `drawId=10071` — 0.5 AZN
8. `drawId=10068` — 0.5 AZN
9. `drawId=10069` — 0.5 AZN
10. `drawId=10070` — 0.5 AZN
11. `drawId=10074` — 0.5 AZN

Because the fresh first-party listing still renders Cosmic Orange as the first current card and the current first-card link was already recovered as `drawId=10065`, the bound execution record is now:

`(drawId=10065, iPhone 17 Pro 256 GB Cosmic Orange, 1 AZN, 16.09.2026, 43% sold, observed 2026-08-27)`.

This removes the prize→drawId ambiguity for the current primary finite-pool target.

## Fresh sell-through snapshot

The official Azerlotereya index still reports **43% sold** today. A cached first-party Misli snapshot for the same prize/price/date showed **34% sold** about three crawl-days earlier. No new percentage movement was observed in this run; the execution input remains 43%.

Do not infer that sales stopped: crawler timestamps are sparse observations and percentage display is coarse.

## What remains missing

The decisive variable is still the predetermined ticket cap / absolute sold / absolute remaining count for drawId `10065`.

Once one of these is recovered:

- `M = sold tickets`, or
- `M = C - R` from cap `C` and remaining `R`,

compute immediately:

`ROI = V_net / (1 AZN * M)`

using the existing 14% non-cash-prize tax model and 60/70/80/100% usable-value haircuts, plus an execution buffer for additional sell-through after observation.

At 43% sold and retail benchmark 3,289 AZN, the current break-even cap ceilings remain approximately:

- 60% usable value: **3,519** tickets;
- 70%: **4,284**;
- 80%: **5,049**;
- 100%: **6,578**.

## Decision

`drawId=10065` is now the canonical Cosmic Orange target. Future client/account/rendered-surface searches should target that exact drawId rather than the generic prize page.

No positive-EV claim is made until an absolute denominator is recovered.
