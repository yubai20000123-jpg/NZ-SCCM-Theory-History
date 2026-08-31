# NZ-SCCM — 钢壳–UHPC 显式极限承载力理论集中技术总账 R01

**Date:** 2026-08-31  
**Repository:** `yubai20000123-jpg/NZ-SCCM-Theory-History`  
**Working branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Document role:** `CENTRAL_TECHNICAL_LEDGER / THEORY–PARAMETER–ALGORITHM–CODE MAPPING / TRANSFER BASELINE`  
**Production main:** unchanged by this document.  
**Formal spatial quadrature:** `0`  
**Material-point grid:** `0`  
**Effective-width/effective-area repair:** prohibited.  
**Comparator/test/FEM in parameter calibration or root selection:** `0`.

---

# 0. Locked theory identity

本总账只记录当前钢壳–UHPC 完整显式理论本体，不再把 20260821 早期 `Z-section m_u(n)` 简化容量面替换成当前截面理论，也不把后续 diagnostic 的变量解释问题反向删掉已经建立的 R02/R06/UHPC 模块。

当前母链唯一写成：

```text
raw geometry/material
-> initial composite A/D
-> integer global mode
-> Marguerre–Airy Pcr,C,Kx,G,Jx,Jy
-> q and Q=q(q+2q0)
-> Airy generalized N/M demand
-> UHPC continuous-thickness section operator
+ upper/lower steel-face R02
-> R06 local-yield resultant return when active
+ longitudinal web constituent
-> total section S = SU + Ss,+ + Ss,- + Sw
-> explicit section/global closure
```

当前 source-audited BH050 capacity-contact regression target remains

```text
q = 0.004772819645833164
P = 13.3563763545430 MN
terminal rule = FORCE_FIRST_CAPACITY_CONTACT_R01
output identity = AIRY_NM_CAPACITY_CONTACT_PREDICTION
```

`17.1449738 MN` belongs to the older 20260821 simplified Z-section capacity model and is **not** a regression target of this ledger.

The later same-q deformation-compatible endpoint remains a separate research correction of curvature ownership; it is not allowed to erase or silently replace the above source-audited capacity-contact map.

---

# 1. Source chain

1. `semantic_v2/20_theory/20260821_1733__NZSCCM__MARGUERRE_AIRY_EXPLICIT_LIMIT_THEORY_V1.md` — global geometry, initial composite stiffness, integer mode and Airy coefficient derivation only.
2. `semantic_v2/20_theory/20260822_1240__NZSCCM__UHPC_ZHANG_BACKBONE_AND_LIU_CC_CONTINUOUS_SOURCE_MIN_GATE.md` — UHPC compression/tension/current-section source and exact primitives.
3. `semantic_v2/20_theory/20260825_1530__NZSCCM__STEEL_SHELL_COMMON_R06_LOCAL_YIELD_RESULTANT_GATE_V1.md` — common R06 local-yield resultant gate.
4. `semantic_v2/20_theory/20260827_1623__NZSCCM__R02_NONNEGATIVE_AMPLITUDE_ACTIVESET_COMPLETION_R01.md` — R02 constrained active set.
5. `20260827_1135__NZSCCM__UNIFIED_Q_U_EXPLICIT_KINEMATIC_LEDGER_AND_GENERALIZED_WORK_R01.md` — verified local geometry/harmonic bookkeeping; qU generalized-work closure variants are not automatically reactivated.
6. `semantic_v2/40_execution/steel_shell/20260825_1622__NZSCCM__STEEL_SHELL_COMMON_R06_SSUHPC_7CASE_BH050_FULL_EXECUTION_R01.md` — BH050 source-audited full execution and 13.3563763545430 MN regression.
7. `semantic_v2/40_execution/steel_shell/20260827_2052__NZSCCM__BH050_BH032_CLASSICAL_W_KAPPA_EPS_KINEMATIC_RECONSTRUCTION_R01.md` — separates geometric curvature from historical capacity coordinates and records qU production retirement.

No source below may be replaced by the older simplified Z-section capacity surface merely because that older route produces a lower-degree q polynomial.

---

# 2. Units, coordinates and ownership

Use N–mm–MPa.  
`x`: transverse; `y`: axial; `z`: through thickness, positive to upper face.

Global geometry:
\[
0\le x\le b,\qquad0\le y\le a_{phys}.
\]

Global mode:
\[
\psi=\sin(\alpha x)\sin(\beta y),\qquad
\alpha=\pi/b,\qquad \beta=m\pi/a_{phys}.
\]

