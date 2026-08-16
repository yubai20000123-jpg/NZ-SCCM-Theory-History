# NZ-SCCM semantic tree v2

This namespace is the **content-first, non-destructive semantic reconstruction** of the repository.

A legacy path or filename is a locator only. It does not confer current/superseded/rejected identity.

## Current operational entry

Use first:

`20260816_1043__NZSCCM__PROJECT__CURRENT_STATE_Z0_Z6_AR2_SSSS_CAPACITY_MATRIX__SEMANTIC_INDEX.md`

## Current locked status

```text
PRODUCTION_BOUNDARY = THEORETICAL_FOUR_EDGE_SIMPLY_SUPPORTED
ZHOU_FE_UX_UY_IMPLEMENTATION = OUT_OF_SCOPE_FOR_PRODUCTION

ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
Nguyen second-order kinematics = ACTIVE
R10/N48-C1-MM/Cayley-Hamilton = ACTIVE
General D15 exact moments = ACTIVE
A0=a/500
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1

free p20,p02 membrane DOFs = RETIRED
PF/end-warp/axial-trace FE corrections = NOT USED IN SSSS PRODUCTION
Zhou/Winter calibration = NO

Z6_AR2_USER_ACCEPTED_Pu = 51.30 MN
```

## Current controlled AR2 capacity matrix

Z0–Z5 are modified only by setting physical `a/b=2`; all retain source section/material parameters. Every modified case has `m*=2`, `ell=b`, `q0=.004`.

|Case|NZ-SCCM Pu (MN)|Zhou (MN)|Winter (MN)|NZ−Zhou|NZ−Winter|
|---|---:|---:|---:|---:|---:|
|Z0|33.4910|36.9455|41.5008|-9.35%|-19.30%|
|Z1|19.7360|23.7214|26.1001|-16.80%|-24.38%|
|Z2|35.9781|41.2134|45.7333|-12.70%|-21.33%|
|Z3|39.6889|44.3203|49.0469|-10.45%|-19.08%|
|Z4|63.7385|69.3399|79.3861|-8.08%|-19.71%|
|Z5|14.7824|14.6816|14.6816|+0.69%|+0.69%|
|Z6|51.30|49.4868|50.1859|+3.65%|+2.21%|

Modified Z0–Z5 all have `Pcr>Pyth`, while accepted Z6 has `Pcr<Pyth`; later interpretation must distinguish the material-strength-dominated modified objects from the buckling/postbuckling-dominated Z6 object.

## Repository semantic read order

1. `20260816_1043__NZSCCM__PROJECT__CURRENT_STATE_Z0_Z6_AR2_SSSS_CAPACITY_MATRIX__SEMANTIC_INDEX.md`
2. `../10_governance/20260816_1043__NZSCCM__Z0_Z6_AR2_FOUR_EDGE_SSSS_COMPARISON_SCOPE__LOCK.md`
3. `../40_execution/steel_shell/20260816_1043__NZSCCM__Z0_Z5_AR2_SSSS_FULLSECTION_CAPACITY__EXECUTION_REPORT.md`
4. `../40_execution/steel_shell/20260816_1043__NZSCCM__Z0_Z5_AR2_SSSS_FULLSECTION__PARAMS_BRANCH_AND_INTERMEDIATES.json`
5. `../40_execution/steel_shell/20260816_1043__NZSCCM__Z0_Z5_AR2_SSSS_ZHOU_WINTER__COMPARISON.csv`
6. `../40_execution/steel_shell/20260816_1043__NZSCCM__Z0_Z5_AR2_SSSS_FULLSECTION__REPRO.py`
7. `../60_validation/steel_shell/20260816_1043__NZSCCM__Z0_Z5_AR2_SSSS_ZHOU_WINTER_COMPARISON__AUDIT.md`
8. `20260816_0249__NZSCCM__PROJECT__CURRENT_STATE_Z6_AR2_SSSS_CAPACITY__SEMANTIC_INDEX.md` — accepted Z6 base
9. `20260816_0121__NZSCCM__PROJECT__CURRENT_STATE_ZHOU_AXIAL_END_ASYMMETRY_GATE__SEMANTIC_INDEX.md` — preserved historical FE-boundary detour; superseded for production
10. `20260816_0007__NZSCCM__PROJECT__CURRENT_STATE_CLASSICAL_ELASTIC_POSTBUCKLING_LIMIT_GATE_PASS__SEMANTIC_INDEX.md`
11. `20260813_1328__NZSCCM__REPOSITORY__CONTENT_FIRST_NAMING_AND_TREE_POLICY__GOVERNANCE.md`

## Audit levels

- `A_DIRECT_CONTENT_AUDIT`: file body opened/read; identity derived from content + chronology.
- `B_CONTENT_DERIVED_REGISTRY_OR_LEDGER`: stable source/history role derived from a content-read registry/ledger; open the leaf before using it for a technical claim.
- `C_NOT_YET_DIRECT_CONTENT_AUDITED`: locator known, semantic identity not yet asserted beyond family/locator role.

## Canonical naming

`YYYYMMDD_HHMM__NZSCCM__<SCOPE>__<SPECIFIC_CONTENT>__<ARTIFACT_KIND>.<ext>`

No legacy file is deleted, moved or renamed solely from filename identity.
