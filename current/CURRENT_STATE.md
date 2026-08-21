# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-21 23:50 +08:00  
**Status:** `MARGUERRE_AIRY_EXPLICIT + UNIFIED_MULTIAXIAL_CAPACITY_GATE = CURRENT ACTIVE LINE`

## 0. Current governing architecture

The current structural theory remains the low-order explicit Marguerre–Airy line:

\[
P_{pb}(q)=P_{cr}\frac{q}{q+q_0}+Cq(q+2q_0),
\]

\[
n(s;q)=\frac{P_{pb}(q)}b+Gq(q+2q_0)(1-2s^2),
\qquad
m(s;q)=Jqs.
\]

Canonical structural theory:

`semantic_v2/20_theory/20260821_1733__NZSCCM__MARGUERRE_AIRY_EXPLICIT_LIMIT_THEORY_V1.md`

Mandatory capacity interface:

`semantic_v2/20_theory/20260821_2315__NZSCCM__UNIFIED_MULTIAXIAL_CAPACITY_GATE_V1.md`

\[
\boxed{
\text{structural resultants}
\to
\text{phase stress recovery}
\to
\text{material admissibility}
\to
\text{section capacity}
}
\]

The interface is common to NC/RC, steel-shell concrete (SC), and steel-shell UHPC (SUHPC). Material laws differ by material identity; the constraint architecture does not.

```text
STRUCTURAL_BACKBONE = FROZEN
UMCG_ARCHITECTURE = PASS
UMCG_DIMENSION = PLANE_STRESS_2D
SIGMA_Z_RECOVERY = NOT_ACTIVATED
RITZ_ORDER = NONE
LOAD_PATH_TRACKING = NOT_REQUIRED
FORMAL_SPATIAL_QUADRATURE = 0
EXPERIMENT_IN_ROOT_SELECTION = 0
FEM_IN_ROOT_SELECTION = 0
STRUCTURE_SPECIFIC_CAPACITY_MULTIPLIER = PROHIBITED
```

## 1. Unified material identities

### NC / RC

Uses the frozen ordinary-concrete current material identity plus explicit reinforcement phases. Current NC low-parameter targets retain CC enhancement, TC/CT weakening and TT interaction. Swartz-specific correction coefficients are prohibited.

Swartz specimen-specific `ft` remains source-open; therefore any exact specimen TC prediction whose numerical value depends on that missing property must be labelled accordingly. The project NC baseline `ft=0.10fc` may be used only with its explicit project-material identity, never inferred from panel failure load.

### UHPC

Uses the same UMCG interface but its own UHPC material sources.

- UHPC CC: UHPC-specific biaxial compression source/target;
- UHPC tension: fibre-bridged UHPC tensile backbone;
- UHPC TC: must use UHPC-specific Liu-source softening/regularization; the NC TC numerical rule is not transferable as production law;
- full arbitrary-path UHPC TC vector closure remains partial/open.

### Steel

External faces and any two-dimensional steel phase must satisfy the steel plane-stress yield surface in addition to section equilibrium. Webs/rebars use their source axial/yield laws unless a recovered two-dimensional stress state is assigned.

A uniaxial fully plastic section pattern cannot be assumed to carry arbitrary transverse Airy membrane force without rebalancing its longitudinal stress.

## 2. Swartz RC current diagnostic status

Mandatory source correction remains:

\[
\rho_x=\rho_y=p_{table},
\]

not `p_table/2`.

Experimental `Pcr` is not used to modify stiffness or the current structural backbone. Validation priority remains trusted repeat/near-repeat design points rather than direct 24-point fitting:

- Case1/2: repeat well experimentally; current pre-TC theory high by about 13%; NC-TC gate has the correct selective downward direction;
- Case9/10: same structural design, theory low; weak CC enhancement cannot fully explain Case10;
- Case19/20: strongest repeat evidence, theory low about 10% under the current base-strength identity;
- Case21/22: near repeat and close to current theory.

Primary-source audit confirms each panel had companion 28-day cylinders; the historical `0.85 fcyl` belongs to the Swartz/Nguyen analysis material identity and is not authorized for arbitrary replacement by another universal constant.

Latest diagnostics:

- `current/diagnostics/NZ_SCCM_SWARTZ24_SOURCE_CORRECTION_PAIR_MATRIX_TC_CAPACITY_AUDIT_20260821.md`
- `current/diagnostics/NZ_SCCM_SWARTZ_PRIMARY_SOURCE_CASTING_CURING_085_MATERIAL_IDENTITY_AUDIT_20260821.md`

