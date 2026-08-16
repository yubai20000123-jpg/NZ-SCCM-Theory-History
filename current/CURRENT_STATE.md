# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-16 17:12 +08:00  
**Status:** LEGACY MUTABLE POINTER ONLY

## Current operational entry

`semantic_v2/00_index/20260816_1712__NZSCCM__PROJECT__CURRENT_STATE_PARAMETER_DERIVED_DOMAIN_WORKFLOW_CORRECTION__SEMANTIC_INDEX.md`

## Frozen project-wide production backbone

```text
UNIFIED_PRODUCTION_WORKFLOW_V1 = ACTIVE
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
Nguyen second-order continuous kinematics = ACTIVE
MEMBRANE_STRESS_REDISTRIBUTION = REQUIRED
source current material operator = REQUIRED
same-state current stress + consistent current tangent = REQUIRED
Cayley-Hamilton / approved finite matrix lift = ACTIVE
General D15 moment-first exact moments = ACTIVE
P,Rq,L connected-branch topology = ACTIVE
same-state material + geometric KZ audit = ACTIVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
Gauss/Simpson/adaptive/collocation/material-point-grid = PROHIBITED
experiment/Zhou/Winter calibration in solve/compiler = PROHIBITED
```

## 17:12 correction — unified workflow does not mean identical numerical boundaries/domains

The project had previously already established that method unification applies to the **calculation rules**, not to every numerical input/boundary/domain value.

For specimen `i`, physical/source boundary, halfwave selector, geometry and material parameters may differ. Under one common reachability rule they may therefore generate different material-coordinate domains:

\[
\Lambda_i=\mathcal B(\text{geometry}_i,\text{physical boundary}_i,\text{halfwave}_i,\theta_{m,i},\text{declared generalized-coordinate bounds}).
\]

Then the same material-family compiler policy and source-value/tangent/divided-difference gates are applied on `Lambda_i`.

```text
UNIFIED_WORKFLOW != ONE_IDENTICAL_DOMAIN_FOR_ALL_SPECIMENS
UNIFIED_WORKFLOW != ONE_IDENTICAL_BOUNDARY_INPUT_FOR_ALL_SPECIMENS
UNIFIED_WORKFLOW != ONE_IDENTICAL_HALFWAVE_LENGTH_FOR_ALL_SPECIMENS
```

Allowed:

```text
same domain-generation rule + different specimen parameters -> different domains
same convergence rule + different derived domains -> different converged orders
```

Prohibited:

```text
case label -> manually selected special interval/order
observed Pu error -> change interval/order
experiment/Zhou/Winter -> select compiler domain/order
Z6-only fallback solver
```

For the Zhou Z-series, the theoretical four-edge simply-supported/Navier source boundary remains the current boundary model; `m*`, `ell=a/m*`, strain reachability and resulting compiler domain may still vary with specimen geometry/parameters under the common selector.

## NC source and recent diagnostics

R10 remains frozen and unchanged.

The former family-wide wide-domain screen:

```text
core=[-2.35,+1.90]
guard=[-2.60,+2.15]
N=3584
E_sigma=.00107218
E_tangent=.04066517
E_divided_difference=.00381386
```

remains a valid conservative source-representability witness only. It is **not** a mandatory identical production interval for Z0-Z6.

The 13:55 intrinsic-scale result and 14:17 exact-Pi closure test remain diagnostic evidence:

```text
N3584_AS_PRODUCTION_BASIS = REJECTED
EXACT_PI_MATRIX_LIFT = PASS
EXACT_PI_TO_EXISTING_GENERAL_D15 = FAIL
```

But the previous conclusion that the next task must regularize `Pi_eta` is cancelled, because that conclusion followed an over-strict family-wide fixed-domain interpretation.

```text
PI_REGULARIZATION_AS_CURRENT_MANDATORY_NEXT_TASK = CANCELLED
R10_MATERIAL_CHANGE = NOT_AUTHORIZED / NOT_EXECUTED
```

## Capacity-result status

```text
Z6_AR2_Pu = 51.30 MN  # retained user-accepted engineering baseline only
Z6_UNIFIED_RERUN = NOT COMPLETED
Z0_Z5_20260816_1043_Pu = RETRACTED
Z0_Z5_20260816_1248_LOCATORS = DIAGNOSTIC_ONLY
NEW_Z0_Z6_PRODUCTION_Pu = NOT RELEASED
SAME_EXPRESSION_L = NOT COMPLETED
SAME_STATE_KZ = NOT COMPLETED
```

## Current unique next gate

```text
UNIFIED_V1_PARAMETER_DERIVED_MATERIAL_DOMAIN_AND_COMPILER_GATE
```

Required next work:

1. derive one analytic/closed specimen-parameter reachability-domain rule;
2. use geometry, physical/source boundary, halfwave and material parameters plus declared generalized-coordinate admissibility/search bounds only;
3. apply the same rule to Z0-Z6 and preserve each resulting domain/guard;
4. apply the same R10 compiler grammar and source stress/tangent/divided-difference convergence gates to each derived domain;
5. allow numerical interval/order differences only as deterministic consequences of the same rule;
6. retain all common mechanics and zero-spatial-integration constraints;
7. only after this gate determine whether any particular derived domain still requires intrinsic-factor or Pi-specific treatment.

## Current key artifacts

- `semantic_v2/10_governance/20260816_1712__NZSCCM__UNIFIED_WORKFLOW_PARAMETER_DERIVED_DOMAIN_BOUNDARY__CORRECTION_LOCK.md`
- `semantic_v2/00_index/20260816_1712__NZSCCM__PROJECT__CURRENT_STATE_PARAMETER_DERIVED_DOMAIN_WORKFLOW_CORRECTION__SEMANTIC_INDEX.md`
- `semantic_v2/20_theory/20260816_1217__NZSCCM__UNIFIED_PRODUCTION_WORKFLOW_V1__THEORY_AND_EXECUTION_CONTRACT.md` — updated with 17:12 clarification
- `semantic_v2/40_execution/common/20260816_1417__NZSCCM__R10_FACTORIZED_PI_EXISTING_D15_ADAPTER__EXECUTION_REPORT.md` — retained diagnostic predecessor
