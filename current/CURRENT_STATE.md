# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-16 20:59 +08:00  
**Status:** LEGACY MUTABLE POINTER ONLY

## Current operational entry

`semantic_v2/00_index/20260816_2059__NZSCCM__PROJECT__CURRENT_STATE_FULL_R10_64_STATE_ADJOINT_TARGET_OPEN__SEMANTIC_INDEX.md`

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

with current-material equilibrium and consistent Schur condensation retained.

## Retained predecessor results

```text
five-term elastic Airy/FvK recovery = PASS_EXACT
five membrane General-D15 targets = PASS
20:05 exact finite-matrix R10 source lift = PASS_EXACT
20:14 scalar quartic atom reduction = PASS_EXACT
20:34 noncommuting smooth-quartic holonomic thickness recurrence = PASS_EXACT
```

## 20:59 full R10 three-generator compositum state

The exact atom families `s_eta,s_1,s_10` are represented as three quadratic towers

```text
q^2=Q(x)
s^2=A(x)+2q
basis=[1,q,s,q*s]
```

and the complete field basis has exactly

```text
4 x 4 x 4 = 64 states.
```

Each local four-state derivative operator is exact and the full derivative operator is the Kronecker sum of the three blocks.

```text
FULL_64_STATE_DERIVATIVE_CLOSURE = PASS_EXACT
FULL_64_STATE_VECTOR_MOMENT_FORM = PASS_EXACT
A64_NONZEROS = 159 / 4096
```

For the retained noncommuting prototype, the LCM denominator degree of the nine local derivative coefficients is `13`.

## Actual R10 source graph reaches the complete field

The exact source graph was executed through

```text
R_eta -> t,c -> shifted knot projectors -> uR -> T -> T7=T^7
```

inside the fixed field.

Observed support:

```text
t entries = 3/64
uR entries = 20/64
T7 entries = 64/64
tr(T7) = 64/64
```

The raw `T^7` field multiplication took about `36.95 s` in the diagnostic Python/SymPy implementation.

The knot rationalization used in that timing probe is diagnostic only; the formal material law retains the exact algebraic R10 knot roots.

## Current implementation boundary

Naively flattening and canonicalizing all rational coefficients of `tr(T7)` exceeded the 60 s execution limit. A smaller flattened `tr(uR)` canonicalization also exceeded the limit.

Therefore:

```text
THREE_GENERATOR_QUADRATIC_TOWER = PASS_EXACT_PARAMETRIC
FULL_R10_T7_64_BASIS_SUPPORT = PASS_EXECUTED_DIAGNOSTIC
NAIVE_FLATTENED_RATIONAL_COEFFICIENT_NORMALIZATION = FAIL_TRACTABILITY
FULL_R10_THICKNESS_TARGET_CONTRACTION = PARTIAL_PASS_TO_ADJOINT_DAG_BOUNDARY
```

This is not a return of the old polynomial-degree explosion: the algebraic state remains fixed at 64. The rejected implementation is only full rational-expression flattening.

The next implementation must keep the 4x4x4 factor graph and perform target-side/adjoint rational reduction in the fixed state.

## Capacity status

```text
Case21 368.189 kN = historical/current-support closure only
Z6 51.30 MN = retained engineering baseline only
Z0-Z5 old values = retracted/diagnostic under current governance
NEW current membrane r(D,q) solve = NOT_RUN
NEW membrane-redistributed Pu = NOT_RELEASED
```

## Current unique next gate

```text
UNIFIED_V1_FULL_R10_64_STATE_ADJOINT_RATIONAL_TARGET_REDUCTION_GATE
```

## Current key artifacts

- `semantic_v2/00_index/20260816_2059__NZSCCM__PROJECT__CURRENT_STATE_FULL_R10_64_STATE_ADJOINT_TARGET_OPEN__SEMANTIC_INDEX.md`
- `semantic_v2/20_theory/nc_rebar_panel/20260816_2059__NZSCCM__FULL_R10_QUADRATIC_TOWER_64_STATE_THICKNESS_COMPOSITUM__THEORY.md`
- `semantic_v2/40_execution/common/20260816_2059__NZSCCM__FULL_R10_QUADRATIC_TOWER_64_STATE__EXECUTION_REPORT.md`
- `semantic_v2/40_execution/common/20260816_2059__NZSCCM__FULL_R10_QUADRATIC_TOWER_64_STATE__PARAMS_AND_INTERMEDIATES.json`
- `semantic_v2/40_execution/common/20260816_2059__NZSCCM__FULL_R10_QUADRATIC_TOWER_64_STATE__REPRO.py`
- `semantic_v2/60_validation/common/20260816_2059__NZSCCM__FULL_R10_QUADRATIC_TOWER_64_STATE__AUDIT.md`
- `semantic_v2/10_governance/20260816_2059__NZSCCM__FULL_R10_64_STATE_ADJOINT_TARGET_NEXT__GATE_LOCK.md`
