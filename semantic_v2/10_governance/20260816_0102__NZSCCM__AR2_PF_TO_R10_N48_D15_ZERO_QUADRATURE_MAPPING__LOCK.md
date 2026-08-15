# NZ-SCCM — AR2 PF boundary membrane -> R10/N48/D15 zero-quadrature mapping gate

**Timestamp:** 2026-08-16 01:02 +08:00

## Locked purpose

Execute the previously authorized gate

`AR2_PF_BOUNDARY_MEMBRANE_TO_R10_N48_D15_ZERO_QUADRATURE_MAPPING_GATE`

without computing a new Z6 Pu unless the complete nonlinear-material mapping passes.

## Hard invariants

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order kinematics
R10 / N48-C1-MM / Cayley-Hamilton unchanged
General D15 unchanged
A0=a/500
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
Gauss/Simpson/adaptive/collocation/cells/material-point-grid=PROHIBITED
no Zhou/Winter calibration
no out-of-plane multimode expansion
```

The historical Gauss AR2 `Pu=40.97334 MN` remains retracted and invalid.

## Mapping rule

The elastic PF/Airy stress field shall **not** be transplanted as a nonlinear R10 stress field.

The only admissible mapping is kinematic/variational:

1. construct boundary-admissible in-plane displacement/strain shapes;
2. keep their amplitudes as membrane generalized coordinates in the nonlinear problem;
3. calculate current stresses exclusively by `sigma=M(epsilon)` for each material phase;
4. determine membrane amplitudes from generalized virtual-work residuals;
5. prove the homogeneous elastic limit recovers the PF/FvK mixed-boundary solution.

## Direct-PF function-space caution

The PF modes contain non-integer complex-root factors `cos(lambda t)`, `t sin(lambda t)` and finite-panel hyperbolic factors. They are not finite members of the existing integer-trigonometric General-D15 algebra. Therefore a direct PF-function insertion into the current finite D15 coefficient arrays is forbidden.

The allowed bridge investigated in this gate is a **boundary-admissible integer-trigonometric Ritz lift**. Every finite lift remains exactly inside General D15; the formal complete Ritz space recovers the PF elastic solution by variational uniqueness.

## Release conditions

A new AR2 Pu remains blocked unless all of the following hold:

```text
KINEMATIC_NONLINEAR_MAPPING = PASS
ELASTIC_PF_LIMIT = PASS
FINITE_D15_MEMBRANE_BASIS = CERTIFIED
MULTICOORDINATE_R10_N48_D15_IMPLEMENTATION = PASS
FULL REQUIRED IN-PLANE BC = ADEQUATELY CLOSED
ZERO SPATIAL QUADRATURE = PASS
```

No finite membrane rank may be frozen merely because it gives a convenient Pu.