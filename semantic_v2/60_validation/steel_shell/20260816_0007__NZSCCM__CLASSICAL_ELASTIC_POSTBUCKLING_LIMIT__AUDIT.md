# NZ-SCCM — Classical elastic postbuckling limit audit

**Timestamp:** 2026-08-16 00:07 +08:00

## Source cross-check

Yun Lu's thesis derives a Kármán large-deflection Airy stress function from the deformation-compatibility equation (thesis Eq. 2-23 through 2-27) and then obtains the postbuckling relation Eq. (2-32):

`p_x = [k_crx A/(A+A0) + k_p(1-nu^2)(2A0A+A^2)/t^2] * pi^2 D/(t b^2)`.

The thesis explicitly interprets `k_p` as the contribution coefficient of membrane stress to postbuckling strength and reports positive values; for integer aspect ratio its unilateral/clamped model gives `k_p=42.64`.

The present canonical simply-supported benchmark independently reproduces the same algebraic structure from the FvK equations with exact analytical moments.

## Exact benchmark result

For

`w0=A0 sin(alpha x) sin(beta y)`,
`wa=A sin(alpha x) sin(beta y)`,

compatibility gives the coupled Airy harmonics

`C20=E t S beta^2/(32 alpha^2)`,
`C02=E t S alpha^2/(32 beta^2)`,

where `S=A^2+2A0A`.

Exact Galerkin integration gives

`N=Ncr*A/(A+A0)+E t S/16*(beta^2+alpha^4/beta^2)`.

For `ell=b` and `A0=0`,

`sigma/sigma_cr = 1 + 3(1-nu^2)/8*(A/t)^2`.

Therefore the canonical elastic postbuckling branch is stable and increasing.

## Stress-redistribution sign

Compression-positive axial membrane resultant is

`n_y(x)=N+E t S beta^2/8*cos(2 alpha x)`.

Thus

- longitudinal edges `x=0,b`: compression increases;
- plate center `x=b/2`: compression decreases;
- the width average remains `N`.

This is the required classical edgeward stress redistribution.

## Numerical sanity example — analytical formula only

For a square steel plate with `E=206000 MPa`, `nu=.30`, `b/t=100`:

`sigma_cr=74.47393797 MPa`.

Using the exact closed-form branch:

| A/t | sigma/sigma_cr | sigma MPa |
|---:|---:|---:|
|0.0|1.0000000|74.47394|
|0.5|1.0853125|80.82750|
|1.0|1.3412500|99.88817|
|1.5|1.7678125|131.65596|
|2.0|2.3650000|176.13086|

No spatial points or numerical quadrature were used to obtain these values.

## Decision

```text
CLASSICAL_ELASTIC_THIN_PLATE_POSTBUCKLING_LIMIT_GATE = PASS
POSITIVE_MEMBRANE_POSTBUCKLING_BRANCH = RECOVERED
EDGEWARD_AXIAL_STRESS_REDISTRIBUTION = RECOVERED
ZERO_SPATIAL_NUMERICAL_INTEGRATION = PASS
```

At the same time:

```text
p20,p02 AS TWO INDEPENDENT FREE MEMBRANE COORDINATES = RETIRED
```

Their `(2,0)` and `(0,2)` harmonic identities remain correct, but the classical FvK solution proves that their amplitudes are compatibility/equilibrium-coupled through the single nonlinear source `S`, rather than freely minimizing the energy as two unrelated coordinates.

## Remaining limitation / next gate

This benchmark uses a canonical Navier/Galerkin in-plane boundary class. It is not yet the exact Zhou Z6 in-plane boundary-value problem (`u_x=0` at loaded ends with lateral sides free).

Therefore nonlinear-material Z6 Pu remains blocked until the same Airy/compatibility construction is made boundary-admissible for the actual Z6 loaded/free edge conditions while retaining exact analytical moments and zero spatial numerical integration.

Mandatory next gate:

`ZHOU_Z6_BOUNDARY_ADMISSIBLE_CLASSICAL_FVK_AIRY_CLOSURE_ZERO_QUADRATURE`
