# NZ-SCCM — 钢壳-UHPC T120/T360 与 BH005–BH050 当前状态（Codex复核后）

**Updated:** 2026-08-21 23:30 +08:00  
**Status:** CURRENT WORKING SUMMARY / CONTRACT-AUDITED / NON-CALIBRATING

## 0. Current theory interface

Structure layer remains

\[
\boxed{\text{Marguerre--Airy explicit postbuckling}+\text{finite algebraic control candidates}}.
\]

Capacity now must pass

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

as formalized in

`semantic_v2/20_theory/20260821_2315__NZSCCM__UNIFIED_MULTIAXIAL_CAPACITY_GATE_V1.md`.

No SUHPC-specific empirical confinement multiplier is permitted.

---

## 1. T120 / T360 retained working values

The old values that omitted internal longitudinal webs are superseded:

- T120: `11.7073 MN`;
- T360: `11.0538 MN`.

The later web-included working values remain:

\[
\boxed{P_{u,T120}^{work}=12.34799984\rm\ MN},
\]

\[
\boxed{P_{u,T360}^{work}=11.29784021\rm\ MN}.
\]

Existing Abaqus R02 peaks in the Codex audit are:

\[
P_{R02,T120}=12.6378\rm\ MN,
\]

\[
P_{R02,T360}=10.9688\rm\ MN,
\]

which correspond to approximately +2.35% and -2.91% FEM-theory differences respectively.

These are **scale agreements only**, not VERIFIED theory validation, because the audited contracts are not identical:

- theory UHPC `nu=0.20` versus FEM UC141 `nu=0.30`;
- theory tensile/cracking anchor about `9.77 MPa` versus FEM tensile onset about `5.57 MPa`;
- current theory steel post-yield treatment differs from FEM Q355 segmented hardening;
- analytic and R02/R03 boundary/contact contracts differ.

### T120 mode label

Canonical geometry is approximately

\[
b=1600\rm\ mm,\qquad a_{phys}=3000\rm\ mm.
\]

The R02 imperfection has two longitudinal halfwaves. The old text label `m*=1` is therefore classified as a likely documentation error; the audited numerical branch is consistent with `m*=2`.

```text
T120_T360_WORKING_PU = RETAINED_FOR_PROVENANCE_AND_SCALE_CHECK
T120_T360_VERIFICATION = ANALYZED_NOT_VERIFIED
T120_MSTAR_TEXT_LABEL = SUSPECT_REPAIR_REQUIRED
FULL_UMCG_UHPC_TC_CLOSURE = OPEN
```

---

## 2. BH geometry contract: 32 mm revoked as current validation geometry

BH family nominal external dimensions remain:

|Case|B/H|B mm|L mm|H mm|
|---|---:|---:|---:|---:|
|BH005|5|250|500|50|
|BH010|10|500|1000|50|
|BH020|20|1000|2000|50|
|BH032|32|1600|3200|50|
|BH050|50|2500|5000|50|

with

\[
L=2B,\qquad t_s=4\rm\ mm,\qquad t_c=42\rm\ mm,
\qquad q_0=1/400.
\]

The previous BH theory used nine longitudinal webs/PBL with effective height

\[
h_w=32\rm\ mm,
\]

so

\[
A_{w,32}=9\times4\times32=1152\rm\ mm^2.
\]

The Codex geometry audit shows that the canonical PBL height is about 41 mm and the shell thickness is 4 mm; the net added steel height inside the core is therefore closer to

\[
\boxed{h_w\approx37\rm\ mm}.
\]

The old 32-mm value likely double-deducted a gap/clearance. Accordingly:

```text
BH_32MM_WEB_HEIGHT = SUPERSEDED_AS_CURRENT_VALIDATION_GEOMETRY
BH_37MM_WEB_HEIGHT = STRONGLY_INDICATED_REBASE_CANDIDATE
BH_37MM_FINAL_GEOMETRY_CONTRACT = PENDING_FORMAL_FREEZE
```

For reference only, a 37-mm candidate would give

