# NZ-SCCM — Case21 + Z6(24000) finite-R10 / true-infinite-D15 joint execution

**Timestamp:** 2026-08-17 17:30 +08:00  
**Identity:** JOINT EXECUTION / NO NEW THEORY BRANCH  
**Purpose:** execute Case21 and Z6 simultaneously under one unchanged chain, and remove the mistaken interpretation that R10 itself is an infinite nonlinear constitutive model.

## 0. Locked interpretation

R10 is a finite current material operator. The infinity belongs only to an exact analytic representation of the finite nonlinear composition `S_R10(E(X,Y,z))`.

Formal chain:

```text
actual specimen geometry
-> one continuous complete representative halfwave
-> Nguyen second-order finite trigonometric-thickness strain field
-> finite frozen R10 current operator
-> exact infinite analytic representation of the composed material field
-> nth analytic term -> 2x2 Cayley-Hamilton reduction
-> exact General-D15 moment of that nth term
-> n -> infinity target sum
-> finite P,Rq,RA and same-source tangent
-> finite coupled equilibrium/limit solve
-> Pu
-> post-solve comparator only
```

No new full-R10 recurrence is required. Uniform/absolute convergence of the primitive streams plus continuity of the finite algebraic operations in R10 gives `S_N -> S_R10`; linear continuity of D15 gives

\[
\lim_{N\to\infty}D15[W:S_N]=D15[W:S_{R10}].
\]

Formal counters remain

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

---

# 1. Common finite kinematics

For both current Case21 and the controlling Z6 representative halfwave, `b=ell`, define

\[
X=\pi x/b,\qquad Y=\pi y/\ell,\qquad u=\sin X,\qquad v=\sin Y,\qquad \zeta=2z/t.
\]

Let

\[
M=\frac{\pi^2}{\varepsilon_0}\left(q_0q+\frac12q^2\right),
\qquad
B=\frac{\pi^2t}{2\varepsilon_0b}q,
\qquad
\alpha=\lambda_A M.
\]

Square-halfwave Airy fields:

\[
A_x=-\frac14-\frac\nu2u^2-\frac12v^2+u^2v^2,
\]
\[
A_y=\frac\nu4-\frac\nu2v^2-\frac12u^2+u^2v^2.
\]

Normalized physical strains:

\[
e_x=\nu D+M(v^2-u^2v^2)+\alpha A_x+Buv\zeta,
\]
\[
e_y=-D+M(u^2-u^2v^2)+\alpha A_y+Buv\zeta,
\]
\[
\gamma=2\cos X\cos Y\big[(M-\alpha)uv-B\zeta\big].
\]

Equivalent-strain matrix:

\[
E_{11}=\frac{e_x+\nu e_y}{1-\nu^2},\qquad
E_{22}=\frac{\nu e_x+e_y}{1-\nu^2},\qquad
E_{12}=\frac{\gamma}{2(1+\nu)}.
\]

Principal material coordinates:

\[
\lambda_{1,2}=\frac{E_{11}+E_{22}}2\pm
\sqrt{\left(\frac{E_{11}-E_{22}}2\right)^2+E_{12}^2}.
\]

---

# 2. Common finite R10 current operator

Frozen scalar primitives:

\[
\pi_\eta(z)=\frac{z^2(\sqrt{z^2+\eta^2}+z)}{2(z^2+\eta^2)},
\qquad c_i=\pi_\eta(-\lambda_i),\qquad t_i=\pi_\eta(\lambda_i),
\]

\[
C_i=\frac{\kappa c_i}{1+(\kappa-2)c_i+c_i^2},
\qquad T_i=u_R(t_i)/\rho,
\]

\[
U_i=\kappa\lambda_i-C_i+\kappa c_i+u_R(t_i)-\kappa t_i.
\]

Principal normalized stress:

\[
s_1=U_1-ACC\,C_1^2C_2+C_1T_2-\rho AT\,T_1T_2^8,
\]
\[
s_2=U_2-ACC\,C_2^2C_1+C_2T_1-\rho AT\,T_2T_1^8.
\]

Equivalent 2x2 matrix identity:

\[
S=U-ACC\det(C)C+C\operatorname{adj}(T)-\rho AT\det(T)\operatorname{adj}(T7).
\]

