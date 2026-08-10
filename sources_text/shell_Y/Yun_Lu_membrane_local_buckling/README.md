# 云露 — 考虑薄膜效应的钢箱混凝土壁板局部屈曲行为研究

## Evidence identity

- authoritative PDF: `考虑薄膜效应的钢箱混凝土壁板局部屈曲行为研究_云露.pdf`
- PDF pages: `81`
- PDF size: `6109981 bytes`
- PDF SHA-256: `1fce0f9ce9058f00b2a6ddd0f6dd11faa41366816e2145348812c1a93884e897`
- extraction method: `pdftotext -layout`
- extracted TXT size: `194496 bytes`
- extracted TXT SHA-256: `5dc2c4cdab6329ebed748da8195fc45490e6129c6ebedea3c438a7d39cba3ea0`

The PDF is authoritative. These TXT parts are only a searchable mechanical extraction.

## Exact chunk plan

The local extracted TXT was split at existing newline boundaries into 21 ordered chunks. Local concatenation of all 21 chunks exactly reproduces the extracted TXT SHA-256 above.

Expected sizes / Git blob SHAs:

| part | bytes | expected Git blob SHA |
|---|---:|---|
| 01 | 9451 | `b335e08f3928d9cb202277c48fd9498f2fb585e2` |
| 02 | 9443 | `c88c28b6b864497483c264ccfc4c8569cf06f25c` |
| 03 | 9406 | `55a47a58cc2ec7d63b058d0b4a32b9bac6c26c9e` |
| 04 | 9408 | `ed4283d75ea3c240b2b9bdbd00907e5e624da7c7` |
| 05 | 9486 | `ed45edca814e6740f45585f4b7108d3ce6672ad3` |
| 06 | 9403 | `06901967b57d18f2be759f4e168c3006fe1e603d` |
| 07 | 9474 | `c0ada4fe872f201ef2cd944b59699b52dc826cce` |
| 08 | 9377 | `f4fa1d3efc3a80489bcbf075d9a9043f0e9c7d5f` |
| 09 | 9446 | `31766324fbcf47df3d1d825d90609300fbe2fd28` |
| 10 | 9452 | `18094db3707be862fcef8054579f4569c741fe5f` |
| 11 | 9490 | `51ef8c14fd800aafe68fd3bdc3c64f68f7055776` |
| 12 | 9426 | `000b0514695d862e095f6b408fb98a9a88d7b0b7` |
| 13 | 9450 | `033c5478d18cd9d05040b3ae448735b87bbc1e11` |
| 14 | 9451 | `591850e777a0fe7ae14c8dfafe8ec5d51af0309f` |
| 15 | 9446 | `3edb44b868c9be291ff6476a6a48e95258bb7ad2` |
| 16 | 9496 | `d29f9023a66976b1166984f640635a78b9bf4fa0` |
| 17 | 9432 | `188ef0ed0f2696fbf18a325306a25b3f3fd43308` |
| 18 | 9391 | `9c83bbd8192781aa93c12909094c639431cdd881` |
| 19 | 9471 | `8c1b986725cf58091bf5f3edda179a75f8626620` |
| 20 | 9426 | `78ac8bcd53ff5d5365b413533cdcd4d5d34af366` |
| 21 | 5671 | `b1ab9a99c563eacc08b8e3fea548bf9a917082cc` |

## Current migration status

**PARTIAL_TEXT_MIRROR_MIGRATION 6/21 — first six Git blobs SHA-verified.**

`part_01.txt` through `part_06.txt` are present and their Git blob SHAs match the locally computed expected values above. Parts `07..21` are pending. Until all 21 are present and the final reconstruction is certified, a missing GitHub search hit must not be interpreted as absence from the thesis.

## Project source role

This thesis is primary source material for the Y / steel-shell branch, especially:

- unilateral constraint: concrete blocks inward wall-panel buckling, so the steel wall develops outward deformation;
- Kármán large-deflection / membrane-action post-buckling theory;
- assumed deflection field, stress-function construction and Galerkin solution;
- influence of length-width ratio, width-thickness ratio and geometric imperfection;
- analytical / finite-element comparison;
- effective-width derivation and later empirical correction.

## Current-theory boundary

The project preserves Yun's large-deflection mechanics and source formulas as theory material, but **does not automatically adopt her empirical effective-width correction coefficient as the formal NZ-SCCM operator**. Any later Y-shell integration must distinguish source derivation, validation formula and current formal modelling assumptions.
