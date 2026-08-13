# NZ-SCCM repository content semantic tree

**Timestamp:** 2026-08-13 13:28 +08:00  
**Mode:** non-destructive content audit / semantic reconstruction  
**Theory/result change:** NONE

## 0. Audit levels

This tree distinguishes three evidence levels rather than pretending every leaf was inferred from its name.

```text
A_DIRECT_CONTENT_AUDIT
  The file body was opened/read in the current repository audit and its role was derived from content + supersession.

B_CONTENT_DERIVED_REGISTRY_OR_LEDGER
  The leaf is classified through a content-derived source registry, inventory, or historical component ledger whose own body was read. This is acceptable for stable source/archive role, but is not a substitute for direct leaf reading when a future technical claim depends on that leaf.

C_NOT_YET_DIRECT_CONTENT_AUDITED
  Path is known from the real repository tree, but no semantic claim beyond locator/family role should be made until its body is read.
```

The objective is to drive `C` toward zero for ambiguous current/governance artifacts. Primary literature/source leaves may remain `B` until a concrete claim requires direct source inspection.

---

# 1. Canonical semantic tree

```text
semantic_v2/
├── 00_index/                       [CURRENT repository navigation/governance]
├── 10_governance/                  [project rules, source-of-truth, recovery, checkpoints]
├── 20_theory/
│   ├── nc_material/                [R10 material target and compiler representation]
│   ├── nc_rebar_panel/             [CH + Nguyen + D15 + P/Rq/L + KZ theory]
│   ├── uhpc_material/              [source-ledger/closure work, not current NC production]
│   └── steel_shell_pbl/            [Yun/Sun/Zhang-derived theory/evidence]
├── 30_workflows/
│   ├── case21/                     [execution contracts, blind-reproduction inputs]
│   └── swartz24/                   [batch-production/recovery workflow]
├── 40_execution/
│   ├── case21/                     [raw input, coefficients, code/checkpoints]
│   └── swartz24/                   [batch checkpoints; current gap for Cases1–18 roots]
├── 50_results/
│   ├── case21/                     [current root/KZ freeze and historical candidates]
│   └── swartz24/                   [current Pu/Pf table and historical direct-N48 tables]
├── 60_validation/
│   ├── swartz24/                   [failure-load comparison and mechanism diagnostics]
│   └── external_rc_panels/         [candidate external validation literature]
├── 70_evidence/
│   ├── nc/
│   ├── uhpc/
│   ├── stability/
│   ├── steel_shell_pbl/
│   ├── mathematics/
│   └── literature/
├── 80_history/
│   ├── case21/
│   ├── d_g_r_routes/
│   ├── ucft/
│   ├── rejected_routes/
│   └── recovery/
└── 90_raw/
    ├── conversation_exports/
    ├── original_source_locators/
    └── preclean_locators/
```

This semantic tree supersedes the assumption that `current/` itself is semantically pure.

---

# 2. Current primary chain — A_DIRECT_CONTENT_AUDIT

## 2.1 Project/current state

Legacy:
`current/CURRENT_STATE.md`

Semantic role:
`PROJECT / CURRENT_STATE_POINTER`

Status:
`CURRENT_PRIMARY`

Important content:
- current Case21 final root/load/residual/KZ state;
- current Swartz24 status;
- still points to the 17:34 theory as primary theory entry, while a later 22:45 production theory/execution contract exists.

Therefore the pointer layer is usable but not fully synchronized with the latest production-contract layer.

## 2.2 Primary NC+rebar production theory/execution contract

Legacy:
`current/theory/NZ_SCCM_NC_REBAR_ZERO_SPATIAL_PRODUCTION_THEORY_CONTRACT_20260812_2245.md`

Canonical content ID:
`20260812_2245__NZSCCM__NC_REBAR_PANEL__R10_N48C1MM_CH_NGUYEN_GENERAL_D15__THEORY_EXECUTION_CONTRACT`

Status:
`CURRENT_PRIMARY`

Content identity:
- explicitly declares `CURRENT PRODUCTION THEORY + EXECUTION CONTRACT`;
- R10 frozen;
- U/C/T7 = N48-C1;
- T = N48-C1 constrained minimax;
- Cayley–Hamilton;
- Nguyen second-order complete halfwave;
- general-D15;
- P/Rq/L and KZ language;
- no structural calibration or formal spatial quadrature.

