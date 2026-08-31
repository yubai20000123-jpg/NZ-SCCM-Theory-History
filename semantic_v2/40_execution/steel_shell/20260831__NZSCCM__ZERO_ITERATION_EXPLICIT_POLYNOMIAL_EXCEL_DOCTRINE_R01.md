# NZ-SCCM — Zero-Iteration Explicit-Polynomial Excel Doctrine R01

**Date:** 2026-08-31  
**Branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Production main:** unchanged  
**Role:** implementation-governance / diagnostic freeze; not a new physical terminal rule.

## 1. User instruction now frozen for this branch

Formal calculation must not use Newton iteration, Goal Seek, Solver path iteration, load-step continuation, eta scanning, or repeated unknown correction as the primary theory/solver identity.

Even when an explicit polynomial expansion is algebraically larger than an iterative update, the preferred formal route is:

```text
explicit finite equation
-> explicit polynomial coefficients / analytic primitives
-> complete algebraic root set
-> admissibility / active-set / energy / first-event selection
-> result
```

The reason is transferability and auditability: a larger finite polynomial ledger is preferable to a shorter but path-dependent iterative history.

## 2. Consequences for current steel-shell/UHPC chain

### R02 local amplitude U

R02 energy is quartic in U and dPi/dU is cubic. Therefore U must be obtained by explicit enumeration of the cubic real-root set plus the boundary candidate U=0. The authoritative selection remains:

- U >= 0;
- evaluate Pi for every admissible candidate;
- choose the global minimum-energy candidate;
- never impose U>=A0;
- never choose the largest or comparator-nearest root.

For the BH050 source-audited terminal:

- upper cubic gives `U+=0.169266885792264 mm` by Cardano closed form;
- lower projected cubic gives three real roots and the only admissible positive minimum-energy root `U-=2.93984591447788 mm`.

No Newton iteration is needed or allowed in the formal workbook.

### R06 local Mises maximum

The exact finite polynomial field remains the theory. On each of the four edges, Phi reduces to a one-variable quartic and edge stationarity is cubic, so all edge candidates are explicitly enumerable. Corners are direct candidates.

Interior stationary points must be obtained by algebraic elimination:

`Fu=dPhi/du=0`, `Fv=dPhi/dv=0` -> resultant polynomial `R_u(u)=Res_v(Fu,Fv)` or equivalent `R_v(v)`.

All algebraic roots are then back-substituted and filtered to the physical square. No spatial sampling is introduced.

For the frozen BH050 lower projected state, the governing candidate remains the v=-1 edge stationary root `u=0.757308975358...`, giving `Phi=126025 MPa^2` and `sigma_VM=355 MPa`.

### R06 first local-yield eta

Eta scanning/iteration is removed from the formal identity. The preferred compilation is:

`F(U,eta)=dPi/dU=0`

and the active local-yield candidate equation

`G(U,eta)=Phi_candidate(U,eta)-fy^2=0`.

Eliminate U:

`R_eta(eta)=Res_U(F,G)=0`.

Enumerate the finite eta-root set, retain `0<eta<=1`, rebuild the R02 active set at each algebraic candidate, certify the local maximum, and select the first physical local-yield root.

## 3. Excel boundary

Excel is the ledger/calculation surface, not a license to introduce iterative methods.

Native Excel formulas can directly evaluate:

- integer mode enumeration;
- Airy P(q), N, M;
- cubic Cardano/trigonometric roots;
- quartic energy values;
- edge quartic/cubic Mises candidates;
- admissibility and finite candidate comparison.

For general resultants of degree >4, native Excel has no universal radicals formula. The formal object remains a finite polynomial / RootOf set. A symbolic/algebraic backend may compile the concrete roots/factors once into the workbook; this is not a load-step/Newton iteration and must not change root-selection rules.

## 4. Important current terminal boundary

The historical R4 five-equation capacity-contact system contains the current UHPC source operator with noninteger powers/hypergeometric primitives. Therefore it is not presently a pure polynomial system.

Under the zero-iteration doctrine, Excel Solver is no longer accepted as the formal way to close this terminal system. A future implementation must either:

1. derive an explicit analytic elimination for the frozen current operator; or
2. compile an equivalent finite algebraic representation without changing the material source contract.

Until then the historical R4 terminal root remains a reproducible regression checkpoint, not a newly re-solved zero-iteration terminal.

The same-q deformation-compatible structural terminal remains research-open and is not created by this implementation rule.

## 5. Status

```text
FORMAL_NEWTON = PROHIBITED
FORMAL_GOAL_SEEK = PROHIBITED
FORMAL_EXCEL_SOLVER = PROHIBITED
FORMAL_LOAD_STEP_CONTINUATION = PROHIBITED
FORMAL_ETA_SCAN = PROHIBITED
R02_EXPLICIT_CUBIC_ROOT_SET = REQUIRED
R06_EDGE_EXPLICIT_POLYNOMIALS = REQUIRED
R06_INTERIOR_RESULTANT = REQUIRED
R06_ETA_RESULTANT = REQUIRED
HIGH_DEGREE_ROOT_IDENTITY = FINITE_ROOTOF_SET
PHYSICAL_TERMINAL_RULE = STILL_NOT_FROZEN
PRODUCTION_MAIN = UNCHANGED
```
