# UCFT 低维全过程半解析理论 — 当前状态（M8）

更新时间：2026-09-30 22:35 +08:00

## Stage
M0–M7 = PASS

M8_INPUT_FREEZE = PASS
M8_RATIONAL_Y_OPERATOR = PASS
M8_UHPC_UC141_FINAL_INP = PASS
M8_M5_STEEL_OPERATOR = PASS
M8_PATH_SOLVER = PARTIAL
M9 = NOT STARTED

## Final-INP UHPC lock
Material: UHPC_UC141.
E=43400 MPa, nu=0.30, density=2.5e-09 tonne/mm3.
CDP constants are retained as FEM provenance.
Compression/tension hardening/stiffening tables supplied from the final submitted INP are now the material source for the M8 low-dimensional monotonic backbone.

Abaqus inelastic/cracking strains are converted to total strain by sigma/E before use in the low-dimensional stress-strain operator.

Compression peak:
141.1 MPa at total strain 0.003500000073732719 in compression.

Tension peak:
7.3 MPa at total strain 0.0009722027649769585 in tension.
The INP value 0.000804 is cracking strain, not total strain.

Damage tables are not silently promoted to a history-damage law.

## Latest actual computation
The existing finite-trigonometric/rational-Y active-set operator was re-run with the final-INP piecewise-linear total-strain backbone.

Regression against independent diagnostic integration:
- baseline: max rel diff 4.3564168e-09
- high harmonic k=7,9,16: 1.9992804e-09
- mixed: 6.4278613e-10

=> actual-INP rational-Y operator PASS.

M5 Q355 ideal elastic-perfectly plastic secant-Mises kernel also rechecked:
exact thickness resultant errors <=4.19e-14 in the tested states;
consistent tangent FD relative errors <=1.42e-10.

## Solver warning
The old M2 prototype `current/code/UCFT_nonlinear_membrane_condensation_solver.py` is not an M8 production solver because it belongs to the earlier baseline implementation and must not be allowed to reintroduce old material constants such as nu_c=0.20 or the former tensile surrogate.

## Unique NEXT_ACTION
Build the full fixed-q M8 evaluator returning:
G, Rq, RA+, RA-, full/condensed Jacobian, material active-set ledger, P/Pc/Ps+/Ps-, A+/A-, derived Delta.

Then execute BH005:
A0=0 perfect-local mode identification N,m
-> restore A0 coefficient 0.225b/1600
-> connected imperfect q-path.

No new theory gate. No FEM/test Pu fitting.
