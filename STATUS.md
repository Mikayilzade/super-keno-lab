# Super Keno Lab — status

Last updated: 2026-08-26

## Phase

`PHASE 18 — external EV modifiers / promotion overlays / variance-aware execution`

## Core state

- Dedicated repo: `Mikayilzade/super-keno-lab`; broad `loto-research` remains separate.
- **195** validated Super Keno draws, 2022-12-21..2026-08-23.
- Portfolio size **N remains a free integer optimization variable**.
- All history-based predictive branches are closed as primary edge sources after strict walk-forward/seed testing.
- Fixed-list universal guarantee is mathematically impossible for the base game.
- Mandatory rule: stochastic strategy construction must be evaluated across seeds, never one favorable seed.

## Exact base-game economics

For a fixed 10-number ticket, exact gross return over all mathematically possible 20-of-70 draws is **0.5985557942634199 per 1 AZN stake**.

Current exact after-tax expected cash-return ratios:
- 1x: **0.5918070335**;
- 2x: 0.591266;
- 5x: 0.589036;
- 10x: 0.586982.

1x is therefore best on expected after-tax cash.

Break-even modifier thresholds at 1x:
- direct cash-equivalent subsidy: **40.82%** of paid stake;
- one-wager bonus balance: **68.97%** of paid stake.

See `results/PHASE17_EXTERNAL_EV_MODIFIERS.md` and `src/ev_modifiers.py`.

## Closed primary routes

Do not reopen without materially new information:
1. fixed-list geometry alone;
2. hot/cold, pair/context and mean-reversion ensembles;
3. supervised per-number ranking;
4. direct ticket-payoff regression/ranking;
5. continuous structure forecasting;
6. discrete regime/Markov forecasting.

## Phase 18 completed checkpoints

- `PHASE18_OVERLAY_LEDGER_PILOT.md`: historical `Sürətli Şans`; denominator unknown.
- `PHASE18B_WELCOME_BONUS_CONDITIONAL_EV.md` / `PHASE18C_WELCOME_BONUS_STATUS_RESOLUTION.md`: old 10→10 offer would be +EV if live, but is historical/inactive.
- `PHASE18D_CURRENT_OVERLAY_AND_PAYMENT_SCAN.md`: current Azerlotereya public campaign listing had no active campaign; mainstream bank cashback stacks are excluded by published rules.
- `PHASE18E_RETAIL_OVERLAY_AUDIT.md`: OBA excludes chance-game purchases; Araz cashback excludes winning games; historical Araz receipt overlay remained unverified.
- `PHASE18F_DISTRIBUTOR_AND_CURRENT_PROMOCODE_SCAN.md`: Azərpoçt is neutral distribution; live RadioArena 10-AZN promo-code lead found.
- `PHASE18G_RADIOARENA_TERMS_RESOLUTION_ATTEMPT.md`: RadioArena promo remains live but public official sources do not resolve product eligibility/wagering/withdrawal; `#Futbol` is a sports-context signal, not proof. Do not count it as Super-Keno EV.

## Phase 18H — live `Oley Oley` overlay — HIGHEST PRIORITY

See `results/PHASE18H_CURRENT_OLEY_OLEY_OVERLAY.md`.

Fresh official Misli posts explicitly state:
- every **5 AZN** of sports betting => **1 chance**;
- every **5 AZN** in **Virtual İdman, ePoz-Qazan, Lotereya** => **2 chances**.

This is the first currently live overlay in Phase 18 with **explicit lottery-category eligibility**, making it materially stronger than RadioArena for Super Keno research.

Published weekly prize ladder for the third draw:
- 1 x Changan UNI-Z;
- 3 x iPhone 17 Pro;
- 5 x PlayStation 5;
- 50 x 200 AZN bonus (10,000 AZN nominal bonus face value).

After week 3, official Misli advertised remaining inventory equal to three such weekly prize ladders: 1 car, 9 iPhones, 15 PS5s and 30,000 AZN bonus.

### Break-even math for Super Keno spend

For 5 AZN of 1x Super Keno:
- expected base cash = **2.9590351675 AZN**;
- shortfall to break-even = **2.0409648325 AZN**;
- campaign grants **2 entries**;
- required overlay EV = **1.02048241625 AZN per entry**.

Diagnostic only: if the weekly 50x200-AZN bonus pool were worth its full 10,000-AZN face value as cash-equivalent EV, ignoring the car/iPhones/PS5s, combined break-even would hold for approximately **<=9,799 total weekly entries**. This is not yet a valid +EV claim because bonus conversion/wagering is unresolved and the entry denominator is unknown.

Classification: **`current_super_keno_eligible_denominator_unresolved`**.

## Current EV-modifier ledger

See `results/phase18_ev_modifier_ledger.csv`.

Key live states:
- `Oley Oley`: explicit lottery eligibility, denominator/value terms unresolved — highest priority;
- RadioArena 10 AZN promo: live, but Super-Keno product scope unresolved;
- ordinary bank/retail cashback routes: excluded/low priority under current published rules.

## NEXT ACTION — Phase 18 continuation

1. **Highest priority:** resolve `Oley Oley` exact official rules: campaign dates, whether chance numbers reset weekly or accumulate, 200-AZN bonus wagering/withdrawal rules, and any disclosed total entry count / number domain.
2. Search official draw videos/results/posts only for a defensible denominator or upper bound; do not infer total entries from winner-number ranges without proof of numbering scheme.
3. Build conservative / central / optimistic prize-value scenarios for the weekly Changan UNI-Z + 3 iPhone 17 Pro + 5 PS5 + 50x200-AZN bonus ladder.
4. Convert each scenario into maximum weekly total entries compatible with combined Super Keno personal-capital EV >= 1.
5. If an official denominator/bound falls below a break-even threshold, immediately design a variance-aware distinct-ticket Super Keno execution with **N free**.
6. Keep RadioArena as a watch item; do not spend repeated cycles on the same unresolved public keywords unless new official material appears.
7. Continue scanning genuinely current official Misli/Azerlotereya overlays only after the Oley Oley denominator/value audit.
8. Do not reopen rejected history-prediction branches without materially new information.
