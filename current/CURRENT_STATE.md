# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-24 13:26 +08:00  
**Status:** `MARGUERRE_AIRY_EXPLICIT / Ny_My_RESULTANT_TERMINAL / R17_YUN_ALWAYS_ON_REWIRE_AUTHORIZED / R16_PARAMETER_ACTIVATION_GATE_WITHDRAWN / R07_R14_PRE_YUN_REWIRE_BASELINES / STATIC_STEEL_CAP_RETIRED_FROM_TARGET / TC_ROUTE_WITHDRAWN / USER_ACCEPTANCE_PENDING`

> This entry supersedes the 13:10 R16 entry in **steel-shell architecture and next-task governance**. R16 geometry and `sigma_cr/f_y` calculations remain available as diagnostic event-ordering information only. They must not be used to switch the Yun module on/off.

## 0. Frozen architecture

```text
STRUCTURAL_FRONT = FULL_2D_MARGUERRE_AIRY
TERMINAL_OBJECT = AXIAL_Y_NORMAL_Ny_My
Nx_Mx_IN_STRUCTURAL_FIELD = YES
Nx_Mx_HARD_TERMINAL_ON_Y_CUT = NO
FORMAL_SPATIAL_QUADRATURE = 0
THICKNESS_QUADRATURE = 0
MATERIAL_POINTS = 0
LOAD_PATH_TRACKING = 0
HISTORY_STATE_MACHINE = OFF_MAINLINE
EXPERIMENT_IN_ROOT_SELECTION = 0
FEM_IN_ROOT_SELECTION = 0
TC_CC_TT_ROUTE = OFF_MAINLINE
```

The corrected steel-shell chain is

\[
\boxed{
\text{global Marguerre--Airy state}
\rightarrow
\text{always-on Yun/Karman steel-shell operator}
\rightarrow
\{\sigma_s,E_{t,s},N_s,M_s,K_s,R_s,R_{A_i}\}
\rightarrow
\text{coupled global equilibrium/Jacobian}
\rightarrow
(N_y,M_y)
\rightarrow P_u.
}
\]

No specimen is classified into “use Yun / do not use Yun” before solving.

---

## 1. R17 architecture correction

Report:

`semantic_v2/40_execution/20260824_1326__NZSCCM__YUN_ALWAYS_ON_STEEL_SHELL_OPERATOR_REWIRE_R17.md`

Operator contract:

`semantic_v2/40_execution/steel_shell/20260824_1326__NZSCCM__YUN_ALWAYS_ON_OPERATOR_CONTRACT_R17.py`

The project already had the correct precedent in

`semantic_v2/40_execution/steel_shell/20260818_1421__NZSCCM__Z1_Z4__UNIFIED_YUN_IDEAL_EP_LOCAL_AMPLITUDE_FULL_RECALC.md`:

```text
YIELD FIRST changes the steel material state;
it does NOT delete the Yun/Karman local-amplitude geometry or membrane redistribution.
```

R17 restores that principle under the current Marguerre--Airy / `Ny-My` architecture.

---

## 2. R16 supersession boundary

Retained from R16:

- local geometry/provenance information;
- `B_s/t_s` values;
- Yun elastic `sigma_cr` and `sigma_cr/f_y` calculations;
- event-ordering interpretation such as “hypothetical elastic bifurcation above/below first yield”.

Withdrawn from R16:

```text
R16_PARAMETER_GATE_AS_YUN_MODULE_ACTIVATION = WITHDRAWN
Z_YUN_INACTIVE_BECAUSE_SIGMA_CR_GT_FY = WITHDRAWN
T120_YUN_INACTIVE_BECAUSE_SIGMA_CR_GT_FY = WITHDRAWN
BH005_BH020_YUN_INACTIVE_BECAUSE_SIGMA_CR_GT_FY = WITHDRAWN
ONLY_T360_BH032_BH050_PROGRESSIVE_CANDIDATES = WITHDRAWN
```

Correct rule:

```text
YUN_STEEL_SHELL_MODULE = ALWAYS_ON
SIGMA_CR_OVER_FY = DIAGNOSTIC_ONLY
YIELD_ORDERING = DIAGNOSTIC_ONLY
```

