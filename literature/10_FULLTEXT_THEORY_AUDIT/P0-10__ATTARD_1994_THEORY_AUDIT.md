# P0-10 — Attard (1994) theory audit

Evidence scope: official UNSW UNICIV Report R-339 PDF. The file opens and has 23 PDF pages including cover, but is a scan without a usable text layer. The following is a **scan-limited audit**, not a lossless equation transcription.

## A. STRUCTURAL_OBJECT

- Object: reinforced-concrete walls under axial compression; report abstract and title identify wall buckling and moment amplification.
- Boundary/loading: simply supported wall idealisations are described in the public report record; exact support variants require visual page-by-page OCR.
- Imperfection/material: report-level evidence indicates stress–strain and reinforcement/yield-moment capacity treatment; exact equations are unresolved from the scan.

## B–G. FORMULATION STATUS

- Kinematics: wall/plate buckling and amplified bending are identified, but `u,v,w,w0` mode equations cannot be reliably extracted.
- Airy: no evidence of an Airy stress function in the accessible text; mark `NO_EVIDENCE` rather than infer.
- Compatibility/transverse equilibrium: likely beam-column/plate stability formulation, but governing equation numbers are not recoverable from the scan.
- Postbuckling relation: `NO_EXPLICIT_POSTBUCKLING_RELATION` verified from the accessible text layer only; this is an evidence limitation, not a claim that the report contains none.
- Structural demand: axial load, amplified moment, wall slenderness and effective height are the identifiable demand variables.

## CAPACITY_LAYER

The report is clearly concerned with reinforcement/yield moment capacity and concrete wall stability, but the exact `N-M` surface and material law are unresolved from the scan.

## CONTROL_LOCATION_SOURCE

`UNRESOLVED` from the scan-limited evidence.

## ULTIMATE_SOLVER

`UNRESOLVED` from the scan-limited evidence; do not upgrade to a direct-root or incremental classification without OCR/equation inspection.

## EMPIRICISM_LOCATION

`UNRESOLVED`; the report's existence as a technical analytical report is verified, but formula-level attribution is not.

## VERIFIED_CLASS

`UNRESOLVED_SCAN_LIMITED`. It must not be used as FULL_TEXT_VERIFIED evidence for a specific Marguerre–Airy or finite-root claim.

## NZ_SCCM_INTERFACE_COMPARISON

Kinematics, Airy, postbuckling, `P-q`, `N-M`, control location and `Pu` closure are all `UNRESOLVED`; overlap is `LOW` for formula-level comparison until a readable copy is obtained.

## LESSONS_FOR_NZ_SCCM

The useful negative lesson is evidence discipline: a publicly downloadable PDF is not automatically a formula-auditable source. Do not infer an Airy field, direct root or empirical factor from an abstract/title alone.

