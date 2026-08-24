# NZ-SCCM — SSNC-R03 current 6×6 steel-shell tangent/resultant gate

**Time:** 2026-08-25 07:46 +08:00  
**Status:** `EXECUTED / ELASTIC-POSTBUCKLING CURRENT 6x6 TANGENT PASS / POST-FIRST-YIELD PLASTIC TANGENT NOT FALSELY CLOSED / Pu NOT CALCULATED`

## 0. Why R03 exists

R02 closed the finite biaxial-normal PBL postbuckling **stress/resultant** field, but it still used the gross elastic steel-skin bending matrix when returning the gross moment. That was not sufficient for the global tangent problem.

The key correction is:

> `mean(local high-frequency bending moment)=0` does **not** imply that local buckling leaves the global/current bending tangent unchanged.

The steel base material modulus `E` does not physically decrease merely because an elastic plate buckles. However, after the local amplitude `U` is condensed, the **plate-level current membrane tangent** becomes state-dependent and generally direction-dependent. Because the top and bottom skins sit at finite offsets `z_f`, this reduced membrane tangent enters the gross bending tangent through `z_f^2 A_f^tan`. Therefore the global steel-shell `Dx,Dy,...` change even before first steel yield.

This R03 modifies only the steel-shell submodule.

```text
GLOBAL_STRUCTURAL_FRONT = FULL_2D_MARGUERRE_AIRY / UNCHANGED
GLOBAL_ULTIMATE_STATE_CRITERION = UNCHANGED
FORMAL_SPATIAL_QUADRATURE = 0
MATERIAL_POINTS = 0
EFFECTIVE_WIDTH_OR_AREA_AS_PRODUCTION = PROHIBITED
Pu_CALCULATED_IN_R03 = NO
```

---

## 1. R02 condensed potential retained exactly

For the PBL local mode

\[
\phi=(1-\cos k_xx)(1-\cos k_yy),
\qquad
\Delta=U^2-A_0^2,
\]

R02 gives

\[
c_x=\frac38k_x^2,
\qquad
c_y=\frac38k_y^2,
\]

\[
m_x=e_x-c_x\Delta,
\qquad
m_y=e_y-c_y\Delta,
\]

and the mean compression-positive stresses

\[
\bar\sigma_x=Q(m_x+\nu m_y),
\qquad
\bar\sigma_y=Q(m_y+\nu m_x),
\qquad
\bar\tau_{xy}=G\gamma_{xy},
\]

where

\[
Q=\frac{E}{1-\nu^2},
\qquad
G=\frac{E}{2(1+\nu)}.
\]

The same condensed energy per unit local-cell area is

\[
\boxed{
\Pi(e_x,e_y,\gamma,U)
=
\frac{tQ}{2}(m_x^2+m_y^2+2\nu m_xm_y)
+\frac{tG}{2}\gamma^2
+\frac{K_b}{2}(U-A_0)^2
+tEK_A\Delta^2 .
}
\]

Stationarity

\[
\Pi_{,U}=0
\]

is exactly the existing R02 cubic

\[
\boxed{B_3U^3+B_1U+B_0=0}.
\]

No new local constitutive assumption is introduced in this step.

---

## 2. Exact current membrane tangent after eliminating U

Define the uncondensed elastic membrane matrix

\[
\boxed{
\mathbf A_e
=t
\begin{bmatrix}
Q&\nu Q&0\\
\nu Q&Q&0\\
0&0&G
\end{bmatrix}.
}
\]

The coupling vector between mean strain and the local amplitude is

\[
\boxed{
\mathbf h
=\Pi_{,\varepsilon U}
=-2tQU
\begin{bmatrix}
c_x+\nu c_y\\
c_y+\nu c_x\\
0
\end{bmatrix}.
}
\]

At a selected smooth stable root,

\[
\boxed{
k_U=\Pi_{,UU}=3B_3U^2+B_1>0.
}
\]

