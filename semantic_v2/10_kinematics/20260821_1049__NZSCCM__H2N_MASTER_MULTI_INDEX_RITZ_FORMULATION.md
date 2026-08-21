# NZ-SCCM H_{2N} master multi-index Ritz formulation

Timestamp: 2026-08-21 10:49 +08:00
Status: master symbolic formulation for subsequent derivation
NC-M6: FROZEN

## 1. Motivation

H2, H4, H6, ... should not be treated as separately invented kinematic models. They are nested truncations of one even-harmonic admissible family.

Introduce dummy Fourier indices m,n and a single truncation order N. The production equations are derived once in indexed form; H2/H4/H6 correspond only to N=1,2,3 during convergence audit.

## 2. Coordinates

X = pi*x/b
Y = pi*y/ell
k = b/ell

Use the same out-of-plane single complete halfwave and frozen second-order geometric terms as the existing NZ-SCCM system.

## 3. General H_{2N} in-plane displacement family

u displacement is denoted u below.

u(x,y) = eps0 [ eta*x + sum_{m=1..N} sum_{n=0..N} b/(2*m*pi) * a_{2m,2n} * sin(2mX) cos(2nY) ]

v(x,y) = eps0 [ -D*y + sum_{m=0..N} sum_{n=1..N} ell/(2*n*pi) * b_{2m,2n} * cos(2mX) sin(2nY) ]

For Swartz side-edge x restraint, eta is fixed according to the essential boundary condition (in the currently projected admissible family eta=0). For a free-transverse-resultant family such as the Z panels, eta is an active coordinate and R_eta=0 enforces the transverse resultant condition.

## 4. Generic linear membrane strain contribution

After differentiating the indexed displacement family:

e_x^L = eta + sum_{m=1..N} sum_{n=0..N} a_{2m,2n} cos(2mX) cos(2nY)

e_y^L = -D + sum_{m=0..N} sum_{n=1..N} b_{2m,2n} cos(2mX) cos(2nY)

For m>=1,n>=1,

gamma^L_{mn} = -[ k*(n/m)*a_{2m,2n} + (m/(k*n))*b_{2m,2n} ] sin(2mX) sin(2nY)

The n=0 u modes and m=0 v modes carry no corresponding cross-shear term.

The complete strain is

epsilon = epsilon_linear(D,eta,{a},{b}) + epsilon_vonKarman(q) + epsilon_bending(q,zeta)

with the frozen q-dependent geometric and bending terms retained exactly.

## 5. Multi-index form

Define one modal multi-index

mu = (type,m,n)

type in {u,v}.

Let c_mu denote the associated modal coefficient and B_mu(x,y) = partial epsilon / partial c_mu its analytic strain basis vector.

Then the complete normalized/physical strain can be written abstractly as

epsilon(x,y,z; zeta_global) = epsilon_0(D,q,eta;x,y,z) + sum_{mu in I_N} c_mu B_mu(x,y)

where I_N is the finite H_{2N} index set.

This replaces separate H2/H4/H6 strain derivations by one master expression.

## 6. Generic residuals

For every active modal coordinate c_mu,

R_mu = sum_phases integral_V sigma_p(epsilon) : B_mu dV = 0.

For eta,

R_eta = sum_phases integral_V sigma_x * eps0 dV = 0

when eta is free.

Rq and the axial resultant P retain their existing source-consistent definitions.

## 7. Generic Jacobian

For modal coordinates c_mu and c_nu, because the strain is linear in these coefficients,

J_{mu,nu} = sum_phases integral_V B_mu^T D_p B_nu dV.

Mixed entries with q are

J_{mu,q} = sum_phases integral_V B_mu^T D_p epsilon_,q dV

plus any source-consistent geometric second-derivative term only where epsilon_,mu q is nonzero in the chosen parameterization.

The q-q entry retains the complete von-Karman second derivative:

J_{q,q} = sum_phases integral_V [ epsilon_,q^T D_p epsilon_,q + sigma_p : epsilon_,qq ] dV.

No artificial major symmetry is imposed on the NC-M6 tangent.

## 8. H2/H4/H6 as truncations

H2: N=1
H4: N=2
H6: N=3
H8: N=4
...

Thus H2→H4 and H4→H6 are not changes of theory. They are consecutive truncations of the same H_{2N} master operator.

## 9. Error-order program

The preferred long-term target is to replace repeated named-order comparisons by a mathematical truncation statement in N.

Possible rigorous routes, in descending preference:

A. Parseval/Fourier tail bound.
If sufficient regularity of the converged membrane field is established, the L2 truncation error is the Fourier coefficient tail outside I_N. A decay estimate for modal coefficients then gives an explicit E_N bound.

B. Regularity-based spectral estimate.
If the field belongs to H^s, expect algebraic tail control of order N^{-s} (with the precise exponent determined by the norm and dimensional indexing). If the entire composed field is analytic in the spatial variables, exponential spectral decay may be available. NC-M6 state-front crossings may reduce global regularity, so exponential convergence must not be assumed without proof.

C. Consecutive-shell a posteriori estimator.
Use the newly activated shell max(m,n)=N+1 to measure unresolved modal energy. If a verified contraction/decay ratio is obtained, bound the remaining infinite tail without reference to experimental loads.

The error relation must be based on analytic regularity, residual/tail norm, or consecutive spectral spaces—not fitted to test ultimate loads.

## 10. What can and cannot be 'eliminated'

The integers m,n are dummy labels and disappear automatically after the finite sums are assembled. They are not physical unknowns.

The modal amplitudes a_{2m,2n}, b_{2m,2n} are genuine generalized coordinates and cannot in general be algebraically deleted merely by Fourier orthogonality because NC-M6 is nonlinear and couples spatial harmonics through sigma=M6(epsilon).

Exact/algorithmic reduction remains possible in limited senses:

1. Compile all indexed exact moments into a finite flat residual/Jacobian for a chosen N; m,n then exist only as assembly indices.
2. Use block/Schur condensation inside a Newton solve where appropriate; this changes computational organization, not the theoretical Ritz space.
3. If an implicit-function/static-condensation relation for high modes is proved, substitute it into a reduced residual. For nonlinear NC-M6 this is not assumed to possess a closed form.
4. If a rigorous N-error bound proves a finite N* sufficient, all modes above N* are eliminated by convergence proof rather than empirical deletion.

## 11. Recommended identity

Use H_{2N} as the formal membrane family and use H2/H4/H6 only as audit shorthand.

The desired final state is one of:

- a proven finite N*=constant production truncation; or
- an N-dependent error bound E_N <= tolerance that determines N* automatically from theory.

The final theory should not carry an experimentally tuned N.
