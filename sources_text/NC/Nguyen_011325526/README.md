# Nguyen — Reinforced-concrete panel/wall source mirror

## Evidence identity

- authoritative PDF: `Nguyen-011325526.pdf`
- PDF pages: `340`
- PDF bytes: `34860966`
- PDF SHA-256: `de4369d427540716e965bd9188ef0aaac77146eab3f054a433703f772e20111e`
- extraction method: `pdftotext -layout`
- full extracted TXT bytes: `455954`
- full extracted TXT SHA-256: `cb1bd34ca0c0ccb6eb0abfeb7e0151da56baad0b3a228b9dddb8ca60512938f4`

The PDF is authoritative. GitHub TXT files are searchable mechanical/normalized mirrors and must not be treated as a substitute for the PDF when equation glyphs, subscripts, figures or page layout matter.

## Priority source regions

| source region | frozen extracted-text line range | bytes | SHA-256 | GitHub status | project role |
|---|---:|---:|---|---|---|
| Chapter 3 | 3069–5051 | 57186 | `fa35797006ef4834b631bfde03cdc041c59ae13fdcacdc8c8b9e2dcf845ce32b` | **FULL SEARCHABLE MIRROR 7/7** | biaxial concrete states, tangent/secant relations, reinforcement |
| Chapter 4 | 5052–6272 | 37111 | `5ad40a84c886c1c46ef6625f4945bb715f9a43b4a422d080bbcbbc9e31430840` | **FULL SEARCHABLE MIRROR 4/4** | Q4/Hermite/discrete-rebar stability formulation, `K+S`, 9-point Gauss, critical-load search |
| Chapter 6 | 8448–10060 | 46042 | `edd9ad9551afd6d84b9fba96e6353067c5d4269f2836c6a965a8c52bdc20c0cf` | **FULL SEARCHABLE MIRROR 5/5** | imperfection/eccentricity, second-order kinematics, full layered formulation and approximate route |
| Appendix B | 12581–15437 | 74435 | `39079268da5513bd3c20419e5732580d3b3b54e836926317d026672b534d2da1` | **PENDING — 8 planned chunks** | original FORTRAN/program-source provenance |

The line ranges refer to the frozen `pdftotext -layout` extraction, not PDF page numbers.

## Chapter 3

`CH3/part_01.txt` … `part_07.txt` now form a complete searchable Chapter-3 mirror. The high-priority material core `3.4–3.6` is also separately duplicated under `CH3_MATERIAL_CORE/` for fast retrieval.

Source structure retained:

- 3.4.1 Undamaged Concrete
- 3.4.2 Cracked Concrete in Tension-Compression
- 3.4.3 Cracked Concrete in Tension-Tension
- 3.4.4 Crushed Concrete in Compression-Compression
- 3.4.5 Crushing of Cracked Concrete
- 3.5 Constitutive Relationship for Reinforcement

The GitHub text-transfer layer normalizes some extracted characters/newline details, so the frozen local slice SHA above remains the source identity; the mirror is certified for search/recovery, not as a byte-exact replacement for the PDF.

## Chapter 4

`CH4/part_01.txt` … `part_04.txt` are complete. This preserves the historical numerical source architecture explicitly, including:

- four-node 16-DOF plate element;
- discrete 2-node reinforcement beam elements;
- tangent stiffness plus stability matrix;
- nine-point Gauss integration;
- load stepping and determinant-based critical-load search;
- buckled-mode recovery.

This is source/provenance evidence. It does **not** authorize Gauss/material-point discretization in the current formal zero-spatial NZ-SCCM operator.

## Chapter 6

`CH6/part_01.txt` … `part_05.txt` are complete. The mirror preserves an important historical distinction often lost in later summaries:

1. Nguyen derives a coupled layered formulation in which in-plane/out-of-plane behaviour and nonlinear material states can interact;
2. the thesis then states that the full nonlinear solution of that coupled equation was not realised because of time limitations;
3. the implemented route adopts an approximate tangent-modulus solution with small imperfection/eccentricity and uncracked/parabolic-through-thickness assumptions, with nine-point Gaussian integration.

Therefore later project “Branch C” reconstructions must be distinguished from what Nguyen actually implemented and documented in Chapter 6.

## Historical-project boundary

Nguyen is a **primary literature source and numerical-source oracle**. Later NZ-SCCM governance may reuse the source physics/material equations while rejecting the FE/Gauss/material-point implementation as the formal production operator. Project current-state operators derived from Nguyen/Foster are project transformations and must not be represented as verbatim Nguyen equations without source support.

## Remaining Nguyen migration

1. `APPENDIX_B/` — 8 chunks, highest remaining priority because it contains original program provenance;
2. optional full-thesis remainder outside Chapters 3, 4, 6 and Appendix B — about `241180 bytes`, useful for archival completeness but lower priority than Appendix B;
3. byte-exact PDF upload remains pending until a proper binary push/upload channel is available.

Current status: `CH3_COMPLETE; CH4_COMPLETE; CH6_COMPLETE; APPENDIX_B_PENDING`.
