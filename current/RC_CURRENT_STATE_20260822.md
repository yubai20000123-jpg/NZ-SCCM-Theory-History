# RC CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-22 16:56 +08:00

```text
RC_PRIORITY = WAVEFORM / HALFWAVE EFFECT
CURRENT_EXPLICIT_METHOD = UNCHANGED
CASES_1_16_SOURCE_HALFWAVE = ell=2440 mm
CASES_17_24_SOURCE_HALFWAVE = ell=1220 mm
SELECTED_8_OBSERVED_WAVEFORM_1D_RERUN = EXECUTED
WAVEFORM_CONDITIONED_2D_PROPAGATION = PENDING
MATERIAL_RETUNING = OFF
Z6_ACTIVESET_PROOF = DEPRIORITIZED_BY_USER
```

Current execution:

`semantic_v2/40_execution/20260822_1656__NZSCCM__SWARTZ_RC_OBSERVED_HALFWAVE_CONDITIONED_EXPLICIT_RERUN.md`

Current result card:

`current/results/NZ_SCCM_SWARTZ_RC_OBSERVED_HALFWAVE_CURRENT_20260822.md`

## Main result

- Case9/10: imposing the source one-half-wave form changes the current explicit 1D errors from approximately `-17.65/-23.19%` to `-6.54/-13.41%`.
- Case1/2: the same structural change raises 1D errors from approximately `+15.81/+10.85%` to `+40.57/+32.91%`.
- Case19-22: source already has two half-waves, therefore unchanged.

This establishes waveform selection as a major structural variable, but not a universal correction.

The old Case1/2 `495.989/501.025 kN` m=2 TC-sensitivity values are not transferable to the m=1 rerun.

Next RC step: propagate the fixed 2D material constraint through the regenerated m=1 structural demand, then construct a tangent-stiffness mode gate so production does not require experimental waveform input.
