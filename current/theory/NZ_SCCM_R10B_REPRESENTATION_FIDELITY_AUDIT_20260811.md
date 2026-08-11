# NZ-SCCM R10B REPRESENTATION FIDELITY AUDIT

**Date:** 2026-08-11 16:05 +08:00  
**Identity:** CURRENT RECOVERY AUDIT. No material law is changed in this file.

## 1. Object being audited

The frozen executed material target is the existing R10 scalar/current map. The audited transformation is only

```text
frozen R10 material target
-> finite 1D material-coordinate representation
-> same U/C/T + CC/TC/TT algebra
-> finite spatial coefficient representation
-> exact complete-halfwave moment contraction
```

R10B is not allowed to alter R10 material physics.

## 2. Direct historical evidence

The retained original `00_R10B_report.md` records the N=48 material-coordinate errors on the certified safe spectral branches:

| scalar | max abs error | p95 abs error | max error / function scale | p95 / scale |
|---|---:|---:|---:|---:|
| U | 0.000200 | 0.000138 | 0.018198 % | 0.012547 % |
| C | 0.002895 | 0.000712 | 0.289479 % | 0.071158 % |
| T | 0.027887 | 0.006928 | 2.845694 % | 0.706922 % |
| T^7 | 0.027497 | 0.017399 | 3.167978 % | 2.004616 % |

Therefore the historical N48 representation was already highly faithful for U and C, while the positive tensile scalar T and T^7 were the limiting material objects.

## 3. What the historical order study proves

At the same R10 structural audit state, the retained zero-spatial order study changes material and spatial orders together:

| N_M | N_S | P (kN) | R (kN mm) |
|---:|---:|---:|---:|
| 32 | 20 | 366.9675246 | 18.8609835 |
| 40 | 24 | 367.6357111 | 8.2488354 |
| 48 | 28 | 367.8426262 | 6.1492893 |
| 56 | 30 | 368.1017038 | 3.4003506 |
| 64 | 32 | 368.2664235 | 1.8739463 |
| 72 | 34 | 368.3534474 | 1.1915080 |
| 80 | 36 | 368.3983685 | 0.8428271 |
| 96 | 40 | 368.5026604 | 0.1030400 |

A separate N96 equilibrium reclosure at the N48 stationary D gives

```text
P_N96,eq = 368.50804285212683 kN
Delta from N48 stationary result = 0.18849035625 kN = 0.0511757671 %
```

This is strong engineering evidence that the retained finite representation is stable at the structural observable level.

However it is **not** a decomposition of material truncation error versus spatial truncation error, because N_M and N_S were raised simultaneously. It is also not a full N96 stationary-root certificate because D was not reoptimized.

## 4. Exactness boundary

Once a finite material/spatial coefficient representation is fixed, the following operations are exact for that retained representation:

- Cayley-Hamilton pair algebra;
- reconstruction of the same CC/TC/TT interaction;
- coefficient-index convolution;
- complete-halfwave moment contraction;
- same-expression chain-rule derivatives.

Thus the remaining approximation is representation truncation, not spatial quadrature.

## 5. Reproducibility gap

The historical execution package does not retain the actual coefficient arrays or the complete coefficient generator. Original conversation evidence explicitly records that `07_R10B_zero_spatial_compiler_core.py` omitted material coefficient generation and FFT coefficient-convolution plumbing.

Therefore:

```text
HISTORICAL_R10B_MATHEMATICAL_PATH       = PASS
HISTORICAL_R10B_RESULT_RECORD            = PASS
HISTORICAL_R10B_MATERIAL_FIDELITY        = PASS_ENGINEERING
HISTORICAL_R10B_BYTE_REPRODUCIBILITY     = HOLD
HISTORICAL_COEFFICIENT_GENERATOR         = UNRECOVERED
```

No DCT-I, DCT-II, least-squares weighting, or other convention may be retroactively asserted as the exact historical generator.

## 6. Audit decision

```text
R10B_REPRESENTATION_FIDELITY_AUDIT
= PASS_ENGINEERING_WITH_REPRODUCIBILITY_GAP
```

This closes recovery step 2. The next action is recovery step 3 only: freeze a transparent coefficient-generation convention without changing R10 material physics.
