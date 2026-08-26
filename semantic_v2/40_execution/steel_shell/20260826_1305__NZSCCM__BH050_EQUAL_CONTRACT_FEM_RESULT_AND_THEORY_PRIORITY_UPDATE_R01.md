# NZ-SCCM — BH050 equal-contract FEM result and theory-priority update R01

**Date:** 2026-08-26

## 1. Equal-contract FEM result

User/Codex reported the completed equal-contract model:

- Job: `BH050_EQUAL_CONTRACT_R02_GRID_B400`
- Step: `EXPLICIT_LOADING`
- peak load: `12.591227 MN`
- peak time: `2.1200006 s`
- peak frame: `212`
- loading-end reaction: `12.582368 MN`
- fixed-end reaction: `12.591227 MN`
- reaction imbalance: about `0.07%`

Quasi-static checks:

- peak `ALLKE/ALLIE = 0.043%`
- max `ALLKE/ALLIE = 0.049%`
- max `ALLVD/ALLIE = 0.886%`

The result is accepted as usable for comparison.

## 2. Comparison

Existing special BH050 comparator:

`Pu_old = 12.2198 MN`

Equal-contract BH050:

`Pu_equal = 12.591227 MN`

Frozen R06 theory:

`Pu_theory = 13.3563763545430 MN`

Thus the equal-contract model increases the FEM peak by about `0.3714 MN`, or about `3.04%` relative to the old special BH050 model.

Using the report convention `(FEM-theory)/theory`, the theory/FEM error changes from about `-8.51%` to `-5.73%`.

Using the more direct theory-over-FEM convention `(theory-FEM)/FEM`, the remaining equal-contract overprediction is about `+6.08%`.

`MODEL_CONTRACT_HYPOTHESIS = PARTIALLY_SUPPORTED`.

## 3. Important theory-priority update

The equal-contract result materially weakens the claim that BH050 is a unique severe-local-buckling outlier requiring an immediate new local-global stability mechanism.

The remaining theory-over-FEM error for BH050 is about `6.08%`, which is of the same order as the already-existing BH010 and BH020 theory overpredictions (roughly 6.5–6.9% in the current seven-case table).

Therefore the residual BH050 gap is no longer uniquely diagnostic of a missing severe-local-buckling coupling mechanism.

Current interpretation:

1. The old `12.2198 MN` comparator was partly depressed by its special model contract.
2. The equal-contract result removes about one third of the old discrepancy.
3. The remaining ~6% difference lies within the same error band already seen in other BH cases that are not local-buckling-first.
4. Consequently, do **not** introduce a new q-U coupled global stability theory solely to fit BH050 at this stage.
5. The previously checked minimal q-U matrix assembled directly from the frozen Airy branch and R02 amplitude equation remains triangular because the global Airy residual has no U-feedback; obtaining a genuine local-global zero would require adding new coupling physics/energy, not merely reassembling existing equations.

## 4. Peak mechanism reported by FEM

At the equal-contract peak:

- max steel-shell Mises: `463.67 MPa`
- max steel-shell PEEQ: `0.12199`
- controlling element: `4940`
- approximate location: `(x,y,z)=(-281.25,-16.84,4650) mm`
- location: lower outer steel shell, near loading end but not on the end GS reaction element
- UHPC `DAMAGEC = 0.1937`
- UHPC `DAMAGET = 0.4926`
- UHPC `SDEG = 0.2907`
- max UHPC PEEQ: `8.84e-4`

The equal-contract peak is therefore a combined steel local-postbuckling plastic development + distributed UHPC damage state, not a pure end-GS failure.

## 5. Current decision

```text
BH050_OLD_SPECIAL_COMPARATOR_EQUAL_CONTRACT = NO
BH050_EQUAL_CONTRACT_Pu = 12.591227 MN
MODEL_CONTRACT_HYPOTHESIS = PARTIALLY_SUPPORTED
BH050_UNIQUE_SEVERE_LOCAL_GLOBAL_GAP = NOT_ESTABLISHED
NEW_qU_COUPLING_THEORY_NOW = HOLD
R06_MODIFICATION_NOW = HOLD
```

The next theory decision should be made from the whole case family, not by continuing to chase BH050 alone.
