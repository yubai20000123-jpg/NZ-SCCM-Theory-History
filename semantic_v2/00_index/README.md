# NZ-SCCM semantic tree v2

This namespace is the **content-first, non-destructive semantic reconstruction** of the repository.

## Current operational entry

Use first:

`20260816_2005__NZSCCM__PROJECT__CURRENT_STATE_R10_EXACT_MATRIX_SOURCE_LIFT_FIXED_ATOM_OPEN__SEMANTIC_INDEX.md`

## Frozen production backbone

```text
UNIFIED_PRODUCTION_WORKFLOW_V1
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order continuous kinematics
MEMBRANE_STRESS_REDISTRIBUTION = REQUIRED
R10 source current material operator = FROZEN
reinforcement/steel phase before root solve
same-state current stress + consistent tangent
Cayley-Hamilton / approved finite matrix lift
General-D15 exact target moments
P,Rq,L connected-branch topology
same-state material + geometric KZ
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
N_formal_thickness_quadrature=0
```

## Five-term membrane model retained

Global production remains `(D,q)`. Compatible membrane redistribution uses internal coordinates

```text
r=[r0,r20,r22,s02,s22]
```

with `Rm=0` and consistent Schur condensation. The exact elastic Airy/FvK recovery and the five General-D15 residual targets remain PASS.

## 19:32 nested-RC1 target boundary retained

```text
ADJOINT_CLENSHAW_ALGEBRA = PASS_EXACT
LOW_ORDER_GENERAL_D15_TARGET_IDENTITY = PASS_EXACT
ACTIVE_RC1_NESTED_TARGET_RUNTIME = FAIL_PREFLIGHT
```

Target-side recurrence does not remove nested polynomial composition degree when ordinary polynomial D15 remains the only leaf algebra.

## 20:05 exact R10 finite-matrix source lift

The frozen R10 source now has an exact finite matrix representation:

```text
Pi(E)=1/2 E^2 [sqrt(E^2+eta^2 I)+E] [E^2+eta^2 I]^-1
c=Pi(-E), t=Pi(E)
C=kappa c [I+(kappa-2)c+c^2]^-1

uR = exact C2 degree-5 truncated-power spline in t/(rho/kappa)
T=uR/rho
T7=T^7
```

and the full 2D stress is exactly

```text
S =
U
- ACC det(C) C
+ C [tr(T)I-T]
- rho AT det(T) [tr(T^7)I-T^7].
```

Audit status:

```text
R10_EXACT_SOURCE_MATRIX_LIFT = PASS_EXACT
UR_TRUNCATED_POWER_SPLINE = PASS_EXACT
R10_2D_STRESS_MATRIX_IDENTITY = PASS_EXACT
FIXED_ALGEBRAIC_ATOM_GRAPH = PASS_FORMAL
```

The previous material fit-order hierarchy `Ng,Nc,Nt` is absent from this structural candidate. `R10-MSAC-RC1` remains a retained material-level source-fidelity reference.

## Remaining fixed atom problem

```text
sqrt(E^2+eta^2 I)
inverse(I+(kappa-2)c+c^2)
(t/a-I)_+^k, k=3..5
(t/a-10I)_+^k, k=3..5
```

Their exact/controlled `P,Rq,Rm,KZ` target moments remain open.

```text
GENERAL_D15_ALGEBRAIC_ATOM_MOMENT_CLOSURE = OPEN
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
UNIFIED_V1_R10_FIXED_ALGEBRAIC_ATOM_GENERAL_D15_CAS_MOMENT_CLOSURE_GATE
```

## Repository semantic read order

1. `20260816_2005__NZSCCM__PROJECT__CURRENT_STATE_R10_EXACT_MATRIX_SOURCE_LIFT_FIXED_ATOM_OPEN__SEMANTIC_INDEX.md`
2. `../10_governance/20260816_2005__NZSCCM__R10_EXACT_MATRIX_SOURCE_LIFT_FIXED_ATOM_MOMENT__GATE_LOCK.md`
3. `../20_theory/nc_rebar_panel/20260816_2005__NZSCCM__R10_EXACT_FINITE_MATRIX_SOURCE_LIFT_AND_FIXED_ALGEBRAIC_ATOMS__THEORY.md`
4. `../40_execution/common/20260816_2005__NZSCCM__R10_EXACT_FINITE_MATRIX_SOURCE_LIFT__EXECUTION_REPORT.md`
5. `../40_execution/common/20260816_2005__NZSCCM__R10_EXACT_FINITE_MATRIX_SOURCE_LIFT__PARAMS_AND_INTERMEDIATES.json`
6. `../40_execution/common/20260816_2005__NZSCCM__R10_EXACT_FINITE_MATRIX_SOURCE_LIFT__REPRO.py`
7. `../60_validation/common/20260816_2005__NZSCCM__R10_EXACT_FINITE_MATRIX_SOURCE_LIFT__AUDIT.md`
8. `20260816_1932__NZSCCM__PROJECT__CURRENT_STATE_RC1_ADJOINT_TARGET_PREFLIGHT_FAIL__SEMANTIC_INDEX.md` — predecessor
9. `20260816_1912__NZSCCM__PROJECT__CURRENT_STATE_FIVE_TERM_MEMBRANE_CONDENSATION_PARTIAL_PASS__SEMANTIC_INDEX.md` — predecessor
10. `20260816_1734__NZSCCM__PROJECT__CURRENT_STATE_R10_MSAC_RC1_MATERIAL_PASS__SEMANTIC_INDEX.md` — compiler predecessor

No legacy file is deleted, moved or renamed solely from filename identity.
