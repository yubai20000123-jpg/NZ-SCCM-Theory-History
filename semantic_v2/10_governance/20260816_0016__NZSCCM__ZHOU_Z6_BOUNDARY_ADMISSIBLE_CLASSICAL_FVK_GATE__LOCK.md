# NZ-SCCM — Zhou/Z6 实际面内边界 Classical FvK/Airy 零空间积分门禁

**Timestamp:** 2026-08-16 00:16 +08:00  
**Identity:** boundary-specific classical-limit gate; no nonlinear-material Pu

## 1. 固定边界

本阶段继续强制：

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order geometric source retained
R10/N48/Cayley-Hamilton/General-D15 physical-material line unchanged but NOT entered in this gate
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
Gauss/Simpson/adaptive/collocation/cells/material-point-grid = PROHIBITED
```

23:43 AR2 spatial-Gauss path and `Pu=40.97334 MN` remain retracted historical error evidence.

## 2. Direct Zhou source boundary class

Zhou thesis Table 1.3 for the four-edge simply-supported wall gives the in-plane translation settings:

```text
loaded top:    ux=0, uy=unset
loaded bottom: ux=0, uy=0
non-loaded left/right: ux=unset, uy=unset
```

and `uz=0` on all four edges for the out-of-plane simply-supported class.

Therefore the classical membrane boundary gate uses:

```text
u(x,0)=u(x,a)=0                         essential transverse displacement on loaded ends
lateral x=0,b edges = in-plane free     natural side tractions Nx=Nxy=0
```

The previous uniform free-Poisson base field is not boundary admissible.

## 3. Gate decision

The 00:07 particular Airy field passes compatibility but fails the free lateral-side traction condition because its `(0,2)` term gives nonzero `Nx` at `x=0,b`.

An exact homogeneous biharmonic correction has now been derived for this side-traction defect. It satisfies `Nx=Nxy=0` exactly at both lateral sides, with no spatial numerical integration.

However that side-corrected field still fails the loaded-edge pointwise condition implied by `u=0`:

```text
epsilon_x(x,0)=0 -> Nx(x,0)-nu Ny(x,0)=0
```

The residual is an x-dependent combination of the side-correction hyperbolic functions and `cos(2 alpha x)`. A single mean axial resultant cannot cancel it. Therefore a second homogeneous boundary-layer family is mathematically necessary.

Locked verdict:

```text
ZHOU_SOURCE_LOADED_EDGE_UX_ZERO = CONFIRMED
ZHOU_SIDE_INPLANE_FREE = CONFIRMED
CLASSICAL_FVK_PARTICULAR_ONLY = FAIL_SIDE_TRACTION
EXACT_SIDE_FREE_BIHARMONIC_CORRECTION = PASS
SIDE_FREE_CORRECTION_ALONE = FAIL_LOADED_EDGE_UX_ZERO
EXACT_ZHOU_MIXED_BOUNDARY_AIRY_CLOSURE = OPEN
ZHOU_BOUNDARY_CLASSICAL_MEMBRANE_STIFFENING_SIGN = POSITIVE / PASS
ZERO_SPATIAL_NUMERICAL_INTEGRATION = PASS
R10_N48_MAPPING = BLOCKED_UNTIL_MIXED_BOUNDARY_CLOSURE
NEW_Z6_Pu = NOT_CALCULATED
```

## 4. What is retired / retained

Retained:

```text
D+q+c old in-plane field is incomplete
FvK geometric source contains (2,0)/(0,2) harmonic content
compatibility-generated membrane response gives positive postbuckling stiffness
```

Retired:

```text
p20,p02 as two independent free membrane coordinates
particular Airy field as a complete Zhou-boundary closure
```

## 5. Mandatory next execution

```text
ZHOU_MIXED_END_RESTRAINT_HOMOGENEOUS_BIHARMONIC_SERIES_ZERO_QUADRATURE
```

Requirements:

1. add only the homogeneous biharmonic boundary-layer family needed to satisfy `u(x,0)=u(x,a)=0` together with free lateral tractions;
2. determine its coefficients from compatibility/equilibrium/boundary conditions, not from Pu fitting;
3. use analytical Fourier/hyperbolic moments only;
4. prove positive classical postbuckling stiffness after condensation;
5. only after this closure passes may the membrane field be mapped back into R10/N48/Cayley-Hamilton and a Z6 Pu path be recomputed.
