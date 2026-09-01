# NZ-SCCM — 钢壳–UHPC 显式极限承载力集中技术总账 R11 — POLYNOMIAL UHPC

**Date:** 2026-09-01  
**Working branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Production main:** unchanged  
**Current transfer identity:** `STEEL_SHELL_UHPC_R11_POLYNOMIAL_UHPC`  
**Formal spatial quadrature:** `0`  
**Material-point grid:** `0`  
**Effective-width/effective-area repair:** prohibited  
**FEM/test comparator in material calibration or root selection:** `0`  
**Supersedes for current execution:** `R10_SIMPLE_MATERIAL`  
**Preserves as historical evidence:** R01 Hu-full evaluator, R09 tombstoned solver detour, R10 oversimplified material experiment

---

# 0. Governing decision

R11 corrects one specific error in R10: **UHPC is not represented by an elastic-perfectly-plastic compression law and its tensile contribution is not set to zero.**

The accepted structural mechanics chain is retained:

```text
raw specimen geometry + material parameters
-> initial full-composite A/D
-> minimum admissible integer global mode
-> Marguerre–Airy Pcr,C,Kx,G,Jx,Jy
-> q and Q=q(q+2q0)
-> Airy generalized N/M demand
-> automatic steel-face event order
   -> R04_YIELD_FIRST
   -> or R02 + R06_LOCAL_BUCKLING_FIRST
-> UHPC continuous-thickness section N/M
-> longitudinal web steel N/M
-> total section N/M
-> four Airy/section equilibrium equations
-> first admissible UHPC capacity-contact terminal
-> q
-> P_u
```

R11 changes the scalar UHPC section material to:

```text
compression, 0 <= xi_c <= 1:
    source-anchored sixth-degree polynomial

tension, 0 <= eps_t <= eps_t,lim:
    source-anchored finite piecewise cubic Hermite polynomial

compression beyond xi_c=1:
    not entered by the present compression-contact terminal

tension beyond eps_t,lim:
    sigma_t = 0 with C1 terminal connection
```

The central mathematical objective is therefore:

```text
physical UHPC nonlinearity retained
+ finite polynomial material pieces
+ exact thickness primitives
+ no Gamma / hypergeometric / numerical thickness quadrature
+ no structure-level material backfit
```

R11 does **not** alter the steel-face R04/R06 theory, Airy demand, R02 local-buckling condensation, web steel phase, section equilibrium equations, or current capacity-contact architecture.

---

# 1. Supersession and historical status

## 1.1 R10 is retired as a current material law

R10 used

```text
compression: linear elastic -> constant -fc plateau
tension:     zero
```

for UHPC. That representation was introduced only for algebraic simplicity and is now judged to remove too much of the physical material response.

Accordingly:

```text
R10_UHPC_EP_COMPRESSION        = RETIRED_FROM_CURRENT_EXECUTION
R10_UHPC_ZERO_TENSION          = RETIRED_FROM_CURRENT_EXECUTION
R10_STRUCTURAL_AIRY_R04_R06    = RETAINED
R10_WEB_STEEL_EP               = RETAINED
R10_NUMERICAL_RESULTS          = HISTORICAL_COMPARATOR_ONLY
```

The objection to R10 applies to **UHPC**. It does not by itself revoke the separately defined ideal elastic-perfectly-plastic law currently used for the steel shell/web phases.

## 1.2 Earlier Hu-Wenxu calculations remain historical regression evidence

The earlier source-audited capacity-contact calculations used the Hu-Wenxu uniaxial UHPC source law and produced the established BH/T360 regression checkpoints. Those calculations remain valid historical evidence for the previous material identity; they are not relabelled as R11 results.

## 1.3 Historical Wu/Hiew material research is promoted only at the scalar section level

The project history already contains the following material-level facts:

1. a Wu-type UHPC compression reference was adopted in the material-research branch,
2. its ascending branch was written

\[
y=A x+(6-5A)x^5+(4A-5)x^6,
\]

3. Hiew 2% steel-fibre direct-tension anchors were assembled for effective cracking, peak, localisation and tensile limit,
4. those objects were originally labelled **material anchors**, not a frozen multidimensional production operator.

R11 makes one new, explicit project decision:

> For the present steel-shell–UHPC capacity-contact **scalar through-thickness section operator**, promote the Wu-type ascending polynomial and a deterministic Hiew-anchor cubic-Hermite tensile transformation to the active scalar law.

This does **not** retroactively claim that the older G16R multidimensional UHPC operator was production-frozen.

---

# 2. Scope and non-negotiable boundaries

