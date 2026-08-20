# TREE DELTA — Case21 NC-M4 pure-concrete three-variable solve

Time: 2026-08-20 19:08 +08:00

Current node:

`Case21 raw geometry/compression inputs -> NC-M4 exact shared-GKZ Rm/P/RA -> three-variable limit system -> source-input gate -> direct-continuous nonproduction audit`.

Locked conclusions:

1. Final mathematical system is `(R_A,R_m,det J_lim)=(0,0,0)` in `(Delta,A,epsilon_m)`.
2. Implicit-function proof: `det J_lim = det J_c * dP/dDelta` on the equilibrium manifold; ordinary fold requires `det J_c != 0`, plus local-max and branch-connectivity checks.
3. Original Case21 input supplies `b=ell=1220 mm`, `h=19.30 mm`, `fc=21.23 MPa`, `E0=20321 MPa`, `eps_c0=0.00209`, `nu=0.18`, `A0=b/400=3.05 mm`, but does not supply specimen tensile strength `ft` required by NC-M4.
4. If initial tensile tangent is locked to `E0`, then `eps_t0 = 0.0967635 ft/E0`; therefore only `ft` remains as the independent tensile input gap.
5. Diagnostic transfer only: `ft=0.1fc=2.123 MPa`, `eps_t0=1.01091929777e-5` gives a direct-continuous audit root `Delta=1.17258497 mm`, `A=2.84803957 mm`, `epsilon_m=-3.28075016e-5`, `Pu=288.7205038 kN`. This used spatial quadrature and finite-difference derivatives only as an independent audit and is NOT production.
6. Formal numerical production remains blocked until `ft` is explicitly locked/provided and the exact shared-GKZ derivative evaluator is used.
