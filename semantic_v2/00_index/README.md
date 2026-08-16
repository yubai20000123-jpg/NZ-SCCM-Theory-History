# NZ-SCCM semantic tree v2

This namespace is the **content-first, non-destructive semantic reconstruction** of the repository.

## Current operational entry

Use first:

`20260816_1248__NZSCCM__PROJECT__CURRENT_STATE_N3584_COMMON_BACKEND_TRACTABILITY_FAIL__SEMANTIC_INDEX.md`

## Current locked production backbone

```text
UNIFIED_PRODUCTION_WORKFLOW_V1
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order continuous kinematics
MEMBRANE_STRESS_REDISTRIBUTION = REQUIRED
source current material operator
same-state consistent current tangent
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

The same workflow serves NC+rebar, NC+steel shell, UHPC+rebar and UHPC+steel shell. Physical adapters may differ, but the parent kinematics, membrane redistribution, zero-integration philosophy, generalized root topology and consistent-current-tangent requirement may not change case by case.

## NC source-fidelity result retained

The ordinary-concrete source remains frozen R10. The 12:29 source-only convergence result remains:

```text
core = [-2.35,+1.90]
guard = [-2.60,+2.15]
source-fidelity candidate order = 3584
E_sigma = .00107218
E_tangent = .04066517
E_divided_difference = .00381386
```

Therefore `N3584_SOURCE_FIDELITY = PASS`.

## 12:48 structural-backend result

An order-agnostic backward Chebyshev/Cayley-Hamilton Clenshaw pair was implemented and verified against the historical degree-48 forward recurrence at roundoff scale.

```text
ORDER_AGNOSTIC_CH_CLENSHAW_IDENTITY = PASS
```

However a simple coefficient-amplitude pruning strategy is not a certified exact production backend: Z0 generalized residuals vary non-monotonically as the threshold is reduced.

Z0-Z5 branch neighborhoods can be reached diagnostically using the N3584 source coefficients and the common SSSS/Nguyen/membrane equations, but the values are not production Pu because `L`, same-state `KZ`, and algebraic convergence are not closed.

At the wide-spectrum Z6 engineering state the present N3584 coefficient-tensor realization becomes impractical:

```text
full concrete tol=2e-4: >180 s / not completed
full concrete tol=1e-3: >120 s / not completed
T-channel CH pair only tol=1e-3: >120 s / not completed
```

Hence:

```text
N3584_SOURCE_FIDELITY = PASS
N3584_FULL_PRODUCTION_COMPILER_PROMOTION = WITHHELD
CURRENT_COEFFICIENT_TENSOR_COMMON_BACKEND = FAIL_TRACTABILITY
```

No Z6-only fallback solver is permitted.

## Capacity status

```text
Z6 51.30 MN = retained user-accepted engineering baseline only
Z6 unified rerun = incomplete
Z0-Z5 10:43 values = retracted
Z0-Z5 12:48 values = diagnostic locators only
new Z0-Z6 production Pu = not released
```

## Current next gate

`UNIFIED_V1_NC_COMPILER_STRUCTURAL_TRACTABILITY_REDESIGN_GATE`

The next representation/backend must be family-level, source-controlled, zero-spatial-integration, General-D15 compatible, and tractable across Z0-Z6. Case-specific compiler intervals/orders and Z6-only fallbacks remain prohibited.

## Repository semantic read order

1. `20260816_1248__NZSCCM__PROJECT__CURRENT_STATE_N3584_COMMON_BACKEND_TRACTABILITY_FAIL__SEMANTIC_INDEX.md`
2. `../10_governance/20260816_1248__NZSCCM__N3584_CH_D15_BACKEND_TRACTABILITY_GATE__LOCK.md`
3. `../40_execution/common/20260816_1248__NZSCCM__N3584_CH_D15_BACKEND_AND_Z0_Z6_RERUN__EXECUTION_REPORT.md`
4. `../40_execution/common/20260816_1248__NZSCCM__N3584_CH_D15_BACKEND__PARAMS_AND_INTERMEDIATES.json`
5. `../40_execution/common/20260816_1248__NZSCCM__N3584_CH_CLENSHAW_D15_BACKEND__REPRO.py`
6. `../60_validation/common/20260816_1248__NZSCCM__N3584_CH_D15_COMMON_BACKEND_TRACTABILITY__AUDIT.md`
7. `20260816_1229__NZSCCM__PROJECT__CURRENT_STATE_NC_FAMILY_COMPILER_SOURCE_FREEZE_PASS__SEMANTIC_INDEX.md` — source-fidelity predecessor
8. `../20_theory/20260816_1217__NZSCCM__UNIFIED_PRODUCTION_WORKFLOW_V1__THEORY_AND_EXECUTION_CONTRACT.md`
9. `20260816_0249__NZSCCM__PROJECT__CURRENT_STATE_Z6_AR2_SSSS_CAPACITY__SEMANTIC_INDEX.md` — retained Z6 engineering baseline
10. `20260816_1134__NZSCCM__PROJECT__CURRENT_STATE_Z0_Z5_FIXED_N48_REPRESENTATION_CAPACITY_FAIL__SEMANTIC_INDEX.md` — historical N48 representation diagnostic

No legacy file is deleted, moved or renamed solely from filename identity.
