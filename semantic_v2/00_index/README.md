# NZ-SCCM semantic tree v2

This namespace is the **content-first, non-destructive semantic reconstruction** of the repository.

## Current operational entry

Use first:

`20260816_1720__NZSCCM__PROJECT__CURRENT_STATE_PARAMETER_DERIVED_DOMAIN_GATE_RESULT__SEMANTIC_INDEX.md`

## Current locked production backbone

```text
UNIFIED_PRODUCTION_WORKFLOW_V1
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order continuous kinematics
MEMBRANE_STRESS_REDISTRIBUTION = REQUIRED
source current material operator
same-state current stress + consistent current tangent
Cayley-Hamilton / approved finite matrix lift
moment-first General-D15 exact structural moments
P,Rq,L connected-branch primary limit root
same-state material + geometric tangent/stability audit
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
structural calibration = NO
```

## Unified workflow means unified rules, not identical numerical domains

The 17:12 correction is now executed. Each specimen receives a material-coordinate validity domain from one common source/design-side reachability rule using its geometry, physical boundary, selected complete halfwave, material parameters and declared generalized-coordinate bounds. The same material-family compiler policy and source stress/tangent gates are then applied.

```text
same rule + different specimen parameters -> different domains/orders = ALLOWED
case ID / Pu error / experiment -> special domain/order = PROHIBITED
```

## 17:20 parameter-derived-domain result

Generated Z0-Z6 cores:

```text
Z0 [-2.326966,+.398162]
Z1 [-2.246565,+.304377]
Z2 [-2.326966,+.398162]
Z3 [-2.241404,+.293969]
Z4 [-2.385927,+.469962]
Z5 [-2.980899,+1.194486]
Z6 [-2.768805,+2.128027]
```

Applying the same baseline single-global-lambda R10 convergence screen on each domain gives:

```text
Z0 N=1792
Z1 N=1536
Z2 N=1792
Z3 N=1536
Z4 N=1792
Z5 N=3072
Z6 N=3840
```

Therefore the former identical family-wide interval requirement is retired, but one global lambda polynomial remains too high-order to be the desired production grammar.

```text
PARAMETER_DERIVED_DOMAIN_RULE = PASS
SINGLE_GLOBAL_LAMBDA_POLYNOMIAL_LOW_COMPLEXITY = FAIL
R10_PHYSICAL_OPERATOR = UNCHANGED
```

The exact-Pi elliptic-period audit remains diagnostic only; Pi regularization is not the mandatory next task.

## Capacity status

```text
Z6 51.30 MN = retained user-accepted engineering baseline only
Z6 unified rerun = incomplete
Z0-Z5 10:43 values = retracted
Z0-Z5 12:48 values = diagnostic locators only
new Z0-Z6 production Pu = not released
```

## Current next gate

```text
UNIFIED_V1_PARAMETER_DERIVED_DOMAIN_PLUS_HISTORICAL_MULTISCALE_COMPILER_RECONNECTION_GATE
```

The next step reconnects the historical R5/MSAC/source-landmark multiscale analytic compiler and moment-first contraction lessons on the corrected specimen-derived domains. No R10 material-law change is authorized before that gate is tested.

## Repository semantic read order

1. `20260816_1720__NZSCCM__PROJECT__CURRENT_STATE_PARAMETER_DERIVED_DOMAIN_GATE_RESULT__SEMANTIC_INDEX.md`
2. `../10_governance/20260816_1720__NZSCCM__PARAMETER_DERIVED_DOMAIN_AND_COMPILER_GATE__LOCK.md`
3. `../40_execution/common/20260816_1720__NZSCCM__PARAMETER_DERIVED_DOMAIN_AND_COMPILER__EXECUTION_REPORT.md`
4. `../40_execution/common/20260816_1720__NZSCCM__PARAMETER_DERIVED_DOMAIN_AND_COMPILER__PARAMS_AND_INTERMEDIATES.json`
5. `../40_execution/common/20260816_1720__NZSCCM__PARAMETER_DERIVED_DOMAIN_AND_COMPILER__REPRO.py`
6. `../60_validation/common/20260816_1720__NZSCCM__PARAMETER_DERIVED_DOMAIN_AND_GLOBAL_COMPILER__AUDIT.md`
7. `../20_theory/20260816_1217__NZSCCM__UNIFIED_PRODUCTION_WORKFLOW_V1__THEORY_AND_EXECUTION_CONTRACT.md`
8. `20260816_1712__NZSCCM__PROJECT__CURRENT_STATE_PARAMETER_DERIVED_DOMAIN_WORKFLOW_CORRECTION__SEMANTIC_INDEX.md` — governance predecessor

No legacy file is deleted, moved or renamed solely from filename identity.
