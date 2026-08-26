# Phase 18H — current `Oley Oley` overlay audit

Date: 2026-08-26

Status: **LIVE SUPER-KENO-COMPATIBLE OVERLAY VERIFIED; EV SIGN STILL UNRESOLVED BECAUSE TOTAL ENTRY DENOMINATOR AND BONUS CASH-VALUE ARE NOT PUBLICLY RESOLVED.**

## Why this matters

This is the strongest current lead found in Phase 18 because the official Misli material explicitly includes **Lotereya** among qualifying products.

Official Misli Telegram states that after joining the campaign:
- every **5 AZN** spent on sports betting earns **1 chance**;
- every **5 AZN** spent on other games — explicitly **Virtual İdman, ePoz-Qazan, Lotereya** — earns **2 chances**.

Super Keno is sold on Misli as a lottery product, so the campaign is directly relevant to Super Keno spend at the product-category level.

Sources:
- https://t.me/s/misliaz?before=4870
- https://www.misli.az/kampaniyalar/oley-oley

## Current prize structure

The official Misli post for the third draw states the weekly draw prizes:
- 1 x **Changan UNI-Z**;
- 3 x **iPhone 17 Pro**;
- 5 x **PlayStation 5**;
- 50 x **200 AZN bonus** = 10,000 AZN nominal bonus face value.

After the third-week winners were announced, Misli advertised remaining campaign prizes of:
- 1 Changan UNI-Z;
- 9 iPhone 17 Pro;
- 15 PlayStation 5;
- total 30,000 AZN bonus.

That remaining inventory is exactly three copies of the weekly prize ladder, strongly indicating **three weekly draws remain** at this snapshot, subject to the campaign rules page/app state.

Official source:
- https://t.me/s/misliaz?q=%23Kampaniya

## Super Keno break-even math

Exact 1x Super Keno after-tax expected cash-return ratio from Phase 17:

`e = 0.5918070335`

For 5 AZN of personal Super Keno stake:
- expected base cash = `5 * e = 2.9590351675 AZN`;
- expected shortfall to break-even = `5 - 2.9590351675 = 2.0409648325 AZN`.

The Oley Oley overlay grants **2 entries** for that 5 AZN spend. Therefore the overlay must contribute at least:

`2.0409648325 / 2 = 1.02048241625 AZN expected value per campaign entry`

to lift the combined expected personal-capital return to 1.0.

### Nominal 10,000-AZN bonus-pool diagnostic

If the 50 x 200-AZN weekly bonuses were worth their full 10,000 AZN face value in withdrawable cash-equivalent EV, ignoring all car/iPhone/PS5 value, a weekly equal-entry pool would cross break-even whenever:

`10000 / total_entries >= 1.02048241625`

so:

`total_entries <= ~9,799`.

This is **not yet a valid positive-EV claim** because the prizes are explicitly called `bonus`, not cash; wagering/withdrawal rules are not yet established publicly. The non-cash hardware prizes add material value, so the true break-even denominator is higher than the bonus-only face-value diagnostic if those prizes are valued positively.

## What is still missing

1. Total eligible chance entries in each weekly draw, or a defensible upper bound.
2. Exact 200-AZN bonus conversion/wagering/withdrawal rules.
3. Whether campaign chance numbers reset weekly or accumulate across campaign periods.
4. Exact remaining campaign dates / draw schedule from accessible official rules.
5. Retail/market value and tax/transfer treatment of Changan/iPhone/PS5 prizes if we want a full prize-pool EV rather than a conservative bound.

Winner-number ranges are **not** used as a denominator unless the official numbering scheme is proven.

## Decision

Promote `Oley Oley` to **highest-priority live Phase-18 lead**, classification:

`current_super_keno_eligible_denominator_unresolved`

This is materially stronger than RadioArena because Super-Keno-category eligibility is explicitly published. It is still not proven +EV.

## Next action

1. Recover exact official campaign rules from Misli app/page/search cache/social posts: dates, chance reset/accumulation, bonus withdrawal terms.
2. Search draw videos/results/posts for any officially revealed total-entry count or draw-number domain.
3. Build conservative/central/optimistic prize-value scenarios for Changan UNI-Z, 3x iPhone 17 Pro, 5x PS5, and 50x200-AZN bonus.
4. Convert each scenario into the maximum weekly entry count compatible with Super Keno combined EV >= 1.
5. If an official denominator/bound puts the real pool below a break-even threshold, immediately move to variance-aware Super Keno execution with **N free**.