Therefore

\[
\frac{\partial U}{\partial\boldsymbol\varepsilon}
=-k_U^{-1}\mathbf h^{\mathsf T},
\]

and the exact condensed plate-level tangent is the scalar-internal-coordinate Schur complement

\[
\boxed{
\mathbf A_{pb}^{tan}
=
\Pi_{,\varepsilon\varepsilon}
-\Pi_{,\varepsilon U}\Pi_{,UU}^{-1}\Pi_{,U\varepsilon}
=
\mathbf A_e-\frac{\mathbf h\mathbf h^{\mathsf T}}{k_U}.
}
\]

Explicitly,

\[
A_{11}^{pb}
=tQ-
\frac{4t^2Q^2U^2}{k_U}(c_x+\nu c_y)^2,
\]

\[
A_{22}^{pb}
=tQ-
\frac{4t^2Q^2U^2}{k_U}(c_y+\nu c_x)^2,
\]

\[
A_{12}^{pb}=A_{21}^{pb}
=t\nu Q-
\frac{4t^2Q^2U^2}{k_U}
(c_x+\nu c_y)(c_y+\nu c_x),
\]

\[
A_{66}^{pb}=tG.
\]

For the present normal-buckling PBL mode, `U` is not driven by uniform mean shear because the exact mean geometric shear is zero. Therefore the shear tangent remains `tG` in this **pre-first-yield normal-postbuckling** subgate. This does not claim that arbitrary shear postbuckling is closed.

### Consequence

If `kx != ky`, then generally

\[
\boxed{A_{11}^{pb}\ne A_{22}^{pb}}.
\]

Thus the directional current stiffness difference requested by the user appears automatically without defining artificial scalar `Ex_eff` and `Ey_eff` first. Those scalars, if desired, are derived outputs of the matrix, not primitive material constants.

---

## 3. Correct interpretation of the steel-skin bending stiffness

Before first steel material yield, the steel **material** remains elastic. Hence the own-skin material bending matrix remains

\[
\boxed{
\mathbf D_{skin,e}
=
\begin{bmatrix}
D&\nu D&0\\
\nu D&D&0\\
0&0&(1-\nu)D/2
\end{bmatrix},
\qquad
D=\frac{Et^3}{12(1-\nu^2)}.
}
\]

This statement applies only to the skin's own `Et^3/12` term before first yield.

It does **not** mean that the entire steel-shell bending tangent remains elastic.

For one steel face at distance `z_f` from the existing global reference surface,

\[
\boldsymbol\varepsilon_f
=\boldsymbol\varepsilon_0+z_f\boldsymbol\kappa.
\]

The current face resultants are

\[
\mathbf N_f=\mathbf N_f(\boldsymbol\varepsilon_f,U_f),
\]

\[
\boxed{
\mathbf M_f
=z_f\mathbf N_f+\mathbf D_{skin,e}\boldsymbol\kappa.
}
\]

Differentiation gives the exact pre-first-yield face tangent

\[
\boxed{
\mathbf K_f^{tan}
=
\begin{bmatrix}
\mathbf A_f^{pb} & z_f\mathbf A_f^{pb}\\
z_f\mathbf A_f^{pb} & z_f^2\mathbf A_f^{pb}+\mathbf D_{skin,e}
\end{bmatrix}.
}
\]

For the top and bottom skins,

\[
\boxed{
\mathbf K_s^{tan}=\sum_{f=+,-}\mathbf K_f^{tan}.
}
\]

Hence

\[
\boxed{
\mathbf A_s=\mathbf A_+^{pb}+\mathbf A_-^{pb},
}
\]

\[
\boxed{
\mathbf B_s=z_+\mathbf A_+^{pb}+z_-\mathbf A_-^{pb},
}
\]

\[
\boxed{
\mathbf D_s^{current}
=z_+^2\mathbf A_+^{pb}+z_-^2\mathbf A_-^{pb}
+\mathbf D_{skin,e}^++\mathbf D_{skin,e}^-.
}
\]

