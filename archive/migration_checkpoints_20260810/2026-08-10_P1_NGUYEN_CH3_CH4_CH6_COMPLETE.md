# Checkpoint — Nguyen Chapter 3 / 4 / 6 source mirror completion

**Date:** 2026-08-10

## Completed in this batch

The Nguyen primary-source mirror now contains:

- `CH3/part_01.txt` … `part_07.txt` — full searchable Chapter 3;
- `CH3_MATERIAL_CORE/part_01.txt` … `part_04.txt` — duplicated high-priority material core 3.4–3.6;
- `CH4/part_01.txt` … `part_04.txt` — full searchable Chapter 4;
- `CH6/part_01.txt` … `part_05.txt` — full searchable Chapter 6.

Frozen local source identities remain:

- full PDF SHA-256: `de4369d427540716e965bd9188ef0aaac77146eab3f054a433703f772e20111e`;
- full `pdftotext -layout` extraction: `455954 bytes`, SHA-256 `cb1bd34ca0c0ccb6eb0abfeb7e0151da56baad0b3a228b9dddb8ca60512938f4`;
- Chapter 3: `57186 bytes`, SHA-256 `fa35797006ef4834b631bfde03cdc041c59ae13fdcacdc8c8b9e2dcf845ce32b`;
- Chapter 4: `37111 bytes`, SHA-256 `5ad40a84c886c1c46ef6625f4945bb715f9a43b4a422d080bbcbbc9e31430840`;
- Chapter 6: `46042 bytes`, SHA-256 `edd9ad9551afd6d84b9fba96e6353067c5d4269f2836c6a965a8c52bdc20c0cf`.

The GitHub UTF-8 connector normalizes some extraction details, so these mirrors are certified as **search/recovery mirrors**, not byte-exact substitutes for the PDF.

## Important source conclusion preserved

Chapter 6 itself distinguishes the theoretically derived coupled layered formulation from the implemented approximate solution: the thesis states that the full nonlinear solution of equation (6.36) was not realised because of time limitations, and then adopts an approximate tangent-modulus route under restricted assumptions. This distinction must be preserved when discussing historical Branch-C reconstruction.

## Immediate next priority

1. Nguyen `APPENDIX_B/`: `74435 bytes`, planned as 8 chunks. This is the highest-priority remaining Nguyen source because it preserves original program/FORTRAN provenance.
2. Sun Lipeng PBL/steel-shell thesis: extracted text `546279 bytes`, approximately 59 chunks at the current transfer size.
3. Optional Nguyen full-thesis remainder outside Chapters 3/4/6/Appendix B: approximately `241180 bytes` (~26 chunks). Lower priority because the repeatedly used theory regions are already preserved.

## Quantitative local-primary-source status

For the eight local primary PDFs currently extracted into searchable text:

- full searchable mirrors: 周俊、王淑楠、胡文旭、Attard、张宁、云露 = 6 files;
- Nguyen: priority Chapters 3/4/6 complete; Appendix B pending; other chapters optional for full-thesis archival completeness;
- 孙立鹏: PDF identity/SHA registered, full extracted text ready locally, GitHub text mirror pending.

Total local extracted-text corpus = `1,737,026 bytes`.
Unique source text already represented in GitHub mirrors, counting Nguyen Chapters 3/4/6 once and excluding duplicated material-core copies, is about `875,132 bytes` (~50.4% of the full eight-PDF extracted corpus). This byte percentage is intentionally conservative: it treats every page of the 340-page Nguyen thesis and 187-page Sun thesis as equally mandatory, even though current theory repeatedly uses only selected Nguyen chapters.

## Infrastructure-limited item

Byte-exact PDF binaries are not yet claimed as stored in GitHub because the current GitHub connector exposes UTF-8 content writes but no mounted-file binary upload parameter. PDF filenames, SHA-256, File Library IDs and public-source locators remain registered so evidence is not lost. A later real git/binary-upload channel should copy the authoritative PDF bytes and verify SHA-256.
