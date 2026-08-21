# NZ-SCCM H4→H6 result ledger and H4 production rejection

Timestamp: 2026-08-21 11:55 +08:00
Status: DECISIVE NO-EXPERIMENT CONVERGENCE AUDIT
Pre-frozen gate source: `20260821_1049__NZSCCM__H4_TO_H6__PREFROZEN_NO_EXPERIMENT_GATE.md`
Material operator: NC-M6 FROZEN

## 1. Governance boundary

This audit evaluates the H4 (N=2) candidate against the nested H6 (N=3) admissible Ritz/Fourier subspace. The H6 results were not available when the acceptance gate was frozen.

Frozen acceptance thresholds:

- delta_P <= 0.5%
- delta_D <= 0.5%
- delta_w <= 1.0%
- delta_epsilon <= 2.0%
- same origin-connected equilibrium branch
- audit-localizer independence required for a numerically marginal rejection

Experimental failure loads were not used for order selection, root selection, continuation, tolerance definition, or acceptance.

Formal identities remain unchanged:

- ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
- NC_M6 = FROZEN
- M7 = PROHIBITED
- N_formal_spatial_sampling = 0
- N_formal_spatial_quadrature = 0
- N_formal_spatial_subdomains = 1
- material_points = 0

The direct-current Gauss evaluations used below are AUDIT-ONLY continuum decimal localizers. They do not enter the formal operator.

## 2. Swartz24 full H4→H6 audit

At the common 28x28 in-plane by 14 thickness audit localizer:

- H4 PASS = 14/24
- H4 FAIL = 10/24
- FAIL cases = 2, 3, 4, 5, 7, 9, 10, 12, 13, 16
- every failure is caused by delta_epsilon > 2.0%

Max differences over all 24 panels:

- max delta_P = 0.022766%
- max delta_D = 0.154236%
- max delta_w = 0.171361%
- max delta_epsilon = 2.571331%

Group field convergence:

- Cases 1–8: 3/8 PASS; mean delta_epsilon = 2.12894%; max = 2.52026%
- Cases 9–16: 3/8 PASS; mean delta_epsilon = 2.14589%; max = 2.57133%
- Cases 17–24: 8/8 PASS; mean delta_epsilon = 0.74839%; max = 0.76967%

Thus the global resultant Pu has essentially converged before the nonlinear membrane redistribution field has converged. The H2→H4 observation therefore persists one spectral level higher.

## 3. High-resolution audit-localizer check for decisive failures

The following panels were recomputed at 40x40 in-plane by 20 thickness audit resolution.

| Case | delta_P | delta_D | delta_w | delta_epsilon | Decision |
|---|---:|---:|---:|---:|---|
| 4 | 0.006508% | 0.005248% | 0.069205% | 2.399036% | FAIL |
| 7 | 0.004110% | 0.034756% | 0.094685% | 2.003846% | FAIL, marginal |
| 10 | 0.019956% | 0.116241% | 0.054810% | 2.016404% | FAIL, marginal |
| 16 | 0.001189% | 0.042995% | 0.094069% | 2.359592% | FAIL |

Cases 4 and 16 remain comfortably above the 2% field gate at the refined localizer. Therefore H4 rejection is decisive and does not depend on borderline decimal localization in Cases 7 or 10.

## 4. H4 tail residual in the newly opened H6 modes

At each H4 peak, the H4 coefficients were embedded in H6 and every H6-only coefficient was set to zero. Define

r_tail^(3) = R^(3)(D4, x_H4 embedded in H6) restricted to I3 \ I2.

The raw L2 norm of this tail residual is not a universal truncation-error measure across the full structural population.

For Swartz24, raw ||r_tail||_2 correlations were approximately:

- with delta_epsilon: Pearson 0.67946; Spearman 0.63478
- with delta_P: Pearson -0.79963; Spearman -0.63304
- with delta_D: Pearson -0.79474; Spearman -0.68435
- with delta_w: Pearson -0.0810; Spearman -0.0539

The sign and magnitude changes arise because the same residual forcing is filtered by a specimen-dependent tangent/limit operator. Therefore `RAW_TAIL_UNIVERSAL_ESTIMATOR = NO`.

## 5. Condition-aware first-order tail correction

At fixed D4 in the H6 space, let

r0 = R^(3)(D4,x0),
Jx = partial R^(3)/partial x evaluated at (D4,x0),

where x0 is the embedded H4 state. The one-step correction is

Delta x_lin = - Jx^+ r0.

The membrane field reconstructed from x0 + Delta x_lin gives a prediction \hat{delta_epsilon} without solving the complete H6 equilibrium problem.

Across Swartz24:

- Pearson(actual delta_epsilon, predicted delta_epsilon) = 0.9998626764
- Spearman = 0.9973913043
- actual/predicted ratio range = 0.9924375 to 1.0162670
- median actual/predicted ratio = 1.0005664
- through-origin slope actual = 1.0006822 x predicted
- unconstrained fit in percentage units: actual = 0.9967963 predicted + 0.0075763
- RMSE = 0.011254 percentage points
- maximum absolute prediction error = 0.032184 percentage points
- pass/fail classification by the 2% field gate = 23/24 correct at baseline resolution

The only baseline misclassification is Case 10: predicted 1.97847% versus actual 2.01065%. At the refined localizer it becomes predicted 1.99129% versus actual 2.01640%.

This strongly validates the leading-order causal relation

Delta x approximately = -J^{-1} r_tail,

delta_epsilon approximately = L_epsilon J^{-1} r_tail

for the field truncation error. It is an audit result, not yet a rigorous theorem or certified error bound.

## 6. Why the fixed-D predictor is not yet a complete production stopping rule

The fixed-D predictor is excellent for the membrane-field change, but it does not yet predict all limit-point observables sufficiently well. In particular, its correlation with delta_P is only moderate (Pearson about 0.776, Spearman about 0.793).

At an ultimate point the correct a-posteriori operator is the bordered/augmented limit system A_N, not the fixed-D equilibrium Jacobian alone. The next mathematical target is therefore

Delta y_lim approximately = - A_N^{-1} F_tail,

where y contains the physical equilibrium variables, D, and the consistent limit condition.

No universal inequality of the form E_N <= C ||A_N^{-1}|| ||R_tail|| is claimed at this stage.

## 7. Coefficient-decay diagnosis

At the H6 peak, Ritz coefficients were grouped by harmonic ring r=max(m,n). The H6 ring is not uniformly smaller than the H4 ring across the 24 panels.

For raw coefficient L2 ring norms:

- median c2/c1 approximately 0.14595
- median c3/c2 approximately 0.78143
- c3/c2 range approximately 0.35081 to 1.37167

For strain-weighted ring norms:

- median ring2/ring1 approximately 0.16924
- median ring3/ring2 approximately 0.59574
- ring3/ring2 range approximately 0.34064 to 1.18631

Several Cases 1–5, 12, and related panels have an H6 ring contribution comparable to or larger than the H4 ring contribution. Hence no universal monotone power-law or exponential coefficient decay has been established at N=3.

Consequently:

- `UNIVERSAL_E_N_EQUALS_F_N = NOT ESTABLISHED`
- `ELIMINATE_N_BY_COEFFICIENT_DECAY = NOT AUTHORIZED`

## 8. Z0 cross-family check

The Z0 steel-shell/concrete system was also evaluated on the same nested H4→H6 formulation. Because the enlarged system exposes a D-fold, the H6 solution was projected and traced on the same origin-connected continuation manifold rather than selected by a disconnected root.

At the 28x28x14 audit localizer:

H4 peak approximately:

- D4 = 0.95753410
- q4 = 0.005622414
- P4 = 31.65466 MN

H6 peak approximately:

- D6 = 0.95771298
- q6 = 0.006094117
- eta6 = 0.17212008
- P6 = 31.60031 MN

Consecutive-order differences:

- delta_P = 0.17199%
- delta_D = 0.01868%
- delta_w = 4.67305%
- delta_epsilon = 7.41529%
- ||r_tail||_2 = 0.029586

Thus Z0 is a strong H4 failure in the deformation amplitude and membrane field. Its absolute Pu decimal is audit-grid sensitive at this resolution and is not promoted as a final value. H4 rejection does not rely on this Z0 result because the independently refined Swartz Cases 4 and 16 are already decisive.

Z1–Z5 were not run after global H4 rejection became logically irreversible. Continuing them cannot reverse the pre-frozen production decision and is deferred unless a complete failure-map characterization is explicitly requested.

## 9. Decision

H4_PRODUCTION_FREEZE = NO
H4_REJECTION = DETERMINED
H6 = NEXT_MINIMUM_CANDIDATE
H6_PRODUCTION_FREEZE = NOT_AUTHORIZED
NC_M6 = FROZEN
M7 = PROHIBITED
EXPERIMENT_USED_FOR_ORDER = NO
RAW_TAIL_UNIVERSAL_ESTIMATOR = NO
TAIL_PLUS_FIXED_D_TANGENT_FIELD_PREDICTOR = STRONGLY_VALIDATED_ON_SWARTZ24_AUDIT
LIMIT_POINT_BORDERED_ESTIMATOR = OPEN
FORMAL_SPATIAL_QUADRATURE = 0
AUDIT_QUADRATURE = AUDIT_ONLY

The next spectral-order gate must be H6→H8 and must be frozen before any H8 result is inspected. H6 cannot be called production before that audit closes.
