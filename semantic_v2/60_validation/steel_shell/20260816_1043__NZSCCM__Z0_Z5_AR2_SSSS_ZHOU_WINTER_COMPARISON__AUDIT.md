# NZ-SCCM — Z0–Z5 AR2 SSSS / Zhou / Winter comparison audit

**Timestamp:** 2026-08-16 10:43 +08:00  
**Status:** VALIDATION AUDIT

## Audit scope

The calculation reuses the user-accepted Z6 production identity and modifies Z0–Z5 only by enforcing physical `a/b=2`.

```text
BOUNDARY = theoretical four-edge simply supported
m* = 2 for Z0-Z5
ell = a/m* = b
A0 = a/500
q0 = .004
formal spatial sampling = 0
formal spatial quadrature = 0
formal spatial subdomains = 1
```

## Gate results

### Geometry / modal mapping

All cases:

```text
AR2_GEOMETRY = PASS
ZHOU_THEORETICAL_m_STAR = 2
ONE_COMPLETE_HALFWAVE_MAPPING_ell_EQ_b = PASS
```

### Compiler coverage

Declared interval: `[-2.35,+1.90]`.

Final ranges:

```text
Z0 [-1.122437,+.207140]
Z1 [-.748914,+.182632]
Z2 [-1.389472,+.269563]
Z3 [-.848527,+.176233]
Z4 [-1.122763,+.180918]
Z5 [-1.064099,+.074178]
```

```text
CONTINUOUS_COMPILER_DOMAIN_COVERAGE = PASS for Z0-Z5
```

### q-equilibrium component-scale residual

```text
Z0 Rnorm ~ 3.7e-11
Z1 Rnorm ~ 1.1e-9
Z2 Rnorm ~ 8.9e-11
Z3 Rnorm ~ 9.4e-9
Z4 Rnorm ~ 2.0e-8
Z5 Rnorm ~ 4.2e-8
```

All satisfy the frozen `Rnorm <= 1e-5` gate.

### First local + -> - peak

Degree-40 connected-branch neighborhoods show an increasing-to-decreasing change around the retained peak for every case. Degree-48 steel/web cap refinement is then applied at the local peak coordinate and q is re-equilibrated.

```text
FIRST_LOCAL_CAPACITY_PEAK = LOCATED for Z0-Z5
STEEL_WEB_CAP_FINAL_DEGREE = 48
```

## Comparator isolation

Zhou and Winter quantities are evaluated after the NZ-SCCM state is frozen. They do not enter material coefficients, q-equilibrium, branch selection, or peak localization.

```text
ZHOU_CALIBRATION = NO
WINTER_CALIBRATION = NO
COMPARATOR_IN_ROOT_SELECTION = NO
```

## Final comparison

```text
case  NZ-SCCM    Zhou       Winter      NZ-Zhou    NZ-Winter
Z0    33.4910    36.9455    41.5008      -9.35%     -19.30%
Z1    19.7360    23.7214    26.1001     -16.80%     -24.38%
Z2    35.9781    41.2134    45.7333     -12.70%     -21.33%
Z3    39.6889    44.3203    49.0469     -10.45%     -19.08%
Z4    63.7385    69.3399    79.3861      -8.08%     -19.71%
Z5    14.7824    14.6816    14.6816      +0.69%      +0.69%
```

## Mechanical regime audit

For all modified Z0–Z5:

```text
Pcr > Pyth
```

so these AR2 objects reach the material-strength scale before the classical elastic plate critical load. This differs from accepted Z6 AR2, for which `Pcr < Pyth` and postbuckling response remains central.

Therefore comparison of Z0–Z5 against Z6 must distinguish **material-strength-dominated AR2 objects** from the **buckling/postbuckling-dominated Z6 AR2 object**.

## Z5 note

Z5 gives `Pu/Pyth=1.00686`. The +0.69% exceedance is recorded, not tuned away. It may reflect the multiaxial R10 current response plus finite N48 wide-hull representation error. This audit does not authorize any comparator-driven material adjustment.

## Final audit decision

```text
Z0_Z5_AR2_SSSS_CALCULATION = COMPLETE
ZERO_SPATIAL_NUMERICAL_INTEGRATION = PASS
COMPILER_COVERAGE = PASS
RQ_RESIDUAL_GATE = PASS
ZHOU_POSTSOLVE_COMPARISON = COMPLETE
WINTER_POSTSOLVE_COMPARISON = COMPLETE
USER_ACCEPTED_Z6_51_30_MN = RETAINED
```

These results are controlled hypothetical AR2 geometry-adjusted calculations, not direct replicas of the original Zhou specimens at their historical aspect ratios.
