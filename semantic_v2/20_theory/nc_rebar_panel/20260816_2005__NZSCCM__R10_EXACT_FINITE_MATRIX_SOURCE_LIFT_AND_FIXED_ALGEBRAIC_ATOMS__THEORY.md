# NZ-SCCM — R10 exact finite-matrix source lift and fixed algebraic-atom reduction

**Timestamp:** 2026-08-16 20:05 +08:00  
**Parent gate:** `UNIFIED_V1_NC_EXACT_NESTED_ATOM_MOMENT_CLOSURE_OR_STRUCTURALLY_CLOSED_COMPILER_REDESIGN_GATE`

## 1. Purpose

The 19:32 gate proved that target-side / adjoint Clenshaw is algebraically exact but does **not** remove the composed degree of the nested beta/Chebyshev RC1 graph when the terminal algebra is ordinary polynomial General-D15.

This gate therefore takes the second admissible route: preserve the frozen R10 physical current law, but replace the nested material approximation graph by an **exact finite matrix-function source lift** before any structural moment approximation is considered.

No `P`, `Rq`, `Rm`, `L`, `KZ`, or `Pu` is solved here.

## 2. Existing scalar R10 source functions

Let the normalized current strain matrix be `E` with principal values `lambda_1,lambda_2`. Retain the frozen constants

```text
rho   = 0.1
H     = 0.09799750427197301
UR    = 0.03
ACC   = 0.1072329249362415
AT    = 1-2^(-1/8)
kappa = source parameter
xcr   = rho/kappa
eta   = xcr/20
```

The existing smooth source split is

\[
\pi(x)=
\frac{x^2\left(\sqrt{x^2+\eta^2}+x\right)}
{2(x^2+\eta^2)} ,
\]

\[
c(\lambda)=\pi(-\lambda),\qquad
t(\lambda)=\pi(\lambda).
\]

The compression function is

\[
C(c)=
\frac{\kappa c}
{1+(\kappa-2)c+c^2}.
\]

The tension-return function `u_R(t)` is the existing quintic/C2 source law with knots

\[
a=x_{cr}=\rho/\kappa,\qquad b=10a.
\]

Then

\[
T=u_R/\rho,
\]

\[
U=\kappa\lambda-C+\kappa c+u_R-\kappa t.
\]

The frozen two-principal-value R10 stress law is

\[
s_1=
U_1-A_{CC}C_1^2C_2+C_1T_2
-\rho A_T T_1T_2T_2^7,
\]

\[
s_2=
U_2-A_{CC}C_2^2C_1+C_2T_1
-\rho A_T T_2T_1T_1^7.
\]

## 3. Exact matrix lift of the smooth source split

Define

\[
R_\eta(E)=\sqrt{E^2+\eta^2 I}.
\]

Because `E` and `R_eta(E)` commute, the scalar source split lifts exactly to

\[
\boxed{
\Pi(E)
=
\frac12 E^2\,[R_\eta(E)+E]\,[E^2+\eta^2I]^{-1}
}
\]

and therefore

\[
\boxed{
c=\Pi(-E),\qquad t=\Pi(E).
}
\]

This is not a fit and has no material polynomial order.

For a real symmetric 2x2 matrix `A>=0`, the principal square root itself has the finite Cayley-Hamilton form

\[
\boxed{
\sqrt A=
\frac{A+\sqrt{\det A}\,I}
{\sqrt{\operatorname{tr}A+2\sqrt{\det A}}}
}
\]

away from the removable zero limit. Thus `Pi(E)` is a fixed algebraic 2x2 matrix function of the strain invariants.

The compression operator becomes exactly

\[
\boxed{
C=
\kappa c
\left[
I+(\kappa-2)c+c^2
\right]^{-1}.
}
\]

For 2x2 matrices the inverse is also finite by Cayley-Hamilton / adjugate-determinant reduction.

## 4. Exact truncated-power representation of the tension source

Introduce

\[
z=t/a,\qquad a=\rho/\kappa.
\]

For `0<=z<=1` define

\[
P_1(z)=
\rho z
+(10H-6\rho)z^3
+(8\rho-15H)z^4
+(6H-3\rho)z^5.
\]

The existing middle branch is

\[
P_2(z)
=
H+(U_R-H)
\left[
10s^3-15s^4+6s^5
\right],
\qquad
s=\frac{z-1}{9},
\]

for `1<z<=10`, and `u_R=U_R` for `z>10`.

The whole source law is exactly one global truncated-power spline:

\[
\boxed{
u_R(z)
=
P_1(z)
+\sum_{k=3}^{5}A_k(z-1)_+^k
+\sum_{k=3}^{5}B_k(z-10)_+^k
}
\]

with

\[
A_3=4\rho+\frac{-7300H+10U_R}{729},
\]

\[
A_4=7\rho+\frac{-32800H-5U_R}{2187},
\]

\[
A_5=3\rho+\frac{-118100H+2U_R}{19683},
\]

\[
B_3=\frac{10(H-U_R)}{729},
\qquad
B_4=\frac{5(H-U_R)}{2187},
\qquad
B_5=\frac{2(H-U_R)}{19683}.
\]

The reproducer proves symbolically that the middle-branch and upper-branch residuals are both exactly zero.

For a symmetric matrix `Z=t/a`, define the spectral positive part

\[
X_+=\frac12\left(X+\sqrt{X^2}\right).
\]

Then the exact matrix tension source is

