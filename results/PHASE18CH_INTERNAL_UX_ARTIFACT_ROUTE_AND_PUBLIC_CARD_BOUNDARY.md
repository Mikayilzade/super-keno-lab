# Phase 18CH — internal UX artifact route and public card boundary

Date: 2026-08-29

## Goal

Continue the highest-priority `10066 Silver` denominator recovery without repeating bounded generic exact-ID, Telemetr, direct-Telegram or mirror searches. Target a genuinely new rendered/product-design surface that could expose the field behind the visible sold-progress UI.

## New evidence

A previously unrecorded public LinkedIn post by **Zulfiyya Shikhaliyeva**, who identifies herself as one of the UX/UI designers of the live `1001 Sevinc` product, explicitly says the product was designed by her and Hasan Aliyev and names Azərlotereya Digital/QA contributors. The post contains a `1001 Sevinc` launch creative and two outbound `lnkd.in` links. This is materially different from operator marketing posts because it originates from a product-design contributor and therefore creates a new potential route to historical UI mockups/screenshots/design artifacts.

Public source:
- LinkedIn post: `https://tr.linkedin.com/posts/zulfiyya-shikhaliyeva-273a231b3_1001-sevincimizi-sizinl%C9%99-b%C3%B6l%C3%BC%C5%9Fm%C9%99k-ist%C9%99dik-activity-7336014796846227456-fOK9`
- Post text says the `1001 Sevinc` UX/UI was designed by Zulfiyya Shikhaliyeva and Hasan Aliyev.
- Two outbound short links are present: `https://lnkd.in/eDBMFtdj` and `https://lnkd.in/e9beCW9w`.

A matching Behance profile for Zulfiyya Shikhaliyeva is public and lists **Middle UX/UI Designer — Azərlotereya, Baku** as work experience. The currently indexed first page of her Behance portfolio does not contain a `1001 Sevinc` case study; page-2 retrieval timed out in this run, so the portfolio route is not yet exhausted.

Behance source:
- `https://www.behance.net/zulfiyyajsef94`

## Current first-party card boundary reconfirmed

The live first-party parent page was crawled today and still exposes 11 current draw cards dated `16.09.2026`. Following card links resolves cleanly to current draw IDs including:
- card -> `drawId=10065`
- card -> `drawId=10066`
- card -> `drawId=10072`

But each direct draw URL still renders only the client shell to the public crawler; no absolute `remaining`, `total`, `soldCount`, stock or cap is present in crawler-visible text. Thus generic detail-page text extraction remains bounded.

## Negative probes in this batch

- Targeted web queries for `10066 Silver`, `33%`, `qalıb`, `satılıb` again produced no numeric denominator artifact.
- Search-engine probes for client field names (`remainingTickets`, `remainingCount`, `soldPercentage`, `ticketCount`, `maxTickets`) on `azerlotereya.com` returned no indexed API/schema hit.
- Direct raw HTML/JS acquisition from the execution container hit a transient DNS resolution failure, so no new bundle/API extraction was possible in this run.
- The LinkedIn short-link redirects are not directly fetchable through the current web fetcher; destination resolution remains open.

## Classification

`NEW_PRODUCT_DESIGN_ARTIFACT_ROUTE_NO_DENOMINATOR_YET`

This is a real phase advance because a new non-marketing, product-contributor surface is now identified. It should not be treated as proof of any denominator until an actual UI artifact is recovered.

## Implication for denominator recovery

A product-design screenshot/mockup may reveal the exact UI labels and field arrangement used for sold-progress / remaining-ticket information. Even if a historical mockup contains placeholder numbers rather than live data, exact field labels can materially narrow API/schema searches. A real launch/runtime screenshot with numbers could additionally constrain historical cap mechanics.

`N` remains a free integer optimization variable. No paid probe is authorized or performed.

## Next action

1. Resolve the two LinkedIn short links through a genuinely new redirect/cache/index surface; determine whether either points to a design case study, product prototype, Azerlotereya page or Misli page.
2. Continue the contributor-artifact route: inspect additional indexed Behance/Dribbble/portfolio pages for Zulfiyya Shikhaliyeva and Hasan Aliyev specifically for `1001 Sevinc` UI screenshots, progress bars, `remaining`, sold-percent or ticket-count labels.
3. If any exact field labels are recovered, immediately search those labels against Azerlotereya/Misli public web assets and runtime artifacts rather than broad guessing.
4. Keep `10066 Silver` exact `R` as the target. If a contemporaneous `R` is recovered, run `scripts/phase18cf_remaining_plus_percent_cap_solver.py` and compute compatible `C`, `M`, ROI, execution buffer and positive-EV purchase range with free integer `N`.
