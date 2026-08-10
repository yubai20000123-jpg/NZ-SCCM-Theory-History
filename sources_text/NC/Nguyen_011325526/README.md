# Nguyen — Reinforced-concrete panel/wall source mirror

## Evidence identity

- authoritative PDF: `Nguyen-011325526.pdf`
- PDF pages: `340`
- PDF bytes: `34860966`
- PDF SHA-256: `de4369d427540716e965bd9188ef0aaac77146eab3f054a433703f772e20111e`
- extraction method: `pdftotext -layout`
- full extracted TXT bytes: `455954`
- full extracted TXT SHA-256: `cb1bd34ca0c0ccb6eb0abfeb7e0151da56baad0b3a228b9dddb8ca60512938f4`

The PDF is the authoritative literature source. GitHub TXT files are only a searchable mechanical/normalized mirror.

## Priority source sections

The project repeatedly relies on four source regions. They have been independently sliced from the full extracted TXT at original line boundaries:

| source region | extracted-text line range | bytes | SHA-256 | project role |
|---|---:|---:|---|---|
| Chapter 3 | 3069–5051 | 57186 | `fa35797006ef4834b631bfde03cdc041c59ae13fdcacdc8c8b9e2dcf845ce32b` | 2D concrete states, reinforcement constitutive relation, source material equations |
| Chapter 4 | 5052–6272 | 37111 | `5ad40a84c886c1c46ef6625f4945bb715f9a43b4a422d080bbcbbc9e31430840` | Q4/Hermite/discrete-rebar FE stability formulation and solution method |
| Chapter 6 | 8448–10060 | 46042 | `edd9ad9551afd6d84b9fba96e6353067c5d4269f2836c6a965a8c52bdc20c0cf` | initial imperfection/eccentricity, second-order wall formulation, layered/full-coupling discussion |
| Appendix B | 12581–15437 | 74435 | `39079268da5513bd3c20419e5732580d3b3b54e836926317d026672b534d2da1` | original FORTRAN/program-source provenance |

These line ranges refer to the frozen `pdftotext -layout` extraction identified by the full-TXT SHA above; they are not PDF page numbers.

## Chapter-3 source structure

The original thesis contents identify the following Chapter 3 sections:

- 3.1 Introduction
- 3.2 Wall design according to current building codes
- 3.3 theoretical/experimental RC-wall buckling research
- 3.4 Constitutive Relationship for Concrete
  - 3.4.1 Undamaged Concrete
  - 3.4.2 Cracked Concrete in Tension-Compression
  - 3.4.3 Cracked Concrete in Tension-Tension
  - 3.4.4 Crushed Concrete in Compression-Compression
  - 3.4.5 Crushing of Cracked Concrete
- 3.5 Constitutive Relationship for Reinforcement
- 3.6 Summary

The high-priority material core `3.4–3.6` is now fully present as four searchable parts under `CH3_MATERIAL_CORE/`. Its frozen local source slice is 30488 bytes with SHA-256 `ceef5ad5f3c6c0cbc96dc63a6fabe861782693e0a4d98739cba628bb6d64ec51`; the directory README records exact-versus-normalized chunk status.

The broader Chapter-3 mirror has also started under `CH3/`; `part_01.txt` is present. The full Chapter-3 frozen source identity remains the 57186-byte SHA shown above until all seven planned chunks are migrated.

## Historical-project boundary

Nguyen is a **primary source and numerical-source oracle**, but later NZ-SCCM governance does not automatically adopt Nguyen's FE architecture, Gauss/material-point discretization or history-machine implementation as the current formal operator. Current formal theory may reuse source material equations/physics while still enforcing its separate zero-formal-spatial-quadrature governance.

Similarly, later project current-state operators derived from Nguyen/Foster are project transformations; they must not be represented as verbatim Nguyen equations unless the original thesis supports them.

## Migration order

1. `CH3_MATERIAL_CORE/` — **COMPLETE searchable mirror (4/4; transfer audit recorded)**;
2. `CH3/` — full chapter, **IN PROGRESS (1/7)**;
3. `CH4/` — stability FE source formulation;
4. `CH6/` — initial-imperfection / second-order formulation;
5. `APPENDIX_B/` — original program provenance;
6. remaining thesis text if useful.

Current status: `SOURCE_IDENTITY_AND_CHAPTER_MAP_LOCKED; CH3_MATERIAL_CORE_COMPLETE; FULL_CH3_1_OF_7`.
