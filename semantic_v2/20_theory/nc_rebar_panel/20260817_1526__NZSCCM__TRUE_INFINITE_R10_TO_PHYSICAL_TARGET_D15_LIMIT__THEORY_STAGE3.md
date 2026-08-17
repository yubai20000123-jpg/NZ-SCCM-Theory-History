# NZ-SCCM — true-infinite R10 -> physical P/Rq/RA/Kt D15 limit, Stage III

**Timestamp:** 2026-08-17 15:26 +08:00  
**Status:** THEORY STAGE-III CONNECTION PASS / LIMIT IDENTITY ESTABLISHED

## 0. Purpose

This stage connects the Stage-I true-infinite scalar material streams `U,C,T,T7` to the Stage-II general-n Cayley-Hamilton / General-D15 target streams and closes the mathematical `n -> infinity` operation for the physical targets.

The governing chain remains

```text
geometry/boundary
 -> complete representative halfwave
 -> frozen R10 source
 -> true infinite material coefficient streams
 -> membrane-redistributed Nguyen field
 -> same-source directional tangent
 -> exact nth-term CH/D15 moments
 -> n->infinity target limit
 -> finite P,Rq,RA,Kt
 -> coupled limit solve -> Pu.
```

No spatial Gauss/Simpson/cells/material-point grid is introduced into the formal operator.

---

## 1. Stage-I scalar streams

For each scalar R10 primitive `F in {U,C,T,T7}` write on a geometry-certified affine material interval

\[
F(\lambda)=\sum_{n=0}^{\infty} f_n T_n(\widehat\lambda),
\qquad
\widehat\lambda=(\lambda-c_0)/h.
\]

Stage I supplies the source-derived recurrences/generators and the physical-knot tail law. In particular the `C2` tensile joins imply for `T,U,T7`

\[
f_n=O(n^{-4}),
\]

while the smooth square-root kernel contribution is exponentially controlled by its complex singularity geometry.

The derivative stream is the derivative of the same identity,

\[
F_{,\lambda}=\frac1h\sum_{n=1}^{\infty}n f_n U_{n-1}(\widehat\lambda),
\]

and is uniformly/absolutely convergent on the certified real interval under the Stage-I bounds.

---

## 2. Matrix lift of every scalar stream

Let

\[
Y=(E-c_0I)/h,
\qquad \tau=\operatorname{tr}Y,
\qquad \delta=\det Y.
\]

Stage II gives, for every n,

\[
T_n(Y)=p_n(\tau,\delta)I+q_n(\tau,\delta)Y,
\]

with

\[
p_{n+1}=-2\delta q_n-p_{n-1},
\qquad
q_{n+1}=2p_n+2\tau q_n-q_{n-1}.
\]

Hence every infinite material matrix channel is

\[
\boxed{
F(Y)=A_F(\tau,\delta)I+B_F(\tau,\delta)Y
}
\]

with

\[
A_F=\sum_{n=0}^{\infty}f_np_n,
\qquad
B_F=\sum_{n=0}^{\infty}f_nq_n.
\]

The finite N48 representation was therefore a finite prefix of this matrix-stream architecture; the formal object is the converged infinite stream.

---

## 3. Full R10 stress operator: infinite-stream closure

The current 2x2 R10 stress operator is retained exactly as

\[
\boxed{
S
=U
-ACC\,\det(C)\,C
+C\,\operatorname{adj}(T)
-\rho AT\,\det(T)\,\operatorname{adj}(T7).
}
\]

All four matrix functions are functions of the same symmetric matrix `Y`; their CH pairs commute. For any pair

\[
F=A_FI+B_FY,\qquad G=A_GI+B_GY,
\]

the exact 2x2 product remains a CH pair,

\[
FG=
\left(A_FA_G-B_FB_G\delta\right)I
+\left(A_FB_G+B_FA_G+B_FB_G\tau\right)Y.
\]

