# Z6 aspect-ratio / halfwave / in-plane-boundary audit

**Timestamp:** 2026-08-15 17:31 +08:00  
**Revised:** after direct Zhou boundary-condition and current D-q kinematics comparison  
**Identity:** causal audit; no calibration and no production-theory change yet.

## 1. Trigger geometry

```text
Z6:
a = 9000 mm   # loading direction / wall height
b = 12000 mm  # transverse wall width
h = 130 mm

a/b = 0.75
b/a = 1.333333...
a/h = 69.23077
b/h = 92.30769
```

Z6 is therefore a squat finite plate: compression acts along the shorter in-plane dimension.

## 2. Source identity

Zhou Table 5.1 Group 4 gives `ns=10–60`, `ls=200 mm`, `h=100–130 mm`, `ts=4 mm`, `fy=355 MPa`, `fcu=40 MPa`, `a=3000–9000 mm`, `b=2000–12000 mm`.

The accompanying source paragraph states that wall width `b` is changed and, **with b held fixed, wall height a is changed** over `3000–9000 mm`, with `h=100,130 mm`. Thus `(a,b,h,ns)=(9000,12000,130,60)` is strongly supported as a real Group-4 FE input combination, although a unique source model ID and individually tabulated raw FE ultimate load are not recovered.

`49.6724359 MN` remains the Zhou Eq.5-87/5-88 fitted lower-envelope value, not a recovered raw FE Pu.

## 3. Classical plate / Zhou m check

For a simply supported isotropic plate compressed along `a`,

`w=A sin(pi x/b) sin(m pi y/a)`

and

`k_m=(a/(m b)+m b/a)^2`.

At `a/b=0.75`, `m=1` gives `k=4.34027778` and is the integer minimum. Zhou's orthotropic version uses

`beta=(Dx/Dy)^(1/4)*(a/b)`

and selects integer `m` from the lower envelope. Therefore:

```text
a/b<1 => classical theory invalid = FALSE
a/b<1 => m=1 wrong              = FALSE
a/b<1 => squat-panel regime      = TRUE
```

## 4. Newly identified exact kinematic mismatch

The current reduced NZ D-q field uses, before the finite-amplitude terms,

```text
ex = +nu*D + ...
ey = -D    + ...
gxy = ...
```

At `q=0`, this gives

```text
ex = nu D
ey = -D
gxy = 0
```

For an isotropic plane-stress elastic material,

`sigma_x = E/(1-nu^2)*(ex + nu ey) = 0`.

Hence the current base field encodes a **free transverse Poisson state** throughout the panel.

Zhou's actual four-edge simply-supported FE in-plane boundary conditions are different. On both loaded edges (top and bottom), the transverse displacement is fixed:

```text
u_x = 0 on y=0 and y=a
```

while the two non-loaded side edges leave `u_x` free.

A uniform field with `ex=nu D` corresponds to `u~nu D x` and cannot satisfy `u_x=0` along the entire top and bottom loaded edges. Therefore:

```text
CURRENT NZ PREBUCKLING IN-PLANE FIELD
!=
ZHOU FE IN-PLANE BOUNDARY-ADMISSIBLE FIELD
```

This mismatch is now **confirmed algebraically**, independently of any Pu comparison.

## 5. Why a/b<1 makes this important

For a long wall, the end-restraint disturbance at `y=0,a` can occupy a relatively small fraction of the wall, allowing a large interior region to approach the free-Poisson state `sigma_x≈0`.

For Z6, `a/b=0.75`: the loaded edges are closer together than the transverse width. There is no long-wall interior in the same sense. The two end-restraint fields can influence a much larger fraction of the plate. Thus the approximation `ex=nu D` everywhere is least defensible in precisely this squat-panel regime.

The physical consequences all act in quantities that matter to the current model:

- nonzero transverse membrane stress `sigma_x`;
- biaxial concrete current state and tangent;
- biaxial steel von-Mises utilization / redistribution;
- membrane energy;
- `Dx`, `H`, and geometric-stiffness balance;
- finite-amplitude `Rq(D,q)` and final Pu.

For a fully restrained isotropic plane-stress reference state `ex=0`, the elastic axial tangent changes from `E` to `E/(1-nu^2)`, and `sigma_x=nu sigma_y`; this is only an illustrative upper-bound reference, not the actual Zhou field, because Zhou restrains `u_x` only on the loaded edges and the interior field must be solved continuously.

## 6. Z4 control does not eliminate this mechanism

```text
Z4: a=6000, b=8000, h=200, a/b=0.75, NZ error about -4.7%
Z6: a=9000, b=12000, h=130, a/b=0.75, NZ error about -24.5%
```

Therefore aspect ratio alone is not enough. But Z4 is much stockier / less stability-controlled, whereas Z6 is deeply stability-controlled. A boundary-admissibility error can be weakly visible in a strength-dominated case and become decisive when the ultimate path is governed by membrane/tangent/geometric-stiffness interaction.

Correct diagnostic object:

```text
SQUAT GEOMETRY
x HIGH GLOBAL SLENDERNESS
x WRONG PREBUCKLING IN-PLANE ADMISSIBILITY
```

not simply `a/b<1`.

## 7. Required next test — no theory retuning

Before changing materials, steel map, D15, or adding transverse modes:

1. Replace only the affine/free-Poisson transverse membrane assumption by a boundary-admissible continuous in-plane field satisfying `u(x,0)=u(x,a)=0` and free side-edge traction/displacement conditions consistent with Zhou.
2. Condense the added in-plane amplitude(s) analytically / variationally so formal structural spatial quadrature remains zero.
3. Retain the same out-of-plane `m=1` complete halfwave, same R10/N48-C1-MM/Cayley-Hamilton/General-D15, same steel current law and same imperfection contract.
4. Recompute Z6 first, then Z4 as the controlled same-`a/b` case.
5. If Z6 rises substantially while Z4 changes little, the causal mechanism is confirmed. If not, reject it and continue to the next mechanism.

## 8. Current verdict

```text
Z6 a/b=0.75 = CONFIRMED
m=1 at Z6 = CONSISTENT
EXACT ZHOU GROUP-4 INPUT COMBINATION = STRONGLY SOURCE-SUPPORTED
CURRENT FREE-POISSON BASE FIELD = CONFIRMED
ZHOU LOADED-EDGE ux=0 CONDITION = CONFIRMED
BOUNDARY-KINEMATICS MISMATCH = CONFIRMED
MISMATCH AS FULL EXPLANATION OF -24.5% Pu = NOT YET CONFIRMED
NEXT CAUSAL TEST = BOUNDARY-ADMISSIBLE IN-PLANE FIELD, UNCHANGED MATERIAL/OUT-OF-PLANE THEORY
```
