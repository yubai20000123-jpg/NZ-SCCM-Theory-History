# GOVERNANCE DECISION — R10 → N48 → D15 PAPER-STYLE THEORY EXPRESSION

**Date:** 2026-08-11 16:38 +08:00

## Decision

The paper-style derivation in

- `current/theory/NZ_SCCM_R10_N48_D15_PAPER_STYLE_DERIVATION_20260811.md`

is accepted as the governing explanatory form for the current ordinary-concrete analytic chain.

The theory shall be presented as

```text
material parameters
-> closed Foster/R10 scalar formulas
-> SAME multidimensional current map
-> one N48 coefficient formula
-> Cayley-Hamilton finite matrix recurrence
-> finite complete-halfwave coefficient field
-> D15 exact moment contraction
```

The following identities are frozen:

```text
MATERIAL_THEORY = CLOSED_R10_PARAMETER_FORMULA
MATERIAL_COMPILER_ORDER = 48
CHEBYSHEV_COEFFICIENTS = DERIVED_COMPILER_QUANTITIES
LONG_DECIMAL_COEFFICIENT_LIST_IN_THEORY = PROHIBITED
N112_REQUIREMENT = SUPERSEDED
CASE21_NUMERICAL_RECLOSURE_IN_THIS_STEP = NO
ZERO_SPATIAL_D15 = RETAINED
```

## Required paper-style notation

For every major equation group, parameters must be defined in `式中，...表示...` form or an equivalent symbol table.

Long decimal substitutions are not to replace transparent symbolic combinations when a closed parameter form exists. Examples include

\[
10h-6\rho,\qquad 8\rho-15h,\qquad 6h-3\rho,
\]

rather than their decimal evaluations.

The 49 N48 material coefficients are defined by one general expression,

\[
a_n^{(F)}=
\frac{2-\delta_{n0}}{49}
\sum_{j=0}^{48}F(\lambda_j)\cos(n\theta_j),
\qquad F\in\{U,C,T,T^7\},
\]

and are not individual constitutive parameters.

The term-by-term analytic chain is

\[
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
c_{ijk}M_iM_jZ_k.
\]

This is the governing explanation of how a closed material term enters D15.

## Scope boundary

This decision authorizes theory presentation only. It does not authorize:

- Case21 numerical solution;
- compiler-order escalation;
- material-law replacement;
- structural calibration;
- Swartz24 calculation.

The next action remains user-directed.