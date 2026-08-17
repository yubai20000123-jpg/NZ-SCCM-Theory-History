# NZ-SCCM Z5 — independent AR2/SSSS calculation

**Identity:** SINGLE-SPECIMEN INDEPENDENT EXECUTION. Z5 starts from its own input and origin state; no other specimen state is reused.

## Input

```text
b=2000 mm, a=4000 mm, ell=2000 mm, m*=2, SSSS
A0=8 mm, q0=0.004
tc=122 mm, ts=4 mm each face, h=130 mm
fc=30.4 MPa, E0=32500 MPa, eps0=0.0018712490394580678, nu_c=0.18
Es=206000 MPa, fy=355 MPa, nu_s=0.30, rho_w=0.02
```

Formal target remains true-infinite analytic current representation + exact CH + General-D15. Direct-continuum evaluations are decimal-localization audits only.

## Membrane OFF — fresh solve

```text
D_u=0.9470490639
q_u=0.0001782931013
M_u=0.003845345526
Pc=6.59353300 MN
Pface=6.00136029 MN
Pw=1.73239768 MN
Pu_OFF=14.32729097 MN
max trial VM/fy=1.03690
```

## Membrane ON — separate fresh solve

The zero-driver branch is regular and does not show the former `lambda_A~-13` pathology:

```text
D=0.01: alpha/M=0.994045
D=0.02: alpha/M=0.957764
D=0.03: alpha/M=0.905234
```

The same connected branch later crosses `alpha=0`; this is not a root jump because `alpha` itself remains continuous and tends to zero with the geometric driver at the origin.

First reachable limit:

```text
D_u=0.9389323273
q_u=0.0001626758202
M_u=0.003501819149
alpha_u=-0.008201133539
lambda_A=-2.341963759
Pc=6.36786753 MN
Pface=5.97797708 MN
Pw=1.73236665 MN
Pu_ON=14.07821126 MN
Rq=-1.56e-7 N mm
RA_delta=1.16e-10 N mm
max trial VM/fy=1.02944
```

Unlike the retracted total-RA run, `lambda_A` is finite and `alpha->0` at zero driver; therefore the zero-driver gate is satisfied.

## Independent decimal convergence audit at localized D

OFF:

```text
nxy24 14.325617 MN
nxy32 14.327291 MN
nxy40 14.327889 MN
nxy48 14.328131 MN
```

ON:

```text
nxy24 14.076673 MN, alpha/M=-2.349859
nxy32 14.078211 MN, alpha/M=-2.341964
nxy40 14.078498 MN, alpha/M=-2.340961
nxy48 14.078475 MN, alpha/M=-2.341230
```

Last two ON audit values differ by about 0.000023 MN.

## Same-object membrane increment

```text
Delta P_mem ~= -0.24908 MN
Delta P_mem/Pu_OFF ~= -1.74%
```

No comparator is used for root selection.

## Historical pre-membrane provenance

The GitHub H0 same-D diagnostic stored ~14.9633 MN for Z5 at its historical old D, versus Zhou/Winter ~14.68165 MN. H0 explicitly identified this as a same-D branch-location diagnostic rather than a newly solved Pu; it is not used as a target.

```text
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
N_formal_thickness_quadrature=0
```
