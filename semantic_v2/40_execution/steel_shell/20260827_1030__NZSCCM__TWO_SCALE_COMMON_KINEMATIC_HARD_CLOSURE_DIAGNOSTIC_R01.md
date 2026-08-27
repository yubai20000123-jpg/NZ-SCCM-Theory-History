# NZ-SCCM — two-scale common-kinematic hard-closure diagnostic R01

**Time:** 2026-08-27 10:30 +08:00  
**Status:** `DIAGNOSTIC ONLY / NO THEORY PROMOTION / NO MATERIAL CHANGE / NO R06 CHANGE / NO Ly CHANGE / NO INTERFACE SLIP / NO FEM CALIBRATION`

## 0. Purpose

Execute the minimal diagnostic implied by the previous common-curvature audit:

> Tie the common composite-section curvature strictly to the same global Marguerre–Airy amplitude `q`, retain the existing R02 local amplitude condensation inside each steel face, solve only the membrane-resultant closure, and inspect what happens to the section stress sharing and the old independent moment equations.

This is **not** a new production theory and does **not** produce a new Pu. Its purpose is to test whether the excessive compression-bending in the current terminal system is being created primarily by the independent section curvatures `kappa_x,kappa_y`.

Canonical frozen sources retained:

- `current/MILESTONE_RC_SSNC_FINAL_THEORY_20260825.md`
- `semantic_v2/40_execution/steel_shell/20260825_1535__NZSCCM__STEEL_SHELL_COMMON_R06_LOCAL_YIELD_RESULTANT_GATE.py`
- `semantic_v2/40_execution/steel_shell/20260825_1550__NZSCCM__STEEL_SHELL_COMMON_R06_Z6_NONREGRESSION_T360_BH032_BLIND_EXECUTION_R01.md`
- `semantic_v2/40_execution/steel_shell/20260825_1622__NZSCCM__STEEL_SHELL_COMMON_R06_SSUHPC_7CASE_BH050_FULL_EXECUTION_R01.md`
- `semantic_v2/40_execution/steel_shell/20260827_1014__NZSCCM__COMMON_CURVATURE_VS_LOCAL_BUCKLING_KINEMATIC_PROJECTION_AUDIT_R01.md`

## 1. Minimal two-scale kinematic statement

Use one common/global displacement field

\[
\Delta w_g=bq\sin X\sin Y,
\]

and retain the steel-face local field through the already-existing R02 amplitude `U_f`.

For the common composite section,

\[
\kappa_x^g=-\Delta w_{g,xx},\qquad
\kappa_y^g=-\Delta w_{g,yy}.
\]

At the BH-family antinode, `a=2b`, `m*=2`, `ell=b`, hence

\[
\boxed{\kappa_x^g=\kappa_y^g=\pi^2q/b.}
\]

Therefore the gross strains passed to each constituent are

\[
\varepsilon_x(z)=\varepsilon_x^0+z\kappa_x^g,
\qquad
\varepsilon_y(z)=\varepsilon_y^0+z\kappa_y^g.
\]

The local steel mode is **not deleted**. In the frozen R02 code,

\[
d_f=U_f^2-A_0^2,
\]

\[
m_x=e_x-c_xd_f,\qquad m_y=e_y-c_yd_f,
\]

so local von-Karman shortening/relaxation is already condensed into each face response. The diagnostic therefore does not add a new `U^2` term and does not set `U=0`.

## 2. Diagnostic equation set HC0

For a prescribed `q`, impose

\[
\kappa_x=\kappa_x^g(q),\qquad
\kappa_y=\kappa_y^g(q),
\]

and solve only

\[
N_x^{sec}(\varepsilon_x^0,\varepsilon_y^0;q)=N_x^d(q),
\]

\[
N_y^{sec}(\varepsilon_x^0,\varepsilon_y^0;q)=N_y^d(q).
\]

Unknowns are only

\[
(\varepsilon_x^0,\varepsilon_y^0).
\]

Then evaluate, but do **not** force,

\[
\Delta M_x=M_x^{sec}-M_x^d,
\qquad
\Delta M_y=M_y^{sec}-M_y^d.
\]

