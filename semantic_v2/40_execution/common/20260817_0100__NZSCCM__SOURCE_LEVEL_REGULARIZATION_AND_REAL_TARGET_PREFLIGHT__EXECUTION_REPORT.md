# NZ-SCCM — source/matrix-level regularization + real R10 target preflight

**Timestamp:** 2026-08-17 01:00 +08:00  
**Status:** EXECUTED / PARTIAL PASS TO COMPACT TARGET-PERIOD BOUNDARY

## 0. Scope

This execution continues from the accepted 2026-08-16 21:18 compact R10 target DAG and fixed 64-state algebraic-field result.

It does **not** compute a new Pu and does **not** reopen N48/high-order coefficient enumeration.

Formal counters remain:

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

User correction entering this gate:

```text
Z6_BOUNDARY = FOUR_EDGE_SIMPLY_SUPPORTED / SSSS
```

Any earlier current-mainline description of Z6 as a mixed in-plane-boundary case is superseded.

---

## 1. First objective: determine whether the 21:36 apparent pole is physical

Retain the noncommuting affine thickness pencil used by the 20:59/21:36 exact-branch audit:

\[
E(x)=\begin{bmatrix}
1/5+x/3 & 1/7+x/5\\
1/7+x/5 & -1/4+2x/7
\end{bmatrix}.
\]

For the smooth R10 atom define

\[
M(x)=E(x)^2+\eta^2I,
\qquad R(x)=\sqrt{M(x)}.
\]

The old rationalized quadratic-tower connection produced

\[
A^2-4Q
=\frac{(260x-21)^2(28624x^2+47880x+50121)}{31116960000},
\]

hence the apparent pole

\[
x_*=21/260=0.080769230769\ldots.
\]

At exactly this point,

\[
E(x_*)=
\begin{bmatrix}
59/260 & 1447/9100\\
1447/9100 & -59/260
\end{bmatrix},
\]

so

\[
\operatorname{tr}E(x_*)=0,
\qquad
E(x_*)^2=\frac{3179017}{41405000}I.
\]

For the retained prototype `eta=1/400`,

\[
M(x_*)=\frac{4069473}{52998400}I,
\]

and therefore

\[
R(x_*)=\frac{\sqrt{4069473}}{7280}I
=0.27710075327665486951\,I.
\]

The principal square-root derivative is obtained directly from the Sylvester equation

