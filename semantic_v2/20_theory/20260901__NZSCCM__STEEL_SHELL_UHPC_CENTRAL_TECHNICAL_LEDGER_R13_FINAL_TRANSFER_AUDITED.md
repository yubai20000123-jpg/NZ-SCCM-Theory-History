# NZ-SCCM — 钢壳–UHPC 显式极限承载力集中技术总账 R13 — FINAL TRANSFER AUDITED

**Date:** 2026-09-01  
**Working branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Production main:** unchanged  
**Current transfer identity:** `STEEL_SHELL_UHPC_R13_FINAL_TRANSFER_AUDITED`  
**Mechanical relation to R12:** unchanged; R13 is a notation/definition/standalone-transfer audit completion  
**Runtime dependence on historical markdown files:** `NONE`  
**Formal spatial quadrature:** `0`  
**Material-point grid:** `0`  
**Reference-specimen/result lookup:** `0`  
**Comparator/test/FEM in material calibration or root selection:** `0`

---

# 0. Governing decision and transfer identity

R13 does **not** create a new capacity theory relative to R12. It closes the remaining transfer risks found in the final audit:

1. every symbol required to calculate the current steel-shell–UHPC axial capacity is defined in this ledger;
2. symbols that could be confused with one another are separated explicitly;
3. upper/lower steel-face section strains are written explicitly;
4. the tension-positive conversion of the historical R02 local operator is stated explicitly;
5. the current scalar UHPC section approximation is stated explicitly, including where `nu_c` is and is not used;
6. the current independent generalized section curvatures are distinguished explicitly from the separate, not-frozen deformation-compatible `q -> kappa^g` research branch;
7. units of total load, membrane resultant and moment resultant are stated explicitly;
8. the complete generic R06 two-dimensional local field is retained inline so no historical source file is needed at runtime or during reimplementation.

The current mechanical chain is

```text
raw user-defined geometry/material inputs
-> input-contract gates
-> initial full-composite A/D
-> exact positive-integer global mode
-> Marguerre–Airy Pcr,C,Kx,G,Jx,Jy
-> q and Q=q(q+2q0)
-> Airy generalized N/M demand
-> explicit upper/lower steel-face centroid strains
-> automatic steel-face event order
   -> R04_YIELD_FIRST
   -> or R02 + R06_LOCAL_BUCKLING_FIRST
-> R13/R12 polynomial UHPC continuous-thickness section operator
-> longitudinal web ideal-EP continuous-thickness operator
-> total Nx,Mx,Ny,My
-> first admissible axial UHPC compression-contact closure
-> smallest positive-q admissible root
-> Pu=P(q)
```

A new AI is not expected to infer any missing equation from another markdown file.

---

# 1. Applicability and hard boundaries

R13 is an axial-compression reduced plate/steel-shell capacity-contact theory, not a general arbitrary-loading finite-element constitutive model.

The current closed scope is

```text
one rectangular gross panel
x = transverse direction
y = axial-loading direction
one continuous global sinusoidal family
positive integer longitudinal half-wave number selected mechanically
zero imposed uniform engineering shear at the axial terminal
independent generalized section strains/curvatures
one rectangular registered local steel-face cell Lx,Ly,A0_local
R04/R06 steel-face event theory
scalar nonlinear UHPC section operator
longitudinal web steel represented by total area Aw smeared through the core thickness
axial UHPC compression-contact terminal
```

The following are prohibited as formal mechanics:

```text
spatial Gauss integration
Simpson integration
adaptive spatial quadrature
material-point grids
material history stepping as the formal theory
effective width/effective area
reference-specimen branch lookup
stored Pu lookup
FEM/test-based material fitting
FEM/test-based root selection
33-point radial-factor sampling
fitted radial-factor quintic surrogate
3x3x3 terminal cell search
8-level terminal refinement
```

If a user-defined parameter set lies outside the stated domain or no admissible root exists, the implementation must return an explicit failure status. It must not switch theories or substitute a stored value.

---

# 2. Units, resultants, coordinates and signs

Use the base unit system

```text
force  N
length mm
stress MPa = N/mm^2
strain dimensionless
```

Coordinates:

```text
x = transverse gross-panel coordinate
y = axial gross-panel coordinate
z = through-thickness coordinate, positive toward the upper steel face
```

Gross panel domain:

\[
0\le x\le b,\qquad 0\le y\le a.
\]

Signs:

```text
normal strain: tension positive
normal stress: tension positive
positive kappa_i means strain increases as z increases
```

Generalized resultants are per unit gross width unless explicitly stated otherwise:

\[
[N_x]=[N_y]=\mathrm{N/mm},
\]

\[
[M_x]=[M_y]=\mathrm{N},
\]

while the axial load

\[
[P]=\mathrm{N}
\]

is the **total** panel load. If an implementation reports MN, it shall use

\[
P_{MN}=P/10^6.
\]

---

# 3. Reserved notation dictionary — do not merge these symbols

This section is mandatory because several historical symbols had visually similar names.

## 3.1 Global geometry and amplitudes

```text
b           gross panel width
a           physical axial panel length
A0g         global initial-imperfection amplitude
q0=A0g/b    dimensionless global initial amplitude
q           dimensionless added global amplitude
m           positive integer longitudinal half-wave count
ell=a/m     physical longitudinal half-wave length
```

## 3.2 Local steel-face geometry

```text
Lx,Ly       local steel-face cell dimensions
A0l         local initial-imperfection amplitude; A0l := A0_local
xi_l,zeta_l local physical cell coordinates
kx,ky       local cell wave numbers 2pi/Lx, 2pi/Ly
```

The local physical coordinate `zeta_l` must **not** be confused with the historical R06 radial projection parameter.

## 3.3 R06 radial projection parameter

R13 writes the R06 radial factor as

\[
\lambda\in[0,1].
\]

The historical symbol `eta` used in earlier R06 files means the same radial factor. Therefore

```text
lambda_y in R13 == historical eta_y
```

but `lambda` is used here to eliminate confusion with local physical coordinates.

## 3.4 Local harmonic indices

R13 uses

\[
(r,s)
\]

for local Airy harmonic indices. These are integers 0,1,2 and are **not** the global amplitude `q`.

## 3.5 Global membrane stiffness versus local Airy harmonic coefficient

The symbols

\[
A_{11},A_{22},A_{12}
\]

are reserved exclusively for the initial global membrane stiffness matrix.

The local LL Airy harmonic coefficient is denoted

\[
\boxed{\mathcal F_{rs}}
\]

