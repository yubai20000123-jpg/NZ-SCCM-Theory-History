# NZ-SCCM Swartz24 prediction-accuracy change root-cause audit

**Time basis:** 2026-08-13 16:27 +08:00  
**Purpose:** identify why later representation/execution changes appeared to reduce prediction accuracy, without recalibrating R10 or using experiment in the solve.

## 1. Compared states

This audit compares two already frozen blind-production states using the same Swartz experimental failure/ultimate loads only after prediction freeze:

1. **Historical direct-N48**: R10 -> direct N48 -> Cayley-Hamilton -> Nguyen -> D15 -> Pu.
2. **Current production**: R10 -> N48-C1 for U/C/T7 + constrained-minimax T -> Cayley-Hamilton -> Nguyen -> general-D15 -> primary-branch first +->- Pu -> same-branch KZ audit.

The current theory body is not modified by this audit.

## 2. Whole-sample accuracy did not materially collapse at direct-N48 -> current

Using the 24 signed percentage errors in the frozen comparison tables:

| metric | old direct-N48 | current C1/MM + general-D15 | change |
|---|---:|---:|---:|
| mean signed error | -3.62397% | -2.81047% | +0.81350 percentage point |
| mean absolute error | 12.05580% | 12.05997% | +0.00417 percentage point |
| RMS percentage error | 13.51808% | 13.52440% | +0.00633 percentage point |
| median absolute error | 12.56597% | 11.78194% | -0.78403 percentage point |
| within 5% | 4/24 | 4/24 | unchanged |
| within 10% | 9/24 | 8/24 | -1 panel |
| within 15% | 16/24 | 17/24 | +1 panel |

Therefore the immediately preceding direct-N48 baseline and the current production baseline have essentially the same whole-24 error magnitude. It is not supported to describe this transition as a large global loss of predictive accuracy.

## 3. The Pu shift is nevertheless systematic, not random

The frozen direct-N48-to-current delta table shows:

- Cases 1-16: every current Pu is higher than direct-N48, mostly by about +0.64% to +2.22%;
- Cases 17-24: every current Pu is lower, by about -0.54% to -1.32%.

Group error changes are correspondingly structured:

| group | old mean signed / MAE | current mean signed / MAE |
|---|---:|---:|
| Cases 1-8 | +4.425% / 12.656% | +6.313% / 13.135% |
| Cases 9-16 | -13.229% / 15.454% | -11.849% / 14.662% |
| Cases 17-24 | -2.068% / 8.058% | -2.896% / 8.383% |

Thus the representation update improves one regime while slightly worsening others. The sign split is evidence of a mechanics/representation-regime effect rather than generic numerical drift.

## 4. First identified mechanics problem in old direct-N48

The 2026-08-11 tangent audit established that old direct-N48 could approximate primitive values reasonably while badly violating the frozen R10 first-derivative identity near lambda=0:

```text
R10 target: T(0)=0, T'(0)=0
old direct N48: T48'(0) approximately +8.689 to +11.364 across the 24 compiler intervals
```

The same audit found old N48 reconstructed the loaded tangent near elastic magnitude and inflated the Zhou-form H contribution by roughly 4.72-6.79 times relative to the R10 target. Therefore old direct-N48 cannot be retained merely because some Pu comparisons happen to be slightly closer to experiment.

## 5. Why C1/MM changes Pu

N48-C1 imposes the exact R10 value/first-derivative anchors while keeping degree 48 and the same finite analytic architecture. The repair passes the tangent/anchor gates, but the degree-48 representation has a real value-fidelity trade-off in the very narrow tensile boundary layer.

The recorded 24-panel mean full-hull maximum primitive errors changed approximately as follows for plain C1:

| primitive | direct N48 | N48-C1 |
|---|---:|---:|
| U | 0.00110 | 0.00124 |
| C | 0.00499 | 0.01252 |
| T | 0.04979 | 0.12215 |
| T7 | 0.11599 | 0.11706 |

The later constrained-minimax T repair reduced mean T full-hull error to about 0.08195 while preserving strict C1, but it still cannot recover the old direct-N48 value-error level at fixed degree 48. This is a documented representation-capacity boundary, not evidence that R10 physical material law itself failed.

Hence the main real source of the systematic current-vs-direct-N48 Pu shift is the **finite material compiler representation change made to restore tangent fidelity**, with an unavoidable value-side perturbation at the chosen degree.

## 6. Case21 isolates where the numerical shift entered

Case21 provides a clean chronology:

```text
old direct-N48 Pu              = 368.189337466 kN
early C1/MM + D15 Pu           = 365.607776 kN
final current Pu               = 365.580427565 kN
```

The total old-to-current change is -2.60891 kN. The direct-N48 -> early C1/MM change is -2.58156 kN, about 98.95% of the final shift. The later corrections alter the result by only about -0.02735 kN.

Therefore, for Case21, general-D15/root/KZ finalization is not the source of the approximately 2.61 kN change; almost all of it entered with the compiler representation transition.

## 7. A separate intermediate execution error did occur and must not be confused with accuracy degradation

One intermediate Case21 formal-closure calculation reported a candidate around 372.775725 kN. The subsequent general-D15 recheck proved that its axial Syy contraction was reproduced but its Qq generalized-work contraction was not. The reported state had a large nonzero canonical general-D15 Rq residual and was therefore not on the governing equilibrium branch.

That 372.775725 kN value is an audit record only, not a production Pu.

A second, independent source of apparent degradation was comparison against **336 kN as if it were experimental ultimate/failure load** in that historical record. Current provenance distinguishes 336 kN as buckling/critical-load evidence and uses about 368.313 kN as Case21 failure/ultimate load for Pu validation. Mixing Pcr and Pf can make a correct/near-correct Pu appear substantially inaccurate without any theory change.

## 8. Current root-cause verdict

```text
LARGE_GLOBAL_ACCURACY_COLLAPSE_DIRECT_N48_TO_CURRENT = NOT_SUPPORTED
SYSTEMATIC_PU_SHIFT = CONFIRMED
PRIMARY_REAL_SHIFT_SOURCE = N48_REPRESENTATION -> STRICT_C1/MM_COMPILER
PHYSICAL_REASON_FOR_REPAIR = DIRECT_N48_FIRST_TANGENT_FIDELITY_FAIL
VALUE_SIDE_COST_OF_REPAIR = CONFIRMED
GENERAL_D15_FINALIZATION_AS_MAIN_CASE21_SHIFT_SOURCE = NO
INTERMEDIATE_GENERAL_D15_QQ_IMPLEMENTATION_MISMATCH = CONFIRMED_AND_SUPERSEDED
Pcr_336_VS_Pf_368p313_IDENTITY_CONFUSION = CONFIRMED_HISTORICAL_APPARENT_ERROR_SOURCE
R10_RECALIBRATION_JUSTIFIED_BY_THIS_AUDIT = NO
STRUCTURAL_Pu_BACKFIT = PROHIBITED
```

## 9. What remains to audit

The user's recollection may refer to an earlier successful stage preceding the 2026-08-11 direct-N48 baseline. Therefore repository recovery should next scan older Swartz24/Case21 prediction tables and compare each theory stage using the same experimental quantity (failure/ultimate for Pu). Only after normalizing the comparison target can an earlier stage be declared genuinely more accurate.

Missing or recomputable historical files are not blockers: record the gap and continue.
