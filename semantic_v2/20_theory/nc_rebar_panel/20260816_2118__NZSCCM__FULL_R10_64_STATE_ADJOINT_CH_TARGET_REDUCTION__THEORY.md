# NZ-SCCM — full R10 64-state adjoint target reduction with exact 2x2 CH elimination of T^7

**Timestamp:** 2026-08-16 21:18 +08:00  
**Gate:** `UNIFIED_V1_FULL_R10_64_STATE_ADJOINT_RATIONAL_TARGET_REDUCTION_GATE`

## 0. Result first

The 20:59 fixed 64-state quadratic-tower field remains accepted. This gate does **not** return to flattened 64 rational coefficients. Instead it makes two exact reductions:

1. the matrix power `T^7` is removed from the production target graph by 2x2 Cayley–Hamilton;
2. every remaining field product is contracted target-side by the transpose of the fixed field multiplication operator.

The resulting target graph was executed on the actual frozen R10 source graph at two exact rational thickness fibers of the retained noncommuting prototype. For the `Syy` target, the target-side contraction agrees **exactly** with the directly materialized full-R10 field result at both fibers.

```text
R10_PHYSICS = UNCHANGED
FULL_64_STATE_FIELD = RETAIN_PASS
T7_MATRIX_POWER_PRODUCTION_NODE = ELIMINATED_EXACT_BY_2X2_CH
T7_MATRIX_DERIVATIVE_PRODUCTION_NODE = ELIMINATED_TO_SCALAR_RECURRENCE
FIELD_PRODUCT_ADJOINT_PULLBACK = PASS_EXACT
FULL_R10_SYY_TARGET_DAG = PASS_EXACT
FULL_R10_SYY_ADJOINT_FIBER_AUDIT = PASS_EXACT_2_FIBERS
FINAL_64_COEFFICIENT_CANONICALIZATION = NOT_REQUIRED_BY_TARGET_ARCHITECTURE
X_DEPENDENT_DUAL_TO_HOLONOMIC_MOMENT_RUNTIME = OPEN
BETA_WEIGHTED_XY_CREATIVE_TELESCOPING = OPEN
NEW_Pu = NOT_RUN
```

No structural spatial or thickness numerical quadrature is introduced.

---

## 1. Exact Cayley–Hamilton removal of the matrix `T^7` node

Let the exact 2x2 spectral tension matrix be `T`, with invariants

\[
t=\operatorname{tr}T,\qquad d=\det T.
\]

For every integer `n>=1`, define

\[
b_0=0,\qquad b_1=1,
\]

\[
\boxed{b_n=t b_{n-1}-d b_{n-2}.}
\]

Then the 2x2 Cayley–Hamilton identity gives

\[
\boxed{T^n=b_nT-d b_{n-1}I.}
\]

For the R10 interaction only `n=7` is required. The exact coefficients are

\[
\boxed{
b_7=t^6-5t^4d+6t^2d^2-d^3,
}
\]

\[
\boxed{
b_8=t^7-6t^5d+10t^3d^2-4td^3.
}
\]

Because for a 2x2 matrix

\[
\operatorname{adj}A=\operatorname{tr}(A)I-A,
\]

we obtain directly

\[
\boxed{
\operatorname{adj}(T^7)
=\operatorname{tr}(T^7)I-T^7
=b_8I-b_7T.
}
\]

Therefore the last frozen R10 interaction term

\[
-\rho A_T\det(T)
[\operatorname{tr}(T^7)I-T^7]
\]

is exactly

\[
\boxed{
-\rho A_T d\,[b_8I-b_7T].
}
\]

No 2x2 matrix seventh power is required in the production target graph.

This supersedes the 20:59 `T7` full-64-support calculation **only as a production implementation choice**. That earlier calculation remains valid evidence that the R10 tension branch can reach the full compositum; it is not retracted.

---

## 2. Compact exact full-R10 matrix stress

Retain the exact 20:05 invariant form and write

\[
d_C=\det C,\qquad d_T=\det T.
\]

Since

\[
\operatorname{adj}T=tI-T,
\]

the complete normalized R10 current stress becomes

\[
\boxed{
S=
U
-A_{CC}d_C C
+C\operatorname{adj}T
-\rho A_Td_T(b_8I-b_7T).
}
\]

This uses only additions and products in the already-closed 64-state field plus scalar invariant recurrences.

The components needed by General-D15 are therefore