This is later than the 17:34 baseline and incorporates the successful Swartz24 operational chain plus accepted formal repairs.

## 2.3 Mechanics baseline

Legacy:
`current/theory/NZ_SCCM_NC_REBAR_ZERO_SPATIAL_ANALYTIC_LIMIT_TANGENT_UNIFIED_THEORY_20260812_1734.md`

Canonical content ID:
`20260812_1734__NZSCCM__NC_REBAR_PANEL__R10_N48C1MM_CH_NGUYEN_GENERAL_D15_LIMIT_KZ__THEORY`

Status:
`CURRENT_SUPPORT`

Content identity:
current governing mechanics baseline; incorporated into the later 22:45 production contract.

## 2.4 Formal theory-writing chain

A_DIRECT files:

- `current/theory/NZ_SCCM_NC_R1_FORMAL_CLOSURE_ZHOU_STYLE_20260812.md`
  - earlier formal-closure writing baseline;
  - status `RETAINED_LINEAGE` after canonical formal closure.

- `current/theory/NZ_SCCM_NC_R1_FORMAL_CLOSURE_ZHOU_STYLE_CANONICAL_20260812.md`
  - canonical formal closure;
  - status `CURRENT_SUPPORT`, incorporated by later timestamped unified/production theory.

- `current/theory/NZ_SCCM_NC_R1_ZHOU_STYLE_FORMAL_EQUATION_DERIVATION_20260812.md`
  - formal equation-by-equation derivation;
  - status `CURRENT_SUPPORT` as writing/derivation, not independent production contract.

- `current/theory/NZ_SCCM_R10_N48C1MM_D15_EQUATION_BY_EQUATION_DERIVATION_20260812.md`
  - current equation-by-equation derivation;
  - status `CURRENT_SUPPORT`.

- `current/theory/NZ_SCCM_R10_N48C1MM_D15_PAPER_STYLE_DERIVATION_20260812.md`
  - current paper-style derivation;
  - status `CURRENT_SUPPORT`.

## 2.5 Current compiler decisions

A_DIRECT:

- `governance/N48_C1_VALUE_TANGENT_REPAIR_DECISION_20260811.md`
  - N48-C1 candidate and tangent repair;
  - production was HOLD at that stage;
  - status `RETAINED_LINEAGE`.

- `governance/N48_C1_TENSILE_MINIMAX_BOUNDARY_LAYER_DECISION_20260812.md`
  - freezes U/C/T7=N48-C1 and T=N48-C1 constrained minimax;
  - status `CURRENT_SUPPORT`, incorporated into 22:45 production contract.

- `current/audits/NZ_SCCM_N48_C1_VALUE_TANGENT_REPAIR_AUDIT_20260811.md`
  - diagnostic basis of C1 repair;
  - status `RETAINED_LINEAGE/AUDIT_ONLY`.

- `current/audits/NZ_SCCM_N48_C1_TENSILE_MINIMAX_BOUNDARY_LAYER_AUDIT_20260812.md`
  - companion minimax audit;
  - status `CURRENT_SUPPORT/AUDIT`.

---

# 3. Case21 semantic branch — A_DIRECT_CONTENT_AUDIT

## 3.1 Current execution inputs

`current/case21/NZ_SCCM_CASE21_RAW_INPUT_FREEZE_20260812_1734.md`

Status: `CURRENT_EXECUTION_INPUT`

Contains geometry/material/rebar/q0/compiler interval and source identities.

`current/case21/NZ_SCCM_CASE21_FRESH_MATERIAL_COEFFICIENTS_20260812_1802.csv`

Status: `CURRENT_EXECUTION_INPUT`

Contains 49×4 current material compiler coefficients: U_C1/C_C1/T_MM/T7_C1.

`current/case21/NZ_SCCM_CASE21_NC_R1_FRESH_N48_COEFFICIENTS_20260812.csv`

Status: `SUPERSEDED`

Earlier coefficient set/candidate; not the final 18:02 coefficient freeze.

## 3.2 Current Case21 execution contract

`current/workflows/NZ_SCCM_CASE21_ZERO_SPATIAL_ANALYTIC_EXECUTION_CONTRACT_20260812_1734.md`

Canonical content ID:
`20260812_1734__NZSCCM__CASE21__R10_N48C1MM_GENERAL_D15_LIMIT_KZ__EXECUTION_CONTRACT`

Status: `CURRENT_PRIMARY`

Defines the current Case21 chain including primary branch, first limit candidate and same-branch KZ audit.

