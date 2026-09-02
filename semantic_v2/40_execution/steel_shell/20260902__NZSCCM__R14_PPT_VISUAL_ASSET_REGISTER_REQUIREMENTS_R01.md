# NZ-SCCM R14 — PPT VISUAL ASSET REGISTER REQUIREMENTS R01

**Date:** 2026-09-02

This file locks the visual-asset requirements established in the current chat before switching conversations.

## 1. Governing principle

The R14 technical ledger governs the narrative. Figures must explain already-frozen mechanics and must not introduce new topology, boundary conditions, material mechanisms, discretization, or root-selection logic.

Priority:

`G0 exact current UCFT geometry > G1 direct mechanics source > R14 equation-generated figure > strict 2D reduced diagram > clearly labeled analogous mechanism`.

Generic AI-generated engineering geometry is rejected when it is only visually plausible.

## 2. Locked source hierarchy

### G0 exact current object

Use current UCFT manuscript/project figures for the physical object: outer/inner steel plates, UHPC core, longitudinal PBL ribs and perforation/dowel relation, with correct longitudinal/axial direction.

### G1 direct mechanics sources

Preferred direct-source figures:

- Zhang Ning PBL-stiffened local-buckling geometry / wave-length relation;
- Yun Lu simply-supported compressed plate and Karman/Airy mechanics;
- Sun Lipeng PBL/local-buckling test morphology;
- Zhou Jun / Wang Shunan UHPC compression/failure background.

### R14 equation-generated figures

Generate directly from current equations for:

- integer global modes and `Pcr,m`;
- `P(q)`;
- R04 plane-stress von-Mises proportional projection;
- R02 `Pi(U)` and finite candidate roots;
- R06 physical local cell → normalized `(u,v)` domain → interior/edge/corner candidates → `Phi_max` → first radial yield;
- current UHPC stress–strain law;
- connected branch / material terminal / `J4` fold logic.

## 3. Internal-code external names

R04: `plane-stress von-Mises proportional yield projection` / yield-first steel-face branch.

R02: `energy-stationary reduced local-postbuckling amplitude model`.

R06: `finite-harmonic local-postbuckling stress reconstruction + constrained von-Mises maximization + first-yield scaling`.

Do not introduce R04/R02/R06 to an external audience as unexplained project codes.

## 4. Locked 14 visual assets before deck rebuild

1. G0-01 current UCFT exact configuration/exploded figure.
2. G0-02 gross-panel strict outline derived from current geometry.
3. G1-01 simply-supported axial-compression plate figure.
4. G1-02 Karman–Airy source figure/equation page.
5. G1-03 PBL local-buckling figure.
6. G1-04 real/analogous local-buckling failure morphology.
7. T-01 exact R14 2D section + strain gradients.
8. T-02 global mode `m=1,2,3` plots and discrete `Pcr,m` chart.
9. T-03 Airy derivative / membrane-resultant relationship schematic.
10. T-04 R04 Mises locus + proportional projection.
11. T-05 R02 `Pi(U)` + cubic candidate roots + minimum-energy `U*`.
12. T-06 R06 physical cell → `(u,v)` bounded domain → finite candidate sets.
13. T-07 connected equilibrium branch + competing terminal + `J4` fold.
14. T-08 current UHPC compression/tension curve from frozen R14 anchors.

Asset package must be audited before rebuilding the PPT.

## 5. Page-level geometry rules

- Every figure belongs to exactly one primary scale: GLOBAL, LOCAL, or SECTION.
- `x=transverse`, `y=axial`, `z=thickness` must remain consistent.
- Actual geometry and equivalent-theory geometry must be explicitly distinguished.
- `A_w` is the current equivalent longitudinal steel contribution in the R14 operator; do not invent a physical number/layout of ribs from `A_w`.
- Airy `F` is a membrane stress-resultant potential, not the out-of-plane deflection `w`.
- `q` is a connected equilibrium-branch coordinate, not a material load-history step.
- `U` is the local condensed amplitude, not a global displacement/load variable.
- R06 `u,v` are normalized bounded-domain coordinates/candidate-root coordinates, not spatial material sampling points.
- terminal is a branch event, not a deformation photograph.

## 6. Rebuild order

`source figures / exact geometry → equation-derived assets → geometry/boundary audit → slide layout → Excel/BH examples last`.

The Excel and BH050/BH005–BH100 results are auxiliary demonstrations only. They must not determine the theory order.

## 7. Acceptance gate for every figure

A figure is rejected unless all are unambiguous:

1. scale identity: GLOBAL / LOCAL / SECTION;
2. coordinate and load directions;
3. actual versus equivalent geometry;
4. PBL/UHPC/steel spatial relation;
5. source identity: exact/direct/analogous;
6. absence of forbidden hidden mechanisms such as effective width, material grid, FE root selection, incremental plastic history;
7. formula narrative remains valid without relying on an unsupported implication from the image.

## 8. Current PPT status

Previously generated R01/R02 decks are not the accepted visual baseline. Their formula narrative may be reused only after review, but the visual layer must be rebuilt from the asset register above.
