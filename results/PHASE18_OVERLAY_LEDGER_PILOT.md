# Phase 18 — EV modifier ledger / stimulating-lottery overlay pilot

Date: 2026-08-25

Status: **NO CURRENT POSITIVE-EV OVERLAY VERIFIED; HISTORICAL OVERLAY THRESHOLD QUANTIFIED.**

## Current snapshot

- Official Azerlotereya current-campaign listing: no current campaign verified on 2026-08-25.
- Historical `10 oyna, 10 qazan` remains a proof-of-mechanism only; it is not treated as active.
- Current Unibank cashback terms exclude lottery/gambling transactions.
- `Şans Karvanı 2` is an event/marketing format with gifts but public terms do not provide a defensible ticket-linked probability model.

## Historical stimulating-lottery control: `Sürətli Şans`

Official terms (2025-09-01..2025-10-26):
- every 5 AZN ordinary play on Azerlotereya.com/Misli.az earned 1 chance code;
- every 5 AZN ePoz-Qazan earned 2 chance codes;
- all games were eligible;
- 8 weekly cash draws;
- total cash prizes advertised: 8 x 10,000 + 16 x 2,000 + 80 x 1,000 = **192,000 AZN**;
- every four weeks, accumulated weekly chance codes also entered a Toyota Corolla Hybrid draw; total **2 cars**.

For one weekly draw the cash pool was:

`10,000 + 2*2,000 + 10*1,000 = 24,000 AZN`.

## Super Keno overlay break-even threshold

Current exact after-tax 1x Super Keno EV is:

`e = 0.5918070335083189` cash per 1 AZN stake.

For 5 AZN personal spend:

- expected base-game cash = `5e = 2.9590351675 AZN`;
- shortfall to personal-capital break-even = `5 - 5e = 2.0409648325 AZN`.

A single stimulating-lottery chance earned per 5 AZN therefore needs expected overlay value of at least **2.0409648325 AZN**.

Ignoring the car prize, if a weekly chance code has equal probability over `C` eligible codes, weekly cash overlay EV per code is `24,000/C`. Cash-only break-even is:

`24,000/C >= 2.0409648325`

so:

**C <= 11,759.14 codes**.

Thus for Super Keno, the cash part alone would have made the combined personal-capital EV >=1 only if the relevant weekly competition pool were at most about **11,759 chance codes**. The Toyota draw increases the maximum tolerable competition pool, but its exact incremental EV needs the registered monetary value of the car and the number of codes entering the monthly car draw.

For ePoz-Qazan the historical promotion awarded 2 codes per 5 AZN, so the overlay subsidy per paid manat was mechanically twice as large before considering the base-game EV of the ePoz game. This does **not** imply ePoz was positive EV; it identifies promotion qualification efficiency as an optimization variable for future overlays.

## Missing variable that blocks historical EV classification

The official public pages expose winners and prize structure but do not expose the total eligible chance-code count per weekly/monthly draw. Without that denominator, assigning a precise overlay EV would be fabricated. Therefore `Sürətli Şans` is classified as **indeterminate historical overlay**, not positive EV.

## Decision / next action

1. Keep `results/phase18_ev_modifier_ledger.csv` as the structured source-of-truth ledger.
2. For future stimulating lotteries, capture the total code/entry pool if exposed by rules, draw logs, APIs or official reports.
3. Add a generic overlay-EV function to `src/ev_modifiers.py`: prize pool / competition entries x entries earned per qualifying spend, then combine with base-game after-tax EV.
4. Compare qualification efficiency across eligible games when an overlay exists; a lower/base-EV game can still be inferior even if it earns more codes.
5. Continue searching current/public partner promos and legal additional-chance overlays. Do not classify anything as positive EV without both prize value and defensible competition denominator/bound.

Sources:
- https://www.azerlotereya.com/suretli-sans
- https://www.azerlotereya.com/faq/suretli-sans
- https://www.azerlotereya.com/kampaniyalar
- https://www.azerlotereya.com/faq/10oyna-10qazan
- https://unibank.az/cards/cashback
