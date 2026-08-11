# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-11 16:31 +08:00  
**Purpose:** 唯一当前工作入口；保持主线简单。

## 0. Highest-priority contract

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
ACTIVE_MODE = m=1
KINEMATICS = NGUYEN_SECOND_ORDER
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
```

No spatial Gauss/Simpson/adaptive quadrature, material-point grid, moving TT/TC/CC cells, whole-structure P/R fitting, structural-load material calibration, or finite-difference production derivatives.

---

## 1. Material theory — use the closed R10 formula, not coefficient tables

The governing material chain is

```text
source Foster current relation
-> R10 one-dimensional energy-smoothed scalar
-> SAME U/C/T + CC/TC/TT multidimensional current map
```

The R10 scalar is already a compact closed formula. Define

\[
\kappa=\frac{E_0\varepsilon_0}{f_c},\qquad x_{cr}=\frac{\rho}{\kappa},
\]

\[
W_{src}=\rho x_{cr}\int_0^{10}T_{src}(r)\,dr,
\]

and

\[
\boxed{
h=\frac15\left(\frac{W_{src}}{x_{cr}}-\frac{\rho}{10}-\frac92u_r\right)}.
\]

Rise branch, \(\tau=t/x_{cr}\):

\[
\boxed{
u_1(\tau)=
\rho\tau+(10h-6\rho)\tau^3+(8\rho-15h)\tau^4+(6h-3\rho)\tau^5}.
\]

Fall branch, \(s=(t-x_{cr})/(9x_{cr})\):

\[
\boxed{
u_2(s)=h+(u_r-h)(10s^3-15s^4+6s^5)}.
\]

Therefore the theory shall use symbolic parameter combinations such as \(10h-6\rho\), not long decimal constants.

The multidimensional relation remains

\[
U_i=\kappa\lambda_i-C_i+\kappa c_i+\rho T_i-\kappa t_i,
\]

\[
s_+=U_+-a_{cc}C_+^2C_-+C_+T_- -\rho a_tT_+T_-^8,
\]

\[
s_-=U_- -a_{cc}C_-^2C_+ + C_-T_+ -\rho a_tT_-T_+^8.
\]

No new material route is active.

---

## 2. R10B compiler — restore the successful N48 order

R10B is only the analytic compiler needed by D15. The governing order is

\[
\boxed{N_M=48}.
\]

The previous N112 re-freeze is superseded. The N112 coefficient table has been removed from `current/`.

For

\[
F\in\{U,C,T,T^7\},
\]

write

\[
\boxed{F_{48}(\lambda)=\sum_{n=0}^{48}a_n^{(F)}T_n(\xi)}.
\]

Use

\[
\theta_j=\frac{(j+\tfrac12)\pi}{49},\qquad
\lambda_j=\lambda_c+\lambda_h\cos\theta_j,
\]

and the single general coefficient formula

\[
\boxed{
a_n^{(F)}=
\frac{2-\delta_{n0}}{49}
\sum_{j=0}^{48}F(\lambda_j)\cos(n\theta_j),
\qquad n=0,\ldots,48.}
\]

This is the complete calculation rule for all 49 coefficients. The theory does not print 49 long decimal numbers.

Equivalent theoretical projection form:

\[
a_0^{(F)}=\frac1\pi\int_0^\pi F[\lambda(\theta)]d\theta,
\]

\[
a_n^{(F)}=\frac2\pi\int_0^\pi F[\lambda(\theta)]\cos(n\theta)d\theta,
\quad n\ge1.
\]

Historical R10B already achieved a complete N48 zero-spatial Case21 stationary root. The N96 fixed-D order audit differed by about 0.051%, which is accepted for engineering continuation; near-zero compiler error is not a project objective.

---

## 3. Status

```text
R10_MATERIAL_TARGET_AUDIT = COMPLETE
R10_CLOSED_PARAMETER_FORMULA = GOVERNING
R10B_REPRESENTATION_FIDELITY_AUDIT = PASS_ENGINEERING_WITH_REPRODUCIBILITY_GAP
HISTORICAL_COEFFICIENT_GENERATOR = UNRECOVERED
CURRENT_TRANSPARENT_COEFFICIENT_FORMULA = FROZEN
MATERIAL_COMPILER_ORDER = 48
N112_REQUIREMENT = SUPERSEDED
LONG_DECIMAL_COEFFICIENT_TABLE_IN_THEORY = PROHIBITED
ZERO_SPATIAL_D15_ARCHITECTURE = RETAINED
STRUCTURAL_Pu_CALIBRATION = NO
SWARTZ24 = NOT_STARTED
```

---

## 4. Immediate next task

```text
CURRENT_NEXT_TASK
= WRITE_THE_N48_MATERIAL_AND_COEFFICIENT_DERIVATION_IN_PAPER_STYLE
```

The next task is **not** Case21 reclosure. It is to present, in Zhou-style theory-derivation form:

1. source material parameters -> \(W_{src}\) -> \(h\);
2. \(u_1,u_2\) in symbolic form;
3. \(U,C,T,T^7\) definitions;
4. the single N48 coefficient formula;
5. how each term \(a_nT_n\) enters the current-map algebra;
6. then how these finite terms enter D15 exact moments.

Keep the derivation formula-based and compact. Do not list long decimal coefficient arrays.
