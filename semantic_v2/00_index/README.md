# NZ-SCCM semantic tree v2

This namespace is the **content-first, non-destructive semantic reconstruction** of the repository.

## Current operational entry

Use first:

`20260818_1201__NZSCCM__PROJECT__CURRENT_STATE_STEEL_SHELL_SOURCE_CONSISTENT_OPERATOR_GATE__SEMANTIC_INDEX.md`

The active technical gate is now the steel-shell same-source plane-stress current operator:

```text
exact production steel stress update
 -> sigma_s(epsilon) + same-source Ct_s(epsilon)
 -> independent local full-map derivative audit
 -> Ct_s(X,Y,z) into KZ_s^mat + current-stress KZ_s^geo
 -> same operator in P,Rq,RA,KZ,L
 -> Z1/Z4 rerun
 -> Z0-Z5 batch
 -> global / Phase-C hard gate
 -> production Pu freeze only after PASS
```

The 20260816 N48 membrane-production entry and the 20260817 true-infinite Case21/Z6 checkpoints remain retained historical/theoretical evidence, but they no longer define the current execution stop point.

## Current controlling steel-shell audit

`../40_execution/steel_shell/20260817_2342__NZSCCM__Z0_Z5__STEEL_LOCAL_YIELD_SEQUENCE_AND_TANGENT_RECALC_AUDIT.md`

Key status:

```text
CENTER_FIRST_LOCAL_YIELD_FRONT = ESTABLISHED_FOR_Z0_TO_Z5
CURRENT_RADIAL_CAP_TANGENT_PHYSICAL_ACCEPTANCE = FAIL / NOT PRODUCTION-FROZEN
OLD_Z0_TO_Z5_Pu_FULL_STEEL_TANGENT_PRODUCTION_CERTIFICATE = NOT PASSED
TANGENT_ONLY_IDEAL_J2_SUBSTITUTION = AUDIT ONLY
NEXT = SAME-SOURCE PLANE-STRESS STEEL OPERATOR FREEZE
```

## Short current pointer

Also read:

`../../current/CURRENT_STATE.md`

That file is intentionally kept short so the detailed current-state identity lives in one timestamped semantic artifact rather than being duplicated and drifting again.

## Repository semantic read order

1. this `README.md`;
2. the current operational entry above;
3. `../../current/CURRENT_STATE.md`;
4. the controlling leaf audit/execution artifact named by the current state;
5. `20260813_1328__NZSCCM__REPOSITORY__CONTENT_FIRST_NAMING_AND_TREE_POLICY__GOVERNANCE.md`;
6. `20260813_1328__NZSCCM__REPOSITORY__CONTENT_SEMANTIC_TREE__SEMANTIC_MANIFEST.md`;
7. `20260813_1328__NZSCCM__REPOSITORY__ARTIFACT_SUPERSESSION__SUPERSESSION_MAP.csv`;
8. legacy/source files only through their semantic locator/provenance chain.

## Identity discipline

```text
PATH_NAME_ONLY_CLASSIFICATION = PROHIBITED
LEGACY_CURRENT_DIRECTORY_SEMANTIC_PURITY = FALSE
CONTENT_AUDIT_BEFORE_USE = REQUIRED
NON_DESTRUCTIVE_HISTORY = REQUIRED
```

A filename containing `current`, `production`, `PASS`, or a later date does not by itself establish governing status. Current identity is determined by content, direct audit, and the supersession/revocation chain.

## Formal production boundaries retained

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
PRODUCTION_TRUTH = Stage3/Stage4 only
FULL_24_PANEL_PRODUCTION_RELEASE = BLOCKED until hard model-path gates pass
```

No legacy file is deleted, moved, or renamed solely from filename identity.