\[
\boxed{
u_R(Z)=
P_1(Z)
+\sum_{k=3}^{5}A_k(Z-I)_+^k
+\sum_{k=3}^{5}B_k(Z-10I)_+^k.
}
\]

Therefore the former independent fitted `T7(lambda)` channel is mathematically unnecessary:

\[
\boxed{
T=u_R/\rho,\qquad T^7=(T)^7.
}
\]

## 5. Exact invariant matrix form of the full 2D R10 stress

Because `C`, `T`, and `U` are all spectral functions of the same symmetric strain matrix, they commute and share eigenvectors.

For either principal index `i` and the opposite index `j`,

\[
C_i^2C_j=\det(C)\,C_i,
\]

\[
C_iT_j=C_i[\operatorname{tr}(T)-T_i],
\]

and

\[
T_iT_jT_j^7
=
\det(T)\,[\operatorname{tr}(T^7)-T_i^7].
\]

Hence the entire two-principal-value R10 law is exactly the finite matrix identity

\[
\boxed{
S=
U
-A_{CC}\det(C)\,C
+C[\operatorname{tr}(T)I-T]
-\rho A_T\det(T)
[\operatorname{tr}(T^7)I-T^7].
}
\]

This is the same R10 physical law; it is not a new constitutive model.

The reproducer checks this invariant matrix identity against the direct principal-value source law for random symmetric states throughout all Z0-Z6 guard domains. The largest observed matrix-stress discrepancy is approximately `8.1e-15`.

## 6. Consistent tangent remains finite and exact in the same graph

No numerical material tangent is required.

For example,

\[
d(T^7)
=
\sum_{k=0}^{6}T^k(dT)T^{6-k},
\]

and

\[
d[\det X]
=
\operatorname{adj}(X):dX.
\]

For a principal square-root atom `R=sqrt(A)`,

\[
\boxed{
R\,dR+dR\,R=dA
}
\]

is the exact Sylvester equation for its Frechet derivative.

The inverse derivative is

\[
d(Q^{-1})=-Q^{-1}(dQ)Q^{-1}.
\]

Therefore the same fixed source graph supplies current stress and consistent tangent; the tangent does not require an independent fitted material surface.

At the two tension spline knots, the original source law is C2. The truncated-power representation uses powers `k=3,4,5`, so the physical first derivative required for the current tangent is continuous.

## 7. Fixed algebraic atom graph

The nested RC1 material coefficient hierarchy is no longer required by this candidate structural representation.

The only non-polynomial source atom families are fixed:

```text
A1: sqrt(E^2 + eta^2 I)
A2: inverse(I + (kappa-2)c + c^2)
A3: (t/a - I)_+^k,   k=3,4,5
A4: (t/a - 10I)_+^k, k=3,4,5
```

All other operations are finite matrix additions, multiplications, traces, determinants, and powers no higher than 7.

Consequences:

```text
Ng,Nc,Nt material fit orders        -> absent in this candidate source graph
beta-lens nested composition        -> absent
independent T7 fit                   -> absent
specimen-specific material order    -> absent
R10 physical law                    -> unchanged
```

`R10-MSAC-RC1` remains a valid material-level source-fidelity witness; it is not retracted. It is simply no longer the preferred structural representation candidate after the 19:32 nested-target failure.

## 8. What this gate does and does not solve

This gate removes the *material representation order explosion*. It does **not** yet prove that the fixed algebraic atoms above possess a practical exact structural moment transform.

The remaining structural problem is now independent of material approximation order:

\[
\boxed{
\mathcal L_K[
\text{fixed algebraic matrix atom}(E(X,Y,z))
]
}
\]

for the existing finite General-D15 target kernels `P,Rq,Rm,KZ`.

The next closure may use General-D15 plus exact algebraic/CAS/special-function moment recurrences, but it may not reintroduce spatial Gauss/Simpson/adaptive/collocation/material-point grids.

## 9. Gate verdict

```text
R10_PHYSICAL_CURRENT_LAW                         = RETAIN_FROZEN
R10_EXACT_SMOOTH_SPLIT_MATRIX_LIFT              = PASS_EXACT
UR_TRUNCATED_POWER_SPLINE                       = PASS_EXACT
R10_2D_STRESS_INVARIANT_MATRIX_IDENTITY         = PASS_EXACT
CONSISTENT_TANGENT_FINITE_GRAPH                 = PASS_FORMAL
INDEPENDENT_T7_COMPILER_CHANNEL                 = ELIMINATED
MATERIAL_FIT_ORDER_DEPENDENCE_IN_SOURCE_GRAPH   = ELIMINATED
FIXED_ALGEBRAIC_ATOM_GRAPH                      = PASS_FORMAL
GENERAL_D15_ALGEBRAIC_ATOM_MOMENT_CLOSURE      = OPEN
NEW_CURRENT_MEMBRANE_r_SOLVE                    = NOT_RUN
NEW_Pu                                          = NOT_RUN
```

## 10. New unique next gate

```text
UNIFIED_V1_R10_FIXED_ALGEBRAIC_ATOM_GENERAL_D15_CAS_MOMENT_CLOSURE_GATE
```

The next work must construct and audit an exact/controlled target-moment backend for the fixed algebraic atom graph above. It must begin with the simplest atom `sqrt(E^2+eta^2 I)` and then add the 2x2 inverse and the two C2 positive-part spline-knot atom families.

Only after the same backend closes `P,Rq,Rm,KZ` may the five internal membrane coordinates be solved and Schur-condensed to release a new `Pu`.
