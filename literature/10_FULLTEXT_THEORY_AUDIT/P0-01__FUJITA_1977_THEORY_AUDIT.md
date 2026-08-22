# P0-01 — Fujita, Nomoto & Niho (1977) theory audit

Evidence scope: J-STAGE version-of-record PDF, 8 pages. English abstract and section headings are machine-readable; Japanese equation text is affected by legacy RKSJ encoding. Equation numbers and the mechanics sequence are therefore recorded, but unreadable symbols are not reconstructed.

## A. STRUCTURAL_OBJECT

- Object: stiffened steel plate; square/rectangular plate examples with longitudinal and transverse stiffeners.
- Boundary/loading: in-plane compression; simply supported edge idealisation is used in the analytical plate examples.
- Imperfection: initial out-of-plane deflection is included in the plate energy formulation.
- Material: elastic plate in the large-deflection stage, followed by elastic-perfectly-plastic/collapse-mechanism treatment; stiffener geometry enters through area and flexural rigidity.

## B. KINEMATICS

- Kármán large-deflection plate kinematics are stated in the first analytical section. Unknown amplitudes are `A1,A2,A3,B1,B2,B3,W` (PDF Eq. 1a–1d; pp. 191–192).
- The assumed displacement family is sinusoidal/half-wave compatible with the simply supported boundaries; the initial shape `w0` is taken in the same modal family.
- Classification: `THEORETICAL_MODE + RAYLEIGH_RITZ`; not an empirical shape and not an FE mode.
- Exact symbolic `u(x,y), v(x,y), w(x,y), w0(x,y)` cannot be losslessly transcribed from the Japanese scan/text encoding; the PDF itself is the governing evidence.

## C. IN_PLANE_EQUILIBRIUM

- The paper works with membrane resultants `Nx, Ny, Nxy` and bending moments `Mx, My, Mxy` (p. 191).
- No explicit Airy stress function `F(x,y)` is named in the available text. Equilibrium is embedded in the Kármán/Rayleigh–Ritz energy formulation. `AIRY = UNRESOLVED/NOT_EXPLICIT`.

## D. COMPATIBILITY

- Nonlinear membrane compatibility is included through Kármán strain terms; the total potential energy is stationarised with respect to the Ritz amplitudes (Eq. 7–10, pp. 191–192).
- Classification: `RITZ + APPROXIMATE_MODE`, not an incremental compatibility solve.

## E. TRANSVERSE_EQUILIBRIUM

- Large-deflection plate equilibrium is obtained from the stationary total potential energy and the Rayleigh–Ritz equations (Eq. 10–11).
- The second analytical branch is a plastic collapse-mechanism calculation, not a transverse FE equilibrium equation.

## F. POSTBUCKLING_RELATION

- The elastic/Ritz branch produces a load–lateral-deflection relation and post-buckling response; Fig. 2 is explicitly labelled “Load-lateral deflection for elastic-plastic plate”.
- No single polynomial `P=P(q)` is recoverable from the text layer. The relation is a finite algebraic system in Ritz amplitudes and load parameter `P`.
- Physical amplitude: `W`/lateral deflection; initial defect `W0`.
- `Pcr` is the bifurcation/elastic buckling point obtained from the Ritz solution; no incremental load stepping is required in the stated analytical procedure.
- Classification: `NO_EXPLICIT_SCALAR_P_Q`; finite algebraic stationarity equations plus a collapse branch.

## G. STRUCTURAL_DEMAND

- Demand variables: membrane resultants and plate/stiffener bending resultants; the stiffener contributes area `As` and second moment `Is`.
- Critical locations are examined through whole-plate collapse, panel/local collapse, and stiffener-associated mechanisms (Fig. 6 and conclusions).
- Effective-width results are used for comparison, not as the primary structural demand operator.

## CAPACITY_LAYER

- Capacity is expressed through plastic collapse mechanisms and full plastic moment on fold lines; the plastic branch is combined with the large-deflection elastic branch.
- The capacity condition is mechanism work/energy equilibrium, not simply `sigma=f_y` at one point.
- Concrete/UHPC capacity: not applicable.

## CONTROL_LOCATION_SOURCE

`FINITE_BOUNDARY_CANDIDATES + ASSUMED` — whole plate, panel, and stiffener collapse mechanisms are selected analytically; the paper does not claim an FE-discovered unique location.

## ULTIMATE_SOLVER

`FINITE_ALGEBRAIC_ROOTS / DIRECT_DEMAND_CAPACITY_INTERSECTION` (the paper describes analytical solutions and intersection of the elastic/post-buckling and plastic branches). No Newton path, arc-length continuation, or material-history integration is required.

## EMPIRICISM_LOCATION

`MULTIPLE` but limited: assumed modal imperfection and mechanism geometry; effective-width concept is a comparison benchmark. No whole-panel empirical reduction is the primary closure.

## VERIFIED_CLASS

`CLASS_B_VERIFIED` for the mechanics sequence (large-deflection structural demand + plastic mechanism capacity + direct analytical closure), with the Airy status explicitly unresolved from the encoded PDF.

## NZ_SCCM_INTERFACE_COMPARISON

- KINEMATICS = `SAME_FAMILY`
- AIRY = `UNRESOLVED`
- POSTBUCKLING = `SAME_FAMILY`
- P_Q = `RELATED`
- N_M_DEMAND = `RELATED`
- CAPACITY = `RELATED`
- CONTROL_LOCATION = `RELATED`
- PU_CLOSURE = `RELATED`
- OVERLAP_LEVEL = `HIGH`

## LESSONS_FOR_NZ_SCCM

1. Mature step to adopt: Rayleigh–Ritz/Kármán large-deflection structural operator followed by a separate plastic-capacity operator.
2. Useful structure: keep geometry/imperfection parameters in the demand solution and keep collapse mechanisms in the capacity layer.
3. Closed form comes from a small modal basis and a finite catalogue of mechanisms.
4. Generality is lost when only a few sinusoidal modes and prescribed collapse patterns are retained.
5. Effective-width comparison is a warning: a mechanics solution can be benchmarked without absorbing the empirical reduction into the governing operator.
6. Incremental tracking is avoided because the paper solves algebraic stationarity and mechanism work equations rather than a material-history path.
7. The first complexity source is mode selection and stiffener coupling, not the material law.
8. Transfer to concrete/UHPC first fails at the plastic mechanism/section-capacity definition, because heterogeneous compression, cracking and tension need a multiaxial capacity surface.
9. NZ-SCCM can avoid this failure by retaining a replaceable section-capacity module.
10. NZ-SCCM should not add unnecessary incremental material tracking if the required output is a direct limit load and the capacity law is path-independent.

