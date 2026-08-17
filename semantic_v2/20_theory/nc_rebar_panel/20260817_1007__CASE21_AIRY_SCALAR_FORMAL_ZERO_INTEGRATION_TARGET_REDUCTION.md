# NZ-SCCM — Case21 Airy-scalar formal zero-integration target reduction

**Timestamp:** 2026-08-17 10:07 +08:00  
**Status:** DERIVATION CLOSED AT STRUCTURAL TARGET LEVEL / FORMAL NUMERIC RELEASE STILL OPEN

## 0. Identity

This note continues the active Case21 closure

\[
\mathbf r=\lambda M\mathbf a(\nu),
\qquad
\mathbf a(\nu)=\left[-\frac{1+\nu}{4},-\frac{1-\nu}{4},\frac14,-\frac{1-\nu}{4},\frac14\right]^T,
\]

with

\[
M=\frac{\pi^2}{\varepsilon_0}\left(q_0q+\frac12q^2\right).
\]

It does **not** modify R10, the one-complete-halfwave domain, reinforcement, or the current direct-source mechanics target `Pu = 366.767829 kN`.

The purpose is to reduce the remaining formal zero-spatial-integration task after the five-free membrane coordinates were superseded.

Formal counters remain

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

The direct-source Gauss result remains audit-only until the descriptor below is implemented and solved.

---

## 1. Airy-scalar kinematics in low Fourier form

Let

\[
C_X=\cos2X,\quad C_Y=\cos2Y,\quad S_X=\sin2X,\quad S_Y=\sin2Y.
\]

The base Nguyen complete-halfwave membrane terms are

\[
M\cos^2X\sin^2Y=\frac M4(1+C_X-C_Y-C_XC_Y),
\]

\[
M\sin^2X\cos^2Y=\frac M4(1-C_X+C_Y-C_XC_Y),
\]

\[
2M\sin X\cos X\sin Y\cos Y=\frac M2S_XS_Y.
\]

After substituting `r=lambda*M*a(nu)`, the full normalized strains become

\[
\boxed{
\begin{aligned}
e_x={}&\nu D+\frac M4\Big[1+C_X-C_Y-C_XC_Y\\
&-\lambda(1+\nu)-\lambda(1-\nu)C_X+\lambda C_XC_Y\Big]\\
&+B\sin X\sin Y\,\zeta,
\end{aligned}}
\]

\[
\boxed{
\begin{aligned}
e_y={}&-D+\frac M4\Big[1-C_X+C_Y-C_XC_Y\\
&-\lambda(1-\nu)C_Y+\lambda C_XC_Y\Big]\\
&+B\sin X\sin Y\,\zeta,
\end{aligned}}
\]

\[
\boxed{
\gamma_{xy}=\frac M2(1-\lambda)S_XS_Y-2B\cos X\cos Y\,\zeta,
}
\]

where

\[
B=\frac{\pi^2}{2\varepsilon_0}\frac tb q.
\]

At the elastic Airy limit `lambda=1`, the membrane shear term vanishes exactly.

The normalized strain tensor is still mapped through the frozen R10 current operator without any new material approximation.

---

## 2. Exact thickness moment interface

Define

\[
N_x^{(k)}(X,Y)=\int_{-1}^{1}\zeta^k\sigma_x(X,Y,\zeta)\,d\zeta,
\]

\[
N_y^{(k)}(X,Y)=\int_{-1}^{1}\zeta^k\sigma_y(X,Y,\zeta)\,d\zeta,
\]

\[
N_{xy}^{(k)}(X,Y)=\int_{-1}^{1}\zeta^k\tau_{xy}(X,Y,\zeta)\,d\zeta.
\]

The already-selected production representation remains the global fixed-endpoint branch-free factorised R10 period, evaluated between `zeta=-1,+1`; no moving material-event endpoint is exposed to the XY layer.

For the current scalar closure the structural target no longer needs five independent `Rm` values. It needs only

```text
P, RA, Rq
```

and their same-source parameter derivatives.

---

## 3. Direct Airy projection replaces all five Rm outputs

The retained Airy virtual-strain basis is

\[
B_A^x=-\frac{1+\nu}{4}-\frac{1-\nu}{4}C_X+\frac14C_XC_Y,
\]

