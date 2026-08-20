# semantic_v2 tree delta — 2026-08-20 16:22

New theory checkpoint:

`semantic_v2/20_theory/20260820_1622__NZSCCM__MEMBRANE_RESULTANTS_AND_THETA_TC_CORRECTION.md`

Current correction:

- Explicitly restore Nguyen membrane/bending resultant split `N/M` in the reduced three-variable continuous theory.
- `R_A` must contain both membrane-resultant virtual work and bending-moment virtual work.
- `R_m = integral_A N_x dA`; `P = -(1/ell) integral_A N_y dA`.
- TC/CT principal-direction handling may use derived `theta(x,y,z)`; theta is not a new structural DOF.
- Do not redesign TC/CT merely to eliminate square-root eigenvalue formulas.
- For NC-M4 total-strain simplification, theta is taken as current principal-strain direction; this is distinct from Nguyen source cracked-history principal stress angle.
- Next execution target: direct continuous integration using full membrane + curvature kinematics, theta-based local state evaluation, thickness resultants N/M, then R_m/P/R_A.
