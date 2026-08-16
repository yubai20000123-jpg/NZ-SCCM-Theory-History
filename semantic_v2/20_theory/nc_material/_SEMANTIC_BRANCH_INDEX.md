# NC material semantic branch

## Current material target

- R10 physical current material target remains **CURRENT_SUPPORT / FROZEN**.
- R10 material physics is not reopened.
- Governing project workflow is `UNIFIED_PRODUCTION_WORKFLOW_V1`.

## 12:29 NC source-fidelity result — PASS

Current source-fidelity support:

- `../../40_execution/common/20260816_1229__NZSCCM__NC_FAMILY_COMPILER_FREEZE__EXECUTION_REPORT.md`
- `../../40_execution/common/20260816_1229__NZSCCM__NC_FAMILY_COMPILER_FREEZE__PARAMS_AND_INTERMEDIATES.json`
- `../../40_execution/common/20260816_1229__NZSCCM__NC_FAMILY_COMPILER_FREEZE__REPRO.py`

Material-only result:

```text
source operator = R10
operational core = [-2.35,+1.90]
coefficient guard = [-2.60,+2.15]
channels = U,C,T,T7
single global Chebyshev polynomial per channel
same order for all four channels
M = 8*(N+1)
exact C1 at lambda=0
E_sigma <= .005
E_tangent <= .05
E_divided_difference <= .05
N_source_candidate = 3584
```

Reference errors:

```text
E_sigma = .00107218
E_tangent = .04066517
E_divided_difference = .00381386
```

The same source-only order/core/guard/algorithm passes the audited NC kappa extrema.

## 12:48 production-promotion correction

The 12:48 structural gate establishes that `N=3584` is a **source-fidelity candidate order**, not yet a fully frozen production NC family compiler.

Current governance:

- `../../10_governance/20260816_1248__NZSCCM__N3584_CH_D15_BACKEND_TRACTABILITY_GATE__LOCK.md`

Execution / validation:

- `../../40_execution/common/20260816_1248__NZSCCM__N3584_CH_D15_BACKEND_AND_Z0_Z6_RERUN__EXECUTION_REPORT.md`
- `../../40_execution/common/20260816_1248__NZSCCM__N3584_CH_D15_BACKEND__PARAMS_AND_INTERMEDIATES.json`
- `../../40_execution/common/20260816_1248__NZSCCM__N3584_CH_CLENSHAW_D15_BACKEND__REPRO.py`
- `../../60_validation/common/20260816_1248__NZSCCM__N3584_CH_D15_COMMON_BACKEND_TRACTABILITY__AUDIT.md`

An order-agnostic backward Chebyshev/Cayley-Hamilton Clenshaw pair was derived and verified against the historical forward N48 CH recurrence at roundoff scale:

```text
ORDER_AGNOSTIC_CH_CLENSHAW_IDENTITY = PASS
```

However the current high-order coefficient-tensor realization fails the family-level structural tractability requirement at the wide-spectrum Z6 state. Simple coefficient-threshold pruning is also not production-certified because generalized residual convergence is non-monotone under support changes.

Therefore:

```text
NC_N3584_SOURCE_FIDELITY = PASS
NC_N3584_FULL_PRODUCTION_COMPILER_PROMOTION = WITHHELD
CURRENT_N3584_COEFFICIENT_TENSOR_BACKEND = FAIL_COMMON_TRACTABILITY
```

## Meaning of “same NC method”

All NC specimens must share the same family-level material representation/convergence policy and the same downstream kinematics, CH/approved matrix lift, General-D15, `P,Rq,L`, and same-state `KZ` logic.

A source parameter may change coefficient values physically, but a case ID may not select a different representation, order, interval, or fallback structural solver.

```text
NC+REBAR -> SAME_NC_FAMILY_METHOD
NC+SHELL -> SAME_NC_FAMILY_METHOD
Z0-Z6    -> SAME_NC_FAMILY_METHOD
```

## Common mechanics inherited by every NC specimen

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
NGUYEN_SECOND_ORDER
MEMBRANE_STRESS_REDISTRIBUTION
CURRENT_STRESS + CONSISTENT_CURRENT_TANGENT
CAYLEY_HAMILTON / APPROVED FINITE MATRIX LIFT
MOMENT_FIRST_GENERAL_D15
ZERO_FORMAL_SPATIAL_AND_THICKNESS_QUADRATURE
COMMON_P_Rq_L_CONNECTED_BRANCH_LIMIT
SAME_STATE_MATERIAL_PLUS_GEOMETRIC_KZ
```

## Current numerical result boundary

```text
Z6 51.30 MN = RETAINED ENGINEERING BASELINE ONLY
Z0-Z5 10:43 Pu = RETRACTED
Z0-Z5 12:48 N3584 values = DIAGNOSTIC LOCATORS ONLY
NEW Z0-Z6 PRODUCTION Pu = NOT RELEASED
```

The 12:48 diagnostic locators remaining near several old load neighborhoods means the old discrepancy is not yet explained solely by the old N48 source error. This is a diagnosis to be resolved only after a common production backend reaches converged `Rq`, same-expression `L`, and same-state `KZ`.

## Current next gate

`UNIFIED_V1_NC_COMPILER_STRUCTURAL_TRACTABILITY_REDESIGN_GATE`

The next gate must retain R10 and all project-wide mechanics while redesigning the **family-level finite analytic representation and/or exact coefficient contraction architecture** so one source-controlled method is tractable across Z0-Z6.

Allowed directions include universal factorized/low-rank analytic representations or another finite analytic material-family representation with explicit source stress/tangent error and General-D15-compatible contraction.

Prohibited:

```text
case-specific compiler/order/domain
Z6-only fallback solver
spatial numerical quadrature/collocation/material points
experiment/Zhou/Winter-driven representation choice
disabling membrane redistribution in stocky cases
```
