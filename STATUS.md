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

`src/ev_modifiers.py` now also supports equal-entry prize overlays via:
- `overlay_ev_per_qualifying_spend(...)`;
- `combined_return_ratio_with_overlay(...)`.

CI passes with the Phase-18 overlay boundary test.

## Phase 18A — stimulating-lottery overlay pilot

See:
- `results/PHASE18_OVERLAY_LEDGER_PILOT.md`
- `results/phase18_ev_modifier_ledger.csv`

Historical `Sürətli Şans` (2025) control:
- every 5 AZN ordinary eligible play earned 1 chance; ePoz-Qazan earned 2;
- weekly cash pool = **24,000 AZN**;
- total campaign cash = **192,000 AZN + 2 Toyota Corolla Hybrid**.

For 5 AZN of 1x Super Keno, expected after-tax base cash is 2.9590 AZN, so the overlay must contribute at least **2.0409648325 AZN per code** to reach personal-capital break-even.

Cash-only weekly break-even requires competition pool approximately:

**<= 11,759 chance codes**.

The public denominator is unknown, so the historical overlay remains `indeterminate`, not positive EV.

## Phase 18B — important conditional-positive candidate

See `results/PHASE18B_WELCOME_BONUS_CONDITIONAL_EV.md`.

The official `10 oyna, 10 qazan` page currently contains contradictory status signals:
- campaign body and term #5 say validity through **31 August 23:59**;
- term #8 references bonus loading from **24 July** onward;
- same page/search classification labels it a **past campaign**;
- embedded FAQ still says **14 April–31 July**, indicating stale/conflicting content;
- an official Azerlotereya Telegram post advertises the same 10-play/10-bonus offer as new, but its public rendering does not provide a reliable calendar date.

Terms currently exposed on the official campaign page:
- new Azerlotereya.com account;
- deposit/play at least 10 AZN;
- verify account;
- first 10,000 eligible users;
- 10 AZN additional balance, one use per user;
- Misli-to-Azerlotereya migrated accounts excluded;
- additional balance has no turnover requirement;
- unused deposited/additional balance withdrawal fee: 30%, minimum 5 AZN;
- winnings withdrawal: no commission.

### Conditional Super Keno EV

If the offer is currently enforceable and the user is eligible:

**Route A — wager 10 AZN paid + wager 10 AZN bonus once in 1x Super Keno**
- personal outlay: 10 AZN;
- expected total cash: **11.8361406702 AZN**;
- expected P/L: **+1.8361406702 AZN**;
- expected personal-capital ROI: **1.1836140670** (+18.36%).

**Route B — wager required 10 AZN paid, withdraw 10 AZN unused bonus under stated fee rule**
- expected original-play cash: 5.9180703351 AZN;
- net bonus withdrawal after minimum 5 AZN fee: 5 AZN;
- expected total cash: **10.9180703351 AZN**;
- expected ROI: **1.0918070335**.

Route A is superior in expectation. This is the first externally driven **conditional +EV candidate** in this repo, but it is not yet classified as currently actionable because the official page status/date signals conflict.

No account circumvention or multi-account exploitation is considered; this model assumes one lawful eligible user and one permitted use.

## Strategic decision

The base game remains negative-EV. External subsidies can overturn that negative EV. The project therefore prioritizes:
1. current promotions/bonuses with exact terms;
2. prize overlays with a defensible entry denominator;
3. legal stackability across independent modifiers;
4. variance-aware execution only after positive EV is established.

Finite one-time offers are tracked separately from repeatable strategies.

## NEXT ACTION — Phase 18 continuation

1. Resolve current status of `10 oyna, 10 qazan` using a clean current signal: active campaign API/listing, account-visible offer, or dated official announcement. Do not call it actionable while status remains conflicted.
2. Continue scanning current Azerlotereya/Misli campaigns and partner/payment promos for modifiers exceeding the established threshold.
3. Search stimulating-lottery/extra-chance overlays for published entry counts or defensible upper bounds; use generic overlay helpers for immediate EV classification.
4. If the 10→10 candidate is confirmed active and eligible, design a variance-aware 20-AZN total play execution (10 paid + 10 bonus) with **N free**, while preserving the subsidy-driven +EV.
5. Compare possible distinct-ticket portfolios for that finite 20-AZN execution by downside/variance, not by pretending ticket selection changes base EV.
6. Keep current/inactive/conflicted statuses explicit in `results/phase18_ev_modifier_ledger.csv` so stale pages never become false opportunities.
7. Continue searching for repeatable modifiers after the one-time welcome offer because even a valid +EV welcome bonus is capacity- and account-limited.
