# Nguyen source map — ordinary concrete / RC panels

- Source PDF: `Nguyen-011325526.pdf`
- PDF SHA-256: `de4369d427540716e965bd9188ef0aaac77146eab3f054a433703f772e20111e`
- Role: primary source / numerical-source oracle.

## Effective regions

- Chapter 3: 2D concrete states U/TC/TT/CC/TCX, equivalent-uniaxial relations, Saenz compression, tension stiffening/shear retention, reinforcement relation.
- Chapter 4: Q4 + Hermite out-of-plane + discrete reinforcement + stability matrix and source numerical route.
- Chapter 6: imperfection/eccentricity, second-order kinematics, layered/coupled formulation; the thesis distinguishes derived full coupling from its implemented approximate solution.
- Appendix B: selected original program routines are preserved in `Nguyen_AppendixB/`.

## Current-use boundary

Nguyen material physics/source equations may constrain the current operator, but Nguyen's FE/Gauss/material-point architecture is historical numerical provenance and does not override the current formal zero-spatial-quadrature rule. Project transformations derived from Nguyen/Foster must be labelled as project transformations, not verbatim Nguyen equations.
