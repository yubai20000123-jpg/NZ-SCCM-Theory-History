# Steel non-discretization / semi-analytical stability reference map

**Date:** 2026-08-10  
**Role:** EXTERNAL STRUCTURAL-METHOD REFERENCE ONLY  
**Current project authority:** does not override NC/UHPC material provenance, Case21 kinematics, or the zero-spatial-quadrature formal boundary.

## 0. Why this reference lane is retained

NZ-SCCM is pursuing a continuous-field / finite-generalized-coordinate route in which structural target functionals are obtained from analytic whole-domain contraction instead of a topological finite-element mesh and material-point grid.

There is a real steel-plate stability literature using Rayleigh–Ritz, Galerkin, Airy-stress and other semi-analytical/non-discretization formulations for buckling, postbuckling and ultimate-strength analysis. These works are useful precedents for the **structural reduction philosophy**, the variational construction of finite amplitude equations, equilibrium-path/stability interpretation and independent verification against nonlinear FEM.

They are **not** authority for ordinary-concrete or UHPC constitutive physics.

Formal project identity:

```text
REFERENCE_LANE_STEEL_NONDISCRETIZATION = RETAIN
ROLE = STRUCTURAL_METHOD_REFERENCE_ONLY
CURRENT_NC_MATERIAL_AUTHORITY = NONE
CURRENT_UHPC_MATERIAL_AUTHORITY = NONE
CURRENT_FORMAL_INTEGRATION_OVERRIDE = NONE
```

---

## 1. Smith, Bradford & Oehlers (2003)

**Title:** *Inelastic buckling of rectangular steel plates using a Rayleigh–Ritz method*  
**Journal:** International Journal of Structural Stability and Dynamics, 3(4), 503–521  
**DOI:** `10.1142/S0219455403001026`  
**Institutional record:** University of Adelaide digital repository.

### Methodological relevance

The institutional abstract explicitly describes the formulation as a **Rayleigh–Ritz based non-discretization method** for inelastic local buckling of rectangular steel plates under axial, bending and shear actions with various boundary conditions. Displacements are represented by a domain polynomial multiplied by a boundary polynomial.

This is direct precedent for the proposition that plate stability need not be formulated through topological FEM discretization.

### Important difference from NZ-SCCM

The paper's von-Mises/flow-law inelastic treatment is incremental and iterative. Therefore it supports the non-discretized structural-field philosophy, but **does not itself establish NZ-SCCM's stronger requirement of zero formal spatial quadrature plus a strong multiaxial concrete material operator contracted analytically to P/Rq/L**.

---

## 2. Brubak & Hellesland (2007)

**Title:** *Semi-analytical postbuckling and strength analysis of arbitrarily stiffened plates in local and global bending*  
**Journal:** Thin-Walled Structures 45(6), 620–633  
**DOI:** `10.1016/j.tws.2007.04.011`

### Methodological relevance

The paper combines large-deflection plate theory with an **incremental Rayleigh–Ritz approach**. It traces local and global equilibrium paths of imperfect stiffened plates and predicts ultimate strength using a membrane-stress von Mises criterion. Results are checked against nonlinear FEM.

Useful NZ-SCCM reference roles:

- finite generalized displacement amplitudes instead of a dense FE displacement field;
- equilibrium-path tracing through postbuckling;
- local/global modal interaction;
- variational/Ritz derivation as an independent check on residual/tangent equations;
- using nonlinear FEM as verification rather than as the definition of the theory.

### Limit

Its incremental solution and steel collapse criterion are not transferable as NC/UHPC material law.

---

## 3. Brubak, Andersen & Hellesland (2013)

**Title:** *Ultimate strength prediction by semi-analytical analysis of stiffened plates with various boundary conditions*  
**Journal:** Thin-Walled Structures 62, 28–36  
**DOI:** `10.1016/j.tws.2012.08.005`

### Methodological relevance

This work explicitly treats semi-analytical elastic plate methods as a computationally efficient route to ultimate-strength limits when combined with strength criteria. Large-deflection theory and incremental Rayleigh–Ritz are used to trace the equilibrium path and account for postbuckling reserve strength, with nonlinear FEA comparisons.

For NZ-SCCM it is especially useful as precedent for separating:

```text
continuous/semi-analytical structural response
+
explicit strength/limit-state condition
```

rather than requiring a conventional nonlinear FE collapse simulation as the only route to ultimate capacity.

### Limit

The strength criterion and incremental steel treatment are structural-method references only.

---

## 4. Ferreira & Virtuoso (2014)

**Title:** *Semi-analytical models for the post-buckling analysis and ultimate strength prediction of isotropic and orthotropic plates under uniaxial compression with the unloaded edges free from stresses*  
**Journal:** Thin-Walled Structures 82, 82–94  
**DOI:** `10.1016/j.tws.2014.04.003`

