# Phase 17 — external EV modifiers / purchase-economics audit

Date: 2026-08-25

Status: **NO CURRENT PUBLICLY VERIFIED REPEATABLE EV MODIFIER FOUND; IMPORTANT BREAK-EVEN THRESHOLDS ESTABLISHED.**

This phase deliberately stops trying to predict the next draw. It asks whether purchase mechanics, bonuses, multipliers, tax, cashback or promotions can make the effective economics of an otherwise negative-EV Super Keno ticket positive.

## Official current baseline

Official Super Keno page checked 2026-08-25:
- base stake: 1 AZN;
- payout tiers: hit 1=1, 5=2, 6=5, 7=15, 8=150, 9=1500, 10=100000 AZN at 1x;
- multipliers: 1x / 2x / 5x / 10x scale stake and gross prize;
- tax: 10% of `(gross prize - ticket stake - 500 AZN)` when positive.

Source: https://www.azerlotereya.com/game/superkeno

Exact gross fair-distribution EV already proved in this repo:
- gross return per 1 AZN stake: **0.5985557942634199**.

Exact expected *after-ticketwise-tax cash* under current published tax formula:

| multiplier | expected cash per ticket | expected cash / stake |
|---:|---:|---:|
| 1x | 0.591807 | **0.591807** |
| 2x | 1.182532 | **0.591266** |
| 5x | 2.945178 | **0.589036** |
| 10x | 5.869825 | **0.586982** |

Conclusion: **1x is the best multiplier on after-tax EV.** Higher multipliers do not create edge; they slightly reduce expected cash-return ratio because more high-tier winnings become taxable.

## Subsidy / bonus thresholds

Let `e = 0.5918070335`, the expected cash returned per 1 AZN of 1x Super Keno stake after the published ticketwise tax formula.

### Cash-equivalent rebate that does not need wagering

If a promotion returns directly cashable value `B` after paid stake `W`, break-even requires:

`e*W + B >= W`

Therefore:

`B/W >= 1-e = 0.408193`

**Direct cash-equivalent subsidy threshold: ~40.82% of paid stake.**

### Bonus balance that must be wagered once

If paid stake `W` earns bonus balance `B`, and both paid stake and the full bonus are wagered once at the same 1x EV before winnings are withdrawn:

`e*(W+B) >= W`

Therefore:

`B/W >= 1/e - 1 = 0.689740`

**One-times-wager bonus threshold: ~68.97% of paid stake.**

A true 100% match, if fully usable on Super Keno and if resulting winnings are cash-withdrawable without extra friction, would have expected cash:

`2*e = 1.183614` per 1 AZN of personal outlay,

or about **+18.36% expected profit** before any account-specific fees/eligibility effects.

## Historical official proof-of-mechanism: 10 play / 10 bonus

Azerlotereya still exposes a page for a **past** campaign offering new users 10 AZN additional balance after depositing/playing at least 10 AZN. The page says:
- first 10,000 eligible new users;
- 10 AZN played -> 10 AZN additional balance;
- additional balance had no turnover requirement;
- unused deposited/additional balance withdrawal had a 30% fee with minimum 5 AZN;
- winnings withdrawal had no commission.

Sources:
- https://www.azerlotereya.com/kampaniya/10oyna-10qazan
- https://www.azerlotereya.com/game/10oyna-10qazan

This is **not treated as active on 2026-08-25**: the official current-campaign listing says `Cari kampaniya mövcud deyil` (no current campaign), while the 10/10 page is classified in search/indexing as a past campaign.

Current campaign listing:
- https://www.azerlotereya.com/kampaniyalar

Interpretation: the 10/10 structure demonstrates that external promotions *can* cross the mathematical break-even threshold, but this specific opportunity is not currently verified as playable.

## Cashback / payment-channel audit

No current official Azerlotereya campaign was listed publicly at the snapshot date.

A current Unibank cashback terms page explicitly excludes gambling/betting and lottery payments from cashback, so ordinary card cashback there cannot be counted as an EV subsidy.

Source:
- https://unibank.az/cards/cashback

Public searches did not produce a current Super-Keno-specific Misli/Azerlotereya bonus that can be safely included as repeatable value. Absence from public search is not proof that account-targeted promos/promocodes do not exist; account-specific offers must be evaluated only from their exact terms when observed.

## Other purchase mechanics

- Multi-draw purchase (same ticket for several consecutive draws) changes total price proportionally; no public discount is stated, so it does not alter per-stake EV.
- 2x/5x/10x multipliers scale gross payouts and cost together and are slightly worse after tax; no edge.
- The 125-ticket-per-game-room limit is operational, not an EV improvement.
- Ticket refunds are described only for cancelled games/technical problems; not a systematic arbitrage source.

## Decision

The `history -> next draw` prediction branch is closed as a primary route after Phase 16.

External economics is a valid qualitatively different route because sufficiently large rebates/bonuses can mathematically overturn the negative base EV. At the 2026-08-25 public snapshot, however, **no active repeatable public modifier meeting the threshold is verified**.

## Next action

1. Build an `EV modifier ledger` for any future promotion/bonus/promocode: eligibility, usable games, bonus/stake ratio, wagering count, withdrawal fees, expiry and max size.
2. Automatically calculate effective Super Keno EV using the exact after-tax base return and promotion terms.
3. Search non-prediction mechanisms next: cross-game promotional qualification, free-ticket/stimulating-lottery codes, account-targeted promos when terms are available, channel-specific price/reward differences, and any legal prize-pool overlays.
4. Separately test whether a promotion can be combined with a robust diversified ticket portfolio to reduce variance while retaining >1 expected personal-capital return.
5. Do not count leaderboard/tournament prize value unless participant count and prize distribution allow a defensible expected-value estimate.
6. Keep current-public and historical/inactive promotions strictly separated.
