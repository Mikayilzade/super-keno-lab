# Super Keno Lab — status

Last updated: 2026-08-26

## Phase

`PHASE 18 — external EV modifiers / promotion overlays / variance-aware execution`

## Core state

- Dedicated repo: `Mikayilzade/super-keno-lab`; broad `loto-research` remains separate and untouched.
- **195** validated Super Keno draws, 2022-12-21..2026-08-23.
- Portfolio size **N remains a free integer optimization variable**.
- All historical draw-based predictive branches are closed as primary edge sources after strict walk-forward/seed testing.
- Working assumption: lototron unchanged; physical/video branch remains deprioritized.
- Mandatory rule: stochastic strategy construction must be evaluated across strategy/universe seeds, never one favorable seed.

## Exact base-game result

For a fixed 10-number ticket, exact gross return over all mathematically possible 20-of-70 draws is **0.5985557942634199 per 1 AZN stake**. No fixed ticket list at any N can guarantee break-even/profit across all possible draws.

Current exact after-tax expected cash-return ratios:
- 1x: **0.5918070335**;
- 2x: 0.591266;
- 5x: 0.589036;
- 10x: 0.586982.

Therefore 1x is the best multiplier on expected after-tax cash.

## Closed predictive routes

Rejected as primary sources after strict robustness checks:
1. fixed-list geometry alone;
2. hot/cold, pairs, group mean reversion and ensembles;
3. supervised per-number ranking;
4. direct ticket-payoff regression/ranking;
5. continuous draw-structure prediction;
6. discrete regime/Markov classification.

Do not reopen these via nearby parameter tuning without materially new information.

## Phase 17 — EV modifier foundation

See:
- `results/PHASE17_EXTERNAL_EV_MODIFIERS.md`
- `src/ev_modifiers.py`
- `tests/test_ev_modifiers.py`

Break-even thresholds for 1x Super Keno:
- direct cash-equivalent subsidy: **40.82% of paid stake**;
- one-wager bonus balance: **68.97% of paid stake**;
- a genuine 100% one-wager match implies expected personal-capital ROI about **1.1836** before extra friction.

`src/ev_modifiers.py` supports equal-entry prize overlays via `overlay_ev_per_qualifying_spend(...)` and `combined_return_ratio_with_overlay(...)`.

## Phase 18A — stimulating-lottery overlay pilot

See:
- `results/PHASE18_OVERLAY_LEDGER_PILOT.md`
- `results/phase18_ev_modifier_ledger.csv`

Historical `Sürətli Şans` (2025) control:
- every 5 AZN ordinary eligible play earned 1 chance; ePoz-Qazan earned 2;
- weekly cash pool = **24,000 AZN**;
- total campaign cash = **192,000 AZN + 2 Toyota Corolla Hybrid**.

For 5 AZN of 1x Super Keno, expected after-tax base cash is 2.9590 AZN, so the overlay must contribute at least **2.0409648325 AZN per code** to reach personal-capital break-even.

Cash-only weekly break-even requires competition pool approximately **<= 11,759 chance codes**. Public denominator remains unknown, so this historical overlay is `indeterminate`, not positive EV.

## Phase 18B/18C — welcome-bonus candidate resolved

See:
- `results/PHASE18B_WELCOME_BONUS_CONDITIONAL_EV.md`
- `results/PHASE18C_WELCOME_BONUS_STATUS_RESOLUTION.md`
- `results/phase18_ev_modifier_ledger.csv`

The archived `10 oyna, 10 qazan` mechanics are mathematically important:
- new eligible user played 10 AZN;
- 10 AZN additional balance;
- no turnover requirement on additional balance;
- one use per user; first 10,000 eligible users.

If currently valid, playing 10 AZN paid + 10 AZN bonus once at 1x Super Keno would have expected personal-capital ROI **1.1836140670**, expected P/L **+1.8361406702 AZN** on 10 AZN personal outlay.

### Current status resolution — 2026-08-26

The ambiguity is resolved against actionability:
- official `Cari kampaniyalar` public snapshot explicitly says **`Cari kampaniya mövcud deyil`**;
- the dedicated 10→10 URL is indexed/labeled **`keçmiş kampaniya`**;
- its body still says through 31 August while embedded FAQ says 14 April–31 July, so conflicting date fragments are treated as stale archived content.

