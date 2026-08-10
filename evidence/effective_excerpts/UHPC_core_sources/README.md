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
5. `TC_AND_MULTIAXIAL_CLOSURE_BOUNDARY.md`
   - explicit list of what these sources do **not** close in the current project.

## Governing interpretation

These sources constrain different aspects of UHPC and must not be collapsed into one undocumented formula:

- Hiew: **uniaxial monotonic direct tension**;
- Liu 2024: **planar biaxial strength envelope + loading-path sensitivity**;
- Lee 2017: **TC lower-bound / independent strength trend validation**;
- Leutbecher 2020: **TC compressive-strength and stiffness reduction + model evidence**;
- Zhou / Wang thesis sources elsewhere in the repository: **triaxial/failure-surface qualification**.

A complete production material operator still requires a declared mapping from current strain/state to full stress vector and a consistent tangent. A strength envelope alone is not that operator.

No Case21/Swartz/UCFT structural ultimate load may be used to calibrate any coefficient in these source laws.
