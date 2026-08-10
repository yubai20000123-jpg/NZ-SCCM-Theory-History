# NZ-SCCM R09A — TENSION SATURATION SENSITIVITY

Date: 2026-08-10

## 1. Question

Test the user's hypothesis directly:

> In axial compression stability, force equilibrium and tangent/stability equilibrium should be dominated by the compression side. Therefore the tensile branch may be simplified much more aggressively than in R08.

R09A changes ONLY the tensile branch. Compression, geometry, reinforcement and the explicit limit equations are kept fixed.

No saturation level is chosen from the Case21 experiment.

## 2. Tested tensile functions

R08 baseline:
rounded peak at about 0.09 fc followed by monotone decay to 0.03 fc.

R09A saturation family:

u_t(lambda)
= u_inf * r/(1+r),

r = kappa lambda/u_inf,

lambda >= 0.

Derivative:

u_t'(lambda)
= kappa/(1+kappa lambda/u_inf)^2.

Properties:
- u_t(0)=0;
- u_t'(0)=kappa;
- monotone increasing;
- no peak, no dip, no rebound;
- asymptotic plateau u_inf.

Executed:
SAT03: u_inf=0.03
SAT05: u_inf=0.05
SAT07: u_inf=0.07

## 3. Explicit RC chain

For each candidate, the same R08 architecture is used:

P = Pc + Ps,
R = Rc + Rs,

L = P_D R_q - P_q R_D.

Reinforcement is analytic and inserted before solving the limit state.

Concrete Pc(D,q), Rc(D,q) are represented locally by explicit degree-(16,16) Chebyshev surfaces around the mechanically located main branch. Their coefficients and analytic derivatives are part of the saved artifact.

The offline full-halfwave evaluation used for coefficient identification remains an audit/identification step; runtime limit-state evaluation is explicit.

## 4. Results

| candidate | u_inf/fc | D_u | q_u | A_u (mm) | Pc (kN) | Ps (kN) | Pu (kN) | error vs Case21 experiment |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| R08 | — | 0.706185 | 0.0165438 | 20.1834 | 317.3033 | 18.2991 | 335.6024 | -8.8811% |
| SAT03 | 0.03 | 0.674303 | 0.0166825 | 20.3526 | 305.3951 | 17.0068 | 322.4019 | -12.4652% |
| SAT05 | 0.05 | 0.732368 | 0.0175027 | 21.3533 | 316.3733 | 18.4497 | 334.8230 | -9.0928% |
| SAT07 | 0.07 | 0.789742 | 0.0182769 | 22.2978 | 325.9317 | 19.8795 | 345.8111 | -6.1094% |

Independent same-root audit residuals are all small:

- R08: R_audit = -0.024836 kN mm
- SAT03: R_audit = +0.020661 kN mm
- SAT05: R_audit = +0.003797 kN mm
- SAT07: R_audit = +0.004502 kN mm

All reinforcement remains elastic for all four candidates.

Sensitivity across SAT03, SAT05, SAT07:

Pu span = 23.409173 kN
Pu span / mean Pu = 7.001495 %
D span = 0.11543949
q span = 0.00159440

## 5. Interpretation

The user's compression-dominance intuition is partly correct but must be stated carefully.

At every stationary root, direct load decomposition is compression dominated:

- concrete contributes about 305–326 kN;
- reinforcement contributes about 17–20 kN.

However, the tensile branch is NOT negligible in the coupled stability problem. Changing only the monotone tensile saturation level from 0.03 fc to 0.07 fc changes the stationary Pu by about 23.41 kN, or 7.00% of the mean SAT-series capacity.

The mechanism is indirect as well as direct: changing the tensile branch shifts the equilibrium/stationary coordinates D_u and q_u, which in turn changes the compression-side concrete contribution Pc. Therefore a statement such as “tension carries little direct axial load” does not imply “the tensile constitutive branch has little effect on Pu”.

This result still supports aggressive simplification of the tensile law SHAPE. The high-complexity source peak/softening details are not needed. But the retained tensile capacity level cannot be chosen arbitrarily; it needs a material/source-based rule or an explicit conservative design convention.

## 6. Decision

R09A_TENSION_SATURATION_SENSITIVITY = PASS_DIAGNOSTIC

COMPRESSION_DOMINATES_DIRECT_LOAD = PASS

TENSILE_SHAPE_CAN_BE_STRONGLY_SIMPLIFIED = PASS

TENSILE_CAPACITY_LEVEL_IS_NEGLIGIBLE = FAIL

MONOTONE_SATURATION_FAMILY = RETAINED AS SIMPLE EXPLICIT CANDIDATE

SAT03/SAT05/SAT07 = SENSITIVITY BRACKETS ONLY; NONE IS FROZEN FROM CASE21 EXPERIMENT

FORMAL_ZERO_QUADRATURE_PRODUCTION = HOLD (same offline-identification caveat as R08)

## 7. Next task

The next task is not to restore the old sharp tensile peak and not yet to add a multiaxial correction.

First define a source-grounded or explicitly conservative rule for the one retained tensile-capacity parameter of the simple monotone law, and test that rule on the NC material domain rather than fitting it to Case21 Pu.

Recommended next task:

R09B_SOURCE_GROUNDED_TENSION_CAPACITY_LEVEL

After that scalar tension level is frozen independently of structural experiments, return to the minimum source-grounded multiaxial correction question.