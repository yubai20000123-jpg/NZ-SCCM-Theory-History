# NZ-SCCM — Zhou end-restraint Papkovich–Fadle zero-quadrature gate lock

**Timestamp:** 2026-08-16 00:47 +08:00

## Locked task

Execute only:

`ZHOU_MIXED_END_RESTRAINT_HOMOGENEOUS_BIHARMONIC_SERIES_ZERO_QUADRATURE`

No new nonlinear-material Pu is authorized in this gate.

## Source boundary retained

Zhou four-edge simply-supported wall translation boundary:

- loaded top: ux=0, uy=unset;
- loaded bottom: ux=0, uy=0;
- non-loaded left/right: ux,uy unset.

The present gate addresses the previously confirmed transverse loaded-end restraint mismatch `ux=0` while retaining lateral in-plane freedom.

## Hard computational boundary

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
Gauss/Simpson/adaptive/collocation/cells/material-point-grid = PROHIBITED
```

Coefficient-space root solving and exact analytical moments are permitted. They are not spatial discretization.

## Formal closure family

Use the even Papkovich–Fadle / homogeneous biharmonic strip family on the centered transverse coordinate

`t=(x-b/2)/(b/2)`, `-1<=t<=1`.

The even transverse eigenfunction is

`F_n(t)=sin(lambda_n) cos(lambda_n t)-t cos(lambda_n) sin(lambda_n t)`

with nonzero complex roots

`sin(2 lambda_n)+2 lambda_n=0`.

Every mode satisfies the free lateral traction conditions exactly:

`F_n(+/-1)=F_n'(+/-1)=0`.

For a finite panel with identical transverse restraint at both physical loaded ends, use

`Y_n(y)=cosh(lambda_n (y-a/2)/(b/2))/cosh(lambda_n a/b)`.

For the AR2 object `a/b=2, m=2`, the one-halfwave domain is chosen as the physical end to the midheight symmetry plane: `0<=y<=a/2=ell`. The internal line `y=a/2` is a symmetry interface, NOT a fictitious loaded edge; therefore `ux=0` must not be imposed there.

## Exact coefficient realization

The end boundary operator is

`B_n(t)=lambda_n^2 F_n(t)-nu F_n''(t)`

which simplifies to

`B_n=(1+nu) lambda_n^2 F_n+2 nu lambda_n cos(lambda_n) cos(lambda_n t)`.

The formal exact closure is

`H(t)+Re sum_{n>=1} a_n B_n(t)=0`.

Finite reproducibility uses exact cosine moments only:

`int_{-1}^1 residual(t) cos(k pi t) dt = 0`.

No point collocation is accepted as evidence.

## Gate decision vocabulary

```text
PAPKOVICH_FADLE_EVEN_EIGENFAMILY = DERIVED
SIDE_TRACTION_FREE_PER_MODE = REQUIRED_PASS
FORMAL_TRANSVERSE_END_RESTRAINT_SERIES = REQUIRED_CLOSED
N6_EXACT_MOMENT_TRUNCATION = COEFFICIENT_SPACE_REPRO_ONLY
ZERO_SPATIAL_NUMERICAL_INTEGRATION = REQUIRED_PASS
AR2_M2_ONE_HALFWAVE_MAPPING = REQUIRED_PASS_BY_END_TO_MIDHEIGHT_SYMMETRY
FICTITIOUS_INTERNAL_UX_ZERO = PROHIBITED
FULL_ZHOU_ALL_INPLANE_END_DOF_EQUIVALENCE = NOT_CLAIMED_BY_THIS_GATE
NEW_Z6_Pu = NOT_AUTHORIZED
```
