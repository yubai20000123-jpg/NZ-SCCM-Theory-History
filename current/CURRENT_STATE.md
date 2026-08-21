# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-21 23:35 +08:00  
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

The mandatory capacity interface is now:

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

Uses the ordinary-concrete Nguyen/Foster/Kupfer material identity plus explicit reinforcement phases. CC, TC/CT and TT use the NC source family. Swartz-specific correction coefficients are prohibited.

Swartz specimen-specific `ft` remains source-open; therefore the previously demonstrated TC selectivity for Case1/2 is physical-direction evidence, not a frozen exact corrected Pu.

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

- Case1/2: repeat well experimentally; current pre-TC theory high by about 13%; NC-TC gate has the correct selective downward direction but exact specimen `ft` is not source-closed;
- Case9/10: same structural design, theory low; weak CC enhancement cannot fully explain Case10;
- Case19/20: strongest repeat evidence, theory low about 10% under the current base-strength identity;
- Case21/22: near repeat and close to current theory.

Primary-source audit confirms each panel had companion 28-day cylinders; the historical `0.85 fcyl` belongs to the Swartz/Nguyen analysis material identity and is not authorized for arbitrary replacement by another universal constant.

Latest diagnostics:

- `current/diagnostics/NZ_SCCM_SWARTZ24_SOURCE_CORRECTION_PAIR_MATRIX_TC_CAPACITY_AUDIT_20260821.md`
- `current/diagnostics/NZ_SCCM_SWARTZ_PRIMARY_SOURCE_CASTING_CURING_085_MATERIAL_IDENTITY_AUDIT_20260821.md`

## 3. Steel-shell concrete Z6 — current explicit execution

Current execution:

`semantic_v2/40_execution/20260821_2320__NZSCCM__Z6_CURRENT_EXPLICIT_PRE_GATE_AND_UNIFIED_GATE_AUDIT.md`

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

The existing uniaxial Z-section finite algebraic capacity gives a PRE-GATE Regime-B interior root:

\[
q_u^{pre}=0.01380741294,
\qquad
s_u^{pre}=0.298387166,
\]

\[
\boxed{P_u^{pre}=56.37942109\rm\ MN}.
\]

Only after solution, historical comparators show this PRE-GATE value is about +13.93% versus Zhou and +12.34% versus Winter.

At that root Airy transverse demand is

\[
N_x^d=+2070.408\rm\ N/mm.
\]

The unchanged Regime-B fully plastic longitudinal stress pattern fails a necessary UMCG transverse-admissibility screen: with the current tensile-face steel strip plus the project ordinary-concrete `0.10fc` tension diagnostic, available transverse tension under the unchanged pattern is only about `760.47 N/mm`, demand/capacity ratio about `2.72`.

Decision:

```text
Z6_PRE_GATE_ROOT = SOLVED
Z6_PRE_GATE_PU = 56.37942109 MN
Z6_UMCG_BASELINE_STRESS_PATTERN = FAIL
Z6_FINAL_UNIFIED_PU = OPEN
Z6_STRUCTURAL_BACKBONE_MODIFICATION = NO
```

Interpretation: Z6 demonstrates an applicability boundary of the simple uniaxial N-M section layer, not of the Marguerre–Airy structural backbone itself. Final Z6 requires a phase-rebalanced NC+steel UMCG section solution.

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

The Codex report did **not** provide a new 37-mm BH Pu table; no such values are invented here.

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

1. solve the Z6 phase-rebalanced NC+steel UMCG section to obtain the first **final unified SC Pu** without changing `Ppb`;
2. formally freeze the BH net web/PBL geometry (37-mm candidate strongly indicated), then recompute BH structural coefficients/pre-gate roots;
3. pass T120/T360 and geometry-corrected BH cases through the same UMCG, keeping UHPC TC source status explicit;
4. use Abaqus/test values only after theoretical roots are fixed.