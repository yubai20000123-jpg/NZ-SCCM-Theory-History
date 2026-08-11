# NZ-SCCM R10B COEFFICIENT-GENERATION CONTRACT V1

**Date:** 2026-08-11 16:05 +08:00  
**Identity:** NEW TRANSPARENT REPRODUCIBILITY CONVENTION. This file does not claim to be the byte-exact historical R10B generator and changes no R10 material parameter.

## 1. Why a new convention is frozen

The exact historical coefficient generator and coefficient arrays are not recoverable from the retained R10B execution package. The project therefore freezes one explicit deterministic convention so that every coefficient is reproducible from the frozen R10 formulas alone.

The convention is deliberately not a least-squares fit and has no hidden weights, regularization parameters, or structural-load calibration.

## 2. Compiler hull

Retain the Case21 safe scalar hull

\[
\lambda_a=-1.01,\qquad \lambda_b=0.105.
\]

Define

\[
\lambda_c=\frac{\lambda_a+\lambda_b}{2}=-0.4525,
\qquad
\lambda_h=\frac{\lambda_b-\lambda_a}{2}=0.5575,
\]

and

\[
\boxed{\xi(\lambda)=\frac{\lambda-\lambda_c}{\lambda_h}
=\frac{400\lambda+181}{223}}.
\]

## 3. Scalar objects

Compile exactly the four scalar objects already audited by R10B:

\[
F\in\{U,C,T,T^7\},
\]

where every source value is evaluated from the frozen R10 material formulas, not from experimental data.

## 4. Unique coefficient rule

For material order \(N\), use the \(N+1\) roots of \(T_{N+1}\):

\[
\boxed{\theta_j=\frac{(j+\tfrac12)\pi}{N+1}},
\qquad j=0,\ldots,N,
\]

\[
\boxed{\xi_j=\cos\theta_j},
\qquad
\boxed{\lambda_j=\lambda_c+\lambda_h\cos\theta_j}.
\]

Evaluate the frozen material formula:

\[
f_j^{(F)}=F(\lambda_j).
\]

The finite representation is

\[
\boxed{F_N(\lambda)=\sum_{n=0}^{N}a_n^{(F)}T_n[\xi(\lambda)]}.
\]

The coefficients are fixed by the discrete Chebyshev transform

\[
\boxed{
a_n^{(F)}
=
\frac{2-\delta_{n0}}{N+1}
\sum_{j=0}^{N}
F(\lambda_j)\cos(n\theta_j)
},
\qquad n=0,\ldots,N.
\]

This is a direct formula-to-formula analytic compilation. It is not constitutive calibration.

## 5. Why this convention is preferred for reproducibility

This rule has:

- no least-squares weighting;
- no SVD/rcond choice;
- no branch-dependent sample count;
- no regularization coefficient;
- no material or structural test data;
- one explicit hull and one explicit coefficient formula;
- stable coefficient magnitudes;
- exact interpolation of the source values at the \(N+1\) Chebyshev-root nodes up to floating-point roundoff.

## 6. Material-order re-freeze

The historical N48 error table is used only as a **material-fidelity floor**, not as a structural calibration target.

The deterministic validation set is:

```text
100001 equally spaced lambda values on [-1.01,-0.68]
100001 equally spaced lambda values on [-0.10, 0.105]
```

Orders \(N=48,56,\ldots\) are checked. The first tested order for which all four objects simultaneously satisfy both historical N48 max-error and p95-error ceilings is:

\[
\boxed{N_M^{repro}=112}.
\]

At N=112:

| scalar | max abs error | p95 abs error | historical N48 ceiling passed |
|---|---:|---:|---|
| U | 7.3352195900e-05 | 4.1632950383e-05 | YES |
| C | 2.0457015200e-03 | 6.0108850303e-04 | YES |
| T | 1.6385185836e-02 | 3.7906918519e-03 | YES |
| T^7 | 2.8889305301e-03 | 5.2677094828e-04 | YES |

The maximum interpolation residual at the N=112 compiler nodes is about \(2.1\times10^{-14}\) for U/C and below \(4\times10^{-15}\) for T/T^7 in IEEE double evaluation.

Therefore:

```text
COEFFICIENT_GENERATION_CONVENTION = CHEBYSHEV_ROOT_DCT
MATERIAL_REPRODUCTION_ORDER       = 112
HISTORICAL_N48_ORDER              = RETAINED_REFERENCE_ONLY
```

N=112 is a compiler/reproducibility order, not a material-model order and not a material parameter count.

## 7. Numerical storage rule

- theory: use the generating formulas above;
- machine coefficient table: store 17 significant decimal digits for IEEE-double round-trip;
- optional high-precision audit may regenerate from the formula with higher precision;
- do not hand-enter or manually tune coefficients.

## 8. Structural boundary

This contract freezes only the 1D material-coordinate coefficient generator and its material fidelity floor.

It does **not** yet re-freeze a structural spatial order \(N_S\), because the historical N48/N96 order study changed \(N_M\) and \(N_S\) together.

Next structural action is simply to feed the N=112 material coefficients into the already retained zero-spatial Cayley-Hamilton/D15 backend, then determine the smallest \(N_S\) meeting the engineering order gate. No material retuning is allowed.
