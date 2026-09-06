# NZ-SCCM — UHPC-GS2/MNφ + steel R02/R06 direct-state gate R01

**Date:** 2026-09-06  
**Branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Status:** `DIAGNOSTIC / ARCHITECTURE LOCK / NO PRODUCTION THEORY MODIFICATION / NO FEM CALIBRATION`

---

## 0. Purpose

This execution performs two tasks only:

1. condense the UHPC side into a low-dimensional **2D current-section operator** suitable for the Aghayere–MacGregor `M-N-phi` equilibrium layer without returning to a full Nguyen ordinary-concrete state machine;
2. recover the exact frozen R02/R06 steel-shell operator and redefine the **true FEM-state forward gate**, then execute every part that is possible from the currently archived FEM observables.

No FEM/test value is used to fit a coefficient or modify a theory root.

---

# 1. R02/R06 source recovery — previous “D_s / K_A unavailable” blocker is superseded

The frozen common R06 source is:

`20260825_1535__NZSCCM__STEEL_SHELL_COMMON_R06_LOCAL_YIELD_RESULTANT_GATE.py`.

For one PBL cell:

\[
k_x=2\pi/L_x,\qquad k_y=2\pi/L_y,
\]

\[
Q_s=\frac{E_s}{1-\nu_s^2},\qquad
D_s=\frac{E_st_s^3}{12(1-\nu_s^2)},
\]

\[
c_x=\frac{3k_x^2}{8},\qquad c_y=\frac{3k_y^2}{8},
\]

\[
K_b=D_s\left[\frac34(k_x^4+k_y^4)+\frac12k_x^2k_y^2\right].
\]

Let `r=kx/ky`. Then

\[
K_A=\frac{k_y^4 P(r)}{256(r^2+1)^2(r^2+4)^2(4r^2+1)^2},
\]

\[
P(r)=272r^{16}+2856r^{14}+11273r^{12}+23146r^{10}+31506r^8
+23146r^6+11273r^4+2856r^2+272.
\]

With R02 internal **compression-positive** membrane strains `(e_x,e_y)`:

\[
L_0=Q_s\{c_x(e_x+\nu_se_y)+c_y(e_y+\nu_se_x)\},
\]

\[
C_g=Q_s(c_x^2+c_y^2+2\nu_sc_xc_y),
\]

\[
B_3=4t_sE_sK_A+2t_sC_g,
\]

\[
B_1=K_b-2t_sL_0-B_3A_0^2,
\qquad
B_0=-K_bA_0.
\]

The stationary amplitude is an admissible nonnegative real root of

\[
\boxed{B_3U^3+B_1U+B_0=0}
\]

selected by minimum total cell energy, not by FEM information.

Let

\[
d=U^2-A_0^2,
\qquad
m_x=e_x-c_xd,
\qquad
m_y=e_y-c_yd.
\]

The physical tension-positive mean stresses are

\[
\boxed{\bar\sigma_x=-Q_s(m_x+\nu_sm_y)},
\qquad
\boxed{\bar\sigma_y=-Q_s(m_y+\nu_sm_x)}.
\]

R06 does **not** cap the mean stress directly at `fy`. It evaluates the finite harmonic local Mises polynomial over the complete cell and, when necessary, radially projects the complete face-strain ray to the first local-Mises-yield state.

Therefore `D_s`, `K_A`, `B3/B1/B0`, the amplitude energy rule and the mean-stress return are now source-recovered. The former source-availability blocker is closed.

---

# 2. Corrected identity of the steel-only direct-state gate

The standard R02/R06 operator already predicts `U` internally from the two face membrane strains. Therefore the minimum true forward gate is **not**

\[
(\varepsilon_x,\varepsilon_y,q_g,A_\ell^{FE})\to R02/R06,
\]

but

\[
\boxed{
(\varepsilon_{x,s}^{FE},\varepsilon_{y,s}^{FE};L_x,L_y,A_0,E_s,\nu_s,f_y)
\to R02\to U^{pred}\to R06\to(\bar\sigma_x^{pred},\bar\sigma_y^{pred}).
}
\]

The FEM local-wave amplitude is a **validation observable** for `U`, not an input to the standard operator.

A second optional diagnostic may condition the stress reconstruction on `U_FE`; that would isolate the amplitude equation from the stress-return equation, but it is not the production R02/R06 path.

Hence the exact ODB contract needed for every face/cell is:

- area-weighted shell `LE11`, `LE22` in the frozen local shell axes;
- area-weighted `S11`, `S22` on the same region;
- cell/face registration and class (`n` or geometry from which `n` is determined);
- Coons/local-wave displacement observable retained separately for `U` validation.

Global `q_FE` is not an R02 input once actual shell membrane strains are supplied.

---

# 3. Existing archive limitation

The current BH032/BH050 post-LY archive contains actual shell longitudinal `LE22` and longitudinal mean stress `S22`, but it did not archive the matching transverse shell `LE11` at the same face/cell contract.

Therefore a mathematically complete 2D FEM-state R02/R06 gate cannot yet be claimed for all nine specimens.

However a stronger conditional gate than the previous tangent-only audit can be executed now:

> Hold the frozen theory transverse face strain `eps_x` fixed, replace **only the longitudinal face strain** by the actual FEM peak `LE22`, and re-evaluate the unchanged frozen R02/R06 operator.

This does not calibrate anything. It asks whether correcting the known upstream longitudinal strain-path error is sufficient to recover the measured mean longitudinal steel stress.

---

# 4. Conditional direct-state execution — BH032/BH050, n=4 regular cell

Cell geometry uses the frozen Multiwave same-side PBL rule `s=0.225b`, `n0=4`:

- BH032: `Lx=360 mm`, `Ly=400 mm`, `A0=0.225 mm`;
- BH050: `Lx=562.5 mm`, `Ly=625 mm`, `A0=0.3515625 mm`.

The transverse reference strains are the frozen force-first face states. The longitudinal strains and comparator stresses are read-only FEM peak observables.

| case/face | frozen `eps_x` | FEM peak `eps_y=LE22` | R02/R06 `sigma_y` MPa | FEM `S22` MPa | compression-magnitude error | `U_pred` mm | `eta_R06` |
|---|---:|---:|---:|---:|---:|---:|---:|
| BH032 upper | +6.36993e-4 | -2.50958e-3 | **-290.62** | -292.61 | **-0.68%** | 1.1026 | 0.6174 |
| BH050 upper | +1.04084e-3 | -1.43804e-3 | **-248.44** | -254.45 | **-2.36%** | 0.8056 | 0.9991 |
| BH032 lower | -3.15782e-4 | -2.66991e-3 | **-277.77** | -198.10 | **+40.22%** | 1.5870 | 0.5570 |
| BH050 lower | -9.84430e-4 | -1.72567e-3 | **-212.16** | -231.59 | **-8.39%** | 3.3366 | 0.7467 |

The sign of the error is based on compression magnitude.

## 4.1 Upper-face decision

For both BH032 and BH050, simply replacing the wrong theory longitudinal face strain by the actual FEM longitudinal strain recovers the upper-face mean longitudinal stress to about **0.7% and 2.4%**, even though the transverse strain has not yet been replaced by its FEM value.

This is a stronger result than the previous consistent-tangent audit:

\[
\boxed{\text{BH032/BH050 upper R02/R06 mean-stress operator is not the source of the theory upper-face unloading.}}
\]

The dominant upper-face failure is upstream: the coupled section solution feeds R02/R06 the wrong longitudinal strain path.

## 4.2 Lower-face decision

The same conditional substitution is not uniformly sufficient on the lower face:

- BH050 lower is already within about `8.4%` in mean longitudinal stress;
- BH032 lower remains about `40%` too compressive under the held-theory transverse state.

Therefore the following broader statement is **not** allowed:

`ALL STEEL R02/R06 = VERIFIED`.

BH032 lower remains a genuine unresolved direct-state case. The first missing discriminator is actual FEM `LE11` on the same lower-face region. If the full `(LE11,LE22)` input still yields the wrong `S22`, then R06/local post-yield continuation must be opened. Until then, changing R06 is premature.

---

# 5. Steel decision after this execution

```text
MULTIWAVE_GLOBAL_MODIFICATION = NO
R02_SOURCE_RECOVERY = PASS
R06_SOURCE_RECOVERY = PASS
UPPER_R02_R06_CONDITIONAL_DIRECT_STATE_BH032 = STRONG_PASS (~0.7%)
UPPER_R02_R06_CONDITIONAL_DIRECT_STATE_BH050 = STRONG_PASS (~2.4%)
LOWER_BH050_CONDITIONAL = NEAR_PASS (~8.4%)
LOWER_BH032_CONDITIONAL = FAIL (~40%)
FULL_2D_DIRECT_STATE = BLOCKED_BY_MISSING_FE_LE11
NINE_SPECIMEN_DIRECT_STATE = NOT_YET CLAIMED
```

