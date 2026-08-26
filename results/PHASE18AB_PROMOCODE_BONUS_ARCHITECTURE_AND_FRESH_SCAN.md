# Phase 18AB — promo-code / bonus architecture + fresh zero-cost scan

Date: 2026-08-27

Status: **NO NEW EXECUTABLE +EV MODIFIER; PRODUCT-ELIGIBLE PROMO-BALANCE ARCHITECTURE CONFIRMED.**

## Purpose

This run deliberately avoided repeating exhausted APL winner-post, RadioArena generic-term, and 10→10 status searches. The goal was to scan for genuinely new current zero-cost/free-entry Lottery overlays and to determine whether the operator has a technically documented promotional-balance path that can be restricted/allowed by product category.

## Fresh current scan

Fresh searches across Misli/Azerlotereya and public partner/retail surfaces found no newly dated zero-cost/free-entry offer with explicit `Lotereya` / Super Keno eligibility on 2026-08-27.

The current public Azerlotereya homepage exposes logged-in account surfaces for both:
- `Bonus` balance; and
- a dedicated `Promokod` section.

Source snapshot:
- https://azerlotereya.com/

This is architectural evidence only; it does not establish that any currently circulating code credits a Lottery-eligible balance.

## Strong first-party proof that Lottery-eligible promotional balance exists

The official `10 oyna, 10 qazan` FAQ documents a promotional balance with explicit product scope:
- the additional 10 AZN can be used in `Lotereya`, `ePoz-Qazan`, and `Digital Oyunlar`;
- there is **no turnover requirement** for using the additional balance;
- winnings can be withdrawn without commission;
- the additional amount appears in the account balance surface.

Source:
- https://www.azerlotereya.com/faq/10oyna-10qazan

This matters even though 10→10 operational status remains conflicted: it proves that the operator's account/payment architecture supports a promotional credit that is explicitly usable on ordinary lottery products and can produce withdrawable winnings.

## Interpretation for current leads

### Misli APL Fantasy

Still:
`current_repeatable_free_entry_bonus_product_scope_unresolved`

The repeated 30/20/10 AZN awards are likely internal Misli account bonuses, but there is still no direct evidence that they instantiate the same Lottery-eligible balance type documented by Azerlotereya 10→10.

Do **not** infer eligibility merely because a generic bonus wallet exists.

### RadioArena

Still:
`current_terms_unresolved_sports_context`

The existence of a `Promokod` input surface confirms technical promo-code support, but it does not reveal RadioArena code product scope, wagering, expiry, award count, or withdrawal treatment.

### 10→10

No classification change in this run. The first-party FAQ is useful as architecture/product-scope proof, not as fresh operational-status evidence.

## EV implications

If a future zero-cost promotional credit is explicitly declared usable on 1x Super Keno and resulting winnings are withdrawable, its expected cash conversion remains:

`promo_credit × 0.5918070335`

Examples:
- 10 AZN free credit -> **5.9181 AZN** expected cash;
- 20 AZN -> **11.8361 AZN**;
- 30 AZN -> **17.7542 AZN**.

If the promotion instead requires own paid stake, use the existing modifier thresholds in `src/ev_modifiers.py`:
- direct cash-equivalent subsidy: ~40.82% of paid stake;
- one-wager bonus balance: ~68.97% of paid stake.

## Decision

No EV-ledger classification changes: no new executable offer was found.

However, the project can now treat **`explicit Lotereya-eligible promotional balance` as a proven operator capability**, not a hypothetical mechanism. Future scans should therefore prioritize exact wording such as:
- `Lotereya bölməsində istifadə oluna bilər`;
- `əlavə balans`;
- `dövriyyə şərti yoxdur`;
- bonus/promokod product-category labels visible in account UI.

Generic `bonus`, `promokod`, or `ürəyincə əylən` wording remains insufficient.

## Next action

1. Until APL round 3 is complete, prioritize newly dated offers that explicitly name `Lotereya` or expose a product-category label for credited bonus/promocode balance.
2. On a new APL winner/result artifact after round 3, inspect for any wallet/category text before repeating generic searches.
3. If any current free credit is proven Lottery-eligible, immediately run the variance-aware Super Keno conversion portfolio with **N free**.
4. Do not reopen draw-history predictive branches.
