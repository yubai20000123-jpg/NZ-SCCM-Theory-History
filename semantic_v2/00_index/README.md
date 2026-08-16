# NZ-SCCM semantic tree v2

This namespace is the **content-first, non-destructive semantic reconstruction** of the repository.

## Current operational entry

Use first:

`20260816_1417__NZSCCM__PROJECT__CURRENT_STATE_R10_EXACT_PI_EXISTING_D15_ADAPTER_FAIL__SEMANTIC_INDEX.md`

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
same-state material + geometric KZ audit
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
structural calibration = NO
```

The same workflow serves NC+rebar, NC+steel shell, UHPC+rebar and UHPC+steel shell. Physical adapters may differ; the parent kinematics, membrane redistribution, zero-integration philosophy, generalized root topology and consistent-current-tangent requirement may not change case by case.

## NC representation status

The ordinary-concrete source remains frozen R10.

The former wide single-global lambda-space `N=3584` result is retained only as a source-fidelity witness:

```text
E_sigma=.00107218
E_tangent=.04066517
E_divided_difference=.00381386
```

It is no longer the intended production representation.

The 13:55 intrinsic-coordinate material screen retained exact `Pi_eta` and used `N_C=6`, `N_u=64`, giving 72 fitted scalar coefficients and

```text
E_sigma=.003337
E_tangent=.030469
E_divided_difference=.046869
```

which passes the material gates.

## 14:17 exact Pi adapter result

Exact algebra gives

```text
Pi(z)+Pi(-z)=z^2/sqrt(z^2+eta^2)
Pi(z)-Pi(-z)=z^3/(z^2+eta^2)
```

For a simple traceless finite-trigonometric matrix field, exact spectral lifting already requires a moment

```text
J=2*eta*[E(-m)-K(-m)]
```

with complete elliptic integrals.

Therefore exact `Pi_eta` is outside the currently approved finite Beta/Gamma General-D15 closure algebra.

```text
EXACT_PI_MATRIX_LIFT = PASS
EXACT_PI_TO_EXISTING_GENERAL_D15_FINITE_MOMENT_CLOSURE = FAIL
NEW_SPECIAL_FUNCTION_STRUCTURAL_BACKEND = NOT_AUTHORIZED
R10_MATERIAL_CHANGE = NOT_EXECUTED
```

This does not prove every possible exact special-function backend impossible; it establishes that the current General-D15 engine cannot absorb exact `Pi_eta` without leaving its finite moment class.

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
UNIFIED_V1_R10_PI_D15_COMPATIBLE_LOW_PARAMETER_REGULARIZATION_DECISION_GATE
```

No new splitter is frozen yet. The next decision must compare a deliberately new special-function moment backend against a low-parameter D15-compatible material splitter, using material/source criteria only and no structural calibration.

## Repository semantic read order

1. `20260816_1417__NZSCCM__PROJECT__CURRENT_STATE_R10_EXACT_PI_EXISTING_D15_ADAPTER_FAIL__SEMANTIC_INDEX.md`
2. `../10_governance/20260816_1417__NZSCCM__R10_FACTORIZED_PI_EXISTING_D15_ADAPTER_GATE__LOCK.md`
3. `../40_execution/common/20260816_1417__NZSCCM__R10_FACTORIZED_PI_EXISTING_D15_ADAPTER__EXECUTION_REPORT.md`
4. `../40_execution/common/20260816_1417__NZSCCM__R10_FACTORIZED_PI_EXISTING_D15_ADAPTER__PARAMS_AND_INTERMEDIATES.json`
5. `../40_execution/common/20260816_1417__NZSCCM__R10_FACTORIZED_PI_EXISTING_D15_ADAPTER__REPRO.py`
6. `../60_validation/common/20260816_1417__NZSCCM__R10_EXACT_PI_TO_GENERAL_D15_CLOSURE__AUDIT.md`
7. `20260816_1355__NZSCCM__PROJECT__CURRENT_STATE_R10_INTRINSIC_SCALE_GLOBAL_ORDER_DIAGNOSIS__SEMANTIC_INDEX.md` — predecessor
8. `../20_theory/20260816_1217__NZSCCM__UNIFIED_PRODUCTION_WORKFLOW_V1__THEORY_AND_EXECUTION_CONTRACT.md`
9. `20260816_0249__NZSCCM__PROJECT__CURRENT_STATE_Z6_AR2_SSSS_CAPACITY__SEMANTIC_INDEX.md` — retained Z6 baseline

No legacy file is deleted, moved or renamed solely from filename identity.
