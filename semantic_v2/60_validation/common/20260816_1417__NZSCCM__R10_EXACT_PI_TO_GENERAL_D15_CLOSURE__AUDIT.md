# NZ-SCCM validation audit — exact R10 Pi factor versus existing General-D15 closure

**Timestamp:** 2026-08-16 14:17 +08:00

## Audit question

Can the exact R10 smooth sign-split factor `Pi_eta` be inserted into the existing finite General-D15 moment algebra while preserving:

```text
one continuous complete halfwave
zero formal spatial sampling/quadrature
same-map stress and consistent tangent
low-parameter intrinsic factorization
no thousands-order global lambda polynomial
```

## Audit result

```text
EXACT_SCALAR_IDENTITY = PASS
EXACT_2X2_CAYLEY_HAMILTON_LIFT = PASS
EXISTING_GENERAL_D15_FINITE_BETA_GAMMA_CLOSURE = FAIL
STRUCTURAL_SPECIAL_FUNCTION_EXTENSION = NOT_AUTHORIZED
```

## Evidence A — exact Pi contains irreducible non-polynomial factors

The identities

\[
\Pi(z)+\Pi(-z)=z^2/\sqrt{z^2+\eta^2},
\qquad
\Pi(z)-\Pi(-z)=z^3/(z^2+\eta^2)
\]

show that an inverse-square-root algebraic factor survives any simple even/odd reduction.

## Evidence B — failure appears inside the simplest D15-compatible field

For

\[
X(\xi)=\beta\sin\xi\,\mathrm{diag}(1,-1),
\]

General-D15 would ordinarily integrate any finite polynomial of `sin(xi)` by its standard moment table.

Exact `Pi_eta`, however, produces the trace moment

\[
J=\int_0^\pi
\frac{\beta^2\sin^2\xi}{\sqrt{\eta^2+\beta^2\sin^2\xi}}d\xi
=2\eta[E(-m)-K(-m)],
\quad m=(\beta/\eta)^2.
\]

Thus the exact moment is elliptic for generic nonzero `beta`.

The present General-D15 contract is a finite sum of trigonometric/thickness Beta/Gamma moments. It does not contain elliptic moment primitives.

## Evidence C — full Nguyen field cannot be easier in the general case

The actual equivalent-uniaxial tensor has finite trigonometric/thickness entries, but its invariants contain multiple coordinate products. Applying exact `Pi_eta` at matrix level therefore introduces algebraic functions of multivariate trigonometric/thickness polynomials.

The one-dimensional elliptic witness is a strict special case of that class. Therefore a general existing-D15 exact closure cannot be asserted when it already fails in the special case.

This is a closure-class argument, not a numerical-timeout argument.

## Historical cross-check

The result is consistent with the repository history:

- R5: exact/high-order factor graphs caused expression swell when naively expanded; moment-first contraction was retained.
- PF1: algebraic-period / Picard-Fuchs machinery increased production complexity and failed its complexity gate.
- energy-potential gate: hidden high-degree/global-coefficient inflation was explicitly rejected as a theory simplification.
- R10: successful simplification came from low-parameter local material formulas, not from a globally enormous polynomial.

## Non-overclaim boundary

This audit does **not** establish mathematical impossibility of every conceivable exact special-function backend.

It establishes:

\[
\boxed{
\text{exact Pi_eta is outside the currently approved General-D15 finite moment algebra}
}
\]

and hence the exact-Pi intrinsic factor graph cannot yet be promoted to production under V1.

## Current implication

The project now faces a clean choice, to be made in a separate gate:

1. deliberately create and approve a new algebraic-period/special-function structural moment backend; or
2. retain General-D15 and reformulate the `Pi_eta` regularization into a low-parameter D15-compatible smooth material splitter.

Given the historical complexity failures and the project's hand-auditability requirement, option 2 is the current recommended **decision gate**, but no material replacement is executed by this audit.

## Capacity boundary

```text
Z6 51.30 MN = retained engineering baseline only
Z0-Z5 old Pu = retracted
Z0-Z5 N3584 locators = diagnostic only
new Z0-Z6 production Pu = not run
same-expression L = not run
same-state KZ = not run
```
