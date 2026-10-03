# Super Keno draw collection log

## 2026-10-03 collection run

- Added 35 validated draws in `data/super_keno_draws_part_005.csv`.
- Coverage added: 2026-08-28 through 2026-10-01 inclusive.
- Primary source: Magayo Azerbaijan Super Keno recent-results archive.
- Structural validation passed for every added row: exactly 20 unique integers, all in 1..70, no duplicate dates within the new shard.
- Independent web evidence (LotteryGuru statistics/current-result pages) confirms that draws continued daily through 2026-10-02 and corroborates many recent last-drawn dates, but its indexed page did not expose a complete per-date 20-number table suitable for row-by-row cross-check in this run.
- Deliberately not added: 2026-08-24..2026-08-27 (not recovered from a sufficiently reliable indexed source in this run); 2026-10-02 (Magayo page exposes the date but the 20 balls were image-only in the fetched text, so numbers were not guessed).
- Older known gap 2026-06-22..2026-07-09 remains unresolved.
- No conflicting candidate rows were written.

Sources checked:
- https://www.magayo.com/lotto/azerbaijan/super-keno-results/
- https://lotteryguru.com/azerbaijan-lottery-results/az-super-keno
- https://lotteryguru.com/azerbaijan-lottery-results/az-super-keno/az-super-keno-statistics
- Azerlotereya indexed/search results for official evidence.

## 2026-10-04 verification run

- Added 2026-10-02, official draw 26405, from the Azərlotereya official results page.
- Numbers: 8, 9, 10, 12, 13, 18, 21, 22, 25, 37, 38, 39, 46, 51, 52, 55, 58, 60, 61, 69.
- Structural validation: exactly 20 unique integers, all in 1..70.
- Official page gives date/time 2026-10-02 18:45 and draw number 26405.
- Searched again for 2026-08-24..2026-08-27 and 2026-06-22..2026-06-25; indexed search results did not yield trustworthy Azerbaijan Super Keno rows. A 2026-08-24 German Keno result was explicitly rejected as the wrong lottery.
- Remaining priority gaps: 2026-06-22..2026-07-09 and 2026-08-24..2026-08-27. No unverified rows added.

Sources checked:
- https://www.azerlotereya.com/lotereya-neticeleri
- https://www.azerlotereya.com/neticeler/super-keno
- targeted web searches for the unresolved June/August dates.
