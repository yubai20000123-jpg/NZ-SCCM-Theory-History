# NZ-SCCM — exact R10 Pi factor to existing General-D15 adapter execution report

**Timestamp:** 2026-08-16 14:17 +08:00  
**Gate:** `UNIFIED_V1_R10_INTRINSIC_SCALE_FACTORIZED_PI_ADAPTER_GATE`  
**Result:** `PASS_DIAGNOSTIC / FAIL_EXISTING_GENERAL_D15_EXACT_CLOSURE / NO Pu RUN`

## 1. Objective

The previous 13:55 intrinsic-scale audit showed that the current R10 material law is low/moderate complexity in its own coordinates and that the thousands-order result is driven mainly by forcing the narrow `Pi_eta` sign split into one wide global lambda polynomial.

The present gate therefore tests the only remaining exact low-parameter question:

> Can `Pi_eta` remain exact and still enter the existing zero-spatial-integration General-D15 moment engine without a thousands-order global polynomial?

No structural capacity solve is performed.

## 2. Frozen R10 constants

```text
kappa = 2.0005129533678754
rho   = 0.1
xcr   = 0.04998717945397425
eta   = 0.0024993589726987125
h     = 0.09799750427197301
ur    = 0.03
```

The 13:55 material-only factor screen remains retained:

```text
Pi_eta = exact
C(c): N_C=6
u_R(t): N_u=64
fitted scalar coefficients = 72
E_sigma = 0.003337
E_tangent = 0.030469
E_divided_difference = 0.046869
```

These numbers establish material fidelity only; they do not solve the exact-moment adapter.

## 3. Exact scalar identities

Starting from

\[
\Pi_\eta(z)=\frac{z^2(\sqrt{z^2+\eta^2}+z)}{2(z^2+\eta^2)},
\]

one obtains exactly

\[
\boxed{\Pi_\eta(z)+\Pi_\eta(-z)=\frac{z^2}{\sqrt{z^2+\eta^2}}},
\]

\[
\boxed{\Pi_\eta(z)-\Pi_\eta(-z)=\frac{z^3}{z^2+\eta^2}}.
\]

Therefore

\[
\boxed{\Pi_\eta(z)=\frac12\left(\frac{z^2}{\sqrt{z^2+\eta^2}}+\frac{z^3}{z^2+\eta^2}\right)}.
\]

This decomposition is useful because it identifies the exact obstruction explicitly. The odd part is rational, while the even part contains an inverse square root. The factor cannot be reduced to a finite polynomial in `z` by Cayley-Hamilton alone.

## 4. Exact 2x2 spectral lift in a traceless test field

Take a traceless 2x2 tensor with eigenvalues `+r,-r`. For any spectral scalar `f`, the 2x2 Cayley-Hamilton lift has the form

\[
f(\mathbf X)=a(r)\mathbf I+b(r)\mathbf X.
\]

For `f=Pi_eta`, the preceding identities give

\[
\boxed{a(r)=\frac{r^2}{2\sqrt{r^2+\eta^2}}},
\]

\[
\boxed{b(r)=\frac{r^2}{2(r^2+\eta^2)}}.
\]

This is already an exact low-parameter matrix representation. The issue is not matrix lifting; the issue is the structural moment of `a(r)` and `b(r)` when `r` is a trigonometric/thickness field.

## 5. Minimal exact-moment closure test

Choose the admissible finite-trigonometric tensor field

\[
\mathbf X(\xi)=\beta\sin\xi\,\mathrm{diag}(1,-1),
\qquad 0\le\xi\le\pi.
\]

This is deliberately simpler than the actual Nguyen field. If the exact `Pi_eta` factor cannot close under existing D15 even here, it cannot be claimed to have a general existing-D15 adapter.

Its trace after the exact `Pi_eta` lift is

\[
\operatorname{tr}[\Pi_\eta(\mathbf X)]
=\frac{\beta^2\sin^2\xi}{\sqrt{\eta^2+\beta^2\sin^2\xi}}.
\]

Hence the required exact moment is

\[
J(\beta,\eta)=\int_0^\pi
\frac{\beta^2\sin^2\xi}{\sqrt{\eta^2+\beta^2\sin^2\xi}}\,d\xi.
\]