and never `A_rs` in R13. This avoids collision between global `A12` and the local `(1,2)` harmonic.

## 3.6 Tensile interpolation coordinate

The normalized coordinate inside one Hiew tensile segment is

\[
\theta\in[0,1]
\]

and is not the local cosine variable `u`.

## 3.7 Upper/lower signs

```text
+ = upper steel face / upper core endpoint, z>0
- = lower steel face / lower core endpoint, z<0
```

---

# 4. Complete independent input contract

## 4.1 Geometry

Independent geometry inputs:

```text
b          gross width
 a         physical axial length
 tc        UHPC core thickness
 ts        thickness of EACH steel face
 A0g       global initial-imperfection amplitude
 Aw        total longitudinal web steel area represented across gross width b
 Lx        local steel-face cell size in x
 Ly        local steel-face cell size in y
 A0l       local steel-face imperfection amplitude (=A0_local)
```

Required gates:

\[
b>0,\quad a>0,\quad t_c>0,\quad t_s>0,
\]

\[
L_x>0,\quad L_y>0,
\]

\[
A_{0g}\ge0,\quad A_{0l}\ge0,\quad A_w\ge0.
\]

Derived web area fraction and steel-face centroid offset:

\[
\boxed{\rho_w=\frac{A_w}{bt_c}},
\qquad
\boxed{z_f=\frac{t_c+t_s}{2}}.
\]

Require

\[
\boxed{0\le\rho_w<1}.
\]

`Aw` is the **total longitudinal web steel area contained in the full gross width b**. The model replaces that discrete area by the uniform core-thickness area fraction `rho_w` and subtracts the same fraction once from the UHPC core operator.

## 4.2 Steel

Independent inputs:

```text
Es      Young modulus
nu_s    Poisson ratio
fy      yield stress
```

Require

\[
E_s>0,\qquad -1<\nu_s<0.5,\qquad f_y>0.
\]

## 4.3 UHPC compression / initial stiffness

Independent inputs:

```text
Ec       UHPC initial Young modulus
nu_c     UHPC initial Poisson parameter used in initial A/D only
fc       uniaxial compression peak stress magnitude
eps_c0   uniaxial compression peak strain magnitude
```

Require

\[
E_c>0,\qquad -1<\nu_c<0.5,\qquad f_c>0,\qquad \varepsilon_{c0}>0.
\]

No structure-level relation `Ec=Ec(fc)` is imposed.

## 4.4 UHPC tensile anchors

Five material-source points are required:

\[
(\varepsilon_0,s_0)=(0,0),
\]

\[
(\varepsilon_1,s_1)=(\varepsilon_{t,cr},f_{t,cr}),
\]

\[
(\varepsilon_2,s_2)=(\varepsilon_{t,p},f_{t,p}),
\]

\[
(\varepsilon_3,s_3)=(\varepsilon_{t,l},f_{t,l}),
\]

\[
(\varepsilon_4,s_4)=(\varepsilon_{t,lim},0).
\]

Require

\[
0<\varepsilon_1<\varepsilon_2<\varepsilon_3<\varepsilon_4,
\]

\[
0<s_1\le s_2,\qquad 0<s_3\le s_2.
\]

Current representative material defaults are

```text
eps_t_cr   = 0.000420
ft_cr      = 9.767718 MPa

eps_t_peak = 0.003800
ft_peak    = 10.734818 MPa

eps_t_loc  = 0.006900
ft_loc     = 10.347978 MPa

eps_t_lim  = 0.007590
```

These are material defaults, not specimen-specific calibration values. If a source-specific UHPC fibre series is known, change the tensile anchors at the material-input layer only. Do not choose them from structural Pu agreement.

## 4.5 Software label

`specimen_id`, if present, is a label only. No equation in R13 contains `specimen_id`.

---

# 5. Global mode and imperfection amplitude

Define

\[
\psi(x,y)=\sin(\alpha x)\sin(\beta y),
\]

\[
\boxed{\alpha=\frac{\pi}{b}},
\qquad
\boxed{\beta=\frac{m\pi}{a}}.
\]

Stress-free initial and added global fields:

\[
w_0=bq_0\psi,
\qquad
\Delta w=bq\psi,
\]

\[
\boxed{q_0=\frac{A_{0g}}{b}}.
\]

Define the Marguerre amplitude combination

\[
\boxed{Q(q)=q(q+2q_0)}.
\]

`a` is always the full physical axial length. The selected longitudinal half-wave length is

\[
\ell=\frac{a}{m^*}.
\]

---

# 6. Initial full-composite A/D operator

Define

\[
K_s=\frac{E_s}{1-\nu_s^2},
\qquad
K_c=\frac{E_c}{1-\nu_c^2},
\]

\[
G_s=\frac{E_s}{2(1+\nu_s)},
\qquad
G_c=\frac{E_c}{2(1+\nu_c)}.
\]

Initial membrane stiffness terms:

\[
\boxed{A_{11}=2t_sK_s+(1-\rho_w)t_cK_c},
\]

\[
\boxed{A_{22}=A_{11}+\rho_wt_cE_s},
\]

\[
\boxed{A_{12}=2t_s\nu_sK_s+(1-\rho_w)t_c\nu_cK_c}.
\]

The two steel faces contribute

\[
\boxed{D_f=2K_s\left(\frac{t_s^3}{12}+t_sz_f^2\right)}.
\]

UHPC and longitudinal-web contributions:

\[
D_c=(1-\rho_w)K_c\frac{t_c^3}{12},
\]

\[
D_w=\rho_wE_s\frac{t_c^3}{12}.
\]

Thus

\[
\boxed{D_x=D_f+D_c},
\]

\[
\boxed{D_y=D_x+D_w},
\]

\[
\boxed{D_\mu=\nu_sD_f+\nu_cD_c},
\]

\[
D_{66}=2G_s\left(\frac{t_s^3}{12}+t_sz_f^2\right)
+(1-\rho_w)G_c\frac{t_c^3}{12},
\]

\[
\boxed{H=D_\mu+2D_{66}}.
\]

`Ec,nu_c` enter this initial elastic composite front. The nonlinear UHPC section stress law used later is scalar and is defined separately in Sections 17–20.

---

# 7. Exact positive-integer global mode selection

For any positive integer `m`,

\[
\beta_m=\frac{m\pi}{a},
\]

\[
\boxed{
N_{cr,m}=\frac{D_x\alpha^4+2H\alpha^2\beta_m^2+D_y\beta_m^4}{\beta_m^2}
},
\]

\[
\boxed{P_{cr,m}=bN_{cr,m}}.
\]

