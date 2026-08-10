# 云露 source map — steel-shell / Y branch

- Source PDF: `考虑薄膜效应的钢箱混凝土壁板局部屈曲行为研究_云露.pdf`
- PDF SHA-256: `1fce0f9ce9058f00b2a6ddd0f6dd11faa41366816e2145348812c1a93884e897`
- Role: primary source for unilateral wall-panel restraint, large-deflection/membrane post-buckling mechanics and steel-wall stress redistribution.

## Effective source content

- free-plate buckling background;
- von Kármán large-deflection formulation;
- concrete restraining inward buckling and outward unilateral wall deformation;
- assumed deflection field, stress-function construction and Galerkin solution;
- imperfection, width-thickness and aspect-ratio influence;
- post-buckling stress redistribution / effective-width derivation.

## Current-use boundary

The project may reuse the mechanics and derivation logic, but Yun's later empirical effective-width correction (including the fitted `k=0.74`) is historical empirical design closure and is not automatically part of the current NZ-SCCM production operator. FE results remain validation evidence, not permission to introduce formal spatial cells/integration points.
