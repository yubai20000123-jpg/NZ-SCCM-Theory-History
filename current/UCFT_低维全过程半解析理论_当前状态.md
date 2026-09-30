# UCFT 低维全过程半解析理论 — 当前状态（M8）

更新时间：2026-09-30 23:29 +08:00

## Stage
M0–M7 = PASS

M8_INPUT_FREEZE = PASS
M8_RATIONAL_Y_OPERATOR = PASS
M8_UHPC_UC141_FINAL_INP = PASS
M8_M5_STEEL_OPERATOR = PASS
M8_HUMAN_REPRO_FIXED_Q_BASE = PASS
M8_PERFECT_LOCAL_MODE_ID = NEEDS_IMPLEMENTATION_CORRECTION
M8_PATH_SOLVER = PARTIAL
M9 = NOT STARTED

## Instruction lock added
Current instruction now includes section 29.1:
- human reproducibility means no step may exist only as a program black box;
- given a q-state, a human must be able to reproduce strain evaluation, active-boundary roots, interval sorting, analytic integration, residual/Jacobian assembly, linear solve and Newton update;
- repeating those explicit steps must in principle reconstruct q->P(q);
- formal default unknowns remain current C1 only:
  Ex,Ey,Bx,By,Hx,Hy,P,A+,A-;
- M3 candidate harmonics are not instantiated by default;
- synthetic high-frequency harmonics used to validate integrators are not formal shape functions or unknowns.

## Final material lock
UHPC_UC141 final INP remains governing M8 source:
Ec=43400 MPa, nuc=0.30.
Compression peak 141.1 MPa at total compression strain about 0.0035.
Tension peak 7.3 MPa at total tension strain 0.0009722027649769585.
Damage/CDP tables remain FEM provenance and are not silently converted into hidden history variables.

Steel:
Es=206000 MPa, nus=0.30, fy=355 MPa,
M5 consistent secant-Mises deformation-theory EPP baseline.

## Latest actual fixed-q computation: BH005
Perfect-local auxiliary geometry:
A0+=A0-=0.

First nonzero continuation seed:
q=1.0e-5.

BH005:
b=250 mm, ah=500 mm, tc=42 mm, ts=4 mm, q0=0.0025.

At this q the complete final-INP/M5 active-set proof shows:
- UHPC all elastic;
- both steel skins all elastic.

Therefore the fixed-q C1 residual is exactly reducible to closed-form trigonometric integrals.

Starting from q=0 predictor:
Ex=Ey=Bx=By=Hx=Hy=P=0.

One Newton solve gives:
Ex = 4.26540289e-4
Ey = -1.421800965e-3
Bx = 4.63562982e-9
By = 1.85425193e-8
Hx = 0
Hy = 0
P = 1.233696696957e6 N = 1233.696696957 kN

post-update residual:
max absolute component = 1.16e-10 in the q residual.

Force shares:
Pc = 647.914699554 kN
Ps+ = Ps- = 292.890998701 kN

BH005 chi_w = 1.475275839368
P_report = 1541.634899626 kN.

Derived end shortening:
Delta = 0.710908208334 mm.
It emerges from the solved field; it was not used as a control variable.

## New exact mode-identification audit
Before evaluating the old perfect-local tangent scan, M6 RA residuals were analytically integrated at the same real BH005 base point.

At A0+=A0-=0 and A+=A-=0:

candidate N=m=1:
RA+ = -2561.158110982 N
RA- = +2644.857566627 N

candidate N=m=2:
RA+ = -1666.066308563 N
RA- = +1666.066308563 N

Thus A=0 is not generally an unconstrained local equilibrium for q>0.
The previous auxiliary rule
"A=0 base -> evaluate K_l,cond -> lambda_min=0"
cannot be interpreted as a strict local bifurcation criterion because the tangent was being evaluated at RA != 0.

This is an implementation-level mode-identification defect, not a failure of single-q/C1/M4/M5/M6.

## Locked minimal correction
For each candidate integer pair (N,m):
1. keep A0+=A0-=0;
2. start at q=0, A+=A-=0;
3. for q>0 solve the original M6 equilibrium including RA+=RA-=0, obtaining candidate-wise forced local responses A+(q;N,m), A-(q;N,m);
4. evaluate K_l,cond only on those true equilibrium points;
5. record the first candidate-wise tangent-loss event;
6. choose the earliest event among candidates, then restore the production A0=0.225b/1600 and run the imperfect connected path.

No material law, shape function, structural variable, or empirical coefficient is changed.

## Solver warning
The old M2 prototype remains prohibited as an M8 production solver.
No default high-frequency M3 variables are allowed.

## Unique NEXT_ACTION
Build the BH005 candidate-wise perfect-geometry forced-response evaluator with A0+=A0-=0.

For each (N,m) in the initial 1..12 search window, continue from q=0 and solve:
Ex,Ey,Bx,By,Hx,Hy,P,A+,A-,
with a complete human-reproducible Newton ledger.

Evaluate K_l,cond only after RA+=RA-=0 is satisfied.
Do not instantiate M3 candidate harmonics unless the real-path omitted residual is significant.
