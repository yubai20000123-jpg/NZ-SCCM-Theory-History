# Copy-only migration Batch 01 audit

Time basis: 2026-08-13 16:27 +08:00

## Scope

This batch physically instantiates canonical semantic_v2 copies for the smallest self-contained chain needed to preserve the current successful theory and diagnose the later accuracy-degradation concern:

- current integrated NC+rebar production theory;
- current mechanics/formal/root/compiler support;
- Case21 workflow, input, coefficients and result freeze;
- current Swartz24 Pu-vs-failure result set;
- old direct-N48 Swartz24 result and tangent/C1-repair lineage for before/after comparison;
- current-state snapshot.

## Copy identity

Every migrated legacy artifact in the manifest is installed at its canonical path by reusing the exact legacy Git blob SHA.

```text
BYTE_IDENTICAL_COPY = YES
LEGACY_PATH_PRESERVED = YES
SOURCE_BLOB_SHA_CHANGED = NO
THEORY_BODY_REWRITTEN = NO
NUMERICAL_RESULT_CHANGED = NO
```

The only newly authored files in this commit are repository-governance/manifest/audit metadata.

## Known intentional gaps

- This is not yet a complete copy of all PDFs, raw archives, UHPC evidence, steel-shell/PBL evidence or every historical D/G/R artifact.
- Missing or low-value historical files do not block recovery; they may remain unmigrated or be recomputed if needed.
- The partially-superseded Case21 full-closure body is preserved byte-identically; its adjacent locator remains authoritative for valid versus superseded scope.
- The R10 20260810 lineage file contains a historical structural-Gauss subsection. Its canonical status remains CURRENT_SUPPORT only for material-target lineage; that subsection is not promoted into the formal production operator.

## Gate

```text
COPY_ONLY_MIGRATION_BATCH01 = PASS
CURRENT_SUCCESSFUL_THEORY_PHYSICALLY_PRESERVED = YES
DEGRADATION_COMPARISON_BASELINE_PHYSICALLY_PRESERVED = YES
DESTRUCTIVE_MIGRATION = NO
NEXT_PRIORITY = COMPARE_OLD_DIRECT_N48_VS_CURRENT_C1MM_GENERAL_D15_AND_ISOLATE_WHERE_PU_SHIFT_ENTERED
```
