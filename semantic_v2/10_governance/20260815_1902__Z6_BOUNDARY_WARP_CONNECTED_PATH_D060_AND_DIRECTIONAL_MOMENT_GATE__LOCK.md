# Z6 boundary-warp connected-path D=0.60 lock

Timestamp: 2026-08-15 19:02 +08:00

## Accepted status

- D=0.50 coupled Rq/Rc checkpoint = certified.
- D=0.55 and D=0.60 = connected near-equilibrium checkpoints with residuals O(1e-4) relative to internal cancellation scales.
- P rises 37.3451 -> 38.4106 -> 39.1270 MN; no peak found by D=0.60.
- D=0.625 best attempt is not accepted because Rc residual remains about 1.2% of its internal cancellation scale.
- D=0.65 exploratory states are not equilibrium.
- corrected Z6 Pu remains NOT SOLVED.

## Representation gate

Beyond D=0.60, small q/c perturbations required for numerical 2x2 Jacobians cause severe generalized coefficient growth/runtime variability in the current N48/Cayley-Hamilton implementation.

This is a representation/runtime gate, not proof of physical path termination.

## Mandatory next task

`CURRENT_NEXT_TASK = Z6_BOUNDARY_WARP_DIRECTIONAL_MOMENT_JACOBIAN_FROM_D060`

Keep the same material/current map and kinematics. Compute only directional moment contractions needed for P,Rq,Rc and the 2x2 q/c local Jacobian; do not construct the full generalized high-degree stress polynomial for every perturbation.

## Aspect-ratio correction retained

Synthetic a/b energy diagnosis must use elastic energy Pcr first. Zhou Eq5-87/5-88 remains an FE-fitted lower-envelope design comparator, not an energy-law Pu response.

## Frozen parent

R10, N48-C1/MM, Cayley-Hamilton, General D15, Nguyen second-order kinematics, one complete halfwave, A0=a/500, degree24 shell radial-cap production checkpoint, and zero formal structural spatial quadrature remain unchanged.
