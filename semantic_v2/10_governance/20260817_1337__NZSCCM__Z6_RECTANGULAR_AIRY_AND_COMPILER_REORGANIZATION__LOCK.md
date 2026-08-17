# NZ-SCCM — Z6 rectangular Airy and compiler-reorganization lock

**Timestamp:** 2026-08-17 13:37 +08:00  
**Status:** GOVERNANCE LOCK / Z6 FORMAL Pu NOT RELEASED

## 1. User correction recorded

The 2026-08-17 13:37 user correction is controlling:

1. The earlier Case21 N48/CH/D15 path is a **reasoning precedent**, not a command to copy the old compiler literally.
2. The Case21 formal result already obtained may be retained.
3. Z6 is the next diagnostic case.
4. If Z6 shows an obvious discrepancy under direct reuse, the material analytic compiler must be reorganized along a convergent-series / finite-exact-moment route rather than brute-force copying the Case21 fixed-N48 representation.

Therefore:

```text
OLD_PATH_AS_REASONING_PRECEDENT = YES
LITERAL_CASE21_COMPILER_COPY_TO_Z6 = NOT_AUTHORIZED_AS_FINAL_METHOD
Z6_DIAGNOSTIC_BEFORE_BULK = REQUIRED
```

## 2. Real Z6 identity

The current Z6 is the original representative Zhou-Table-5.1 parameter combination:

```text
a = 9000 mm
b = 12000 mm
m* = 1
ell = 9000 mm
k = b/ell = 4/3
h = 130 mm
tc = 122 mm
ts = 4 mm
ns = 60
ls = 200 mm
rho_w = ts/ls = 0.02
fc = 30.4 MPa
eps0 = 0.0018712490394580678
nu_c = 0.18
Es = 206000 MPa
fy = 355 MPa
nu_s = 0.30
A0 = a/500 = 18 mm
q0 = A0/b = 0.0015
```

The later virtual `AR2: a=24000, b=12000, m=2, ell=12000, q0=.004` object is **not** the current Z6 and shall not be substituted for it.

## 3. Rectangular Airy direction — no square-copy shortcut

For `k=b/ell`, the retained scalar membrane correction is

\[
r=\lambda M a(k,\nu),\qquad
M=\frac{\pi^2}{\varepsilon_0}\left(q_0q+\frac12q^2\right),
\]

with

\[
a(k,\nu)=\left[
-\frac{1+\nu k^2}{4},
\frac{\nu k^2-1}{4},
\frac14,
\frac{\nu-k^2}{4},
\frac{k^2}{4}
\right]^T.
\]

This is derived from the rectangular complete-halfwave elastic Airy benchmark. It reduces exactly to the Case21 square direction only when `k=1`.

For real Z6 (`k=4/3`, `nu=.18`):

```text
r0 coefficient  = -0.3300000000000000
r20 coefficient = -0.1700000000000000
r22 coefficient = +0.2500000000000000
s02 coefficient = -0.3994444444444444
s22 coefficient = +0.4444444444444444
shear Airy coefficient = -k/2 = -0.6666666666666666
```

## 4. Direct-R10 mechanics oracle identity

A direct frozen-R10 continuum calculation is permitted only as an external mechanics/compiler audit oracle:

```text
DIRECT_R10_GAUSS = AUDIT_ONLY
FORMAL_SPATIAL_SAMPLING = 0
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_SPATIAL_SUBDOMAINS = 1
FORMAL_THICKNESS_QUADRATURE = 0
```

The current direct-R10 Z6 Airy-scalar audit gives an engineering peak near

```text
D ~= 1.3072
q ~= 0.021443
lambda ~= 0.84614
Pu_direct_R10 ~= 43.46 MN
```

with face-shell local yielding active and the concrete normalized principal material coordinate spanning approximately

```text
[-1.6225, +1.0732].
```

This number is **not** a formal zero-quadrature production Pu.

## 5. Fixed-N48 direct-copy gate — FAIL

The historical Z6 narrow compiler `[-1.15,+0.23]` cannot contain the current Airy branch.

A fixed order N48 compiler regenerated over the previously used broad interval `[-2.35,+1.90]` has large primitive fidelity errors:

```text
U  max value error ~= 0.02625
C  max value error ~= 0.08247
T  max value error ~= 0.71062
T7 max value error ~= 0.79605
T constrained-minimax objective ~= 0.70394
```

At the same direct-R10 peak state, the old CH/D15 architecture with this broad fixed-N48 compiler gives approximately

```text
Pc_full_N48 ~= 18.5008 MN
Pc_full_raw_R10 ~= 20.6509 MN
relative fixed-state concrete difference ~= -10.4 %
```

This is already an obvious compiler-representation discrepancy before solving a new formal Z6 branch.

Therefore:

```text
DIRECT_COPY_FIXED_N48_TO_Z6_WIDE_DOMAIN = FAIL
FORMAL_Z6_Pu_FROM_THIS_COMPILER = PROHIBITED
FAILURE_CLASS = MATERIAL_ANALYTIC_COMPILER_FIDELITY
FAILURE_CLASS != SPATIAL_INTEGRATION
```

No Zhou/reference load is used to make this compiler decision.

## 6. Current next task

The unique next task is

```text
Z6_CONVERGENT_SERIES_FINITE_MOMENT_MATERIAL_COMPILER
```

The compiler shall preserve the frozen R10 physical source and reorganize only its analytic representation:

```text
R10 scalar source
 -> source-consistent convergent scalar series / factorized analytic expansion
 -> termwise 2x2 Cayley-Hamilton lift
 -> target-first exact D15 moments
 -> finite partial sum chosen by source/target convergence, not by observed capacity
```

The key distinction is:

- the **series identity may be infinite and convergent**;
- every retained structural term has a finite exact integral;
- production stops at an engineering-converged partial sum;
- no spatial Gauss/Simpson/cells/collocation/material-point grid is introduced;
- increasing a single global polynomial degree blindly is not the intended solution.

## 7. Comparison discipline

Zhou-original-full Z6 formula result `49.672436 MN` remains a post-solve external fitted-formula comparator, not an experimental truth and not a compiler calibration target.

The direct raw-R10 audit being about 12.5% below Zhou therefore cannot by itself be assigned to compiler error. The compiler error is diagnosed separately by same-state raw-R10 versus formal-representation comparison.
