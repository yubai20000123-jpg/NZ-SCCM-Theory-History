# NZ-SCCM — 钢壳–UHPC 极限承载力集中技术总账 R09

**Date:** 2026-09-01  
**Working branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Role:** standalone theory + implementation specification for current steel-shell–UHPC capacity-contact solver  
**Production main:** unchanged  
**Supersedes as current transfer specification:** `20260831__NZSCCM__STEEL_SHELL_UHPC_CENTRAL_TECHNICAL_LEDGER_R01.md`  
**Formal spatial quadrature:** `0`  
**Material-point grid:** `0`  
**Excel Solver / Goal Seek / load stepping / path tracking:** `0`  
**Comparator/test/FEM in parameter calibration or root selection:** `0`

---

# 0. Purpose and locked identity

This file is intentionally self-contained enough that a new AI/model with no project memory can rebuild the current R09 capacity-contact evaluator from raw specimen/material inputs.

Current chain:

```text
raw independent inputs
-> material-contract derived parameters
-> composite A/D
-> minimum integer global mode m*=argmin Pcr,m over m=1..12
-> Marguerre–Airy Pcr,C,Kx,G,Jx,Jy
-> automatic steel branch gate sigma_cr,s^E versus fy
   -> R04_YIELD_FIRST
   -> R02 + R06_LOCAL_BUCKLING_FIRST
-> exact Hu-Wenxu UHPC continuous-thickness resultants
-> longitudinal web ideal-EP resultants
-> section N/M closure
-> FORCE_FIRST_CAPACITY_CONTACT_R01 terminal
-> deterministic finite candidate evaluator
-> q and P
```

The old 20260821 simplified `Z-section m_u(n)` surface is excluded. Effective width/effective area repairs are excluded. The later same-q deformation-compatible research correction is not silently substituted for this archived capacity-contact terminal.

The current output identity is:

```text
terminal_rule = FORCE_FIRST_CAPACITY_CONTACT_R01
output_identity = AIRY_NM_CAPACITY_CONTACT_PREDICTION
```

---

# 1. Required independent inputs

Use N–mm–MPa. A new specimen is not fully defined by only `b,a,tc,ts,fc,fy`.

Required inputs:

```text
Geometry/global imperfection:
  b            gross transverse width [mm]
  a_phys       physical axial length [mm]
  tc           UHPC thickness [mm]
  ts           each steel-face thickness [mm]
  A0g          global imperfection amplitude [mm]

Longitudinal web:
  Aw           total longitudinal web-steel area distributed across width [mm^2]

Steel:
  Es           Young modulus [MPa]
  nu_s         Poisson ratio
  fy           yield strength [MPa]

UHPC:
  Ec           initial modulus [MPa]
  nu_c         initial Poisson parameter
  fc           compression-strength parameter [MPa]
  eps_c0       peak compression strain
  fct          tensile-strength parameter [MPa]
  eps_t0       tensile strain scale

Fibres:
  Vf           fibre volume fraction
  lf           fibre length [mm]
  df           fibre diameter [mm]

Local steel cell for R02/R06:
  Lx           local transverse cell length [mm]
  Ly           local axial cell length [mm]
  A0           local imperfection amplitude [mm]
```

Derived only; do not ask the user to enter them independently:

\[
q_0=A_{0g}/b,
\qquad
\rho_w=\frac{A_w}{bt_c},
\qquad
z_f=\frac{t_c+t_s}{2}.
\]

UHPC material contract:

\[
E_0=\frac{f_c}{\varepsilon_{c0}},
\qquad
n_c=\frac{E_c\varepsilon_{c0}}{f_c},
\]

\[
K_f=\left(\frac{l_f}{d_f}\right)V_f,
\qquad
m_t=0.85-0.47K_f+0.12K_f^2.
\]

Accept only positive physical scales together with

```text
n_c > 1
0 < K_f <= 3
m_t > 0
```

If the contract fails, return `UHPC_MATERIAL_CONTRACT_FAIL`. Do not silently switch material law.

---

# 2. Coordinates and global mode

