# NZ-SCCM — R10 true infinite-series Stage-I execution report

**Timestamp:** 2026-08-17 14:56 +08:00  
**Status:** EXECUTED / SERIES-LAW STAGE-I PASS / NO NEW Pu RELEASE

## 0. Purpose

The previous canonical correction rejected `N48 -> N96 -> N144 -> ...` as the formal theory. This execution therefore tested whether the frozen R10 source actually contains a discoverable **infinite coefficient law** analogous in architecture to classical convergent plate-series solutions.

The result is affirmative.

This report records the source algebra, coefficient recurrences, convergence constants and independent numerical diagnostics used to validate them.

---

# 1. Source constants used

```text
kappa = 2.0005129533678754
rho   = 0.1
a=rho/kappa = 0.0499871794539742
eta   = 0.00249935897269871
H     = 0.0979975042719730
UR    = 0.03
```

No material parameter was changed.

The current Z6 material guard used for the Stage-I concrete sequence instantiation is

```text
lambda in [-1.75,+1.45]
center c0 = -0.15
halfwidth h = 1.6
```

This is a material-coordinate interval, not a spatial subdivision.

---

# 2. Exact universal-kernel decomposition — PASS

The frozen `pi_eta` was algebraically simplified to

\[
t=\frac{\lambda^2}{2\sqrt{\lambda^2+\eta^2}}
+\frac{\lambda^3}{2(\lambda^2+\eta^2)},
\]

\[
c=\frac{\lambda^2}{2\sqrt{\lambda^2+\eta^2}}
-\frac{\lambda^3}{2(\lambda^2+\eta^2)}.
\]

Thus only two universal scalar kernels are needed:

```text
f = 1/sqrt(lambda^2+eta^2)
r = 1/(lambda^2+eta^2)
```

This was checked symbolically, not fitted.

---

# 3. Exact infinite recurrence for f — derived and numerically verified

On

```text
lambda=c0+h*cos(theta)
```

the exact five-term Chebyshev recurrence is

```text
(h^2/4)(n-1) a[n-2]
+ h*c0*(n-.5) a[n-1]
+ A0*n a[n]
+ h*c0*(n+.5) a[n+1]
+ (h^2/4)(n+1) a[n+2] = 0
```

where

```text
A0 = c0^2 + eta^2 + h^2/2.
```

For Z6:

```text
h^2/4 = +0.64
h*c0  = -0.24
A0    = +1.30250624679527
```

so

```text
0.64(n-1)a[n-2]
-0.24(n-.5)a[n-1]
+1.30250624679527*n*a[n]
-0.24(n+.5)a[n+1]
+0.64(n+1)a[n+2] = 0.
```

A high-resolution cosine-transform coefficient ledger was used **only as an external sequence diagnostic**. Relative recurrence residuals were approximately

```text
n=10     2.76e-17
n=100    0
n=1000   3.55e-17
```

before floating/noise contamination becomes visible in coefficients approaching machine precision.

Therefore

```text
UNIVERSAL_SQRT_KERNEL_P_RECURSIVE_LAW = PASS
```

This is a recurrence law for the infinite sequence; no degree sweep is involved.

---

# 4. Exact rational-kernel recurrence — PASS

For

\[
r=(\lambda^2+\eta^2)^{-1},
\]

`q*r=1` gives the finite-band tail recurrence

```text
0.64(b[n-2]+b[n+2])
-0.24(b[n-1]+b[n+1])
+1.30250624679527*b[n] = 0
```

away from the finite low-mode forcing.

Combined with the finite Chebyshev shift operator for multiplication by `lambda`, this generates the exact infinite coefficient sequences of `c` and `t`.

---

# 5. Compression C — two independent infinite-law checks

## 5.1 Global geometric identity

The exact transform

\[
s=c/(1+c)^2
\]

gives

\[
C=\kappa\sum_{m=1}^{\infty}(4-\kappa)^{m-1}s^m.
\]

