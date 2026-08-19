# NZ-SCCM — Direct R10/R13 complete-ledger resume point

**Date:** 2026-08-19 21:42 +08  
**Identity:** CHAT-LENGTH SAFETY CHECKPOINT / ACTIVE EXECUTION CONTRACT

## 1. User directive being resumed

The active instruction is to continue execution, not stop at another gate or half-product. The calculation must continue until there is a fully implementable calculation ledger. The mathematical/physical intent that led here must be preserved in GitHub so that another chat can resume without reconstructing the rationale.

## 2. Material identity lock

R10/R13 is a specimen-independent current material system once its material parameters are supplied. Geometry, specimen identity, Case21/Swartz24 membership, or later benchmark coverage must not modify the R10/R13 physical material operator.

Formal pointwise chain:

```text
continuous structural kinematics
-> current strain tensor epsilon(x,y,z)
-> fixed R10/R13 current material operator
-> current stress sigma(x,y,z)
-> continuous virtual-work/generalized-force integrands
-> continuous analytic integration
-> P, Rq, Ralpha and same-source derivatives
-> Rq=0, Ralpha=0, det(Jlim)=0
-> Du, qu, alphau, Pu
```

## 3. Two-level integration strategy

### Route A — preferred, material unchanged

Increase/reorganize integral multiplicity only as an analytic change of variables / state-space reduction. Use the material state plane (principal-state CC/TC/TT or invariants J1=tr(E), J2=det(E)) to separate structural state occupancy from the fixed R10/R13 material surface. This is not material-coordinate sampling and not spatial discretization.

### Route B — fallback if Route A cannot be made Excel-evaluable

Do not fit a specimen-specific 2D material surface. Simplify only the source one-dimensional scalar material curves, retain the R10 multiaxial CC/TC/TT assembly, and make the simplification intentionally conservative and Excel-evaluable. The original R10/R13 remains the material audit reference. Conservatism must be checked at stress/tangent/work level over the used material states and then at Pu level.

## 4. Production prohibitions

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_material_points = 0
spatial Gauss/Simpson/adaptive quadrature = prohibited
spatial cells/material-point grid = prohibited
material-coordinate N48/N96 sampling = prohibited
specimen-specific material fitting = prohibited
trial/experimental Pu used for solve/root choice = prohibited
```

## 5. Structural requirement

The structural side may be expanded to represent membrane-stress redistribution and directional stiffness matching, but such changes belong to kinematics/equilibrium/tangent structure. They must not be implemented by modifying R10/R13 material physics.

The current R15 three-variable `(D,q,alpha)` formulation remains the immediately executable baseline unless a later explicit structural extension supersedes it.

## 6. Deliverable required before stopping

A visible Excel calculation ledger in which raw geometry/material/reinforcement inputs drive the formulas through the material law, continuous analytic integration or documented conservative scalar-law fallback, generalized residuals, same-source Jacobian and final limit solution. Solver, if used, is only for the final finite-dimensional structural unknowns.

Existing `NZ_SCCM_Case21_显式人工Excel完整极限承载力计算_v1.0_20260819.xlsx` is retained as audit evidence but is not the final target because its degree-12 invariant material compiler is an approximation layer that the current direct-R10/R13 route is explicitly trying to avoid.

## 7. Resume rule

Do not resume by debugging R17/R18 exact-evaluator timeouts, rebuilding N48, or creating a new specimen-specific compiler. Resume by implementing Route A and, if it cannot become Excel-evaluable within the production ledger, immediately execute Route B rather than stopping at a gate.