```text
x = transverse
y = axial
z = through thickness, positive to upper steel face
```

\[
\psi=\sin(\alpha x)\sin(\beta y),
\qquad
\alpha=\pi/b,
\qquad
\beta_m=m\pi/a_{phys}.
\]

\[
w_0=bq_0\psi,
\qquad
w=b(q_0+q)\psi,
\qquad
Q(q)=q(q+2q_0).
\]

The capacity-contact generalized curvatures below are section coordinates; do not relabel them as geometric curvatures without the separate same-q repair.

---

# 3. Composite A/D operator

Define

\[
K_s=\frac{E_s}{1-\nu_s^2},\quad
K_c=\frac{E_c}{1-\nu_c^2},\quad
G_s=\frac{E_s}{2(1+\nu_s)},\quad
G_c=\frac{E_c}{2(1+\nu_c)}.
\]

In-plane terms used by R09:

\[
A_{11}=2t_sK_s+(1-\rho_w)t_cK_c,
\]

\[
A_{22}=A_{11}+\rho_wt_cE_s,
\]

\[
A_{12}=2t_s\nu_sK_s+(1-\rho_w)t_c\nu_cK_c,
\]

\[
A_{66}=2t_sG_s+(1-\rho_w)t_cG_c.
\]

Bending terms:

\[
D_f=2K_s\left(\frac{t_s^3}{12}+t_sz_f^2\right),
\]

\[
D_c=(1-\rho_w)K_c\frac{t_c^3}{12},
\qquad
D_w=\rho_wE_s\frac{t_c^3}{12},
\]

\[
D_x=D_f+D_c,
\qquad
D_y=D_x+D_w,
\]

\[
D_\mu=\nu_sD_f+\nu_cD_c,
\]

\[
D_{66}=2G_s\left(\frac{t_s^3}{12}+t_sz_f^2\right)
 +(1-\rho_w)G_c\frac{t_c^3}{12},
\]

\[
\boxed{H=D_\mu+2D_{66}}.
\]

For each integer `m=1,...,12`,

\[
N_{cr,m}=\frac{D_x\alpha^4+2H\alpha^2\beta_m^2+D_y\beta_m^4}{\beta_m^2},
\qquad
P_{cr,m}=bN_{cr,m}.
\]

Select

\[
\boxed{m^*=\arg\min_{m\in\{1,...,12\}}P_{cr,m}}.
\]

No FEM/test value enters mode selection.

---

# 4. Marguerre–Airy demand

Let

\[
\Delta_A=A_{11}A_{22}-A_{12}^2,
\qquad
\beta=\beta_{m^*}.
\]

R09 coefficients are

\[
K_x=\frac{b^2\alpha^2}{8(A_{22}/\Delta_A)},
\]

\[
G=\frac{b^2\beta^2}{8(A_{11}/\Delta_A)},
\]

\[
C=\frac{b^3\Delta_A}{16\beta^2}
\left(\frac{\alpha^4}{A_{22}}+\frac{\beta^4}{A_{11}}\right),
\]

\[
J_x=b(D_x\alpha^2+D_\mu\beta^2),
\qquad
J_y=b(D_\mu\alpha^2+D_y\beta^2).
\]

The load map is

\[
\boxed{P^A(q)=P_{cr}\frac{q}{q+q_0}+CQ(q)}.
\]

At the capacity-contact control section,

\[
N_x^A=K_xQ(q),
\qquad
M_x^A=J_xq,
\]

\[
N_y^A=-\left[\frac{P^A(q)}{b}-GQ(q)\right],
\qquad
M_y^A=J_yq.
\]

---

# 5. Automatic R04/R06 branch gate

Define

\[
r=L_y/L_x,
\]

\[
k_{cr}=\frac{4(3r^4+2r^2+3)}{3r^2},
\]

\[
\boxed{
\sigma_{cr,s}^{E}=\frac{\pi^2E_st_s^2}{12(1-\nu_s^2)L_x^2}k_{cr}
}.
\]

Mechanical switch:

