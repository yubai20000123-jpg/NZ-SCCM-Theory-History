# TREE DELTA — Case21 286 kN gap diagnosis

Time: 2026-08-20 19:29 +08:00

Current node:

`NC-M4 + reduced (Delta,A,epsilon_m) kinematics -> hr=0 rebar -> 286.12 kN audit -> comparator corrected to Pf_exp=368.31275 kN -> material/kinematic root-cause diagnosis`.

Locked conclusions:

1. Case21 `336 kN` is experimental buckling onset, not ultimate/failure. Ultimate comparator is `368.312750 kN`.
2. `286.12 kN` is withdrawn as a valid Case21 benchmark prediction; it remains only the solution of the current NC-M4 + reduced-kinematics equations.
3. Decisive material issue: NC-M2 beta was defined using `t=eps_t/eps_cr`; NC-M4 changed the T4 coordinate to `eps_t/eps_t0` and reused it in beta. For Case21 `eps_t0≈1.0109e-5`, creating a ~10.33x coordinate amplification.
4. At the old successful Case21 center state, current NC-M4 gives beta≈0.00763484 and axial TC stress ≈-0.15758 MPa, whereas the old source-consistent R10 operator gives ≈-20.60002 MPa. The unsoftened NC-M4 compression skeleton gives ≈-20.63922 MPa, proving beta is the immediate axial-compression killer.
5. Restoring only the old beta coordinate gives beta≈0.451 and stress≈-9.31 MPa at that state; therefore the simplified beta function itself also requires source-range audit, not merely scale correction.
6. NC-M4 also loses initial Poisson/biaxial coupling; nu is absent from the current operator. This drives the Rm=0 root toward the wrong transverse-strain branch.
7. The current `(Delta,A,epsilon_m)` field is not algebraically equivalent to the previous Airy-compatible `(D,q,alpha)` field. The current square-halfwave midsurface x-strain requires the coefficient constraints `u^2=0` and `v^2=-u^2v^2`, which the old successful field does not satisfy.
8. Reinforcement is secondary: current-vs-old steel contribution difference is ~13.6 kN, while concrete contribution difference is ~67.0 kN.
9. Next unique work: material gate first (TC coordinate/coupling and Poisson consistency), then kinematics gate (restore or exactly condense compatible Airy redistribution), then recompute Case21 without experiment-based tuning.
