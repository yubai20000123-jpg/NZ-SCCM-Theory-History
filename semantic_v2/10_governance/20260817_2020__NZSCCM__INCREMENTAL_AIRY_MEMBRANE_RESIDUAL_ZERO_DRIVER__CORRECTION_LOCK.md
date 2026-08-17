# NZ-SCCM — Incremental Airy membrane residual / zero-driver correction lock

**Timestamp:** 2026-08-17 20:20 +08:00  
**Identity:** CANONICAL IMPLEMENTATION CORRECTION / NO NEW THEORY BRANCH  
**Parent:** `20260817_1824__NZSCCM__ZERO_SPATIAL_DISCRETIZATION_FINITE_CURRENT_TRUE_INFINITE_D15__CANONICAL_LOCK.md`

## 1. Purpose

The accepted structural identity is

```text
CURRENT THEORY
= HISTORICAL ACCEPTED NGUYEN/VON-KARMAN BACKBONE
+ POSTBUCKLING MEMBRANE-STRESS REDISTRIBUTION DELTA
```

The Airy internal coordinate is therefore an **incremental redistribution coordinate**. It is not allowed to relax the pre-buckling steel/concrete Poisson mismatch or to redefine the historical backbone at `q=0`.

## 2. Governing correction

Let

\[
\alpha=\lambda_A M,
\qquad
M={\pi^2\over\varepsilon_0}\left(q_0q+{q^2\over2}\right),
\]

and let `B_A` be the same compatible Airy/FvK strain direction already frozen in the current theory.

The total Airy generalized residual

\[
R_A^{tot}(D,q,\alpha)
=\int_V \boldsymbol\sigma(D,q,\alpha):B_A\,dV
\]

is **not** the membrane-delta closure for a multiphase composite plate, because at `q=0, alpha=0` different phase Poisson responses can give a non-zero generalized work.

The production membrane-delta residual is therefore locked as

\[
\boxed{
R_A^{\Delta}(D,q,\alpha)
=R_A^{tot}(D,q,\alpha)-R_A^{tot}(D,0,0)=0
}
\]

or equivalently

\[
\boxed{
R_A^{\Delta}
=\int_V
[\boldsymbol\sigma(D,q,\alpha)-\boldsymbol\sigma(D,0,0)]
:B_A\,dV=0.
}
\]

All material phases present in the current state are also present in the reference state. No phase is added after the solve.

## 3. Mandatory degeneration

By construction,

\[
q=0,\quad M=0,\quad\alpha=0
\quad\Longrightarrow\quad
R_A^{\Delta}=0.
\]

Hence

\[
\boxed{
q\to0\Rightarrow M\to0\Rightarrow\Delta\varepsilon_{mem}\to0
}
\]

and the accepted historical backbone is recovered exactly.

The membrane coordinate is prohibited from creating a finite correction at zero geometric membrane driver by allowing `lambda_A` to diverge.

## 4. Elastic Airy/FvK regression

For a homogeneous isotropic linear-elastic square complete halfwave, the classical compatible redistribution is recovered at

\[
\boxed{\alpha=M},\qquad \boxed{\lambda_A=1}.
\]

An independent direct-continuum audit of the corrected incremental residual gives `alpha/M = 1.000000000000` to numerical roundoff for representative small finite `q` values. This is an audit oracle only; it does not change the formal integration identity.

## 5. Structural equations

The complete nonlinear structural solve remains

\[
R_q(D,q,\alpha)=0,
\qquad
R_A^{\Delta}(D,q,\alpha)=0,
\]

on the branch connected continuously to

\[
D=0,\quad q=0,\quad\alpha=0,
\]

followed by the first reachable limit point of

\[
P(D,q,\alpha).
\]

Equivalently, after condensation of `(q,alpha)`, the first reachable point with `dP/dD=0` is the ultimate point. No comparator load is used for branch or root selection.

## 6. Formal analytic identity unchanged

For every current/reference stress target separately:

```text
finite current material operator
-> true-infinite analytic representation
-> exact 2x2 Cayley-Hamilton recurrence
-> General-D15 exact moments
-> true-infinite target sum
```

Then the two exact generalized Airy works are subtracted. The subtraction does not introduce spatial discretization.

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

Any direct-current/Gauss evaluation used to locate or independently audit decimal roots remains `AUDIT_ONLY` and never becomes the formal structural integral.

## 7. Per-specimen production discipline for Z0–Z5

For the immediately authorized Z0–Z5 recalculation:

1. each specimen starts from its own raw input;
2. each specimen creates a fresh material/structural state;
3. no root, branch state, series prefix, internal coordinate, convergence state, or intermediate result is inherited from another specimen;
4. membrane-OFF is solved independently for the exact same specimen;
5. membrane-ON is then solved independently from the origin with `R_A^Delta=0`;
6. low-load `alpha/M -> 1` is audited where the homogeneous elastic limit is applicable;
7. first reachable limit point is frozen before reading Zhou/Winter comparators;
8. only after all six independent solves pass may a cross-specimen summary table be assembled.

## 8. Prohibitions retained

```text
NO spatial Gauss/Simpson/adaptive quadrature in formal operator
NO spatial cells/collocation/material-point grids
NO experimental/Zhou/Winter root selection or calibration
NO shared root continuation across specimens
NO batch surrogate or cross-case interpolation
NO finite-order material model substitution for the true-infinite formal representation
```
