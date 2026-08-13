# NZ-SCCM Swartz24 — control-ordering audit refinement after Case1 reconstruction

**Date:** 2026-08-13  
**Time:** TUNK  
**Identity:** CORRECTION OVERLAY TO 16:47 AUDIT / NO THEORY CHANGE

The 16:47 audit was correct to reopen the full same-branch `K_Z=0` versus first-load-maximum ordering before calling all 24 stored load maxima governing capacities.

Its broad statement that the Case1 mechanical objection was "substantively supported" is now narrowed by the subsequent independent reconstruction:

```text
SUPPORTED:
- the current Case1 stored load maximum really worsened from +22.30% to +24.22%;
- the current first-load-maximum state occurs at a slightly smaller D than the old direct-N48 state;
- a local/center R10-faithful tangent proxy is dramatically lower than direct N48;
- therefore the KZ ordering had to be checked rather than assumed.

NOT SUPPORTED BY THE NEW FULL-FIELD AUDIT:
- an earlier complete-halfwave KZ=0 event before the current Case1 load maximum.
```

The audit-reconstructed full-field current KZ is strongly positive at the current load maximum (about +3.07e3 N/mm), and all 15 checked equilibrium states before that maximum also have positive KZ.

The new evidence instead isolates the dominant Case1 load increase to the C1/MM compiler's stress-value shift and re-equilibration:

```text
same old state, direct N48 P        = 599.515895 kN
same old state, current C1/MM P     = 618.677432 kN
value-field shift                   = +19.161537 kN
re-equilibration to current maximum =  -9.751008 kN
net                                 =  +9.410529 kN
```

Formal zero-spatial general-D15 KZ has not yet been regenerated for Case1, so production promotion remains on hold. This refinement changes the diagnosis, not the frozen theory or any stored numerical result.

Governing detailed audit:

`semantic_v2/60_validation/swartz24/20260813_TUNK__NZSCCM__CASE1__COMPILER_VALUE_SHIFT_AND_FULL_FIELD_KZ_RECONSTRUCTION__AUDIT.md`
