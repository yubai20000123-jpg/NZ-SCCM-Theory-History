# Multiwave Steel Shell 03 R02 — fixed-m=2 PBL-kps recalculation for BH032/BH050

Status: DIAGNOSTIC. Production R14 unchanged.

This execution uses the corrected theory file:

`semantic_v2/20_theory/20260904__NZSCCM__MULTIWAVE_STEEL_SHELL_03_FIXED_M2_PBL_KPS_DISTRIBUTED_PARTIAL_INTERACTION_R02.md`

## 1. Fixed global-mode rule

The BH global longitudinal halfwave count remains

\[
\boxed{m=2}
\]

throughout. No new mode minimization is performed.

Therefore

\[
L_G=a/2=b,
\]

and the standard local candidates remain

\[
\boxed{n=3,4,5}.
\]

## 2. PBL connector diagnostic design

The user-supplied perforated-plate shear-stiffness formula is

\[
k_{ps}=23.4\sqrt{(d-d_s)d_sE_cf_{ck}}\quad(N/mm).
\]

For this first explicit design trial:

\[
d=20\ mm,
\qquad
d_s=8\ mm,
\qquad
s_c=60\ mm=3d,
\]

\[
E_c=43400\ MPa,
\qquad
f_{ck}^{trial}=141.1\ MPa.
\]

Hence

\[
\boxed{k_{ps}=567.361478\ kN/mm/hole}
\]

and

\[
\boxed{k_{\ell,r}=k_{ps}/s_c=9.45602464\ kN/mm^2/rib}.
\]

For BH TOP 4 ribs and BOTTOM 5 ribs:

\[
\boxed{k_+=37.8240986\ kN/mm^2}
\]

\[
\boxed{k_-=47.2801232\ kN/mm^2}.
\]

These are not fitted to FEM.

## 3. Partial-interaction condensed coefficients

### BH032

\[
h_+=-2.84441442\ mm,
\]

\[
h_c=+0.13199326\ mm,
\]

\[
h_-=+2.54812252\ mm.
\]

Equivalent retained pure-y-curvature lever fractions:

\[
\gamma_{+,eq}=0.87632981,
\qquad
\gamma_{-,eq}=0.88921206.
\]

Fixed-mode condensed critical load:

\[
\boxed{P_{cr}^{m=2}=29.43274796\ MN.}
\]

### BH050

\[
h_+=-1.90240702\ mm,
\]

\[
h_c=+0.09152285\ mm,
\]

\[
h_-=+1.70183181\ mm.
\]

Equivalent retained lever fractions:

\[
\gamma_{+,eq}=0.91728665,
\qquad
\gamma_{-,eq}=0.92600731.
\]

Fixed-mode condensed critical load:

\[
\boxed{P_{cr}^{m=2}=19.08106647\ MN.}
\]

## 4. Local-bay implementation

Standard bays remain:

- TOP: 3/4/5;
- BOTTOM: 3/4/5/4.

TOP edge bays are each 0.1625b and use their own count

\[
n_e=\lfloor L_G/(0.1625b)\rfloor=6.
\]

BOTTOM edge bays are each 0.05b and use

\[
n_e=20.
\]

Every edge bay now runs the same \(\sigma_{cr}^E\) gate as a standard bay.

For BH032 TOP edges:

\[
\sigma_{cr,e}=470.50\ MPa>355\ MPa,
\]

so the edge remains yield-first.

For BH050 TOP edges:

\[
\sigma_{cr,e}=192.72\ MPa<355\ MPa,
\]

so the edge is local-first. This corrects the old 01/02 assumption that all TOP edge width was automatically E/yield-first.

## 5. Connected material-boundary roots

The current first recalculation keeps the existing first-local-yield-capped R06 reduced operator. During the nonlinear root solve the R06 extremum was screened on a 41×41 u-v grid only as a numerical accelerator; every reported endpoint branch was then rechecked with continuous u-v optimization. The continuous recheck changed the controlling local VM values by at most about 0.013 MPa, so the listed loads are unaffected at the shown precision.

### BH032

Solution:

\[
\boxed{\varepsilon_x^0=1.51852\times10^{-4}}
\]

\[
\boxed{\kappa_x=2.07852\times10^{-5}\ mm^{-1}}
\]

\[
\boxed{\varepsilon_y^0=-2.45879\times10^{-3}}
\]

\[
\boxed{\kappa_y=4.99343\times10^{-5}\ mm^{-1}}
\]

\[
\boxed{q_u=0.00153875}
\]

and

\[
\boxed{P_u^{03R02}=11.28397\ MN.}
\]

Face mean stresses:

\[
\boxed{(\bar\sigma_x^+,\bar\sigma_y^+)=(+52.54,-280.40)\ MPa}
\]

\[
\boxed{(\bar\sigma_x^-,\bar\sigma_y^-)=(-69.12,-295.23)\ MPa.}
\]

Relative to the current FEM peak 10.884984 MN, the post-hoc error is approximately

\[
\boxed{+3.67\%}.
\]

### BH050

Solution:

\[
\boxed{\varepsilon_x^0=3.35443\times10^{-5}}
\]

\[
\boxed{\kappa_x=4.65463\times10^{-5}\ mm^{-1}}
\]

\[
\boxed{\varepsilon_y^0=-2.09063\times10^{-3}}
\]

\[
\boxed{\kappa_y=6.74677\times10^{-5}\ mm^{-1}}
\]

\[
\boxed{q_u=0.00554205}
\]

and

\[
\boxed{P_u^{03R02}=13.78281\ MN.}
\]

Face mean stresses:

\[
\boxed{(\bar\sigma_x^+,\bar\sigma_y^+)=(+201.58,-83.20)\ MPa}
\]

\[
\boxed{(\bar\sigma_x^-,\bar\sigma_y^-)=(-80.64,-244.88)\ MPa.}
\]

Relative to the current FEM peak 12.572657 MN, the post-hoc error is approximately

\[
\boxed{+9.63\%}.
\]

## 6. Interpretation

The corrected PBL-based stiffness is much larger than the previous trial stiffness scale of 75.835 kN/mm/rib. Consequently the distributed partial-interaction condensation remains close to the no-slip limit:

- BH032 retains about 88% of the pure-y steel-face curvature lever action;
- BH050 retains about 92%.

Thus the large reduction previously observed in Multiwave-02 is not reproduced when the user-supplied PBL stiffness formula is used with a plausible small-hole design.

This is a physically useful result. It indicates that the connector stiffness should now be treated as a genuine PBL design property rather than a free reduction parameter.

The next acceptable operation is not to change m. The next parameter study, if needed, should keep m=2 and examine only defensible PBL details \((d,d_s,s_c,f_{ck})\), or replace the current trial values with the actual test/model PBL geometry when available.