Since

\[
N_{cr,m}=\frac{A}{m^2}+C_0+Bm^2,
\]

with positive `A,B`, the positive continuous minimizer is

\[
\boxed{m_c=\frac{a}{b}\left(\frac{D_x}{D_y}\right)^{1/4}}.
\]

Therefore the exact positive-integer minimizer is among

\[
\boxed{m_1=\max(1,\lfloor m_c\rfloor)},
\]

\[
\boxed{m_2=m_1+1}.
\]

Evaluate both and set

\[
\boxed{m^*=\arg\min_{m\in\{m_1,m_2\}}P_{cr,m}}.
\]

There is no fixed `m<=12` or `m<=40` cutoff.

Define

\[
\Delta_A=A_{11}A_{22}-A_{12}^2,
\qquad
\beta=\frac{m^*\pi}{a}.
\]

Then

\[
\boxed{K_x=\frac{b^2\alpha^2}{8(A_{22}/\Delta_A)}},
\]

\[
\boxed{G=\frac{b^2\beta^2}{8(A_{11}/\Delta_A)}},
\]

\[
\boxed{
C=\frac{b^3\Delta_A}{16\beta^2}
\left(\frac{\alpha^4}{A_{22}}+\frac{\beta^4}{A_{11}}\right)
},
\]

\[
\boxed{J_x=b(D_x\alpha^2+D_\mu\beta^2)},
\]

\[
\boxed{J_y=b(D_\mu\alpha^2+D_y\beta^2)}.
\]

Units:

```text
Pcr  N
Kx,G N/mm
C    N
Jx,Jy N
```

---

# 8. Marguerre–Airy generalized demand

The total axial-load relation is

\[
\boxed{P(q)=P_{cr}\frac{q}{q+q_0}+CQ(q)}.
\]

For `q>0` and `q0=0`, interpret the first factor as its perfect-panel limit `Pcr`.

The retained generalized demand is

\[
\boxed{N_x^A=K_xQ},
\]

\[
\boxed{M_x^A=J_xq},
\]

\[
\boxed{N_y^A=-\left[\frac{P(q)}{b}-GQ\right]},
\]

\[
\boxed{M_y^A=J_yq}.
\]

These have the same units as the section resultants in Section 22.

---

# 9. Current generalized section kinematics — explicit face mapping

The current capacity-contact section unknowns are

\[
(q,\varepsilon_x^0,\kappa_x,\varepsilon_y^0,\kappa_y).
\]

Core through-thickness strains are affine:

\[
\boxed{\varepsilon_x(z)=\varepsilon_x^0+\kappa_x z},
\]

\[
\boxed{\varepsilon_y(z)=\varepsilon_y^0+\kappa_y z}.
\]

Upper/lower UHPC core endpoint strains:

\[
\boxed{\varepsilon_x^{U,+}=\varepsilon_x^0+\kappa_x\frac{t_c}{2}},
\qquad
\boxed{\varepsilon_x^{U,-}=\varepsilon_x^0-\kappa_x\frac{t_c}{2}},
\]

\[
\boxed{\varepsilon_y^{U,+}=\varepsilon_y^0+\kappa_y\frac{t_c}{2}},
\qquad
\boxed{\varepsilon_y^{U,-}=\varepsilon_y^0-\kappa_y\frac{t_c}{2}}.
\]

Upper/lower steel-face **centroid** strains passed to R04/R02/R06 are

\[
\boxed{e_x^+=\varepsilon_x^0+\kappa_x z_f},
\qquad
\boxed{e_x^-=\varepsilon_x^0-\kappa_x z_f},
\]

\[
\boxed{e_y^+=\varepsilon_y^0+\kappa_y z_f},
\qquad
\boxed{e_y^-=\varepsilon_y^0-\kappa_y z_f}.
\]

At the current axial terminal, imposed uniform engineering shear is

\[
\gamma_{xy}=0.
\]

## 9.1 Critical current-theory boundary

In R13/R12, `kappa_x,kappa_y` are **independent generalized section-curvature unknowns solved from N/M closure**.

Do **not** impose

\[
\kappa_x=bq\alpha^2,
\qquad
\kappa_y=bq\beta^2
\]

inside R13. That relation belongs to a separate deformation-compatible `q -> kappa^g` research branch that is not the current frozen capacity-contact identity.

A new implementation that silently replaces the independent `kappa_x,kappa_y` by geometric q-curvatures is implementing a different theory.

---

# 10. R02 local geometry and sign convention

Local physical coordinates are

\[
0\le\xi_\ell\le L_x,
\qquad
0\le\zeta_\ell\le L_y.
\]

Local shape:

\[
\phi_\ell=(1-\cos k_x\xi_\ell)(1-\cos k_y\zeta_\ell),
\]

\[
\boxed{k_x=\frac{2\pi}{L_x}},
\qquad
\boxed{k_y=\frac{2\pi}{L_y}}.
\]

Exact local mean coefficients:

\[
\boxed{c_x=\frac{3k_x^2}{8}},
\qquad
\boxed{c_y=\frac{3k_y^2}{8}}.
\]

Define

\[
D_s=\frac{E_st_s^3}{12(1-\nu_s^2)},
\]

\[
\boxed{K_b=D_s\left[\frac34(k_x^4+k_y^4)+\frac12k_x^2k_y^2\right]}.
\]

Local amplitude variable:

\[
U\ge0,
\]

\[
\boxed{d=U^2-A_{0\ell}^2}.
\]

## 10.1 Tension-positive R13 form versus historical compression-positive R02 form

Historical R02 source files often wrote compression-positive normal strain. R13 uses tension-positive strain everywhere.

If historical compression-positive quantities are denoted with superscript `c`, then

\[
e_i=-e_i^c,\qquad m_i=-m_i^c.
\]

Therefore the R13 tension-positive local means are

\[
\boxed{m_x=e_x+c_xd},
\]

\[
\boxed{m_y=e_y+c_yd}.
\]

This plus sign is the sign-converted form of the historical compression-positive relation and must not be flipped again.

Let

\[
\boxed{Q_s=\frac{E_s}{1-\nu_s^2}}.
\]

Mean tension-positive stresses are

\[
\boxed{\bar\sigma_x=Q_s(m_x+\nu_sm_y)},
\]

\[
\boxed{\bar\sigma_y=Q_s(m_y+\nu_sm_x)}.
\]

---

# 11. R02 nonnegative cubic active set

The exact LL harmonic set is

