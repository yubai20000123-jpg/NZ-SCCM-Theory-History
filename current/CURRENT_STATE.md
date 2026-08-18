# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-19  
**Status:** `R13_CASE21_Z6_UNBUCKLED_BRANCH_BIAS_DIAGNOSED = ACTIVE`

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

```text
GLOBAL_THREE_BRANCH_MATRIX_SPLINE = PASS
FULL_THREE_BRANCH_SPARSE_CH_CIRCUIT = PASS
FULL_THREE_BRANCH_MASTER_ASTAR = PASS
MATERIAL_SERIES_REPLACEMENT = COMPLETE
```

## Latest execution diagnosis

`semantic_v2/40_execution/combined/20260819__NZSCCM__CASE21_Z6__R13_UNBUCKLED_BRANCH_OVERPREDICTION_DIAGNOSIS.md`

The previous Case21 `q=0, alpha=0` calculation was a **uniform material/section stationary point**, not the plate Pu. Using `dP(D,0,0)/dD=0` suppresses the nonuniform buckling/postbuckling branch and is therefore rejected as a Pu definition.

Case21:

```text
P*_uniform = 538.273498279198 kN
Pcr        = 407.136279059126 kN
D(Pcr)     = 0.478843845165660
D*_uniform = 1.083794870106547
released coupled Pu = 366.767828685212 kN
experiment          = 368.312749743569 kN
uniform-vs-experiment = +46.1458 %
```

Z6 was then calculated by the same exact zero-discretization uniform-branch method while retaining the frozen Z6 concrete/face/web current laws:

```text
web yield D       = 0.920936195308814
face radial-cap D = 0.939442186454484
uniform stationary D* = 0.999995310340506
Pc,eff   = 43.6158967880144 MN
Pfaces   = 36.1401413279875 MN
Pweb     = 10.3944000000000 MN
P*_uniform,Z6 = 90.1504381160020 MN
Pcr,Z6        = 39.2880147150278 MN
D(Pcr,Z6)     = 0.303002225781078
```

Post-solve comparison only:

```text
vs released coupled Z6 Pu = +86.2377 %
vs Zhou comparator         = +82.1708 %
vs Winter comparator       = +79.6332 %
```

Therefore the severe overprediction is systematic for the **uniform unbuckled branch used as a surrogate for Pu**, especially when the instability scale lies far below the material section capacity. It does not establish an overprediction of the R13 finite material constructor itself.

## Correct structural limit identity

The formal plate limit remains

```text
Rq(D,q,alpha) = 0
Ralpha(D,q,alpha) = 0
det(Jlim(D,q,alpha)) = 0
Pu = P(Du,qu,alphau)
```

The next execution must use the full nonuniform continuous `(D,q,alpha)` system with the same R13 finite material constructor. No new material gate is created and no discrete fallback is allowed.
