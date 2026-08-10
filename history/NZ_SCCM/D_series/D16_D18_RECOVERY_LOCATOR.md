# D16–D18 Recovery Locator and Role Ledger

**Purpose:** preserve what D16, D17 and D18 actually established, where the original artifacts are, and what they did **not** authorize. This file is a recovery aid; where it conflicts with an original report/code artifact, the original artifact wins.

## Source locators

### D16
- Original report: `NZ_SCCM_UHPC_FSAM_v0.1_D16_完整状态来源与方程门禁报告.md`
- File Library ID: `file_000000003c588230b6557f5355bac9a9`
- Complete-text archive in this repo: `history/D_series/D16/NZ_SCCM_UHPC_FSAM_v0.1_D16_完整状态来源与方程门禁报告.md`
- Raw reconstructed dialogue sources:
  - `00_按时间重建的完整对话正文.txt` — `file_000000006e10820686cb6f86d20c7569`
  - `00_按时间重建的完整对话正文_R02.md` — `file_000000000ec88206a74063658767b20b`
  - TURN 0001–0148 original shared dialogue — `file_00000000b7788209a161cd5ec2db852a`

### D17
- Original report: `NZ_SCCM_ANALYTICAL_MATRIX_v0.2_D17_REPORT.md`
- File Library ID: `file_000000007d1081fd84f4ce14c9de8db8`
- Complete-text archive in this repo: `history/D_series/D17/NZ_SCCM_ANALYTICAL_MATRIX_v0.2_D17_REPORT.md`
- Deliverable ZIP SHA source: `NZ_SCCM_ANALYTICAL_MATRIX_v0.2_D17_DELIVERABLE.zip.sha256`
- File Library ID: `file_00000000da9881f8ae446cc5d6f9c53d`
- ZIP SHA-256: `0e0226f8b7cadc0117dc8ea13b023d001c60bcaf533981f0a568fe38abbc2e71`

### D18
- Deliverable ZIP hash file: `NZ_SCCM_ANALYTICAL_MATRIX_v0.3_D18_DELIVERABLE.zip.sha256`
- File Library ID: `file_00000000931481fb93c28dd40397e473`
- ZIP SHA-256: `cc0c33a42aaa32da1fe0960903219433e91a605dc2704a3475e8c103a1beb391`
- Core source: `inplane_algebraic_state_front.py`
- File Library ID: `file_000000005b588208afa008801f236b78`
- Complete-text recovery mirror in this repo: `history/D_series/D18/inplane_algebraic_state_front.py`
- Event-system source: `branch_event_system.py`
- File Library ID: `file_0000000073a4820b8a21860085f6cad1`
- `branch_event_system.py` is **not yet claimed byte-exact or complete-text migrated** because the File Library viewer truncates the long file. Keep the locator rather than store a truncated pseudo-original.

## D16 role

D16 was a **source registration + explicit-equation + analytic-integrability gate**, not an authorization to calculate UHPC plate capacity with an allegedly complete constitutive operator.

Its historical result was:

```text
D16_NSC_BOTTOM_LOGIC                     = PASS
D16_UHPC_LAYER0                          = ABOLISHED
D16_UHPC_FULL_STATE_FAMILY               = ESTABLISHED
D16_WW_FAILURE_SURFACE                   = PASS
D16_DP_INDEPENDENT_CHECK                 = PASS
D16_AXISYMMETRIC_TRIAXIAL_CURVE          = PASS
D16_TC_COMPLETE_FORMULA                  = OPEN
D16_TT_COMPLETE_FORMULA                  = OPEN
D16_TCX_COMPLETE_FORMULA                 = OPEN
D16_TRUE_TRIAXIAL_CONSISTENT_TANGENT     = OPEN
D16_FULL_UHPC_ANALYTICAL_MATRIX          = NOT YET AUTHORIZED
```

The state family was `U, TC, TT, CC, TCX, C3`. This was a source/provenance framework, not proof that each state had a complete stress update/history/tangent.

## D17 role

D17 eliminated **through-thickness material-point discretization for principal-strain threshold locations**. At fixed `(X,Y)`, with strain tensor affine in thickness `z`, a principal-strain threshold is obtained from:

```text
c2*z^2 + c1*z + c0 = 0
```

The original report records:

```text
D17 exact thickness-front tests: PASS (755 random roots + fixtures)
```

But it also records:

```text
D17_IN_PLANE_MOVING_STATE_DOMAIN = OPEN
D17_FULL_PANEL_PRODUCTION         = NOT AUTHORIZED
```

Thus “755 roots PASS” means the thickness-front implementation was checked; it does not mean the full plate material operator or ultimate-capacity path was solved.

## D18 role

D18 moved the **in-plane** principal-threshold front into algebraic variables:

```text
u = sin^2(X)
v = sin^2(Y)
```

At fixed `u`, the squared algebraic threshold equation is represented as a cubic in `v`. The source code preserves both:

- the unsquared physical equation, used to reject spurious roots introduced by squaring;
- the polynomial/cubic representation, used to obtain algebraic front roots.

The later event system records that topology events are roots of boundary polynomials, cubic leading coefficient, cubic discriminant and the `P0=P1` resultant; it explicitly states that **no u-grid is used to locate topology events**.

However, the event-system file also contains an adaptive one-dimensional audit evaluator. Therefore:

```text
D18_ALGEBRAIC_FRONT = RETAINED_HISTORICAL_TOOL
D18_NO_U_GRID_EVENT_LOCATION = SUPPORTED_BY_SOURCE
D18_AUDIT_QUAD_PRESENT = YES
D18_FULL_ZERO_QUADRATURE_PRODUCTION = NOT IMPLIED
```

This distinction prevents later recovery from turning an audit implementation into a formal zero-quadrature operator.

## D16 → D17 → D18 → D19 logical chain

```text
D16: what material states/equations are actually sourced?
  -> D17: where do principal-threshold state changes occur through thickness?
  -> D18: how can those fronts be represented algebraically in-plane?
  -> D19: where do algebraic branches enter/exit/merge/split, and how are moving-front derivatives handled?
```

Historical recovery sources summarize the roles as:

- D17: fixed plate position -> threshold in thickness from a quadratic equation;
- D18: `u=sin^2X, v=sin^2Y` -> algebraic in-plane front; fixed `u` gives a cubic in `v`;
- D19: entry/exit/merge/split/spurious-root/front-derivative handling.

## Non-equivalence rule

The following implication is prohibited:

```text
D17/D18/D19 state-front machinery closed
=> complete NC/UHPC material operator closed
```

It is false. State-domain geometry and material-state constitutive closure are separate layers. D16 itself left TC/TT/TCX and true-triaxial consistent tangent OPEN.

## Current historical identity

```text
D16 = RETAINED_AS_SOURCE_AND_INTEGRABILITY_AUDIT
D17 = RETAINED_AS_EXACT_THICKNESS_FRONT_TOOL
D18 = RETAINED_AS_ALGEBRAIC_INPLANE_FRONT_TOOL
D19 = RETAINED_AS_STATE_FRONT_EVENT/DERIVATIVE_AUDIT

NONE_OF_THE_ABOVE = CURRENT_MATERIAL_OPERATOR_BY_ITSELF
```