```text
if sigma_cr,s^E >= fy:
    branch = R04_YIELD_FIRST
else:
    branch = R06_LOCAL_FIRST
```

The specimen name is not used by the switch.

---

# 6. R04 yield-first face operator

At a face generalized strain `(eps_x, eps_y)` with zero face shear in the current control-section implementation,

\[
\sigma_x^{tr}=\frac{E_s}{1-\nu_s^2}(\varepsilon_x+\nu_s\varepsilon_y),
\]

\[
\sigma_y^{tr}=\frac{E_s}{1-\nu_s^2}(\varepsilon_y+\nu_s\varepsilon_x),
\]

\[
\sigma_{VM}^{tr}=
\sqrt{(\sigma_x^{tr})^2-\sigma_x^{tr}\sigma_y^{tr}+(\sigma_y^{tr})^2}.
\]

\[
\lambda_p=\min\left(1,\frac{f_y}{\sigma_{VM}^{tr}}\right),
\]

\[
\boxed{\sigma_x=\lambda_p\sigma_x^{tr},\qquad
\sigma_y=\lambda_p\sigma_y^{tr}}.
\]

Do not insert R02 local-buckling reduction before yield in R04.

---

# 7. R02 local postbuckling operator

Local wavenumbers:

\[
k_x=2\pi/L_x,\qquad k_y=2\pi/L_y,
\]

\[
c_x=3k_x^2/8,\qquad c_y=3k_y^2/8.
\]

\[
K_b^\ell=
\frac{E_st_s^3}{12(1-\nu_s^2)}
\left[\frac34(k_x^4+k_y^4)+\frac12k_x^2k_y^2\right].
\]

\[
K_A=k_x^4k_y^4\left[
\frac{17}{256k_y^4}+\frac{17}{256k_x^4}
+\frac1{8(k_x^2+k_y^2)^2}
+\frac1{32(k_x^2+4k_y^2)^2}
+\frac1{32(4k_x^2+k_y^2)^2}
\right].
\]

Let

\[
Q_s=E_s/(1-\nu_s^2).
\]

For input face strains `(e_x,e_y)`,

\[
B_3=4t_sE_sK_A+2t_sQ_s(c_x^2+2\nu_sc_xc_y+c_y^2),
\]

\[
B_1=K_b^\ell-A_0^2B_3
+2t_sQ_s(c_xe_x+\nu_sc_xe_y+\nu_sc_ye_x+c_ye_y),
\]

\[
B_0=-A_0K_b^\ell.
\]

Solve the cubic

\[
\boxed{B_3U^3+B_1U+B_0=0}.
\]

Candidate set:

```text
U=0
+ every nonnegative real cubic root
```

Select the candidate minimizing

\[
\Pi(U)=\frac{B_3}{4}U^4+\frac{B_1}{2}U^2+B_0U.
\]

Then

\[
d=U^2-A_0^2,
\qquad
m_x=e_x+c_xd,
\qquad
m_y=e_y+c_yd,
\]

\[
\bar\sigma_x=Q_s(m_x+\nu_sm_y),
\qquad
\bar\sigma_y=Q_s(m_y+\nu_sm_x).
\]

The LL Airy harmonics retained by the current source-audited family are exactly

```text
(p,q,c_pq)
(0,1,+1/2)
(0,2,-1/2)
(1,0,+1/2)
(1,1,-1)
(1,2,+1/2)
(2,0,-1/2)
(2,1,+1/2)
```

For the source-audited BH/T360 family the active local-yield edge is `v=cos(Y)=-1`. R09 therefore compiles the exact edge polynomial in `u=cos(X)`:

```text
T_0(u)=1
T_1(u)=u
T_2(u)=2u^2-1
```

For each harmonic define

\[
\Lambda_{pq}=((pk_x)^2+(qk_y)^2)^2,
\]

\[
A_{pq}=E_sdk_x^2k_y^2\frac{c_{pq}}{\Lambda_{pq}}(-1)^q.
\]

Then on `v=-1`,

\[
\sigma_x(u)=\bar\sigma_x+
\sum_{pq}\left[-A_{pq}(qk_y)^2T_p(u)\right],
\]

