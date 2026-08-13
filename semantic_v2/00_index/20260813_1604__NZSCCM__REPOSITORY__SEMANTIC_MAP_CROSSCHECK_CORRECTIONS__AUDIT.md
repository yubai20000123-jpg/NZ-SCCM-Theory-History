# NZ-SCCM semantic-map cross-check and correction overlay

**Timestamp:** 2026-08-13 16:04 +08:00  
**Role:** repository information architecture / metadata audit only  
**Theory/result change:** NONE

## 1. Scope

Cross-check the 13:28 semantic manifest, rename map, supersession map and actual `semantic_v2` tree after the interrupted reconstruction.

## 2. Structural gaps found and resolved in this completion commit

Exactly five declared leaf branches lacked `_SEMANTIC_BRANCH_INDEX.md` while their siblings already had one:

```text
semantic_v2/30_workflows/case21/
semantic_v2/40_execution/case21/
semantic_v2/50_results/case21/
semantic_v2/50_results/swartz24/
semantic_v2/80_history/d_g_r_routes/
```

All five branch indexes are added in the same commit as this audit.

`semantic_v2/80_history/case21/_SEMANTIC_BRANCH_INDEX.md` previously stated that the branch contained canonical locators while the directory contained only the index. Selected high-risk Case21 lineage locators are now added and the branch index is made explicit.

## 3. Locator coverage correction

The pre-interruption tree already contained the primary locators for:

- NC+rebar 22:45 production contract;
- Case21 execution contract;
- Case21 raw inputs and final coefficient table;
- Case21 current theory/result freezes;
- Swartz24 current Pu/Pf table and completion report;
- checkpoint governance;
- the misleading old direct-N48 Swartz24 root table.

This completion adds locators for the current-state pointer, key current-support theory/material/governance objects, the unique limit-root production contract, and high-risk superseded/correction lineage needed to interpret the supersession graph.

Locator coverage is therefore sufficient for current-chain navigation and high-risk supersession recovery, but it is not claimed to be one-locator-per-every-B/C-level source/history leaf.

## 4. Cross-map discrepancies

### 4.1 Supersession path typo

The 13:28 supersession map contains:

```text
govenance/N48_C1_VALUE_TANGENT_REPAIR_DECISION_20260811.md
```

The actual repository path and authoritative interpretation are:

```text
governance/N48_C1_VALUE_TANGENT_REPAIR_DECISION_20260811.md
```

This is a path typo only; it does not change the repair chronology.

### 4.2 `canonical_id` namespace shorthand in the 13:28 audited-artifact CSV

The `canonical_id` column in the 13:28 audited-artifact CSV systematically omits the `NZSCCM` namespace token that is required by the naming policy and is present in canonical filenames/locator bodies.

Authoritative normalization rule:

```text
AUDITED_MANIFEST_CANONICAL_ID
= shorthand metadata only

FULL_CANONICAL_ID
= canonical filename stem / locator Canonical ID
= YYYYMMDD_HHMM__NZSCCM__<SCOPE>__<SPECIFIC_CONTENT>__<ARTIFACT_KIND>
```

No theory/status interpretation is changed by this normalization.

### 4.3 Supersession endpoints not represented in the 13:28 rename-map coverage

Two direct-read relation endpoints used by the supersession map were not represented in the inspected 13:28 rename-map coverage:

1. `current/governance/NZ_SCCM_NC_R1_LIMIT_ROOT_PRODUCTION_CONTRACT_V1_20260812.md`
2. `governance/REVOCATION_WRONG_GLOBAL_ENERGY_POTENTIAL_GATE_20260810.md`

Canonical locators for both are added in this completion commit. Until a consolidated rename-map v2 is generated, these two locator entries plus this audit are the authoritative overlay for those endpoints.

## 5. Consistency verdict

```text
SEMANTIC_TREE_DECLARED_VS_ACTUAL_BRANCHES = PASS_AFTER_COMPLETION
PRIMARY_CURRENT_LOCATOR_NAVIGATION = PASS_AFTER_COMPLETION
PARTIAL_SUPERSESSION_CASE21_336KN_VS_Pf = CONSISTENT
DIRECT_N48_CURRENT_STATUS = CONSISTENTLY_SUPERSEDED
SUPERSESSION_PATH_SPELLING = PASS_WITH_THIS_OVERLAY
CANONICAL_ID_NAMESPACE = PASS_WITH_NORMALIZATION_OVERLAY
RENAME_MAP_RELATION_ENDPOINT_COVERAGE = PASS_WITH_TWO-ENDPOINT_OVERLAY
THEORY_CHANGED = NO
RESULT_CHANGED = NO
```

The 13:28 files remain preserved as an auditable snapshot. This 16:04 overlay controls only metadata/path/canonical-ID interpretation where the older maps differ.
