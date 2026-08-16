# NC + rebar panel theory semantic branch

## Current production identity

Historical/current-support anchor:

`20260812_2245__NZSCCM__NC_REBAR_PANEL__R10_N48C1MM_CH_NGUYEN_GENERAL_D15__THEORY_EXECUTION_CONTRACT.LOCATOR.md`

Current governance is `UNIFIED_PRODUCTION_WORKFLOW_V1`.

## Retained global RC skeleton

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
 -> global (D,q), A=bq
 -> Nguyen second-order continuous strain
 -> R10 concrete + reinforcement current laws
 -> compatible membrane redistribution internal solve
 -> finite matrix / analytic material representation
 -> General-D15 exact target moments
 -> P,Rq,L connected branch
 -> first +->- limit
 -> same-state KZ
```

## Five internal membrane coordinates

```text
r=[r0,r20,r22,s02,s22]
```

remain finite internal response coordinates with `Rm=0` and consistent Schur condensation. The outer root topology remains `(D,q)`.

## 19:32 nested RC1 boundary

`R10-MSAC-RC1` remains material-level source-fidelity PASS for Z0-Z6, but its nested beta/Chebyshev graph failed structural target preflight when the terminal algebra remained ordinary polynomial General-D15.

```text
ADJOINT_CLENSHAW_ALGEBRA = PASS_EXACT
ACTIVE_RC1_NESTED_TARGET_RUNTIME = FAIL_PREFLIGHT
```

No full nested flattening is permitted.

## 20:05 exact source matrix lift

The frozen R10 source law now has an exact finite matrix-function representation:

```text
Pi(E)=1/2 E^2 [sqrt(E^2+eta^2 I)+E] [E^2+eta^2 I]^-1
c=Pi(-E)
t=Pi(E)

C=kappa c [I+(kappa-2)c+c^2]^-1

uR = exact degree-5 C2 truncated-power spline in z=t/(rho/kappa)
T=uR/rho
T7=T^7

S =
U
- ACC det(C) C
+ C[tr(T)I-T]
- rho AT det(T)[tr(T^7)I-T^7]
```

Audit:

```text
R10_EXACT_SOURCE_MATRIX_LIFT = PASS_EXACT
UR_TRUNCATED_POWER_SPLINE = PASS_EXACT
R10_2D_STRESS_MATRIX_IDENTITY = PASS_EXACT
CONSISTENT_TANGENT_FINITE_GRAPH = PASS_FORMAL
MATERIAL_FIT_ORDER_DEPENDENCE_IN_SOURCE_GRAPH = ELIMINATED
```

The nested RC1 fit hierarchy is therefore retained only as a material reconstruction/audit reference, not as the preferred structural representation.

## Fixed algebraic atom boundary

The remaining non-polynomial atom families are

```text
sqrt(E^2+eta^2 I)
inverse(I+(kappa-2)c+c^2)
(t/a-I)_+^k, k=3..5
(t/a-10I)_+^k, k=3..5
```

Their General-D15/CAS target moments remain open.

```text
GENERAL_D15_ALGEBRAIC_ATOM_MOMENT_CLOSURE = OPEN
NEW_Pu = NOT_RUN
```

## Reinforcement adapter

Rebar continues to use the same redistributed continuous strain field and participates in `P_s,Rq_s,Rm,Krr,KZ` before condensation/root solve. No post-hoc `As*fy` capacity addition is introduced.

## Zero-integration lock

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

## Current artifacts

- `20260816_2005__NZSCCM__R10_EXACT_FINITE_MATRIX_SOURCE_LIFT_AND_FIXED_ALGEBRAIC_ATOMS__THEORY.md`
- `../../40_execution/common/20260816_2005__NZSCCM__R10_EXACT_FINITE_MATRIX_SOURCE_LIFT__EXECUTION_REPORT.md`
- `../../40_execution/common/20260816_2005__NZSCCM__R10_EXACT_FINITE_MATRIX_SOURCE_LIFT__PARAMS_AND_INTERMEDIATES.json`
- `../../40_execution/common/20260816_2005__NZSCCM__R10_EXACT_FINITE_MATRIX_SOURCE_LIFT__REPRO.py`
- `../../60_validation/common/20260816_2005__NZSCCM__R10_EXACT_FINITE_MATRIX_SOURCE_LIFT__AUDIT.md`
- `../../10_governance/20260816_2005__NZSCCM__R10_EXACT_MATRIX_SOURCE_LIFT_FIXED_ATOM_MOMENT__GATE_LOCK.md`
- `../../00_index/20260816_2005__NZSCCM__PROJECT__CURRENT_STATE_R10_EXACT_MATRIX_SOURCE_LIFT_FIXED_ATOM_OPEN__SEMANTIC_INDEX.md`
