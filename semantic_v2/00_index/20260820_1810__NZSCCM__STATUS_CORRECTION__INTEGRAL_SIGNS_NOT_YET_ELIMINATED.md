# NZ-SCCM — Status correction: integral symbols are not yet eliminated

时间：2026-08-20 18:10 +08:00

状态：`CORRECTION / REPRESENTATION_PASS_BUT_EXPLICIT_EVALUATION_OPEN`

The previous node promoted the NC-M4 global R_m, P, R_A construction too early to `GLOBAL_*_ANALYTIC_CLOSURE = PASS`.

That statement is corrected here.

What has actually passed is:

- direct substitution of frozen NC-M4 into Nguyen second-order kinematics;
- exact elimination of the local principal direction into algebraic/rational data;
- exact rational-period / relative-GKZ representation of the complete-halfwave R_m, P, R_A targets;
- shared sparse master-support construction for the three targets;
- zero formal spatial quadrature and zero material-point grid.

What has NOT yet been completed in the user's required sense is removal of the remaining integral/contour symbols. Therefore the correct status is:

```text
GLOBAL_Rm_EXACT_REPRESENTATION = PASS
GLOBAL_P_EXACT_REPRESENTATION = PASS
GLOBAL_RA_EXACT_REPRESENTATION = PASS
GLOBAL_Rm_EXPLICIT_EVALUATION = OPEN
GLOBAL_P_EXPLICIT_EVALUATION = OPEN
GLOBAL_RA_EXPLICIT_EVALUATION = OPEN
```

The next task is exactly to evaluate the displayed rational-period integrals into finite explicit standard-function expressions with all coefficients, parameters and arguments enumerated, so that no anonymous integral signs remain in the final definitions of R_m(Delta,A,epsilon_m), P(Delta,A,epsilon_m), and R_A(Delta,A,epsilon_m).

Only after that step should same-source derivatives and the final limit determinant be formed.
