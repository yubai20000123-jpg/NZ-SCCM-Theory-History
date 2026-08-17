# NZ-SCCM Z4 — independent AR2/SSSS calculation

**Identity:** SINGLE-SPECIMEN INDEPENDENT EXECUTION. Z4 is initialized from its own raw input and origin state; no Z0–Z3/Z5 numerical state is reused.

## Input

```text
b=8000 mm, a=16000 mm, ell=8000 mm, m*=2, SSSS
A0=32 mm, q0=0.004
tc=192 mm, ts=4 mm each face, h=200 mm
fc=30.4 MPa, E0=32500 MPa, eps0=0.0018712490394580678, nu_c=0.18
Es=206000 MPa, fy=355 MPa, nu_s=0.30, rho_w=0.02
```

Formal target remains finite-current -> true-infinite representation -> exact CH -> General-D15 -> infinite target sum. Direct-continuum values are audit-only decimal localization.

## Membrane OFF — fresh solve

The connected OFF branch was followed from the origin through its first reachable maximum. Later post-peak continuation failure is irrelevant to the already bracketed first maximum and is not used to switch roots.

```text
D_u=0.9065170837
q_u=0.001300622089
M_u=0.03190077859
Pc=29.72498103 MN
Pface=22.87275570 MN
Pw=10.60724737 MN
Pu_OFF=63.20498410 MN
max trial VM/fy=1.04911
```

## Membrane ON — separate fresh solve

Low-load branch:

```text
D=0.01: alpha/M=0.992272
D=0.02: alpha/M=0.963779
D=0.03: alpha/M=0.932851
```

The first reachable maximum is obtained before the later post-peak continuation failure:

```text
D_u=0.9177226716
q_u=0.001403182997
M_u=0.03479584286
alpha_u=0.004739862166
lambda_A=0.1362192083
Pc=29.95661850 MN
Pface=23.06325243 MN
Pw=10.70096609 MN
Pu_ON=63.72083702 MN
Rq=-1.67e-6 N mm
RA_delta=3.73e-9 N mm
max trial VM/fy=1.06578
```

Neighboring equilibrated states (`D≈0.917` and `0.919`) are both lower than the localized peak.

## Independent decimal convergence audit at localized D

OFF:

```text
nxy24 63.216390 MN
nxy32 63.204984 MN
nxy40 63.206775 MN
nxy48 63.208409 MN
```

ON:

```text
nxy24 63.717532 MN, alpha/M=0.135155
nxy32 63.720837 MN, alpha/M=0.136219
nxy40 63.730087 MN, alpha/M=0.137539
nxy48 63.733004 MN, alpha/M=0.138394
```

The last two ON audit loads differ by ~0.0029 MN (~0.005%).

## Same-object membrane increment

```text
Delta P_mem ~= +0.51585 MN
Delta P_mem/Pu_OFF ~= +0.82%
```

This result is recorded as calculated, not adjusted to the prior expectation that Z4 should necessarily exhibit the largest membrane delta.

## Historical pre-membrane provenance

The GitHub H0 same-D diagnostic stored ~77.2971 MN for Z4 at its historical old D, versus the then-used Zhou value ~70.1873 MN. H0 explicitly states this was a same-D branch locator, not a newly solved Pu; it is not used as a target.

```text
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
N_formal_thickness_quadrature=0
```