Also

\[
\operatorname{tr}F=2A_F+B_F\tau,
\]

\[
\det F=A_F^2+A_FB_F\tau+B_F^2\delta,
\]

\[
\operatorname{adj}F=(A_F+B_F\tau)I-B_FY.
\]

Therefore `S` is obtained entirely by finite algebraic operations on the four convergent infinite streams. The required Cauchy/Chebyshev products are well-defined because the value streams converge uniformly and the material functions remain bounded on the certified compact interval.

This is the exact Stage-I -> Stage-II connection for the nonlinear cross-principal R10 terms; no independently fitted panel-level stress surrogate is introduced.

---

## 4. Physical target weights

For any generalized coordinate `z` (`D`, `q`, or an admissible membrane coordinate), define the equivalent-strain invariants

\[
I_1=\operatorname{tr}E,
\qquad I_2=\det E,
\]

and

\[
I_{1,z}=\partial I_1/\partial z,
\qquad
G_z=E:E_{,z}=I_1I_{1,z}-I_{2,z}.
\]

If

\[
S=A_SI+B_SY,
\]
then

\[
S:E_{,z}
=A_SI_{1,z}
+\frac{B_S}{h}\left(G_z-c_0I_{1,z}\right).
\]

Because the physical normalized strain tensor is

\[
e=(1+\nu)E-\nu\operatorname{tr}(E)I,
\]
its virtual-work density is

\[
\boxed{
Q_z
=(1+\nu)S:E_{,z}
-\nu\operatorname{tr}(S)I_{1,z}.
}
\]

Thus the concrete generalized residual is

\[
\boxed{
R_z^c
=\frac{f_c\varepsilon_0 b\ell t}{2\pi^2}
\,D15[Q_z].
}
\]

The axial load is

\[
\boxed{
P_c=-\frac{f_cbt}{2\pi^2}\,D15[S_{yy}].
}
\]

For the scalar Airy parameterization `alpha=lambda_A M`, production uses

```text
Rq_base : q derivative at fixed alpha
RA      : derivative with respect to alpha along the mechanically admitted Airy direction.
```

Writing the branch in `(D,q,lambda_A)` is row-equivalent for active `M>0`; at `RA=0` the same finite equilibrium/limit locus is obtained.

---

## 5. Physical D15 nth target stream

After the nonlinear R10 stream algebra is collapsed to the output CH pair `S=A_S I+B_S Y`, every scalar coefficient sequence entering `S`, `Qq`, `QA`, and the tangent has a source-generated infinite index.

For a requested structural target weight `W`, Stage II supplies exact invariant moments

\[
A_{rs}^{(W)}=D15[(W:I)\tau^r\delta^s],
\]

\[
B_{rs}^{(W)}=D15[(W:Y)\tau^r\delta^s].
\]

The nth contribution is

\[
J_n^{(W)}
=\sum_{r,s}P_n[r,s]A_{rs}^{(W)}
+\sum_{r,s}Q_n[r,s]B_{rs}^{(W)}.
\]

After all finite Cauchy/product contractions in the R10 stress formula are accounted for, the physical target has the form

\[
\boxed{
J^{(W)}=\sum_{n=0}^{\infty}s_n^{(W)}J_n^{(W)}
}
\]

(or an equivalent absolutely convergent diagonal enumeration of the finite multi-index Cauchy products).

Every `J_n` is a finite exact complete-halfwave/thickness moment. The series index is not a spatial degree of freedom.

---

## 6. Same-source full directional tangent stream

For each matrix material channel

\[
F=\sum f_nT_n(Y),
\]
Stage II gives

\[
dT_n[H]
=(p_{n,\tau}d\tau+p_{n,\delta}d\delta)I
+(q_{n,\tau}d\tau+q_{n,\delta}d\delta)Y+q_nH.
\]

The full R10 directional derivative is obtained by ordinary product rules applied to the same converged streams. In particular

