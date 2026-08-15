# Nguyen/FvK postbuckling source-chain reference note

**Timestamp:** 2026-08-15 21:18 +08:00

This note records the external/source basis used by the no-Pu membrane compatibility audit.

## Nguyen source chain

Nguyen Dai Minh (1996), *Buckling of reinforced concrete walls by the finite element method*, UNSW.

Relevant source locations:

- Ch.2: nonlinear theory of thin flat plates; equilibrium equations reduce under stated assumptions to von Karman/Timoshenko plate equations.
- Ch.6 Eq.(6.1): `w=w0+wm`.
- Ch.6 Eq.(6.3): strain field contains `wm^2` and `w0*wm` second-order terms.
- Ch.6 Eqs.(6.8),(6.9): independent in-plane and out-of-plane virtual-displacement equilibrium statements.
- Ch.6 Eqs.(6.27)-(6.36): layered nonlinear virtual-work/finite-element statement; Eq.(6.36) includes both nonlinear material properties and geometric effects.
- Immediately after Eq.(6.36): full nonlinear solution was not realized in the thesis because of time limitations; an approximate uncoupled tangent-modulus strategy was adopted for small imperfections/eccentricities.

## Classical/independent postbuckling corroboration

A. C. Walker (1969), *The Post-Buckling Behaviour of Simply-Supported Square Plates*, Aeronautical Quarterly 20(3), 203-222, DOI 10.1017/S0001925900005035.

Source-supported points used here:

- von Karman equations;
- trigonometric series + Galerkin solution;
- two distinct in-plane unloaded-edge conditions treated separately;
- initial geometric imperfection effect included;
- ultimate load/end-shortening/stiffness obtained from nonlinear postbuckling equations.

M. Stein (1959), NASA TR R-40, *Loads and Deformations of Buckled Rectangular Plates*.

Source-supported points used here:

- nonlinear von Karman large-deflection plate equations;
- simply supported rectangular plates under longitudinal compression;
- postbuckling loads/deformations solved by power-series reduction;
- experimental comparison includes shortening, strain, and deflection.

International Journal of Non-Linear Mechanics 179 (2025) 105210, *The interplay of pre-stress and higher-order basis functions in Galerkin-based postbuckling analysis of a von Karman plate*.

Used only as modern corroboration:

- transverse deflection can be accurately represented with low-order functions while in-plane stresses still require higher-order basis functions;
- this supports auditing in-plane stress/basis completeness before adding new out-of-plane harmonics.

## Source-boundary rule

The modern paper is not used to modify NZ-SCCM theory. The governing source identity remains Nguyen + frozen NZ-SCCM material/operator contracts. Classical FvK literature is used only as a mathematical completeness benchmark for the membrane-equilibrium space.
