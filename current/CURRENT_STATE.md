# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-15 17:31 +08:00  
**Status:** LEGACY MUTABLE POINTER ONLY

Current Z6 causal correction:

```text
Nguyen second-order kinematics as primary Z6 cause = NOT SUPPORTED
wrong linear m=1 halfwave as primary cause = NOT SUPPORTED
q31 as the cause of the low Z6 Pu = NOT ESTABLISHED
single-q finite-amplitude restriction as an explanation for conservative Pu = RETRACTED
original one-complete-halfwave production baseline = RESTORED
```

New aspect-ratio finding:

```text
Z6: a=9000 mm, b=12000 mm, h=130 mm
Z6: a/b=0.75 < 1; width is larger than wall height/loading length
classical plate theory remains valid at a/b=0.75
classical integer optimum remains m=1 for a/b<sqrt(2)
aspect-ratio<1 as sole Z6 cause = REJECTED
squat-panel / representative-halfwave semantics audit = REQUIRED
exact Zhou FE identity of (a,b,h,ns)=(9000,12000,130,60) = UNRESOLVED
```

Critical controlled countercheck:

```text
Z4: a=6000, b=8000, h=200, a/b=0.75, NZ error about -4.7%
Z6: a=9000, b=12000, h=130, a/b=0.75, NZ error about -24.5%
```

Therefore the ratio `a/b=0.75` by itself cannot explain the discrepancy. What must now be checked is the interaction of the squat-panel geometry with the very high `a/h,b/h` regime and, before that, whether the exact extreme-corner Z6 tuple was actually a literal Zhou FE model rather than a synthetic combination constructed from Table-5.1 ranges.

Current causal priorities for Z6:

```text
1. recover exact Zhou-source FE tuple identity for the constructed Z6 extreme corner
2. audit ONE_CONTINUOUS_COMPLETE_HALFWAVE semantics and all ell/b normalizations in the squat-panel regime; do not assume a/b>=1 or ell≈b
3. use Z4 vs Z6 as the same-a/b controlled pair to isolate absolute slenderness/topology effects
4. discrete internal-web topology vs homogenized/reduced NZ representation at high b/h
5. full incremental ideal-elastoplastic redistribution vs path-independent radial-cap current map
6. concrete current-tangent / geometric-stiffness balance on a valid Z6 branch
7. only if still needed: fully variationally consistent multimode Ritz extension including associated in-plane fields
```

Frozen parent identity remains:

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order
R10 / N48-C1-MM / Cayley-Hamilton / General D15 unchanged
A0 = a/500
formal structural spatial sampling = 0
formal structural quadrature = 0
no Zhou/Winter calibration
```

Current correction/audit artifacts:

- `semantic_v2/10_governance/20260815_1725__Z6_Q31_CAUSAL_RETRACTION_AND_VARIATIONAL_CONSISTENCY__LOCK.md`
- `semantic_v2/60_validation/steel_shell/20260815_1731__NZSCCM__Z6__ASPECT_RATIO_AND_HALFWAVE_IDENTITY__AUDIT.md`

The earlier q31 artifacts remain historical diagnostics only. The new `a/b=0.75` observation is a real geometry/audit gate, but is not yet accepted as the direct cause of the Z6 capacity gap because Z4 has the same aspect ratio and is predicted much better.
