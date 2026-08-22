# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-22 13:40 +08:00  
**Status:** `MARGUERRE_AIRY_EXPLICIT / SUHPC_2D_RESOLVED / NC_TC_R1_MEMORYLESS_CANDIDATE / Z6_S0_ENDPOINT_RESOLVED / Z_GENERAL_S_FINAL_PU_OPEN / CONSTITUTIVE_PIVOT_GATED / USER_ACCEPTANCE_PENDING`

## 0. Governing structural mainline

The structural theory remains unchanged:

`semantic_v2/20_theory/20260821_1733__NZSCCM__MARGUERRE_AIRY_EXPLICIT_LIMIT_THEORY_V1.md`

The governing sequence remains

\[
\boxed{
\text{1D explicit structural/capacity root}
\to
\text{Airy 2D membrane demand}
\to
\text{finite 2D material-capacity/current judgment}
}
\]

and not a second material-point/history solver.

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_material_points = 0
RITZ_ORDER = NONE
LOAD_PATH_TRACKING = 0
HISTORY_STATE_MACHINE = OFF_MAINLINE
HARD_ENVELOPE_HISTORY_OVERLAY = OFF_MAINLINE_DIAGNOSTIC
EXPERIMENT_IN_ROOT_SELECTION = 0
FEM_IN_ROOT_SELECTION = 0
STRUCTURAL_BACKBONE_CHANGED = FALSE
USER_ACCEPTANCE = PENDING
```

---

## 1. Current material source-of-truth chain

Existing seven-gate chain:

1. `semantic_v2/20_theory/20260822_1151__NZSCCM__NC_UHPC_7GATE_EXPLICIT_MATERIAL_REORGANIZATION_V1.md`
2. `semantic_v2/20_theory/20260822_1240__NZSCCM__UHPC_ZHANG_BACKBONE_AND_LIU_CC_CONTINUOUS_SOURCE_MIN_GATE.md`
3. `semantic_v2/20_theory/20260822_1255__NZSCCM__NC_TC_FAILURE_ENVELOPE_VS_APPENDIXB_CONSTITUTIVE_PEAK_RESOLUTION.md`
4. `semantic_v2/20_theory/20260822_1315__NZSCCM__NC_UHPC_7GATE_MATERIAL_CERTIFICATE_V1.md`
5. `semantic_v2/20_theory/20260822_1320__NZSCCM__NC_CC_EQ317_PRINTED_TYPO_VS_FIG32_APPENDIXB_RESOLUTION.md`

New postcrack-TC candidate audit:

6. `semantic_v2/20_theory/20260822_1338__NZSCCM__NC_TC_MEMORYLESS_REDUCTION_R1_AND_ALTERNATIVE_MODEL_AUDIT.md`

Current endpoint execution:

7. `semantic_v2/40_execution/20260822_1340__NZSCCM__Z6_TC_R1_ENDPOINT_EXECUTION_AND_PIVOT_DECISION.md`

Reproducible endpoint solver:

8. `semantic_v2/40_execution/steel_shell/20260822_1340__NZSCCM__Z6_TC_R1_DIRECT_ENDPOINT_SOLVER.py`

Current result summary:

`current/results/NZ_SCCM_POST_7GATE_STRUCTURAL_RERUN_CURRENT_20260822.md`

---

## 2. NC: literal Nguyen vs TC-R1

Nguyen Ch.3/App.B postcrack TC/TCX stores crack-event and historical peak quantities such as `eps_cr`, `f_cr`, precrack shear modulus, softened peak stress/strain and crushing state. Therefore:

```text
LITERAL_NGUYEN_POSTCRACK_TC_SOURCE_FIDELITY = ORACLE_PASS
LITERAL_NGUYEN_POSTCRACK_TC_G6 = FAIL
LITERAL_NGUYEN_POSTCRACK_TC = OFF_MAINLINE
```

The active project candidate is the source-constrained memoryless reduction `TC-R1`:

- T5 current tension;
- Poisson-free material-coordinate transverse tension;
- Nguyen/Vecchio–Collins current compression softening;
- Saenz with the current softened peak;
- bounded source-style postcrush continuation;
- no crack-event or TCX history variable.

The key excess/material-coordinate tension is

\[
\widehat\varepsilon_t
=\frac{\varepsilon_t+\nu\varepsilon_c}{1-\nu^2}
=\varepsilon_0\lambda_t,
\]

and

\[
\gamma_c(\lambda_t)
=\min\left(1,\frac1{0.8+0.34\lambda_t}\right).
\]

Pure uniaxial compression gives `lambda_t=0 -> gamma_c=1`, preventing false Poisson-induced softening.

```text
NC_TC_R1_MATERIAL_7GATE = PASS_CANDIDATE
NC_TC_R1_PRODUCTION_FREEZE = NOT_YET
```

All previously solved Z TC-transition coordinates lie far below `lambda_t=10/17`, so TC-R1 connects continuously to the current pretransition T5+Saenz map without storing a crack event.

---

## 3. NC source-transition status remains distinct

Nguyen Eqs. (3.18)–(3.19) remain the source-identified TC cracking/state-transition boundary, not the final steel-shell ultimate hard cap.

|Case|P_TC-transition / MN|
|---|---:|
|Z0|27.033151885|
|Z1|17.093528920|
|Z2|27.033151885|
|Z3|36.744639968|
|Z4|56.203522296|
|Z5|10.747333454|
|Z6|23.832330467|

```text
Z0_Z6_NC_TC_TRANSITION = SOLVED
TC_ENVELOPE_AS_FINAL_SC_PU = REJECTED
OLD_Z6_51_345 = SUPERSEDED
```

---

## 4. Z6 TC-R1 direct endpoint result

At `s=0`, bending demand vanishes and every phase is uniform through thickness. The current finite algebraic phase-equilibrium system plus the longitudinal-web compression-yield active boundary gives:

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

At that point:

\[
\gamma_c\approx0.95559147,
\]

concrete is approximately

\[
(\sigma_x^c,\sigma_y^c)=(+0.913890,-28.338086)\ \mathrm{MPa},
\]

both outer steel faces are on the plane-stress radial cap, and the equivalent longitudinal web reaches

\[
\sigma_y^w=-355\ \mathrm{MPa}.
\]

A one-sided active-set derivative audit shows that this is a terminal complementarity kink of the **s=0 finite system**.

Only after solving, its difference is about `+1.483%` vs Zhou and `+0.069%` vs Winter. Neither comparator entered the calculation.

```text
Z6_TC_R1_S0_ENDPOINT = RESOLVED_CANDIDATE
Z6_TC_R1_S0_P = 50.22069 MN
```

---

## 5. Why final Z6/Z0–Z6 Pu is still open

For `s>0`, nonzero bending makes longitudinal strain vary through thickness. A formal TC-R1 integration then requires finite branch-front primitives for:

- rational T5;
- softened Saenz;
- plane-stress steel radial cap;
- partially yielded web.

A numerical thickness-integration scan was used only as an **off-mainline diagnostic** and suggests that the controlling location may shift a small distance away from exactly `s=0`. Since formal spatial/thickness quadrature is prohibited, the diagnostic value is not adopted.

```text
Z6_TC_R1_GENERAL_S_DIAGNOSTIC = OFF_MAINLINE_ONLY
Z6_TC_R1_GENERAL_S_FORMAL_CERTIFICATE = OPEN
Z0_Z6_FINAL_POSTCRACK_2D_PU = OPEN
```

The project will not automatically build a large opaque primitive/compiler layer merely to preserve Nguyen lineage.

---

## 6. Constitutive replacement gate

Alternative literature models were screened in parallel:

### Cedolin–Mulas 1984

Very strong G4/G6 architecture: total explicit biaxial stress–strain law, explicit plane-stress transverse-strain elimination, only three material parameters. Current recovered source scope is, however, up to peak; a source-closed post-transverse-crack TC continuation is not yet established.

```text
CEDOLIN_MULAS_1984 = FIRST_REPLACEMENT_CANDIDATE
DROP_IN_POSTCRACK_TC_REPLACEMENT = NOT_YET_PROVEN
```

### Bažant–Tsubaki 1980

Algebraic total-strain core with peak, strain softening and dilatancy, but the source domain is plain concrete free of continuous cracks. Use as a postpeak total-strain oracle unless cracked-TC domain equivalence is demonstrated.

```text
BAZANT_TSUBAKI_1980 = POSTPEAK_TOTAL_STRAIN_ORACLE
```

Darwin–Pecknold remains a biaxial reference/oracle; full softened-membrane models are richer but currently too state/path/reinforcement-heavy for the production G6 role.

The explicit pivot rule is now:

```text
IF TC_R1 general-s closure cannot be written with a small auditable finite primitive set
OR branch/admissibility certification fails,
THEN switch the NC production audit first to Cedolin-Mulas 1984,
without using structural Pu to identify coefficients.
```

---

## 7. UHPC remains unchanged by this NC step

```text
UHPC_COMPRESSION_BACKBONE = ZHANG_2023
UHPC_TENSION_BACKBONE = HIEW_2024
UHPC_CC_CAPACITY = LIU2024_SOURCE_MIN_PROJECT_REDUCTION
UHPC_TC_CT_CAPACITY = LIU2024_SEQUENTIAL_CONSERVATIVE_ENVELOPE
UHPC_TT_CAPACITY = LIU2024_UNIAXIAL_TENSILE_CAP
```

Current post-7gate values remain:

|Case|Current 2D / MN|
|---|---:|
|T120|12.22252|
|T360|11.36533|
|BH005|2.42351|
|BH010|4.46632|
|BH020|8.21925|
|BH032|11.21046|
|BH050|12.77154|

No UHPC parameter or result was changed in the present NC TC-R1 step.
