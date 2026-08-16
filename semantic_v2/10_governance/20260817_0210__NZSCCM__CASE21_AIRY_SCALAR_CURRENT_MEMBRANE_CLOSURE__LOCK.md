# NZ-SCCM governance — Case21 Airy-scalar current membrane closure

**Timestamp:** 2026-08-17 02:10 +08:00

## Decision

The five compatible membrane functions remain the exact elastic Airy/FvK span, but they are no longer released as five independent nonlinear current amplitudes for Case21 production development.

The active Case21 membrane closure is

\[
\boxed{r=\lambda M a(\nu)}
\]

with

\[
M=\frac{\pi^2}{\varepsilon_0}\left(q_0q+\frac12q^2\right),
\]

\[
a(\nu)=\left[-\frac{1+\nu}{4},-\frac{1-\nu}{4},\frac14,-\frac{1-\nu}{4},\frac14\right]^T.
\]

`lambda` is an internal current-material generalized coordinate determined by

\[
R_A=a^T R_m=0.
\]

The outer path is determined jointly by

\[
R_q=0,\qquad R_A=0.
\]

## Why this supersedes five-free Rm=0

The unconstrained five-coordinate nonlinear release is known to rotate strongly away from the exact Airy direction under frozen R10 softening and to enter large-amplitude internal relaxation states that are incompatible with the small Case21 membrane driver.

This is a mechanics failure, not an integration-accuracy failure. Increasing CAS precision or changing the exact integration backend cannot repair it.

The Airy-scalar closure retains the exact classical compatible shape and permits only its current-material amplitude to evolve.

## Elastic benchmark

For linear elastic plane stress the scalar generalized equilibrium gives exactly

```text
lambda = 1
```

and reproduces the classical complete-halfwave FvK/Airy membrane field and positive postbuckling branch.

## Current R10 Case21 direct-source result

The direct frozen-R10 continuum audit gives a smooth first peak near

```text
D = 0.78879
q = 0.00180836
lambda = 0.08624
Pc = 337.9230 kN
Ps = 28.8448 kN
Pu = 366.7678 kN
experiment = 368.31275 kN
error = -0.4195 %
```

Steel remains elastic.

This direct-source result is the current mechanics target for the formal zero-spatial-integration implementation. It is not calibrated to the experiment.

## Formal integration boundary

The formal counters remain

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

The high-order Gauss-Legendre calculation used to establish the direct-source result is audit-only and does not become the formal production operator.

The exact R10 source DAG, General-D15 target philosophy, one continuous complete halfwave, reinforcement-before-solve rule and Z6 four-edge simply-supported boundary remain unchanged.

## Locked identities

```text
CASE21_FIVE_FREE_CURRENT_MEMBRANE_AMPLITUDES = SUPERSEDED
CASE21_AIRY_SCALAR_CURRENT_MEMBRANE_CLOSURE = ACTIVE
CASE21_DIRECT_SOURCE_MECHANICS_TARGET_Pu = 366.768 kN
EXPERIMENTAL_CALIBRATION = PROHIBITED / NOT USED
FORMAL_ZERO_QUADRATURE_NUMERIC_RELEASE = OPEN
Z6_BOUNDARY = FOUR_EDGE_SIMPLY_SUPPORTED_SSSS
```
