# NZ-SCCM current state — exact R10 finite-matrix source lift / fixed algebraic atoms

**Timestamp:** 2026-08-16 20:05 +08:00

## Current verdict

The 19:32 adjoint-Clenshaw structural adapter failure is retained. Instead of returning to nested polynomial expansion, the frozen R10 source law has now been rewritten as an exact finite 2x2 matrix-function graph.

```text
R10_EXACT_SMOOTH_SPLIT_MATRIX_LIFT = PASS_EXACT
UR_TRUNCATED_POWER_SPLINE = PASS_EXACT
R10_2D_STRESS_INVARIANT_MATRIX_IDENTITY = PASS_EXACT
CONSISTENT_TANGENT_FINITE_GRAPH = PASS_FORMAL
INDEPENDENT_T7_COMPILER_CHANNEL = ELIMINATED
MATERIAL_FIT_ORDER_DEPENDENCE_IN_SOURCE_GRAPH = ELIMINATED
FIXED_ALGEBRAIC_ATOM_GRAPH = PASS_FORMAL
GENERAL_D15_ALGEBRAIC_ATOM_MOMENT_CLOSURE = OPEN
NEW_Pu = NOT_RUN
```

## What changed

The structural material representation no longer needs the RC1 nested hierarchy

```text
beta-lens -> Chebyshev -> natural-coordinate lens -> Chebyshev
```

or the active `Ng,Nc,Nt` fit orders.

The source law itself is represented exactly by:

```text
Pi(E) = 1/2 E^2 [sqrt(E^2+eta^2 I)+E] [E^2+eta^2 I]^-1
c=Pi(-E), t=Pi(E)

C = kappa c [I+(kappa-2)c+c^2]^-1

uR = exact degree-5 truncated-power spline in z=t/(rho/kappa)
     with knots z=1 and z=10

T=uR/rho
T7=T^7
```

The full 2D principal interaction is exactly

```text
S =
U
- ACC det(C) C
+ C [tr(T) I - T]
- rho AT det(T) [tr(T^7) I - T^7]
```

## Exactness audit

Symbolic spline branch residuals are zero exactly.

Across 500 deterministic random symmetric matrix states per Z0-Z6 guard domain, the maximum matrix-stress identity error is approximately `8.05e-15`.

No structural spatial sample or quadrature point is used.

## Retained membrane model

Global coordinates remain

```text
(D,q)
```

and the five membrane redistribution coordinates remain internal:

```text
r=[r0,r20,r22,s02,s22]
```

with

```text
Rm=0
Krr=dRm/dr
r_g=-Krr^-1 Rm_g
Pbar_g=P_g+P_r r_g
Rqbar_g=Rq_g+Rq_r r_g
Lbar=Pbar_D Rqbar_q-Pbar_q Rqbar_D
Kgg_cond=Kgg-Kgr Krr^-1 Krg
```

No new internal solve or Pu has yet been run.

## Fixed remaining atom problem

The material-order explosion is removed, but structural moments of the fixed algebraic atoms remain open:

```text
sqrt(E^2+eta^2 I)
inverse(I+(kappa-2)c+c^2)
(t/a-I)_+^k, k=3..5
(t/a-10I)_+^k, k=3..5
```

The next backend must close these atoms directly under existing `P,Rq,Rm,KZ` target kernels through General-D15/CAS/special-function/holonomic algebra, while preserving zero formal spatial integration.

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
NEW membrane-redistributed Pu = NOT RELEASED
```

## Current unique next gate

```text
UNIFIED_V1_R10_FIXED_ALGEBRAIC_ATOM_GENERAL_D15_CAS_MOMENT_CLOSURE_GATE
```

## Key artifacts

1. `../20_theory/nc_rebar_panel/20260816_2005__NZSCCM__R10_EXACT_FINITE_MATRIX_SOURCE_LIFT_AND_FIXED_ALGEBRAIC_ATOMS__THEORY.md`
2. `../40_execution/common/20260816_2005__NZSCCM__R10_EXACT_FINITE_MATRIX_SOURCE_LIFT__EXECUTION_REPORT.md`
3. `../40_execution/common/20260816_2005__NZSCCM__R10_EXACT_FINITE_MATRIX_SOURCE_LIFT__PARAMS_AND_INTERMEDIATES.json`
4. `../40_execution/common/20260816_2005__NZSCCM__R10_EXACT_FINITE_MATRIX_SOURCE_LIFT__REPRO.py`
5. `../60_validation/common/20260816_2005__NZSCCM__R10_EXACT_FINITE_MATRIX_SOURCE_LIFT__AUDIT.md`
6. `../10_governance/20260816_2005__NZSCCM__R10_EXACT_MATRIX_SOURCE_LIFT_FIXED_ATOM_MOMENT__GATE_LOCK.md`
7. `20260816_1932__NZSCCM__PROJECT__CURRENT_STATE_RC1_ADJOINT_TARGET_PREFLIGHT_FAIL__SEMANTIC_INDEX.md` — predecessor
