# NZ-SCCM — SSNC-R02 PBL steel-shell 2D full-resultant gate

**Time:** 2026-08-25 01:30 +08:00  
**Status:** `EXECUTED / Biaxial-normal PBL postbuckling full-resultant gate PASS / SHEAR_POSTBUCKLING_OPEN / Pu NOT CALCULATED`

## 0. Governance boundary

This node modifies **only the steel-shell submodule**.

```text
GLOBAL_STRUCTURAL_FRONT = EXISTING_MARGUERRE_AIRY / UNCHANGED
GLOBAL_ULTIMATE_STATE_CRITERION = UNCHANGED
D15 = NOT_USED
GLOBAL_MATERIAL_VIRTUAL_WORK_RJ = NOT_USED
FORMAL_SPATIAL_QUADRATURE = 0
MATERIAL_POINTS = 0
EFFECTIVE_WIDTH_OR_AREA_AS_PRODUCTION = PROHIBITED
Pu_CALCULATED_IN_R02 = NO
```

The rejected SSNC-R01 effective-width/effective-strength terminal is not promoted. R02 keeps the **full steel area** and the **full steel-skin bending matrix**.

Formal Z-family comparators remain **Zhou Siming** and **Winter only**, and are not opened in this R02 steel-module gate because R02 does not calculate Pu.

---

## 1. Literature roles recovered

### 1.1 Ishibashi–Ikemoto–Tatsumi–Fujikubo 2021/2024

Source: *Simplified Ultimate Strength Evaluation Method of Rectangular Plates under Combined Loads*, JASNAOE 33 (2021), DOI `10.2534/jjasnaoe.33.159`; later Marine Structures version 95 (2024) 103592.

Retained source ideas:

- elastic large-deflection plate theory;
- finite assumed buckling mode + Airy stress function;
- biaxial normal stresses enter the same postbuckling amplitude relation;
- the resulting amplitude equation is cubic and can be solved by Cardano without incremental convergence;
- local two-dimensional Mises stress is an admissible physical steel-yield diagnostic.

Classification:

```text
ISHIBASHI_FINITE_MODE_ELDA = ANALYTICAL LARGE-DEFLECTION APPROXIMATION
ISHIBASHI_AIRY_STRESS_REDISTRIBUTION = ANALYTICAL / SOURCE-BACKED
ISHIBASHI_CARDANO = EXACT ALGEBRAIC SOLUTION OF THE ASSUMED-MODE CUBIC
ISHIBASHI_LOCAL_MISES = PHYSICAL YIELD DIAGNOSTIC
ISHIBASHI_FE_INFORMED_COLLAPSE_LOCATION_OR_MIXING_RULE = NOT IMPORTED
```

The simply-supported Ishibashi sine mode is **not** transplanted onto the PBL subpanel because the current PBL boundary/mode is different.

### 1.2 Ueda–Rashed–Paik 1984

Source: *Buckling and Ultimate Strength Interactions of Plates and Stiffened Plates under Combined Loads (1st Report): In-plane Biaxial and Shearing Forces*, DOI `10.2534/jjasnaoe1968.1984.156_355`.

The paper gives explicit buckling/ultimate/fully-plastic interaction relations for biaxial normal force plus shear. Role in R02:

```text
UEDA_1984 = EXPLICIT ULTIMATE/INTERACTION APPROXIMATION
ROLE = INDEPENDENT 2D COMBINED-LOAD CHECK
NOT_USED_AS_CURRENT_STRAIN_TO_RESULTANT_OPERATOR
```

### 1.3 Ueda–Rashed–Paik 1985

Source: *Elastic Buckling Interaction Equation of Simply Supported Rectangular Plates Subjected to Five Load Components*, DOI `10.2534/jjasnaoe1968.1985.425`.

It treats two compressions, two in-plane bending distributions and shear by an explicit practical interaction relation.

