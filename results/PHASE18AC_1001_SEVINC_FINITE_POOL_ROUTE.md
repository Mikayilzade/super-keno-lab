# Phase 18AC — 1001 Sevinc finite-pool / under-sell EV route

Date: 2026-08-27

Status: **NEW MATERIAL NON-HISTORY MECHANISM; NOT YET EXECUTABLE +EV; NOT A SUPER-KENO MODIFIER.**

## Why this route matters

This checkpoint deliberately does not reopen any rejected Super Keno prediction route. It identifies a different operator-side mechanism: `1001 Sevinc`, a registered in-kind lottery where each prize category has its own ticket pool, a scheduled draw date and live sell-through percentage.

Official/public evidence:

- Azerlotereya describes `1001 Sevinc` as an in-kind lottery run among purchased tickets, with category-specific ticket prices and predeclared draw dates.
- Current Azerlotereya surface shows eleven scheduled draws on **16.09.2026**, with ticket prices currently **0.5 AZN or 1 AZN** on that surface.
- Rules say that if tickets sell out early and more than 7 business days remain, the draw may be moved earlier after notice. This proves that each prize category has a finite ticket inventory rather than an unlimited stream.
- Misli's current indexed `1001 Sevinc` surface exposes a live `Satıldı:` (sold) percentage. A current indexed snippet shows, among other entries, **`Satıldı: 33%` for iPhone 17 Pro 256 GB Deep Blue**; another active entry is indexed at `Satıldı: 41...`.
- Azerlotereya has previously confirmed real `1001 Sevinc` winners and real physical prizes, including a Changan Q05 automobile; one winner reportedly held 19 tickets.

Sources checked 2026-08-27:
- https://www.azerlotereya.com/lotereya/1001-sevinc
- https://www.misli.az/lotereya/1001-sevinc/tirajlar
- https://www.azerlotereya.com/bloq/1001-sevinc-al-qazan-lotereyaya-neca-qosulmaq-olar-23
- https://www.azerlotereya.com/xeberler/samkirli-22-yasli-ganc-1001-sevincdan-avtomobil-qazandi-1898

## EV model

For a single-prize category, let:

- `p` = ticket price;
- `M` = number of valid sold tickets participating in the draw;
- `V` = conservative cash-equivalent resale value of the physical prize, net of friction/tax/transaction costs.

If every sold ticket is equally likely and unsold tickets cannot win, then expected value of one new ticket immediately before close is approximately:

`EV_cash = V / (M + 1)`

and expected personal-capital ROI is:

`ROI = V / ((M + 1) * p)`.

Break-even condition:

`M + 1 < V / p`.

This is fundamentally different from Super Keno: if a prize is fixed but the actual sold-ticket denominator is low, under-selling can raise EV. A live sell-through percentage becomes potentially valuable information **only if the total issued-ticket cap for the category is known**.

If `C` is the fixed maximum ticket inventory and `s` is the final sold fraction, then approximately `M = s*C`, giving:

`ROI ≈ V / (p*s*C)`.

## Tax/value caution

Azerbaijan tax guidance states that lottery winnings/prizes are taxable under the applicable lottery-prize rules; treatment of an in-kind prize and its valuation must be verified before using retail sticker price as `V`. Therefore all future EV estimates must use conservative net realizable value, not headline retail value.

## Current blockers

The public surfaces currently do **not** expose enough information to declare positive EV:

1. exact maximum ticket inventory `C` per active item is not yet public in the indexed page text;
2. exact number of sold/valid tickets `M` is not shown, only percentage;
3. need explicit confirmation that an under-subscribed scheduled draw selects only among sold/valid tickets and is not postponed/cancelled until a minimum threshold;
4. need the prize model/SKU for every current draw and a conservative local resale value;
5. need exact tax / transfer / resale friction for in-kind winnings.

## Important strategic interpretation

`1001 Sevinc` is **not** being promoted as a Super Keno strategy and is not inserted into the Super Keno EV-modifier ledger. It is preserved as a separate finite-pool operator mechanism because it can, in principle, create positive EV through a low realized denominator rather than prediction.

This is exactly the kind of materially new information source the project should prefer over tuning historical-number models.

## Next action

1. Recover the fixed ticket cap `C` for current draw IDs (current indexed draw IDs include 10064, 10065, 10066, 10067, 10072, 10073).
2. Check FAQ/network/static surfaces for category rules and unsold-ticket treatment.
3. Record current sell-through percentages over time rather than one snapshot.
4. Map each current prize to a conservative resale value.
5. If `C` is recovered, compute real-time ROI bounds and only flag categories where conservative lower-bound ROI exceeds 1 after tax/friction.
6. Keep this secondary route separate from the main Super Keno Phase-18 modifier search.