---

## 3. Always-on Yun steel operator

For every steel-shell case:

\[
\boxed{
\mathcal Y_s:
(D,q,\alpha,\{A_i^\pm\})
\mapsto
\{\sigma_s,E_{t,s},\mathbf N_s,\mathbf M_s,
\mathbf K_s,R_{q,s},R_{\alpha,s},R_{A_i}\}.
}
\]

The steel strain includes the global face strain and Yun/Karman local geometry:

\[
\varepsilon_{s,i}
=
\varepsilon_y^g
+A_i(w_{0,y}^g+\Delta w_{,y}^g)\phi_{i,y}
+A_{0i}\Delta w_{,y}^g\phi_{i,y}
+\left(A_{0i}A_i+\frac12A_i^2\right)\phi_{i,y}^2.
\]

Current steel response:

\[
\sigma_s=\sigma_s(\varepsilon_s),
\qquad
E_{t,s}=d\sigma_s/d\varepsilon_s.
\]

Until a fuller source-closed steel hardening law is adopted, the already-executed minimal baseline remains

\[
\sigma_s=\operatorname{clip}(E_s\varepsilon_s,-f_y,+f_y).
\]

The Yun/Karman geometry remains active before and after yield.

---

## 4. Yun enters Airy redistribution, stiffness and equilibrium

The Yun finite harmonic Airy field supplies the local steel-phase membrane redistribution:

\[
N_{x,s}^{Y}=F_{yy}^{Y},\qquad
N_{y,s}^{Y}=F_{xx}^{Y},\qquad
N_{xy,s}^{Y}=-F_{xy}^{Y}.
\]

This is nested inside the global steel phase; it is not a second independent global Airy solution.

Each local amplitude keeps its continuous residual:

\[
R_{A_i}=0.
\]

The current steel tangent contribution has the energy-consistent form

\[
K^{s,i}_{ab}
=t_s\int_{\Omega_i}
\left[
E_{t,s}\varepsilon_{s,a}\varepsilon_{s,b}
+\sigma_s\varepsilon_{s,ab}
\right]d\Omega.
\]

If local amplitudes are condensed, condensation occurs only **after full finite assembly**:

\[
K_{gg}^{s,cond}
=K_{gg}^{s}-K_{gA}^{s}(K_{AA}^{s})^{-1}K_{Ag}^{s}.
\]

Global equilibrium:

\[
R_q=R_{q,c}+R_{q,w}+\sum_iR_{q,s,i}=0,
\]

\[
R_\alpha=R_{\alpha,c}+R_{\alpha,w}+\sum_iR_{\alpha,s,i}=0,
\]

\[
R_{A_i}=0\qquad\forall i,\pm.
\]

Thus Yun acts in the **structural equations themselves**, not only as a terminal capacity correction.

---

## 5. Consequence for previous steel-shell simplifications

The former external-face static compressive cap and frozen elastic-steel structural coefficients are no longer the target steel-shell physics.

```text
STATIC_FACE_CAP_AS_COMPLETE_PRODUCTION_STEEL_MODULE = RETIRED_FROM_TARGET
PRE_YUN_Pcr_C_G_Jy_GLOBAL_FREEZE = RETIRED_FROM_TARGET
POST_HOC_EFFECTIVE_WIDTH_ONLY_FIX = NOT_CURRENT_ROUTE
```

Once Yun current stress/tangent feeds stiffness and equilibrium, pre-generated constant

```text
Pcr, C, G, Jy
```

cannot remain globally frozen through the full nonlinear loading and still claim full Yun coupling. The target is the underlying finite residual/Jacobian system; an equivalent reduced closed law may only be regenerated after exact elimination from that coupled system.

---

## 6. Material/core identities retained

```text
ORDINARY_CONCRETE_CORE_FOR_Z = RETAIN
ZHANG_UHPC_CORE_FOR_T_BH = RETAIN
YUN_STEEL_SHELL_PHASE = REPLACES_PREVIOUS_STEEL_FACE_MODULE
TC_CC_TT_CONCRETE_STATE_MACHINE = OFF_MAINLINE
```

The user correction changes the steel-shell phase, not the already selected ordinary-concrete or Zhang-UHPC core laws.

