# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-16 12:17 +08:00  
**Status:** LEGACY MUTABLE POINTER ONLY

## Current operational entry

`semantic_v2/00_index/20260816_1217__NZSCCM__PROJECT__CURRENT_STATE_UNIFIED_PRODUCTION_WORKFLOW_V1__SEMANTIC_INDEX.md`

## Frozen project-wide production backbone

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
HALFWAVE_SELECTION = physical/source boundary + theoretical/design energy rule
Nguyen second-order kinematics = ACTIVE
MEMBRANE_STRESS_REDISTRIBUTION = REQUIRED
source current material operator = REQUIRED
material-family finite analytic compiler under common interface = REQUIRED
Cayley-Hamilton / approved finite matrix lift = ACTIVE
General D15 moment-first exact moments = ACTIVE
common generalized P,Rq,L / connected-branch root logic = ACTIVE
same-state consistent current tangent/stability audit = ACTIVE
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
N_formal_thickness_quadrature=0
Gauss/Simpson/adaptive/collocation/cells/material-point-grid=PROHIBITED
structural calibration to experiment/Zhou/Winter=PROHIBITED
```

The physical boundary itself may differ between genuine specimen families, but it is frozen before the solve from source/geometry. The current Zhou Z-series uses the theoretical four-edge simply-supported/Navier boundary.

## Four target combinations under one workflow

1. ordinary concrete + reinforcement;
2. ordinary concrete + steel shell;
3. UHPC + reinforcement;
4. UHPC + steel shell.

The project now distinguishes **common invariants** from **legitimate physical adapters**.

### Common invariants

- one continuous complete representative halfwave;
- Nguyen second-order continuous strain field;
- membrane stress redistribution retained for every specimen;
- current stress operator and consistent current tangent from the same material state;
- moment-first General-D15 exact structural moments;
- zero formal structural spatial/thickness quadrature;
- additive phase assembly into the same `P,Rq` system;
- same-expression derivatives and common `L` determinant;
- connected physical branch and first admissible `+ -> -` maximum;
- same-state material + geometric tangent/stability audit;
- no experiment/Zhou/Winter in material compiler, halfwave, root or parameter selection.

### Legitimate physical adapters

- NC versus UHPC source material operator;
- rebar directional/layer phase versus finite-thickness shell phase;
- source-grounded shell local amplitudes, when physically active, with exact algebraic condensation;
- boundary/halfwave formula where a different real specimen boundary requires it;
- material-family analytic basis/order details required to represent the source operator.

A physical adapter may change its local formulas but may not change the parent kinematics, integration philosophy, global root topology or tangent-consistency requirements.

## Common global / internal state contract

Every production run exposes

```text
global coordinates = (D,q)
A = q*b
```

and may expose a finite internal vector `a=(A1,...,An)` only when a source-grounded structural mechanism such as shell local buckling requires it.

Internal coordinates satisfy `R_a=0` and are exactly condensed by

```text
a_g = -R_aa^-1 R_ag
P_g_tilde  = P_g  + P_a  a_g
Rq_g_tilde = Rq_g + Rq_a a_g
Kgg_cond   = Kgg - Kga Kaa^-1 Kag
```

This is not spatial discretization.

## Common limit and stability contract

Without internal coordinates,

```text
P = sum(P_phase)
Rq = sum(Rq_phase)
L = P_D*Rq_q - P_q*Rq_D
```

With internal coordinates use the exactly condensed derivatives in the same determinant.

Primary capacity:

```text
connected physical branch
Rq = 0
L = 0
first admissible + -> - load maximum
```

Same-branch stability:

```text
KZ = sum(KZ_mat_phase + KZ_geo_phase)
```

using the current consistent tangent and the same current stress field. A frozen pre-buckling elastic tangent is not an admissible substitute.

## Material compiler governance — V1

The project is not locked to `N=48` for its own sake.

```text
POLYNOMIAL_ORDER_IS_NOT_A_THEORY_IDENTITY
CASE_BY_CASE_MANUAL_ORDER_TUNING = PROHIBITED
CASE_ID_IN_COMPILER_OBJECTIVE = PROHIBITED
STRUCTURAL_Pu_IN_COMPILER_OBJECTIVE = PROHIBITED
EXPERIMENT_ZHOU_WINTER_IN_COMPILER_OBJECTIVE = PROHIBITED
```

The common compiler **interface/governance** is fixed:

```text
source current operator
-> finite analytic representation
-> source-value fidelity audit
-> source-tangent fidelity audit
-> deterministic family convergence/order/domain rule
-> frozen material-family compiler
-> common matrix lift + D15 structural backend
```

The internal analytic basis/order may differ between NC and UHPC if their source operators require it. Once frozen, however:

```text
NC+rebar and NC+shell -> same NC family compiler
UHPC+rebar and UHPC+shell -> same UHPC family compiler
```

If a later specimen exits a family domain, the family domain is enlarged and that family is recompiled/rerun consistently; no one-off specimen compiler is allowed.

## Material-family status

### Ordinary concrete

```text
source current operator = R10 frozen / unchanged
old Z6-wide N48 coefficient set = NOT ACCEPTABLE AS FAMILY FIDELITY PROOF
single-global-N48 coefficient-only repair = FAIL_REPRESENTATION_CAPACITY
NC family compiler under V1 = NOT YET FROZEN
```

### UHPC

The repository contains UHPC source/evidence and historical operator development, but no final production multidimensional UHPC current operator is yet frozen. UHPC parameters, material-domain details and converged representation order must not be copied from NC. Once frozen, the UHPC operator enters the same V1 compiler interface and structural backend.

## Steel-phase status

Reinforcement and steel shell are phase adapters.

- rebar: exact directional strain/resultant/current-tangent terms;
- shell: exact finite-thickness current stress/resultant/current-tangent terms;
- shell local buckling: finite internal amplitudes only where source-grounded, handled by exact condensation;
- no shell thickness Gauss points.

The shell 2D current material operator must be source-frozen/verified before production use; the structural shell adapter and zero-quadrature D15 closure are current support.

## Z6 versus Z0-Z5 consistency

There is no fundamental solver inability to calculate Z0-Z5. The 10:43 kernel produced numerical connected-branch roots for all of them. Z0-Z5 exposed the compiler-fidelity defect that had not been a rejection gate when Z6 was accepted.

```text
Z0_Z5_ARE_COMPUTATIONALLY_SOLVABLE = YES
Z0_Z5_1043_RESULTS_ARE_PRODUCTION_RELIABLE = NO

