# NZ-SCCM Z1 — R15 zero-discretization execution audit and ledger correction

**Date:** 2026-08-19
**Purpose:** execute Z1 from raw inputs under R15, without spatial discretization, and determine whether R15 is actually a self-contained executable calculation ledger rather than only a complete theory specification.

## 0. Rules used

```text
spatial quadrature = 0
spatial sampling = 0
material points = 0
finite material prefix = 0
discrete oracle = 0
```

No historical Z1 nonlinear root, Pu, Zhou or Winter comparator was used in the front-end calculation or as a solve seed.

## 1. Z1 raw input

```text
a_phys = 12000 mm
b      = 6000 mm
tc     = 92 mm
ts     = 4 mm each face
rho_w  = 0.02
fc     = 30.4 MPa
eps0   = 0.0018712490394580678
kappa  = 2.0005129533678754
nu_c_R10 = 0.18
Es     = 206000 MPa
fy     = 235 MPa
nu_s_face = 0.30
mu_s_Z_shell = 0.30
mu_c_Z_shell = 0.20
A0     = a_phys/500 = 24 mm
q0     = 0.004
```

The Z1 raw data are inherited from the Z0–Z5 AR2/SSSS specimen table; historical nonlinear results were kept sealed during this execution attempt.

## 2. R15 front-end calculation from raw geometry

Initial concrete modulus:

\[
E_c^0=\kappa f_c/\varepsilon_0
=32499.99999999797\ \mathrm{MPa}\approx32500\ \mathrm{MPa}.
\]

Total depth and face centroid:

\[
h=t_c+2t_s=100\ \mathrm{mm},\qquad
z_f=t_c/2+t_s/2=48\ \mathrm{mm}.
\]

Face and core inertias:

\[
I_f=2b\left(t_s^3/12+t_sz_f^2\right)
=110656000\ \mathrm{mm^4},
\]

\[
I_c=bt_c^3/12=389344000\ \mathrm{mm^4}.
\]

Bending stiffnesses:

\[
D_x=(E_sI_f+E_c^0I_c)/b
=5.90813599999987\times10^9\ \mathrm{Nmm},
\]

\[
D_{y,s}=(E_sI_f+\rho_wE_sI_c)/b
=4.06653888000000\times10^9\ \mathrm{Nmm},
\]

\[
D_{y,c}=(1-\rho_w)E_c^0I_c/b
=2.06676773333320\times10^9\ \mathrm{Nmm},
\]

\[
\boxed{D_y=6.13330661333320\times10^9\ \mathrm{Nmm}}.
\]

Shear moduli:

\[
G_s^Z=79230.7692307692\ \mathrm{MPa},
\qquad
G_c^Z=13541.6666666658\ \mathrm{MPa}.
\]

Closed steel box quantities:

\[
A_\Box=(b-t_s)(h-t_s)=575616\ \mathrm{mm^2},
\]

\[
\oint ds/t_s=3046,
\]

\[
D_t^{(s)}=5.74564023165614\times10^9\ \mathrm{Nmm}.
\]

Inner core dimensions:

\[
b_i=5992\ \mathrm{mm},\qquad h_i=92\ \mathrm{mm}.
\]

R15 Saint-Venant rectangle factor:

\[
\beta_{shape}=\frac13\left[1-0.63\frac{h_i}{b_i}+0.052(h_i/b_i)^5\right]
=0.330109034282703.
\]

Hence

\[
D_t^{(c)}=3.47627052178516\times10^9\ \mathrm{Nmm},
\]

\[
D_t=9.22191075344130\times10^9\ \mathrm{Nmm},
\]

\[
D_{xy}=4.61095537672065\times10^9\ \mathrm{Nmm}.
\]

Poisson coupling:

\[
D_\mu=\mu_s^ZD_{y,s}+\mu_c^ZD_{y,c}
=1.63331521066664\times10^9\ \mathrm{Nmm}.
\]

