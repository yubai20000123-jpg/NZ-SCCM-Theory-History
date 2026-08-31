# NZ-SCCM — 钢壳–UHPC 显式极限承载力理论集中技术总账 R01

**Date:** 2026-08-31  
**Working branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Role:** current steel-shell–UHPC theory / parameter / algorithm / Excel transfer baseline  
**Production main:** unchanged  
**Formal spatial quadrature:** `0`  
**Material-point grid:** `0`  
**Effective-width/effective-area repair:** prohibited  
**Comparator/test/FEM in parameter calibration or root selection:** `0`

---

# 0. Locked current identity

This ledger records one current mechanical chain only:

```text
raw specimen geometry + material parameters
-> initial composite A/D
-> minimum admissible integer global mode
-> Marguerre–Airy Pcr,C,Kx,G,Jx,Jy
-> q, Q=q(q+2q0), Airy generalized N/M demand
-> local steel branch gate sigma_cr,s^E versus fy
   -> R04_YIELD_FIRST when sigma_cr,s^E >= fy
   -> R02 + R06_LOCAL_BUCKLING_FIRST when sigma_cr,s^E < fy
-> Hu-Wenxu UHPC continuous-thickness section operator
-> longitudinal web ideal-EP constituent
-> S = SU + Ss,+ + Ss,- + Sw
-> four section/Airy N/M balances
-> FORCE_FIRST_CAPACITY_CONTACT_R01 terminal equation
```

The old 20260821 simplified `Z-section m_u(n)` capacity surface is **not** the current section model and must not be reintroduced merely to obtain a lower-degree terminal polynomial.

The source-audited BH050 capacity-contact checkpoint remains

```text
q = 0.004772819645833164
P = 13.3563763545430 MN
terminal_rule = FORCE_FIRST_CAPACITY_CONTACT_R01
output_identity = AIRY_NM_CAPACITY_CONTACT_PREDICTION
```

The later same-q deformation-compatible endpoint remains a separate research correction of curvature ownership and does not retroactively replace this archived capacity-contact map.

---

# 1. Source identity and chronology

The current capacity-contact regression must preserve source chronology.

1. `20260821_1733__NZSCCM__MARGUERRE_AIRY_EXPLICIT_LIMIT_THEORY_V1.md` supplies the global geometry, initial A/D, integer mode and Marguerre–Airy front-end.
2. The archived steel-shell/UHPC capacity calculations that produced the current R04/R06 checkpoints use the **Hu-Wenxu uniaxial UHPC backbone** as the section material source.
3. `20260825_1530__NZSCCM__STEEL_SHELL_COMMON_R06_LOCAL_YIELD_RESULTANT_GATE_V1.md` supplies the R04/R06 event-order gate and R06 local-yield resultant treatment.
4. `20260827_1623__NZSCCM__R02_NONNEGATIVE_AMPLITUDE_ACTIVESET_COMPLETION_R01.md` supplies the constrained R02 amplitude active set.
5. `20260825_1550__NZSCCM__STEEL_SHELL_COMMON_R06_Z6_NONREGRESSION_T360_BH032_BLIND_EXECUTION_R01.md` supplies the current T360/BH032 blind R06 checkpoints.
6. `20260825_1622__NZSCCM__STEEL_SHELL_COMMON_R06_SSUHPC_7CASE_BH050_FULL_EXECUTION_R01.md` supplies the source-audited BH050 full constituent closure.
7. Later 20260822 material research introduced Zhang/Hiew/Liu material candidates, but **no corresponding Pu rerun was performed at that stage**. Therefore those later material candidates must not be fused retrospectively with the archived R04/R06 Pu values.

Accordingly:

```text
CURRENT_CAPACITY_CONTACT_UHPC_BACKBONE = HU_WENXU_SOURCE_IDENTICAL
LATER_ZHANG_HIEW_LIU_MATERIAL_RESEARCH = SEPARATE_NOT_RETROACTIVE_TO_ARCHIVED_PU
```

---

# 2. Coordinates and global kinematics

Use N–mm–MPa.

```text
x = transverse
y = axial
z = through thickness, positive to upper face
```

\[
\psi=\sin(\alpha x)\sin(\beta y),\qquad
\alpha=\pi/b,\qquad \beta=m\pi/a_{phys}.
\]

\[
w_0=bq_0\psi,\qquad
w=b(q_0+q)\psi,\qquad
w_d=bq\psi,
\]

