# NZ-SCCM — Yun always-on steel-shell operator rewire R17

**Time:** 2026-08-24 13:26 +08:00  
**Status:** `ARCHITECTURE_CORRECTION / R16_ACTIVATION_GATE_WITHDRAWN / YUN_ALWAYS_ON / DIRECT_AIRY_STIFFNESS_EQUILIBRIUM_REWIRE_AUTHORIZED / R07_R14_PRE_REWIRE_BASELINES`

## 0. Correction trigger

R16 made a layer error: it used case-specific `B_s/t_s`, `sigma_cr`, and yield ordering to decide whether the Yun module itself should be active. That is not the intended steel-shell architecture.

The corrected rule is:

\[
\boxed{
\text{Yun module is always present for every steel-shell case.}
}
\]

Geometry, slenderness, yield ordering and current stress state determine the **response produced by the Yun module**; they do not switch the module on or off.

Therefore R16's numerical `sigma_cr/f_y` calculations are retained only as diagnostic event-ordering information. The following R16 governance inferences are withdrawn:

```text
Z_YUN_ELASTIC_PREYIELD_GATE = INACTIVE
Z6_YUN_PROGRESSIVE_ELASTIC_AREA = REJECT
T120_YUN_ELASTIC_PREYIELD_GATE = INACTIVE
BH005_BH020_YUN_ELASTIC_PREYIELD_GATE = INACTIVE
ONLY_T360_BH032_BH050_USE_YUN = REJECT
```

No case is excluded from Yun on the basis of a parameter threshold.

---

## 1. The project already contained the correct precedent

The executed 2026-08-18 unified Yun + ideal-EP recalculation explicitly established:

```text
YIELD FIRST changes the steel material state;
it does NOT delete the Yun/Karman local-amplitude geometry or membrane redistribution.
```

It also used one continuous Yun local-amplitude row for every local strip/face, with no S0/S1/S2 activation switch.

That earlier architecture is now restored as the conceptual basis of the steel-shell phase, while preserving the newer Marguerre--Airy / `Ny-My` terminal identity.

The Yun Ch.2 exact symbolic audit also proves that the Yun Airy coefficients, `k_crx`, `k_p`, axial stress redistribution and edge-shortening compatibility have finite analytic/D15 form and require no formal spatial quadrature.

---

## 2. Correct steel-shell phase identity

For every steel-shell specimen define an always-on current steel operator

\[
\boxed{
\mathcal Y_s:
(D,q,\alpha,\{A_i^\pm\})
\mapsto
\{\sigma_s,E_{t,s},\mathbf N_s,\mathbf M_s,
\mathbf K_s,R_{q,s},R_{\alpha,s},R_{A_i}\}.
}
\]

`A_i^\pm` are finite current local-amplitude coordinates of the Yun/Karman subpanel geometry. They are not material points and are not case-classification states.

```text
YUN_MODULE_ACTIVE = TRUE FOR ALL STEEL_SHELL_CASES
SIGMA_CR_OVER_FY = DIAGNOSTIC_ONLY
YIELD_EVENT = MATERIAL_EVENT / NOT_MODULE_DELETION
LOCAL_BUCKLING_EVENT = DIAGNOSTIC / NOT_OPERATOR_ACTIVATION_SWITCH
```

---

## 3. Yun local geometry is inserted before steel stress is evaluated

For local subpanel `i`, retain the Yun finite local field

\[
\phi_i=
\left(1-\cos\frac{2\pi x_i}{B_{s,i}}\right)
\left(1-\cos\frac{2m_i\pi y}{\ell_i}\right).
\]

The steel face strain is not the old gross-face affine strain alone. It is the global Marguerre--Airy face strain plus the Yun/Karman local geometric terms. In the previously executed notation,

\[
\boxed{
\varepsilon_{s,i}
=
\varepsilon_y^g
+A_i(w_{0,y}^g+\Delta w_{,y}^g)\phi_{i,y}
+A_{0i}\Delta w_{,y}^g\phi_{i,y}
+\left(A_{0i}A_i+\frac12A_i^2\right)\phi_{i,y}^2.
}
\]

