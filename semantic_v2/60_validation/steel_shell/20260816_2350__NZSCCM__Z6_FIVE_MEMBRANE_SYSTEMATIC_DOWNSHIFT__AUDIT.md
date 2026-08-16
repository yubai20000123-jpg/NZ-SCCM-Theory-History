# NZ-SCCM — Z6 five-membrane systematic-downshift audit

**Timestamp:** 2026-08-16 23:50 +08:00

## Question

Does the new five-term membrane redistribution merely change Case21, or does it produce a comparable downward capacity shift in a structurally different Z6 plate?

## Controlled comparison

Use the same direct-R10 full-section audit evaluator for both states. Change only whether the five membrane coordinates are fixed to zero or solved from their generalized equilibrium equations.

```text
same material operator = YES
same Z6 geometry = YES
same face steel law = YES
same web/PBL homogenized phase = YES
same numerical audit grid = YES
same Rq equilibrium = YES
only membrane-coordinate release differs = YES
```

Result:

```text
r=0 peak              = 51.480540 MN
five-membrane peak    = 43.762840 MN
relative shift        = -14.9915 %
```

Case21 independently gives:

```text
r=0 -> five-membrane shift = -12.2630 %
```

## Decision

`SYSTEMATIC_DOWNSHIFT_RELATIVE_TO_CONSTRAINED_MEMBRANE_BASELINE = SUPPORTED_BY_TWO_CASES`

This is stronger than a one-case numerical anomaly because the shift persists when the material compiler difference is removed from Z6 by using direct R10 on both sides.

However:

`SYSTEMATIC_UNDERPREDICTION_VS_EXPERIMENT = NOT_YET_PROVEN`

Reason: Case21 has an independent experimental comparator, while the current Z6 branch mainly has Zhou/Winter analytical/design comparators.

## Physical warning

At the Z6 redistributed audit peak:

```text
D ~= 1.1562
s22 ~= +0.6736
r22 ~= +0.3960
r0  ~= -0.3747
r20 ~= -0.3768
```

The internal membrane amplitudes are mechanically large and materially alter the load split:

```text
r=0 peak:
Pc=20.586, Ps=21.877, Pw=9.018 MN

five-membrane peak:
Pc=19.983, Ps=17.393, Pw=6.387 MN
```

The dominant capacity loss is therefore not only a concrete-material effect. The redistribution substantially unloads the face steel and web/PBL axial contribution.

## Required theory audit before further promotion

Do NOT tune the material law to recover the lost capacity. First audit the membrane module itself:

1. derive each of the five coordinates back to its parent in-plane displacement field;
2. verify in-plane boundary admissibility at all four edges under the intended SSSS membrane scope;
3. verify no coordinate duplicates a rigid/free Poisson relaxation already represented by D or the prebuckling field;
4. verify generalized external work terms for loaded-edge displacement control;
5. verify Schur condensation does not treat a load-controlled/global coordinate as a free internal coordinate;
6. only after this audit decide whether all five coordinates remain active.

This is a theory-consistency audit, not response calibration.

## Formal production boundary

The direct-R10 Gauss computation is an oracle only. No new formal Z6 Pu is released. The current family-level zero-integration blocker remains the N3584 structural coefficient-tensor tractability failure. Do not reopen an unbounded backend-development loop.
