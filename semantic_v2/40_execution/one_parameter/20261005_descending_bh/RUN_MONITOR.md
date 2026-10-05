# Run monitor

BH085-BH050 old results remain quarantined. BH032 and smaller remain paused.

BH100 UHPC Poisson false-cracking correction trial completed, but its 15.61115 MN total result is now also provisional because the steel-shell audit found a separate whole-face plastic-corrector error.

Steel audit at w=82.15506222 mm:
- TOP Yun predictor mean axial stress = 251.08787 MPa
- BOTTOM Yun predictor mean axial stress = 271.59798 MPa
- TOP single-e Mises corrector reduces TOP whole-face mean to 148.05383 MPa
- BOTTOM remains 271.59798 MPa
- this single corrector event removes about 2.061 MN from the combined steel force
- global-only exact area-mean axial stresses are about 223.793 MPa TOP and 299.077 MPa BOTTOM
- TOP global-only outer-surface Mises first reaches 355 MPa at w about 78.688 mm; at w=82.155 mm it is about 375.43 MPa, while BOTTOM global-only max is about 337.57 MPa

Conclusion: the current implementation lets one controlling Mises point reduce a single recoverable amplitude for the entire steel face, which collapses the whole-face mean TOP stress and exaggerates TOP/BOTTOM asymmetry. Global yielding and local postbuckling plasticity are also conflated.

Next target: BH100 only. Freeze corrected UHPC. Replace the single-e whole-face corrector by a continuous local Mises-cap operator and integrate the resulting steel stress field. Do not resume smaller BH cases before this is done.

Detailed audit: AUDIT_BH100_STEEL_TOP_BOTTOM_ASYMMETRY.md
