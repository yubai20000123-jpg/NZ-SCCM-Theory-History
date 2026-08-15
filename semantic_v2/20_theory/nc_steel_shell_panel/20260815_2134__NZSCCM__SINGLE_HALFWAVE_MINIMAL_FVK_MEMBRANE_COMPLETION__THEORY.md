# NZ-SCCM — 单一完整面外半波的最小 FvK 膜力重分布补全系统

**Timestamp:** 2026-08-15 21:34 +08:00  
**Purpose:** determine whether the existing `D+q+c` theory can exactly capture the membrane redistribution forced by Nguyen second-order kinematics, and construct the minimum analytic completion without changing D15 integration.

---

## 1. Coordinates and frozen out-of-plane field

Use

\[
X=\pi x/b,\qquad Y=\pi y/a,\qquad k=b/a.
\]

The out-of-plane field is unchanged:

\[
w_0=A_0\sin X\sin Y,\qquad
w_m=A\sin X\sin Y.
\]

No `q31`, `q13` or other out-of-plane harmonic is introduced.

Nguyen Eq.(6.3) produces the already-audited second-order membrane source. Under the FvK compatibility operator, the incremental geometric source contains independent `cos(2X)` and `cos(2Y)` directions plus a homogeneous membrane field fixed by mean loading and in-plane boundary conditions.

---

## 2. Existing D-q-c in-plane space

The full-current boundary-warp implementation currently uses, for the normalized mid-plane in-plane strain directions,

### Mean axial coordinate D

\[
\varepsilon_{x,D}/\varepsilon_0=0,\qquad
\varepsilon_{y,D}/\varepsilon_0=-1.
\]

### Boundary warp coordinate c

With `x_s=sin X`, `y_s=sin Y`,

\[
\frac{\varepsilon_{x,c}}{\varepsilon_0}
=\frac{4}{\pi}\sin X\sin^2Y,
\]

\[
\frac{\varepsilon_{y,c}}{\varepsilon_0}
=\frac{8k^2}{\pi}\sin X\cos 2Y.
\]

The associated linear shear is zero by construction.

Thus the exact X-harmonic content of the retained independent in-plane directions is only:

```text
D : X-harmonic 0
c : X-harmonic 1 (sin X)
```

The FvK compatibility source requires an independent X-harmonic 2 (`cos 2X`) response and an independent X-harmonic 0 / Y-harmonic 2 (`cos 2Y`) response.

---

## 3. Exact span proof: D+c cannot represent both FvK redistribution directions

### 3.1 Missing `(2,0)` direction

Any linear combination of the existing independent in-plane virtual strains has

\[
\varepsilon_x^{trial}
=\alpha\,0
+\beta\frac{4}{\pi}\sin X\sin^2Y.
\]

To reproduce a `cos 2X`-type admissible response would require, for nonzero `sin^2Y`,

\[
\cos 2X=C\sin X
\]

for all `X in [0,pi]`, which is impossible.

Therefore the current `D+c` in-plane span contains no exact X-second-harmonic redistribution direction.

### 3.2 Missing pure `(0,2)` direction

To produce a pure `cos 2Y` axial redistribution with zero accompanying `eps_x`, the coefficient of `c` must be zero because `eps_x,c` is nonzero. The remaining D direction is spatially uniform and cannot produce `cos 2Y`.

Therefore the current `D+c` span also cannot exactly reproduce the independent pure Y-second-harmonic redistribution direction.

Hence

```text
D_PLUS_C_EXACT_FVK_SOURCE_SPAN = FAIL
```

This is a function-space/rank result and does not depend on a new Z6 load calculation.

---

## 4. Minimal admissible completion basis

The new basis must satisfy the Zhou loaded-edge essential in-plane conditions already adopted in the boundary-warp audit:

```text
u(x,0)=u(x,a)=0
warping part of v(x,0)=v(x,a)=0
```

while the non-loaded side edges retain no imposed in-plane displacement.

Two dimensionless generalized coordinates are sufficient to add the missing FvK source directions at minimum order.

### 4.1 p20 direction — X-second-harmonic redistribution

Define the displacement field per unit `p20`:

\[
U_{20}=\frac{b}{2\pi}\sin2X\,\sin^2Y,
\]

\[
V_{20}=\frac{b^2}{4\pi a}\cos2X\,\sin2Y.
\]

The physical displacement contribution is

\[
u_{20}=\varepsilon_0p_{20}U_{20},\qquad
v_{20}=\varepsilon_0p_{20}V_{20}.
\]

It satisfies exactly

\[
U_{20}(Y=0,\pi)=0,
\qquad
V_{20}(Y=0,\pi)=0.
\]

Its normalized virtual strains are

\[
e_{x,20}=\cos2X\,\sin^2Y,
\]