This is finite. Infinite Chebyshev/Fourier streams are only exact representations of these finite scalar/matrix functions on the certified material interval.

For a scalar stream

\[
F(\lambda)=\sum_{n=0}^{\infty} f_nT_n(\widehat\lambda),
\]

the 2x2 lift is

\[
T_n(Y)=p_nI+q_nY,
\]

\[
p_{n+1}=-2\delta q_n-p_{n-1},\qquad
q_{n+1}=2p_n+2\tau q_n-q_{n-1},
\]

where `tau=tr(Y)`, `delta=det(Y)`.

Each nth structural target is exact:

\[
J_n^{(W)}=\sum P_n[r,s]A_{rs}^{(W)}+\sum Q_n[r,s]B_{rs}^{(W)},
\]

and

\[
J^{(W)}=\sum_{n=0}^{\infty} f_nJ_n^{(W)}.
\]

No finite final material degree is part of the theory.

---

# 3. CASE21 execution

## 3.1 Inputs and released coupled root

```text
b = ell = 1220 mm
t = 19.30 mm
q0 = 0.0025
fc = 21.23 MPa
eps0 = 0.00209
nu = 0.18
rho_sx = rho_sy = 0.00375
Es = 200000 MPa

D = 0.7887924801
q = 0.0018083572562965242
lambda_A = 0.08623596353826937
```

## 3.2 Kinematic numbers

\[
M=0.02907033478365149,
\]
\[
M_q=20.345350113975815,
\]
\[
B=0.06754686155676540,
\]
\[
B_q=37.352609016594364,
\]
\[
\alpha=0.002506908330448254,
\qquad M-\alpha=0.026563426453203236.
\]

Expanded normalized strain field:

\[
e_x=0.141355919335388
-0.000225621749740u^2
+0.027816880618427v^2
-0.026563426453203u^2v^2
+0.067546861556765uv\zeta,
\]

\[
e_y=-0.788679669225130
+0.027816880618427u^2
-0.000225621749740v^2
-0.026563426453203u^2v^2
+0.067546861556765uv\zeta,
\]

\[
\gamma=2\cos X\cos Y\left[0.026563426453203uv-0.067546861556765\zeta\right].
\]

## 3.3 Concrete exact-D15 target at the released limit

The infinite analytic representation is evaluated termwise by D15 and summed to the R10 limit. The released limit concrete axial load is

\[
P_c=337.92303037\ \mathrm{kN}.
\]

Using

\[
P_c=-\frac{f_cbt}{2\pi^2}D15[S_{yy}],
\]

this corresponds to

\[
\boxed{D15[S_{yy}]=-13.3438268630311}.
\]

For generalized residuals

\[
R_z^c=\frac{f_c\varepsilon_0b\ell t}{2\pi^2}D15[Q_z],
\]

the common dimensional factor is

\[
\frac{f_c\varepsilon_0b\ell t}{2\pi^2}=64571.8916831\ \mathrm{N\,mm}.
\]

At equilibrium, steel contributes

\[
R_q^s=-294.703813363\ \mathrm{kN\,mm},
\]
\[
R_A^s=-4.331387968\ \mathrm{kN\,mm},
\]

so the corresponding concrete target values are approximately the opposite values, giving the hand-audit normalized D15 values

\[
D15[Q_q]\approx4.56396437648,
\qquad
D15[Q_A]\approx0.06707853610.
\]

## 3.4 Reinforcement exact closed form

Axial reinforcement:

\[
P_s=\rho_{sy}tbE_s\varepsilon_0\left(D-\frac M4\right).
\]

The prefactor is

\[
\rho_{sy}tbE_s\varepsilon_0=36908.355\ \mathrm{N},
\]

therefore

\[
\boxed{P_s=28.844798318\ \mathrm{kN}}.
\]

For the constrained-Airy residual convention,

\[
C_R=\frac{\rho_sE_s\varepsilon_0^2b\ell t}{32\times1000}
=2.94090386184375.
\]

Then

\[
R_A^s=-C_R\left[8D\nu(\nu+1)+M\{5-(4\nu^2+5)\lambda_A\}\right],
\]

\[
R_q^s=C_RM_q\left[8D(\nu-1)+M(9-5\lambda_A)\right],
\]