Initial/current deflection:
\[
w_0=bq_0\psi,\qquad w=b(q_0+q)\psi,\qquad w_d=bq\psi,
\]
\[
\boxed{Q(q)=q(q+2q_0)}.
\]

Actual geometric curvature is owned by q:
\[
\kappa_x^{geo}=bq\alpha^2\psi,\qquad
\kappa_y^{geo}=bq\beta^2\psi.
\]
Historical R4/J4 affine capacity coordinates are not to be renamed as these geometric curvatures.

---

# 3. Initial composite A/D and global mode

Plane-stress phase constants:
\[
K_s=E_s/(1-\nu_s^2),\qquad K_c=E_c/(1-\nu_c^2),
\]
\[
G_s=E_s/[2(1+\nu_s)],\qquad G_c=E_c/[2(1+\nu_c)].
\]

With distributed longitudinal-web ratio
\[
\rho_w=A_w/(bt_c),
\]
and face centroid
\[
z_f=t_c/2+t_s/2,
\]
current BH-family initial ABD is compiled from the two steel faces, UHPC volume reduced by the distributed web volume, and the actual longitudinal-web steel contribution. The BH050 audited target is

```text
A11=3.685652010989011e6 N/mm
A22=3.795408810989011e6 N/mm
A12=9.182293032967034e5 N/mm
A66=1.383711353846154e6 N/mm
Dx =1.236003299827839e9 Nmm
Dy =1.252137549427839e9 Nmm
Dmu=3.432434438483517e8 Nmm
D66=4.463799279897436e8 Nmm
H  =1.236003299827839e9 Nmm
```

Orthotropic convention:
\[
\boxed{H=D_\mu+2D_{66}}.
\]

Integer mode:
\[
N_{cr,m}=
\frac{D_x\alpha^4+2H\alpha^2\beta_m^2+D_y\beta_m^4}{\beta_m^2},
\qquad P_{cr,m}=bN_{cr,m}.
\]
Choose the minimum admissible integer mode without comparator information.

BH050:
\[
\boxed{m_*=2},\qquad \ell=2500\text{ mm},\qquad
\boxed{P_{cr}=19.5818772367311\text{ MN}}.
\]

---

# 4. Marguerre–Airy compiled demand

For the selected mode, compile
\[
P_{cr},\;C,\;K_x,\;G,\;J_x,\;J_y
\]
from geometry and initial A/D only.

Runtime:
\[
\boxed{P^A(q)=P_{cr}\frac{q}{q+q_0}+C Q(q)},
\]
\[
N_T^A=K_xQ(q)\cos(2\beta y),
\]
\[
N_L^A=-\left[P^A(q)/b+GQ(q)(1-2\sin^2\alpha x)\right],
\]
\[
M_T^A=J_xq\sin\alpha x\sin\beta y,
\qquad
M_L^A=J_yq\sin\alpha x\sin\beta y.
\]

BH050 audited coefficients:

```text
Kx=4.272925966136171e6 N/mm
G =4.400171479082513e6 N/mm
C =1.0841371806523354e10 N
Jx=6.234616244717026e6 N
Jy=6.298311709061200e6 N
```

---

# 5. R02 local steel-face operator

Local cell:
\[
0\le\xi\le L_x,\qquad0\le\eta\le L_y,
\]
\[
\phi=(1-\cos k_x\xi)(1-\cos k_y\eta),
\qquad k_x=2\pi/L_x,\quad k_y=2\pi/L_y.
\]

Exact local averages:
\[
\boxed{c_x=3k_x^2/8},\qquad
\boxed{c_y=3k_y^2/8},\qquad
\langle\phi_x\phi_y\rangle=0.
\]

Local plate stiffness:
\[
D_s=E_st_s^3/[12(1-\nu_s^2)],
\]
\[
\boxed{K_b^\ell=D_s[\tfrac34(k_x^4+k_y^4)+\tfrac12k_x^2k_y^2]}.
\]

For the retained production qU-off common-R06 baseline, the LL variables are
\[
d=U^2-A_0^2,
\]
and the cell-mean membrane terms follow the frozen execution sign convention used by the source-audited BH050 regression. Any GL/qU sensitivity terms must remain off unless their own version is explicitly selected.

LL Airy compatibility:
\[
\nabla^4F_{LL}=-E_sd(\phi_{xx}\phi_{yy}-\phi_{xy}^2).
\]
Exactly seven harmonics occur:
\[
(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1)
\]
with coefficients
\[
1/2,-1/2,1/2,-1,1/2,-1/2,1/2.
\]

