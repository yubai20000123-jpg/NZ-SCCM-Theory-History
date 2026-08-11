# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-12 02:18 +08:00  
**Purpose:** 唯一当前工作入口；只保留当前有效状态、canonical evidence 和下一门禁。

## 0. Highest-priority contract

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
ACTIVE_MODE = m=1
KINEMATICS = NGUYEN_SECOND_ORDER
STABILITY_BACKBONE = ZHOU_NAVIER_TANGENT_STABILITY
EXACT_MOMENT_ENGINE = D15
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
STRUCTURAL_CALIBRATION = NO
```

Formal production prohibits spatial Gauss/Simpson/adaptive quadrature, spatial Chebyshev collocation, material-point grids/cells, whole-structure P/R fitting and experiment-driven material tuning.

---

## 1. Governing material target — R10 FROZEN

```text
source Foster current relation
-> R10 1D energy-smoothed tensile scalar
-> SAME U/C/T + CC/TC/TT multidimensional current map
```

Core identities remain

\[
\kappa=\frac{E_0\varepsilon_0}{f_c},\qquad
x_{cr}=\frac{\rho}{\kappa},\qquad \rho=0.1,
\]

\[
h=\frac15\left(\frac{W_{src}}{x_{cr}}-\frac{\rho}{10}-\frac92u_r\right).
\]

Exact zero-state anchors:

\[
U(0)=0,\quad U'(0)=\kappa,
\]

\[
C(0)=T(0)=T^7(0)=0,
\]

\[
C'(0)=T'(0)=(T^7)'(0)=0.
\]

```text
R10_MATERIAL_TARGET = GOVERNING_AND_UNCHANGED
NEW_MATERIAL_MECHANISM = NOT_AUTHORIZED
```

---

## 2. Current N48 compiler identity

\[
\boxed{N_M=48}.
\]

```text
U_COMPILER  = N48-C1
C_COMPILER  = N48-C1
T7_COMPILER = N48-C1
T_COMPILER  = N48-C1-CONSTRAINED-MINIMAX
```

For \(F\in\{U,C,T^7\}\), first generate the direct Chebyshev-root coefficients

\[
a_n^{(F,0)}=
\frac{2-\delta_{n0}}{49}
\sum_{j=0}^{48}F(\lambda_j)\cos(n\theta_j),
\]

then enforce the strict-C1 anchors by

\[
\boxed{
\mathbf a^{(F,C1)}
=
\mathbf a^{(F,0)}
+
\mathbf H^{-1}\mathbf G^T
(\mathbf G\mathbf H^{-1}\mathbf G^T)^{-1}
(\mathbf d_F-\mathbf G\mathbf a^{(F,0)}).
}
\]

For \(T\), use the degree-48 strict-C1 constrained minimax solution over the full compiler interval.

Current compiler gates:

```text
R10_VALUE_ANCHOR_GATE = PASS
R10_FIRST_TANGENT_GATE = PASS
N48_NEAR_ZERO_T_VALUE_GATE = PASS
O1_COEFFICIENT_GATE = PASS
CAYLEY_HAMILTON_COMPATIBILITY = PASS
D15_COMPATIBILITY = PASS
ZHOU_Dx_Dy_H_GATE = PASS
N48_STRICT_C1_FULL_HULL_DIRECT_VALUE_LEVEL = NOT_FULLY_RECOVERED
```

The last item is a degree-48 representation-capacity boundary, not authorization to reopen R10 or raise polynomial order.

Canonical compiler audits:

- `current/audits/NZ_SCCM_N48_C1_VALUE_TANGENT_REPAIR_AUDIT_20260811.md`
- `current/audits/NZ_SCCM_N48_C1_TENSILE_MINIMAX_BOUNDARY_LAYER_AUDIT_20260812.md`
- `governance/N48_C1_VALUE_TANGENT_REPAIR_DECISION_20260811.md`
- `governance/N48_C1_TENSILE_MINIMAX_BOUNDARY_LAYER_DECISION_20260812.md`

---

## 3. Canonical updated paper-style derivations — COMPLETE

Current theory files:

- `current/theory/NZ_SCCM_R10_N48C1MM_D15_PAPER_STYLE_DERIVATION_20260812.md`
- `current/theory/NZ_SCCM_R10_N48C1MM_D15_EQUATION_BY_EQUATION_DERIVATION_20260812.md`
- `governance/R10_N48C1MM_D15_PAPER_STYLE_DERIVATION_DECISION_20260812.md`

The equation-by-equation file contains the full material-parameter -> R10 -> N48-C1/MM -> Cayley-Hamilton -> Nguyen -> D15 -> P/Rq/L -> Zhou Dx-Dy-H chain with paper-style symbol definitions.

```text
UPDATED_PAPER_STYLE_DERIVATION = COMPLETE
EQUATION_BY_EQUATION_DERIVATION = COMPLETE
SYMBOL_DEFINITIONS = COMPLETE
```

---

## 4. Updated Case21 fresh N48-C1/MM + D15 closure — COMPLETE

This calculation was executed fresh under the updated compiler. It did not load or use historical Case21 calculated loads, historical Case21 roots, historical load paths, historical FE/Gauss results, or the experimental failure load during the solve.

Canonical evidence:

- `current/results/NZ_SCCM_CASE21_N48C1MM_D15_FRESH_BLIND_RESULT_20260812.md`
- `current/results/NZ_SCCM_CASE21_N48C1MM_D15_FRESH_COEFFICIENTS_20260812.csv`
- `current/results/NZ_SCCM_CASE21_N48C1MM_D15_FRESH_FULL_CALCULATION_20260812.md`
- `current/results/NZ_SCCM_CASE21_N48C1MM_D15_FRESH_THEORY_VS_EXPERIMENT_20260812.md`
- `current/workflows/NZ_SCCM_CASE21_N48C1MM_D15_BLIND_AUDIT_INPUT_20260812.md`
- `current/workflows/NZ_SCCM_CASE21_N48C1MM_D15_BLIND_AUDIT_PROMPT_20260812.txt`
- `governance/CASE21_N48C1MM_D15_FRESH_CLOSURE_DECISION_20260812.md`

Repository ordering freezes the blind theory result before the experiment-comparison file.

Fresh source inputs:

\[
b=\ell=1220\ {\rm mm},\quad t_p=19.30\ {\rm mm},
\]

\[
f_c=21.23\ {\rm MPa},\quad E_0=20321\ {\rm MPa},\quad
\varepsilon_0=0.00209,\quad \nu=0.18,
\]

\[
q_0=1/400.
\]

The fresh compiler interval was fixed before solving as

\[
\boxed{\lambda\in[-1.15,0.12]}.
\]

The final continuous spectral certificate is

\[
-0.874981134\le\lambda\le0.092641134,
\]

and the final steel certificate is

\[
\max|\varepsilon_s|=0.001635091<0.00265.
\]

Fresh blind theoretical state:

\[
D_u\approx0.78234,\qquad q_u\approx0.00177047,
\]

\[
\boxed{P_{u,th}\approx365.61\ {\rm kN}}.
\]

Engineering residuals:

\[
\frac{|R_q|}{|R_{q,c}|+|R_{q,s}|}
\approx2.27\times10^{-5},
\]

\[
L_{norm}\approx-2.35\times10^{-4},
\]

\[
(dP/dD)_{R_q=0}\approx-0.06805\ {\rm kN}.
\]

Only after the blind result was frozen was the experimental failure load attached:

\[
P_{f,exp}=82.8\ {\rm kip}=368.312750\ {\rm kN}.
\]

Thus

\[
\boxed{\text{signed error}\approx-0.734\%}.
\]

```text
CASE21_N48C1MM_D15_FRESH_BLIND = PASS_ENGINEERING
HISTORICAL_CASE21_COMPUTED_VALUES_USED = NO
HISTORICAL_CASE21_ROOTS_OR_PATHS_USED = NO
HISTORICAL_GAUSS_HISTORY_USED = NO
EXPERIMENT_USED_DURING_SOLVE = NO
FORMAL_SPATIAL_QUADRATURE = 0
CONTINUOUS_SPECTRAL_CERTIFICATE = PASS
STEEL_BRANCH = ELASTIC
Rq_EQUILIBRIUM = PASS_ENGINEERING
LIMIT_L = PASS_ENGINEERING
EXPERIMENT_COMPARISON_AFTER_BLIND_FREEZE = COMPLETE
```

The backend may use FFT only to accelerate finite analytic coefficient convolution; no physical-space FFT/collocation points are used. D15 exact moments remain the formal spatial integration identity.

---

## 5. Earlier completed structural records remain preserved

```text
EARLIER_CASE21_DIRECT_N48_VALUE_CLOSURE = PRESERVED_HISTORICAL_RECORD
SWARTZ24_FRESH_BLIND_VALUE_CLOSURE = 24/24 PRESERVED_RECORD
SWARTZ24_PRIMARY_MECHANISM_AUDIT = COMPLETE
```

They are not inputs to the fresh updated Case21 closure and are not silently overwritten.

---

## 6. Current execution boundary

Do not automatically:

- reopen R10;
- add a new material mechanism;
- raise to N96/N112;
- overwrite earlier Case21/Swartz24 records;
- use experiments to tune compiler coefficients;
- automatically recalculate the full Swartz24 series without user instruction.

```text
R10 = FROZEN
N48_ORDER = 48
UPDATED_N48_C1_MM_D15_DERIVATION = CANONICAL
CASE21_N48C1MM_D15_FRESH_CLOSURE = COMPLETE
CURRENT_NEXT_TASK = USER_DIRECTED
```