\[
\boxed{Q(q)=q(q+2q_0)}.
\]

Actual geometric curvature is owned by q:

\[
\kappa_x^{geo}=bq\alpha^2\psi,\qquad
\kappa_y^{geo}=bq\beta^2\psi.
\]

Historical capacity-contact coordinates \(\kappa_x^{cap},\kappa_y^{cap}\) must not be relabelled as these geometric curvatures.

---

# 3. Initial composite A/D and integer global mode

\[
K_s=\frac{E_s}{1-\nu_s^2},\qquad
K_c=\frac{E_c}{1-\nu_c^2},
\]

\[
G_s=\frac{E_s}{2(1+\nu_s)},\qquad
G_c=\frac{E_c}{2(1+\nu_c)}.
\]

\[
\rho_w=\frac{A_w}{bt_c},\qquad
z_f=\frac{t_c}{2}+\frac{t_s}{2}.
\]

The initial A/D operator contains the two steel faces, UHPC volume reduced by the distributed web volume, and the longitudinal web steel contribution.

Orthotropic bending convention:

\[
\boxed{H=D_\mu+2D_{66}}.
\]

For integer m,

\[
N_{cr,m}=\frac{D_x\alpha^4+2H\alpha^2\beta_m^2+D_y\beta_m^4}{\beta_m^2},
\qquad
P_{cr,m}=bN_{cr,m}.
\]

Select the minimum admissible integer mode without comparator information.

BH050 regression:

```text
m* = 2
ell = 2500 mm
Pcr = 19.5818772367311 MN
Kx = 4.272925966136171e6 N/mm
G  = 4.400171479082513e6 N/mm
C  = 1.0841371806523354e10 N
Jx = 6.234616244717026e6 N
Jy = 6.298311709061200e6 N
```

---

# 4. Marguerre–Airy compiled demand

\[
\boxed{P^A(q)=P_{cr}\frac{q}{q+q_0}+CQ(q)}.
\]

At the current capacity-contact control section used by the archived execution,

\[
N_x^A=K_xQ(q),
\]

\[
N_y^A=-\left[\frac{P^A(q)}{b}-GQ(q)\right],
\]

\[
M_x^A=J_xq,\qquad M_y^A=J_yq.
\]

The same convention must be used on both the demand and section sides.

---

# 5. R02 local steel-face operator

Local cell:

\[
0\le\xi\le L_x,\qquad 0\le\eta\le L_y,
\]

\[
\phi=(1-\cos k_x\xi)(1-\cos k_y\eta),\qquad
k_x=\frac{2\pi}{L_x},\quad k_y=\frac{2\pi}{L_y}.
\]

Exact local averages:

\[
\boxed{c_x=\frac{3k_x^2}{8}},\qquad
\boxed{c_y=\frac{3k_y^2}{8}}.
\]

\[
D_s=\frac{E_st_s^3}{12(1-\nu_s^2)},
\]

\[
K_b^\ell=D_s\left[\frac34(k_x^4+k_y^4)+\frac12k_x^2k_y^2\right].
\]

For the retained common-R06 qU-off baseline,

\[
d=U^2-A_0^2.
\]

The LL Airy compatibility contains exactly the seven harmonics

```text
(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1)
coefficients = 1/2,-1/2,1/2,-1,1/2,-1/2,1/2
```

and

\[
K_A=k_x^4k_y^4\left[
\frac{17}{256k_y^4}+\frac{17}{256k_x^4}
+\frac1{8(k_x^2+k_y^2)^2}
+\frac1{32(k_x^2+4k_y^2)^2}
+\frac1{32(4k_x^2+k_y^2)^2}
\right].
\]

R02 is a constrained finite algebraic active set:

\[
\boxed{U^*=\arg\min_{U\ge0}\Pi_{R02}(U)}.
\]

Because \(\Pi_{R02}\) is quartic in U, its stationarity equation is cubic. The candidate set is exactly

\[
\{U=0\}\cup\{\text{all nonnegative real cubic stationary roots}\}.
\]

---

# 6. Automatic R04 / R06 steel-face branch gate

First calculate the local elastic plate critical stress

\[
\sigma_{cr,s}^{E}=\frac{\pi^2E_st_s^2}{12(1-\nu_s^2)L_x^2}
\,k_{cr}(L_y/L_x),
\]

\[
k_{cr}=\frac{4(3r^4+2r^2+3)}{3r^2},\qquad r=L_y/L_x.
\]

