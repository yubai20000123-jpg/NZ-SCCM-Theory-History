# P1-06 — Doh (2002) thesis theory audit

Evidence scope: Griffith Research Online PhD thesis, title page dated August 2002; repository metadata gives 2003. The thesis contains both experimental/LFEM work and the full WASTABT development. This audit focuses on the analytical Chapter 7 interface and records LFEM as a comparator, not as a direct-formula theory.

## A. STRUCTURAL_OBJECT

- Object: normal- and high-strength reinforced-concrete wall panels, one-way and two-way action, with support/restraint and eccentricity variations.
- Material: NSC/HSC concrete compression models, tension model, elastic-perfectly-plastic reinforcement; layered FE is used for comparison.
- Imperfection/loading: assumed central deflection and eccentric axial load; symmetry reduces TW analysis to one quarter.

## B. KINEMATICS

- WASTABT: beam-column unit strips and a product-sine wall field, Eq. (7.6): `Y_ij = Y_mn sin(alpha*pi*i/(2m)) sin(pi*j/(2n))`.
- LFEM: layered shell/finite-element field, with spatial layers through the concrete section; it is an FE comparator rather than the direct closed-form operator.
- Classification: `THEORETICAL_MODE + FINITE_DIFFERENCE` for WASTABT; `FE_MODE` for LFEM.

## C–E. EQUILIBRIUM/COMPATIBILITY

- No Airy stress function.
- Section compatibility is plane sections remain plane; section resultants are fibre/layer sums (Eq. 7.1–7.2).
- Global equilibrium is finite-difference strip equilibrium and numerical curvature/slope integration (Eq. 7.7–7.13).
- The beam-column term `P Y_ij`, eccentric end moment and strip reactions `F_ij` form the transverse equilibrium.

## F. POSTBUCKLING_RELATION

- `NO_EXPLICIT_POSTBUCKLING_RELATION`. A central deflection `Y_mn` is prescribed/incremented; forces, moments, curvature and deflections are iterated until `|Delta y - Delta y_new| <= tolerance`.
- The solver stops when `M_ij` exceeds the section moment capacity from Eq. (7.2); the peak/maximum failure load is reported.

## G. STRUCTURAL_DEMAND

- `N`, `M`, `M_ij`, `F_ij`, curvature and deflection are evaluated at strip/grid points.
- The control point is a spatially resolved grid station, not an Airy boundary stress point.

## CAPACITY_LAYER

- Fibre/layer integration of concrete and steel stress–strain laws; ultimate moment is the peak `M-phi` value.
- LFEM can include cracking and layered material response; WASTABT uses selected constitutive curves.

## CONTROL_LOCATION_SOURCE

`INCREMENTAL_SEARCH + FE_INFORMED + TEST_INFORMED` — assumed modal field, then iterative grid search, with LFEM and experiments used for validation.

## ULTIMATE_SOLVER

`INCREMENTAL_LOAD_PATH + PARAMETRIC_SEARCH + FE_PEAK` for the thesis's combined analytical/FE program family.

## EMPIRICISM_LOCATION

`MATERIAL_ONLY + STRUCTURAL_RESPONSE + WHOLE_PANEL_STRENGTH` — constitutive curves, assumed mode, strip idealisation and test/code comparison.

## VERIFIED_CLASS

`CLASS_D_VERIFIED` for the WASTABT/LFEM route; the thesis is not a Class A/B direct finite-root theory.

## NZ_SCCM_INTERFACE_COMPARISON

- KINEMATICS = `DIFFERENT`
- AIRY = `NO`
- POSTBUCKLING = `DIFFERENT`
- P_Q = `ABSENT`
- N_M_DEMAND = `RELATED`
- CAPACITY = `RELATED`
- CONTROL_LOCATION = `DIFFERENT`
- PU_CLOSURE = `DIFFERENT`
- OVERLAP_LEVEL = `MEDIUM`

## LESSONS_FOR_NZ_SCCM

The thesis demonstrates why RC wall methods drift toward iteration: section capacity is nonlinear, the global field is support-dependent, and the peak load is a coupled material/geometric instability. Its strongest reusable idea is the strict `section M-kappa` / `global equilibrium` separation. Its strongest warning is that replacing this with an empirical effective-height factor hides the side-restraint physics.

