# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-12 14:51 +08:00  
**Purpose:** 唯一当前工作入口；反映独立理论审计后的正式闭合状态，以及 Case21 在该闭合理论下的全新计算闭合。

## 0. Highest-priority invariants

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
ACTIVE_MODE = m=1
KINEMATICS = NGUYEN_SECOND_ORDER
R10_MATERIAL_TARGET = FROZEN
N48_ORDER = 48
U_COMPILER  = N48-C1
C_COMPILER  = N48-C1
T7_COMPILER = N48-C1
T_COMPILER  = N48-C1-CONSTRAINED-MINIMAX
CAYLEY_HAMILTON = GOVERNING
EXACT_MOMENT_ENGINE = D15_GENERAL_TRIG_MOMENTS
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
STRUCTURAL_CALIBRATION = NO
```

Production prohibits spatial Gauss/Simpson/adaptive quadrature, spatial Chebyshev collocation, material-point grids/cells, panel-level P/R surrogates, experiment-driven material tuning and experiment-driven root selection.

---

## 1. Formal theory audit and closure

The independent theory audit did not overturn the central architecture:

\[
\boxed{
\text{continuous complete halfwave}
\to R10
\to N48\text{-}C1/MM
\to \text{CH}
\to \text{Nguyen}
\to \text{D15 exact moments}
\to P(D,q),R_q(D,q),L(D,q)
\to \text{low-dimensional limit root}.}
\]

The effective audit criticisms were closed without reopening R10, increasing N48 order, introducing spatial quadrature or creating a second Pu solver.

Current canonical formal theory:

- `current/theory/NZ_SCCM_NC_R1_FORMAL_CLOSURE_ZHOU_STYLE_CANONICAL_20260812.md` **← CURRENT GOVERNING FORMAL THEORY-WRITING BASELINE**
- `current/theory/NZ_SCCM_NC_R1_FORMAL_CLOSURE_CANONICAL_ERRATA_20260812.md`

Governance:

- `current/governance/NZ_SCCM_NC_R1_FORMAL_CLOSURE_DECISION_20260812.md`
- `current/governance/NZ_SCCM_NC_R1_LIMIT_ROOT_PRODUCTION_CONTRACT_V1_20260812.md`

No new theory number such as NC-R1.1 or NC-R2 is created.

---

## 2. Governing material/compiler identity

```text
R10 = FROZEN
N48_ORDER = 48
U = N48-C1
C = N48-C1
T7 = N48-C1
T = N48-C1-CONSTRAINED-MINIMAX
```

The formal closure defines a unique T production coefficient even if the primary minimax optimum is non-unique: preserve the same minimax optimum and select the unique minimum-H-distance solution relative to the T-C1 reference.

Current compiler evidence remains:

```text
R10_VALUE_ANCHOR_GATE = PASS
R10_FIRST_TANGENT_GATE = PASS
N48_NEAR_ZERO_T_VALUE_GATE = PASS
O1_COEFFICIENT_GATE = PASS
CAYLEY_HAMILTON_COMPATIBILITY = PASS
D15_COMPATIBILITY = PASS
```

No theorem-level 1e-10 global remainder certificate is required as an engineering production gate.

---

## 3. D15 formal identity

The governing exact-moment basis is the general finite trigonometric-thickness basis

\[
Q=\sum c_{prush}\sin^pX\cos^rX\sin^uY\cos^sY\zeta^h,
\]

with exact moments

\[
J_{pr}=\int_0^\pi\sin^pX\cos^rX\,dX,
\qquad
Z_h=\int_{-1}^{1}\zeta^h\,d\zeta.
\]

Thus naked cosine factors in intermediate fields do not invalidate D15. Final scalar integrands are finite analytic fields contracted by exact moments.

```text
D15_GENERAL_EXACT_TRIG_MOMENTS = GOVERNING
FORMAL_SPATIAL_QUADRATURE = 0
```

---

## 4. Rebar and axial-load identity

The governing formal theory explicitly defines the source steel stress law, direction strain \(\mathbf n^T\mathbf E\mathbf n\), smeared-layer thickness, \(P_s(D,q)\) and \(R_{q,s}(D,q)\).

If a reinforcement family crosses an unsupported material branch and no single-domain analytic contract is frozen:

```text
BLOCKED_AT_STEEL_BRANCH
```

No spatial rebar Gauss points/cells may be introduced.

The concrete load

\[
P_c=-\ell^{-1}\int_{\Omega_h}\sigma_{yy}\,dV
\]

is classified as the representative-halfwave **average axial load observable**, not an unconditional local-end-reaction identity.

---

## 5. NC-R1 root topology — governing

\[
\mathcal A=\{D\ge0,q\ge0,\text{ all compiler/material/rebar/source gates pass}\},
\]

\[
\Gamma_0=\operatorname{Conn}_{(0,0)}(\{R_q=0\}\cap\mathcal A).
\]

At regular points,

\[
\mathbf t_0=(R_{q,q},-R_{q,D}),
\qquad
L=P_DR_{q,q}-P_qR_{q,D}=\nabla P\cdot\mathbf t_0.
\]

Unique production ultimate:

\[
\boxed{P_u=\text{first }+\to-\text{ local maximum encountered from }(0,0)\text{ along }\Gamma_0.}
\]

Maximum-among-all-roots, experiment-nearest-root and historical-root targeting remain prohibited.

---

## 6. Zhou current-tangent role

```text
ZHOU = FULL-FIELD CURRENT-TANGENT MODAL AUDIT / INTERPRETATION
NOT = SECOND Pu SOLVER
```

For nonuniform current tangent fields, the canonical theory uses full-field exact modal second variation and D15-evaluable projected \(D_x^*,D_y^*,D_\mu^*,D_{66}^*,H^*\). Local \(t_p^3C_t/12\) formulas are only the uniform-tangent degeneration.

---

## 7. Precise non-iterative structural identity

After material coefficients are frozen and within a supported rebar branch,

\[
P(D,q)=\sum p_{ij}D^iq^j,
\qquad
R_q(D,q)=\sum r_{ij}D^iq^j,
\]

\[
L(D,q)=P_DR_{q,q}-P_qR_{q,D}.
\]

Thus the formal ultimate problem is the finite low-dimensional joint system

\[
R_q(D,q)=0,
\qquad
L(D,q)=0,
\]

followed by NC-R1 branch/root classification.

This means the theory does not depend on structural load-step/material-point iteration or spatial quadrature. A chosen low-dimensional mathematical backend may internally iterate without changing this formal identity.

---

## 8. Case21 fresh formal-closure calculation — COMPLETE

Fresh calculation report:

- `current/results/NZ_SCCM_CASE21_NC_R1_FORMAL_CLOSURE_FRESH_CALCULATION_20260812.md`

Fresh material coefficient table:

- `current/case21/NZ_SCCM_CASE21_NC_R1_FRESH_N48_COEFFICIENTS_20260812.csv`

Experiment-only source, opened only after the theoretical result was frozen:

- `current/case21/NZ_SCCM_CASE21_EXPERIMENT_ONLY_SOURCE_20260812.md`

Isolation status:

```text
HISTORICAL_CASE21_D_Q_P_ROOT_PATH_USED = NO
HISTORICAL_CASE21_THEORY_RESULT_USED = NO
HISTORICAL_FE_GAUSS_SIMPSON_RESULT_USED = NO
EXPERIMENT_USED_DURING_SOLVE = NO
EXPERIMENT_USED_FOR_ROOT_SELECTION = NO
EXPERIMENT_USED_FOR_PARAMETER_TUNING = NO
FORMAL_SPATIAL_SAMPLING = 0
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_SPATIAL_SUBDOMAINS = 1
```

Fresh material/compiler quantities include

\[
\kappa=2.0005129533678754,
\quad
x_{cr}=0.04998717945397425,
\quad
\eta=0.0024993589726987125,
\]

\[
W_{src}=0.03174123518124918,
\qquad
h=0.09799750427197022.
\]

Fresh T-minimax material representation:

\[
E_T^*=0.08957188456536706,
\]

with zero-anchor residuals at machine scale.

Fresh NC-R1 production root:

\[
\boxed{D_u=0.8903314709224796},
\]

\[
\boxed{q_u=0.0018331919936158214},
\]

\[
\boxed{A_u=2.236494232211302\ \mathrm{mm}},
\]

\[
\boxed{P_u^{theory}=372.7757254085579\ \mathrm{kN}}.
\]

Production residuals:

\[
\boxed{R_{norm}=2.1729946248051996\times10^{-9}<10^{-5}},
\]

\[
\boxed{|L_{norm}|=8.347329895379345\times10^{-6}<10^{-5}}.
\]

Continuous compiler-domain certificate over the entire complete halfwave: PASS.

Rebar branch certificate:

\[
\max|\varepsilon_s|=0.001860792774228<\varepsilon_y=0.00265,
\]

so the complete reinforcement field remains on the supported elastic branch.

First-maximum classification is confirmed by a fresh +→− sign change of the equilibrium-branch load tangent around the production root.

```text
CASE21_CURRENT_THEORY_CALCULATION = COMPLETE
CASE21_UNIQUE_PRODUCTION_Pu = REPRODUCED UNDER FORMAL-CLOSURE BASELINE
CASE21_CALCULATION_CLOSURE = PASS
```

---

## 9. Case21 experiment-only comparison

Only after the theoretical result was frozen, Nguyen Chapter 5 Section 5.2 experimental table was opened. Case21 experimental load:

\[
P_u^{exp}=336\ \mathrm{kN}.
\]

Final blind comparison:

\[
\Delta P=+36.7757254085579\ \mathrm{kN},
\]

\[
\boxed{\frac{P_u^{theory}-P_u^{exp}}{P_u^{exp}}\times100\%=+10.9451563716\%}.
\]

The experimental value did not participate in coefficient generation, root finding, branch selection or parameter adjustment.

---

## 10. Current execution boundary

```text
CASE21_FRESH_CALCULATION = COMPLETE
CASE21_CALCULATION_CLOSURE = PASS
SWARTZ24_RECALCULATION = NOT AUTHORIZED / NOT PERFORMED
R10_REOPEN = NO
N48_ORDER_CHANGE = NO
NEW_MATERIAL_MODEL = NO
NEW Pu SOLVER = NO
CURRENT_NEXT_TASK = USER_DIRECTED
```
