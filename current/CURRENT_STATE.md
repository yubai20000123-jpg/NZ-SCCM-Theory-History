# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-11 17:12 +08:00  
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

## 1. Material theory — closed R10 formula

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

Rise branch:

\[
\boxed{u_1(\tau)=
\rho\tau+(10h-6\rho)\tau^3+(8\rho-15h)\tau^4+(6h-3\rho)\tau^5}.
\]

Fall branch:

\[
\boxed{u_2(s)=h+(u_r-h)(10s^3-15s^4+6s^5)}.
\]

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

## 2. N48 analytic compiler

\[
\boxed{N_M=48}.
\]

For

\[
F\in\{U,C,T,T^7\},
\]

\[
\boxed{F_{48}(\lambda)=\sum_{n=0}^{48}a_n^{(F)}\mathcal C_n(\xi)},
\]

\[
\theta_j=\frac{(j+\tfrac12)\pi}{49},\qquad
\lambda_j=\lambda_c+\lambda_h\cos\theta_j,
\]

\[
\boxed{
a_n^{(F)}=
\frac{2-\delta_{n0}}{49}
\sum_{j=0}^{48}F(\lambda_j)\cos(n\theta_j),
\qquad n=0,\ldots,48.}
\]

No long decimal coefficient table is part of the theory.

---

## 3. Paper-style derivation

Canonical derivation:

- `current/theory/NZ_SCCM_R10_N48_D15_PAPER_STYLE_DERIVATION_20260811.md`

The term-by-term chain is

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

For any retained spatial coefficient field

\[
Q(X,Y,\zeta)
=\sum_{i,j,k}c_{ijk}
\mathcal C_i(\sin X)
\mathcal C_j(\sin Y)
\mathcal C_k(\zeta),
\]

D15 uses

\[
\boxed{\mathscr D[Q]=\sum_{i,j,k}c_{ijk}M_iM_jZ_k},
\]

with

\[
M_n=\begin{cases}
\pi,&n=0,\\
2\sin(n\pi/2)/n,&n\ge1,
\end{cases}
\qquad
Z_k=\begin{cases}
0,&k\text{ odd},\\
2/(1-k^2),&k\text{ even}.
\end{cases}
\]

---

## 4. Current fresh Case21 calculation closure — PASS

Canonical files:

- `current/theory/NZ_SCCM_CASE21_FRESH_R10_N48_D15_CLOSURE_20260811.md`
- `current/theory/NZ_SCCM_CASE21_FRESH_R10_N48_D15_CLOSURE_results.json`
- `governance/CASE21_FRESH_R10_N48_D15_CLOSURE_DECISION_20260811.md`

The calculation was regenerated from the closed R10 formulas and the N48 coefficient rule. No historical Case21 computed load, historical root or historical load path was used as an input, target, guide or calibration quantity.

Fresh limit state:

\[
\boxed{D_u\approx0.835918},
\qquad
\boxed{q_u\approx0.00178979},
\]

\[
\boxed{A_u\approx2.18354\ \mathrm{mm}},
\]

\[
\boxed{P_c\approx337.60174\ \mathrm{kN}},
\qquad
\boxed{P_s\approx30.58760\ \mathrm{kN}},
\]

\[
\boxed{P_u\approx368.18934\ \mathrm{kN}}.
\]

Equilibrium closure:

\[
R_{q,c}\approx+311.30656\ \mathrm{kN\,mm},
\]

\[
R_{q,s}\approx-311.30656\ \mathrm{kN\,mm},
\]

\[
\boxed{R_q\approx2.3\times10^{-12}\ \mathrm{kN\,mm}}.
\]

Same-expression limit determinant normalized residual:

\[
\boxed{L_{norm}\approx4.4\times10^{-9}}.
\]

The only post-calculation numerical comparison is the Case21 experimental failure load:

\[
P_{f,exp}=368.31275\ \mathrm{kN},
\]

\[
\boxed{\text{error}\approx-0.0335\%}.
\]

### 4.1 Governing dimensional/conjugacy clarification

Direct concrete axial force is

\[
\boxed{
P_c=-\frac{f_cb t_p}{2\pi^2}\mathscr D[S_{yy}]
}
\]

rather than an un-divided complete-halfwave volume resultant.

For amplitude generalized work, physical stress is conjugate to normalized physical strain

\[
\mathbf e=\frac{\mathbf E}{\varepsilon_0}
=(1+\nu)\mathbf X-\nu\operatorname{tr}(\mathbf X)\mathbf I,
\]

so

\[
\boxed{Q_q=\mathbf S:\mathbf e_{,q}}.
\]

These are dimensional/conjugacy clarifications only; the R10 material target, N48 compiler, Nguyen second-order kinematics and D15 exact-moment architecture are unchanged.

---

## 5. Status

```text
R10_CLOSED_PARAMETER_FORMULA = GOVERNING
MATERIAL_COMPILER_ORDER = 48
N112_REQUIREMENT = SUPERSEDED
LONG_DECIMAL_COEFFICIENT_TABLE_IN_THEORY = PROHIBITED
R10_N48_D15_PAPER_STYLE_DERIVATION = COMPLETE
CASE21_FRESH_R10_N48_D15_CLOSURE = PASS
HISTORICAL_CASE21_COMPUTED_RESULTS_USED_IN_FRESH_CLOSURE = NO
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
SAME_EXPRESSION_LIMIT_CONDITION = PASS_ENGINEERING
STRUCTURAL_Pu_CALIBRATION = NO
FINAL_CASE21_COMPARISON = EXPERIMENT_ONLY
SWARTZ24 = NOT_STARTED
```

---

## 6. Current execution boundary

Case21 is now closed under the current paper-style R10 → N48 → D15 chain. No automatic material change, compiler-order escalation or historical-result reconciliation is authorized.

```text
CURRENT_NEXT_TASK = USER_DIRECTED
```
