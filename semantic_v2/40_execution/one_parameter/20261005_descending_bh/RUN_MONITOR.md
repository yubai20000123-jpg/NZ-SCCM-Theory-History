# Run monitor

BH085-BH050 old results remain quarantined. BH032 and smaller remain paused.

## BH100 restored UHPC + continuous local-Mises steel run — COMPLETE

The accidental ABS/raw UHPC reversion has been removed.

### Locked UHPC identity
- eta_t = positive_part(eps1)
- eta_c = positive_part(-eps2)
- d_hat_t = 0 for eta_t <= eps_tp
- d_hat_c = 0 for eta_c <= eps_cp
- post-peak damage is PEAK-REBASED from the Abaqus source table
- Delta p_t = max[p_t(eta_t)-p_t,p,0]
- Delta p_c = max[p_c(eta_c)-p_c,p,0]
- w_P is projected only from these peak-rebased plastic strains
- no equivalent-uniaxial Poisson correction
- no ABS/raw damage or plastic

### Mandatory UHPC regression at w=82.2 mm — PASSED
rho_A = 0.97921043
rho_D = 0.96641992
w_P = 10.330668 mm
P_UHPC = 10.569428 MN

This reproduces the previously locked BH100 UHPC state.

### Continuous local-Mises steel candidate at w=82.2 mm
A_TOP = 4.434799 mm
A_BOTTOM = 4.660565 mm
Yun predictor means = 251.401 / 271.665 MPa
global elastic means = 223.961 / 299.286 MPa
continuous capped means = 246.978 / 271.665 MPa
P_TOP = 4.93956 MN
P_BOTTOM = 5.43330 MN
P_total = 20.94229 MN
steel resultant eccentricity about UHPC mid-plane ~= 1.09 mm

The previous artificial 148/272-MPa whole-face split is removed.

### Candidate branch maximum
Numerical continuous-integral evaluator:
w_u ~= 142.3 mm
P_u ~= 26.873 MN
P_UHPC ~= 14.070 MN
P_TOP ~= 6.147 MN
P_BOTTOM ~= 6.656 MN
rho_A ~= 0.86181
rho_D ~= 0.82880
w_P ~= 79.02 mm

This is NOT accepted as the final UCFT theory result.

## Current interpretation
The restored UHPC path is now correct, so the high total load cannot be attributed to the earlier ABS/raw UHPC mistake.

The candidate continuous local Mises-cap removes the nonphysical whole-face TOP collapse, but exposes a remaining steel predictor/mean-stress inconsistency:
the Yun whole-face predictor is still used as a total face mean while the global base already carries the overall axial demand. This likely duplicates mean axial demand at the global/local interface.

## Decision
Do not resume BH085-BH005.

Next audit:
keep the restored peak-rebased UHPC and continuous local Mises cap fixed, and re-derive only the steel global-base / Yun-local mean compatibility so Yun contributes the true local increment rather than a second total mean.

## Backed-up files
- RETRACTION_BH100_UHPC_PATH_REVERSION.md
- BH100_RESTORED_UHPC_CONTINUOUS_STEEL_RUN.md
- BH100_RESTORED_UHPC_CONTINUOUS_STEEL_RESULT.md
- BH100_RESTORED_UHPC_CONTINUOUS_STEEL_CURVE.csv
- bh100_restored_uhpc_continuous_steel_evaluator.py
