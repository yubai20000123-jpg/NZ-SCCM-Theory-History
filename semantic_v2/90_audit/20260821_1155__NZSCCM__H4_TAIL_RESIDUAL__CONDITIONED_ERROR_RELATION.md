# NZ-SCCM H4 tail residual → conditioned truncation-error relation

Timestamp: 2026-08-21 11:55 +08:00
Status: AUDIT RELATION, NOT YET A THEOREM
Material operator: NC-M6 FROZEN

## 1. Question

Can the newly opened H6 residual rows, evaluated at the converged H4 state, predict the H4→H6 truncation error without first solving the complete H6 system?

This study uses no experimental failure load. It is entirely an internal nested-space convergence audit of the unified H_{2N} system.

## 2. Tail residual definition

Let I_N denote the active Ritz multi-index set at spectral level N. For H4, N=2; for H6, N=3.

After solving H4, embed the state into H6 by preserving all I_2 coefficients and assigning zero to every coefficient in I_3 \ I_2. Let this embedded vector be x0.

Define

r_tail = [R_mu^(3)(D4,x0)] for mu in I_3 \ I_2.

At an exact H6 equilibrium every one of these rows would be zero. Therefore r_tail directly measures the unresolved Galerkin equilibrium forcing seen by the next spectral shell.

## 3. Raw tail norm is not sufficient

Across Swartz24, the raw norm ||r_tail||_2 has only moderate correlation with the actual membrane-field change and substantially different behavior for the global peak observables.

Observed correlations:

| quantity | Pearson with raw tail | Spearman with raw tail |
|---|---:|---:|
| delta_epsilon | 0.67946 | 0.63478 |
| delta_P | -0.79963 | -0.63304 |
| delta_D | -0.79474 | -0.68435 |
| delta_w | -0.0810 | -0.0539 |

The residual forcing cannot be interpreted independently of the local tangent/limit operator. A small residual in a soft direction may matter more than a larger residual in a stiff direction.

Therefore

RAW_TAIL_UNIVERSAL_ESTIMATOR = NO.

## 4. Conditioned equilibrium correction

At fixed H4 peak D, evaluate the complete H6 equilibrium residual and tangent at the embedded H4 state:

r0 = R^(3)(D4,x0),
Jx = partial R^(3)/partial x |_(D4,x0).

Use the Moore-Penrose/rank-aware solve consistently with the audit implementation:

Delta x_lin = -Jx^+ r0.

This is not a new physical solve, fitted correction, or material model. It is the first Newton correction that the H6 Galerkin system itself demands from the H4 embedded state.

The predicted membrane-field change is

hat(delta_epsilon) = || e_m(x0+Delta x_lin)-e_m(x0) ||_L2 / ||e_m(x0+Delta x_lin)||_L2.

## 5. Swartz24 validation

Against the actual completed H6 solution:

- Pearson(actual,predicted) = 0.9998626764
- Spearman(actual,predicted) = 0.9973913043
- actual/predicted ratio: 0.9924375 to 1.0162670
- median ratio = 1.0005664
- through-origin slope actual/predicted = 1.0006822
- ordinary regression in percentage units:
  actual = 0.9967963 predicted + 0.0075763
- RMSE = 0.011254 percentage points
- maximum absolute prediction error = 0.032184 percentage points

The pre-frozen 2% membrane-field pass/fail gate is classified correctly for 23 of the 24 panels. The sole baseline mismatch is Case 10, lying almost exactly on the gate.

This is strong numerical evidence for the first-order relation

Delta x = -J^{-1} r_tail + higher-order terms,

and therefore

Delta e_m = L_e J^{-1} r_tail + higher-order terms.

## 6. Why this does not yet eliminate the full H6/H8 comparison

The fixed-D correction omits movement of the ultimate point itself. At a peak/fold, D and the consistent limit condition form part of the nonlinear system. The equilibrium Jacobian alone is not the correct operator for the complete peak error.

The required next object is a bordered/augmented limit system

F_N(y) = [R_N(y); L_N(y)] = 0,

where L_N is the consistent limit condition and y contains D plus all equilibrium coordinates. Its linearization is

A_N = partial F_N / partial y.

The higher-order prediction should therefore take the form

Delta y_lim = - A_N^+ F_tail + higher-order terms.

Only after validating this relation against an independently solved higher order can it be promoted to a stopping diagnostic for delta_P, delta_D, delta_w and delta_epsilon simultaneously.

No rigorous global constant C has been established, so the inequality

||Delta y|| <= C ||A_N^{-1}|| ||F_tail||

is a research target, not a current theorem.

## 7. Coefficient-decay implication

The H6 harmonic ring does not decrease monotonically relative to H4 for all panels. The raw coefficient ring ratio c3/c2 ranges from about 0.3508 to 1.3717. The strain-weighted ring3/ring2 ratio reaches about 1.1863.

Hence coefficient decay alone cannot yet provide a universal N-dependent error law. In particular, neither

E_N = C N^{-p}

nor

E_N = C exp(-rho N)

is currently justified across the structural families.

## 8. Current mathematical status

RAW_TAIL_ONLY = INSUFFICIENT
TAIL_PLUS_LOCAL_TANGENT = STRONGLY_PREDICTIVE_FOR_MEMBRANE_FIELD
BORDERED_LIMIT_TAIL_ESTIMATOR = REQUIRED_NEXT
UNIVERSAL_COEFFICIENT_DECAY_LAW = NOT_ESTABLISHED
ELIMINATION_OF_N = NOT_YET_AUTHORIZED

The H6→H8 audit should retain the complete pre-frozen consecutive-order gate while also recording F_tail and the bordered prediction. If that predictor remains reliable, subsequent orders may be auditable without repeatedly solving every higher-order system.