R11 inherits the following project boundaries:

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_material_points = 0
LOAD_PATH_TRACKING = 0
EFFECTIVE_WIDTH = PROHIBITED
EFFECTIVE_AREA = PROHIBITED
FEM_IN_ROOT_SELECTION = 0
TEST_LOAD_IN_ROOT_SELECTION = 0
PANEL_PU_MATERIAL_BACKFIT = 0
```

Formal theory shall not introduce:

```text
33-point eta sampling
fitted eta quintic surrogate
terminal endpoint grids
3x3x3 affine stencils
fixed multi-level refinement tables
Gauss/Simpson/adaptive spatial quadrature
material-point Newton history
specimen-name branch lookup
historical Pu lookup
```

A numerical root evaluator may be used only as a transparent execution/checking backend until the finite-algebraic all-root backend is completed. It does not define the theory.

---

# 3. Source and evidence hierarchy for R11

The relevant source chain is separated by role.

## 3.1 Global/steel mechanics

1. `20260821_1733__NZSCCM__MARGUERRE_AIRY_EXPLICIT_LIMIT_THEORY_V1.md`  
   Role: global geometry, initial A/D, integer mode, Airy front-end.

2. `20260827_1623__NZSCCM__R02_NONNEGATIVE_AMPLITUDE_ACTIVESET_COMPLETION_R01.md`  
   Role: exact nonnegative local-amplitude active set.

3. `20260825_1530__NZSCCM__STEEL_SHELL_COMMON_R06_LOCAL_YIELD_RESULTANT_GATE_V1.md`  
   Role: R04/R06 event-order gate and R06 local-yield resultant.

4. `20260831__NZSCCM__STEEL_SHELL_UHPC_SPECIMEN_PARAMETER_MASTER_R01.csv`  
   Role: BH-family geometry/material input registry.

## 3.2 UHPC scalar material evidence

1. Historical G16R material research: Wu-type smooth compression reference + Hiew 2% direct-tension anchors.  
   This source was historically a material anchor/identification branch.

2. `evidence/materials/UHPC/core_sources/Hiew_2024_direct_tension.md`  
   Role: direct-tension elastic/strain-hardening/peak/localisation/softening evidence and source-series parameters.

3. `evidence/materials/UHPC/audits/NZ_SCCM_G16R_signed_excess坐标_材料参数重审_U候选_D可识别性门禁.md`  
   Role: current project representative 2%-fibre tensile anchor transfer and the earlier Wu-type compression reference.

4. `evidence/materials/UHPC/LOCAL_THESES_SOURCE_MAP.md`  
   Role: Zhou/Wang/Hu provenance and multiaxial qualification boundaries.

5. `20260822_1240__NZSCCM__UHPC_ZHANG_BACKBONE_AND_LIU_CC_CONTINUOUS_SOURCE_MIN_GATE.md`  
   Role: later alternative compression and multiaxial capacity research. It is retained as an independent comparator/qualification source; it does not overwrite R11's scalar polynomial decision.

## 3.3 Multiaxial evidence remains a qualification layer

Liu TC/CC/TT, Diab/Ferche compression-softening, Zhou DP and Wang W-W remain material-level multiaxial/failure evidence. R11 does not silently multiply those strength surfaces into the scalar section stress law.

Therefore:

```text
R11_SCALAR_SECTION_OPERATOR = FROZEN_BY_THIS_LEDGER
UHPC_FULL_2D_CURRENT_OPERATOR = NOT_FROZEN_BY_R11
MULTIAXIAL_SOURCE_EVIDENCE = RETAINED_AS_QUALIFICATION_BOUNDARY
```

---

# 4. Coordinates, signs and global kinematics

Use N–mm–MPa.

```text
x = transverse
y = axial
z = through thickness, positive toward upper face
strain: tension positive
stress: tension positive
```

Global one-half-wave field:

\[
\psi=\sin(\alpha x)\sin(\beta y),
\qquad
\alpha=\frac{\pi}{b},
\qquad
\beta=\frac{m\pi}{a_{phys}}.
\]

\[
w_0=bq_0\psi,
\qquad
w=b(q_0+q)\psi,
\qquad
w_d=bq\psi,
\]

\[
\boxed{q_0=\frac{A_{0g}}{b}},
\qquad
\boxed{Q(q)=q(q+2q_0)}.
\]

The actual geometric curvature generated by the global mode is owned by q:

\[
\kappa_x^{geo}=bq\alpha^2\psi,
\qquad
\kappa_y^{geo}=bq\beta^2\psi.
\]

Historical capacity-contact section coordinates \(\kappa_x,\kappa_y\) remain section closure variables and must not be relabelled as the pointwise geometric curvature field.

---

# 5. Required inputs and parameter contract

## 5.1 Geometry

```text
b        panel width
a_phys   physical axial length
tc       UHPC core thickness
ts       each steel-face thickness
A0g      global initial-imperfection amplitude
Aw       total longitudinal web steel area represented in the core
Lx,Ly    local steel-face cell dimensions
A0local  local initial-imperfection amplitude
```

Derived:

\[
\rho_w=\frac{A_w}{bt_c},
\qquad
z_f=\frac{t_c+t_s}{2}.
\]

Require

\[
0\le\rho_w<1.
\]

## 5.2 Steel

```text
Es
nu_s
fy
```

with

\[
E_s>0,
\quad -1<\nu_s<0.5,
\quad f_y>0.
\]

## 5.3 UHPC compression

Independent inputs:

```text
Ec
nu_c
fc
eps_c0
```

No empirical relation `Ec=Ec(fc)` or `eps_c0=eps_c0(fc)` is imposed unless a future source-specific material contract explicitly requires it.

Derived polynomial shape parameter:

\[
\boxed{A_c=\frac{E_c\varepsilon_{c0}}{f_c}}.
\]

## 5.4 UHPC tension

The active tensile law is defined by source-derived anchors:

```text
eps_t_cr,   f_t_cr
eps_t_peak, f_t_peak
eps_t_loc,  f_t_loc
eps_t_lim
```

with terminal stress

\[
f_t(\varepsilon_{t,lim})=0.
\]

The Hiew 2024 source-series model parameters retained in the project evidence include:

| source series | eps_t_cr | f_t_cr MPa | eps_t_peak | f_t_peak MPa | eps_t_loc | f_t_loc MPa | eps_t_lim |
|---|---:|---:|---:|---:|---:|---:|---:|
| SL-2.0 | 0.00040 | 10.0 | 0.00380 | 11.7 | 0.00624 | 9.9 | 0.00759 |
| HL-2.0 | 0.00042 | 10.3 | 0.00674 | 11.1 | 0.00872 | 10.8 | 0.01000 |
| SL-HL-2.0 | 0.00042 | 10.1 | 0.00380 | 11.0 | 0.00690 | 10.7 | 0.00741 |

The current project representative default inherited from G16R is:

```text
eps_t_cr    = 0.000420
f_t_cr      = 9.767718 MPa

eps_t_peak  = 0.003800
f_t_peak    = 10.734818 MPa

eps_t_loc   = 0.006900
f_t_loc     = 10.347978 MPa

