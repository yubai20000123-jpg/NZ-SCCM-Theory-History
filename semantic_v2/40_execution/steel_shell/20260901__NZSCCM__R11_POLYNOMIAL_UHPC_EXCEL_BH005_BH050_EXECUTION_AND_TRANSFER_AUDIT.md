# NZ-SCCM — R11 polynomial-UHPC Excel execution + BH005–BH050 rerun + transfer audit

**Date:** 2026-09-01  
**Branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Production main:** unchanged

## 0. Scope

This execution follows the R11 central ledger NEXT-1 -> NEXT-2 sequence without reopening the structural theory.

Implemented UHPC scalar law:

- compression: sixth-degree source-anchored polynomial
- tension: Hiew-anchor cubic-Hermite material-level polynomial pieces
- exact F0/F1 thickness primitives
- same Airy / R02 / R04 / R06 / web / section-closure chain

No Hu incomplete-gamma tension primitive, no R10 UHPC elastic-perfectly-plastic law, no 33-point eta surrogate, no 3x3x3/8-level terminal detour.

## 1. Transfer audit: can a new AI calculate without the old markdown files?

### R11 Excel + complete raw inputs

**YES.** The workbook contains the executable R02/R04/R06 + R11 material + section-closure engine. The old markdown files are provenance, not runtime dependencies. The execution environment must support Excel `PY()` / Python-in-Excel with NumPy/SciPy.

### R11 central ledger only + complete raw inputs

**PARTIAL / NOT GUARANTEED FOR GENERIC R06.** The current R11 ledger contains the complete global/Airy/R02/R04/R11-material/web/closure equations and the generic R06 event definition, but it does not inline every exact local-harmonic stress reconstruction coefficient from the dedicated R06 source document. A new AI can reconstruct the R04 cases directly from the ledger; a byte-for-byte faithful generic R06 implementation is not guaranteed from the ledger alone.

Therefore the safest handoff is:

```text
R11 Excel + R11 central ledger + complete specimen/material inputs
```

If the future goal is a single-text-document handoff with no Excel, the remaining governance task is to inline the full generic R06 reconstruction algebra into the central ledger.

## 2. Current workbook

Generated workbook:

`NZSCCM_钢壳UHPC_R11_六次受压_Hiew三次受拉_BH全算_20260901.xlsx`

SHA-256:

`43f490698638ffec114f109f2f47ccc646182bb1748f91516371a20ae9fc158e`

Workbook additions/repairs:

- `08_R11_MATERIAL`: Ac/Bc/Cc, Hiew source anchors, deterministic Hermite slopes and cubic coefficients, material gates
- `03_ENGINE`: R11 material replacement in the existing parameter-driven solver; no specimen-ID lookup
- `07_REGRESSION`: independent BH005–BH050 raw-input rerun
- `09_BH_RAW_INPUT_R11`: exact raw specimen inputs used
- `10_TRANSFER_CONTRACT`: new-AI standalone transfer boundary

The embedded PY engine was also executed outside Excel through a mock `xl()` reader for the BH050 current input. It reproduced the independent R11 evaluator to machine precision:

```text
q = 0.004930910692159491
P = 13.524781954837966 MN
branch = R06_LOCAL_FIRST
Rmax = 1.265e-12
```

Independent reference:

```text
q = 0.004930910692158645
P = 13.524781954837081 MN
```

Thus the workbook engine logic and the independent evaluator are source-identical for the checked current input.

## 3. BH005–BH050 independent R11 rerun

All cases were recomputed from raw geometry/material inputs. No Hu/FEM/experiment comparator entered the solve or root selection.

| case | branch | q_R11 | P_R11 MN | prior Hu MN | R11-Hu | canonical FEM MN | R11-FEM | Rmax |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| BH005 | R04_YIELD_FIRST | 0.00003199456624236 | 2.48342733101527 | 2.4623346768686 | +0.8566% | 2.3558110 | +5.4171% | 1.19e-10 |
| BH010 | R04_YIELD_FIRST | 0.00012378010854000 | 4.62776917686044 | 4.5834217800205 | +0.9676% | 4.3043290 | +7.5143% | 8.42e-11 |
| BH020 | R04_YIELD_FIRST | 0.00053639192349462 | 8.66628508009364 | 8.5787958279264 | +1.0198% | 8.0079015 | +8.2217% | 2.18e-11 |
| BH032 | R06_LOCAL_FIRST | 0.00141287380194881 | 11.1136415727505 | 10.9405345132294 | +1.5823% | 10.9904800 | +1.1206% | 3.12e-12 |
| BH050 | R06_LOCAL_FIRST | 0.00493091069215865 | 13.5247819548371 | 13.3563763545430 | +1.2609% | 12.5912270 | +7.4143% | 9.09e-13 |

Post-hoc FEM summary:

```text
mean absolute FEM error = 5.9376%
maximum absolute FEM error = 8.2217% (BH020)
```

BH020 is intentionally left visible above 8%; no material/root backfit is made.

## 4. Face-event diagnostics

R11 retains the same mechanical R04/R06 classification:

```text
BH005 -> R04
BH010 -> R04
BH020 -> R04
BH032 -> R06
BH050 -> R06
```

Selected face factors at the R11 terminal:

```text
BH005 upper/lower = 0.5941655808 / 0.4996791876
BH010 upper/lower = 0.6362937817 / 0.4995675310
BH020 upper/lower = 0.7450054886 / 0.4976842788
BH032 upper/lower = 1.0000000000 / 0.4250042880
BH050 upper/lower = 1.0000000000 / 0.3840194772
```

## 5. Current status after NEXT-1 -> NEXT-2

```text
R11_UHPC_POLYNOMIAL_MATERIAL_IMPLEMENTED_IN_EXCEL = PASS
R11_EXACT_F0_F1_IMPLEMENTED = PASS
R11_PARAMETER_DRIVEN_ENGINE = PASS
R11_BH005_BH050_RAW_INPUT_RERUN = PASS
R11_R04_R06_AUTO_SWITCH = PASS
R11_NO_HISTORICAL_RESULT_LOOKUP = PASS
R11_EXCEL_PY_ENGINE_BH050_MOCK_XL_CHECK = PASS
R11_FEM_BACKFIT = ZERO
R11_BH020_WITHIN_8_PERCENT = FAIL_POSTHOC_ONLY
R11_LEDGER_ALONE_GENERIC_R06_STANDALONE = NOT_YET_FULLY_SELF_CONTAINED
```

The next formal solver task, if pursued, remains algebraization of the R06 eta event and the final terminal closure without changing the R11 material or structural equations.
