# UHPC core sources — effective evidence package

This directory follows `EFFECTIVE_SOURCE_EXCERPT_POLICY.md`: preserve only material evidence that constrains the UHPC operator, plus precise source locators and non-use boundaries. It is **not** a full-PDF mirror.

## Primary files in this package

1. `Hiew_2024_direct_tension.md`
   - direct tensile constitutive stages and source equations/parameter roles.
2. `Liu_2024_biaxial_strength_path.md`
   - CC/TT/TC planar strength tests, complete biaxial envelope and loading-path effect.
3. `Lee_2017_TC_validation.md`
   - independent 30-panel TC evidence for fibre tension-stiffening and compression-softening.
4. `Leutbecher_2020_TC_strength_stiffness.md`
   - independent panel evidence that transverse tension/cracking reduces both compressive strength and stiffness; source modeling role.
5. `Shen_2020_TT_equi_biaxial.md`
   - equi-biaxial tensile strength, elastic-limit and hardening-strain coordinates for TT qualification.
6. `Diab_Ferche_2026_compression_softening_synthesis.md`
   - cross-study UHPC compression-softening synthesis and `beta*f'c` modeling role.
7. `FHWA_HRT_23_077_design_locator.md`
   - official design/material-qualification terminology and parameter-range locator; auxiliary, not a replacement for material experiments.
8. `TC_AND_MULTIAXIAL_CLOSURE_BOUNDARY.md`
   - explicit list of what these sources do **not** close in the current project.

## Governing interpretation

These sources constrain different aspects of UHPC and must not be collapsed into one undocumented formula:

- Hiew: **uniaxial monotonic direct tension**;
- Liu 2024: **planar biaxial strength envelope + loading-path sensitivity**;
- Lee 2017: **TC lower-bound / independent strength trend validation**;
- Leutbecher 2020: **TC compressive-strength and stiffness reduction + model evidence**;
- Shen 2020: **TT strain-coordinate qualification**;
- Diab/Ferche 2026: **cross-study compression-softening synthesis**;
- FHWA-HRT-23-077: **official design/material qualification boundary**;
- Zhou / Wang thesis sources elsewhere in the repository: **triaxial/failure-surface qualification**.

A complete production material operator still requires a declared mapping from current strain/state to full stress vector and a consistent tangent. A strength envelope alone is not that operator.

No Case21/Swartz/UCFT structural ultimate load may be used to calibrate any coefficient in these source laws.
