# NZ-SCCM R07R — EXPLICIT SURFACE SIMPLIFICATION AND CAPACITY CHAIN

Date: 2026-08-10

## 1. Purpose

Execute the latest priority reset:

> do not pursue minimum pointwise material regression error;  
> allow deliberate under-use of sharp material peaks;  
> allow 4D current surfaces or whole/global target functions;  
> require the final capacity to come from explicit formulas and explicit derivatives.

This R07R deliberately tests the simplest end-to-end route.

## 2. Explicit material family

For each candidate,

\[
u(\lambda)=\lambda\frac{N_5(\lambda)}{D_6(\lambda)},
\]

\[
N_5(\lambda)=\kappa+a_1\lambda+a_2\lambda^2+a_3\lambda^3+a_4\lambda^4+a_5\lambda^5,
\]

\[
D_6(\lambda)=1+b_1\lambda+b_2\lambda^2+b_3\lambda^3+b_4\lambda^4+b_5\lambda^5+b_6\lambda^6.
\]

Derivative:

\[
u'(\lambda)=\frac{(N+\lambda N')D-\lambda ND'}{D^2}.
\]

The 2x2 current stress is the matrix/spectral function

\[
\boldsymbol\sigma=f_c\,u(\mathbf E_u).
\]

Therefore the principal stresses are simply

\[
\sigma_i=f_c\,u(\lambda_i),
\]

and the full tensor is reconstructed with the standard 2x2 divided difference. No TT/TC/CC runtime state machine is used.

## 3. Deliberate material under-use candidates

These were frozen **before** any Case21 capacity evaluation:

```text
A_FC100_FT90 : compression peak retention = 100%; tensile peak retention = 90%
B_FC97_FT90  : compression peak retention = 97%;  tensile peak retention = 90%
C_FC95_FT80  : compression peak retention = 95%;  tensile peak retention = 80%
```

All candidates retain:

- zero stress at the origin;
- initial slope through the fixed `kappa` coefficient;
- about 10% compression residual;
- about 3% tensile residual plateau;
- no pole in the material fitting window `[-10,3]`.

Executed material summary:

| candidate | compression peak retention | tensile peak retention | min denominator | min compression sigma/fc | max tension sigma/fc |
|---|---:|---:|---:|---:|---:|
| A_FC100_FT90 | 1.00 | 0.90 | 0.608916 | -1.000300 | 0.091368 |
| B_FC97_FT90 | 0.97 | 0.90 | 0.601166 | -0.970283 | 0.091388 |
| C_FC95_FT80 | 0.95 | 0.80 | 0.799914 | -0.950244 | 0.081494 |

This step intentionally does **not** force the fitted function to reproduce the sharp local source peak or transition ridge.

## 4. Minimal multiaxial choice in R07R

R07R deliberately starts from the minimal scalar matrix-function surface

\[
\boldsymbol\sigma=f_c\,u(\mathbf E_u)
\]

with **no additional `J2/CC/TC` enhancement**.

This is not a claim that biaxial enhancement is unnecessary. It is a controlled simplification experiment answering:

> how far can the explicit capacity theory go before extra multiaxial complexity is actually needed?

Any later multiaxial correction must improve a demonstrated deficiency rather than be carried automatically from the old source oracle.

## 5. Whole-structure explicit target

For each material candidate, high-accuracy full-halfwave response values were generated on a fixed `D-q` box and compressed into explicit finite Chebyshev surfaces:

\[
P(D,q)=\sum_{i=0}^{10}\sum_{j=0}^{10}p_{ij}T_i(\xi_D)T_j(\xi_q),
\]

\[
R_q(D,q)=\sum_{i=0}^{10}\sum_{j=0}^{10}r_{ij}T_i(\xi_D)T_j(\xi_q).
\]

with

```text
D in [0.35, 1.40]
q in [0.003, 0.033]
```

and

\[
\xi_D=\frac{2D-(0.35+1.40)}{1.40-0.35},
\qquad
\xi_q=\frac{2q-(0.003+0.033)}{0.033-0.003}.
\]

