# NZ-SCCM SPECTRAL REACHABLE DOMAIN REDUCTION R03

Date: 2026-08-10

## 1. Identity
Same-route G18/G20/G27 dimensional/reachable-domain reduction.
No route switch. No Case21/Swartz Pu calibration. No formal spatial quadrature.

## 2. Convention and exact sufficient separation inequality
This R03 fixes:

```text
r = ell/b
```

Thus cases 1-16 use `r=2` and cases 17-24 use `r=1`.

For the generalized halfwave kinematics,

\[
X_{11}-X_{22}=D+\frac{C_m}{1+\nu}\left[(1-\sin^2X)\sin^2Y-r^{-2}\sin^2X(1-\sin^2Y)\right]
+\frac{C_b(1-r^{-2})}{1+\nu}\sin X\sin Y\,\zeta.
\]

Therefore, for `q>=0` and `r>=1`,

\[
X_{11}-X_{22}\ge
D-\frac{C_m}{r^2(1+\nu)}
-\frac{|C_b|(1-r^{-2})}{1+\nu}.
\]

Since

\[
\lambda_+-\lambda_-=\sqrt{(X_{11}-X_{22})^2+4X_{12}^2},
\]

the sufficient all-space spectral-order condition is

\[
\boxed{
D>D_{\rm sep}(q)
=\frac{C_m}{r^2(1+\nu)}
+\frac{|C_b|(1-r^{-2})}{1+\nu}.
}
\]

## 3. Executed common diagnostic contract

```text
D in [0.60,0.78]
q in [0.0001,0.006]
```

This contains the historical Case21 regression box but is **not frozen as the final Swartz24 production reachability box**.

Across all 24 source panels the above inequality certifies positive spectral separation.

Worst panel: Case 11.

```text
D_sep(q=0.006) = 0.3214976720
certified gap lower at D=0.60 = 0.2785023280
```

Audit-only dense material-coordinate sampling found:

```text
minimum observed gap = 0.3179329509
case                  = 11
```

Audit union over the executed diagnostic contract:

\[
\lambda_+\in[-0.479285,0.479285],
\]

\[
\lambda_-\in[-1.123467,-0.252159].
\]

The audit cloud is diagnostic only and is not part of the formal structural operator.

## 4. Interpretation
The earlier Case21 two-interval observation was not accidental. Under this explicit diagnostic D-q contract, ordered principal spectra remain globally separated for all 24 Swartz geometries.

This is not yet a final Swartz24 production theorem because the final admissible D-q box remains open. The reusable result is the analytic inequality `D>D_sep(q)`: any future structural search box must pass it before a separated two-interval scalar compiler is accepted.

## 5. Saddle-surface diagnostic
For the current reference principal surface `s1(lambda1,lambda2)`, a Hessian-sign diagnostic over `[-1.1,0.18]^2` gives approximately:

```text
det(H)<0 / saddle-like = 30.62%
convex-like            = 68.54%
concave-like           = 0.84%
```

Therefore the plotted current surface contains substantial local saddle-like patches, but it is **not** one global hyperbolic paraboloid. Visual saddle resemblance does not by itself identify an integration family.

## 6. Exact dimensional reduction: source-shaped principal surface has separated rank <= 4
This is stronger than the numerical SVD observation. The source-shaped reference map is algebraically separable:

\[
s_+(\lambda_+,\lambda_-)
=U(\lambda_+)
-a_{cc}C(\lambda_+)^2C(\lambda_-)
+C(\lambda_+)T(\lambda_-)
-\rho a_tT(\lambda_+)T(\lambda_-)^8,
\]

\[
s_-(\lambda_+,\lambda_-)
=U(\lambda_-)
-a_{cc}C(\lambda_-)^2C(\lambda_+)
+C(\lambda_-)T(\lambda_+)
-\rho a_tT(\lambda_-)T(\lambda_+)^8.
\]

Hence each principal stress surface is a sum of at most **four products of one-variable functions**. A generic two-dimensional surface fit is not mathematically necessary for this reference architecture.

On the R03 audit reachable cloud:

| term | max abs normalized stress | P95 abs | mean abs |
|---|---:|---:|---:|
| `splus_U` | 7.79560e-1 | 4.27339e-1 | 9.95678e-2 |
| `splus_CC` | 6.51463e-2 | 1.90762e-2 | 2.84402e-3 |
| `splus_C*Tminus` | 3.05283e-5 | 1.62591e-5 | 3.48135e-6 |
| `splus_Tplus*Tminus^8` | 6.45159e-36 | 1.65283e-37 | 3.30782e-38 |
| `sminus_U` | 1.00001 | 9.87652e-1 | 9.41105e-1 |
| `sminus_CC` | 8.35480e-2 | 4.33017e-2 | 8.61624e-3 |
| `sminus_Cminus*Tplus` | 9.73450e-1 | 8.08333e-1 | 1.18088e-1 |
| `sminus_Tminus*Tplus^8` | 3.91963e-7 | 1.34062e-7 | 1.56897e-8 |

