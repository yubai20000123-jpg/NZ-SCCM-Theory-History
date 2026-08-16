# NZ-SCCM — R10 exact finite-matrix source lift audit

**Timestamp:** 2026-08-16 20:05 +08:00

## A. Frozen mechanics

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = PRESERVED
Nguyen second-order kinematics = PRESERVED
five membrane internal coordinates = PRESERVED
R10 physical current law = UNCHANGED
reinforcement adapter = UNCHANGED
P,Rq,L root topology = PRESERVED
same-state KZ requirement = PRESERVED
```

No experimental, Zhou, Winter, or desired-capacity calibration is used.

## B. Why this is not a new constitutive law

The scalar functions `pi,c,t,C,uR,T,U` and the two-principal-value stress equation are unchanged.

The present gate only uses spectral/matrix identities to rewrite exactly the same scalar mapping.

Therefore:

```text
R10_PHYSICS_REOPENED = NO
R10_SOURCE_PARAMETERS_CHANGED = NO
```

## C. Tension spline exactness

The existing `uR(t)` branches form an exact degree-5 truncated-power spline in `z=t/(rho/kappa)`.

Symbolic residuals:

```text
middle branch = 0 exactly
upper branch  = 0 exactly
```

The spline uses only the two existing physical source knots `z=1` and `z=10`.

## D. Smooth split exact matrix lift

For

\[
R_\eta(E)=\sqrt{E^2+\eta^2I},
\]

the matrix formula

\[
\Pi(E)=\frac12E^2(R_\eta+E)(E^2+\eta^2I)^{-1}
\]

has eigenvalues exactly equal to the frozen scalar `pi(lambda_i)`. Thus `c=Pi(-E)` and `t=Pi(E)` are exact spectral lifts.

The random numerical audit gives a worst explicit-matrix residual below `7e-11` across Z0-Z6 guards; this is a floating conditioning check, not an approximation tolerance.

## E. Full 2D stress identity

The principal formula is transformed by exact identities

```text
C_i^2 C_j = det(C) C_i
C_i T_j   = C_i (tr(T)-T_i)
T_i T_j T_j^7 = det(T) (tr(T^7)-T_i^7)
```

to

\[
S=
U-ACC\det(C)C
+C(\operatorname{tr}(T)I-T)
-\rho A_T\det(T)(\operatorname{tr}(T^7)I-T^7).
\]

Across 3500 random matrix states (500 per case), the largest stress-matrix discrepancy from direct principal-source evaluation is approximately `8.05e-15`.

```text
R10_2D_STRESS_MATRIX_IDENTITY = PASS_EXACT
```

## F. Tangent identity

Because the current stress mapping is identical as a function of `E`, its Frechet derivative is also identical wherever the frozen source derivative exists.

The required derivatives are finite:

```text
sqrt atom  -> Sylvester equation
inverse    -> dQ^-1=-Q^-1 dQ Q^-1
matrix power -> finite Leibniz sum
determinant -> adjugate contraction
```

The two spline knots are C2 in the frozen source; the first derivative used by the material tangent is continuous.

```text
CONSISTENT_TANGENT_GRAPH = PASS_FORMAL
```

A structural same-state KZ is not run in this gate.

## G. Complexity audit

The candidate exact source graph has no fitted `Ng,Nc,Nt` and no beta/Chebyshev nesting.

Fixed atom families:

```text
1. sqrt(E^2+eta^2 I)
2. inverse(I+(kappa-2)c+c^2)
3. C2 positive-part powers at t/a=1
4. C2 positive-part powers at t/a=10
```

`T^7` is a finite matrix power, not a separately fitted channel.

Thus the 19:32 RC1 polynomial composition ledger no longer controls this candidate representation.

This is a **representation-complexity pass**, not yet a structural integration pass.

## H. Zero-integration audit

```text
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
N_formal_thickness_quadrature=0
Gauss=0
Simpson=0
adaptive=0
collocation=0
material-point grid=0
```

The random state audit samples material matrices only. It is not a structural spatial discretization and is not used to calculate any resultant.

## I. What remains open

The fixed atom graph still contains algebraic square-root, reciprocal and positive-part functions.

The present General-D15 engine closes polynomial/integer-trigonometric/thickness moments, but a direct exact/controlled target-moment rule for these algebraic atoms has not yet been executed.

```text
GENERAL_D15_ALGEBRAIC_ATOM_MOMENT_CLOSURE = OPEN
```

## J. Capacity audit

```text
new r(D,q) = NOT_SOLVED
new Case21 Pu = NOT_RUN
new Z0-Z6 Pu = NOT_RUN
```

## K. Final verdict

```text
STRUCTURALLY_CLOSED_COMPILER_REDESIGN_DIRECTION = PASS_TO_FIXED_ATOM_BOUNDARY
R10_EXACT_SOURCE_MATRIX_LIFT = PASS_EXACT
FIXED_ALGEBRAIC_ATOM_REDUCTION = PASS
STRUCTURAL_TARGET_MOMENT_RUNTIME = OPEN
NEW_Pu = NOT_RUN
```

## L. Next gate

```text
UNIFIED_V1_R10_FIXED_ALGEBRAIC_ATOM_GENERAL_D15_CAS_MOMENT_CLOSURE_GATE
```

The next gate may not return to the already failed nested-RC1 ordinary-polynomial flattening route.