---

## 7. `Ny-My` terminal retained

After the fully coupled solution,

\[
N_y=N_{y,c}+N_{y,w}+N_{y,s}^{Yun},
\]

\[
M_y=M_{y,c}+M_{y,w}+M_{y,s}^{Yun}.
\]

The terminal is still the axial y-normal `Ny-My` resultant capacity/contact object. `Nx/Mx` remain part of the full 2D structural field but are not independent hard terminal coordinates on this cut.

---

## 8. Numerical baselines now reclassified

### Steel-shell ordinary concrete — R07

```text
Z0 37.825706787 MN
Z1 24.714128548 MN
Z2 42.959011131 MN
Z3 46.495651955 MN
Z4 70.265718566 MN
Z5 14.118193577 MN
Z6 56.379421090 MN
```

Against Zhou: mean `+3.877%`, MAE `4.973%`; Z6 `+13.93%`.

Identity after R17:

```text
R07_Z0_Z6 = PRE_YUN_REWIRE_BASELINE
```

### Steel-shell UHPC — R14

```text
T120  12.252164525 MN
T360  11.133264739 MN
BH005  2.422372923 MN
BH010  4.462040087 MN
BH020  8.155351621 MN
BH032 11.163055965 MN
BH050 13.650448214 MN
```

Primary six: mean `+1.392%`, MAE `2.409%`, RMSE `2.544%`.

Identity after R17:

```text
R14_STEEL_SHELL_UHPC = PRE_YUN_REWIRE_BASELINE
R14_ZHANG_UHPC_CORE = RETAIN
```

No new `Pu` is claimed in R17.

---

## 9. Current decisions

```text
R17_ARCHITECTURE_CORRECTION = COMPLETE

R16_SIGMA_CR_SCREEN = DIAGNOSTIC_EVENT_ORDERING_ONLY
R16_PARAMETER_GATE_AS_MODULE_ACTIVATION = WITHDRAWN

YUN_STEEL_SHELL_MODULE = ALWAYS_ON
YUN_LOCAL_KARMAN_GEOMETRY = ACTIVE
YUN_LOCAL_AIRY_REDISTRIBUTION = ACTIVE
CURRENT_STEEL_STRESS = ACTIVE
CURRENT_STEEL_TANGENT = ACTIVE
YUN_TO_CURRENT_STIFFNESS = ACTIVE
YUN_LOCAL_ROWS_IN_GLOBAL_EQUILIBRIUM = ACTIVE
FINITE_LOCAL_AMPLITUDES_Ai = ACTIVE
OPTIONAL_STATIC_CONDENSATION_AFTER_FULL_ASSEMBLY = ALLOWED

MARGUERRE_AIRY = RETAIN
Ny_My_RESULTANT_TERMINAL = RETAIN
ORDINARY_CONCRETE_CORE = RETAIN
ZHANG_UHPC_CORE = RETAIN
TC_CC_TT = OFF_MAINLINE

R07_R14 = PRE_YUN_REWIRE_BASELINES
NEW_FITTED_FACTOR = NO
PRODUCTION_Pu_CHANGED_IN_R17 = NO
```

---

## 10. Exact next task

```text
NEXT_TASK = REPLACE_CURRENT_STEEL_SHELL_PHASE_BY_ALWAYS_ON_YUN_OPERATOR_IN_R07_R14_FULL_RESIDUAL_JACOBIAN_AND_RERUN
```

Execution order:

1. recover the already-executed 2026-08-18 Yun local-amplitude equations;
2. transplant them as the steel phase of the current Marguerre--Airy system;
3. keep ordinary-concrete and Zhang-UHPC core laws fixed;
4. assemble Yun Airy redistribution, current `sigma_s`, current `E_t,s`, all local `R_Ai`, and their consistent tangent into the global residual/Jacobian;
5. do not classify cases by width-thickness or `sigma_cr/f_y` before solving;
6. solve the connected coupled branch;
7. recover `Ny`, `My`, and `Pu` from the same solution;
8. rerun all Z0--Z6 and T120/T360/BH cases before reopening comparator data.

```text
USER_ACCEPTANCE = PENDING
```