```text
(r,s,c_rs)
(0,1,+1/2)
(0,2,-1/2)
(1,0,+1/2)
(1,1,-1)
(1,2,+1/2)
(2,0,-1/2)
(2,1,+1/2)
```

Define

\[
\boxed{
K_A=k_x^4k_y^4\left[
\frac{17}{256k_y^4}
+\frac{17}{256k_x^4}
+\frac1{8(k_x^2+k_y^2)^2}
+\frac1{32(k_x^2+4k_y^2)^2}
+\frac1{32(4k_x^2+k_y^2)^2}
\right]
}.
\]

The stationary amplitude equation is

\[
\boxed{B_3U^3+B_1U+B_0=0},
\]

with

\[
\boxed{B_3=4t_sE_sK_A+2t_sQ_s(c_x^2+2\nu_sc_xc_y+c_y^2)},
\]

\[
\boxed{
B_1=K_b-A_{0\ell}^2B_3
+2t_sQ_s(c_xe_x+\nu_sc_xe_y+\nu_sc_ye_x+c_ye_y)
},
\]

\[
\boxed{B_0=-A_{0\ell}K_b}.
\]

Candidate set:

\[
\boxed{
\mathcal U=\{0\}\cup\{U\ge0:\ B_3U^3+B_1U+B_0=0,\ U\in\mathbb R\}
}.
\]

Condensed energy, up to an irrelevant state-only constant:

\[
\boxed{
\Pi(U)=\frac{B_3}{4}U^4+\frac{B_1}{2}U^2+B_0U
}.
\]

Select

\[
\boxed{U^*=\arg\min_{U\in\mathcal U}\Pi(U)}.
\]

R02 is therefore an all-real-root cubic active set, not amplitude stepping.

---

# 12. Generic continuous R02 local stress field — complete inline form

Define local cosine variables

\[
\boxed{u=\cos(k_x\xi_\ell)},
\qquad
\boxed{v=\cos(k_y\zeta_\ell)},
\]

\[
(u,v)\in[-1,1]^2.
\]

Use

\[
T_0(s)=1,
\qquad
T_1(s)=s,
\qquad
T_2(s)=2s^2-1.
\]

For every harmonic `(r,s,c_rs)` in Section 11 define

\[
\boxed{\Lambda_{rs}=\left[(rk_x)^2+(sk_y)^2\right]^2},
\]

and the local LL Airy coefficient

\[
\boxed{
\mathcal F_{rs}=\frac{E_s d\,k_x^2k_y^2 c_{rs}}{\Lambda_{rs}}
}.
\]

The local tension-positive normal stresses are

\[
\boxed{
\sigma_x(u,v)=\bar\sigma_x
-\sum_{(r,s)}\mathcal F_{rs}(sk_y)^2T_r(u)T_s(v)
},
\]

\[
\boxed{
\sigma_y(u,v)=\bar\sigma_y
-\sum_{(r,s)}\mathcal F_{rs}(rk_x)^2T_r(u)T_s(v)
}.
\]

Only `(1,1),(1,2),(2,1)` contribute to local shear. Write

\[
\boxed{
\tau_{xy}(u,v)=\sqrt{1-u^2}\sqrt{1-v^2}\,P_\tau(u,v)
},
\]

with

\[
\boxed{
P_\tau(u,v)
=-k_xk_y\left[
\mathcal F_{11}+4\mathcal F_{12}v+4\mathcal F_{21}u
\right]
}.
\]

This notation deliberately avoids the global stiffness symbols `A11,A12`.

Define the Mises-square polynomial

\[
\boxed{
\Phi(u,v)=\sigma_x^2-\sigma_x\sigma_y+\sigma_y^2+3\tau_{xy}^2
}.
\]

Since

\[
\tau_{xy}^2=(1-u^2)(1-v^2)P_\tau^2,
\]

`Phi` is an ordinary finite bivariate polynomial of total degree no greater than six.

---

# 13. Exact generic local Mises maximum

The formal maximum of `Phi` on the closed square is obtained from a finite algebraic candidate set.

## 13.1 Interior

Solve

\[
\boxed{\Phi_{,u}=0},
\qquad
\boxed{\Phi_{,v}=0},
\]

and retain all real roots satisfying

\[
-1<u<1,\qquad -1<v<1.
\]

A formal elimination backend may form

\[
\boxed{R_u(u)=\operatorname{Res}_v(\Phi_{,u},\Phi_{,v})},
\]

enumerate all real roots `u`, recover common real `v`, and verify both derivative residuals.

## 13.2 Edges

At `u=+1,-1`, solve all real roots

\[
\boxed{\frac{d}{dv}\Phi(\pm1,v)=0},\qquad -1<v<1.
\]

At `v=+1,-1`, solve all real roots

\[
\boxed{\frac{d}{du}\Phi(u,\pm1)=0},\qquad -1<u<1.
\]

## 13.3 Corners

Always include

\[
(-1,-1),\ (-1,1),\ (1,-1),\ (1,1).
\]

## 13.4 Maximum

Let the admitted union be `C_Phi`. Then

\[
\boxed{
\Phi_{max}=\max_{(u,v)\in\mathcal C_\Phi}\Phi(u,v)
}.
\]

No spatial stress grid or effective width is part of the formal operator.

---

# 14. Automatic R04/R06 event-order gate

Define

\[
\boxed{r_c=\frac{L_y}{L_x}},
\]

where `r_c` is a local-cell aspect ratio and is unrelated to the harmonic index `r`.

\[
\boxed{k_{cr}=\frac{4(3r_c^4+2r_c^2+3)}{3r_c^2}},
\]

\[
\boxed{
\sigma_{cr,s}^{E}
=\frac{\pi^2E_st_s^2}{12(1-\nu_s^2)L_x^2}k_{cr}
}.
\]

Mechanical event order:

```text
sigma_cr,s^E >= fy  -> R04_YIELD_FIRST
sigma_cr,s^E <  fy  -> R06_LOCAL_BUCKLING_FIRST
```

No specimen name enters this decision.

---

# 15. R04 yield-first steel-face law

For one face strain pair `(e_x,e_y)` and zero imposed terminal engineering shear:

\[
\boxed{\sigma_x^{tr}=Q_s(e_x+\nu_se_y)},
\]

\[
\boxed{\sigma_y^{tr}=Q_s(e_y+\nu_se_x)}.
\]

With `tau_xy^tr=0` in the current axial terminal, the general Mises form is

\[
\boxed{
\sigma_{VM}^{tr}=\sqrt{(\sigma_x^{tr})^2-\sigma_x^{tr}\sigma_y^{tr}+(\sigma_y^{tr})^2+3(\tau_{xy}^{tr})^2}
}.
\]

