# Phase 4 — operational mechanics and physical-bias audit

Date: 2026-08-24

Status: **NO EDGE CONFIRMED**. Mechanism model materially improved; two weak physical/regime leads retained. Final 35-row holdout remains sealed.

## 1. Mechanism conclusion changed

Phase 4 found substantially stronger evidence that televised Super Keno belongs to a **physical lototron / physical-ball draw process**, not a pure software-RNG model.

Evidence chain:

- Azerbaijani draw-lottery regulations explicitly require fair/correct lototron operation, equal-weight/size/shape draw items, visible automatic mixing and sealed/closed storage between uses.
- A 2022 media tour specifically covering the studio for Mega 5/36, 4+4 and Super Keno reports pre-draw equipment testing, ball weighing, gloves to avoid contaminating ball weight, French **Akanis Technologies** machines, and backup lototron/equipment.
- Akanis states it manufactures air-mix lottery draw machines and ball sets; PC control, audit logging and optional RFID are available.

Exact current machine model, ball-set identity/rotation and RFID mode are **not yet known**, so no physical-bias claim is made from manufacturer capabilities alone.

Full evidence ledger: `research/OPERATIONAL_MECHANICS_2026-08-24.md`.

## 2. Correction to Phase 3 regime assumption

The current rule registration effective **2025-01-10** is **not accepted as a mechanical regime boundary**.

Official Azərlotereya TV draw sequence is continuous around the date: 25024 (Jan 9), 25025 (Jan 10), 25026 (Jan 11), 25027 (Jan 12). Super Keno also existed/broadcast well before 2025.

Therefore the earlier provisional Phase 3 exclusion of pre-2025-01-10 rows is superseded for mechanical-regime research. Those rows may still differ administratively, but they are not labelled a different machine regime without independent evidence.

## 3. Time discrepancy demoted

Official current TV schedule: **19:45** daily.

Current results metadata: **18:45** for Super Keno. But the same results page also shows 18:45 for Beşdə 5 and 4+4. Therefore the one-hour mismatch is treated as a likely site-wide metadata/timezone/display offset, not a Super Keno-specific edge.

Historical schedule changes still exist (the 2022 media tour described a 20:30 broadcast) and will be catalogued separately from machine changes.

## 4. Physical-frequency audit on exposed data only

Reproducible code: `experiments/phase4_physical_regime_audit.py`.
Raw output: `results/phase4_physical_regime_audit.json`.

Rows used: first **160 already-exposed draws** only. Final rows 160..194 remain sealed.

With 160 fair 20-of-70 draws, expected appearances per number = **45.714**.

Observed:

- coldest number: **4**, 24 appearances;
- hottest number: **45**, 58 appearances;
- max-min range: **34**, 1,000-simulation adjusted fair-control p ≈ **0.052**;
- maximum absolute single-number deviation: **21.714**, scan-adjusted Monte Carlo p ≈ **0.011**;
- global chi-like statistic: **54.03**, Monte Carlo p ≈ **0.909**.

Interpretation: the complete 70-number distribution does **not** look globally abnormal, but one extreme low-frequency number creates a legitimate follow-up lead.

### Number 4 independent check

In the first 120 design rows, number 4 appeared **16 times** versus fair expectation ≈34.29. This looks extreme after discovery, but discovery scanned all 70 numbers so the naive single-number p-value cannot be treated as a clean prospective test.

In the already-exposed next 40 diagnostic rows, number 4 appeared **8 times** versus fair expectation ≈11.43. Direction remains low, but the preselected one-sided diagnostic p is only about **0.15**.

Verdict: **H-PHY-01 remains open but does not pass the signal gate**.

Design-coldest ten and diagnostic counts are saved in the JSON. The first five were 4, 19, 64, 1, 38.

## 5. Hard-exclusion monetary stress test

A second reproducible experiment is stored in `experiments/phase4_cold_exclusion_test.py`. It uses the frozen Phase 2 robust search configuration and changes only the allowed ticket universe.

Previously reproduced diagnostic results:

| Candidate universe | Selected N | diagnostic min return | diagnostic avg return | profitable draws |
|---|---:|---:|---:|---:|
| unrestricted Phase 2 | 203 | 0.2759 | 0.7393 | 12.5% |
| exclude #4 | 281 | 0.3167 | 0.4944 | 2.5% |
| exclude 4,19,64 | 228 | 0.3026 | 0.5103 | 5.0% |
| exclude 4,19,64,1,38 | 239 | 0.2510 | 0.5067 | 5.0% |

Avoiding #4 slightly improves the single worst diagnostic ratio, but destroys average return and profitable-draw share. Broader exclusions are also worse overall.

Verdict: **do not convert the cold-ball lead into a betting rule yet**.

## 6. Change-point scan

Using adjacent accepted-row windows and 1,000 fair 20-of-70 simulations with the maximum cut selected inside each simulation:

| window per side | strongest exposed cut | statistic | adjusted MC p |
|---:|---|---:|---:|
| 10 | 2026-06-01 → 2026-06-02 | 4.620 | 0.070 |
| 15 | 2026-06-01 → 2026-06-02 | 2.951 | 0.149 |
| 20 | 2026-06-05 → 2026-06-06 | 2.005 | 0.505 |
| 30 | 2026-05-05 → 2026-05-06 | 1.164 | 0.897 |

The short-window hint near **2026-06-02** is worth checking against video/equipment metadata, but absence of support at longer windows means it is **not a statistical regime boundary** by itself.

Verdict: **H-REG-01 weak lead only**.

## 7. Phase 4 hypothesis decisions

- `H-MECH-01` pure software-RNG working model: **downgraded/rejected on current evidence**; physical lototron is better supported.
- `H-RULE-01` Jan-10-2025 mechanical reset: **rejected as unsupported**.
- `H-TIME-01` Super-Keno-specific 18:45 shift: **rejected as game-specific clue**.
- `H-PHY-01` persistent ball/set bias, especially number 4: **open, not confirmed**.
- `H-REG-01` early-June-2026 operational change: **open weak lead, not confirmed**.

## 8. Holdout decision

**Do not open the final 35 draws.** Neither the #4 hypothesis nor the June change-point hint is strong enough yet. Spending the holdout now would mostly create another retrospective story.

## Next phase

Phase 5 should build a **draw-video / equipment-set metadata ledger** and use it to define physical regimes before more number optimization:

1. inspect official historical draw videos around known dates, especially 2025-01-09..12 and 2026-05-20..06-15;
2. record machine appearance/model clues, ball-set appearance, studio/layout, draw sequence, presenters and interruptions;
3. find exact Akanis model and any evidence of multiple ball sets, rotation/replacement policy, RFID/number recognition and backup-machine substitutions;
4. search official reports/news for technical interruptions or equipment/studio changes;
5. expand older contiguous draw history where possible to increase independent physical-bias sample size;
6. only after an externally defined physical regime exists, retest number 4 / other ball identities and feed any confirmed signal to the free-N robust portfolio layer.
