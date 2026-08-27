# NZ-SCCM — common curvature vs local-buckling kinematic projection audit R01

**Time:** 2026-08-27 10:14 +08:00  
**Status:** DIAGNOSTIC ONLY / NO MATERIAL CHANGE / NO R06 CHANGE / NO AIRY COEFFICIENT CHANGE / NO COMPARATOR CALIBRATION

## 0. Audit question

Test the sharper hypothesis exposed by BH050:

> Does the current SSUHPC architecture incorrectly turn a strongly local steel-face buckling state into excessive common composite-section compression-bending?

This audit does not alter UHPC, R02, R06, local half-wave geometry, interface law, or the Marguerre–Airy coefficients.

## 1. What the frozen equations actually do

The common Marguerre–Airy kinematics retain

\[
w_0=bq_0\sin X\sin Y,\qquad \Delta w=bq\sin X\sin Y.
\]

Therefore, at an antinode, the geometric curvature carried by this common mode is

\[
\kappa_x^{MA}=\alpha^2 bq,\qquad \kappa_y^{MA}=\beta^2 bq.
\]

For the BH family, `a=2b`, `m*=2`, hence `ell=b` and

\[
\boxed{\kappa_y^{MA}=\pi^2 q/b.}
\]

The Airy demand uses the same global amplitude,

\[
M_y^d=J_yqs.
\]

However, the terminal/current section layer is parameterized independently by

\[
(q,\varepsilon_x^0,\kappa_x,\varepsilon_y^0,\kappa_y)
\]

and closes four section-resultant equations

\[
N_x^{sec}=N_x^d,\quad M_x^{sec}=M_x^d,\quad N_y^{sec}=N_y^d,\quad M_y^{sec}=M_y^d,
\]

with no equation enforcing

\[
\kappa_x=\kappa_x^{MA},\qquad \kappa_y=\kappa_y^{MA}.
\]

Thus `q` determines the common Airy displacement/moment demand, while `kappa_x,kappa_y` are allowed to re-solve independently from the nonlinear section response. Since `CURRENT_MATERIAL_TANGENT_INTO_AIRY = NO`, any section softening and curvature amplification do not feed back into the global Airy displacement field.

This is a hybrid demand/capacity bridge, not a fully kinematically closed nonlinear plate state.

## 2. R02 local bending is NOT directly inserted as global section moment

The common R06 source returns whole-width face membrane resultants. The global face moments are only eccentric membrane-force moments

\[
M_{y,f}=z_fN_{y,+}-z_fN_{y,-}.
\]

R02 local plate bending energy affects the condensed local amplitude `U`, but its local bending-moment field is not directly added to the global `M_y^{sec}`.

Therefore the literal hypothesis

```text
local plate bending moment is directly counted as common section moment
```

is false.

The actual coupling is indirect:

```text
local U / R06
 -> changes each face mean membrane resultant
 -> creates upper/lower membrane-force asymmetry at ±zf
 -> changes global section moment capacity
 -> four-equation section equilibrium changes common kappa_y
```

Because there is no independent local-shortening/common-curvature compatibility equation and no feedback of the changed section tangent into the Airy field, this mechanism can generate a much larger common section curvature than is represented by the frozen global `q` mode.

## 3. Direct kinematic closure check

### BH032 current R06 root

Frozen values:

\[
b=1600\ \mathrm{mm},\qquad q=0.00137889961633743,
\]

\[
\kappa_y^{sec}=4.78843761523\times10^{-5}\ \mathrm{mm}^{-1}.
\]

The curvature implied by the frozen common Airy displacement is

\[
\kappa_y^{MA}=\frac{\pi^2q}{b}
=8.50574608\times10^{-6}\ \mathrm{mm}^{-1}.
\]

Hence

\[
\boxed{\kappa_y^{sec}/\kappa_y^{MA}=5.63.}
\]

The section strain bridge therefore carries over five times the curvature contained in the global Airy displacement amplitude.

The existing BH032 ODB peak extraction gives

\[
\kappa_y^{FE}=3.485\times10^{-6}\ \mathrm{mm}^{-1},\qquad \chi_y^{FE}=0.03095.
\]

At the almost identical load, the R06 terminal section curvature is about 13.7 times the FEM face-mean curvature. Thus BH032's excellent Pu agreement does not validate its terminal strain/curvature state; it is compatible with error compensation.

### BH050 current R06 root

Frozen values:

\[
b=2500\ \mathrm{mm},\qquad q=0.004772819645833164,
\]

\[
\kappa_y^{sec}=6.49781910466\times10^{-5}\ \mathrm{mm}^{-1}.
\]

The curvature carried by the Airy displacement amplitude is

\[
\kappa_y^{MA}=\frac{\pi^2q}{b}
=1.88423367\times10^{-5}\ \mathrm{mm}^{-1},
\]

so

\[
\boxed{\kappa_y^{sec}/\kappa_y^{MA}=3.45.}
\]

The archived BH050 ODB strain diagnosis at its FEM peak gave

