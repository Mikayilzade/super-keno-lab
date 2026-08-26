# Phase 18P — current-surface and RadioArena recheck

Date: 2026-08-26

Status: **NO VERIFIED EXECUTABLE +EV MODIFIER FOUND; ONE PREVIOUS NEGATIVE STATUS SIGNAL WEAKENED.**

## Objective

Continue Phase 18 without reopening rejected draw-history branches. Recheck only genuinely current first-party surfaces for:
- new Lottery/Super-Keno-eligible overlays;
- materially new RadioArena promo-code terms;
- materially changed evidence around the 10→10 operational-status conflict.

## Fresh first-party findings

### Azerlotereya current-campaign index

A fresh crawl of `https://www.azerlotereya.com/kampaniyalar` on 2026-08-26 no longer exposes the earlier literal text `Cari kampaniya mövcud deyil` in the retrieved body. The page currently exposes the `Cari kampaniyalar / Keçmiş kampaniyalar / Kampaniya tarixçəsi` navigation but no rendered current campaign cards in the text snapshot.

Interpretation:
- this does **not** prove that 10→10 is active;
- it does weaken the earlier campaign-index negative signal, because the exact `no current campaign` text is no longer observable in the fresh page snapshot;
- the dedicated 10→10 first-party page still says registration/qualification through 31 Aug 23:59, first 10,000 eligible new users, and explicitly permits `Lotereya`, but remains classified as `keçmiş kampaniya` in page/search presentation.

Therefore 10→10 remains `official_status_conflict_conditional_positive`, but the evidence weights change slightly: dedicated live terms are now opposed mainly by past-campaign classification / stale FAQ rather than a currently observable explicit `no campaigns` sentence.

Execution gate is unchanged: no stake unless account UI, *2080 support, or a newly dated official current signal confirms eligibility.

### RadioArena 10-AZN promo code

Fresh first-party/public search again failed to locate terms resolving:
- eligible product(s);
- whether the promo code is sports-only or cross-product;
- whether `Lotereya` / Super Keno can consume the balance;
- wagering requirement;
- withdrawal rule;
- expiry;
- number of codes awarded.

The candidate remains `current_terms_unresolved_sports_context`; no EV may be booked into Super Keno until product scope is proven.

If a 10-AZN code were truly free, usable once on 1x Super Keno, and resulting winnings cash-withdrawable, its expected after-tax cash value would remain **5.918070335 AZN per awarded code**. This is a conditional diagnostic only.

### New current Lottery-eligible overlays

A fresh scan of current Azerlotereya/Misli-indexed material did not reveal a new public, repeatable, account-independent overlay that explicitly admits Super Keno and has enough terms for an EV calculation.

Recent `Sürətlə Qazan` remains historical (7-14 Aug 2026) and limited to 52 tagged digital/ePoz games, not Super Keno. `Şans Karvanı 2` is event/marketing activity with gifts but no defensible ticket-linked probability/prize mechanic in the public terms.

## Decision

- **No executable +EV modifier is promoted.**
- Keep RadioArena unresolved and secondary until terms materially improve.
- Keep 10→10 at `official_status_conflict_conditional_positive`; do not reclassify active merely because the current-index negative sentence disappeared.
- However, stop citing `Cari kampaniya mövcud deyil` as a fresh 2026-08-26 current-page fact unless a later crawl shows it again. Treat that evidence as an earlier snapshot, not a persistent current signal.

## Next action

1. Search for product-scope terms through first-party Misli promo-code/help/bonus rules rather than repeating the same RadioArena post search.
2. Scan newly dated Misli/Azerlotereya campaign/news/social material for explicit `Lotereya` qualification, free tickets, extra draws, or free balance.
3. Passively recheck 10→10 only when a materially new operational/current signal appears.
4. If any free-balance candidate is proven usable on Super Keno, compute exact cash EV first, then design variance-aware distinct tickets with **N free**.