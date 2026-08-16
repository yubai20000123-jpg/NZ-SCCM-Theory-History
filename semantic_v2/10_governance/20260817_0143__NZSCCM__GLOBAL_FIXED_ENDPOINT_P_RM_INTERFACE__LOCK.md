# NZ-SCCM — global fixed-endpoint P/Rm production interface lock

**Timestamp:** 2026-08-17 01:43 +08:00

## Decision

The actual `P + five Rm` thickness-to-`(X,Y)` comparison is closed.

```text
PRODUCTION_THICKNESS_TO_XY_REPRESENTATION
  = GLOBAL_FIXED_ENDPOINT_POSITIVE_PART_FACTORISED_PERIOD

EVENT_RESOLVED_BRANCHWISE_8_STATE
  = RETAIN_AS_LOCAL_EXACT/AUDIT REPRESENTATION
  = NOT GLOBAL PRODUCTION INTERFACE
```

## Reason

The event-resolved form is locally compact (`<=8` field states), but its exact source-knot roots

\[
\zeta_m(X,Y)
\]

change existence/order over the complete halfwave. The in-plane event fronts are nontrivial algebraic/trigonometric curves

\[
\det(E(X,Y,\pm1)-\lambda_mI)=0.
\]

For the generic five-coordinate strain field the endpoint-front total trigonometric degree is 8 and the event-root discriminant degree is 12.

Global use of the event-resolved form would therefore require either:

1. formal `(X,Y)` region subdivision; or
2. clipped-root / positive-part selectors that reconstruct the branch-free source structure.

The first is inconsistent with `N_formal_spatial_subdomains=1`; the second adds bookkeeping without improving the global interface.

## Actual interface frozen

Define only the three common thickness stress resultants

```text
Nx0  = int sigma_x  dzeta
Ny0  = int sigma_y  dzeta
Nxy0 = int tau_xy   dzeta
```

between fixed endpoints `zeta=-1,+1`.

These three quantities generate:

```text
P_c
Rm0_c
Rm20_c
Rmu22_c
Rm02_c
Rmv22_c
```

through finite trigonometric target weights.

The production operator must compute all three from one common current material state.

## Downstream API requirement

Do not design a P-only thickness operator. The common implementation must be extensible to the finite moment family required later:

```text
stress moments:  k=0,1
tangent target moments: k=0,1,2
```

No arbitrary/high-order thickness moment ladder is authorized.

## Allowed mathematics/tools

Any exact/analytic backend may be used provided the production object stays compact and does not enumerate high-order material coefficients. This includes factorized algebraic periods, matrix-function Fréchet/Sylvester evaluation, Cayley-Hamilton reduction, target-side adjoints, holonomic/creative-telescoping reduction, and special functions.

Independent numerical quadrature may be used only as an audit oracle.

## Formal counters

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
Z6_BOUNDARY = FOUR_EDGE_SIMPLY_SUPPORTED / SSSS
```

## Prohibited regressions

```text
NO XY EVENT-TOPOLOGY CELLS/SUBDOMAINS
NO MATERIAL-POINT GRID
NO GAUSS/SIMPSON/ADAPTIVE PRODUCTION INTEGRATION
NO N1000/N3000/N5000 COEFFICIENT ENUMERATION
NO EXPLICIT 64-RATIONAL-COEFFICIENT CANONICALIZATION AS PRODUCTION REQUIREMENT
NO N48 FALLBACK AS FIX FOR COMPACT-EXACT BLOCKERS
```

## Unique next task

`GLOBAL_FIXED_ENDPOINT_THREE_STRESS_MOMENT_DESCRIPTOR_GATE`

Construct, at fixed `(D,q,r;X,Y)`, the actual common analytic operator

\[
[N_x^{(0)},N_y^{(0)},N_{xy}^{(0)}]
=\int_{-1}^{1}[\sigma_x,\sigma_y,\tau_{xy}]\,d\zeta
\]

using the source-regular factorized R10 DAG, without numerical thickness quadrature and without explicit high-order coefficient enumeration.

The operator must carry same-source parameter derivatives needed by P/Rm before the subsequent exact `(X,Y)` contraction is started.

`NEW_Pu = NOT_RUN`.
