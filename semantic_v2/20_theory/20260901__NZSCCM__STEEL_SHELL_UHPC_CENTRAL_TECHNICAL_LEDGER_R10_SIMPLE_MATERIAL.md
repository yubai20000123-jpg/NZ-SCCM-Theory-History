# NZ-SCCM — 钢壳–UHPC 极限承载力集中技术总账 R10 — SIMPLE MATERIAL

**Date:** 2026-09-01  
**Working branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Production main:** unchanged  
**Current transfer identity:** `STEEL_SHELL_UHPC_R10_SIMPLE_MATERIAL`  
**Supersedes for current execution:** R01 Hu-full evaluator and deprecated R09 finite-grid detour

---

# 0. Governing decision

R10 changes **only the UHPC scalar material law**. The accepted structural calculation process is unchanged:

```text
raw specimen/material inputs
-> initial full-composite A/D
-> minimum integer global mode
-> Marguerre–Airy Pcr,C,Kx,G,Jx,Jy
-> automatic R04/R06 steel-face branch
-> UHPC continuous-thickness N/M
-> longitudinal web ideal-EP N/M
-> total section N/M
-> four Airy/section balances
-> FORCE_FIRST_CAPACITY_CONTACT terminal
-> q
-> P_u
```

The following are not part of R10:

```text
33-point eta sampling
fitted quintic eta surrogate
terminal endpoint grid search
3x3x3 affine stencil
8-level refinement
material-point grid
spatial quadrature
effective-width/effective-area repair
FEM/test calibration or root selection
```

R09 was deprecated because those devices were solver engineering rather than derived mechanics.

---

# 1. Why the UHPC law is simplified

The prior Hu-Wenxu compression/tension law is source-valid but unnecessarily complicated for the present direct axial-capacity section calculation. In particular, the Hu tensile law generates incomplete-gamma primitives. R10 therefore selects a design-oriented piecewise-linear compression law and neglects UHPC tensile contribution in the axial capacity terminal.

This selection is made **before** FEM comparison and is based on source/analytic simplicity, not fit to the BH FEM values.

Source precedents:

1. Project steel-shell precedent for zero UHPC tension in the early axial N-M terminal:
   `20260825_1300__NZSCCM__STEEL_SHELL_UHPC_HU_EARLY_REPLACEMENT_THEORY_V1.md`.
2. Design-oriented UHPC literature documents linear-ascending + plateau idealizations for UHPC structural design; see the review discussion in:
   https://www.sciencedirect.com/science/article/pii/S0141029626003007

R10 is therefore a **simple design material module**, not a claim that UHPC has zero tensile strength physically.

---

# 2. Required inputs

Use N–mm–MPa.

```text
Geometry:
  b, a_phys, tc, ts, A0g

Web:
  Aw

Steel:
  Es, nu_s, fy

UHPC simple material:
  Ec, nu_c, fc, eps_cu_terminal

Local R02/R06 cell:
  Lx, Ly, A0_local
```

The former Hu tensile inputs

```text
fct, eps_t0, Vf, lf, df
```

are inactive in R10 and must not affect the result.

Derived:

\[
q_0=A_{0g}/b,
\qquad
\rho_w=\frac{A_w}{bt_c},
\qquad
z_f=\frac{t_c+t_s}{2}.
\]

The compression plateau begins at

\[
\boxed{\varepsilon_{cy}=\frac{f_c}{E_c}}.
\]

Material contract:

\[
E_c>0,\qquad f_c>0,\qquad
\boxed{\varepsilon_{cu}\equiv\varepsilon_{cu,terminal}\ge\varepsilon_{cy}}.
\]

Default carried terminal limit for the current BH family:

\[
\varepsilon_{cu}=0.0035.
\]

---

# 3. R10 UHPC scalar law

Sign convention: tension positive, compression negative.

\[
\boxed{
\sigma_U(\varepsilon)=
\begin{cases}
0, & \varepsilon\ge0,\\[4pt]
E_c\varepsilon, & -\varepsilon_{cy}\le\varepsilon<0,\\[4pt]
-f_c, & -\varepsilon_{cu}\le\varepsilon<-\varepsilon_{cy}.
\end{cases}}
\]

The capacity calculation terminates at first contact with `-eps_cu_terminal`; therefore no post-terminal material branch is required.

This material contains only constants and first-degree polynomials.

---

# 4. Exact UHPC primitives

Define

\[
F_0'(\varepsilon)=\sigma_U(\varepsilon),
\qquad
F_1'(\varepsilon)=\varepsilon\sigma_U(\varepsilon),
\]

with `F0(0)=F1(0)=0`.

For tension `eps>=0`:

\[
F_0=F_1=0.
\]

For the elastic compression interval `-eps_cy <= eps < 0`:

\[
\boxed{F_0(\varepsilon)=\frac12E_c\varepsilon^2},
\]

\[
\boxed{F_1(\varepsilon)=\frac13E_c\varepsilon^3}.
\]

For the compression plateau `eps < -eps_cy`:

\[
\boxed{F_0(\varepsilon)=-f_c\varepsilon-\frac12f_c\varepsilon_{cy}},
\]

\[
\boxed{F_1(\varepsilon)=-\frac12f_c\varepsilon^2+
\frac16f_c\varepsilon_{cy}^2}.
\]

These expressions are continuous at `eps=-eps_cy` and contain no Gamma, logarithm, arctangent, fractional power, numerical thickness quadrature, or material-point discretization.

For affine strain

\[
\varepsilon(z)=\varepsilon^0+\kappa z,
\qquad
\varepsilon_\pm=\varepsilon^0\pm\kappa t_c/2,
\]

if `kappa != 0`:

\[
\boxed{N^U=(1-\rho_w)
\frac{F_0(\varepsilon_+)-F_0(\varepsilon_-)}{\kappa}},
\]

\[
\boxed{M^U=(1-\rho_w)
\frac{F_1(\varepsilon_+)-F_1(\varepsilon_-)
-\varepsilon^0[F_0(\varepsilon_+)-F_0(\varepsilon_-)]}{\kappa^2}}.
\]

For `kappa=0`:

\[
N^U=(1-\rho_w)t_c\sigma_U(\varepsilon^0),
\qquad M^U=0.
\]

Thus the UHPC section operator is exact piecewise-polynomial.

---

# 5. Initial composite A/D — unchanged

Define

\[
K_s=\frac{E_s}{1-\nu_s^2},\qquad
K_c=\frac{E_c}{1-\nu_c^2},
\]

\[
G_s=\frac{E_s}{2(1+\nu_s)},\qquad
G_c=\frac{E_c}{2(1+\nu_c)}.
\]

\[
A_{11}=2t_sK_s+(1-\rho_w)t_cK_c,
\]

\[
A_{22}=A_{11}+\rho_wt_cE_s,
\]

\[
A_{12}=2t_s\nu_sK_s+(1-\rho_w)t_c\nu_cK_c.
\]

Steel-face centroid offset is retained once:

\[
D_f=2K_s\left(\frac{t_s^3}{12}+t_sz_f^2\right).
\]

\[
D_c=(1-\rho_w)K_c\frac{t_c^3}{12},
\qquad
D_w=\rho_wE_s\frac{t_c^3}{12},
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
+(1-\rho_w)G_c\frac{t_c^3}{12},
\]

\[
H=D_\mu+2D_{66}.
\]

---

# 6. Integer mode and Airy demand — unchanged

\[
\alpha=\pi/b,\qquad \beta_m=m\pi/a_{phys}.
\]

\[
N_{cr,m}=\frac{D_x\alpha^4+2H\alpha^2\beta_m^2+D_y\beta_m^4}{\beta_m^2},
\qquad P_{cr,m}=bN_{cr,m}.
\]

Select the minimum admissible integer mode without FEM/test information.

Let `Delta_A=A11*A22-A12^2` and `beta=beta_m*`. Then

