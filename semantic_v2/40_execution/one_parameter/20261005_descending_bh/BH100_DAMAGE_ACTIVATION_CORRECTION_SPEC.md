# RETRACTED — WRONG UHPC PATH

This file is retained only as an audit artifact. It used/inherited ABS/raw UHPC damage-plastic instead of the locked PEAK-REBASED damage and plastic-initial-imperfection path. Do not use its numerical results. See RETRACTION_BH100_UHPC_PATH_REVERSION.md.

# BH100 multiaxial UHPC damage-activation correction trial

## Purpose
Only correct the identified UHPC Poisson false-cracking mechanism first. Keep all other BH100 13.40-MN numerical-path ingredients unchanged for an A/B audit. Do not use FEM/test data in the solve.

## Old driver (rejected)
[
eta_t^{old}=langlearepsilon_1angle_+,qquad
eta_c^{old}=langle-arepsilon_2angle_+.
]
This makes pure uniaxial compression ((arepsilon_1=
u e_c,arepsilon_2=-e_c)) generate false tensile damage.

## Corrected plane-stress equivalent uniaxial strain driver
In the principal axes of the total trial strain field,
[
oxed{eta_t^{eq}=
rac{langlearepsilon_1+
u_carepsilon_2angle_+}{1-
u_c^2}}
]
[
oxed{eta_c^{eq}=
rac{langle-arepsilon_2-
u_carepsilon_1angle_+}{1-
u_c^2}}
]
where (langle xangle_+=(x+|x|)/2).

Properties:
1. uniaxial tension: (arepsilon_2=-
uarepsilon_1Rightarroweta_t^{eq}=arepsilon_1);
2. uniaxial compression: (arepsilon_1=
u e_c,arepsilon_2=-e_cRightarroweta_t^{eq}=0,eta_c^{eq}=e_c);
3. (eta_t^{eq}=langlesigma_1^Eangle_+/E_c), (eta_c^{eq}=langle-sigma_2^Eangle_+/E_c) for the corresponding plane-stress elastic principal trial stress, so the sign of the principal stress—not positive Poisson strain alone—activates tension/compression.

## Material functions
Keep exactly the same ABS/raw UC141 functions already used by the BH100 13.40-MN route; only replace their multiaxial driver by (eta_t^{eq},eta_c^{eq}). Thus this trial changes one mechanism only.

## Integration identity
Theoretical definitions remain continuous area integrals for (ho_A,ho_D,w_P). Numerical evaluation is only an independent evaluator; fixed spatial material points are not part of the theory.

## Steel
For this A/B trial, keep the same BH100 predictor/corrector formulation as the 13.40-MN path. Any steel implementation uncertainty is logged separately and is not modified simultaneously with the UHPC activation correction.