Radial ideal elastic-perfectly-plastic steel cap:

\[
\boxed{\lambda_p=\min\left(1,\frac{f_y}{\sigma_{VM}^{tr}}\right)},
\]

\[
\boxed{\boldsymbol\sigma_s=\lambda_p\boldsymbol\sigma_s^{tr}}.
\]

This ideal-EP law applies to steel, not UHPC.

---

# 16. R06 local-buckling-first steel-face law

For one fixed current face strain direction

\[
\mathbf e_f=(e_x,e_y),
\]

define the path-free radial family

\[
\boxed{\mathbf e_f(\lambda)=\lambda\mathbf e_f},
\qquad 0\le\lambda\le1.
\]

For every `lambda`:

1. use `lambda e_x, lambda e_y` in the R02 coefficients;
2. rebuild `B1`;
3. enumerate all nonnegative R02 cubic candidates;
4. choose `U*(lambda)` by the same condensed energy;
5. build the complete local polynomial field in Sections 12–13;
6. obtain `Phi_max(lambda)`.

Define

\[
\boxed{\Psi(\lambda)=\Phi_{max}(\lambda)-f_y^2}.
\]

If

\[
\Psi(1)\le0,
\]

retain the full current R02 mean state and set the radial factor to `1`.

If

\[
\Psi(1)>0,
\]

define first radial local yield

\[
\boxed{
\lambda_y=\min\{\lambda\in(0,1]:\Psi(\lambda)=0\}
}.
\]

The R06 gross/full-width face stress is

\[
\boxed{
\bar{\boldsymbol\sigma}_{R06}(\mathbf e_f)
=\bar{\boldsymbol\sigma}_{R02}(\lambda_y\mathbf e_f)
}.
\]

Historical notation mapping:

\[
\boxed{\lambda_y\equiv\eta_y\ \text{in earlier R06 files}}.
\]

No reduced width or reduced area is introduced.

The formal implementation should enumerate the same algebraic candidate events; a numerical evaluator may solve the exact `Psi(lambda)=0` equation but may not replace it by a sampled/fitted surrogate.

---

# 17. R13/R12 UHPC compression polynomial

For compression

\[
-\varepsilon_{c0}\le\varepsilon<0,
\]

define

\[
\boxed{\xi=-\frac{\varepsilon}{\varepsilon_{c0}}},
\qquad 0\le\xi\le1.
\]

Define

\[
\boxed{A_c=\frac{E_c\varepsilon_{c0}}{f_c}},
\]

\[
\boxed{B_c=6-5A_c},
\qquad
\boxed{C_c=4A_c-5}.
\]

Current source-shape gate:

\[
\boxed{0<A_c\le1.5}.
\]

Signed compression stress:

\[
\boxed{
\sigma_c(\varepsilon)
=-f_c\left(A_c\xi+B_c\xi^5+C_c\xi^6\right)
}.
\]

Exact endpoint conditions:

\[
\sigma_c(0)=0,
\qquad
\left.\frac{d\sigma_c}{d\varepsilon}\right|_{0^-}=E_c,
\]

\[
\sigma_c(-\varepsilon_{c0})=-f_c,
\qquad
\left.\frac{d\sigma_c}{d\varepsilon}\right|_{-\varepsilon_{c0}}=0.
\]

No post-peak compression branch is used. A state with

\[
\varepsilon<-\varepsilon_{c0}
\]

is outside the current capacity-contact domain.

Compression primitives satisfying `F0'=sigma` and `F1'=epsilon sigma`:

\[
\boxed{
F_{0c}(\varepsilon)=f_c\varepsilon_{c0}
\left(\frac{A_c}{2}\xi^2+\frac{B_c}{6}\xi^6+\frac{C_c}{7}\xi^7\right)
},
\]

\[
\boxed{
F_{1c}(\varepsilon)=-f_c\varepsilon_{c0}^2
\left(\frac{A_c}{3}\xi^3+\frac{B_c}{7}\xi^7+\frac{C_c}{8}\xi^8\right)
}.
\]

---

# 18. Hiew-anchor cubic-Hermite UHPC tension

Use the five nodes from Section 4.4.

Define interval lengths and secants

\[
\boxed{h_i=\varepsilon_{i+1}-\varepsilon_i},
\]

\[
\boxed{d_i=\frac{s_{i+1}-s_i}{h_i}},
\qquad i=0,1,2,3.
\]

Endpoint slopes:

\[
\boxed{m_0=E_c},
\qquad
\boxed{m_4=0}.
\]

Require the origin shape gate

\[
\boxed{0<E_c\le3d_0}.
\]

For internal nodes `i=1,2,3`:

if

\[
d_{i-1}d_i\le0,
\]

set

\[
\boxed{m_i=0}.
\]

Otherwise

\[
w_1=2h_i+h_{i-1},
\qquad
w_2=h_i+2h_{i-1},
\]

\[
\boxed{
m_i=\frac{w_1+w_2}{w_1/d_{i-1}+w_2/d_i}
}.
\]

On tensile interval `i`, define

\[
\boxed{\theta=\frac{\varepsilon-\varepsilon_i}{h_i}},
\qquad 0\le\theta\le1.
\]

Stress polynomial:

\[
\boxed{
\sigma_t(\varepsilon)=c_{i0}+c_{i1}\theta+c_{i2}\theta^2+c_{i3}\theta^3
},
\]

where

\[
c_{i0}=s_i,
\]

\[
c_{i1}=h_im_i,
\]

\[
c_{i2}=-3s_i+3s_{i+1}-2h_im_i-h_im_{i+1},
\]

\[
c_{i3}=2s_i-2s_{i+1}+h_im_i+h_im_{i+1}.
\]

For

\[
\varepsilon\ge\varepsilon_{t,lim},
\]

set

\[
\boxed{\sigma_t=0}.
\]

The construction is `C1` at all tensile nodes and joins the zero-stress tail with zero tangent.

---

# 19. Complete scalar UHPC operator and exact tensile primitives

## 19.1 Scalar operator identity

The current nonlinear UHPC capacity-contact phase is a **direction-by-direction scalar section operator**:

\[
\boxed{\sigma_x^U(z)=\sigma_U(\varepsilon_x(z))},
\]

\[
\boxed{\sigma_y^U(z)=\sigma_U(\varepsilon_y(z))}.
\]

There is no nonlinear cross-term such as

\[
\sigma_x^U=\sigma_x^U(\varepsilon_x,\varepsilon_y)
\]

in R13.

