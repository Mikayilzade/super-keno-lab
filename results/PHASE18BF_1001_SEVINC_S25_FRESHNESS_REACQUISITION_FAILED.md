# Phase 18BF — S25 fresh sell-through reacquisition failed

Date: 2026-08-28

## Goal

Follow `STATUS.md` NEXT ACTION #1: reacquire a fresh complete first-party sold percentage for `drawId=10072 / Samsung Galaxy S25 Ultra Black` before using it for execution ranking.

## Fresh search result

Targeted first-party searches on 2026-08-28 for the current 16.09.2026 cycle did **not** return a complete S25 record containing all of: prize name + 0.5 AZN price + 16.09.2026 draw date + sold percentage.

Queries targeted Azerlotereya and Misli with combinations of:
- `Samsung Galaxy S25 Ultra Black`
- `0.5 AZN / 0.5₼`
- `16.09.2026`
- `Satıldı`
- `drawId 10072`

No fresh complete record was recovered. Therefore the older ~41% S25 observation remains **monitoring-only** and must not be used as a live execution input.

## Control observation

The same fresh first-party surface still reproduces `iPhone 17 Pro 256 GB Cosmic Orange — 1 AZN — 16.09.2026 — Satıldı: 43%`, showing that the crawler is capable of returning current-cycle sell-through for at least some cards. This makes the missing S25 percentage a genuine current-surface limitation rather than evidence that the whole page is stale.

A Misli cache crawled several days earlier still shows Cosmic Orange at 34%, confirming cross-surface cache divergence and reinforcing the rule that sell-through inputs must be bound to source and crawl time.

## Decision

- `10072 S25 Ultra Black` stays fully drawId-bound but **not executable** without a fresh sold percentage.
- Do not promote it above `10066 Silver` on the basis of the stale ~41% figure.
- Do not reopen generic API/registry/Trendyol/local-download routes; no materially new denominator surface appeared in this batch.
- `10066 Silver` remains denominator target #1 because it is the strongest currently bound candidate with a fresh complete sold input (33%).
- `10065 Cosmic Orange` remains the control candidate with a reproducible 43% fresh first-party sell-through.

## Next action

Continue only with materially new rendered/account/client artifacts for absolute `cap / remaining / sold-count` on `10066` or `10072`. Reacquire S25 sell-through only when a newly dated/current first-party card surfaces. Preserve N as a free integer variable.
