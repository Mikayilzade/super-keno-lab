# Phase 18AK — current-cycle multi-prize live sell-through snapshot

Date: 2026-08-27

Status: **NO POSITIVE-EV CLAIM; LIVE SELL-THROUGH EVIDENCE EXPANDED.**

## Why this batch matters

The current 16.09.2026 `1001 Sevinc` cycle is now sufficiently indexed by first-party Azerlotereya/Misli search surfaces to expose multiple prize names and `Satıldı` percentages. This gives a time-bound live state and, for some prizes, a short sell-through trajectory. It still does **not** expose the predetermined absolute ticket cap / remaining count required for a defensible ROI calculation.

All observations below are bound to the current draw date **16.09.2026** and the observation/search-crawl dates. Do not combine them with older completed cycles.

## Current first-party sell-through observations

### 1 AZN iPhone draws

Azerlotereya current-cycle index, crawled 2026-08-27:

| prize | ticket price | current sold |
|---|---:|---:|
| iPhone 17 Pro 256 GB Cosmic Orange | 1 AZN | **43%** |
| iPhone 17 Pro 256 GB Deep Blue | 1 AZN | **35%** |
| iPhone 17 Pro 256 GB Silver | 1 AZN | **32%** |

Misli index, crawled about three days earlier, exposed approximately:
- Cosmic Orange **41–42%**;
- Deep Blue **33–34%**.

Because search-index crawl timing is coarse, treat the exact elapsed interval as approximate rather than a precise timestamp. Nevertheless, both first-party surfaces are directionally consistent with roughly **+1 to +2 percentage points** of additional sales over a few days.

The exact mapping of Cosmic / Deep Blue / Silver to draw IDs `10065 / 10064 / 10066` is **still not proven**. Do not infer it from card ordering alone.

### 0.5 AZN draws currently exposed

Azerlotereya current index:

| prize | ticket price | current sold |
|---|---:|---:|
| PlayStation 5 Slim 1 TB | 0.5 AZN | **55%** |
| Samsung Galaxy S25 Ultra Black | 0.5 AZN | **42%** |
| 1000 AZN-lik Hədiyyə Kuponu | 0.5 AZN | **17%** |
| iPad Air 13-inch (M2) Starlight 128GB | 0.5 AZN | **26%** |

Misli, crawled about three days earlier, showed:
- PS5 Slim **53%**;
- Samsung Galaxy S25 Ultra Black **41%**;
- 1000-AZN gift coupon **16%**.

Thus the live-index trajectory again moves in the expected direction by roughly +1–2 percentage points over a few days.

The remaining four 0.5-AZN current prizes are not safely identified in this batch and are not guessed.

## New economic implication — waiting has a measurable cost

For a finite-pool single-prize draw with ticket price `p`, net realizable prize value `V_net`, cap `C`, and sold fraction `s`, expected-value break-even requires:

`C < V_net / (p * s)`.

Therefore as `s` rises, the maximum cap compatible with positive EV falls proportionally. A prize that looks potentially attractive at 30–40% sold can become unattractive by the scheduled draw even if the cap itself never changes.

### Cosmic Orange example

At current `s = 0.43`, previously established cap thresholds using the 3,289 AZN retail benchmark are approximately:
- 60% net-value haircut: cap < **4,589**;
- 70%: cap < **5,354**;
- 80%: cap < **6,119**;
- 100% retail ceiling: cap < **7,649**.

If the recent ~1–2 percentage-point / few-days sell-through persists and the draw reaches roughly 55–57% sold by the scheduled cutoff, the compatible cap thresholds shrink materially. At `s = 0.56` they become approximately:
- 60% net value: **3,524**;
- 70%: **4,111**;
- 80%: **4,699**;
- 100% ceiling: **5,873**.

This is **not a forecast of final sales**; it is a sensitivity illustration showing that denominator recovery is time-sensitive.

### 1000-AZN gift coupon — useful exact face-value diagnostic

At current `s = 0.17`, `p = 0.5 AZN`, and face value 1,000 AZN, a no-haircut ceiling would permit break-even only if:

`C < 1000 / (0.5 * 0.17) = 11,764.7` tickets.

With a 20% haircut to reflect redemption/resale/usage friction (`V_net=800`), the threshold is about **9,412** tickets.

Again, these are cap thresholds, not evidence that the actual cap is below them.

## Source snapshot

First-party surfaces checked in this batch:
- Azerlotereya `1001 Sevinc / tirajlar`, current index crawl 2026-08-27.
- Misli `1001 Sevinc / tirajlar`, indexed/crawled approximately three days earlier.
- Azerlotereya parent page confirming 11 current draws dated 16.09.2026.

The current first-party parent HTML itself still renders the draw cards as client-loaded shells to the crawler; prize/sold-percent detail is being recovered from search-index rendering rather than the static opened page.

## Decision

1. `1001 Sevinc` remains the strongest materially different finite-pool route, but **no stake is justified yet** because absolute cap/remaining is unknown.
2. The route has become more time-sensitive: live sold percentages are increasing.
3. Do not use percent alone to claim positive EV.
4. Do not map draw IDs to prize names by ordering alone.
5. Continue searching for predetermined cap / remaining count through rendered/index/client/account/regulatory surfaces.
6. Record future sold-percent snapshots because a short time series can bound sales velocity and help decide whether a recovered cap is still actionable.