`nu_c` belongs to the initial elastic A/D operator only. A new AI must **not** reinsert a nonlinear Poisson coupling into the scalar R13 section stress law unless a later theory explicitly supersedes R13.

The scalar stress function is

\[
\boxed{
\sigma_U(\varepsilon)=
\begin{cases}
\sigma_c(\varepsilon),&-\varepsilon_{c0}\le\varepsilon<0,\\
\sigma_t(\varepsilon),&0\le\varepsilon<\varepsilon_{t,lim},\\
0,&\varepsilon\ge\varepsilon_{t,lim}.
\end{cases}
}
\]

## 19.2 Tensile primitives

On interval `i` define

\[
\mathcal A_i(\theta)=
 c_{i0}\theta+
 \frac{c_{i1}}2\theta^2+
 \frac{c_{i2}}3\theta^3+
 \frac{c_{i3}}4\theta^4,
\]

\[
\mathcal B_i(\theta)=
 \frac{c_{i0}}2\theta^2+
 \frac{c_{i1}}3\theta^3+
 \frac{c_{i2}}4\theta^4+
 \frac{c_{i3}}5\theta^5.
\]

Incremental primitives measured from the left node:

\[
\boxed{\Delta F_{0,i}=h_i\mathcal A_i(\theta)},
\]

\[
\boxed{
\Delta F_{1,i}=h_i\varepsilon_i\mathcal A_i(\theta)+h_i^2\mathcal B_i(\theta)
}.
\]

Define cumulative values at each left node by summing all completed previous intervals:

\[
F_{0t}(\varepsilon)=
\sum_{j<i}h_j\mathcal A_j(1)+h_i\mathcal A_i(\theta),
\]

\[
F_{1t}(\varepsilon)=
\sum_{j<i}\left[h_j\varepsilon_j\mathcal A_j(1)+h_j^2\mathcal B_j(1)\right]
+h_i\varepsilon_i\mathcal A_i(\theta)+h_i^2\mathcal B_i(\theta).
\]

At and beyond `eps_t_lim`, hold both primitives constant because `sigma_t=0`.

The complete primitive functions are therefore

\[
F_0(\varepsilon)=
\begin{cases}
F_{0c}(\varepsilon),&-\varepsilon_{c0}\le\varepsilon<0,\\
F_{0t}(\varepsilon),&\varepsilon\ge0,
\end{cases}
\]

\[
F_1(\varepsilon)=
\begin{cases}
F_{1c}(\varepsilon),&-\varepsilon_{c0}\le\varepsilon<0,\\
F_{1t}(\varepsilon),&\varepsilon\ge0.
\end{cases}
\]

with

\[
F_0(0)=F_1(0)=0.
\]

No Gamma, hypergeometric, logarithmic or arctangent material primitive remains.

---

# 20. Exact UHPC continuous-thickness resultants

For either direction `i=x,y`, use

\[
\varepsilon_i(z)=\varepsilon_i^0+\kappa_i z,
\]

\[
\varepsilon_i^\pm=\varepsilon_i^0\pm\kappa_i\frac{t_c}{2}.
\]

For

\[
\kappa_i\ne0,
\]

\[
\boxed{
N_i^U=(1-\rho_w)
\frac{F_0(\varepsilon_i^+)-F_0(\varepsilon_i^-)}{\kappa_i}
},
\]

\[
\boxed{
M_i^U=(1-\rho_w)
\frac{
F_1(\varepsilon_i^+)-F_1(\varepsilon_i^-)
-\varepsilon_i^0[F_0(\varepsilon_i^+)-F_0(\varepsilon_i^-)]
}{\kappa_i^2}
}.
\]

For

\[
\kappa_i=0,
\]

use the exact continuous limit

\[
\boxed{N_i^U=(1-\rho_w)t_c\sigma_U(\varepsilon_i^0)},
\]

\[
\boxed{M_i^U=0}.
\]

No through-thickness quadrature is used.

---

# 21. Longitudinal web ideal-EP operator

Web strain follows the same generalized axial section field:

\[
\boxed{\varepsilon_y^w(z)=\varepsilon_y^0+\kappa_y z}.
\]

Steel law:

\[
\boxed{
\sigma_y^w(z)=\operatorname{clip}(E_s\varepsilon_y^w(z),-f_y,+f_y)
}.
\]

Exact elastic/yield crossings are obtained from

\[
\varepsilon_y^w=\pm\frac{f_y}{E_s}.
\]

If a crossing lies in

\[
[-t_c/2,t_c/2],
\]

split the analytic integral at that exact coordinate.

Elastic subinterval `[za,zb]`:

\[
\int_{z_a}^{z_b}\sigma dz
=E_s\left[\varepsilon_y^0(z_b-z_a)+\frac{\kappa_y}{2}(z_b^2-z_a^2)\right],
\]

\[
\int_{z_a}^{z_b}z\sigma dz
=E_s\left[\frac{\varepsilon_y^0}{2}(z_b^2-z_a^2)+\frac{\kappa_y}{3}(z_b^3-z_a^3)\right].
\]

Yielded subinterval with sign `s_y=+1` or `-1`:

\[
\int_{z_a}^{z_b}\sigma dz=s_yf_y(z_b-z_a),
\]

\[
\int_{z_a}^{z_b}z\sigma dz=\frac{s_yf_y}{2}(z_b^2-z_a^2).
\]

Multiply the total thickness integrals by `rho_w`:

\[
\boxed{N_y^w=\rho_w\int_{-t_c/2}^{t_c/2}\sigma_y^w dz},
\]

\[
\boxed{M_y^w=\rho_w\int_{-t_c/2}^{t_c/2}z\sigma_y^w dz}.
\]

There is no transverse web term in the current physical web orientation.

---

# 22. Total section generalized forces

Let the upper/lower current steel-face mean stresses after R04 or R06 be

\[
(\sigma_x^+,\sigma_y^+),
\qquad
(\sigma_x^-,\sigma_y^-).
\]

Then

\[
\boxed{N_x=N_x^U+t_s(\sigma_x^++\sigma_x^-)},
\]

\[
\boxed{M_x=M_x^U+t_sz_f(\sigma_x^+-\sigma_x^-)},
\]

\[
\boxed{N_y=N_y^U+t_s(\sigma_y^++\sigma_y^-)+N_y^w},
\]

\[
\boxed{M_y=M_y^U+t_sz_f(\sigma_y^+-\sigma_y^-)+M_y^w}.
\]

`(1-rho_w)` in the UHPC operator and `rho_w` in the web operator appear exactly once.

---

