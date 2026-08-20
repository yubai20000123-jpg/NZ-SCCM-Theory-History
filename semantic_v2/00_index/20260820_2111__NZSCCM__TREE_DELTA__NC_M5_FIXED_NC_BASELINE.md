# TREE DELTA — NC-M5 fixed NC baseline

Time: 2026-08-20 21:11 +08:00

Current material node:

`NC-基准本构 (G21 physical target renamed) -> NC-M5 low-complexity direct current operator`.

Locked governance:

- no reference-model switching;
- NC baseline sectors: CC `c_i*=c_i(1+a_cc c1 c2)`, TC/CT `c*=c(1-tau)`, TT `tau_i*=tau_i(1-a_t tau_j^8)`;
- specimen inputs: `E0,nu,fc,eps_c0,ft`; if ft absent, `ft=0.1fc`;
- derived: `kappa=E0 eps_c0/fc`, `rho=ft/fc`, `xcr=rho/kappa`;
- `k_tc` and `k_eta` deleted from NC-M5 architecture.

NC-M5 key architecture:

\[
X=((1-\nu)E+\nu\,tr(E)I)/[(1-\nu^2)\varepsilon_{c0}].
\]

X is a fixed linear NC material-coordinate transform, not R3 state-dependent dilation and not an additive stress correction. X and E are coaxial, so no second theta and no new radical.

Four NC material sectors are defined only on the signs of X eigenvalues `(lambda1,lambda2)`.

Origin gate proved:

\[
D_{CC}(0)=D_{TC}(0)=D_{CT}(0)=D_{TT}(0)
=\frac{E_0}{1-\nu^2}
\begin{bmatrix}1&\nu&0\\\nu&1&0\\0&0&(1-\nu)/2\end{bmatrix}.
\]

Structural baseline restored as `eps_x = nu Delta/ell + eps_m + second-order terms`; at A=0, eps_m=0 the NC material coordinates reduce exactly to one zero transverse coordinate plus one axial compression coordinate, so fake-TC is avoided.

Status:

`NC_M5_ARCHITECTURE = ACTIVE_CANDIDATE`
`PLANE_STRESS_ORIGIN_TANGENT_GATE = PASS`
`POISSON_FIX_WITHOUT_COMPLEXITY_INCREASE = PASS`

Open before production lock:

1. compile fixed NC tensile baseline into a low-complexity single analytic `T5` without changing reference;
2. audit finite sector-boundary tangent/C1-C2 regularization;
3. full-domain boundedness;
4. joint stress+tangent certificate;
5. recompile exact analytic Rm/P/RA backend, then Case21.