Hence local redistribution exists continuously even when the hypothetical pure-elastic Yun bifurcation stress is above `f_y`.

---

## 4. Current stress and current tangent are part of the Yun steel operator

The geometric Yun module must be composed with the current steel constitutive law:

\[
\boxed{
\sigma_s=\sigma_s(\varepsilon_s),
\qquad
E_{t,s}=\frac{d\sigma_s}{d\varepsilon_s}.
}
\]

Until a fuller source-closed steel hardening law is adopted, the already-executed source-frozen ideal elastic-perfectly-plastic law remains an admissible minimal baseline:

\[
\boxed{
\sigma_s=\operatorname{clip}(E_s\varepsilon_s,-f_y,+f_y).
}
\]

Its tangent changes automatically with the current state. There is no whole-face `E_t=0` switch and no rule that deletes Yun after first yield.

Important source boundary:

```text
YUN_CH2 = GEOMETRIC / AIRY / LARGE_DEFLECTION REDISTRIBUTION SOURCE
CURRENT_STEEL_SIGMA_TANGENT = COMPOSED MATERIAL PART OF STEEL OPERATOR
DO_NOT_CLAIM_YUN_CH2_ALONE_IS_AN_ARBITRARY_VARIABLE_MODULUS_LAW
```

---

## 5. Yun Airy redistribution enters the steel membrane resultants

The Yun Ch.2 Airy solution supplies finite harmonic local membrane redistribution. In local notation,

\[
N_{x,s}^{Y}=F_{i,yy}^{Y},\qquad
N_{y,s}^{Y}=F_{i,xx}^{Y},\qquad
N_{xy,s}^{Y}=-F_{i,xy}^{Y}.
\]

The global Marguerre--Airy field is **not** supplemented by an unrelated second global Airy solution. Instead, the Yun finite-harmonic Airy field is the local steel-phase redistribution operator nested inside the global steel contribution.

The global generalized strain/state generates the local steel field; the local Yun solution returns current steel membrane resultants and tangents to the same global equilibrium system.

```text
GLOBAL_AIRY_AND_LOCAL_YUN = NESTED COUPLING
INDEPENDENT_DOUBLE_GLOBAL_AIRY = NO
USE_GROSS_MA_q_AS_LOCAL_YUN_A = NO
LOCAL_A_i = CURRENT FINITE INTERNAL COORDINATE
```

---

## 6. Yun local amplitude row remains in the coupled equations

The previously executed continuous local residual is restored as the correct structural form:

\[
\boxed{
R_{A_i}=C_\sigma
\left[
 k_{cr}A_i
 +H(2A_{0i}A_i+A_i^2)(A_i+A_{0i})
\right]
-\bar\sigma_{c,i}(A_i+A_{0i})=0,
}
\]

where

\[
\bar\sigma_{c,i}
=-\frac1{\Omega_i}\int_{\Omega_i}\sigma_s\,d\Omega.
\]

The row remains present whether yielding occurs before or after the hypothetical purely elastic bifurcation.

Thus:

```text
R_Ai_EXISTS_FOR_EVERY_LOCAL_STEEL_SUBPANEL = YES
R_Ai_DELETED_WHEN_SIGMA_CR_GT_FY = NO
R_Ai_DELETED_AFTER_YIELD = NO
```

---

## 7. Yun enters the current stiffness directly

For generalized variables `eta_a, eta_b` (global `q`, Airy/generalized membrane coordinate `alpha`, and local amplitudes `A_i`), the steel contribution to the current consistent tangent has the generic energy-consistent form

\[
\boxed{
K^{s,i}_{ab}
=t_s\int_{\Omega_i}
\left[
E_{t,s}\,\varepsilon_{s,a}\varepsilon_{s,b}
+\sigma_s\,\varepsilon_{s,ab}
\right]d\Omega.
}
\]

