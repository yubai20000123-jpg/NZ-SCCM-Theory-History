# NC material semantic branch

## Current material target

- R10 physical current material target remains **CURRENT_SUPPORT / FROZEN**.
- R10 material physics is not reopened.
- Governing project workflow is `UNIFIED_PRODUCTION_WORKFLOW_V1`.

## NC family compiler source freeze — PASS

Current governance:

- `../10_governance/20260816_1229__NZSCCM__NC_FAMILY_COMPILER_SOURCE_FIDELITY_AND_ORDER_FREEZE__LOCK.md`

Current source-fidelity execution:

- `../../40_execution/common/20260816_1229__NZSCCM__NC_FAMILY_COMPILER_FREEZE__EXECUTION_REPORT.md`
- `../../40_execution/common/20260816_1229__NZSCCM__NC_FAMILY_COMPILER_FREEZE__PARAMS_AND_INTERMEDIATES.json`
- `../../40_execution/common/20260816_1229__NZSCCM__NC_FAMILY_COMPILER_FREEZE__REPRO.py`

Frozen current NC compiler contract:

```text
source operator = R10
operational core = [-2.35,+1.90]
coefficient guard = [-2.60,+2.15]
channels = U,C,T,T7
single global Chebyshev polynomial per channel
same order for all four channels
M = 8*(N+1)
exact C1 at lambda=0
E_sigma <= 0.005
E_tangent <= 0.05
E_divided_difference <= 0.05
N_NC = 3584
```

The order is the first passing candidate from the deterministic V1 ladder. It is not selected from any case `Pu`, experiment or Zhou/Winter comparison.

Reference R10 assembled-current errors at `N=3584`:

```text
E_sigma = 0.00107218
E_tangent = 0.04066517
E_divided_difference = 0.00381386
```

The same order/core/guard/algorithm passes the current Swartz `kappa` extrema `1.9993148515` and `2.0008935611`.

## Meaning of “same NC compiler”

All NC specimens use the same **compiler protocol, core/guard policy, source-fidelity contract, frozen family order and downstream CH/D15/root architecture**.

Actual coefficient values may vary with physical R10 material parameters such as `kappa`, because the source operator itself varies with those parameters. That is a parameterized family compiler, not a specimen-specific method.

```text
NC+REBAR -> SAME_NC_FAMILY_COMPILER_PROTOCOL / ORDER / DOMAIN POLICY
NC+SHELL -> SAME_NC_FAMILY_COMPILER_PROTOCOL / ORDER / DOMAIN POLICY
```

If a future NC source parameter or admissible principal spectrum exits the frozen envelope, the NC family is audited/recompiled consistently; a one-off case order is prohibited.

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

## Retained historical diagnostics

- 10:54: the old Z6-wide N48 coefficient set has order-one T/T7 error in the Z0-Z5 occupied range.
- 11:34: one global degree-48 C1 polynomial per primitive cannot satisfy the broad NC source fidelity need.
- 11:10 multirate high-order result remains diagnostic only; its ad hoc different channel orders are not the current family compiler.

## Current next gate

`UNIFIED_V1_N3584_CH_MOMENT_FIRST_D15_BACKEND_AND_Z0_Z6_RERUN_GATE`

The next step is to implement the frozen high-order family compiler through an order-agnostic/factorized Cayley-Hamilton and moment-first General-D15 backend, then rerun Z0-Z6 under the same workflow. No further specimen-specific compiler redesign is authorized.
