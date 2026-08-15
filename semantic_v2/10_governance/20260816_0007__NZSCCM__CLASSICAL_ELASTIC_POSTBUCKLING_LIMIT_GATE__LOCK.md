# NZ-SCCM — Classical elastic thin-plate postbuckling limit gate

**Timestamp:** 2026-08-16 00:07 +08:00

## Locked purpose

Before any new nonlinear-material Z6 Pu calculation, the membrane-redistribution closure must recover a canonical classical Kármán/FvK postbuckling branch using **zero spatial numerical integration**.

## Frozen project boundary

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order geometric source retained
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
Gauss/Simpson/adaptive/collocation/cells/material-point-grid = PROHIBITED
```

The retracted 23:43 Gauss-based AR2 path remains historical error evidence only.

## Gate benchmark

Use a canonical isotropic elastic plate, one complete sinusoidal halfwave,

w0=A0 sin(alpha x) sin(beta y),
wa=A  sin(alpha x) sin(beta y),
alpha=pi/b, beta=pi/ell.

The benchmark is a Navier/Galerkin FvK limit case with the mean axial compression represented by the homogeneous Airy term and the nonlinear membrane redistribution represented by the compatibility-generated Airy harmonics. It is a **classical-limit sign/closure benchmark**, not yet the final Zhou in-plane boundary-value problem.

## Mandatory pass conditions

1. The incremental compatibility source must be derived exactly from `(w0+wa)` relative to `w0`.
2. Airy harmonic amplitudes must be determined by the compatibility equation, not introduced as independent generalized coordinates.
3. The Galerkin moments must be evaluated analytically.
4. The resulting postbuckling load must contain a positive membrane contribution proportional to `A^2+2 A0 A`.
5. For a perfect square representative halfwave, the classical branch must reduce to

   sigma/sigma_cr = 1 + 3(1-nu^2)/8 * (A/t)^2.

6. The axial membrane stress must redistribute from the plate center toward the longitudinal edges.

## Governance consequence

If the gate passes, the previous independent-coordinate interpretation

```text
p20,p02 as two freely relaxing membrane coordinates
```

is retired. The harmonic labels `(2,0)` and `(0,2)` remain valid bookkeeping labels, but their amplitudes must be compatibility/equilibrium-derived or obtained from an equivalent proven displacement closure.

No nonlinear-material Z6 Pu continuation is allowed until the boundary-specific membrane closure is rebuilt from this classical foundation.
