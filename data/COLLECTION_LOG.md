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

## 2026-10-04 backfill write

- Added previously recovered Super Keno draws 2026-06-22 through 2026-06-26 to `data/super_keno_draws_part_003.csv`.
- Official draw numbers: 26261, 26262, 26263, 26264, 26265.
- 2026-06-22..2026-06-24 were cross-checked across Eurooppalotto Belgium and Italy and matched exactly.
- 2026-06-25..2026-06-26 are currently supported by the Eurooppalotto Belgium archive; both rows pass structural validation (20 unique integers, all 1..70), but a second independent source is still pending.
- No conflicts were found and no existing rows were overwritten.
- Remaining priority gaps are now 2026-06-27..2026-07-09 and 2026-08-24..2026-08-27.

Sources:
- https://eurooppalotto.be/andere-loterijen/azerbeidzjan-super-keno-11717.html
- https://eurooppalotto.it/altre-lotterie/azerbaijan-super-keno-11717.html

## 2026-10-04 schedule-gap correction

- Verified from the current Eurooppalotto Azerbaijan Super Keno pages that the published draw schedule is Monday, Tuesday, Thursday, Friday, Saturday and Sunday; Wednesday is not a scheduled draw day.
- Corrected the unresolved-gap interpretation accordingly: 2026-07-01, 2026-07-08 and 2026-08-26 are Wednesdays and should NOT be treated as missing draws.
- Remaining actual missing draw dates in the current target windows: 2026-06-27..2026-06-30, 2026-07-02..2026-07-07, 2026-07-09, and 2026-08-24, 2026-08-25, 2026-08-27.
- Checked Eurooppalotto Belgium/Italy current pages and targeted indexed searches. No trustworthy complete 20-number rows for those older dates were exposed in this run, so no draw row was fabricated or added.

Sources:
- https://eurooppalotto.be/andere-loterijen/azerbeidzjan-super-keno-11717.html
- https://eurooppalotto.it/altre-lotterie/azerbaijan-super-keno-11717.html

## 2026-10-05 verification run

- Confirmed that 2026-10-04 official draw 26407 is already present in `data/super_keno_draws_part_005.csv`; no duplicate row added.
- Official Azərlotereya current-results page confirms draw 26407 at 18:45 and the exact 20-number set already stored.
- LotteryGuru statistics independently show Super Keno activity in the target summer period (including dated signals on 2026-07-02 and a table extending through 2026-08-24), but the indexed statistics page does not expose complete 20-number rows for the unresolved dates. It was therefore used only as corroborating evidence, not to reconstruct draws.
- Targeted searches for 2026-06-27..2026-06-30, 2026-07-02..2026-07-07, 2026-07-09, and 2026-08-24, 2026-08-25, 2026-08-27 did not yield trustworthy complete 20-number candidate rows in this run.
- No conflicts found; no unverified numbers added.

Sources checked:
- https://www.azerlotereya.com/lotereya-neticeleri
- https://loteriaguru.com/azerbaijao-resultados-loteria/az-super-keno/az-super-keno-estatisticas
- targeted indexed searches for each unresolved date.



## 2026-10-05 schedule correction

- Corrected an earlier erroneous assumption that Wednesday dates were non-draw days. Official Azərlotereya material states Super Keno is held every day, and the official TV schedule lists Super Keno on all seven weekdays.
- Therefore 2026-07-01, 2026-07-08 and 2026-08-26 remain genuine unresolved candidate gaps and must not be excluded by weekday.
- Fresh searches did not recover complete trustworthy 20-number rows for the remaining June/July/August gaps, so no draw rows were added in this run.
- Current official results still show 2026-10-04 draw 26407 as the latest completed Super Keno draw; no newer completed draw was available at check time.
- No conflicts or existing draw rows were overwritten.

Sources checked:
- https://www.azerlotereya.com/lotereya-neticeleri
- https://www.azerlotereya.com/tv-yayimlari
- https://www.azerlotereya.com/xeberler/super-keno-lotereyaasinda-100-000-manat-uduldu-1905

