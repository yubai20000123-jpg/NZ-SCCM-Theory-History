# Execution checkpoint — Zhou reduced rigidity and steel-tangent-loss diagnostic

Date: 2026-08-14 16:06 +08:00

## 0. Scope

This checkpoint continues the current Zhou discrepancy diagnosis. It does **not** reopen Yang specimens, does not calibrate any material/structural parameter, and does not relabel the historical `P_NZ_diag = 26.1085 MN` as a production `Rq=0 + L=0` root.

The purpose is to answer two narrower questions:

1. how much of the reduced wall elastic bending rigidity is carried by the two outer steel faceplates;
2. whether loss of steel current tangent at yield is large enough, in scale, to explain the remaining Zhou-theory versus NZ diagnostic gap.

## 1. Source-corrected reduced reference

Reduced object retained from the prior Zhou Table 5.1 checkpoint:

```text
a = b = 6000 mm
h = 130 mm
ts = 4 mm each faceplate
Ac = 6000*(130-8) = 732000 mm2
As = 2*6000*4 = 48000 mm2
fy = 355 MPa
fcu = 40 MPa
fc' = 0.76*fcu = 30.4 MPa
Psteel,0 = 17.0400 MN
Pconcrete,0 = 22.2528 MN
Pyth,reduced = 39.2928 MN
P_NZ,diag = 26.1085 MN   [historical diagnostic branch-peak neighbourhood only]
```

Direct Zhou-source material moduli for the corresponding `fy=355 MPa, fcu=40 MPa` parametric family are:

```text
Es = 206000 N/mm2
Ec = 32500 N/mm2
```

This corrects the earlier transient summary value for `Ec`.

## 2. Source-grounded DSCW E*I decomposition

For the web-deleted double-skin sandwich degeneration, the per-unit-width second moments about the midplane are

\[
I_c=\frac{(h-2t_s)^3}{12}=151320.666666667\ \mathrm{mm^3},
\]

\[
I_s=\frac{h^3-(h-2t_s)^3}{12}=31762.666666667\ \mathrm{mm^3}.
\]

Hence

\[
D_c=E_c I_c=4.917921666667\times10^9\ \mathrm{N\,mm},
\]

\[
D_s=E_s I_s=6.543109333333\times10^9\ \mathrm{N\,mm},
\]

\[
D_{EI}=D_c+D_s=1.146103100000\times10^{10}\ \mathrm{N\,mm}.
\]

The exact stiffness shares are therefore

\[
w_c=D_c/D_{EI}=0.429099412319,
\]

\[
w_s=D_s/D_{EI}=0.570900587681.
\]

Thus the two 4-mm faceplates provide **57.09% of the reduced object's E*I bending rigidity** even though their gross area is much smaller than the concrete core area. This is because they lie at the outer fibres.

The previously used scalar value

\[
D_{red}=11.461031\times10^9\ \mathrm{N\,mm}
\]

is therefore reclassified: it is not an arbitrary surrogate for `Dx/Dy`; it is the source-grounded `E_s I_s + E_c I_c` DSCW bending-rigidity degeneration. The full source-exact `H=Dxy+Dmu` of the web-deleted object is still not claimed closed in this checkpoint.

## 3. Isotropic square diagnostic baseline

Only as the same square isotropic degeneration used in the prior sensitivity calculation,

\[
P_{cr,0}=\frac{4\pi^2 D_{EI}}{b}=75.4105613324\ \mathrm{MN}.
\]

With `Pyth,reduced = 39.2928 MN`, this gives

\[
\lambda_0=\sqrt{P_{yth}/P_{cr,0}}=0.7218389\ldots
\]

and reproduces the prior comparator scale.

This `Pcr,0` remains a reduced isotropic diagnostic until `H` is rederived directly from Zhou Eq. (2-12)/(2-18)/(2-19) for the web-deleted object.

## 4. Steel tangent-loss envelope

Define tangent-retention factors relative to the source elastic moduli:

\[
\eta_c=E_{c,t}/E_c,\qquad \eta_s=E_{s,t}/E_s.
\]

For the bending-rigidity part alone,

\[
\frac{D_t}{D_{EI}}
=w_c\eta_c+w_s\eta_s
=0.429099412319\eta_c+0.570900587681\eta_s.
\]

Under the same square isotropic diagnostic scaling,

\[
\frac{P_{cr,t}}{P_{cr,0}}=w_c\eta_c+w_s\eta_s.
\]

If concrete were still elastic (`eta_c=1`) while the ideal elastic-perfectly-plastic steel entered plastic loading (`eta_s=0`), then

\[
P_{cr,t}=32.3586275504\ \mathrm{MN}.
\]

This is a **57.09% loss of the elastic bending-stability scale** solely from loss of steel material tangent. Steel axial stress/force need not vanish; only the material-tangent contribution is removed in this envelope.

Representative retention map:

| eta_c | eta_s | Pcr/Pcr0 | Pcr / MN |
|---:|---:|---:|---:|
|1.00|1.00|1.000000|75.4106|
|1.00|0.75|0.857275|64.6476|
|1.00|0.50|0.714550|53.8846|
|1.00|0.25|0.571825|43.1216|
|1.00|0.00|0.429099|32.3586|
|0.75|1.00|0.892725|67.3209|
|0.75|0.75|0.750000|56.5579|
|0.75|0.50|0.607275|45.7949|
|0.75|0.25|0.464550|35.0320|
|0.75|0.00|0.321825|24.2690|
|0.50|0.50|0.500000|37.7053|
|0.50|0.00|0.214550|16.1793|

