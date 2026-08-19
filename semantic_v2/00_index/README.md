# NZ-SCCM semantic tree v2

This namespace is the **content-first, non-destructive semantic reconstruction** of the repository.

## Current operational entry

Use first:

`20260819__NZSCCM__CURRENT_STATE_R15_FULL_FROM_ZERO_CALCULATION_LEDGER__INDEX.md`

## Canonical single-file ledger

`../20_theory/20260819__NZSCCM__R15_FULL_FROM_ZERO_CALCULATION_LEDGER_CASE21_Z6.md`

R15 is the current complete from-zero calculation specification for Case21 and Z6. It consolidates:

```text
raw specimen inputs
-> Dx,Dy,H
-> physical controlling halfwave
-> continuous Nguyen/von-Karman kinematics
-> finite global current material operators
-> continuous P,Rq,Ralpha + same-source derivatives
-> direct limit system
-> Pu
```

## Current main correction

```text
former true-infinite Chebyshev/material-prefix production layer = removed
complete three-branch R10 tension = exact finite global matrix spline
Z6 face radial cap = exact finite global algebraic function
Z6 web ideal EP = exact finite global clip
Nguyen second-order kinematics and direct P/R/J limit system = unchanged
uniform q=alpha=0 stationary branch = rejected as Pu
```

## Physical halfwave correction

R15 explicitly restores the physical geometry distinction for Case21:

```text
a_phys = 2440 mm
b = 1220 mm
m_phys = 2
ell = 1220 mm
```

Historical files that write `a=b=ell=1220 mm, m*=1` are already in representative-halfwave coordinates.

## Mandatory governance

`../10_governance/20260819_0142__NZSCCM__PROJECT__ZERO_DISCRETIZATION_AND_GITHUB_CONTINUITY__LOCKED_GOVERNANCE.md`

```text
ZERO_DISCRETIZATION_DEFAULT = LOCKED
DISCRETE_AUDIT_ORACLE = PROHIBITED
FINITE_PREFIX_CONVERGENCE_AS_EVIDENCE = PROHIBITED
TASK_LOCAL_DISCRETIZATION_EXCEPTION_ONLY = TRUE
AUTO_GITHUB_CHECKPOINT_AFTER_MATERIAL_CHANGE = REQUIRED
PROACTIVE_CHAT_LENGTH_CHECKPOINT = REQUIRED
```

## Governing artifacts

R09 — material-series removal:
`../20_theory/20260819__NZSCCM__MATERIAL_SERIES_LAYER_REMOVAL_AND_MAINLINE_REBASE__R09.md`

R13 — full three-branch R10 matrix-spline constructor:
`../20_theory/20260819__NZSCCM__CASE21__FULL_THREE_BRANCH_MATRIX_SPLINE_GKZ_CONSTRUCTOR__R13.md`

R14 — finite material constructors and coupled-solution invariance:
`../40_execution/combined/20260819__NZSCCM__CASE21_Z6__R14_FULL_FINITE_MATERIAL_AND_COUPLED_INVARIANCE_EXECUTION.md`

R15 — canonical single-file from-zero calculation ledger:
`../20_theory/20260819__NZSCCM__R15_FULL_FROM_ZERO_CALCULATION_LEDGER_CASE21_Z6.md`

R10-R12 remain constructor provenance only.

## R15 evidence identity

R15 is complete as a **calculation specification**. Its sealed regression-target section contains the released Case21/Z6 roots and loads only for post-execution comparison.

Blind re-execution must provide only Sections 0–10 to the independent executor and must hide the sealed targets until after the result is frozen.

R15 does not claim that this chat has already independently recomputed the full nonuniform roots with a new CAS backend.

## Execution discipline

Do not deadlock on one exact representation and do not create representation-specific theory gates. Switch among mature mathematically equivalent exact representations when needed. A failed representation never authorizes spatial or material discretization.

## Current read order

1. this README;
2. `20260819__NZSCCM__CURRENT_STATE_R15_FULL_FROM_ZERO_CALCULATION_LEDGER__INDEX.md`;
3. R15 canonical ledger;
4. mandatory governance;
5. R09;
6. R13;
7. R14;
8. R10-R12 only for constructor provenance;
9. 20260818 locked handoff + errata for historical provenance;
10. `../../current/CURRENT_STATE.md`.

## Current status

```text
R15_FULL_FROM_ZERO_CALCULATION_LEDGER = ACTIVE
MATERIAL_TRUE_INFINITE_SERIES_LAYER = REMOVED
CASE21_MATERIAL_SERIES_REPLACEMENT = COMPLETE
Z6_MATERIAL_SERIES_REPLACEMENT = COMPLETE
SPATIAL_DISCRETIZATION = NONE
FINITE_PREFIX = NONE
DISCRETE_ORACLE = NONE
NEXT = INDEPENDENT BLIND FULL NONUNIFORM RE-EXECUTION FROM R15 SECTIONS 0-10
```
