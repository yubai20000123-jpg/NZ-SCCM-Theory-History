# NZ-SCCM — corrected Z6 N48-family source compiler + Airy membrane redistribution

**Timestamp:** 2026-08-17 14:07 +08:00

## 1. Correct representative halfwave

The physical Z6 plate is

\[
a=24000\text{ mm},\qquad b=12000\text{ mm},\qquad m^*=2,
\]

so the single formal representative halfwave is

\[
\ell=a/m^*=12000\text{ mm}=b.
\]

Hence

\[
X=\pi x/b,\qquad Y=\pi y/\ell,
\qquad k=b/\ell=1.
\]

With `A0=a/500=48 mm`, `q0=A0/b=.004`.

## 2. Retained Airy scalar redistribution

For the square representative halfwave

\[
a(\nu)=\left[-\frac{1+\nu}{4},-\frac{1-\nu}{4},\frac14,-\frac{1-\nu}{4},\frac14\right]^T.
\]

At `nu=.18`,

\[
a=[-0.295,-0.205,0.25,-0.205,0.25]^T.
\]

Define

\[
M=\frac{\pi^2}{\varepsilon_0}\left(q_0q+\frac12q^2\right),
\qquad
B=\frac{\pi^2t_c}{2\varepsilon_0 b}q.
\]

Then the normalized core strains are

\[
\begin{aligned}
e_x={}&\nu D+M\cos^2X\sin^2Y+\lambda M B_A^x+B\sin X\sin Y\,\zeta,\\
e_y={}&-D+M\sin^2X\cos^2Y+\lambda M B_A^y+B\sin X\sin Y\,\zeta,\\
\gamma_{xy}={}&\frac M2(1-\lambda)\sin2X\sin2Y-2B\cos X\cos Y\,\zeta,
\end{aligned}
\]

with

\[
B_A^x=-\frac{1+\nu}{4}-\frac{1-\nu}{4}\cos2X+\frac14\cos2X\cos2Y,
\]

\[
B_A^y=-\frac{1-\nu}{4}\cos2Y+\frac14\cos2X\cos2Y.
\]

The production branch conditions are

\[
R_q^{base}=0,\qquad R_A=a^TR_m=0.
\]

This is the constrained membrane-stress redistribution direction; it is neither `r=0` nor the previously over-released five-independent-coordinate family.

## 3. N48-family compiler

The physical R10 scalar sources remain unchanged. Only the analytic representation is rebuilt.

For each source

\[
F\in\{U,C,T,T^7\},
\]

use the normalized material coordinate

\[
\xi=\frac{\lambda-\lambda_c}{h_\lambda},
\]

and a C1-constrained Chebyshev representation

\[
F_N(\lambda)=\sum_{n=0}^{N}c_nT_n(\xi).
\]

The prototype order is `48`; the convergence family uses

\[
N=48,96,144,192,240,288.
\]

The constraints at `lambda=0` preserve the source origin identities:

```text
U(0)=0, U'(0)=kappa
C(0)=0, C'(0)=0
T(0)=0, T'(0)=0
T7(0)=0, T7'(0)=0
```

The corrected Z6 peak neighborhood uses

\[
\lambda\in[-1.75,1.45].
\]

## 4. Why this is an N48 prototype rather than literal N48 copying

The old implementation asked one order-48 polynomial to represent the whole wide Z6 material range. That is the part being discarded.

N48 now acts as the **spectral block / refinement quantum**. Increasing from 48 to 96, 144, ... asks whether the source-generated structural targets have converged. No capacity comparator enters the order choice.

The underlying limiting representation is the convergent Chebyshev source series

\[
F(\lambda)=\sum_{n=0}^{\infty}c_nT_n(\xi).
\]

Every finite partial member is a finite material polynomial. After 2x2 Cayley-Hamilton lifting, every retained term composes with the finite Nguyen trigonometric field and therefore has finite exact General-D15 moments.

This realizes the intended architecture:

```text
convergent material series
+ finite retained partial sum
+ finite exact structural moments for every retained term
```

rather than spatial numerical integration.

## 5. Full section phases

The corrected Z6 section contains, before branch solution:

1. effective R10 concrete core factor `1-rho_w=.98`;
2. two steel faceplates, ideal elastic-perfectly-plastic local radial cap;
3. longitudinal web/PBL phase homogenized through the core at `rho_w=.02`.

No web force is appended after solving; all phases contribute to `P`, `Rq`, and `RA` before the branch root.

## 6. Formal moment identity

For a finite source order, set

\[
Y=(X-\lambda_cI)/h_\lambda.
\]

Each scalar Chebyshev term is lifted by

\[
T_n(Y)=A_n(I_1,I_2)I+B_n(I_1,I_2)Y
\]

using the 2x2 Cayley-Hamilton recurrence. Since the strain invariants are finite trigonometric-thickness polynomials, all requested contractions reduce to finite sums of

\[
\int_0^\pi\sin^pX\,dX,
\quad
\int_0^\pi\sin^qY\,dY,
\quad
\int_{-1}^{1}\zeta^r\,d\zeta.
\]

Therefore the material refinement order changes only the number of analytic terms; it does not introduce structural spatial points.

## 7. Engineering convergence criterion used in the 14:07 execution

The order gate is assessed by consecutive source-family capacity changes and same-resolution comparison to the raw-R10 mechanics oracle. The comparator loads from Zhou/Winter are excluded from this gate.

The corrected Z6 execution shows that the N192-N288 family is already clustered within a few hundredths of a MN around 48.42 MN; this is far smaller than the previously observed error from literal wide-domain N48 copying and smaller than the model-to-comparator discrepancy.