\[
\sigma_y(u)=\bar\sigma_y+
\sum_{pq}\left[-A_{pq}(pk_x)^2T_p(u)\right].
\]

Thus

\[
\Phi(u)=\sigma_x^2-\sigma_x\sigma_y+\sigma_y^2
\]

is a quartic polynomial. Its exact finite extremum candidate set is

```text
u=-1, +1
+ all real roots in (-1,1) of dPhi/du=0
```

and

\[
\sigma_{VM,max}^2=\max\Phi(u_c).
\]

**Transfer boundary:** `v=-1` is source-audited for the current BH032/BH050/T360 R06 family. For a new topology/local registration where another edge/interior candidate may govern, this edge identity must be audited before claiming universal R06 transfer. Do not silently assume it is universal outside the validated family.

---

# 8. R06 finite eta candidate enumeration — no Brent/Newton

For a requested face strain vector `(e_x,e_y)`, define

\[
h(\eta)=\sigma_{VM,max}^2(\eta e_x,\eta e_y)-f_y^2,
\qquad 0\le\eta\le1.
\]

If `h(1)<=0`, set

```text
eta=1
```

and use the unprojected R02 mean.

Otherwise R09 uses this deterministic finite candidate procedure:

1. Prescribe exactly 33 nodes

\[
\eta_j=j/32,\qquad j=0,...,32.
\]

2. Evaluate the exact source `h(eta_j)` at all 33 nodes.
3. Retain every adjacent interval `[eta_i,eta_{i+1}]` with an exact zero or a sign change.
4. For each retained interval set

```text
j0=max(0,min(27,i-2))
```

and use the six nodes `eta[j0:j0+6]`.
5. Fit a degree-5 polynomial in eta to those six exact h-values.
6. Enumerate **all** roots of that degree-5 polynomial; retain real roots lying in the six-node window.
7. Also add the one-shot secant-interpolation candidate from the isolated sign-changing interval. This is not an iterative secant solver.
8. Evaluate the exact source `|h(eta)|` at every retained candidate and choose the one with minimum exact residual.
9. Re-condense R02 at that eta and return the whole-width R02 mean stress/resultant.

Failures are explicit:

```text
R06_ETA_NOT_ISOLATED
R06_ETA_CANDIDATE_EMPTY
```

No `brentq`, Newton, Goal Seek or Solver is used.

---

# 9. Hu-Wenxu UHPC scalar law

Sign convention: tension positive, compression negative.

Compression magnitude, with

\[
\xi=|\varepsilon|/\varepsilon_{c0},
\qquad n=n_c,
\]

is

\[
\widehat\sigma_c=
\begin{cases}
f_c\dfrac{n\xi-\xi^2}{1+(n-2)\xi},&0\le\xi\le1,\\[6pt]
f_c\dfrac{\xi}{2(\xi-1)^2+\xi},&\xi>1.
\end{cases}
\]

and `sigma=-widehat_sigma_c` in compression.

Tension, with

\[
\xi_t=\varepsilon/\varepsilon_{t0}>0,
\]

is

\[
\boxed{
\sigma_t=f_{ct}e^{1/m_t}\xi_t
\exp\left(-\frac{\xi_t^{m_t}}{m_t}\right)
}.
\]

---

# 10. Exact continuous-thickness UHPC primitives

Define compression primitive integrals.

Ascending branch `0<=xi<=1`:

\[
I_{0a}(\xi)=
-\frac{\xi^2}{2(n-2)}
+\frac{(n-1)^2\xi}{(n-2)^2}
-\frac{(n-1)^2}{(n-2)^3}\ln[1+(n-2)\xi],
\]

\[
I_{1a}(\xi)=
-\frac{\xi^3}{3(n-2)}
+\frac{(n-1)^2\xi^2}{2(n-2)^2}
-\frac{(n-1)^2\xi}{(n-2)^3}
+\frac{(n-1)^2}{(n-2)^4}\ln[1+(n-2)\xi].
\]

Descending raw primitives:

