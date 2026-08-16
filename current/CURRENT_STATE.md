# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-17 02:10 +08:00  
**Status:** LEGACY MUTABLE POINTER ONLY

## Current controlling governance

`semantic_v2/10_governance/20260817_0210__NZSCCM__CASE21_AIRY_SCALAR_CURRENT_MEMBRANE_CLOSURE__LOCK.md`

## Frozen backbone

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
Nguyen second-order continuous kinematics = ACTIVE
R10 physical current operator = FROZEN
reinforcement before coupled solve = REQUIRED
General-D15 target philosophy = ACTIVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
Z6_BOUNDARY = FOUR_EDGE_SIMPLY_SUPPORTED / SSSS
```

Formal infinite/high-order analytic representations remain allowed. Direct production computation by enumerating thousands of analytic coefficients remains prohibited.

## Mechanics correction completed at 02:10

The five compatible membrane functions remain the exact elastic Airy/FvK span, but the five amplitudes are no longer released independently in the nonlinear Case21 current-material problem.

The active Case21 membrane closure is

```text
r = lambda * M * a(nu)
M = pi^2/eps0 * (q0*q + 0.5*q^2)
a(nu) = [-(1+nu)/4, -(1-nu)/4, +1/4, -(1-nu)/4, +1/4]
```

with the internal current-material scalar equilibrium

```text
RA = a^T Rm = 0
```

and the outer path equation

```text
Rq = 0.
```

For linear elasticity this closure gives exactly `lambda=1` and reproduces the classical complete-halfwave Airy/FvK solution.

The unconstrained five-free-coordinate `Rm=0` route is superseded for Case21 nonlinear production because direct frozen-R10 continuation drives it far away from the Airy direction into large nonlinear relaxation states. This is a mechanics failure rather than an integration-accuracy problem.

## Current actual Case21 result

A direct frozen-R10 continuum audit was continued on the origin-connected `(Rq=0,RA=0)` branch and independently refined through `144 x 144 x 76` Gauss-Legendre audit grids.

Representative peak state:

```text
D = 0.78879248
q = 0.0018083573
lambda = 0.08623596
M = 0.02907033478
A_increment = 2.20620 mm
A_total = 5.25620 mm

r = [-0.00073954,
     -0.00051392,
     +0.00062673,
     -0.00051392,
     +0.00062673]

Pc = 337.923030 kN
Ps =  28.844798 kN
Pu = 366.767829 kN
```

Same-state equilibrium audit:

```text
Rq ~= 6.3e-13 kN mm
RA ~= 3.6e-15
```

Steel remains elastic:

```text
ex_s in [+0.00029496,+0.00035355]
ey_s in [-0.00164881,-0.00159022]
|eps_s| < 0.00265
```

Experiment:

```text
P_exp = 368.312750 kN
error = -0.41946 %
```

Direct frozen-R10 constrained `r=0` comparison:

```text
P_r0 ~= 368.731457 kN
Airy-scalar redistribution delta ~= -1.96363 kN = -0.53254 %
```

The correction is therefore small for Case21. The sign is slightly capacity-reducing relative to the old constrained `r=0` backbone; this does not contradict the positive classical membrane postbuckling term, which is defined relative to the elastic buckling load rather than relative to the over-constrained `r=0` kinematics.

## Formal exact-integration status

The direct-source numerical result above is the current mechanics target; its Gauss-Legendre executor is audit-only.

The exact integration work already established and retained:

```text
old rationalized c0,c1 apparent pole = representation artifact
source-level matrix sqrt + Frechet/Sylvester = retained
64-state = valid global branch-free algebraic closure bound
8-state = valid fixed-event-topology local exact bound
fixed-endpoint global positive-part / factorised period = retained production representation
```

The remaining formal production task is now narrower because the structural state is `(D,q,lambda)` rather than `(D,q,r1..r5)`.

No new material fit or experimental calibration is authorized.

## Capacity status

```text
CASE21_CURRENT_DIRECT_SOURCE_MECHANICS_TARGET_Pu = 366.768 kN
CASE21_FORMAL_ZERO_QUADRATURE_NUMERIC_RELEASE = OPEN
CASE21_EXPERIMENT_ERROR = -0.4195 %
Z6_NEW_CALCULATION = NOT YET RUN UNDER THIS CLOSURE
```

## Current artifacts

- `semantic_v2/40_execution/common/20260817_0210__NZSCCM__CASE21_AIRY_SCALAR_CURRENT_R10_CONTINUATION__EXECUTION_REPORT.md`
- `semantic_v2/40_execution/common/20260817_0210__NZSCCM__CASE21_AIRY_SCALAR_CURRENT_R10_CONTINUATION__PARAMS_AND_RESULTS.json`
- `semantic_v2/40_execution/common/20260817_0210__NZSCCM__CASE21_AIRY_SCALAR_CURRENT_R10_CONTINUATION__REPRO.py`
- `semantic_v2/10_governance/20260817_0210__NZSCCM__CASE21_AIRY_SCALAR_CURRENT_MEMBRANE_CLOSURE__LOCK.md`