Uniform ratio bound:

```text
(4-kappa)/4 = 0.499871761658031 < 0.5
```

so the rational compression denominator has a global exact geometric remainder formula.

## 5.2 Quadratic-field ODE

A separate symbolic reduction used

```text
f^2 = 1/(lambda^2+eta^2)
C = A_C(lambda) + B_C(lambda)*f
```

and generated the first-order cleared ODE

```text
P1(lambda) C' + P0(lambda) C = PR(lambda)
```

with polynomial degrees

```text
deg P1 = 17
deg P0 = 16
deg PR = 14.
```

Because polynomial multiplication in `lambda=c0+h*cos(theta)` has finite Fourier bandwidth, this ODE generates a finite-band linear P-recurrence for the entire infinite Chebyshev coefficient sequence of `C`.

Spot evaluation of the derived ODE against raw R10 at

```text
lambda=-1.6,-.7,-.1,.02,.5,1.3
```

left only floating residuals, from about `1e-40` to roughly `1e-10` at the largest-scaled endpoint check. The relation is symbolically generated from the exact quadratic-field identity.

```text
C_QUADRATIC_FIELD_CLOSURE = PASS
C_FINITE_BAND_RECURRENCE_GENERATOR = PASS
```

---

# 6. Tension branch structure — exact C2 factorization

The two branch differences were symbolically factored.

With `r=t/a`:

```text
u_mid-u_low
= -(r-1)^3/196830 * [quadratic polynomial in r]
```

and

```text
u_high-u_mid
= (H-UR)*(r-10)^3*(2*r^2+5*r+20)/19683.
```

Thus both branch switches are exactly cubic-contact joins. This proves the global frozen tension source is `C2` at the two landmarks without adding any smoothing law.

The landmark roots are

```text
lambda_1  = 0.0500805176491376
lambda_10 = 0.499881166745393
```

with

```text
t'(lambda_1)  = 1.00185527313813
t'(lambda_10) = 1.00001874800801.
```

Mapped to the Z6 interval:

```text
x_1      = 0.125050323530711
theta_1  = 1.44541777411337 rad
x_10     = 0.406175729215871
theta_10 = 1.15253121911414 rad.
```

The exact step-function Chebyshev sequence is

```text
h0 = theta_k/pi
hn = 2*sin(n*theta_k)/(pi*n), n>=1.
```

The global tension coefficient sequence is therefore a closed infinite Chebyshev convolution of the low/mid/high branch sequences with these two explicit step sequences.

The low and mid branch quadratic-field reductions give cleared first-order ODE degree triples

```text
T_low : (25,24,23)
T_mid : (25,24,24)
T_high: constant.
```

Hence all three branch sequences are finite-band P-recursive.

---

# 7. Exact third-derivative jump constants and n^-4 law

The source branch third-derivative jumps with respect to `t` are

```text
Delta u''' at t=a   = -27905.0340327012
Delta u''' at t=10a = +44.8064770469412
```

After composition with `t(lambda)`:

```text
Delta T'''_lambda at lambda_1  = -280606.367416764
Delta T'''_lambda at lambda_10 = +448.089971907599
```

After the Z6 affine Chebyshev map `lambda=c0+h*cos(theta)`, the jumps in the theta-function third derivative are

```text
T:
  Delta g'''(theta_1)  = -1122509.44854571
  Delta g'''(theta_10) = +1400.46250338021

U:
  Delta g'''(theta_1)  = -112250.944854571
  Delta g'''(theta_10) = +140.046250338021

T^7:
  Delta g'''(theta_1)  = -6959501.59272060
  Delta g'''(theta_10) = +7.14656015474921
```

The predicted asymptotic Chebyshev coefficient is

\[
a_n^{pred}
=\frac{2}{\pi n^4}
[\Delta g'''_1\cos(n\theta_1)+\Delta g'''_{10}\cos(n\theta_{10})].
\]

Independent high-resolution coefficient diagnostics gave the following actual/predicted ratios:

