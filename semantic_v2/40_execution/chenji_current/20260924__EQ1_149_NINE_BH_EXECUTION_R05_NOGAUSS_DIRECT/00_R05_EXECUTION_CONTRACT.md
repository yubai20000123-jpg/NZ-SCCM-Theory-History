# Eq.(1)–(149) R05 — direct 10-scalar iteration, zero spatial Gauss

## State vector at prescribed Delta

X = [q, Aplus, Aminus, epsx_bar, epsy_bar, ex_alpha, ey_beta, Fx, Fy, P]^T.

No extra structural unknowns are allowed.

## Residual vector

R = [R1,R2,R3,R4,R5,R6,R_Aplus,R_Aminus,R_q,R_Delta]^T.

R1–R6 are the Chen-Ji §8.8/H1 current-resultant consistency equations; R_Aplus is Eq.(114); R_Aminus is Eq.(119); R_q is Eq.(109); R_Delta is Eq.(123) evaluated on the retained compatible field.

## Spatial integration rule

N_spatial_Gauss = 0.
N_spatial_sampling = 0.
N_material_point_grid = 0.

Thickness integrals are eliminated by constitutive branch roots and exact antiderivatives wherever the current material law admits them. Area integrals are evaluated from algebraic/Fourier expansion coefficients and exact trigonometric moments, or by symbolic regional integration when a moving constitutive branch boundary is active. Expanding the integrand in strain/invariant space is permitted; evaluating the field at x_i,y_j,z_k is not.

## Iteration

At each prescribed Delta, iterate the same 10 equations directly:

J(X^k) dX = -R(X^k),
X^{k+1}=X^k + lambda dX.

Jacobian differentiation may be analytic or finite-difference only with respect to the ten scalar unknowns. A finite difference in the ten-dimensional state is not a spatial discretization and introduces no extra unknown.

Start from the zero-load root and use the previous converged state only as the initial guess for the next Delta. If a fold is encountered, change only the continuation parameter; do not change equations or unknown count.

No quadrature-order comparison or accuracy ranking is part of R05 execution.
