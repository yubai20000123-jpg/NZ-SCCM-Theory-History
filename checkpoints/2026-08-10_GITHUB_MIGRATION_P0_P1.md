# Checkpoint — GitHub evidence migration P0/P1

**Date:** 2026-08-10

## P0 status — substantially closed

Repository now has the recovery skeleton required for a new conversation:

- `START_HERE.md`;
- `SOURCE_OF_TRUTH_POLICY.md`;
- `RECOVERY_PROTOCOL.md`;
- `SYNC_PROTOCOL.md`;
- `CURRENT_STATE.md`;
- 89-row first-pass `evidence/MASTER_SOURCE_INVENTORY.csv`;
- current NC/rebar benchmark contract + executable helper;
- 2026-08-10 priority-reset governance;
- TURN 0001–0148 original-chat locator and the G15/R04/R05/D4–D20 recovery locators;
- R2 full-context recovery snapshot files;
- current Case21 global-audit/next-step state;
- Path-A / UCFT Layer-0 / v5 historical locators and source boundaries.

## P1 exact/complete text copies now archived

### D-series / R-series

- `history/D_series/BASELINE_GATE_STATUS.json`
- `history/D_series/D12/D12_CANDIDATE_GATE_SUMMARY.csv`
- `history/D_series/D15/NZ_SCCM_DAEM_v0.5_D15_精确矩生成与UHPC解析矩公式报告.md`
- `history/D_series/D15/D15_UHPC_SOURCE_CONSTRAINT_REGISTRY.csv`
- `history/D_series/D15R/D15R_HISTORY_EQUIVALENCE_REPORT.md`
- `history/D_series/D15R/D15R_V054_HAND_CALC.md`
- `history/D_series/D19/D19_TEST_LOG.txt`
- `history/D_series/D19R/D19R_V052_EXECUTION_REPORT.md`
- `history/D_series/D19R/D19R_ZERO_QUADRATURE_FEASIBILITY_DECISION.md`
- `history/D_series/D19R/D19R_FROZEN_MATERIAL_INTEGRABILITY_AUDIT.csv`
- `history/D_series/D19R/NZ_SCCM_ANALYTICAL_MATRIX_v0.5.1_D19R_M1_ROLLBACK_REPORT.md`
- `history/R_series/R19/equation_to_code_registry_R19.csv`

These preserve both positive results and blockers. In particular: D19R is not allowed to be rewritten as a fully zero-quadrature matrix; R19 keeps the unconstrained multi-DOF source-active arc gate OPEN; D15R preserves the 155-vs-156 provenance issue rather than forcing reconciliation.

### Material recovery / historical governance

- `history/material_recovery/MATERIAL_RECOVERY_EXECUTION_REPORT.md`
- `history/material_recovery/MATERIAL_COMPONENT_RECOVERY_LEDGER.csv`
- `history/HISTORICAL_COMPONENT_LEDGER.md`
- G16R, UHPC state-equation ledger, D19 Liu-TC closure matrix and historical UHPC-C0 contract

### G-series

- `history/G_series/G20/NZ_SCCM_G20_C1平滑强度域_UHPC应变硬化闭合_NC开裂轴正则化报告.md`
- `history/G_series/G21/07_G21_gate_decision.json`
- `history/G_series/G22/NZ_SCCM_G22_FINAL_普通混凝土全局多项式PASS报告.md`

These are retained as historical evidence. Their PASS/HOLD labels do not silently override the later explicit-current-operator/direct-analytic/single-domain/2026-08-10 priority-reset governance.

### Case21 analytical-route history

- one-shot direct-analytic report + complete SymPy source;
- multi-backend direct-analytic result;
- material-compiler R5 report;
- common-policy R2 report;
- analytic-spatial-subdivision revocation notice;
- global one-domain handoff + `NEXTSTEP_EXECUTION_REPORT.md` + `results_nextstep.json`;
- nested-D15 and G31 provenance locators.

The archived local original of `NZ_SCCM_CASE21_MULTI_BACKEND_DIRECT_ANALYTIC_RESULT(1).md` had SHA-256:

`e19b8dbc2c4c1835ed2ce36d8e9d027c3d6fd7e6aed2b4d9eaabcfa83cf5c55f`

Other local pending exact-text hashes are registered separately before copy.

## UCFT v5 history

`history/UCFT_v5/UCFT_V5_SOURCE_LOCATOR.md` records exact File Library IDs and independently audited SHA-256 for the v5 local-steel-shell, material/asymmetric-shell, simply-supported matrix/postbuckling, all-buckling integration and v4 boundary files.

This preserves PBL-as-boundary, `Nu=max N(lambda)`, local/global event != Pu, and Yunlu-source-boundary history without reviving v5 as the current production mother theory.

## Original-binary status

Large PDF/ZIP binaries are still **not claimed as uploaded**. Current GitHub connector accepts UTF-8 content but no mounted local file parameter. Therefore the repository preserves:

- exact filename;
- File Library ID;
- local SHA-256 when available;
- DOI/publisher/public URL when known;
- evidence role and historical identity.

A future true binary upload/git-push channel must place byte-exact originals under `sources/` / `history/raw_original/` and verify their SHA-256.

## Remaining P1/P2 targets

1. copy remaining Case21 local readable reports: Sage/FriCAS result, explicit algebraic-series result, nested-D15 full audit, reproducibility-closure R1;
2. copy/split the three existing UHPC PDF extracted-text mirrors under `sources_text/UHPC/`, with manifest and explicit subordinate-to-PDF status;
3. recover remaining D16/D17/D18 and selected R16–R20 source/audit artifacts where File Library has complete text;
4. append discoveries to `MASTER_SOURCE_INVENTORY.csv` rather than deleting old rows;
5. byte-exact PDF/ZIP migration when a proper binary upload channel exists.

## Governing rule

Do not delete or overwrite an old route merely because a newer route exists. Record `RETAINED / SUPERSEDED / REJECTED / DIAGNOSTIC_ONLY / CURRENT` explicitly, preserve the original evidence locator, and distinguish byte-exact originals from normalized/full-text mirrors.