Earlier:
`current/workflows/NZ_SCCM_CASE21_NC_R1_FORMAL_CLOSURE_PRODUCTION_CONTRACT_WITH_TANGENT_GATE_20260812.md`

Status: `RETAINED_LINEAGE`; later 17:34 timestamped Case21 contract is primary.

## 3.3 Current Case21 results

`current/results/NZ_SCCM_CASE21_ZERO_SPATIAL_ANALYTIC_THEORY_FREEZE_20260812_1802.md`

Status: `CURRENT_RESULT`

Contains final current theory root/load/residual freeze.

`current/results/NZ_SCCM_CASE21_ZERO_SPATIAL_ANALYTIC_FULL_CLOSURE_20260812_1802.md`

Status: `PARTIALLY_SUPERSEDED`

Valid scope:
- final current root/load/residual;
- KZ decomposition;
- first same-branch KZ zero;
- limit-point vs tangent-control classification.

Superseded scope:
- its final `ultimate` experiment comparison to 336 kN. Later source review establishes that 336 kN is the Swartz/Nguyen buckling/critical load, whereas current ultimate/failure comparison uses Pf≈368.313 kN.

## 3.4 Earlier Case21 candidate lineage

`current/results/NZ_SCCM_CASE21_N48C1MM_D15_FRESH_BLIND_RESULT_20260812.md`
- earlier candidate root/result;
- status `SUPERSEDED`.

`current/results/NZ_SCCM_CASE21_N48C1MM_D15_FRESH_FULL_CALCULATION_20260812.md`
- status `RETAINED_LINEAGE`;
- root/result in the report was later superseded, but the file preserves important backend process: finite coefficient algebra, FFT coefficient convolution, power-to-Chebyshev conversion, D15 exact contraction and directional AD.

`current/results/NZ_SCCM_CASE21_NC_R1_FORMAL_CLOSURE_FRESH_CALCULATION_20260812.md`
- earlier root candidate;
- status `SUPERSEDED` by the general-D15 Qq correction/final branch.

`current/audits/NZ_SCCM_CASE21_TANGENT_GATE_AND_GENERAL_D15_RECHECK_20260812.md`
- status `RETAINED_LINEAGE/AUDIT`;
- documents the general-D15/Qq correction that invalidated the earlier branch.

`current/audits/NZ_SCCM_CASE21_N48C1MM_INDEPENDENT_REPRO_BLOCKED_R10_20260812.md`
- first independent reproduction blocked because the earlier full calculation report was not self-contained at R10;
- status `SUPERSEDED_AUDIT` by the second blank reproduction.

`current/audits/NZ_SCCM_CASE21_V2_SECOND_BLANK_REPRO_STATUS_20260812.md`
- second blank reproduction passed R10/C1/MM/CH/kinematics/D15/steel/Rq/spectral but remained blocked at L/root-definition;
- status `RETAINED_LINEAGE/AUDIT` because later root contract/final closure resolves the production identity.

`current/workflows/NZ_SCCM_CASE21_N48C1MM_D15_SELF_CONTAINED_BLIND_CONTRACT_V2_20260812.md`
- reproduction contract, not current production contract;
- status `RETAINED_LINEAGE`.

`current/workflows/NZ_SCCM_CASE21_N48C1MM_D15_BLIND_AUDIT_INPUT_20260812.md`
- blind audit input; status `RETAINED_LINEAGE`.

## 3.5 Misleading Case21 legacy files still under current/case21

`current/case21/NEXTSTEP_EXECUTION_REPORT.md`
- Aug-09 tail/Chebyshev route report;
- status `SUPERSEDED`.

`current/case21/results_nextstep.json`
- companion old-route result JSON;
- status `SUPERSEDED`.

`current/case21/NZ_SCCM_CASE21_GLOBAL_AUDIT_HANDOFF_20260809.md`
- historical handoff for an older direct-analytic/tail route;
- status `RETAINED_LINEAGE/HISTORICAL`.

## 3.6 Experiment-source identity

`current/case21/NZ_SCCM_CASE21_EXPERIMENT_ONLY_SOURCE_20260812.md`
- labels Nguyen/Swartz 336 kN buckling quantity as an ultimate quantity;
- status `SUPERSEDED/MISLABELLED`.

