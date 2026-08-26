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
- `PHASE18G_RADIOARENA_TERMS_RESOLUTION_ATTEMPT.md`: RadioArena promo remains live but public official sources do not resolve product eligibility/wagering/withdrawal; do not count it as Super-Keno EV.
- `PHASE18H_CURRENT_OLEY_OLEY_OVERLAY.md`: live Oley Oley explicitly includes Lotereya at 2 chances / 5 AZN; denominator unresolved.
- `PHASE18I_OLEY_OLEY_VALUE_BOUNDS.md`: full weekly prize ladder valued under conservative/central/optimistic realizability scenarios.

## Phase 18I — Oley Oley value bounds — HIGHEST PRIORITY

Fresh official Misli posts still make `Oley Oley` the strongest current external-EV lead:
- every 5 AZN sports betting => 1 chance;
- every 5 AZN in Virtual Idman, ePoz-Qazan, **Lotereya** => 2 chances.

Published weekly ladder:
- 1 x Changan UNI-Z;
- 3 x iPhone 17 Pro;
- 5 x PlayStation 5;
- 50 x 200 AZN bonus.

Current Azerbaijan prize-value references used only as valuation anchors:
- Changan UNI-Z IDD: **38,900 AZN** official reference;
- iPhone 17 Pro 256GB: about **3,099.99 AZN** current retail promo reference;
- PS5 Slim Blue-Ray 1TB: about **1,449.99 AZN** current retail promo reference.

### Break-even math

For 5 AZN 1x Super Keno:
- base expected cash = **2.9590351675 AZN**;
- shortfall = **2.0409648325 AZN**;
- 2 campaign entries are earned;
- required campaign EV = **1.02048241625 AZN per entry**.

### Weekly denominator thresholds

`PHASE18I` deliberately separates realizable value from face value:

| scenario | effective weekly prize value | max equal-probability weekly entries for combined EV >= 1 |
|---|---:|---:|
| conservative | **40,397.45 AZN** | **~39,587** |
| central | **54,633.00 AZN** | **~53,536** |
| optimistic | **65,449.92 AZN** | **~64,136** |

Conservative assumptions already assign **zero** value to the 10,000-AZN nominal bonus and haircut physical prizes heavily. Central values the bonus only at one-wager Super-Keno expected cash. Optimistic uses full retail/face values.

This materially improves the earlier bonus-only threshold (~9,799 entries): the car/electronics account for most of the overlay value. Therefore Oley Oley could remain compatible with positive combined EV at competition pools in the tens of thousands.

However, public official material still does **not** disclose a defensible weekly entry denominator, number-domain interpretation, reset/accumulation rule, or 200-AZN bonus wagering/withdrawal terms. Winner-number ranges are not used to infer denominator without proof.

Classification remains:

`current_super_keno_eligible_denominator_unresolved`

Do **not** stake based on this overlay yet.

## Current EV-modifier ledger

See `results/phase18_ev_modifier_ledger.csv`.

Key live states:
- `Oley Oley`: explicit lottery eligibility; full-prize break-even threshold now ~39.6k–64.1k weekly entries depending realizable value; denominator unresolved — highest priority;
- RadioArena 10 AZN promo: live, but Super-Keno product scope unresolved;
- ordinary bank/retail cashback routes: excluded/low priority under current published rules.

## NEXT ACTION — Phase 18 continuation

1. **Highest priority:** resolve `Oley Oley` weekly denominator or a defensible upper bound from official material; do not infer it merely from winner-number ranges.
2. Resolve whether entries reset each weekly draw or accumulate and retrieve exact campaign start/end dates from official terms if a newly indexed source appears.
3. Resolve 200-AZN bonus withdrawal/turnover/product-scope rules; update central scenario rather than assuming one wager if exact terms surface.
4. Search official draw videos/results/posts for an explicit total-entry count, issued-number count, participant count, or numbering statement.
5. If no exact denominator exists, seek an evidence-based upper bound from official campaign/platform participation disclosures.
6. If a defensible denominator/upper bound falls below **~39,587 weekly entries**, promote immediately to positive-EV candidate even under the conservative prize-value scenario and design a variance-aware distinct-ticket Super Keno execution with **N free**.
7. Continue scanning genuinely current lottery-eligible overlays in parallel; do not spend repeated cycles on unchanged RadioArena keywords.
8. Do not reopen rejected history-prediction branches without materially new information.
