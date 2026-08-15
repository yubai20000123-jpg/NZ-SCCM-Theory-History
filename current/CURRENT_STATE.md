# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-15 13:08 +08:00  
**Status:** LEGACY MUTABLE POINTER ONLY

The operational project entry is now:

`semantic_v2/00_index/20260815_1308__NZSCCM__PROJECT__CURRENT_STATE_AND_OPEN_GAPS__SEMANTIC_INDEX.md`

Current comparison identity remains:

```text
NZ = reduced analytical object; internal steel webs equivalent/absorbed into concrete
ZHOU = original full MCFSTW; internal steel web topology retained
ZHOU FORMULAS = original source formulas without reduction
```

Latest causal audit:

- `semantic_v2/60_validation/steel_shell/20260815_1308__NZSCCM__Z4_Z5_Z6__GEOMETRY_STABILITY_MECHANISM_DECOMPOSITION__AUDIT.md`
- `semantic_v2/50_results/steel_shell/20260815_1308__NZSCCM__Z0_Z6__STRENGTH_VS_STABILITY_DECOMPOSITION__RESULT.csv`

Key decisions:

```text
Z5 gap = essentially intended section-representation effect; no stability deficiency supported
Z4 small total error = partly cancellation between lower reduced section strength and higher NZ stability retention
Z6 total gap decomposition:
  section representation = 5.35931 MN = 44.1%
  additional stability/path deficit = 6.80370 MN = 55.9%
Z4/Z6 controlled pair has same fy,fcu,ts,ls/ts,a/b
Z4 a/h,b/h = 30,40
Z6 a/h,b/h = 69.23,92.31
NZ normalized retention degrades 22.33% more strongly than Zhou from Z4 to Z6
GLOBAL_SLENDERNESS_FINITE_AMPLITUDE_AXIS = PRIMARY ACTIVE CAUSAL TARGET
CURRENT_NEXT_TASK = Z4_Z6_PAIRED_SAME_BRANCH_KZ_HALFWAVE_AUDIT
```

Parent R10/N48/D15 theory is unchanged. Swartz24 full 24-panel same-expression L/KZ remains open/deferred.