# 23. Axial UHPC compression-contact closure

The active R13 terminal chooses the section orientation

\[
\boxed{\kappa_y\ge0}
\]

so the lower core endpoint `z=-tc/2` is the axial compression-control side. The mirrored solution has the same symmetric-section capacity and is not treated as a second physical branch.

Terminal condition:

\[
\boxed{
\varepsilon_y^{U,-}
=\varepsilon_y^0-\kappa_y\frac{t_c}{2}
=-\varepsilon_{c0}
}.
\]

Therefore

\[
\boxed{
\varepsilon_y^0=-\varepsilon_{c0}+\kappa_y\frac{t_c}{2}
}.
\]

This eliminates `eps_y0` and leaves four unknowns

\[
\boxed{(q,\varepsilon_x^0,\kappa_x,\kappa_y)}.
\]

Four equilibrium equations:

\[
\boxed{R_1=N_x-N_x^A=0},
\]

\[
\boxed{R_2=M_x-M_x^A=0},
\]

\[
\boxed{R_3=N_y-N_y^A=0},
\]

\[
\boxed{R_4=M_y-M_y^A=0}.
\]

A numerical implementation may scale moment residuals by a positive constant such as `zf`; this changes conditioning only and does not change the equations.

---

# 24. Root admission, terminal scope and Pu selection

A compression-contact candidate is admissible only if

```text
q > 0
kappa_y >= 0
all four original N/M equations are satisfied
all UHPC core compression endpoints >= -eps_c0
all UHPC tensile endpoints <= eps_t_lim
R04/R06 event gate is obeyed
R02 uses the minimum-energy nonnegative cubic candidate
web subintervals are split only at exact yield crossings
```

Among all admissible compression-contact roots, select

\[
\boxed{q_u=\min(q>0)}.
\]

Then

\[
\boxed{P_u=P(q_u)}.
\]

## 24.1 Terminal-domain boundary

R13 is currently a **y-direction compression-contact** capacity theory.

If a candidate requires an UHPC strain below `-eps_c0`, it is inadmissible.

If a tensile endpoint reaches or exceeds `eps_t_lim` before an admissible axial compression-contact root, return

```text
UHPC_TENSION_FIRST_TERMINAL_NOT_CLOSED
```

rather than extending the tensile law or switching theories.

Likewise, if a non-axial UHPC compression terminal controls first in a user-defined geometry, that case is outside the current y-compression-contact closure and must be reported as outside the current terminal scope rather than repaired by a fitted rule.

The current workbook is intended for compression-controlled axial panels and enforces endpoint-domain gates at the accepted compression-contact root.

---

# 25. Formal solver identity versus current executable evaluator

The **theory** consists of the equations and finite event sets above.

Formal algebraic target:

```text
R02: cubic all-real roots
R06 local maximum: resultant / univariate edge roots / corners
R06 radial first-yield: algebraic event elimination where practical
section terminal: all admissible physical roots
selection: smallest positive q
```

The current Excel executable is a transparent numerical evaluator of the same equations. It may use:

```text
numpy polynomial roots for univariate polynomial equations
scipy root for exact interior stationary equations with residual verification
brentq for the exact R06 radial first-crossing equation
scipy root for the exact four section residual equations with physical admission checks
```

These numerical calls have **no material or structural theory identity**. They do not authorize stress grids, fitted radial-factor surrogates, stored roots or Pu lookup.

The final zero-iteration algebraic backend, if later substituted, must solve the same R13 equations and preserve the same physical root-selection rules.

---

# 26. Standalone implementation sequence for a new AI

A new AI with only this ledger and one complete input set shall proceed in this exact order.

1. Read the unit/sign convention in Section 2.
2. Read the reserved-symbol rules in Section 3 before coding.
3. Validate all geometry, steel and UHPC input gates in Section 4.
4. Compute `q0,rho_w,zf`.
5. Compute the initial A/D terms in Section 6.
6. Compute `m_c,m1,m2,m*` exactly as in Section 7.
7. Compute `Pcr,Kx,G,C,Jx,Jy`.
8. Build the Airy load/resultant demand in Section 8.
9. For each trial section state, impose the explicit steel-face centroid strain mapping in Section 9.
10. Compute local `kx,ky,cx,cy,Kb,KA`.
11. Compute `sigma_cr,s^E` and select R04 or R06 mechanically.
12. If R04: evaluate the plane-stress trial and radial steel cap.
13. If R06: build R02 cubic candidates, select `U*`, construct the complete local 2D field, enumerate the Mises candidates, then apply the first radial local-yield projection if required.
14. Generate UHPC compression coefficients `Ac,Bc,Cc` and enforce the shape gate.
15. Generate Hiew node slopes and the four cubic tensile segments.
16. Generate the complete UHPC `F0,F1` primitives.
17. Evaluate exact UHPC x/y continuous-thickness resultants using the scalar directional operator.
18. Evaluate web resultants using exact yield crossings.
19. Assemble total `Nx,Mx,Ny,My`.
20. Impose the axial compression-contact relation to eliminate `eps_y0`.
21. Solve the four equilibrium equations for all candidate physical roots permitted by the chosen evaluator.
22. Reject every root violating the domain/event/admissibility rules.
23. Select the smallest positive-q admissible root.
24. Return `Pu=P(q)` plus the full audit state.

No historical markdown file is required in any of these steps.

---

# 27. Minimum transferable output/audit state

A compliant implementation shall expose at least

```text
INPUTS
b,a,tc,ts,A0g,Aw,Lx,Ly,A0l
Es,nu_s,fy
Ec,nu_c,fc,eps_c0
all tensile anchors

DERIVED GEOMETRY/MATERIAL
q0,rho_w,zf
Ac,Bc,Cc
Hiew hi,di,mi and all cubic coefficients

GLOBAL
Dx,Dy,Dmu,D66,H
mc,m1,m2,m*
Pcr,Kx,G,C,Jx,Jy

LOCAL STEEL
kx,ky,cx,cy,Kb,KA
sigma_cr,s^E
R04/R06 branch
for R02: B3,B1,B0, candidate roots, selected U
for R06: active (u,v), radial factor lambda_y
upper/lower face stresses

UHPC/WEB
UHPC endpoint strains
UHPC F0/F1 endpoint values
UHPC Nx,Mx,Ny,My
web Ny,My

CLOSURE
total Nx,Mx,Ny,My
Airy target Nx,Mx,Ny,My
four original residuals
q
Pu
root count
status/failure reason
```

---

# 28. Excel implementation mapping

The current parameter-driven executable workbook uses the following logical mapping:

```text
00_README              identity and dependency contract
01_INPUT               one active geometry/material set + input gates
02_GLOBAL              initial A/D + exact integer mode + Airy
03_ENGINE              R02/R04/R06 + UHPC/web + nonlinear closure evaluator
04_CONSTITUENTS        phase resultants
05_CLOSURE             section/Airy residuals
06_OUTPUT              current calculated result
07_DEPENDENCY_AUDIT    arbitrary non-reference dependency tests
08_R12_MATERIAL        UHPC polynomial/tensile-anchor generator
09_INPUT_SCHEMA        standalone input dictionary
10_TRANSFER_CONTRACT   no-lookup/runtime-dependency contract
11_FINAL_AUDIT         final transfer/parameterization audit
```

The workbook may retain the executable identity `R12` because R13 changes notation/transfer definitions only and does not change the mechanical equations used by the R12 workbook.

---

# 29. Anti-lookup and parameter-driven contract

A compliant executable must satisfy

```text
ONE_ACTIVE_INPUT_SET = YES
REFERENCE_SPECIMEN_PARAMETER_DATABASE = NONE
REFERENCE_PU_TABLE = NONE
SPECIMEN_ID_IN_ENGINE = NO
BRANCH_BY_SPECIMEN_NAME = NO
MODE_BY_SPECIMEN_NAME = NO
ROOT_BY_REFERENCE_LOAD = NO
```

Changing any physical input must propagate through the equations.

A generic workbook may contain one arbitrary illustrative active input so formulas are visible, but it must not contain alternate historical specimen rows that the engine can select.

---

# 30. Required explicit failure statuses

At minimum:

```text
GEOMETRY_CONTRACT_FAIL
WEB_FRACTION_CONTRACT_FAIL
STEEL_MATERIAL_CONTRACT_FAIL
UHPC_BASIC_MATERIAL_CONTRACT_FAIL
UHPC_COMPRESSION_POLYNOMIAL_CONTRACT_FAIL
HIEW_TENSION_ANCHOR_CONTRACT_FAIL
R02_NO_ADMISSIBLE_NONNEGATIVE_CANDIDATE
R06_LOCAL_YIELD_ROOT_FAIL
UHPC_COMPRESSION_DOMAIN_EXCEEDED
UHPC_TENSION_FIRST_TERMINAL_NOT_CLOSED
AXIAL_COMPRESSION_TERMINAL_SCOPE_FAIL
NO_PHYSICAL_CAPACITY_CONTACT_ROOT
```

A failure is not permission to switch to another material law, another branch, a stored specimen result or a fitted correction.

---

# 31. Non-runtime provenance statement

The current equations were assembled historically from the project’s Marguerre–Airy global front, R02/R06 local steel theory, ideal-EP steel, and UHPC material-source studies. Those source files remain audit evidence.

However:

```text
HISTORICAL_MARKDOWN_RUNTIME_DEPENDENCY = NONE
HISTORICAL_MARKDOWN_REQUIRED_TO_REIMPLEMENT_R13 = NONE
```

A new AI may consult provenance files to audit source history, but it does not need them to know what equation to calculate.

---

# 32. Final standalone-readiness checklist

Before accepting a new implementation, verify all items below.

```text
[ ] every independent input is present and unit-labelled
[ ] geometry/material gates pass
[ ] rho_w is in [0,1)
[ ] Ac compression gate passes
[ ] Hiew origin/tension-anchor gates pass
[ ] global A/D uses nu_c only in the initial elastic front
[ ] nonlinear UHPC section uses scalar directional sigma_U(epsilon)
[ ] section kappa_x,kappa_y remain independent closure unknowns
[ ] steel-face centroid strains use +/- zf explicitly
[ ] R02 uses tension-positive +cx*d,+cy*d means
[ ] local harmonic indices are not confused with global q
[ ] local Airy coefficients are not confused with global A11/A12
[ ] R04/R06 branch comes only from sigma_cr,s^E versus fy
[ ] R06 maximum is from the full 2D finite polynomial candidate set
[ ] no local stress grid/effective width is introduced
[ ] UHPC thickness uses exact F0/F1 endpoint primitives
[ ] web uses exact yield-crossing integration
[ ] four original N/M equilibrium equations close
[ ] axial compression-contact condition is enforced
[ ] all material/event/domain conditions are checked
[ ] smallest positive-q admissible root is selected
[ ] Pu is computed from P(q), not read from a table
```

If these items pass, the implementation is mechanically identical to the current R13/R12 capacity-contact theory.

---

# 33. Current lock

```text
CURRENT_TRANSFER_LEDGER
= R13_FINAL_TRANSFER_AUDITED

MECHANICAL_BASELINE
= R12 equations unchanged

GLOBAL
= INITIAL COMPOSITE A/D
  + EXACT POSITIVE-INTEGER MODE
  + MARGUERRE-AIRY

SECTION KINEMATICS
= INDEPENDENT epsx0,kappax,epsy0,kappay
  + EXPLICIT +/- FACE CENTROID STRAINS

STEEL FACE
= AUTO(R04,R02/R06)

R02
= NONNEGATIVE CUBIC ALL-ROOT ACTIVE SET

R06
= FULL 2D FINITE LL AIRY POLYNOMIAL
  + INTERIOR/EDGE/CORNER MISES CANDIDATES
  + FIRST RADIAL LOCAL-YIELD PROJECTION

UHPC
= DIRECTION-BY-DIRECTION SCALAR SECTION OPERATOR
  + SIXTH-DEGREE COMPRESSION
  + HIEW-ANCHOR CUBIC-HERMITE TENSION
  + EXACT POLYNOMIAL THICKNESS PRIMITIVES

WEB
= LONGITUDINAL IDEAL EP
  + EXACT YIELD-CROSSING INTEGRATION

TERMINAL
= AXIAL LOWER-CORE FIRST COMPRESSION CONTACT

REFERENCE LOOKUP
= NONE

HISTORICAL MARKDOWN RUNTIME DEPENDENCY
= NONE
```

Compactly,

\[
\boxed{
\text{raw user inputs}
\to\text{gates}
\to A/D
\to m^*
\to\text{Airy}
\to\text{explicit face strains}
\to\operatorname{AUTO}(R04,R02/R06)
\to\text{scalar polynomial UHPC section}
\to\text{web}
\to N/M\text{ closure}
\to\text{axial compression contact}
\to q_u
\to P_u
}
\]

**This ledger is the current standalone text implementation contract for the steel-shell–UHPC axial capacity-contact prediction.**