## 3. Steel-shell concrete Z6 — final UMCG result resolved

PRE-GATE audit:

`semantic_v2/40_execution/20260821_2320__NZSCCM__Z6_CURRENT_EXPLICIT_PRE_GATE_AND_UNIFIED_GATE_AUDIT.md`

Final UMCG execution:

`semantic_v2/40_execution/20260821_2348__NZSCCM__Z6_FULL_UMCG_RECALCULATION_AND_FORMAL_ENDPOINT_REDUCTION.md`

Source-closed Z6 whole wall:

\[
a_{phys}=24000\rm\ mm,\quad b=12000\rm\ mm,\quad
 t_c=122\rm\ mm,\quad t_s=4\rm\ mm/face,
\]

\[
\rho_w=0.02,\quad f_c=30.4\rm\ MPa,\quad E_c=32.5\rm\ GPa,
\quad E_s=206\rm\ GPa,\quad f_y=355\rm\ MPa,
\]

\[
A_0=48\rm\ mm,\qquad q_0=0.004.
\]

Fresh integer halfwave search gives

\[
\boxed{m_*=2},\qquad \ell=12000\rm\ mm.
\]

Current explicit coefficients:

\[
P_{cr}=39.28801472\rm\ MN,
\]

\[
C=86071.59746\rm\ MN,
\qquad
G=7.4692093\times10^6\rm\ N/mm,
\qquad
J=1.2419245\times10^7\rm\ N.
\]

The old uniaxial Z-section capacity produced the PRE-GATE interior root

\[
q_u^{pre}=0.01380741294,
\qquad
s_u^{pre}=0.298387166,
\]

\[
P_u^{pre}=56.37942109\rm\ MN,
\]

but its longitudinal plastic stress allocation failed UMCG because it could not simultaneously satisfy the large Airy transverse membrane demand.

The phase-rebalanced NC+steel UMCG calculation now resolves the first admissible capacity state at

\[
\boxed{s_u=0},
\]

\[
\boxed{q_u^{UMCG}=0.01236088015386989},
\]

\[
\boxed{P_u^{UMCG}=51.34502178921372\rm\ MN}.
\]

The UMCG therefore reduces the PRE-GATE capacity by

\[
\boxed{8.92950\%}.
\]

At the governing endpoint, `m_y=0`, section curvature recovery is zero and the final state is uniform through thickness by phase. Hence the controlling root admits a formal no-thickness-quadrature reduction.

NC equivalent principal coordinates:

\[
\lambda_x=1.4043063311724063,
\qquad
\lambda_y=-10/7.
\]

The frozen NC-M6 T5 tensile target has \(\tau=0.3\), so

\[
(-\lambda_y)(1-\tau)=1,
\]

and the compressed NC principal direction reaches the Saenz peak:

\[
\sigma_y^c=-30.4\rm\ MPa,
\qquad
\sigma_x^c=+0.912\rm\ MPa.
\]

External faces are on the plane-stress von-Mises radial cap:

\[
\sigma_x^s=+202.6895\rm\ MPa,
\qquad
\sigma_y^s=-207.2208\rm\ MPa,
\]

and the longitudinal web is at y-compression yield \(-355\rm\ MPa\).

The final phase sums satisfy

\[
N_x=1730.5550\rm\ N/mm,
\qquad
N_y=-6158.5905\rm\ N/mm,
\qquad
M_y=0,
\]

which equal the structural demands at the same q.

Only after fixing this root, comparison gives:

\[
\boxed{+3.75505\%\ \text{vs Zhou}},
\]

\[
\boxed{+2.30975\%\ \text{vs Winter}}.
\]

No parameter is adjusted to remove the residual.

```text
Z6_FINAL_UMCG_ROOT = RESOLVED
Z6_CONTROL_LOCATION = s=0
Z6_FINAL_UMCG_PU = 51.34502178921372 MN
Z6_GATE_EFFECT_FROM_PRE_GATE = -8.92950 percent
Z6_FINAL_VS_ZHOU = +3.75505 percent
Z6_FINAL_VS_WINTER = +2.30975 percent
Z6_FORMAL_ENDPOINT_THICKNESS_QUADRATURE = 0
Z6_STRUCTURAL_BACKBONE_MODIFICATION = NO
COMPARATOR_IN_ROOT_SELECTION = 0
```

