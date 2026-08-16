# NZ-SCCM — audit: full R10 64-state adjoint/CH target reduction

**Timestamp:** 2026-08-16 21:18 +08:00

## Audit scope

This audit checks only the new 21:18 target-reduction layer. It does not re-open the frozen R10 physical source, Nguyen kinematics, five-term membrane model, steel adapter, or the previously accepted 64-state field construction.

## Exact symbolic identities

The following identities are algebraic consequences of the 2x2 Cayley–Hamilton theorem:

```text
b0=0
b1=1
bn=t*b(n-1)-d*b(n-2)
T^n=bn*T-d*b(n-1)*I
adj(T^7)=b8*I-b7*T
```

with

```text
b7=t^6-5*t^4*d+6*t^2*d^2-d^3
b8=t^7-6*t^5*d+10*t^3*d^2-4*t*d^3
```

The core reproducer verifies the generic symbolic 2x2 residuals exactly equal zero.

## Field-adjoint identity

For the retained quadratic-tower multiplication tensor, the reproducer checks

```text
lambda(u*v) - <M_v^T lambda,u> = 0 exactly
```

on an exact rational 64-state fiber with deterministic sparse field vectors and a deterministic 64-component rational dual seed.

This check is algebraic only and is not a structural spatial/thickness quadrature.

## Full frozen-R10 stress execution

The actual source graph was executed at exact rational fibers `x=0` and `x=1/2`, including

```text
t,c,C,knot projectors,uR,T,U,full interaction stress
```

using the same 64-state multiplication rules. Knot constants were rationalized only for deterministic exact-rational timing, consistent with the predecessor 20:59 diagnostic practice. The formal source retains the exact R10 algebraic roots.

The compact CH stress and the previously materialized matrix-`T7` stress were compared at `x=0`; all four matrix-entry field residuals were exactly zero.

For the target-specific `Syy` contraction, the exact adjoint result and the directly materialized `Syy` coefficient vector satisfy

```text
x=0   : residual = 0 exactly
x=1/2 : residual = 0 exactly
```

The deterministic target seed was

```text
lambda_i=((i mod 7)-3)/11.
```

## Complexity audit

The executed fibers satisfy

```text
Syy support = 60/64
b7 support  = 64/64
b8 support  = 64/64
```

Hence the compact CH target still reaches the full material compositum. The exact reduction is not produced by an accidental low-dimensional branch.

Diagnostic target timings:

```text
x=0   : old binary-T7 target 14.897 s -> CH compact target 5.103 s
x=1/2 : old binary-T7 target 17.459 s -> CH compact target 5.681 s
```

The timing ratio is approximately `2.92x` and `3.07x`, respectively. Timing is not a theory gate; exact residuals are the primary evidence.

## Zero-integration audit

```text
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
N_formal_thickness_quadrature=0
```

No Gauss, Simpson, adaptive spatial integration, collocation, material-point grid, or thickness quadrature is introduced.

The two fibers are algebraic implementation checks and do not contribute to a structural resultant.

## Boundary audit

The present gate removes the target-side matrix `T7` and final 64-coefficient canonicalization requirement. It does **not** yet evaluate the x-dependent rational dual functional over the full thickness analytically.

Therefore the following claims are **not** made:

```text
FULL_R10_DUAL_HOLONOMIC_THICKNESS_MOMENT_RUNTIME = PASS
BETA_WEIGHTED_XY_CREATIVE_TELESCOPING = PASS
NEW_CURRENT_MEMBRANE_r_SOLVE = RUN
NEW_Pu = RELEASED
```

## Audit verdict

```text
T7_MATRIX_POWER_CH_REDUCTION = PASS_EXACT
FIELD_PRODUCT_ADJOINT_PULLBACK = PASS_EXACT
FULL_R10_COMPACT_STRESS_IDENTITY = PASS_EXACT
FULL_R10_SYY_ADJOINT_FIBER_AUDIT = PASS_EXACT_2_FIBERS
FINAL_64_COEFFICIENT_CANONICALIZATION = NOT_REQUIRED
FULL_R10_DUAL_HOLONOMIC_THICKNESS_MOMENT_RUNTIME = OPEN
NEW_Pu = NOT_RUN
```
