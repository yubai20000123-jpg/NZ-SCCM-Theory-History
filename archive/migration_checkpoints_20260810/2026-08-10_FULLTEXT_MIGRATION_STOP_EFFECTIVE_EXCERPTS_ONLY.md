# Checkpoint — Stop full-text migration; effective excerpts only

**Date:** 2026-08-10

## User decision

The project no longer pursues full-text GitHub mirroring of every PDF. Only source portions with direct theoretical, material, experimental, numerical-provenance or historical-decision value are to be uploaded.

## Immediate cancellations

The following previously planned bulk jobs are cancelled as default tasks:

- Nguyen Appendix B — no automatic 8-chunk full migration;
- Nguyen remaining non-core thesis chapters — no automatic ~26-chunk migration;
- Sun Lipeng thesis — no automatic ~59-chunk full migration;
- Hiew / Liu / Lee / Leutbecher / Shen / FHWA — no automatic whole-paper text mirrors.

These sources remain registered by filename, File Library ID, SHA/URL/DOI where available. Relevant portions are extracted only when needed.

## Existing full mirrors

Do not delete already migrated mirrors. They remain useful retrieval assets:

- 周俊;
- 王淑楠;
- 胡文旭;
- Attard;
- 张宁;
- 云露;
- Nguyen Chapter 3, Chapter 4, Chapter 6 and Chapter-3 material core.

## New completion criterion

Migration is considered sufficiently complete when:

1. every core source has a reliable locator;
2. all formulas/parameters/state definitions/experimental values actually used by the project have provenance-rich excerpts;
3. historical route changes can be reconstructed from original dialogue/response/audit evidence;
4. current theory can be recovered without loading the entire conversation or full literature corpus.

Full-text percentage is no longer a project metric.

## Next source-excerpt priorities

1. Nguyen Appendix B — only RECAP/material-update/stability routines and variables actually cited by the N-module / current-operator provenance;
2. Sun Lipeng — only PBL local-buckling, elastoplastic/Ramberg–Osgood/Bleich, boundary/half-wave/design-theory parts relevant to Y-shell development;
3. Hiew — tensile law stages and 2% fibre material parameters/data actually used or audited;
4. Liu / Lee / Leutbecher — biaxial TC/TT paths, sequential/path-dependence evidence, strength and softening relations needed for UHPC operator design;
5. 周俊 / 王淑楠 — triaxial strength/failure equations already in full mirrors, to be distilled into compact formula/parameter excerpts;
6. 云露 — large-deflection membrane/Galerkin/post-buckling equations and empirical-effective-width boundary, distilled from existing full mirror.

## Governing files

- `EFFECTIVE_SOURCE_EXCERPT_POLICY.md`
- `SOURCE_OF_TRUTH_POLICY.md`
- `RECOVERY_PROTOCOL.md`
- `START_HERE.md`

This checkpoint supersedes earlier plans that measured progress by remaining full-text chunks.