| primitive | n=10000 | n=15000 | n=20000 | n=30000 |
|---|---:|---:|---:|---:|
| T | 1.10046 | 1.02420 | 0.99323 | 0.98517 |
| U | 0.98904 | 1.02367 | 0.99324 | 0.98525 |
| T^7 | 0.99487 | 1.02351 | 0.99323 | 0.98515 |

This is strong numerical confirmation of the analytically derived `n^-4` physical-knot tail.

```text
R10_TENSION_N_MINUS_4_TAIL = PASS
```

---

# 8. Why N48 looked difficult on Z6 — now explained analytically

The universal square-root kernel has complex branch points at

\[
\lambda=\pm i\eta.
\]

Mapped to the Z6 interval, the nearest Bernstein ellipse parameter is

```text
rho_eta = 1.0015702405147586.
```

Thus the analytic-kernel component has very slow geometric decay before the asymptotic real-knot `n^-4` tail dominates.

The coefficient diagnostics show exactly this crossover:

- at moderate n the nearby complex branch points dominate;
- only at very high n does the cubic-contact knot law clearly control the sequence.

This explains the historical broad-domain N48 difficulty without interpreting it as a failure of exact structural integration.

---

# 9. Tangent convergence gate — PASS at sequence-theory level

For the true infinite Chebyshev identity

\[
F'=h^{-1}\sum n a_nU_{n-1},
\]

and

\[
|U_{n-1}(x)|\le n,
\]

so the derivative series is dominated by

\[
\sum n^2|a_n|.
\]

The physical `n^-4` coefficient law therefore gives

\[
\sum n^2|a_n|<\infty.
\]

Hence the first same-source directional tangent series required by the current stability/limit equations is absolutely convergent on the certified material interval.

```text
VALUE_SERIES_CONVERGENCE = PASS
FIRST_TANGENT_SERIES_CONVERGENCE = PASS
INDEPENDENT_TANGENT_FIT = NOT_REQUIRED / PROHIBITED
```

---

# 10. D15 infinite-moment limit gate — mathematical pass, runtime not yet promoted

For every coefficient term, `T_n(Ehat)` is a finite matrix polynomial. The existing 2x2 CH recurrence turns it into finite invariant-polynomial coefficients, and General-D15 integrates every retained term exactly.

The resulting formal structural series is

\[
J_\infty=\sum_{n=0}^{\infty}a_nJ_n,
\qquad
J_n=\mathscr D_{15}[W:T_n(Ehat)].
\]

Because `|T_n|<=1` on the certified spectral interval and `sum |a_n|<infinity`, the value moment series is absolutely convergent. The tangent series is controlled by `sum n^2|a_n|`, which also converges.

Therefore the Stage-I mathematical exchange

```text
infinite material sum <-> first derivative <-> exact structural integration
```

is justified.

However this execution did **not** yet implement the streaming CH/D15 target recurrence and did not solve a new Pu from the infinite limit. Existing finite-order Case21/Z6 capacities remain diagnostics only for the next regression.

---

# 11. Stage-I decision

```text
TRUE_INFINITE_R10_SERIES_ARCHITECTURE = PASS
FINITE_BAND_SOURCE_RECURRENCES = PASS
PHYSICAL_KNOT_CONVERGENCE_LAW = PASS
SAME_SOURCE_FIRST_TANGENT_CONVERGENCE = PASS
TERM_BY_TERM_EXACT_D15_LIMIT_THEOREM = PASS
NEW_Pu_RELEASE = NO
```

## Unique next executable task

```text
STREAMING_R10_SEQUENCE
 -> 2x2 CH TERM GENERATOR
 -> TARGET_FIRST_D15 MOMENT SEQUENCE J_n
 -> analytic/tail-law n->infinity summation
 -> finite P,Rq,RA,tangent functions
 -> coupled Z6 / Case21 solve
```

This is a continuation of one theory, not a new route.
