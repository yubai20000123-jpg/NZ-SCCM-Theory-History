# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-11 16:38 +08:00  
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

Define

\[
\kappa=\frac{E_0\varepsilon_0}{f_c},\qquad
x_{cr}=\frac{\rho}{\kappa},
\]

\[
W_{src}=\rho x_{cr}\int_0^{10}T_{src}(r)\,dr,
\]

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

The theory shall use symbolic parameter combinations such as \(10h-6\rho\), not long decimal constants.

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

## 2. R10B compiler — successful N48 order is governing

\[
\boxed{N_M=48}.
\]

For

\[
F\in\{U,C,T,T^7\},
\]

write

\[
\boxed{F_{48}(\lambda)=\sum_{n=0}^{48}a_n^{(F)}\mathcal C_n(\xi)},
\]

where \(\mathcal C_n\) denotes the first-kind Chebyshev polynomial and

\[
\theta_j=\frac{(j+\tfrac12)\pi}{49},\qquad
\lambda_j=\lambda_c+\lambda_h\cos\theta_j.
\]

All 49 coefficients are defined by the single formula

\[
\boxed{
a_n^{(F)}=
\frac{2-\delta_{n0}}{49}
\sum_{j=0}^{48}F(\lambda_j)\cos(n\theta_j),
\qquad n=0,\ldots,48.}
\]

No long decimal coefficient table is part of the theory.

---

## 3. Paper-style R10 → N48 → D15 derivation — COMPLETE

Canonical derivation:

- `current/theory/NZ_SCCM_R10_N48_D15_PAPER_STYLE_DERIVATION_20260811.md`

This file now gives the complete theory in paper-style form, including:

1. every material parameter and its physical meaning;
2. equivalent-uniaxial tensor and principal equivalent strains;
3. Foster source scalar and source work;
4. derivation of the R10 rise-branch coefficients from six endpoint/C2 conditions;
5. derivation of the R10 fall branch;
6. derivation of the energy equation and the closed formula for \(h\);
7. reinsertion into the unchanged U/C/T + CC/TC/TT current operator;
8. the one-formula N48 coefficient rule;
9. Cayley–Hamilton reduction of every material term to \(A_nI+B_nY\);
10. explicit recurrences for \(A_n,B_n\);
11. algebraic reconstruction of CC, TC and TT;
12. one continuous complete-halfwave coordinates and Jacobian;
13. the exact D15 moment rule for every spatial analytic term;
14. compact D15 expressions for \(P_c\) and \(R_{q,c}\);
15. a complete symbol/parameter table.

The central term-by-term chain is frozen as

\[
\boxed{
a_n^{(F)}
\rightarrow
(A_n,B_n)
\rightarrow
\mathbf F_{48}
\rightarrow
\mathbf S
\rightarrow
c_{ijk}
\rightarrow
c_{ijk}M_iM_jZ_k.}
\]

No Case21 numerical closure was performed in this step.

---

## 4. D15 exact-moment identity retained

For any retained finite spatial analytic quantity

\[
Q(X,Y,\zeta)
=\sum_{i,j,k}c_{ijk}
\mathcal C_i(\sin X)
\mathcal C_j(\sin Y)
\mathcal C_k(\zeta),
\]

D15 uses

\[
\boxed{
\mathscr D[Q]
=\sum_{i,j,k}c_{ijk}M_iM_jZ_k,
}
\]

with

\[
M_n=
\begin{cases}
\pi,&n=0,\\
2\sin(n\pi/2)/n,&n\ge1,
\end{cases}
\]

\[
Z_k=
\begin{cases}
0,&k\text{ odd},\\
2/(1-k^2),&k\text{ even}.
\end{cases}
\]

Thus formal spatial integration remains exactly zero-quadrature.

---

## 5. Status

```text
R10_MATERIAL_TARGET_AUDIT = COMPLETE
R10_CLOSED_PARAMETER_FORMULA = GOVERNING
R10B_REPRESENTATION_FIDELITY_AUDIT = PASS_ENGINEERING_WITH_REPRODUCIBILITY_GAP
HISTORICAL_COEFFICIENT_GENERATOR = UNRECOVERED
CURRENT_TRANSPARENT_COEFFICIENT_FORMULA = FROZEN
MATERIAL_COMPILER_ORDER = 48
N112_REQUIREMENT = SUPERSEDED
LONG_DECIMAL_COEFFICIENT_TABLE_IN_THEORY = PROHIBITED
R10_N48_D15_PAPER_STYLE_DERIVATION = COMPLETE
ZERO_SPATIAL_D15_ARCHITECTURE = RETAINED
STRUCTURAL_Pu_CALIBRATION = NO
CASE21_RECLOSURE_IN_THIS_STEP = NO
SWARTZ24 = NOT_STARTED
```

---

## 6. Current execution boundary

The requested theory-writing step is complete. No automatic new material stage, no automatic order escalation, and no Case21 calculation is authorized by this update.

```text
CURRENT_NEXT_TASK = USER_DIRECTED
```

When numerical work is later requested, it must use the paper-style formula chain above directly rather than reopen the material model.