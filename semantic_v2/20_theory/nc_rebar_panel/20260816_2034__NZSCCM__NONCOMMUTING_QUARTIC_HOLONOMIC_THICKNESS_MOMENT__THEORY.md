# NZ-SCCM — noncommuting quartic algebraic period → holonomic thickness-moment closure

**Timestamp:** 2026-08-16 20:34 +08:00  
**Gate:** `UNIFIED_V1_NONCOMMUTING_QUARTIC_ALGEBRAIC_PERIOD_HOLONOMIC_GENERAL_D15_GATE`

## 0. Verdict

The 20:14 boundary is advanced, but the full 3D R10 target runtime is not yet released.

```text
UNIVERSAL_SMOOTH_QUARTIC_SECOND_ORDER_ODE = PASS_EXACT
PROTOTYPE_NONCOMMUTING_QUARTIC_ANNIHILATOR = PASS_EXACT
POLYNOMIAL_THICKNESS_MOMENT_RECURRENCE = PASS_EXACT
ANTIDERIVATIVE_HOLONOMIC_ORDER_BOUND = PASS_EXACT_ORDER_LE_3
SMOOTH_R10_THICKNESS_HOLONOMIC_RUNTIME_CLASS = CLOSED_FORMALLY
FULL_R10_THREE_ATOM_COMPOSITUM_HOLONOMIC_EXISTENCE = PASS_FORMAL_ORDER_LE_64
FULL_R10_COMPOSITUM_ANNIHILATOR_RUNTIME = OPEN
BETA_WEIGHTED_XY_CREATIVE_TELESCOPING_RUNTIME = OPEN
NEW_CURRENT_MEMBRANE_r_SOLVE = NOT_RUN
NEW_Pu = NOT_RUN
```

No structural spatial or thickness numerical quadrature is introduced.

---

## 1. What was open at 20:14

For fixed in-plane coordinates `(X,Y)`, Nguyen kinematics makes the normalized 2x2 equivalent-strain matrix affine through thickness:

\[
E(\zeta)=E_m+\zeta E_b.
\]

The exact R10 smooth atom had already been reduced to

\[
s_\eta(\zeta)=\operatorname{tr}\sqrt{E(\zeta)^2+\eta^2I},
\]

with scalar quartic relation

\[
s_\eta^4-2p(\zeta)s_\eta^2+r(\zeta)=0,
\]

where

\[
p=\operatorname{tr}(E^2+\eta^2I),
\]

\[
r=(\operatorname{tr}E)^2\big[(\operatorname{tr}E)^2-4\det E\big].
\]

For an affine 2x2 pencil, `p(zeta)` has degree at most 2 and `r(zeta)` degree at most 4. Direct generic `CAS.integrate` was not a common backend.

The present gate does not ask CAS for an antiderivative. It derives the differential equation satisfied by the algebraic atom itself.

---

## 2. Universal order-2 holonomic equation for the quartic smooth atom

Consider the general algebraic branch

\[
y^4-2p(x)y^2+r(x)=0,
\qquad y>0\text{ on the physical real branch}.
\]

Define

\[
\Delta=p^2-r,
\]

and write

\[
y^2=p+\sqrt{\Delta}.
\]

The logarithmic derivative has the exact two-dimensional form

