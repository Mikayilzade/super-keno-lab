# Phase 18AF — 1001 Sevinc current draw denominator surface audit

Date: 2026-08-27

Status: **NOT YET SUCCESS — absolute current denominator remains unresolved, but the public-surface failure mode is now identified precisely.**

## Goal

Target the current 16.09.2026 `1001 Sevinc` draws directly and recover at least one exact `cap`, `sold`, or `remaining` count keyed to the current draw ID.

## Current live draw set re-verified

The official `1001 Sevinc` page currently exposes 11 draw cards for 16.09.2026:
- three 1 AZN cards;
- eight 0.5 AZN cards.

Following those first-party card links resolves to the same current IDs already recorded in Phase 18AE:
- 1 AZN: `10065`, `10064`, `10066`;
- 0.5 AZN: `10072`, `10073`, `10067`, `10071`, `10068`, `10069`, `10070`, `10074`.

Official page:
- https://www.azerlotereya.com/lotereya/1001-sevinc

Current detail URLs use the form:
- `https://www.azerlotereya.com/lotereya/1001-sevinc/tirajlar?drawId=<ID>`

## Direct current-ID audit result

Each of the 11 current detail URLs was opened individually.

For all 11 IDs, the public HTML/search-crawler surface contains only the client shell:

`1001 Sevinc` → `Tirajlar` / `Biletlərim` / `Tiraj nəticələri`

It does **not** expose any of the following in the crawler-visible document:
- prize name;
- sold percentage;
- absolute sold ticket count;
- remaining ticket count;
- predetermined ticket cap.

The parent page also does not expose `Satıldı`, `Qalan`, or the draw IDs as rendered text; the IDs exist in the card links, while the sold/remaining state is evidently populated client-side.

Example first-party current detail pages:
- https://www.azerlotereya.com/lotereya/1001-sevinc/tirajlar?drawId=10064
- https://www.azerlotereya.com/lotereya/1001-sevinc/tirajlar?drawId=10065
- https://www.azerlotereya.com/lotereya/1001-sevinc/tirajlar?drawId=10066

Search-index queries combining current draw IDs with `Satıldı` / `Qalan` produced no indexed Azerlotereya payload containing absolute denominator data.

## Important interpretation

This is **not evidence that the denominator is secret or unavailable to users**. Prior official documentation says the site displays remaining-ticket information, and the game logic requires a predetermined finite ticket quantity.

It is evidence that the current denominator is **not server-rendered into the publicly crawlable HTML/search surface** for these current detail pages. It is likely loaded by the web client after page load and/or gated by an authenticated application call.

Therefore repeated generic search-engine queries against the same draw IDs are now a closed route unless a new indexed snippet/screenshot appears.

## Data-integrity rule retained

Never reuse a sold percentage from another cycle. Any future denominator observation is valid only as:

`(drawId, prize, ticket_price, draw_date, observed_timestamp, cap/sold/remaining)`.

## ROI trigger remains unchanged

If exact sold tickets `M` are recovered:

`ROI = V_net / (ticket_price * M)`

If cap `C` and remaining `R` are recovered:

`M = C - R`

and then apply the same ROI formula.

Do not call a draw +EV until prize identity, conservative net realizable value, and an absolute current denominator are all tied to the same draw ID.

## New next action

1. Stop routine search-index attempts for `10064..10074 + Satıldı/Qalan`; that surface is exhausted.
2. Target materially different public artifacts: newly indexed screenshots/social cards, result/winner images, cached client payloads, or first-party pages that render a remaining-ticket number outside the JS shell.
3. If any current screenshot exposes both prize identity and sold/remaining state, bind it to the exact draw ID before computing ROI.
4. In parallel, continue the main Phase-18 search for genuinely new zero-cost / promotional balances with explicit `Lotereya` eligibility.
5. Revisit the current draw pages only when a new first-party client-visible artifact or indexed payload becomes available.

No +EV classification is promoted in this checkpoint.