```text
UEDA_1985 = ANALYTICAL/PRACTICAL ELASTIC-BUCKLING INTERACTION APPROXIMATION
ROLE = ELASTIC-FRONT / MODE / MULTICOMPONENT CHECK
NOT_USED_AS CURRENT POSTBUCKLING CONSTITUTIVE LAW
```

### 1.4 Ueda–Rashed–Paik 1986

Source: *Effective Width of Rectangular Plates Subjected to Combined Loads*, DOI `10.2534/jjasnaoe1968.1986.258`.

The source gives analytical effective-width relations including biaxial compression and shear, with initial deflection/residual-stress effects.

Per current project governance:

```text
UEDA_1986_EFFECTIVE_WIDTH = SOURCE-VALID ANALYTICAL RESULTANT REDUCTION
PRODUCTION_USE = REJECTED
ROLE = TREND / INDEPENDENT VALIDATION ONLY
```

No effective-width ratio multiplies steel area, membrane resultant, or bending rigidity in R02.

### 1.5 Yun PBL source retained only for actual local PBL boundary/mode

Historical project source:

`semantic_v2/40_execution/steel_shell/20260818_1421__NZSCCM__Z1_Z4__UNIFIED_YUN_IDEAL_EP_LOCAL_AMPLITUDE_FULL_RECALC.md`

Use the local PBL mode

\[
\boxed{\phi=(1-\cos k_xx)(1-\cos k_yy)}
\]

with initial coefficient `A0` and total current coefficient `U=A0+A`.

Yun effective width is **not** used. The role of Yun here is the actual PBL-supported local mode and the independent uniaxial `kcr/kp` coefficient identity.

---

## 2. Exact finite compatibility expansion for the PBL mode

Let

\[
X=k_xx,\qquad Y=k_yy,
\]

\[
\phi=(1-\cos X)(1-\cos Y),
\qquad
\Delta=U^2-A_0^2.
\]

The von Karman compatibility source for the increment relative to the stress-free initial imperfection is

\[
\nabla^4F
=E\Delta\left(\phi_{xy}^2-\phi_{xx}\phi_{yy}\right).
\]

Direct symbolic expansion gives the **finite seven-harmonic identity**

\[
\boxed{
\begin{aligned}
\phi_{xy}^2-\phi_{xx}\phi_{yy}
=k_x^2k_y^2[&\tfrac12\cos Y-\tfrac12\cos2Y
+\tfrac12\cos X-\cos X\cos Y\\
&+\tfrac12\cos X\cos2Y
-\tfrac12\cos2X
+\tfrac12\cos2X\cos Y].
\end{aligned}}
\]

Therefore the local Airy field is obtained harmonic-by-harmonic without spatial quadrature:

\[
\boxed{
F_{mn}=
\frac{E\Delta\,S_{mn}}
{[(mk_x)^2+(nk_y)^2]^2}
\cos(mX)\cos(nY),
}
\]

for

\[
(m,n)\in\{(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1)\}.
\]

Then

\[
\tilde\sigma_x=F_{,yy},\qquad
\tilde\sigma_y=F_{,xx},\qquad
\tilde\tau_{xy}=-F_{,xy}
\]

are finite explicit trigonometric fields.

This is the missing two-direction local postbuckling redistribution; it is not an effective-area surrogate.

---

## 3. Mean geometric shortening and full-area membrane resultants

Exact cell averages are

\[
\langle\phi_x^2\rangle=\frac34k_x^2,
\qquad
\langle\phi_y^2\rangle=\frac34k_y^2,
\qquad
\langle\phi_x\phi_y\rangle=0.
\]

Hence

\[
\boxed{g_x=\frac38k_x^2\Delta},
\qquad
\boxed{g_y=\frac38k_y^2\Delta},
\qquad g_{xy}=0.
\]

For compression-positive imposed mean normal strains `(ex,ey)`:

\[
\boxed{
\bar\sigma_x
=Q[(e_x-g_x)+\nu(e_y-g_y)],
}
\]

\[
\boxed{
\bar\sigma_y
=Q[(e_y-g_y)+\nu(e_x-g_x)],
}
\]