This is deliberately a hard-closure diagnostic. If the old terminal architecture were kinematically compatible, the two moment residuals would remain small. If they become large, the old four independent section-resultant equations cannot coexist with the global `q` kinematics after current-material/local-buckling softening.

## 3. Reproduction gate before the new diagnostic

The reconstructed evaluator was first required to reproduce the frozen R06 states.

### BH032 frozen R06 root

The evaluator reproduces, to numerical roundoff,

\[
q=0.00137889961633743,
\]

\[
N_x^{sec}=37.4812947953\ \mathrm{N/mm},\quad
N_y^{sec}=-6798.60232003\ \mathrm{N/mm},
\]

\[
M_x^{sec}=13412.3427833\ \mathrm N,\quad
M_y^{sec}=13626.7706431\ \mathrm N,
\]

including the lower-face R06 projection

\[
\eta_-=0.425379325768,
\qquad U_-=1.51865039134\ \mathrm{mm}.
\]

### BH050 frozen R06 root

The evaluator reproduces

\[
q=0.004772819645833164,
\qquad P=13.3563763545430\ \mathrm{MN},
\]

with residuals of order `1e-5` or smaller in the raw section balances, and reproduces

\[
\eta_-=0.384465068174,
\qquad U_-=2.93984591428\ \mathrm{mm},
\]

\[
\bar\sigma_{y,+}=-75.74345\ \mathrm{MPa},
\qquad
\bar\sigma_{y,-}=-222.05557\ \mathrm{MPa}.
\]

Therefore the HC0 differences below are not produced by a changed material or a changed R06 implementation.

## 4. Phase A — blind hard closure at the already-frozen theory q values

No FEM value is used in this phase.

### 4.1 BH032

At the frozen `q=0.00137889961633743`, hard common kinematics gives

\[
\boxed{\kappa_x=\kappa_y=8.50574608\times10^{-6}\ \mathrm{mm}^{-1}}.
\]

Solving only the two membrane balances gives

\[
\varepsilon_x^0=+2.48288090\times10^{-4},
\qquad
\varepsilon_y^0=-2.39856351\times10^{-3}.
\]

Longitudinal face strains become

\[
\varepsilon_{y,+}=-0.00220293,
\qquad
\varepsilon_{y,-}=-0.00259420.
\]

The steel-face mean longitudinal stresses are

\[
\boxed{\bar\sigma_{y,+}=-284.365\ \mathrm{MPa}},
\qquad
\boxed{\bar\sigma_{y,-}=-281.075\ \mathrm{MPa}}.
\]

Load share:

```text
UHPC   62.385 %
steel  33.268 %
web     4.347 %
```

But the current section moments become only

\[
M_x^{sec}=4340.63\ \mathrm N=0.3236\,M_x^d,
\]

\[
M_y^{sec}=1845.82\ \mathrm N=0.1355\,M_y^d.
\]

### 4.2 BH050

At the frozen `q=0.004772819645833164`, hard common kinematics gives

\[
\boxed{\kappa_x=\kappa_y=1.88423367\times10^{-5}\ \mathrm{mm}^{-1}}.
\]

The two membrane balances give

\[
\varepsilon_x^0=+1.46214916\times10^{-4},
\qquad
\varepsilon_y^0=-1.76650664\times10^{-3}.
\]

Longitudinal face strains:

\[
\varepsilon_{y,+}=-0.00133313,
\qquad
\varepsilon_{y,-}=-0.00219988.
\]

Steel-face mean longitudinal stresses:

\[
\boxed{\bar\sigma_{y,+}=-222.633\ \mathrm{MPa}},
\qquad
\boxed{\bar\sigma_{y,-}=-226.111\ \mathrm{MPa}}.
\]

The lower face remains on R06, but with a much less severe projection:

\[
\eta_-=0.640157,
\qquad U_-=2.75978\ \mathrm{mm}.
\]

Load share:

```text
UHPC   61.546 %
steel  34.940 %
web     3.514 %
```

The old highly asymmetric compression-bending state disappears even though R02/R06 and all material laws are unchanged.

However, again the old moment equations are badly violated:

\[
M_x^{sec}=12404.65\ \mathrm N=0.4169\,M_x^d,
\]

\[
M_y^{sec}=5355.86\ \mathrm N=0.1782\,M_y^d.
\]

Thus HC0 is not a new equilibrium solution. It is a direct demonstration that tying `kappa` to the global mode removes most of the spurious face-force asymmetry, while simultaneously proving that the old separate `Mx/My` demand matching cannot remain unchanged.

## 5. Phase B — comparator post-check at the FEM-peak load levels

Only after the HC0 mechanism was fixed above were FEM peak loads reopened.

### 5.1 BH032 FEM peak load level

Using `P=10.99048 MN`, inversion of the unchanged frozen Airy `P(q)` gives

\[
q=0.00138864223475.
\]

#### Current four-equilibrium section bridge

At this same load:

\[
\kappa_y=4.87634\times10^{-5}/\mathrm{mm},
\qquad
\chi_y=0.4458,
\]

\[
\bar\sigma_{y,+}=-256.61\ \mathrm{MPa},
\qquad
\bar\sigma_{y,-}=-278.07\ \mathrm{MPa},
\]

with load share

```text
UHPC   64.389 %
steel  31.316 %
web     4.294 %
```

#### HC0 hard common kinematics

\[
\kappa_x=\kappa_y=8.56584\times10^{-6}/\mathrm{mm},
\qquad
\chi_y=0.08153,
\]

\[
\bar\sigma_{y,+}=-284.36\ \mathrm{MPa},
\qquad
\bar\sigma_{y,-}=-281.07\ \mathrm{MPa},
\]

with load share

```text
UHPC   62.555 %
steel  33.118 %
web     4.327 %
```

The archived BH032 FEM peak load-share comparator is

```text
UHPC   66.49 %
steel  28.95 %
web     4.56 %
```

Thus hard common curvature does not improve every BH032 internal quantity. BH032 still requires local/material redistribution beyond a pure common-plane-section picture. This is useful: the diagnostic is not simply forcing all cases toward the comparator.

### 5.2 BH050 equal-contract FEM peak load level

Using accepted equal-contract `P=12.591227 MN`, unchanged Airy inversion gives

\[
\boxed{q=0.00411758955748}.
\]

#### Current four-equilibrium section bridge

\[
\varepsilon_y^0=-0.00192732,
\qquad
\kappa_y=5.382996\times10^{-5}/\mathrm{mm},
\]

\[
\chi_y=0.64239,
\]

\[
\bar\sigma_{y,+}=-94.76\ \mathrm{MPa},
\qquad
\bar\sigma_{y,-}=-222.41\ \mathrm{MPa}.
\]

Load share:

```text
UHPC   70.501 %
steel  26.044 %
web     3.455 %
```

#### HC0 hard common kinematics

\[
\boxed{\kappa_x=\kappa_y=1.62555920\times10^{-5}/\mathrm{mm}},
\]

\[
\varepsilon_y^0=-0.00164237,
\qquad
\chi_y=0.22765.
\]

The face strains are

\[
\varepsilon_{y,+}=-0.00126849,
\qquad
\varepsilon_{y,-}=-0.00201625.
\]

The steel-face mean longitudinal stresses become

\[
\boxed{\bar\sigma_{y,+}=-212.35\ \mathrm{MPa}},
\qquad
\boxed{\bar\sigma_{y,-}=-226.32\ \mathrm{MPa}}.
\]

Load share becomes

```text
UHPC   60.391 %
steel  36.021 %
web     3.589 %
```

The accepted equal-contract FEM peak extraction is

```text
UHPC   55.80 %
steel  40.61 %
web     3.58 %
```

Hence the load-share error vector changes from approximately

```text
current four-equilibrium:  (+14.70, -14.57, -0.12) percentage points
HC0 hard closure:          ( +4.59,  -4.59, +0.01) percentage points
```

and its Euclidean magnitude falls by about `68.6%`.

This is not a calibration: no FEM value entered the HC0 equations. The FEM load is used only to choose the same physical load level for post-check.

## 6. Main result

The diagnostic gives a strong result:

```text
INDEPENDENT_SECTION_KAPPA_IS_PRIMARY_DRIVER_OF_BH050_ARTIFICIAL_COMPRESSION_BENDING = STRONGLY_SUPPORTED
HARD_COMMON_KAPPA_REMOVES_BH050_UPPER_FACE_UNLOADING_DIRECTION = YES
HARD_COMMON_KAPPA_IMPROVES_BH050_LOAD_SHARE = STRONGLY_YES
HARD_COMMON_KAPPA_IS_COMPLETE_EQUILIBRIUM_THEORY = NO
OLD_TWO_INDEPENDENT_MOMENT_BALANCES_SURVIVE_HARD_CLOSURE = NO
R02_U2_MEAN_EFFECT_MISSING = NO
R06_CHANGED = NO
```

The most important algebraic observation is that the common mode has only one generalized transverse amplitude `q`. For the BH family it imposes a fixed curvature ratio

\[
\kappa_x/\kappa_y=1.
\]

The current terminal system instead solves `kappa_x` and `kappa_y` independently. At the frozen roots:

```text
BH032: kappa_y/kappa_x = 2.312
BH050: kappa_y/kappa_x = 1.476
```

so the terminal common strain field is not the curvature field of the global displacement mode used to generate the Airy demand.

## 7. What the complete repair must look like

The next model must **not** add the two hard constraints on top of the old four resultant equations; that would be overconstrained and Phase A shows why.

The correct generalized-coordinate structure is instead:

1. one common/global displacement amplitude `q` fixes the common curvature field;
2. R02 local amplitudes `U_f` remain condensed local variables and keep their existing `U^2-A0^2` membrane-relaxation terms;
3. mean/in-plane variables enforce membrane equilibrium/compatibility;
4. the two pointwise terminal equations `Mx_sec=Mx_d` and `My_sec=My_d` are replaced by **one global transverse virtual-work equation associated with q**.

Schematically,

\[
\boxed{R_q=\delta W_{int}(q,U_f,\varepsilon^0)-\delta W_{ext}=0.}
\]

The current resultants must enter this `R_q`. Therefore local steel softening can feed back into global deflection through the same `q`, rather than being absorbed by an independent section curvature.

For a conservative pre-R06 branch this can be written after local condensation as

\[
\widehat\Pi(q,\varepsilon^0)
=\Pi\bigl(q,\varepsilon^0,U_f^*(q,\varepsilon^0)\bigr),
\qquad
\frac{\partial\Pi}{\partial U_f}=0,
\]

and the envelope theorem provides the reciprocal `U -> q` feedback automatically. No fitted `qU` coefficient is required.

After R06 activation, the same idea should be written in current virtual-work/resultant form rather than assuming a global scalar potential for the path-free cap.

## 8. Remaining nontrivial requirement

A production `R_q` cannot be obtained from the single antinode section alone. It must integrate the current bending/resultant work over the continuous representative half-wave, including the twisting contribution away from the antinode.

Therefore the next derivation target is:

\[
R_q=\int_{\Omega_{1/2}}
\left[
\mathbf N:\frac{\partial\boldsymbol\varepsilon}{\partial q}
+\mathbf M:\frac{\partial\boldsymbol\kappa}{\partial q}
\right]d\Omega
-\frac{\partial W_{ext}}{\partial q}=0,
\]

with

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = retained
FORMAL_SPATIAL_QUADRATURE = 0
MATERIAL_POINTS = 0
```

This is a structural-current virtual-work closure problem, not a reason to retune R06 or add interface slip.

## 9. Decision

```text
HC0_DIAGNOSTIC = PASS_AS_CAUSAL_TEST
HC0_PRODUCTION_Pu = PROHIBITED
COMMON_KAPPA_FROM_q = REQUIRED_FOR_NEXT_DERIVATION
OLD_INDEPENDENT_kappa_x_kappa_y_TERMINAL_BRIDGE = HOLD_FOR_REPLACEMENT
NEXT_TASK = DERIVE_ONE_q_GLOBAL_CURRENT_VIRTUAL_WORK_RESIDUAL_WITH_R02_LOCAL_CONDENSATION
```
