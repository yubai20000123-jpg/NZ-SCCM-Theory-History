# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-11 23:55 +08:00  
**Purpose:** 唯一当前工作入口；只保留当前有效状态和下一门禁，详细过程由 canonical files 承担。

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

Formal production continues to prohibit spatial Gauss/Simpson/adaptive quadrature, spatial Chebyshev collocation, material-point grids/cells, whole-structure P/R fitting and experiment-driven material tuning.

---

## 1. Governing material target — R10 FROZEN

```text
source Foster current relation
-> R10 1D energy-smoothed tensile scalar
-> SAME U/C/T + CC/TC/TT multidimensional current map
```

Core identities:

\[
\kappa=\frac{E_0\varepsilon_0}{f_c},\qquad
x_{cr}=\frac{\rho}{\kappa},\qquad \rho=0.1,
\]

\[
W_{src}=\rho x_{cr}\int_0^{10}T_{src}(r)dr,
\]

\[
h=\frac15\left(\frac{W_{src}}{x_{cr}}-\frac{\rho}{10}-\frac92u_r\right).
\]

Exact R10 zero-state anchors used by the current compiler audit:

\[
U(0)=0,\qquad U'(0)=\kappa,
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

## 2. Direct N48 — completed value-closure representation; tangent FAIL diagnostic

Historical/current completed calculations used

\[
F_{48}(\lambda)=\sum_{n=0}^{48}a_n^{(F)}\mathcal C_n(\xi),
\qquad F\in\{U,C,T,T^7\},
\]

with the 49 Chebyshev material roots

\[
\theta_j=\frac{(j+\tfrac12)\pi}{49},\qquad
\lambda_j=\lambda_c+\lambda_h\cos\theta_j.
\]

The fresh Case21 and Swartz24 blind results remain preserved as completed **value-closure records**. They are not silently overwritten.

P1 showed that direct N48 does not preserve the exact R10 first-derivative identity at \(\lambda=0\); in particular \(T'_{48}(0)\) was approximately 8.7–11.4 instead of zero and the Zhou-form \(H\) stiffness was inflated by about 4.7–6.8 times.

Canonical P1 files:

- `current/results/NZ_SCCM_SWARTZ24_P1_CURRENT_TANGENT_AUDIT_20260811.md`
- `current/results/NZ_SCCM_SWARTZ24_P1_CURRENT_TANGENT_AUDIT_COMPACT_20260811.csv`
- `evidence/literature/NZ_SCCM_ZHOU_ATTARD_TANGENT_STABILITY_INTERPRETATION_20260811.md`
- `governance/P1_N48_TANGENT_FIDELITY_DECISION_20260811.md`

```text
N48_DIRECT_VALUE_CLOSURE_RECORD = PRESERVED
N48_DIRECT_TANGENT_FIDELITY = FAIL_DIAGNOSTIC
FIRST_CLEAR_DEVIATION = R10_TARGET -> N48_FIRST_DERIVATIVE
```

---

## 3. N48-C1 — simplest value/first-tangent constrained repair candidate

Canonical files:

- `current/audits/NZ_SCCM_N48_C1_VALUE_TANGENT_REPAIR_AUDIT_20260811.md`
- `current/audits/NZ_SCCM_N48_C1_VALUE_TANGENT_REPAIR_AUDIT_TABLE_20260811.csv`
- `governance/N48_C1_VALUE_TANGENT_REPAIR_DECISION_20260811.md`

N48-C1 keeps:

```text
MATERIAL_COMPILER_ORDER = 48
MATERIAL_COORDINATE_NODES = SAME_49_CHEBYSHEV_ROOTS
R10 = UNCHANGED
NEW_MATERIAL_PARAMETER = NONE
EXPERIMENT_IN_COMPILER = NO
```

For each \(F\in\{U,C,T,T^7\}\), define the old direct coefficient vector \(\mathbf a^{(0)}\), the 49-node matrix \(V\), and the value/first-derivative constraint matrix \(C\) at \(\lambda=0\). Since

\[
H=V^TV=
\operatorname{diag}\left(49,\frac{49}{2},\ldots,\frac{49}{2}\right),
\]

N48-C1 is the explicit minimum-nodal-disturbance correction

\[
\boxed{
\mathbf a^{C1}
=
\mathbf a^{(0)}
+
H^{-1}C^T(CH^{-1}C^T)^{-1}
(\mathbf d_F-C\mathbf a^{(0)}).
}
\]

with

\[
\mathbf d_U=(0,\kappa)^T,
\qquad
\mathbf d_C=\mathbf d_T=\mathbf d_{T^7}=(0,0)^T.
\]

Thus each material function adds only a \(2\times2\) correction solve.

### 3.1 Passed gates

Across the 24 panel-specific compiler intervals:

```text
R10_VALUE_ANCHOR_MAX_RESIDUAL          ≈ 3.0e-14    PASS
R10_FIRST_TANGENT_MAX_RESIDUAL         ≈ 3.0e-14    PASS
MAX_ABS_COEFFICIENT_DIRECT_N48          ≈ 0.62990
MAX_ABS_COEFFICIENT_N48_C1              ≈ 0.62976   PASS
```

At the 24 frozen theoretical ultimate states, using Zhou/Navier directional stiffness as the stability acceptance gate:

```text
max |(Eparallel_C1-Eparallel_R10)/E0|   ≈ 0.00689
max |H_C1/H_R10 - 1|                    ≈ 0.1386 %
mean |H_C1/H_R10 - 1|                   ≈ 0.0459 %
max |ZhouMargin_C1/ZhouMargin_R10 - 1|  ≈ 0.3872 %
mean |ZhouMargin_C1/ZhouMargin_R10 - 1| ≈ 0.1394 %
```

Group mean loaded-direction tangent ratios:

| Group | R10 target | direct N48 | N48-C1 |
|---|---:|---:|---:|
| Case1–8 | -0.0195 | 0.9928 | -0.0188 |
| Case9–16 | -0.0360 | 0.9362 | -0.0337 |
| Case17–24 | +0.0599 | 0.9659 | +0.0591 |

Therefore:

```text
R10_VALUE_ANCHOR_GATE = PASS
R10_FIRST_TANGENT_GATE = PASS
COEFFICIENT_MAGNITUDE_GATE = PASS
ZHOU_Dx_Dy_H_GATE = PASS
```

### 3.2 Remaining hold — near-zero R10 tensile boundary layer

The global primitive value fidelity is not yet promoted to production. Mean maximum errors over the complete compiler hull are:

| primitive | direct N48 | N48-C1 |
|---|---:|---:|
| U | 0.00110 | 0.00124 |
| C | 0.00499 | 0.01252 |
| T | 0.04979 | 0.12215 |
| T^7 | 0.11599 | 0.11706 |

The main trade-off is the very narrow R10 tensile boundary layer near \(\lambda=0\): exact R10 requires \(T'(0)=0\), while the old direct N48 obtained better nearby T values partly by using a false slope of approximately 9–11.

```text
N48_C1_TANGENT_DIAGNOSTIC = PASS
GLOBAL_PRIMITIVE_VALUE_GATE = HOLD
N48_C1_PRODUCTION = HOLD
```

N48-C1 is therefore the current **simplest constrained candidate**, not yet the production replacement.

---

## 4. Completed calculation and validation records remain frozen

Canonical calculation records:

- `current/theory/NZ_SCCM_R10_N48_D15_PAPER_STYLE_DERIVATION_20260811.md`
- `current/theory/NZ_SCCM_CASE21_FRESH_R10_N48_D15_CLOSURE_20260811.md`
- `current/workflows/NZ_SCCM_CASE21_CALCULATION_PROCESS_TEMPLATE_V1_20260811.md`
- `current/results/NZ_SCCM_SWARTZ24_FRESH_BLIND_THEORY_RESULTS_20260811.csv`
- `current/results/NZ_SCCM_SWARTZ24_FRESH_THEORY_VS_EXPERIMENT_20260811.csv`
- `current/results/NZ_SCCM_SWARTZ24_PRIMARY_MECHANISM_AUDIT_20260811.md`

```text
CASE21_VALUE_CLOSURE = COMPLETE_RECORD
SWARTZ24_FRESH_BLIND_VALUE_CLOSURE = 24/24 COMPLETE_RECORD
SWARTZ24_PRIMARY_MECHANISM_AUDIT = COMPLETE
HISTORICAL_CASE_ROOTS_OR_LOADS_USED = NO
EXPERIMENT_USED_IN_SOLVE = NO
```

No current compiler repair is allowed to use those structural values as fitting targets.

---

## 5. Current next gate

The next task remains deliberately narrow:

\[
\boxed{
\text{within N48-level complexity, reduce the }\lambda\approx0\text{ R10 tensile boundary-layer value error without losing exact C1 anchors, O(1) coefficients, Cayley-Hamilton/D15 compatibility, or Zhou }D_x-D_y-H\text{ fidelity.}
}
\]

Do not yet:

- reopen R10;
- add a new material mechanism;
- raise to N96/N112;
- recalculate Swartz24 \(P_u\);
- tune coefficients from experiments.

```text
CURRENT_NEXT_TASK = N48_NEAR_ZERO_VALUE_FIDELITY_WITH_C1_ANCHORS
```