Exact energy coefficient:
\[
K_A=k_x^4k_y^4\left[
\frac{17}{256k_y^4}+\frac{17}{256k_x^4}
+\frac1{8(k_x^2+k_y^2)^2}
+\frac1{32(k_x^2+4k_y^2)^2}
+\frac1{32(4k_x^2+k_y^2)^2}
\right].
\]

R02 condensation:
\[
\boxed{U^*=\arg\min_{U\ge0}\Pi_{R02}(U)}.
\]
Because \(\Pi_{R02}\) is quartic in U, \(d\Pi/dU\) is cubic. The candidate set is exactly
\[
\{U=0\}\cup\{\text{all positive real cubic stationary roots}\}.
\]
No Newton path is part of the formal R02 definition.

---

# 6. R06 local-yield resultant gate

Local elastic classification:
\[
\sigma_{cr,s}^{E}=
\frac{\pi^2E_st_s^2}{12(1-\nu_s^2)L_x^2}
\,k_{cr}(L_y/L_x),
\]
\[
k_{cr}=\frac{4(3r^4+2r^2+3)}{3r^2},\qquad r=L_y/L_x.
\]

If \(\sigma_{cr,s}^{E}\ge f_y\), use yield-first parent treatment.  
If \(\sigma_{cr,s}^{E}< f_y\), use `R06_LOCAL_BUCKLING_FIRST`.

For local-buckling-first, along the generalized face-strain ray
\[
\varepsilon_f(\eta)=\eta\varepsilon_f,\qquad0<\eta\le1,
\]
R02 is re-condensed and the exact LL local field is reconstructed. The first local yield satisfies
\[
\boxed{\max_{[-1,1]^2}\sigma_{VM}(\eta_y)=f_y}.
\]
The section receives the whole-width R02 mean resultant at that projected state; no effective width/area and no pointwise clipping are allowed.

BH050:
\[
\sigma_{cr,s}^{E}=100.449667483867\text{ MPa}<355\text{ MPa},
\]
therefore `R06_LOCAL_BUCKLING_FIRST`.

---

# 7. UHPC current material and exact thickness section operator

Compression magnitude
\[
x=|\varepsilon_c|/\varepsilon_{c0},
\]
\[
\kappa_U=E_c\varepsilon_{c0}/f_c,
\qquad
r=\frac{E_c}{E_c-f_c/\varepsilon_{c0}}.
\]

Ascending branch:
\[
\boxed{g_a(x)=\frac{rx}{r-1+x^r}},\qquad0\le x\le1.
\]

For the source-audited 2% fibre descending branch:
\[
\boxed{g_d(x)=0.18+\frac{0.82}{1+(2/3)(x-1)^2}},\qquad x\ge1.
\]

Affine through-thickness strain:
\[
\varepsilon_i(z)=\varepsilon_i^0+\kappa_i z.
\]

UHPC resultants:
\[
N_i^U=(1-\rho_w)\int_{-t_c/2}^{t_c/2}\sigma_U(\varepsilon_i^0+\kappa_i z)\,dz,
\]
\[
M_i^U=(1-\rho_w)\int_{-t_c/2}^{t_c/2}z\sigma_U(\varepsilon_i^0+\kappa_i z)\,dz.
\]

These are evaluated by exact endpoint primitives; formal thickness Gauss points are zero.

---

# 8. Section assembly

Face centroids:
\[
z_\pm=\pm(t_c/2+t_s/2).
\]

Total generalized section resultant:
\[
\boxed{
\mathbf S=[N_x,M_x,N_y,M_y]^T
=\mathbf S_U+\mathbf S_{s,+}+\mathbf S_{s,-}+\mathbf S_w
}.
\]

Every constituent ledger must remain available before summation. A total load alone is not an adequate audit output.

---

# 9. Current source-audited capacity-contact closure

Historical/source-audited state:
\[
\mathbf x=[\varepsilon_x^0,\kappa_x^{cap},\varepsilon_y^0,\kappa_y^{cap}]^T.
\]

Airy demand:
\[
\mathbf D^A(q)=[N_x^A,M_x^A,N_y^A,M_y^A]^T.
\]

Section residual:
\[
\boxed{\mathbf R_4(\mathbf x,q)=\mathbf S(\mathbf x,q)-\mathbf D^A(q)=0}.
\]

For `FORCE_FIRST_CAPACITY_CONTACT_R01`, the fifth terminal equation used by BH050 is
\[
\boxed{\varepsilon_y(-t_c/2)=-\varepsilon_{c0}}.
\]