\[
I_{0d}^{raw}(\xi)=
\frac14\ln\left(\xi^2-\frac32\xi+1\right)
+\frac{3\sqrt7}{14}\arctan\left(\frac{\sqrt7(4\xi-3)}7\right),
\]

\[
I_{1d}^{raw}(\xi)=
\frac{\xi}{2}
+\frac38\ln\left(\xi^2-\frac32\xi+1\right)
+\frac{\sqrt7}{28}\arctan\left(\frac{\sqrt7(4\xi-3)}7\right).
\]

For `xi>1`, use the continuous cumulative form

\[
I_j(\xi)=I_{ja}(1)+I_{jd}^{raw}(\xi)-I_{jd}^{raw}(1).
\]

Compression strain primitives:

\[
F_0(\varepsilon<0)=f_c\varepsilon_{c0}I_0(\xi),
\]

\[
F_1(\varepsilon<0)=-f_c\varepsilon_{c0}^2I_1(\xi).
\]

For tension set

\[
t=\xi_t^{m_t}/m_t,
\]

and let `gamma(s,t)` denote the lower incomplete gamma function. Then

\[
F_0(\varepsilon>0)=
f_{ct}e^{1/m_t}\varepsilon_{t0}
 m_t^{2/m_t-1}\gamma(2/m_t,t),
\]

\[
F_1(\varepsilon>0)=
f_{ct}e^{1/m_t}\varepsilon_{t0}^2
 m_t^{3/m_t-1}\gamma(3/m_t,t).
\]

Set `F0(0)=F1(0)=0`.

For an affine directional strain

\[
\varepsilon(z)=\varepsilon^0+\kappa z,
\qquad
\varepsilon_\pm=\varepsilon^0\pm\kappa t_c/2,
\]

if `kappa != 0`,

\[
\boxed{
N^U=(1-\rho_w)\frac{F_0(\varepsilon_+)-F_0(\varepsilon_-)}{\kappa}
},
\]

\[
\boxed{
M^U=(1-\rho_w)\frac{
F_1(\varepsilon_+)-F_1(\varepsilon_-)
-\varepsilon^0[F_0(\varepsilon_+)-F_0(\varepsilon_-)]
}{\kappa^2}
}.
\]

For `kappa=0`, use the continuous limit

\[
N^U=(1-\rho_w)t_c\sigma_U(\varepsilon^0),
\qquad M^U=0.
\]

No through-thickness Gauss points are introduced.

---

# 11. Longitudinal web exact ideal-EP operator

Web strain:

\[
\varepsilon_y^w(z)=\varepsilon_y^0+\kappa_yz.
\]

Steel law:

\[
\sigma_y^w=\operatorname{clip}(E_s\varepsilon_y^w,-f_y,+f_y).
\]

Let `eps_yield=fy/Es`. Split the interval `[-tc/2,+tc/2]` only at analytic crossing locations

\[
z=(\pm\varepsilon_{yield}-\varepsilon_y^0)/\kappa_y
\]

that lie inside the thickness. On each elastic or yielded subinterval integrate `sigma` and `z sigma` analytically. Multiply by `rho_w`.

This is an exact phase integral, not spatial numerical quadrature.

---

# 12. Section assembly

Section state:

\[
\varepsilon_x(z)=\varepsilon_x^0+\kappa_xz,
\qquad
\varepsilon_y(z)=\varepsilon_y^0+\kappa_yz.
\]

Steel-face strain pairs:

\[
(e_x^+,e_y^+)=(\varepsilon_x^0+\kappa_xz_f,\varepsilon_y^0+\kappa_yz_f),
\]

\[
(e_x^-,e_y^-)=(\varepsilon_x^0-\kappa_xz_f,\varepsilon_y^0-\kappa_yz_f).
\]

Evaluate each face by R04 or R02/R06 according to the automatic branch gate.

Total resultants:

\[
N_x=N_x^U+t_s(\sigma_x^++\sigma_x^-),
\]

\[
M_x=M_x^U+t_sz_f(\sigma_x^+-\sigma_x^-),
\]