Let

\[
m=(\beta/\eta)^2.
\]

Using

\[
\frac{\beta^2\sin^2\xi}{\sqrt{\eta^2+\beta^2\sin^2\xi}}
=\sqrt{\eta^2+\beta^2\sin^2\xi}
-\frac{\eta^2}{\sqrt{\eta^2+\beta^2\sin^2\xi}},
\]

and the standard complete elliptic definitions, the exact result is

\[
\boxed{J=2\eta\,[E(-m)-K(-m)]}.
\]

This is an elliptic period, not a finite sum of the current General-D15 monomial moments.

## 6. Exact special-function values for representative beta/eta ratios

No structural spatial quadrature is used. The table evaluates only the closed elliptic expression above.

| beta | beta/eta | m | exact J |
|---:|---:|---:|---:|
|0.00249935897270|1|1|0.00299458254624|
|0.0124967948635|5|25|0.0237600555095|
|0.0499871794540 (= xcr)|20|400|0.0994896158879|
|0.1|40.0103|1600.82083064|0.199714240635|

The appearance of `K` and `E` occurs for any non-degenerate `beta`; it is not a large-amplitude artifact.

## 7. Comparison with the approved General-D15 algebra

The current V1 S5 contract requires each structural integrand to reduce to finite analytic trigonometric/thickness terms and then applies

\[
\mathscr D[Q]=\sum_k c_k J_{p_kr_k}J_{u_ks_k}Z_{h_k}.
\]

Those primitive moments are Beta/Gamma-type moments of finite powers of sine/cosine and thickness coordinate.

The exact `Pi_eta` special case above requires instead complete elliptic functions. In the full Nguyen 2D/thickness field, `r^2` is itself a multivariate trigonometric/thickness polynomial, so the exact factor generates multivariate algebraic-period objects at least as complicated as the one-dimensional elliptic witness.

Therefore:

```text
EXACT_PI_MATRIX_LIFT = PASS
EXACT_PI_TO_EXISTING_GENERAL_D15_FINITE_MOMENT_CLOSURE = FAIL
```

## 8. Historical consistency

This result reconnects directly to two earlier project lessons:

1. R5: high-order/nested material factors caused expression swell; the remedy was moment-first contraction, not spatial quadrature.
2. PF1: algebraic-period / Picard-Fuchs machinery was explored as a compiler representation and failed the production complexity gate (15x15 connection witness).

The current elliptic witness shows why simply declaring `Pi_eta` exact and asking D15 to absorb it would reopen that old special-function complexity route.

## 9. What is and is not concluded

Concluded:

```text
R10 exact Pi_eta does not belong to the current finite Beta/Gamma General-D15 closure algebra.
A general exact adapter cannot be claimed within the existing D15 engine.
```

Not concluded:

```text
No theorem is claimed that every possible exact CAS/special-function backend is impossible.
No claim is made that R10 material physics is wrong.
No claim is made that the 13:55 low-complexity factor screen is invalid at material level.
```

A new elliptic/Appell/Lauricella/Picard-Fuchs structural moment family would be a new backend with substantial theoretical complexity. It is not activated here.

## 10. Gate decision

```text
R10_PHYSICAL_OPERATOR = UNCHANGED
N3584_SOURCE_FIDELITY_WITNESS = RETAINED
N3584_AS_NEXT_PRODUCTION_BASIS = REJECTED
INTRINSIC_FACTOR_MATERIAL_SCREEN = PASS_DIAGNOSTIC
EXACT_PI_EXISTING_D15_ADAPTER = FAIL
NEW_SPECIAL_FUNCTION_BACKEND = NOT_AUTHORIZED
NEW_Z0_Z6_Pu = NOT RUN
```

## 11. Next unique gate

```text
UNIFIED_V1_R10_PI_D15_COMPATIBLE_LOW_PARAMETER_REGULARIZATION_DECISION_GATE
```

That gate must decide whether the `Pi_eta` regularization itself may be replaced by a small, source-controlled, D15-compatible smooth splitter. It must be material-only first and may not use specimen capacities to choose the replacement.
