# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-19  
**Status:** `R14_CASE21_Z6_FULL_FINITE_MATERIAL_AND_COUPLED_INVARIANCE = ACTIVE`

## Canonical current-state artifact

`semantic_v2/00_index/20260819__NZSCCM__CURRENT_STATE_R14_FULL_FINITE_MATERIAL_AND_COUPLED_INVARIANCE__INDEX.md`

## Mandatory governance

`semantic_v2/10_governance/20260819_0142__NZSCCM__PROJECT__ZERO_DISCRETIZATION_AND_GITHUB_CONTINUITY__LOCKED_GOVERNANCE.md`

```text
ZERO_DISCRETIZATION_DEFAULT = LOCKED
DISCRETE_AUDIT_ORACLE = PROHIBITED
FINITE_PREFIX_CONVERGENCE_AS_EVIDENCE = PROHIBITED
TASK_LOCAL_DISCRETIZATION_EXCEPTION_ONLY = TRUE
AUTO_GITHUB_CHECKPOINT_AFTER_MATERIAL_CHANGE = REQUIRED
PROACTIVE_CHAT_LENGTH_CHECKPOINT = REQUIRED
```

## Material-series correction

R09 removes the former true-infinite Chebyshev/material-prefix production layer.

R13 replaces the full three-branch R10 concrete tension execution by one exact global truncated-power matrix spline.

R14 completes the same finite replacement for Z6 steel constituents:

```text
face radial cap:
g(r) = 2 / [1 + sqrt(r) + |sqrt(r)-1|]

web ideal EP:
sigma = (|x+fy| - |x-fy|)/2
```

These are exact global identities of the frozen finite laws, not approximations and not spatial partitions.

## Governing R14 execution

`semantic_v2/40_execution/combined/20260819__NZSCCM__CASE21_Z6__R14_FULL_FINITE_MATERIAL_AND_COUPLED_INVARIANCE_EXECUTION.md`

Because every new constituent map is pointwise identical to the old finite current map, the exact continuous generalized functions are identical:

```text
P_new      == P_old
Rq_new     == Rq_old
Ralpha_new == Ralpha_old
Jlim_new   == Jlim_old
```

Therefore the complete coupled root set is invariant. The old material series is not used as a production backend.

## Full coupled benchmark state under the finite constructors

Case21:

```text
D = 0.7887924801
q = 0.0018083572562965242
alpha = 0.002506908330448254
Pc = 337.92303037 kN
Ps = 28.844798318 kN
Pu = 366.767828685 kN
experiment = 368.312749744 kN
error = -0.419459 %
```

Z6:

```text
D = 1.36180798
q = 0.0264854039
alpha = 1.8954326279510263
Pc,eff = 22.8171044 MN
Pface = 18.5564373 MN
Pweb = 7.0325797 MN
Pu = 48.4061215 MN
Zhou error = -2.183706 %
Winter error = -3.546283 %
```

## Uniform-branch correction

The former `q=0, alpha=0` stationary calculations are retained only as diagnostics and are explicitly rejected as Pu definitions:

```text
Case21 uniform stationary = 538.273498279 kN
Z6 uniform stationary     = 90.150438116 MN
```

The high values arise because the uniform branch suppresses the nonuniform structural buckling/postbuckling mechanism. They are not evidence of bias introduced by the finite material constructors.

## Formal mainline

```text
raw specimen
-> controlling complete representative halfwave
-> continuous Nguyen/von-Karman second-order kinematics
-> finite global current material constructors
-> exact continuous P,Rq,Ralpha + same-source derivatives
-> direct solve Rq=0, Ralpha=0, det(Jlim)=0
-> Pu
```

No material degree N, finite-prefix convergence gate, spatial discretization, numerical quadrature, material point, or discrete oracle is part of the active theory.

No new theory gate is introduced by R14.
