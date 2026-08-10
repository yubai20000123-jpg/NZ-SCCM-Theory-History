# Nguyen Chapter 3 — material-core searchable mirror

## Frozen local source slice

This directory mirrors the source region beginning at the actual Chapter-3 heading `3.4 CONSTITUTIVE RELATIONS... FOR CONCRETE` and continuing through the Chapter-3 reinforcement relation and summary.

- source extraction: frozen full `pdftotext -layout` mirror of `Nguyen-011325526.pdf`
- line range: `3911–5051` of that frozen extraction
- local source-slice bytes: `30488`
- local source-slice SHA-256: `ceef5ad5f3c6c0cbc96dc63a6fabe861782693e0a4d98739cba628bb6d64ec51`

The PDF remains authoritative.

## Coverage

The four ordered parts preserve searchable source text for:

- 3.4 concrete constitutive relationship and biaxial failure envelope;
- 3.4.1 undamaged concrete / equivalent-uniaxial strain framework;
- secant/tangent/shear modulus construction;
- Saenz compressive relation and tangent derivative;
- 3.4.2 cracked tension-compression state, compression softening, tension stiffening and shear retention;
- 3.4.3 cracked tension-tension state;
- 3.4.4 crushed compression-compression state;
- 3.4.5 crushing of cracked concrete;
- 3.5 bilinear reinforcement relation;
- 3.6 Chapter-3 summary.

## Transfer audit

Local exact 9500-byte-boundary split expected Git blob SHAs:

| part | local bytes | expected exact blob | GitHub current blob | status |
|---|---:|---|---|---|
| 01 | 9416 | `0446a97600d1626050d7354810c841241696c072` | `0446a97600d1626050d7354810c841241696c072` | EXACT |
| 02 | 9493 | `ae7fdf1c2ec3b8dbf6650ac69bf96ab858b4f685` | `4eb1320dfecaeb8f99a6f7984cb2cacb036bbaff` | NORMALIZED_TEXT_MIRROR |
| 03 | 9421 | `0a9b4fdcecf6c8161842911d89455aeb28e39e5c` | `b488c02e1df5238ceda7202f98573b719b266c41` | NORMALIZED_TEXT_MIRROR |
| 04 | 2158 | `4e5f347706c82eba2d6b2f8612ac6962f5dc94aa` | `4554b37588c12380545e1e407fc7f82dfd6d70b0` | NORMALIZED_TEXT_MIRROR |

Therefore this directory is tagged:

`FULL_MATERIAL_CORE_SEARCH_MIRROR / 4_OF_4 / 1_EXACT + 3_NORMALIZED`

No whole-directory byte-exact claim is made. The local source-slice SHA and authoritative PDF SHA control source identity.

## Interpretation boundary

This directory stores Nguyen source text. It does **not** assert that every OCR/text-extracted equation is visually complete: matrices, stacked fractions, subscripts and figures may be damaged or omitted by `pdftotext`. Any exact formula transcription must be checked against the PDF page.

It also does not convert Nguyen's state/history constitutive formulation into the later NZ-SCCM current operator. That conversion, when used, is a separate project-level derivation and must be cited as such.