The branch is mechanical, not a specimen-name lookup:

```text
if sigma_cr,s^E >= fy: R04_YIELD_FIRST
if sigma_cr,s^E <  fy: R06_LOCAL_BUCKLING_FIRST
```

## 6.1 R04 yield-first parent

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

\[
\sigma_{VM}^{tr}=
\sqrt{(\sigma_x^{tr})^2-\sigma_x^{tr}\sigma_y^{tr}+(\sigma_y^{tr})^2+3(\tau_{xy}^{tr})^2}.
\]

\[
\boxed{\lambda_p=\min\left(1,\frac{f_y}{\sigma_{VM}^{tr}}\right)},
\qquad
\boxed{\boldsymbol\sigma_s=\lambda_p\boldsymbol\sigma_s^{tr}}.
\]

No local-buckling reduction is inserted before yield in this branch.

## 6.2 R06 local-buckling-first

For \(\sigma_{cr,s}^{E}<f_y\), R02 is evaluated first. Along the generalized face-strain ray

\[
\boldsymbol\varepsilon_f(\eta)=\eta\boldsymbol\varepsilon_f,\qquad 0<\eta\le1,
\]

R02 is re-condensed and the exact LL local field is reconstructed. First local yield satisfies

\[
\boxed{\max_{[-1,1]^2}\sigma_{VM}(\eta_y)=f_y}.
\]

The section receives the whole-width R02 mean resultant at the projected state. Pointwise clipping and effective-width/effective-area replacement are prohibited.

Current family classification:

```text
BH005, BH010, BH020 -> R04_YIELD_FIRST
BH032, BH050, T360 -> R06_LOCAL_BUCKLING_FIRST
```

---

# 7. UHPC material parameter contract — Hu-Wenxu source-identical backbone

The current capacity-contact Excel and archived Pu checkpoints use the Hu-Wenxu uniaxial UHPC backbone.

## 7.1 Independent material inputs

The following are material inputs and are **not** forced to obey an invented empirical Ec(fc) relation:

```text
Ec      initial elastic modulus
fc      uniaxial compression-strength parameter
eps_c0  peak compression strain
fct     tensile-strength parameter
eps_t0  tensile strain scale
Vf      steel-fibre volume fraction
lf      fibre length
df      fibre diameter
nu_c    initial stiffness Poisson parameter
```

Hu Wenxu reports these mechanical properties as measured material quantities; the constitutive formula then builds its dimensionless shape parameters from them.

## 7.2 Derived compression parameters

\[
\boxed{E_0=\frac{f_c}{\varepsilon_{c0}}},
\qquad
\boxed{n_c=\frac{E_c}{E_0}=\frac{E_c\varepsilon_{c0}}{f_c}}.
\]

Let \(\xi=|\varepsilon_c|/\varepsilon_{c0}\). The compression magnitude is

\[
\widehat\sigma_c=
\begin{cases}
 f_c\dfrac{n_c\xi-\xi^2}{1+(n_c-2)\xi},&0\le\xi\le1,\\[6pt]
 f_c\dfrac{\xi}{2(\xi-1)^2+\xi},&\xi>1.
\end{cases}
\]

Compression stress in the project tension-positive sign convention is \(-\widehat\sigma_c\).

For the prepeak rational branch to remain regular over \(0\le\xi\le1\), the project material contract requires

\[
\boxed{n_c>1}.
\]

If a user supplies \((E_c,f_c,\varepsilon_{c0})\) with \(n_c\le1\), the input is incompatible with this locked Hu-Wenxu branch; the implementation must report a material-contract failure rather than silently change the material law.

## 7.3 Derived fibre/tension parameters

Hu Wenxu defines the steel-fibre factor

\[
\boxed{K_f=\left(\frac{l_f}{d_f}\right)V_f},
\]

and

\[
\boxed{m_t=0.85-0.47K_f+0.12K_f^2},\qquad 0<K_f\le3.
\]

The tensile curve is

\[
\boxed{
\sigma_t=f_{ct}\exp(1/m_t)\,\xi_t
\exp\left(-\frac{\xi_t^{m_t}}{m_t}\right)
},
\qquad
\xi_t=\frac{\varepsilon_t}{\varepsilon_{t0}}.
\]

For the current default fibre geometry

```text
lf = 13 mm
df = 0.2 mm
Vf = 0.02
```

