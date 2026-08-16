# NZ-SCCM semantic tree v2

This namespace is the **content-first, non-destructive semantic reconstruction** of the repository.

## Current operational entry

Use first:

`20260816_2059__NZSCCM__PROJECT__CURRENT_STATE_FULL_R10_64_STATE_ADJOINT_TARGET_OPEN__SEMANTIC_INDEX.md`

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

## Exact R10 algebraic route

The frozen R10 physical law is unchanged.  The preferred current structural representation is the exact finite matrix/algebraic source graph rather than an N48/RC1 material-coordinate polynomial compiler.

## 20:59 full three-generator quadratic-tower state

The retained atom families `s_eta,s_1,s_10` are represented as three exact nested quadratic pairs

```text
q^2=Q
s^2=A+2q
basis=[1,q,s,q*s]
```

so the full compositum basis has exactly `4^3=64` states.

The full derivative system is a Kronecker sum of three local 4x4 blocks and has only

```text
159 nonzeros / 4096 possible entries.
```

The complete 64-state vector thickness moments satisfy one exact denominator-cleared integration-by-parts recurrence.

```text
THREE_GENERATOR_QUADRATIC_TOWER = PASS_EXACT_PARAMETRIC
FULL_64_STATE_DERIVATIVE_CLOSURE = PASS_EXACT
FULL_64_STATE_VECTOR_MOMENT_FORM = PASS_EXACT
```

## Actual R10 graph probe

The exact field graph was executed through

```text
R_eta -> t,c -> knot projectors -> uR -> T -> T7=T^7.
```

The diagnostic prototype reaches the complete field:

```text
t entries = 3/64
uR entries = 20/64
T7 entries = 64/64
tr(T7) = 64/64
```

Thus the full compositum is not merely a formal upper bound.

## Current implementation boundary

Naively flattening/canonicalizing all rational coefficients of the complete `tr(T7)` field exceeded the 60 s execution window; even flattened `tr(uR)` canonicalization exceeded the same limit.

```text
NAIVE_FLATTENED_RATIONAL_COEFFICIENT_NORMALIZATION = FAIL_TRACTABILITY
FULL_R10_THICKNESS_TARGET_CONTRACTION = PARTIAL_PASS_TO_ADJOINT_DAG_BOUNDARY
```

This does not reopen the field dimension or material physics.  The next runtime must keep the fixed 4x4x4 factor graph and perform target-side/adjoint rational reduction without coefficient flattening.

Unlike the 19:32 RC1 adjoint-Clenshaw failure, every multiplication here is reduced modulo exact quadratic relations and the algebraic state cannot grow beyond 64.

## Capacity boundary

```text
Case21 368.189 kN = historical/current-support closure only
Z6 51.30 MN = retained engineering baseline only
Z0-Z5 old values = retracted/diagnostic under current governance
NEW membrane-redistributed Pu = not released
```

## Current next gate

```text
UNIFIED_V1_FULL_R10_64_STATE_ADJOINT_RATIONAL_TARGET_REDUCTION_GATE
```

## Repository semantic read order

1. `20260816_2059__NZSCCM__PROJECT__CURRENT_STATE_FULL_R10_64_STATE_ADJOINT_TARGET_OPEN__SEMANTIC_INDEX.md`
2. `../10_governance/20260816_2059__NZSCCM__FULL_R10_64_STATE_ADJOINT_TARGET_NEXT__GATE_LOCK.md`
3. `../20_theory/nc_rebar_panel/20260816_2059__NZSCCM__FULL_R10_QUADRATIC_TOWER_64_STATE_THICKNESS_COMPOSITUM__THEORY.md`
4. `../40_execution/common/20260816_2059__NZSCCM__FULL_R10_QUADRATIC_TOWER_64_STATE__EXECUTION_REPORT.md`
5. `../40_execution/common/20260816_2059__NZSCCM__FULL_R10_QUADRATIC_TOWER_64_STATE__PARAMS_AND_INTERMEDIATES.json`
6. `../40_execution/common/20260816_2059__NZSCCM__FULL_R10_QUADRATIC_TOWER_64_STATE__REPRO.py`
7. `../60_validation/common/20260816_2059__NZSCCM__FULL_R10_QUADRATIC_TOWER_64_STATE__AUDIT.md`
8. `20260816_2034__NZSCCM__PROJECT__CURRENT_STATE_NONCOMMUTING_QUARTIC_HOLONOMIC_PASS_FULL_R10_COMPOSITUM_OPEN__SEMANTIC_INDEX.md` — predecessor
9. `20260816_2014__NZSCCM__PROJECT__CURRENT_STATE_QUARTIC_ALGEBRAIC_PERIOD_HOLONOMIC_OPEN__SEMANTIC_INDEX.md` — predecessor
10. `20260816_2005__NZSCCM__PROJECT__CURRENT_STATE_R10_EXACT_MATRIX_SOURCE_LIFT_FIXED_ATOM_OPEN__SEMANTIC_INDEX.md` — predecessor

No legacy file is deleted, moved or renamed solely from filename identity.
