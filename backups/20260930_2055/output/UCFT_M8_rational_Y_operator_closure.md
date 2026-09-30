# UCFT M8 — finite-trigonometric/rational-Y production operator closure

Timestamp: 2026-09-30 20:55 +08:00

## Recovered entry state
- M0–M7: PASS.
- M8_INPUT_FREEZE: PASS.
- M8_PATH_SOLVER: PARTIAL.
- Recovered sole blocker: M4 baseline analytic-Y active-set was limited to e(Y)=A+B cos(2Y)+C sin(Y) and could not directly accept M3 C/S/B compatible high harmonics.

## This execution
Implemented a production fixed-X Y operator that preserves the theory contract:
- material boundary location: exact finite-trigonometric algebra using t=tan(Y/2);
- UHPC thickness: analytic cumulative primitives;
- active intervals: exact root partition;
- Y integration: analytic/rational elementary primitives;
- no Y Gauss material points;
- only the outer X deterministic integral remains.

To avoid catastrophic coefficient cancellation of one giant high-degree P(t)/Q(t), the integrand is retained as a finite complex Fourier series. Division by sin(Y) and sin^2(Y) is integrated with closed elementary primitives that are algebraic reductions of the same tan-half rational integral.

## Validation 1 — baseline C1 degeneration
Compared against the original M4 analytic-Y kernel over three states, X={0.31,0.87,1.43}, both x/y directions, including states with 1–15 material active intervals.

Worst scaled relative difference:
3.5100223534585275e-10.

Hence baseline C1 -> original M4 analytic-Y kernel passes.

## Validation 2 — C/S/B high harmonics
Synthetic finite harmonics up to k=16, 21–29 material intervals, weights 1, cos(7Y), sin(9Y).

Against independent direct-Y diagnostic quadrature:
- N moment relative errors: typically 1e-15–1e-13;
- M moment relative errors: typically 1e-11–1e-9;
- worst scaled relative difference: 4.120394325741984e-09.
The independent reference itself emitted roundoff/extrapolation warnings; the production operator performs no Y quadrature.

## Validation 3 — frozen 7.2 MPa production UHPC law
Added a general piecewise UHPC law adapter for:
- compression: locked sixth-order polynomial, with exact negative terminal root;
- tension: elastic -> plateau -> three frozen cubic segments -> zero terminal branch.

Exact interface polynomial-value jumps are <=4.55e-12 MPa (compression terminal <=3.07e-12 MPa).
Production-law high-harmonic rational-Y validation:
- 25–27 active intervals;
- worst scaled relative difference against independent diagnostic quadrature:
  4.76117956931638e-09.

## Verdict
M8 finite-trigonometric UHPC active interval analytic/rational-Y operator: PASS.

This removes the recovered M4/M3 implementation-interface blocker without:
- adding global q modes;
- adding structural DOFs;
- changing M6 residuals;
- changing M3 compatible enrichment;
- fitting FEM/test Pu;
- introducing 2D/3D Gauss material-point production definitions.

M8 whole nine-specimen connected paths are NOT yet claimed as completed in this checkpoint.

## Next action
Execute BH005 exactly as specified:
1. perfect-local A0+=A0-=0;
2. identify (N,m) using first zero of the exact inner-condensed local tangent over the connected C1 base q-branch, expanding the integer search window if required;
3. restore A0=0.225 b/1600;
4. solve the imperfect connected q-path and record the full M8 ledger.