with

\[
Q=\frac{E}{1-\nu^2}.
\]

For the current normal-buckling mode the mean geometric shear is zero; the retained mean elastic shear channel is

\[
\bar\tau_{xy}=G\gamma_{xy}.
\]

The steel membrane resultants use the **whole physical steel thickness**:

\[
\boxed{
N_x^s=t_s\bar\sigma_x,
\quad
N_y^s=t_s\bar\sigma_y,
\quad
N_{xy}^s=t_s\bar\tau_{xy}.
}
\]

There is no `be/b`, no `Aeff/A`, and no reduced `fy`.

---

## 4. Exact finite Airy membrane-energy coefficient and Yun identity

The orthogonal seven-harmonic Airy field gives the exact fluctuation membrane energy per unit cell area

\[
U_A=t_sE K_A\Delta^2,
\]

where, with

\[
r=\frac{k_x}{k_y}=\frac{L_y}{L_x},
\]

\[
\boxed{
K_A
=k_y^4\frac{P(r)}
{256(r^2+1)^2(r^2+4)^2(4r^2+1)^2},
}
\]

and

\[
\boxed{
\begin{aligned}
P(r)={}&272r^{16}+2856r^{14}+11273r^{12}+23146r^{10}+31506r^8\\
&+23146r^6+11273r^4+2856r^2+272.
\end{aligned}}
\]

This polynomial is exactly the numerator appearing in the historical Yun `kp` source coefficient.

The local incremental bending energy is

\[
U_B=\frac12K_b(U-A_0)^2,
\]

\[
\boxed{
K_b=D_s\left[\frac34(k_x^4+k_y^4)+\frac12k_x^2k_y^2\right],
}
\]

\[
D_s=\frac{Et_s^3}{12(1-\nu^2)}.
\]

This retains the full physical skin bending rigidity.

For the uniaxial-y degeneration with `bar sigma_x=0`, define

\[
C_\sigma=\frac{\pi^2Et_s^2}{12(1-\nu^2)L_x^2}.
\]

The R02 energy coefficients reduce exactly to

\[
\boxed{
\frac{K_b}{2t_sc_yC_\sigma}
=\frac{4(3r^4+2r^2+3)}{3r^2}=k_{cr}^{Yun},
}
\]

and

\[
\boxed{
\frac{2EK_A}{c_y}=C_\sigma H^{Yun},
}
\]

where

\[
H^{Yun}=k_p\frac{1-\nu^2}{t_s^2}.
\]

So the new biaxial-normal PBL derivation does **not merely resemble Yun**: it algebraically reproduces both of Yun's uniaxial PBL coefficients while adding the missing x-direction mean work and explicit finite Airy redistribution.

Numerical gate over `r={0.5,0.75,1,1.5,2}`:

```text
yun_kcr_abs = 3.552713678801e-15
yun_nonlinear_abs = 8.526512829121e-14
```

---

## 5. Strain-driven amplitude remains an explicit cubic

Let

\[
c_x=\frac38k_x^2,\qquad c_y=\frac38k_y^2.
\]

The condensed stationary equation at prescribed mean `(ex,ey)` is

\[
\boxed{
K_b(U-A_0)
+4t_sEK_AU(U^2-A_0^2)
-2t_sU(c_x\bar\sigma_x+c_y\bar\sigma_y)=0.
}
\]

Because `bar sigma_x,bar sigma_y` are affine in `U^2-A0^2`, this is exactly

\[
\boxed{B_3U^3+B_1U+B_0=0},
\]

with no quadratic term. Define

\[
L_0=Q[c_x(e_x+\nu e_y)+c_y(e_y+\nu e_x)],
\]

\[
C_g=Q(c_x^2+c_y^2+2\nu c_xc_y).
\]

Then

\[
\boxed{B_3=4t_sEK_A+2t_sC_g},
\]

\[
\boxed{B_1=K_b-2t_sL_0-B_3A_0^2},
\]

