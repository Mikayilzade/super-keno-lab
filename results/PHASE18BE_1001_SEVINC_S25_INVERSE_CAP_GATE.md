# Phase 18BE — S25 inverse cap gate under missing fresh sell-through

Date: 2026-08-28

Status: **NO EXECUTABLE +EV YET; fresh S25 sell-through still unresolved.**

## Fresh-source result

A fresh first-party crawl of the current `1001 Sevinc` surface still exposes only the first current card in the search/index layer: iPhone 17 Pro 256 GB Cosmic Orange, 1 AZN, draw date 16.09.2026, sold 43%. Targeted fresh searches for `Samsung Galaxy S25 Ultra Black`, `drawId=10072`, `iPhone 17 Pro 256 GB Silver`, `10066`, and `qalan bilet / remaining / sold-count` did **not** produce a new complete first-party execution record.

The current parent page still confirms the 11 draws dated 16.09.2026 (3 x 1 AZN, 8 x 0.5 AZN). The public blog/explainer still confirms that the user-facing client can show how many tickets remain until a draw, but that absolute value is not surfaced to the public crawler.

Therefore the several-days-old S25 ~41% observation remains monitoring-only and is not promoted back to live execution input.

## Inverse decision gate for `drawId=10072 / S25 Ultra Black`

Instead of repeatedly using a stale sold fraction, this checkpoint inverts the finite-pool condition.

Assumptions:
- ticket price `p = 0.5 AZN`;
- market/liquidation reference `V = 2,050 AZN`;
- standing conservative property-prize tax model:
  `V_net = h*V - 0.14*(V-p)`;
- `h` = usable/resale-value fraction;
- if total ticket cap is `C`, positive expectation requires:
  `sold_fraction < V_net / (p*C)`.

### Maximum sold fraction compatible with break-even

| total cap C | 60% usable | 70% usable | 80% usable | 100% usable |
|---:|---:|---:|---:|---:|
| 4,000 | 47.15% | 57.40% | 67.65% | 88.15% |
| 5,000 | 37.72% | 45.92% | 54.12% | 70.52% |
| 6,000 | 31.44% | 38.27% | 45.10% | 58.77% |
| 7,500 | 25.15% | 30.62% | 36.08% | 47.02% |
| 10,000 | 18.86% | 22.96% | 27.06% | 35.26% |

## Interpretation

This gives a faster promotion rule once a fresh S25 sold percentage reappears:

- if fresh S25 is around **40–42%**, a 60%-usable conservative case is positive only if cap is below roughly **4.5k–4.7k**;
- at the same sold level, a 70%-usable case tolerates cap around **5.5k**;
- at 80% usable value, cap can be roughly **6.4k–6.8k**;
- a cap near **10k** would already require sold fraction below ~27% even at 80% usable value, so a reappearance near 40% would largely kill that cap scenario.

This does **not** infer the actual cap. It only turns the next fresh sold observation into an immediate go/no-go screen before more denominator effort.

## New-source scan

A fresh scan for current zero-cost / free-entry offers explicitly naming `Lotereya` did not reveal a new actionable modifier. The old `Sürətli Şans` page remains a historical 2025 campaign and is not current evidence.

## Decision

- `10066 Silver` remains the freshest fully bound execution record at 33% sold.
- `10072 S25` remains potentially economically superior because of its 0.5-AZN ticket, but **cannot be promoted without fresh sold%**.
- No purchase is justified without an absolute cap / remaining / sold-count or another defensible denominator bound.

## Next action

1. Continue looking only for materially new current-cycle rendered/account/client evidence exposing S25 sold% or absolute remaining/cap.
2. If a fresh S25 sold% appears, apply the inverse table immediately; if it is incompatible with plausible caps under conservative 60–70% usable value, deprioritize S25 rather than continuing denominator search blindly.
3. Continue denominator search for `10066 Silver` in parallel because its 33% execution record remains fresh and bound.
4. Do not reopen generic API/registry/Trendyol/local-download routes without materially new surface evidence.
5. Keep N free for any later Super-Keno bonus-conversion portfolio.
