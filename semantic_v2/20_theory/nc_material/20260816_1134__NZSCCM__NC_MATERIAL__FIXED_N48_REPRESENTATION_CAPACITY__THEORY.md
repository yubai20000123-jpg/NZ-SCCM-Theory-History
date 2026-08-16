# NZ-SCCM NC material — fixed-N48 representation-capacity audit theory

**Timestamp:** 2026-08-16 11:34 +08:00  
**Identity:** SOURCE-OPERATOR REPRESENTATION CAPACITY / ORDER FIXED AT 48

## 1. Frozen source

The physical material law is the already-frozen R10 current operator. No material parameter or multiaxial interaction coefficient is changed.

For the scalar principal coordinate `lambda`, R10 uses

\[
c=\Pi_\eta(-\lambda),\qquad t=\Pi_\eta(\lambda),
\]

\[
C=\frac{\kappa c}{1+(\kappa-2)c+c^2},
\]

with the frozen C2 energy-smoothed tensile scalar `u_R(t)` and

\[
T=u_R(t)/\rho,
\qquad
U=\kappa\lambda-C+\kappa c+u_R(t)-\kappa t.
\]

The R10 two-principal-value spectral scalar is retained as

\[
s_i=U_i-a_{cc}C_i^2C_j+C_iT_j-\rho a_t T_iT_j^8.
\]

Nothing in this gate changes those equations.

## 2. Fixed N48 admissible approximation space

For every primitive

\[
F\in\{U,C,T,T^7\},
\]

retain one global degree-48 Chebyshev polynomial

\[
p_F(\lambda)=\sum_{n=0}^{48}a_n^{(F)}C_n(\xi),
\qquad
\xi=\frac{\lambda-\lambda_c}{\lambda_h}.
\]

Exact source C1 anchors at `lambda=0` are imposed:

\[
p_U(0)=0,\quad p_U'(0)=\kappa,
\]

\[
p_C(0)=p_C'(0)=0,
\]

\[
p_T(0)=p_T'(0)=0,
\]

\[
p_{T^7}(0)=p_{T^7}'(0)=0.
\]

No order higher than 48 is admitted.

## 3. Coefficient-only best-value test

For each primitive and each conservative case envelope, solve

\[
\boxed{
\min_{a\in\mathcal F_{48,C1}}
\|p_a-F_{R10}\|_{L^\infty([\lambda_a,\lambda_b])}
}
\]

by material-coordinate linear-program/exchange discretization followed by a much finer independent material-coordinate audit.

This is deliberately stronger than the historical least-squares/N48-C1 coefficient generator for **value fidelity**. For the tensile primitive T, if this constrained minimax still leaves a large error, changing coefficient weights or node density inside the same global N48 polynomial space cannot remove the basic approximation-capacity limitation.

The numerical LP is not claimed as a theorem-level exact Remez certificate. It is used as a near-minimax representation-capacity audit, with dense independent re-evaluation of the resulting polynomial.

## 4. Why T controls the current-master fidelity

For a strongly compressed principal coordinate near `lambda_1=-1`, the R10 source has approximately

\[
C_1\approx1,\qquad T_1\approx3\times10^{-5}.
\]

For a second coordinate in the positive transition range,

\[
s_1\approx U_1+C_1T_2
\]

because `C_2` is small and the `T_1 T_2^8` term is negligible.

Therefore an absolute error `delta T_2` enters the current-master stress scalar almost one-for-one. This means the tensile-primitive approximation limit is not a harmless internal-coordinate error; it propagates directly into the mixed compression/tension material stress state that the plate can visit.

This observation also explains the 10:54 defect: the old wide N48 T error was order one and the current-master stress error became order one.

## 5. Structural implication of a failed fixed-global-N48 value gate

If the constrained value-optimal N48 T polynomial retains errors of order 0.1–0.25 on conservative Z0–Z5 envelopes, then a corrected Pu must not be computed from that representation and interpreted physically.

The permitted next response is **not** order escalation. The next representation must keep the order ceiling at 48 while introducing an analytically justified multiscale factorization/basis or exact source component that resolves the R10 transition without structural spatial quadrature.

Such a future representation must independently re-pass:

```text
R10 source value fidelity
R10 current-master stress fidelity
R10 tangent fidelity
Cayley-Hamilton compatibility
General-D15 / moment-first zero-spatial compatibility
fixed order 48 governance
```

No new Z0–Z5 Pu is authorized by this representation-capacity audit itself.