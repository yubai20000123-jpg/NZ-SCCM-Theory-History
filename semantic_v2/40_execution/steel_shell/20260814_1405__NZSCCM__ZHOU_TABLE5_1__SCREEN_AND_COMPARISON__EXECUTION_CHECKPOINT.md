# Execution checkpoint — Zhou Table 5.1 source screen and comparator

Date: 2026-08-14 14:05 Asia/Tokyo

## Requested operation

1. Screen Zhou Table 5.1 for a real four-edge simply-supported axial-compression point with `b_s/t_s >= ~56`.
2. If one exists, run the frozen `R10 + exact-D15 + double-shell + Yun-Lu` branch and inspect `B_s -> S1_Yun -> Y_s -> KZ/L`.
3. Repair the missing comparison between the previous NZ-SCCM result and Zhou's formulas.
4. Write the result back to GitHub.

## Source screen result

Zhou Table 5.1 fixes `l_s=200 mm` and `t_s=4 mm` for all four parameter groups. Therefore

```text
b_s/t_s = l_s/t_s = 50
requested threshold ~= 56
match count = 0
```

No legal Table-5.1 source point exists for the requested mechanism screen.

## Execution decision

```text
NEW_TABLE5_1_YUN_RUN = NOT EXECUTED
REASON = EMPTY SOURCE SET
SYNTHETIC ts OR bs = NOT CREATED
FAILURE_TYPE = SOURCE_PARAMETER_SPACE, NOT SOLVER
```

## Repaired Zhou formula comparison

Using Zhou Eq.(3-2)/(3-3) on the exact same user-reduced object previously solved:

```text
b = 6000 mm
h = 130 mm
ts = 4 mm each outer shell
internal web steel bearing term = removed
Ac = 6000*(130-8) = 732000 mm2
As = 2*6000*4 = 48000 mm2
fy = 355 MPa
fcu = 40 MPa
fc' = 0.76*fcu = 30.4 MPa
```

Results:

```text
steel strength contribution = 17.0400 MN
concrete strength contribution = 22.2528 MN
Pyth_reduced_Zhou_Eq3_2 = 39.2928 MN
previous NZ branch peak diagnostic = 26.1085 MN
NZ / Pyth_reduced = 0.6644601556
relative difference = -33.55398444 percent
```

Important identity lock:

- `39.2928 MN` is Zhou's cross-section strength equation replayed on the reduced two-shell object, not the original full multi-cell MCFSTW section.
- `26.1085 MN` is still the preceding diagnostic first-load-maximum neighbourhood, not a final frozen `Rq=0 + L=0` production root.
- Zhou Eq.(5-79) remains the elastic global-stability comparator, but original MCFSTW `Dy/Dxy/Dmu/H` must not be mixed with the reduced object after internal web steel is removed.

## Output files

- `semantic_v2/60_validation/steel_shell/20260814_1405__NZSCCM__ZHOU_TABLE5_1__BS_TS_SCREEN_AND_FORMULA_COMPARISON__VALIDATION.md`
- `semantic_v2/50_results/steel_shell/20260814_1405__NZSCCM__ZHOU_TABLE5_1__SCREEN_AND_FORMULA_COMPARISON__RESULT_TABLE.csv`
- this execution checkpoint

## Next gate

Search a different real source for a concrete-constrained steel subpanel with source-defined geometry satisfying either

```text
b_s/t_s >= ~56   [screen only]
```

or, preferably, directly

```text
sigma_cr,el < fy [actual mechanism gate]
```

Then execute the unchanged analytic branch. No structural calibration is authorized.