This is the missing mechanism in R02.

Even when

\[
\langle\mathbf m_{local}\rangle=0,
\]

local postbuckling reduces `A_f^pb`, and the dominant lever-arm contribution `z_f^2 A_f^pb` therefore reduces the gross bending tangent. If the two faces are at different current states, `B_s` also generally becomes nonzero even for a geometrically symmetric section.

---

## 4. Exact uniaxial degeneration now includes tangent, not only kcr/kp

R02 already proved that the biaxial PBL coefficients reduce exactly to Yun's uniaxial `kcr` and `kp` coefficients.

For the stress-free transverse condition

\[
\bar\sigma_x=0,
\]

one obtains

\[
\boxed{
e_x=-\nu e_y+(c_x+\nu c_y)\Delta,
}
\]

and

\[
\boxed{
\bar\sigma_y=E(e_y-c_y\Delta).
}
\]

The reduced amplitude equation is

\[
\boxed{
R_y=
K_b(U-A_0)
+4tEK_AU\Delta
-2tEc_yU(e_y-c_y\Delta)=0.
}
\]

Therefore

\[
\frac{dU}{de_y}
=
\frac{2tEc_yU}{R_{y,U}},
\]

and

\[
\boxed{
E_{y,pb}^{tan}
=\frac{d\bar\sigma_y}{de_y}
=E\left(1-2c_yU\frac{dU}{de_y}\right).
}
\]

This is a derivative of the R02/Yun-coefficient-consistent branch. It is **not** attributed to Yun as a published tangent formula.

The executable independently evaluates the same scalar tangent by condensing the biaxial matrix under `dNx=0`:

\[
\boxed{
E_{y,pb}^{tan}
=\frac1t\left(
A_{22}^{pb}-\frac{A_{21}^{pb}A_{12}^{pb}}{A_{11}^{pb}}
\right).
}
\]

The two derivations agree to machine precision.

---

## 5. Executed R03 gates

Executable:

`semantic_v2/40_execution/steel_shell/20260825_0746__NZSCCM__SSNC_R03_CURRENT_6X6_TANGENT_GATE.py`

The gate geometries/states below are mathematical verification states only. They are **not Z0–Z6 predictions**.

Executed values:

```text
SSNC_R03_CURRENT_6X6_TANGENT_GATE = PASS
ELASTIC_POSTBUCKLING_CURRENT_TANGENT = CLOSED
POST_FIRST_YIELD_2D_PLASTIC_TANGENT = OPEN
GLOBAL_AIRY_CHANGED = False
ULTIMATE_STATE_CHANGED = False
EFFECTIVE_WIDTH_PRODUCTION = False
Pu_CALCULATED_IN_R03 = False

small_deflection_A_abs       = 0.000000000000e+00
full_skin_D_preyield_abs     = 0.000000000000e+00
xy_U_abs                     = 0.000000000000e+00
xy_A_abs                     = 0.000000000000e+00
postbuckling_anisotropy_ratio= 3.466188846419e-01
A_tangent_fd_rel             = 9.595929051176e-09
uniaxial_U_abs               = 2.220446049250e-16
uniaxial_tangent_abs_MPa     = 5.820766091347e-11
uniaxial_tangent_ratio_E     = 7.031662269129e-01
uniaxial_mean_stress_MPa     = 2.755713456187e+02
two_face_K_sym_abs           = 0.000000000000e+00
Dx_current_over_elastic      = 7.918419815200e-01
Dy_current_over_elastic      = 5.175593619368e-01
K6_fd_rel                    = 9.595929051176e-09
```

### 5.1 Nonsquare-cell current A matrix

For the executed `Lx=360 mm`, `Ly=240 mm`, `t=4 mm` verification state,

\[
U=0.2005277540\ \mathrm{mm},
\]