\[
N_y=N_y^U+t_s(\sigma_y^++\sigma_y^-)+N_y^w,
\]

\[
M_y=M_y^U+t_sz_f(\sigma_y^+-\sigma_y^-)+M_y^w.
\]

Keep the UHPC, upper face, lower face, web and total ledgers separately visible.

---

# 13. Capacity-contact reduction to three endpoint variables

Terminal rule:

\[
\boxed{\varepsilon_y(-t_c/2)=-\varepsilon_{c0}}.
\]

Use three endpoint variables

\[
\boxed{p=(x_-,x_+,y_+)},
\]

where

\[
x_-=\varepsilon_x(-t_c/2),
\quad
x_+=\varepsilon_x(+t_c/2),
\quad
y_+=\varepsilon_y(+t_c/2),
\]

and set

\[
y_-=-\varepsilon_{c0}.
\]

Recover section coordinates explicitly:

\[
\varepsilon_x^0=(x_-+x_+)/2,
\qquad
\kappa_x=(x_+-x_-)/t_c,
\]

\[
\varepsilon_y^0=(y_-+y_+)/2,
\qquad
\kappa_y=(y_+-y_-)/t_c.
\]

Use the `Mx` balance to eliminate q:

\[
\boxed{q=M_x/J_x}.
\]

Independently form

\[
q_y=M_y/J_y.
\]

For `q>0` and `q+q0>0`, compute

\[
Q=q(q+2q_0),
\]

\[
P=P_{cr}\frac{q}{q+q_0}+CQ.
\]

The three scaled residuals used by the deterministic terminal evaluator are

\[
r_1=\frac{q-q_y}{\max(q_0,10^{-12})},
\]

\[
r_2=\frac{N_x-K_xQ}{1000},
\]

\[
r_3=\frac{N_y+\left(P/b-GQ\right)}{1000}.
\]

The raw closure audit additionally reports

\[
R_{raw}=\max\left(
|N_x-N_x^A|,
\frac{|M_x-M_x^A|}{z_f},
|N_y-N_y^A|,
\frac{|M_y-M_y^A|}{z_f}
\right).
\]

---

# 14. R09 deterministic finite terminal candidate backend

The exact Hu-Wenxu tension primitive contains an incomplete-gamma function; therefore the full terminal system is not an ordinary polynomial system. R09 does **not** pretend otherwise. It removes the former Newton/Brent evaluator and uses a fixed finite candidate procedure with exact-source residual verification.

## 14.1 Fixed global endpoint box

Define

\[
u_x=\max(\varepsilon_{c0},3\varepsilon_{t0}),
\]

\[
u_y=\max(2\varepsilon_{t0},0.75\varepsilon_{c0}).
\]

Global box:

```text
x_- in [-eps_c0, u_x]
x_+ in [-eps_c0, u_x]
y_+ in [-eps_c0, u_y]
```

Grid size is fixed by steel branch:

```text
R04_YIELD_FIRST: n0 = 25 nodes per axis
R06_LOCAL_FIRST: n0 = 7 nodes per axis
```

The finite candidate count retained for refinement is bounded:

```text
R04: first 32 deduplicated candidate boxes
R06: first 12 deduplicated candidate boxes
```

## 14.2 Initial sign-bracket candidate boxes

Evaluate the exact residual vector `(r1,r2,r3)` at every fixed grid node.

For each adjacent cube, examine its eight corner residual vectors. Keep the cube only if for **each** residual component the eight corners bracket zero:

```text
min(r_k at 8 corners) <= 0 <= max(r_k at 8 corners), k=1,2,3
```

Fit the affine map

\[
r(p)\approx c+A p
\]

by least squares to the eight corner residual vectors and solve

\[
Ap=-c.
\]

If that affine candidate lies outside a 25%-padded cube, replace it by the cube center.

Rank initial candidates by exact `max(abs(r1),abs(r2),abs(r3))` and deduplicate candidates closer than `1e-6` in endpoint-strain Euclidean norm.

## 14.3 Exactly eight predetermined local refinements

For each retained initial candidate:

