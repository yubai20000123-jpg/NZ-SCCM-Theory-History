# NZ-SCCM governance — Case21 certified 16-state semialgebraic-period refinement

**Timestamp:** 2026-08-17 11:55 +08:00  
**Status:** CONTROLLING RUNTIME REFINEMENT / SAME END-TO-END TASK / FORMAL Pu STILL OPEN

## 0. End-to-end task identity is unchanged

The project-level task remains exactly

```text
CASE21_AIRY_SCALAR_FORMAL_ZERO_SPATIAL_ULTIMATE_LOAD
```

This record does **not** create a new task and does not alter the mechanical path. It refines the mathematical identity of the already-selected fixed-endpoint positive-part period runtime and narrows its state size on the current Case21 branch.

Frozen boundary remains

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
Nguyen second-order continuous kinematics = ACTIVE
R10 physical current operator = FROZEN
reinforcement before coupled solve = REQUIRED
Airy-scalar r=lambda*M*a(nu) = ACTIVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
formal Gauss/Simpson/adaptive/cells/material-point-grid = PROHIBITED
high-order coefficient enumeration as production architecture = PROHIBITED
experimental calibration/root selection = PROHIBITED
```

## 1. Stable conformal source identity is promoted

For the source-level symmetric equivalent-strain matrix `E`, define

\[
W=E\left(\sqrt{E^2+\eta^2I}+\eta I\right)^{-1}.
\]

The old conformal inverse relation is

\[
E=2\eta W(I-W^2)^{-1}.
\]

The smoothed positive/negative source maps admit the exact identities

\[
\boxed{
\pi_\eta(E)=E\,W\,(I+W)^2\,(I+W^2)^{-2}
}
\]

and

\[
\boxed{
\pi_\eta(-E)=E\,W\,(I-W)^2\,(I+W^2)^{-2}.
}
\]

These identities are exact by scalar reduction and symmetric-matrix functional calculus. They replace the numerically poor implementation that separately inverts `I-W` and `I+W`. In the certified Case21 search box the negative principal conformal coordinate can approach about `-0.9973`, while `I+W^2` remains uniformly well away from singularity.

```text
STABLE_CONFORMAL_SOURCE_IDENTITY = PASS_EXACT
OLD_SEPARATE_(I+/-W)_INVERSE_IMPLEMENTATION = NOT PRODUCTION
```

## 2. Bernstein no-spatial-sampling spectral certificate

Use

```text
u = sin X in [0,1]
v = sin Y in [0,1]
w = (zeta+1)/2 in [0,1]
```

only as polynomial variables for exact Bernstein coefficient enclosure, not as spatial sampling points.

For the active Airy-scalar kinematics,

```text
deg tr(E)    = (2,2,1)
deg Delta(E) = (4,4,2)
```

at fixed `(D,q,lambda)`.

At the current direct-source peak the complete continuous halfwave is enclosed by

```text
tr(E)    in [-0.9516607416735428, -0.6221638560307847]
Delta(E) in [+0.5843087672642922, +0.6592312757236101]
gap       in [+0.7644009205019916, +0.8119305855327844]

lambda_plus  in [-0.09362991058577558, +0.09488336475099984]
lambda_minus in [-0.8817956636031636, -0.6932823882663881]
```

For the frozen R10 source

```text
a = rho/kappa = 0.04998717945397425
lambda1  = 0.05008051764913754
lambda10 = 0.49988116674539307
```

and the same enclosure gives

```text
t_plus/a  <= 1.8971668284751766 < 10
t_minus/a <= 4.506313752829062e-5 < 1
```

Therefore the second tensile source knot is rigorously inactive at the peak, the minus principal branch is entirely in the low tensile-source branch, and the spectral gap does not close.

## 3. Certified formal search box

A wider non-experimental solver neighborhood enclosing the current mechanics oracle was checked by one tensor-product Bernstein coefficient enclosure over the six variables `(u,v,w,D,q,lambda)`:

```text
D      in [0.75, 0.82]
q      in [0.00175, 0.00187]
lambda in [0.0, 0.15]
```

The exact polynomial degrees are

```text
deg tr(E)    = (2,2,1,1,2,1)
deg Delta(E) = (4,4,2,2,4,2)
```

and the Bernstein enclosure gives

```text
tr(E)    in [-0.9903643386854425, -0.5762231481954689]
Delta(E) in [+0.5246013442823345, +0.7152191687187780]
gap       in [+0.7242936864852092, +0.8457063135147910]

lambda_plus  in [-0.13303532610011665, +0.13474158265966102]
lambda_minus in [-0.9180353261001167, -0.6502584173403391]

