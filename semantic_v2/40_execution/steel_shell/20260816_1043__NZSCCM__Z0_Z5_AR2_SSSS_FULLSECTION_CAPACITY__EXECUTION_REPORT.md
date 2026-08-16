# NZ-SCCM — Z0–Z5 AR2 theoretical four-edge simply-supported full-section capacity

**Timestamp:** 2026-08-16 10:43 +08:00  
**Status:** CURRENT PRODUCTION CALCULATION / Z6-ACCEPTED PROCESS REPLAY

## 1. Scope

The user accepted the current Z6 result `Pu=51.30 MN` and instructed Z0–Z5 to be recalculated by the same process, while changing each physical panel length so that `a/b=2`.

Production boundary:

```text
THEORETICAL_FOUR_EDGE_SIMPLY_SUPPORTED
```

No attempt is made to reproduce Zhou FE-specific `ux/uy` implementation. No PF end layer, FE boundary warp, axial-trace condensation, or free `p20,p02` coordinate enters this calculation.

## 2. Modified geometry

Only `a` is changed to `2b`; source section/material parameters remain unchanged.

|Case|b (mm)|a (mm)|a/b|m*|ell=a/m* (mm)|A0=a/500 (mm)|q0=A0/b|
|---|---:|---:|---:|---:|---:|---:|---:|
|Z0|6000|12000|2|2|6000|24|0.004|
|Z1|6000|12000|2|2|6000|24|0.004|
|Z2|6000|12000|2|2|6000|24|0.004|
|Z3|6000|12000|2|2|6000|24|0.004|
|Z4|8000|16000|2|2|8000|32|0.004|
|Z5|2000|4000|2|2|2000|8|0.004|

Thus each production representative complete halfwave is square, `ell=b`.

## 3. Frozen analytical production chain

Concrete:

```text
R10 target
-> N48-C1 for U,C,T7
-> N48-C1-CONSTRAINED-MINIMAX for T
-> Cayley-Hamilton 2D current map
-> General D15 exact moments
```

Kinematics:

\[
w_0=A_0\sin X\sin Y,\qquad w=A\sin X\sin Y,
\]

\[
X=\pi x/b,\qquad Y=\pi y/\ell,
\]

with Nguyen second-order `q0*q + q^2/2` membrane terms retained.

Steel/full section:
- two face steel plates;
- ideal elastic-perfectly-plastic coefficient-space radial cap;
- longitudinal homogenized PBL/web phase with `rho_w=ts/ls=0.02`;
- concrete contribution multiplied by `1-rho_w=0.98` to avoid web-volume double counting.

Formal structural integration:

```text
N_formal_spatial_sampling   = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
```

All integrations are finite coefficient-space / General-D15 analytical moments. Material-coordinate nodes used to build N48 or steel-cap coefficients are not structural spatial points.

## 4. Common compiler interval

The same predeclared interval used for the accepted Z6 run was retained:

\[
\lambda\in[-2.35,1.90].
\]

The final principal-value ranges were:

|Case|lambda_min|lambda_max|lower margin|upper margin|
|---|---:|---:|---:|---:|
|Z0|-1.122437|0.207140|1.227563|1.692860|
|Z1|-0.748914|0.182632|1.601086|1.717368|
|Z2|-1.389472|0.269563|0.960528|1.630437|
|Z3|-0.848527|0.176233|1.501473|1.723767|
|Z4|-1.122763|0.180918|1.227237|1.719082|
|Z5|-1.064099|0.074178|1.285901|1.825822|

All final states lie strictly inside the declared compiler hull.

The wide-hull N48-C1/MM representation error already documented for this interval remains fidelity information, not a spatial-integration error and not a new reject threshold.

## 5. Peak-location procedure

For each case:
1. solve the connected positive-amplitude `Rq=0` branch with degree-40 steel/web coefficient cap;
2. identify the first local load change `+ -> -`;
3. fit the local three-point load neighborhood to locate `D_peak`;
4. at that `D_peak`, increase the steel/web analytic cap to degree 48;
5. re-solve the local `q` equilibrium;
6. evaluate concrete/face-steel/web components and freeze the degree-48 state.

Representative peak brackets:

```text
Z0: D=.910 33.628675 -> .915 33.634352 -> .920 33.629880 MN
Z1: D=.560 19.783288 -> .580 19.791252 -> .600 19.708529 MN
Z2: D=1.100 35.965630 -> 1.120 36.041157 -> 1.140 35.964472 MN
Z3: D=.660 39.795288 -> .680 39.829797 -> .700 39.563339 MN
Z4: D=.920 63.828680 -> .940 63.988159 -> .960 63.878369 MN
Z5: D=.980 14.833398 -> 1.000 14.833162 -> 1.020 14.773691 MN
```

