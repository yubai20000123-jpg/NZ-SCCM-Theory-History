# NZ-SCCM H2→H4 result ledger and H2 rejection

Timestamp: 2026-08-21 10:49 +08:00
Status: audit decision ledger
Material operator: NC-M6 FROZEN
Production status: H4 NOT YET FROZEN

## 1. Governance boundary

This ledger records the already obtained H2→H4 convergence audit. It does not change NC-M6 and does not authorize H4 as the production membrane subspace.

Formal identity remains:
- ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
- N_formal_spatial_sampling = 0
- N_formal_spatial_quadrature = 0
- N_formal_spatial_subdomains = 1
- N_formal_thickness_quadrature = 0
- material_points = 0

Direct-current high-order continuum quadrature used in the audit is an AUDIT-ONLY decimal localizer and has no formal theoretical identity.

## 2. H2→H4 pre-frozen acceptance quantities

The order decision was made without experimental loads. The frozen convergence observables were

- delta_P <= 0.5%
- delta_D <= 0.5%
- delta_w <= 1.0%
- delta_epsilon <= 2.0%

where delta_epsilon is the L2 difference of the midsurface membrane strain field between consecutive spectral spaces on the same origin-connected equilibrium branch.

A close Pu value alone is not sufficient to freeze the lower spectral order.

## 3. Swartz24 result

H2 passes only Cases 1–8.

- Cases 1–8: 8/8 PASS
- Cases 9–16: 0/8 PASS
- Cases 17–24: 0/8 PASS
- Total: 8/24 PASS

Global-load convergence is much faster than membrane-field convergence:

- max(delta_P) = 0.1367%
- median(delta_P) = 0.02294%
- max(delta_epsilon) = 4.157%
- median(delta_epsilon) = 2.061%

Representative cases:
- Case 9: delta_P = 0.1155%, delta_epsilon = 3.666%
- Case 10: delta_P = 0.1367%, delta_epsilon = 4.106%
- Case 11: delta_P = 0.1213%, delta_epsilon = 4.157%
- Case 14: delta_P = 0.1035%, delta_epsilon = 3.924%
- Case 15: delta_P = 0.0897%, delta_epsilon = 3.787%

Therefore Pu convergence does not imply membrane redistribution convergence.

## 4. Case21 audit-localizer independence check

At increased audit resolution:

H2:
- Pu = 259.21868 kN
- change relative to lower audit order ≈ 0.00528%

H4:
- Pu = 259.15585 kN
- change relative to lower audit order ≈ 0.00188%

Both are below the 0.05% audit-localizer stability threshold. Hence the H2/H4 difference is not attributable to the audit quadrature resolution.

## 5. Z0 decisive result

High-order audit localization gives approximately:

H2:
- Du ≈ 0.930
- qu ≈ 0.00453
- Pu ≈ 31.90 MN

H4:
- Du ≈ 0.967
- qu ≈ 0.00586
- Pu ≈ 31.77 MN

The total load is already close, but the state and field are not:

- delta_D ~ 4%
- delta_w ~ 14%
- delta_epsilon ~ 15%

The H4 Z0 audit-localizer change from G56→G64 satisfies
- delta_quad(Pu) = 0.03025% < 0.05%

Thus the Z0 field-convergence failure is decisive and cannot be dismissed as numerical integration noise.

## 6. Branch-tracking consequence

The enlarged membrane subspace exposes a D-fold on the origin-connected Z branch. Consequently D cannot be assumed to remain a globally valid continuation parameter.

The formal limit condition remains the complete consistent determinant. Audit continuation must allow an augmented/pseudo-arclength parameterization through folds. This changes no physical degree of freedom and is only a branch-tracking device.

## 7. Physical interpretation

For the single (1,1) out-of-plane halfwave, von Karman geometric forcing directly generates the low even-harmonic family represented by H2. However the nonlinear current material map sigma=M6(epsilon) generates higher spatial harmonics after constitutive composition.

Therefore:

kinematic forcing closes at H2

DOES NOT imply

nonlinear membrane stress redistribution closes at H2.

H4 has the physical role of recovering constitutively generated membrane harmonics, not changing the frozen out-of-plane halfwave or material law.

## 8. Decision

H2_GLOBAL_FREEZE = NO
H2_REJECTION = DETERMINED
H4 = NEXT_MINIMUM_CANDIDATE
H4_PRODUCTION_FREEZE = NOT AUTHORIZED
M7 = PROHIBITED

The next order decision must be H4→H6 under a criterion frozen before examining the H6 results.
