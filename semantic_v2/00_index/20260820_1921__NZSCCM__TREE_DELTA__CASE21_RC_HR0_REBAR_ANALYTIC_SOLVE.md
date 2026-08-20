# TREE DELTA — Case21 NC-M4 + hr=0 reinforcement

Time: 2026-08-20 19:21 +08:00

Current node:

`NC-M4 pure concrete exact global Rm/P/RA -> source-consistent Case21 mid-plane orthogonal reinforcement -> exact elementary Ps/Rm,s/RA,s -> same 3-variable total system -> RC limit audit`.

Locked conclusions:

1. General reinforcement representation may remain two-layer bookkeeping; Case21 uses the source value `hr=0`, so the two bookkeeping layers coincide and their areas sum to the original single physical layer. No reinforcement area doubling.
2. Case21 nominal total reinforcement ratio `p=0.75%` is split equally between orthogonal directions in the current project interpretation: `rho_x=rho_y=0.00375`, equivalent steel thickness per direction `t_s=0.072375 mm`.
3. Case21 steel input: `Es=200000 MPa`, `eps_y=0.00265`, `fy=530 MPa`.
4. At the RC limit audit all reinforcement remains elastic; therefore the reinforcement additions are exact elementary formulas:
   - `Rm,s=t_s Es (B^2 eps_m + pi^2 S/4)`;
   - `Ps=t_s Es (Delta - pi^2 S/(4B))`;
   - `RA,s=t_s Es H [pi^2/4(eps_m-Delta/B)+9 pi^4 S/(32 B^2)]` for Case21 `b=ell=B`.
5. Total system remains exactly three unknowns `(Delta,A,eps_m)` with `R_A,c+R_A,s=0`, `R_m,c+R_m,s=0`, and total `det J_lim=0`; steel derivatives are elementary exact and concrete derivatives remain in the same shared-GKZ family.
6. Independent direct-continuous audit checkpoint: `Delta≈1.078263 mm`, `A≈2.868101 mm`, `eps_m≈-3.258896e-5`, `Pu≈286.1263 kN`; converged audit band at 40-48 area orders is about `286.117-286.126 kN`.
7. This is about `-0.90%` relative to the earlier pure-concrete audit `288.7205 kN`; the y steel contributes positive axial force but the transverse reinforcement shifts the `Rm=0` state and reduces concrete contribution.
8. Numerical value remains `DIRECT_CONTINUOUS_AUDIT` until the exact concrete shared-GKZ derivative evaluator is numerically executed; formal reinforcement addition itself is closed with zero spatial quadrature.
