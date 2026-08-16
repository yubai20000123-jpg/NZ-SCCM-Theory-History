# NZ-SCCM governance lock — RC1 adjoint target failure / next exact moment closure

**Timestamp:** 2026-08-16 19:32 +08:00

## Locked results

```text
R10_MSAC_RC1_MATERIAL_SOURCE_FIDELITY = PASS_RETAINED
FIVE_TERM_MEMBRANE_GENERAL_D15_TARGETS = PASS_RETAINED
ADJOINT_CLENSHAW_ALGEBRA = PASS_EXACT
LOW_ORDER_NESTED_TARGET_IDENTITY = PASS_EXACT
RC1_NESTED_ATOM_CLOSED_MOMENT_RULE = ABSENT
ACTIVE_RC1_STRUCTURAL_TARGET_RUNTIME = FAIL_PREFLIGHT
NEW_Pu = NOT_RUN
```

The structural failure does not reopen the R10 physical law and does not invalidate the RC1 material-only source-fidelity gate.

## Prohibited misinterpretations

```text
ADJOINT_CLENSHAW_PASS => RC1_PRODUCTION_PASS        = FALSE
MATERIAL_SOURCE_FIDELITY_PASS => STRUCTURAL_PASS    = FALSE
DELAYED_EXPRESSION_DAG => EXACT_MOMENT_CLOSURE      = FALSE
FULL_NESTED_FLATTENING                            = PROHIBITED
COEFFICIENT_THRESHOLD_PRUNING                     = PROHIBITED_AS_PRODUCTION
Z6_ONLY_FALLBACK                                  = PROHIBITED
NEW_Pu_BEFORE_STRUCTURAL_CLOSURE                  = PROHIBITED
```

## Required interpretation

Adjoint Clenshaw changes where the recurrence is carried but does not eliminate polynomial-composition degree. If the target leaf algebra only knows ordinary General-D15 polynomial moments, multiplication by a nested beta/Chebyshev atom must eventually be reduced to that algebra and recreates the degree hierarchy.

The missing primitive is a true exact closure such as

```text
L[K Phi(F)] -> closed finite moment transform
```

without expanding `Phi(F)` into the ordinary base polynomial field.

## Current unique next gate

```text
UNIFIED_V1_NC_EXACT_NESTED_ATOM_MOMENT_CLOSURE_OR_STRUCTURALLY_CLOSED_COMPILER_REDESIGN_GATE
```

Only two families of next route are admissible:

1. **Exact nested-atom moment closure:** derive a closed analytic transform for the current RC1 beta/natural-coordinate atoms under the required D15 targets; or
2. **Structurally closed family compiler redesign:** replace the material analytic representation, without changing R10 physics, by a source-faithful basis whose exact target moments close directly through General-D15/CAS/special-function algebra.

Any new representation must remain one family-level method for NC+rebar and NC+shell and may not use experiment/Zhou/Winter response calibration.

## Zero-integration lock retained

```text
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
N_formal_thickness_quadrature=0
```