\[
A_{w,37}=9\times4\times37=1332\rm\ mm^2
\]

and candidate web ratios:

|Case|rho_w at 32 mm|rho_w at 37 mm candidate|
|---|---:|---:|
|BH005|10.9714%|12.6857%|
|BH010|5.4857%|6.3429%|
|BH020|2.7429%|3.1714%|
|BH032|1.7143%|1.9821%|
|BH050|1.0971%|1.2686%|

No new 37-mm Pu is frozen in this document because the uploaded Codex report did not provide a recalculated 37-mm Pu table; it flagged the geometry inconsistency while its theory-vs-Abaqus table still used the old 32-mm theory values.

---

## 3. Old BH 32-mm results: provenance only

The following values are retained only as the old geometry-mismatched comparator:

|Case|old 32-mm theory Pu / MN|Abaqus value in Codex audit / MN|reported FEM-theory|
|---|---:|---:|---:|
|BH005|2.382928|2.3558|-1.14%|
|BH010|4.417320|4.3043|-2.56%|
|BH020|8.139798|8.0076|-1.62%|
|BH032|11.110053|10.9905|-1.08%|
|BH050*|13.594607|12.2198|-10.11%|

`*` BH050 is from a different diagnostic model family and is not an equal-contract validation point.

These close values may contain geometry/material/boundary error cancellation and therefore must not be used as evidence to preserve the 32-mm theory contract.

```text
BH005_BH050_OLD_PU = HISTORICAL_32MM_COMPARATOR
BH_CURRENT_QUANTITATIVE_VALIDATION_BASELINE = OPEN_PENDING_GEOMETRY_REBASE
```

---

## 4. Damage/mode evidence from Codex audit

The existing ODB mapping indicates:

- T120 UHPC-core damage is the closest to the global `m=2` wave;
- T360 and BH032 longitudinal damage positions are compatible with the global `m=2` antinode, while transverse position is affected by local plate/boundary effects;
- BH005/BH010 are predominantly side/end damage controlled at peak;
- BH020 shows mixed side/end and global-wave damage;
- maximum steel-shell PEEQ in unified R02 cases lies at `x=±B/2`, so the global Marguerre wave alone is not a complete local steel failure descriptor;
- a unique local-panel coordinate/identity is still required for a quantitative theory–PEEQ local-mode comparison.

Therefore:

```text
MODE_AGREEMENT = QUALITATIVE_PARTIAL
VERIFICATION_LEVEL = ANALYZED_NOT_VERIFIED
```

---

## 5. Unified multiaxial capacity status

Previous T120/T360 plane-stress screening found mixed CC/TC states but did not trigger the old theoretical UHPC tensile anchor. This remains a useful working screen only.

The new UMCG requires the same sequence as NC and steel-shell concrete:

\[
\text{Airy/section resultants}
\to
\text{UHPC + face steel + web steel stress recovery}
\to
\text{UHPC/steel admissibility}
\to
\text{capacity root}.
\]

UHPC is not allowed to use the NC TC numerical law. UHPC TC must remain source-specific; the currently available Liu compression-softening subbranch is not yet a complete arbitrary-path vector material operator.

```text
T120_T360_2D_PRECHECK = RETAINED_AS_WORKING_SCREEN
BH_UMCG_EXECUTION = BLOCKED_BY_GEOMETRY_REBASE
UHPC_FULL_TC_VECTOR_CLOSURE = PARTIAL_OPEN
TRIAXIAL_SIGMA_Z_GATE = NOT_ACTIVATED_IN_CURRENT_PLANE_STRESS_THEORY
```

---

## 6. Current next action

1. freeze the canonical BH net web/PBL geometry from the source model (37-mm candidate currently strongly indicated);
2. recompute BH elastic/extensional coefficients and pre-gate roots from that frozen geometry;
3. pass T120/T360/BH through the same UMCG architecture used for NC and SC;
4. keep Abaqus peaks/damage maps as post-solution validation evidence only.

No theoretical parameter is to be adjusted to recover the existing R02 peaks.