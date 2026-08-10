# USER-SKETCH SHAPE-PRESERVING SMOOTHING RULE

**Date:** 2026-08-10

## 1. User correction

The R07R rational scalar candidates are not the preferred interpretation of deliberate material under-use because their tensile side may still show an artificial overshoot / dip / rebound sequence.

The accepted interpretation is a **shape-preserving data-processing operation**:

```text
source / measured sharp feature
-> deliberately do not use the full sharp local capacity
-> replace the local cut / spike by a low-parameter smooth monotone cap
-> keep the main mechanical landmarks explicit
-> evaluate the structural consequence afterwards
```

The objective is NOT minimum pointwise material regression error.

## 2. Admissible representation

Any mathematical representation is admissible, including:

- explicit piecewise analytic scalar functions;
- smooth 2D/4D current surfaces;
- local Hermite / Bezier / polynomial patches;
- invariant or spectral matrix functions;
- whole-structure explicit target functions;
- low-rank / special-function constructions.

The mandatory end condition is:

\[
P(D,q),\qquad R_q(D,q),
\]

with explicit derivatives from the same formulas,

\[
P_{,D},P_{,q},R_{q,D},R_{q,q},
\]

and

\[
L=P_{,D}R_{q,q}-P_{,q}R_{q,D}=0,
\]

so that

\[
P_u=P(D^*,q^*)
\]

is obtained from explicit formulas.

## 3. Shape-preserving requirement

For a deliberately simplified tensile branch, the preferred prototype is:

- monotone increase from the origin to one rounded tensile peak;
- zero tangent at the retained peak;
- monotone decrease to the retained residual level;
- zero tangent at the residual onset;
- no artificial secondary undershoot;
- no rebound after the local minimum;
- no local oscillation introduced only by the regression family.

The same principle applies to compression or mixed-state patches: remove a local cut/spike only when its mechanical consequence is explicitly reported.

## 4. Structural validation order

1. Freeze the material simplification before viewing the structural experimental target used for validation.
2. Insert reinforcement into the SAME `P,Rq` equations before solving the RC limit state.
3. Compare the resulting RC prediction with experiment.
4. Only if a systematic deficiency remains may a minimal source-grounded multiaxial correction be introduced.
5. Do not restore the full historical CC/TC/TT complexity merely to reduce local material regression error.

## 5. Formal-status distinction

An explicit whole-structure target identified offline from numerical data may be retained as a proof-of-concept under the current user priority, provided the offline identification is disclosed.

It is NOT automatically identical to the older pure-D15 zero-spatial-quadrature production identity. That distinction must remain visible.