eps_t_lim   = 0.007590
```

These values are a **project representative 2%-fibre anchor set**, not a claim that all 2% UHPC fibre systems have identical tensile strain capacity.

The effective-cracking point is treated as a source anchor. R11 does **not** impose the false identity

\[
f_{t,cr}=E_c\varepsilon_{t,cr},
\]

because the Hiew/AASHTO effective-cracking strain has an offset-based testing meaning. The first cubic interval is precisely what allows the material to preserve the common origin tangent \(E_c\) while also passing through the effective-cracking anchor.

If the actual fibre system is known, source-specific Hiew SL-2.0 / HL-2.0 / hybrid anchors take precedence over the representative set. No structural Pu may be used to choose among them.

The old Hu parameters

```text
fct
eps_t0
Vf
lf
df
m_t
```

are no longer active coefficients of the R11 scalar law. They may remain as source metadata, but changing them must not change R11 unless an explicit Hiew source-to-anchor mapping is added.

---

# 6. Initial full-composite A/D operator — unchanged

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
A_{11}=2t_sK_s+(1-\rho_w)t_cK_c,
\]

\[
A_{22}=A_{11}+\rho_wt_cE_s,
\]

\[
A_{12}=2t_s\nu_sK_s+(1-\rho_w)t_c\nu_cK_c.
\]

Face bending term including centroid offset exactly once:

\[
D_f=2K_s\left(\frac{t_s^3}{12}+t_sz_f^2\right).
\]

Core and web terms:

\[
D_c=(1-\rho_w)K_c\frac{t_c^3}{12},
\qquad
D_w=\rho_wE_s\frac{t_c^3}{12}.
\]

\[
D_x=D_f+D_c,
\qquad
D_y=D_x+D_w.
\]

\[
D_\mu=\nu_sD_f+\nu_cD_c,
\]

\[
D_{66}=2G_s\left(\frac{t_s^3}{12}+t_sz_f^2\right)
+(1-\rho_w)G_c\frac{t_c^3}{12}.
\]

Orthotropic coupling convention:

\[
\boxed{H=D_\mu+2D_{66}}.
\]

These are initial elastic stiffness quantities only. Nonlinear UHPC section stress is computed separately from the R11 polynomial law.

---

# 7. Integer global mode and Marguerre–Airy demand — unchanged

For each positive integer m:

\[
\beta_m=\frac{m\pi}{a_{phys}},
\]

\[
\boxed{
N_{cr,m}=
\frac{D_x\alpha^4+2H\alpha^2\beta_m^2+D_y\beta_m^4}{\beta_m^2}},
\]

\[
\boxed{P_{cr,m}=bN_{cr,m}}.
\]

Select

\[
\boxed{m^*=\arg\min_{m\in\mathbb N^+}P_{cr,m}}
\]

using mechanics only; FEM/test information is prohibited from mode selection.

Let

\[
\Delta_A=A_{11}A_{22}-A_{12}^2,
\qquad \beta=\beta_{m^*}.
\]

Then

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
\]

\[
J_y=b(D_\mu\alpha^2+D_y\beta^2).
\]

With

\[
Q=q(q+2q_0),
\]

the global load-amplitude relation is

\[
\boxed{
P^A(q)=P_{cr}\frac{q}{q+q_0}+CQ}.
\]

Current generalized Airy demand at the capacity-control section:

\[
\boxed{N_x^A=K_xQ},
\]

\[
\boxed{M_x^A=J_xq},
\]

\[
\boxed{N_y^A=-\left(\frac{P^A}{b}-GQ\right)},
\]

\[
\boxed{M_y^A=J_yq}.
\]

---

# 8. R02 local steel-face condensation — unchanged finite algebraic form

Local coordinates:

\[
0\le\xi\le L_x,
\qquad
0\le\eta\le L_y,
\]

\[
\phi=(1-\cos k_x\xi)(1-\cos k_y\eta),
\]

\[
k_x=\frac{2\pi}{L_x},
\qquad
k_y=\frac{2\pi}{L_y}.
\]

Exact local averages:

\[
\boxed{c_x=\frac{3k_x^2}{8}},
\qquad
\boxed{c_y=\frac{3k_y^2}{8}}.
\]

Local plate bending coefficient:

\[
D_s=\frac{E_st_s^3}{12(1-\nu_s^2)},
\]

\[
\boxed{
K_b=D_s\left[\frac34(k_x^4+k_y^4)+\frac12k_x^2k_y^2\right]}.
\]

For local amplitude U and initial amplitude \(A_0=A_{0local}\):

\[
d=U^2-A_0^2,
\]

\[
m_x=e_x+c_xd,
\qquad
m_y=e_y+c_yd.
\]

Let

\[
Q_s=\frac{E_s}{1-\nu_s^2}.
\]

The exact LL Airy compatibility uses the seven harmonics

```text
(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1)
coefficients = 1/2,-1/2,1/2,-1,1/2,-1/2,1/2
```

and

\[
K_A=k_x^4k_y^4\left[
\frac{17}{256k_y^4}
+\frac{17}{256k_x^4}
+\frac{1}{8(k_x^2+k_y^2)^2}
+\frac{1}{32(k_x^2+4k_y^2)^2}
+\frac{1}{32(4k_x^2+k_y^2)^2}
\right].
\]

The quartic condensed energy has derivative

\[
\boxed{B_3U^3+B_1U+B_0=0},
\]

where

\[
\boxed{
B_3=4t_sE_sK_A
+2t_sQ_s(c_x^2+2\nu_sc_xc_y+c_y^2)},
\]

\[
\boxed{
B_1=K_b-A_0^2B_3
+2t_sQ_s
(c_xe_x+\nu_sc_xe_y+\nu_sc_ye_x+c_ye_y)},
\]

\[
\boxed{B_0=-A_0K_b}.
\]

The exact candidate set is

\[
\boxed{
\mathcal U=
\{0\}
\cup
\{U\ge0:\ B_3U^3+B_1U+B_0=0,\ U\in\mathbb R\}}.
\]

Select

\[
\boxed{
U^*=\arg\min_{U\in\mathcal U}
\left(\frac{B_3}{4}U^4+\frac{B_1}{2}U^2+B_0U\right)}.
\]

R02 therefore requires all-real-root enumeration of one cubic, not Newton continuation and not a local amplitude grid.

---

# 9. Automatic R04/R06 steel-face event order — unchanged

Define

\[
r=\frac{L_y}{L_x},
\]

\[
\boxed{
k_{cr}=\frac{4(3r^4+2r^2+3)}{3r^2}},
\]

\[
\boxed{
\sigma_{cr,s}^{E}
=
\frac{\pi^2E_st_s^2}{12(1-\nu_s^2)L_x^2}k_{cr}}.
\]

Mechanical branch gate:

```text
sigma_cr,s^E >= fy  -> R04_YIELD_FIRST
sigma_cr,s^E <  fy  -> R06_LOCAL_BUCKLING_FIRST
```

There is no specimen-name lookup.

## 9.1 R04 yield-first face law

Plane-stress elastic trial:

\[
\sigma_x^{tr}=\frac{E_s}{1-\nu_s^2}(\varepsilon_x+\nu_s\varepsilon_y),
\]

\[
\sigma_y^{tr}=\frac{E_s}{1-\nu_s^2}(\nu_s\varepsilon_x+\varepsilon_y),
\]

\[
\tau_{xy}^{tr}=\frac{E_s}{2(1+\nu_s)}\gamma_{xy}.
\]

Trial Mises stress:

\[
\boxed{
\sigma_{VM}^{tr}
=\sqrt{(\sigma_x^{tr})^2-
\sigma_x^{tr}\sigma_y^{tr}+
(\sigma_y^{tr})^2+3(\tau_{xy}^{tr})^2}}.
\]

Radial ideal-EP cap:

\[
\boxed{
\lambda_p=\min\left(1,\frac{f_y}{\sigma_{VM}^{tr}}\right)},
\qquad
\boxed{\boldsymbol\sigma_s=\lambda_p\boldsymbol\sigma_s^{tr}}.
\]

This ideal-EP relation is a **steel-face** law. R11's rejection of UHPC perfect plasticity does not alter it.

## 9.2 R06 local-buckling-first face law

For \(\sigma_{cr,s}^{E}<f_y\), R02 is first condensed. Along the mean-strain projection

\[
\boldsymbol\varepsilon_f(\eta)=\eta\boldsymbol\varepsilon_f,
\qquad 0<\eta\le1,
\]

R02 is re-condensed and the exact local field is reconstructed.

Define

\[
\Phi(u,v;\eta)=\sigma_{VM}^2(u,v;\eta),
\qquad (u,v)=(\cos X,\cos Y)\in[-1,1]^2.
\]

Then

\[
\Psi(\eta)=\max_{[-1,1]^2}\Phi(u,v;\eta)-f_y^2,
\]

and first local yield is

\[
\boxed{
\eta_y=\min\{\eta\in(0,1]:\Psi(\eta)=0\}}.
\]

Formal spatial maximisation is finite algebraic: interior stationary points, edge stationary points and corners. For the audited BH032/BH050/T360 family, the controlling lower-face yield point further reduces to the exact edge \(v=-1\), where shear vanishes and \(\Phi\) is quartic in u; its stationary points are the real roots of a cubic derivative. That specimen-family reduction is an audited consequence, not a universal replacement of the generic R06 candidate set.

The section receives the whole-width R02 mean resultant at the projected state. Pointwise clipping and effective-width/effective-area replacement are prohibited.

Current family classification retained from the source-audited geometry:

| specimen | sigma_cr,s^E MPa | fy MPa | branch |
|---|---:|---:|---|
| BH005 | 10044.966748 | 355 | R04_YIELD_FIRST |
| BH010 | 2511.241687 | 355 | R04_YIELD_FIRST |
| BH020 | 627.810422 | 355 | R04_YIELD_FIRST |
| BH032 | 245.238446 | 355 | R06_LOCAL_BUCKLING_FIRST |
| BH050 | 100.449667 | 355 | R06_LOCAL_BUCKLING_FIRST |

T360 is also retained as an R06 local-buckling-first regression specimen under its registered local geometry.

---

# 10. R11 UHPC scalar constitutive law

## 10.1 Domain and sign convention

Tension is positive. Compression is negative.

Current compression-contact calculation only admits

\[
-\varepsilon_{c0}\le\varepsilon\le\varepsilon_{t,lim}.
\]

The active scalar law is

\[
\boxed{
\sigma_U(\varepsilon)=
\begin{cases}
\sigma_c(\varepsilon),&-\varepsilon_{c0}\le\varepsilon<0,\\[2mm]
\sigma_t(\varepsilon),&0\le\varepsilon\le\varepsilon_{t,lim},\\[2mm]
0,&\varepsilon>\varepsilon_{t,lim}.
\end{cases}}
\]

Any candidate section state with \(\varepsilon<-\varepsilon_{c0}\) is outside the present compression-contact admissible domain and is rejected rather than evaluated on an invented post-peak branch.

## 10.2 Compression: sixth-degree source-anchored polynomial

Define compression magnitude coordinate

\[
\boxed{\xi=-\frac{\varepsilon}{\varepsilon_{c0}}},
\qquad 0\le\xi\le1,
\]

and

\[
\boxed{A_c=\frac{E_c\varepsilon_{c0}}{f_c}}.
\]

Define

\[
B_c=6-5A_c,
\qquad
C_c=4A_c-5.
\]

The normalized compression magnitude is

\[
\boxed{
g_c(\xi)=A_c\xi+B_c\xi^5+C_c\xi^6}.
\]

Therefore the signed stress is

\[
\boxed{
\sigma_c(\varepsilon)
=-f_c\left[A_c\xi+(6-5A_c)\xi^5+(4A_c-5)\xi^6\right]}.
\]

This is not a fit to BH/T360 capacity. Once \(E_c,f_c,\varepsilon_{c0}\) are supplied, all coefficients are fixed.

### 10.2.1 Exact endpoint conditions

At the origin:

\[
g_c(0)=0.
\]

Its derivative is

\[
\boxed{
g_c'(\xi)=A_c+5B_c\xi^4+6C_c\xi^5}.
\]

Hence

\[
\left.\frac{d\sigma_c}{d\varepsilon}\right|_{0^-}
=\frac{f_cA_c}{\varepsilon_{c0}}
=E_c.
\]

At the compression peak:

\[
g_c(1)=1,
\qquad
g_c'(1)=0,
\]

so

\[
\boxed{\sigma_c(-\varepsilon_{c0})=-f_c},
\qquad
\boxed{
\left.\frac{d\sigma_c}{d\varepsilon}\right|_{-\varepsilon_{c0}}=0}.
\]

### 10.2.2 Shape gate

The derivative can be factored as

\[
g_c'(\xi)
=(\xi-1)
\left[(24A_c-30)\xi^4
-A_c(\xi^3+\xi^2+\xi+1)\right].
\]

A simple sufficient source-shape gate for monotone nonnegative ascent on \(0\le\xi\le1\) is

\[
\boxed{0<A_c\le1.5}.
\]

If the supplied \(E_c,f_c,\varepsilon_{c0}\) violate this gate, the implementation must report

```text
UHPC_COMPRESSION_POLYNOMIAL_CONTRACT_FAIL
```

rather than clip coefficients or silently revert to R10/Hu/Zhang.

### 10.2.3 Current default numerical polynomial

For

\[
E_c=43400\ \mathrm{MPa},
\qquad
f_c=141.1\ \mathrm{MPa},
\qquad
\varepsilon_{c0}=0.0035,
\]

\[
A_c=1.076541459957477,
\]

\[
B_c=0.617292700212615,
\]

\[
C_c=-0.693834160170092.
\]

Thus

\[
\boxed{
\sigma_c=-141.1
\left[
1.076541459957477\,\xi
+0.617292700212615\,\xi^5
-0.693834160170092\,\xi^6
\right]\ \mathrm{MPa}}.
\]

No yield plateau exists in the UHPC law.

## 10.3 Why no compression descending branch is active in R11

The present terminal is first contact with

\[
\varepsilon=-\varepsilon_{c0}.
\]

Therefore the active section domain never requires \(\xi>1\) for an admissible compression-controlled root.

R11 deliberately avoids adding a post-peak branch that the present terminal cannot reach. If a future theory changes the terminal to permit post-peak UHPC redistribution, the descending branch must be reopened from a source before calculations proceed; it must not be inferred from R10 or invented from continuity alone.

## 10.4 Tension: Hiew-anchor finite cubic-Hermite law

The Hiew evidence shows fibre-bridged UHPC tension as

```text
origin
-> effective cracking
-> strain hardening
-> tensile peak
-> localisation
-> softening/pullout
-> tensile limit
```

R11 does not retain Hiew's exponential tail as an exponential function. Instead it performs a transparent **material-level analytic transformation**: preserve the source anchors and build a finite shape-preserving cubic Hermite law. This is a project transformation, not a claim that Hiew's published equation itself is cubic.

Define five nodes:

\[
(\varepsilon_0,s_0)=(0,0),
\]

\[
(\varepsilon_1,s_1)=(\varepsilon_{t,cr},f_{t,cr}),
\]

\[
(\varepsilon_2,s_2)=(\varepsilon_{t,peak},f_{t,peak}),
\]

\[
(\varepsilon_3,s_3)=(\varepsilon_{t,loc},f_{t,loc}),
\]

\[
(\varepsilon_4,s_4)=(\varepsilon_{t,lim},0).
\]

Require

\[
0<\varepsilon_1<\varepsilon_2<\varepsilon_3<\varepsilon_4,
\]

\[
0<s_1\le s_2,
\qquad
0<s_3\le s_2.
\]

For each interval

\[
h_i=\varepsilon_{i+1}-\varepsilon_i,
\qquad
 d_i=\frac{s_{i+1}-s_i}{h_i}.
\]

### 10.4.1 Node slopes

The origin slope is fixed by the same small-strain modulus as compression:

\[
\boxed{m_0=E_c}.
\]

For internal nodes \(i=1,2,3\), define

\[
 m_i=0,
\qquad d_{i-1}d_i\le0,
\]

and otherwise

\[
\boxed{
 m_i=
\frac{w_1+w_2}
{w_1/d_{i-1}+w_2/d_i}},
}
\]

where

\[
w_1=2h_i+h_{i-1},
\qquad
w_2=h_i+2h_{i-1}.
\]

At the tensile terminal:

\[
\boxed{m_4=0}.
\]

This gives zero slope automatically at the tensile peak whenever the source secants change sign there, and gives a zero tangent at the tensile limit before joining the zero-stress branch.

The first interval additionally requires the shape-preserving gate

\[
\boxed{0<E_c\le3d_0=\frac{3f_{t,cr}}{\varepsilon_{t,cr}}}.
\]

If this is violated, the source-anchor set is incompatible with the imposed common origin tangent and the input is rejected. The implementation must not clip \(E_c\) or move \(f_{t,cr}\).

### 10.4.2 Cubic on each interval

For

\[
u=\frac{\varepsilon-\varepsilon_i}{h_i}\in[0,1],
\]

use Hermite basis

\[
H_{00}=2u^3-3u^2+1,
\]

\[
H_{10}=u^3-2u^2+u,
\]

\[
H_{01}=-2u^3+3u^2,
\]

\[
H_{11}=u^3-u^2.
\]

Then

\[
\boxed{
\sigma_t(\varepsilon)
=H_{00}s_i+H_{10}h_im_i+H_{01}s_{i+1}+H_{11}h_im_{i+1}}.
\]

Equivalently,

\[
\boxed{
\sigma_t=c_{i0}+c_{i1}u+c_{i2}u^2+c_{i3}u^3},
\]

with

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

This is a finite cubic polynomial in every source interval.

### 10.4.3 Current representative numerical cubic coefficients

Using the current G16R representative anchor set exactly as displayed in Section 5.4 and \(E_c=43400\) MPa, the deterministic node slopes are

```text
m0 = +43400.000000000 MPa
m1 =   +757.094372739 MPa
m2 =      0.000000000 MPa
m3 =   -312.701361245 MPa
m4 =      0.000000000 MPa
```

The corresponding normalized-u cubics are:

Interval 0, \(0\le\varepsilon\le0.00042\):

\[
\boxed{
\sigma_t
=18.228000000000u
-7.470825636550u^2
-0.989456363450u^3\ \mathrm{MPa}}.
\]

Interval 1, \(0.00042\le\varepsilon\le0.00380\):

\[
\boxed{
\sigma_t
=9.767718000000
+2.558978979857u
-2.216657959715u^2
+0.624778979857u^3\ \mathrm{MPa}}.
\]

Interval 2, \(0.00380\le\varepsilon\le0.00690\):

\[
\boxed{
\sigma_t
=10.734818000000
-0.191145780142u^2
-0.195694219858u^3\ \mathrm{MPa}}.
\]

Interval 3, \(0.00690\le\varepsilon\le0.00759\):

\[
\boxed{
\sigma_t
=10.347978000000
-0.215763939259u
-30.612406121482u^2
+20.480192060741u^3\ \mathrm{MPa}}.
\]

The implementation shall generate these coefficients from the anchor/slopes equations rather than store them as specimen-specific magic constants. The displayed numbers are an audit example for the current representative anchor set.

### 10.4.4 Continuity and source role

The tension construction is C1 at every internal node by definition. At the origin,

\[
\sigma_t(0)=0,
\qquad
\sigma_t'(0^+)=E_c,
\]

matching the compression-side origin tangent.

At the tensile peak, the shape-preserving internal rule gives

\[
\sigma_t'(\varepsilon_{t,peak})=0
\]

when the hardening and softening secants have opposite signs.

At the tensile limit,

\[
\sigma_t(\varepsilon_{t,lim})=0,
\qquad
\sigma_t'(\varepsilon_{t,lim})=0,
\]

so the continuation \(\sigma_t=0\) for larger positive strain is C1.

---

# 11. Exact UHPC material primitives

Define

\[
\boxed{F_0'(\varepsilon)=\sigma_U(\varepsilon)},
\qquad
\boxed{F_1'(\varepsilon)=\varepsilon\sigma_U(\varepsilon)},
\]

with

\[
F_0(0)=F_1(0)=0.
\]

## 11.1 Compression primitives

For \(-\varepsilon_{c0}\le\varepsilon<0\), let

\[
\xi=-\frac{\varepsilon}{\varepsilon_{c0}}.
\]

Then

\[
\boxed{
F_{0c}(\varepsilon)
=f_c\varepsilon_{c0}
\left[
\frac{A_c}{2}\xi^2
+\frac{B_c}{6}\xi^6
+\frac{C_c}{7}\xi^7
\right]},
\]

\[
\boxed{
F_{1c}(\varepsilon)
=-f_c\varepsilon_{c0}^2
\left[
\frac{A_c}{3}\xi^3
+\frac{B_c}{7}\xi^7
+\frac{C_c}{8}\xi^8
\right]}.
\]

These are finite polynomials. No logarithm, arctangent, hypergeometric function or incomplete Gamma function remains.

## 11.2 Tension primitives

On interval i write

\[
\sigma_t=c_{i0}+c_{i1}u+c_{i2}u^2+c_{i3}u^3,
\qquad
u=\frac{\varepsilon-\varepsilon_i}{h_i}.
\]

Define

\[
\mathcal A_i(u)
=c_{i0}u
+\frac{c_{i1}}{2}u^2
+\frac{c_{i2}}{3}u^3
+\frac{c_{i3}}{4}u^4,
\]

\[
\mathcal B_i(u)
=\frac{c_{i0}}{2}u^2
+\frac{c_{i1}}{3}u^3
+\frac{c_{i2}}{4}u^4
+\frac{c_{i3}}{5}u^5.
\]

The incremental primitives from the left endpoint are

\[
\boxed{
\Delta F_{0,i}(u)=h_i\mathcal A_i(u)},
\]

\[
\boxed{
\Delta F_{1,i}(u)
=h_i\varepsilon_i\mathcal A_i(u)
+h_i^2\mathcal B_i(u)}.
\]

The global tensile primitive is obtained by adding the completed previous intervals:

\[
F_{0t}(\varepsilon)
=\sum_{j<i}h_j\mathcal A_j(1)+h_i\mathcal A_i(u),
\]

\[
F_{1t}(\varepsilon)
=\sum_{j<i}
\left[h_j\varepsilon_j\mathcal A_j(1)+h_j^2\mathcal B_j(1)\right]
+h_i\varepsilon_i\mathcal A_i(u)+h_i^2\mathcal B_i(u).
\]

For \(\varepsilon\ge\varepsilon_{t,lim}\), stress is zero and both primitives remain constant at their tensile-limit values.

Therefore the complete R11 scalar section law has exact finite polynomial primitives over every active interval.

---

# 12. Exact continuous-thickness UHPC section resultants

For either direction \(i\in\{x,y\}\), use affine section strain

\[
\boxed{\varepsilon_i(z)=\varepsilon_i^0+\kappa_i z},
\qquad
-\frac{t_c}{2}\le z\le\frac{t_c}{2}.
\]

Endpoint strains:

\[
\varepsilon_i^+=\varepsilon_i^0+\kappa_i\frac{t_c}{2},
\qquad
\varepsilon_i^-=\varepsilon_i^0-\kappa_i\frac{t_c}{2}.
\]

For \(\kappa_i\ne0\):

\[
\boxed{
N_i^U
=(1-\rho_w)
\frac{F_0(\varepsilon_i^+)-F_0(\varepsilon_i^-)}{\kappa_i}},
\]

\[
\boxed{
M_i^U
=(1-\rho_w)
\frac{
F_1(\varepsilon_i^+)-F_1(\varepsilon_i^-)
-\varepsilon_i^0
[F_0(\varepsilon_i^+)-F_0(\varepsilon_i^-)]
}{\kappa_i^2}}.
\]

For \(\kappa_i=0\), use the exact continuous limit

\[
\boxed{
N_i^U=(1-\rho_w)t_c\sigma_U(\varepsilon_i^0)},
\qquad
\boxed{M_i^U=0}.
\]

No thickness mesh is introduced. Every change of polynomial material interval is handled by the primitive itself; the section formula remains an endpoint difference.

## 12.1 Current scalar-section approximation boundary

R11 evaluates the same scalar law in x and y section directions. Initial Poisson coupling remains in the initial A/D operator. R11 does **not** claim that this is the final source-frozen 2D UHPC current operator.

Therefore:

```text
R11_SECTION_SCALAR_NM = CURRENT_CAPACITY_CONTACT_OPERATOR
FULL_NONLINEAR_2D_UHPC_POISSON_TC_CC_TT_OPERATOR = NOT_FROZEN
```

This boundary must remain visible in any paper/theory claim.

---

# 13. Steel-face section contributions — unchanged

Let upper/lower face stresses after the applicable R04/R06 operator be

\[
(\sigma_x^+,\sigma_y^+),
\qquad
(\sigma_x^-,\sigma_y^-).
\]

Then

\[
\boxed{
N_x^s=t_s(\sigma_x^++\sigma_x^-)},
\]

\[
\boxed{
M_x^s=t_sz_f(\sigma_x^+-\sigma_x^-)},
\]

\[
\boxed{
N_y^s=t_s(\sigma_y^++\sigma_y^-)},
\]

\[
\boxed{
M_y^s=t_sz_f(\sigma_y^+-\sigma_y^-)}.
\]

The steel-face law and UHPC law are separate phase operators and must not share material parameters.

---

# 14. Longitudinal web steel phase — unchanged ideal EP

The web occupies the UHPC-subtracted area fraction \(\rho_w\) and is added back as steel.

For axial web strain

\[
\varepsilon_y^w(z)=\varepsilon_y^0+\kappa_yz,
\]

use

\[
\boxed{
\sigma_y^w(z)=\operatorname{clip}(E_s\varepsilon_y^w(z),-f_y,+f_y)}.
\]

The yield crossings are exact:

\[
\varepsilon_y^w=\pm\frac{f_y}{E_s}.
\]

The thickness is split only at those analytic crossing locations and integrated in closed form. This is not numerical quadrature.

Web resultants are denoted

\[
N_y^w,
\qquad
M_y^w.
\]

No transverse web term is added unless a separate physical web orientation exists in the specimen definition.

---

# 15. Total section generalized forces

Total section output is

\[
\boxed{
\mathbf S=
\begin{bmatrix}
N_x\\M_x\\N_y\\M_y
\end{bmatrix}
=\mathbf S_U+\mathbf S_{s,+}+\mathbf S_{s,-}+\mathbf S_w}.
\]

Explicitly:

\[
\boxed{
N_x=N_x^U+t_s(\sigma_x^++\sigma_x^-)},
\]

\[
\boxed{
M_x=M_x^U+t_sz_f(\sigma_x^+-\sigma_x^-)},
\]

\[
\boxed{
N_y=N_y^U+t_s(\sigma_y^++\sigma_y^-)+N_y^w},
\]

\[
\boxed{
M_y=M_y^U+t_sz_f(\sigma_y^+-\sigma_y^-)+M_y^w}.
\]

The UHPC volume reduction \((1-\rho_w)\) and web-steel add-back \(\rho_w\) must appear exactly once each.

---

# 16. Capacity-contact closure

Historical section coordinates are

\[
(q,\varepsilon_x^0,\kappa_x,\varepsilon_y^0,\kappa_y).
\]

Four section/Airy balances:

\[
\boxed{N_x-N_x^A=0},
\]

\[
\boxed{M_x-M_x^A=0},
\]

\[
\boxed{N_y-N_y^A=0},
\]

\[
\boxed{M_y-M_y^A=0}.
\]

## 16.1 Primary compression terminal

The active R11 compression limit is the actual polynomial peak strain:

\[
\boxed{\varepsilon_{c,lim}=\varepsilon_{c0}}.
\]

For the current orientation the archived terminal is lower-core contact:

\[
\boxed{
\varepsilon_y\left(-\frac{t_c}{2}\right)
=\varepsilon_y^0-\kappa_y\frac{t_c}{2}
=-\varepsilon_{c0}}.
\]

Hence

\[
\boxed{
\varepsilon_y^0
=-\varepsilon_{c0}+\kappa_y\frac{t_c}{2}}.
\]

This removes \(\varepsilon_y^0\) and leaves four unknowns

\[
\boxed{(q,\varepsilon_x^0,\kappa_x,\kappa_y)}
\]

for the four equilibrium equations.

## 16.2 Admissibility

An R11 compression-controlled candidate must satisfy at least:

```text
q > 0
kappa_y >= 0
four N/M residuals within tolerance
all UHPC compression endpoints >= -eps_c0
all tensile endpoints <= eps_t_lim
R04/R06 event-order rule satisfied on each face
R02 uses the minimum-energy nonnegative cubic candidate
web yield regions consistent with analytic crossings
```

Among admissible compression-contact roots, select the first/smallest positive-q root. FEM/test load is forbidden from selecting among roots.

## 16.3 Tension-first fail-fast gate

If a candidate path/state reaches

\[
\varepsilon=\varepsilon_{t,lim}
\]

before the compression terminal, the current `FORCE_FIRST_COMPRESSION_CONTACT` closure is no longer sufficient.

R11 does not silently ignore that event. It returns

```text
UHPC_TENSION_FIRST_TERMINAL_NOT_CLOSED
```

and stops. A future tension-first terminal must be derived explicitly before such a case is accepted.

For the currently studied BH axial-compression family, the existing capacity-contact calculations have been compression-controlled; R11 shall verify this rather than assume it by specimen name.

---

# 17. Formal algebraic status and solver doctrine

R11 materially improves the algebraic structure:

```text
UHPC compression stress: degree 6
UHPC compression F0:     degree 7 in xi
UHPC compression F1:     degree 8 in xi
UHPC tension stress:     degree 3 per interval
UHPC tension F0:         degree 4 per interval
UHPC tension F1:         degree 5 per interval
R02 local amplitude:     cubic stationary equation
web steel:               finite piecewise polynomial at exact yield crossings
R04 steel:               finite algebraic radial cap
R06 local maximisation:  finite algebraic stationary/corner candidate set
```

No material special function remains in the scalar UHPC section operator.

However, the complete current structural closure still contains piece-selection/event equations and the R06 first-yield condition. Therefore the final **zero-iteration all-root polynomial elimination backend is not yet frozen**.

Current formal doctrine:

```text
THEORY = finite equations/events stated above
NUMERICAL root/brentq = allowed only as transparent execution evaluator
FORMAL TARGET = resultants / companion matrices / RootOf / all-real-root enumeration
STRUCTURAL Newton/path continuation = not the target formal method
```

A future algebraic backend must solve the same R11 equations; it may not simplify the material again merely to lower polynomial degree.

---

# 18. Excel / implementation transfer contract

## 18.1 R10 workbook status

The workbook

`NZSCCM_钢壳UHPC_R10_简化材料_线弹性平台受压_受拉零_20260901.xlsx`

is retired as a current material implementation because its UHPC law is R10.

It may be retained only as historical evidence of the oversimplification test.

## 18.2 R07/R08 status

The earlier R07/R08 Hu-based workbooks remain useful as dependency/no-lookup audits and previous-material regressions. They are not R11 material implementations.

## 18.3 Required R11 workbook identity

The next workbook must expose, visibly and independently:

```text
Geometry inputs
Steel inputs
UHPC Ec,nu_c,fc,eps_c0
Hiew tensile anchor inputs / source selector
Ac,Bc,Cc
Hiew interval h_i,d_i,m_i
all cubic coefficients c_i0..c_i3
A/D
integer mode table
Airy Pcr,C,Kx,G,Jx,Jy
R04/R06 branch gate
R02 cubic coefficients and selected U
face resultants
UHPC endpoint strains
UHPC F0/F1 endpoint values
UHPC N/M
web N/M
four closure residuals
q
P_u
branch/status flags
```

Changing a physical input must propagate through the formulas. Specimen ID must remain a label only and must not be read by the engine for result lookup.

## 18.4 Implementation prohibition

The new workbook shall not contain:

```text
historical BH Pu lookup table inside the engine
specimen-ID switch returning stored roots
33 eta nodes
8-level terminal grids
hidden FEM target values in residual equations
hard-coded BH050 q
hard-coded branch by specimen name
```

---

# 19. Current numerical provenance — do not confuse identities

## 19.1 Previous Hu-based current-operator reruns

These are **historical Hu-material results**, not R11 predictions:

```text
BH005  R04  P =  2.4623346768686 MN
BH010  R04  P =  4.5834217800205 MN
BH020  R04  P =  8.5787958279264 MN
BH032  R06  P = 10.9405345132294 MN
BH050  R06  P = 13.3563763545430 MN
```

## 19.2 Retired R10 oversimplified-material results

These are **R10 historical comparator values**, not R11 predictions:

```text
BH005  R04  P =  2.456276463270581 MN
BH010  R04  P =  4.587123324786989 MN
BH020  R04  P =  8.646251511137743 MN
BH032  R06  P = 11.072946520366022 MN
BH050  R06  P = 13.479943092945515 MN
```

## 19.3 R11 result status

At issuance of this ledger:

```text
R11_UHPC_MATERIAL_FORMULA = FROZEN_BY_LEDGER
R11_UHPC_PRIMITIVES = CLOSED_ANALYTICALLY
R11_STRUCTURAL_CHAIN = SPECIFIED
R11_BH005_BH050_FULL_RERUN = NOT_YET_EXECUTED
R11_EXCEL = NOT_YET_GENERATED
```

No old Hu or R10 number may be copied into an R11 output cell and labelled as an R11 prediction.

---

# 20. Current BH-family input registry

The following table is retained as the current specimen parameter master for regression inputs. Units are mm / MPa unless noted.

| specimen | b | a_phys | tc | ts | A0g | Aw | Lx | Ly | A0local |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| BH005 | 250 | 500 | 42 | 4 | 0.625 | 1332 | 56.25 | 55.55556 | 0.03515625 |
| BH010 | 500 | 1000 | 42 | 4 | 1.25 | 1332 | 112.5 | 111.1111 | 0.0703125 |
| BH020 | 1000 | 2000 | 42 | 4 | 2.5 | 1332 | 225 | 222.2222 | 0.140625 |
| BH032 | 1600 | 3200 | 42 | 4 | 4.0 | 1332 | 360 | 355.5556 | 0.225 |
| BH050 | 2500 | 5000 | 42 | 4 | 6.25 | 1332 | 562.5 | 555.5556 | 0.3515625 |

Common current steel/UHPC compression defaults:

```text
Es      = 206000 MPa
nu_s    = 0.30
fy      = 355 MPa
Ec      = 43400 MPa
nu_c    = 0.20
fc      = 141.1 MPa
eps_c0  = 0.0035
```

Current representative Hiew tension anchors are those listed in Section 5.4. They are material-source inputs, not specimen-specific calibration parameters.

---

# 21. Historical BH050 Airy regression values retained for audit

For the archived BH050 geometry/operator:

```text
m*   = 2
ell  = 2500 mm
Pcr  = 19.5818772367311 MN
Kx   = 4.272925966136171e6 N/mm
G    = 4.400171479082513e6 N/mm
C    = 1.0841371806523354e10 N
Jx   = 6.234616244717026e6 N
Jy   = 6.298311709061200e6 N
```

These are front-end A/D/Airy quantities. R11 does not change them when the same initial \(E_c,\nu_c\) are used.

The previous Hu capacity-contact checkpoint

```text
q = 0.004772819645833164
P = 13.3563763545430 MN
```

is a **previous-material regression target only**. It is not an R11 root constraint.

---

# 22. Explicitly prohibited theory substitutions

The following may not be introduced to make R11 easier to calculate:

1. return to R10 UHPC elastic-perfectly-plastic compression;
2. set UHPC tension to zero;
3. replace the sixth-degree compression polynomial by a line/plateau without a new user/source decision;
4. choose Hiew tensile anchors by matching BH/T360/FEM Pu;
5. restore Hu incomplete-Gamma tension merely because an existing spreadsheet already implements it;
6. restore Zhang/Popovics compression merely because an existing solver already implements it;
7. replace R02 by a secant local stiffness or effective width;
8. replace R06 first-yield maximisation by fixed local spatial sampling;
9. use 33 eta nodes or an eta fitted quintic as formal theory;
10. use a terminal strain grid/refinement hierarchy as formal theory;
11. use a specimen-ID branch switch;
12. use Abaqus/test values to choose among multiple roots;
13. call the scalar section operator a complete multidimensional UHPC constitutive model;
14. silently add Liu/DP/W-W capacity enhancement into the scalar stress update;
15. silently remove the current steel ideal-EP law while correcting the UHPC law.

---

# 23. Material and mechanics gate table

| Gate | R11 status | Meaning |
|---|---|---|
| UHPC compression origin | PASS by formula | \(\sigma(0)=0,\ d\sigma/d\varepsilon=E_c\) |
| UHPC compression peak | PASS by formula | \(\sigma=-f_c,\ tangent=0\) at \(-\varepsilon_{c0}\) |
| UHPC compression monotonicity | PARAMETRIC GATE | require \(0<A_c\le1.5\) |
| UHPC tension origin | PASS by construction | stress zero, tangent \(E_c\) |
| UHPC effective crack/peak/loc/limit | PASS by construction | exact source-anchor interpolation |
| UHPC tension peak slope | PASS by shape rule | zero when secant sign changes |
| UHPC tension terminal | PASS by construction | stress and tangent zero |
| UHPC thickness integration | PASS | exact primitive endpoint differences |
| UHPC special functions | ZERO | none in R11 scalar section operator |
| Initial plane-stress A/D | RETAINED | uses \(E_c,\nu_c\) |
| Full nonlinear 2D UHPC current operator | OPEN | not claimed by R11 |
| R02 | PASS finite algebraic | cubic all-root active set |
| R04/R06 branch | PASS mechanical gate | \(\sigma_{cr,s}^E\) vs \(f_y\) |
| R06 spatial grid | ZERO formal | finite stationary/corner set |
| Web thickness quadrature | ZERO | analytic yield crossings |
| Structure/root FEM calibration | ZERO | prohibited |
| Final zero-iteration structural root backend | OPEN | same equations must be algebraized |

---

# 24. Current open items and required next execution

R11 closes the **material-function simplification decision** but does not pretend that all downstream execution has already been redone.

The required next sequence is unique:

```text
NEXT-1
Implement R11 compression polynomial + Hiew-anchor cubic generator
and exact F0/F1 primitives in the current workbook/engine.

