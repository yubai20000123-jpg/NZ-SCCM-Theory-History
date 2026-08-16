# Audit — Case21 N48 membrane continuation start

**2026-08-16 22:34 +08:00**

## Scope

Audit of the first executable subgate after reactivating `N48-C1/MM + Cayley-Hamilton + General-D15` for five-term membrane redistribution.

## Source identity

- material coefficient source: `current/case21/NZ_SCCM_CASE21_FRESH_MATERIAL_COEFFICIENTS_20260812_1802.csv`
- governing Case21 execution contract: `current/workflows/NZ_SCCM_CASE21_ZERO_SPATIAL_ANALYTIC_EXECUTION_CONTRACT_20260812_1734.md`
- five-term internal coordinates: `[r0,r20,r22,s02,s22]`
- formal spatial sampling/quadrature: zero

## Fingerprint audit

At the frozen 18:02 `r=0` state, reconstructed values are:

```text
P_repro = 365.58042692483133 kN
P_freeze = 365.58042756532977 kN
Delta P = -6.4049844e-7 kN

D15[Syy]_repro = -13.306145513409462
D15[Syy]_freeze = -13.306145538701315

D15[Qq]_repro = 4.479711739911862
D15[Qq]_freeze = 4.479715227945151

Rqc_repro = 289.26346124101434 kN mm
Rqc_freeze = 289.26368646992213 kN mm
relative component difference ~= 7.8e-7
```

`PASS` for same implementation family. Total `Rq` is deliberately not judged by relative error because it is the cancellation of two approximately 289 kN mm components.

## Direct-old-limit insertion audit

Putting the classical elastic five-term predictor directly at the old 18:02 limit gives

`||Rm||2 = 15.5546386653`.

A diagnostic generalized-coordinate Jacobian has `cond2 ~=714.75` and produces an O(1) full Newton update in `r22/s22`. This is not accepted as a connected-start solution.

Verdict:

`DIRECT_NEAR_LIMIT_INSERTION = REJECTED_AS_START_STRATEGY`.

## Connected-start audit

At

```text
q=1e-4
D=0.016046306
r=[-0.0004765646208971642,
   -0.0002322819318541890,
   +0.0002805628349612065,
   -0.0002432861950486819,
   +0.0003034158793738149]
```

N=28 corrector gives

```text
||Rm||2 = 6.9022384258e-6
Rq = +1.9082556149e-6 kN mm
P = 15.2626325741107 kN
```

The independently used N=20 predictor gives the same accepted state observables to displayed precision; N=28 remains the corrector/acceptance identity.

## Compiler-domain audit

Analytic interval + Gershgorin enclosure, without spatial scanning:

```text
lambda in [-0.02454674538198, +0.00935909011672]
compiler interval = [-1.15,+0.12]
lower margin = 1.12545325461802
upper margin = 0.110640909883278
```

`PASS`.

## Governance audit

```text
R10_CHANGED = NO
N48_MATERIAL_COORDINATE_ROOTS_AS_SPATIAL_POINTS = NO
SPATIAL_GAUSS = 0
SPATIAL_SIMPSON = 0
SPATIAL_ADAPTIVE = 0
SPATIAL_COLLOCATION = 0
MATERIAL_POINT_GRID = 0
EXPERIMENT_IN_SOLVE = NO
NEW_Pu_RELEASED = NO
```

## Verdict

```text
BASELINE_FINGERPRINT = PASS
CONNECTED_CONTINUATION_START = PASS
FIRST_NONZERO_POINT = PASS
FULL_BRANCH = OPEN
SCHUR = OPEN
LIMIT = OPEN
KZ = OPEN
```

Next gate: `CASE21_N48_MEMBRANE_CONNECTED_BRANCH_CONTINUATION_AND_SCHUR_GATE`.