## 6. Final degree-48 NZ-SCCM states

|Case|D_u|q_u|A=q b (mm)|Pc_eff (MN)|Ps (MN)|Pw (MN)|Pu (MN)|Rnorm|
|---|---:|---:|---:|---:|---:|---:|---:|---:|
|Z0|0.915297|0.003167611|19.006|11.7383|16.7473|5.0055|**33.4910**|3.7e-11|
|Z1|0.571756|0.003592523|21.555|7.2727|10.1534|2.3099|**19.7360**|1.1e-9|
|Z2|1.119924|0.004121962|24.732|9.2597|20.5913|6.1272|**35.9781**|8.9e-11|
|Z3|0.672293|0.003650179|21.901|18.2855|16.4559|4.9475|**39.6889**|9.4e-9|
|Z4|0.941845|0.002343933|18.751|29.7288|23.1581|10.8516|**63.7385**|2.0e-8|
|Z5|0.989921|0.000378114|0.756|6.8088|6.1793|1.7944|**14.7824**|4.2e-8|

All component-scale equilibrium residuals pass the frozen `Rnorm <= 1e-5` requirement by several orders of magnitude.

## 7. Zhou same-parameter replay

The Zhou comparison is evaluated with the original full-MCFSTW section replay:
- full steel + concrete squash load `Pyth`;
- Zhou `Dx,Dy,Dxy,H`;
- Eq.(5-79) over integer `m=1..50` with theoretical minimum selected;
- `lambda=sqrt(Pyth/Pcr)`;
- Zhou Eqs.(5-87)/(5-88) reduction law.

For every modified AR2 case the theoretical minimum is `m*=2`, matching the one-complete-halfwave production mapping.

## 8. Winter same-parameter replay

Using the same `Pyth` and `Pcr`,

\[
\lambda=\sqrt{P_{yth}/P_{cr}},
\]

and the project Winter replay

\[
\phi_W=1\quad(\lambda\le0.673),
\]

\[
\phi_W=\frac{1-0.22/\lambda}{\lambda}\quad(\lambda>0.673),
\qquad P_W=\phi_WP_{yth}.
\]

No Zhou/Winter quantity enters the NZ-SCCM solve.

## 9. Same-parameter comparison

|Case|NZ-SCCM Pu (MN)|Pcr (MN)|Pyth (MN)|Zhou (MN)|Winter (MN)|NZ−Zhou|NZ−Winter|
|---|---:|---:|---:|---:|---:|---:|---:|
|Z0|**33.4910**|78.3067|44.0449|36.9455|41.5008|-9.35%|-19.30%|
|Z1|**19.7360**|40.3502|30.3196|23.7214|26.1001|-16.80%|-24.38%|
|Z2|**35.9781**|78.3067|50.6221|41.2134|45.7333|-12.70%|-21.33%|
|Z3|**39.6889**|81.7974|54.9488|44.3203|49.0469|-10.45%|-19.08%|
|Z4|**63.7385**|179.7548|79.3861|69.3399|79.3861|-8.08%|-19.71%|
|Z5|**14.7824**|231.7884|14.6816|14.6816|14.6816|+0.69%|+0.69%|

Useful normalized values:

|Case|Pu/Pcr|Pu/Pyth|
|---|---:|---:|
|Z0|0.42769|0.76038|
|Z1|0.48912|0.65093|
|Z2|0.45945|0.71072|
|Z3|0.48521|0.72229|
|Z4|0.35459|0.80289|
|Z5|0.06378|1.00686|

## 10. Immediate mechanical reading

A major distinction appears once all specimens are forced to AR2:

- Z0–Z5 all have `Pcr > Pyth`; the modified objects are therefore primarily material-strength dominated before the classical elastic plate critical load is reached.
- The accepted Z6 AR2 object has `Pcr=39.288 MN < Pyth=88.090 MN`, so it remains a genuine buckling/postbuckling-controlled object.

Therefore the former statement that Z6 alone was low because of its historical `a/b<1` cannot be carried forward after this AR2 normalization. The six modified Z0–Z5 objects now reveal a systematic NZ-SCCM-vs-Zhou/Winter separation for Z0–Z4, while Z5 is essentially coincident (+0.69%).

Z5's small `Pu>Pyth` result is preserved rather than calibrated away: R10 is a multiaxial current material operator and the common wide N48 hull has known representation uncertainty. It is an audit item, not a reason to alter the material law from the comparator.

## 11. Scope caveat

These Z0–Z5 values are **hypothetical AR2 geometry-adjusted calculations**. They are not direct predictions of the original Zhou test specimens at their historical lengths/aspect ratios. The purpose is controlled theory comparison at a common `a/b=2`.
