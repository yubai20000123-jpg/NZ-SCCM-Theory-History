# NZ-SCCM semantic tree v2

This namespace is the **content-first, non-destructive semantic reconstruction** of the repository.

A legacy path or filename is a locator only. It does not confer current/superseded/rejected identity.

## Current operational entry

Use first:

`20260816_0249__NZSCCM__PROJECT__CURRENT_STATE_Z6_AR2_SSSS_CAPACITY__SEMANTIC_INDEX.md`

## Current locked status

```text
Z6_PRODUCTION_BOUNDARY = THEORETICAL_FOUR_EDGE_SIMPLY_SUPPORTED
ZHOU_FE_UX_UY_IMPLEMENTATION = OUT_OF_SCOPE_FOR_Z6_PRODUCTION
20260816_0016_TO_0121_FE_BOUNDARY_DETOUR = SUPERSEDED_FOR_Z6_PRODUCTION

ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
Nguyen second-order kinematics = ACTIVE
R10/N48-C1-MM/Cayley-Hamilton = ACTIVE
General D15 exact moments = ACTIVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1

free p20,p02 membrane DOFs = RETIRED
PF/end-warp/axial-trace FE corrections = NOT USED IN Z6 SSSS PRODUCTION

Z6_AR2_CURRENT_Pu = 51.30 MN
Du ~= 1.585
qu ~= .021665
Au ~= 260 mm

Pu_40.97334_MN = RETRACTED / INVALID
Pu_44.552919_MN = HISTORICAL REDUCED Q-ONLY AUDIT ONLY
```

## Current Z6 result

AR2 object:

```text
a=24000 mm
b=12000 mm
a/b=2
m*=2
ell=12000 mm=b
A0=48 mm
q0=.004
```

Degree-48 local peak state:

```text
Pc_eff = 20.72760903 MN
Ps     = 21.59547236 MN
Pw     =  8.97221193 MN
Pu     = 51.29529333 MN
Rq     = -311.161 N mm
Rnorm  ~= 1.36e-8
```

Engineering-frozen capacity:

`Pu = 51.30 MN`.

Post-solve comparisons only:

```text
Pu/Pcr    = 1.30562
Pu/Pyth   = 0.58231
vs Zhou   = +3.65%
vs Winter = +2.21%
```

The declared compiler interval `[-2.35,+1.90]` contains the final reachable principal-value envelope `[-2.293694,+1.823242]`. Wide-hull N48-C1/MM fidelity is recorded as the main representation uncertainty; it does not reopen FE boundary reverse engineering or spatial numerical integration.

## Repository semantic read order

1. `20260816_0249__NZSCCM__PROJECT__CURRENT_STATE_Z6_AR2_SSSS_CAPACITY__SEMANTIC_INDEX.md`
2. `../10_governance/20260816_0249__NZSCCM__ZHOU_Z6_FOUR_EDGE_SIMPLY_SUPPORTED_PRODUCTION_SCOPE__LOCK.md`
3. `../40_execution/steel_shell/20260816_0249__NZSCCM__Z6_AR2_SSSS_FULLSECTION_CAPACITY__EXECUTION_REPORT.md`
4. `../40_execution/steel_shell/20260816_0249__NZSCCM__Z6_AR2_SSSS_FULLSECTION__PARAMS_BRANCH_AND_INTERMEDIATES.json`
5. `../60_validation/steel_shell/20260816_0249__NZSCCM__Z6_AR2_SSSS_FULLSECTION_CAPACITY__AUDIT.md`
6. `20260816_0121__NZSCCM__PROJECT__CURRENT_STATE_ZHOU_AXIAL_END_ASYMMETRY_GATE__SEMANTIC_INDEX.md` — preserved historical FE-boundary detour; superseded for Z6 production
7. `20260816_0102__NZSCCM__PROJECT__CURRENT_STATE_AR2_PF_TO_D15_CURRENT_MATERIAL_MAPPING_GATE__SEMANTIC_INDEX.md` — preserved historical FE-boundary detour; superseded for Z6 production
8. `20260816_0047__NZSCCM__PROJECT__CURRENT_STATE_ZHOU_END_RESTRAINT_PF_SERIES_AND_AR2_MAPPING__SEMANTIC_INDEX.md` — preserved historical FE-boundary detour; superseded for Z6 production
9. `20260816_0007__NZSCCM__PROJECT__CURRENT_STATE_CLASSICAL_ELASTIC_POSTBUCKLING_LIMIT_GATE_PASS__SEMANTIC_INDEX.md`
10. `20260815_2358__NZSCCM__PROJECT__CURRENT_STATE_CLASSICAL_POSTBUCKLING_REDERIVATION_GATE__SEMANTIC_INDEX.md`
11. `20260815_2343__NZSCCM__PROJECT__CURRENT_STATE_Z6_AR2_UPDATED_FVK_DIRECT_R10_RECALC__SEMANTIC_INDEX.md` — historical invalid under current zero-spatial-integration governance
12. `20260813_1328__NZSCCM__REPOSITORY__CONTENT_FIRST_NAMING_AND_TREE_POLICY__GOVERNANCE.md`
13. `20260813_1328__NZSCCM__REPOSITORY__CONTENT_SEMANTIC_TREE__SEMANTIC_MANIFEST.md`

## Audit levels

- `A_DIRECT_CONTENT_AUDIT`: file body opened/read; identity derived from content + chronology.
- `B_CONTENT_DERIVED_REGISTRY_OR_LEDGER`: stable source/history role derived from a content-read registry/ledger; open the leaf before using it for a technical claim.
- `C_NOT_YET_DIRECT_CONTENT_AUDITED`: locator known, semantic identity not yet asserted beyond family/locator role.

## Canonical naming

`YYYYMMDD_HHMM__NZSCCM__<SCOPE>__<SPECIFIC_CONTENT>__<ARTIFACT_KIND>.<ext>`

No legacy file is deleted, moved or renamed solely from filename identity.