### Methodological relevance

The paper provides a particularly clear two-stage semi-analytical architecture:

1. an analytical Airy-stress-function solution satisfying the compatibility/Marguerre equation;
2. trigonometric series satisfying plate boundary conditions for out-of-plane displacement and imperfection;
3. unknown amplitudes obtained through a variational solution of equilibrium;
4. the resulting continuous response used for postbuckling analysis and ultimate-strength prediction.

This is conceptually close to NZ-SCCM's desired separation:

```text
finite admissible analytic field
-> generalized amplitudes
-> continuous-domain equilibrium functionals
-> stability / ultimate condition
```

It is useful both for the current plate backbone and for the later steel-shell/Y module.

### Limit

Its steel/isotropic-or-orthotropic plate constitutive and yield assumptions do not supply NC/UHPC material physics.

---

## 5. Koiter nonlinear stability theory

**Source:** *W. T. Koiter's Elastic Stability of Solids and Structures*, Cambridge University Press, 2008/2009 online edition.

### Methodological relevance

Koiter's framework is a general reference for nonlinear postbuckling, imperfection sensitivity and stability of continuous beams, plates and shells. For NZ-SCCM the relevant conceptual tools are:

- distinction between bifurcation and nonlinear postbuckling;
- finite generalized-coordinate/asymptotic reduction of a continuous stability problem;
- imperfection sensitivity;
- modal interaction;
- energy/tangent interpretation of stability conditions.

This is particularly useful for auditing whether `Rq=0` and the `P-Rq-L` limit/stability construction have the correct continuous-system interpretation when the material layer is changed.

### Limit

Koiter is a structural stability framework, not a concrete material source.

---

## 6. What NZ-SCCM may borrow later

The steel reference lane can legitimately inform:

1. boundary-condition-satisfying Ritz/Navier/Galerkin basis construction;
2. exact/variational construction of generalized residuals from a continuous plate field;
3. finite generalized amplitudes and basis-enrichment convergence studies;
4. equilibrium-path, bifurcation and limit-point classification;
5. imperfection-sensitivity and modal-interaction diagnostics;
6. independent energy/virtual-work checks of `P`, `Rq` and analytic tangent;
7. later steel-shell/Y-module local/global postbuckling architecture;
8. comparison against FEM as external verification rather than replacement of the analytic theory.

The relevant convergence concept for the current formal branch is **analytic basis enrichment**, not mesh refinement or growth in spatial integration points.

---

## 7. What must NOT be imported automatically

These references do not authorize:

```text
topological finite elements
spatial numerical quadrature
material-point incremental integration
mesh-convergence as formal integration theory
von-Mises cutoff as NC/UHPC material replacement
effective-width empirical rules as the current material operator
changing P/Rq/L only to imitate a steel formulation
```

If a specific steel method relies on numerical spatial integration internally, only its structural/variational idea may be retained unless its integrals can be rebuilt under the NZ-SCCM exact-analytic boundary.

---

## 8. Innovation implication

The existence of this literature means that the generic statement

```text
"we do not use FEM; we use a continuous assumed field and integrals"
```

is **not by itself a sufficient novelty claim**. Rayleigh–Ritz/Galerkin/semi-analytical/non-discretization approaches already provide clear antecedents in steel plate stability and strength.

The more defensible NZ-SCCM novelty target is the coupled architecture:

```text
strong multiaxial NC/UHPC material physics
+ source-shaped finite analytic material compiler
+ invariant/tensor reduction
+ exact whole-halfwave material/structural contraction
+ zero formal spatial quadrature/material points
+ analytic tangent
+ direct P-Rq-L ultimate-state system
+ later compatible steel-shell/Y coupling
```

Whether that full combination is publication-level novel must ultimately be established by a dedicated literature review; this note only records the presently identified methodological antecedents and the resulting claim boundary.

---

## 9. Source links / provenance

- University of Adelaide record, Smith/Bradford/Oehlers: `https://digital.library.adelaide.edu.au/items/339e6ab6-4bb6-46ca-90ab-36ba45d3c270`
- Smith/Bradford/Oehlers DOI: `https://doi.org/10.1142/S0219455403001026`
- Brubak & Hellesland 2007 DOI: `https://doi.org/10.1016/j.tws.2007.04.011`
- Brubak/Andersen/Hellesland 2013 DOI: `https://doi.org/10.1016/j.tws.2012.08.005`
- Ferreira & Virtuoso 2014 DOI: `https://doi.org/10.1016/j.tws.2014.04.003`
- Cambridge Koiter book record: `https://www.cambridge.org/core/books/w-t-koiters-elastic-stability-of-solids-and-structures/87DB64B6D82A4A3D6EC70E32DA2EF5E9`
