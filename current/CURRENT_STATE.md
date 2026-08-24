# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-25 01:30 +08:00  
**Status:** `MARGUERRE_AIRY_EXPLICIT_UNCHANGED / GLOBAL_ULTIMATE_STATE_UNCHANGED / SSNC_R01_EFFECTIVE_AREA_REJECTED / SSNC_R02_PBL_2D_FULL_RESULTANT_GATE_PASS / FULL_STEEL_AREA / FULL_SKIN_Ds / BIAXIAL_NORMAL_POSTBUCKLING / FINITE_AIRY_HARMONICS / YUN_UNIAXIAL_DEGENERATION_PASS / SHEAR_POSTBUCKLING_OPEN / Pu_NOT_CALCULATED_IN_R02 / NEXT_CONNECT_TO_NC_FIXED_TERMINAL`

> Current work is no longer governed by the historical R20 numbering. The user explicitly fixed the architecture: the steel-shell model is only a replaceable explicit submodule; it may not change the existing Marguerre–Airy structural path or the already-selected global ultimate-state criterion. The SSNC-R01 effective-width/effective-strength production interpretation is rejected because it removes physical steel-shell bending contribution. SSNC-R02 instead retains the full steel area and full steel-skin bending matrix and builds a finite two-direction PBL postbuckling operator.

## 0. Hard architecture

```text
GLOBAL_STRUCTURAL_FRONT = FULL_2D_MARGUERRE_AIRY / UNCHANGED
AIRY_FUNCTION = RETAINED
GLOBAL_ULTIMATE_STATE_CRITERION = UNCHANGED
STEEL_SHELL = SUBMODULE_ONLY
D15 = NO
GLOBAL_MATERIAL_VIRTUAL_WORK_RJ = NO
FORMAL_SPATIAL_QUADRATURE = 0
MATERIAL_POINTS = 0
LOAD_PATH_TRACKING = 0
HISTORY_STATE_MACHINE = OFF_MAINLINE
EXPERIMENT_IN_ROOT_SELECTION = 0
FEM_IN_ROOT_SELECTION = 0
EFFECTIVE_WIDTH_OR_AREA_AS_PRODUCTION = PROHIBITED
FORMAL_Z_COMPARATORS = ZHOU_SIMING + WINTER ONLY
```

The existing global Marguerre–Airy demand, generalized coordinates and ultimate-state equations remain authoritative. R02 calculates no `Pu`.

## 1. SSNC-R01 supersession

Historical R01 artifacts remain in the repository for audit only:

- `semantic_v2/40_execution/steel_shell/20260825_0030__NZSCCM__SSNC_R01_YUN_HOMOGENIZED_NC_EXACT_AIRY_TERMINAL.py`
- `semantic_v2/40_execution/20260825_0030__NZSCCM__SSNC_R01_YUN_HOMOGENIZED_NC_EXACT_AIRY_TERMINAL.md`

Current identity:

```text
SSNC_R01_YUN_EFFECTIVE_AREA_PRODUCTION = REJECTED
SSNC_R01_Pu = DO_NOT_PROMOTE
SSNC_R01_INTERNAL_COMPARATORS = NOT_FORMAL_Z_COMPARATORS
```

Retain only reusable Airy/NC exact-section implementation pieces; replace the reduced steel-shell terminal.

## 2. SSNC-R02 source and executable

Report:

`semantic_v2/40_execution/steel_shell/20260825_0130__NZSCCM__SSNC_R02_PBL_2D_FULL_RESULTANT_GATE.md`

Executable:

`semantic_v2/40_execution/steel_shell/20260825_0130__NZSCCM__SSNC_R02_PBL_2D_FULL_RESULTANT_GATE.py`

The production candidate uses the PBL local mode

\[
\phi=(1-\cos k_xx)(1-\cos k_yy),
\]

with stress-free initial coefficient `A0` and current total coefficient `U`.

The exact compatibility source is a finite seven-harmonic field, so local Airy redistribution is closed without spatial quadrature.

## 3. Full-area biaxial-normal steel operator

For

\[
\Delta=U^2-A_0^2,
\]

exact mean geometric shortenings are

\[
g_x=\frac38k_x^2\Delta,
\qquad
g_y=\frac38k_y^2\Delta.
\]

Mean compression-positive steel stresses are

\[
\bar\sigma_x=\frac{E}{1-\nu^2}[(e_x-g_x)+\nu(e_y-g_y)],
\]

\[
\bar\sigma_y=\frac{E}{1-\nu^2}[(e_y-g_y)+\nu(e_x-g_x)].
\]

The full physical steel membrane resultants are

\[
\boxed{N_x=t_s\bar\sigma_x,\quad N_y=t_s\bar\sigma_y,\quad N_{xy}=t_sG\gamma_{xy}}.
\]

No effective width or area multiplier is used.

