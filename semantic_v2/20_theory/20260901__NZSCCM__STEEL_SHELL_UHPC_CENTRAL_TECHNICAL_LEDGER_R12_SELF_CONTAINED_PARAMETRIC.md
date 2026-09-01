# NZ-SCCM — 钢壳–UHPC 显式极限承载力集中技术总账 R12 — SELF-CONTAINED PARAMETRIC

**Date:** 2026-09-01  
**Working branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Production main:** unchanged  
**Current transfer identity:** `STEEL_SHELL_UHPC_R12_SELF_CONTAINED_PARAMETRIC`  
**Runtime dependence on historical markdown files:** `NONE`  
**Formal spatial quadrature:** `0`  
**Material-point grid:** `0`  
**Effective-width/effective-area repair:** prohibited  
**Comparator/test/FEM in material calibration or root selection:** `0`

---

# 0. Governing decision

R12 does **not** introduce a new structural theory. Relative to R11, it performs two implementation/governance completions only:

1. inline every equation required by the current axial steel-shell–UHPC capacity-contact calculation, especially the previously externally referenced generic R06 local-field reconstruction;
2. require the executable workbook to contain only **one active user-defined parameter set**, with no reference-specimen geometry table and no stored ultimate-load lookup.

The mechanical chain remains

```text
user-defined geometry/material inputs
-> initial full-composite A/D
-> exact positive-integer global mode selection
-> Marguerre–Airy Pcr,C,Kx,G,Jx,Jy
-> q, Q=q(q+2q0), Airy generalized N/M demand
-> automatic local steel event order
   -> R04_YIELD_FIRST
   -> or R02 + R06_LOCAL_BUCKLING_FIRST
-> R12 polynomial UHPC continuous-thickness section operator
-> longitudinal web ideal-EP continuous-thickness operator
-> total section N/M
-> four Airy/section balances
-> first admissible UHPC compression-contact terminal
-> q
-> Pu=P(q)
```

No historical file is required to evaluate this chain once this ledger and the input set are supplied. Historical files remain provenance/audit evidence only.

---

# 1. Applicability and hard boundaries

R12 is an **axial-compression plate/steel-shell capacity-contact model** with the following fixed scope:

```text
single continuous global half-wave family
integer longitudinal half-wave number m selected mechanically
zero imposed uniform in-plane shear at the axial terminal
affine through-thickness section strains
one registered rectangular local steel-face cell characterized by Lx,Ly,A0_local
R04/R06 steel material/event theory
R12 scalar UHPC section material
longitudinal web steel represented by area Aw distributed through the core thickness
```

R12 does not claim a general arbitrary-loading finite-element constitutive model.

The following remain prohibited:

```text
spatial Gauss/Simpson/adaptive integration
material-point grids
material history stepping as the formal theory
effective width/effective area
reference-specimen branch lookup
stored Pu lookup
FEM/test-based material fitting
FEM/test-based root selection
33-point eta sampling
fitted eta quintic surrogate
3x3x3 terminal cell search
8-level terminal refinement
```

A user may change the geometry/material parameters arbitrarily **inside the stated input contracts**. If the resulting state lies outside the model domain or no admissible capacity-contact root exists, the implementation must fail explicitly; it must never substitute a stored reference result.

---

# 2. Units, coordinates and signs

Use N–mm–MPa.

```text
x = transverse plate direction
y = axial loading direction
z = through thickness, positive toward the upper steel face
normal strain: tension positive
normal stress: tension positive
```

Global mode:

\[
\psi=\sin(\alpha x)\sin(\beta y),
\qquad
\alpha=\frac{\pi}{b},
\qquad
\beta=\frac{m\pi}{a}.
\]

Stress-free initial and added amplitudes:

\[
w_0=bq_0\psi,
\qquad
\Delta w=bq\psi,
\qquad
\boxed{q_0=\frac{A_{0g}}{b}}.
\]

Define

\[
\boxed{Q(q)=q(q+2q_0)}.
\]

---

# 3. Complete independent input contract

## 3.1 Geometry

