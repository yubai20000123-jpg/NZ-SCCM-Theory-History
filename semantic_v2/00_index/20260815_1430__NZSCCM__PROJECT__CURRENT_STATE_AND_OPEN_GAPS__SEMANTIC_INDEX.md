# NZ-SCCM project current state and open gaps — semantic index

**Timestamp:** 2026-08-15 14:30 +08:00  
**Status:** CURRENT OPERATIONAL STATE

## 1. Parent theory remains frozen

```text
FORMAL_DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
GENERALIZED_COORDINATES = D,q
KINEMATICS = NGUYEN_SECOND_ORDER
R10 = FROZEN
N48-C1/MM = FROZEN
CAYLEY_HAMILTON = GOVERNING
GENERAL_D15 = GOVERNING
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
STRUCTURAL_CALIBRATION = NO
A0 = a/500
```

## 2. Zhou comparison band

User-directed comparison convention:

```text
LOWER = Zhou Eqs. (5-87)-(5-88) FE-informed conservative design/lower-envelope curve
UPPER = Winter curve
RAW FE = optional strengthening evidence if later recovered; not the current blocking task
```

The exact Winter algebraic definition must be stated with any numeric Winter result and is not relabeled as Zhou source data.

## 3. Z6 is the current priority

```text
CURRENT_FOCUS = WHY_Z6_IS_SIGNIFICANTLY_BELOW_ZHOU_LOWER_ENVELOPE
```

Z6 source/replay quantities:

```text
Pyth = 88.089888 MN
Pcr = 42.83147561 MN
lambda_n = 1.434106851
phi_Zhou_lower = 0.563883518
P_Zhou_lower = 49.67243594 MN
```

Using the common Winter slender-branch expression only as a provisional upper-envelope arithmetic convention gives approximately `P_Winter=52.002 MN`.

## 4. What has already been isolated

Old reduced/local-progressive Z6 peak:

```text
P_old = 37.50942609 MN
```

H0 web-steel activation at that same old state:

```text
Pfixed,H0 = 44.50618420 MN
Rq = -1.658145e9 N mm
```

Thus H0 recovers `+6.996758 MN` at the frozen state, closing about 57.5% of the old gap to Zhou lower. Omitted web-steel axial material was therefore a major partial cause.

But the H0 state is not equilibrated. The Z6 `Rq=0` branch is driven to larger q and leaves the current validated N48 concrete compiler domain before a same-D root is found.

## 5. Current causal hierarchy

```text
OLD WEB-STEEL AXIAL MATERIAL OMISSION = MAJOR PARTIAL CAUSE
WHOLE-SHELL FIRST-YIELD CUSP = REAL ARTIFACT, NOT DOMINANT REMAINING GAP
OLD N48 BREADTH SENSITIVITY = MINOR AS LOAD-GAP CAUSE
Z6 GLOBAL SLENDERNESS / FINITE AMPLITUDE = PRIMARY ACTIVE AXIS
H0 LONGITUDINAL WEB MATERIAL WITHOUT FULL ORTHOTROPIC/TOPOLOGICAL RESTRAINT = STRONGEST CURRENT STRUCTURAL HYPOTHESIS
N48 H0 DOMAIN EXHAUSTION = CURRENT COMPUTATIONAL GATE, NOT YET PHYSICAL CAUSE
KZ / HALFWAVE / EVENT ORDERING = OPEN
```

The H0 theory contract itself explicitly states that it restores web material but not periodic faceplate support, cell boundary restraint, or the full original `Dx,Dy,Dxy,Dmu,H` topology.

## 6. Why Z6 is the clean discriminator

Z4 and Z6 share `fy`, `fcu`, `ts`, `ls`, `ls/ts=50` and `a/b=0.75`, while:

```text
Z4 a/h=30.00, b/h=40.00
Z6 a/h=69.23, b/h=92.31
```

Old reduced total amplitude ratio:

```text
Z4 (A0+Ainc)/h ~= 0.0788
Z6 (A0+Ainc)/h ~= 0.6829
```

Z6 is the only representative case whose normalized NZ retention was below Zhou. This points to a deep stability-path softness, not a universal material-strength defect.

## 7. Current next task

```text
CURRENT_NEXT_TASK = Z6_H0_SAME_BRANCH_STABILITY_CAUSAL_DECOMPOSITION
```

Required order:

1. analytic Z6 H0 material-domain preflight, no extrapolation;
2. recover the connected H0 `Rq=0` branch;
3. persist component forces/residuals and current tangents;
4. evaluate same-branch `L` and Zhou/Navier `KZ`;
5. establish `first yield -> KZ=0 -> load maximum/fold` ordering;
6. separate longitudinal web-force benefit from missing orthotropic/tangent restraint;
7. only on evidence decide whether an orthotropic homogenized-web stability extension is required.

No Z6 empirical factor, no R10 refit, no Winter/Zhou calibration, and no observed-mode-guided halfwave selection are authorized.

## 8. New artifacts

- `semantic_v2/10_governance/20260815_1430__ZHOU_WINTER_BRACKET_AND_Z6_CAUSAL_PRIORITY__LOCK.md`
- `semantic_v2/60_validation/steel_shell/20260815_1430__NZSCCM__Z6_BELOW_ZHOU_LOWER_ENVELOPE__CAUSAL_DIAGNOSIS.md`
