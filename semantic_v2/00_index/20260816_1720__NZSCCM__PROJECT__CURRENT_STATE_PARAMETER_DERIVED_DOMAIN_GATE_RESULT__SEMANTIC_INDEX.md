# NZ-SCCM current state — parameter-derived domain gate result

**Timestamp:** 2026-08-16 17:20 +08:00

## Current result

The 17:12 governance correction has now been executed numerically/material-analytically for Z0-Z6.

One common source/design-side domain-generation rule was applied to all seven specimens. The resulting domains are specimen-parameter dependent rather than one identical family-wide interval.

```text
Z0 [-2.326966,+.398162]
Z1 [-2.246565,+.304377]
Z2 [-2.326966,+.398162]
Z3 [-2.241404,+.293969]
Z4 [-2.385927,+.469962]
Z5 [-2.980899,+1.194486]
Z6 [-2.768805,+2.128027]
```

All are generated without experiment/Zhou/Winter calibration and with zero formal structural spatial sampling/quadrature.

## Compiler consequence

Applying the same baseline R10 source-fidelity convergence policy on each domain gives first-passing single-global-lambda orders:

```text
Z0 1792
Z1 1536
Z2 1792
Z3 1536
Z4 1792
Z5 3072
Z6 3840
```

Therefore:

```text
PARAMETER_DERIVED_DOMAIN_RULE = PASS
IDENTICAL_FAMILY_WIDE_PRODUCTION_DOMAIN = RETIRED
SINGLE_GLOBAL_LAMBDA_POLYNOMIAL_LOW_COMPLEXITY = FAIL
R10_PHYSICAL_OPERATOR = UNCHANGED
NEW_Z0_Z6_Pu = NOT RUN
```

The fixed family-wide interval was an over-constraint, but removing it alone does not solve the high-order representation problem. The next step must reconnect the earlier historical multiscale/source-landmark analytic compiler strategy on these corrected domains before any R10 material regularization is considered.

## Current next gate

```text
UNIFIED_V1_PARAMETER_DERIVED_DOMAIN_PLUS_HISTORICAL_MULTISCALE_COMPILER_RECONNECTION_GATE
```

## Read order

1. `../10_governance/20260816_1720__NZSCCM__PARAMETER_DERIVED_DOMAIN_AND_COMPILER_GATE__LOCK.md`
2. `../40_execution/common/20260816_1720__NZSCCM__PARAMETER_DERIVED_DOMAIN_AND_COMPILER__EXECUTION_REPORT.md`
3. `../40_execution/common/20260816_1720__NZSCCM__PARAMETER_DERIVED_DOMAIN_AND_COMPILER__PARAMS_AND_INTERMEDIATES.json`
4. `../40_execution/common/20260816_1720__NZSCCM__PARAMETER_DERIVED_DOMAIN_AND_COMPILER__REPRO.py`
5. `../60_validation/common/20260816_1720__NZSCCM__PARAMETER_DERIVED_DOMAIN_AND_GLOBAL_COMPILER__AUDIT.md`
6. `../20_theory/20260816_1217__NZSCCM__UNIFIED_PRODUCTION_WORKFLOW_V1__THEORY_AND_EXECUTION_CONTRACT.md`
7. `20260816_1712__NZSCCM__PROJECT__CURRENT_STATE_PARAMETER_DERIVED_DOMAIN_WORKFLOW_CORRECTION__SEMANTIC_INDEX.md` — governance predecessor
