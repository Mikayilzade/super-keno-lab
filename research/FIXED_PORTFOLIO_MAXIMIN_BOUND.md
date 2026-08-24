# Fixed-portfolio maximin bound for Super Keno

Date: 2026-08-24

## Question

Can there exist a fixed portfolio of **N distinct 10-number tickets** whose total payout is greater than its total cost for **every possible** Super Keno draw of 20 numbers from 70?

Under the current snapshotted gross payout table and 1 AZN base ticket cost, the answer is **no**.

This is an exact combinatorial result, not a simulation.

## Per-ticket draw distribution

For any fixed 10-number ticket and a uniformly distributed 20-of-70 draw,

`P(K=k) = C(10,k) * C(60,20-k) / C(70,20)`,

where `K` is the number of matches.

Using the current gross payouts

- 0 -> 0
- 1 -> 1
- 2 -> 0
- 3 -> 0
- 4 -> 0
- 5 -> 2
- 6 -> 5
- 7 -> 15
- 8 -> 150
- 9 -> 1500
- 10 -> 100000

the exact expected gross payout of every fixed 1-AZN ticket is

`E[payout] = 0.5985557942634199 AZN`.

## Universal upper bound

Let a fixed portfolio contain N tickets and let `P(D)` be its total gross payout on draw D.

Every individual ticket has the same average payout over all `C(70,20)` possible draws. Therefore the portfolio average is

`average_D P(D) = N * 0.5985557942634199`.

The minimum can never exceed the average, so

`min_D P(D) / N <= 0.5985557942634199`.

Therefore **no fixed portfolio at any N can guarantee break-even (ratio 1.0), let alone positive profit, across every mathematically possible draw**.

This remains true for duplicated tickets. Multipliers 2x/5x/10x scale both stake and gross payouts linearly and do not change the ratio. Taxes can only reduce net return further.

## Bound is achievable

There are

`C(70,10) = 396,704,524,216`

distinct tickets.

If the portfolio contains **all** of them, symmetry makes the total payout identical for every possible 20-number draw. The constant gross payout is

`237,449,791,580 AZN`

on a cost of

`396,704,524,216 AZN`,

giving exactly

`237,449,791,580 / 396,704,524,216 = 0.5985557942634199`.

Hence the best possible universal fixed-portfolio guaranteed gross return ratio, when N is free, is **exactly 59.8555794263%**.

## Project consequence

The search target must distinguish two different problems:

1. **Universal fixed portfolio** — mathematically solved. Maximum guaranteed gross ratio is 0.5985557942634199; guaranteed positive profit is impossible under the current payout schedule.
2. **Real-draw / predictive process** — still open. A portfolio may outperform if ticket selection uses a genuine predictive bias or other information that changes the distribution of actual future draws away from uniform fair 20-of-70 behavior.

Historical fitting alone is not evidence of that second case.