The current local amplitude is the finite algebraic solution of

\[
\boxed{B_3U^3+B_1U+B_0=0},
\]

solved by Cardano/trigonometric real-root formulas. No incremental local loading is required.

## 4. Full steel-shell bending retained

The skin own bending matrix is unchanged:

\[
\boxed{
\mathbf D_s=
\begin{bmatrix}
D_s&\nu D_s&0\\
\nu D_s&D_s&0\\
0&0&(1-\nu)D_s/2
\end{bmatrix},
\qquad
D_s=\frac{Et_s^3}{12(1-\nu^2)}.
}
\]

For the existing gross/global curvature input,

\[
\mathbf m_s^g=\mathbf D_s\boldsymbol\kappa^g.
\]

Local high-frequency PBL curvature is retained in pointwise surface stress and Mises. Its exact cell average is zero:

\[
\langle\phi_{,xx}\rangle=
\langle\phi_{,yy}\rangle=
\langle\phi_{,xy}\rangle=0,
\]

so it does not generate an artificial extra mean gross moment and does not reduce `Ds`.

For two faces:

\[
\mathbf N_s=\mathbf N_s^++\mathbf N_s^-,
\]

\[
\boxed{
\mathbf M_s=z_+\mathbf N_s^+ + z_-\mathbf N_s^- + \mathbf m_s^{g,+}+\mathbf m_s^{g,-}.
}
\]

## 5. Exact Yun uniaxial degeneration

The derived Airy membrane-energy polynomial exactly reproduces the historical Yun `kp` numerator. For arbitrary local aspect ratio `r=Ly/Lx`, the R02 coefficients satisfy

\[
\frac{K_b}{2t_sc_yC_\sigma}=k_{cr}^{Yun},
\]

and

\[
\frac{2EK_A}{c_y}=C_\sigma H^{Yun}.
\]

Executed errors over `r={0.5,0.75,1,1.5,2}`:

```text
yun_kcr_abs = 3.552713678801e-15
yun_nonlinear_abs = 8.526512829121e-14
```

Thus the biaxial-normal operator recovers the Yun PBL uniaxial source while adding the transverse work and finite two-direction Airy redistribution.

## 6. R02 executed gates

```text
SSNC_R02_PBL_2D_FULL_RESULTANT_GATE = PASS
X_Y_SYMMETRY = PASS
ZERO_LOAD_U_EQUALS_A0 = PASS
SMALL_DEFLECTION_FULL_A_MATRIX = PASS
FULL_SKIN_Ds = PASS
YUN_UNIAXIAL_Kcr = PASS
YUN_UNIAXIAL_Kp = PASS
FINITE_AIRY_HARMONICS = PASS
POINTWISE_2D_MISES = PASS
MEAN_LOCAL_HIGH_FREQUENCY_BENDING = EXACT_ZERO
TOP_BOTTOM_FULL_RESULTANT_ASSEMBLY = PASS
Pu_CALCULATED_IN_R02 = NO
```

Observed machine errors are all zero to machine precision except the two Yun coefficient comparisons above, which are `O(1e-14)`.

## 7. Explicit open boundary

```text
BIAXIAL_NORMAL_POSTBUCKLING = SOURCE-CLOSED CANDIDATE
MEAN_SHEAR_STRESS = ACTIVE
SHEAR_IN_2D_MISES = ACTIVE
SHEAR_POSTBUCKLING = NOT_SOURCE_CLOSED
UNIVERSAL_ARBITRARY_SHEAR_6COMP_PLATE_OPERATOR = NOT_CLAIMED
POST_FIRST_YIELD_2D_PLASTIC_REDISTRIBUTION = NOT_YET_FROZEN
```

The current Z axial family has `Nxy=0` in the existing symmetric Marguerre–Airy demand, so the shear-buckling gap does not by itself block the Z-specific next interface. If the fixed global ultimate-state equations require continuation beyond first local steel yield, that continuation must be source-closed **inside the steel submodule only**; it may not alter the global structure or ultimate criterion.

## 8. Exact next task

```text
NEXT = CONNECT SSNC_R02 FULL-RESULTANT STEEL SHELL
       + EXISTING ORDINARY-CONCRETE EXACT SECTION
       + EXISTING MARGUERRE-AIRY STRUCTURAL DEMAND
       + EXISTING FIXED ULTIMATE-STATE EQUATIONS

FIRST_GATE = DETERMINE WHETHER THE FIXED TERMINAL ROOTS REQUIRE
             POST-FIRST-YIELD 2D STEEL CONTINUATION

IF NO  -> SOLVE Z0-Z6 DIRECTLY
IF YES -> SOURCE-CLOSE STEEL-ONLY POST-YIELD SUBGATE, THEN SOLVE

FORMAL RESULT TABLE AFTER SOLVE = CURRENT THEORY vs ZHOU vs WINTER ONLY
```
