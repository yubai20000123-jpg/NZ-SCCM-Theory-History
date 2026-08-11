# GOVERNANCE DECISION — UPDATED R10 → N48-C1/MM → D15 PAPER-STYLE DERIVATION

**Date:** 2026-08-12

## Decision

The canonical paper-style derivation is now:

- `current/theory/NZ_SCCM_R10_N48C1MM_D15_PAPER_STYLE_DERIVATION_20260812.md`

It supersedes the earlier direct-N48 paper-style derivation **for explanatory/theory-writing purposes only**. Historical Case21 and Swartz24 value-closure records are preserved and are not silently recalculated.

## Governing chain

```text
material parameters
-> frozen closed R10 current operator
-> primitives {U,C,T,T^7}
-> degree-48 analytic compiler
   U/C/T^7 = N48-C1
   T       = N48-C1-CONSTRAINED-MINIMAX
-> Cayley-Hamilton 2D lift
-> current stress / same-expression tangent
-> D15 complete-halfwave exact moments
-> Zhou Dx-Dy-H tangent-stability acceptance gate
```

## Frozen boundaries

```text
R10_MATERIAL_TARGET = FROZEN
MATERIAL_COMPILER_ORDER = 48
NEW_MATERIAL_MECHANISM = NO
ORDER_ESCALATION = NO
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_SPATIAL_SAMPLING = 0
FORMAL_SPATIAL_SUBDOMAINS = 1_COMPLETE_HALFWAVE
STRUCTURAL_CALIBRATION = NO
SWARTZ24_Pu_RECALCULATION = NO
```

## Coefficient identity

For all primitives, the direct Chebyshev-root coefficients remain the base formula

\[
a_n^{(F,0)}=
\frac{2-\delta_{n0}}{49}
\sum_{j=0}^{48}F(\lambda_j)\cos(n\theta_j).
\]

For \(F\in\{U,C,T^7\}\), production-candidate coefficients use the explicit C1 minimum-disturbance correction

\[
\mathbf a^{(F,C1)}
=
\mathbf a^{(F,0)}
+
\mathbf H^{-1}\mathbf G^T
(\mathbf G\mathbf H^{-1}\mathbf G^T)^{-1}
(\mathbf d_F-\mathbf G\mathbf a^{(F,0)}).
\]

For \(T\), the governing updated coefficient identity is the degree-48 strict-C1 constrained minimax definition over the full compiler hull.

## D15 term identity

Each material coefficient enters D15 through

\[
\mathscr D[F_{ab}^{(n)}]
=
a_n^{(F,*)}
\sum_{i,j,k}
\phi_{ijk,ab}^{(F,n)}M_iM_jZ_k.
\]

Thus the canonical chain is

\[
\boxed{
\text{R10}
\to a_n^{(F,*)}
\to(A_n,B_n)
\to\mathbf F_{48}^{(n)}
\to\mathbf S
\to c_{ijk}
\to c_{ijk}M_iM_jZ_k.
}
\]

## Status

```text
UPDATED_PAPER_STYLE_DERIVATION = COMPLETE
SYMBOL_DEFINITIONS = COMPLETE
R10_REOPEN = NO
N48_ORDER = 48
NEAR_ZERO_T_VALUE_GATE = PASS
ZHOU_Dx_Dy_H_GATE = PASS
CURRENT_NEXT_TASK = USER_DIRECTED
```