\[
d(\det F)=\operatorname{adj}(F):dF,
\]

and for 2x2 matrices

\[
d(\operatorname{adj}F)=\operatorname{tr}(dF)I-dF.
\]

Hence

\[
\begin{aligned}
dS={}&dU\\
&-ACC\{d(\det C)C+\det(C)dC\}\\
&+dC\,\operatorname{adj}T+C\,d(\operatorname{adj}T)\\
&-\rho AT\{d(\det T)\operatorname{adj}(T7)
+\det(T)d(\operatorname{adj}T7)\}.
\end{aligned}
\]

`D15[W:dS]` therefore gives every required element of the directional consistent `Kt`. The tangent is not a secant fit and is not generated from a separate material approximation.

---

## 7. The actual n -> infinity operation

The crucial Stage-III point is that the infinite material stream is not merely an asymptotic numerical sequence. Stage I establishes that its sum is the frozen R10 source itself on the certified material interval. Since the source value series and first derivative series satisfy the required uniform/normal convergence and the structural domain has finite measure, the D15 target functional is continuous on the relevant function class.

Therefore dominated/uniform convergence gives

\[
\boxed{
\lim_{N\to\infty}D15[S_N]
=D15\left[\lim_{N\to\infty}S_N\right]
=D15[S_{R10}].
}
\]

Likewise

\[
\boxed{
\lim_{N\to\infty}D15[dS_N]
=D15[dS_{R10}].
}
\]

Thus the formal infinite D15 target functions are **exactly the R10 continuous target functions**, not an order-selected surrogate.

The physical-knot algebraic tail can additionally be written using the Stage-I oscillatory `n^-4` law and Lerch transcendent; the smooth-kernel tail is fixed by its recurrence/complex-singularity law. These are acceleration/evaluation tools, not definitions of a finite final order.

---

## 8. Coupled finite limit system

After the `n -> infinity` operation the series index disappears. The remaining equations are finite:

\[
R_q(D,q,\lambda_A)=0,
\qquad
R_A(D,q,\lambda_A)=0,
\]

plus the ultimate/limit condition. A convenient bordered form is

\[
\boxed{
L_3=\det
\begin{bmatrix}
P_D&P_q&P_\lambda\\
R_{q,D}&R_{q,q}&R_{q,\lambda}\\
R_{A,D}&R_{A,q}&R_{A,\lambda}
\end{bmatrix}=0.
}
\]

Equivalently one follows the connected equilibrium branch and takes its first reachable `dP/dD=0` maximum. The derivatives are entries of the same-source infinite-limit tangent/Jacobian.

---

## 9. Numerical localization versus formal identity

A direct raw-R10 continuum evaluator may be used as an **external numerical oracle** to localize/check the finite root of the exact limit functions, because Stage III proves the infinite D15 limit and frozen R10 define the same target functions. Such an oracle is not promoted to formal spatial quadrature.

Accordingly, numerical root localization and formal operator identity are reported separately:

```text
FORMAL OPERATOR:
true-infinite R10 series -> exact nth D15 -> n->infinity limit

NUMERICAL ORACLE:
direct continuous R10 evaluation used only to independently locate/check the same finite root.
```

This distinction prevents the numerical audit backend from acquiring theoretical identity.

---

## 10. Formal counters

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

## 11. Stage-III conclusion

```text
STAGE_I U/C/T/T7 TRUE-INFINITE STREAM -> STAGE_II CH/D15 = CONNECTED
NONLINEAR R10 CROSS-PRINCIPAL PRODUCTS = CLOSED BY CH + CONVERGENT CAUCHY PRODUCTS
PHYSICAL P/Rq/RA TARGETS = DERIVED
SAME-SOURCE FULL Kt STREAM = DERIVED
N_TO_INFINITY D15 LIMIT IDENTITY = PASS
FINITE COUPLED LIMIT SYSTEM = RETAINED
```