\[
\frac{y'}{y}=a+\frac{b}{\sqrt{\Delta}},
\]

with

\[
\boxed{a=\frac{r'}{4r}},
\]

\[
\boxed{b=\frac{p'}2-\frac{pr'}{4r}}.
\]

Differentiating once more gives

\[
\frac{y''}{y}=c+\frac{e}{\sqrt{\Delta}},
\]

where

\[
\boxed{c=a'+a^2+\frac{b^2}{\Delta}},
\]

\[
\boxed{e=b'-\frac{b\Delta'}{2\Delta}+2ab}.
\]

Eliminating the single radical generator gives the exact linear ODE

\[
\boxed{
b\,y''-e\,y'+(ea-bc)y=0.
}
\]

After clearing denominators, all coefficients are polynomials/rational functions of the finite base field. Therefore the noncommuting 2x2 quartic smooth atom is a D-finite/holonomic function of thickness of order at most 2.

This is a structural result, not a special property of the numerical prototype below.

---

## 3. Why the order collapses to 2 rather than 4

The minimal polynomial is even in `y`. Under exact differentiation modulo

\[
y^4-2py^2+r=0,
\]

`y`, `y'`, `y''`, ... remain in the odd algebraic subspace

\[
\operatorname{span}_{\mathbb Q(x)}\{y,y^3\}.
\]

That space has dimension 2. Hence any three consecutive derivatives are linearly dependent over the rational-function base field. The explicit equation above is the closed analytic form of that dependence.

This is the main advance over the 20:14 result: the generic noncommuting quartic period is no longer only identified as an algebraic-period class; its through-thickness generator now has a constructive finite differential operator.

---

## 4. Exact polynomial-thickness moment recurrence

Let the cleared operator be

\[
A_2(x)y''+A_1(x)y'+A_0(x)y=0,
\]

with polynomial coefficients.

Define the complete-thickness moments

\[
M_n=\int_{-1}^{1}x^n y(x)\,dx.
\]

Multiply the ODE by `x^n` and integrate by parts twice. No numerical quadrature is required in the formal derivation:

\[
\boxed{
B_n+\int_{-1}^{1}
\left[
(x^nA_2)''-(x^nA_1)'+x^nA_0
\right]y\,dx=0,
}
\]

where the boundary term is

\[
\boxed{
B_n=\left[
x^nA_2y'-(x^nA_2)'y+x^nA_1y
\right]_{-1}^{1}.
}
\]

If

\[
A_i(x)=\sum_j a_{ij}x^j,
\]

then

\[
\boxed{
\sum_j a_{2j}(n+j)(n+j-1)M_{n+j-2}
-\sum_j a_{1j}(n+j)M_{n+j-1}
+\sum_j a_{0j}M_{n+j}
=-B_n.
}
\]

Thus arbitrary polynomial thickness weights do not create new integrals one-by-one. They belong to one finite holonomic moment family controlled by the same order-2 atom and algebraic endpoint data.

---

## 5. Antiderivative identity

If

\[
Y(x)=\int^x y(t)\,dt,
\]

then `Y'=y`. Therefore

\[
\boxed{
A_2Y'''+A_1Y''+A_0Y'=0.
}
\]

So a definite complete-thickness integral is a boundary evaluation of a holonomic function of order at most 3, rather than a spatial quadrature rule.

This provides the formal special-function object needed by a zero-spatial-quadrature backend.

---

## 6. Exact noncommuting rational prototype

The same prototype used at 20:14 is retained:

\[
E(x)=
\begin{bmatrix}
1/5+x/3 & 1/7+x/5\\
1/7+x/5 & -1/4+2x/7
\end{bmatrix},
\qquad \eta=1/20.
\]

For

\[
y(x)=\operatorname{tr}\sqrt{E(x)^2+\eta^2I},
\]

the exact quotient-field algorithm produces

\[
A_2y''+A_1y'+A_0y=0,
\]

with degrees

```text
deg A0 = 6
deg A1 = 7
deg A2 = 9
```

and integer-polynomial coefficients stored in the parameter JSON and reproducer.

The annihilator residual is exactly zero in

\[
\mathbb Q(x)[y]/(y^4-2p(x)y^2+r(x)).
\]

Hence this is an exact algebraic identity, not a fit to sampled values.

---

## 7. Moment recurrence audit

For audit only, high-precision direct quadrature was used to evaluate prototype moments and check the exact integration-by-parts recurrence. This numerical quadrature is not part of the production operator.

For `n=0,...,6`, the recurrence residual magnitudes were

```text
n=0   0
n=1   1.47e-39
n=2   1.47e-39
n=3   0
n=4   5.88e-39
n=5   0
n=6   2.94e-39
```

The nonzero figures are high-precision audit roundoff. The formal recurrence itself is exact.

---

## 8. Relation to the complete R10 field

The exact R10 source graph is generated over the finite trigonometric/thickness base field by three algebraic scalar generators

```text
s_eta
s_1
s_10
```

with conservative total algebraic field-degree bound `<=64`.

For a fixed `(X,Y)`, any scalar component of stress or consistent tangent is therefore algebraic in thickness and its derivative sequence lies in a finite-dimensional algebraic field. Consequently a linear differential annihilator exists with order at most the algebraic field degree.

The present gate implements the quartic smooth-generator runtime exactly. It does not yet construct the full primitive-element/compositum annihilator for all three generators simultaneously.

Therefore:

```text
SMOOTH_R10_THICKNESS_HOLONOMIC_RUNTIME = PASS_EXACT
FULL_R10_THREE_ATOM_HOLONOMIC_EXISTENCE = PASS_FORMAL
FULL_R10_THREE_ATOM_RUNTIME = OPEN
```

---

## 9. Relation to General-D15

The old polynomial D15 engine evaluated every thickness monomial by the elementary moment `Z_h`.

The new exact-source route keeps those elementary polynomial moments, but adds a finite holonomic moment object when an algebraic R10 atom is present:

```text
old leaf:  polynomial/trigonometric monomial -> beta/Z_h exact moment
new leaf:  polynomial kernel * algebraic atom -> holonomic moment recurrence/operator
```

This is not spatial discretization. There are still no material points, Gauss points, cells, or spatial collocation nodes.

After thickness contraction, the remaining complete-halfwave `X,Y` integrals are beta-weighted algebraic periods. Their general two-coordinate creative-telescoping runtime remains open.

---

## 10. Literature/mathematical backend identity

The admissible next implementation class is consistent with reduction-based creative telescoping for algebraic functions (Chen, Kauers, Koutschan, ISSAC 2016 / arXiv:1602.00424): algebraic functions admit exact reduction and telescoper construction rather than requiring direct elementary antiderivatives.

The project uses that mathematics only as a solution backend. It does not alter the R10 material law or obtain material-theory identity.

---

## 11. Gate decision

```text
R10_PHYSICS = UNCHANGED
FIVE_TERM_MEMBRANE_MODEL = RETAINED
GLOBAL_ROOT_TOPOLOGY = (D,q) AFTER CONDENSATION
UNIVERSAL_SMOOTH_QUARTIC_SECOND_ORDER_ODE = PASS_EXACT
PROTOTYPE_QUOTIENT_FIELD_ANNIHILATOR = PASS_EXACT
POLYNOMIAL_THICKNESS_MOMENT_RECURRENCE = PASS_EXACT
ANTIDERIVATIVE_HOLONOMIC_ORDER_LE_3 = PASS_EXACT
FULL_R10_FIELD_ORDER_LE_64 = PASS_FORMAL
FULL_R10_COMPOSITUM_RUNTIME = OPEN
GENERAL_BETA_WEIGHTED_XY_TELESCOPER = OPEN
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
NEW_Pu = NOT_RUN
```

## 12. Unique next gate

```text
UNIFIED_V1_FULL_R10_ALGEBRAIC_COMPOSITUM_HOLONOMIC_TARGET_CONTRACTION_GATE
```

The next gate must construct one actual full-R10 thickness annihilator/finite moment state including the `s_eta,s_1,s_10` compositum and then connect its thickness-contracted coefficients to the beta-weighted `(X,Y)` General-D15 creative-telescoping layer. No new Pu is released before that common target runtime passes.
