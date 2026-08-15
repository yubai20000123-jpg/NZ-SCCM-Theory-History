# Z6 boundary-warp preflight / aspect-ratio fallback lock

**Timestamp:** 2026-08-15 18:13 +08:00

## Locked decisions

```text
ZHOU_LOADED_EDGE_UX_CONSTRAINT = CONFIRMED
CURRENT_FREE_POISSON_AFFINE_INPLANE_FIELD_ADMISSIBILITY = FAIL FOR ZHOU BC
BOUNDARY_ADMISSIBLE_CONTINUOUS_WARP_FIELD = CONSTRUCTED
ELASTIC_STATIC_CONDENSATION = CLOSED_FORM_PASS
ZERO_STRUCTURAL_SPATIAL_QUADRATURE_COMPATIBILITY = PASS
FULL_NONLINEAR_R10_N48_COUPLED_Rq_Rc = NOT YET SOLVED
NAIVE_GENERALIZED_CH_EXPAND_THEN_COMPOSE = REPRESENTATION_RUNTIME_FAIL
BOUNDARY_MISMATCH_EXPLAINS_FULL_Z6_Pu_GAP = NOT CLAIMED
Z6_SQUARE_FULL_NZ_Pu = NOT SOLVED
```

## Admissible field

With `X=pi x/b`, `Y=pi y/a`, odd `n<=N`:

```text
F_N = -(4b/pi^2) sum cos(nX)/n^2
H_N = -(4b^2/pi^3) sum sin(nX)/n^3
u(x,y) = eps0*c*F_N*sin^2(Y)
v(x,y) = -eps0*D*y - eps0*c*H_N*(pi/a)*sin(2Y)
```

Properties:

```text
u(x,0)=u(x,a)=0 exactly
v_warp(x,0)=v_warp(x,a)=0 exactly
left/right in-plane displacement remains free
added linear gamma_xy = 0 exactly
N=1,3,5 are finite trigonometric-polynomial fields compatible with D15 exact moments
```

## Elastic gate

At `a/b=0.75`, `nu=0.18`:

```text
N=1: c/D=0.01411546, Keff/Kfree=1.03242069
N=3: c/D=0.01557057, Keff/Kfree=1.03218055
N=5: c/D=0.01609379, Keff/Kfree=1.03208818
```

The loaded-edge restraint strongly suppresses transverse Poisson expansion, but the elastic axial membrane stiffness rises only about 3.2%. Therefore no 24.5% Pu correction is inferred from this gate alone.

## Aspect-ratio fallback status

Synthetic source-side comparators were created for Z4/Z6 at `a/b=0.75,1.0,1.25`. For Z6 the Zhou fitted lower-envelope Pu remains approximately 49.5 MN across these ratios. This is a useful discriminator because the source comparator is nearly unchanged.

An unchanged single-q/current-local-cap partial probe for square Z6 (`a=b=12000`) was executed. Sampled states have not yet produced an Rq sign change, so no connected root or Pu is released.

## Frozen parent identity

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order kinematics
R10 / N48-C1-MM / Cayley-Hamilton / General D15 unchanged
A0=a/500
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
no Zhou/Winter calibration
no out-of-plane multimode expansion
```

## Current next task

```text
CURRENT_NEXT_TASK = Z6_BOUNDARY_WARP_SPARSE_STATIC_CONDENSATION
```

The next implementation must contract the `c` directional residual moment-first / sparsely and avoid constructing the full high-degree generalized stress polynomial before integration.