Thus the steel operator remains **frozen under direct-state audit**, not modified.

---

# 6. UHPC-GS2/MNphi architecture — minimal 2D current-section operator

The previous one-dimensional section contract

\[
(\varepsilon_0,\kappa)\to(N,M,A^t,B^t,D^t)
\]

is retained only as a regression/degeneration case.

The new generalized in-plane section strains are

\[
\mathbf e_0=
[\varepsilon_x^0,\varepsilon_y^0,\gamma_{xy}^0]^T,
\qquad
\boldsymbol\kappa=
[\kappa_x,\kappa_y,\kappa_{xy}]^T.
\]

At thickness coordinate `z`:

\[
\boxed{\boldsymbol\varepsilon(z)=\mathbf e_0+z\boldsymbol\kappa}
\]

where the mid-plane quantities are supplied by the global/Aghayere kinematics, including the current von-Karman membrane terms. UHPC receives no independent local buckling amplitude.

Define the reduced 2D current material kernel

\[
\boxed{\boldsymbol\sigma(z)=\mathcal M_U^{2D}[\boldsymbol\varepsilon(z);\mathcal S_U]}
\]

and its exact current tangent

\[
\boxed{\mathbf C_U^t(z)=\partial\boldsymbol\sigma/\partial\boldsymbol\varepsilon}.
\]

The section resultant is

\[
\boxed{
\mathbf r_U=
\begin{bmatrix}\mathbf N_U\\\mathbf M_U\end{bmatrix}
=
\int_{-t_c/2}^{t_c/2}
\begin{bmatrix}\mathbf I\\z\mathbf I\end{bmatrix}
\boldsymbol\sigma(z)\,dz
}
\]

with

\[
\mathbf N_U=[N_x,N_y,N_{xy}]^T,
\qquad
\mathbf M_U=[M_x,M_y,M_{xy}]^T.
\]

The exact consistent generalized tangent is

\[
\boxed{
\mathbf K_{U,sec}^t=
\int
\begin{bmatrix}\mathbf I\\z\mathbf I\end{bmatrix}
\mathbf C_U^t(z)
\begin{bmatrix}\mathbf I&z\mathbf I\end{bmatrix}dz
=
\begin{bmatrix}
\mathbf A_U^t&\mathbf B_U^t\\
\mathbf B_U^t&\mathbf D_U^t
\end{bmatrix}
}
\]

where `A/B/D` are **3×3 matrices**, not scalar moduli.

This is the formal UHPC-GS2/MNphi interface:

\[
\boxed{
\mathcal U_{GS2}:
(\mathbf e_0,\boldsymbol\kappa)
\mapsto
(\mathbf N_U,\mathbf M_U,\mathbf A_U^t,\mathbf B_U^t,\mathbf D_U^t).
}
\]

---

# 7. What is source-locked inside the 2D kernel, and what is still open

## 7.1 Locked

1. current stress and current tangent are different objects;
2. the existing UHPC uniaxial compression curve including its physical post-peak negative tangent remains the one-dimensional baseline;
3. the existing complete L0 source requires a consistent tangent including principal-direction rotation; a simple diagonal principal tangent rotated back to x-y is not sufficient;
4. a local UHPC fiber reaching the uniaxial peak is an event, not the global `Nu` endpoint;
5. no Nguyen ordinary-concrete dilation, tension-stiffening, shear-retention, crushing constants, unload/reload history machine is imported;
6. no independent `A_U` local-buckling DOF is introduced.

## 7.2 State branches retained in GS2

Use principal ordering `epsilon_1 >= epsilon_2` only to classify the current 2D state:

- `UC`: one-dimensional/uniaxial regression state;
- `TC`: one principal tensile and one principal compressive state;
- `CC`: both principal directions compressive;
- `TT`: both tensile, retained for completeness but not expected to control the current axial peak family.

## 7.3 The only constitutive interaction still open

The nine-specimen forward audit has already shown that

\[
\sigma_y=\sigma_y(\varepsilon_y)\quad\text{alone}
\]

is insufficient. Therefore GS2 leaves exactly one material interaction operator open:

\[
\boxed{\mathcal I_U(\varepsilon_1,\varepsilon_2;\text{current state})}.
\]