t_plus/a  <= 2.6948274361042803 < 10
t_minus/a <= 4.804460717539394e-5 < 1
```

This box is an implementation/search enclosure derived from the direct-source oracle only; it is not experimental calibration and does not select a final root.

## 4. Current Case21 algebraic field shrinks from generic 64 to certified 16

Within the certified search box, the only radicals needed by the source-regular current R10 field are

\[
g=\sqrt{\Delta_E},
\qquad
s_+=\sqrt{\lambda_+^2+\eta^2},
\qquad
s_-=\sqrt{\lambda_-^2+\eta^2},
\]

and the single first-knot positive-part selector

\[
h_1=\sqrt{(t_+-a)^2}=|t_+-a|.
\]

All `U,C,T,T^7`, the 2x2 spectral projector, the current stress and its same-source first tangent stay in the multiquadratic span

\[
\boxed{
\mathcal B_{16}=\{g^i s_+^j s_-^k h_1^\ell: i,j,k,\ell\in\{0,1\}\}
}
\]

with rational functions of the base kinematic variables as coefficients.

Hence

```text
CASE21_CERTIFIED_SEARCH_BOX_ALGEBRAIC_STATE_BOUND = 16
GENERIC_GLOBAL_R10_BRANCH_FREE_STATE_BOUND = 64  # retained outside the certified box
```

The `16` bound does not supersede the generic `64` bound globally; it is a Case21 branch-specific exact reduction.

## 5. Important mathematical classification correction

The first source knot is physically crossed inside the complete halfwave. At `X=Y=pi/2`, the current peak has

```text
lambda_plus(zeta=-1) = -0.08174749432807749 < lambda1
lambda_plus(zeta=+1) = +0.08300094849330153 > lambda1
zeta(lambda_plus=lambda1) ~= +0.600355180536
```

The frozen tensile source is `C2` but not analytic at that knot. In normalized tensile coordinate `z=t/a`, the jumps of derivatives `0,1,2` are exactly zero, while the third derivative jump is

```text
-3.485446758727596
```

and the first truncated-power coefficient is

```text
A3 = -0.580907793121266 != 0.
```

Therefore the physical fixed-endpoint positive-part field is **not one holomorphic algebraic branch across the whole real interval**. The pointwise 16-state algebraic field is glued by the semialgebraic selector `h1=|t_plus-a|`.

The previously selected production representation

```text
GLOBAL_FIXED_ENDPOINT_POSITIVE_PART_FACTORISED_PERIOD
```

is retained, but its precise mathematical class is now

```text
SINGLE_FIXED_DOMAIN_SEMIALGEBRAIC_PERIOD
= positive-part-glued algebraic density over one fixed domain
```

rather than an ordinary single analytic algebraic-period branch.

This is a classification refinement, not a physics-route change.

## 6. One-domain rationalization is exact

For each in-plane coordinate use

\[
r=\frac{\tan(X/2)}{1+\tan(X/2)}\in[0,1],
\qquad
Q(r)=r^2+(1-r)^2.
\]

Then

\[
\sin X=\frac{2r(1-r)}{Q(r)},
\qquad
\cos X=\frac{1-2r}{Q(r)},
\qquad
dX=\frac{2\,dr}{Q(r)}.
\]

Together with `zeta=2w-1`, every Case21 kinematic factor and every T12 weight is rational on a **single fixed unit cube** before the finite algebraic/positive-part source lift.

```text
FORMAL_SPATIAL_SUBDOMAINS = 1 remains exact
NO XY EVENT CELL IS INTRODUCED
```

## 7. Runtime implication

A naive ordinary analytic/Pfaffian propagator for the 16-state basis cannot cross the physical first knot without a gluing rule: differentiating

\[
h_1=\sqrt{(t_+-a)^2}
\]

produces a denominator `1/h1`, while the physical branch switches from `h1=-(t_+-a)` to `h1=+(t_+-a)` at the real knot. This is the exact reason the previous generic `algebraic-period runtime` description was incomplete.

The still-missing production primitive is therefore not a generic 64-state coefficient machine. It is a **non-enumerative fixed-domain semialgebraic-period evaluator** that carries the positive-part gluing without spatial cells/quadrature and returns T12 plus same-source derivatives.

Current status:

```text
CURRENT_END_TO_END_TASK = CASE21_AIRY_SCALAR_FORMAL_ZERO_SPATIAL_ULTIMATE_LOAD
COMPACT_SOURCE_R10 = PASS
T12_CONTRACT = PASS_AUDIT
CASE21_SEARCH_BOX_16_STATE_REDUCTION = PASS_EXACT
SINGLE_FIXED_DOMAIN_SEMIALGEBRAIC_NORMAL_FORM = PASS_EXACT
NONENUMERATIVE_SEMIALGEBRAIC_PERIOD_NUMERIC_RUNTIME = NOT IMPLEMENTED / BLOCKING
FORMAL_CASE21_Rq_RA_L3_SOLVE = NOT RUN
FORMAL_CASE21_Pu = NOT RELEASED
```

## 8. Prohibited regressions remain

```text
NO FORMAL GAUSS/SIMPSON/ADAPTIVE QUADRATURE
NO XY/THICKNESS CELLS OR EVENT SUBDOMAINS
NO MATERIAL-POINT GRID/HISTORY
NO HIGH-ORDER MULTIVARIATE COEFFICIENT ENUMERATION AS PRODUCTION
NO EXPERIMENTAL LOAD CALIBRATION OR ROOT SELECTION
NO NEW PROJECT-LEVEL TASK NAME FOR THIS BLOCKER
```