\[
b>0,\quad a>0,\quad t_c>0,\quad t_s>0,
\]

```text
b          gross width
a          physical axial length
tc         UHPC core thickness
ts         thickness of each steel face
A0g        global initial-imperfection amplitude
Aw         longitudinal web steel area represented in the core
Lx         local steel-face cell dimension in x
Ly         local steel-face cell dimension in y
A0_local   local steel-face initial-imperfection amplitude
```

Derived

\[
\boxed{\rho_w=\frac{A_w}{bt_c}},
\qquad
\boxed{z_f=\frac{t_c+t_s}{2}}.
\]

Require

\[
0\le\rho_w<1.
\]

## 3.2 Steel

```text
Es
nu_s
fy
```

with

\[
E_s>0,\qquad -1<\nu_s<0.5,\qquad f_y>0.
\]

## 3.3 UHPC compression

```text
Ec
nu_c
fc
eps_c0
```

with positive scales. No structure-level relation `Ec=Ec(fc)` is imposed.

## 3.4 UHPC tension anchors

Five source points are used:

\[
(0,0),
\quad
(\varepsilon_{t,cr},f_{t,cr}),
\quad
(\varepsilon_{t,p},f_{t,p}),
\quad
(\varepsilon_{t,l},f_{t,l}),
\quad
(\varepsilon_{t,lim},0).
\]

Require

\[
0<\varepsilon_{t,cr}<\varepsilon_{t,p}<\varepsilon_{t,l}<\varepsilon_{t,lim},
\]

\[
0<f_{t,cr}\le f_{t,p},
\qquad
0<f_{t,l}\le f_{t,p}.
\]

The current representative Hiew/G16R material anchors are material defaults, not specimen-specific parameters:

```text
eps_t_cr   = 0.000420
ft_cr      = 9.767718 MPa

eps_t_peak = 0.003800
ft_peak    = 10.734818 MPa

eps_t_loc  = 0.006900
ft_loc     = 10.347978 MPa

eps_t_lim  = 0.007590
```

If a source-specific fibre series is known, replace these anchors at the material-input layer. Do not choose them from structural Pu agreement.

`specimen_id`, if present in software, is a label only and is not an input to any equation below.

---

# 4. Initial full-composite A/D operator

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

Membrane terms:

\[
\boxed{A_{11}=2t_sK_s+(1-\rho_w)t_cK_c},
\]

\[
\boxed{A_{22}=A_{11}+\rho_wt_cE_s},
\]

\[
\boxed{A_{12}=2t_s\nu_sK_s+(1-\rho_w)t_c\nu_cK_c}.
\]

Face bending contribution, with the face centroid offset included exactly once:

\[
\boxed{D_f=2K_s\left(\frac{t_s^3}{12}+t_sz_f^2\right)}.
\]

Core and longitudinal-web contributions:

\[
D_c=(1-\rho_w)K_c\frac{t_c^3}{12},
\qquad
D_w=\rho_wE_s\frac{t_c^3}{12}.
\]

\[
\boxed{D_x=D_f+D_c},
\qquad
\boxed{D_y=D_x+D_w}.
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

---

# 5. Exact positive-integer global mode selection

For any positive integer m,

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

There is no need for a fixed `m=1..12` or `m=1..40` truncation. Since

\[
N_{cr,m}=\frac{A}{m^2}+C_0+Bm^2,
\]

with positive A and B, the positive continuous minimizer is

\[
\boxed{
m_c=\frac{a}{b}\left(\frac{D_x}{D_y}\right)^{1/4}
}.
\]

The function decreases before \(m_c\) and increases after \(m_c\). Therefore the exact positive-integer minimum is among

\[
\boxed{m_1=\max(1,\lfloor m_c\rfloor)},
\qquad
\boxed{m_2=m_1+1}.
\]

Evaluate \(P_{cr,m_1}\) and \(P_{cr,m_2}\), and set

\[
\boxed{m^*=\arg\min_{m\in\{m_1,m_2\}}P_{cr,m}}.
\]

This makes mode selection fully parametric with no aspect-ratio-specific cutoff.

Let

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
\qquad
\boxed{J_y=b(D_\mu\alpha^2+D_y\beta^2)}.
\]

