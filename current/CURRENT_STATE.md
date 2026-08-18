# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-19  
**Status:** `R13_CASE21_ZERO_DISCRETE_TRIAL_CALC_COMPLETE = ACTIVE`

## Canonical current-state artifact

`semantic_v2/00_index/20260819__NZSCCM__CURRENT_STATE_FULL_THREE_BRANCH_MATRIX_SPLINE_R13__INDEX.md`

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

## Governing material-series correction

`semantic_v2/20_theory/20260819__NZSCCM__MATERIAL_SERIES_LAYER_REMOVAL_AND_MAINLINE_REBASE__R09.md`

The former true-infinite Chebyshev/material-prefix production layer remains removed.

## Complete replacement constructor

`semantic_v2/20_theory/20260819__NZSCCM__CASE21__FULL_THREE_BRANCH_MATRIX_SPLINE_GKZ_CONSTRUCTOR__R13.md`

R13 replaces the entire three-branch R10 tension piecewise execution by one exact global truncated-power spline and its spectral matrix lift.

```text
GLOBAL_THREE_BRANCH_MATRIX_SPLINE = PASS
FULL_THREE_BRANCH_SPARSE_CH_CIRCUIT = PASS
FULL_THREE_BRANCH_MASTER_ASTAR = PASS
MATERIAL_SERIES_REPLACEMENT = COMPLETE
```

Exact sparse master structure:

```text
relations = 112
variables = 115
A* rows   = 227
A* columns= 403
max monomials/relation = 13
```

## Case21 zero-discretization trial calculation

`semantic_v2/40_execution/combined/20260819__NZSCCM__CASE21__R13_ZERO_DISCRETE_TRIAL_CALC_UNBUCKLED_BRANCH.md`

The trial uses the real Case21 specimen on the exact continuous unbuckled branch `q=0, alpha=0`. The field is uniform, so the full specimen concrete integral reduces analytically to area times the exact finite R10 stress; no spatial quadrature or discrete oracle is involved.

```text
D* = 1.0837948701065467
Pc(D*) = 498.272412466126 kN
Ps(D*) = 40.0010858130713 kN
P*(unbuckled stationary) = 538.273498279198 kN
Pcr(exact Navier halfwave reference) = 407.136279059126 kN
```

The reinforcement remains elastic at the stationary point. This calculation validates actual execution of the finite R13 constructor on a real specimen branch. It does **not** claim the final nonlinear plate Pu; that requires the full nonuniform `(D,q,alpha)` continuous system.

## Same-source tangent

The global spline is C2 and its tangent is generated from the same scalar function by exact derivative/divided-difference spectral calculus. No finite-difference tangent, fitted tangent, or independent stiffness surrogate is introduced.

## Formal chain

```text
raw specimen
-> controlling complete representative halfwave
-> continuous Nguyen/von-Karman second-order kinematics
-> exact finite R10 current operator
-> exact global three-branch matrix-spline constructor
-> exact continuous generalized integrals in standard A-hypergeometric/relative-period representation
-> P,Rq,Ralpha + same-source derivatives
-> direct solve Rq=0, Ralpha=0, det(Jlim)=0
-> Pu
```

There is no production material degree N and no material-series convergence gate.

## Execution rule after R13

If one exact evaluation representation becomes inconvenient, cross out that representation and switch to another mature equivalent representation of the same fixed mathematical object. Do not promote representation-specific difficulty into a new theory gate and do not fall back to discretization.
