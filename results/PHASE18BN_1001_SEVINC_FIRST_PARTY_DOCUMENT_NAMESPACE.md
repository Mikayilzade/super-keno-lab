# Phase 18BN — `1001 Sevinc` first-party document namespace

Date: 2026-08-28

## Result

Not yet success: registration 316 / 12.05.2025 was not recovered in this batch, but a materially new first-party storage route was identified and validated.

## New evidence

Azərlotereya's official `Keçmiş Oyunlar` page exposes lottery-condition files directly as `.docx` documents. Following one of those first-party links reveals the live storage pattern:

`https://st.azerlotereya.com/public/data/files/WidgetFileController/documents/<2>/<2>/<2>/<2>/<uuid>.docx`

Example observed from the official page:

`https://st.azerlotereya.com/public/data/files/WidgetFileController/documents/Cd/oK/hj/Jh/9_aef3d362-f596-4c57-886b-9d8437b4d336.docx`

This is important because it proves that registered/lottery-condition documents are not necessarily linked from the ordinary game page and can live in a dedicated static document namespace.

The same official `Keçmiş Oyunlar` page currently lists many `.docx` lottery-condition files (`... lotereyasının şərtləri.docx`), confirming that Azərlotereya uses downloadable office documents for formal lottery conditions.

## Search performed

Targeted searches were run for:

- `1001 Sevinc` + registration 316
- `1001 Sevinc` + `docx` / `pdf`
- `1001 Sevinc` + `WidgetFileController/documents`
- `st.azerlotereya.com/public/data/files/WidgetFileController/documents` + `1001 Sevinc`

No indexed `1001 Sevinc` conditions file surfaced. The current `1001 Sevinc` page also exposes no visible PDF/DOCX link.

## Interpretation

This materially narrows the archival branch:

1. `WidgetFileController/documents` is now a proven first-party document namespace and should be treated as the primary static-storage target.
2. Search-engine indexing of this namespace is weak or absent for `1001 Sevinc`; repeated generic text search is therefore low-value.
3. A future hit should be accepted only if document content or surrounding metadata binds it to registration 316 / 12.05.2025 or clearly to `1001 Sevinc`.
4. A recovered ticket quantity/range still must be classified by scope: whole lottery, category, draw, or issuance batch before it can be used for `10066` or `10072`.
5. The §2.2.5 sold-dependent-prize-fund exception remains unresolved until the actual registered conditions or amendment is recovered.

## Closed / do-not-repeat

Do not repeat generic web searches for the May-2025 launch text or ordinary current game-page detail. Do not brute-force random UUID paths: the namespace uses high-entropy UUID filenames and this would be both inefficient and unsupported by evidence.

## NEXT ACTION

Prioritize discovery of metadata or archived page payloads that reference `WidgetFileController/documents` around 12–15 May 2025, including old CMS/page JSON, sitemap/search-index artifacts, and any first-party condition-document listing that may have once linked `1001 Sevinc`. If a file is recovered, inspect it first for registration number/date, ticket quantity/range, prize-fund model, and amendment history. Preserve free integer N; do not stake or run paid probes.