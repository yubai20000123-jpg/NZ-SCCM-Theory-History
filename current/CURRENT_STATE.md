# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-16 02:49 +08:00  
**Status:** LEGACY MUTABLE POINTER ONLY

## Current operational entry

`semantic_v2/00_index/20260816_0249__NZSCCM__PROJECT__CURRENT_STATE_Z6_AR2_SSSS_CAPACITY__SEMANTIC_INDEX.md`

## Governing Z6 production scope

Per the latest user instruction, Zhou's wall is treated analytically as a **theoretical four-edge simply-supported plate**. Detailed FE translational `ux/uy` implementation is not part of the Z6 analytical capacity task.

```text
Z6_PRODUCTION_BOUNDARY = THEORETICAL_FOUR_EDGE_SIMPLY_SUPPORTED
NAVIER_COMPLETE_HALFWAVE = GOVERNING
ZHOU_FE_UX_UY_IMPLEMENTATION = OUT_OF_SCOPE_FOR_Z6_PRODUCTION
20260816_0016_TO_0121_FE_BOUNDARY_DETOUR = SUPERSEDED_FOR_Z6_PRODUCTION
```

The historical FE-boundary files remain preserved but no longer block or define Z6 production.

## Hard computational boundary

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order kinematics
R10/N48-C1-MM/Cayley-Hamilton unchanged
General D15 unchanged
A0=a/500
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
Gauss/Simpson/adaptive/collocation/cells/material-point-grid=PROHIBITED
out-of-plane multimode production expansion=PROHIBITED
Zhou/Winter calibration=PROHIBITED
```

`p20,p02` as independent free membrane DOFs remain retired. PF/end-warp/axial-trace FE-boundary corrections are not used in the current SSSS production field.

## Z6 AR2 production object

```text
a=24000 mm
b=12000 mm
a/b=2
m*=2
ell=a/m*=12000 mm=b
A0=48 mm
q0=.004

tc=122 mm
ts=4 mm
rho_w=.02
fc=30.4 MPa
eps0=.0018712490394580678
nu_c=.18
Es=206000 MPa
fy=355 MPa
nu_s=.30
```

The full section contains effective concrete core, both face steel plates, and the equivalent longitudinal web/PBL steel phase.

## Current Z6 capacity

Final degree-48 local peak state:

```text
D       = 1.5853259043
q       = 0.02166488056895
A=q*b   = 259.9785668 mm

Pc_eff  = 20.72760903 MN
Ps      = 21.59547236 MN
Pw      =  8.97221193 MN
P       = 51.29529333 MN
Rq      = -311.161 N mm
Rnorm   ~= 1.36e-8
```

Engineering-frozen result:

```text
CURRENT_Z6_Pu = 51.30 MN
Du ~= 1.585
qu ~= .021665
Au ~= 260 mm
```

Connected branch locator around the first local maximum:

```text
D=1.56  P=51.23273135 MN
D=1.58  P=51.31276663 MN
D=1.60  P=51.28835746 MN
```

so the load changes from increasing to decreasing around `D~1.585`.

## Compiler / spatial audit

Declared material interval:

`lambda in [-2.35,+1.90]`.

Final envelope:

```text
lambda_min=-2.2936943231
lambda_max=+1.8232424497
```

Coverage passes. Wide-hull N48-C1/MM fidelity error is retained as representation uncertainty; it is not a spatial-integration or boundary-condition error and the frozen production contract has no universal full-hull rejection threshold.

## Post-solve comparisons

```text
Pcr_AR2               = 39.2880147150 MN
Pyth_full              = 88.089888 MN
Zhou Eq.(5-87)/(5-88) = 49.4867667519 MN
Winter                 = 50.1858541295 MN

Pu/Pcr    = 1.30562
Pu/Pyth   = 0.58231
vs Zhou   = +3.65%
vs Winter = +2.21%
```

No comparator entered the solve.

## Historical values

```text
Pu=40.97334 MN = RETRACTED / INVALID (Gauss + free p20/p02 path)
44.552919 MN    = historical reduced q-only audit only
51.30 MN        = current theoretical-four-edge-SSSS full-section Z6 capacity
```

## Current artifacts

- `semantic_v2/10_governance/20260816_0249__NZSCCM__ZHOU_Z6_FOUR_EDGE_SIMPLY_SUPPORTED_PRODUCTION_SCOPE__LOCK.md`
- `semantic_v2/40_execution/steel_shell/20260816_0249__NZSCCM__Z6_AR2_SSSS_FULLSECTION_CAPACITY__EXECUTION_REPORT.md`
- `semantic_v2/40_execution/steel_shell/20260816_0249__NZSCCM__Z6_AR2_SSSS_FULLSECTION__PARAMS_BRANCH_AND_INTERMEDIATES.json`
- `semantic_v2/60_validation/steel_shell/20260816_0249__NZSCCM__Z6_AR2_SSSS_FULLSECTION_CAPACITY__AUDIT.md`
- `semantic_v2/00_index/20260816_0249__NZSCCM__PROJECT__CURRENT_STATE_Z6_AR2_SSSS_CAPACITY__SEMANTIC_INDEX.md`
