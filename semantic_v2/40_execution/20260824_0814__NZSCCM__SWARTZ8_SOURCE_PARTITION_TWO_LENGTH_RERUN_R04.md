# NZ-SCCM — Swartz8 source-partition two-length Ny–My rerun R04

**Time:** 2026-08-24 08:14 +08:00  
**Status:** `EXECUTED / AIRY_UNCHANGED / AXIAL_CUT_Ny_My_UNCHANGED / NO_ADJACENT_NAVIER_ASSUMPTION / SOURCE_SEMANTICS_EXPLICIT`

## 0. Scope

Only Cases `{4,5,6,8,9,14,21,23}` are rerun. The R03 full-2D Marguerre–Airy front end and axial `y`-normal `Ny-My` resultant terminal are unchanged. No material-point law, no experimental failure load in root selection, and no parameter fitting are introduced.

This run responds to the instruction to evaluate both physical longitudinal partition lengths instead of retaining only one length. It does **not** manufacture a neighboring Navier mode.

## 1. Source semantic audit before calculation

Swartz–Rosebraugh–Berman (ACI Journal, 1974) Table 2 labels the relevant column **Buckling location**, not wavelength. The source entries are:

- Case 4: `Bottom 1/3`
- Case 5: `Top 2/3 and bottom 1/3`
- Case 6: `Top 1/3`
- Case 8: `Top 1/4`
- Case 9: `Top 1/3`
- Case 14: `Middle`
- Case 21: `Top 1/2 and bottom 1/2`
- Case 23: `Top 1/3`

The same paper states that some panels approximately formed two square bulges, but in general panels tended to bulge in one panel, with Plate 6 as the representative one-bulge profile. Therefore the fractional Table-2 entry cannot be silently renamed an exact sinusoidal wavelength.

Nguyen later reports a group-level FE morphology: Panels 17–24 have two sinusoidal half waves, while panels in the lower-slenderness first two groups have approximately one half sinusoidal wave. Panel 21 FE shape is stated to be similar to the experiment; Panel 14 is shown as a representative approximately one-halfwave case.

Accordingly this R04 distinguishes two evidence levels:

1. `REPORTED_FRACTION`: the fraction printed in Swartz Table 2.
2. `FULL_LENGTH_COMPLEMENT`: the arithmetic remainder of the 2440-mm panel length. This is calculated because the user requested the two physical partitions, but is **not claimed to be a separately source-named second bulge** unless the table itself lists both regions (Cases 5 and 21).

No `a/m` adjacent-mode construction is used.

## 2. Length ledger used in this diagnostic

Using the project-frozen physical length `a=2440 mm`:

|Case|Table-2 entry|Length 1 / mm|Length 2 / mm|Evidence qualification|
|---:|---|---:|---:|---|
|4|Bottom 1/3|813.333|1626.667|1/3 explicit; 2/3 is full-length complement|
|5|Top 2/3 and bottom 1/3|1626.667|813.333|both explicit in Table 2|
|6|Top 1/3|813.333|1626.667|1/3 explicit; 2/3 is complement|
|8|Top 1/4|610.000|1830.000|1/4 explicit; 3/4 is complement|
|9|Top 1/3|813.333|1626.667|1/3 explicit; 2/3 is complement|
|14|Middle|2440.000|—|single full-length approximately-one-halfwave interpretation retained from Nguyen group/Fig.5.8; Table 2 itself gives no fraction|
|21|Top 1/2 and bottom 1/2|1220.000|1220.000|both explicit; numerically identical|
|23|Top 1/3|813.333|1626.667|1/3 explicit; 2/3 is complement|

## 3. Calculation equations

For each candidate length `ell`, regenerate all wavelength-dependent Airy coefficients:

\[
\alpha=\pi/b,\qquad \beta=\pi/\ell,
\]

\[
P_{cr}=\frac{b(D_x\alpha^4+2H\alpha^2\beta^2+D_y\beta^4)}{\beta^2}\frac1{1000},
\]

\[
K_y=\frac{b^2\beta^2\Delta_A}{8A_{11}},\qquad
C=\frac b{2000}\left(K_y+K_x\frac{\alpha^2}{\beta^2}\right),
\]

