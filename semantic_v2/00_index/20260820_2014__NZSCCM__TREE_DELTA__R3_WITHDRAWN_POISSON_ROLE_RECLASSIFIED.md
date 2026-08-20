# TREE DELTA — R3 withdrawn / Poisson role reclassified

Time: 2026-08-20 20:14 +08:00

Current node:

`NC-M4 -> R1 scale correction -> R2 TC-interaction repair (reopen functional form) -> R3 equivalent-uniaxial repair withdrawn -> restore Poisson baseline in reduced physical kinematics -> impose direct small-strain plane-stress tangent on restructured 2D material map`.

Locked corrections:

1. R3 equivalent-uniaxial transform is withdrawn; it was an unnecessary inheritance from Nguyen/R10 for the new reconstructed 2D material law.
2. Historical successful Case21 reduced physical kinematics already contains a Poisson baseline `e_x=nu D+...`, `e_y=-D+...`.
3. The recent three-variable formula incorrectly replaced that baseline with total `epsilon_m`. Reaudit target is `epsilon_x = nu Delta/ell + epsilon_m + nonlinear/bending terms`, where `epsilon_m` is an additional correction.
4. Poisson behavior remains a constitutive consistency requirement: the direct 2D material tangent at the origin must equal the isotropic plane-stress matrix `E0/(1-nu^2)[[1,nu],[nu,1]]`.
5. R3-only issues (raw/equivalent grid conflict; constant-dilation-vs-Nguyen issue) are removed.
6. R2's capped gamma_c non-C1 threshold is an R2-introduced issue and is reopened rather than silently retained.
7. Pre-existing NC-M4 issues remain: tangent asymmetry, no proven hyperelastic potential, missing shear-retention channel, T4 peak-strain consistency, compression initial-tangent compatibility.
