# NZ-SCCM CURRENT STATE — R14 full finite material constructors + coupled-solution invariance

**Date:** 2026-08-19  
**Status:** `R14_CASE21_Z6_FULL_FINITE_MATERIAL_AND_COUPLED_INVARIANCE = ACTIVE`

## Governing execution

`../40_execution/combined/20260819__NZSCCM__CASE21_Z6__R14_FULL_FINITE_MATERIAL_AND_COUPLED_INVARIANCE_EXECUTION.md`

## What R14 adds

R13 had already removed the old material-series representation from the complete three-branch R10 concrete operator. R14 finishes the same job for the remaining Z6 steel constituents by exact global algebraic identities:

```text
face radial cap:
g(r) = 2 / [1 + sqrt(r) + |sqrt(r)-1|]

web ideal EP:
sigma = (|x+fy| - |x-fy|)/2
```

No elastic/plastic spatial partition, material degree N, finite prefix, numerical quadrature, grid, material point, collocation or discrete oracle is used.

## Exact invariance result

All new finite global constituent maps are pointwise identical to the frozen finite current laws they replace. Therefore

```text
P_new(D,q,alpha)      == P_old(D,q,alpha)
Rq_new(D,q,alpha)     == Rq_old(D,q,alpha)
Ralpha_new(D,q,alpha) == Ralpha_old(D,q,alpha)
Jlim_new              == Jlim_old
```

as exact continuous functionals. Hence the coupled root sets are invariant.

## Full coupled benchmark results carried by exact identity

Case21:

```text
D  = 0.7887924801
q  = 0.0018083572562965242
alpha = 0.002506908330448254
Pc = 337.92303037 kN
Ps = 28.844798318 kN
Pu = 366.767828685 kN
experiment = 368.312749744 kN
error = -0.419459 %
```

Z6:

```text
D  = 1.36180798
q  = 0.0264854039
alpha = 1.8954326279510263
Pc,eff = 22.8171044 MN
Pface  = 18.5564373 MN
Pweb   = 7.0325797 MN
Pu     = 48.4061215 MN
Zhou   = 49.4867667519 MN   error = -2.183706 %
Winter = 50.1858541295 MN   error = -3.546283 %
```

The rejected uniform-branch stationary values remain provenance only and are not Pu definitions.

## Mandatory governance

`../10_governance/20260819_0142__NZSCCM__PROJECT__ZERO_DISCRETIZATION_AND_GITHUB_CONTINUITY__LOCKED_GOVERNANCE.md`

```text
ZERO_DISCRETIZATION_DEFAULT = LOCKED
DISCRETE_AUDIT_ORACLE = PROHIBITED
FINITE_PREFIX_CONVERGENCE_AS_EVIDENCE = PROHIBITED
AUTO_GITHUB_CHECKPOINT_AFTER_MATERIAL_CHANGE = REQUIRED
PROACTIVE_CHAT_LENGTH_CHECKPOINT = REQUIRED
```

## Current material layer

```text
Case21 concrete          -> R13 global finite matrix spline
Case21 reinforcement     -> existing finite closed form
Z6 concrete              -> R13 global finite matrix spline
Z6 face steel radial cap -> R14 global finite algebraic cap
Z6 web/PBL ideal EP      -> R14 global finite algebraic clip
```

## Current mainline

```text
raw specimen
-> controlling complete representative halfwave
-> Nguyen continuous second-order kinematics
-> finite global current material constructors
-> exact continuous P,Rq,Ralpha and same-source derivatives
-> direct solve Rq=0, Ralpha=0, det(Jlim)=0
-> Pu
```

No new theory gate is introduced by R14.