The first term is the current material-tangent contribution; the second is the current geometric-stress contribution. Yun therefore changes the steel stiffness continuously through both the redistributed `sigma_s` field and the state-dependent `E_{t,s}` field.

If local amplitudes are algebraically condensed after assembling the full finite system, the correct condensed global steel tangent is

\[
\boxed{
K_{gg}^{s,\mathrm{cond}}
=
K_{gg}^{s}
-K_{gA}^{s}(K_{AA}^{s})^{-1}K_{Ag}^{s}.
}
\]

This is a post-assembly finite-coordinate condensation, not deletion of Yun physics.

The total current operators must therefore use

\[
\boxed{
\mathbf A^{cur}
=\mathbf A_c^{cur}+\mathbf A_w^{cur}+\mathbf A_s^{Yun},
}
\]

\[
\boxed{
\mathbf D^{cur}
=\mathbf D_c^{cur}+\mathbf D_w^{cur}+\mathbf D_s^{Yun}.
}
\]

---

## 8. Yun enters the global equilibrium equations directly

The steel phase contributes to the same global virtual-work/equilibrium rows:

\[
R_{q,s,i}=t_s\int_{\Omega_i}\sigma_s\varepsilon_{s,q}\,d\Omega,
\]

\[
R_{\alpha,s,i}=t_s\int_{\Omega_i}\sigma_s\varepsilon_{s,\alpha}\,d\Omega.
\]

The coupled equilibrium is therefore

\[
\boxed{
R_q=R_{q,c}+R_{q,w}+\sum_iR_{q,s,i}=0,
}
\]

\[
\boxed{
R_\alpha=R_{\alpha,c}+R_{\alpha,w}+\sum_iR_{\alpha,s,i}=0,
}
\]

with

\[
\boxed{R_{A_i}=0\quad\forall i,\pm.}
\]

This replaces the notion that a precomputed constant steel-shell reduction is appended only at the terminal capacity stage.

---

## 9. Consequence for the current closed-form demand law

The present R07/R14 structural demand form

\[
P(q)=P_{cr}\frac{q}{q+q_0}+Cq(q+2q_0),
\]

\[
n(s;q)=\frac{P(q)}b+Gq(q+2q_0)(1-2s^2),
\qquad
m(s;q)=J_yqs
\]

uses pre-generated coefficients `Pcr, C, G, J_y` based on the former steel-shell treatment.

Once Yun current stress/tangent feeds the steel stiffness and equilibrium, these coefficients cannot simply remain globally frozen constants and still claim full Yun coupling.

Therefore:

```text
Pcr_C_G_Jy_FROM_PRE_YUN_ELASTIC_STEEL = PRE_REWIRE_BASELINE_ONLY
FREEZE_Pcr_C_G_Jy_THROUGH_FULL_LOADING = NOT_AUTHORIZED_FOR_YUN_REWIRE
```

The preferred target is the underlying finite residual/Jacobian formulation with Yun assembled directly. Only if the coupled equations can later be analytically eliminated back to an equivalent closed demand law may new state-consistent coefficients be introduced.

---

## 10. The terminal object remains `Ny-My`

This correction does not reopen the terminal architecture.

After solving the coupled Yun + Marguerre--Airy state,

\[
\boxed{
N_y=N_{y,c}+N_{y,w}+N_{y,s}^{Yun},
}
\]

\[
\boxed{
M_y=M_{y,c}+M_{y,w}+M_{y,s}^{Yun}.
}
\]

The structural solution still terminates in the same axial y-normal `Ny-My` resultant object. No `TC/CC/TT` pointwise concrete classification is reintroduced.

```text
Ny_My_TERMINAL = RETAIN
Nx_Mx_HARD_TERMINAL = NO
TC_CC_TT = OFF_MAINLINE
```

---

## 11. What is retained and what is replaced

### Retained

- full 2D Marguerre--Airy structural architecture;
- axial y-normal `Ny-My` terminal identity;
- ordinary-concrete core law for the Z family;
- Zhang UHPC compression law / R14 physical peak core treatment for the UHPC family;
- finite exact/D15 integration requirement;
- zero formal spatial quadrature/material points;
- R16 geometry information and `sigma_cr/f_y` calculations as diagnostics only.

