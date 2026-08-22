# NZ-SCCM — Steel-shell UHPC 2026-08-21 Summary

**Status:** `SUPERSEDED AS CURRENT RESULT / RETAINED IN GIT HISTORY FOR PROVENANCE`

This file was the 2026-08-21 contract-audited working summary before the 2026-08-22 seven-gate material reorganization and structural rerun.

The current result source is now:

`current/results/NZ_SCCM_POST_7GATE_STRUCTURAL_RERUN_CURRENT_20260822.md`

Full execution report:

`semantic_v2/40_execution/20260822_1315__NZSCCM__POST_7GATE_STRUCTURAL_RERUN_SUHPC_AND_Z_NC_TC_SOURCE_ROLE_AUDIT.md`

The superseded working values included T120 `12.34799984 MN`, T360 `11.29784021 MN`, and the earlier BH pre/post-geometry states. They must not be mixed with the current Zhang-2023/Liu-2024 post-seven-gate table.

Current headline SUHPC values are:

|Case|Current 1D / MN|Current 2D / MN|
|---|---:|---:|
|T120|12.41101|12.22252|
|T360|11.36533|11.36533|
|BH005|2.42351|2.42351|
|BH010|4.46632|4.46632|
|BH020|8.21925|8.21925|
|BH032|11.21046|11.21046|
|BH050|13.67770|12.77154|

```text
HU_WENXU = HISTORICAL_UNIAXIAL_COMPARATOR_ONLY
UHPC_COMPRESSION_BACKBONE = ZHANG_2023
UHPC_TC_CT_CAPACITY = LIU2024_SEQUENTIAL_CONSERVATIVE_ENVELOPE
BH050_OLD_PU_OPEN = CLOSED_UNDER_CURRENT_LIU_CAPACITY_ARCHITECTURE
```
