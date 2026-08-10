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

## P1 text/artifact archival completed in this checkpoint

### D-series / R-series

Archived exact/full text where available:

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

## Case21 analytical-route history now preserved

Archived:

- one-shot direct-analytic report + complete SymPy source;
- multi-backend direct-analytic result;
- Sage/FriCAS zero-spatial execution report;
- `case21_zero_spatial_analytic.sage` historical source;
- nested-D15 full audit;
- nested-D15 reproducibility closure R1;
- material-compiler R5 report;
- Swartz24 common-policy Case21 gate R2 report;
- analytic-spatial-subdivision revocation notice;
- explicit algebraic zero-spatial series historical result as a clearly marked **NORMALIZED_MIRROR**;
- global one-domain handoff + `NEXTSTEP_EXECUTION_REPORT.md` + `results_nextstep.json`;
- G31 provenance locator.

The explicit-algebraic-series local source had SHA-256:

`1b045d3a248564d69bd063a765bd5a757d3c42db8b918a71c638e8179e50f655`

Its historical local text contained five form-feed corruption sequences preceding `rac`; the GitHub version normalizes those into LaTeX `\frac` and therefore does **not** claim byte-exact identity.

The Sage/FriCAS source is archived as historical source evidence without silently repairing source-code behavior; if a corrected runnable copy is later needed, it must be added as a separate derived file.

## UHPC source-text mirrors

A searchable `sources_text/UHPC/` layer now exists, subordinate to the authoritative PDFs.

### Fully migrated

1. 周俊 — `UHPC三轴受压力学性能研究_周俊.pdf`
   - PDF SHA-256: `37531c8f73765fea9192bef094a88edd7d7eacc5756b51640a7353b65ed72e59`
   - extracted TXT SHA-256: `dad0fe2521e0d79a037dac540d4d75603a45c2d723b98a86a1da57706b671097`
   - GitHub: 6 ordered parts, `FULL_TEXT_MIRROR_MIGRATED`.

2. 王淑楠 — `超高性能混凝土三轴受压力学性能及破坏准则_王淑楠.pdf`
   - PDF SHA-256: `e6e24cf47b21b1faa09f13ceb97a599321283c154578da92ef844b5d8e5c27dd`
   - extracted TXT SHA-256: `5f962ddbbfe307c25e1514b9b521b690a2ad55c04d84e98116e370d97f6b3139`
   - GitHub: 4 ordered parts, `FULL_TEXT_MIRROR_MIGRATED`.

### In progress

3. 胡文旭 — `钢-预制UHPC开孔板组合桥面板界面抗剪性能研究_胡文旭.pdf`
   - PDF SHA-256: `a554649f440bdb5d6523dc174aab68e1128aa6e4f9d19ebb9b67a9e19b544909`
   - extracted TXT SHA-256: `cfd0ed0378554f57e3e58373ca10eb619aa772ab5f1c44da53e44c248b8bbf13`
   - local extraction has been split into 10 ordered chunks;
   - GitHub currently contains `part_01.txt` and `part_02.txt` only;
   - status remains `PARTIAL_TEXT_MIRROR_MIGRATION 2/10` until all 10 are present and recombination is checked.

This partial status is deliberate: a missing GitHub search hit must not be interpreted as absence from the Hu thesis until all parts are migrated.

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

1. finish Hu extracted-text mirror `part_03..10`, then recombine/check against `cfd0ed...bf13`;
2. recover remaining D16/D17/D18 and selected R16–R20 source/audit artifacts where File Library has complete text;
3. append discoveries/status changes to inventory without deleting old rows;
4. build searchable mirrors/locators for Hiew, Liu, Lee, Leutbecher and other File-Library-only UHPC originals;
5. byte-exact PDF/ZIP migration when a proper binary upload channel exists.

## Governing rule

Do not delete or overwrite an old route merely because a newer route exists. Record `RETAINED / SUPERSEDED / REJECTED / DIAGNOSTIC_ONLY / CURRENT` explicitly, preserve the original evidence locator, and distinguish byte-exact originals from normalized/full-text mirrors.
