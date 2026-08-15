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
Z6: a/b=0.75 < 1; compression acts along the shorter in-plane dimension
classical plate theory remains valid at a/b=0.75
classical integer optimum remains m=1 for a/b<sqrt(2)
Zhou orthotropic theory also selects m from a lower envelope and does not require a/b>=1
aspect-ratio<1 as sole Z6 cause = REJECTED
squat-panel x high-slenderness interaction = PRIMARY NEW AUDIT TARGET
```

Direct Zhou-source re-read now gives stronger source identity:

```text
Table 5.1 Group 4: ns=10-60, ls=200, h=100-130, a=3000-9000, b=2000-12000
source paragraph: width b is changed and, with b held fixed, height a is changed over 3000-9000; h takes 100 and 130
Z6 exact Group-4 input combination (a,b,h,ns)=(9000,12000,130,60) = STRONGLY SOURCE-SUPPORTED
unique raw FE model ID / individually tabulated raw FE Pu = NOT RECOVERED
49.6724359 MN = Zhou Eq.5-87/5-88 fitted lower-envelope value, NOT raw FE Pu
```

Critical controlled countercheck:

```text
Z4: a=6000, b=8000, h=200, a/b=0.75, NZ error about -4.7%
Z6: a=9000, b=12000, h=130, a/b=0.75, NZ error about -24.5%
```

Therefore `a/b=0.75` alone cannot explain the discrepancy. But Z4 is much less stability-controlled, so an error tied to squat-panel representative-halfwave semantics or nonlinear normalization could be weak in Z4 and strongly amplified in Z6. The diagnostic target is the interaction `a/b<1 + very large a/h,b/h + high normalized slenderness`.

Current causal priorities for Z6:

```text
1. audit ONE_CONTINUOUS_COMPLETE_HALFWAVE semantics and every ell/b normalization in the squat finite-panel regime; do not assume a/b>=1 or ell≈b
2. use Z4 vs Z6 as the same-a/b controlled pair to isolate the role of high slenderness
3. run unchanged-method aspect-ratio neighborhood cases from Zhou Group 4, crossing/approaching a/b=1 where source inputs permit
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

The earlier q31 artifacts remain historical diagnostics only. The current next task is a no-theory-change audit of the squat-panel halfwave/normalization chain followed by an unchanged-method Group-4 aspect-ratio sweep.
