# NZ-SCCM Case21 R13 — Full three-branch R10 matrix-spline / relative-GKZ constructor

**Date:** 2026-08-19  
**Status:** `FULL_THREE_BRANCH_MATERIAL_SERIES_REPLACEMENT = COMPLETE`  
**Formal discretization:** `NONE`

## 0. Scope

This artifact closes exactly one requested modification: replace the former material-coordinate true-infinite Chebyshev/prefix layer by one finite exact constructor.

It does **not** change Nguyen second-order kinematics, R10 material parameters, the definitions of \(P,R_q,R_\alpha\), the same-source derivative requirement, or the direct limit system.

The previous R12 planned extension

```text
add threshold surfaces as separate relative-GKZ divisors
```

is **rejected as unnecessary** for the material law itself. The three R10 tension branches are instead represented globally by one finite truncated-power spline, so no material-region partition is required.

## 1. Scalar R10 tension law

Let
\[
r=t/x_{cr}\ge 0.
\]

The original frozen law is

\[
p_1(r)
=
\rho r+(10H_R-6\rho)r^3+(8\rho-15H_R)r^4+(6H_R-3\rho)r^5,
\quad 0\le r\le1,
\]

\[
p_2(r)
=
H_R+(U_R-H_R)
\left[
10s^3-15s^4+6s^5
\right],
\qquad
s=\frac{r-1}{9},
\quad 1<r\le10,
\]

\[
p_3(r)=U_R,\qquad r>10.
\]

Because the frozen joins are \(C^2\), the differences factor exactly as

\[
p_2-p_1
=
A_3(r-1)^3+A_4(r-1)^4+A_5(r-1)^5,
\]

\[
p_3-p_2
=
B_3(r-10)^3+B_4(r-10)^4+B_5(r-10)^5,
\]

where

\[
\boxed{A_3
=
4\rho-\frac{7300}{729}H_R+\frac{10}{729}U_R},
\]

\[
\boxed{A_4
=
7\rho-\frac{32800}{2187}H_R-\frac{5}{2187}U_R},
\]

\[
\boxed{A_5
=
3\rho-\frac{118100}{19683}H_R+\frac{2}{19683}U_R},
\]

\[
\boxed{B_3=\frac{10(H_R-U_R)}{729}},
\qquad
\boxed{B_4=\frac{5(H_R-U_R)}{2187}},
\qquad
\boxed{B_5=\frac{2(H_R-U_R)}{19683}}.
\]

For the frozen values
\[
\rho=0.1,\quad H_R=0.09799750427197301,\quad U_R=0.03,
\]
these are

```text
A3 = -0.58090779312126608093
A4 = -0.76980710567933915318
A5 = -0.28799193489407165986
B3 = +0.00093275040153598093278
B4 = +0.00015545840025599682213
B5 = +0.0000069092622335998587614
```

Therefore the original three-branch law is exactly the **single global spline**

\[
\boxed{u_R(r)
=
p_1(r)
+A_3(r-1)_+^3
+A_4(r-1)_+^4
+A_5(r-1)_+^5
+B_3(r-10)_+^3
+B_4(r-10)_+^4
+B_5(r-10)_+^5.
}
\]

This is an identity, not an approximation.

The scalar positive part is
\[
x_+=\frac12(x+|x|)=\frac12\left(x+\sqrt{x^2}\right).
\]

Thus the entire three-branch law is a finite algebraic expression.

## 2. Matrix lift: no threshold partition

The R10 tensile projector matrix is positive semidefinite:
\[
\mathbf t\succeq0,
\qquad
\mathbf r=\mathbf t/x_{cr}.
\]

For any real symmetric matrix \(\mathbf X\), define its spectral positive part

\[
\boxed{
\langle\mathbf X\rangle_+
=
\frac12\left(
\mathbf X+(\mathbf X^2)^{1/2}
\right).
}
\]

Hence define

\[
\mathbf P_1=\langle\mathbf r-\mathbf I\rangle_+,
\qquad
\mathbf P_{10}=\langle\mathbf r-10\mathbf I\rangle_+.
\]

Then the **complete three-branch R10 tensile matrix function** is

\[
\boxed{
\mathbf u_R
=
p_1(\mathbf r)
+A_3\mathbf P_1^3
+A_4\mathbf P_1^4
+A_5\mathbf P_1^5
+B_3\mathbf P_{10}^3
+B_4\mathbf P_{10}^4
+B_5\mathbf P_{10}^5.
}
\]

By spectral calculus, each eigenvalue \(r_i\) receives exactly the original scalar \(u_R(r_i)\). Therefore this single formula reproduces all three original R10 branches simultaneously, including states in which the two principal values lie in different branches.

## 3. Exact matrix positive-part circuit at each knot

For \(a\in\{1,10\}\), let
\[
\mathbf X_a=\mathbf r-a\mathbf I.
\]

Define
\[
d_a=\det\mathbf X_a,
\qquad
\widehat d_a=\sqrt{d_a^2}=|d_a|,
\]
\[
\sigma_a=
\sqrt{
\operatorname{tr}(\mathbf X_a^2)+2\widehat d_a
}.
\]