NEXT-2
Re-run BH005/BH010/BH020/BH032/BH050 from raw inputs,
with automatic R04/R06 switching and no historical target lookup.

NEXT-3
Perform post-hoc unfamiliar parameter pressure tests,
including changes in ts, A0g, Ec, fc, eps_c0 and Hiew anchor set.

NEXT-4
Only after the numerical R11 evaluator passes dependency/no-lookup audits,
compile the remaining R06 eta and terminal closure into finite algebraic/all-root form.
```

Failure discipline:

```text
material contract fail -> STOP
R02 no admissible candidate -> STOP
R06 no admissible yield event -> STOP
closure no admissible positive-q root -> STOP
tension terminal reached first -> STOP with explicit open status
```

No alternate constitutive law is to be tried automatically after any failure.

---

# 25. Final current-state lock

The current steel-shell–UHPC centralized technical identity after R11 is:

```text
GLOBAL STRUCTURE
  Marguerre–Airy one-complete-half-wave front-end
  initial composite A/D
  minimum integer mode

STEEL FACE
  automatic R04/R06 event order
  R02 exact cubic active set
  R04 plane-stress elastic trial + radial ideal-EP steel cap
  R06 exact local-yield finite algebraic maximisation

UHPC SCALAR SECTION
  compression:
    sigma/fc = -[Ac*xi + (6-5Ac)*xi^5 + (4Ac-5)*xi^6]
    0 <= xi <= 1
    Ac = Ec*eps_c0/fc
  tension:
    Hiew source anchors
    -> deterministic shape-preserving cubic Hermite pieces
  exact finite polynomial F0/F1
  zero thickness quadrature