\[
K_f=1.3,\qquad m_t=0.4418.
\]

Thus `m_t` is derived, not an independent editable parameter in the repaired Excel.

## 7.4 Material-contract gate

The parameterized implementation shall expose at least

```text
E0 = fc/eps_c0
n_c = Ec*eps_c0/fc
K_f = (lf/df)*Vf
m_t = 0.85 - 0.47*K_f + 0.12*K_f^2
```

and require positive physical scales together with

```text
n_c > 1
0 < K_f <= 3
m_t > 0
```

This is parameter validation inside the selected source law, not a second material model.

---

# 8. Exact continuous-thickness UHPC section operator

For direction \(i\in\{x,y\}\),

\[
\varepsilon_i(z)=\varepsilon_i^0+\kappa_i z.
\]

With UHPC effective volume fraction \(1-\rho_w\),

\[
N_i^U=(1-\rho_w)\int_{-t_c/2}^{t_c/2}
\sigma_U(\varepsilon_i^0+\kappa_i z)\,dz,
\]

\[
M_i^U=(1-\rho_w)\int_{-t_c/2}^{t_c/2}
z\sigma_U(\varepsilon_i^0+\kappa_i z)\,dz.
\]

Define exact primitives

\[
F_0'(\varepsilon)=\sigma_U(\varepsilon),\qquad
F_1'(\varepsilon)=\varepsilon\sigma_U(\varepsilon).
\]

For \(\kappa_i\ne0\),

\[
\boxed{N_i^U=\frac{1-\rho_w}{\kappa_i}
\left[F_0(\varepsilon_+)-F_0(\varepsilon_-)\right]},
\]

\[
\boxed{M_i^U=\frac{1-\rho_w}{\kappa_i^2}
\left\{F_1(\varepsilon_+)-F_1(\varepsilon_-)
-\varepsilon_i^0\left[F_0(\varepsilon_+)-F_0(\varepsilon_-)\right]\right\}}.
\]

For \(\kappa_i=0\), use the continuous limit

\[
N_i^U=(1-\rho_w)t_c\sigma_U(\varepsilon_i^0),\qquad M_i^U=0.
\]

Formal thickness Gauss points remain zero.

---

# 9. Longitudinal web and total section

The web phase is removed from UHPC volume and added back as its own longitudinal ideal-EP steel constituent:

\[
\sigma_y^w=\operatorname{clip}(E_s\varepsilon_y^w,-f_y,+f_y).
\]

Total generalized section resultant:

\[
\boxed{
\mathbf S=[N_x,M_x,N_y,M_y]^T
=\mathbf S_U+\mathbf S_{s,+}+\mathbf S_{s,-}+\mathbf S_w.
}
\]

Every constituent ledger must remain visible before summation.

---

# 10. Capacity-contact closure and physical root admissibility

Historical/source-audited section state:

\[
\mathbf x=[\varepsilon_x^0,\kappa_x^{cap},\varepsilon_y^0,\kappa_y^{cap}]^T.
\]

\[
\boxed{\mathbf R_4(\mathbf x,q)=\mathbf S(\mathbf x,q)-\mathbf D^A(q)=0}.
\]

For `FORCE_FIRST_CAPACITY_CONTACT_R01`,

\[
\boxed{\varepsilon_y(-t_c/2)=-\varepsilon_{c0}}.
\]

If the coupled nonlinear system has multiple mathematical roots, root selection must be physical rather than comparator-driven. For this terminal identity the admissible root must satisfy, at minimum:

```text
q > 0
four N/M residuals within tolerance
kappa_y >= 0 for the designated lower-y first-compression contact
no other UHPC x/y endpoint is already more compressive than -eps_c0
```

Among admissible capacity-contact roots, the first positive q is the terminal candidate. No test/FEM value may enter this screening.

---

# 11. Regression ledger after R04/R06 + UHPC parameter-contract repair

Exact current-state checkpoints reproduced by the repaired parameterized operator:

```text
T360:
q = 0.00134518627955957
P = 10.8183777809815 MN
branch = R06_LOCAL_BUCKLING_FIRST

BH032:
q = 0.00137889961633743
P = 10.9405345132294 MN
branch = R06_LOCAL_BUCKLING_FIRST

BH050:
q = 0.004772819645833164
P = 13.3563763545430 MN
branch = R06_LOCAL_BUCKLING_FIRST
```