1. Initial half-width is `1.5 * global_grid_step` in each coordinate.
2. At every stage use exactly a `3 x 3 x 3` stencil clipped to the fixed global box.
3. Evaluate the exact source residual vector at all 27 points.
4. Fit an affine residual map to the 27 values and solve its `3 x 3` linear system.
5. If the affine candidate lies inside the fixed global box, use it; otherwise use the sampled stencil point with minimum exact `max(abs(r))`.
6. Multiply all half-widths by exactly `0.35`.
7. Repeat for exactly **8 stages**.

The number of stages is not a convergence loop and must not be increased until a target value is reached.

## 14.4 Candidate admissibility and selection

After the eight fixed stages, retain candidates satisfying the endpoint/contact orientation

```text
min(x_-,x_+,y_+) >= -eps_c0 - 1e-9
q > 0
q + q0 > 0
```

A R09 `PASS` candidate additionally requires

\[
\boxed{\max(|r_1|,|r_2|,|r_3|)\le5\times10^{-4}}.
\]

Among `PASS` candidates select the smallest positive q. This is a physical first-capacity-contact selection; FEM/test values are forbidden in the ranking.

If finite candidates exist but none meets the PASS residual gate, return `CHECK`, not a calibrated answer. If no candidate survives, return `NO_FINITE_TERMINAL_CANDIDATE`.

## 14.5 Forbidden hidden methods

R09 terminal implementation shall contain no calls equivalent to

```text
scipy.optimize.root
fsolve
nsolve
newton
brentq
bisect
Excel Solver
Goal Seek
load stepping
path continuation
```

Polynomial root enumeration such as `numpy.roots` is allowed for the R02 cubic, the edge-Mises derivative cubic and the fitted finite R06 eta candidate polynomial.

---

# 15. Required output ledger

Every accepted calculation must expose at least:

```text
raw independent inputs
q0, rho_w, zf
E0, n_c, K_f, m_t and material-contract status
A11,A22,A12,A66,Dx,Dy,Dmu,D66,H
m*, beta, Pcr,Kx,G,C,Jx,Jy
sigma_cr,s^E and R04/R06 branch ID
R02 cubic candidate roots/selected U when R06 is active
R04 lambda_p when R04 is active
R06 eta and local Mises residual when R06 is active
UHPC endpoint strains and NxU,MxU,NyU,MyU
upper/lower face stresses and resultants
web Nyw,Myw
total Nx,Mx,Ny,My
Airy NxA,MxA,NyA,MyA
raw closure residuals
scaled terminal residuals
candidate count
terminal status PASS/CHECK
q
P [MN]
```

---

# 16. R09 regression checkpoints

Independent R09 finite-candidate execution gives:

```text
BH005
branch = R04_YIELD_FIRST
q = 0.00003171937844289577
P = 2.462334761886874 MN

BH010
branch = R04_YIELD_FIRST
q = 0.00012253583272986489
P = 4.583421997191359 MN

BH020
branch = R04_YIELD_FIRST
q = 0.0005298324925967968
P = 8.578796170132193 MN

BH032
branch = R06_LOCAL_FIRST
q = 0.001378899786761743
P = 10.940535389068453 MN

BH050
branch = R06_LOCAL_FIRST
q = 0.0047728206527406485
P = 13.356377445246078 MN

T360
branch = R06_LOCAL_FIRST
q = 0.0013451863077927676
P = 10.818377929317574 MN
```

Exact source-audited current-state checkpoints for the three R06 specimens are approximately

```text
BH032 = 10.9405345132294 MN
BH050 = 13.3563763545430 MN
T360  = 10.8183777809815 MN
```

R09 differs only by the finite candidate evaluator tolerance, at the order of `1e-7` relative in these checkpoints.

A non-historical automatic branch-switch test:

```text
BH050 geometry with ts=8 mm
sigma_cr,s^E = 401.798669935469 MPa > fy=355 MPa
branch = R04_YIELD_FIRST
q = 0.00357727818074878
P = 24.30966406541705 MN
```

This is an implementation audit, not a calibration datum.

