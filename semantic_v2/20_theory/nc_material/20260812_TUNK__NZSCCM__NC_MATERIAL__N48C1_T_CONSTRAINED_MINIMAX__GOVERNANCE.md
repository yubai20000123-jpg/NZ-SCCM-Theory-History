# GOVERNANCE DECISION — N48-C1 TENSILE MINIMAX BOUNDARY-LAYER REPAIR

**Date:** 2026-08-12

## 1. Frozen boundaries

```text
R10_MATERIAL_TARGET = FROZEN
MATERIAL_COMPILER_ORDER = 48
NEW_MATERIAL_MECHANISM = NO
ORDER_ESCALATION = NO
SWARTZ24_Pu_RECALCULATION = NO
STRUCTURAL_CALIBRATION = NO
FORMAL_SPATIAL_QUADRATURE = 0
```

This decision concerns only the near-zero value fidelity of the finite analytic representation.

## 2. Minimal compiler decision

Keep the previous N48-C1 representation for

```text
U
C
T^7
```

because their R10 near-zero boundary-layer value errors already passed the local diagnostic.

Only the tensile utilization primitive T is changed at the coefficient-generation level.

Final T form remains one degree-48 Chebyshev polynomial:

\[
T_{48}^{C1-MM}(\lambda)=\sum_{n=0}^{48}a_n^{(T,MM)}\mathcal C_n(\xi).
\]

Its coefficients are defined by the R10-only constrained minimax problem

\[
\min_{\mathbf a}
\|V(\lambda)\mathbf a-T_{R10}(\lambda)\|_{L^\infty([\lambda_a,\lambda_b])}
\]

subject to

\[
T_{48}^{C1-MM}(0)=0,
\qquad
(T_{48}^{C1-MM})'(0)=0.
\]

No experiment, Case load, root, Pu, or structural response enters this compiler problem.

## 3. Near-zero material boundary-layer definition

Use the existing R10 smoothing scale only:

\[
\mathcal B_\eta=
\{\lambda\ge0:\ 0\le \Pi_\eta(\lambda)\le\eta\}.
\]

No new material length or fitting parameter is introduced.

Across the 24 panel-specific material intervals,

\[
\lambda_\eta\approx3.42\times10^{-3},
\]

where \(\Pi_\eta(\lambda_\eta)=\eta\).

## 4. Passed gates

24-panel average T maximum absolute error over the complete compiler hull:

```text
direct N48                  ≈ 0.04981
N48-C1                      ≈ 0.12216
N48-C1 + T constrained MM   ≈ 0.08195
```

Thus the T minimax refinement reduces the N48-C1 full-hull T error by about 32.9%.

Over the narrow R10 boundary layer \(\mathcal B_\eta\):

```text
direct N48                  ≈ 0.04460
N48-C1                      ≈ 0.04089
N48-C1 + T constrained MM   ≈ 0.03728
```

Thus the strict-C1 near-zero T error is reduced by another 8.8% relative to N48-C1.

Exact C1 residuals remain approximately

```text
max |T(0)|      ≈ 1.42e-14
max |T'(0)|     ≈ 5.31e-14
```

Coefficient simplicity remains

```text
max |a_n^(T,MM)| ≈ 0.329
```

At the already frozen 24 theoretical states, without recalculating Pu:

```text
max |H_candidate/H_R10 - 1|                    ≈ 0.1386 %
mean |H_candidate/H_R10 - 1|                   ≈ 0.0459 %
max |ZhouMargin_candidate/ZhouMargin_R10 - 1|  ≈ 0.3872 %
mean |ZhouMargin_candidate/ZhouMargin_R10 - 1| ≈ 0.1394 %
```

Therefore:

```text
STRICT_R10_C1_ANCHOR_GATE = PASS
N48_NEAR_ZERO_T_VALUE_GATE = PASS
O1_COEFFICIENT_GATE = PASS
CAYLEY_HAMILTON_COMPATIBILITY = PASS
D15_COMPATIBILITY = PASS
ZHOU_Dx_Dy_H_GATE = PASS
```

## 5. Representation-capacity boundary

The constrained minimax audit also establishes an engineering representation boundary: with a single degree-48 polynomial and exact R10 C1 anchors, the old direct-N48 full-hull T value level is not fully recoverable.

```text
N48_STRICT_C1_FULL_HULL_DIRECT_VALUE_LEVEL = NOT_RECOVERED
```

This is recorded as an N48 representation-capacity limit, not as evidence that R10 material physics must be reopened.

## 6. Decision

```text
R10 = DO_NOT_REOPEN
N48_ORDER = 48
U_COMPILER = N48-C1
C_COMPILER = N48-C1
T7_COMPILER = N48-C1
T_COMPILER = N48-C1-CONSTRAINED-MINIMAX

NEAR_ZERO_T_VALUE_GATE = PASS
GLOBAL_DIRECT_N48_VALUE_LEVEL = NOT_FULLY_RECOVERED
SWARTZ24_Pu_RECALCULATION = NOT_PERFORMED
STRUCTURAL_CALIBRATION = NO
```

This completes the requested near-zero boundary-layer investigation. No further order escalation or material modification is authorized by this decision.