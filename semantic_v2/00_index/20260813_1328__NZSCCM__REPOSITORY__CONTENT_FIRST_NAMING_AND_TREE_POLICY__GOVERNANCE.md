# NZ-SCCM content-first naming and semantic-tree policy

**Timestamp:** 2026-08-13 13:28 +08:00  
**Role:** repository information architecture / naming governance only  
**Theory/result change:** NONE

## 1. Root defect being corrected

The legacy repository mixes current, retained, superseded, rejected, diagnostic and source artifacts under paths such as `current/`, and many filenames contain mutable status words such as `CURRENT`, `FRESH`, `PASS`, `PRODUCTION`, `CLOSURE`, `R01`, `V1`.

Those tokens are locators, not semantic identity. Content and supersession chronology are authoritative.

## 2. Mandatory identity order

For any artifact used in recovery or continuation:

1. read file content;
2. identify what equations/data/code/results it actually contains;
3. identify its self-declared role at creation time;
4. check later supersession/correction/revocation/incorporation;
5. record valid scope and superseded scope separately when only part of a file is outdated;
6. use path/name/timestamp only as locator metadata.

## 3. Canonical filename grammar

New canonical names use:

```text
YYYYMMDD_HHMM__NZSCCM__<SCOPE>__<SPECIFIC_CONTENT>__<ARTIFACT_KIND>.<ext>
```

If a legacy artifact has a known date but no defensible clock time, use:

```text
YYYYMMDD_TUNK__NZSCCM__... 
```

Do not invent `00:00` as an exact time. If even the date is genuinely unknown, use `DATEUNK_TUNK` and preserve commit/source metadata in the manifest.

### 3.1 SCOPE

Use the physical/theoretical object, not its mutable status. Examples:

```text
PROJECT
NC_MATERIAL
NC_REBAR_PANEL
CASE21
SWARTZ24
UHPC_MATERIAL
STEEL_SHELL
PBL
HISTORY_RECOVERY
```

### 3.2 SPECIFIC_CONTENT

Describe what the artifact actually contains. Examples:

```text
R10_N48C1MM_CH_NGUYEN_GENERAL_D15
LIMIT_ROOT_KZ
PU_VS_FAILURE_LOAD
DIRECT_N48_LIMIT_ROOTS_AND_DERIVATIVES
TANGENT_FIDELITY
CASE21_RAW_INPUTS
R10_MATERIAL_COEFFICIENTS_N48C1MM
```

Avoid generic names such as `report`, `new`, `fresh`, `final2`, `updated`, `current` as the content description.

### 3.3 ARTIFACT_KIND

Use a small controlled vocabulary:

```text
GOVERNANCE
THEORY
THEORY_DERIVATION
THEORY_CONTRACT
EXECUTION_CONTRACT
WORKFLOW
INPUT_FREEZE
COEFFICIENT_TABLE
CODE
RESULT_FREEZE
RESULT_TABLE
EXECUTION_REPORT
AUDIT
DIAGNOSTIC
SOURCE_EXCERPT
SOURCE_MAP
SOURCE_REGISTRY
RAW_EXPORT
LOCATOR
RENAME_MAP
SUPERSESSION_MAP
SEMANTIC_MANIFEST
```

## 4. Status is metadata, never filename authority

Canonical filenames must not rely on mutable status words. Current validity is stored in the semantic manifest as one of:

```text
CURRENT_PRIMARY
CURRENT_SUPPORT
CURRENT_RESULT
CURRENT_EXECUTION_INPUT
RETAINED_LINEAGE
PARTIALLY_SUPERSEDED
SUPERSEDED
REJECTED
DIAGNOSTIC_ONLY
AUDIT_ONLY
SOURCE_ONLY
RAW_ARCHIVE
LOCATOR_ONLY
UNKNOWN_NOT_CONTENT_AUDITED
```

A status can change without renaming the artifact, which is precisely why status is not embedded as the decisive part of the filename.

