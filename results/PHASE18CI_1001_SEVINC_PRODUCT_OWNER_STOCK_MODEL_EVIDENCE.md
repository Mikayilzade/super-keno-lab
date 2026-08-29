# Phase 18CI — `1001 Sevinc` product-owner stock-model evidence

Date: 2026-08-29

## Goal

Continue the Phase 18CH product-design / denominator recovery route without repeating bounded generic searches. Test whether public artifacts from the product team expose a stronger operational model for `1001 Sevinc` and any new path toward draw-level stock / remaining-ticket counts.

## New evidence

A public LinkedIn year-end product overview by **Tabriz Dumanlı, MBA, PMP®**, an Azərlotereya product leader, explicitly describes the 2025 `1001 Sevinc` work as an end-to-end operating model covering:

- `prize/price` structure;
- **stock (`stok`)**;
- launch in **partner channels**;
- draw coordination;
- prize-claim coordination.

Source: https://tr.linkedin.com/posts/tabriz-dumanl%C4%B1-mba-pmp%C2%AE-239729202_2025-last-working-day-product-overview-activity-7411783157387030528--NNN

A mirrored/reposted copy of the same text is currently indexed on Konul B. Gulmammadova's public LinkedIn activity page, giving a second retrievable surface for the same operator-side statement.

## Interpretation

This is materially stronger than generic marketing language about a draw occurring after enough tickets are sold. It confirms that **stock is an explicit product/operations dimension of `1001 Sevinc`**, alongside price/prize configuration and partner-channel launch.

It does **not** yet prove the exact backend field name, whether stock is stored globally or per draw/prize, nor the numeric cap for `10066 Silver`. Existing evidence still favors draw + prize-category scope, and we should keep that assumption until contradicted.

The artifact also suggests a new evidence route that is more targeted than generic web search:

1. product-management / operations portfolio posts;
2. partner-channel launch artifacts where stock synchronization may be discussed;
3. retail/digital integration screenshots or launch decks;
4. employee posts mentioning `stok`, `inventory`, `qalıq`, `remaining`, `sold`, `limit`, `ticket count`, or channel synchronization together with `1001 Sevinc`.

## Short-link resolution attempt from Phase 18CH

The two links in Zulfiyya Shikhaliyeva's launch post remain unresolved in the public crawler:

- `https://lnkd.in/eDBMFtdj`
- `https://lnkd.in/e9beCW9w`

The public LinkedIn redirect endpoint is fetch-restricted and exact-short-link web searches only re-index the original LinkedIn post, not the destinations. This subroute is therefore **bounded for now** unless a destination URL becomes visible through a new cache/index/share surface.

## Denominator outcome

No numeric `remaining`, `total`, `cap`, `soldCount`, stock quantity, numerator/denominator, or exact `R` was recovered for `10066 Silver` or `10072 S25` in this batch.

Classification: `NEW_OPERATOR_PRODUCT_MODEL_EVIDENCE_NO_NUMERIC_DENOMINATOR_YET`.

## Decision

- Keep `10066 Silver` as denominator target #1.
- Preserve **N as a free integer optimization variable**.
- Do not treat the word `stok` itself as a numeric denominator.
- Do not repeat generic `1001 Sevinc + stok` searches mechanically; use the product/operations people + partner-channel integration route only when a new indexed artifact appears.

## Next action

Prioritize operator/partner-channel integration artifacts where inventory has to be synchronized across Azerlotereya.com, Misli, Trendyol, and retail/POS. Search specifically for screenshots, product requirements, launch posts, support text, or network/API artifacts exposing a stock/remaining/count field. If exact `R` for `10066` appears contemporaneously with the preserved 33% sold observation, run the Phase 18CF cap solver immediately and compute compatible `C`, `M`, ROI, execution buffer, and maximum positive-EV purchase size with free integer **N**.