On the executed audit interval

\[
\lambda_-\in[-1.123467,-0.252159],
\]

we obtained

\[
\max |T(\lambda_-)|=1.23799\times10^{-4}.
\]

Corresponding interval bounds include

```text
|C(lambda+) T(lambda-)| <= 9.65e-5
rho*a_t |T(lambda+) T(lambda-)^8| <= 4.52e-34
rho*a_t |T(lambda-) T(lambda+)^8| <= 9.23e-7
```

These are diagnostic material-coordinate bounds, not a production deletion rule. They show why the negative ordered branch is overwhelmingly compression-dominated in the executed contract.

## 7. Numerical low-rank confirmation
SVD of `s1` gives:

```text
full square [-1.25,0.15]^2:
  rank 3 -> relative Frobenius residual < 1e-4
  rank 4 -> machine-level residual

R03 ordered reachable rectangle:
  rank 2 -> relative Frobenius residual < 1e-4
  rank 3 -> machine-level residual
```

The machine-level rank-4 result follows from the exact algebra above; the lower numerical rank on the reachable rectangle occurs because several separated interaction terms are extremely small there.

## 8. Univariate branch-compiler implication
Once the map is kept in exact rank-4 form, the remaining scalar approximation problem is one-dimensional on `lambda+` and `lambda-` separately.

Diagnostic compiler results on the R03 audit intervals:

```text
lambda- branch:
  U,C,T,T8 all reach <=0.1% normalized max error by degree 8

lambda+ branch:
  U reaches <=1% by degree 32
  C reaches <=1% by degree 48
  T and T8 still do not reach <=1% by degree 96 on the broad diagnostic union
```

Thus the hard part has been localized again: it is almost entirely the positive ordered branch crossing the narrow tensile transitions. The negative compression branch is analytically cheap.

## 9. Exact Appell-F1 master kernel demonstrated
For

\[
D(X,Y)=a+b\sin^2X+c\sin^2Y+d\sin^2X\sin^2Y,
\]

the whole-domain master is

\[
\boxed{
\mathcal M=
\frac{\pi^2}{\sqrt{a(a+b)}}
F_1\!\left(
\frac12;\frac12,\frac12;1;
-\frac ca,-\frac{c+d}{a+b}
\right).
}
\]

R03 representative execution:

```text
formal Appell-F1 value = 6.611588675823622
audit-only Gauss value = 6.611588675823635
relative difference     = 1.881e-15
formal spatial quadrature count = 0
```

Parameter derivatives of this master generate squared-denominator/numerator moments. Appell/Carlson are therefore genuine candidate **named exact kernels** when the reduced NZ-SCCM algebra matches their denominator class.

## 10. Coalescence-safe 2x2 matrix-function form
A future broader D-q box may reduce the principal gap. This still does not require a TT/TC/CC material state switch.

For

\[
\mathbf X=\mu\mathbf I+\mathbf Y,
\qquad
\mathbf Y^2=r_s^2\mathbf I,
\]

any scalar matrix function has the exact form

\[
f(\mathbf X)=f_e(\mu,r_s)\mathbf I+f_o(\mu,r_s)\mathbf Y,
\]

\[
f_e=\frac{f(\mu+r_s)+f(\mu-r_s)}2,
\]

\[
f_o=\frac{f(\mu+r_s)-f(\mu-r_s)}{2r_s},
\qquad
f_o\to f'(\mu)\quad(r_s\to0).
\]

This Cayley-Hamilton/divided-difference representation is continuous through repeated eigenvalues and is preferable to fragile eigenvector branch logic.

## 11. R03 decision

```text
SPECTRAL_REACHABLE_DOMAIN_REDUCTION_R03 = PASS_DIAGNOSTIC
ROUTE_SWITCH = NO
GLOBAL_TWO_BRANCH_SEPARATION_IN_R03_CONTRACT = CERTIFIED
FINAL_SWARTZ24_PRODUCTION_DQ_BOX = OPEN
EXACT_RANK4_PRINCIPAL_FACTORISATION = PROMOTED
GENERIC_2D_SURFACE_FIT = NOT_NEEDED_FOR_SOURCE_SHAPED_REFERENCE
K_1P25_PHYSICAL_WIDENING = OPTIONAL_NOT_FROZEN
APPELL_F1_CARLSON = PROMOTED_WHEN_KERNEL_CLASS_MATCHES
LARGE_PICARD_FUCHS_RETURN = NOT_AUTHORIZED
```

Preferred next representation task:

```text
1D_BRANCH_PRIMITIVES
-> EXACT_RANK4_CONTRACTION
-> COALESCENCE_SAFE_2x2_MATRIX_FUNCTION
-> DIRECT_BETA/APPELL/CARLSON_KERNEL_CLASSIFICATION
```

No Case21 or Swartz Pu was solved in R03.