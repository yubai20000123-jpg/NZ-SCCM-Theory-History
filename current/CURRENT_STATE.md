# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-17 11:05 +08:00  
**Status:** LEGACY MUTABLE POINTER ONLY

## Current operational entry

`semantic_v2/00_index/20260817_1105__NZSCCM__PROJECT__CURRENT_STATE_CASE21_AIRY_SCALAR_QUALIFIED__SEMANTIC_INDEX.md`

## Current controlling governance

`semantic_v2/10_governance/20260817_1105__NZSCCM__CASE21_AIRY_SCALAR_MECHANICS_QUALIFICATION_AND_LOAD_IDENTITY__LOCK.md`

## Frozen backbone

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
Nguyen second-order continuous kinematics = ACTIVE
R10 physical current operator = FROZEN
reinforcement before coupled solve = REQUIRED
General-D15 / target-first exact-moment philosophy = ACTIVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
formal Gauss/Simpson/adaptive/cells/material-point-grid = PROHIBITED
high-order coefficient enumeration as production architecture = PROHIBITED
experimental calibration/root selection = PROHIBITED
Z6_BOUNDARY = FOUR_EDGE_SIMPLY_SUPPORTED / SSSS
```

Gauss-Legendre remains allowed only as an independent audit/oracle backend and never becomes the formal production operator.

## Case21 load identity — hard locked

```text
experimental buckling load:
Pcr_exp = 75.6 kip = 336.285554 kN

experimental failure / ultimate load:
Pf_exp  = 82.8 kip = 368.312750 kN

Nguyen FE buckling comparator = 298 kN
```

Therefore:

```text
Pcr calculations compare only with 336.285554 kN
Pu calculations compare only with 368.312750 kN
cross-comparison is prohibited
```

## Active Case21 membrane closure

The five compatible membrane functions retain their exact classical Airy/FvK span, but the five amplitudes are not released independently in the nonlinear current-material problem.

The active retained subspace is

```text
r = lambda * M * a(nu)
M = pi^2/eps0 * (q0*q + 0.5*q^2)
a(nu) = [-(1+nu)/4, -(1-nu)/4, +1/4, -(1-nu)/4, +1/4]
```

with

```text
RA = a^T Rm = 0
Rq_base = 0
```

The five-free nonlinear `Rm=0` route remains rejected because it can rotate far away from the Airy direction and enter large nonphysical relaxation states.

## 11:05 mechanics qualification

The scalar-coordinate virtual-work transformation is exact:

```text
R_lambda = M*RA
Rq_restricted = Rq_base + lambda*Mq*RA
```

Thus `(Rq_base=0, RA=0)` is exactly row-equivalent to restricted `(q,lambda)` equilibrium for active `M>0`.

### Elastic benchmark scope correction

For a single isotropic plane-stress continuum:

```text
lambda = 1 exactly
```

and the classical complete-halfwave Airy/FvK stress redistribution is recovered.

With reinforcement included before the solve, the actual linear RC scalar benchmark is instead

```text
lambda_lin_RC = 0.999266844854884
              + 0.0096124785693025 * D/M
```

for the current Case21 reinforcement/material data. Therefore `lambda!=1` in the reinforced composite is not itself a mechanics failure.

### Scalar internal stability

Inherited active-state criterion:

```text
dRA/dlambda > 0
K_lambda_lambda = M*dRA/dlambda > 0
```

Direct frozen-R10 audit remains positive along the origin-connected branch through the present peak.

At the `144 x 144 x 76` audit peak state:

```text
D = 0.7887924801
q = 0.0018083573
lambda = 0.0862359635
M = 0.02907033478
Pu = 366.76782869 kN

dRA/dlambda = +25.24850924
M*dRA/dlambda = +0.733982616
```

No scalar internal membrane instability is found before the current load peak.

## Current Case21 mechanics target

```text
D = 0.7887924801
q = 0.0018083573
lambda = 0.0862359635
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
Pf_exp = 368.312750 kN
error = -0.419459 %
```

The direct-source result remains an audit/mechanics oracle; no experimental load was used to choose `lambda`, R10 parameters, or the peak.

Relative to the same direct-R10 constrained `r=0` backbone:

```text
Pu_r0 = 368.731457 kN
Airy-scalar delta = -1.96363 kN = -0.53254 %
```

This remains a small correction for the Case21 membrane-driver scale.

## Formal operator preparation completed

The reinforcement is elastic at the current Case21 peak and its `P,RA,Rq` contribution is now available in exact closed form.

The concrete value-level structural target is reduced to the direct 12-functional package

```text
T12 =
Jx00, Jx20, Jx02, Jx22c,
Jy00, Jy20, Jy02, Jy22c,
Jxy22s,
Jx11s_1, Jy11s_1, Jxy11c_1
```

which feeds exactly

```text
Pc
RAc
Rqc
```

without reconstructing a full stress surface.

Finite thickness-order contract:

```text
stress moments  : k = 0,1
tangent kernels : k = 0,1,2
```

Production thickness representation remains

```text
GLOBAL_FIXED_ENDPOINT_POSITIVE_PART_FACTORISED_PERIOD
```

using the source-regular R10 matrix DAG / Frechet-Sylvester rules / 2x2 Cayley-Hamilton / target-side contraction.

## Capacity status

```text
CASE21_CURRENT_DIRECT_SOURCE_MECHANICS_TARGET_Pu = 366.767829 kN
CASE21_FORMAL_ZERO_QUADRATURE_NUMERIC_RELEASE = OPEN
CASE21_Pf_EXP = 368.312750 kN
CASE21_CURRENT_MECHANICS_ERROR = -0.419459 %
CASE21_SCALAR_INTERNAL_STABILITY_TO_PEAK = PASS_AUDIT
Z6_NEW_CALCULATION_UNDER_CURRENT_CLOSURE = NOT YET RUN
```

## Unique next gate

```text
CASE21_AIRY_SCALAR_FORMAL_T12_FIXED_ENDPOINT_DESCRIPTOR_GATE
```

No parallel route and no new Pu before this descriptor and its same-source `(D,q,lambda)` derivative package pass.

## Current artifacts

- `current/case21/CASE21_AIRY_SCALAR_MECHANICS_QUALIFICATION_20260817.md`
- `semantic_v2/10_governance/20260817_1105__NZSCCM__CASE21_AIRY_SCALAR_MECHANICS_QUALIFICATION_AND_LOAD_IDENTITY__LOCK.md`
- `semantic_v2/20_theory/nc_rebar_panel/20260817_1105__NZSCCM__CASE21_AIRY_SCALAR_MECHANICS_QUALIFICATION_AND_T12_OPERATOR_CONTRACT__THEORY.md`
- `semantic_v2/40_execution/common/20260817_1105__NZSCCM__CASE21_AIRY_SCALAR_MECHANICS_QUALIFICATION__EXECUTION_REPORT.md`
- `semantic_v2/40_execution/common/20260817_1105__NZSCCM__CASE21_AIRY_SCALAR_MECHANICS_QUALIFICATION__PARAMS_AND_INTERMEDIATES.json`
- `semantic_v2/40_execution/common/20260817_1105__NZSCCM__CASE21_AIRY_SCALAR_MECHANICS_QUALIFICATION__REPRO.py`
- `semantic_v2/00_index/20260817_1105__NZSCCM__PROJECT__CURRENT_STATE_CASE21_AIRY_SCALAR_QUALIFIED__SEMANTIC_INDEX.md`
