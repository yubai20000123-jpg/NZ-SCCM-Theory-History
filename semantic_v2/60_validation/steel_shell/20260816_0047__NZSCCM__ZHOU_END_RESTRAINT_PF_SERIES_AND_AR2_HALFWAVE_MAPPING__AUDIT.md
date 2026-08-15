# NZ-SCCM — Zhou end-restraint PF series and AR2 one-halfwave mapping audit

**Timestamp:** 2026-08-16 00:47 +08:00

## Audit question

Can the x-dependent transverse loaded-end residual left by the 00:16 side-free FvK/Airy solution be closed analytically, with zero spatial numerical integration, and can that physical end layer be represented on the AR2 `m=2` one-complete-halfwave production domain without imposing a fictitious `ux=0` at the internal halfwave interface?

## A. Source boundary gate

Retained source facts:

```text
loaded top:    ux=0, uy=unset, uz=0
loaded bottom: ux=0, uy=0,     uz=0
lateral sides: ux=unset, uy=unset, uz=0
```

The present audit is limited to the transverse `ux=0` end-restraint correction already identified as inconsistent with the old uniform free-Poisson field.

Decision:

`SOURCE_TRANSVERSE_END_RESTRAINT = CONFIRMED`.

## B. Free-side homogeneous eigenfamily

For

`F=sin(lambda)cos(lambda t)-t cos(lambda)sin(lambda t)`,

`F(+/-1)=0` identically and `F'(+/-1)=0` for roots of

`sin(2 lambda)+2 lambda=0`.

Therefore each Airy mode `F(t)Y(y)` gives exactly zero `Nx` and `Nxy` on both lateral sides.

Decision:

`SIDE_TRACTION_FREE_PER_MODE = PASS`.

## C. Homogeneous biharmonic gate

With

`Y=cosh(lambda(y-a/2)/c)/cosh(lambda a/(2c))`, `c=b/2`,

`Y''=(lambda/c)^2Y`.

The transverse mode is a generalized solution of

`(D_t^2+lambda^2)^2F=0`.

Hence

`nabla^4(FY)=0`.

Decision:

`HOMOGENEOUS_BIHARMONIC_FIELD = PASS`.

## D. Mean axial resultant gate

The PF correction contributes `Ny ~ F''`. Since

`int_-1^1 F'' dt = F'(1)-F'(-1)=0`,

each mode is self-equilibrated and does not alter the mean axial resultant.

Decision:

`PF_CORRECTION_ZERO_MEAN_AXIAL_RESULTANT = PASS`.

## E. End boundary closure gate

The loaded-end transverse-strain operator is

`B=lambda^2F-nu F''`.

The formal series equation is

`H(t)+Re sum a_n B_n(t)=0`.

The present implementation does not use point collocation. Complex coefficients are determined from closed analytical cosine moments. The N=6 truncation reduces omitted exact cosine moments through k=24 to:

```text
original Z6, chi=4/3, nu=.18: 4.59790404023e-6
normalized by max H moment:      2.46510424082e-6

AR2, chi=1, nu=.18:             1.34959944364e-6
normalized by max H moment:      1.77440598813e-6
```

The formal infinite PF series is the exact closure family; N=6 is only a finite coefficient-space reproduction.

Decision:

```text
FORMAL_TRANSVERSE_END_RESTRAINT_SERIES = CLOSED
N6_COEFFICIENT_MOMENT_REPRODUCTION = PASS
N6_POINTWISE_EXACTNESS = NOT_CLAIMED
```

## F. Zero spatial integration gate

No spatial quadrature is used. No spatial residual grid is used. No collocation points are used. No spatial subdomains are introduced.

Only:

- complex eigenvalue roots;
- exact analytical moments;
- finite coefficient-space linear systems

are used.

Decision:

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
ZERO_SPATIAL_NUMERICAL_INTEGRATION = PASS
```

## G. Original-Z6 versus AR2 physical end-layer overlap

The exact midheight factor is `1/cosh(lambda_n a/b)`.

First-mode magnitude:

```text
original Z6 a/b=.75: 0.413781180629
AR2 a/b=2:           0.029623149557
```

Thus the transverse end-restraint layers overlap strongly in original squat Z6 but are much more localized in AR2. This is an analytical field property, not a sampled observation.

## H. AR2 m=2 one-halfwave mapping

AR2:

```text
a=24000 mm
b=12000 mm
m=2
ell=12000 mm
```

The physical loaded ends are `y=0,a`. The internal out-of-plane nodal line is `y=a/2` and is not a loaded edge.

Because m=2, one complete halfwave is exactly the physical half-panel `0<=y<=a/2`. The PF finite-length field is symmetric there:

`Y'(a/2)=0`.

Therefore the correct one-halfwave mapping uses:

```text
y=0   = physical loaded end
y=ell = physical midheight symmetry plane
```

and does not impose `ux=0` at `y=ell`.

Decision:

```text
AR2_M2_ONE_HALFWAVE_MAPPING = PASS
FICTITIOUS_INTERNAL_UX_ZERO = PROHIBITED
```

This conclusion is not generalized to arbitrary m>2.

## I. Remaining theory boundary

The PF/Airy field is a classical elastic membrane solution. The NZ-SCCM material operator is nonlinear and strain-driven.

Therefore it would be invalid to insert the elastic Airy stress field directly as the nonlinear R10/N48 stress field.

Before nonlinear capacity calculation, the PF boundary correction must be converted to either:

1. a compatible displacement/strain basis whose elastic condensed solution reproduces this PF result; or
2. a rigorously equivalent mixed formulation preserving constitutive compatibility.

All generalized material residuals and moments must remain analytically evaluable with zero spatial quadrature.

Also, this gate does not independently prove complete equivalence to the bottom `uy=0` versus top `uy=unset` FE boundary detail.

Decision:

```text
FULL_ZHOU_ALL_INPLANE_END_DOF_EQUIVALENCE = NOT_YET_PROVEN
R10_N48_D15_MAPPING = BLOCKED_PENDING_ELASTIC_EQUIVALENCE_CONSTRUCTION
NEW_Z6_Pu = NOT_CALCULATED
```

## Final audit verdict

```text
PAPKOVICH_FADLE_EVEN_EIGENFAMILY = DERIVED
SIDE_TRACTION_FREE_PER_MODE = PASS
HOMOGENEOUS_BIHARMONIC_FIELD = PASS
PF_CORRECTION_ZERO_MEAN_AXIAL_RESULTANT = PASS
FORMAL_TRANSVERSE_END_RESTRAINT_SERIES = CLOSED
N6_EXACT_MOMENT_TRUNCATION = PASS_AS_COEFFICIENT_SPACE_REPRO
ZERO_SPATIAL_NUMERICAL_INTEGRATION = PASS
AR2_M2_ONE_HALFWAVE_MAPPING = PASS
FICTITIOUS_INTERNAL_UX_ZERO = PROHIBITED
FULL_ZHOU_ALL_INPLANE_END_DOF_EQUIVALENCE = NOT_YET_PROVEN
NEW_Z6_Pu = NOT_CALCULATED
```

## Next execution gate

`AR2_PF_BOUNDARY_MEMBRANE_TO_R10_N48_D15_ZERO_QUADRATURE_MAPPING_GATE`

Pass condition: construct the nonlinear-capable membrane kinematic/mixed representation, prove its elastic limit reproduces the present PF closure, and retain zero spatial quadrature. Only after that may a new AR2 Z6 Pu calculation resume.
