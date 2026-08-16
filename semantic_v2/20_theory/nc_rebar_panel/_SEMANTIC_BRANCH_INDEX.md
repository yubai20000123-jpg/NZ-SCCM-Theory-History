# NC + rebar panel theory semantic branch

## Current production-development identity

The current mainline is the compact exact R10 target route, not the retracted Case21 N48 five-free-coordinate membrane Pu path.

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
 -> Nguyen second-order continuous strain
 -> compatible membrane-stress redistribution
 -> same-state R10 concrete + reinforcement
 -> regular source/matrix material DAG
 -> global fixed-endpoint compact thickness period
 -> finite beta/XY target contraction
 -> low-dimensional connected structural solve
```

Formal structural spatial/thickness numerical quadrature remains zero.

## Formal-series rule

```text
FORMAL_INFINITE_OR_HIGH_ORDER_SERIES = ALLOWED_AS_REPRESENTATION
TERM_EXPANSION_FOR_THEORY_AUDIT = ALLOWED
DIRECT_THOUSANDS_OF_COEFFICIENTS_PRODUCTION = PROHIBITED
```

## Source regularity

The old rationalized `c0,c1` connection pole at `x=21/260` is a representation artifact. The source matrix square root is regular there, so production differentiation stays at matrix/source level through Fréchet/Sylvester rules. True Foster source knots remain physical material events.

## Algebraic state identities

```text
64_STATE = global branch-free algebraic closure bound
8_STATE  = exact branch-aware full-R10 stress bound on fixed event topology
```

The branchwise 8-state field remains retained for local exact/audit use.

## Actual P/Rm interface closure

The six concrete structural targets

```text
P_c + five Rm,c
```

share only three common thickness resultants:

```text
Nx0  = int sigma_x dzeta
Ny0  = int sigma_y dzeta
Nxy0 = int tau_xy dzeta
```

with fixed physical endpoints `zeta=-1,+1`.

All five `Rm` are finite trigonometric combinations of these three resultants, and `P_c` uses `Ny0`.

Therefore:

```text
P_PLUS_FIVE_RM_COMMON_THICKNESS_RESULTANTS = 3
```

The downstream full state evaluator also needs only the finite thickness-moment family

```text
stress: k=0,1
tangent target kernels: k=0,1,2
```

rather than an unbounded moment ladder.

## Thickness-to-XY representation decision

The event-resolved `<=8`-state form is locally smaller but its source-knot roots

```text
zeta_m(X,Y)
```

change existence/order over the complete halfwave.

For generic five-coordinate kinematics:

```text
deg_zeta event equation = 2
XY trig degree of a2,a1,a0 = 4,6,8
XY trig degree of event discriminant = 12
XY trig degree of endpoint event front = 8
```

A Case21 audit confirms both `no-event` and `one lambda1 event` regions occur within the same `(X,Y)` domain.

Thus global event resolution would require either in-plane region subdivision or clipped-root/positive-part selectors. The former conflicts with the single-domain formal architecture; the latter reconstructs the branch-free source structure.

Current production choice is therefore locked as

```text
GLOBAL_FIXED_ENDPOINT_POSITIVE_PART_FACTORISED_PERIOD = PRODUCTION
EVENT_RESOLVED_8_STATE = LOCAL_EXACT/AUDIT ONLY
```

Conceptual fixed bound for the actual zero-order three-resultant package is

```text
<=64 common branch-free field states + 3 target accumulators = <=67
```

without requiring materialization/canonicalization of 67 giant rational functions.

## Z6 boundary

```text
Z6_BOUNDARY = FOUR_EDGE_SIMPLY_SUPPORTED / SSSS
```

Any older mixed-boundary branch text is superseded.

## Capacity status

```text
Case21 320.749185 kN = RETRACTED DIAGNOSTIC ONLY
Z6 43.762840 MN = RETRACTED DIAGNOSTIC ONLY
Case21 retained support baseline = 368.189 kN
Z6 retained engineering support baseline = 51.30 MN
NEW_CORRECTED_MEMBRANE_REDISTRIBUTED_Pu = NOT RELEASED
```

## Current next task

`GLOBAL_FIXED_ENDPOINT_THREE_STRESS_MOMENT_DESCRIPTOR_GATE`

Construct the actual compact analytic operator

```text
(D,q,r;X,Y) -> [Nx0,Ny0,Nxy0]
```

from the source-regular factorized R10 DAG, with no numerical thickness quadrature and no explicit high-order coefficient enumeration. The same operator must carry same-source derivatives needed by P/Rm and remain extensible to the already bounded k=1 stress / k<=2 tangent moment family.

After that passes, perform exact `(X,Y)` contraction to obtain actual `P_c` and all five `Rm,c`.

## Current artifacts

- `../../40_execution/common/20260817_0100__NZSCCM__SOURCE_LEVEL_REGULARIZATION_AND_REAL_TARGET_PREFLIGHT__EXECUTION_REPORT.md`
- `../../40_execution/common/20260817_0115__NZSCCM__FULL_SYY_BRANCH_AWARE_8_STATE_REDUCTION__EXECUTION_REPORT.md`
- `../../40_execution/common/20260817_0143__NZSCCM__ACTUAL_P_RM_THICKNESS_TO_XY_INTERFACE_COMPACTNESS__EXECUTION_REPORT.md`
- `../../40_execution/common/20260817_0143__NZSCCM__ACTUAL_P_RM_THICKNESS_TO_XY_INTERFACE_COMPACTNESS__PARAMS_AND_INTERMEDIATES.json`
- `../../40_execution/common/20260817_0143__NZSCCM__ACTUAL_P_RM_THICKNESS_TO_XY_INTERFACE_COMPACTNESS__REPRO.py`
- `../../10_governance/20260817_0143__NZSCCM__GLOBAL_FIXED_ENDPOINT_P_RM_INTERFACE__LOCK.md`