`current/case21/NZ_SCCM_CASE21_EXPERIMENT_ONLY_SOURCE_20260812_1802.md`
- corrects 336 kN to experimental buckling/critical-load identity and retains raw input provenance;
- status `SOURCE_ONLY` for buckling/critical information, not the final failure-load Pf source.

---

# 4. Swartz24 semantic branch — A_DIRECT_CONTENT_AUDIT

## 4.1 Current final result

`current/results/NZ_SCCM_SWARTZ24_CURRENT_FRESH_PU_FAILURE_COMPARISON_20260813_0047.csv`

Canonical content ID:
`20260813_0047__NZSCCM__SWARTZ24__C1MM_GENERAL_D15_PU_VS_FAILURE_LOAD__RESULT_TABLE`

Status: `CURRENT_RESULT`

Contains current 24/24 Pu and experimental failure Pf comparison. It does not contain Cases1–18 current Du/qu.

`current/results/NZ_SCCM_SWARTZ24_FRESH_PU_COMPLETION_FAILURE_COMPARISON_AND_EXTERNAL_PANEL_SCREEN_20260813_0047.md`

Status: `CURRENT_RESULT/EXECUTION_REPORT`

Contains 24/24 current Pu and current roots for Cases19–24. Does not establish a 24/24 KZ bulk audit.

## 4.2 Superseded direct-N48 table hidden in current/results

`current/results/NZ_SCCM_SWARTZ24_FRESH_BLIND_THEORY_RESULTS_20260811.csv`

Canonical content ID:
`20260811_TUNK__NZSCCM__SWARTZ24__DIRECT_N48_LIMIT_ROOTS_DERIVATIVES_AND_CERTIFICATES__RESULT_TABLE`

Status: `SUPERSEDED`

Despite `current/results` and `FRESH` in its legacy name, its body contains the old direct-N48 roots/results, including Case1 Pu=599.515895 kN. It is not the current C1/MM + general-D15 root table.

`current/results/NZ_SCCM_SWARTZ24_FRESH_THEORY_VS_EXPERIMENT_20260811.csv`
- companion direct-N48 Pu-vs-failure comparison;
- status `SUPERSEDED`.

`current/results/NZ_SCCM_SWARTZ24_FRESH_R10_N48_D15_REPORT_20260811.md`
- direct-N48 production-at-the-time report;
- status `SUPERSEDED`.

## 4.3 Tangent-fidelity correction lineage

`current/results/NZ_SCCM_SWARTZ24_P1_CURRENT_TANGENT_AUDIT_20260811.md`

`current/results/NZ_SCCM_SWARTZ24_P1_CURRENT_TANGENT_AUDIT_COMPACT_20260811.csv`

Status: `RETAINED_LINEAGE/DIAGNOSTIC_ONLY`

The table explicitly contains the old direct-N48 Du/Pu and compares R10-target vs N48 tangent quantities. It is diagnostic evidence for why direct N48 cannot be treated as current tangent-faithful production.

`governance/P1_N48_TANGENT_FIDELITY_DECISION_20260811.md`

Status: `RETAINED_LINEAGE/GOVERNANCE`.

## 4.4 Mechanism diagnostics

`current/results/NZ_SCCM_SWARTZ24_PRIMARY_MECHANISM_AUDIT_20260811.md`

`current/results/NZ_SCCM_SWARTZ24_PRIMARY_MECHANISM_AUDIT_TABLE_20260811.csv`

Status: `PARTIALLY_SUPERSEDED`.

Valid scope:
- digitized source variables / buckling-method flags / historical mechanism exploration.

Superseded scope:
- Pu/error statistics based on old direct-N48 results.

`current/diagnostics/NZ_SCCM_SWARTZ24_SOURCE_OBSERVATIONS_AND_GROUP_ERROR_MECHANISM_20260811.md`

Status: `PARTIALLY_SUPERSEDED`.

Valid scope:
- Nguyen/Swartz source observations on b/t groups, buckling mode and buckling-load interpretation.

Superseded scope:
- numerical group Pu/error statistics built from the old direct-N48 table.

---

# 5. R10 / compiler material lineage — A_DIRECT_CONTENT_AUDIT

`current/theory/NZ_SCCM_R10_1D_ENERGY_SMOOTHING_REINSERTION_CASE21_20260810.md`
- origin of the currently frozen R10 material-target modification;
- status `CURRENT_SUPPORT` for material lineage;
- its structural Gauss calculation is explicitly audit-only and not production.

