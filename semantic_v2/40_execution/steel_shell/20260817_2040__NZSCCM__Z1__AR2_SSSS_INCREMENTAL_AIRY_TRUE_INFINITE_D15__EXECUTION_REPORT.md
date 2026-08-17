# NZ-SCCM Z1 — independent AR2/SSSS calculation

**Identity:** SINGLE-SPECIMEN INDEPENDENT EXECUTION  
**Membrane closure:** `R_A^Delta=R_A(D,q,alpha)-R_A(D,0,0)=0`

Z1 was initialized independently at `D=0,q=0,alpha=0`. No Z0/Z2–Z5 root, state, series prefix, internal variable or comparator was imported.

## Input

```text
b=6000 mm, a=12000 mm, ell=6000 mm, m*=2, SSSS
A0=24 mm, q0=0.004
tc=92 mm, ts=4 mm each face, h=100 mm
fc=30.4 MPa, E0=32500 MPa, eps0=0.0018712490394580678, nu_c=0.18
Es=206000 MPa, fy=235 MPa, nu_s=0.30, rho_w=0.02
```

All phases enter `P,Rq,R_A^Delta` before solve. Formal evaluation remains finite-current -> true-infinite representation -> exact CH -> General-D15 -> infinite sum. Direct-continuum values below are decimal-localization/convergence audits only.

## Membrane OFF — independent origin-to-limit solve

```text
D_u = 0.5939452076
q_u = 0.003204740061
M_u = 0.09469624416
Pc = 6.36270446 MN
Pface = 10.55882825 MN
Pw = 2.40703640 MN
Pu_OFF = 19.32856911 MN
max trial VM/fy = 1.17963
```

Neighboring equilibrated states bracket the first maximum.

## Membrane ON — separate independent origin-to-limit solve

Low-load branch check:

```text
D=0.01: alpha/M=0.999320
D=0.02: alpha/M=0.983646
D=0.03: alpha/M=0.967314
```

First reachable limit:

```text
D_u = 0.5820414604
q_u = 0.004873166767
M_u = 0.1654378314
alpha_u = 0.1317481353
lambda_A = 0.7963603861
Pc = 8.51817908 MN
Pface = 10.02451724 MN
Pw = 2.28604053 MN
Pu_ON = 20.82873685 MN
Rq = -1.01e-6 N mm
RA_delta = 1.86e-9 N mm
max trial VM/fy = 1.19533
```

Neighboring equilibrated values:

```text
D=0.581: P=20.82858657 MN
D=0.583: P=20.82858157 MN
```

## Independent decimal convergence audit at localized D

OFF:

```text
nxy 24: 19.324565 MN
nxy 32: 19.328569 MN
nxy 40: 19.331637 MN
nxy 48: 19.332370 MN
```

ON:

```text
nxy 24: 20.868042 MN, alpha/M=0.802642
nxy 32: 20.828737 MN, alpha/M=0.796360
nxy 40: 20.816067 MN, alpha/M=0.793857
nxy 48: 20.813187 MN, alpha/M=0.793148
```

The last two audit loads differ by ~0.00288 MN (~0.014%) at the fixed localized D.

## Same-object membrane increment

Using the independent primary OFF/ON branches:

```text
Delta P_mem ~= +1.50017 MN
Delta P_mem / Pu_OFF ~= +7.76%
```

This value is frozen only as the Z1 calculation outcome; it is not inferred from other Z cases or comparator envelopes.

## Historical pre-membrane provenance

The GitHub H0 `SAME_D_RQ_LOCATED_DIAGNOSTIC` gave Z1 approximately `24.8777 MN` at its then-frozen old D, versus Zhou `23.7214 MN`. H0 explicitly states that this was not a new equilibrated ultimate-load result. It is retained as historical pre-membrane provenance only, not as the target for this calculation.

```text
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
N_formal_thickness_quadrature=0
```
