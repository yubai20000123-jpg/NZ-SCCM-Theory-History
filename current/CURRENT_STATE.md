# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-15 12:33 +08:00  
**Status:** LEGACY MUTABLE POINTER ONLY

The operational project entry is now:

`semantic_v2/00_index/20260815_1233__NZSCCM__PROJECT__CURRENT_STATE_AND_OPEN_GAPS__SEMANTIC_INDEX.md`

Current comparison identity:

```text
NZ = reduced analytical object; internal steel webs equivalent/absorbed into concrete
ZHOU = original full MCFSTW; internal steel web topology retained
ZHOU FORMULAS = original source formulas without reduction
D1-R reduced Zhou rederivation = CANCELLED BY USER DIRECTION
```

Latest Zhou-original recalculation artifacts:

- `semantic_v2/10_governance/20260815_1233__NZSCCM_REDUCED_VS_ZHOU_ORIGINAL_FULL__COMPARISON_IDENTITY__LOCK.md`
- `semantic_v2/40_execution/steel_shell/20260815_1233__ZHOU_ORIGINAL_FULL_MCFSTW__Z0_Z6__RECALCULATION_REPORT.md`
- `semantic_v2/40_execution/steel_shell/20260815_1233__ZHOU_ORIGINAL_FULL_MCFSTW__Z0_Z6__PARAMS_AND_INTERMEDIATES.json`
- `semantic_v2/40_execution/steel_shell/20260815_1233__ZHOU_ORIGINAL_FULL_MCFSTW__Z0_Z6__REPRO.py`
- `semantic_v2/50_results/steel_shell/20260815_1233__ZHOU_ORIGINAL_FULL_MCFSTW__Z0_Z6__RESULT.csv`

Current comparison results:

```text
Z0 NZ 36.619330 vs Zhou 36.945541 = -0.883%
Z1 NZ 23.190470 vs Zhou 23.721432 = -2.238%
Z2 NZ 40.208070 vs Zhou 41.213379 = -2.439%
Z3 NZ 45.022780 vs Zhou 44.320271 = +1.585%
Z4 NZ 66.886850 vs Zhou 70.187272 = -4.702%
Z5 NZ 13.177570 vs Zhou 14.681648 = -10.245%
Z6 NZ 37.509426 vs Zhou 49.672436 = -24.486%
MAPE Z0-Z5 = 3.6821%
MAPE Z0-Z6 = 6.6541%
```

Z0-Z4 are all within +/-5%. Z5 is a secondary outlier and Z6 remains the dominant outlier.

`CURRENT_NEXT_TASK = USER_DIRECTED_AFTER_ZHOU_ORIGINAL_Z0_Z6_RECALCULATION`

Swartz24 full 24-panel L/KZ remains open/deferred. No accepted parent R10/N48/D15 theory is changed by this pointer update.