\[
K_x=\frac{b^2\alpha^2}{8(A_{22}/\Delta_A)},
\qquad
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

\[
Q=q(q+2q_0),
\]

\[
\boxed{P(q)=P_{cr}\frac{q}{q+q_0}+CQ}.
\]

Airy generalized demand:

\[
N_x^A=K_xQ,
\quad
M_x^A=J_xq,
\quad
N_y^A=-\left(P/b-GQ\right),
\quad
M_y^A=J_yq.
\]

---

# 7. Steel face R04/R06 — unchanged

Automatic branch gate:

\[
\sigma_{cr,s}^{E}=\frac{\pi^2E_st_s^2}{12(1-\nu_s^2)L_x^2}
\frac{4(3r^4+2r^2+3)}{3r^2},
\qquad r=L_y/L_x.
\]

```text
sigma_cr,s^E >= fy -> R04_YIELD_FIRST
sigma_cr,s^E <  fy -> R06_LOCAL_BUCKLING_FIRST
```

R04 remains the current plane-stress elastic trial plus radial ideal-EP von-Mises cap.

R02 remains the constrained cubic active set

\[
B_3U^3+B_1U+B_0=0,
\]

with candidates `U=0` plus every nonnegative real cubic root, selecting minimum condensed energy.

R06 remains the source theory definition

\[
\Psi(\eta)=\max_{(u,v)\in[-1,1]^2}\Phi(u,v;\eta)-f_y^2,
\]

\[
\boxed{\eta_y=\min\{\eta\in(0,1]:\Psi(\eta)=0\}},
\]

where the local Mises maximum is obtained from the finite algebraic candidate set of interior stationary points, edge stationary points and corners described in
`20260825_1530__NZSCCM__STEEL_SHELL_COMMON_R06_LOCAL_YIELD_RESULTANT_GATE_V1.md`.

No 33-node surrogate belongs to the theory.

---

# 8. Web and total section — unchanged

The longitudinal web uses the exact ideal elastic-perfectly-plastic law

\[
\sigma_y^w=\operatorname{clip}(E_s\varepsilon_y^w,-f_y,+f_y)
\]

and is integrated analytically through the core thickness at its exact yield-crossing locations.

Total section:

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

---

# 9. Capacity-contact closure — same process, simplified material limit

Unknown section coordinates remain

\[
(q,\varepsilon_x^0,\kappa_x,\varepsilon_y^0,\kappa_y).
\]

Four balances:

\[
\boxed{[N_x,M_x,N_y,M_y]_{section}=[N_x^A,M_x^A,N_y^A,M_y^A]}.
\]

The fifth terminal equation retains exactly the same first-compression-limit contact form, but its material parameter is now the R10 terminal limit:

\[
\boxed{\varepsilon_y(-t_c/2)=-\varepsilon_{cu,terminal}}.
\]

For the current BH-family default

\[
\varepsilon_{cu,terminal}=0.0035.
\]

This is the same structural terminal architecture as before; only the scalar UHPC law and interpretation of the compression-limit parameter have changed.

Root admissibility remains physical:

```text
q > 0
kappa_y >= 0
all four N/M residuals within tolerance
no other UHPC endpoint already more compressive than -eps_cu_terminal
choose the first/smallest positive-q admissible capacity-contact root
FEM/test comparator is forbidden in root selection
```

---

# 10. Excel execution identity

Current executable workbook:

`NZSCCM_钢壳UHPC_R10_简化材料_线弹性平台受压_受拉零_20260901.xlsx`

The workbook follows the equations above and contains no Hu tension Gamma primitive and no R09 33-point/8-level detour.

Its `PY()` coupled root evaluator may use `scipy.optimize.root` and the existing R06 `brentq` only as a transparent numerical execution/validation backend. These numerical functions do not define or modify the mechanical theory. If a future formal algebraic root backend is implemented, it must solve the same equations without changing the material or structural chain.

---

# 11. Independent R10 regression — material frozen before comparator

Using the same BH geometry/steel/Airy/R04-R06 inputs and only replacing the UHPC scalar material law gives:

```text
BH005  R04  P = 2.456276463270581 MN
BH010  R04  P = 4.587123324786989 MN
BH020  R04  P = 8.646251511137743 MN
BH032  R06  P = 11.072946520366022 MN
BH050  R06  P = 13.479943092945515 MN
```

For reference, the prior full-Hu current values were

```text
BH005 2.4623346768686 MN
BH010 4.5834217800205 MN
BH020 8.5787958279264 MN
BH032 10.9405345132294 MN
BH050 13.3563763545430 MN
```

Thus the material simplification changes the five predictions by approximately

```text
BH005 -0.246%
BH010 +0.081%
BH020 +0.786%
BH032 +1.210%
BH050 +0.925%
```

Only after these calculations were frozen were the canonical FEM values compared:

```text
BH005 FEM 2.355811 MN  -> R10 +4.26%
BH010 FEM 4.304329 MN  -> R10 +6.57%
BH020 FEM 8.0079015 MN -> R10 +7.97%
BH032 FEM 10.990480 MN -> R10 +0.75%
BH050 FEM 12.591227 MN -> R10 +7.06%
```

All five remain within ±8%. This is an external verification result, not a calibration criterion.

---

# 12. Current verdict

```text
CURRENT_STEEL_SHELL_UHPC_BASELINE = R10_SIMPLE_MATERIAL
STRUCTURAL_CHAIN_CHANGED = NO
UHPC_COMPRESSION = LINEAR_ELASTIC_TO_fc_THEN_PLATEAU
UHPC_TENSION_IN_AXIAL_CAPACITY_TERMINAL = ZERO
UHPC_THICKNESS_PRIMITIVES = PIECEWISE_POLYNOMIAL_EXACT
SPECIAL_FUNCTIONS_IN_UHPC = 0
FORMAL_SPATIAL_QUADRATURE = 0
MATERIAL_POINTS = 0
R09_33_POINT_ETA = DEPRECATED
R09_8_LEVEL_TERMINAL_REFINEMENT = DEPRECATED
FEM_TEST_IN_PARAMETER_OR_ROOT_SELECTION = 0
PHYSICAL_SAME_Q_DEFORMATION_COMPATIBLE_TERMINAL = NOT_FROZEN
```

**END — R10 SIMPLE MATERIAL**