Therefore

\[
\boxed{H=6.24427058738729\times10^9\ \mathrm{Nmm}}.
\]

## 3. Controlling physical halfwave

Continuous optimum:

\[
\boxed{j_0=1.98138534989740}.
\]

Exact Navier candidate loads from the R15 front end:

```text
j=1 : 61.9390247832 MN
j=2 : 40.3502059923 MN
j=3 : 47.5621487985 MN
j=4 : 63.3279903309 MN
j=5 : 85.1533170840 MN
j=6 :112.4226244263 MN
```

Thus independently from the nonlinear historical result,

\[
\boxed{m_{phys}=2,\qquad \ell=6000\ \mathrm{mm},\qquad k=1,\qquad q_0=0.004.}
\]

The exact elastic structural scale is

\[
\boxed{P_{cr}=40.3502059923\ \mathrm{MN}}.
\]

Material phase areas are

\[
A_{c,eff}=0.98bt_c=540960\ \mathrm{mm^2},
\]

\[
A_{face}=2bt_s=48000\ \mathrm{mm^2},
\]

\[
A_w=\rho_wbt_c=11040\ \mathrm{mm^2}.
\]

## 4. Full nonlinear R15 execution attempt

The next required objects are the exact continuous functions

\[
P(D,q,\alpha),\qquad R_q(D,q,\alpha),\qquad R_\alpha(D,q,\alpha),
\]

and their same-source first derivatives. R15 Section 7 currently gives only an **allowed backend class list**:

```text
elementary/Beta/Gamma
Carlson elliptic
Gauss/Appell/Lauricella
algebraic Abelian periods
GKZ/relative-incomplete A-hypergeometric
Mellin-Barnes
differential-system/holonomic
```

but it does not contain a specimen-independent executable map from the finite R13/R14 current operators to a concrete evaluable standard-function expression for P, Rq and Ralpha.

A direct exact Wolfram `Integrate` constructor was attempted on the essential algebraic R10 projector integral, with symbolic affine strain parameters and no NIntegrate or sampling. That constructor did not close in the available service and returned an upstream symbolic-evaluation error. Per project rule, this representation is therefore **crossed out as the production constructor**; it is not promoted into a new theory gate.

No numerical integration was substituted.

## 5. Audit conclusion

The Z1 trial proves the following distinction:

```text
R15 raw-input/front-end specification = EXECUTABLE / PASS
R15 continuous kinematics = COMPLETE
R15 finite material maps = COMPLETE
R15 formal definitions of P,Rq,Ralpha,Jlim = COMPLETE
R15 exact continuous integral evaluator = NOT ACTUALLY INSTANTIATED
R15 full nonlinear from-zero execution ledger = OVERCLAIMED
```

Therefore R15 must be downgraded from “complete executable from-zero calculation ledger” to:

\[
\boxed{\text{complete from-zero theory/specification ledger, but not yet a complete executable evaluator}.}
\]

This is not a new gate. It is a correction of the previous R15 identity claim exposed by the requested Z1 execution test.

## 6. What is and is not a Z1 result from this run

Valid new R15 Z1 results from this run:

```text
Ec0 = 32500 MPa
Dx = 5.90813599999987e9 Nmm
Dy = 6.13330661333320e9 Nmm
H  = 6.24427058738729e9 Nmm
j0 = 1.98138534989740
m_phys = 2
ell = 6000 mm
k = 1
q0 = 0.004
Pcr = 40.3502059923 MN
```

Not produced independently in this run:

```text
Du, qu, alphau
Pc, Pface, Pw
Pu
```

Any historical Z1 nonlinear values remain comparison-only provenance and are not relabeled as a new R15 solve.

## 7. Required correction to project state

Do not create another formal “gate”. The next constructor work must directly instantiate one exact continuous evaluator. If a chosen exact constructor cannot evaluate the full finite R10 + face + web period, cross it out and switch constructor; do not use spatial discretization.
