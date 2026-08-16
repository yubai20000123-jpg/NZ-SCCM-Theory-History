# NZ-SCCM — Z0–Z5 fixed-N48 representation-capacity audit

**Timestamp:** 2026-08-16 11:34 +08:00

## Audit question

Can the current fixed global degree-48 polynomial space be made materially faithful for Z0–Z5 AR2 simply by changing coefficient generation, while retaining exact R10 C1 anchors and zero structural spatial integration?

## Audit method

For each conservative case interval:

1. solve source-only degree-48 constrained minimax for U,C,T,T7;
2. independently re-evaluate each polynomial on a much finer material-coordinate set;
3. insert the four polynomials into the unchanged R10 spectral master;
4. separately isolate the T contribution by keeping U,C,T7 exact and replacing only T by its value-optimal N48 approximation.

No experiment, Zhou/Winter capacity, structural root or Pu enters coefficient generation.

## Key source-fidelity result

Best found fixed-global-N48 T value errors on conservative intervals:

```text
Z0  .19812
Z1  .12199
Z2  .25816
Z3  .13381
Z4  .17144
Z5  .10580
```

Even on the challenged occupied intervals without conservative margin:

```text
Z0  .12838
Z1  .08945
Z2  .19683
Z3  .09472
Z4  .11875
Z5  .06554
```

Hence the representation issue is not solely the old `[-2.35,+1.90]` hull. The narrow R10 tensile scale remains too sharp relative to a single global degree-48 polynomial over the compression-to-tension range that the stocky panels can visit.

## Current-master audit

Maximum spectral stress-scalar errors after separate value-minimax fitting of all four primitives:

```text
Z0  .21376
Z1  .13061
Z2  .28470
Z3  .14902
Z4  .18634
Z5  .11574
```

The favorable T-only audit, with U/C/T7 kept exact, still produces:

```text
Z0  .19679
Z1  .11953
Z2  .25709
Z3  .13357
Z4  .17040
Z5  .10580
```

Therefore the current-master failure is directly traceable to the fixed-global-N48 representation of T itself.

## Governance verdict

```text
FIXED_N48_ORDER = PASS / RETAINED
R10_PHYSICAL_OPERATOR = PASS / UNCHANGED
EXACT_C1_ANCHORS = PASS
O1_COEFFICIENTS = PASS
SINGLE_GLOBAL_N48_COEFFICIENT_ONLY_VALUE_FIDELITY = FAIL
SINGLE_GLOBAL_N48_CURRENT_MASTER_STRESS_FIDELITY = FAIL
CORRECTED_Z0_Z5_Pu = NOT_AUTHORIZED
```

This audit does not authorize order escalation. It only establishes that the next repair cannot be another weighting/node/objective variation inside the same single-global degree-48 polynomial form.

## Next required gate

`Z0_Z5_AR2_FIXED_N48_MULTISCALE_ANALYTIC_REPRESENTATION_GATE`

The next representation must preserve the degree-48 ceiling while resolving the known R10 tensile scale through analytic factorization/enrichment compatible with Cayley-Hamilton and moment-first D15, without structural spatial quadrature or material-point grids.