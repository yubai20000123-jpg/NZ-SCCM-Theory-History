# P1 checkpoint — Yun Lu full mirror / Nguyen material core

**Date:** 2026-08-10

## Yun Lu

`考虑薄膜效应的钢箱混凝土壁板局部屈曲行为研究_云露.pdf`

- PDF SHA-256: `1fce0f9ce9058f00b2a6ddd0f6dd11faa41366816e2145348812c1a93884e897`
- local `pdftotext -layout` TXT: `194496 bytes`
- local TXT SHA-256: `5dc2c4cdab6329ebed748da8195fc45490e6129c6ebedea3c438a7d39cba3ea0`
- GitHub: all `part_01..part_21` present.
- byte audit: 19 chunk blobs match local exact expected Git SHA; `part_13` and `part_17` are searchable normalized-text copies and do not match the exact local blob SHA.

Formal status:

`FULL_TEXT_MIRROR_MIGRATED_21_OF_21 / SEARCH_COMPLETE / NOT_BYTE_EXACT_AS_A_WHOLE`

This is intentionally not called SHA-certified as a whole. Original PDF and frozen local extraction hashes remain source identity.

Project source boundary is retained: Kármán large-deflection mechanics, unilateral restraint, stress-function/Galerkin derivation and membrane/postbuckling mechanics remain source material; the empirical effective-width correction `k=0.74` remains historical empirical design correction, not current formal NZ-SCCM production closure.

## Nguyen source initialization

`Nguyen-011325526.pdf`

- PDF SHA-256: `de4369d427540716e965bd9188ef0aaac77146eab3f054a433703f772e20111e`
- full extracted TXT: `455954 bytes`
- full TXT SHA-256: `cb1bd34ca0c0ccb6eb0abfeb7e0151da56baad0b3a228b9dddb8ca60512938f4`

Priority source slices are now frozen in `CHAPTER_MAP.csv`:

- Chapter 3: 57186 bytes / SHA `fa357970...ce32b`
- Chapter 4: 37111 bytes / SHA `5ad40a84...30840`
- Chapter 6: 46042 bytes / SHA `edd9ad95...0c0cf`
- Appendix B: 74435 bytes / SHA `39079268...d2da1`

### Material core 3.4–3.6

Frozen source slice:

- lines `3911–5051`
- `30488 bytes`
- SHA-256 `ceef5ad5f3c6c0cbc96dc63a6fabe861782693e0a4d98739cba628bb6d64ec51`

GitHub now contains all four searchable material-core parts, covering undamaged, TC, TT, CC, crushing-after-cracking and reinforcement relations. Transfer audit is recorded in `CH3_MATERIAL_CORE/README.md`; only part 01 is byte-exact to its local expected Git blob, while parts 02–04 are explicitly normalized text mirrors.

The broader Chapter-3 mirror has started: `CH3/part_01.txt` is present (`1/7`).

## Next queue

1. finish full Nguyen Chapter 3 (`part_02..07`);
2. migrate Chapter 6 and Appendix B because they are the most important source/provenance regions for the historical N-branch;
3. migrate Chapter 4;
4. then start Sun Lipeng searchable source mirror;
5. keep binary-PDF migration pending until a real mounted-file/git-push channel exists.