\[
\boxed{RR'+R'R=M'.}
\]

Because `R(x*)` is a positive scalar multiple of the identity, the Sylvester operator eigenvalues are all

\[
2R_*=0.55420150655330973902,
\]

and

```text
cond2(Sylvester operator at x*) = 1
```

rather than singular.

The exact/numerical derivative is finite:

\[
R'(x_*)\approx
\begin{bmatrix}
+0.387740640083909 & +0.177616576255538\\
+0.177616576255538 & -0.119209228565276
\end{bmatrix}.
\]

For the actual Case21 material `kappa=386099/193000`,

```text
eta = 965/386099 = 0.0024993589726987119884
R(x*) = 0.27710074749405488380 I
2 R(x*) = 0.55420149498810976759 I
```

so the same source-level regularity conclusion holds.

### Decision

```text
PHYSICAL_SMOOTH_MATRIX_SQRT_AT_xstar = REGULAR
SOURCE_LEVEL_SYLVESTER_DERIVATIVE_AT_xstar = REGULAR / WELL_CONDITIONED
OLD_c0_c1_APPARENT_POLE = REPRESENTATION_ARTIFACT
HAND_PATCHING_c0_c1 = NOT REQUIRED
```

The previous rationalized connection must therefore not be repaired term by term. The source/matrix function is the correct regular object.

---

## 2. Direct comparison with the old divergent connection

At the same `x*`, the old separate coefficients diverge while their physical combination stays finite.

For `h=1e-3`:

```text
x=x*-h: c0=-499.758..., c1=+6521.18..., c0+c1*q=.484478...
x=x*+h: c0=+500.242..., c1=-6502.25..., c0+c1*q=.484596...
```

For `h=1e-5`:

```text
x=x*-h: c0=-49999.758..., c1=+651179.78..., c0+c1*q=.48453688...
x=x*+h: c0=+50000.242..., c1=-651160.85..., c0+c1*q=.48453808...
```

Exact limit:

\[
\boxed{
\lim_{x\to x_*}(c_0+c_1q)
=\frac{29577184}{61042095}
=0.48453749826246953025\ldots
}
\]

This confirms that continuing to manipulate `c0` and `c1` separately is the wrong production representation.

---

## 3. True source knots are different from the apparent pole

The 20:05 exact R10 source lift rewrites the tensile source as a C2 spline/truncated-power graph. Its two source-defined transition thresholds satisfy

\[
t(\lambda_1)=a,
\qquad
t(\lambda_{10})=10a,
\qquad a=\rho/\kappa.
\]

For the actual Case21 material:

```text
kappa = 2.0005129533678756477
rho   = .1
a     = .04998717945397423977
eta   = .002499358972698711988
lambda1  = .05008051764913754367
lambda10 = .49988116674539300084
```

For the retained affine thickness prototype, solving analytically

\[
\det(E(x)-\lambda_m I)=0
\]

produces the in-thickness material events

```text
lambda1 crossing  x = -0.4667260750489900...
lambda10 crossing x = +0.5655380435733645...
```

(the second roots lie outside the complete thickness interval).

These are genuine source-knot events, not fake singularities.

The underlying source spline satisfies exact C2 matching:

```text
jump at z=1  : value=0, first derivative=0, second derivative=0
jump at z=10 : value=0, first derivative=0, second derivative=0
```

The retained truncated-power coefficients at `rho=.1`, `H=.09799750427197301`, `UR=.03` are

```text
A3 = -0.580907793121266081
A4 = -0.769807105679339153
A5 = -0.287991934894071660
B3 = +0.000932750401535980933
B4 = +0.000155458400255996822
B5 = +0.00000690926223359985876
```

### Projector-free source form

For a symmetric matrix `D`, instead of a singular `sign(D)`/spectral-projector representation, use the exact identity

\[
\boxed{
D_+^p
=\left(\frac{D+|D|}{2}\right)^p,
\qquad |D|=\sqrt{D^2},
\qquad p=3,4,5.
}
\]

This represents the actual C2 truncated-power source without dividing by the vanishing eigenvalue at a knot.

For the consistent tangent, the matrix function `f_p(z)=z_+^p` is differentiated by its finite divided-difference/Fréchet derivative, not by differentiating a standalone singular sign projector.

Therefore the true knot can remain a material event while the value/tangent source DAG remains finite.

---

## 4. Real target-specific algebraic preflight

To avoid another toy-only gate, this execution selected a **real term of the 21:18 compact stress target**:

\[
\boxed{Y_c(x)=\det C(x)\,C_{yy}(x).}
\]

It is the actual compression-interaction subtarget entering

\[
S_{yy}=U_{yy}-a_{cc}\det(C)C_{yy}+\cdots.
\]

For the retained exact rational prototype `kappa=2`, `eta=1/400`, the source algebra uses only the smooth quadratic pair

\[
q^2=Q(x),\qquad s^2=A(x)+2q,
\]

with basis

\[
[1,q,s,qs].
\]

The complete matrix chain

```text
R=sqrt(E^2+eta^2 I)
 -> c=Pi_eta(-E)
 -> C=kappa*c*(I+(kappa-2)c+c^2)^(-1)
 -> Yc=det(C)*Cyy
```

was executed exactly in this four-state field.

Observed field support:

```text
Yc support = 4 / 4 states
```

The multiplication-by-`Yc` operator is a 4x4 matrix over `Q(x)`. Its characteristic polynomial

\[
P_c(x,Y)=\det(YI-M_{Y_c})
\]

was constructed successfully.

```text
DEGREE_Y(Pc) = 4
characteristic-polynomial construction runtime ~ 0.9 s in the retained SymPy prototype
coefficient expression-operation counts ~ [0, 230, 473, 464, 455]
```

Therefore the real compression target is indeed a compact algebraic period of degree at most four; it does **not** require a high-order material series.

For audit only, direct high-precision quadrature of this prototype target gives

\[
\int_{-1}^{1}Y_c(x)\,dx
\approx
0.03256204357343014004437563917901173297.
\]

This number is an independent oracle only; no production resultant uses quadrature.

---

## 5. A second fail-fast: explicit annihilator canonicalization is also the wrong implementation

After the successful degree-4 minimal-polynomial construction, two exact attempts were made to convert `P_c(x,Y)` into a fully canonical scalar differential annihilator by explicitly inverting `P_Y` modulo `P` over `Q(x)`.

Both exceeded the 60 s symbolic execution boundary:

```text
route A: expand/convert P_x + modular inverse -> >60 s
route B: coefficient-wise Q(x) construction + modular inverse -> >60 s
```

A separate direct differentiation of the already-reduced four-state target likewise showed rapid rational-expression swell by derivative order 3.

This is not a failure of algebraicity; the algebraic degree is only four. It is a failure of **canonicalizing large rational coefficient functions in the current SymPy representation**.

### Decision

```text
REAL_TARGET_ALGEBRAIC_DEGREE_BOUND = PASS_COMPACT
EXPLICIT_CANONICAL_RATIONAL_ANNIHILATOR_IN_SYMPY = FAIL_TRACTABILITY
DO_NOT_FIX_BY_INCREASING_TIMEOUT_OR_EXPANDING_MORE = YES
DO_NOT_REOPEN_HIGH_ORDER_SERIES = YES
```

This is exactly the kind of intermediate implementation feedback that the project now requires: a mathematically small object can still be represented badly by a CAS, so the theory/runtime interface must remain factorized.

---

## 6. Surviving compact route

The surviving route is now narrowed to:

```text
GLOBAL REGULAR SOURCE/MATRIX DAG
  - principal matrix sqrt by Sylvester/Fréchet relation
  - positive-part spline powers in projector-free form
  - 2x2 Cayley-Hamilton reduction

        ↓

FACTORISED TARGET ALGEBRAIC OBJECT
  - no c0/c1 separation
  - no final 64-coefficient canonicalization
  - no giant rational-function annihilator expansion

        ↓

ALGEBRAIC-PERIOD / DESCRIPTOR EVALUATOR
  - retain finite algebraic degree/state
  - derive/evaluate target moment without enumerating thousands of coefficients
```

The old 64-state result remains useful as a rigorous finite-degree/state bound, but the runtime need not literally canonicalize 64 rational coefficient functions.

The next implementation must keep the target in factor-graph / descriptor form and operate on the finite algebraic object directly.

---

## 7. Gate result

```text
Z6_BOUNDARY = SSSS / FOUR-EDGE SIMPLY SUPPORTED
SMOOTH_APPARENT_POLE_PHYSICAL = NO
SOURCE_LEVEL_SYLVESTER_REGULARITY = PASS
TRUE_FOSTER_KNOT_CLASSIFICATION = PASS
PROJECTOR_FREE_POSITIVE_PART_SOURCE_FORM = PASS_FORMAL
REAL_TARGET_Yc_ALGEBRAIC_DEGREE = 4 / PASS
REAL_TARGET_Yc_PERIOD_IDENTITY = ESTABLISHED
EXPLICIT_SYMPY_ANNIHILATOR_CANONICALIZATION = FAIL_TRACTABILITY
HIGH_ORDER_COEFFICIENT_ESCAPE = PROHIBITED
NEW_Pu = NOT_RUN
```

## 8. Next direct task

The next task is no longer “regularize c0/c1”. That problem is closed by returning to the regular source/matrix function.

The direct next task is:

```text
FULL_COMPACT_R10_FACTOR_GRAPH_ALGEBRAIC_PERIOD_TARGET_EVALUATOR
```

Required output:

1. take an actual full 21:18 `Syy`/`Rm` target, not a toy;
2. retain the global regular source DAG and finite algebraic-state bound;
3. construct/evaluate its complete-thickness algebraic-period contribution without explicit rational coefficient canonicalization and without high-order coefficient enumeration;
4. return the value and consistent derivative package needed by `P/Rm`;
5. if the factorised period backend cannot keep a fixed finite bound, stop there and report the mathematical blocker rather than generating another backend chain.
