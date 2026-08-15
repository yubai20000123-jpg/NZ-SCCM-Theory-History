# NZ-SCCM — AR2 PF -> D15 current-material mapping audit

**Timestamp:** 2026-08-16 01:02 +08:00

## Audit question

Can the 00:47 elastic PF/FvK end-restraint closure be admitted into the nonlinear R10/N48/D15 production chain without spatial quadrature and without treating elastic Airy stress as nonlinear stress?

## Findings

### A. Direct PF function insertion

**FAIL.** The PF functions use complex non-integer strip eigenvalues and hyperbolic finite-length factors. They are not finite integer-trigonometric polynomials, while the current finite General-D15 compilation is built from finite trig-polynomial coefficient algebra. Direct insertion would require a different function algebra.

### B. Conforming displacement lift

**PASS FORMAL.** A one-halfwave integer-trigonometric displacement family was constructed with the actual transverse loaded-end essential condition built in. Every finite level is General-D15 compatible. The complete space is conforming for the symmetric transverse-restraint subproblem and therefore converges to the PF/Airy elastic solution by variational uniqueness.

### C. Current-material consistency

**PASS ARCHITECTURE.** The new membrane amplitudes enter strain, not stress. Concrete/steel stresses remain `M(epsilon)`. In nonlinear response the elastic condensed coefficients are not frozen; amplitudes must satisfy their own generalized virtual-work residuals.

### D. Zero spatial integration

**PASS.** The elastic mapping calculation uses exact Fourier coefficient products and analytic exponential antiderivatives only.

```text
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
```

### E. Prebuckling boundary effect

**PASS AS MAPPING CONTENT.** The same membrane basis responds to D and to the nonlinear geometric driver. The q=0 free-Poisson mismatch is therefore not left outside the new formulation.

### F. Positive membrane sign

**PASS.** `Q_GG` remains positive for all tested exact coefficient-space truncations R=S=1...12. No repeat of the retired p20/p02 artificial softening occurs in the elastic gate.

### G. Production implementation

**OPEN.** Existing R10/N48 code is specialized to the historical low-rank strain algebra. A generic vector membrane-coordinate coefficient compiler/residual/Jacobian implementation does not yet exist.

### H. Finite membrane rank

**OPEN.** The exact PF solution corresponds to the complete Ritz limit. The R=S sequence is convergent but the production order is not frozen. R/S are coefficient-space basis orders, not spatial cells or integration points.

### I. Zhou bottom uy / top uy asymmetry

**OPEN AND PRIORITY.** The source boundary has `bottom uy=0`, `top uy=unset`. The current one-halfwave transverse-restraint lift uses a symmetric axial correction for the ux-end-restraint subproblem. It has not proven that the asymmetric axial-end condition is merely a rigid-reference choice. Therefore full Zhou all-in-plane-DOF equivalence cannot yet be claimed.

## Gate verdict

```text
AR2_PF_TO_NONLINEAR_KINEMATIC_MAPPING = PASS_ARCHITECTURE
DIRECT_PF_HYPERBOLIC_TO_FINITE_D15 = FAIL_FUNCTION_SPACE
BOUNDARY_ADMISSIBLE_INTEGER_TRIG_D15_LIFT = PASS
ELASTIC_PF_LIMIT = PASS_FORMAL_COMPLETE_BASIS
ZERO_SPATIAL_INTEGRATION = PASS
MULTICOORDINATE_R10_N48_IMPLEMENTATION = OPEN
PRODUCTION_MEMBRANE_RANK = OPEN
FULL_ZHOU_ALL_INPLANE_END_DOF_EQUIVALENCE = OPEN
NEW_AR2_Pu = BLOCKED
```

## Required next gate

`ZHOU_BOTTOM_UY0_TOP_UYFREE_ONE_HALFWAVE_COMPATIBILITY_ZERO_QUADRATURE_GATE`

Reason for priority: if the bottom/top axial displacement asymmetry destroys the current half-panel symmetry reduction, the multi-coordinate nonlinear compiler basis must be changed before implementation. This boundary question therefore precedes compiler productionization.