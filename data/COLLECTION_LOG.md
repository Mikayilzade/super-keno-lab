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

## 2026-10-10 recovery/write check

- GitHub write access is working again.
- Added 2026-10-07 draw 26413 and 2026-10-08 draw 26414 to `data/super_keno_draws_part_005.csv`; both were cross-checked across independent result sources and pass structural validation.
- Added 2026-10-09 official draw 26415 to `data/super_keno_draws_part_005.csv`; official Azərlotereya numbers were independently corroborated by Misli. Numbers: 7, 10, 17, 18, 19, 20, 22, 33, 34, 36, 41, 43, 48, 51, 53, 55, 63, 64, 69, 70.
- Backfilled 2026-08-24 through 2026-08-27 in `data/super_keno_draws_part_004.csv`. 2026-08-24 matched LotteryGuru and Lucky Numbers; 2026-08-25..27 matched Eurooppalotto and LotteryGuru.
- Every added row contains exactly 20 unique integers in 1..70; no duplicate dates were inserted.
- Latest completed official Super Keno draw at check time is 2026-10-09 (26415). The 2026-10-10 daily draw has not yet occurred at this check time.
- Remaining priority historical gap: 2026-06-27 through 2026-07-09 inclusive. Wednesday dates remain valid candidate gaps because official Azərlotereya scheduling shows Super Keno on all seven weekdays.
- No source conflicts found in this run.

Sources checked:
- https://www.azerlotereya.com/lotereya-neticeleri
- https://www.misli.az/lotereya/super-keno/neticeler/
- https://azerbaijan.eurooppalotto.com/diger-lotereyalar/azerbaycan-super-keno-11717.html
- https://loteria.guru/resultados-loteria-azerbaiyan/az-super-keno/resultados-anteriores-super-keno-az
- https://lucky-numbers.ru/lottery/az/super-keno/trend-chart

## 2026-10-10 verification and completeness audit

- Added 0 draw rows. Latest official published result remains 2026-10-09, draw 26415 (checked before the next evening draw).
- Independent Statlotto result for 2026-06-22 (internal draw 1645) matches all 20 numbers already in part 003; the existing Belgium/Italy sources are mirrors of one publisher.
- Targeted searches of Statlotto, Eurooppalotto, LotteryGuru and official Azərlotereya did not expose complete trustworthy rows for 2026-06-27 through 2026-07-09. No conflicts found.
- Repository-wide audit: 247 distinct dates across five CSV parts; every row has 20 unique integers in 1..70 and no duplicate dates. Coverage is sparse outside the recent period. In 2026 through October 9 there are 96 calendar dates not yet recorded, including the 13-day June/July priority gap. The other missing blocks are Jan 1-Feb 12 (43), Feb 24-Mar 9 (14), Mar 18-26 (9), Mar 28 (1), Mar 30-31 (2), Apr 3 (1), Apr 17-23 (7), Apr 25-27 (3), and May 8-10 (3). These are collection gaps, not proof of completed draws.
- Statlotto archive exposes only recent rows freely, and attempted direct older-date pages did not return verifiable full results. Do not infer numbers from timestamps or draw IDs.

Sources checked:
- https://statlotto.com/lottery/az/super-keno/1782143100000
- https://statlotto.com/lottery/az/super-keno
- https://www.azerlotereya.com/lotereya-neticeleri
- https://eurooppalotto.be/andere-loterijen/azerbeidzjan-super-keno-11717.html
- https://lotteryguru.com/azerbaijan-lottery-results/az-super-keno/az-super-keno-results-history