## 5. Partial supersession

Whole-file status is insufficient when only one section became obsolete. The manifest therefore has both:

```text
valid_scope
superseded_scope
superseded_by
```

Example: the 2026-08-12 18:02 Case21 full-closure report retains the current theory root and KZ audit, but its comparison of ultimate load with `336 kN` is superseded by the later failure-load comparison (`Pf≈368.313 kN`). It is therefore `PARTIALLY_SUPERSEDED`, not simply CURRENT or HISTORICAL.

## 6. Semantic directory tree

The canonical role tree is:

```text
semantic_v2/
  00_index/
  10_governance/
  20_theory/
    nc_material/
    nc_rebar_panel/
    uhpc_material/
    steel_shell_pbl/
  30_workflows/
    case21/
    swartz24/
  40_execution/
    case21/
    swartz24/
  50_results/
    case21/
    swartz24/
  60_validation/
    swartz24/
    external_rc_panels/
  70_evidence/
    nc/
    uhpc/
    stability/
    steel_shell_pbl/
    mathematics/
    literature/
  80_history/
    case21/
    d_g_r_routes/
    ucft/
    rejected_routes/
    recovery/
  90_raw/
    conversation_exports/
    original_source_locators/
    preclean_locators/
```

The semantic tree is role-based. `current` versus `history` is no longer the primary information architecture.

## 7. Migration discipline

This reconstruction is non-destructive until content classification is complete enough to preserve provenance.

```text
DELETE_LEGACY_FILE_BEFORE_AUDIT = PROHIBITED
MOVE_BY_FILENAME_GUESS = PROHIBITED
BREAK_EXISTING_PROVENANCE_LINK = PROHIBITED
```

The first pass establishes canonical IDs, a rename map and a supersession map. Physical moves/renames may then be performed with old-path locator stubs or Git-history preservation.

## 8. Source/evidence naming

Primary literature and user-uploaded originals are not renamed to imply project conclusions. Their canonical locator names should preserve author/year/source identity, e.g.:

```text
20260807_TUNK__NZSCCM__UHPC_MATERIAL__HIEW2024_DIRECT_TENSION__SOURCE_LOCATOR.md
20260712_TUNK__NZSCCM__NC_MATERIAL__NGUYEN_THESIS__SOURCE_LOCATOR.md
```

Publication year belongs in `SPECIFIC_CONTENT`; project ingestion/audit time remains the leading timestamp.

## 9. Execution artifacts

Any future successful production run must persist at least:

- exact input snapshot;
- theory/contract identity and commit;
- compiler interval/order/coefficient checksum;
- executable code/hash or exact tool execution record;
- roots and residuals;
- derivatives and limit function;
- material-domain/rebar certificates;
- KZ quantities when requested;
- experiment-isolation flags.

A final Pu table without the run checkpoint is a result artifact, not a resumable execution artifact.

## 10. Immediate naming examples

```text
20260812_2245__NZSCCM__NC_REBAR_PANEL__R10_N48C1MM_CH_NGUYEN_GENERAL_D15__THEORY_EXECUTION_CONTRACT.md
20260812_1734__NZSCCM__CASE21__ZERO_SPATIAL_LIMIT_ROOT_KZ__EXECUTION_CONTRACT.md
20260812_1802__NZSCCM__CASE21__LIMIT_ROOT_AND_KZ__RESULT_FREEZE.md
20260813_0047__NZSCCM__SWARTZ24__PU_VS_FAILURE_LOAD__RESULT_TABLE.csv
20260811_TUNK__NZSCCM__SWARTZ24__DIRECT_N48_LIMIT_ROOTS_AND_DERIVATIVES__RESULT_TABLE.csv
20260811_TUNK__NZSCCM__SWARTZ24__DIRECT_N48_TANGENT_FIDELITY__DIAGNOSTIC.md
```

These canonical names describe immutable content; current/superseded status remains in the manifest.
