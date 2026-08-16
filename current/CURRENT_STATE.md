# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-16 12:29 +08:00  
**Status:** LEGACY MUTABLE POINTER ONLY

## Current operational entry

`semantic_v2/00_index/20260816_1229__NZSCCM__PROJECT__CURRENT_STATE_NC_FAMILY_COMPILER_SOURCE_FREEZE_PASS__SEMANTIC_INDEX.md`

## Frozen project-wide production backbone

```text
UNIFIED_PRODUCTION_WORKFLOW_V1 = ACTIVE
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
HALFWAVE_SELECTION = source/design-side physical rule
Nguyen second-order continuous kinematics = ACTIVE
MEMBRANE_STRESS_REDISTRIBUTION = REQUIRED
source current material operator = REQUIRED
same-state consistent current tangent = REQUIRED
Cayley-Hamilton / approved finite matrix lift = ACTIVE
General D15 moment-first exact moments = ACTIVE
P,Rq,L connected-branch root topology = ACTIVE
same-state material + geometric KZ audit = ACTIVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
Gauss/Simpson/adaptive/collocation/material-point-grid = PROHIBITED
experiment/Zhou/Winter calibration in solve/compiler = PROHIBITED
```

The four intended combinations remain under this one workflow:

```text
ordinary concrete + reinforcement
ordinary concrete + steel shell
UHPC + reinforcement
UHPC + steel shell
```

Physical adapters may differ, but they may not replace the common kinematics, membrane redistribution, zero-integration philosophy, generalized root topology or tangent-consistency rules.

## NC family compiler — source-fidelity freeze PASS

The ordinary-concrete source operator remains the frozen R10 current operator.

Current family compiler contract:

```text
NC operational principal-coordinate core = [-2.35,+1.90]
NC coefficient-generation guard         = [-2.60,+2.15]
channels = U,C,T,T7
one global Chebyshev polynomial per channel
same order for all four channels
M = 8*(N+1) Gauss-Chebyshev material coordinates
exact R10 C1 anchors at lambda=0
```

Material-coordinate coefficient/audit points are not structural material points.

### Frozen source-fidelity thresholds

```text
E_sigma <= 0.005
E_tangent <= 0.05
E_divided_difference <= 0.05
```

These are assembled-current-operator source errors, not structural-load errors.

### Deterministic order selection

```text
48,96,192,384,768,
then +256 beginning at 1024
```

Reference R10 result:

```text
N=3328: E_sigma=0.001414, E_tangent=0.055699 -> FAIL tangent
N=3584: E_sigma=0.001072, E_tangent=0.040665, E_div=0.003814 -> PASS
```

Therefore

```text
NC_FAMILY_ORDER = 3584
NC_FAMILY_SOURCE_COMPILER_FREEZE = PASS
```

The same order/core/guard/algorithm passes the current Swartz R10 `kappa` envelope:

```text
kappa_min = 1.9993148515: E_sigma=0.0010695, E_tangent=0.0406008
kappa_ref = 2.0005129533678754: E_sigma=0.0010722, E_tangent=0.0406652
kappa_max = 2.0008935611: E_sigma=0.0010730, E_tangent=0.0406856
```

The compiler coefficients remain O(1); maximum absolute coefficient is about `0.512`, maximum coefficient l1 sum about `2.082`.

The frozen object is a **family compiler protocol/order/domain**. Actual coefficients may depend on physical R10 material parameters such as `kappa`; this is not a specimen-specific calculation method. A future NC material input outside the audited parameter/core domain triggers family-level audit/recompile, not an ad hoc case order.

## Structural backend status

Every frozen R10 channel is still a finite polynomial, so Cayley-Hamilton and General-D15 remain formally compatible.

However:

```text
N3584_HIGH_ORDER_CH_MOMENT_FIRST_D15_BACKEND = NOT_YET_EXECUTED
NAIVE_FULL_STRESS_FIELD_EXPANSION = PROHIBITED
NEW_Z0_Z6_UNIFIED_RESULTS = NOT_YET_CALCULATED
```

The next implementation must be order-agnostic/factorized and moment-first; it may not first expand a huge full spatial stress polynomial.

## Capacity-result status

```text
Z6_AR2_Pu = 51.30 MN  # retained user-accepted engineering baseline only
Z6_UNIFIED_RERUN = REQUIRED
Z0_Z5_20260816_1043_Pu = RETRACTED_PENDING_UNIFIED_RERUN
Z0_Z5_20260816_1043_ZHOU_WINTER_TABLE = RETRACTED_PENDING_UNIFIED_RERUN
```

Z0-Z5 remain computationally solvable; the old values were withdrawn because they exposed the former compiler-fidelity defect. Z6 is not exempt and must be rerun under the frozen NC family workflow.

## Mandatory intermediate-state record

Every future production run must preserve at least:

1. specimen/source inputs;
2. boundary and halfwave selection;
3. material family/compiler identity, source parameters, core/guard, order and source errors;
4. `D,q,A=q*b` and any source-grounded finite internal amplitudes;
5. continuous principal/invariant material envelope;
6. phase load and `Rq` decompositions;
7. `P_D,P_q,Rq_D,Rq_q,L` or exact condensed equivalents;
8. internal residual/condensation conditioning where applicable;
9. same-state material/geometric `KZ` phase decomposition;
10. branch/peak bracket;
11. formal spatial/thickness counters.

## Current unique next gate

`UNIFIED_V1_N3584_CH_MOMENT_FIRST_D15_BACKEND_AND_Z0_Z6_RERUN_GATE`

Required order:

1. implement the order-agnostic/factorized Cayley-Hamilton recurrence at frozen `N_NC=3584`;
2. connect it directly to moment-first General-D15 without naive full-field expansion;
3. audit complexity, coefficient conditioning and exact-moment consistency;
4. use the same backend/compiler to rerun Z0-Z6;
5. verify every continuous reachable NC spectrum stays in `[-2.35,+1.90]`;
6. calculate `P,Rq,L` and same-state `KZ` under the common V1 contract;
7. only after roots are frozen compare with the retained Z6 baseline and Zhou/Winter/experiments.

## Current key artifacts

- `semantic_v2/10_governance/20260816_1229__NZSCCM__NC_FAMILY_COMPILER_SOURCE_FIDELITY_AND_ORDER_FREEZE__LOCK.md`
- `semantic_v2/40_execution/common/20260816_1229__NZSCCM__NC_FAMILY_COMPILER_FREEZE__EXECUTION_REPORT.md`
- `semantic_v2/40_execution/common/20260816_1229__NZSCCM__NC_FAMILY_COMPILER_FREEZE__PARAMS_AND_INTERMEDIATES.json`
- `semantic_v2/40_execution/common/20260816_1229__NZSCCM__NC_FAMILY_COMPILER_FREEZE__REPRO.py`
- `semantic_v2/00_index/20260816_1229__NZSCCM__PROJECT__CURRENT_STATE_NC_FAMILY_COMPILER_SOURCE_FREEZE_PASS__SEMANTIC_INDEX.md`
- `semantic_v2/20_theory/20260816_1217__NZSCCM__UNIFIED_PRODUCTION_WORKFLOW_V1__THEORY_AND_EXECUTION_CONTRACT.md`