---

# 6. Marguerre–Airy generalized demand

\[
\boxed{P(q)=P_{cr}\frac{q}{q+q_0}+CQ(q)}.
\]

At the retained capacity-control section,

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

The same sign convention must be used on the demand and section sides.

---

# 7. R02 local steel-face operator — complete qU-off current capacity-contact form

R12 retains the source-audited common R02/R06 capacity-contact operator used by the present steel-shell branch. No qU augmentation is introduced here.

Local cell:

\[
0\le\xi\le L_x,
\qquad
0\le\eta\le L_y,
\]

\[
\phi=(1-\cos k_x\xi)(1-\cos k_y\eta),
\]

\[
\boxed{k_x=\frac{2\pi}{L_x}},
\qquad
\boxed{k_y=\frac{2\pi}{L_y}}.
\]

Exact local means:

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

The exact LL Airy harmonic set is

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

and

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

For a face-centroid tension-positive strain pair \((e_x,e_y)\), define

\[
d=U^2-A_0^2,
\]

\[
m_x=e_x+c_xd,
\qquad
m_y=e_y+c_yd,
\]

\[
Q_s=\frac{E_s}{1-\nu_s^2}.
\]

Mean stresses are

\[
\boxed{\bar\sigma_x=Q_s(m_x+\nu_sm_y)},
\]

\[
\boxed{\bar\sigma_y=Q_s(m_y+\nu_sm_x)}.
\]

The condensed stationary equation is

\[
\boxed{B_3U^3+B_1U+B_0=0},
\]

with

\[
\boxed{B_3=4t_sE_sK_A+2t_sQ_s(c_x^2+2\nu_sc_xc_y+c_y^2)},
\]

\[
\boxed{
B_1=K_b-A_0^2B_3
+2t_sQ_s(c_xe_x+\nu_sc_xe_y+\nu_sc_ye_x+c_ye_y)
},
\]

\[
\boxed{B_0=-A_0K_b}.
\]

The nonnegative-amplitude KKT-complete candidate set is

\[
\boxed{
\mathcal U=\{0\}\cup\{U\ge0:\ B_3U^3+B_1U+B_0=0,\ U\in\mathbb R\}
}.
\]

Evaluate the same condensed energy, up to an irrelevant state-dependent constant,

\[
\boxed{
\Pi(U)=\frac{B_3}{4}U^4+\frac{B_1}{2}U^2+B_0U
},
\]

and select

\[
\boxed{U^*=\arg\min_{U\in\mathcal U}\Pi(U)}.
\]

Thus R02 is a cubic all-real-root active set, not an amplitude stepping algorithm.

---

# 8. Generic R02 continuous local stress field — fully inlined

This section closes the previous standalone gap.

Define