\[
\boxed{B_0=-K_bA_0}.
\]

R02 uses the exact Cardano/trigonometric real-root formulas and chooses the nonnegative finite root minimizing the same condensed elastic energy. No load stepping or history state variable is needed for this local algebraic coordinate.

At zero load:

\[
\boxed{U=A_0}
\]

is recovered exactly.

---

## 6. Full steel-skin bending resultants are retained

The steel-skin own bending matrix remains

\[
\boxed{
\mathbf D_s=
\begin{bmatrix}
D_s&\nu D_s&0\\
\nu D_s&D_s&0\\
0&0&(1-\nu)D_s/2
\end{bmatrix}.
}
\]

For the **existing global curvature input**

\[
\boldsymbol\kappa^g=(\kappa_x,\kappa_y,\kappa_{xy})^T,
\]

the skin returns

\[
\boxed{\mathbf m_s^g=\mathbf D_s\boldsymbol\kappa^g}.
\]

No postbuckling scalar multiplies `Ds`.

The local high-frequency curvature increment is retained separately:

\[
\boldsymbol\kappa^{loc}
=-(U-A_0)(\phi_{,xx},\phi_{,yy},2\phi_{,xy})^T.
\]

Exact cell averages satisfy

\[
\boxed{
\langle\phi_{,xx}\rangle
=\langle\phi_{,yy}\rangle
=\langle\phi_{,xy}\rangle=0,
}
\]

hence

\[
\boxed{\langle\mathbf m_s^{loc}\rangle=0}.
\]

This result is important:

- local buckling bending is **not deleted**; it enters pointwise surface stress/Mises;
- it does not create a spurious additional cell-average gross bending resultant;
- the full ordinary skin bending rigidity `Ds` remains in the gross structural moment channel.

Thus there is no double counting between gross Airy curvature and local PBL curvature.

---

## 7. Pointwise 2D steel stress and Mises diagnostic

At any local `(x,y)` the exact finite Airy field gives the postbuckling membrane fluctuation. It is superposed on the mean membrane stress and the local plate-bending surface stress.

The pointwise diagnostic is

\[
\boxed{
\sigma_{vm}
=\sqrt{\sigma_x^2-\sigma_x\sigma_y+\sigma_y^2+3\tau_{xy}^2}.
}
\]

This preserves longitudinal, transverse and shear stress in the local yield check.

R02 deliberately does **not** import an Ishibashi FE-informed collapse mixing rule, and it does not use local Mises reaching `fy` to replace the already-fixed global NZ-SCCM ultimate-state criterion.

---

## 8. Top/bottom full-resultant assembly

For each external steel face, R02 returns

\[
\boxed{
\mathcal S_{face}^{2D}:
(e_x,e_y,\gamma_{xy},\boldsymbol\kappa^g)
\mapsto
(U,N_x,N_y,N_{xy},m_x,m_y,m_{xy}).
}
\]

For top/bottom faces at `z+`,`z-`:

\[
\boxed{\mathbf N_s=\mathbf N_s^++\mathbf N_s^-},
\]

\[
\boxed{
\mathbf M_s
=z_+\mathbf N_s^+
+z_-\mathbf N_s^-
+\mathbf m_s^{g,+}
+\mathbf m_s^{g,-}.
}
\]

This explicitly contains both:

1. the lever-arm moment generated by the **full physical membrane resultants**;
2. the **full own-skin bending stiffness** of both steel faces.

Therefore the user-identified bending-stiffness loss of an effective-area model is removed.

---

## 9. Gate execution

Executable:

`semantic_v2/40_execution/steel_shell/20260825_0130__NZSCCM__SSNC_R02_PBL_2D_FULL_RESULTANT_GATE.py`

Observed output:

