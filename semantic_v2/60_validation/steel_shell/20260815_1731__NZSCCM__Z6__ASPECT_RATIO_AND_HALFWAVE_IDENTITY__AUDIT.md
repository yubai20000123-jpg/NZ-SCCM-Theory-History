# Z6 aspect-ratio / halfwave identity audit

**Timestamp:** 2026-08-15 17:31 +08:00  
**Revised:** 2026-08-15 after direct Zhou Group-4 source re-read  
**Identity:** causal audit; no theory modification and no calibration.

## Trigger

User noticed that Z6 has width larger than its loaded height:

```text
a = 9000 mm   # loading direction / wall height
b = 12000 mm  # transverse wall width
h = 130 mm

a/b = 0.75
b/a = 1.333333...
a/h = 69.23077
b/h = 92.30769
```

Earlier discussion emphasized `a/h` and `b/h`, obscuring that Z6 is a squat finite plate with compression along the shorter in-plane dimension.

## Direct source facts

1. Zhou's coordinate/layout treats `a` as wall height/loading direction and `b` as wall width; four-edge axial loading is applied at the top/bottom edges.
2. Zhou Table 5.1 Group 4 gives `ns=10–60`, `ls=200 mm`, `h=100–130 mm`, `ts=4 mm`, `fy=355 MPa`, `fcu=40 MPa`, `a=3000–9000 mm`, `b=2000–12000 mm`.
3. More importantly, Zhou's paragraph immediately describing Group 4 states that the wall width `b` is changed and, **with wall width b held fixed, wall height a is changed**, with `a=3000–9000 mm` in 1000-mm increments, `b=2000–12000 mm`, and `h=100,130 mm`. This is strong direct evidence that Group 4 is a crossed width-height parametric sweep, not merely a table of independent marginal ranges.
4. Consequently, `(a,b,h)=(9000,12000,130)` and, because `ls=200`, the corresponding `ns=60`, are strongly supported as an actual Group-4 FE input combination. A unique source model ID and its individually tabulated raw FE ultimate load have still not been recovered.
5. Therefore Zhou `49.6724359 MN` must still be labelled **Eq.5-87/5-88 fitted lower-envelope design-curve value**, not a recovered raw FE load for that individual model.
6. Nguyen explicitly studied simply-supported wall aspect ratios `a/b = 0.5, 0.75, 1.0, ...`; therefore `a/b<1` is not outside the mathematical wall/plate formulation by itself.

## Classical plate check

For a simply supported isotropic plate under uniform compression in the `a` direction with

`w = A sin(pi x/b) sin(m pi y/a)`, `m=1,2,...`,

the dimensionless buckling coefficient is

`k_m = (a/(m b) + m b/a)^2`.

For `a/b=0.75`:

```text
m=1: k = (0.75 + 1/0.75)^2 = 4.34027778
m>=2: larger
```

The integer optimum remains `m=1` because `a/b < sqrt(2)`.

Zhou's orthotropic theory generalizes the geometric ratio through

`beta=(Dx/Dy)^(1/4) * a/b`

and selects the physical integer `m` from the lower envelope of the corresponding buckling-coefficient curves. Hence `a/b<1` does not invalidate Zhou's theory and does not, by itself, make `m=1` wrong.

Therefore:

```text
A/B < 1 => INVALID PLATE THEORY          = FALSE
A/B < 1 => M=1 WRONG                     = FALSE
A/B < 1 => IMPORTANT SQUAT-PANEL REGIME  = TRUE
```

## Controlled-project countercheck

The current Z0–Z6 diagnostic dataset contains:

```text
Z4: a=6000, b=8000, h=200, a/b=0.75, a/h=30, b/h=40
Z6: a=9000, b=12000, h=130, a/b=0.75, a/h=69.23, b/h=92.31
```

Both have exactly the same geometric aspect ratio `a/b=0.75`. Yet the current NZ diagnostic is close for Z4 (about -4.7% vs Zhou lower envelope) and very low for Z6 (about -24.5%).

Hence `a/b<1` alone cannot explain the Z6 discrepancy. However, Z4 is much less stability-controlled while Z6 is deeply stability-controlled, so a squat-panel/half-wave normalization defect could be weak in Z4 and amplified in Z6. The correct diagnostic variable is the interaction

`a/b<1 + very large a/h,b/h + high normalized slenderness`, not `a/b<1` in isolation.

## What the observation exposes

### Gate A — squat finite-panel identity

For Z6, `m=1`, so the complete longitudinal halfwave length is

`ell=a=9000 mm < b=12000 mm`.

This halfwave is the **entire squat finite plate**. It is not a repeat cell extracted from a long plate. Therefore any derivation or normalization that silently relied on `ell≈b`, `a/b>=1`, or a long-wall representative-cell picture must be audited line-by-line.

### Gate B — existing code is not trivially square

The current reduced kernel retains `b` and `ell` separately and uses `k=b/ell`. Thus a simple `a=b` coding mistake is not presently established. The audit must target the nonlinear normalization and residual construction, not assume the failure in advance.

### Gate C — same-a/b controlled pair

Z4 and Z6 must be used as a controlled pair. A correct explanation must account for why the same `a/b=0.75` produces only a small discrepancy at Z4 but a large discrepancy at Z6.

## Current verdict

```text
Z6 a/b = 0.75 = CONFIRMED
Z6 COMPRESSION ALONG SHORTER IN-PLANE DIMENSION = CONFIRMED
CLASSICAL m=1 FOR a/b=0.75 = CONSISTENT
ZHOU ORTHOTROPIC m-SELECTION AT a/b<1 = VALID
ASPECT-RATIO<1 AS SOLE CAUSE = REJECTED
SQUAT-PANEL x HIGH-SLENDERNESS INTERACTION = PRIMARY NEW AUDIT TARGET
Z6 GROUP-4 INPUT COMBINATION = STRONGLY SOURCE-SUPPORTED
Z6 UNIQUE RAW FE MODEL ID / RAW FE Pu = NOT RECOVERED
49.6724 MN = ZHOU FITTED LOWER-ENVELOPE VALUE, NOT RAW FE
Z4 SAME-a/b CONTROL = CRITICAL
```

No change is authorized yet to R10, N48-C1/MM, Cayley–Hamilton, General D15, Nguyen second-order kinematics, current local steel map, `A0=a/500`, or zero formal structural spatial sampling/quadrature.
