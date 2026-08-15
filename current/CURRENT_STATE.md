# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-16 01:02 +08:00  
**Status:** LEGACY MUTABLE POINTER ONLY

## Current operational entry

`semantic_v2/00_index/20260816_0102__NZSCCM__PROJECT__CURRENT_STATE_AR2_PF_TO_D15_CURRENT_MATERIAL_MAPPING_GATE__SEMANTIC_INDEX.md`

## Hard computational boundary

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order kinematics
R10/N48-C1-MM/Cayley-Hamilton unchanged
General D15 unchanged
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
Gauss/Simpson/adaptive/collocation/cells/material-point-grid=PROHIBITED
```

Historical Gauss-based AR2 `Pu=40.97334 MN` remains retracted and invalid.

## 01:02 PF -> nonlinear current-material mapping result

The exact 00:47 PF/Airy end-restraint field is an elastic solution and is **not** transplanted as nonlinear stress.

Direct finite PF functions contain complex non-integer eigenvalues and hyperbolic factors and therefore are not finite members of the current integer-trigonometric D15 coefficient algebra:

```text
DIRECT_PF_HYPERBOLIC_TO_FINITE_D15 = FAIL_FUNCTION_SPACE
```

A conforming integer-trigonometric displacement/strain lift has instead been constructed on the AR2 one-halfwave domain `ell=b`:

```text
u_rs=(b/pi) U_rs cos(rX)[1-cos(sY)], r odd
v_rs=(b/pi) V_rs cos(rX)sin(sY),      r even
```

with membrane strains

```text
u-mode: ex=-rU sin(rX)[1-cos(sY)], ey=0, gxy=sU cos(rX)sin(sY)
v-mode: ex=0, ey=sV cos(rX)cos(sY), gxy=-rV sin(rX)sin(sY)
```

Every finite truncation is exactly a finite integer trig polynomial and therefore remains inside unchanged General D15.

## Nonlinear mapping rule

The current strain chain becomes

`epsilon=epsilon_D(D)+epsilon_g(q,q0)+sum_j r_j B_j+existing Nguyen curvature`.

For each material phase:

`sigma_p=M_p(epsilon_p)`.

The membrane coordinates satisfy

`R_j=sum_p int sigma_p:B_j dV=0`.

Thus the elastic PF stress field is never reused as nonlinear stress.

In the homogeneous elastic limit:

`r=c_D D+c_G Gamma/eps0=c_D D+2 c_G M`,

where `Gamma=pi^2(A^2+2A0A)/b^2` and `M=pi^2/eps0*(q0q+q^2/2)`.

The complete conforming Ritz space and PF/Airy solve the same strictly convex elastic membrane minimization problem, so their complete-basis elastic limits coincide by uniqueness.

## Exact coefficient-space validation

All finite-Ritz matrices were assembled from finite Fourier coefficients and exact antiderivatives only; no spatial points were used.

For `nu=.18`:

```text
R=S  nmem   Q_GG             Q_DD             Q_DG
1      2    .710327899673    9.716401029828   -1.359305267256
2      8    .380985323731    9.661181203174   -1.280790283542
3     18    .338757150201    9.639425364487   -1.257398206363
4     32    .318834041670    9.628042047630   -1.246067137428
6     72    .299568422262    9.616453853076   -1.235062292357
8    128    .290150329916    9.610639322927   -1.229696366445
10   200    .284558250341    9.607163461818   -1.226522139050
12   288    .280851744614    9.604857758524   -1.224424967309
```

All `Q_GG>0`, preserving the classical positive membrane effect.

The pre-buckling D-driven end-restraint field is also part of the same coordinates. At R=S=12:

```text
free-Poisson Q_DD=9.549829218494
mixed-end Ritz Q_DD=9.604857758524
fully-restrained Q_DD=9.869604401089
```

so the mixed boundary lies physically between free and fully restrained transverse response.

## Current verdict

```text
AR2_PF_TO_NONLINEAR_KINEMATIC_MAPPING = PASS_ARCHITECTURE
BOUNDARY_ADMISSIBLE_INTEGER_TRIG_D15_LIFT = PASS
GENERAL_D15_THEORY_CHANGE = NO
ELASTIC_PF_LIMIT = PASS_FORMAL_COMPLETE_BASIS
PREBUCKLING_D_END_RESTRAINT = INCLUDED
POSTBUCKLING_FVK_MEMBRANE_DRIVER = INCLUDED
ZERO_SPATIAL_NUMERICAL_INTEGRATION = PASS
MULTICOORDINATE_R10_N48_IMPLEMENTATION = OPEN
PRODUCTION_MEMBRANE_RANK = NOT_FROZEN
FULL_ZHOU_ALL_INPLANE_END_DOF_EQUIVALENCE = OPEN
NEW_AR2_Z6_Pu = NOT_CALCULATED
```

## Why Pu remains blocked

1. the existing reduced R10/N48 code is specialized to historical low-rank D-q(/c) fields and does not yet accept a generic membrane-coordinate vector;
2. a production membrane rank has not been selected by coefficient-space convergence;
3. Zhou's actual `bottom uy=0` versus `top uy=unset` axial end asymmetry has not yet been proven compatible with the one-halfwave condensation.

Because item 3 can alter the admissible membrane basis, it precedes nonlinear compiler implementation.

## Current next execution

`ZHOU_BOTTOM_UY0_TOP_UYFREE_ONE_HALFWAVE_COMPATIBILITY_ZERO_QUADRATURE_GATE`

## 01:02 artifacts

- `semantic_v2/10_governance/20260816_0102__NZSCCM__AR2_PF_TO_R10_N48_D15_ZERO_QUADRATURE_MAPPING__LOCK.md`
- `semantic_v2/20_theory/nc_steel_shell_panel/20260816_0102__NZSCCM__AR2_BOUNDARY_ADMISSIBLE_D15_RITZ_LIFT_TO_CURRENT_MATERIAL__THEORY.md`
- `semantic_v2/40_execution/steel_shell/20260816_0102__NZSCCM__AR2_PF_TO_R10_N48_D15_MAPPING__EXECUTION_REPORT.md`
- `semantic_v2/40_execution/steel_shell/20260816_0102__NZSCCM__AR2_D15_RITZ_LIFT__PARAMS_AND_INTERMEDIATES.json`
- `semantic_v2/40_execution/steel_shell/20260816_0102__NZSCCM__AR2_D15_RITZ_LIFT__REPRO.py`
- `semantic_v2/60_validation/steel_shell/20260816_0102__NZSCCM__AR2_PF_TO_D15_CURRENT_MATERIAL_MAPPING__AUDIT.md`
- `semantic_v2/00_index/20260816_0102__NZSCCM__PROJECT__CURRENT_STATE_AR2_PF_TO_D15_CURRENT_MATERIAL_MAPPING_GATE__SEMANTIC_INDEX.md`
