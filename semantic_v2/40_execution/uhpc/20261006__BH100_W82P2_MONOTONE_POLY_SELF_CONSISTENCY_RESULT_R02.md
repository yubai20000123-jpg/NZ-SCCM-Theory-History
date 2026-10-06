# BH100 @ w=82.2 mm UHPC monotone-polynomial self-consistency R02

Date: 2026-10-06
Branch: diagnostic/20261006-bh100-uhpc-we-wp-d-self-consistency

## Material surrogate

Replace discrete tension/compression table segments by continuous monotone polynomials.
Source internal variable: tension cracking strain xi_t; compression inelastic strain xi_c.
Derived source quantities:
- total strain = xi + sigma/Ec
- true plastic strain = xi - d/(1-d) * sigma/Ec

Use r = sqrt(xi/xi_max) and degree-6 Bernstein polynomials.
For Y(r) = Y_scale * sum c_k B_k^6(r), coefficient monotonicity c_(k+1)>=c_k guarantees dY/dr>=0.
The zero-data point is NOT a hard interpolation constraint. It is only given weight 0.1; all nonzero source points have weight 1.0.
Exact polynomial coefficients are stored in 20261006__UC141_MONOTONE_BERNSTEIN_POLY_COEFF_R02.csv.

Fit quality on nonzero material points:
- tension total-strain relative RMS = 2.2475e-4
- tension true-plastic relative RMS = 2.5809e-5
- tension damage RMS = 3.8311e-5; max abs damage error = 9.72e-5
- compression total-strain relative RMS = 4.7264e-4
- compression true-plastic relative RMS = 1.5773e-4
- compression damage RMS = 8.1613e-4; max abs damage error = 1.80e-3

At the source tensile peak the source values are:
- total strain 0.000970435765
- true plastic strain 0.000567960624
- damage 0.58207912
Polynomial values:
- total strain 0.000969565086
- true plastic strain 0.000567908909
- damage 0.582117455

## Local return

Recoverable principal elastic strain eta_E satisfies:
eta_E = eps_total(r) - eps_plastic(r).
Both terms are degree-6 Bernstein polynomials, so local return is a single degree-6 algebraic root problem.
No 23/30 material-segment search and no local Newton iteration are used.
Connected-root selection is retained for later softening states.

At the final BH100 same-mode root, the maximum tensile recoverable strain is about 5.76288e-4.
The degree-6 material equation has a unique physical root r_t = 0.64443716 there.
This gives true tensile plastic strain about 0.00195017 and damage about 0.769486.

## Same-mode global equations

Fixed total increment w = 82.2 mm, initial imperfection w0 = 12.5 mm.
Unknowns are w_E, rho_A, rho_D.
w_P = w - w_E.
Q = 2*(w0+w)*w_E - w_E^2.
Three residuals:
- F_E = w_E + w_P_calc - 82.2
- F_A = rho_A - rho_A_calc
- F_D = rho_D - rho_D_calc

## Converged same-mode diagnostic root

- w_E = 26.1791 mm
- w_P = 56.0209 mm
- rho_A = 0.75217
- rho_D = 0.67885
- Q = 4272.98 mm^2
- N_y_bar = 750.694 N/mm
- P_U(82.2) = 3.7535 MN

Load decomposition:
- bending contribution = 0.6817 MN
- membrane contribution = 3.0717 MN

Material-state audit:
- max recoverable tensile principal strain = 5.763e-4
- min recoverable compressive principal strain = -6.705e-4
- compression nonlinear activation is about 119.49/43400 = 2.753e-3
- therefore compression plastic/damage is inactive at this point
- max tensile true plastic strain = 1.950e-3
- max damage = 0.76949
- area-average of mean surface damage = 0.2370
- top active tensile-damage area fraction = 67.25%
- bottom active tensile-damage area fraction = 35.58%
- top d>0.5 area fraction = 41.77%
- bottom d>0.5 area fraction = 3.40%

## Integral audit

The theory remains a continuous field plus algebraic local return.
For this execution, deterministic high-order quadrature was used ONLY to evaluate the final continuous scalar area integrals and to establish a numerical benchmark; it is not a material-point history discretization.
Convergence:

| order | w_E mm | rho_A | rho_D | P_U MN |
|---:|---:|---:|---:|---:|
|32|26.1774|0.75213|0.67891|3.75313|
|48|26.1783|0.75198|0.67875|3.75248|
|64|26.1790|0.75190|0.67859|3.75210|
|96|26.1792|0.75207|0.67876|3.75299|
|128|26.1796|0.75226|0.67889|3.75390|
|160|26.1791|0.75225|0.67892|3.75384|
|192|26.1791|0.75220|0.67887|3.75358|
|256|26.1791|0.75217|0.67885|3.75347|

## Plastic-curvature modal audit

Define K_p = (alpha^2+nu beta^2) kappa_xp + (beta^2+nu alpha^2) kappa_yp.
Projection onto odd sine modes gives:
- (1,1) energy fraction = 0.7707; inferred plastic-reference amplitude = +56.0209 mm
- (1,3) energy fraction = 0.2125; inferred plastic-reference amplitude = -4.8113 mm
- (1,5) energy fraction = 0.01318; inferred amplitude = +0.2027 mm

First-mode residual norm ratio:
||K_p-K_p11|| / ||K_p|| = 0.4788.

Thus the same-mode root is NOT a final UHPC prediction.
The material field itself identifies one dominant missing mode: phi_13 = sin(alpha x) sin(3 beta y).
Modes (1,1)+(1,3) already explain about 98.32% of the current plastic-curvature-driver energy.

## R03 next step

Do not launch a large high-order Ritz basis.
Add only phi_13.
Allow both permanent plastic-reference geometry and recoverable elastic geometry to contain the (1,3) mode.
At fixed total maximum w=82.2 mm, solve the total-amplitude constraint, (1,1)/(1,3) equilibrium, (1,1)/(1,3) plastic projections, and damage-condensed current stiffness together.
Only after this two-mode closure may P_U(82.2) be promoted from diagnostic to current theory output.