Then on the principal real sheet
\[
|\mathbf X_a|
=
(\mathbf X_a^2)^{1/2}
=
\frac{\mathbf X_a^2+\widehat d_a\mathbf I}{\sigma_a},
\]
with the zero-matrix case defined by continuous extension.

Therefore
\[
\boxed{
\mathbf P_a
=
\frac12(\mathbf X_a+|\mathbf X_a|)
}.
\]

Every required power
\[
\mathbf P_a^2,\mathbf P_a^3,\mathbf P_a^4,\mathbf P_a^5
\]
is evaluated by the same \(2\times2\) Cayley–Hamilton pair product.

If
\[
\mathbf X=x_0\mathbf I+x_1\mathbf E,
\qquad
\mathbf Y=y_0\mathbf I+y_1\mathbf E,
\]
then
\[
\boxed{
(x_0,x_1)\odot(y_0,y_1)
=
\left(
x_0y_0-\delta_E x_1y_1,\,
x_0y_1+x_1y_0+\tau_E x_1y_1
\right).
}
\]

No threshold surface is used as a spatial subdomain.

## 4. Same-source tangent remains exact

The global spline is \(C^2\), hence in particular \(C^1\). Its derivative is one finite expression,

\[
u_R'(r)
=
p_1'(r)
+3A_3(r-1)_+^2
+4A_4(r-1)_+^3
+5A_5(r-1)_+^4
+3B_3(r-10)_+^2
+4B_4(r-10)_+^3
+5B_5(r-10)_+^4.
\]

For the matrix function, the same-source Fréchet derivative is obtained from the same scalar spline through first divided differences,

\[
L_f(\mathbf r)[\mathbf H]
=
\sum_{i,j}
f^{[1]}(r_i,r_j)
\mathbf P_i\mathbf H\mathbf P_j,
\]

with the coalescent limit
\[
f^{[1]}(r,r)=f'(r).
\]

No finite-difference tangent and no independently fitted stiffness is introduced.

## 5. Full finite R10 circuit

All other R12 finite operations remain unchanged:

```text
continuous strain E
-> exact 2x2 square-root projector
-> t,c
-> C
-> GLOBAL THREE-BRANCH MATRIX SPLINE u_R(t)
-> T,U,T^7
-> finite R10 stress S
-> Syy
```

The only change relative to the R12 pilot circuit is the replacement of the first-branch-only `ur0,ur1` nodes by the global matrix-spline circuit above.

## 6. Complete sparse master A* generated

The full symbolic circuit has now been generated exactly.

```text
polynomial/circuit relations = 112
monomial-space variables     = 115
Cayley A* rows               = 227
Cayley A* columns            = 403
max monomials in one relation= 13
```

The master configuration is therefore

\[
\boxed{
A_*\in\mathbb Z^{227\times403}.
}
\]

This is the complete three-branch material circuit; it is not the R07 first-branch pilot.

## 7. Exact integral-function identity

After the finite algebraic auxiliary variables are introduced, the complete generalized integrands are finite algebraic/rational relative periods over the one continuous representative halfwave.

The bounded physical chain is represented in the standard relative/incomplete \(A\)-hypergeometric/GKZ class; this is an integration representation of the same finite current operator, not a new constitutive model.

The three targets

\[
P,\qquad R_q,\qquad R_\alpha
\]

share the same denominator/support family. Same-source derivatives increase pole powers or apply finite differential/contiguity shifts; they do not reintroduce a material degree \(N\).

Hence one master \(A_*\) supports the complete current target family.

## 8. Constructor-switch decision

The following planned constructor is crossed out:

```text
R12 NEXT = add xcr and 10*xcr threshold divisors / material-region boundaries
STATUS   = REJECTED AS UNNECESSARY
```

Reason: the exact global matrix truncated-power spline eliminates the material branch partition before integration.

The retained complete constructor is

```text
finite R10
-> exact projector t,c
-> exact global matrix spline for all 3 tension branches
-> sparse 2x2 CH algebraic circuit
-> one finite master relative-GKZ A*
-> exact continuous P,Rq,Ralpha and same-source derivatives
-> unchanged direct limit system
```

If a particular evaluator of the standard \(A\)-hypergeometric object is inconvenient, one may switch among its standard Euler/residue/Mellin–Barnes/differential-system representations. That is a representation switch of the same mathematical object, not a new theory gate.

## 9. Formal status

```text
MATERIAL_TRUE_INFINITE_SERIES_LAYER        = REMOVED
FINITE_PREFIX_CONVERGENCE_GATE             = REMOVED
R10_THREE_BRANCH_MATERIAL_PARTITION        = REMOVED FROM FORMAL INTEGRATION
GLOBAL_THREE_BRANCH_MATRIX_SPLINE           = PASS
FULL_THREE_BRANCH_SPARSE_CH_CIRCUIT         = PASS
FULL_THREE_BRANCH_MASTER_ASTAR              = PASS
SAME_SOURCE_TANGENT_FROM_SAME_GLOBAL_SPLINE = PASS
DISCRETIZATION                              = ZERO / PROHIBITED BY DEFAULT
```

This closes the material-series replacement as a complete finite constructor.
