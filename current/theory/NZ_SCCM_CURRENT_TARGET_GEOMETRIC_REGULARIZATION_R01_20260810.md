# NZ-SCCM Current Target Geometric Regularization R01

**Date:** 2026-08-10  
**Status:** `PASS_DIAGNOSTIC / SAME_ROUTE / NO Pu RUN`

## 0. Purpose and identity

This step executes the already-authorized `EXISTING_PATH_CONSERVATIVE_CURRENT_TARGET_REFORMULATION` after the full-startup recovery. It is **not** a new material route.

Retained architecture:

```text
G18/G27 invariant current-map architecture
-> G20/G21 smooth conservative strength-domain philosophy
-> G26 moment-first D15
-> G28/G30 direct P,Rq,L kernel
```

No Case21/Swartz structural ultimate load is used to choose any material smoothing parameter. No formal spatial numerical quadrature, material-point grid, spatial cell, auxiliary quadrature, or ODE propagation is introduced.

## 1. Source/current reference used only for geometric diagnosis

For the current Case21 ordinary-concrete reference operator, use the already explicit source-shaped scalar coordinates:

```text
kappa = 2.0005129533678754
rho   = 0.1
xcr   = rho/kappa = 0.04998717945397425
eta_pi = xcr/20 = 0.0024993589726987125
eta_r = 0.05
m_t = -7/90
```

Smooth sign split:

\[
\Pi_\eta(z)=\frac{z^2(\sqrt{z^2+\eta^2}+z)}{2(z^2+\eta^2)}.
\]

For principal equivalent-uniaxial coordinate \(\lambda\):

\[
c=\Pi_\eta(-\lambda),\qquad t=\Pi_\eta(\lambda),
\]

\[
C=\frac{\kappa c}{1+(\kappa-2)c+c^2},
\]

\[
r=\frac{t}{x_{cr}},
\]

\[
H(r;r_0)=\frac12[(r-r_0)+\sqrt{(r-r_0)^2+\eta_r^2}]
-\frac12[-r_0+\sqrt{r_0^2+\eta_r^2}],
\]

\[
T=r+(m_t-1)H(r;1)-m_tH(r;10),
\]

\[
U=\kappa\lambda-C+\kappa c+\rho T-\kappa t.
\]

Current biaxial reference:

\[
s_1=U_1-a_{cc}C_1^2C_2+C_1T_2-\rho a_tT_1T_2^8,
\]

\[
s_2=U_2-a_{cc}C_2^2C_1+C_2T_1-\rho a_tT_2T_1^8,
\]

with

```text
a_cc = 0.1072329249362415
a_t  = 1-2^(-1/8) = 0.08299595679532878
```

This operator remains a regression/reference current target, not final source truth. R01 uses it only to identify where geometric sharpness actually resides.

## 2. Four-dimensional current-map interpretation

The constitutive object is a two-input/two-output map

\[
(\varepsilon_1,\varepsilon_2)\mapsto(\sigma_1,\sigma_2).
\]

Its graph is a two-dimensional manifold embedded in the four-dimensional coordinate space

\[
(\varepsilon_1,\varepsilon_2,\sigma_1,\sigma_2).
\]

For principal strains with zero principal shear, the current reference first maps to equivalent-uniaxial principal coordinates

\[
\lambda_1=\frac{\varepsilon_1+\nu\varepsilon_2}{(1-\nu^2)\varepsilon_0},
\qquad
\lambda_2=\frac{\nu\varepsilon_1+\varepsilon_2}{(1-\nu^2)\varepsilon_0},
\]

then evaluates \((s_1,s_2)\), with \(\sigma_i=f_c s_i\).

The visualization package therefore provides two complementary projections:

1. `(lambda1,lambda2,sigma1/fc)` with color = `sigma2/fc`, and the swapped projection;
2. actual Case21 `(eps1,eps2,sigma1)` in microstrain/MPa with color = `sigma2`, and the swapped projection.

