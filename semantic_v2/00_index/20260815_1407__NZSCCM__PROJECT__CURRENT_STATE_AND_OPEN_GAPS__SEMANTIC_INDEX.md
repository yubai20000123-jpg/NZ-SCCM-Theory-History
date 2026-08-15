# NZ-SCCM project current state and open gaps — semantic index

**Timestamp:** 2026-08-15 14:07 +08:00  
**Status:** CURRENT OPERATIONAL STATE

## 1. Parent production-theory identity remains frozen

```text
FORMAL_DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
GENERALIZED_COORDINATES = D,q
KINEMATICS = NGUYEN_SECOND_ORDER
R10 = FROZEN
N48-C1/MM = FROZEN
CAYLEY_HAMILTON = GOVERNING
GENERAL_D15 = GOVERNING
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
STRUCTURAL_CALIBRATION = NO
```

No parent concrete or structural coefficient was changed in this step.

## 2. H0 homogenized web-steel extension status

The current steel-shell extension diagnostic represents internal webs by a continuous homogenized longitudinal steel phase:

\[
\rho_w=t_s/l_s,
\qquad
A_{w,eq}=\rho_wbt_c=n_st_st_c.
\]

For Z0-Z6, `rho_w=0.02`.

```text
H0_SECTION_MATERIAL_CONSERVATION = PASS
H0_ZERO_STRUCTURAL_DISCRETIZATION = PASS
H0_WEB_STEEL_AREA_IDENTITY = PASS
H0_PRODUCTION_PROMOTION = NO
```

Z0-Z5 same-D `Rq=0` branch relocation is confirmed. Z6 H0 equilibrium remains blocked by the current validated N48 compiler domain; extrapolation and silent domain widening remain prohibited.

## 3. New Zhou comparator semantic correction

The active Zhou side remains the original full MCFSTW topology and original source formulas. However, the role of the axial Eqs. (5-87)-(5-88) result is now explicitly corrected:

```text
ZHOU_EQ_5_87_5_88_ROLE = FE-INFORMED CONSERVATIVE LOWER-ENVELOPE / DESIGN CURVE
ZHOU_RAW_FE_POINT = SEPARATE VALIDATION OBJECT
DESIGN_CURVE_AS_RAW_FE_TRUTH = PROHIBITED
```

The old numerical replay remains valid; only the semantic label changes.

The 2021 Thin-Walled Structures source states that the design curve was established from numerous FE models with `w0=a/500` and conservatively predicts axial ultimate resistance. The dissertation Chapter 5 separately identifies the elastoplastic numerical analysis, Figure 5.8 fitted axial stability curve, and the theory-derived stability curve.

## 4. Current H0 margins relative to the Zhou lower-envelope design curve

For Z0-Z5, these remain same-D `Rq`-located diagnostics, **not final Pu**:

```text
Z0 +10.845%
Z1  +4.874%
Z2  +9.035%
Z3 +11.679%
Z4 +10.130%
Z5  +1.918%
```

These are now interpreted as margins above a conservative design reference, not errors against Zhou FE.

Therefore:

```text
H0_Z0_Z5_TOO_STRONG_CONCLUSION = WITHDRAWN / UNRESOLVED
H0_OVERPREDICTION_AGAINST_ZHOU_FE = NOT ESTABLISHED
H0_VALIDATION_AGAINST_ZHOU_FE = OPEN
```

For Z6, the old fixed H0 state is about 10.401% below the Zhou lower-envelope design value, but it is not a new H0 equilibrium or Pu.

## 5. Raw FE point recovery result

Search/audit performed on:

- Zhou dissertation Chapter 5, especially §5.3.2-§5.3.5, Table 5.1, Figure 5.8;
- primary 2021 Thin-Walled Structures article `10.1016/j.tws.2021.107966`;
- public metadata/full-text availability and supplementary/data discovery paths.

Recovered:

- FE parametric-study identity;
- conservative design-curve identity;
- `w0=a/500` source convention;
- source parameter space and Figure 5.8 identity.

Not recovered:

```text
MODEL-BY-MODEL RAW FE ULTIMATE-RESISTANCE TABLE = NOT FOUND
Z0-Z6 ONE-TO-ONE SOURCE FE MODEL IDS = NOT FOUND
PUBLIC SUPPLEMENTARY PARAMETER-RESULT DATASET = NOT FOUND
ZHOU_RAW_FE_Z0_Z6_NUMERIC VALUES = OPEN
```

Z0-Z6 are project representative parameter tuples, not presumed literal source IDs. Unlabeled nearest-point assignment from Figure 5.8 is prohibited.

## 6. New artifacts

Governance:

- `semantic_v2/10_governance/20260815_1407__ZHOU_FOUR_EDGE_AXIAL__FE_LOWER_ENVELOPE_COMPARATOR_IDENTITY__LOCK.md`

Execution/intermediates:

- `semantic_v2/40_execution/steel_shell/20260815_1407__ZHOU_Z0_Z6__FE_RECOVERY_SEARCH_LEDGER_AND_INTERMEDIATES.json`

Validation:

- `semantic_v2/60_validation/steel_shell/20260815_1407__ZHOU_Z0_Z6__RAW_FE_POINT_RECOVERY_AND_H0_COMPARISON__AUDIT.md`

Result table:

- `semantic_v2/50_results/steel_shell/20260815_1407__ZHOU_Z0_Z6__LOWER_ENVELOPE_VS_H0_AND_FE_RECOVERY_STATUS__RESULT.csv`

## 7. Current open gates and priorities

```text
ZHOU_RAW_FE_CASE-MATCHED_RECOVERY = OPEN / HIGHEST CURRENT VALIDATION PRIORITY
H0_Z0_Z5_FULL_CONNECTED Rq=0 -> L=0 Pu = NOT YET EXECUTED
Z6_H0_MATERIAL_DOMAIN_PREFLIGHT = REAL GATE / TEMPORARILY SUBORDINATE
H0_KZ = NOT YET PROMOTED
SWARTZ24_FULL_24_PANEL_SAME_EXPRESSION_L_KZ = OPEN / DEFERRED
```

No H0 reduction factor, R10 adjustment, N48-order change, imperfection retune, or Zhou-driven calibration is authorized.

## 8. Current next task

```text
CURRENT_NEXT_TASK = ZHOU_FOUR_EDGE_RAW_FE_PRIMARY_DATA_OR_FIG5_8_POINT_MAPPING_RECOVERY
```

Priority order:

1. seek source-identifiable model-by-model FE results or a uniquely mappable Figure-5.8 series;
2. if recovered, execute `Zhou lower envelope <-> NZ-H0 <-> Zhou FE` three-way comparison;
3. then decide whether to proceed with full H0 Z0-Z5 Pu and Z6 material-domain preflight;
4. no theory retuning before this comparator-truth gate is resolved.
