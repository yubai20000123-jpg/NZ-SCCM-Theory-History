# NZ-SCCM current state — adjoint/CH target pass / dual-holonomic thickness runtime open

**Timestamp:** 2026-08-16 21:18 +08:00

## Current verdict

The frozen R10 source, five-term membrane redistribution, and exact 64-state quadratic-tower field remain active. The production target graph is reduced further by an exact 2x2 Cayley–Hamilton identity that removes the matrix `T^7` node.

```text
FULL_64_STATE_FIELD = RETAIN_PASS
T7_MATRIX_POWER_PRODUCTION_NODE = ELIMINATED_EXACT_BY_2X2_CH
T7_MATRIX_DERIVATIVE_PRODUCTION_NODE = ELIMINATED_TO_SCALAR_RECURRENCE
FIELD_PRODUCT_ADJOINT_PULLBACK = PASS_EXACT
FULL_R10_COMPACT_STRESS_TARGET = PASS_EXACT
FULL_R10_SYY_ADJOINT_FIBER_AUDIT = PASS_EXACT_2_FIBERS
FINAL_64_COEFFICIENT_CANONICALIZATION = NOT_REQUIRED
FULL_R10_DUAL_HOLONOMIC_THICKNESS_MOMENT_RUNTIME = OPEN
BETA_WEIGHTED_XY_CREATIVE_TELESCOPING_RUNTIME = OPEN
NEW_Pu = NOT_RUN
```

## Exact CH tension interaction

Let

```text
t=tr(T)
d=det(T)
b0=0
b1=1
bn=t*b(n-1)-d*b(n-2)
```

Then

```text
T^n=bn*T-d*b(n-1)*I
adj(T^7)=b8*I-b7*T
```

with

```text
b7=t^6-5*t^4*d+6*t^2*d^2-d^3
b8=t^7-6*t^5*d+10*t^3*d^2-4*t*d^3.
```

The full normalized stress is now carried as

```text
S=U-ACC*det(C)*C+C*adj(T)-rho*AT*det(T)*(b8*I-b7*T).
```

The earlier 20:59 materialized `T7` calculation remains diagnostic evidence only; production no longer needs a matrix seventh-power node.

## Adjoint target rule

For field products

```text
e_i*e_j=sum_k m_ij^k e_k
```

and a linear target `lambda`,

```text
lambda(a*b)=<M_a^T lambda,b>=<M_b^T lambda,a>.
```

Therefore structural targets are pulled backward through the fixed field DAG. The final product coefficient vector need not be normalized coefficient-by-coefficient.

## Executed R10 audit

Retained noncommuting prototype:

```text
E(x)=[[1/5+x/3,1/7+x/5],
      [1/7+x/5,-1/4+2*x/7]]
```

Exact rational audit fibers:

```text
x=0
x=1/2
```

At both fibers:

```text
Syy support = 60/64
b7 support = 64/64
b8 support = 64/64
adjoint Syy - direct materialized Syy = 0 exactly
```

At `x=0`, the complete CH stress and the prior matrix-`T7` stress agree entry-by-entry exactly.

Diagnostic exact-rational runtimes:

```text
x=0   : old binary-T7 target 14.897 s -> CH compact target 5.103 s
x=1/2 : old binary-T7 target 17.459 s -> CH compact target 5.681 s
```

The fibers are algebraic audit points only and are not structural quadrature.

## Structural model retained

```text
global coordinates = (D,q)
internal membrane coordinates = [r0,r20,r22,s02,s22]
Rm=0
Krr=dRm/dr
r_g=-Krr^-1 Rm_g
Pbar_g=P_g+P_r r_g
Rqbar_g=Rq_g+Rq_r r_g
Lbar=Pbar_D Rqbar_q-Pbar_q Rqbar_D
Kgg_cond=Kgg-Kgr Krr^-1 Krg
```

## Zero-integration status

```text
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
N_formal_thickness_quadrature=0
```

## Capacity boundary

```text
Case21 368.189 kN = historical/current-support closure only
Z6 51.30 MN = retained engineering baseline only
Z0-Z5 old values = retracted/diagnostic under current governance
NEW current membrane r(D,q) solve = NOT_RUN
NEW membrane-redistributed Pu = NOT_RELEASED
```

## Current unique next gate

```text
UNIFIED_V1_FULL_R10_DUAL_HOLONOMIC_THICKNESS_MOMENT_RUNTIME_GATE
```

The next gate must connect the compact adjoint target DAG to the accepted 64-state thickness holonomic system without rebuilding a flat vector of canonical rational coefficient functions.

## Key artifacts

1. `../20_theory/nc_rebar_panel/20260816_2118__NZSCCM__FULL_R10_64_STATE_ADJOINT_CH_TARGET_REDUCTION__THEORY.md`
2. `../40_execution/common/20260816_2118__NZSCCM__FULL_R10_64_STATE_ADJOINT_CH_TARGET__EXECUTION_REPORT.md`
3. `../40_execution/common/20260816_2118__NZSCCM__FULL_R10_64_STATE_ADJOINT_CH_TARGET__PARAMS_AND_INTERMEDIATES.json`
4. `../40_execution/common/20260816_2118__NZSCCM__FULL_R10_64_STATE_ADJOINT_CH_TARGET__REPRO.py`
5. `../60_validation/common/20260816_2118__NZSCCM__FULL_R10_64_STATE_ADJOINT_CH_TARGET__AUDIT.md`
6. `../10_governance/20260816_2118__NZSCCM__FULL_R10_ADJOINT_CH_TARGET_AND_DUAL_HOLONOMIC_NEXT__GATE_LOCK.md`
7. `20260816_2059__NZSCCM__PROJECT__CURRENT_STATE_FULL_R10_64_STATE_ADJOINT_TARGET_OPEN__SEMANTIC_INDEX.md` — predecessor
