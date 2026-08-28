# PHASE 18BR — 1001 Sevinc Trendyol account surface

Date: 2026-08-28

## Result

Not yet success: no absolute `remaining`, `total`, issuance count, or exact cap was recovered for current draw `10066 Silver` or `10072 S25`.

This batch did identify a materially different account/rendered surface that was not yet represented in the denominator-route hierarchy: **Trendyol Azerbaijan is an official e-commerce sub-distributor for 1001 Sevinc, and purchased 1001 Sevinc tickets have their own account/order surface inside Trendyol.**

## New evidence

A December-2025 partnership announcement reproduced by multiple Azerbaijani outlets states that Trendyol became an official e-commerce sub-distributor of Azərlotereya. Customers can buy `1001 Sevinc` tickets from the Trendyol main banner or from `Sifarişlərim / My Orders -> 1001 Sevinc`.

More importantly for this project, the same announcement explicitly says the Trendyol account surface exposes information on purchased tickets including:

- ticket status;
- draw date;
- lottery result.

That makes Trendyol a distinct **authenticated account/rendered ticket surface**, separate from Azerlotereya.com, Misli.az, and retail/POS artifacts.

Searches for indexed public screenshots/text containing `remaining`, `total`, ticket count, issuance count, chance-range, or current draw IDs `10066` / `10072` did not recover an absolute denominator in this batch. Public search results only expose the partnership/account capabilities, not the authenticated ticket card payload itself.

## Why this matters

The strongest current denominator lead is account-side data because Azerlotereya's own explainer already indicates that client/account surfaces can expose how many tickets remain until a draw. Trendyol is now proven to maintain a second authenticated representation of the same purchased-ticket object/status lifecycle.

A second implementation surface can be useful even if the primary Azerlotereya detail page remains a client shell, because its order/ticket model may expose fields or network payloads omitted from public pages.

This is materially new evidence, so this branch is opened; it is not a reopening of the rejected generic web-card crawl.

## Boundaries

- No denominator is inferred from ticket/chance IDs.
- No claim is made that Trendyol currently displays `remaining` or `total`; only that it maintains a dedicated authenticated 1001 Sevinc ticket/status surface.
- No paid ticket probe is authorized or performed.
- Denominator scope remains `(drawId, prize category, draw period)`.
- Portfolio size `N` remains a free integer optimization variable.

## NEXT ACTION

1. Promote Trendyol `Sifarişlərim -> 1001 Sevinc` to the account-surface search hierarchy alongside Azerlotereya/Misli.
2. Seek materially new screenshots, help content, cached app payloads, or public technical artifacts exposing the actual Trendyol 1001 Sevinc ticket-card fields; useful targets are `remaining`, `total`, issuance count, inventory/stock, sold count, or a directly interpretable finite range.
3. Keep `10066 Silver` and `10072 S25` as the denominator targets; bind any observation to draw/category/date/source/time.
4. If an exact denominator appears, immediately compute buffered ROI at 60/70/80/100% usable prize value under the standing 14% property-prize tax model and keep `operational_integrity_status` separate.
5. Do not infer cap from chance-number namespace and do not perform paid probes autonomously.
