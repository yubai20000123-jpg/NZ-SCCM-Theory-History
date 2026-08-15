# Z6 aspect-ratio / halfwave identity audit

**Timestamp:** 2026-08-15 17:31 +08:00  
**Identity:** causal audit; no theory modification and no new calibration.

## Trigger

User noticed that the constructed Z6 has width larger than height:

```text
a = 9000 mm   # loading direction / wall height
b = 12000 mm  # transverse wall width
h = 130 mm

a/b = 0.75
b/a = 1.333333...
a/h = 69.23077
b/h = 92.30769
```

This was obscured in earlier discussion by reporting only `a/h` and `b/h`.

## Source facts

1. Zhou's coordinate/layout treats `a` as wall height/loading direction and `b` as wall width; four-edge axial loading is applied at top/bottom.
2. Zhou Table 5.1 Group 4 gives nominal ranges `ns=10–60`, `ls=200 mm`, `h=100–130 mm`, `ts=4 mm`, `fy=355 MPa`, `fcu=40 MPa`, `a=3000–9000 mm`, `b=2000–12000 mm`.
3. The table ranges do NOT by themselves prove that the exact Cartesian corner `(a,b,h,ns)=(9000,12000,130,60)` was a literal FE model.
4. Nguyen explicitly studied simply-supported wall aspect ratios `a/b = 0.5, 0.75, 1.0, ...`; therefore `a/b<1` is not outside the mathematical wall/plate formulation by itself.

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

Therefore:

```text
A/B < 1 => INVALID PLATE THEORY          = FALSE
A/B < 1 => M=1 WRONG                     = FALSE
A/B < 1 => IMPORTANT SQUAT-PANEL REGIME  = TRUE
```

## Controlled-project counterexample

The current Z0–Z6 diagnostic dataset already contains:

```text
Z4: a=6000, b=8000, h=200, a/b=0.75, a/h=30, b/h=40
Z6: a=9000, b=12000, h=130, a/b=0.75, a/h=69.23, b/h=92.31
```

Both have the same `a/b=0.75`. Yet the current NZ diagnostic is close for Z4 (about -4.7% vs Zhou lower envelope) and very low for Z6 (about -24.5%).

Hence `a/b<1` alone cannot explain the Z6 discrepancy.

## What the observation DOES expose

The observation creates two high-priority gates:

### Gate A — exact source-case identity

Before treating Zhou `Pu=49.6724 MN` as the comparator for a literal Z6 specimen/model, recover whether `(9000,12000,130,60)` was actually run as one FE model. Table-5.1 independent ranges are insufficient proof of Cartesian combination identity.

### Gate B — representative-halfwave semantics

`ONE_CONTINUOUS_COMPLETE_HALFWAVE` must be interpreted carefully. For long plates, a repeated full plate mode with `m>1` can be represented by one identical halfwave of length `ell=a/m`. For Z6, `m=1`, so `ell=a=9000 mm<b=12000 mm`: this is the entire squat finite plate, not a repeat-cell abstraction.

The existing reduced kernel does retain `ell` and `b` separately and uses `k=b/ell`, so no algebraic failure is established. Nevertheless all nonlinear `D,q` normalizations and the steel-shell extension must be audited for any hidden assumption inherited from `ell≈b`, `a/b>=1`, or long-wall representative-cell logic.

## Current verdict

```text
Z6 a/b = 0.75 = CONFIRMED
CLASSICAL m=1 FOR a/b=0.75 = CONSISTENT
ASPECT-RATIO<1 AS SOLE CAUSE = REJECTED
SQUAT-PANEL / HALFWAVE-SEMANTICS AUDIT = REQUIRED
EXACT ZHOU Z6 FE TUPLE IDENTITY = UNRESOLVED
Z4 SAME a/b CONTROL = CRITICAL COUNTERCHECK
```

No change is authorized to R10, N48-C1/MM, Cayley–Hamilton, General D15, Nguyen second-order kinematics, current local steel map, `A0=a/500`, or zero formal structural spatial sampling/quadrature.