which give

\[
\boxed{R_A^s=-4.331387968\ \mathrm{kN\,mm}},
\]
\[
\boxed{R_q^s=-294.703813363\ \mathrm{kN\,mm}}.
\]

## 3.5 Finite coupled limit condition

At the released root the same-source Jacobian, rows `(P,Rq,RA)` and columns `(D,q,lambda_A)`, is

\[
\begin{bmatrix}
140.016244 & -70566.7765 & 75.4429339\\
-1587.62545 & 920049.913 & -1213.05\\
6.41847002 & -10550.5046 & 25.2481285
\end{bmatrix}.
\]

The equilibrium equations are

\[
R_q=0,\qquad R_A=0,
\]

and the limit condition is the bordered determinant / connected-branch first maximum.

Final released load:

\[
\boxed{P_u=P_c+P_s=366.767828685\ \mathrm{kN}}.
\]

Only after the solve, compare with

\[
P_{f,exp}=368.312749744\ \mathrm{kN},
\]

so

\[
\Delta=-1.544921058\ \mathrm{kN},
\qquad
\boxed{error=-0.419459\%}.
\]

---

# 4. Z6(24000) execution

## 4.1 Physical geometry and one representative halfwave

```text
a = 24000 mm
b = 12000 mm
a/b = 2
m_star = 2
ell = a/m_star = 12000 mm = b
physical repeated halfwaves = 2
formal structural domain = ONE complete representative halfwave
A0 = a/500 = 48 mm
q0 = A0/b = 0.004
concrete/core thickness tc = 122 mm
face steel thickness ts = 4 mm each
total h = 130 mm
rho_w = 0.02
```

Material:

```text
fc = 30.4 MPa
eps0 = 0.0018712490394580678
nu_c = 0.18
Es = 206000 MPa
fy = 355 MPa
nu_s = 0.30
```

Released coupled state:

```text
D = 1.36180798
q = 0.0264854039
lambda_A = 0.786915819
```

## 4.2 Kinematic numbers

\[
M=2.4086853792820073,
\]
\[
M_q=160.79039729931628,
\]
\[
B=0.7101062648720707,
\]
\[
B_q=26.81123034986341,
\]
\[
\alpha=1.8954326279510263,
\qquad M-\alpha=0.513252751330981.
\]

Concrete-thickness normalized strain field:

\[
e_x=-0.228732720587757
-0.170588936515592u^2
+1.460969065306494v^2
-0.513252751330981u^2v^2
+0.710106264872071uv\zeta,
\]

\[
e_y=-1.276513511742204
+1.460969065306494u^2
-0.170588936515592v^2
-0.513252751330981u^2v^2
+0.710106264872071uv\zeta,
\]

\[
\gamma=2\cos X\cos Y\left[0.513252751330981uv-0.710106264872071\zeta\right].
\]

For the physical face-steel thickness coordinate `z` measured from the section midsurface,

\[
\beta=\frac{\pi^2q}{\varepsilon_0b}=0.0116410863093782\ \mathrm{mm^{-1}},
\]

so the steel trial strains are affine in `z`.

## 4.3 Concrete true-infinite-D15 limit

The released full concrete target is

\[
\boxed{P_{c,full}=23.2827595918\ \mathrm{MN}}.
\]

From

\[
P_{c,full}=-\frac{f_cbtc}{2\pi^2}D15[S_{yy}],
\]

one obtains

\[
\boxed{D15[S_{yy}]=-10.32641404844}.
\]

The adopted effective concrete contribution in the current Z6 full-section state is

\[
P_{c,eff}=0.98P_{c,full}
=\boxed{22.8171044\ \mathrm{MN}}.
\]

The 0.98 factor is retained from the already released Z6 full-section identity; it is not introduced or recalibrated in this joint execution.

## 4.4 Face-steel finite material map and exact-D15 representation

Plane-stress elastic trial stresses:

\[
\sigma_x^{tr}=\frac{E_s}{1-\nu_s^2}(\varepsilon_x+\nu_s\varepsilon_y),
\]
\[
\sigma_y^{tr}=\frac{E_s}{1-\nu_s^2}(\nu_s\varepsilon_x+\varepsilon_y),
\]
\[
\tau^{tr}=\frac{E_s}{2(1+\nu_s)}\gamma.
\]

