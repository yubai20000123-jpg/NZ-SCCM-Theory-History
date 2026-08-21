# NZ-SCCM — steel ideal-EP CAP-C73 material-only convergence lock

时间：2026-08-21 15:43 +08:00

## Target

The physical target is unchanged:

\[
\alpha(r)=\begin{cases}
1,&0\le r\le1,\\
r^{-1/2},&1<r\le25/4.
\end{cases}
\]

No structural load, Zhou result, or Swartz result is used in selecting the compiler order.

## Canonical analytic Chebyshev projection

Map `r in [0,25/4]` to

\[
\xi=\frac{8r}{25}-1.
\]

The yield point `r=1` is `xi=-17/25`. Put

\[
\theta_y=\arccos(-17/25)=2\arccos(2/5).
\]

Because on the post-yield interval `r=(25/4)cos^2(theta/2)`, the Chebyshev projection integral is analytic.

For `n=0`,

\[
d_0=\frac1\pi\left[
\frac45\ln\frac{5+\sqrt{21}}2
+\pi-2\arccos\frac25
\right].
\]

For `n>=1`,

\[
\boxed{
 d_n=\frac2\pi\left\{
\frac25\left[
2(-1)^n\ln\frac{5+\sqrt{21}}2
+4\sum_{j=1}^{n}(-1)^{n-j}
\frac{\sin[(2j-1)\arccos(2/5)]}{2j-1}
\right]
-\frac{\sin[2n\arccos(2/5)]}{n}
\right\}.
}
\]

Then

\[
\alpha_N(r)=\sum_{n=0}^{N}d_n\,\mathcal C_n(8r/25-1).
\]

This requires no material-coordinate fitting nodes.

## Gate

Predeclared material compiler gate:

\[
\|\alpha_N-\alpha\|_{\infty,[0,25/4]}\le5\times10^{-3}.
\]

An extremum audit is performed separately on `[0,1]` and `[1,25/4]`: on `[0,1]`, stationary points satisfy `alpha_N'(r)=0`; on `[1,25/4]`, stationary points satisfy

\[
\alpha_N'(r)+\frac1{2r^{3/2}}=0.
\]

Endpoints and `r=1` are included.

Results:

```text
N=72  max_abs_error = 0.0050310959297616975  at r=1  FAIL
N=73  max_abs_error = 0.0049126778555285130  at r=1  PASS
N=80  max_abs_error = 0.0045088748567914120  at r=1  PASS
```

Therefore the minimum passing production profile is

```text
STEEL_CAP_COMPILER = CAP-C73
R_MAX = 25/4
DEGREE = 73
MATERIAL_NODE_COUNT = 0
MAX_CAP_FACTOR_ERROR = 0.004912677855528513
```

If a future calculation proves analytically that `r>25/4` is required, direct extrapolation is forbidden. The same analytic coefficient derivation must be regenerated on a larger declared material interval, with the same material-only error gate, before solving that case. This is an implementation-domain change, not a new physical steel law.