and

\[
\boxed{
\mathbf A_{pb}^{tan}
\approx
\begin{bmatrix}
716908.04&-15453.44&0\\
-15453.44&468414.17&0\\
0&0&316923.08
\end{bmatrix}\ \mathrm{N/mm}.
}
\]

The difference between the two normal tangent terms is about `34.66%` relative to the larger one. The negative condensed `A12` in this verification state is a **plate-level postbuckling coupling**, not a negative steel material Poisson ratio.

### 5.2 Uniaxial tangent trend

For the square `360×360×4 mm` verification cell at the selected postbuckling state,

\[
\bar\sigma_y=275.57\ \mathrm{MPa}<f_y=355\ \mathrm{MPa},
\]

and

\[
\boxed{
E_{y,pb}^{tan}/E=0.703166.
}
\]

Thus the new operator recovers the expected postbuckling tangent reduction before material yield, whereas R02 only checked Yun's `kcr/kp` coefficient identities.

### 5.3 Gross bending tangent

For a symmetric two-face verification section with `z_+=+50 mm`, `z_-=-50 mm`, the current/elastic ratios are

\[
\boxed{D_x^{current}/D_x^{elastic}=0.791842},
\]

\[
\boxed{D_y^{current}/D_y^{elastic}=0.517559}.
\]

Again these are gate-state values, not UCFT Z-series results. Their purpose is to prove the mechanism: local buckling can reduce gross bending stiffness strongly and unequally in x/y **even while the steel base material is still elastic**.

---

## 6. Literature audit for the post-first-yield part

The user's second correction is also confirmed: once steel begins to yield, keeping `D_skin=E t^3/[12(1-nu^2)]` is no longer generally valid.

### 6.1 Yun Lu thesis

Yun's analytical large-deflection theory is an elastic postbuckling theory. The thesis itself states in its outlook that steel plastic constitutive behavior was not included and that a plastic analytical model remains necessary. Therefore Yun cannot be used as the source of a post-yield tangent law.

### 6.2 Ishibashi et al. 2021/2024

The method explicitly uses **elastic large-deflection theory + Mises yield criterion** to evaluate ultimate strength/collapse without curve fitting. This is valid support for the current finite-mode/Airy/first-yield architecture, but it does not provide a post-first-yield consistent `strain -> resultant -> tangent` continuation.

### 6.3 Ueda–Rashed–Paik 1984/1985

These papers provide explicit combined-load buckling/ultimate/plastic interaction checks. They remain useful independent checks but are not a current strain-to-resultant tangent operator.

### 6.4 Inoue & Kato 1983 is the important source found in this R03 audit

Primary source:

Tetsuro Inoue and Ben Kato, *Flexural Rigidities and Local Buckling of Steel Plates in the Plastic Flow Range*, Transactions of AIJ, No. 332, 1983.

The paper directly studies yielded steel plates under two orthogonal in-plane compressions. It uses the **von Mises yield condition** and **Reuss incremental equations** for non-hardening material and derives finite out-of-plane flexural rigidities at the instant of local buckling in the plastic-flow range.

Its important implication for NZ-SCCM is exactly the user's point:

```text
POST-YIELD STEEL-PLATE BENDING RIGIDITY IS FINITE,
STATE-DEPENDENT,
AND DIRECTION/COUPLING DEPENDENT UNDER BIAXIAL STRESS.
```

The same paper treats the strain-hardening range in an orthotropic form and states that `Ex,Ey` are functions of the current `sigma_x,sigma_y`; the corresponding bending rigidities are therefore direction-dependent.

### 6.5 Inoue & Kato 1993

Their later plastic-buckling paper develops an effective plastic shear/twisting rigidity and shows that the shear part needs its own plastic treatment. This is relevant to a future arbitrary-shear subgate, but it is not required to pretend that the current `Nxy=0` Z-family shear-postbuckling problem is already closed.

