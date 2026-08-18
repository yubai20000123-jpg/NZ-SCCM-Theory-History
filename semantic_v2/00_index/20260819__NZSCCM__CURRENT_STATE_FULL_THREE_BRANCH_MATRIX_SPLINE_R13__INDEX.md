# NZ-SCCM CURRENT STATE — FULL THREE-BRANCH MATRIX-SPLINE CONSTRUCTOR R13

**Date:** 2026-08-19  
**Status:** `R13_CASE21_ZERO_DISCRETE_TRIAL_CALC_COMPLETE`

## Governing constructor

`semantic_v2/20_theory/20260819__NZSCCM__CASE21__FULL_THREE_BRANCH_MATRIX_SPLINE_GKZ_CONSTRUCTOR__R13.md`

## What is now closed

The former true-infinite Chebyshev/material-prefix production layer is removed and is not replaced by another custom infinite series.

The complete three-branch R10 tension law is represented by one exact finite truncated-power spline and its spectral matrix lift:

```text
finite R10 projector t,c
-> r=t/xcr
-> exact matrix positive parts <r-I>+ and <r-10I>+
-> one global C2 three-branch matrix spline u_R(r)
-> finite CH circuit
-> finite master relative/incomplete-GKZ A*
```

No material-state spatial partition is used.

## Complete machine structure

```text
relations             = 112
monomial variables    = 115
Cayley A* rows         = 227
Cayley A* columns      = 403
max relation monomials= 13
```

Metadata:

`semantic_v2/40_execution/combined/20260819__NZSCCM__CASE21__R13__FULL_THREE_BRANCH_SPLINE_GKZ_METADATA.json`

## First real-specimen execution

`semantic_v2/40_execution/combined/20260819__NZSCCM__CASE21__R13_ZERO_DISCRETE_TRIAL_CALC_UNBUCKLED_BRANCH.md`

The real Case21 specimen has been executed on the exact continuous unbuckled branch `q=0, alpha=0` with the R13 finite constructor and no discretization.

```text
D* = 1.0837948701065467
Pc = 498.272412466126 kN
Ps = 40.0010858130713 kN
P*(unbuckled stationary) = 538.273498279198 kN
Pcr(exact Navier reference) = 407.136279059126 kN
```

This is an execution test of the material-series replacement, not the final nonuniform plate Pu.

## Same-source tangent

The scalar global spline is C2. The tangent is generated from the same spline derivative/divided-difference matrix function. No finite-difference tangent or separate stiffness fit is permitted.

## Mandatory governance

`semantic_v2/10_governance/20260819_0142__NZSCCM__PROJECT__ZERO_DISCRETIZATION_AND_GITHUB_CONTINUITY__LOCKED_GOVERNANCE.md`

```text
ZERO_DISCRETIZATION_DEFAULT = LOCKED
DISCRETE_AUDIT_ORACLE = PROHIBITED
FINITE_PREFIX_CONVERGENCE_AS_EVIDENCE = PROHIBITED
AUTO_GITHUB_CHECKPOINT_AFTER_MATERIAL_CHANGE = REQUIRED
PROACTIVE_CHAT_LENGTH_CHECKPOINT = REQUIRED
```

## Formal chain after R13

```text
raw specimen
-> controlling complete representative halfwave
-> Nguyen/von-Karman continuous second-order kinematics
-> exact finite R10 current operator
-> exact global three-branch matrix-spline constructor
-> exact continuous generalized integrals represented by standard A-hypergeometric/relative-period functions
-> P,Rq,Ralpha and same-source derivatives
-> direct solve Rq=0, Ralpha=0, det(Jlim)=0
-> Pu
```

There is no material degree N and no material-series convergence gate.

## Execution discipline

Do not create a new theory gate when one exact evaluation representation is inconvenient. Cross out that representation and switch among mathematically equivalent mature representations of the same fixed function object. A representation-specific failure is not promoted into a new project gate, and no discrete fallback is allowed unless the user explicitly authorizes it for that task.

The material-series replacement itself is complete at R13; the next calculation may proceed to the full nonuniform continuous `(D,q,alpha)` target system.
