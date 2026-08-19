# NZ-SCCM semantic tree v2

This namespace is the **content-first, non-destructive semantic reconstruction** of the repository.

## Current operational entry

Use first:

`20260819__NZSCCM__CURRENT_STATE_R14_FULL_FINITE_MATERIAL_AND_COUPLED_INVARIANCE__INDEX.md`

## Current main correction

```text
remove the former true-infinite Chebyshev/material-prefix production layer
restore the exact finite current material operators as the formal objects
replace complete three-branch R10 tension by one exact global matrix spline
replace Z6 face radial-cap and web ideal-EP series representations by exact global algebraic forms
keep Nguyen second-order kinematics and the direct P/R/J limit system unchanged
```

## Current material constructors

```text
Case21 concrete          -> R13 global finite matrix spline
Case21 reinforcement     -> existing finite closed form
Z6 concrete              -> R13 global finite matrix spline
Z6 face steel radial cap -> R14 g(r)=2/[1+sqrt(r)+|sqrt(r)-1|]
Z6 web/PBL ideal EP      -> R14 sigma=(|x+fy|-|x-fy|)/2
```

All are exact identities of the frozen finite current laws.

## Current main chain

```text
raw specimen
-> controlling complete representative halfwave
-> continuous Nguyen/von-Karman second-order kinematics
-> finite global current material constructors
-> exact continuous P,Rq,Ralpha + same-source derivatives
-> direct solve Rq=0, Ralpha=0, det(J_lim)=0
-> Pu
```

No production material degree N or finite-prefix convergence gate exists.

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

R14 — Case21 + Z6 full finite material constructors and exact coupled-solution invariance:
`../40_execution/combined/20260819__NZSCCM__CASE21_Z6__R14_FULL_FINITE_MATERIAL_AND_COUPLED_INVARIANCE_EXECUTION.md`

R10-R12 remain constructor provenance only.

## Exact coupled invariance result

Because the new finite constructors are pointwise identical to the frozen finite current laws,

```text
P_new      == P_old
Rq_new     == Rq_old
Ralpha_new == Ralpha_old
Jlim_new   == Jlim_old
```

as exact continuous functionals. Hence the complete coupled root sets are unchanged without using the old material series as a production backend.

Current benchmark values carried by this exact identity:

```text
Case21 Pu = 366.767828685 kN, error vs experiment = -0.419459 %
Z6 Pu     = 48.4061215 MN, error vs Zhou = -2.183706 %, vs Winter = -3.546283 %
```

The earlier uniform `q=alpha=0` stationary values are diagnostics only and are not Pu definitions.

## Execution discipline

Do not deadlock on one exact representation and do not turn representation-specific inconvenience into a theory gate. Switch among mathematically equivalent mature exact representations when needed. A failed representation does not authorize discretization.

## Current read order

1. this README;
2. `20260819__NZSCCM__CURRENT_STATE_R14_FULL_FINITE_MATERIAL_AND_COUPLED_INVARIANCE__INDEX.md`;
3. mandatory governance;
4. R09;
5. R13;
6. R14;
7. R10-R12 only for constructor provenance;
8. 20260818 locked handoff + R01 errata for unchanged surrounding theory;
9. `../../current/CURRENT_STATE.md`.

## Current status

```text
MATERIAL_TRUE_INFINITE_SERIES_LAYER = REMOVED
CASE21_MATERIAL_SERIES_REPLACEMENT = COMPLETE
Z6_MATERIAL_SERIES_REPLACEMENT = COMPLETE
FULL_COUPLED_FUNCTIONAL_IDENTITY = EXACT
CASE21_COUPLED_ROOT_INVARIANCE = PASS
Z6_COUPLED_ROOT_INVARIANCE = PASS
SPATIAL_DISCRETIZATION = NONE
FINITE_PREFIX = NONE
DISCRETE_ORACLE = NONE
```