```text
SSNC_R02_PBL_2D_FULL_RESULTANT_GATE = PASS
full_Ds=0.000000000000e+00
mean_local_kappa_exact=0.000000000000e+00
small_A_matrix=0.000000000000e+00
small_U=0.000000000000e+00
two_face_M=0.000000000000e+00
two_face_N=0.000000000000e+00
xy_U=0.000000000000e+00
xy_local_normal=0.000000000000e+00
xy_mean_normal=0.000000000000e+00
yun_kcr_abs=3.552713678801e-15
yun_nonlinear_abs=8.526512829121e-14
zero_load_U_minus_A0=0.000000000000e+00
mises_demo_MPa=110.105324543556
EFFECTIVE_WIDTH_PRODUCTION = False
FULL_SKIN_D_RETAINED = True
SHEAR_POSTBUCKLING_CLOSED = False
GLOBAL_AIRY_CHANGED = False
ULTIMATE_STATE_CHANGED = False
Pu_CALCULATED_IN_R02 = False
```

Passed gates:

```text
X_Y_SYMMETRY = PASS
ZERO_LOAD_INITIAL_GEOMETRY = PASS
SMALL_DEFLECTION_FULL_A_MATRIX = PASS
SMALL_DEFLECTION_FULL_Ds = PASS
YUN_UNIAXIAL_Kcr_DEGENERATION = PASS
YUN_UNIAXIAL_Kp_DEGENERATION = PASS
FINITE_AIRY_HARMONICS = PASS
POINTWISE_2D_MISES_EVALUATOR = PASS
LOCAL_HIGH_FREQUENCY_MEAN_BENDING = EXACT_ZERO
TOP_BOTTOM_FULL_RESULTANT_ASSEMBLY = PASS
```

---

## 10. Exact scope boundary after R02

R02 closes the steel module required by the **current Z axial domain** in the following sense:

```text
PBL_BIAXIAL_NORMAL_POSTBUCKLING = PASS_CANDIDATE
FULL_STEEL_AREA = RETAINED
FULL_SKIN_BENDING_RIGIDITY = RETAINED
Nx_Ny_COUPLED = ACTIVE
LOCAL_AIRY_REDISRIBUTION_X_Y_XY = ACTIVE
SHEAR_MEMBRANE_STRESS = ACTIVE
SHEAR_IN_MISES = ACTIVE
SHEAR_POSTBUCKLING = NOT_SOURCE_CLOSED
GENERAL_ARBITRARY_SHEAR_BUCKLING_6COMP_OPERATOR = NOT_CLAIMED
```

The shear gap does **not** change the global theory and does not block the current Z axial family, whose existing Marguerre-Airy demand has `Nxy=0` in the present symmetric single-mode domain. It **does** block claiming that R02 is already a universal plate operator for arbitrary externally applied shear-dominated loading.

Also, R02 is an elastic-large-deflection/current-yield-diagnostic steel module. A post-first-yield two-dimensional plastic redistribution law has not been invented here. If the fixed global ultimate-state evaluation needs continuation beyond local first yield, that extension must be source-closed as a steel-only subgate; it still may not alter the global Airy structure or the global ultimate-state criterion.

---

## 11. Decision

```text
SSNC_R01_EFFECTIVE_AREA_PRODUCTION = SUPERSEDED / REJECTED
SSNC_R02_PBL_2D_FULL_RESULTANT_GATE = PASS
STEEL_SHELL_MODULE_ARCHITECTURE = FULL_AREA + FULL_Ds + BIAXIAL_NORMAL_POSTBUCKLING
GLOBAL_MARGUERRE_AIRY = UNCHANGED
GLOBAL_ULTIMATE_STATE = UNCHANGED
Pu_IN_R02 = NONE
FORMAL_Z_COMPARATORS = ZHOU + WINTER ONLY / NOT OPENED IN R02
```

**Next task:** connect this R02 steel-shell operator to the already-existing ordinary-concrete + fixed Airy + fixed ultimate-state equations, first auditing whether the fixed terminal state requires steel response beyond local first yield. Only after that interface is source-closed should Z0–Z6 Pu be calculated; the resulting table must compare only with Zhou and Winter.
