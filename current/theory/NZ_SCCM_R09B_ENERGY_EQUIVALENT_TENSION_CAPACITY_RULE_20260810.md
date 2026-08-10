# NZ-SCCM R09B — ENERGY-EQUIVALENT TENSION CAPACITY RULE

Date: 2026-08-10
Status: PROPOSED / MATERIAL-LEVEL RULE TO EXECUTE NEXT

## 1. Core idea

Do not choose the retained tensile-capacity parameter `u_inf` from Case21/Swartz structural Pu.
Instead reduce the full tensile constitutive branch to one simple monotone saturation law by matching a declared amount of material tensile strain energy on the material-native tensile interval.

For the R09A saturation family

\[
u_t(\lambda)=u_\infty\frac{\kappa\lambda/u_\infty}{1+\kappa\lambda/u_\infty},\qquad \lambda\ge 0,
\]

its dimensionless tensile energy primitive is

\[
\widehat\Psi_t(\lambda;u_\infty)
=\int_0^\lambda u_t(s)\,ds
=u_\infty\lambda-\frac{u_\infty^2}{\kappa}
\ln\left(1+\frac{\kappa\lambda}{u_\infty}\right).
\]

The physical energy density is `fc*eps0*widehatPsi_t`.

## 2. Material-native energy matching

Use the NC source-native tensile transition limit

\[
\lambda_T=10x_{cr}=10\rho/\kappa.
\]

Define a reference tensile energy

\[
E_{t,ref}=\int_0^{\lambda_T}u_{t,ref}(\lambda)\,d\lambda.
\]

Then choose `u_inf` from

\[
\widehat\Psi_t(\lambda_T;u_\infty)=\eta_E E_{t,ref},
\]

where

- `eta_E=1`: energy-preserving smoothing;
- `0<eta_E<1`: deliberate conservative under-use of tensile material energy.

This is a material-level rule. `eta_E` must not be selected from Case21/Swartz Pu.

## 3. Current NC numerical identities

With the current Case21 NC material constants

\[
\kappa=2.0005129533678754,\qquad
x_{cr}=0.04998717945397425,
\]

\[
\lambda_T=0.4998717945397425.
\]

For the R08 adopted rounded-peak tensile baseline (0.09 peak -> 0.03 residual), the dimensionless tensile energy over `[0,lambda_T]` is

\[
E_{t,R08}=0.0297423717751147.
\]

Energy-preserving reduction to the R09A saturation law gives

\[
\boxed{u_\infty=0.0742211076392}.
\]

If instead the older frozen smooth source-shaped tensile reference is used directly,

\[
E_{t,source}=0.0317645237620717,
\]

which gives

\[
\boxed{u_\infty=0.0803081815656}.
\]

These two numbers are material-energy reductions, not structural back-calibration.

For the R08 reference, deliberate energy-retention factors give:

| eta_E | u_inf |
|---:|---:|
| 1.0 | 0.0742211 |
| 0.9 | 0.0655232 |
| 0.8 | 0.0571214 |
| 0.7 | 0.0490082 |

## 4. Relation to the structural limit equations

If the unified current material law is generated from a scalar material potential, the halfwave internal potential can be written

\[
\mathcal U(D,q)=\mathcal U_c+\mathcal U_t+\mathcal U_s.
\]

Under displacement-type axial control,

\[
P=\mathcal U_{,D},\qquad R_q=\mathcal U_{,q}.
\]

Therefore the existing stationary-limit condition

\[
L=P_{,D}R_{q,q}-P_{,q}R_{q,D}=0
\]

becomes the Hessian singularity

\[
\boxed{
L=\mathcal U_{,DD}\mathcal U_{,qq}-\mathcal U_{,Dq}^2=0
}
\]

provided the material tangent is potential-consistent (Maxwell symmetry / integrability).

This shows that force equilibrium and tangent/stability equilibrium are two derivative levels of the same energy functional rather than unrelated conditions.

## 5. Mandatory caveat

Energy balance alone cannot identify `u_inf`: for every admissible tensile law, the structural variables `(D,q)` can move to a different equilibrium state.
Therefore `u_inf` must be fixed by a MATERIAL energy convention first (energy-preserving or declared conservative energy-retention factor), and only then passed to the structural equilibrium/limit calculation.

For a general 2D current map, a scalar material potential exists only if the tangent is integrable, e.g.

\[
\frac{\partial\sigma_1}{\partial\varepsilon_2}
=
\frac{\partial\sigma_2}{\partial\varepsilon_1}
\]

in the chosen coordinates. If this fails, the project must either construct the current map from a potential first or treat the energy interpretation as pseudo-energy only.

## 6. UHPC portability

The same rule is transferable to UHPC without copying NC numerical values:

1. define the UHPC material-native tensile interval from the selected UHPC source;
2. compute/define the UHPC reference tensile energy;
3. choose an energy-retention factor independent of structural Pu;
4. solve the same one-parameter energy equation for `u_inf,UHPC`;
5. use the same explicit structural energy/P/R/L architecture.

## 7. Recommended next execution

`R09B_ENERGY_EQUIVALENT_TENSION_LEVEL_EXECUTION`

Execute both:

- `eta_E=1` relative to the currently adopted R08 baseline (`u_inf=0.0742211`);
- one explicitly conservative material rule (suggested first diagnostic: `eta_E=0.9`, `u_inf=0.0655232`).

Then rerun Case21 using the unchanged compression and reinforcement model. Do not choose between them from the Case21 experimental load; the structural results are validation only.
