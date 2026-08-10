# R09A — TENSION SATURATION SENSITIVITY — HISTORY

Date: 2026-08-10

## Trigger

After R08 replaced the oscillatory R07R tensile regression by a shape-preserving rounded peak, the user proposed an even more aggressive simplification: because axial-compression force equilibrium and stiffness equilibrium are expected to be compression dominated, the tensile branch could be reduced to a simple monotone rise toward a lower plateau instead of preserving a distinct tensile peak/softening history.

## Execution

R09A kept fixed:

- NC compression branch from R08;
- Case21 geometry;
- Nguyen second-order halfwave kinematics;
- analytic reinforcement coupling;
- same explicit limit equations `P,R,L`.

Only the tensile branch was changed.

Test family:

\[
u_t=u_\infty\frac{\kappa\lambda/u_\infty}{1+\kappa\lambda/u_\infty},\qquad \lambda\ge0.
\]

Predeclared brackets, before structural comparison:

- SAT03: `u_inf=0.03`
- SAT05: `u_inf=0.05`
- SAT07: `u_inf=0.07`

## Results

```text
R08   Pu = 335.602379 kN
SAT03 Pu = 322.401942 kN
SAT05 Pu = 334.822979 kN
SAT07 Pu = 345.811115 kN
```

SAT03–SAT07 spread:

```text
23.409173 kN
7.001495 % of the SAT-series mean Pu
```

Direct load decomposition remains compression dominated, but changing the tensile level moves `D_u` and `q_u`, which changes the compression-side `Pc` itself.

## Historical correction

The project therefore corrects an overly strong interpretation of the user's compression-dominance hypothesis.

Correct statement:

> Tension does not dominate the direct axial load, and its detailed sharp source shape can be strongly simplified. But the retained tensile capacity level is not negligible in the coupled stability equations.

## Governance consequence

Do not restore the old high-complexity tensile peak/softening law.

Do not select a tensile plateau from Case21/Swartz Pu.

First freeze one simple tensile-capacity parameter from material-source evidence or a declared conservative material convention.

Next:

`R09B_SOURCE_GROUNDED_TENSION_CAPACITY_LEVEL`.