# NZ-SCCM CURRENT STATE — GLOBAL RESIDUE / GKZ R11

**Date:** 2026-08-19  
**Status:** `CASE21_GLOBAL_RESIDUE_GKZ_RELATIVE_A_HYPERGEOMETRIC_R11 = ACTIVE`

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

The former true-infinite Chebyshev/material-prefix production layer is removed. The formal material object is the exact finite current operator.

## R10 local exact integration step

`semantic_v2/20_theory/20260819__NZSCCM__CASE21_CONCRETE__THICKNESS_ALGEBRAIC_FIELD_TO_FINITE_LAURICELLA_CLOSURE__R10.md`

R10 remains a valid fixed-(r,s) local representation: thickness integration can be reduced to finite elementary / elliptic / Lauricella FD combinations. It is no longer mandatory as the only route for the outer variables.

## R11 active constructor switch

`semantic_v2/20_theory/20260819__NZSCCM__CASE21_CONCRETE__GLOBAL_RESIDUE_GKZ_AND_RELATIVE_INCOMPLETE_A_HYPERGEOMETRIC_CLOSURE__R11.md`

R11 retains all spatial variables simultaneously, removes the finite algebraic radicals by exact iterated residue lifting, and rewrites the complete-halfwave target as one finite rational period. The finite denominator polynomial supports define a Cayley A-configuration and therefore a standard GKZ A-hypergeometric family. Because the physical [0,1]^3 factor is a bounded relative chain, the strict physical identity is ordinary GKZ after closed-cycle/Pochhammer continuation or relative/incomplete A-hypergeometric when boundary terms remain.

```text
MATERIAL_TRUE_INFINITE_SERIES_LAYER = REMOVED
OUTER_RS_SEQUENTIAL_LAURICELLA = NOT REQUIRED
GLOBAL_MULTIRESIDUE_RATIONALIZATION = PASS
GLOBAL_RATIONAL_PERIOD = PASS
GLOBAL_GKZ_STANDARD_FUNCTION_CLASSIFICATION = PASS
PHYSICAL_CHAIN_RELATIVE_INCOMPLETE_GKZ_CLASSIFICATION = PASS
FULL_MINIMAL_A_MATRIX_PRINTED = NO
FULL_CASE21_Pc_STANDARD_FUNCTION_EVALUATED = NO
ZERO_DISCRETIZATION = PASS
```

## Why this supersedes the R10-only next step

The fixed-(r,s) Lauricella arguments move algebraically with (r,s), so there is no reason the remaining two integrations must remain low-dimensional Lauricella. Per user instruction, failure/inconvenience of one named special-function constructor is not a reason to deadlock. R11 promotes a more general standard constructor rather than reverting to custom series or discretization.

## Exact backend hierarchy

```text
elementary/Beta/Gamma
-> Carlson R / Appell F1 / Lauricella FD when favorable
-> GKZ generalized Euler/residue representation
-> relative/incomplete A-hypergeometric for physical bounded chains / exact threshold boundaries
-> Picard-Fuchs/holonomic only as optional evaluation reduction
```

## Unchanged theory

- raw specimen -> controlling complete representative halfwave;
- Nguyen/von-Karman continuous second-order kinematics;
- exact finite R10 / exact finite steel current operators;
- P(D,q,alpha), Rq(D,q,alpha), Ralpha(D,q,alpha);
- same-source derivatives;
- direct solve Rq=0, Ralpha=0, det(J_lim)=0;
- no comparator in solve.

## Current unique next task

Extract the actual finite denominator set from the Case21 finite-R10 Syy expression; print the monomial supports of G1,G2,G3 and D_S; construct the actual finite Cayley matrix A_GKZ; then test whether P,Rq,Ralpha and all J_lim entries share one master A_* support family. Reduce A_* only by exact algebraic factorization/elimination/symmetry, never by discretization.