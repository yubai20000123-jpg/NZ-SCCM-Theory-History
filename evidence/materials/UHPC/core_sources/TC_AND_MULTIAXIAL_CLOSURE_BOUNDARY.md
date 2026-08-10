# UHPC TC / multiaxial closure boundary

This file prevents an evidence-aggregation error: having Hiew + Liu + Lee + Leutbecher + triaxial strength sources does **not** automatically mean a complete UHPC production constitutive operator has been recovered.

## What is already source-closed or strongly constrained

Historical `D19_LIU_TC_CLOSURE_MATRIX.csv` records the Liu-2023 TC compression sub-branch as follows:

- ascending compressive uniaxial backbone: `CLOSED`;
- descending compressive backbone: `CLOSED`;
- peak compressive stress softening: `CLOSED`;
- peak compressive strain softening: `CLOSED`;
- softened compressive stress–strain relation: `CLOSED`;
- analytic `d sigma_c / d epsilon_c`: `CLOSED_DERIVED`;
- analytic coupling `d sigma_c / d epsilon_r`: `CLOSED_DERIVED`.

The four primary sources in this directory additionally constrain:

- monotonic direct-tension shape and fibre parameters (Hiew);
- planar CC/TT/TC strength and loading-path dependence (Liu 2024);
- TC compression-softening lower-bound/trend data (Lee);
- TC compressive-strength **and stiffness** reduction (Leutbecher).

## What remains OPEN if a full 2D/history-capable material law is claimed

The same historical closure audit explicitly leaves open:

- tensile-direction stress law inside a complete TC vector update;
- crack shear transfer `tau_12`;
- tensile unloading/reloading and crack closure;
- unique U -> TC entry continuity;
- arbitrary biaxial loading-path validity;
- complete TCX transition/history loop;
- complete full TC state loop.

The broader `UHPC_STATE_EQUATION_LEDGER.csv` also leaves general TT multidirectional coupling/shear/history incomplete and does not freeze a complete arbitrary-biaxial/3D CC/C3 stress–strain+tangent operator. Zhou-DP and Wang-Willam-Warnke evidence are retained as strength/failure qualifications rather than silently multiplied into a 2D current stress update.

## Consequence for NZ-SCCM

A project may deliberately define a reduced monotonic/current-state material operator for the present plate problem. If so, it must state the approximation explicitly and demonstrate material-level qualification against these sources. It must **not** claim that the original literature supplied a unique general memoryless `sigma = M(epsilon)` law.

Likewise, a future history-capable operator must introduce its state variables/update law transparently rather than hiding them inside a fitted structural surrogate.

## Structural calibration prohibition

Neither route may use Case21, Swartz24 or UCFT ultimate load to identify the missing material mechanisms or coefficients. Structural tests are reserved for downstream validation of the already-defined material/structural operator.

## Current status tag

`UHPC_EVIDENCE_SET = STRONG_FOR_UNIAXIAL_TENSION + PLANAR_STRENGTH + TC_STRENGTH_STIFFNESS`

`GENERAL_UHPC_2D_CONSTITUTIVE_OPERATOR = NOT_CLOSED_BY_SOURCES_ALONE`