\[
\boxed{
S_{xx}=U_{xx}-A_{CC}d_CC_{xx}
+C_{xx}T_{yy}-C_{xy}T_{xy}
-\rho A_Td_T(b_8-b_7T_{xx}),
}
\]

\[
\boxed{
S_{yy}=U_{yy}-A_{CC}d_CC_{yy}
+C_{yy}T_{xx}-C_{xy}T_{xy}
-\rho A_Td_T(b_8-b_7T_{yy}),
}
\]

\[
\boxed{
S_{xy}=U_{xy}-A_{CC}d_CC_{xy}
-C_{xx}T_{xy}+C_{xy}T_{xx}
+\rho A_Td_T b_7T_{xy}.
}
\]

Thus `P`, `Rq` and all five `Rm` targets can be seeded directly from three compact scalar field DAGs. The trace of a materialized `T7` matrix is never needed.

---

## 3. Consistent tangent also avoids a matrix-power derivative

Differentiate the scalar CH recurrence instead of differentiating a matrix seventh power:

\[
\boxed{
\dot b_n
=\dot t\,b_{n-1}+t\dot b_{n-1}
-\dot d\,b_{n-2}-d\dot b_{n-2}.
}
\]

Together with

\[
\dot d_T=\operatorname{adj}(T):\dot T,
\]

this generates the exact first derivative of the R10 tension interaction using the same field graph. Therefore the same-state consistent tangent and later `KZ` target do not need either

```text
T7 as an independent material compiler
```

or

```text
d(T^7)=sum_{k=0}^6 T^k(dT)T^(6-k)
```

as the production implementation.

---

## 4. Exact target-side pullback in the 64-state field

Let the fixed field basis be `B={e_0,...,e_63}` and let

\[
e_i e_j=\sum_k m_{ij}^{k}(x)e_k.
\]

A field element is represented as

\[
a=\sum_i a_i e_i.
\]

For any linear target functional `lambda`, define multiplication by `a` as `M_a`. Then bilinearity gives the exact adjoint identity

\[
\boxed{
\lambda(ab)
=\langle\lambda,M_a b\rangle
=\langle M_a^T\lambda,b\rangle.
}
\]

In components, the target pullback through `z=a*b` is

\[
\boxed{
(\bar a)_i
=\sum_{j,k}\bar z_k\,b_j\,m_{ij}^{k},
}
\]

\[
\boxed{
(\bar b)_j
=\sum_{i,k}\bar z_k\,a_i\,m_{ij}^{k}.
}
\]

The key implementation property is that this uses the existing fixed multiplication table and never asks SymPy to canonicalize the 64 output coefficients of the product.

For a 2x2 matrix product `Z=XY`, the same rule is applied entrywise:

\[
\bar X_{ik} \mathrel{+}= \mathcal M_{Y_{kj}}^*(\bar Z_{ij}),
\qquad
\bar Y_{kj} \mathrel{+}= \mathcal M_{X_{ik}}^*(\bar Z_{ij}).
\]

This is the exact field analogue of reverse-mode matrix multiplication.

---

## 5. Why the 20:59 flattening failure is bypassed rather than hidden

At 20:59 the exact field itself was already fixed at 64 states, but a naive implementation attempted

```text
T7 field vector
 -> materialize 64 large rational coefficients
 -> SymPy.cancel each coefficient
```

and exceeded the 60 s execution window.

The present target architecture instead uses

```text
field DAG node
 -> seed structural target
 -> pull target backward through multiplication nodes
 -> retain fixed 64-state dual object
```

so no final 64-coefficient normalization is mathematically required.

This is different from the rejected 19:32 RC1 adjoint-Clenshaw route. In the old route the leaf algebra was still an expanding polynomial representation; here every field operation is reduced modulo the six quadratic relations and the algebraic state cannot exceed 64.

---

## 6. Executed full-R10 `Syy` fiber audit

The retained noncommuting rational prototype is used:

\[
E(x)=
\begin{bmatrix}
1/5+x/3&1/7+x/5\\
1/7+x/5&-1/4+2x/7
\end{bmatrix}.
\]

As in the 20:59 runtime probe, the two knot locations are rationalized **only for deterministic symbolic timing**. The formal source continues to retain the exact R10 algebraic roots.

Two exact rational fibers were audited:

```text
x = 0
x = 1/2
```

At each fiber the actual source graph included

```text
smooth t,c
compression C
knot projectors
uR
T
U
full interaction stress S
```