\[
B_A^y=-\frac{1-\nu}{4}C_Y+\frac14C_XC_Y,
\]

\[
B_A^{\gamma}=-\frac12S_XS_Y.
\]

Therefore the concrete Airy scalar residual is obtained directly as

\[
\boxed{
R_A^c=C_{vol}\int_0^\pi\!\int_0^\pi
\left(B_A^xN_x^{(0)}+B_A^yN_y^{(0)}+B_A^{\gamma}N_{xy}^{(0)}\right)dYdX,
}
\]

with

\[
C_{vol}=\frac{\varepsilon_0 b\ell t}{2\pi^2}.
\]

Thus the formal implementation does not need to materialize the five-component `Rm` vector and contract it afterward.

---

## 4. Rq needs only k=0 and k=1 stress moments

Define

\[
M_q=\frac{\pi^2}{\varepsilon_0}(q_0+q),
\qquad
B_q=\frac{\pi^2}{2\varepsilon_0}\frac tb.
\]

Because `r=lambda*M*a`, differentiation with respect to `q` at fixed `lambda` contains an additional term `lambda*M_q*a`. Its virtual work is proportional to `a^T Rm`, hence it vanishes identically on the retained internal equilibrium `RA=0`. Therefore the outer residual may use the base Nguyen q-derivative without losing any branch-equilibrium term.

The exact concrete q residual is

\[
\boxed{
\begin{aligned}
R_q^c=C_{vol}\int\!\int\Big\{&M_q\big[
\cos^2X\sin^2Y\,N_x^{(0)}
+\sin^2X\cos^2Y\,N_y^{(0)}\\
&+2\sin X\cos X\sin Y\cos Y\,N_{xy}^{(0)}\big]\\
&+B_q\big[
\sin X\sin Y(N_x^{(1)}+N_y^{(1)})
-2\cos X\cos YN_{xy}^{(1)}\big]\Big\}\,dYdX.
\end{aligned}}
\]

No stress moment above order `k=1` is required for the values of `P,RA,Rq`.

---

## 5. Collapse the full XY requirement to a finite 12-target moment vector

For any stress component define

\[
\mathcal J_{\alpha,k}[w]=\int_0^\pi\!\int_0^\pi w(X,Y)N_\alpha^{(k)}(X,Y)\,dYdX.
\]

At `k=0`, only the four cosine weights

```text
1, cos2X, cos2Y, cos2X cos2Y
```

are needed for `Nx0` and `Ny0`, plus

```text
sin2X sin2Y
```

for `Nxy0`.

At `k=1`, only

```text
sinX sinY   for Nx1 and Ny1
cosX cosY   for Nxy1
```

are needed.

Hence the complete concrete value-level target is the fixed 12-scalar vector

\[
\boxed{
\begin{aligned}
\mathcal T_{12}=\{&J_{x,00},J_{x,20},J_{x,02},J_{x,22c},\\
&J_{y,00},J_{y,20},J_{y,02},J_{y,22c},\\
&J_{xy,22s},J_{x,11s}^{(1)},J_{y,11s}^{(1)},J_{xy,11c}^{(1)}\}.
\end{aligned}}
}
\]

The concrete load is simply

\[
\boxed{P_c=-\frac{bt}{2\pi^2}J_{y,00}.}
\]

The Airy residual is

\[
\boxed{
R_A^c=C_{vol}\left[
-\frac{1+\nu}{4}J_{x,00}
-\frac{1-\nu}{4}J_{x,20}
+\frac14J_{x,22c}
-\frac{1-\nu}{4}J_{y,02}
+\frac14J_{y,22c}
-\frac12J_{xy,22s}
\right].
}
\]

Using

\[
\cos^2X\sin^2Y=\frac14(1+C_X-C_Y-C_XC_Y),
\]

\[
\sin^2X\cos^2Y=\frac14(1-C_X+C_Y-C_XC_Y),
\]

and

\[
2\sin X\cos X\sin Y\cos Y=\frac12S_XS_Y,
\]

we obtain

