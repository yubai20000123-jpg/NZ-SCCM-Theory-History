# Z6 original-method causal reset and neighborhood-sweep governance lock

**Timestamp:** 2026-08-15 15:33 +08:00

## Locked correction

The deep-q outer-shell coefficient-composition failure discovered at 15:00 is retained as a real **representation gate**, but it is not promoted to a physical explanation for the Z6 capacity discrepancy and it is not evidence that the original NZ-SCCM method is wrong.

The source audit establishes:

```text
Z6_OUTSIDE_ZHOU_NOMINAL_TABLE5_1_RANGE = NO
Z6_AT_ZHOU_GROUP4_EXTREME_CORNER = YES
Z6_ONLY_CURRENT_REPRESENTATIVE_WITH_LAMBDA_N_GT_1 = YES
ZHOU_49P6724_IDENTITY = FE_INFORMED_LOWER_ENVELOPE_DESIGN_VALUE
ZHOU_Z6_NEIGHBORHOOD_RESPONSE = SMOOTH
ORIGINAL_NZ_METHOD_AS_ROOT_CAUSE = NOT ESTABLISHED
```

Zhou Table 5.1 Group 4 nominally includes `ns=10–60`, `ls=200`, `h=100–130`, `ts=4`, `fy=355`, `fcu=40`, `a=3000–9000`, `b=2000–12000`. Z6 is exactly at the upper corner `ns=60,h=130,a=9000,b=12000`.

Zhou Eqs. (5-87)/(5-88) are a Perry-Robertson lower-envelope fit to the FE cloud; Winter is approximately the upper envelope for `lambda_n >= 1`. Therefore the current Zhou comparator is not to be relabelled as a literal raw FE capacity for a specimen called Z6.

## Frozen next test

Before changing any material, shell, compiler or imperfection rule, execute the **unchanged NZ-SCCM method** on this neighborhood:

```text
S0: a=9000, b=12000, h=130, ns=60
S1: a=8000, b=12000, h=130, ns=60
S2: a=9000, b=10000, h=130, ns=50
S3: a=8000, b=10000, h=130, ns=50
S4: a=8550, b=11400, h=130, ns=57
```

All keep `ls=200, ts=4, fy=355, fcu=40`.

Frozen NZ identity:

```text
R10 = unchanged
N48-C1/MM = unchanged
Cayley-Hamilton = unchanged
General D15 = unchanged
Nguyen second-order kinematics = unchanged
local progressive radial-cap outer shell current-map = unchanged
A0 = a/500
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
Zhou/Winter values = comparison only after NZ result freeze
```

## Interpretation gate

- If a small move away from Z6 causes the unchanged NZ prediction to recover sharply while Zhou changes smoothly, audit NZ branch/halfwave/deep-amplitude representation.
- If NZ underprediction persists smoothly across S0–S4, prioritize a high-slenderness finite-amplitude reserve missing from the current reduced generalized-coordinate representation.
- Do not use the shell compiler failure itself as the physical cause.
- Do not fit an empirical Z6 factor.
- Do not change R10/N48 order or material parameters to force agreement.

```text
CURRENT_NEXT_TASK = Z6_UNCHANGED_NZ_METHOD_NEIGHBORHOOD_SWEEP
```
