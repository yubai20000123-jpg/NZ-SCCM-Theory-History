# Checkpoint — P1 source-text batch 2

**Date:** 2026-08-10

This checkpoint is append-only relative to `2026-08-10_GITHUB_MIGRATION_P0_P1.md`.

## 1. UHPC File-Library-only primary sources now have a strong recovery index

Created:

- `materials/UHPC/sources/PRIMARY_SOURCE_LOCATOR_20260810.md`
- `materials/UHPC/sources/G12_SOURCE_ROLE_LEDGER_RECOVERED.csv`
- `materials/UHPC/sources/README.md`

The locator records exact File Library IDs and public DOI/OA locators for Hiew 2024, Liu 2024, Leutbecher 2020 + Data S1, Lee 2017, Shen 2020, Diab/Ferche 2026 and FHWA-HRT-23-077.

The PDFs are still not claimed as GitHub byte-exact binaries.

## 2. Historical G12 source extractions archived

Created:

- `G12_source_Hiew_2pct_summary.csv`
- `G12_source_Leutbecher_key_MRC2_biaxial.csv`
- `G12_source_Liu2024_sequential_TC.csv`
- `G12_source_Diab_beta_table.csv`

These are historical extracted/source-derived tables, subordinate to the original PDFs. Their historical roles are explicitly preserved:

- Hiew: direct-tension shape/strain anchors;
- Leutbecher: external TC strength/stiffness validation;
- Liu sequential TC: loading-path-dependent evidence, not exact pointwise identity for a path-independent current map;
- Diab/Ferche: synthesis oracle, not original two-dimensional experiment.

`G12_source_Liu2024_peak_coordinates.csv` is deliberately not reconstructed because only partial rows are currently recovered. No incomplete reconstruction is allowed to masquerade as the original historical CSV.

## 3. Attard searchable mirror — FULL

Authoritative PDF:

`BUCKLING OF REINFORCED CONCRETE WALLS Attard UNICIV.pdf`

- PDF SHA-256: `a32fdbd8d397c34f13bd347d12da27438c84b8988fc22e795e3f5a4ba6f9fba6`
- mechanical extraction size: `45300 bytes`
- extracted TXT SHA-256: `7a2b7030d5c0aa26038a8ae20ced6de4b90e643d235fbb93c0a546a524e22542`
- GitHub: `sources_text/stability/Attard_UNICIV/part_01.txt .. part_03.txt`
- status: **FULL_TEXT_MIRROR_MIGRATED_3_PARTS_SHA_MATCH**

A one-byte transfer discrepancy in part 02 was detected during blob verification and repaired before the FULL label was issued.

## 4. Zhang Ning searchable mirror — FULL

Authoritative PDF:

`PBL加劲型矩形钢管混凝土轴压柱局部屈曲性能分析_张宁.pdf`

- PDF SHA-256: `7ae43da9f08d777e8b6a47acfff450ff22929dc7fcdad15fe95d29a5370572c5`
- extracted TXT size: `112471 bytes`
- extracted TXT SHA-256: `3e12d8b2c60f6d9f205887cf7505b16ba76697768b75eabb7b654181cb61ca19`
- status: **FULL_TEXT_MIRROR_MIGRATED_10_SEGMENTS_SHA_MATCH**

Exact reconstruction order is recorded in:

`sources_text/shell_Y/Zhang_Ning_PBL_local_buckling/README.md`

A first `part_02.txt` transfer was found to be one byte short, deleted, and replaced by exact `part_02a/02b/02c` segments. The incorrect transient file is excluded from the reconstruction sequence.

Source/theory boundary is also explicit: Zhang's PBL-as-continuous-elastic-support energy model remains primary historical source evidence, but does not automatically authorize an independent PBL spring-energy or PBL axial-force term in current NZ-SCCM.

## 5. Yun Lu searchable mirror — PARTIAL 6/21

Authoritative PDF:

`考虑薄膜效应的钢箱混凝土壁板局部屈曲行为研究_云露.pdf`

- PDF SHA-256: `1fce0f9ce9058f00b2a6ddd0f6dd11faa41366816e2145348812c1a93884e897`
- mechanical extraction size: `194496 bytes`
- extracted TXT SHA-256: `5dc2c4cdab6329ebed748da8195fc45490e6129c6ebedea3c438a7d39cba3ea0`
- local exact split: 21 newline-boundary chunks, each <= 9496 bytes except the final shorter chunk
- GitHub current status: **PARTIAL_TEXT_MIRROR_MIGRATION 6/21**
- `part_01 .. part_06` Git blob SHAs have been checked and match locally expected Git blob SHAs.

The first six parts already include the thesis identity, abstract, literature review, research plan and the beginning of Chapter 2 (`自由板的小挠度弹性屈曲`). This does not make the thesis FULL. Parts `07..21` remain required before absence in GitHub search can be treated as evidence.

The exact 21-part expected size/blob table is stored in:

`sources_text/shell_Y/Yun_Lu_membrane_local_buckling/README.md`

## 6. Local extraction registry

Created/updated:

- `sources_text/LOCAL_EXTRACTION_MANIFEST_20260810.csv`
- `sources_text/README.md`
- `evidence/inventory_append/20260810_P1_UHPC_G12_SOURCE_TEXT_BATCH.csv`

Current statuses:

```text
Attard     FULL / SHA MATCH
张宁       FULL / SHA MATCH
云露       PARTIAL 6/21 / first six blob SHA match
Nguyen     READY_FOR_TEXT_MIRROR
孙立鹏      READY_FOR_TEXT_MIRROR
```

## Next exact queue

1. Yun `part_07 .. part_21`; verify all blob SHAs, then certify final reassembly against `5dc2c4cd...3ea0`.
2. Nguyen searchable mirror (`455954 bytes`, extracted TXT SHA `cb1bd34c...938f4`).
3. Sun Lipeng searchable mirror (`546279 bytes`, extracted TXT SHA `2c7eda7f...60e92`).
4. Continue File-Library-only UHPC primary-source text mirrors where full original retrieval is technically available.
5. Byte-exact PDF/ZIP migration only when a true binary upload/push channel is available.

## Governing rule

Do not promote a partial mirror to FULL; do not infer absence from a partial mirror; do not promote extracted tables into constitutive truth; do not let a historical source model silently override the current project modelling contract.
