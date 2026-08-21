# NZ-SCCM H6→H8 pre-frozen no-experiment convergence gate

Timestamp: 2026-08-21 11:55 +08:00
Status: PRE-FROZEN BEFORE ANY H8 RESULT
Material operator: NC-M6 FROZEN
Current candidate: H6 (N=3)
Next audit space: H8 (N=4)

## 1. Purpose

H4 has failed the previously pre-frozen H4→H6 gate. This document freezes the next consecutive-order acceptance gate before any H8 result is inspected.

The sole order-selection question is whether H6 is sufficient as the production membrane subspace. Experimental ultimate loads remain prohibited from order selection, mode selection, root selection, tolerance adjustment, or acceptance.

## 2. Nested-space identity

Use the same H_{2N} mother formulation and the same admissible even-harmonic multi-index family.

- H6: N=3
- H8: N=4
- I_3 subset I_4

No new material parameter, restraint factor, fitted harmonic coefficient, empirical weighting, or out-of-plane mode is introduced by this audit.

## 3. Frozen physical and formal identities

The following may not change during H6→H8:

- NC-M6 current material operator
- ONE_CONTINUOUS_COMPLETE_HALFWAVE
- Nguyen second-order/von-Karman kinematics
- frozen out-of-plane representative halfwave
- phase/section definitions
- source-consistent material tangent
- family-specific essential in-plane boundary conditions
- origin-connected equilibrium branch
- exact formal moment/zero-formal-spatial-quadrature identity
- formal spatial sampling = 0
- formal spatial quadrature = 0
- formal spatial subdomains = 1
- M7 prohibited

Audit-only direct-current continuum quadrature may be used solely to localize decimals and verify that a marginal gate decision is not a quadrature artifact.

## 4. H6→H8 pre-frozen acceptance gate

H6 is accepted only if H6 and H8 agree on the same origin-connected branch within ALL of the following unchanged tolerances:

1. delta_P(H6,H8) <= 0.5%
2. delta_D(H6,H8) <= 0.5%
3. delta_w(H6,H8) <= 1.0%
4. delta_epsilon(H6,H8) <= 2.0%
5. no branch jump, disconnected root switch, or different fold branch
6. for a numerically marginal rejection, refinement of the audit localizer changes Pu by less than 0.05%

The membrane-field metric remains

Delta_epsilon = ||e_m^(H8)-e_m^(H6)||_L2 / max(||e_m^(H8)||_L2,epsilon_floor),

e_m = [e_x,e_y,gamma]^T,

over the same complete continuous representative halfwave.

## 5. New diagnostic recorded in parallel, but NOT a replacement for this gate

Because H4→H6 established that raw tail norm alone is not a universal error estimator, H6→H8 shall additionally record the unresolved H8 shell residual

r_tail^(4) = R^(4)(y_H6 embedded in H8) restricted to I_4 \ I_3.

It shall also evaluate a condition-aware prediction.

For ordinary equilibrium diagnostics:

Delta x_lin = -J_x^+ r0.

For the ultimate-point diagnostic, the preferred object is the bordered/augmented limit operator

A_6 = partial [R_6; L_6] / partial y,

with a corresponding higher-order forcing F_tail. The research predictor is

Delta y_lim,pred = -A_6^+ F_tail.

These predictions are diagnostic only during H6→H8. They may not replace the actual H8 solve for this validation pair and may not alter the pre-frozen tolerances after the results are known.

## 6. Coefficient-decay record

For both H6 and H8, record harmonic-ring norms by r=max(m,n), including raw coefficient and strain-weighted norms. No power-law or exponential tail law is assumed in advance.

A relation E_N=F(N), or elimination of N, may be proposed only after the observed H6→H8 behavior supports it together with the conditioned residual analysis.

## 7. Decision logic

If every required sample/family passes all frozen consecutive-order criteria:

H6_PRODUCTION_FREEZE = YES
STOP_SPECTRAL_ENRICHMENT = YES
H8 = AUDIT_REFERENCE_ONLY

If any decisive sample fails after audit-localizer independence is established:

H6_PRODUCTION_FREEZE = NO
H8 = NEXT_MINIMUM_CANDIDATE
NEXT_GATE = H8→H10, to be frozen before H10 results
NC_M6 = FROZEN
TOLERANCES = UNCHANGED_AFTER_RESULTS

The conditioned tail predictor may reduce future full higher-order work only after it has been validated by this H6→H8 independent comparison. It is not yet a theorem or production stopping rule.

## 8. Status at freeze time

H4_PRODUCTION_FREEZE = NO
H4_REJECTION = DETERMINED
H6 = ACTIVE_CANDIDATE
H8 = NEXT_AUDIT_SPACE
H6_PRODUCTION_FREEZE = UNRESOLVED
H6_TO_H8_GATE = FROZEN_BEFORE_RESULTS
EXPERIMENT_USED_FOR_ORDER = NO
RAW_TAIL_UNIVERSAL_ESTIMATOR = NO
BORDERED_LIMIT_TAIL_ESTIMATOR = VALIDATION_REQUIRED