WEB
  distributed longitudinal steel
  ideal EP
  exact analytic yield-crossing integration

SECTION CLOSURE
  Nx,Mx,Ny,My = Airy demand
  primary terminal = first compression contact at -eps_c0
  tension-first event = explicit fail-fast open branch

GOVERNANCE
  no material backfit to Pu
  no FEM/test root selection
  no effective width
  no spatial material-point grid
  no R09 fixed-grid detour
  no R10 UHPC elastic-perfectly-plastic simplification

FORMAL SOLVER TARGET
  finite polynomial/event equations
  all-real-root / resultant / companion / RootOf backend
  not structural Newton/path continuation as the final theory
```

In compact form:

\[
\boxed{
\text{Airy}
\rightarrow
\operatorname{AUTO}(R04,R02/R06)
\rightarrow
\text{UHPC polynomial section}
\rightarrow
\text{web steel}
\rightarrow
[N_x,M_x,N_y,M_y]\text{ closure}
\rightarrow
\text{first admissible capacity contact}
\rightarrow P_u
}
\]

and the material correction made by R11 is

\[
\boxed{
\cancel{\text{UHPC elastic-perfectly-plastic + zero tension}}
\quad\Longrightarrow\quad
\text{sixth-degree compression + Hiew-anchor cubic tension}
}
\]

This is the current centralized transfer baseline. Any future modification must identify explicitly whether it changes the material source, the scalar-section approximation, the multiaxial qualification layer, the steel-face event theory, the Airy backbone, or only the execution backend.
