# NZ-SCCM — Engineering current operator derivation

**Date:** 2026-08-19 23:40 +08  
**Identity:** `ENGINEERING_CURRENT_OPERATOR_DERIVATION`  
**Previous checkpoint:** `5dc2d5390b57243477c4c7d7a408b88cca7d8db1`

## 1. Input tensor and invariants

The normalized equivalent-uniaxial 2x2 strain matrix is the frozen R10 matrix

\[
E=\begin{bmatrix}E_{11}&E_{12}\\E_{12}&E_{22}\end{bmatrix},
\qquad
J_1=\operatorname{tr}E,
\qquad
J_2=\det E.
\]

Cayley–Hamilton:

\[
\boxed{E^2-J_1E+J_2I=0.}
\]

## 2. Polynomial scalar chains

Use the material-only engineering chains locked in the preceding checkpoint:

\[
\widetilde C(\lambda),\quad
\widetilde T(\lambda),\quad
\widetilde U(\lambda).
\]

For Case21 these are finite degrees

```text
deg C~ = 12
deg T~ = 6
deg U~ = 12
```

(the compact factored forms are the formal source; the power coefficients are derived algebraically from them).

## 3. Exact matrix lift without eigenvalue radicals

For any polynomial

\[
f(\lambda)=\sum_{n=0}^Nc_n\lambda^n,
\]

write

\[
E^n=a_nI+b_nE.
\]

Initialize

\[
(a_0,b_0)=(1,0),
\qquad
(a_1,b_1)=(0,1),
\]

and recur

\[
\boxed{a_{n+1}=-J_2b_n,}
\qquad
\boxed{b_{n+1}=a_n+J_1b_n.}
\]

Then

\[
\boxed{
f(E)=A_fI+B_fE,
}
\]

with

\[
A_f=\sum c_na_n,
\qquad
B_f=\sum c_nb_n.
\]

Thus

\[
\widetilde C(E)=A_CI+B_CE,
\]

\[
\widetilde T(E)=A_TI+B_TE,
\]

\[
\widetilde U(E)=A_UI+B_UE.
\]

No principal-value square root is evaluated in the engineering operator.

## 4. 2x2 pair algebra

Represent

\[
[A,B]\equiv AI+BE.
\]

For two pairs

\[
[A,B]\odot[C,D]
=
\boxed{
[AC-J_2BD,\ AD+BC+J_1BD]
}.
\]

Determinant:

\[
\boxed{
\det(AI+BE)=A^2+ABJ_1+B^2J_2.
}
\]

Adjugate:

\[
\boxed{
\operatorname{adj}(AI+BE)=(A+BJ_1)I-BE.
}
\]

An independent symbolic check gives

\[
E^2=-J_2I+J_1E,
\]

\[
E^3=-J_1J_2I+(J_1^2-J_2)E,
\]

confirming the recurrence.

## 5. Full R10 CC / TC / TT identity retained

The frozen principal interaction equations are kept exactly through the coordinate-free matrix identity

\[
\boxed{
S_{eng}
=\widetilde U
-a_{cc}\det(\widetilde C)\widetilde C
+\widetilde C\operatorname{adj}(\widetilde T)
-\rho a_t\det(\widetilde T)\operatorname{adj}(\widetilde T^7).
}
\]

This identity has principal values

\[
\widetilde s_1
=\widetilde U_1
-a_{cc}\widetilde C_1^2\widetilde C_2
+\widetilde C_1\widetilde T_2
-\rho a_t\widetilde T_1\widetilde T_2^8,
\]

\[
\widetilde s_2
=\widetilde U_2
-a_{cc}\widetilde C_2^2\widetilde C_1
+\widetilde C_2\widetilde T_1
-\rho a_t\widetilde T_2\widetilde T_1^8.
\]

Therefore the R10 interaction identities `CC`, `TC`, `TT` remain present and are not replaced by a 2D fitted surface.

## 6. Finite pair construction

Let

\[
\widetilde C=[A_C,B_C],
\quad
\widetilde T=[A_T,B_T],
\quad
\widetilde U=[A_U,B_U].
\]

Compute `T2,T4,T7` only through pair multiplication, e.g.

\[
T^2=T\odot T,
\quad
T^4=T^2\odot T^2,
\quad
T^7=T^4\odot T^2\odot T.
\]

Then

\[
d_C=A_C^2+A_CB_CJ_1+B_C^2J_2,
\]

\[
d_T=A_T^2+A_TB_TJ_1+B_T^2J_2.
\]

Write

\[
T^7=[A_{T7},B_{T7}].
\]

The complete stress pair is finite:

\[
\boxed{
A_S=A_U-a_{cc}d_CA_C+A_{CT}
-\rho a_td_T(A_{T7}+B_{T7}J_1),
}
\]

\[
\boxed{
B_S=B_U-a_{cc}d_CB_C+B_{CT}
+\rho a_td_TB_{T7},
}
\]

where

\[
A_{CT}=A_C(A_T+B_TJ_1)+B_CB_TJ_2,
\]

\[
B_{CT}=A_TB_C-A_CB_T.
\]

Hence

\[
\boxed{S_{eng}=A_S(J_1,J_2)I+B_S(J_1,J_2)E.}
\]

Physical stress:

\[
\boxed{\sigma=f_cS_{eng}.}
\]

## 7. Same-source tangent

The tangent is defined by differentiating the same finite polynomial/pair circuit. No finite differences and no separate material tangent are formal components.

For a generalized coordinate `g`:

\[
J_{1,g}=\operatorname{tr}E_{,g},
\]

\[
J_{2,g}=E_{22}E_{11,g}+E_{11}E_{22,g}-2E_{12}E_{12,g}.
\]

Differentiate the CH power recurrence:

\[
a_{n+1,g}=-J_{2,g}b_n-J_2b_{n,g},
\]

\[
b_{n+1,g}=a_{n,g}+J_{1,g}b_n+J_1b_{n,g}.
\]

Then differentiate all pair products, determinants, adjugates and the final stress pair by product rule. This is the formal tangent used for `P_g`, `R_{q,g}`, `R_{alpha,g}`.

## 8. Domain gate

For the two eigenvalues of `E`, the engineering operator is certified only if

\[
\boxed{-1\le\lambda_i\le10x_{cr}\qquad(i=1,2).}
\]

The eigenvalues need not be explicitly evaluated during production: the two scalar inequalities can be audited from the characteristic polynomial/invariant conditions if desired. A violation is a material-domain failure, not a reason to fit new coefficients to the specimen.

## 9. Production status

```text
FINITE_SCALAR_SOURCE_LAWS          = PASS
PRINCIPAL_SQRT_IN_PRODUCTION       = REMOVED
2x2_CH_REDUCTION                   = PASS
CC_TC_TT_IDENTITY                  = RETAINED
SAME_SOURCE_TANGENT                = PASS
SPATIAL_MATERIAL_POINTS            = ZERO
SPECIMEN_FIT                       = ZERO
```

## 10. Unique resume point

Substitute the retained Case21 R15 continuous strain field into `J1,J2,E`; expand the finite stress and virtual-work integrands into finite trigonometric–thickness monomials; apply exact D15 moments; add analytic reinforcement layers; solve the direct three-equation limit system.