Canonical Abaqus peak-load comparison currently used for external verification:

```text
BH005 FEM = 2.355811 MN
BH010 FEM = 4.304329 MN
BH020 FEM = 8.0079015 MN
BH032 FEM = 10.990480 MN
BH050 FEM = 12.591227 MN
```

Corresponding R09/FEM errors are approximately

```text
BH005 +4.52%
BH010 +6.48%
BH020 +7.13%
BH032 -0.45%
BH050 +6.08%
```

FEM/test data are verification only and must never enter parameter generation, branch switching, candidate construction or root selection.

---

# 17. Standalone new-AI execution protocol

A new AI with this ledger and a complete new-specimen input set shall execute in this order:

```text
1. Parse units and all independent inputs.
2. Compute q0,rho_w,zf,E0,n_c,K_f,m_t.
3. Enforce the UHPC material contract; stop explicitly if it fails.
4. Build A/D and enumerate m=1..12; select minimum Pcr.
5. Build Kx,G,C,Jx,Jy.
6. Compute sigma_cr,s^E and select R04 or R06 mechanically.
7. Build the exact Hu-Wenxu F0/F1 continuous-thickness operator.
8. Build the exact ideal-EP web operator.
9. Build R04, or R02 plus R06 finite eta candidates.
10. Use terminal y_-=-eps_c0 and endpoint variables (x_-,x_+,y_+).
11. Eliminate q through q=Mx/Jx.
12. Execute the fixed finite terminal candidate procedure in Section 14.
13. Reject comparator-guided or residual-failing candidates.
14. Return smallest positive-q PASS candidate.
15. Print the complete audit ledger in Section 15.
16. Run BH032/BH050/T360 regression before declaring the implementation source-identical.
```

Do not use project history, FEM peak loads or specimen names as hidden solver inputs.

---

# 18. Transfer-readiness verdict and scope

```text
R09_EXCEL_SINGLE_FILE_EXECUTABLE = YES,
  provided the environment can execute Excel PY() or extract/run the embedded Python,
  with NumPy and SciPy special functions available.

R09_LEDGER_STANDALONE_REIMPLEMENTABLE = YES,
  for the current capacity-contact solver and the source-audited BH/T360 R06 active-edge family,
  using the formulas and fixed candidate algorithm above.

GROSS_DIMENSIONS_ONLY_SUFFICIENT = NO.
  Aw, Lx, Ly, A0_local and the complete material/fibre inputs are required.

R06_V_MINUS_ONE_EDGE_UNIVERSAL_FOR_ARBITRARY_NEW_LOCAL_TOPOLOGY = NOT_PROVEN.
  New local registrations outside the audited family require a finite full-candidate edge/interior audit before universal transfer is claimed.

PHYSICAL_SAME_Q_DEFORMATION_COMPATIBLE_TERMINAL = NOT_FROZEN.
  This R09 ledger reproduces the current FORCE_FIRST_CAPACITY_CONTACT_R01 identity only.
```

Accordingly, the strongest current handoff package is

```text
R09 central ledger
+ R09 Excel executable reference
+ complete independent specimen/material inputs
```

but either the R09 Excel or this R09 ledger is now sufficient to carry the current solver identity without relying on prior chat memory, subject to the explicit scope boundaries above.

---

# 19. Non-negotiable prohibitions

Do not:

- replace Hu-Wenxu by Zhang/Hiew/Liu without an explicitly new material-study branch;
- use the old simplified Z-section capacity surface;
- use effective width/effective area to repair steel-face response;
- use FEM/test values to select m, R04/R06, eta, q or terminal candidates;
- use spatial Gauss/Simpson/material-point grids in the formal section operator;
- use hidden Newton/Brent/Goal Seek/Solver/load stepping and then label it R09 finite-candidate execution;
- relabel capacity-contact curvature coordinates as geometric curvature;
- claim the `v=-1` R06 active edge is universal outside the currently audited family.

**END — NZ-SCCM STEEL-SHELL/UHPC CENTRAL TECHNICAL LEDGER R09**
