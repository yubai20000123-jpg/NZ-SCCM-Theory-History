# NZ-SCCM current semantic index — Z0–Z6 AR2 SSSS capacity matrix

**Timestamp:** 2026-08-16 10:43 +08:00  
**Status:** CURRENT OPERATIONAL ENTRY

## Current locked production identity

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
Zhou/Winter calibration=NO
```

Z6 `Pu=51.30 MN` is user-accepted and retained.

For the new controlled comparison, Z0–Z5 are modified only so that `a/b=2`. Their theoretical Zhou minimum is `m*=2`, hence every representative complete halfwave has `ell=b` and `q0=.004`.

## Current AR2 capacity matrix

|Case|NZ-SCCM Pu (MN)|Zhou (MN)|Winter (MN)|NZ−Zhou|NZ−Winter|Pcr (MN)|Pyth (MN)|
|---|---:|---:|---:|---:|---:|---:|---:|
|Z0|33.4910|36.9455|41.5008|-9.35%|-19.30%|78.3067|44.0449|
|Z1|19.7360|23.7214|26.1001|-16.80%|-24.38%|40.3502|30.3196|
|Z2|35.9781|41.2134|45.7333|-12.70%|-21.33%|78.3067|50.6221|
|Z3|39.6889|44.3203|49.0469|-10.45%|-19.08%|81.7974|54.9488|
|Z4|63.7385|69.3399|79.3861|-8.08%|-19.71%|179.7548|79.3861|
|Z5|14.7824|14.6816|14.6816|+0.69%|+0.69%|231.7884|14.6816|
|Z6|51.30|49.4868|50.1859|+3.65%|+2.21%|39.2880|88.0899|

## Current interpretation

- Modified Z0–Z5: `Pcr>Pyth`, predominantly material-strength-scale control before classical elastic plate buckling.
- Accepted Z6 AR2: `Pcr<Pyth`, genuine buckling/postbuckling regime.
- Therefore the Z6 anomaly cannot now be attributed simply to its old historical aspect ratio after the full AR2 normalization.
- Z0–Z4 show a systematic NZ-SCCM underprediction relative to Zhou/Winter in this hypothetical AR2 set; Z5 is essentially coincident.
- These modified cases are controlled theory-comparison objects, not direct reproductions of original test geometries.

## Read order

1. `../10_governance/20260816_1043__NZSCCM__Z0_Z6_AR2_FOUR_EDGE_SSSS_COMPARISON_SCOPE__LOCK.md`
2. `../40_execution/steel_shell/20260816_1043__NZSCCM__Z0_Z5_AR2_SSSS_FULLSECTION_CAPACITY__EXECUTION_REPORT.md`
3. `../40_execution/steel_shell/20260816_1043__NZSCCM__Z0_Z5_AR2_SSSS_FULLSECTION__PARAMS_BRANCH_AND_INTERMEDIATES.json`
4. `../40_execution/steel_shell/20260816_1043__NZSCCM__Z0_Z5_AR2_SSSS_ZHOU_WINTER__COMPARISON.csv`
5. `../40_execution/steel_shell/20260816_1043__NZSCCM__Z0_Z5_AR2_SSSS_FULLSECTION__REPRO.py`
6. `../60_validation/steel_shell/20260816_1043__NZSCCM__Z0_Z5_AR2_SSSS_ZHOU_WINTER_COMPARISON__AUDIT.md`
7. `20260816_0249__NZSCCM__PROJECT__CURRENT_STATE_Z6_AR2_SSSS_CAPACITY__SEMANTIC_INDEX.md` — accepted Z6 base

## Historical status retained

```text
Pu_40.97334_MN = RETRACTED / INVALID
Pu_44.552919_MN = HISTORICAL REDUCED Q-ONLY AUDIT ONLY
Z6_51.30_MN = USER ACCEPTED CURRENT RESULT
```
