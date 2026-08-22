# NZ-SCCM — Post-7Gate Structural Rerun Current Summary

**Date:** 2026-08-22  
**Status:** `CURRENT WORKING RESULTS / SUHPC RESOLVED / NC_TC_R1_S0_RESOLVED / Z GENERAL-S POSTCRACK ULTIMATE OPEN`

Governing post-7gate execution report:

`semantic_v2/40_execution/20260822_1315__NZSCCM__POST_7GATE_STRUCTURAL_RERUN_SUHPC_AND_Z_NC_TC_SOURCE_ROLE_AUDIT.md`

Current NC TC-R1 theory/audit:

`semantic_v2/20_theory/20260822_1338__NZSCCM__NC_TC_MEMORYLESS_REDUCTION_R1_AND_ALTERNATIVE_MODEL_AUDIT.md`

Current Z6 TC-R1 endpoint execution:

`semantic_v2/40_execution/20260822_1340__NZSCCM__Z6_TC_R1_ENDPOINT_EXECUTION_AND_PIVOT_DECISION.md`

Reproduction kernels:

- `semantic_v2/40_execution/steel_shell/20260822_1315__NZSCCM__Z0_Z6_NC_TC_SOURCE_TRANSITION_REPRO.py`
- `semantic_v2/40_execution/steel_shell/20260822_1340__NZSCCM__Z6_TC_R1_DIRECT_ENDPOINT_SOLVER.py`

## 1. SUHPC current post-7gate results

| Case | Zhang 1D / MN | Current 2D / MN | status |
|---|---:|---:|---|
|T120|12.41101|12.22252|Liu TC active / finite re-cut|
|T360|11.36533|11.36533|2D gate inactive at 1D root|
|BH005|2.42351|2.42351|2D gate inactive|
|BH010|4.46632|4.46632|2D gate inactive|
|BH020|8.21925|8.21925|2D gate inactive|
|BH032|11.21046|11.21046|2D gate inactive|
|BH050|13.67770|12.77154|Liu TC active / finite re-cut|

```text
UHPC_COMPRESSION_BACKBONE = ZHANG_2023
UHPC_TC_CT_CAPACITY = LIU2024_SEQUENTIAL_CONSERVATIVE_ENVELOPE
BH050_OLD_PU_OPEN = CLOSED_UNDER_CURRENT_LIU_CAPACITY_ARCHITECTURE
```

## 2. Z0–Z6 Nguyen-source TC transition results

|Case|q_TC|P_TC-transition / MN|segment|status|
|---|---:|---:|---|---|
|Z0|0.002007624998|27.033151885|B|TC cracking/state transition|
|Z1|0.002653115864|17.093528920|B|TC cracking/state transition|
|Z2|0.002007624998|27.033151885|B|TC cracking/state transition|
|Z3|0.003023358231|36.744639968|B|TC cracking/state transition|
|Z4|0.001755102366|56.203522296|A|TC cracking/state transition|
|Z5|0.000194052923|10.747333454|A|TC cracking/state transition|
|Z6|0.004014855283|23.832330467|B|TC cracking/state transition|

These are **not final ultimate loads**. Nguyen Eqs. (3.18)–(3.19) mark the TC cracking/state transition; after breach the source enters cracked constitutive continuation.

```text
Z0_Z6_NC_TC_TRANSITION = SOLVED
TC_FULL_FAILURE_ENVELOPE_AS_SC_ULTIMATE_HARD_CAP = REJECTED
OLD_Z6_51_345 = SUPERSEDED_BY_CURRENT_NC_SOURCE_ROLE
```

## 3. Literal Nguyen postcrack law vs TC-R1

The literal Nguyen TC/TCX implementation stores crack-event and peak/history quantities and therefore fails the production G6 requirement:

```text
LITERAL_NGUYEN_POSTCRACK_TC_G6 = FAIL
LITERAL_NGUYEN_POSTCRACK_TC = OFF_MAINLINE_ORACLE
```

