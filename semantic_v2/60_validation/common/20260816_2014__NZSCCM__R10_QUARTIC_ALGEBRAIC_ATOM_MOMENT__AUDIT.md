# NZ-SCCM — quartic algebraic atom / special-function moment gate audit

**Timestamp:** 2026-08-16 20:14 +08:00

## A. Frozen mechanics

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = PRESERVED
Nguyen second-order continuous kinematics = PRESERVED
five internal membrane coordinates = PRESERVED
outer root topology (D,q) = PRESERVED
R10 physical current law = UNCHANGED
reinforcement adapter = UNCHANGED
same-state consistent tangent / KZ = REQUIRED
General-D15 polynomial moment engine = RETAINED_AS_BASE
```

No experiment, Zhou/Winter capacity, historical Pu error sign, or target Pu was used to select any algebraic identity, threshold, root or special-function representation.

## B. Zero-integration audit

Formal production counters remain

```text
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
N_formal_thickness_quadrature=0
Gauss=0
Simpson=0
adaptive=0
collocation=0
material_point_grid=0
```

The only numerical integration in the reproducer is an 80-digit **audit-only** one-dimensional check of an Appell-F1 identity.  It is not used to generate coefficients, structural moments, roots or capacities and therefore does not alter formal production counters.

## C. Smooth split exactness

The symbolic reproducer gives exact zero for

```text
t+c - x^2/sqrt(x^2+eta^2)
t-c - x^3/(x^2+eta^2)
```

and exact zero Cayley-Hamilton residuals for

```text
sqrt(E^2+eta^2 I)
 = [tr(E) E +(s_eta^2-tr(E)^2)I/2]/s_eta.
```

The scalar atom relation

```text
s_eta^4
-2*(T^2-2D+2eta^2)*s_eta^2
+T^2*(T^2-4D)=0
```

is therefore accepted as an exact source identity.

## D. Differential closure

Implicit differentiation of the quartic stays rational in the same scalar atom.  Hence no new fitted tangent channel is introduced by this gate.

```text
QUARTIC_ATOM_DIFFERENTIAL_CLOSURE = PASS_EXACT
```

This is a material/analytic closure statement.  It does not by itself certify that every spatial target moment is already evaluated.

## E. Compression inverse

The 2x2 inverse uses the exact adjugate/determinant identity.  It adds no independent radical atom.

```text
COMPRESSION_INVERSE_INDEPENDENT_ATOM = ELIMINATED
```

## F. Tension knots

The dimensionless quintic and the original unsquared source equation give unique positive roots

```text
u1  = 1.00186724268468168246906635849161509948...
u10 =10.00018749218805659222879628606987649975...
```

The negative-lambda bound and positive-lambda monotonicity prove that the source-knot activation is equivalent to crossing fixed positive principal-strain thresholds.

The six positive-part powers are therefore exactly reduced to two shifted spectral projector atoms.

```text
TENSION_KNOT_THRESHOLDS = PASS_EXACT
TENSION_POSITIVE_PART_NESTING = REDUCED_EXACT
```

## G. Algebraic field size

Three scalar algebraic generators `s_eta,s_1,s_10`, each of degree at most four over the finite base field, give the conservative bound

```text
FIELD_DEGREE_UPPER_BOUND <= 64.
```

This is not interpreted as 64 structural unknowns or 64 required terms.  It is only a fixed algebraic extension bound and is independent of the old material fit orders.

## H. Complete-halfwave fold

The `u=sin^2 X`, `v=sin^2 Y` transformation and quadrant-parity argument are exact for the complete halfwave.  Odd terms vanish; even target terms become beta-weighted algebraic periods on a fixed domain.  No numerical or analytic spatial subdomain splitting is introduced.

```text
COMPLETE_HALFWAVE_BETA_FOLD = PASS_EXACT
```

## I. Exact prototype moment checks

Two subfamilies were actually closed:

1. affine-thickness `1/sqrt(y^2+eta^2)` moments by a finite endpoint recurrence, with exact derivative residuals zero through the tested orders;
2. one-harmonic D15 moments by Appell `F1`, with audit discrepancies below `1e-80` at the test point.

These establish that special-function closure can replace high-order material polynomial expansion for meaningful subfamilies.

## J. Generic non-commuting 2x2 boundary

A generic rational affine thickness pencil produces a square-free quartic `det(E^2+eta^2 I)`.  Direct SymPy exact integration of `tr sqrt(E^2+eta^2I)` remains unevaluated.

Required interpretation:

```text
DIRECT_CAS_INTEGRATE_COMMON_BACKEND = NOT_ESTABLISHED
```

This result must **not** be misread as:

```text
SPECIAL_FUNCTION_CLOSURE_IMPOSSIBLE = TRUE
```

The correct remaining object is an algebraic period requiring a more structured Picard-Fuchs / creative-telescoping / holonomic treatment.

## K. Capacity audit

```text
new current-material r(D,q) solve = NOT_RUN
new Case21 Pu = NOT_RUN
new Z0-Z6 Pu = NOT_RUN
```

No previous capacity identity is upgraded by this gate.

## L. Final verdict

```text
R10_EXACT_MATRIX_SOURCE_LIFT = RETAIN_PASS
SMOOTH_SPLIT_SINGLE_SCALAR_QUARTIC_ATOM = PASS_EXACT
COMPRESSION_INVERSE_INDEPENDENT_ATOM = ELIMINATED
TENSION_KNOT_THRESHOLDS = PASS_EXACT
TENSION_POSITIVE_PART_NESTING = REDUCED_EXACT
QUARTIC_ATOM_DIFFERENTIAL_CLOSURE = PASS_EXACT
FIXED_ALGEBRAIC_FIELD_DEGREE_UPPER_BOUND = 64
COMPLETE_HALFWAVE_BETA_FOLD = PASS_EXACT
AFFINE_THICKNESS_MOMENT_RECURRENCE = PASS_EXACT
ONE_HARMONIC_APPELL_F1 = PASS_EXACT
DIRECT_GENERIC_NONCOMMUTING_CAS_INTEGRATE = FAIL_AS_COMMON_BACKEND
FULL_GENERAL_D15_ALGEBRAIC_PERIOD_RUNTIME = OPEN
NEW_Pu = NOT_RUN
```

## M. Next unique gate

```text
UNIFIED_V1_NONCOMMUTING_QUARTIC_ALGEBRAIC_PERIOD_HOLONOMIC_GENERAL_D15_GATE
```
