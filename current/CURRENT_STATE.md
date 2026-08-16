# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-16 21:18 +08:00  
**Status:** LEGACY MUTABLE POINTER ONLY

## Current operational entry

`semantic_v2/00_index/20260816_2118__NZSCCM__PROJECT__CURRENT_STATE_ADJOINT_CH_TARGET_PASS_DUAL_HOLONOMIC_THICKNESS_OPEN__SEMANTIC_INDEX.md`

## Frozen project-wide backbone

```text
UNIFIED_PRODUCTION_WORKFLOW_V1 = ACTIVE
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
Nguyen second-order continuous kinematics = ACTIVE
MEMBRANE_STRESS_REDISTRIBUTION = REQUIRED
R10 source current material operator = FROZEN
reinforcement/steel phase before root solve = REQUIRED
same-state current stress + consistent tangent = REQUIRED
General-D15 moment-first target framework = ACTIVE
P,Rq,L connected-branch topology = ACTIVE
same-state material + geometric KZ audit = ACTIVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
Gauss/Simpson/adaptive/collocation/material-point-grid = PROHIBITED
experiment/Zhou/Winter response calibration = PROHIBITED
```

## Structural coordinates retained

```text
global coordinates = (D,q), A=bq
internal membrane coordinates = [r0,r20,r22,s02,s22]
```

with `Rm=0` and consistent Schur condensation retained.

## Exact 64-state field retained

The exact R10 source graph remains represented by the fixed three-generator quadratic tower

```text
s_eta,s_1,s_10
4 x 4 x 4 = 64 field states
A64 nonzeros = 159 / 4096
```

Historical N48/RC1 remain reconstruction/audit references only.

## 21:18 exact CH elimination of matrix T^7

For

```text
t=tr(T), d=det(T)
b0=0, b1=1
bn=t*b(n-1)-d*b(n-2)
```

2x2 Cayley-Hamilton gives

```text
T^n=bn*T-d*b(n-1)*I
adj(T^7)=b8*I-b7*T
```

where

```text
b7=t^6-5*t^4*d+6*t^2*d^2-d^3
b8=t^7-6*t^5*d+10*t^3*d^2-4*t*d^3.
```

Therefore the full frozen R10 stress is carried as

```text
S=U-ACC*det(C)*C+C*adj(T)-rho*AT*det(T)*(b8*I-b7*T).
```

The previously materialized matrix `T7` remains diagnostic evidence only. It is no longer a production target node.

```text
T7_MATRIX_POWER_PRODUCTION_NODE = ELIMINATED_EXACT_BY_2X2_CH
T7_MATRIX_DERIVATIVE_PRODUCTION_NODE = ELIMINATED_TO_SCALAR_RECURRENCE
```

## 21:18 target-side field adjoint

For field multiplication

```text
e_i*e_j=sum_k m_ij^k e_k
```

and a linear target `lambda`,

```text
lambda(a*b)=<M_a^T lambda,b>=<M_b^T lambda,a>.
```

Thus structural stress targets are pulled backward through the fixed 64-state field DAG. A final coefficient-by-coefficient `SymPy.cancel` on the full target vector is not required.

Executed full-R10 `Syy` audit on the retained noncommuting prototype at exact rational fibers

```text
x=0
x=1/2
```

gives

```text
Syy support = 60/64
b7 support  = 64/64
b8 support  = 64/64
adjoint Syy - direct materialized Syy = 0 exactly at both fibers
```

At `x=0`, the complete CH stress and the predecessor matrix-`T7` stress agree entry-by-entry with exact zero field residual.

Diagnostic timing:

```text
x=0   : 14.897 s -> 5.103 s
x=1/2 : 17.459 s -> 5.681 s
```

for the old binary-`T7` target path versus the CH compact target path. These times are implementation diagnostics, not theory constants.

```text
FIELD_PRODUCT_ADJOINT_PULLBACK = PASS_EXACT
FULL_R10_COMPACT_STRESS_TARGET = PASS_EXACT
FULL_R10_SYY_ADJOINT_FIBER_AUDIT = PASS_EXACT_2_FIBERS
FINAL_64_COEFFICIENT_CANONICALIZATION = NOT_REQUIRED
```

## Current implementation boundary

The remaining thickness problem is now narrower: the x-dependent rational dual target must be contracted through the already accepted 64-state holonomic thickness system without flattening rational coefficient functions.

```text
FULL_R10_DUAL_HOLONOMIC_THICKNESS_MOMENT_RUNTIME = OPEN
BETA_WEIGHTED_XY_CREATIVE_TELESCOPING_RUNTIME = OPEN
NEW_CURRENT_MEMBRANE_r_SOLVE = NOT_RUN
NEW_Pu = NOT_RUN
```

The algebraic audit fibers are not structural quadrature points.

## Capacity status

```text
Case21 368.189 kN = historical/current-support closure only
Z6 51.30 MN = retained engineering baseline only
Z0-Z5 old values = retracted/diagnostic under current governance
NEW membrane-redistributed Pu = NOT_RELEASED
```

## Current unique next gate

```text
UNIFIED_V1_FULL_R10_DUAL_HOLONOMIC_THICKNESS_MOMENT_RUNTIME_GATE
```

## Current key artifacts

- `semantic_v2/00_index/20260816_2118__NZSCCM__PROJECT__CURRENT_STATE_ADJOINT_CH_TARGET_PASS_DUAL_HOLONOMIC_THICKNESS_OPEN__SEMANTIC_INDEX.md`
- `semantic_v2/20_theory/nc_rebar_panel/20260816_2118__NZSCCM__FULL_R10_64_STATE_ADJOINT_CH_TARGET_REDUCTION__THEORY.md`
- `semantic_v2/40_execution/common/20260816_2118__NZSCCM__FULL_R10_64_STATE_ADJOINT_CH_TARGET__EXECUTION_REPORT.md`
- `semantic_v2/40_execution/common/20260816_2118__NZSCCM__FULL_R10_64_STATE_ADJOINT_CH_TARGET__PARAMS_AND_INTERMEDIATES.json`
- `semantic_v2/40_execution/common/20260816_2118__NZSCCM__FULL_R10_64_STATE_ADJOINT_CH_TARGET__REPRO.py`
- `semantic_v2/60_validation/common/20260816_2118__NZSCCM__FULL_R10_64_STATE_ADJOINT_CH_TARGET__AUDIT.md`
- `semantic_v2/10_governance/20260816_2118__NZSCCM__FULL_R10_ADJOINT_CH_TARGET_AND_DUAL_HOLONOMIC_NEXT__GATE_LOCK.md`
