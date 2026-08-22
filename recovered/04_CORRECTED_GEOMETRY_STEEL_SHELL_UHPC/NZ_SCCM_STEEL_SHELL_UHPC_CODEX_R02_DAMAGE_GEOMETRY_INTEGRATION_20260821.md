# NZ-SCCM — 钢壳-UHPC Codex R02/Abaqus 对照、几何与损伤映射审计整合

**Time:** 2026-08-21 23:25 +08:00  
**Status:** ANALYZED / NOT VERIFIED / NON-CALIBRATING

## 0. Evidence identity

This file integrates the user-provided Codex report `NZ_SCCM_理论复核_Abaqus对照_逐单元损伤映射_综合报告_20260821.md` into the repository governance chain.

The source report explicitly states that it is a read-only review of existing files/ODBs. It did not submit a new Abaqus solve and its final verification level is **ANALYZED / NOT VERIFIED**.

No FEM result is allowed to choose a theoretical root or tune a material parameter.

## 1. What the report supports

The existing explicit scalar postbuckling equation is arithmetically self-consistent at the printed roots. Existing theory/FEM R02 peak comparisons reported are:

| case | theory in audited report / MN | Abaqus R02 / MN | FEM-theory |
|---|---:|---:|---:|
|BH005|2.3829|2.3558|-1.14%|
|BH010|4.4173|4.3043|-2.56%|
|BH020|8.1398|8.0076|-1.62%|
|BH032|11.1101|10.9905|-1.08%|
|BH050*|13.5946|12.2198|-10.11%|
|T120|12.3480|12.6378|+2.35%|
|T360|11.2978|10.9688|-2.91%|

BH050 uses a different diagnostic model family and therefore is not an equal-contract validation point.

The 1–3% peak agreement of BH005–BH032/T120/T360 is encouraging as a scale check but cannot be called VERIFIED because geometry, material cards, boundary conditions and damage/local-mode identities are not yet identical. Error cancellation remains possible.

## 2. Damage/mode mapping

The report's peak-frame element mapping indicates:

- T120 core UHPC damage is the closest to the global m=2 theoretical wave;
- T360 and BH032 are compatible with the m=2 longitudinal antinode location, while transverse location is affected by local plate/boundary mechanisms;
- BH005/BH010 peak core damage is predominantly side/end triggered;
- BH020 is a mixed transition case;
- maximum steel-shell PEEQ in the unified R02 cases lies at x=±B/2 boundary and is not explained by the global Marguerre wave alone;
- theory currently lacks a fully frozen local-panel coordinate identity for unique elementwise comparison with shell PEEQ.

Thus failure-mode agreement remains **qualitative partial agreement**, not verified equivalence.

## 3. T120 mode-label correction

Canonical T120/T360 geometry is approximately

\[
b=1600\rm\ mm,\qquad a_{phys}=3000\rm\ mm.
\]

The R02 imperfection contains two longitudinal halfwaves. The old theory summary text labelled T120 as m*=1, but the audited numerical coefficient branch is much more consistent with m=2. Therefore:

```text
T120_TEXT_MSTAR_1 = DOCUMENT_LABEL_SUSPECT
T120_NUMERICAL_BRANCH = CONSISTENT_WITH_MSTAR_2
```

This is a documentation/geometry-contract issue, not permission to choose m from FEM peak load.

## 4. BH web-height geometry correction status

The report identifies the most important current geometry mismatch:

- canonical PBL height ≈41 mm;
- external shell thickness =4 mm;
- core range ≈±21 mm;
- net steel height inside the core is therefore closer to **37 mm**;
- the current BH theory table used **32 mm**, likely double-deducting a gap/clearance.

The old BH theoretical web area was

\[
A_{w,32}=9\times4\times32=1152\rm\ mm^2.
\]

The geometry-rebase candidate is

\[
A_{w,37}=9\times4\times37=1332\rm\ mm^2.
\]

For tc=42 mm this would imply candidate web ratios:

|Case|B mm|rho_w(32 mm)|rho_w(37 mm candidate)|
|---|---:|---:|---:|
|BH005|250|10.9714%|12.6857%|
|BH010|500|5.4857%|6.3429%|
|BH020|1000|2.7429%|3.1714%|
|BH032|1600|1.7143%|1.9821%|
|BH050|2500|1.0971%|1.2686%|

Critical identity rule:

```text
BH_32MM_WEB_HEIGHT = SUPERSEDED_AS_VALIDATION_GEOMETRY
BH_37MM_WEB_HEIGHT = STRONGLY_INDICATED_REBASE_CANDIDATE
BH_37MM_FINAL_GEOMETRY_CONTRACT = NOT_YET_FORMALLY_VERIFIED_HERE
```

The uploaded Codex report **does not provide a new 37-mm BH Pu table**. Its theory-vs-Abaqus table still uses the old 32-mm theory values. Therefore those old BH Pu values must not be mislabeled as geometry-corrected validation values, and no invented 37-mm Pu values are introduced in this audit.

## 5. Material-contract mismatches

The report also identifies:

- theory UHPC Poisson ratio currently 0.20 versus FEM UC141 elastic card 0.30;
- FEM tensile curve onset around 5.57 MPa versus current theory crack/tension anchor around 9.77 MPa;
- FEM Q355 uses segmented post-yield hardening whereas the current theory uses an R-O/plateau-style steel capacity treatment;
- R02/R03 boundary/contact contracts are not identical to the analytic idealization; R03 additionally contains contact warnings.

Therefore the present 1–3% peak differences cannot be used to backfit any of these parameters.

## 6. Unified multiaxial gate implication

The newly formalized UMCG is the correct place to handle cross-material constraint effects:

\[
\text{structural resultants}
\to
\text{phase stress recovery}
\to
\text{NC/UHPC/steel material admissibility}
\to
\text{section capacity}.
\]

For T120/T360, the previous 2D precheck remains useful as a working screen, but because UHPC material cards and theory/FEM contracts differ, it is not a final validation.

For BH005–BH050, geometry must be rebaselined before quantitative UMCG validation. Multiaxial conclusions based on the old 32-mm section are not promoted to production.

## 7. Current decision

```text
CODEX_REPORT_STATUS = ANALYZED_NOT_VERIFIED
BH005_BH032_PEAK_SCALE_AGREEMENT = ENCOURAGING_BUT_NOT_VALIDATED
BH050_EQUAL_CONTRACT_COMPARISON = NO
BH_32MM_CAPACITY_TABLE = HISTORICAL_GEOMETRY_MISMATCHED_COMPARATOR
BH_GEOMETRY_REBASE = REQUIRED
T120_MSTAR_LABEL = REPAIR_REQUIRED
FEM_BACKFIT = PROHIBITED
```

The next SUHPC production comparison must begin from a frozen canonical geometry/material contract, then run the same UMCG used for NC and SC.