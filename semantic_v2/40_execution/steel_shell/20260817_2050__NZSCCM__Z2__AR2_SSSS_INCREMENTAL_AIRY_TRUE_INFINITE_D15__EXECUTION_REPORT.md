# NZ-SCCM Z2 — independent AR2/SSSS calculation

**Identity:** SINGLE-SPECIMEN INDEPENDENT EXECUTION  
**Membrane closure:** incremental `R_A^Delta=0` with exact zero-driver degeneration.

Z2 is initialized from its own raw input at `D=q=alpha=0`; no Z0/Z1/Z3–Z5 numerical state is reused.

## Input

```text
b=6000 mm, a=12000 mm, ell=6000 mm, m*=2, SSSS
A0=24 mm, q0=0.004
tc=122 mm, ts=4 mm each face, h=130 mm
fc=30.4 MPa, E0=32500 MPa, eps0=0.0018712490394580678, nu_c=0.18
Es=206000 MPa, fy=460 MPa, nu_s=0.30, rho_w=0.02
```

Concrete, both faceplates and homogenized longitudinal web steel all enter `P,Rq,R_A^Delta` before solve. Formal integration remains true-infinite CH/D15; displayed direct-continuum values are decimal-localization audits only.

## Membrane OFF — fresh independent solve

```text
D_u=1.1131281628
q_u=0.003906063091
M_u=0.1226437984
Pc=9.13663634 MN
Pface=20.46564494 MN
Pw=6.09563743 MN
Pu_OFF=35.69791871 MN
max trial VM/fy=1.09330
```

## Membrane ON — separate fresh solve

Low-load branch:

```text
D=0.01: alpha/M=0.996203
D=0.02: alpha/M=0.974189
D=0.03: alpha/M=0.950401
```

First reachable limit:

```text
D_u=1.0748424210
q_u=0.006478838773
M_u=0.2473825512
alpha_u=0.1939709231
lambda_A=0.7840929852
Pc=12.98951719 MN
Pface=19.17657610 MN
Pw=5.70596427 MN
Pu_ON=37.87205756 MN
Rq=-3.58e-7 N mm
RA_delta=-3.73e-9 N mm
max trial VM/fy=1.12295
```

Neighboring equilibrated points bracket the maximum (`D≈1.074` and `1.076`).

## Independent decimal convergence audit at localized D

OFF:

```text
nxy24 35.711483 MN
nxy32 35.697919 MN
nxy40 35.699355 MN
nxy48 35.701848 MN
```

ON:

```text
nxy24 37.939215 MN, alpha/M=0.791819
nxy32 37.872058 MN, alpha/M=0.784093
nxy40 37.824326 MN, alpha/M=0.778205
nxy48 37.808156 MN, alpha/M=0.775866
```

Last two ON audit loads differ by ~0.0162 MN (~0.043%) at the fixed localized D.

## Same-object membrane increment

```text
Delta P_mem ~= +2.17414 MN
Delta P_mem/Pu_OFF ~= +6.09%
```

No Zhou/Winter value entered the solve.

## Historical pre-membrane provenance

The earlier H0 `SAME_D_RQ_LOCATED_DIAGNOSTIC` stored ~44.9368 MN for Z2 at its then-frozen old D, versus Zhou ~41.2134 MN. H0 explicitly labels that number a same-D branch-location diagnostic, not an independently re-solved ultimate load; it is not used as a target here.

```text
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
N_formal_thickness_quadrature=0
```
