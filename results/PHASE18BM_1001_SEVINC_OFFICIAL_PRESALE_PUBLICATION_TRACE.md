# Phase 18BM — official 1001 Sevinc pre-sale publication trace

Date: 2026-08-28
Status: **not yet success** — denominator not recovered, but the §2.5 publication route was materially narrowed.

## Objective

Continue the Phase 18BL `NEXT ACTION`: locate the pre-sale/publication artifact for registration **316 / 12.05.2025**, determine whether it exposes the registered conditions or a ticket-count denominator, and avoid repeating exhausted generic media searches.

## New first-party evidence

A first-party Azərlotereya launch article was recovered:

- title: `“1001 Sevinc” əşya lotereyası başladı`
- publication date: **14/05/2025**
- registration date already bound on the current game page: **316 / 12.05.2025**
- therefore the official launch publication appeared **2 days after registration** and immediately before/at launch.

The article states the initial ticket-price/prize structure (1 / 2 / 5 AZN) and directs participants to the `1001 Sevinc` section to buy tickets.

Crucially, the launch article itself does **not** expose:

- total ticket quantity;
- ticket-number range;
- per-prize/per-draw cap;
- an attached PDF or other visible registered-conditions document;
- classification under the §2.2.5 sold-dependent-prize-fund exception.

## Link-resolution result

The launch article's `1001 Sevinc` link is a Bitly redirect. Following it resolves to the ordinary first-party game page:

`https://www.azerlotereya.com/lotereya/1001-sevinc?...`

The recovered crawler snapshot of that destination contains draw cards and general game rules, but no absolute ticket denominator or registered-conditions attachment.

This matters because it rules out the simplest interpretation of Phase 18BL: the §2.5 publication was **not** a launch article with an obvious downloadable registration package attached to it, at least on the currently recoverable first-party surface.

## External mirror check

Multiple 15 May 2025 media mirrors repeat substantially the same launch text. They add no ticket-count/range semantics and are therefore now treated as **exhausted mirrors**, not independent denominator evidence.

## Interpretation

The 14 May first-party launch article is the strongest candidate yet for the public announcement surrounding §2.5, but it is **not itself enough to prove that the full registered conditions were published there**. The law/registration route remains alive because:

1. registration 316 is still first-party bound;
2. current rules require registered conditions to be announced before sales;
3. the recovered announcement does not contain the denominator fields we need;
4. therefore the useful missing artifact is more likely an older version/static asset/hidden content endpoint of the first-party game page, a separately indexed conditions document, or the regulator/organizer-held registered package/amendment.

Do **not** infer ticket cap from wording such as `yüzlərlə hədiyyə`, nor from chance-number maxima.

## Research decision

Close the following as repetitive unless materially new evidence appears:

- generic May-2025 press mirrors of the launch announcement;
- reopening the same current launch article for denominator extraction;
- assuming the Bitly target itself is a conditions document.

Keep open and prioritize:

1. archived/static first-party `1001 Sevinc` page assets or older page versions around **12–15 May 2025**;
2. exact-file searches around registration `316`, including PDF/document/static-storage namespaces;
3. amendments/new editions that may state ticket quantity or category-level issuance limits;
4. materially new account/rendered/retail/POS artifacts with explicit total/remaining/range semantics.

## Free-N invariant

No portfolio-size restriction was introduced. **N remains a free integer optimization variable.**

## Outcome

**Not yet success.** No `C`, `R`, or exact sold-ticket count `M` was recovered, so no executable buffered +EV claim is made.

## NEXT ACTION

Run a targeted first-party archival/static-asset search for the May-2025 `1001 Sevinc` game page and registration-316 document namespace, looking specifically for PDF/document/storage URLs, old page payloads, ticket quantity/range fields, or amendments. If a quantity is found, determine its semantic scope (global/category/draw/batch) before binding it to `10066 Silver` or `10072 S25`.