\[
\boxed{
\begin{aligned}
R_q^c=C_{vol}\Bigg\{\frac{M_q}{4}\Big[&
J_{x,00}+J_{x,20}-J_{x,02}-J_{x,22c}\\
&+J_{y,00}-J_{y,20}+J_{y,02}-J_{y,22c}\\
&+2J_{xy,22s}\Big]\\
+B_q\Big[&J_{x,11s}^{(1)}+J_{y,11s}^{(1)}-2J_{xy,11c}^{(1)}\Big]\Bigg\}.
\end{aligned}}
}
\]

This means the formal XY layer does **not** need a reconstructed stress surface, a spatial grid, or thousands of Fourier/Chebyshev coefficients. It only needs a direct exact/period evaluator for these 12 target moments.

---

## 6. Reinforcement remains exact and does not enlarge the formal integration problem

At the current Case21 peak the two reinforcement directions remain elastic. At `zeta=0`, all required steel integrals reduce by Fourier orthogonality to finite closed forms.

In particular, the axial steel load remains independent of `lambda` because the Airy correction has zero mean in the loading-direction reinforcement strain:

\[
\boxed{
P_s=\rho_{s,y}tbE_s\varepsilon_0\left(D-\frac M4\right)
}
\]

(before the reporting unit conversion).

The steel contributions to `RA` and `Rq` are likewise finite Fourier moments of linear elastic strain and require no material compiler, no quadrature, and no spatial sampling.

---

## 7. Formal limit-state equation for the 3-variable scalar-closure branch

The current branch is defined by

\[
F_1(D,q,\lambda)=R_q=0,
\qquad
F_2(D,q,\lambda)=R_A=0.
\]

Let

\[
J_F=
\begin{bmatrix}
R_{q,q}&R_{q,\lambda}\\
R_{A,q}&R_{A,\lambda}
\end{bmatrix}.
\]

Along the connected branch, the first stationary load point satisfies

\[
\frac{dP}{dD}=0.
\]

Eliminating `dq/dD` and `dlambda/dD` gives the exact bordered determinant condition

\[
\boxed{
L_3=
\det
\begin{bmatrix}
P_{,D}&P_{,q}&P_{,\lambda}\\
R_{q,D}&R_{q,q}&R_{q,\lambda}\\
R_{A,D}&R_{A,q}&R_{A,\lambda}
\end{bmatrix}=0.
}
\]

Therefore the formal Case21 ultimate state is the connected solution of

\[
\boxed{R_q=0,\qquad R_A=0,\qquad L_3=0.}
\]

All derivatives must be obtained from the same formal period/target descriptor; finite-difference production derivatives are not required.

---

## 8. New unique formal implementation gate

The old five-free-coordinate `P + five Rm` output interface is now unnecessarily large for Case21.

The unique remaining formal gate is reduced to

```text
CASE21_AIRY_SCALAR_DIRECT_12_TARGET_PERIOD_GATE
```

Input:

```text
(D,q,lambda)
```

Output:

```text
T12(D,q,lambda)
+ same-source parameter derivatives wrt D,q,lambda
```

Requirements:

1. frozen direct R10 source DAG;
2. global fixed-endpoint branch-free factorised period representation;
3. no numerical zeta/X/Y quadrature;
4. no spatial sampling/collocation/DCT;
5. one complete continuous halfwave;
6. no explicit high-order coefficient enumeration as production representation;
7. return `P,RA,Rq` from the 12 target moments;
8. return same-source derivatives and solve `Rq=RA=L3=0`;
9. compare only afterward against the read-only direct-source oracle `366.767829 kN`.

Until this gate is executed, the formal numeric release remains OPEN.

---

## 9. Status after this derivation

```text
CASE21_DIRECT_SOURCE_MECHANICS_TARGET_Pu = 366.767829 kN
CASE21_DIRECT_SOURCE_EXECUTOR = HIGH_ORDER_GAUSS_AUDIT_ONLY
CASE21_FORMAL_ZERO_SPATIAL_NUMERIC_RELEASE = OPEN
AIRY_SCALAR_VALUE_TARGET_REDUCTION = PASS
FULL_VALUE_TARGET_DIMENSION = 12 SCALARS
FORMAL_LIMIT_SYSTEM = Rq = 0, RA = 0, L3 = 0
NEXT_UNIQUE_GATE = CASE21_AIRY_SCALAR_DIRECT_12_TARGET_PERIOD_GATE
```
