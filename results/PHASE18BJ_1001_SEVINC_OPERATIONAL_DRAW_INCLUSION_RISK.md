# Phase 18BJ — 1001 Sevinc operational draw-inclusion risk

Date: 2026-08-28

## Result

No absolute current denominator (`cap / remaining / sold-count`) was recovered for `drawId=10066` or `10072` in this batch.

A materially new first-party operational fact was recovered and added to the finite-pool execution model: **1001 Sevinc has had a documented case where purchased tickets were not included in their scheduled draw because of a technical problem.**

Official Azerlotereya notice dated 2026-03-15 states that during the 2026-03-07 AirPods (3), Dyson Fen (1), iPhone 17 Pro Orange (1) and iPhone 17 Pro Blue (1) draws, a technical difficulty caused some tickets not to enter the draw. Azerlotereya announced additional draws for those omitted tickets, planned for 2026-04-03 at 21:00.

Source: https://www.azerlotereya.com/xeberler/1001-sevinc-asya-lotereyasi-ila-bagli-rasmi-malumat-1896

## Why this matters

The mathematical finite-pool route assumes that every purchased eligible ticket is actually present in the relevant selection pool. The March 2026 notice proves that this assumption has failed operationally at least once.

Therefore distinguish:

1. **Mathematical pool guarantee** — conditional on all purchased tickets being correctly admitted to the intended draw.
2. **Operational execution guarantee** — requires evidence that all bought tickets were admitted/settled correctly.

A strategy that buys every remaining ticket can mathematically force ownership of the winning ticket only if the operator's executed pool equals the advertised eligible pool. A technical omission can break the *scheduled-draw* guarantee even when the operator later remedies the problem with an additional draw.

The official notice is evidence of remediation, but it does not by itself prove all details needed to model the remedy as economically identical to the original draw (exact affected ticket set, prize allocation mechanics, timing/cashflow, and automatic inclusion conditions).

## Execution rule added

If a positive-EV finite-pool opportunity is eventually identified, do **not** treat denominator + purchase coverage alone as sufficient for a 100% operational guarantee. Before staking, require a ticket-status/inclusion verification layer where available:

- preserve ticket IDs/order records;
- verify each purchased ticket shows valid/current draw status in the purchasing account/channel;
- record drawId/prize/date and purchase timestamp;
- after draw, reconcile all ticket statuses/results;
- treat unresolved/missing status as execution risk, not as a losing ticket;
- preserve evidence for any operator remediation path.

No autonomous purchases are authorized.

## Model impact

This does **not** invalidate the finite-pool EV route. It adds a separate operational-risk factor and prevents us from calling a theoretical coverage result an unconditional real-world guarantee.

For ordinary expected-value screening, keep the existing ROI formula. For an eventual execution decision, report both:

- `mathematical_ROI` under the observed denominator/sell-through;
- `operational_integrity_status` (`verified`, `partially_verified`, `unverified`).

Until current ticket-inclusion behavior is verified, any wording such as “guaranteed profit” must be qualified as mathematical/conditional rather than unconditional operational certainty.

## Batch conclusion

**Not yet success.** No denominator was found. The meaningful advance is identification of a documented operator-side failure mode that must be incorporated before any finite-pool coverage can be called executable with certainty.

## Next action

Continue the existing denominator search for `10066 Silver` and `10072 S25` only through materially new account/rendered/retail artifacts. In parallel, when such an artifact appears, capture ticket-status semantics because they now serve two purposes: denominator discovery and operational inclusion verification.
