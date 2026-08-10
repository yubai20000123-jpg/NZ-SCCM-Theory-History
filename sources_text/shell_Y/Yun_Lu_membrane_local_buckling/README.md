# 云露 — 考虑薄膜效应的钢箱混凝土壁板局部屈曲行为研究

## Evidence identity

- authoritative PDF: `考虑薄膜效应的钢箱混凝土壁板局部屈曲行为研究_云露.pdf`
- PDF pages: `81`
- PDF size: `6109981 bytes`
- PDF SHA-256: `1fce0f9ce9058f00b2a6ddd0f6dd11faa41366816e2145348812c1a93884e897`
- extraction method: `pdftotext -layout`
- local extracted TXT size: `194496 bytes`
- local extracted TXT SHA-256: `5dc2c4cdab6329ebed748da8195fc45490e6129c6ebedea3c438a7d39cba3ea0`

The PDF is authoritative. These TXT parts are only a searchable mechanical/normalized extraction layer.

## 21-part mirror

The local extracted TXT was split at existing newline boundaries into 21 ordered chunks. Local concatenation of the 21 source chunks exactly reproduces the `194496`-byte extracted TXT and SHA-256 above.

GitHub now contains **all 21 ordered parts**: `part_01.txt` … `part_21.txt`.

### Byte-audit result

Nineteen of the twenty-one GitHub text blobs match the locally computed exact Git blob SHA. Two parts were altered at the UTF-8 text-transfer layer and are therefore retained as searchable **NORMALIZED_TEXT_MIRROR** chunks rather than being falsely labelled byte-exact:

- `part_13.txt`: local expected blob `033c5478d18cd9d05040b3ae448735b87bbc1e11`; GitHub current blob `06f694dda9e618a35ad1442f3c60fd2a49102021`.
- `part_17.txt`: local expected blob `188ef0ed0f2696fbf18a325306a25b3f3fd43308`; GitHub current blob `50cfde09ecd6a86689e6d4f3bb63fc9533cb42a1`.

All other parts were individually checked against their local expected Git blob SHA and matched. Therefore the status is:

`FULL_TEXT_MIRROR_MIGRATED_21_OF_21 / SEARCH_COMPLETE / NOT_BYTE_EXACT_AS_A_WHOLE`

The authoritative byte identity remains the original PDF SHA and the local extracted-TXT SHA recorded above. A later direct binary/git-push channel may replace the two normalized chunks with byte-exact copies; until then, no claim of whole-mirror SHA certification is made.

## Source mechanics preserved in the mirror

The searchable mirror now covers the complete thesis, including:

- free-plate small-deflection buckling background;
- von Kármán large-deflection equations;
- unilateral steel-wall constraint and assumed outward-only deflection field;
- stress-function construction and compatibility equation;
- Galerkin residual/integral equation;
- analytical post-buckling relation `px = f(A,A0)`;
- membrane-force contribution, stress redistribution and post-buckling strength;
- initial imperfection treatment;
- buckling stress / ultimate stress derivation;
- FE verification and parametric studies;
- effective-width derivation and the later empirically fitted correction coefficient `k=0.74`;
- conclusions and references.

## Project source role and boundary

This thesis is primary source material for the Y / steel-shell branch. The project retains Yun's large-deflection mechanics, one-sided restraint concept, stress-function/Galerkin derivation and post-buckling stress redistribution as theory material.

However, the thesis itself also moves from analytical derivation to an empirically corrected effective-width formula. The fitted `k=0.74` is therefore explicitly tagged **HISTORICAL_EMPIRICAL_DESIGN_CORRECTION** and is **not automatically adopted as the formal NZ-SCCM production operator**. The current project has previously rejected use of Yun's effective-width empirical correction as the formal mainline closure unless the user explicitly re-adopts it.

Likewise, finite-element discretization in Chapters 3–4 is retained as validation/source evidence, not as proof that the current formal zero-spatial NZ-SCCM operator may use spatial FE cells or integration points.