\[
e_{y,20}=\frac{k^2}{2}\cos2X\cos2Y,
\]

\[
\gamma_{xy,20}=0.
\]

The zero shear follows identically from `U20,y + V20,x = 0`.

In the existing polynomial variables `xs=sin X`, `ys=sin Y`,

\[
e_{x,20}=y_s^2-2x_s^2y_s^2,
\]

\[
e_{y,20}=\frac{k^2}{2}(1-2x_s^2)(1-2y_s^2).
\]

Therefore the field is directly D15-compatible.

### 4.2 p02 direction — Y-second-harmonic redistribution

Define

\[
U_{02}=0,
\qquad
V_{02}=\frac{a}{2\pi}\sin2Y.
\]

with physical contribution

\[
v_{02}=\varepsilon_0p_{02}V_{02}.
\]

It satisfies `V02=0` on both loaded edges and gives

\[
e_{x,02}=0,
\qquad
e_{y,02}=\cos2Y=1-2\sin^2Y,
\qquad
\gamma_{xy,02}=0.
\]

This is also an exact finite D15 polynomial field.

---

## 5. Minimum augmented in-plane field

The in-plane displacement field becomes

\[
u=u_c(c)+u_{20}(p_{20}),
\]

\[
v=-\varepsilon_0Dy+v_c(c)+v_{20}(p_{20})+v_{02}(p_{02}).
\]

The out-of-plane field remains exactly the existing one-halfwave `q` field.

The generalized coordinate identity is therefore

```text
external/loading coordinate: D
out-of-plane coordinate:      q
membrane coordinates:         m=[c,p20,p02]^T
```

No additional physical spatial subdivision is introduced.

---

## 6. Generalized residual system with the unchanged current material operator

For any retained coordinate `r`, define

\[
R_r=\int_V \boldsymbol\sigma(\boldsymbol\varepsilon)^T
\frac{\partial\boldsymbol\varepsilon}{\partial r}\,dV.
\]

The same current stress operator is retained:

\[
\varepsilon\rightarrow M(\varepsilon)\rightarrow\sigma.
\]

At fixed `(D,q)`, the membrane subsystem is

\[
\mathbf R_m=
\begin{bmatrix}
R_c\\R_{20}\\R_{02}
\end{bmatrix}
=\mathbf0.
\]

The transverse equilibrium remains

\[
R_q=0.
\]

No scalar potential is required for this definition; it is the same generalized virtual-work form already used for `Rq` and `Rc`.

---

## 7. Flat 3x3 static condensation

Define

\[
\mathbf J_{mm}=\frac{\partial\mathbf R_m}{\partial\mathbf m},
\qquad
\mathbf J_{mq}=\frac{\partial\mathbf R_m}{\partial q}.
\]

At a membrane-equilibrated state,

\[
\frac{d\mathbf m}{dq}
=-\mathbf J_{mm}^{-1}\mathbf J_{mq}.
\]

The condensed out-of-plane tangent is

\[
L_{cond}
=R_{q,q}
-\mathbf R_{q,m}\mathbf J_{mm}^{-1}\mathbf J_{m,q}.
\]

This uses only a flat `3x3` membrane matrix plus vectors/scalars. It does not require nested submatrices or a monolithic large FE matrix.

---

## 8. Why the formal integration is unchanged

All added normalized strain directions are finite polynomials of `sin X` and `sin Y`:

```text
e20x = y^2 - 2 x^2 y^2
e20y = (k^2/2)*(1 - 2x^2)*(1 - 2y^2)
e02x = 0
e02y = 1 - 2y^2
g20 = g02 = 0
```

They enter the same finite Nguyen strain algebra before the current material map. Consequently:

```text
R20, R02, their Jacobian entries, and the condensed tangent
= exact coefficient-space moment contractions
```

using the same General D15 rules.

No Gauss, Simpson, adaptive quadrature, spatial cells, material-point grid, or Chebyshev spatial collocation is created.

---

## 9. Status after this construction

Established now:

```text
DQC exact FvK membrane-source span = FAIL
minimum additional source directions required = 2
minimal analytic admissible basis = p20 + p02
loaded-edge boundary admissibility = PASS by construction
linear shear of both added directions = ZERO
D15 finite exact-moment compatibility = PASS
flat 3x3 membrane condensation architecture = ESTABLISHED
```

Not yet established:

```text
R20/R02 magnitude on existing nonlinear Z6 states
new membrane-equilibrated q,c,p20,p02 state
corrected Z6 Pu
full nonlinear PDE completeness beyond this minimum FvK-source basis
```

The immediate next execution is therefore an **existing-state residual-projection gate** using the unchanged R10/N48/Cayley-Hamilton/local-steel/D15 operator. No new Pu may be calculated before that gate is inspected.