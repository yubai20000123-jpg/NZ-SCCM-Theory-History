# NC material semantic branch

## Current material target

- R10 physical current material target remains **CURRENT_SUPPORT / FROZEN**.
- R10 material physics is not reopened.
- Material compiler order is locked at **48 for every primitive** by explicit user instruction.

Current hard order identity:

```text
MATERIAL_COMPILER_ORDER = 48
U_ORDER  = 48
C_ORDER  = 48
T_ORDER  = 48
T7_ORDER = 48
```

No future order change is permitted without explicit user authorization.

## Historical order escalation — not current

The 11:10 multirate candidate

`R10-MR-C1(256,1024,1280,512)`

is **RETRACTED_FROM_CURRENT_PRODUCTION / HISTORICAL_DIAGNOSTIC_ONLY**.

It does not define the current compiler.

## 2026-08-16 11:34 fixed-N48 representation-capacity result

Current governance / theory:

- `../10_governance/20260816_1134__NZSCCM__Z0_Z5_FIXED_N48_FIDELITY_REBUILD__LOCK.md`
- `20260816_1134__NZSCCM__NC_MATERIAL__FIXED_N48_REPRESENTATION_CAPACITY__THEORY.md`

The 10:54 finding that the old Z6-wide N48 coefficient set is invalid remains active. The 11:34 gate then tested whether that defect can be repaired **only by regenerating coefficients inside one global degree-48 Chebyshev polynomial per primitive**.

For each conservative Z0–Z5 source interval, a source-only degree-48 constrained minimax problem with exact R10 C1 anchors was solved.

Best found T maximum value errors remain approximately:

```text
Z0 .19812
Z1 .12199
Z2 .25816
Z3 .13381
Z4 .17144
Z5 .10580
```

Even on the challenged occupied ranges with no conservative margin, T errors remain about `.0655–.1968`.

The unchanged R10 current-master stress error after separate value-minimax fitting remains approximately `.116–.285`; keeping U/C/T7 exact and replacing only T still leaves `.106–.257` error.

Therefore:

```text
FIXED_N48_ORDER = ACTIVE / RETAINED
SINGLE_GLOBAL_N48_COEFFICIENT_ONLY_REPAIR = FAIL_REPRESENTATION_CAPACITY
R10_PHYSICAL_OPERATOR = FROZEN
OLD_Z6_WIDE_N48_Z0_Z5_COEFFICIENT_SET = INVALID
NEW_Z0_Z5_Pu = NOT_CALCULATED
```

The failure is not coefficient blow-up: C1 anchors remain at roundoff and coefficient magnitudes remain O(1). The controlling issue is the narrow small-positive R10 tensile transition relative to the broad compression-to-tension material interval.

## Current required repair space

The next gate is strictly:

`Z0_Z5_AR2_FIXED_N48_MULTISCALE_ANALYTIC_REPRESENTATION_GATE`

It must retain:

```text
fixed order ceiling = 48
unchanged R10 source law
source-only representation design
exact C1 behavior
Cayley-Hamilton compatibility
moment-first General-D15 compatibility
zero structural spatial integration
no experiment / Zhou / Winter / desired Pu in representation design
```

A weighting, node-density or least-squares change inside the same single-global N48 polynomial form is no longer sufficient evidence of a repair.

## Historical compiler-fidelity support

- `20260813_1719__NZSCCM__NC_MATERIAL__VALUE_TANGENT_BALANCED_MINIMAX_AND_REACHABLE_SPECTRUM__COMPILER_AUDIT.md`
- `20260812_TUNK__NZSCCM__NC_MATERIAL__N48C1_T_CONSTRAINED_MINIMAX__GOVERNANCE.md`
- `20260812_TUNK__NZSCCM__NC_MATERIAL__T_CONSTRAINED_MINIMAX_BOUNDARY_LAYER__AUDIT.md`

These remain useful evidence about fixed-N48 source fidelity and value/tangent trade-offs, but they do not authorize a change of order.