### Replaced / retired from the target steel-shell solution

- specimen-by-specimen Yun activation gate;
- `sigma_cr < f_y` as a prerequisite for Yun;
- constant external-face compressive cap as the complete steel-shell physics;
- globally frozen pre-Yun steel `Pcr,C,G,J_y` through the entire nonlinear solution;
- post-hoc effective-width-only correction.

---

## 12. Status of R07 and R14 numbers

R07 and R14 remain valuable reproducible comparison baselines, but after this architecture correction they are no longer identified as the final target steel-shell production solver because their steel phase was not coupled through Yun into the current Airy/stiffness/equilibrium system.

```text
R07_Z0_Z6 = PRE_YUN_REWIRE_BASELINE
R14_STEEL_SHELL_UHPC = PRE_YUN_REWIRE_BASELINE
R14_ZHANG_UHPC_CORE = RETAINED
R07_ORDINARY_CONCRETE_CORE = RETAINED
```

No new `Pu` values are created in R17. The next execution must perform the actual steel-phase replacement and rerun the families.

---

## 13. R17 decision

```text
R17_EXECUTION = ARCHITECTURE_CORRECTION_COMPLETE

R16_SIGMA_CR_SCREEN = RETAIN_DIAGNOSTIC_ONLY
R16_PARAMETER_GATE_AS_YUN_ACTIVATION = WITHDRAWN

YUN_STEEL_SHELL_MODULE = ALWAYS_ON
YUN_LOCAL_KARMAN_GEOMETRY = ACTIVE
YUN_LOCAL_AIRY_REDISTRIBUTION = ACTIVE
CURRENT_STEEL_SIGMA = ACTIVE
CURRENT_STEEL_TANGENT = ACTIVE
YUN_TO_CURRENT_STIFFNESS = ACTIVE
YUN_LOCAL_ROWS_IN_GLOBAL_EQUILIBRIUM = ACTIVE
FINITE_LOCAL_AMPLITUDES_Ai = ACTIVE
OPTIONAL_STATIC_CONDENSATION_AFTER_ASSEMBLY = ALLOWED

STATIC_FACE_CAP_AS_COMPLETE_PRODUCTION_STEEL_MODULE = RETIRED_FROM_TARGET
PRE_YUN_Pcr_C_G_Jy_GLOBAL_FREEZE = RETIRED_FROM_TARGET

MARGUERRE_AIRY = RETAIN
Ny_My = RETAIN
TC_CC_TT = OFF_MAINLINE
ZHANG_UHPC_CORE = RETAIN
ORDINARY_CONCRETE_CORE = RETAIN

R07_R14_NUMBERS = PRE_YUN_REWIRE_BASELINES
PRODUCTION_Pu_CHANGED_IN_R17 = NO
NEW_FITTED_FACTOR = NO
```

## 14. Exact next task

```text
NEXT_TASK = REPLACE_CURRENT_STEEL_SHELL_PHASE_BY_ALWAYS_ON_YUN_OPERATOR_IN_R07_R14_FULL_RESIDUAL_JACOBIAN_AND_RERUN
```

Execution order:

1. recover the existing zero-formal-quadrature Yun local-amplitude implementation from the 2026-08-18 branch;
2. transplant only the steel-shell phase into the current Marguerre--Airy / `Ny-My` architecture;
3. keep NC and Zhang-UHPC core laws unchanged;
4. assemble Yun stress, current tangent, local Airy redistribution and every `R_Ai` into global residual/Jacobian;
5. do not classify cases by `sigma_cr/f_y` before solving;
6. solve the connected coupled branch and recover `Ny, My, Pu`;
7. rerun Z0--Z6 and T120/T360/BH family with comparator still closed during solution;
8. only after predictions are fixed, reopen Zhou/experimental comparators for validation.

```text
USER_ACCEPTANCE = PENDING
```