Trial von Mises invariant:

\[
\sigma_{VM}^{tr}=\sqrt{(\sigma_x^{tr})^2-\sigma_x^{tr}\sigma_y^{tr}+(\sigma_y^{tr})^2+3(\tau^{tr})^2}.
\]

Finite radial-cap material function:

\[
g(r)=\begin{cases}1,&r\le1,\\r^{-1/2},&r>1,\end{cases}
\qquad
r=\frac{(\sigma_{VM}^{tr})^2}{f_y^2},
\]

\[
(\sigma_x,\sigma_y,\tau)=g(r)(\sigma_x^{tr},\sigma_y^{tr},\tau^{tr}).
\]

This steel law is finite just like R10. If represented analytically as

\[
g(r)=\sum_{n=0}^{\infty}g_nT_n(\widehat r),
\]

then every nth face-force contribution is

\[
P_{s,n}=-\frac{b}{\pi^2}\sum_{faces}g_nD15[T_n(\widehat r)\sigma_y^{tr}],
\]

and the formal face result is

\[
\boxed{P_{s,face}=\sum_{n=0}^{\infty}P_{s,n}}.
\]

No elastic/plastic spatial cells are introduced. The local physical yield boundary remains the exact audit equation

\[
A(X,Y)z^2+B(X,Y)z+C(X,Y)-f_y^2=0,
\]

because the trial stresses are affine in `z`; this confirms the physical meaning of the unified `g(r)` representation but does not partition the formal spatial domain.

At the released Z6 state the maximum trial value is

\[
\max\sigma_{VM}^{tr}/f_y\approx1.9474,
\]

and the released exact-limit face contribution is

\[
\boxed{P_{s,face}=18.5564373\ \mathrm{MN}}.
\]

## 4.5 Longitudinal web/PBL steel

The homogenized longitudinal web/PBL contribution retained in the released state is

\[
\boxed{P_w=7.0325797\ \mathrm{MN}}.
\]

Its current one-dimensional steel law is the finite ideal elastic-perfectly-plastic clip composed with the same finite halfwave strain field; the formal exact-moment treatment is unchanged.

## 4.6 Total Z6 ultimate load

\[
P_u=P_{c,eff}+P_{s,face}+P_w,
\]

therefore

\[
P_u=22.8171044+18.5564373+7.0325797
\]

\[
\boxed{P_u=48.4061215\ \mathrm{MN}}.
\]

Only after the solve:

\[
P_{Zhou}=49.4867667519\ \mathrm{MN},
\qquad
\boxed{error=-2.183706\%},
\]

\[
P_{Winter}=50.1858541295\ \mathrm{MN},
\qquad
\boxed{error=-3.546283\%}.
\]

---

# 5. Joint-path audit

The two specimens use the same logical material-to-structure chain:

```text
finite current material function
+ finite continuous halfwave strain field
-> exact infinite analytic representation of their composition
-> nth analytic term
-> exact D15 moment
-> n->infinity target sum
-> finite residual/Jacobian
-> coupled Pu
```

The difference is only the physical constituents:

- Case21: R10 concrete + exact smeared reinforcement.
- Z6: R10 concrete + finite radial-cap face steel + homogenized longitudinal web/PBL steel.

The following interpretations are explicitly rejected:

```text
R10 itself is an infinite constitutive model = FALSE
full nonlinear R10 must first acquire a new standalone infinite recurrence = FALSE
finite evaluation prefix N is a material model degree = FALSE
spatial elastic/plastic partition is required for Z6 radial cap = FALSE
Gauss/Simpson/material-point grid is part of the formal operator = FALSE
```

The released finite roots and loads remain:

```text
Case21: D=0.7887924801, q=0.0018083572562965242, lambda_A=0.08623596353826937,
        Pu=366.767828685 kN, error vs test=-0.419459%

Z6(24000): D=1.36180798, q=0.0264854039, lambda_A=0.786915819,
           Pu=48.4061215 MN,
           error vs Zhou=-2.183706%, error vs Winter=-3.546283%
```

This joint record creates no new theory branch and does not reopen R10 calibration, halfwave selection, or spatial quadrature.