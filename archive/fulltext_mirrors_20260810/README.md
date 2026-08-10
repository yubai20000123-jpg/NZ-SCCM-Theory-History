# Searchable source-text mirrors

This directory is a retrieval layer, not the authoritative literature archive.

## Evidence order

`authoritative PDF > extracted text mirror > evidence note > project interpretation > stage summary`.

## Extraction rule

Where a PDF is locally available and already contains machine-readable text, use a mechanical extractor (`pdftotext -layout` unless otherwise recorded). OCR is not used unless necessary. The extracted TXT receives its own SHA-256 and is registered in `LOCAL_EXTRACTION_MANIFEST_20260810.csv`.

A text mirror may normalize PDF text layout, line wrapping, ligatures or glyph extraction. Therefore it must never be cited as proof of exact formula typography, figure geometry, superscripts/subscripts or page layout when the PDF is available.

## Current prepared mirrors

The following local PDF originals have searchable text extractions prepared and hash-registered:

- Nguyen thesis — NC/RC constitutive, reinforcement, Chapter 4 stability, Chapter 6 path source;
- Yun Lu thesis — steel-box wall local buckling / membrane effect / large-deflection source;
- Zhang Ning — PBL-stiffened rectangular steel-tube local buckling source;
- Sun Lipeng — PBL thin-wall steel-tube concrete theory and historical R-O/Bleich routes;
- Attard — reinforced-concrete wall buckling source.

Their text files are currently marked `READY_FOR_TEXT_MIRROR` in the manifest until copied through the GitHub text interface. This status is intentionally different from `FULL_TEXT_MIRROR_MIGRATED`.

## Binary originals

The PDF byte originals are still governed by `evidence/SOURCE_REGISTRY.md`. A prepared text mirror does not mean the PDF binary itself has been uploaded to GitHub.