The archived BH005/BH010/BH020 common-R06 comparison table carried forward R04 checkpoints without archiving their full current q/section state. The repaired current Hu-Wenxu + R04 operator independently recomputes:

```text
BH005: 2.4623346768686 MN
BH010: 4.5834217800205 MN
BH020: 8.5787958279264 MN
```

Historical carried R04 comparison values were approximately

```text
BH005: 2.46233215 MN
BH010: 4.58337285 MN
BH020: 8.55797773 MN
```

The small BH005/BH010 difference and visible BH020 difference must remain visible; they must not be hidden by preloading the historical values into the new parameterized evaluator.

A non-historical branch-switch test using BH050 geometry with `ts=8 mm` gives

```text
sigma_cr,s^E = 401.798669935469 MPa > fy = 355 MPa
branch = R04_YIELD_FIRST
q = 0.00357727807163097
P = 24.3096637453804 MN
```

This test is an implementation audit, not a calibrated prediction datum.

---

# 12. Formal root-method boundary versus Excel evaluator

The mechanical model and the root backend are separate identities.

Formal project rules remain:

1. finite polynomial subproblems such as R02 must enumerate all real roots plus active boundaries;
2. finite local Mises extrema must use finite algebraic candidates, not spatial sampling;
3. no load stepping or comparator-guided root selection is part of the formal theory;
4. the Hu-Wenxu UHPC thickness operator is analytic and must not be replaced by a simplified capacity surface.

The current R07 Excel is a **parameterization and source-consistency evaluator**. Its coupled terminal special-function system is numerically evaluated inside `PY()` so that raw-parameter propagation and R04/R06 switching can be tested now. This numerical evaluator is not to be relabelled as the final formal zero-iteration terminal backend.

```text
MECHANICAL_MODEL = CURRENT_SOURCE_IDENTICAL
R02_FORMAL_ROOT = FINITE_ALGEBRAIC
R04_FORMAL_OPERATOR = EXPLICIT_RADIAL_CAP
R06_LOCAL_EXTREMUM = FINITE_ALGEBRAIC
R07_EXCEL_COUPLED_TERMINAL_EVALUATOR = NUMERICAL_SPECIAL_FUNCTION_ROOT
FINAL_ZERO_ITERATION_COUPLED_TERMINAL_BACKEND = SEPARATE_FORMAL_IMPLEMENTATION_TASK
```

---

# 13. Minimum audit output

Every current calculation must retain:

```text
raw independent inputs
E0,n_c,K_f,m_t and UHPC material-contract status
m*, ell, alpha, beta
A/D and Pcr,C,Kx,G,Jx,Jy
sigma_cr,s^E and R04/R06 branch ID
R02 roots/energy when R02 is active
R04 lambda_p when R04 is active
R06 eta_y/U/certified local Mises when R06 is active
UHPC endpoint strains/branches and exact N/M
upper/lower steel-face resultants
web resultants
total section S
Airy demand D^A
four raw N/M residuals
terminal equation residual
terminal-rule ID
q and P
```

---

# 14. Current repaired verdict

```text
CURRENT_FORMAL_CHAIN = AIRY + AUTO(R04_OR_R02_R06) + HU_WENXU_UHPC + WEB + SECTION_CLOSURE
UHPC_Ec_fc_eps_c0 = INDEPENDENT_MATERIAL_INPUTS_WITH_DERIVED_n_c
UHPC_K_f = (lf/df)*Vf
UHPC_m_t = 0.85-0.47*K_f+0.12*K_f^2
UHPC_CONTRACT = n_c>1 AND 0<K_f<=3
R04_R06_SWITCH = AUTOMATIC_FROM_sigma_cr,s^E_vs_fy
BH050_CAPACITY_CONTACT_REGRESSION = 13.3563763545430 MN
OLD_V1_Z_SECTION_17.1449738_MN = EXCLUDED_HISTORICAL_SIMPLIFIED_MODEL
LATER_ZHANG_HIEW_LIU_PU_RERUN = NOT_EXECUTED_AT_THE_MATERIAL-RESEARCH_STAGE
FORMAL_SPATIAL_QUADRATURE = 0
COMPARATOR_IN_ROOT_SELECTION = 0
PHYSICAL_SAME_Q_TERMINAL = NOT_FROZEN
```

**END OF CENTRAL TECHNICAL LEDGER R01 — R04/R06 + HU-WENXU PARAMETER-CONTRACT REPAIR**
