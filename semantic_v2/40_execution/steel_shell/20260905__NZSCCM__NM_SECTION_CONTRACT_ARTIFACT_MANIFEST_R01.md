# NZ-SCCM N-M section contract artifact manifest R01

Date: 2026-09-05
Branch: `diagnostic/bh032-bh050-mode-projection-20260827`

## Scope locked

Current work stops at:

\[
(x,y,\lambda,u_2,v_2,q)\rightarrow N_x(x,y),M_x(x,y),N_y(x,y),M_y(x,y).
\]

No area integration, no Gauss, no virtual work, no new R4/J4, no limit load.

UHPC uses the original 01 compression polynomial and four-segment Hermite tension law; the tension anchors are only nondimensionalized. Multiwave steel and web remain downstream section modules.

## Exact local artifacts produced in this session

1. `20260905__NZSCCM__NEW_KINEMATICS_TO_NM_SECTION_CONTRACT_R01.md`
   - SHA-256: `75d2ad39ec96153aea5a91e50039f89f74316b04f9b9f969347f4ec1fa8850bd`
   - exact local snapshot of the current merged general contract.

2. `20260905__NZSCCM__BH050_NEW_KINEMATICS_TO_NM_EXPLICIT_SUBSTITUTION_R01.md`
   - SHA-256: `9f64ca74769a80fe90a2eecf222a5b4d0b5bcb7d009cc38a627b8ac490eb0248`
   - BH050 fixed-parameter substitution ledger through `N_x,M_x,N_y,M_y`.
   - this text artifact is committed on this branch.

3. `20260905__NZSCCM__BH050_NM_SECTION_CONTRACT_R01.xlsx`
   - SHA-256: `b6e890c01ef98d695a595a9156395b18a89d6f345f5221fafc3e2ed8e98a5321`
   - formula-driven Excel foundation with sheets `README`, `BH050_Input`, `Hermite_UHPC`, `Kinematics`, `UHPC_NM`, `Web_NM`, `Steel_Strips`, `Total_NM`.
   - `lambda,u2,v2,q,x,y` are editable inputs.
   - UHPC and web are closed-form; R02 cubic is formula-driven; R04 is complete; exact R06 first-yield scalar root is exposed as the editable `r_y input` interface rather than hidden.

## GitHub text ledger

The BH050 substitution ledger is stored at:

`semantic_v2/40_execution/steel_shell/20260905__NZSCCM__BH050_NEW_KINEMATICS_TO_NM_EXPLICIT_SUBSTITUTION_R01.md`

This manifest records the hashes of the exact local general-contract and workbook snapshots so a later local agent can verify a byte-identical binary/text transfer if required.