## 3. Key executed finding: the true scale separation is about 1268.6:1

The previous summary that the global material interval (~3.17) had to resolve a ~0.05 tension transition was incomplete.

The current reference contains **three much thinner regularization layers**:

### 3.1 Sign-split layer near \(\lambda=0\)

Controlled by

\[
\eta_\Pi=\frac{x_{cr}}{20}=0.0024993589727.
\]

### 3.2 Crack/tension-stiffening transition near \(r=1\)

Nominal location

\[
\lambda\simeq x_{cr}=0.049987179454.
\]

Because the smoothing width in \(r\) is \(\eta_r=0.05\), the corresponding width in \(\lambda\) is approximately

\[
\Delta\lambda_{H}\simeq \eta_r x_{cr}=0.0024993589727.
\]

### 3.3 Second Foster transition near \(r=10\)

Nominal location

\[
\lambda\simeq10x_{cr}=0.49987179454,
\]

with the same order of local transition width.

The current qualification interval used by the old global primitive screen is

\[
\lambda\in[-2.4390243902,\ 0.7317073171],
\]

with width

\[
\Delta\lambda_{global}=3.1707317073.
\]

Therefore

\[
\boxed{
\frac{\Delta\lambda_{global}}{\Delta\lambda_H}
\approx1268.62
}
\]

rather than merely ~60.

This is the central R01 diagnosis:

> the main analytic pressure is a **thin-layer / curvature-concentration problem on the current surface**, not a generic failure of the unified invariant current-map architecture.

## 4. Executed curvature localization

A dense material-coordinate diagnostic of \(T(\lambda)\) was used only to locate curvature concentration; it is not a structural integration rule and is not part of the production operator.

The strongest local curvature locations found were:

| feature | lambda | T | dT/dlambda | d2T/dlambda2 |
|---|---:|---:|---:|---:|
| sign-split neighborhood | 0.000684 | 0.002281 | 7.08560 | +11582.93 |
| r=1 transition | 0.050080 | 0.973725 | 9.24396 | -4330.02 |
| r=10 transition | 0.499882 | 0.302537 | -0.777566 | +311.28 |

These three narrow ridges are then pulled through both principal coordinates and through the biaxial interaction terms. That is why a globally smooth-looking stress surface can still be expensive to represent with one small global polynomial/rational basis.

## 5. Important distinction: strength-envelope corner vs current-map ridge

G20 already addressed the **strength-domain** geometric incompatibility:

- CC: smooth conservative compression ellipse;
- TC: degree-12 C1 Bernstein connection with tangent matching at both axes;
- TT: p=8 superellipse;
- NC source kinks around cracking: narrow C2 quintic regularization.

So the current problem is **not** simply that the outer \((\sigma_1,\sigma_2)\) failure envelope still has a literal corner.

The remaining problem is that the full map

\[
(\varepsilon_1,\varepsilon_2)\mapsto(\sigma_1,\sigma_2)
\]

contains narrow high-curvature transition ridges in the strain directions. A smooth outer strength envelope alone does not remove those ridges.

## 6. Same-route target reformulation decision by sector

### 6.1 CC: retain unchanged

Keep the already-frozen low-parameter compression target

\[
\boxed{c_i^*=c_i(1+a_{cc}c_1c_2)},
\qquad a_{cc}=0.1072329249362415.
\]

Reason: current evidence does not identify the compression-dominant CC region as the source of the sharp global approximation pressure. There is no basis to sacrifice the established biaxial compression enhancement merely to simplify the compiler.

### 6.2 TC/CT: retain the existing conservative low-parameter target

Keep

\[
\boxed{c^*=c(1-\tau)},
\]

with the tensile component not amplified.

This target was already established as deliberately conservative relative to the G20 C1 TC envelope. R01 therefore does not invent a new TC surface.