It must be source-derived and must return both current stress and derivatives. No fitted specimen-by-specimen reduction factor is permitted.

For `TC`, Liu et al. (Construction and Building Materials 401 (2023) 132966) provide direct UHPC plane biaxial element evidence that principal tensile strain reduces the orthogonal peak compressive stress/strain and propose a softened UHPC compression law. This is a legitimate **candidate source branch**, but its normalization must be reconciled with the project's fixed `fc=141.1 MPa` definition before adoption.

For `CC`, the uploaded Wang Shunan UHPC triaxial tests prove strong pressure sensitivity/confinement enhancement, but a conventional triaxial failure envelope is not by itself a complete plane-stress current stress-strain law. Therefore no CC strengthening coefficient is invented at this stage.

---

# 8. Zero-spatial-quadrature contract retained

GS2 does not authorize formal thickness Gauss points.

The formal implementation is:

1. determine finite material-state event locations through the thickness;
2. partition the thickness only at those analytic event roots;
3. compile each active material branch to exact/finite analytic primitives;
4. evaluate `N/M/A/B/D` by endpoint primitives.

If a sourced 2D interaction branch introduces a non-polynomial analytic function, it must enter the existing material-level analytic compiler/special-function backend; formal spatial Gauss/Simpson/adaptive quadrature remains zero.

---

# 9. U0/U1/U2 state semantics

```text
U0 = current UHPC stable/ascending material state; current stress and tangent returned.
U1 = global UCFT geometric postbuckling q != 0; UHPC uses the same GS2 operator and has no independent local amplitude.
U2 = one or more UHPC fibers enter post-peak/negative tangent; this is a path event, not an automatic global terminal.
GLOBAL ENDPOINT = loss of physically admissible equilibrium path or max N on the valid path.
```

---

# 10. Exact next ODB extraction gate for all nine specimens

At each peak frame, and preferably along a short prepeak/post-event path, archive under one identical station/area contract:

### Steel upper/lower faces

- `LE11`, `LE22`, optional `LE12`/engineering shear under verified shell-local axes;
- `S11`, `S22`, `S12` on exactly the same area;
- area weights and face widths so resultants close;
- local Coons-baseline wave amplitude by PBL bay, retained separately.

### UHPC

- corresponding in-plane total strain components on the section: longitudinal, transverse and in-plane shear;
- corresponding stress components;
- through-thickness linear fit and residual, but do not collapse the raw 2D state before the GS2 classification audit.

### Global

- existing projected `q_FE` and modal fit quality;
- total/component axial resultants for closure only.

This single extraction makes both unresolved gates computable:

\[
\boxed{\text{steel full 2D R02/R06 direct-state gate}}
\]

and

\[
\boxed{\text{UHPC GS2 state-classification / interaction-source gate}}.
\]

---

# 11. Current decision ledger

```text
UHPC_GS2_MNPHI_ARCHITECTURE = LOCK
UHPC_SECTION_ABD = 3x3 BLOCKS
UHPC_INDEPENDENT_LOCAL_AMPLITUDE = NO
UHPC_CURRENT_STRESS_TANGENT_SEPARATION = LOCK
UHPC_PRINCIPAL_DIRECTION_ROTATION_TANGENT = RETAIN
UHPC_FIRST_FIBER_PEAK_AS_NU = REJECTED
UHPC_2D_INTERACTION_FUNCTION = OPEN / SOURCE-ONLY
Liu_2023_TC_SOFTENING = CANDIDATE_SOURCE, NOT YET PARAMETER-LOCKED
Wang_TRIAXIAL_CC = PRESSURE-SENSITIVITY EVIDENCE / NOT A PLANE-STRESS LAW
STEEL_R02_R06_SOURCE_IDENTITY = RECOVERED
STEEL_UPPER_PATH_ERROR_PRIMARY = UPSTREAM KINEMATIC/SECTION PATH, STRONGLY SUPPORTED
STEEL_LOWER_BH032 = STILL OPEN
MULTIWAVE_STEEL_MODIFICATION = FORBIDDEN UNTIL FULL FE (LE11,LE22) DIRECT-STATE FAILS
NINE_SPECIMEN_FULL_DIRECT_STATE = BLOCKED ONLY BY MISSING MATCHED 2D FE STATE ARCHIVE
PRODUCTION_MAIN_MODIFIED = NO
```