Interpretation: Z6 validates the purpose of UMCG. The Marguerre–Airy structural backbone need not be altered; the previous error came largely from allowing a uniaxial section allocation to ignore transverse Airy demand. The common multiaxial gate moves the prediction in the correct direction without structural or material backfit.

## 4. Steel-shell UHPC — Codex integration

Integrated audit:

`current/audits/NZ_SCCM_STEEL_SHELL_UHPC_CODEX_R02_DAMAGE_GEOMETRY_INTEGRATION_20260821.md`

The uploaded Codex report is classified:

```text
VERIFICATION_STATUS = ANALYZED_NOT_VERIFIED
NEW_ABAQUS_SOLVE_IN_REPORT = NO
FEM_BACKFIT = PROHIBITED
```

Its existing theory/R02 peak comparisons show roughly 1–3% differences for BH005–BH032/T120/T360, but this is only encouraging scale agreement because geometry/material/boundary contracts differ. BH050 uses a different diagnostic model family.

Damage mapping indicates T120 core damage is the closest to the global m=2 wave; T360/BH032 are longitudinally compatible but transversely affected by local/boundary mechanisms; BH005/BH010 are mainly side/end triggered; steel-shell peak PEEQ generally lies at x=±B/2 and cannot be identified with the global wave alone.

## 5. SUHPC geometry/material corrections

Updated current summary:

`current/results/NZ_SCCM_STEEL_SHELL_UHPC_T120_T360_BH005_BH050_CURRENT_SUMMARY_20260821.md`

### T120/T360

Working web-included values remain retained for provenance/scale check:

\[
P_{u,T120}^{work}=12.3480\rm\ MN,
\qquad
P_{u,T360}^{work}=11.2978\rm\ MN.
\]

However they are not VERIFIED because theory/FEM material cards differ (`nu_UHPC 0.20 vs 0.30`, tensile anchor about `9.77 vs 5.57 MPa`, steel hardening treatment differs), and boundary/contact contracts are not identical.

The old T120 text `m*=1` label is classified as suspect; canonical 3000×1600 geometry and the audited numerical branch are consistent with `m=2`.

### BH005–BH050

The previous BH theory used net web height `32 mm`. Codex geometry audit shows the canonical PBL height is about 41 mm with 4-mm outer shell thickness and a 42-mm core, so net added web steel inside the core is closer to `37 mm`. The old 32-mm value likely double-deducted a gap.

Therefore:

```text
BH_32MM_WEB_HEIGHT = SUPERSEDED_AS_CURRENT_VALIDATION_GEOMETRY
BH_37MM_WEB_HEIGHT = STRONGLY_INDICATED_REBASE_CANDIDATE
BH_37MM_FINAL_CONTRACT = PENDING_FORMAL_FREEZE
BH_OLD_32MM_PU_TABLE = HISTORICAL_GEOMETRY_MISMATCHED_COMPARATOR
BH_CURRENT_QUANTITATIVE_VALIDATION_BASELINE = OPEN
```

The Codex report did not provide a new 37-mm BH Pu table; no such values are invented here.

## 6. Governing validation principle

The project no longer seeks a separate perfect fit for Swartz, SC or SUHPC. It seeks one transferable material-constraint architecture with explainable residual error:

\[
\boxed{
\text{transferable NC--SC--SUHPC mechanics with explainable residual error}
>
\text{dataset-specific fitting}
}
\]

```text
SWARTZ_SPECIFIC_K = PROHIBITED
SC_GLOBAL_SCALE_FACTOR = PROHIBITED
SUHPC_EMPIRICAL_CONFINEMENT_MULTIPLIER = PROHIBITED
STRUCTURAL_PU_BACKFIT_TO_MATERIAL = PROHIBITED
RESIDUAL_MATERIAL_SPECIMEN_SCATTER = ACCEPTABLE_IF_EXPLICITLY_IDENTIFIED
```

## 7. Recommended next execution

The Z6 gate is now resolved. Continue the common architecture in this order:

1. run the Swartz24 UMCG batch with the corrected reinforcement interpretation; preserve explicit status wherever specimen-specific tensile strength is not source-closed;
2. formally freeze the BH net web/PBL geometry (37-mm candidate strongly indicated), then recompute BH structural coefficients/pre-gate roots;
3. pass T120/T360 and geometry-corrected BH cases through the same UMCG, keeping UHPC TC source status explicit;
4. compare RC, SC and SUHPC only after each theoretical root is fixed.