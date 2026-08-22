# NZ-SCCM — Swartz RC observed-halfwave diagnostic current result

**Updated:** 2026-08-22 16:56 +08:00  
**Status:** `OBSERVED_WAVEFORM_CONDITIONED_1D_EXECUTED / EXPLICIT_METHOD_UNCHANGED / WAVEFORM_CONDITIONED_2D_PENDING`

Detailed execution:

`semantic_v2/40_execution/20260822_1656__NZSCCM__SWARTZ_RC_OBSERVED_HALFWAVE_CONDITIONED_EXPLICIT_RERUN.md`

Reproduction script:

`semantic_v2/40_execution/rc/20260822_1656__NZSCCM__SWARTZ_RC_OBSERVED_HALFWAVE_EXPLICIT_RERUN.py`

## Current source waveform condition

```text
Cases 1-16: one approximate sinusoidal half-wave over a=2440 mm -> ell=2440 mm
Cases 17-24: two sinusoidal half-waves -> representative ell=1220 mm
```

The calculation method is not changed. Only `ell` is imposed for this diagnostic; all dependent `Pcr, C, G, J` are regenerated from the same Marguerre–Airy formulas.

## Selected eight fresh 1D results

|Case|source halfwaves|old auto-m2 1D / kN|observed-wave 1D / kN|Pf / kN|observed-wave error|
|---:|---:|---:|---:|---:|---:|
|1|1|567.7122|689.0551|490.1940|+40.568%|
|2|1|561.6381|673.3721|506.6524|+32.906%|
|9|1|515.4243|584.9057|625.8648|−6.544%|
|10|1|534.7112|602.7616|696.1467|−13.415%|
|19|2|339.1773|339.1773|377.6540|−10.188%|
|20|2|335.0132|335.0132|372.7610|−10.127%|
|21|2|350.4603|350.4603|368.3127|−4.847%|
|22|2|351.6793|351.6793|355.8577|−1.174%|

## Current reading

- Case9/10: source waveform materially improves the previous low bias; error changes from approximately `-17.65/-23.19%` to `-6.54/-13.41%`.
- Case1/2: source waveform increases the 1D load substantially; error becomes `+40.57/+32.91%`. Waveform correction therefore does not substitute for 2D material interaction.
- Case19–22: source waveform already matches the current two-half-wave assumption, so this diagnostic causes no change.

## 2D governance

The old Case1/2 `495.989/501.025 kN` values are **not** reused after changing `ell`; they correspond to the earlier m=2 TC-sensitivity object and are not waveform-conditioned TC-R2 results.

```text
OBSERVED_WAVEFORM_CONDITIONED_2D = PENDING
OLD_M2_2D_VALUE_REUSE = PROHIBITED
NEXT_RC_TASK = WAVEFORM_CONDITIONED_2D_PROPAGATION_THEN_TANGENT_MODE_GATE
```
