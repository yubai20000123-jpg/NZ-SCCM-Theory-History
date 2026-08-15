# NZ-SCCM current semantic state — Z6 AR2 theoretical four-edge SSSS capacity

**Timestamp:** 2026-08-16 02:49 +08:00

## User-controlled production boundary

Z6 is now calculated under the theoretical four-edge simply-supported/Navier boundary stated by Zhou. Detailed FE `ux/uy` restraint implementation is outside this analytical production task.

```text
Z6_PRODUCTION_BOUNDARY = THEORETICAL_FOUR_EDGE_SIMPLY_SUPPORTED
ZHOU_FE_TRANSLATIONAL_BC_REVERSE_ENGINEERING = OUT_OF_SCOPE
20260816_0016_TO_0121_FE_BOUNDARY_DETOUR = SUPERSEDED_FOR_Z6_PRODUCTION
```

Historical files remain preserved; they are not used in this capacity result.

## Frozen theory identity

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order kinematics
R10 -> N48-C1/MM -> Cayley-Hamilton
General D15 exact moments
A0=a/500
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
free p20,p02 = RETIRED
FE end warp c = NOT USED
PF end layer = NOT USED
```

## Z6 AR2 object

```text
a=24000 mm
b=12000 mm
a/b=2
m*=2
ell=12000 mm=b
A0=48 mm
q0=.004
fc=30.4 MPa
tc=122 mm
ts=4 mm
rho_w=.02
Es=206000 MPa
fy=355 MPa
```

## Current capacity

Degree-48 local peak state:

```text
D  = 1.5853259043
q  = 0.02166488056895
A  = 259.9785668 mm

Pc_eff = 20.72760903 MN
Ps     = 21.59547236 MN
Pw     =  8.97221193 MN
P      = 51.29529333 MN
Rq     = -311.161 N mm
Rnorm  ~= 1.36e-8
```

Engineering-frozen Z6 capacity:

\[
\boxed{P_u\approx51.30\ \mathrm{MN}}
\]

with

\[
D_u\approx1.585,\qquad q_u\approx0.021665,\qquad A_u\approx260\ \mathrm{mm}.
\]

## Branch identity

Near the first local load maximum, the connected positive-q branch locator gives

```text
D=1.56 -> 51.23273135 MN
D=1.58 -> 51.31276663 MN
D=1.60 -> 51.28835746 MN
```

so the local branch changes from increasing to decreasing around `D~1.585`. Degree-48 steel/web refinement lowers the local peak by about `0.0202 MN` and leaves the rounded `51.30 MN` capacity unchanged.

## Compiler identity

Declared interval:

`lambda in [-2.35,+1.90]`.

Final envelope:

```text
lambda_min=-2.2936943231
lambda_max=+1.8232424497
```

Coverage passes. The wide-hull N48-C1/MM fidelity errors are recorded in the execution JSON; the principal remaining representation uncertainty is compiler fidelity on this broad strain interval, not boundary condition or spatial integration.

## Comparisons after theory solve

```text
Pcr_AR2               = 39.2880147150 MN
Pyth_full              = 88.089888 MN
Zhou Eq.(5-87)/(5-88) = 49.4867667519 MN
Winter                 = 50.1858541295 MN

Pu/Pcr  = 1.30562
Pu/Pyth = 0.58231
vs Zhou = +3.65%
vs Winter = +2.21%
```

No comparator was used in solving or calibration.

## Current verdict

```text
Z6_CAPACITY_CALCULATED = YES
CURRENT_Z6_Pu = 51.30 MN
ZERO_SPATIAL_INTEGRATION = PASS
FOUR_EDGE_SSSS_SCOPE = LOCKED
FULL_SECTION_WEB_PHASE = INCLUDED
40.97334_MN = RETRACTED_INVALID
44.552919_MN = HISTORICAL_REDUCED_AUDIT_ONLY
FE_BOUNDARY_REVERSE_ENGINEERING = STOPPED_FOR_Z6_PRODUCTION
```

## Current artifact read order

1. `../10_governance/20260816_0249__NZSCCM__ZHOU_Z6_FOUR_EDGE_SIMPLY_SUPPORTED_PRODUCTION_SCOPE__LOCK.md`
2. `../40_execution/steel_shell/20260816_0249__NZSCCM__Z6_AR2_SSSS_FULLSECTION_CAPACITY__EXECUTION_REPORT.md`
3. `../40_execution/steel_shell/20260816_0249__NZSCCM__Z6_AR2_SSSS_FULLSECTION__PARAMS_BRANCH_AND_INTERMEDIATES.json`
4. `../60_validation/steel_shell/20260816_0249__NZSCCM__Z6_AR2_SSSS_FULLSECTION_CAPACITY__AUDIT.md`
5. `20260816_0121__NZSCCM__PROJECT__CURRENT_STATE_ZHOU_AXIAL_END_ASYMMETRY_GATE__SEMANTIC_INDEX.md` — historical FE-boundary detour, superseded for Z6 production
6. `20260816_0102__NZSCCM__PROJECT__CURRENT_STATE_AR2_PF_TO_D15_CURRENT_MATERIAL_MAPPING_GATE__SEMANTIC_INDEX.md` — historical FE-boundary detour, superseded for Z6 production

## Next technical priority

The requested Z6 capacity has now been produced. Any next calculation should use this SSSS production scope unless the user explicitly changes the analytical boundary model.