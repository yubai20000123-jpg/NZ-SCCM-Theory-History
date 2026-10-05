# BH100 continuous local-Mises steel recalculation run

Status: RUN STARTED.

Purpose: recalculate BH100 only. Freeze the corrected UHPC multiaxial damage driver. Replace the rejected whole-face single-e steel corrector by a continuous local Mises-cap operator.

Frozen UHPC:
eta_t_eq = positive_part(eps1 + nu_c*eps2)/(1-nu_c^2)
eta_c_eq = positive_part(-eps2 - nu_c*eps1)/(1-nu_c^2)
ABS/raw UC141 damage and ABS/raw plastic functions unchanged.

Steel geometry:
Es=206000 MPa, nu_s=0.30, fy=355 MPa, ts=4 mm.
BH100: b=5000 mm, ah=10000 mm, w0=12.5 mm, A0=0.703125 mm, N=m=4.

Steel sequence for each prescribed w:
1. solve the same predictor total local amplitude A_plus/A_minus used by the prior BH100 path;
2. construct the continuous overall/global steel trial stress field;
3. apply the frozen current-state algebraic Mises limit to the global field pointwise if required;
4. construct the Yun/R06 elastic local stress increment field from the total local geometry;
5. at every continuous point solve the explicit quadratic
   Phi(g + lambda*l)=fy^2
   for the largest admissible lambda in [0,1];
6. integrate sigma_y = g_y + lambda*l_y continuously over each steel face;
7. P_total = P_UHPC + P_top + P_bottom.

No FEM/test value is used in the solve. FEM comparison is permitted only after the theoretical curve and peak are frozen.

Monitoring gates:
- verify old predictor top/bottom means before local plastic limiting;
- verify the repaired face-average stress changes continuously at first yield;
- report yielded-area fraction, face-average stress, top/bottom resultant eccentricity;
- locate the first external maximum of the repaired P(w) curve;
- keep BH085 and smaller cases paused until BH100 is accepted.