\[
u=\cos(k_x\xi),
\qquad
v=\cos(k_y\eta),
\qquad
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

For each of the seven harmonic triples \((p,q,c_{pq})\), define

\[
\boxed{
\Lambda_{pq}=\left[(pk_x)^2+(qk_y)^2\right]^2
},
\]

\[
\boxed{
A_{pq}=\frac{E_sd\,k_x^2k_y^2\,c_{pq}}{\Lambda_{pq}}
}.
\]

Then the exact LL normal-stress field is

\[
\boxed{
\sigma_x(u,v)=\bar\sigma_x
-\sum_{(p,q)}A_{pq}(qk_y)^2T_p(u)T_q(v)
},
\]

\[
\boxed{
\sigma_y(u,v)=\bar\sigma_y
-\sum_{(p,q)}A_{pq}(pk_x)^2T_p(u)T_q(v)
}.
\]

Only the \((1,1),(1,2),(2,1)\) harmonics contribute to shear. Since

\[
\sin(2X)=2u\sqrt{1-u^2},
\qquad
\sin(2Y)=2v\sqrt{1-v^2},
\]

write

\[
\boxed{
\tau_{xy}(u,v)=\sqrt{1-u^2}\sqrt{1-v^2}\,P_\tau(u,v)
},
\]

where

\[
\boxed{
P_\tau(u,v)
=-k_xk_y\left[A_{11}+4A_{12}v+4A_{21}u\right]
}.
\]

The sign of \(P_\tau\) is immaterial to the Mises square but is retained for a complete field reconstruction.

Define

\[
\boxed{
\Phi(u,v)=\sigma_x^2-\sigma_x\sigma_y+\sigma_y^2+3\tau_{xy}^2
}.
\]

Because

\[
\tau_{xy}^2=(1-u^2)(1-v^2)P_\tau^2,
\]

\(\Phi\) is an ordinary finite bivariate polynomial in \(u,v\), with total degree no greater than six.

This formula is sufficient for a new implementation to reconstruct the complete generic R06 local field without any historical markdown source.

---

# 9. Exact generic local Mises maximum

The formal global maximum of \(\Phi\) over the closed square is obtained from a finite algebraic candidate set.

## 9.1 Interior candidates

Solve simultaneously

\[
\boxed{\Phi_{,u}=0},
\qquad
\boxed{\Phi_{,v}=0},
\]

and retain all real solutions satisfying

\[
-1<u<1,
\qquad
-1<v<1.
\]

A formal elimination implementation may form

\[
R_u(u)=\operatorname{Res}_v(\Phi_{,u},\Phi_{,v}),
\]

enumerate all real roots \(u\in(-1,1)\), recover the common real \(v\) roots, and verify both derivative residuals before admission.

## 9.2 Edge candidates

On \(u=+1\) and \(u=-1\), solve all real roots

\[
\boxed{\frac{d}{dv}\Phi(\pm1,v)=0},
\qquad -1<v<1.
\]

On \(v=+1\) and \(v=-1\), solve all real roots

\[
\boxed{\frac{d}{du}\Phi(u,\pm1)=0},
\qquad -1<u<1.
\]

These are ordinary univariate polynomial roots.

## 9.3 Corners

Always include

\[
(-1,-1),\ (-1,1),\ (1,-1),\ (1,1).
\]

## 9.4 Maximum

Let the union of the admitted interior, edge and corner candidates be \(\mathcal C_\Phi\). Then

\[
\boxed{
\Phi_{max}=\max_{(u,v)\in\mathcal C_\Phi}\Phi(u,v)
}.
\]

No spatial stress grid, collocation mesh or effective width is part of the formal operator.

For previously audited families the controlling point may happen to lie on an edge, but R12 generic execution must not hard-code that fact.

---

# 10. Automatic R04/R06 event-order gate

Define

\[
r=\frac{L_y}{L_x},
\]

\[
\boxed{k_{cr}=\frac{4(3r^4+2r^2+3)}{3r^2}},
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

There is no specimen-name branch table.

---

# 11. R04 yield-first face law

For a current face strain pair \((e_x,e_y)\) and zero terminal engineering shear,

\[
\sigma_x^{tr}=\frac{E_s}{1-\nu_s^2}(e_x+\nu_se_y),
\]

\[
\sigma_y^{tr}=\frac{E_s}{1-\nu_s^2}(\nu_se_x+e_y).
\]

General Mises form, retaining shear notation for completeness:

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

This ideal-EP law belongs to steel, not UHPC.

---

# 12. R06 local-buckling-first face law

For a fixed current face-strain direction

\[
\mathbf e_f=(e_x,e_y),
\]

define the path-free radial family

\[
\boxed{\mathbf e_f(\eta)=\eta\mathbf e_f},
\qquad 0\le\eta\le1.
\]

For every \(\eta\):

1. rebuild \(B_1(\eta)\);
2. enumerate the complete R02 nonnegative candidate set;
3. select \(U^*(\eta)\) by the same condensed energy;
4. construct the exact 2D field from Sections 8–9;
5. evaluate

\[
\Phi_{max}(\eta).
\]

Define

\[
\boxed{\Psi(\eta)=\Phi_{max}(\eta)-f_y^2}.
\]

If

\[
\Psi(1)\le0,
\]

the full current R02 mean state is retained.

If

\[
\Psi(1)>0,
\]

define first local yield

\[
\boxed{
\eta_y=\min\{\eta\in(0,1]:\Psi(\eta)=0\}
}.
\]

The R06 face stress is the **gross/full-width R02 mean stress at the projected state**:

\[
\boxed{
\bar{\boldsymbol\sigma}_{R06}(\mathbf e_f)
=\bar{\boldsymbol\sigma}_{R02}(\eta_y\mathbf e_f)
}.
\]

No reduced width or reduced area is introduced.

A formal all-root implementation may eliminate \(U\) jointly with an active algebraic Mises candidate using resultants. A numerical evaluator may solve the exact scalar first-crossing equation, but may not replace \(\Psi\) by sampled/interpolated surrogate data.

---

# 13. R12 UHPC compression polynomial

Compression is active only up to the first compression peak/contact.

Define

\[
\xi=-\frac{\varepsilon}{\varepsilon_{c0}},
\qquad 0\le\xi\le1,
\]

\[
\boxed{A_c=\frac{E_c\varepsilon_{c0}}{f_c}},
\]

\[
B_c=6-5A_c,
\qquad
C_c=4A_c-5.
\]

Require the current shape gate

\[
\boxed{0<A_c\le1.5}.
\]

The signed compression stress is

\[
\boxed{
\sigma_c(\varepsilon)
=-f_c\left[A_c\xi+B_c\xi^5+C_c\xi^6\right]
}.
\]

It satisfies exactly

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

No post-peak compression branch is needed by the current first-contact terminal. A candidate with \(\varepsilon<-\varepsilon_{c0}\) is inadmissible rather than extrapolated.

Compression primitives, with \(F_0'=\sigma\) and \(F_1'=\varepsilon\sigma\):

\[
\boxed{
F_{0c}=f_c\varepsilon_{c0}
\left(\frac{A_c}{2}\xi^2+\frac{B_c}{6}\xi^6+\frac{C_c}{7}\xi^7\right)
},
\]

\[
\boxed{
F_{1c}=-f_c\varepsilon_{c0}^2
\left(\frac{A_c}{3}\xi^3+\frac{B_c}{7}\xi^7+\frac{C_c}{8}\xi^8\right)
}.
\]

---

# 14. R12 Hiew-anchor cubic-Hermite tension

Set nodes

\[
(\varepsilon_i,s_i),\qquad i=0,1,2,3,4,
\]

according to Section 3.4.

Define

\[
h_i=\varepsilon_{i+1}-\varepsilon_i,
\qquad
 d_i=\frac{s_{i+1}-s_i}{h_i}.
\]

Origin and terminal slopes:

\[
\boxed{m_0=E_c},
\qquad
\boxed{m_4=0}.
\]

Require

\[
\boxed{0<E_c\le3d_0}.
\]

For internal nodes \(i=1,2,3\):

if

\[
d_{i-1}d_i\le0,
\]

set

\[
\boxed{m_i=0}.
\]

Otherwise define

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

On interval i, let

\[
u=\frac{\varepsilon-\varepsilon_i}{h_i}\in[0,1].
\]

The cubic is

\[
\boxed{
\sigma_t=c_{i0}+c_{i1}u+c_{i2}u^2+c_{i3}u^3
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

This construction is C1 across all tensile nodes and joins the zero-stress tail at \(\varepsilon_{t,lim}\) with zero tangent.

For \(\varepsilon\ge\varepsilon_{t,lim}\),

\[
\sigma_t=0.
\]

Define

\[
\mathcal A_i(u)=c_{i0}u+\frac{c_{i1}}2u^2+\frac{c_{i2}}3u^3+\frac{c_{i3}}4u^4,
\]

\[
\mathcal B_i(u)=\frac{c_{i0}}2u^2+\frac{c_{i1}}3u^3+\frac{c_{i2}}4u^4+\frac{c_{i3}}5u^5.
\]

Incremental primitives are

\[
\boxed{\Delta F_{0,i}=h_i\mathcal A_i(u)},
\]

\[
\boxed{\Delta F_{1,i}=h_i\varepsilon_i\mathcal A_i(u)+h_i^2\mathcal B_i(u)}.
\]

Completed prior intervals are summed exactly to obtain global \(F_{0t},F_{1t}\).

Thus the active UHPC scalar law contains only finite polynomial pieces; no Gamma, hypergeometric, logarithmic or arctangent material primitive is required.

---

# 15. Exact UHPC continuous-thickness section resultants

For direction \(i=x,y\):

\[
\varepsilon_i(z)=\varepsilon_i^0+\kappa_i z,
\]

\[
\varepsilon_i^\pm=\varepsilon_i^0\pm\kappa_i\frac{t_c}{2}.
\]

For \(\kappa_i\ne0\):

\[
\boxed{
N_i^U=(1-\rho_w)
\frac{F_0(\varepsilon_i^+)-F_0(\varepsilon_i^-)}{\kappa_i}
},
\]

\[
\boxed{
M_i^U=(1-\rho_w)
\frac{F_1(\varepsilon_i^+)-F_1(\varepsilon_i^-)
-\varepsilon_i^0[F_0(\varepsilon_i^+)-F_0(\varepsilon_i^-)]}{\kappa_i^2}
}.
\]

For \(\kappa_i=0\):

\[
\boxed{N_i^U=(1-\rho_w)t_c\sigma_U(\varepsilon_i^0)},
\qquad
\boxed{M_i^U=0}.
\]

No through-thickness quadrature is used.

---

# 16. Longitudinal web ideal-EP operator

The web strain is

\[
\varepsilon_y^w(z)=\varepsilon_y^0+\kappa_yz.
\]

Use

\[
\boxed{
\sigma_y^w(z)=\operatorname{clip}(E_s\varepsilon_y^w,-f_y,+f_y)
}.
\]

Exact yield-strain crossings occur at

\[
\varepsilon_y^w=\pm\frac{f_y}{E_s}.
\]

For any crossing lying inside

\[
[-t_c/2,t_c/2],
\]

split the analytic integral at that exact z only. On an elastic subinterval \([z_a,z_b]\):

\[
\int\sigma dz
=E_s\left[\varepsilon_y^0(z_b-z_a)+\frac{\kappa_y}{2}(z_b^2-z_a^2)\right],
\]

\[
\int z\sigma dz
=E_s\left[\frac{\varepsilon_y^0}{2}(z_b^2-z_a^2)+\frac{\kappa_y}{3}(z_b^3-z_a^3)\right].
\]

On a yielded subinterval with constant sign \(s=\pm1\):

\[
\int\sigma dz=s f_y(z_b-z_a),
\]

\[
\int z\sigma dz=\frac{s f_y}{2}(z_b^2-z_a^2).
\]

Multiply the resulting through-thickness integrals by \(\rho_w\) to obtain \(N_y^w,M_y^w\).

---

# 17. Total section generalized forces

Let upper/lower face current stresses after R04 or R06 be

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

The UHPC volume reduction and steel-web add-back appear exactly once.

---

# 18. Capacity-contact closure

Unknowns are

\[
(q,\varepsilon_x^0,\kappa_x,\varepsilon_y^0,\kappa_y).
\]

Four equilibrium equations:

\[
\boxed{N_x=N_x^A},
\qquad
\boxed{M_x=M_x^A},
\]

\[
\boxed{N_y=N_y^A},
\qquad
\boxed{M_y=M_y^A}.
\]

The active first compression-contact terminal is

\[
\boxed{
\varepsilon_y(-t_c/2)=\varepsilon_y^0-\kappa_y\frac{t_c}{2}=-\varepsilon_{c0}
}.
\]

Hence

\[
\boxed{
\varepsilon_y^0=-\varepsilon_{c0}+\kappa_y\frac{t_c}{2}
},
\]

leaving four unknowns

\[
\boxed{(q,\varepsilon_x^0,\kappa_x,\kappa_y)}
\]

for the four N/M equations.

Admissibility requires at least

```text
q > 0
kappa_y >= 0
all four N/M equations satisfied
all UHPC compression endpoints >= -eps_c0
all UHPC tensile endpoints <= eps_t_lim
R04/R06 branch gate satisfied
R02 uses the minimum-energy nonnegative candidate
web intervals consistent with exact yield crossings
```

Among admissible compression-contact roots, choose the smallest positive q.

If a tensile endpoint reaches \(\varepsilon_{t,lim}\) before the compression contact, return

```text
UHPC_TENSION_FIRST_TERMINAL_NOT_CLOSED
```

rather than ignoring that event.

Finally

\[
\boxed{P_u=P(q)}.
\]

---

# 19. Formal solver identity versus executable evaluator

The **theory** is exactly the finite equations/events in Sections 4–18.

The formal target remains

```text
R02 cubic all-real roots
R06 polynomial stationary/resultant candidates
finite event branches
resultant / companion / RootOf / all-real-root terminal backend
```

The current Excel executable is allowed to use numerical root evaluators only as a transparent implementation of these exact equations. In particular, the generic R06 Excel evaluator may:

- construct the exact bivariate polynomial \(\Phi\);
- obtain edge stationary points from univariate polynomial roots;
- solve the exact interior stationary equations numerically from deterministic starts and verify derivative residuals;
- solve the exact scalar \(\Psi(\eta)=0\) first crossing numerically;
- solve the four exact section residual equations numerically from input-scaled starts.

These numerical calls are **not** additional mechanics and do not authorize a fitted stress/Pu surrogate. No reference result is available to the engine.

The final formal zero-iteration implementation may replace these numerical evaluators, but it must solve the same equations and return the same admissible roots.

---

# 20. Standalone implementation algorithm

A new AI with only this ledger and a complete input set shall execute the following sequence.

1. Validate geometry, steel and UHPC input contracts.
2. Compute \(q_0,\rho_w,z_f\).
3. Compute the initial A/D coefficients.
4. Compute \(m_c\), the two adjacent positive integer candidates and \(m^*\).
5. Compute \(P_{cr},K_x,G,C,J_x,J_y\).
6. Compute local \(k_x,k_y,c_x,c_y,K_b,K_A\).
7. Compute \(\sigma_{cr,s}^{E}\) and choose R04 or R06 mechanically.
8. Generate UHPC compression coefficients \(A_c,B_c,C_c\).
9. Generate the Hiew cubic node slopes and all cubic coefficients.
10. Generate exact UHPC \(F_0,F_1\) primitives.
11. For each candidate section state, evaluate upper/lower face strains.
12. On R04 faces, apply the radial steel Mises cap.
13. On R06 faces, solve R02, reconstruct the full 2D field, enumerate the finite Mises candidates, and apply the first radial local-yield projection if needed.
14. Evaluate UHPC x/y continuous-thickness resultants.
15. Evaluate exact web resultants.
16. Assemble total \(N_x,M_x,N_y,M_y\).
17. Enforce the compression-contact relation to eliminate \(\varepsilon_y^0\).
18. Solve the four section/Airy equations for all admissible physical roots.
19. Reject roots violating material/event/domain conditions.
20. Choose the smallest positive-q admissible compression-contact root.
21. Return \(P_u=P(q)\) and the full audit state.

No external markdown file is needed to define any equation in these steps.

---

# 21. Required output/audit state

A transferable implementation shall expose at least

```text
raw active inputs
rho_w, zf
Ac,Bc,Cc
Hiew node slopes and cubic coefficients
Dx,Dy,Dmu,D66,H
m_cont,m1,m2,m*
Pcr,Kx,G,C,Jx,Jy
sigma_cr,s^E
R04/R06 branch for each face
R02 B3,B1,B0 and selected U
R06 active local (u,v), eta when applicable
upper/lower steel stresses
UHPC endpoint strains
UHPC F0/F1 endpoint values
UHPC Nx,Mx,Ny,My
web Ny,My
total Nx,Mx,Ny,My
Airy target Nx,Mx,Ny,My
four residuals
q
Pu
root count/status
```

---

# 22. Anti-lookup / parameter-driven contract

The executable model must satisfy all of the following:

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

A generic workbook may contain one arbitrary illustrative input state so that formulas have visible values, but that state must not be a historical validation specimen and the engine must not read any stored alternate rows.

---

# 23. Independent arbitrary-parameter pressure tests

Two non-reference parameter sets were used only to verify parameter dependence of the R12 executable.

## USER_A — R04 example

```text
b=900
a=1700
tc=45
ts=5
A0g=1.8
Aw=1000
Lx=180
Ly=160
A0local=0.10
```

with the current common steel/UHPC material defaults gave

```text
branch = R04_YIELD_FIRST
sigma_cr,E = 1564.4211036824 MPa
m* = 2
Pcr = 77.6820828130 MN
q = 0.000259108476551285
Pu = 8.91481531928649 MN
Rmax = 5.09e-11
```

## USER_B — R06 example

```text
b=1800
a=3000
tc=50
ts=4.5
A0g=3.6
Aw=1500
Lx=450
Ly=410
A0local=0.25
```

with the same material defaults gave

```text
branch = R06_LOCAL_FIRST
sigma_cr,E = 201.1861465374 MPa
m* = 2
Pcr = 45.1541579239 MN
q = 0.000942277149009764
Pu = 14.5062617513705 MN
Rmax = 3.82e-11
```

These are not calibration targets and are not stored as runtime lookup rows. They demonstrate that changing geometry switches the branch and changes the load through the equations.

---

# 24. Fail-fast statuses

At minimum, the following failures must remain explicit:

```text
GEOMETRY_CONTRACT_FAIL
WEB_FRACTION_CONTRACT_FAIL
STEEL_MATERIAL_CONTRACT_FAIL
UHPC_COMPRESSION_POLYNOMIAL_CONTRACT_FAIL
HIEW_TENSION_ANCHOR_CONTRACT_FAIL
R02_NO_ADMISSIBLE_NONNEGATIVE_CANDIDATE
R06_LOCAL_YIELD_ROOT_FAIL
UHPC_COMPRESSION_DOMAIN_EXCEEDED
UHPC_TENSION_FIRST_TERMINAL_NOT_CLOSED
NO_PHYSICAL_CAPACITY_CONTACT_ROOT
```

A failure is not permission to switch to another material law, another branch, a stored specimen result or a fitted correction.

---

# 25. Current lock

```text
CURRENT_LEDGER = R12_SELF_CONTAINED_PARAMETRIC

STRUCTURAL_BACKBONE
= INITIAL A/D + EXACT INTEGER MODE + MARGUERRE-AIRY

STEEL FACE
= AUTO(R04, R02/R06)

R02
= NONNEGATIVE CUBIC ALL-ROOT ACTIVE SET

R06
= FULL 2D FINITE LL AIRY POLYNOMIAL
  + INTERIOR/EDGE/CORNER MISES CANDIDATES
  + FIRST RADIAL LOCAL-YIELD PROJECTION

UHPC
= SIXTH-DEGREE COMPRESSION
  + HIEW-ANCHOR CUBIC-HERMITE TENSION
  + EXACT POLYNOMIAL THICKNESS PRIMITIVES

WEB
= IDEAL EP
  + EXACT YIELD-CROSSING INTEGRATION

TERMINAL
= FIRST UHPC COMPRESSION CONTACT

REFERENCE LOOKUP
= NONE

HISTORICAL MARKDOWN RUNTIME DEPENDENCY
= NONE
```

Compactly,

\[
\boxed{
\text{raw user inputs}
\to A/D
\to m^*
\to \text{Airy}
\to \operatorname{AUTO}(R04,R02/R06)
\to \text{R12 UHPC section}
\to \text{web}
\to N/M\text{ closure}
\to \text{first admissible compression contact}
\to P_u
}
\]

This ledger is the current standalone text implementation contract.