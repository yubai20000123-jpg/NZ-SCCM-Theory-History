# TREE DELTA — Case21 NC-M4 first-three repairs

Time: 2026-08-20 19:44 +08:00

Current node:

`NC-M4 original -> R1 separate TC softening scale -> R2 Nguyen Eq.3.43 compression softening -> R3 constant-nu equivalent-uniaxial Poisson restoration -> same Delta/A/eps_m structural kinematics -> hr=0 rebar -> direct-continuous audit`.

Locked:

1. Only root-cause items 1-3 are repaired. Structural issue 4 (uniform eps_m replacing richer Airy compatible redistribution) remains untouched.
2. R1 analytic gate PASS: scale substitution is rational and introduces no new generator.
3. R2 analytic gate PASS: Nguyen Eq.3.43 `gamma_c=min(1,1/(0.8+0.34 eps_t/eps_c0))`; only one algebraic state front `eps_t=(10/17)eps_c0`; relative-GKZ architecture survives.
4. R3 analytic gate PASS: `Ehat=((1-nu)E+nu tr(E)I)/(1-nu^2)`; same eigenvectors and same single principal radical; exact isotropic plane-stress small-strain limit restored.
5. Stepwise nonproduction audit Pu with Case21 hr=0 rebar:
   - original about 286.12 kN;
   - R1 only about 245.1 kN;
   - R1+R2 about 331.94 kN;
   - R1+R2+R3 about 325.8 kN (32/20 checkpoint 325.871 kN; 24-36 orders roughly 325.734-325.871 kN).
6. Correct experimental ultimate comparator remains 368.31275 kN; first-three repaired reduced-kinematics model remains about -11.5% low.
7. No repair parameter is calibrated to the experiment. Spatial Gauss is audit-only, not formal theory.