\[
J_y=b(D_\mu\alpha^2+D_y\beta^2).
\]

Then

\[
P(q)=P_{cr}\frac{q}{q+q_0}+Cq(q+2q_0),
\]

\[
n(q)=-N_y(q)=\frac{1000P(q)}b-K_yq(q+2q_0),
\]

and the same R03 axial-cut capacity is used:

\[
c_L=n/f_c,\qquad c_U=\min[t,(n+F_s)/f_c],\qquad c^*=\operatorname{clip}(h+z_+,c_L,c_U),
\]

\[
M_y^u=f_cc^*(h-c^*/2)+z_+(f_cc^*-n),
\]

with the unique admissible positive root

\[
M_y^u[n(q)]-J_yq=0.
\]

`Pf` is evaluated only after the root is fixed.

## 4. Rerun results

|Case|ell / mm|role|q_u|Pu / kN|Pf / kN|error|active branch|
|---:|---:|---|---:|---:|---:|---:|---|
|4|813.333|reported 1/3|0.0020347511|595.536|534.231|+11.48%|T=Fs|
|4|1626.667|complement 2/3|0.0030424916|679.190|534.231|+27.13%|T=0|
|5|1626.667|reported top 2/3|0.0033869454|650.215|623.641|+4.26%|T=0|
|5|813.333|reported bottom 1/3|0.0022146864|568.598|623.641|-8.83%|T=Fs|
|6|813.333|reported 1/3|0.0028981615|621.074|691.698|-10.21%|T=Fs|
|6|1626.667|complement 2/3|0.0048075911|717.181|691.698|+3.68%|T=0|
|8|610.000|reported 1/4|0.0014110262|521.237|455.053|+14.54%|T=Fs|
|8|1830.000|complement 3/4|0.0032869138|623.193|455.053|+36.95%|T=0|
|9|813.333|reported 1/3|0.0014051167|592.150|625.865|-5.39%|T=0|
|9|1626.667|complement 2/3|0.0018628990|650.922|625.865|+4.00%|T=0|
|14|2440.000|single full-length|0.0009578539|766.430|716.164|+7.02%|T=0|
|21|1220.000|reported top half|0.0095907312|408.081|368.313|+10.80%|T=0|
|21|1220.000|reported bottom half|same|408.081|368.313|+10.80%|T=0|
|23|813.333|reported 1/3|0.0036650017|367.811|346.961|+6.01%|T=0|
|23|1626.667|complement 2/3|0.0078694718|482.939|346.961|+39.19%|T=0|

## 5. What this calculation does and does not prove

The longer partition materially changes the prediction. In particular Cases 5, 6 and 9 become close to experiment on the longer partition (+4.26%, +3.68%, +4.00%), whereas Cases 4, 8 and 23 become strongly high (+27.13%, +36.95%, +39.19%). No experimental load was used to choose these branches.

For Cases 5 and 21 both spatial regions are explicitly named in the original Table 2, so the two-region input is source-closed at the region level. For Cases 4, 6, 8, 9 and 23 only one fractional buckling location is explicitly named; calculating the complementary remainder is a transparent full-length partition diagnostic, not evidence that the original authors identified a second independent sinusoidal halfwave of exactly that length.

Therefore no rule such as `pick whichever Pu is nearer Pf` is allowed. If the production model is to treat both unequal lobes simultaneously, the next structural step would have to define how the two source partitions coexist/couple in the global postbuckling field. This R04 intentionally stops before that new theory choice.

## 6. Gate

```text
SWARTZ8_TWO_LENGTH_RERUN = EXECUTED
ADJACENT_NAVIER_WAVELENGTH_GUESS = PROHIBITED
TABLE2_BUCKLING_LOCATION_RENAMED_AS_EXACT_WAVELENGTH = PROHIBITED
REPORTED_FRACTION_CALCULATION = PASS
FULL_LENGTH_COMPLEMENT_DIAGNOSTIC = PASS_WITH_SOURCE_QUALIFICATION
PF_USED_FOR_ROOT_OR_LENGTH_SELECTION = NO
AIRY = UNCHANGED
TERMINAL = Ny_My_UNCHANGED
NEXT_THEORY_CHANGE = NOT_EXECUTED
```
