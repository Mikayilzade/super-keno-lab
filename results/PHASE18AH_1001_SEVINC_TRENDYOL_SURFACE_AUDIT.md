# Phase 18AH — 1001 Sevinc Trendyol surface audit

Date: 2026-08-27

Status: **NO CURRENT ABSOLUTE DENOMINATOR RECOVERED; TRENDYOL IS ACCOUNT-SCOPED, NOT A PUBLIC DENOMINATOR SURFACE.**

## Question

Can the materially different Trendyol sub-distributor surface expose the current `1001 Sevinc` ticket cap, sold count or remaining count for the live 16.09.2026 draws, avoiding the Azerlotereya public JS-shell blocker?

## Findings

Fresh search/crawl on 2026-08-27 confirms that Trendyol is an official e-commerce sub-distributor for `1001 Sevinc`. Public descriptions of the integration state that a Trendyol customer can enter via the `1001 Sevinc` banner / `Sifarişlərim` and can see **their purchased ticket's status, draw date and lottery results inside their Trendyol account**.

This is materially different from a public catalog/detail page, but the published description is account/ticket-centric. Fresh public search did **not** expose any current Trendyol page/card containing absolute `cap`, `sold`, `remaining`, or a sold percentage for the live 16.09.2026 draw set.

The official Azerlotereya parent page remains current and still shows 11 draws dated 16.09.2026 (3 at 1 AZN, 8 at 0.5 AZN), but it likewise does not server-render the absolute denominator in crawler-visible HTML.

## Decision

Do **not** treat Trendyol as a recovered denominator source. It is a valid independent purchase/status surface, but current evidence supports only per-account purchased-ticket status/results, not public inventory state.

Do not repeat generic `Trendyol + 1001 Sevinc + qalan/satildi` searches unless a newly indexed current card/screenshot appears.

## Data-integrity rules retained

- Never infer sold count from raw chance IDs; historical IDs contain an offset/namespace.
- Never attach a stale sold percentage from an older draw cycle to current draw IDs.
- Any future denominator observation must bind `(drawId, prize, ticket price, draw date, observed timestamp)`.
- Compute live ROI only after an absolute `M` sold count, or `C` cap and `R` remaining count, is tied to the same current draw.

## Next action

1. Pivot away from generic Trendyol search to newly indexed first-party/social screenshots and rendered cards for the current 16.09.2026 cycle.
2. Search for current prize names + `qalan bilet` / `satildi` rather than draw IDs alone, because screenshots/cards may omit internal IDs.
3. Continue fresh Super-Keno modifier scan only for genuinely new zero-cost offers explicitly naming `Lotereya` or exposing product-category scope.
4. After APL round 3 completes, inspect the next new Misli APL result artifact for wallet/category/standings evidence.
5. Preserve free integer N; no draw-history prediction branches are reopened.