`current/theory/NZ_SCCM_R10_MATERIAL_TARGET_INTENT_AUDIT_20260811.md`
- clarifies that executed R10 reconstructs the whole retained tensile interval, not merely an infinitesimal local peak patch;
- status `CURRENT_SUPPORT/AUDIT`.

`governance/R10_R10B_IDENTITY_AND_INTERPRETATION_CLARIFICATION_20260811.md`
- separates R10 material-target change from R10B finite analytic representation;
- status `CURRENT_SUPPORT/RETAINED_LINEAGE`.

`current/theory/NZ_SCCM_R10B_COEFFICIENT_GENERATION_CONTRACT_V1_20260811.md`
- old direct-N48 compiler contract;
- status `SUPERSEDED` by C1/MM compiler decisions.

`current/theory/NZ_SCCM_R10B_REPRESENTATION_FIDELITY_AUDIT_20260811.md`
- historical R10B engineering-fidelity/reproducibility audit;
- status `RETAINED_LINEAGE`.

`current/theory/NZ_SCCM_R10B_ZERO_SPATIAL_D15_CASE21_20260811.md`
- direct-N48 Case21 zero-spatial result/derivatives;
- status `SUPERSEDED` as production.

`current/theory/NZ_SCCM_R10_N48_D15_PAPER_STYLE_DERIVATION_20260811.md`
- old direct-N48 derivation;
- status `SUPERSEDED` by 2026-08-12 N48-C1/MM derivations.

---

# 6. Exploratory routes still physically stored under current/theory

These files prove why physical location under `current/` cannot confer current status.

## 6.1 Rejected / superseded production routes — A_DIRECT

- `NZ_SCCM_EXPLICIT_SURFACE_SIMPLIFICATION_AND_CAPACITY_CHAIN_R07R_20260810.md`
  - panel-level/global D-q Chebyshev surface route;
  - `REJECTED` under current `PANEL_LEVEL_SURROGATE=NO`.

- `NZ_SCCM_NC_ENERGY_POTENTIAL_D15_FEASIBILITY_GATE_20260810.md`
  - D15 finite polynomial closure passes but proposed global energy material potential fails;
  - `REJECTED` material route.

- `NZ_SCCM_M1_STRUCTURED_MATRIX_POLYNOMIAL_SCREEN_R01_20260810.md`
  - low-order structured polynomial material screen fails TC interaction;
  - `REJECTED`.

- `NZ_SCCM_M1R_OUTER_RESOLVENT_HYPERELLIPTIC_CLASSIFICATION_R02_20260810.md`
  - hyperelliptic/outer-resolvent classification, no current Pu production closure;
  - `REJECTED` production route.

- `NZ_SCCM_M1R_P2A_INTEGRABILITY_FIRST_PRIMITIVE_SCREEN_20260810.md`
  - integrability screen/HOLD path; later abandoned;
  - `REJECTED` production route.

- `NZ_SCCM_PF1_GENUS2_GAUSS_MANIN_ABSOLUTE_X_CLOSURE_R03_20260810.md`
- `NZ_SCCM_PF1_RELATIVE_X_ENDPOINT_COMPATIBLE_REDUCTION_R04_20260810.md`
- `NZ_SCCM_PF1_RELATIVE_ENDPOINT_HYPERGEOMETRIC_CLOSURE_R04_20260810.md`
- `NZ_SCCM_PF1_HYPERGEOMETRIC_DRIVER_REDUCTION_R05_20260810.md`
- `NZ_SCCM_PF1_ENDPOINT_IBP_MASTER_CONNECTION_R06_20260810.md`

All are analytically interesting PF1 lineage but not current production. Semantic status: `REJECTED/RETAINED_LINEAGE` depending on whether the artifact is used as mathematical history; none is current execution theory.

## 6.2 Retained diagnostic/design lineage — A_DIRECT

- `NZ_SCCM_TARGET_FUNCTION_REBUILD_ANALYTIC_MOMENT_V1_20260810.md`
  - important finite material-moment / analytic material-structure interface design bridge;
  - `RETAINED_LINEAGE`.

- `NZ_SCCM_INVARIANT_COORDINATE_LIFT_EXACT_REDUCTION_R01_20260810.md`
  - invariant-coordinate exact reduction exploration;
  - `RETAINED_LINEAGE`.

- `NZ_SCCM_SPECTRAL_REACHABLE_DOMAIN_REDUCTION_R03_20260810.md`
  - analytical spectral separation/rank diagnostics;
  - `RETAINED_LINEAGE`, not current production-domain contract.