Z6_AR2_Pu = 51.30 MN
Z6_51_30_STATUS = USER_ACCEPTED_ENGINEERING_BASELINE
Z6_51_30_IS_COMPILER_FIDELITY_PROOF = NO
Z6_UNIFIED_WORKFLOW_RERUN = REQUIRED_AFTER_NC_COMPILER_FREEZE
```

Z6 final old material envelope was

```text
lambda_min = -2.2936943231
lambda_max = +1.8232424497
```

so it also contains the small-positive transition later shown to be poorly represented by the wide N48 compiler. Therefore Z6 is not exempt from the common family-compiler gate.

## Capacity-result status

```text
Z6_AR2_Pu = 51.30 MN  # retained user-accepted engineering baseline
Z0_Z5_20260816_1043_Pu = RETRACTED_PENDING_UNIFIED_RERUN
Z0_Z5_20260816_1043_ZHOU_WINTER_TABLE = RETRACTED_PENDING_UNIFIED_RERUN
NEW_Z0_Z6_UNIFIED_RESULTS = NOT YET CALCULATED
```

The withdrawn interpretation that membrane redistribution itself caused the former 20–36% Z0–Z4 loss remains withdrawn.

## Mandatory intermediate-state record for every production run

Every run must persist:

1. source/specimen input record;
2. boundary + halfwave selector result;
3. material-family compiler identity/domain/value+tangent errors;
4. `D,q` and all active finite internal amplitudes;
5. material principal/invariant envelope;
6. phase load decomposition;
7. phase `Rq` decomposition;
8. `P_D,P_q,Rq_D,Rq_q,L` or exact condensed counterparts;
9. internal residual/condensation conditioning where applicable;
10. current material/geometric `KZ` phase decomposition;
11. branch/peak bracket;
12. formal spatial/thickness counters.

The schema is stored in:
`semantic_v2/40_execution/common/20260816_1217__NZSCCM__UNIFIED_WORKFLOW_V1__INTERMEDIATE_STATE_SCHEMA_AND_CURRENT_BASELINE.json`.

## Historical diagnostics retained

- 10:54: old Z6-wide N48 has order-one T/T7 error inside the Z0-Z5 occupied mixed tension/compression range.
- 11:10: increased approximation capacity can represent R10 accurately; the ad hoc multirate orders remain diagnostic only.
- 11:34: coefficient optimization alone inside one global N48 polynomial is insufficient.
- 12:05: Z6 is not exempt from compiler-fidelity governance.
- 12:17: workflow governance is modular-unified: common mechanics are frozen; genuine material/phase/boundary adapters may differ without becoming separate specimen-specific methods.

## Current unique next gate

`UNIFIED_PRODUCTION_WORKFLOW_V1_IMPLEMENTATION_AND_NC_FAMILY_COMPILER_FREEZE`

Required next actions:

1. implement the V1 common stage/interface contract;
2. freeze numerical source-value/source-tangent fidelity thresholds project/family-wide, not from a specimen error;
3. freeze the NC family compiler/domain under that source-only convergence rule;
4. rerun Z0-Z6 through the same NC compiler + common D15/root/tangent backend;
5. then run NC+rebar through the same NC material compiler;
6. freeze the UHPC multidimensional source current operator;
7. compile UHPC through the same V1 interface and run UHPC+rebar/UHPC+shell.

## Current key artifacts

- `semantic_v2/10_governance/20260816_1217__NZSCCM__UNIFIED_PRODUCTION_WORKFLOW_COMMON_INVARIANTS_AND_TYPE_ADAPTERS__LOCK.md`
- `semantic_v2/20_theory/20260816_1217__NZSCCM__UNIFIED_PRODUCTION_WORKFLOW_V1__THEORY_AND_EXECUTION_CONTRACT.md`
- `semantic_v2/40_execution/common/20260816_1217__NZSCCM__UNIFIED_WORKFLOW_V1__INTERMEDIATE_STATE_SCHEMA_AND_CURRENT_BASELINE.json`
- `semantic_v2/60_validation/common/20260816_1217__NZSCCM__UNIFIED_WORKFLOW_V1__COMMON_VS_TYPE_SPECIFIC_MATRIX__AUDIT.md`
- `semantic_v2/00_index/20260816_1217__NZSCCM__PROJECT__CURRENT_STATE_UNIFIED_PRODUCTION_WORKFLOW_V1__SEMANTIC_INDEX.md`
- `semantic_v2/60_validation/steel_shell/20260816_1205__NZSCCM__Z6_VS_Z0_Z5_CALCULABILITY_AND_COMPILER_CONSISTENCY__AUDIT.md`