The source-constrained project reduction TC-R1 removes those histories by using:

- current bounded T5 tension;
- a Poisson-free transverse material coordinate;
- current Nguyen/MCFT compression-softening factor;
- Saenz with the current softened peak;
- source-style bounded postcrush continuation.

At material level:

```text
NC_TC_R1_MATERIAL_7GATE = PASS_CANDIDATE
NC_TC_R1_PRODUCTION_FREEZE = NOT_YET
```

## 4. Z6 TC-R1 direct s=0 endpoint

At the zero-bending endpoint the finite section system is uniform through thickness and requires no thickness integration. The direct web-yield complementarity root is

\[
\lambda_t\approx0.7249185,
\qquad
\lambda_c\approx-0.7904509,
\]

\[
q\approx0.01202893,
\]

\[
\boxed{P_{Z6,s=0}^{TC-R1}\approx50.22069\ \mathrm{MN}}.
\]

The current compression-softening factor is

\[
\gamma_c\approx0.95559147.
\]

Recovered phase values include approximately:

- concrete: `sigma_x = +0.913890 MPa`, `sigma_y = -28.338086 MPa`;
- outer steel faces: `sigma_x = +193.420 MPa`, `sigma_y = -216.286 MPa`, radial cap active;
- longitudinal web: `sigma_y = -355 MPa` at compression yield.

One-sided active-set derivatives show that the elastic-web branch reaches the yield surface with increasing q, whereas the capped branch immediately points back to the elastic side. Therefore this is a terminal complementarity event of the **s=0 finite system**.

Only after solving, the endpoint candidate is `+1.483%` relative to Zhou and `+0.069%` relative to Winter. No comparator was used in the solve.

## 5. Why the Z6 final value remains open

A non-formal thickness-quadrature diagnostic indicates that the true controlling `s` may move slightly away from exactly zero. The diagnostic is not part of the formal theory and its numerical minimum is not adopted.

A formal general-s TC-R1 proof would require a finite branch-front primitive family for T5, softened Saenz, steel radial-cap and web-yield zones. This appears mathematically possible but may be too large for the intended compact explicit theory.

Therefore:

```text
Z6_TC_R1_S0_ENDPOINT = 50.22069 MN / RESOLVED_CANDIDATE
Z6_TC_R1_GENERAL_S_FORMAL_CERTIFICATE = OPEN
Z0_Z6_FINAL_POSTCRACK_2D_PU = OPEN
```

## 6. Constitutive replacement gate

Alternative literature models were screened instead of automatically expanding Nguyen:

- Cedolin–Mulas (1984): unusually promising total explicit plane-stress law, but currently recovered scope is up to peak and does not yet establish a post-transverse-crack TC continuation;
- Bažant–Tsubaki (1980): algebraic total-strain model with postpeak/softening, but source domain is concrete free of continuous cracks;
- Darwin–Pecknold: strong biaxial oracle, not obviously simpler for the current G6 section closure;
- full softened-membrane models: richer cracked response but import more state/path/reinforcement machinery.

```text
FIRST_REPLACEMENT_CANDIDATE_IF_TC_R1_GENERAL_S_BECOMES_OPAQUE = CEDOLIN_MULAS_1984
POSTPEAK_TOTAL_STRAIN_ORACLE = BAZANT_TSUBAKI_1980
NO_CONSTITUTIVE_MODEL_IS_LOCKED_BY_STRUCTURAL_COMPARATOR_FIT
```

## 7. Formal execution flags

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_material_points = 0
RITZ_ORDER = NONE
LOAD_PATH_TRACKING = 0
HISTORY_STATE_MACHINE = OFF_MAINLINE
EXPERIMENT_IN_ROOT_SELECTION = 0
FEM_IN_ROOT_SELECTION = 0
STRUCTURAL_BACKBONE_CHANGED = FALSE
```