and the full `Syy` field occupied 60 of the 64 basis slots in this diagnostic fiber representation.

A deterministic 64-component rational target seed was used:

```text
lambda_i=((i mod 7)-3)/11
```

The compact target formula

\[
\lambda(S_{yy})
=\lambda(U_{yy})
-A_{CC}\lambda(d_CC_{yy})
+\lambda(C_{yy}T_{xx})
-\lambda(C_{xy}T_{xy})
-\rho A_T\lambda[d_T(b_8-b_7T_{yy})]
\]

was evaluated entirely by field-product pullbacks.

The exact rational residual against the directly materialized full-R10 `Syy` field was

```text
x=0   : 0 exactly
x=1/2 : 0 exactly
```

The CH reconstruction of the complete 2x2 stress was also checked entry-by-entry against the previously materialized `T^7` form and gave zero exact field residual for all four entries.

---

## 7. Diagnostic timing change

For the same Python/SymPy exact-rational fiber backend:

```text
x=0:
old binary-T7 adjoint target path  = 14.897 s  (forward intermediates + reverse target)
CH b7/b8 + compact Syy target      =  5.103 s
ratio                              =  2.919 x faster

x=1/2:
old binary-T7 adjoint target path  = 17.459 s
CH b7/b8 + compact Syy target      =  5.681 s
ratio                              =  3.073 x faster
```

These are implementation diagnostics, not theory constants. The important result is the exact identity and the removal of the matrix-power node.

`b7` and `b8` both reach all 64 field states in the executed fibers, so the speedup does not come from accidentally staying in a lower-dimensional material subspace.

---

## 8. What is closed and what is still open

This gate closes the **algebraic target DAG** problem:

```text
full R10 field              -> fixed 64 states
matrix T7                   -> eliminated by CH
structural stress target    -> finite scalar DAG
field products              -> exact adjoint pullback
final 64 coefficient cancel -> not required
```

It does **not** yet complete the x-dependent thickness integration runtime. The structural thickness functional is not a base-field-linear dot product because rational coefficient functions of `x` cannot simply be pulled outside the integral.

The next layer must combine the present factorized dual target with the already-proved 64-state holonomic system

\[
V'=A_{64}(x)V
\]

using a dual/Hermite-reduction or denominator-gauged vector-moment runtime, while keeping denominator factors and polynomial shifts unflattened.

Therefore:

```text
FULL_R10_ALGEBRAIC_TARGET_REDUCTION = PASS_EXACT
FULL_R10_X_DEPENDENT_DUAL_HOLONOMIC_THICKNESS_RUNTIME = OPEN
BETA_WEIGHTED_XY_RUNTIME = OPEN
```

No new membrane solve or capacity is released in this gate.

---

## 9. Gate decision

```text
R10_PHYSICS = UNCHANGED
FIVE_TERM_MEMBRANE_MODEL = RETAINED
GLOBAL_ROOT_TOPOLOGY = (D,q) AFTER CONDENSATION
FULL_64_STATE_FIELD = RETAIN_PASS
T7_MATRIX_POWER_PRODUCTION_NODE = ELIMINATED_EXACT_BY_2X2_CH
T7_MATRIX_DERIVATIVE_PRODUCTION_NODE = ELIMINATED_TO_SCALAR_RECURRENCE
FIELD_PRODUCT_ADJOINT_PULLBACK = PASS_EXACT
FULL_R10_SXX_SYY_SXY_COMPACT_TARGET_FORM = PASS_EXACT
FULL_R10_SYY_ADJOINT_FIBER_AUDIT = PASS_EXACT_2_FIBERS
FINAL_64_COEFFICIENT_CANONICALIZATION = NOT_REQUIRED
FULL_R10_X_DEPENDENT_DUAL_HOLONOMIC_THICKNESS_RUNTIME = OPEN
BETA_WEIGHTED_XY_CREATIVE_TELESCOPING_RUNTIME = OPEN
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
NEW_CURRENT_MEMBRANE_r_SOLVE = NOT_RUN
NEW_Pu = NOT_RUN
```

## 10. Unique next gate

```text
UNIFIED_V1_FULL_R10_DUAL_HOLONOMIC_THICKNESS_MOMENT_RUNTIME_GATE
```

The next gate must attach the compact adjoint R10 target DAG to the 64-state holonomic thickness operator without expanding a common rational coefficient vector. Only after that thickness target runtime passes may the remaining beta-weighted `(X,Y)` creative-telescoping layer be promoted.
