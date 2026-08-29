# Phase 18CD — current parent index + drawId indexability probe

Date: 2026-08-29

## Goal

Continue the highest-priority `1001 Sevinc` denominator route without reopening bounded APK/mirror/checker branches. Probe whether the freshly indexed first-party web surface leaks per-draw absolute denominator data or a search-indexable drawId/product-card route for the current candidates `10066 Silver` and `10072 S25 Ultra Black`.

`N` remains a free integer optimization variable.

## Fresh evidence

The first-party current parent page was freshly crawled and currently exposes **11 active draws**, all dated **16.09.2026**: three priced at 1 AZN and eight priced at 0.5 AZN. The indexed text contains price, countdown (`19 Gün`) and draw date, but does **not** expose prize name, sold percentage, sold count, remaining count, total issuance, stock, max tickets, or equivalent absolute denominator fields in the public index payload.

Source: https://www.azerlotereya.com/lotereya/1001-sevinc

A search-indexed historical route confirms the site does index URLs of the form:

`/lotereya/1001-sevinc/tirajlar?drawId=<id>`

Example indexed historical artifact: `drawId=10031`.

However, targeted exact searches for the current candidate identifiers/URLs produced **no relevant indexed first-party result** for:

- `drawId=10066`
- `drawId=10072`
- `10066 + 16.09.2026`
- `10072 + 16.09.2026`
- `Silver + 16.09.2026 + 1001 Sevinc`
- `S25 Ultra Black + 16.09.2026 + 1001 Sevinc`

Thus search-engine indexing currently exposes the live parent collection but not a denominator-bearing candidate detail document.

## Result

**Not yet success.** No absolute denominator was recovered for `10066` or `10072`.

This batch materially narrows the web-index route:

1. The current collection is demonstrably fresh and live at the 2026-08-29 snapshot.
2. Search indexing can preserve `drawId` routes historically, so the route family itself is real rather than speculative.
3. Current candidate IDs are not presently surfaced by exact indexed queries, and the fresh parent index strips the per-card fields needed for denominator recovery.
4. Therefore repeating generic exact-ID web searches has low expected value until a new cached/detail document, image, social preview, rendered card, account surface, or network artifact appears.

## Candidate state

- `10066 Silver`: remains denominator target #1; standing first-party sold observation = 33%; absolute `M/C/R` unresolved.
- `10072 S25 Ultra Black`: remains denominator target #2; drawId linkage retained; fresh sold% and absolute `M/C/R` unresolved.
- Draw date for the active collection remains 16.09.2026.

## Next action

Prioritize a **new rendered/card/network/POS artifact** rather than another generic search-index pass. Specifically:

1. Look for current screenshots/social previews/retail terminal or receipt artifacts where the card itself shows numeric `remaining`, `total`, or a progress numerator/denominator.
2. Look for a genuinely new first-party JS/runtime/API host or response artifact tied to the current parent page or Misli app; only resume APK acquisition if a new retrievable file/CDN/cache reference appears.
3. If sequential sold-% observations emerge for the same draw/category, immediately bind timestamps and run the Phase 18BG transition solver.
4. Do not infer cap from drawId, chance number, maximum observed serial, or product ordering.
