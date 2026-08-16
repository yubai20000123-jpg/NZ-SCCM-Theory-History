# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-16 10:43 +08:00  
**Status:** LEGACY MUTABLE POINTER ONLY

## Current operational entry

`semantic_v2/00_index/20260816_1043__NZSCCM__PROJECT__CURRENT_STATE_Z0_Z6_AR2_SSSS_CAPACITY_MATRIX__SEMANTIC_INDEX.md`

## Current production scope

The analytical production boundary is the theoretical **four-edge simply-supported plate**. Zhou FE-specific translational `ux/uy` reverse-engineering is out of scope.

```text
PRODUCTION_BOUNDARY = THEORETICAL_FOUR_EDGE_SIMPLY_SUPPORTED
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
Nguyen second-order kinematics = ACTIVE
R10/N48-C1-MM/Cayley-Hamilton = ACTIVE
General D15 exact moments = ACTIVE
A0=a/500
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
Gauss/Simpson/adaptive/collocation/cells/material-point-grid=PROHIBITED
Zhou/Winter calibration=PROHIBITED
```

No PF/end-warp/axial-trace FE correction and no free `p20,p02` membrane coordinate enters current SSSS production.

## Accepted Z6 base

User accepted:

```text
Z6 a/b=2
m*=2
ell=b=12000 mm
q0=.004
Pu=51.30 MN
Pcr=39.2880147150 MN
Pyth=88.089888 MN
Zhou=49.4867667519 MN
Winter=50.1858541295 MN
```

## New controlled Z0–Z5 AR2 calculation

For Z0–Z5 only the physical panel length `a` was changed so that `a/b=2`; source section/material parameters were retained.

All six modified cases have:

```text
m*=2
ell=a/m*=b
q0=A0/b=.004
```

Current final degree-48 full-section capacities:

|Case|NZ-SCCM Pu (MN)|Zhou (MN)|Winter (MN)|NZ−Zhou|NZ−Winter|
|---|---:|---:|---:|---:|---:|
|Z0|33.4910|36.9455|41.5008|-9.35%|-19.30%|
|Z1|19.7360|23.7214|26.1001|-16.80%|-24.38%|
|Z2|35.9781|41.2134|45.7333|-12.70%|-21.33%|
|Z3|39.6889|44.3203|49.0469|-10.45%|-19.08%|
|Z4|63.7385|69.3399|79.3861|-8.08%|-19.71%|
|Z5|14.7824|14.6816|14.6816|+0.69%|+0.69%|
|Z6|51.30|49.4868|50.1859|+3.65%|+2.21%|

All Z0–Z5 final `Rq` component-scale residuals satisfy `Rnorm<=1e-5`, and all final principal-value envelopes lie inside the predeclared `[-2.35,+1.90]` compiler interval.

## Regime distinction

For modified Z0–Z5:

```text
Pcr > Pyth
```

whereas accepted Z6 AR2 has:

```text
Pcr < Pyth
```

Thus Z0–Z5 are primarily material-strength-scale controlled before classical elastic plate buckling, while Z6 remains a buckling/postbuckling-controlled object. This distinction must be retained in later interpretation.

## Current artifacts

- `semantic_v2/10_governance/20260816_1043__NZSCCM__Z0_Z6_AR2_FOUR_EDGE_SSSS_COMPARISON_SCOPE__LOCK.md`
- `semantic_v2/40_execution/steel_shell/20260816_1043__NZSCCM__Z0_Z5_AR2_SSSS_FULLSECTION_CAPACITY__EXECUTION_REPORT.md`
- `semantic_v2/40_execution/steel_shell/20260816_1043__NZSCCM__Z0_Z5_AR2_SSSS_FULLSECTION__PARAMS_BRANCH_AND_INTERMEDIATES.json`
- `semantic_v2/40_execution/steel_shell/20260816_1043__NZSCCM__Z0_Z5_AR2_SSSS_ZHOU_WINTER__COMPARISON.csv`
- `semantic_v2/40_execution/steel_shell/20260816_1043__NZSCCM__Z0_Z5_AR2_SSSS_FULLSECTION__REPRO.py`
- `semantic_v2/60_validation/steel_shell/20260816_1043__NZSCCM__Z0_Z5_AR2_SSSS_ZHOU_WINTER_COMPARISON__AUDIT.md`
- `semantic_v2/00_index/20260816_1043__NZSCCM__PROJECT__CURRENT_STATE_Z0_Z6_AR2_SSSS_CAPACITY_MATRIX__SEMANTIC_INDEX.md`

## Historical values retained

```text
Pu=40.97334 MN = RETRACTED / INVALID
44.552919 MN    = historical reduced q-only audit only
Z6=51.30 MN     = user-accepted current SSSS full-section result
```

The modified Z0–Z5 AR2 objects are controlled theory-comparison geometries, not direct reproductions of the original physical tests at their historical aspect ratios.
