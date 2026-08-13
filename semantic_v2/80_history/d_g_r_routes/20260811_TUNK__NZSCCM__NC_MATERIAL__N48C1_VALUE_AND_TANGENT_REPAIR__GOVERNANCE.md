# GOVERNANCE DECISION — N48-C1 VALUE / FIRST-TANGENT REPAIR

**Date:** 2026-08-11

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

This decision concerns only the finite analytic representation layer between the frozen R10 material target and the Cayley-Hamilton/D15 structural algebra.

## 2. Candidate identity

The candidate is named:

```text
N48-C1 = SAME 49 CHEBYSHEV MATERIAL NODES
         + SAME DEGREE 48
         + HARD R10 VALUE/FIRST-DERIVATIVE ANCHORS AT lambda=0
         + MINIMUM NODAL L2 DISTURBANCE
```

For each

\[
F\in\{U,C,T,T^7\},
\]

let the old direct N48 coefficient vector be \(\mathbf a^{(0)}\), the 49-node Chebyshev matrix be \(V\), and

\[
H=V^TV=
\operatorname{diag}
\left(49,\frac{49}{2},\ldots,\frac{49}{2}\right).
\]

The value/derivative constraint matrix at \(\lambda=0\) is

\[
C=
\begin{bmatrix}
\mathcal C_0(\xi_0)&\cdots&\mathcal C_{48}(\xi_0)\\
\lambda_h^{-1}\mathcal C_0'(\xi_0)&\cdots&\lambda_h^{-1}\mathcal C_{48}'(\xi_0)
\end{bmatrix}.
\]

Target vectors are

\[
\mathbf d_U=(0,\kappa)^T,
\]

\[
\mathbf d_C=\mathbf d_T=\mathbf d_{T^7}=(0,0)^T.
\]

The unique minimum-disturbance correction is

\[
\boxed{
\mathbf a^{C1}
=
\mathbf a^{(0)}
+
H^{-1}C^T
(CH^{-1}C^T)^{-1}
(\mathbf d_F-C\mathbf a^{(0)}).
}
\]

Thus only a 2×2 matrix inverse is added per scalar material function.

## 3. Diagnostic gates

Across all 24 frozen panel-specific compiler intervals:

```text
R10_VALUE_ANCHOR_MAX_RESIDUAL          ≈ 3.0e-14      PASS
R10_FIRST_TANGENT_MAX_RESIDUAL         ≈ 3.0e-14      PASS
MAX_ABS_COEFFICIENT_DIRECT_N48          ≈ 0.62990
MAX_ABS_COEFFICIENT_N48_C1              ≈ 0.62976      PASS_SIMPLICITY
MEAN_L1_ALL_FUNCTION_COEFF_DIRECT        ≈ 6.272
MEAN_L1_ALL_FUNCTION_COEFF_N48_C1        ≈ 6.360       PASS_SIMPLICITY
```

At the 24 frozen theoretical ultimate states, using the Zhou/Navier directional tangent decomposition as an acceptance gate:

```text
max |(Eparallel_C1-Eparallel_R10)/E0|   ≈ 0.00689
max |H_C1/H_R10 - 1|                    ≈ 0.1386 %
mean |H_C1/H_R10 - 1|                   ≈ 0.0459 %
max |ZhouMargin_C1/ZhouMargin_R10 - 1|  ≈ 0.3872 %
mean |ZhouMargin_C1/ZhouMargin_R10 - 1| ≈ 0.1394 %
```

Therefore:

```text
R10_VALUE_ANCHOR_GATE = PASS
R10_FIRST_TANGENT_GATE = PASS
COEFFICIENT_MAGNITUDE_GATE = PASS
ZHOU_Dx_Dy_H_GATE = PASS
```

## 4. Value-fidelity hold

N48-C1 is not promoted to production because the global primitive value error, especially the narrow R10 tensile boundary layer near \(\lambda=0\), is worse than the old direct N48 interpolation.

24-panel mean maximum errors over each complete compiler hull:

| primitive | direct N48 | N48-C1 |
|---|---:|---:|
| U | 0.00110 | 0.00124 |
| C | 0.00499 | 0.01252 |
| T | 0.04979 | 0.12215 |
| T^7 | 0.11599 | 0.11706 |

This exposes a real representation trade-off: the old direct N48 obtains better near-zero T values partly by violating the exact R10 zero-slope identity; N48-C1 restores the exact first tangent but a single global degree-48 polynomial has difficulty resolving the very narrow R10 near-zero tensile boundary layer.

## 5. Decision

```text
N48_DIRECT_INTERPOLATION = HISTORICAL_VALUE_CLOSURE / TANGENT_FAIL
N48_C1 = PASS_TANGENT_DIAGNOSTIC
N48_C1_PRODUCTION = HOLD
GLOBAL_PRIMITIVE_VALUE_GATE = HOLD
R10 = DO_NOT_REOPEN
N96_N112_ESCALATION = NOT_AUTHORIZED
SWARTZ24_RECALCULATION = NOT_AUTHORIZED
```

The next task is restricted to finding whether the near-zero R10 tensile boundary-layer value error can be reduced while retaining all of the following simultaneously:

```text
ONE GLOBAL N48-LEVEL ANALYTIC REPRESENTATION
O(1) COEFFICIENTS
EXACT R10 VALUE/FIRST-DERIVATIVE ANCHORS
CAYLEY-HAMILTON COMPATIBILITY
D15 COMPATIBILITY
ZHOU Dx-Dy-H GATE
NO NEW MATERIAL PHYSICS
NO STRUCTURAL CALIBRATION
```

If that cannot be achieved at N48-level complexity, the project must explicitly record the representation-capacity boundary rather than silently escalating polynomial order.
