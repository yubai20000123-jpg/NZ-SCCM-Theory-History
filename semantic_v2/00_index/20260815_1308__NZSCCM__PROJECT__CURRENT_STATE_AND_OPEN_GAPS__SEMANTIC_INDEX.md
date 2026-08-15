# CURRENT STATE AND OPEN GAPS — NZ-SCCM

**Timestamp:** 2026-08-15 13:08 +08:00  
**Identity:** CURRENT_PRIMARY / OPERATIONAL ENTRY / GEOMETRY-STABILITY CAUSAL AUDIT COMPLETE  
**Supersedes as operational entry:** `20260815_1233__NZSCCM__PROJECT__CURRENT_STATE_AND_OPEN_GAPS__SEMANTIC_INDEX.md`

---

## 0. Parent theory and comparison identity unchanged

```text
NZ_OBJECT = reduced analytical object; internal steel webs equivalent/absorbed into continuous concrete
ZHOU_OBJECT = original full MCFSTW; internal steel webs retained
ZHOU_FORMULAS = original source formulas
FORMAL_DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
R10 = FROZEN
N48-C1/MM = FROZEN
CAYLEY_HAMILTON = GOVERNING
GENERAL_D15 = GOVERNING
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
STRUCTURAL_CALIBRATION = NO
```

No reduced Zhou rederivation is active.

---

## 1. Current Z0-Z6 comparison retained

```text
Z0 36.619330 vs 36.945541 = -0.883%
Z1 23.190470 vs 23.721432 = -2.238%
Z2 40.208070 vs 41.213379 = -2.439%
Z3 45.022780 vs 44.320271 = +1.585%
Z4 66.886850 vs 70.187272 = -4.702%
Z5 13.177570 vs 14.681648 = -10.245%
Z6 37.509426 vs 49.672436 = -24.486%
```

Z0-Z5 use `A0=a/500 + local progressive radial-cap D32` engineering-diagnostic NZ values; Z6 uses the same current local-cap identity.

---

## 2. Strength-vs-stability decomposition completed

Define

```text
rho_s = Pyth_NZ_reduced / Pyth_Zhou_original
phi_NZ = Pu_NZ / Pyth_NZ_reduced
phi_Z = Pu_Zhou / Pyth_Zhou_original
Pu_NZ/Pu_Zhou = rho_s * (phi_NZ/phi_Z)
```

Key results:

### Z5

```text
strength representation gap = 1.58405 MN
stability/path contribution = -0.07997 MN
phi_NZ/phi_Z = 1.0061
```

Z5 underprediction is essentially the intended web-steel-to-concrete section representation; no Z5 stability deficiency is supported.

### Z4

```text
strength representation gap = 8.81624 MN
NZ higher stability retention offsets 5.51582 MN
phi_NZ/phi_Z = 1.0899
```

Z4's small total error contains substantial cancellation.

### Z6

```text
Pyth_NZ_reduced = 78.5856 MN
Pyth_Zhou_original = 88.089888 MN
phi_NZ = 0.477307
phi_Z = 0.563884
phi_NZ/phi_Z = 0.846463
section-representation part of total gap = 5.35931 MN = 44.1%
additional stability/path part = 6.80370 MN = 55.9%
```

Thus accepting the user's intended internal-web equivalence does not remove Z6. A genuine additional normalized stability/path deficit remains.

Artifacts:

- `semantic_v2/60_validation/steel_shell/20260815_1308__NZSCCM__Z4_Z5_Z6__GEOMETRY_STABILITY_MECHANISM_DECOMPOSITION__AUDIT.md`
- `semantic_v2/50_results/steel_shell/20260815_1308__NZSCCM__Z0_Z6__STRENGTH_VS_STABILITY_DECOMPOSITION__RESULT.csv`

---

## 3. Z4-Z6 controlled-pair diagnosis

Z4 and Z6 share:

```text
fy=355 MPa
fcu=40 MPa
ts=4 mm
ls=200 mm
ls/ts=50
a/b=0.75
```

but global slenderness changes from

```text
Z4: a/h=30.0, b/h=40.0
Z6: a/h=69.23, b/h=92.31
```

Both global ratios increase by about 2.3077.

Normalized retention change:

```text
Zhou: phi 0.8841 -> 0.5639 ; Z6/Z4 = 0.6378
NZ:   phi 0.9636 -> 0.4773 ; Z6/Z4 = 0.4953
relative degradation ratio = 0.7767
```

The NZ path therefore degrades about 22.33% more strongly than Zhou from Z4 to the geometrically similar but much more globally slender Z6.

Local subpanel `ls/ts` is unchanged, so it is not a Z6-unique causal variable.

---

## 4. Finite-amplitude state contrast

Current peak-state amplitude ratios:

```text
Z4: A0/h=0.0600, Ainc/h=0.01881, Atotal/h=0.07881
Z5: A0/h=0.04615, Ainc/h=0.00225, Atotal/h=0.04840
Z6: A0/h=0.13846, Ainc/h=0.54439, Atotal/h=0.68286
```

Z6 is the only case entering a deep finite-amplitude regime.

All-seven normalized-stability sign audit:

```text
phi_NZ/phi_Z:
Z0 1.1110
Z1 1.0563
Z2 1.1140
Z3 1.1071
Z4 1.0899
Z5 1.0061
Z6 0.8465
```

Z6 is the only representative case with normalized NZ stability/path retention below Zhou.

---

## 5. Current decisions

```text
Z5_PRIMARY_GAP = INTENDED SECTION REPRESENTATION
Z5_STABILITY_DEFECT = NOT SUPPORTED
Z4_SMALL_TOTAL_ERROR = PARTLY CANCELLATION
Z6_SECTION_REPRESENTATION_EFFECT = MATERIAL BUT INSUFFICIENT
Z6_ADDITIONAL_STABILITY_PATH_DEFICIT = CONFIRMED
UNIVERSAL_R10_DEFECT = NOT SUPPORTED
LOCAL_ls_over_ts_AS_Z6_UNIQUE_CAUSE = REJECTED
GLOBAL_SLENDERNESS_FINITE_AMPLITUDE_AXIS = PRIMARY ACTIVE CAUSAL TARGET
```

---

## 6. Current next task

```text
CURRENT_NEXT_TASK = Z4_Z6_PAIRED_SAME_BRANCH_KZ_HALFWAVE_AUDIT
```

Required execution:

1. retain current `A0=a/500` and local progressive radial-cap diagnostic;
2. retain internal-web-to-concrete equivalence on NZ side;
3. retain R10/N48/D15 unchanged;
4. evaluate current-tangent Zhou/Navier `KZ` along connected `Rq=0` branches for Z4 and Z6;
5. establish event ordering `yield -> KZ=0 -> load maximum/fold`;
6. independently audit admissible halfwaves for the NZ reduced object without observed-mode or comparator-load selection;
7. determine whether Z6's current `D≈0.705` maximum occurs after an earlier tangent-stability loss or represents path softening with positive stability margin.

Swartz24 full 24-panel same-expression L/KZ remains open/deferred.
