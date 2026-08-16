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
 -> exact finite matrix / algebraic material representation
 -> exact/controlled General-D15 target moments
 -> P,Rq,L connected branch
 -> first +->- limit
 -> same-state KZ
```

## Five internal membrane coordinates

```text
r=[r0,r20,r22,s02,s22]
```

remain finite internal response coordinates with `Rm=0` and consistent Schur condensation. The outer root topology remains `(D,q)`.

## Historical compiler route retained as evidence

Historical/current-support RC production used finite material-coordinate polynomial compilers such as N48. Later RC1 source-fidelity work improved the material approximation but its nested polynomial structural contraction failed the common tractability gate. Those artifacts remain historical/audit evidence only.

## Current exact R10 source route

The frozen R10 physical law is now carried as an exact finite matrix/algebraic graph. Production material fit orders `N48/Ng/Nc/Nt` and an independently fitted `T7` are absent from this preferred candidate.

## 20:59 full three-generator quadratic-tower state

The exact R10 algebraic generators are represented as

```text
smooth: q_eta^2=Q_eta, s_eta^2=P_eta+2q_eta
knot1:  q_1^2=delta_1^2, s_1^2=A_1+2q_1
knot10: q_10^2=delta_10^2, s_10^2=A_10+2q_10
```

Each pair has local basis `[1,q,s,q*s]`, so the complete field has exactly

```text
4^3 = 64 states.
```

Each local pair has an exact four-state rational differential system and the full derivative operator is their Kronecker sum.

```text
FULL_64_STATE_DERIVATIVE_CLOSURE = PASS_EXACT
FULL_64_STATE_VECTOR_MOMENT_FORM = PASS_EXACT
A64_NONZEROS = 159 / 4096
```

For the retained noncommuting prototype, the common denominator degree of all local derivative coefficients is only `13`.

## Actual R10 source graph probe

The exact field arithmetic was executed through

```text
R_eta -> t,c -> shifted knot projectors -> uR -> T -> T7=T^7
```

and reached

```text
t entries = 3/64
uR entries = 20/64
T7 entries = 64/64
tr(T7) = 64/64.
```

Thus the 64-state compositum is actually occupied by the R10 graph.

The diagnostic runtime used rationalized knot constants only for symbolic timing; formal theory retains the exact R10 algebraic roots.

## Current fail-fast boundary

Naively flattening and canonicalizing all rational coefficients of `tr(T7)` exceeded the 60 s execution limit; even the smaller flattened `tr(uR)` coefficient vector exceeded the same limit.

```text
NAIVE_FLATTENED_RATIONAL_COEFFICIENT_NORMALIZATION = FAIL_TRACTABILITY
FULL_R10_THICKNESS_TARGET_CONTRACTION = PARTIAL_PASS_TO_ADJOINT_DAG_BOUNDARY
```

This does not reopen material physics or field dimension.  The exact field is fixed and finite.  The rejected architecture is only full coefficient-expression flattening.

The next implementation must perform target-side/adjoint contraction directly on the factorized 4x4x4 quadratic-tower DAG.  Unlike the failed old RC1 adjoint-Clenshaw route, every multiplication is reduced modulo the exact quadratic relations and algebraic state size cannot grow beyond 64.

## Reinforcement adapter

Rebar continues to use the same redistributed continuous strain field and contributes to `P_s,Rq_s,Rm,Krr,KZ` before condensation/root solve. No post-hoc `As*fy` capacity addition is introduced.

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
UNIFIED_V1_FULL_R10_64_STATE_ADJOINT_RATIONAL_TARGET_REDUCTION_GATE
```

## Current artifacts

- `20260816_2059__NZSCCM__FULL_R10_QUADRATIC_TOWER_64_STATE_THICKNESS_COMPOSITUM__THEORY.md`
- `../../40_execution/common/20260816_2059__NZSCCM__FULL_R10_QUADRATIC_TOWER_64_STATE__EXECUTION_REPORT.md`
- `../../40_execution/common/20260816_2059__NZSCCM__FULL_R10_QUADRATIC_TOWER_64_STATE__PARAMS_AND_INTERMEDIATES.json`
- `../../40_execution/common/20260816_2059__NZSCCM__FULL_R10_QUADRATIC_TOWER_64_STATE__REPRO.py`
- `../../60_validation/common/20260816_2059__NZSCCM__FULL_R10_QUADRATIC_TOWER_64_STATE__AUDIT.md`
- `../../10_governance/20260816_2059__NZSCCM__FULL_R10_64_STATE_ADJOINT_TARGET_NEXT__GATE_LOCK.md`
- `../../00_index/20260816_2059__NZSCCM__PROJECT__CURRENT_STATE_FULL_R10_64_STATE_ADJOINT_TARGET_OPEN__SEMANTIC_INDEX.md`
- `20260816_2034__NZSCCM__HISTORICAL_RC_VS_CURRENT_EXACT_ALGEBRAIC_METHOD_DELTA__NOTE.md` — retained comparison note
