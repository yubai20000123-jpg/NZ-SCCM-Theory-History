# NZ-SCCM 3D CURRENT MAP VISUALIZATION SPEC — R06B

Date: 2026-08-10

## Purpose

Correct the constitutive visualization format. A four-dimensional current map

(ε1, ε2) -> (σ1, σ2)

must not be represented only by a 2D contour map if the objective is to inspect the actual surface geometry.

## Required visualization format

Use a pair of 3D surfaces:

1. z = σ1(ε1, ε2)
2. z = σ2(ε1, ε2)

For each 3D surface, also project the same scalar surface onto all three orthogonal coordinate planes:

- ε1-ε2 base plane;
- ε1-σi side plane;
- ε2-σi side plane.

The two surfaces together represent the 2D current-map manifold embedded in the 4D space (ε1, ε2, σ1, σ2).

## NC figures executed in R06B

Generated session figures:

- `01_NC_sigma1_surface_3projections.png`
- `02_NC_sigma2_surface_3projections.png`
- `03_NC_smoothing_delta_sigma1_3projections.png`
- `04_NC_smoothing_delta_sigma2_3projections.png`
- `05_NC_sigma1_sigma2_pair_3D_with_projections.png`

NC reference visualization range:

lambda1, lambda2 in [-1.20, 0.55],

where lambda_i = ε_iu / ε0.

The R02 k=1.25 mild-smoothing difference surfaces were also plotted in the same format, so the geometry of where smoothing changes the current map can be inspected directly.

Quadrant-level diagnostic effect of k=1.25 on the reference NC map:

| sector | max abs change / fc | P95 abs change / fc | mean signed change / fc |
|---|---:|---:|---:|
| CC | 0.001709 | 0.000416 | 0.000057 |
| TC/CT | 0.005680 | 0.002110 | 0.000509 |
| TT | 0.000378 | 0.000268 | 0.000165 |

This confirms that the mild transition smoothing changes the TC/CT region most strongly in this reference map; CC and TT changes are much smaller.

## UHPC visualization rule

Do not fabricate a full UHPC 3D current surface before the UHPC multiaxial current operator is frozen.

Current project source ledgers record that:

- the general UHPC pre-failure multiaxial stress-strain operator is not frozen;
- the TC 2D operator is incomplete;
- the TT two-direction law is not frozen;
- CC/C3 has source strength/failure constraints and selected axisymmetric fragments, but not a complete arbitrary biaxial/3D current stress-strain operator.

Therefore a source-grounded UHPC surface z=σi(ε1,ε2) cannot yet be drawn as a formal constitutive surface. Once the UHPC operator is frozen, it must be plotted with exactly the same pair-of-surfaces + three-projection format as NC.

## Governance consequence

Future constitutive-surface figures intended for material-shape decisions must use this 3D + three-orthogonal-projection format by default. 2D contour maps may be supplementary only.
