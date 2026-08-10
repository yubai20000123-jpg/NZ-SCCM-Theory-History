# R06B — 3D constitutive visualization correction

Date: 2026-08-10

## Trigger

User rejected the prior 2D contour-style presentation as insufficient for understanding the actual constitutive surface domain. The corrected requirement is to plot the current map as a true 3D surface and place corresponding projections on all three coordinate planes.

## Correction

For the four-dimensional mapping

(ε1, ε2) -> (σ1, σ2),

one 3D surface is insufficient. The correct pair is:

- σ1(ε1, ε2), with projections on ε1-ε2, ε1-σ1, ε2-σ1;
- σ2(ε1, ε2), with projections on ε1-ε2, ε1-σ2, ε2-σ2.

This visualization format is now the default for material-surface discussion.

## NC execution

R06B generated the two NC reference surfaces and two signed smoothing-difference surfaces for the R02 k=1.25 mild regularization.

The quadrant diagnostic shows that the k=1.25 change is concentrated most strongly in TC/CT:

- CC max |Δσ|/fc = 0.001709;
- TC/CT max |Δσ|/fc = 0.005680;
- TT max |Δσ|/fc = 0.000378.

Thus the earlier statement that smoothing mainly affects a narrow mixed tension-compression corridor is directly visible in the 3D surface difference.

## UHPC boundary

No formal UHPC 3D current surface was fabricated. Project source registers still identify the arbitrary multiaxial UHPC current stress-strain closure as open/incomplete. Only source slices, scalar laws, axisymmetric/triaxial fragments, and failure-surface constraints are currently available.

A schematic UHPC surface must not be confused with a formal current operator. When the UHPC operator is frozen, the same 3D + three-projection format must be used.
