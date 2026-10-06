# BH100 UHPC polynomial self-consistency NEXT CHAT HANDOFF R02

Branch: diagnostic/20261006-bh100-uhpc-we-wp-d-self-consistency

Read these files in order:
1. 20261006__BH100_FIXED_W_WE_WP_DAMAGE_SELF_CONSISTENCY_R01.md
2. 20261006__UC141_MATERIAL_TABLE_SOURCE_LOCK_R01.csv
3. 20261006__UC141_MONOTONE_BERNSTEIN_POLY_COEFF_R02.csv
4. 20261006__BH100_W82P2_MONOTONE_POLY_SELF_CONSISTENCY_RESULT_R02.md

Current material identity:
- discrete 23/30 table segments have been replaced by degree-6 monotone Bernstein polynomials
- internal polynomial coordinate r=sqrt(xi/xi_max)
- zero source point is soft-weighted 0.1, not hard-interpolated
- local material update is a degree-6 algebraic root eta_E=eps_total(r)-eps_p(r)
- BH100 @82.2 has no compression nonlinear activation; tension damage/plasticity controls

Current same-mode diagnostic root:
- w_E=26.1791 mm
- w_P=56.0209 mm
- rho_A=0.75217
- rho_D=0.67885
- P_U=3.7535 MN

DO NOT treat P_U=3.7535 MN as final.
Plastic-curvature modal audit:
- (1,1) energy fraction 77.07%
- (1,3) energy fraction 21.25%, plastic amplitude about -4.811 mm
- (1,5) only 1.318%
- first-mode residual norm ratio 47.88%

Therefore R03 must add ONLY phi_13=sin(alpha x) sin(3 beta y), and must allow the recoverable elastic geometry to change with it.
Do not add a large Ritz basis and do not reconnect the steel shell yet.
At fixed total maximum w=82.2, close total-amplitude constraint + (1,1)/(1,3) equilibrium + (1,1)/(1,3) plastic projections + current damage stiffness.