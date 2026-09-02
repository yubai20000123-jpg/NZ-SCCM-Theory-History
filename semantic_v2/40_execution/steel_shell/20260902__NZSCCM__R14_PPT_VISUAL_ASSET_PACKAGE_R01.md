# NZ-SCCM R14 — PPT VISUAL ASSET PACKAGE R01

**Date:** 2026-09-02  
**Branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Production main:** unchanged.  
**R14 mechanics:** FROZEN / NOT REOPENED.

## 1. Package identity

Local chat artifact:

`NZSCCM_R14_PPT_VISUAL_ASSET_PACKAGE_R01_20260902.zip`

SHA-256:

`1dcd995261c0126e8b789f6f1968bcdc798b79deb80e9e93ab1d9af35d254590`

The binary package is a current-chat artifact. This Git entry is the text audit/register and does not falsely claim that the zip binary itself is stored in the Git tree.

## 2. Locked asset register

|ID|Asset|Class|Source|Audit|Scale|
|---|---|---|---|---|---|
|G0-01|current UCFT exact configuration/exploded figure|G0 exact current object|UCFT manuscript Fig.1|HOLD_BINARY_EXTRACTION|GLOBAL/OBJECT|
|G0-02|gross-panel strict outline|strict reduced abstraction|R14 geometry derived|PASS|GLOBAL|
|G1-01|simply-supported axial-compression plate|G1 direct mechanics source|Yun Lu 2024 Fig.2-1|PASS|GLOBAL|
|G1-02|Karman–Airy source/equation page|G1 direct mechanics source|Yun Lu 2024|PASS|GLOBAL|
|G1-03|PBL local-buckling geometry|G1 direct mechanics source|Zhang Ning et al. 2017|PASS|LOCAL|
|G1-04|real/analogous local-buckling morphology|G2 analogous morphology|Sun Lipeng 2023 Fig.3.7|PASS_WITH_ANALOGOUS_LABEL|LOCAL|
|T-01|exact R14 2D section + strain gradients|equation-derived strict reduced diagram|R14 §7|PASS|SECTION|
|T-02|global m=1/2/3 + discrete Pcr chart|R14 equation-derived|R14 §5, BH050 inputs|PASS|GLOBAL|
|T-03|Airy derivative/membrane-resultant schematic|R14 equation-derived|R14 §6 + Yun framework|PASS|GLOBAL|
|T-04|R04 Mises locus + proportional projection|R14 equation-derived|R14 §8|PASS|LOCAL/SECTION|
|T-05|R02 Pi(U) + cubic candidates|R14 equation-derived canonical illustration|R14 §10|PASS_CANONICAL_NOT_SPECIMEN|LOCAL|
|T-06|R06 physical cell -> uv -> candidates|R14 strict mathematical diagram|R14 §11|PASS|LOCAL|
|T-07|connected branch + competing terminal + J4 fold|R14 mathematical prototype|R14 §16–19|PASS_PROTOTYPE_NOT_BH_CURVE|GLOBAL/EQUILIBRIUM|
|T-08|current UHPC compression/tension law|R14 equation-derived|R14 §12 frozen coefficients/anchors|PASS|SECTION/MATERIAL|

## 3. Package gate

`13/14` assets are locally materialized and visually audited.

The single HOLD is deliberate:

`G0-01 current UCFT exact configuration/exploded figure`.

Exact source has been identified and visually verified in the current UCFT manuscript, Fig.1, caption:

`Configuration and constituent components of the flat UCFT panel.`

The source figure shows the exact current spatial grammar required for the deck: outer steel plate, inner steel plate, UHPC core, longitudinal PBL ribs, and PBL-hole/UHPC-dowel relation.

However, the current File-Library interface exposes the rendered source but does not mount the DOCX binary into the local runtime for lossless extraction. Therefore G0-01 is intentionally left as `HOLD_BINARY_EXTRACTION`; no generated or generic sandwich geometry is substituted.

When the manuscript binary is locally mounted, the only required completion action is:

1. extract/crop original Fig.1 losslessly;
2. replace the G0-01 source-pointer note in the local package;
3. rerun the visual gate;
4. only then regenerate the PPT visual layer.

## 4. Audited package contents

Source-derived visuals:

- G1-01 Yun Lu simply-supported axial-compression plate;
- G1-02 Yun Lu Kármán–Airy equation/source page;
- G1-03 Zhang Ning PBL local-buckling geometry;
- G1-04 Sun Lipeng real local-buckling morphology, explicitly analogous only.

Equation/geometry-derived visuals:

- G0-02 strict gross-panel outline;
- T-01 exact R14 reduced section and strain gradients;
- T-02 global m=1/2/3 mode shapes + discrete Pcr,m chart using current BH050 inputs;
- T-03 Airy F -> membrane-resultant derivative relationship;
- T-04 R04 plane-stress von-Mises proportional projection;
- T-05 R02 Pi(U), cubic candidates and minimum-energy U* canonical illustration;
- T-06 R06 physical local cell -> bounded (u,v) domain -> finite interior/edge/corner candidate family;
- T-07 connected R4 branch + material-event/J4-fold competing-terminal mathematical prototype;
- T-08 exact current R14 UHPC compression domain + frozen five-anchor tension law.

PNG versions are intended for direct review; SVG versions are retained for theory-figure editing where appropriate.

## 5. Audit semantics retained

- `x = transverse`, `y = axial`, `z = thickness`.
- Airy `F` is a membrane-resultant potential, not deflection `w`.
- `q` is a connected-equilibrium-branch coordinate, not a material-history step.
- `U` is a local condensed amplitude.
- R06 `u,v` are continuous bounded-domain analytic coordinates, not material sampling points.
- terminal is a branch event.
- `A_w` remains the frozen equivalent longitudinal steel contribution; no discrete-PBL theory is introduced.
- no effective width/effective area.
- no formal spatial Gauss/material-point grid.
- no FEM/test/stored-Pu root or terminal selection.

## 6. Current continuation point

Do not rebuild the deck yet while G0-01 is HOLD.

The next admissible action is to obtain the exact current manuscript Fig.1 binary extraction, close G0-01, and then rebuild the PPT from the already locked 32-page page-to-visual mapping.
