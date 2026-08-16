# NZ-SCCM semantic tree v2

This namespace is the **content-first, non-destructive semantic reconstruction** of the repository.

## Current operational entry

Use first:

`20260816_2118__NZSCCM__PROJECT__CURRENT_STATE_ADJOINT_CH_TARGET_PASS_DUAL_HOLONOMIC_THICKNESS_OPEN__SEMANTIC_INDEX.md`

## Frozen production backbone

```text
UNIFIED_PRODUCTION_WORKFLOW_V1
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order continuous kinematics
MEMBRANE_STRESS_REDISTRIBUTION = REQUIRED
R10 source current material operator = FROZEN
reinforcement/steel phase before root solve
same-state current stress + consistent tangent
General-D15 exact/controlled target framework
P,Rq,L connected-branch topology
same-state material + geometric KZ
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
N_formal_thickness_quadrature=0
```

## Structural coordinates

Global production remains `(D,q)`. Compatible membrane redistribution uses internal coordinates

```text
r=[r0,r20,r22,s02,s22]
```

with `Rm=0` and consistent Schur condensation.

## Exact 64-state R10 field

The frozen R10 physical law is carried by the exact three-generator quadratic tower

```text
s_eta,s_1,s_10
4 x 4 x 4 = 64 field states
A64 nonzeros = 159 / 4096
```

Historical N48/RC1 remain reconstruction/audit references, not the preferred structural material representation.

## 21:18 exact target reduction

2x2 Cayley-Hamilton removes the matrix `T^7` production node. With

```text
t=tr(T), d=det(T)
b0=0, b1=1
bn=t*b(n-1)-d*b(n-2)
```

we have

```text
T^n=bn*T-d*b(n-1)*I
adj(T^7)=b8*I-b7*T
```

and the exact stress target becomes

```text
S=U-ACC*det(C)*C+C*adj(T)-rho*AT*det(T)*(b8*I-b7*T).
```

For field multiplication `e_i e_j=sum_k m_ij^k e_k`, structural targets are pulled backward by the transpose multiplication action

```text
lambda(a*b)=<M_a^T lambda,b>.
```

The final 64 product coefficients therefore do not need coefficient-by-coefficient canonicalization.

Executed full-R10 `Syy` target audits at exact rational fibers `x=0` and `x=1/2` give exact zero residual against the directly materialized stress. `b7` and `b8` occupy all 64 states in both audits.

```text
T7_MATRIX_POWER_PRODUCTION_NODE = ELIMINATED_EXACT_BY_2X2_CH
FIELD_PRODUCT_ADJOINT_PULLBACK = PASS_EXACT
FULL_R10_COMPACT_STRESS_TARGET = PASS_EXACT
FULL_R10_SYY_ADJOINT_FIBER_AUDIT = PASS_EXACT_2_FIBERS
FINAL_64_COEFFICIENT_CANONICALIZATION = NOT_REQUIRED
```

## Current implementation boundary

The remaining thickness problem is the x-dependent rational dual functional. It must be contracted through the accepted 64-state holonomic thickness system without flattening the rational coefficient vector.

```text
FULL_R10_DUAL_HOLONOMIC_THICKNESS_MOMENT_RUNTIME = OPEN
BETA_WEIGHTED_XY_CREATIVE_TELESCOPING_RUNTIME = OPEN
NEW_Pu = NOT_RUN
```

## Capacity boundary

```text
Case21 368.189 kN = historical/current-support closure only
Z6 51.30 MN = retained engineering baseline only
Z0-Z5 old values = retracted/diagnostic under current governance
NEW membrane-redistributed Pu = not released
```

## Current next gate

```text
UNIFIED_V1_FULL_R10_DUAL_HOLONOMIC_THICKNESS_MOMENT_RUNTIME_GATE
```

## Repository semantic read order

1. `20260816_2118__NZSCCM__PROJECT__CURRENT_STATE_ADJOINT_CH_TARGET_PASS_DUAL_HOLONOMIC_THICKNESS_OPEN__SEMANTIC_INDEX.md`
2. `../10_governance/20260816_2118__NZSCCM__FULL_R10_ADJOINT_CH_TARGET_AND_DUAL_HOLONOMIC_NEXT__GATE_LOCK.md`
3. `../20_theory/nc_rebar_panel/20260816_2118__NZSCCM__FULL_R10_64_STATE_ADJOINT_CH_TARGET_REDUCTION__THEORY.md`
4. `../40_execution/common/20260816_2118__NZSCCM__FULL_R10_64_STATE_ADJOINT_CH_TARGET__EXECUTION_REPORT.md`
5. `../40_execution/common/20260816_2118__NZSCCM__FULL_R10_64_STATE_ADJOINT_CH_TARGET__PARAMS_AND_INTERMEDIATES.json`
6. `../40_execution/common/20260816_2118__NZSCCM__FULL_R10_64_STATE_ADJOINT_CH_TARGET__REPRO.py`
7. `../60_validation/common/20260816_2118__NZSCCM__FULL_R10_64_STATE_ADJOINT_CH_TARGET__AUDIT.md`
8. `20260816_2059__NZSCCM__PROJECT__CURRENT_STATE_FULL_R10_64_STATE_ADJOINT_TARGET_OPEN__SEMANTIC_INDEX.md` — predecessor
9. `20260816_2034__NZSCCM__PROJECT__CURRENT_STATE_NONCOMMUTING_QUARTIC_HOLONOMIC_PASS_FULL_R10_COMPOSITUM_OPEN__SEMANTIC_INDEX.md` — predecessor

No legacy file is deleted, moved or renamed solely from filename identity.