- `NZ_SCCM_TENSILE_CURRENT_MAP_TRANSITION_CORRIDOR_R02_20260810.md`
  - tension-width and reachable-domain diagnostic;
  - `RETAINED_LINEAGE/DIAGNOSTIC_ONLY`.

- `NZ_SCCM_CURRENT_TARGET_GEOMETRIC_REGULARIZATION_R01_20260810.md`
  - material-coordinate geometric regularization diagnostic;
  - `RETAINED_LINEAGE/DIAGNOSTIC_ONLY`.

- `NZ_SCCM_EXACT_RANK4_BRANCH_KERNEL_CLASSIFICATION_R04_20260810.md`
  - exact-kernel classification diagnostic;
  - `RETAINED_LINEAGE/DIAGNOSTIC_ONLY`.

- `NZ_SCCM_MATERIAL_NATIVE_1D_PRIMITIVE_REFORMULATION_R05_20260810.md`
- `NZ_SCCM_NC_POSTPEAK_SCALAR_CLOSURE_AND_D15_PRECHECK_R06_20260810.md`
- `NZ_SCCM_R09A_TENSION_SATURATION_SENSITIVITY_20260810.md`
- `NZ_SCCM_R09B_ENERGY_EQUIVALENT_TENSION_CAPACITY_RULE_20260810.md`

These are retained material-route diagnostics/proposals, not current production contracts.

- `NZ_SCCM_USER_SKETCH_SMOOTH_AND_RC_CASE21_R08_20260810.md`
  - historical user-sketch smoothing plus local D-q surrogate;
  - `REJECTED` as current production.

## 6.3 Code identity examples — A_DIRECT

`current/theory/nz_sccm_case21_invariant_exact_moments_v1.py`
- symbolic I1/I2 and exact monomial-moment audit helper;
- self-declares not production material model or spatial quadrature;
- `CURRENT_SUPPORT/CODE_AUDIT_HELPER`, not the entire general-D15 production backend.

`current/theory/nz_sccm_current_operator_explicit_v1.py`
- explicit algebraic-Foster/current material operator and rebar source helper;
- predates final R10/C1MM production identity;
- `RETAINED_LINEAGE/CODE`.

`current/theory/nz_sccm_current_target_geometric_regularization_r01.py`
- numerical material-coordinate diagnostic code generating geometric-regularization evidence;
- `RETAINED_LINEAGE/DIAGNOSTIC_CODE`.

`current/theory/nz_sccm_frozen_nc_invariant_surface_screen_r01.py`
- explicitly diagnostic-only invariant A/B architecture screen;
- `RETAINED_LINEAGE/DIAGNOSTIC_CODE`.

`current/theory/nz_sccm_invariant_coordinate_lift_r01.py`
- exact symbolic check helper for invariant-coordinate lift;
- `RETAINED_LINEAGE/CODE_AUDIT_HELPER`.

Other companion Python/result JSON files in this family are indexed by their parent route. They must not be promoted merely because they reside in `current/theory`.

---

# 7. Governance semantic branch

## 7.1 Current repository governance — A_DIRECT

- `governance/SOURCE_OF_TRUTH_POLICY.md`
  - `CURRENT_PRIMARY/GOVERNANCE`.

- `governance/RECOVERY_PROTOCOL.md`
  - `CURRENT_PRIMARY/GOVERNANCE`; explicitly requires dynamic repository-tree scan and identity classification.

- `governance/CONTENT_SEMANTIC_IDENTITY_RULE_20260813.md`
  - `CURRENT_PRIMARY/GOVERNANCE`.

- `current/governance/NZ_SCCM_EXECUTION_CHECKPOINT_BACKUP_AUDIT_AND_RULE_20260813_1207.md`
  - `CURRENT_PRIMARY/GOVERNANCE` for resumable checkpoint requirements.

## 7.2 Earlier naming rule

`current/governance/NZ_SCCM_TIMESTAMP_NAMING_AND_BASELINE_DECISION_20260812_1734.md`
- useful earlier decision to prefer descriptive content + timestamp over R/V numbering;
- naming portion is `SUPERSEDED_BY semantic_v2 content-first naming policy` because it does not solve path/name semantic contamination or partial supersession;
- provenance-preservation principle remains valid.

## 7.3 Formal-closure decision