### 6.6 Isami 1994

Isami's biaxial elasto-plastic stiffened-plate method explicitly cites the Inoue-type out-of-plane flexural rigidities for the elastic / plastic-flow / strain-hardening ranges and uses direction-specific elasto-plastic material response under prescribed biaxial strain ratio. It supports the architecture of distinct current x/y tangent properties, but it still does not directly supply the present PBL large-deflection current operator after spatially nonuniform yielding.

---

## 7. Why R03 does NOT simply replace E by Et after first yield

This is the most important source boundary found in this execution.

The R02 seven-harmonic Airy solution follows from the **homogeneous elastic** compatibility equation

\[
\nabla^4F
=E\Delta(\phi_{xy}^2-\phi_{xx}\phi_{yy}).
\]

After pointwise yielding begins, the material tangent becomes a local matrix

\[
\mathbf C^{ep}(x,y,z;\sigma_x,\sigma_y,\tau_{xy}),
\]

and yielded/unloading regions need not occupy the whole plate simultaneously. Therefore the elastic Airy operator, its seven fixed harmonic coefficients and the elastic coefficient `K_A` cannot in general remain unchanged merely by writing

```text
E -> Et_x
E -> Et_y
```

or by inserting one scalar tangent modulus into `D=Et^3/[12(1-nu^2)]`.

Doing that would mix:

1. material plasticity,
2. local postbuckling amplitude condensation,
3. biaxial coupling,
4. through-thickness loading/unloading,

without a source-consistent derivation.

So R03 deliberately refuses to declare the post-first-yield operator closed.

---

## 8. Exact current stopping point after R03

The steel-shell chain is now:

```text
mean biaxial strain
-> explicit PBL amplitude U
-> finite Airy postbuckling stress/resultants
-> exact condensed A_pb^tan
-> exact face [A,B,D] current tangent
-> exact two-face 6x6 [N,M] tangent
-> local pointwise Mises first-yield diagnostic
```

This chain is **closed before first local steel yield**.

The only remaining steel-shell constitutive gap is:

```text
POST-FIRST-YIELD:
spatially nonuniform biaxial elastoplastic material tangent
+ through-thickness bending/unloading rigidity
+ consistency with the PBL large-deflection amplitude/Airy redistribution
```

This is narrower and more precise than the R02 statement `post-yield continuation open`.

It is also now clear that the source family for this gap is primarily **Inoue–Kato incremental plastic plate rigidity / biaxial elastoplastic plate theory**, not Yun effective width and not Ueda/Ishibashi ultimate interaction formulas.

---

## 9. Governance result

```text
SSNC_R03_CURRENT_6X6_TANGENT_GATE = PASS
ELASTIC_POSTBUCKLING_CURRENT_TANGENT = SOURCE/DERIVATION CLOSED
POSTBUCKLING_A11_NE_A22 = DEMONSTRATED
GLOBAL_DX_DY_STATE_DEPENDENCE = DEMONSTRATED
OWN_SKIN_D_PRE_FIRST_YIELD = ELASTIC
LEVER_ARM_BENDING_TANGENT = CURRENT / DEGRADED THROUGH A_pb
POST_FIRST_YIELD_2D_PLASTIC_TANGENT = OPEN
SHEAR_POSTBUCKLING = OPEN
EFFECTIVE_WIDTH_PRODUCTION = FALSE
GLOBAL_MARGUERRE_AIRY_CHANGED = FALSE
GLOBAL_ULTIMATE_STATE_CHANGED = FALSE
Pu_CALCULATED_IN_R03 = FALSE
```

**No Z0–Z6 Pu calculation is authorized by R03.**

The next steel-only subgate, if continuing immediately, is to source-close the first-yield-to-post-yield transition using the Inoue–Kato biaxial plastic rigidity framework (and a compatible current membrane law) without altering the global Marguerre–Airy equations or the fixed ultimate-state criterion.
