# PHASE 18CF — remaining-count semantics and cap inversion

Date: 2026-08-29

## Goal

Advance the `1001 Sevinc` denominator route without repeating bounded exact-ID / mirror / Telemetr searches. The batch targeted a different question: **what exactly does the official remaining-ticket field mean, and how much denominator information can be recovered from it once a numeric screenshot/card is obtained?**

## New first-party evidence

The current official `1001 Sevinc` explainer states that users can see **how many tickets remain for the draw to take place** (`tirajın keçirilməsi üçün neçə bilet qaldığını`) in the Azerlotereya.com / Misli.az `1001 Sevinc` section.

The same first-party explainer states that ticket sales stop either:

1. one day before the pre-announced draw date, or
2. when ticket sales reach the **specified number** (`bilet satışı təyin olunmuş saya çatdıqda`).

The current official product page also states that if tickets are sold earlier than the scheduled time and more than 7 business days remain until the draw, the draw date may be moved forward after notice.

Sources:
- https://www.azerlotereya.com/bloq/1001-sevinc-al-qazan-lotereyaya-neca-qosulmaq-olar-23
- https://www.azerlotereya.com/lotereya/1001-sevinc

## Interpretation advanced in this phase

This materially tightens the denominator model. The displayed remaining-ticket count is not best interpreted as a vague site-stock indicator. First-party wording links it directly to the **specified ticket target for that prize-category draw**.

Define:

- `C` = specified ticket count / target pool cap for the prize-category draw,
- `M` = tickets already sold/issued into that draw,
- `R` = exact displayed tickets remaining for the draw to reach the specified number.

Then the operative identity is:

`C = M + R`

and therefore:

`M = C - R`.

If a product card simultaneously exposes an integer sold percentage `p` and exact `R`, then `C` can often be solved or narrowed sharply even if `p` is rounded/truncated.

A dedicated solver was added:

`scripts/phase18cf_remaining_plus_percent_cap_solver.py`

It enumerates integer caps compatible with an exact `R` and displayed integer sold percentage under round/floor/ceil display assumptions.

## Why this matters for current target #1

For `10066 Silver`, a first-party sold percentage of **33%** is already preserved in project state. Therefore the next successful artifact does **not necessarily need to show total/cap**. A clean screenshot/card exposing only the absolute `R = tickets remaining` for that same drawId-bound card can be enough to recover/narrow the denominator.

This changes the priority field list from:

`total / cap / soldCount / stock`

to:

`remaining` **OR** `total/cap/soldCount`, with `remaining` now equally high-value when paired with the already-bound sold%.

Do not combine observations unless they are bound to the same `(drawId, prize, ticket price, draw period)` and close enough in time that no intervening sales make the pair invalid. Prefer one screenshot/card containing both values; otherwise timestamp both observations and treat sequential sales explicitly.

## Current result

- No absolute `R` for `10066` or `10072` recovered in this batch.
- Denominator recovery is nevertheless materially simplified: an exact current **remaining count alone**, if drawId-bound and contemporaneous with sold%, is sufficient input for integer cap inversion.
- Generic exact-ID search, APK mirror guessing, `endir`, Telemetr empty keywords, and ticket-checker guessing were not reopened.
- Super Keno portfolio size **N remains a free integer variable**.

## NEXT ACTION

Target rendered/current `10066 Silver` product-card evidence specifically for the phrase/value corresponding to **tickets remaining for the draw** (`tirajın keçirilməsi üçün ... bilet qalıb` / equivalent UI label). Prefer a single artifact carrying both the 33% progress and absolute remaining count. If `R` is recovered, immediately run the Phase 18CF solver across plausible percent-display rules, compute `C`, `M`, prize ROI, execution buffer, and the maximum positive-EV purchase size while preserving free integer N.
