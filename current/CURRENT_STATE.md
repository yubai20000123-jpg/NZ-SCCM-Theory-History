# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-12 01:01 +08:00  
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

## 2. Direct N48 record and P1 tangent diagnosis

The completed Case21 and Swartz24 blind value-closure records used the historical/current direct N48 representation. They remain preserved and are not silently overwritten.

P1 showed:

```text
N48_DIRECT_VALUE_CLOSURE_RECORD = PRESERVED
N48_DIRECT_TANGENT_FIDELITY = FAIL_DIAGNOSTIC
FIRST_CLEAR_DEVIATION = R10_TARGET -> N48_FIRST_DERIVATIVE
```

Canonical files:

- `current/results/NZ_SCCM_SWARTZ24_P1_CURRENT_TANGENT_AUDIT_20260811.md`
- `governance/P1_N48_TANGENT_FIDELITY_DECISION_20260811.md`

---

## 3. N48-C1 base repair — tangent PASS

N48-C1 keeps degree 48 and uses hard R10 value/first-derivative anchors at \(\lambda=0\). It passed:

```text
R10_VALUE_ANCHOR_GATE = PASS
R10_FIRST_TANGENT_GATE = PASS
COEFFICIENT_MAGNITUDE_GATE = PASS
ZHOU_Dx_Dy_H_GATE = PASS
```

At the frozen 24 theoretical states:

```text
max |H_C1/H_R10 - 1|                    ≈ 0.1386 %
mean |H_C1/H_R10 - 1|                   ≈ 0.0459 %
max |ZhouMargin_C1/ZhouMargin_R10 - 1|  ≈ 0.3872 %
mean |ZhouMargin_C1/ZhouMargin_R10 - 1| ≈ 0.1394 %
```

Canonical files:

- `current/audits/NZ_SCCM_N48_C1_VALUE_TANGENT_REPAIR_AUDIT_20260811.md`
- `governance/N48_C1_VALUE_TANGENT_REPAIR_DECISION_20260811.md`

---

## 4. Near-zero R10 tensile boundary layer — CLOSED AT N48 LEVEL

Canonical files:

- `current/audits/NZ_SCCM_N48_C1_TENSILE_MINIMAX_BOUNDARY_LAYER_AUDIT_20260812.md`
- `current/audits/NZ_SCCM_N48_C1_TENSILE_MINIMAX_BOUNDARY_LAYER_AUDIT_20260812.csv`
- `governance/N48_C1_TENSILE_MINIMAX_BOUNDARY_LAYER_DECISION_20260812.md`

Use the existing R10 smoothing scale only:

\[
\mathcal B_\eta=\{\lambda\ge0:\ 0\le\Pi_\eta(\lambda)\le\eta\}.
\]

Across the 24 material intervals,

\[
\lambda_\eta\approx3.42\times10^{-3}.
\]

Only the T primitive required further value repair. The minimal accepted compiler identity is therefore:

```text
U_COMPILER = N48-C1
C_COMPILER = N48-C1
T7_COMPILER = N48-C1
T_COMPILER = N48-C1-CONSTRAINED-MINIMAX
```

The T representation remains one degree-48 Chebyshev polynomial and satisfies

\[
T_{48}(0)=0,\qquad T'_{48}(0)=0.
\]

24-panel T maximum-error averages:

| Region / compiler | direct N48 | N48-C1 | N48-C1 + T minimax |
|---|---:|---:|---:|
| complete compiler hull | 0.04981 | 0.12216 | 0.08195 |
| near-zero \(\mathcal B_\eta\) | 0.04460 | 0.04089 | 0.03728 |

Thus the T minimax refinement reduces the N48-C1 full-hull T error by about 32.9% and the near-zero boundary-layer error by another 8.8%.

Coefficient and compatibility gates:

```text
max |a_n^(T,MM)| ≈ 0.329                     PASS_O1
max |T(0)| residual ≈ 1.42e-14               PASS
max |T'(0)| residual ≈ 5.31e-14              PASS
CAYLEY_HAMILTON_COMPATIBILITY = PASS
D15_COMPATIBILITY = PASS
FORMAL_SPATIAL_QUADRATURE = 0
```

Zhou/Navier gate remains at essentially the N48-C1 level:

```text
max |H_candidate/H_R10 - 1|                    ≈ 0.1386 %
mean |H_candidate/H_R10 - 1|                   ≈ 0.0459 %
max |ZhouMargin_candidate/ZhouMargin_R10 - 1|  ≈ 0.3872 %
mean |ZhouMargin_candidate/ZhouMargin_R10 - 1| ≈ 0.1394 %
```

Decision:

```text
N48_NEAR_ZERO_T_VALUE_GATE = PASS
N48_STRICT_C1_FULL_HULL_DIRECT_VALUE_LEVEL = NOT_RECOVERED
```

The latter is recorded as an N48 representation-capacity boundary, not a reason to reopen R10 or raise the polynomial order.

---

## 5. Completed structural records remain frozen

```text
CASE21_VALUE_CLOSURE = COMPLETE_RECORD
SWARTZ24_FRESH_BLIND_VALUE_CLOSURE = 24/24 COMPLETE_RECORD
SWARTZ24_PRIMARY_MECHANISM_AUDIT = COMPLETE
HISTORICAL_CASE_ROOTS_OR_LOADS_USED = NO
EXPERIMENT_USED_IN_SOLVE = NO
```

No structural result was recalculated in the 2026-08-12 boundary-layer step.

```text
SWARTZ24_Pu_RECALCULATION = NOT_PERFORMED
CASE21_RECALCULATION = NOT_PERFORMED
```

---

## 6. Current execution boundary

The requested N48 near-zero boundary-layer investigation is complete.

Do not automatically:

- reopen R10;
- add a new material mechanism;
- raise to N96/N112;
- overwrite previous Case21/Swartz24 records;
- use experiments to tune compiler coefficients.

```text
CURRENT_NEXT_TASK = USER_DIRECTED
```
