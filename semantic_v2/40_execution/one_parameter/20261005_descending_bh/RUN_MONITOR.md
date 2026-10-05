# Run monitor

BH085-BH050 old results remain quarantined. BH032 and smaller remain paused.

## BH100 UHPC status
The Poisson false-cracking correction is frozen:
eta_t_eq = positive_part(eps1 + nu_c*eps2)/(1-nu_c^2)
eta_c_eq = positive_part(-eps2 - nu_c*eps1)/(1-nu_c^2)

## BH100 steel-shell continuous local-Mises repair
The rejected whole-face single-e corrector has been replaced by a continuous local Mises-cap operator:
- correct global base pointwise if its Mises trial exceeds fy;
- add Yun/R06 local elastic increment;
- solve the explicit local quadratic Phi(g + lambda*l)=fy^2 for lambda in [0,1];
- integrate the resulting sigma_y field continuously over each face.

At w=82.15506222 mm:
- UHPC = 7.21811 MN
- TOP = about 4.935 MN
- BOTTOM = 5.43196 MN
- total = about 17.585 MN
- TOP/BOTTOM mean steel stresses are about 246.75 / 271.60 MPa, so the rejected 148 / 272 MPa whole-face split is removed.

## Repaired branch maximum
Refined first external maximum of this repaired numerical branch:
- wu about 146.33 mm
- Pu about 24.897 MN
- PUHPC about 12.1032 MN
- Ptop about 6.165 MN
- Pbottom about 6.628 MN
- steel resultant eccentricity about 0.83 mm

This is NOT accepted as the final theory result.

Reason: after removing the artificial whole-face TOP collapse, the total steel force becomes far too large. At the peak the global elastic trial exceeds yield over essentially the full area of both faces. The remaining upstream issue is now the steel predictor / mean-stress identity: Yun whole-face mean is still being used as a total face mean while the global base already carries the overall axial demand. This indicates global/local mean-level double counting or an incompatible predictor closure.

## Post-freeze comparison
Previously extracted BH100 DIRECT peak: 13.486 MN at incremental deflection about 97.392 mm.

The repaired branch:
- gives about 20.875 MN already at w=97.392 mm;
- peaks at about 24.897 MN, about 84.6 percent above DIRECT.

No FEM/test value was used in the theoretical solve.

## Decision
Do not resume BH085-BH005.
Next audit target: keep corrected UHPC and continuous local Mises cap, but re-derive the steel global-base / Yun-local mean compatibility so Yun does not duplicate the global axial demand.

Files:
- BH100_CONTINUOUS_LOCAL_MISES_RUN.md
- BH100_CONTINUOUS_LOCAL_MISES_RESULT.md
- BH100_CONTINUOUS_LOCAL_MISES_CURVE.csv
- AUDIT_BH100_STEEL_TOP_BOTTOM_ASYMMETRY.md
- BH100_STEEL_LOCAL_MISES_REPAIR_SPEC.md
