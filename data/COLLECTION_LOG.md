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
