# Phase 18CB — Oley Oley lottery double-chance overlay

Date: 2026-08-29

## Status

**Not yet success**, but this is a materially new live modifier and should now be tracked as a high-priority EV overlay.

## New evidence

Current Misli operator-channel material for the active **Oley Oley** campaign states:

- user must opt in with `Kampaniyaya qoşul`;
- every **5 AZN** in sports betting earns **1 chance**;
- every **5 AZN** in the other game categories — explicitly including **Lotereya** — earns **2 chances**;
- launch prize inventory was advertised as **2 Changan UNI-Z + 18 iPhone 17 Pro + 30 PlayStation 5 + 60,000 AZN bonus**;
- the first weekly draw advertised **3 iPhone 17 Pro + 5 PlayStation 5 + 50 × 200 AZN bonus**;
- the third weekly draw advertised the same weekly bundle plus **1 Changan UNI-Z**;
- after the third week, the operator advertised the remaining inventory as **1 Changan UNI-Z + 9 iPhone 17 Pro + 15 PlayStation 5 + 30,000 AZN bonus**.

Sources:

- https://t.me/s/misliaz?before=4825
- https://t.me/s/misliaz?q=%23Kampaniya
- https://t.me/s/misliaz?before=4865
- campaign route: https://www.misli.az/kampaniyalar/oley-oley

The arithmetic is internally consistent with a **six-week campaign**: 18 phones / 3 per ordinary weekly draw = 6; 30 PS5 / 5 = 6; 60,000 AZN bonus / 10,000 per week = 6. Two of those six weekly draws additionally contain a car; week 3 is confirmed as one of them. This is an inference from the advertised inventory, not a substitute for the full terms.

## Why this matters for Super Keno

This is stronger than the previous generic promotional leads because the current operator copy explicitly names **Lotereya** and gives it the favorable **2 chances per 5 AZN** rate.

The base Super Keno after-tax expected cash-return ratio already established in this repo is:

`r_base = 0.5918070335`

For 5 AZN of qualifying Super Keno stake, expected base cash return is:

`5 * 0.5918070335 = 2.9590351675 AZN`

Therefore the promotional overlay must contribute more than:

`5 - 2.9590351675 = 2.0409648325 AZN`

per 5 AZN stake to make the combined wager positive EV.

Because 5 AZN of Lotereya stake produces **2 Oley Oley chances**, the required expected value per promo chance is:

`2.0409648325 / 2 = 1.02048241625 AZN/chance`

This gives a clean denominator target.

### Conservative bonus-only weekly threshold

Each ordinary weekly draw visibly contains **10,000 AZN of stated bonus prizes** (`50 × 200 AZN`), before assigning any value to phones, consoles, or cars.

If `T_week` is the total number of eligible promo chances in a weekly draw and chances are equiprobable, then bonus-only EV per chance is:

`10,000 / T_week`

Ignoring all physical prizes, the combined Super Keno + Oley Oley overlay is positive EV whenever:

`10,000 / T_week > 1.02048241625`

or approximately:

`T_week < 9,799 chances`.

This **9,799** figure is deliberately conservative because it assigns zero value to 3 iPhone 17 Pro and 5 PS5 in an ordinary weekly draw, and zero value to the Changan UNI-Z in car weeks.

If physical prizes are valued, the allowed break-even denominator becomes materially larger:

`T_break_even = V_week_usable / 1.02048241625`

where `V_week_usable` is the risk-adjusted usable value of all weekly prizes.

## Critical unresolved fields

Do **not** execute based on this phase alone. We still need:

1. full current campaign terms / exact campaign dates;
2. explicit confirmation that **Super Keno tickets**, not merely other `Lotereya` products, generate the 2 chances;
3. timing rule for draw-based lottery tickets (purchase date vs underlying lottery draw date);
4. whether bonus-funded wagers are excluded;
5. whether Oley Oley chances reset weekly and whether prior-week chances carry into car draws;
6. actual weekly denominator `T_week`, or a defensible bound from chance-number ranges / account UI / support evidence;
7. bonus withdrawal/turnover conditions and usable-value haircut;
8. whether one account can generate unlimited qualifying chances.

The old `Sürətli Şans` rules are useful only as a structural analogue: they explicitly treated draw-lottery tickets on their underlying draw date and excluded bonus-funded play, but those rules must **not** be silently imported into Oley Oley.

## Research consequence

The APK denominator route remains valuable, but Oley Oley is now a parallel high-priority route because it can potentially lift the otherwise negative Super Keno EV without requiring prediction of draw outcomes.

Highest-value next evidence is **the current Oley Oley terms or a live account/support artifact giving weekly chance count / generated chance-number range**. If `T_week` can be bounded, compute the full combined ROI immediately with 0/60/70/80/100% usable-value haircuts for physical prizes and bonus restrictions.

## N discipline

Portfolio size **N remains a free integer optimization variable**. No round-number ticket-count assumption is introduced here.