# NZ-SCCM current state — AR2 PF -> D15 current-material mapping gate

**Timestamp:** 2026-08-16 01:02 +08:00

## Current identity

The elastic PF/Airy boundary field is **not** used as nonlinear stress. A conforming integer-trigonometric displacement/strain lift has been constructed on the AR2 one-complete-halfwave domain.

```text
AR2_PF_TO_NONLINEAR_KINEMATIC_MAPPING = PASS_ARCHITECTURE
DIRECT_PF_HYPERBOLIC_TO_FINITE_D15 = FAIL_FUNCTION_SPACE
BOUNDARY_ADMISSIBLE_INTEGER_TRIG_D15_LIFT = PASS
GENERAL_D15_THEORY = UNCHANGED
ELASTIC_PF_LIMIT = PASS_FORMAL_COMPLETE_BASIS
PREBUCKLING_D_DRIVEN_END_RESTRAINT = INCLUDED
POSTBUCKLING_FVK_DRIVER = INCLUDED
ZERO_SPATIAL_INTEGRATION = PASS
MULTICOORDINATE_R10_N48_IMPLEMENTATION = OPEN
PRODUCTION_MEMBRANE_RANK = OPEN
FULL_ZHOU_ALL_INPLANE_END_DOF_EQUIVALENCE = OPEN
NEW_AR2_Pu = NOT_CALCULATED
```

## Core finite-D15 lift

On AR2 `ell=b`:

```text
u_rs=(b/pi) U_rs cos(rX)[1-cos(sY)], r odd
v_rs=(b/pi) V_rs cos(rX)sin(sY),      r even
```

Every finite level is an integer trig polynomial and remains inside General D15. In the elastic reference

`r=c_D D+2 c_G M`,

where `M=pi^2/eps0*(q0 q+q^2/2)`. This relation is a validation identity only; nonlinear membrane coordinates are independent generalized coordinates solved from `R_j=0`.

Exact coefficient-space energy convergence for `nu=.18` reaches at R=S=12:

```text
nmem=288
Q_GG=.280851744614 > 0
Q_DD=9.604857758524
Q_DG=-1.224424967309
```

with reference bounds

```text
free Poisson Q_DD=9.549829218494
fully transverse restrained Q_DD=9.869604401089
```

No spatial points or quadrature were used.

## Current blocker and next gate

Before implementing a many-coordinate nonlinear compiler, the project must resolve whether Zhou's asymmetric axial boundary

```text
bottom uy=0
top uy=unset
```

is compatible with the current one-halfwave condensation or requires an additional asymmetric in-plane end family.

Current next execution:

`ZHOU_BOTTOM_UY0_TOP_UYFREE_ONE_HALFWAVE_COMPATIBILITY_ZERO_QUADRATURE_GATE`

## Read order

1. `../10_governance/20260816_0102__NZSCCM__AR2_PF_TO_R10_N48_D15_ZERO_QUADRATURE_MAPPING__LOCK.md`
2. `../20_theory/nc_steel_shell_panel/20260816_0102__NZSCCM__AR2_BOUNDARY_ADMISSIBLE_D15_RITZ_LIFT_TO_CURRENT_MATERIAL__THEORY.md`
3. `../40_execution/steel_shell/20260816_0102__NZSCCM__AR2_PF_TO_R10_N48_D15_MAPPING__EXECUTION_REPORT.md`
4. `../40_execution/steel_shell/20260816_0102__NZSCCM__AR2_D15_RITZ_LIFT__PARAMS_AND_INTERMEDIATES.json`
5. `../40_execution/steel_shell/20260816_0102__NZSCCM__AR2_D15_RITZ_LIFT__REPRO.py`
6. `../60_validation/steel_shell/20260816_0102__NZSCCM__AR2_PF_TO_D15_CURRENT_MATERIAL_MAPPING__AUDIT.md`
7. `20260816_0047__NZSCCM__PROJECT__CURRENT_STATE_ZHOU_END_RESTRAINT_PF_SERIES_AND_AR2_MAPPING__SEMANTIC_INDEX.md`

The 23:43 Gauss-based `Pu=40.97334 MN` remains retracted and invalid.