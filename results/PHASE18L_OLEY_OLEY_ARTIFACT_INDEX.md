# Phase 18L — Oley Oley result-artifact index

Date: 2026-08-26

Status: **DENOMINATOR STILL UNRESOLVED; IMAGE-LEVEL TARGETS NOW IDENTIFIED.**

## Purpose

Phase 18K exhausted nearby public-text denominator searches. This batch moved to artifact discovery: identify exact official winner-result posts that may contain visible chance IDs / randomizer ranges in images even when search-index text does not expose them.

## Official result artifacts located

Misli's official Telegram feed points to the following Instagram winner-result posts:

| draw/week | official result artifact | source context |
|---|---|---|
| week 1 | `https://www.instagram.com/p/DZsnX2dCKZl/` | Telegram: `Oley Oley kampaniyasında birinci həftənin qazanan nömrələri artıq bəllidir` |
| week 2 | `https://www.instagram.com/p/DZ-kmE5CJAn/` | Telegram: `Oley Oley kampaniyasında ikinci həftənin qazanan nömrələri artıq bəllidir` |
| week 3 | `https://www.instagram.com/p/DaQwwaFiGbl/` | Telegram: `Oley Oley kampaniyasında üçüncü həftənin qazanan nömrələri bəlli oldu` |

Primary public feed snapshots:
- https://t.me/s/misliaz?before=4837
- https://t.me/s/misliaz?before=4865

These shortcodes are now the preferred targets for future image/cache/mirror retrieval. Do not spend future cycles rediscovering the same result-post URLs.

## New chronology evidence

The official feed around week 2 states again that:
- sports betting earns 1 chance per 5 AZN;
- Virtual Sport / ePoz-Qazan / Lottery earn 2 chances per 5 AZN.

The week-3 post states the same qualification rule and lists the remaining headline pool as:
- 1 Changan UNI-Z;
- 9 iPhone 17 Pro;
- 15 PlayStation 5;
- total 30,000 AZN bonus.

Week-3 draw itself had:
- 1 Changan UNI-Z;
- 3 iPhone 17 Pro;
- 5 PlayStation 5;
- 50 x 200 AZN bonus.

This is internally consistent with the already established six-draw campaign interpretation and with one car appearing at draw 3 plus one remaining after draw 3. It does **not** provide entry count and must not be used as denominator evidence.

## What remains unavailable

The current Misli campaign page is client-rendered and the public text fetch exposes no useful terms beyond the shell. Direct fetching of the week-3 Instagram result post was throttled during this run. Search-indexed Telegram text contains no winner chance numbers.

Therefore still unknown:
- total issued chances per draw;
- whether chance IDs reset weekly or accumulate;
- whether IDs are sequential from a known origin;
- randomizer upper/lower range;
- 200-AZN bonus wagering / withdrawal terms.

## Decision

Classification remains:

`current_super_keno_eligible_denominator_unresolved`

No staking decision is justified.

## Next action

1. Retrieve/cache/mirror the three known Instagram result artifacts by exact shortcode rather than broad text search.
2. Extract all visible winning chance IDs and their formatting from week 1/2/3 images.
3. Compare week-to-week number magnitude/prefix/length only to test reset-vs-accumulation hypotheses.
4. Search the corresponding official YouTube live/replay by exact draw date/title and inspect any visible randomizer range or announced total chances.
5. Do not infer denominator from max winner ID unless sequential issuance from a known origin is independently proven.
6. If a defensible draw-4 upper bound is below ~39,587 entries, promote immediately to positive-EV candidate under the conservative car-draw valuation.