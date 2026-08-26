# Phase 18U — APL Fantasy Misli private-league denominator surface audit

Date: 2026-08-26

Status: **DENOMINATOR NOT RECOVERED; PUBLIC SEARCH SURFACE EXHAUSTED, CLIENT/API LAYER IDENTIFIED AS NEXT TARGET.**

## Objective

Continue the strongest live adjacent lead from `STATUS.md`: recover the participant/team count for the Misli APL Fantasy private league (`188533-FJA0T`) without substituting global APL Fantasy registrations.

## Fresh evidence

### 1. Misli confirms that its league results are public on the official APL Fantasy site

Current Misli posts for the first and second weeks repeat the same flow:
- join APL Fantasy;
- enter private-league code `188533-FJA0T`;
- winners are determined from Misli league results publicly shared on the official site;
- weekly prizes are 30 / 20 / 10 AZN bonus.

Source:
- https://t.me/s/misliaz

This matters because it implies a public standings object exists somewhere in the APL Fantasy client even though search engines do not expose it.

### 2. Exact-code and site-scoped search produced no standings/indexed league page

Queries for:
- `188533-FJA0T`;
- exact Misli league wording;
- `site:aplfantasy.az Misli`;
- `site:aplfantasy.az 188533`;
- `site:aplfantasy.az league/liqa`;

did not return a public indexed standings URL.

The root `https://aplfantasy.az/` currently exposes only an application shell/iframe to the crawler rather than rendered standings data.

Interpretation: routine text search is now exhausted for the denominator. The next useful technical target is the browser/app client data layer (public standings API, route payload, or rendered result artifact), not more keyword variations.

### 3. Platform scale changed rapidly; global population remains unusable as the Misli denominator

AFFA/Fanat reporting provides two useful snapshots:
- 2026-08-03: **3,700+ teams**, with *dozens of leagues* already created; the AFFA marketing representative explicitly named `CBC Sport` and `Misli` among the many leagues.
- by first-round reporting: **14,000+ users** on the overall APL Fantasy platform.

Sources:
- https://fanat.az/az/futbol/153778/ldquoapl-fantasyrdquo-de-nece-komanda-qeydiyyatdan-kecib-aciqlama/%22APL
- https://www.xitab24.az/news/apl-fantasy-de-ilk-turun-qalibi-mukafatlandirdi

Neither figure is a valid substitute for the Misli private-league count.

### 4. Private leagues can be much smaller than the global platform

Fanat.Az's separate current APL private league reports **500+ participants** in round 2 while the overall platform is already above ten thousand users.

Source:
- https://fanat.az/az/futbol/154629/quotfanataz-liqasiquotnda-2-ci-turun-qalibi-hemkarimiz-oldu/

This reinforces the earlier rule: private-league EV cannot be estimated from global registrations.

### 5. Platform implementation clue

The current APL Fantasy app is published by **FANTAKING INTERACTIVE SRL**, a provider whose products support public/private fantasy leagues. This is not evidence about the Misli league size, but it helps define the next technical surface: a Fantaking-hosted SPA/app standings data layer rather than a conventional indexable HTML table.

Sources:
- https://play.google.com/store/apps/details?id=az.affa.fantasy
- https://fantaking.it/custom-fantasy-games

## Decision

No exact or defensible bound for the Misli private-league denominator was recovered in this run.

Classification of the APL Fantasy lead remains:

`current_repeatable_free_entry_bonus_product_scope_unresolved`

No Super Keno EV is assigned because two independent execution gates are still unresolved:
1. Misli bonus `Lotereya` / Super Keno eligibility and withdrawal treatment;
2. Misli private-league participant/team count.

## Methodological closure

Do **not** spend further runs on ordinary search-engine variants for `188533-FJA0T`, `Misli APL Fantasy standings`, or site-scoped `aplfantasy.az` queries unless new indexed content appears.

## Next action

1. Target the public APL Fantasy **client/API standings layer** or a rendered league/result artifact that exposes total rows/team count for `188533-FJA0T`.
2. Search winner-result images/screenshots/comments for a visible ranking footer, page count, league name, or credited bonus-wallet type.
3. Continue fresh scans for live zero-cost offers with **explicit Lotereya eligibility**; these still outrank APL because they bypass the unresolved bonus-scope gate.
4. Preserve the Fanat.Az 500+ private-league observation only as a benchmark, never as a proxy for Misli.
5. Do not reopen draw-history prediction branches.
