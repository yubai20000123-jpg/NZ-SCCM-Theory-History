# NZ-SCCM Z0–Z5 — historical “no membrane redistribution” result identity audit

**Timestamp:** 2026-08-17 21:30 +08:00  
**Purpose:** retrieve, without reinterpretation, the GitHub values that preceded the membrane-redistribution extension and determine whether they were production ultimate loads.

## 1. Recovered H0 values

Source: `20260815_1336__NZSCCM__Z0_Z6__HOMOGENIZED_WEB_STEEL_PHASE__H0_RESULT.csv`.

|case|historical H0 same-D value / MN|Zhou value then used / MN|H0-Zhou|
|---|---:|---:|---:|
|Z0|40.9523375642|36.9455407965|+10.845%|
|Z1|24.8777133762|23.7214316285|+4.874%|
|Z2|44.9368127931|41.2133789112|+9.035%|
|Z3|49.4964234911|44.3202712875|+11.679%|
|Z4|77.2970838602|70.1872722255|+10.130%|
|Z5|14.9632887860|14.6816480000|+1.918%|

These are the values that generate the remembered “Z0–Z5 are above the Zhou lower envelope” pattern.

## 2. Their actual source identity

The parent H0 execution report explicitly states:

```text
H0 purpose = activate continuous homogenized web-steel phase
Pfixed at old state = not a new equilibrated Pu
same-D q relocation = branch-location diagnostic
same-D values = NOT new Pu
FULL Z0-Z6 WEB-PHASE Pu RECALCULATION = NOT COMPLETE
```

The report states that the degree-10 same-D search was deliberately a branch locator and that `q` was re-equilibrated while `D` remained fixed at the previously persisted old peak `D`.

Therefore:

```text
HISTORICAL_H0_Z0_Z5_VALUES = VALID HISTORICAL DIAGNOSTICS
HISTORICAL_H0_Z0_Z5_VALUES_AS_FINAL_Pu = NOT SOURCE-SUPPORTED
```

This distinction is mandatory in the new Z0–Z5 recalculation. The historical values are called as requested and retained for provenance, but they are not imposed as target ultimate loads and are not used for root selection.

## 3. Consequence for current calculation

The current membrane-OFF baseline must itself be solved from the origin with the latest full-section current operators and the first reachable ultimate point; it cannot be defined by keeping the historical H0 `D_old` fixed.

This is why the current independently solved membrane-OFF results may differ materially from the historical H0 same-D values even before the new membrane redistribution coordinate is activated.

No conclusion about the size of the membrane effect is permitted from `current ON - historical H0`. The only valid membrane delta is

\[
\Delta P_{mem}=P_u^{ON}-P_u^{OFF}
\]

for the exact same specimen/current model/geometry/halfwave, with both OFF and ON solved independently.