`current/governance/NZ_SCCM_NC_R1_FORMAL_CLOSURE_DECISION_20260812.md`
- status `CURRENT_SUPPORT/GOVERNANCE`, incorporated into later current production contract.

## 7.4 Priority reset

`governance/PRIORITY_RESET_20260810.md`
- status `PARTIALLY_SUPERSEDED/HISTORICAL_GOVERNANCE`;
- retains important history of dropping theorem-level strict remainder as engineering hard gate and material-vs-solution-operator separation;
- its broader long-term material/operator proposals are not the narrow current NC production contract.

---

# 8. Evidence semantic branch

`evidence/catalog/SOURCE_REGISTRY.md` — A_DIRECT registry read.

`evidence/catalog/MASTER_SOURCE_INVENTORY.csv` — A_DIRECT inventory read at registry level.

These establish stable source identities for Nguyen, Attard, Yun, Zhang, Sun, UHPC theses/papers, raw conversation exports and historical machine artifacts.

Source leaves under `evidence/materials`, `evidence/stability`, `evidence/steel_shell`, `evidence/mathematics`, and `evidence/literature` are therefore classified as `B_CONTENT_DERIVED_REGISTRY_OR_LEDGER` unless separately opened. Their role is stable `SOURCE_ONLY`/`SOURCE_EXCERPT`/`SOURCE_MAP`; no current-theory status is inferred from their filenames.

Important rule: when a technical claim depends on a source leaf, that leaf/PDF must still be opened directly.

---

# 9. History semantic branch

`history/README.md` — A_DIRECT.

`history/ledgers/HISTORICAL_COMPONENT_LEDGER.md` — A_DIRECT.

The ledger already classifies D/G/R components by inherited/rejected role, e.g. active D15 mathematical core versus rejected panel-level Chebyshev condensation and historical state-front routes.

Therefore stable history leaves may be indexed at `B_CONTENT_DERIVED_REGISTRY_OR_LEDGER` until a specific recovery question requires direct leaf inspection.

`history/recovery/PRE_CLEAN_REPOSITORY_POINTER.md`
- `LOCATOR_ONLY/RAW_ARCHIVE_RECOVERY`;
- points to pre-clean Git commits where migration-era full-text mirrors/checkpoints/snapshots remain recoverable.

Pre-clean historical assets are not automatically merged back into the active semantic tree; they are restored by content only when a specific missing artifact is being recovered.

---

# 10. Execution-recovery status

The body-level audit supports the following precise statement:

```text
HISTORICAL_CALCULATION_PROCESS = PRESENT
HISTORICAL_BACKEND_STRATEGY = PRESENT
CASE21_CURRENT_RESUMABLE_CHECKPOINT = COMPLETE
SWARTZ24_CURRENT_PU_TABLE = 24/24 PRESENT
SWARTZ24_CURRENT_ROOTS_RETAINED = 6/24 (Cases19–24)
CASES1_18_CURRENT_CORRECTED_Du_qu = NOT_YET_LOCATED
FINAL_AUG12_13_TRANSIENT_BATCH_TOOL_SOURCE = NOT_YET_LOCATED
FULL_24_PANEL_CURRENT_KZ_TABLE = NOT_PRESENT/NOT_COMPLETED
```

`NOT_YET_LOCATED` must not be rewritten as `did not exist`.

---

# 11. Repository cleanliness verdict

```text
LEGACY_CURRENT_DIRECTORY_SEMANTIC_PURITY = FALSE
LEGACY_FILENAME_STATUS_RELIABILITY = FALSE
CONTENT_FIRST_SEMANTIC_INDEX = ACTIVE
CANONICAL_NAMING_POLICY = ACTIVE
DESTRUCTIVE_MIGRATION = NOT_YET_AUTHORIZED
```

The new tree is intentionally non-destructive. A rename map and supersession map accompany this manifest. Physical moves/renames should occur only after the map is content-audited enough to avoid breaking provenance and recovery links.

---

# 12. Remaining audit frontier

The highest-risk ambiguous branches (`current/results`, `current/case21`, current production theory/workflows, compiler chronology, key current diagnostics/governance) have direct-content classifications above.

Remaining direct-leaf work is lower risk and is tracked as either:

- companion JSON/Python of an already content-audited historical route;
- source/evidence leaves whose stable role is supplied by a content-read registry/ledger;
- older history leaves available through the historical component ledger or pre-clean locator.

No unresolved leaf may be used as current production merely because of its path or filename.
