# R09A TENSION SENSITIVITY DECISION — 2026-08-10

## Locked conclusion

For Case21 axial-compression stability, the direct load is compression dominated, but the tensile constitutive level is not mechanically negligible because it shifts the coupled equilibrium/stationary coordinates `(D,q)` and therefore changes the compression-side contribution itself.

Executed monotone saturation brackets:

```text
SAT03: u_inf = 0.03 fc -> Pu = 322.401942 kN
SAT05: u_inf = 0.05 fc -> Pu = 334.822979 kN
SAT07: u_inf = 0.07 fc -> Pu = 345.811115 kN
```

The spread is

```text
Delta Pu = 23.409173 kN
Delta Pu / mean Pu = 7.001495 %
```

Therefore:

```text
COMPRESSION_DOMINATES_DIRECT_LOAD = PASS
TENSILE_SHAPE_CAN_BE_STRONGLY_SIMPLIFIED = PASS
TENSILE_CAPACITY_LEVEL_IS_NEGLIGIBLE = FAIL
```

## Production implication

The project no longer needs a high-complexity source-faithful tensile peak/softening shape. A simple explicit monotone law is admissible and preferred.

However, the one retained tensile-capacity level must be defined independently of Case21/Swartz experimental Pu. It must come from:

1. the selected material source / constitutive evidence; or
2. an explicit conservative design convention declared before structural validation.

The Case21 experiment may validate the frozen tensile level but may not select it.

## Current simple family retained for screening

For `lambda >= 0`:

\[
u_t(\lambda)=u_\infty\frac{r}{1+r},
\qquad
r=\frac{\kappa\lambda}{u_\infty},
\]

\[
u_t'(\lambda)=\frac{\kappa}{(1+\kappa\lambda/u_\infty)^2}.
\]

This family is retained because it is explicit, monotone, nonoscillatory, has the correct initial tangent, and carries only one tensile-capacity parameter.

## Next task

```text
R09B_SOURCE_GROUNDED_TENSION_CAPACITY_LEVEL
```

R09B must freeze the NC tensile-capacity level from material evidence / a declared conservative material rule before any further multiaxial correction is considered.