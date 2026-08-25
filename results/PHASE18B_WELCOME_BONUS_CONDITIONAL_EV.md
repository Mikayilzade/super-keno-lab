# Phase 18B — 10→10 welcome-bonus conditional EV audit

Date: 2026-08-26

Status: **CONDITIONAL POSITIVE-EV CANDIDATE FOUND; CURRENT AVAILABILITY/ELIGIBILITY NOT YET CLEANLY VERIFIED.**

## Why this needed a separate audit

The official Azerlotereya page currently exposes mutually inconsistent status/date signals for `10 oyna, 10 qazan`:

- the campaign page headline/body says new Azerlotereya.com users who register by **31 August** can play at least 10 AZN and receive 10 AZN additional balance;
- campaign term #5 also says validity through **31 August 23:59**;
- term #8 says bonuses are loaded on Monday/Thursday from **24 July** onward;
- the same page/search classification calls it a **past campaign**;
- the FAQ embedded lower on the page still says **14 April–31 July**, indicating stale/conflicting content;
- an official Azerlotereya Telegram post advertises the same 10-play/10-bonus offer as `yepyeni` (new), but the public Telegram rendering used here does not expose a reliable calendar date for the post.

Therefore this repo must not call the offer definitely active on 2026-08-26 without account-side confirmation or a clean current-campaign listing. It is classified `conditional_positive / status_conflicted`.

Official sources:
- https://www.azerlotereya.com/kampaniya/10oyna-10qazan
- https://www.azerlotereya.com/faq/10oyna-10qazan
- https://t.me/Azerlotereya/1853

## Terms relevant to EV

The current official campaign page states:

1. new Azerlotereya.com account;
2. minimum 10 AZN deposit and minimum 10 AZN play;
3. account verification required;
4. first 10,000 qualifying new users only;
5. maximum additional balance = 10 AZN;
6. Misli.az users migrating to Azerlotereya.com are excluded;
7. qualifying play can be in lottery, ePoz-Qazan and Digital Games;
8. additional balance has **no turnover requirement** and can be used as desired;
9. withdrawing unused deposited/additional balance has a 30% fee with **minimum 5 AZN**;
10. withdrawing winnings has **no commission**.

This is finite and account-specific: at most one 10 AZN bonus per eligible person. It is not a perpetual strategy.

## Super Keno conditional EV

Use the exact current after-tax 1x Super Keno expected cash-return ratio already established in this repo:

`e = 0.5918070335083189`.

### Route A — play the bonus once

Personal outlay: 10 AZN.

Expected cash from the required 10 AZN paid play:

`10e = 5.9180703351 AZN`.

If the resulting 10 AZN bonus is then wagered once in 1x Super Keno, expected bonus-funded winnings are also:

`10e = 5.9180703351 AZN`.

Because the campaign terms say winnings are withdrawn without commission, total expected cash is:

`20e = 11.8361406702 AZN`.

Relative to 10 AZN personal capital:

- expected P/L = **+1.8361406702 AZN**;
- expected personal-capital ROI = **1.1836140670**;
- expected profit rate = **+18.36%**.

This is mathematically positive EV if all cited campaign terms are currently enforceable and the account is eligible.

### Route B — do not wager the bonus; withdraw unused bonus

For a 10 AZN unused bonus, 30% is 3 AZN but the stated minimum withdrawal fee is 5 AZN, so net bonus cash would be 5 AZN if this interpretation is accepted by the platform.

Expected total cash then becomes:

`5.9180703351 + 5 = 10.9180703351 AZN`.

Relative to 10 AZN personal capital:

- expected P/L = **+0.9180703351 AZN**;
- expected ROI = **1.0918070335**.

Thus wagering the bonus once is superior in expectation to withdrawing it unused under the published fee rule.

## Important caveats

- This result is **expectation**, not guaranteed profit; a 20-AZN total play can still lose most/all value in a realized path.
- Eligibility is binary and capacity-limited to the first 10,000 qualifying users.
- A user who already has/used an Azerlotereya.com account, or migrated from Misli.az, may be ineligible.
- The official page currently contains contradictory active/past and July/August signals. Do not treat this candidate as actionable until current account-side eligibility is confirmed.
- No multi-account or identity circumvention is considered; the model assumes one lawful eligible user and one permitted use.

## Engineering update

`src/ev_modifiers.py` now includes generic equal-entry prize-overlay helpers:

- `overlay_ev_per_qualifying_spend(...)`
- `combined_return_ratio_with_overlay(...)`

Tests include the Phase-18 `Sürətli Şans` cash-only break-even boundary (~11,759 weekly entries).

## Decision / next action

1. Promote the 10→10 offer from `historical proof only` to **conditional-positive candidate with status conflict**.
2. Seek a clean active-status signal (current campaign API/listing/account-visible offer or dated official announcement) before calling it available.
3. If current eligibility is verified, design a small variance-aware 10 paid + 10 bonus execution plan; N remains free, but total personal stake is capped by the offer itself.
4. Continue scanning other current modifiers because this candidate is one-time and capacity-limited even if valid.
5. Keep searching for overlays whose denominator/entry count is published so expected value can be independently verified rather than inferred.