Decision: reclassify 10→10 as **`historical_inactive_positive_mechanism`**, not a current opportunity.

## Phase 18D — current overlay + payment-channel scan

See:
- `results/PHASE18D_CURRENT_OVERLAY_AND_PAYMENT_SCAN.md`
- updated `results/phase18_ev_modifier_ledger.csv`

Fresh public scan on 2026-08-26:
- official Azerlotereya current-campaign page still says **no current campaign**;
- recent `Sürətlə Qazan` tournament ran **7–14 Aug 2026**, applied only to 52 tagged digital/ePoz games and is not a Super-Keno modifier;
- `Şans Karvanı 2` publishes gifts/event activity but no defensible ticket-linked qualification/probability table, so its EV is not quantifiable;
- Unibank, ABB/TamKart and Birbank/Kapital Bank published reward rules all exclude lottery/gambling transactions or the relevant MCCs (notably 7800/7995; ABB also names Loto/Casino/Gambling merchants).

Decision: ordinary mainstream bank cashback/reward stacking is now **low priority / closed under current published rules**. Reopen only if a future campaign explicitly includes lottery transactions.

## Phase 18E — retail / merchant overlay audit

See:
- `results/PHASE18E_RETAIL_OVERLAY_AUDIT.md`
- updated `results/phase18_ev_modifier_ledger.csv`

Fresh retail-channel findings:
- OBA receipt-lottery terms explicitly exclude `şans oyunlarının alışı`; a second OBA lottery page independently shows the same chance-game exclusion. Therefore OBA receipt-lottery stacking is closed under current published mechanics.
- Araz sells Azerlotereya Poz-Qazan tickets in 360+ stores, but its standard mobile-app cashback rules explicitly exclude `uduşlu oyunlar`, so ordinary Araz cashback cannot subsidize lottery spend.
- Araz has separately run receipt-lottery campaigns whose published exclusions were narrower. `Uçuşa hazır ol` (4 Jul–4 Aug 2026) gave 1 chance per 20 AZN receipt and 10 x 5,000 AZN travel vouchers; the published exclusions mentioned tobacco/alcohol but did **not** explicitly mention chance games.
- This does **not** make the historical campaign actionable: it is inactive, Super Keno checkout eligibility at Araz is unverified, and total entry count is unknown.

Diagnostic only: if a future materially identical 50,000-AZN equal-entry receipt overlay explicitly allowed 20 AZN of Super Keno spend, the base-game EV shortfall would be **8.16385933 AZN per chance**, so break-even would require approximately **<= 6,124 total equal-weight entries** before discounting non-cash prize value or other friction.

Decision: distinguish **retail cashback exclusions** from **receipt-lottery qualification rules**. A retailer can close one while leaving the other ambiguous; future campaign terms must be checked independently.

## Strategic decision

The base game remains negative-EV. External subsidies can overturn that negative EV, but stale/archived offers must never be counted as live opportunities.

The project prioritizes:
1. genuinely current promotions/bonuses with exact terms;
2. prize overlays with a defensible entry denominator;
3. legal stackability across independent modifiers;
4. variance-aware execution only after positive EV is established.

Finite one-time offers remain separate from repeatable strategies.

## NEXT ACTION — Phase 18 continuation

1. Audit **Azərpoçt / kiosk / distributor** channels and any retailer-specific promotions for exact lottery-spend qualification language, especially channels that directly sell numerical lottery tickets rather than only scratch cards.
2. Search stimulating-lottery/extra-chance overlays for published total entry counts, winner lists from which participation can be bounded, or official statements on code volume; apply generic overlay helpers immediately when a denominator is defensible.
3. Continue current Misli/Azerlotereya account-independent announcement scans for newly launched post-snapshot terms.
4. Monitor future Araz receipt-lottery campaigns specifically for whether `uduşlu oyunlar` / `şans oyunları` are excluded; do not infer receipt-lottery eligibility from cashback rules.
5. Keep OBA standard receipt-lottery stacking closed unless future terms explicitly remove the chance-game exclusion.
6. For every new modifier, update `results/phase18_ev_modifier_ledger.csv` with current/inactive/conflicted status and exact EV classification.
7. If a current positive-EV modifier is verified, design a variance-aware distinct-ticket execution with **N free**, optimizing downside/variance while preserving subsidy-driven positive expectation.
8. Do not reopen rejected history-prediction branches without materially new information.
