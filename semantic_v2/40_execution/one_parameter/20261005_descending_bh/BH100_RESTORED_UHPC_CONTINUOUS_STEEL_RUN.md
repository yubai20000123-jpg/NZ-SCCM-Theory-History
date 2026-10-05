# BH100 RESTORED peak-rebased UHPC + continuous local-Mises steel run

Status: RUN STARTED

Purpose: recompute BH100 only after retracting the accidental ABS/raw UHPC path.

## UHPC identity — frozen, no modification allowed
Use the previously locked peak-rebased path:
- eta_t = positive_part(eps1)
- eta_c = positive_part(-eps2)
- d_hat_t = 0 for eta_t <= eps_tp
- d_hat_c = 0 for eta_c <= eps_cp
- post-peak:
  d_hat_t = max((d_t_ABAQUS-d_t,p)/(1-d_t,p),0)
  d_hat_c = max((d_c_ABAQUS-d_c,p)/(1-d_c,p),0)
- d = max(d_hat_t,d_hat_c)
- Delta p_t = max(p_t(eta_t)-p_t,p,0)
- Delta p_c = max(p_c(eta_c)-p_c,p,0)
- project peak-rebased plastic curvatures to w_P
- rho_A and rho_D remain the locked energy-weighted continuous integrals.

No equivalent-uniaxial Poisson correction. No ABS/raw damage/plastic.

Regression check required:
at BH100 w=82.2 mm the UHPC evaluator must recover approximately
rho_A=0.97921, rho_D=0.96642, w_P=10.33 mm, P_U≈10.57 MN.

## Steel candidate correction — retained
Replace the rejected whole-face single-e plastic corrector by the continuous local Mises-cap operator.

For each prescribed w and each face:
1. solve the same whole-face predictor A from the locked R_A geometry/mean relation using the restored UHPC w_P;
2. form the global steel base field;
3. apply the current-state radial Mises cap to the global base where required;
4. form the R06 seven-harmonic local fluctuation field;
5. assemble the local axial mean shift so that the un-limited global+local axial mean equals the Yun predictor mean;
6. solve pointwise/algebraically Phi(g + lambda*l)=fy^2 for lambda in [0,1];
7. integrate sigma_y continuously over the face/thickness.

## Numerical-evaluator role
The theory remains continuous. Numerical quadrature is used only as an independent evaluator with order convergence; it is not a material-point discretization or constitutive definition.

## Output gates
- UHPC regression at w=82.2 mm.
- TOP/BOTTOM A, predictor means, global means, capped means and yielded fractions.
- complete P(w) key-point curve.
- first external maximum, if it exists in the scanned physical branch.
- convergence check at the candidate maximum.
- no FEM/test value may enter the solve.

BH085 and smaller cases remain paused.
