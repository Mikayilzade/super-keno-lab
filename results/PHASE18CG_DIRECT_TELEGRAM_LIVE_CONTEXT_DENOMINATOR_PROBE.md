# Phase 18CG — direct official Telegram live-context denominator probe

Date: 2026-08-29

## Goal

Follow Phase 18CF's highest-priority lead without reopening the already-bounded Telemetr keyword branch: look for a genuinely different, first-party social surface that could expose a rendered `1001 Sevinc` product card, exact remaining-ticket count, sold count, cap, or numerator/denominator for current draw `10066 Silver` (and secondarily `10072 S25 Ultra Black`).

`N` remains a free integer optimization variable.

## New surface tested

The public Telegram web viewer for the official `@Azerlotereya` channel was opened directly rather than through Telemetr/search snippets.

Relevant first-party surfaces:

- https://t.me/s/Azerlotereya
- current direct-context pages around message IDs in the 2535–2554 range
- current official parent page: https://www.azerlotereya.com/lotereya/1001-sevinc
- draw shells reconfirmed through the parent links:
  - `drawId=10066`
  - `drawId=10072`

## What the direct Telegram surface adds

1. The public Telegram viewer is currently crawlable and exposes official channel post text and message-level context, so it is a distinct recoverable surface from Telemetr.
2. It confirms that `1001 Sevinc` prize-list posts can expose exact prize names and ticket prices in plaintext when the operator chooses to write them into the post body. Example historical/current-context operator copy lists product names such as `iPhone 17 Pro 256 GB Deep Blue`, `Samsung Galaxy TAB S10+`, etc. alongside prices.
3. It also confirms that the official channel is active and current, so future prize-specific posts/media can be bound directly to message IDs instead of relying only on third-party indexing.

## Denominator result

No success yet.

The directly exposed plaintext/context inspected in this batch does **not** provide any of:

- exact remaining ticket count `R`;
- exact sold count `M`;
- total/cap `C`;
- stock/issuance/maxTickets equivalent;
- numerator/denominator pair;
- a text pairing of current `10066 Silver` with the preserved `33%` and an absolute count.

The current official parent page still exposes the 11 draw links/dates/prices, while `drawId=10066` and `drawId=10072` detail URLs remain client-shell pages to the crawler.

## Important boundary

Do **not** mechanically scan the same recent Telegram plaintext window again. The useful next Telegram trigger is a materially new message/media artifact that is specifically one of:

- `Silver` / `S25 Ultra Black` / another current 16.09.2026 prize named in operator text;
- an image or social preview visibly containing progress + remaining count;
- wording with an absolute number of tickets (`qalıb`, `bilet qalıb`, `satılıb`, `cəmi`, `ümumi`, etc. plus a number);
- a retail/POS screenshot reposted by the official channel;
- a message-level media URL that becomes directly retrievable and can be inspected visually.

This is a new surface result, but not denominator recovery.

## Evidence snapshot

- Official current parent page crawl (2026-08-29) shows 11 draws dated 16.09.2026, with 3 × 1 AZN and 8 × 0.5 AZN entries.
- Parent-page link traversal maps the relevant first entries to `drawId=10066`, `10072`, `10073`; detail pages still resolve as client shells.
- Official Telegram public viewer currently exposes active channel history and message IDs; a visible `1001 Sevinc` product-list post demonstrates plaintext prize+price publication, but no absolute ticket quantity.

## Decision

Classification: `NEW_FIRST_PARTY_SOCIAL_SURFACE_NO_DENOMINATOR_HIT`.

The denominator hypothesis is unchanged. For `10066 Silver`, an exact contemporaneous `R` is still enough to run the Phase 18CF cap inversion against the preserved 33% sold observation. No stale percentage/count combination should be merged without intervening-sales modeling.

## Next action

Keep `10066 Silver` denominator recovery as priority #1, but shift effort away from repeated Telegram plaintext queries. Prefer:

1. a genuinely new direct Telegram/media post or social preview containing a numeric remaining/sold field;
2. retail/POS terminal or receipt imagery with numeric stock/progress fields;
3. authenticated/runtime/network product-card evidence;
4. a new APK/CDN/file artifact only if it is genuinely retrievable and materially different from the already-bounded build-1361 routes.

If exact `R` is recovered, immediately run `scripts/phase18cf_remaining_plus_percent_cap_solver.py` under round/floor/ceil assumptions and compute compatible `C`, `M`, ROI, execution buffer and maximum positive-EV purchase size with `N` free.
