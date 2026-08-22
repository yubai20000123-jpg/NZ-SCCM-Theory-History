# NZ-SCCM — Post-7Gate Structural Rerun Current Summary

**Date:** 2026-08-22  
**Status:** `CURRENT WORKING RESULTS / SUHPC RESOLVED / Z POSTCRACK ULTIMATE OPEN`

Governing execution report:

`semantic_v2/40_execution/20260822_1315__NZSCCM__POST_7GATE_STRUCTURAL_RERUN_SUHPC_AND_Z_NC_TC_SOURCE_ROLE_AUDIT.md`

Reproduction kernel for Z source transitions:

`semantic_v2/40_execution/steel_shell/20260822_1315__NZSCCM__Z0_Z6_NC_TC_SOURCE_TRANSITION_REPRO.py`

## 1. SUHPC current post-7gate results

| Case | Zhang 1D / MN | Current 2D / MN | status |
|---|---:|---:|---|
|T120|12.41101|12.22252|Liu TC active / finite re-cut|
|T360|11.36533|11.36533|2D gate inactive at 1D root|
|BH005|2.42351|2.42351|2D gate inactive|
|BH010|4.46632|4.46632|2D gate inactive|
|BH020|8.21925|8.21925|2D gate inactive|
|BH032|11.21046|11.21046|2D gate inactive|
|BH050|13.67770|12.77154|Liu TC active / finite re-cut|

```text
UHPC_COMPRESSION_BACKBONE = ZHANG_2023
UHPC_TC_CT_CAPACITY = LIU2024_SEQUENTIAL_CONSERVATIVE_ENVELOPE
BH050_OLD_PU_OPEN = CLOSED_UNDER_CURRENT_LIU_CAPACITY_ARCHITECTURE
```

## 2. Z0-Z6 current NC source-transition results

|Case|q_TC|P_TC-transition / MN|segment|status|
|---|---:|---:|---|---|
|Z0|0.002007624998|27.033151885|B|TC cracking/state transition|
|Z1|0.002653115864|17.093528920|B|TC cracking/state transition|
|Z2|0.002007624998|27.033151885|B|TC cracking/state transition|
|Z3|0.003023358231|36.744639968|B|TC cracking/state transition|
|Z4|0.001755102366|56.203522296|A|TC cracking/state transition|
|Z5|0.000194052923|10.747333454|A|TC cracking/state transition|
|Z6|0.004014855283|23.832330467|B|TC cracking/state transition|

These are **not final ultimate loads**. Nguyen Eqs. (3.18)-(3.19) are the TC failure/state-transition envelope; after breach the source enters cracked constitutive continuation. The current history-free stripped explicit mainline does not yet have a source-closed finite post-crack continuation for steel-shell NC.

Therefore:

```text
Z0_Z6_NC_TC_TRANSITION = SOLVED
Z0_Z6_FINAL_POSTCRACK_2D_PU = OPEN
TC_FULL_FAILURE_ENVELOPE_AS_SC_ULTIMATE_HARD_CAP = REJECTED
OLD_Z6_51_345 = SUPERSEDED_BY_CURRENT_NC_SOURCE_ROLE
```

The later Z6 mathematical A-segment intersection near `48.63 MN` is diagnostic only and is not selected as Pu.

## 3. Formal execution flags

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_material_points = 0
RITZ_ORDER = NONE
LOAD_PATH_TRACKING = 0
HISTORY_STATE_MACHINE = OFF_MAINLINE
EXPERIMENT_IN_ROOT_SELECTION = 0
FEM_IN_ROOT_SELECTION = 0
STRUCTURAL_BACKBONE_CHANGED = FALSE
```