\[
\kappa_y^{FE}=6.253\times10^{-6}\ \mathrm{mm}^{-1},\qquad \chi_y^{FE}=0.09092,
\]

whereas the frozen R06 terminal has `chi_y≈0.700`. The archived diagnosis already established that both FE face strains continue becoming more compressive while the theoretical upper face unloads.

The equal-contract BH050 model has a different comparator contract and its exact face-strain curvature still requires a dedicated extraction; therefore the old ODB strain number is not silently relabeled as equal-contract evidence. The equal-contract peak stress/load-share evidence nevertheless independently shows much more symmetric continued steel compression than the frozen theory.

## 4. BH050 global moment budget

At the frozen R06 terminal,

\[
M_y^d=30060.706\ \mathrm N.
\]

Exact section components are

\[
M_y^{UHPC}=16306.076\ \mathrm N,\qquad
M_y^{web}=293.915\ \mathrm N.
\]

The steel-face membrane resultants are

\[
N_{y,+}=-302.974\ \mathrm{N/mm},\qquad
N_{y,-}=4(-222.0556)=-888.222\ \mathrm{N/mm}.
\]

Thus

\[
M_y^{faces}=23[N_{y,+}-N_{y,-}]
=13460.715\ \mathrm N.
\]

The moment shares are approximately

```text
UHPC       54.24 %
steel-face eccentric membrane couple 44.78 %
web         0.98 %
```

Therefore almost 45% of the theoretical common longitudinal bending moment at BH050 terminal is generated by the large upper/lower mean membrane-force imbalance.

This is the exact algebraic path by which severe local-face response becomes large common compression-bending in the current section closure.

## 5. Why R06 projection amplifies the tendency without being the root kinematic defect

At BH050 terminal, the actual common lower-face strain is

\[
\varepsilon_{y,-}^{common}=-0.003629956.
\]

R06 does not return a mean stress at that full strain. It projects to the first local-yield ray state

\[
\eta_y=0.384465,
\qquad
\varepsilon_{y,-}^{proj}=-0.001395591,
\]

and returns

\[
\bar\sigma_{y,-}^{R06}=-222.056\ \mathrm{MPa}.
\]

Thus the common kinematic lower-face strain can continue becoming much more compressive while the returned lower-face membrane force grows only through the projected local-yield boundary. To satisfy the unchanged `M_y^d`, the four-equation solve can increase `kappa_y` and unload the upper face.

This does not prove R06 itself is wrong. It proves that a path-free local face cap embedded inside an independently re-solved common section curvature can strongly amplify the missing global/current kinematic feedback.

## 6. Main finding

The audit result is:

```text
DIRECT_LOCAL_BENDING_MOMENT_DOUBLE_COUNT = FALSE
INDIRECT_LOCAL_TO_GLOBAL_BENDING_PROJECTION = TRUE
COMMON_Q_TO_SECTION_KAPPA_KINEMATIC_CLOSURE = ABSENT
CURRENT_SECTION_SOFTENING_FEEDBACK_INTO_AIRY = ABSENT
BH032_PU_AGREEMENT_VALIDATES_CURVATURE_PATH = FALSE
BH050_EXCESS_COMPRESSION_BENDING_ARCHITECTURE_HYPOTHESIS = STRONGLY_SUPPORTED
```

The precise problem is not that `U^2` or local bending moment was literally added twice. The problem is that the architecture combines:

1. a global Airy displacement/moment demand based on the initial composite stiffness and amplitude `q`, with
2. a nonlinear section whose common curvature is independently re-solved after local steel softening,

without a compatibility/update equation tying the new section curvature back to the global displacement field.

This allows the terminal layer to find a highly compression-bending strain state that supports the Airy N–M demand even when the finite-element path remains predominantly membrane compression.

## 7. Consequence for the latest four-equation / fold branch

The newer execution rule that treats UHPC compression peak as only a competing event is still the correct improvement over forcing a fifth `eps=-0.0035` equation. However, the four-equation continuation still uses the same independent `eps0,kappa` section bridge.

Therefore the BH071+ transverse `J4` fold remains a mathematically valid event of the current four-equation system, but its physical interpretation as a structural Pu mechanism must be held pending repair/audit of the common `q`–section-curvature compatibility. It must not be promoted to a universal physical instability criterion from the present equations alone.

## 8. Minimal next theory task

Do not change materials, R06, local `Ly`, or introduce interface slip yet.

Derive one common two-scale kinematic closure in which

\[
w_s=w_g(q)+w_l(U),
\]

but the common composite curvature is tied to the common mode,

\[
\kappa_i^{common}=\kappa_i[w_g],
\]

while local curvature/shortening generated by `w_l` remains a zero-mean/local generalized field and is not automatically converted into the common section curvature.

Then rederive the section equilibrium/energy so that any nonlinear section softening that truly changes global curvature must feed back through the same common displacement variable rather than through an independent `kappa_i` capacity parameter.

This should first be executed as a BH032/BH050 non-calibrated diagnostic. No FEM value may be used to fit a coupling coefficient.