## 5. Inverse-equivalent tangent requirement

The prior inverse diagnostic showed that matching the historical NZ diagnostic level through Zhou's theory-derived curve corresponds to

\[
P_{cr,eq,theory}=40.78637777\ \mathrm{MN}
\]

or

\[
r_{theory}=P_{cr,eq,theory}/P_{cr,0}=0.540857633856.
\]

If the concrete tangent were still fully elastic (`eta_c=1`), the steel tangent retention required to give exactly this bending-stability ratio is

\[
\eta_s
=\frac{r_{theory}-w_c}{w_s}
=0.195757762295.
\]

That is only about **19.58% of the elastic steel modulus**.

For the more aggressive FE-fit inverse comparator,

\[
P_{cr,eq,fit}=33.92124405\ \mathrm{MN},
\qquad r_{fit}=0.449820866609,
\]

and with `eta_c=1` the equivalent steel tangent retention is

\[
\eta_s=0.036296081555.
\]

Hence a transition from elastic steel tangent to the current ideal-EP plastic-loading tangent (`eta_s -> 0`) is easily large enough in **order of magnitude** to cross both inverse-equivalent stability scales. This is a mechanism-scale diagnostic, not yet a proof that the production NZ root is triggered exactly at first steel yield.

If concrete itself has already degraded, the steel tangent required to maintain the same total ratio increases. For the Zhou-theory inverse ratio:

| eta_c | required eta_s |
|---:|---:|
|1.00|0.19576|
|0.90|0.27092|
|0.80|0.34608|
|0.75|0.38366|
|0.60|0.49641|
|0.50|0.57157|

Thus the combination `concrete tangent degradation + steel ideal-EP tangent collapse` can reduce current stability substantially faster than a strength-only comparison suggests.

## 6. Elastic convention cross-check

Using a standard plane-stress tangent convention only as a comparison (`nu_c=0.20`, `nu_s=0.30`), the normal tangent factors would be `E/(1-nu^2)`. This gives

\[
D_{11,ps}=1.231306510607\times10^{10}\ \mathrm{N\,mm}
=1.07434184D_{EI},
\]

and the same square-isotropic diagnostic scale would be about

\[
P_{cr,ps}=81.01672104\ \mathrm{MN}.
\]

Therefore the elastic `E*I` versus plane-stress tangent convention difference is only about `+7.43%` and acts in the direction of **increasing**, not decreasing, the NZ elastic stability scale. It cannot by itself explain a 15–22% low NZ ultimate result.

## 7. Current mechanism diagnosis

The strongest present diagnosis is now more specific:

1. Comparator identity accounts for a material part of the apparent discrepancy: using Zhou's theory-derived Eq. 5-89/5-90 instead of transferring the full-MCFSTW FE lower-envelope fit reduces the gap from about 21.90% to about 15.62%.
2. In the web-deleted reduced section, outer faceplates supply 57.09% of E*I bending rigidity.
3. The Table-5.1 reference is yield-first under the current Yun local gate; therefore the elastic Yun postbuckling branch is not activated before first yield.
4. Current ideal elastic-perfectly-plastic closure then permits high steel axial force while the plastic-loading material tangent falls to zero.
5. Removing the steel tangent alone reduces the bending-stability scale from 75.41 MN to 32.36 MN in the reduced isotropic envelope — a change larger than that required by the inverse-equivalent Zhou/NZ discrepancy.
6. This supplies a direct quantitative reason why a model may be **not very low in axial steel force yet very low in tangent stability**.

This is now a strong mechanism-scale explanation, but final causality still requires a newly generated production path that persists `D,q,Pc,Ps,KZ_c^mat,KZ_s^mat,KZ_geo,KZ,L` at each accepted state.

## 8. Remaining hard boundary

The historical `26.1085 MN` checkpoint does not persist the corresponding `D,q` state or component tangents. Therefore no actual `Pc/Ps/KZ` decomposition at that old point is fabricated here.

```text
ZHOU_REDUCED_DSCW_EI_REDERIVATION = PASS
ZHOU_Ec_SOURCE_CORRECTED = 32500 MPa
STEEL_EI_SHARE = 0.570900587681
CONCRETE_EI_SHARE = 0.429099412319
STEEL_TANGENT_ZERO_ENVELOPE_Pcr = 32.3586275504 MN
INVERSE_THEORY_EQUIVALENT_STEEL_TANGENT_IF_CONCRETE_ELASTIC = 0.195757762295 Es
INVERSE_FEFIT_EQUIVALENT_STEEL_TANGENT_IF_CONCRETE_ELASTIC = 0.036296081555 Es
ELASTIC_CONVENTION_MISMATCH_DOMINANT_CAUSE = NO
STEEL_TANGENT_LOSS_MECHANISM_SCALE = SUFFICIENT_TO_EXPLAIN_GAP
CAUSAL_PRODUCTION_PATH_PROOF = PENDING
HISTORICAL_26p1085_COMPONENT_DECOMPOSITION = BLOCKED_NOT_PERSISTED
CALIBRATION = NO
YANG_BRANCH = NOT_USED
```
