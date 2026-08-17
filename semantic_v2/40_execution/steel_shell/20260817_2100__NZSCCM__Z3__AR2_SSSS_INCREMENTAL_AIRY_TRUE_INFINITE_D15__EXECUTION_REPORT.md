# NZ-SCCM Z3 — independent AR2/SSSS calculation

**Identity:** SINGLE-SPECIMEN INDEPENDENT EXECUTION. Z3 starts from its own `D=q=alpha=0` state; no other specimen numerical state is reused.

## Input

```text
b=6000 mm, a=12000 mm, ell=6000 mm, m*=2, SSSS
A0=24 mm, q0=0.004
tc=122 mm, ts=4 mm each face, h=130 mm
fc=45.6 MPa, E0=35992.80144 MPa, eps0=0.0025344898708809867, nu_c=0.18
Es=206000 MPa, fy=355 MPa, nu_s=0.30, rho_w=0.02
```

The formal chain remains finite-current -> true-infinite analytic representation -> exact CH -> General-D15 -> infinite target sum. Decimal direct-continuum evaluations are audit-only.

## Membrane OFF — fresh solve

```text
D_u=0.6585474415
q_u=0.002406851278
M_u=0.04876944280
Pc=17.19642888 MN
Pface=16.58529439 MN
Pw=4.92207578 MN
Pu_OFF=38.70379905 MN
max trial VM/fy=1.08901
```

## Membrane ON — separate fresh solve

Low-load branch:

```text
D=0.01: alpha/M=0.995324
D=0.02: alpha/M=0.972644
D=0.03: alpha/M=0.948371
```

First reachable limit:

```text
D_u=0.6635029587
q_u=0.003262240010
M_u=0.07153521356
alpha_u=0.04071792758
lambda_A=0.5692011746
Pc=18.97223900 MN
Pface=16.48322927 MN
Pw=4.90456806 MN
Pu_ON=40.36003633 MN
Rq=-1.55e-6 N mm
RA_delta=4.10e-8 N mm
max trial VM/fy=1.12396
```

## Independent decimal convergence audit at localized D

OFF:

```text
nxy24 38.693914 MN
nxy32 38.703799 MN
nxy40 38.705338 MN
nxy48 38.706025 MN
```

ON:

```text
nxy24 40.313556 MN, alpha/M=0.558300
nxy32 40.360036 MN, alpha/M=0.569201
nxy40 40.365344 MN, alpha/M=0.569959
nxy48 40.362366 MN, alpha/M=0.569651
```

The last two ON audit values differ by ~0.0030 MN (~0.007%).

## Same-object membrane increment

```text
Delta P_mem ~= +1.65624 MN
Delta P_mem/Pu_OFF ~= +4.28%
```

No comparator is used in the solve.

## Historical pre-membrane provenance

The GitHub H0 same-D diagnostic stored ~49.4964 MN for Z3 at its historical old D, versus Zhou ~44.3203 MN. H0 explicitly did not claim that value as a newly re-solved ultimate load; it is provenance only.

```text
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
N_formal_thickness_quadrature=0
```
