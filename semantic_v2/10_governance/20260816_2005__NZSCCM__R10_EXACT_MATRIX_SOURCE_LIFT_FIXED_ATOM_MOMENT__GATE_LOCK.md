# NZ-SCCM governance lock — exact R10 matrix source lift / fixed algebraic atom boundary

**Timestamp:** 2026-08-16 20:05 +08:00

## Locked results

```text
R10_PHYSICAL_CURRENT_LAW = RETAIN_FROZEN
R10_MSAC_RC1_MATERIAL_SOURCE_FIDELITY = RETAIN_PASS_AS_REFERENCE
R10_EXACT_SMOOTH_SPLIT_MATRIX_LIFT = PASS_EXACT
UR_TRUNCATED_POWER_SPLINE = PASS_EXACT
R10_2D_STRESS_INVARIANT_MATRIX_IDENTITY = PASS_EXACT
CONSISTENT_TANGENT_FINITE_GRAPH = PASS_FORMAL
INDEPENDENT_T7_COMPILER_CHANNEL = ELIMINATED
MATERIAL_FIT_ORDER_DEPENDENCE_IN_SOURCE_GRAPH = ELIMINATED
FIXED_ALGEBRAIC_ATOM_GRAPH = PASS_FORMAL
GENERAL_D15_ALGEBRAIC_ATOM_MOMENT_CLOSURE = OPEN
NEW_Pu = NOT_RUN
```

## Required interpretation

The 19:32 failure belonged to the **nested RC1 polynomial structural adapter**, not to R10 physics.

The present result shows that the frozen R10 source itself admits a finite exact matrix-function graph. Therefore the project no longer needs to carry the RC1 nested beta/Chebyshev fit hierarchy into the structural moment engine.

`R10-MSAC-RC1` remains an accepted material-level reconstruction/audit witness. It is not deleted or retroactively marked false.

## Fixed source graph

The current structural candidate is built from only these non-polynomial atom families:

```text
sqrt(E^2+eta^2 I)
inverse(I+(kappa-2)c+c^2)
(t/a-I)_+^k,   k=3..5
(t/a-10I)_+^k, k=3..5
```

plus finite 2x2 matrix polynomial/invariant operations.

`T^7` is computed exactly from `T` and is not an independent material approximation channel.

## Prohibited regressions

```text
RETURN_TO_RC1_FULL_POLYNOMIAL_FLATTENING = PROHIBITED
REPEAT_FORWARD_CLENSHAW_WITH_SAME_LEAF = PROHIBITED
REPEAT_ADJOINT_CLENSHAW_WITH_SAME_NESTED_POLYNOMIAL_LEAF = PROHIBITED
COEFFICIENT_THRESHOLD_PRUNING_AS_PRODUCTION = PROHIBITED
Z6_ONLY_FALLBACK = PROHIBITED
SPATIAL_GAUSS_SIMPSON_ADAPTIVE_COLLOCATION = PROHIBITED
MATERIAL_POINT_GRID_AS_FORMAL_THEORY = PROHIBITED
NEW_Pu_BEFORE_FIXED_ATOM_MOMENT_CLOSURE = PROHIBITED
EXPERIMENT_ZHOU_WINTER_RESPONSE_CALIBRATION = PROHIBITED
```

## Zero-integration lock

```text
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
N_formal_thickness_quadrature=0
```

## Global structural topology retained

```text
global coordinates = (D,q)
internal membrane coordinates = [r0,r20,r22,s02,s22]
Rm=0
r_g=-Krr^-1 Rm_g
Schur condensation = required
Pbar,Rqbar,Lbar = same connected-branch framework
same-state KZ = required before production release
```

## Current unique next gate

```text
UNIFIED_V1_R10_FIXED_ALGEBRAIC_ATOM_GENERAL_D15_CAS_MOMENT_CLOSURE_GATE
```

The next gate must derive and execute a target-moment closure for the fixed algebraic atom graph under the existing `P,Rq,Rm,KZ` kernels.

Allowed mathematics includes exact algebraic recurrence, Cayley-Hamilton, CAS, and special-function/holonomic moment identities, provided the formal spatial/thickness numerical quadrature counters remain zero.

If a controlled analytic approximation is introduced for an algebraic atom, it must be a **family-level source-controlled approximation** and must pass the existing stress/tangent/divided-difference material gates before structural promotion.
