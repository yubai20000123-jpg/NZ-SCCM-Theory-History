# NZ-SCCM — RC source-waveform 3-panel current result

**Updated:** 2026-08-22 17:51 +08:00  
**Status:** `SOURCE_WAVEFORM_EXPLICIT_PASS / 1D_CAPACITY_PASS / FULL_2D_SECTION_INTERFACE_INCOMPLETE / MATERIAL_RETUNING_OFF`

Detailed execution:

`semantic_v2/40_execution/20260822_1751__NZSCCM__PANEL1_14_21_SOURCE_WAVEFORM_TO_EXPLICIT_2D_MATERIAL_DIAGNOSTIC.md`

Reproduction:

`semantic_v2/40_execution/rc/20260822_1751__NZSCCM__PANEL1_14_21_SOURCE_WAVEFORM_EXPLICIT_DIAGNOSTIC.py`

|Panel|source-wave Pcr / kN|source-wave 1D Pu / kN|Pf / kN|error|
|---:|---:|---:|---:|---:|
|1|1513.155|676.103|490.194|+37.926%|
|14|2795.789|738.319|716.164|+3.094%|
|21|478.906|327.924|368.313|−10.966%|

The prescribed source waveform exposes transverse and longitudinal bending simultaneously. At the 1D control points:

```text
Panel1  |Mx/My| = 1.643 ; thickness state CC -> TC
Panel14 |Mx/My| = 1.938 ; thickness state CC -> TC
Panel21 |Mx/My| = 0.673 ; thickness state CC -> TC -> TT
```

Therefore the current one-slope TC-R2 section reduction cannot be used to promote a legitimate full-2D waveform-conditioned Pu. The omitted dimension is independent transverse bending curvature, not a missing scalar material coefficient.

Next:

```text
TWO_INDEPENDENT_AFFINE_SLOPE_PHASE_COMPATIBLE_2D_SECTION_RERUN_PANEL1_14_21
```