### 6.3 TT: quantify an admissible contraction corridor, but freeze nothing yet

G20 p=8 remains the current outer admissible reference:

\[
\tau_1^8+\tau_2^8=1.
\]

For visualization and a material-only next screen, R01 compares two simpler conservative inner candidates:

\[
\tau_1^p+\tau_2^p=1,
\qquad p=4,2.
\]

Equal-biaxial strengths are:

| p | equal-biaxial strength | reduction vs p=8 |
|---:|---:|---:|
| 8 | 0.917004 ft | 0% |
| 4 | 0.840896 ft | 8.2996% |
| 2 | 0.707107 ft | 22.8895% |

Decision:

```text
TT p=4 = AUTHORIZED FOR MATERIAL-ONLY SCREEN
TT p=2 = LOWER-BOUND DIAGNOSTIC ONLY
NO TT EXPONENT FROZEN BY R01
```

The p=4 candidate is moderate enough to test; p=2 is presently too aggressive to freeze because it removes ~22.9% of equal-biaxial tensile strength relative to the already-conservative p=8 reference.

## 7. What smoothing is actually allowed next

The primary reformulation target is the **tensile current-map transition corridor**, not CC.

The next same-route material-only construction may widen/regularize the current-map transition corridor only if all of the following are preserved:

```text
1. sigma(0,0)=0
2. initial elastic tangent is preserved
3. uniaxial tensile strength ft anchor is preserved
4. no stress increase above the accepted material target
5. stress and tangent come from the same smooth current map
6. no runtime TT/TC/CC state partition is reintroduced
7. no Case21/Swartz Pu is used to choose smoothing width or coefficients
8. resulting expression must remain plausible under Gate A/B/C before D15 compilation
```

This means the acceptable simplification is **not** “delete tension” or “flatten every transition”. It is a controlled geometric rounding of narrow strain-space ridges while keeping the physically important axis anchors and conservative stress side.

## 8. Visual artifact manifest

The executed local package contains:

```text
02_current_map_4D_sigma1_color_sigma2.png
03_current_map_4D_sigma2_color_sigma1.png
04_tensile_utilization_transitions.png
05_tensile_curvature_concentration.png
06_TT_strength_domain_contraction_candidates.png
10_actual_eps1_eps2_sigma1_color_sigma2.png
11_actual_eps1_eps2_sigma2_color_sigma1.png
12_TC_slice_eps2_minus700.png
13_TC_slice_eps2_minus1300.png
```

Package identity:

```text
NZ_SCCM_CURRENT_TARGET_GEOMETRIC_REGULARIZATION_R01_20260810.zip
SHA256 = e6c4ebeb3615bc0c276f0d887497f29bbe7776adf8287f526da0925aa48d8e38
```

The PNG binaries are session artifacts; the repository stores the formulas, metrics, visualization manifest and regeneration code so the figures can be reproduced without relying on a chat-only image.

## 9. Gate result and next task

```text
TARGET_SURFACE_REFORMULATION_R01 = PASS_DIAGNOSTIC
ROUTE_SWITCH = NO
CC = RETAIN
TC = RETAIN_EXISTING_CONSERVATIVE_TARGET
TT_P4 = AUTHORIZED_FOR_MATERIAL_ONLY_SCREEN
TT_P2 = DIAGNOSTIC_ONLY
PRIMARY_COMPLEXITY_SOURCE = THREE_THIN_TENSILE_TRANSITION_LAYERS
CASE21_PU = NOT_RUN
SWARTZ24 = NOT_RUN
```

Only next task:

```text
TENSILE_CURRENT_MAP_TRANSITION_CORRIDOR_R02
```

R02 must remain on the same G18/G20/G27 current-map route. It should construct a very small number of explicit C2 conservative transition-corridor candidates and evaluate **material stress + tangent + surface shape + algebraic complexity before D15**. It must not reopen compiler-family hunting or use structural Pu to select a material approximation.