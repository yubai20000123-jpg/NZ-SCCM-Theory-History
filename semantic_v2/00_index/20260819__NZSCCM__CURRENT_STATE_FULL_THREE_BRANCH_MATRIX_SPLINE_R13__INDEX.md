# NZ-SCCM CURRENT STATE — FULL THREE-BRANCH MATRIX-SPLINE CONSTRUCTOR R13

**Date:** 2026-08-19  
**Status:** `R13_CASE21_Z6_UNBUCKLED_BRANCH_BIAS_DIAGNOSED`

## Governing constructor

`semantic_v2/20_theory/20260819__NZSCCM__CASE21__FULL_THREE_BRANCH_MATRIX_SPLINE_GKZ_CONSTRUCTOR__R13.md`

## Material-series replacement status

The former true-infinite Chebyshev/material-prefix production layer is removed. The complete three-branch R10 tension law is represented by one exact finite truncated-power spline and its spectral matrix lift.

```text
GLOBAL_THREE_BRANCH_MATRIX_SPLINE = PASS
FULL_THREE_BRANCH_SPARSE_CH_CIRCUIT = PASS
FULL_THREE_BRANCH_MASTER_ASTAR = PASS
MATERIAL_SERIES_REPLACEMENT = COMPLETE
```

Complete machine structure:

```text
relations             = 112
monomial variables    = 115
Cayley A* rows         = 227
Cayley A* columns      = 403
max relation monomials= 13
```

## Mandatory governance

`semantic_v2/10_governance/20260819_0142__NZSCCM__PROJECT__ZERO_DISCRETIZATION_AND_GITHUB_CONTINUITY__LOCKED_GOVERNANCE.md`

```text
ZERO_DISCRETIZATION_DEFAULT = LOCKED
DISCRETE_AUDIT_ORACLE = PROHIBITED
FINITE_PREFIX_CONVERGENCE_AS_EVIDENCE = PROHIBITED
AUTO_GITHUB_CHECKPOINT_AFTER_MATERIAL_CHANGE = REQUIRED
PROACTIVE_CHAT_LENGTH_CHECKPOINT = REQUIRED
```

## Execution artifacts

Case21 first uniform-branch smoke test:

`semantic_v2/40_execution/combined/20260819__NZSCCM__CASE21__R13_ZERO_DISCRETE_TRIAL_CALC_UNBUCKLED_BRANCH.md`

Case21/Z6 bias diagnosis and Z6 same-method calculation:

`semantic_v2/40_execution/combined/20260819__NZSCCM__CASE21_Z6__R13_UNBUCKLED_BRANCH_OVERPREDICTION_DIAGNOSIS.md`

## Corrected interpretation of the uniform branch

The uniform `q=0, alpha=0` stationary condition

```text
dP(D,0,0)/dD = 0
```

is a material/section stationary point only. It is rejected as a definition of plate `Pu` because it suppresses the nonuniform buckling/postbuckling branch.

Case21:

```text
P*_uniform = 538.273498279198 kN
Pcr        = 407.136279059126 kN
D(Pcr)     = 0.478843845165660
released coupled Pu = 366.767828685212 kN
experiment          = 368.312749743569 kN
uniform-vs-experiment = +46.1458 %
```

Z6, calculated by the same exact zero-discretization uniform-branch method with the frozen concrete/face/web current laws:

```text
P*_uniform = 90.1504381160020 MN
Pcr        = 39.2880147150278 MN
D(Pcr)     = 0.303002225781078
released coupled Pu = 48.4061215 MN
Zhou comparator     = 49.4867667519 MN
Winter comparator   = 50.1858541295 MN
```

Uniform-branch overprediction:

```text
Case21 vs experiment = +46.1458 %
Z6 vs released Pu    = +86.2377 %
Z6 vs Zhou           = +82.1708 %
Z6 vs Winter         = +79.6332 %
```

Conclusion: severe overprediction is systematic for using the **unbuckled material branch as a surrogate for structural Pu**. It is not evidence that the R13 finite material spline itself is biased.

## Formal plate limit remains unchanged

```text
Rq(D,q,alpha)=0
Ralpha(D,q,alpha)=0
det(Jlim(D,q,alpha))=0
Pu=P(Du,qu,alphau)
```

The next execution must move to the full nonuniform continuous `(D,q,alpha)` system using the same R13 finite current operator. No new material gate is created and no discrete fallback is permitted.
