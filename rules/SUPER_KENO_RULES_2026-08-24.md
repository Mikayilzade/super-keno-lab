# Azerbaijan Super Keno rules snapshot — 2026-08-24

This snapshot is the monetary reference for Phase 1 experiments. It must be versioned rather than silently changed if the official game changes.

## Official game mechanics

Source: Azərlotereya Super Keno game page, checked 2026-08-24:
https://www.azerlotereya.com/game/superkeno

- Select 10 numbers from 1..70.
- The draw produces 20 numbers.
- Winning match counts are 10, 9, 8, 7, 6, 5 and 1.
- Base ticket/variant price: **1 AZN**.
- Multipliers: **1x, 2x, 5x, 10x**; stake and stated prize scale with the chosen multiplier.
- The current registration shown on the official page is No. 285 / 07.01.2025, valid 10.01.2025–31.12.2027.

## Base payout table (1x)

| Hits | Gross payout AZN |
|---:|---:|
| 10 | 100,000 |
| 9 | 1,500 |
| 8 | 150 |
| 7 | 15 |
| 6 | 5 |
| 5 | 2 |
| 1 | 1 |
| 0,2,3,4 | 0 |

The official page also describes the 10x maximum as 1,000,000 AZN and states that the large prize is shared when there is more than one winning ticket. Phase 1 evaluates ordinary 1x tickets with the fixed base table. Jackpot-sharing/pool effects are explicitly **not yet modeled** and must be handled before any large real-money portfolio claim.

## Tax

Official Azərlotereya wording: 10% tax is withheld after subtracting the ticket price and a 500 AZN exempt amount from the winning amount.

Tax authority references checked 2026-08-24:
- https://www.taxes.gov.az/ru/page/suallar-ve-cavablar?page=45
- https://www.taxes.gov.az/az/post/1753

The code contains a configurable *ticket-wise* tax model. Phase 1 headline comparisons use gross payout minus ticket cost because tax aggregation across multiple variants/physical tickets must be operationally confirmed before it is treated as exact.

## Operational constraint worth testing later

Official FAQ checked 2026-08-24:
https://www.azerlotereya.com/faq/poz-qazan

- FAQ states a maximum of **125 tickets from each game room for one draw**.

The precise meaning of “each game room” and whether multiple channels/rooms can lawfully be combined into a larger portfolio must be established before an executable strategy above that limit is claimed.

## Sanity check only

Under the fixed base payout table and a symmetric 10-of-70 vs 20-of-70 model, the gross expected payout of one 1 AZN ticket is about **0.598556 AZN**. This is used only as a scorer sanity check, not as a reason to terminate empirical/non-mathematical research.
