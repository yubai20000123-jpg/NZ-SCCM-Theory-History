# NZ-SCCM R07R — EXPLICIT SURFACE / GLOBAL TARGET RULE

**Date:** 2026-08-10

## 1. Highest requirement

R07R implements the latest user priority:

```text
FINAL CAPACITY MUST COME FROM EXPLICIT FORMULAS
AND EXPLICIT DERIVATIVES OF THE SAME FORMULAS.
```

Material pointwise regression error is secondary. Sharp source/experimental peaks may be deliberately under-used before structural validation.

## 2. R07R material candidates are frozen before structural validation

Three scalar spectral candidates were defined without using Case21 Pu:

```text
A_FC100_FT90 : compression peak retention 100%, tensile peak retention 90%
B_FC97_FT90  : compression peak retention 97%,  tensile peak retention 90%
C_FC95_FT80  : compression peak retention 95%,  tensile peak retention 80%
```

Common explicit scalar family:

\[
u(\lambda)=\lambda\frac{N_5(\lambda)}{D_6(\lambda)},
\]

\[
N_5=\kappa+a_1\lambda+a_2\lambda^2+a_3\lambda^3+a_4\lambda^4+a_5\lambda^5,
\]

\[
D_6=1+b_1\lambda+b_2\lambda^2+b_3\lambda^3+b_4\lambda^4+b_5\lambda^5+b_6\lambda^6.
\]

Explicit derivative:

\[
u'(\lambda)=\frac{(N+\lambda N')D-\lambda ND'}{D^2}.
\]

The minimal R07R 2D/4D current surface is

\[
\boldsymbol\sigma=f_c\,u(\mathbf E_u),
\]

with standard 2x2 matrix-function/divided-difference reconstruction. No runtime TT/TC/CC state machine is introduced.

## 3. Minimality rule

R07R deliberately omits any extra `J2/CC/TC` multiaxial enhancement in the first proof-of-concept. This does **not** assert that biaxial enhancement is physically unnecessary. It asks whether additional multiaxial complexity is needed only after a deficiency is demonstrated.

## 4. Whole-structure explicit target candidate

R07R also tests an explicit whole-structure representation:

\[
P(D,q)=\sum_{i=0}^{10}\sum_{j=0}^{10}p_{ij}T_i(\xi_D)T_j(\xi_q),
\]

\[
R_q(D,q)=\sum_{i=0}^{10}\sum_{j=0}^{10}r_{ij}T_i(\xi_D)T_j(\xi_q),
\]

with

\[
\xi_D=\frac{2D-(0.35+1.40)}{1.40-0.35},
\qquad
\xi_q=\frac{2q-(0.003+0.033)}{0.033-0.003}.
\]

All derivatives are analytic Chebyshev derivatives of the same finite coefficient arrays, and

\[
L=P_{,D}R_{q,q}-P_{,q}R_{q,D}.
\]

## 5. Status boundary

R07R proves that an end-to-end explicit-capacity chain is feasible, but the coefficient-identification step for the whole-structure target used high-accuracy full-halfwave numerical integration offline.

Therefore:

```text
R07R = PASS_PROOF_OF_CONCEPT_EXPLICIT_END_TO_END_CHAIN
FORMAL_ZERO_QUADRATURE_PRODUCTION_STATUS = HOLD
```

The numerical integration is not the runtime production operator; nevertheless it is not identical to the older pure-D15 coefficient derivation and must remain visible until the project explicitly accepts or replaces it.

## 6. Structural-validation boundary

Case21 experimental Pu was not used to choose any material peak-retention parameter. It is inspected only after all three material candidates are frozen.

The R07R Case21 capacities are concrete-only diagnostics. Reinforcement is not added after the fact and the values are not final RC capacities.

## 7. Next step

```text
NEXT = R08_EXPLICIT_REINFORCEMENT_AND_MINIMUM_MULTAXIAL_CORRECTION
```

First insert reinforcement into the same explicit `P,Rq,L` chain. Only after the RC result is available may a small source-grounded multiaxial correction be considered, and only if a concrete deficiency is demonstrated.