This closure is reproducible and is the calculation identity that gives the frozen BH050 13.3563763545430 MN checkpoint. Its capacity-coordinate curvatures must not be relabelled as global geometric curvature.

---

# 10. BH050 source-audited terminal checkpoint

Input:

```text
b=2500 mm, a_phys=5000 mm, tc=42 mm, ts=4 mm
Aw=1332 mm2, rho_w=0.0126857142857143
q0=0.0025
Es=206000 MPa, nu_s=0.30, fy=355 MPa
Ec=43400 MPa, nu_c=0.20, fc=141.1 MPa, eps_c0=0.0035
Lx=562.5 mm, Ly=555.555555555556 mm, A0=0.3515625 mm
```

Terminal root:
\[
\boxed{q=0.004772819645833164},
\]
\[
\varepsilon_x^0=2.820431413\times10^{-5},
\]
\[
\kappa_x^{cap}=4.402758337803803\times10^{-5}\;\mathrm{mm^{-1}},
\]
\[
\varepsilon_y^0=-0.00213545799,
\]
\[
\kappa_y^{cap}=6.497819104663830\times10^{-5}\;\mathrm{mm^{-1}}.
\]

Airy load:
\[
\boxed{P=13.3563763545430\;\mathrm{MN}}.
\]

Demand at the terminal point:

```text
Nx_d=+199.305955403735 N/mm
Ny_d=-5137.30935871948 N/mm
Mx_d=29756.6988970160 N
My_d=30060.7058605883 N
```

Constituent totals close to the same values to numerical roundoff. This is the compulsory regression gate for any repaired Excel implementation of the current capacity-contact theory.

---

# 11. Zero-iteration implementation rule

The user's current execution rule is now locked as follows:

1. Where a subproblem is a finite polynomial, do **not** use Newton, Goal Seek or Solver. Enumerate all real roots explicitly and apply the same physical/active-set admissibility rules.
2. R02 is quartic-energy/cubic-stationarity and therefore must use `U=0 + all real cubic roots`.
3. Finite local Mises extrema must use finite edge/interior algebraic candidate equations, not spatial sampling.
4. No load stepping or path continuation is part of the formal theory.
5. The exact UHPC thickness operator remains the source-identical analytic operator. It must not be replaced by the older simplified `m_u(n)` Z-section surface merely to reduce the terminal equations to a sixth-degree q polynomial.
6. An Excel workbook may evaluate every explicit formula and every polynomial all-root block directly. A new-specimen full terminal root may be claimed only when the complete source-identical section closure has also been compiled without changing the above physics.

Thus `NO_ITERATION` changes the **root backend**, not the **mechanical model**.

---

# 12. Same-q research correction boundary

The later kinematic correction owns actual curvature by q:
\[
q\rightarrow w_d\rightarrow\kappa_x^{geo}(q),\kappa_y^{geo}(q).
\]
This is retained as a research correction of the physical interpretation of historical capacity coordinates. It does not authorize deletion of R02/R06/UHPC or replacement by the old simplified Z capacity surface.

`DEFORMATION_COMPATIBLE_STRUCTURAL_TERMINAL` remains `NOT_FROZEN` until a complete same-q structural terminal is derived and independently accepted.

---

# 13. Minimum audit output

Every current-theory calculation must retain:

```text
raw inputs
m*, ell, alpha, beta
A/D and Pcr,C,Kx,G,Jx,Jy
R02 cubic coefficients, all candidate roots/energies, selected U
R06 classification and, when active, eta_y + certified max Mises
UHPC face strains/active branches and exact N/M
upper/lower steel-face resultants
web resultants
section total S
Airy demand D^A
four raw N/M residuals
terminal equation residual
terminal-rule ID
q and P
```

---

# 14. Repair verdict

```text
CURRENT_FORMAL_CHAIN = AIRY + R02 + R06 + EXACT_UHPC + WEB + SECTION_CLOSURE
BH050_CAPACITY_CONTACT_REGRESSION = 13.3563763545430 MN
OLD_V1_Z_SECTION_17.1449738_MN = HISTORICAL_SIMPLIFIED_MODEL_ONLY
R02_NEWTON = PROHIBITED
EXCEL_SOLVER_AS_FORMAL_ROOT_METHOD = PROHIBITED
LOAD_STEPPING = PROHIBITED
FORMAL_SPATIAL_QUADRATURE = 0
COMPARATOR_IN_ROOT_SELECTION = 0
PHYSICAL_SAME_Q_TERMINAL = NOT_FROZEN
```

**END OF REPAIRED CENTRAL TECHNICAL LEDGER R01**