Each surface has 121 coefficients.

The production evaluation of this **candidate global target** uses no spatial integration: it evaluates the finite polynomial above.

The derivatives are obtained from the same coefficient arrays:

\[
P_{,D},\quad P_{,q},\quad R_{q,D},\quad R_{q,q},
\]

and

\[
L(D,q)=P_{,D}R_{q,q}-P_{,q}R_{q,D}.
\]

## 6. Independent off-grid global-target validation

| candidate | P max abs error kN | P P95 kN | Rq max abs error kN | Rq P95 kN |
|---|---:|---:|---:|---:|
| A_FC100_FT90 | 3.7091 | 1.6441 | 0.4481 | 0.2420 |
| B_FC97_FT90 | 3.7584 | 1.6186 | 0.4547 | 0.2492 |
| C_FC95_FT80 | 3.5594 | 1.9059 | 0.4208 | 0.2781 |

The global target reproduces the underlying explicit material-surface audit in the present Case21 box to the few-kN/sub-kN level.

## 7. Explicit stationary roots — concrete only

The root equations are

\[
R_q(D,q)=0,
\]

\[
L(D,q)=P_{,D}R_{q,q}-P_{,q}R_{q,D}=0.
\]

Executed roots:

| candidate | D* | q* | A* mm | Pu explicit global target kN | direct material-surface audit P at same root kN |
|---|---:|---:|---:|---:|---:|
| A_FC100_FT90 | 0.914265 | 0.0210447 | 25.6745 | 317.4186 | 317.8396 |
| B_FC97_FT90 | 0.912204 | 0.0211055 | 25.7487 | 309.8781 | 310.2823 |
| C_FC95_FT80 | 0.886755 | 0.0206359 | 25.1758 | 306.1928 | 306.6491 |

Case21 RC experiment, shown only after the material candidates were frozen:

\[
P_f=368.312750\ \mathrm{kN}.
\]

These R07R values are **not final RC capacities**, because reinforcement is not yet inserted into the same explicit `P,Rq,L` equations.

Relative to the old crack-free G31 concrete-only value

\[
476.935634\ \mathrm{kN},
\]

deliberate smoothing/under-use alone reduces the concrete-only stationary capacity to roughly the 306–318 kN band.

This is a major mechanical consequence: removing/under-using sharp material capacity is not merely a cosmetic numerical smoothing.

## 8. Formal-status caveat

The present global `P/Rq` coefficient identification used high-accuracy numerical full-halfwave integration **offline**.

The final runtime formula is fully explicit and differentiable, but this identification step is not yet identical to the older zero-quadrature D15 derivation doctrine.

Therefore R07R is classified as:

```text
R07R = PASS_PROOF_OF_CONCEPT_EXPLICIT_END_TO_END_CHAIN
FORMAL_ZERO_QUADRATURE_PRODUCTION_STATUS = HOLD
```

until the project chooses one of two routes:

A. accept offline identification of an explicit whole-structure target as a legitimate data-processing step; or  
B. regenerate the same `P/Rq` coefficient data with analytic D15 / named-kernel evaluation.

This distinction is intentionally visible and not hidden.

## 9. R07R decision

```text
ultra-close material point fitting = REJECTED AS OBJECTIVE
explicit smooth low-parameter material formula = PASS PROOF OF CONCEPT
explicit material derivatives = PASS
explicit P(D,q), Rq(D,q) = PASS PROOF OF CONCEPT
explicit L(D,q) = PASS
stationary concrete-only Case21 roots = PASS DIAGNOSTIC
reinforcement = OPEN
source-grounded extra multiaxial enhancement = OPEN
final RC Pu = OPEN
```

Recommended next task:

```text
R08_EXPLICIT_REINFORCEMENT_AND_MINIMUM_MULTAXIAL_CORRECTION
```

First add reinforcement to the **same explicit** `P,Rq,L` chain. Only after that, inspect whether a small source-grounded multiaxial correction is actually required.
