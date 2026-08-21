# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-22 01:10 +08:00  
**Status:** `MARGUERRE_AIRY_EXPLICIT + SINGLE_OPERATOR_UMCG_ACTIVE / LITERAL_NGUYEN_HISTORY_OVERLAY_REJECTED`

## 0. Governing structure

The structural backbone remains frozen:

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

Common UMCG architecture:

`semantic_v2/20_theory/20260821_2315__NZSCCM__UNIFIED_MULTIAXIAL_CAPACITY_GATE_V1.md`

After the 2026-08-22 source-continuation audit, the production interpretation is:

\[
\boxed{
\text{structural resultants}
\to
\text{phase-compatible stress recovery}
\to
\mathcal M_r(\varepsilon)
\to
\text{operator-internal branch/domain admissibility}
\to
\text{section equilibrium/fold}
}
\]

Each material phase gets one production current operator. A separate historical source state machine is not overlaid at runtime on top of that operator.

```text
STRUCTURAL_BACKBONE = FROZEN
UMCG_ARCHITECTURE = RETAINED
UMCG_INTERPRETATION = SINGLE_PRODUCTION_OPERATOR_PER_PHASE
UMCG_DIMENSION = PLANE_STRESS_2D
SIGMA_Z_RECOVERY = NOT_ACTIVATED
RITZ_ORDER = NONE
LOAD_PATH_TRACKING = NOT_REQUIRED AT STRUCTURAL LEVEL
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_MATERIAL_POINTS = 0
EXPERIMENT_IN_ROOT_SELECTION = 0
FEM_IN_ROOT_SELECTION = 0
STRUCTURE_SPECIFIC_CAPACITY_MULTIPLIER = PROHIBITED
```

## 1. Nguyen/Foster source-envelope role corrected

Preceding literal hard-envelope audit:

`semantic_v2/40_execution/20260822_0015__NZSCCM__STRICT_HARD_ADMISSIBILITY_CASE1_CASE2_Z6_AUDIT.md`

Latest post-envelope execution:

`semantic_v2/40_execution/20260822_0105__NZSCCM__NGUYEN_POST_ENVELOPE_CONTINUATION_CASE1_CASE2_Z6_AUDIT.md`

The latest audit explicitly tested the proposed continuation:

\[
\text{NC-M6 pre-event}
\to
\text{Nguyen envelope contact}
\to
\text{Nguyen TC/TT/CC/TCX point-history continuation}.
\]

Result:

```text
POST_ENVELOPE_SOURCE_CONTINUATION_AUDIT = EXECUTED
LITERAL_NGUYEN_POINT_HISTORY_OVERLAY = REJECTED_FOR_FORMAL_PRODUCTION
```

The reason is theoretical, not comparator-driven:

1. Nguyen TC/TT/CC/TCX states carry crack/crush event histories such as `eps_cr`, `f_cr`, peak stress and peak strain;
2. postbuckled through-thickness sections generate moving cracked/crushed fronts with spatially varying history fields;
3. the recovered NSC state ledger already marks the general history states as not admissible as a full formal zero-quadrature state;
4. discrete material-point continuation turns a zero-measure first crack into a finite resultant jump and gives resolution-sensitive audit localizers;
5. Nguyen's later approximate initial-imperfection route is explicitly limited against out-of-plane bending cracks, whereas the present ultimate section can develop them.

Therefore the modified Kupfer/Foster envelope is retained as:

```text
SOURCE_STRENGTH_TARGET
MATERIAL_QUALIFICATION_ANCHOR
STATE_MECHANISM_REFERENCE
```

and is **not** an additional terminal runtime cap on top of NC-M6.

This also prevents an invalid transfer to UHPC: an initial TT/TC envelope must not globally clip fibre-bridged post-cracking hardening.

## 2. Ordinary concrete production identity

NC-M6 remains the current ordinary-concrete memoryless production current operator. It already contains bounded TC/TT/CC mechanisms and post-cracking/post-peak continuation in one current-state map.

Its source relationship to Nguyen remains explicit:

- Nguyen/Saenz uniaxial compression anchors;
- Foster-style tension stiffening anchors;
- Nguyen/Kupfer CC/TC/TT strength/mechanism targets;
- project memoryless regularization removes the literal material history field.

This approximation is a declared project modeling choice and must not be hidden.

Swartz specimen-specific tensile strength remains source-open. The project-wide `ft=0.10fc` ordinary-concrete value is a common material identity, not a specimen-fitted input.

## 3. Swartz Case1/2 identities

Correct source reinforcement interpretation remains

\[
\rho_x=\rho_y=p_{table}.
\]

The distinct numerical objects remain:

|Object|Case1 kN|Case2 kN|Identity|
|---|---:|---:|---|
|corrected-reinforcement uniaxial N-M candidate|567.712|561.638|PRE-GATE|
|old separate TC contact|495.989|501.025|MECHANISM SENSITIVITY ONLY|
|Nguyen/Foster first-contact overlay|588.598|584.545|SOURCE-ENVELOPE EVENT DIAGNOSTIC|
|NC-M6 phase-compatible UMCG fold|604.450|597.732|CURRENT COMMON-MATERIAL UMCG DIAGNOSTIC|

The attempted literal Nguyen post-envelope point-history continuation does not define a resolution-independent formal Pu. Audit localizers remained only a few kN above the first-contact events and depended on thickness-state resolution.

Therefore:

```text
CASE1_2_495_501_AS_UNIFIED_STRICT = SUPERSEDED
CASE1_2_588_584_AS_MEMBER_ULTIMATE = NO
CASE1_2_LITERAL_NGUYEN_HISTORY_PU = NOT DEFINED
CASE1_2_NC_M6_UMCG_BIAS = EXPLICITLY RETAINED
SWARTZ_SPECIFIC_K = PROHIBITED
```

The Case1/2 repeat pair remains a real high-bias design point under the common NC-M6 material identity. That residual is not removed by a panel-specific correction.

## 4. Swartz24 common-material diagnostic

Latest common-material batch:

`current/diagnostics/NZ_SCCM_SWARTZ24_UMCG_BATCH_AUDIT_LOCALIZER_20260821.md`

With corrected reinforcement mapping and common NC-M6 material identity:

\[
\text{mean signed error}\approx+0.759\%,
\]

\[
\text{MAE}\approx11.153\%,\qquad \text{RMSE}\approx13.583\%.
\]

The near-zero global signed mean is not treated as calibration success because group/pair biases remain. Trusted repeat-pair interpretation remains primary.

## 5. Steel-shell concrete Z6

Frozen explicit structural coefficients remain:

\[
P_{cr}=39.2880147150\ \mathrm{MN},
\]

\[
C=86071.5974582\ \mathrm{MN},
\quad
G=7.4692093263\times10^6\ \mathrm{N/mm},
\quad
J=1.2419245217\times10^7\ \mathrm{N}.
\]

Numerical identities:

```text
Z6_56P379_MN = UNIAXIAL_PRE_GATE
Z6_47P210_MN = NGUYEN/FOSTER FIRST-CONTACT DIAGNOSTIC
Z6_51P345_MN = CURRENT NC-M6 PHASE-COMPATIBLE UMCG FOLD PREDICTION
LITERAL_NGUYEN_HISTORY_OVERLAY_Z6_FINAL_PU = NOT DEFINED
```

The attempted NC-M6 -> Nguyen TC/TCX history overlay at the first-contact control section `s≈0.452284` produced audit-localizer continuation values near `47.3–47.5 MN` for 20/40/80 thickness-state resolutions, with no convergent formal sequence. It is not promoted.

Under the current single-operator UMCG identity, the retained Z6 prediction is therefore the NC-M6 phase-rebalanced section fold

\[
\boxed{P_{u,Z6}^{NC-M6\ UMCG}=51.3450217892\ \mathrm{MN}}.
\]

Only after that theoretical root is fixed, historical comparators are:

\[
P_{Zhou}=49.48676675\ \mathrm{MN},
\qquad
P_{Winter}=50.18585413\ \mathrm{MN}.
\]

Thus the retained current prediction is approximately

\[
+3.755\%\ \text{vs Zhou},
\qquad
+2.310\%\ \text{vs Winter}.
\]

The desirable `Zhou < NZ-SCCM < Winter` bracket is **not** achieved and is **not** used as a root condition. The residual is retained rather than fitted away.

## 6. Steel and UHPC transfer

Steel runtime yield/von-Mises constraints remain active because they are part of the steel production operator itself, not a second incompatible post-yield model.

UHPC must use the same UMCG architecture but its own material current operator:

- fibre-bridged tension/hardening/softening;
- UHPC CC enhancement;
- UHPC-specific TC regularization;
- no transfer of NC `alpha2=0.3`, Saenz compression or NC shear-retention numbers as production law.

## 7. Steel-shell UHPC geometry status

Codex integration remains:

`current/audits/NZ_SCCM_STEEL_SHELL_UHPC_CODEX_R02_DAMAGE_GEOMETRY_INTEGRATION_20260821.md`

For BH005--BH050:

```text
BH_32MM_WEB_HEIGHT = SUPERSEDED_AS_CURRENT_VALIDATION_GEOMETRY
BH_37MM_WEB_HEIGHT = STRONGLY_INDICATED_REBASE_CANDIDATE
BH_37MM_FINAL_CONTRACT = PENDING_FORMAL_FREEZE
BH_CURRENT_QUANTITATIVE_VALIDATION_BASELINE = OPEN
```

T120/T360 existing web-included values remain working scale checks, not verified geometry/material-matched predictions.

## 8. Governing validation principle

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
NGUYEN_HISTORY_OVERLAY = REJECTED_FOR_FORMAL_PRODUCTION
SOURCE_ENVELOPE_AS_OFFLINE_QUALIFICATION = RETAINED
RESIDUAL_MATERIAL_SPECIMEN_SCATTER = ACCEPTABLE_IF_EXPLICITLY_IDENTIFIED
```

## 9. Recommended next execution

The ordinary-concrete post-envelope history question is now closed negatively: literal Nguyen point-history continuation is not the formal route.

The next admissible system-level execution is:

1. freeze the corrected BH/PBL geometry contract, with 37-mm net web height currently strongly indicated;
2. regenerate BH structural coefficients and NC/UHPC/steel phase geometry from that one contract;
3. apply the same single-operator UMCG to T120/T360 and corrected BH cases using the UHPC current operator, without importing the NC hard-envelope state machine;
4. compare RC / SC / SUHPC residual biases only after theoretical roots are fixed;
5. separately investigate Swartz ordinary-concrete tensile-strength source identity if a common NC material-input refinement is needed, never by fitting Case1/2 failure loads.