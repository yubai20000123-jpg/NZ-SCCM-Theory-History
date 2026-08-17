# NZ-SCCM — corrected Z6 a=24000 Airy redistribution + rebuilt N48-family capacity calculation

**Timestamp:** 2026-08-17 14:07 +08:00  
**Status:** CORRECTED Z6 CALCULATED / N48-FAMILY MATERIAL CONVERGENCE PASS / HIGH-BLOCK D15 FORMAL PROMOTION NOT YET CLAIMED

## 0. Correction of the previous round

The previous 13:37 run used `a=9000 mm`. That was a source-reading error. The backup production record explicitly fixes the Z6 analytical object at

```text
a=24000 mm
b=12000 mm
m*=2
ell=a/m*=12000 mm=b
A0=48 mm
q0=.004
```

The current run returns to that object.

The prior ~43 MN family is also not retained as current production mechanics. The historical `43.76284 MN` value came from freeing five membrane amplitudes independently; that branch over-released the membrane field. The current calculation uses the constrained Airy scalar redistribution, not `r=0` and not free-five condensation.

## 1. Full input

```text
a = 24000 mm
b = ell = 12000 mm
m* = 2
k = b/ell = 1
A0 = 48 mm
q0 = .004

tc = 122 mm
ts = 4 mm
rho_w = .02

fc = 30.4 MPa
eps0 = 0.0018712490394580678
nu_c = .18
Es = 206000 MPa
fy = 355 MPa
nu_s = .30
```

Post-solve comparators only:

```text
Pcr_AR2 = 39.2880147150 MN
Zhou Eq.(5-87)/(5-88) = 49.4867667519 MN
Winter = 50.1858541295 MN
```

## 2. Membrane redistribution used

Because the representative complete halfwave is square (`ell=b`), the qualified Airy direction is

```text
a=[-.295,-.205,+.25,-.205,+.25]
```

with

\[
r=\lambda M a,
\quad
M=\frac{\pi^2}{\varepsilon_0}(q_0q+q^2/2).
\]

The coupled branch solves

```text
Rq_base = 0
RA = a^T Rm = 0
```

with effective concrete, both faceplates and the longitudinal web/PBL phase all active before the solve.

## 3. Raw-R10 mechanics oracle — corrected geometry

The independent direct-R10 continuum oracle gives the following high-resolution branch points:

|D|q|lambda_Airy|P MN|Pc_eff MN|Ps_face MN|Pw MN|
|---:|---:|---:|---:|---:|---:|---:|
|1.34|0.02617602|0.78719647|48.40413|22.79690|18.58797|7.01927|
|1.35|0.02631834|0.78707112|48.40558|22.80669|18.57343|7.02547|
|1.36|0.02645989|0.78694020|48.40612|22.81558|18.55903|7.03151|
|1.37|0.02660070|0.78680459|48.40581|22.82371|18.54473|7.03737|
|1.38|0.02674068|0.78665901|48.40477|22.83114|18.53052|7.04311|

Local quadratic peak location:

```text
D_peak ~= 1.36180798
```

Direct re-solve at this coordinate:

```text
D = 1.36180798
q = 0.0264854039
lambda_Airy = 0.786915819
P = 48.4061215 MN
Pc_eff = 22.8171044 MN
Ps_face = 18.5564373 MN
Pw = 7.0325797 MN
material lambda_min ~= -1.66417
material lambda_max ~= +1.35392
face steel trial VM/fy max ~= 1.9474
```

Thus the corrected raw-R10 engineering oracle is

\[
\boxed{P_u^{raw\ R10,oracle}\approx48.41\text{ MN}.}
\]

This is about 5.97% below the same-evaluator `r=0` Z6 peak `51.48054 MN`, so the constrained membrane-stress redistribution is material but far smaller than the historical free-five reduction to 43.76 MN.

## 4. Rebuilt N48-family material compiler

The source interval is reduced to the actual corrected Airy branch neighborhood with margin:

```text
[-1.75,+1.45]
```

The R10 sources `U,C,T,T7` are regenerated as C1-constrained Chebyshev material functions at cumulative N48-family orders

```text
N=48,96,144,192,240,288.
```

The order gate uses only source/structural-target convergence. Zhou/Winter values do not participate.

## 5. Common-resolution compiler convergence

At the common 40x40x18 direct-continuum **audit evaluator** the raw-R10 peak is `48.43966238 MN`. Replacing only the concrete source by the rebuilt N48-family gives:

|material order|Pu MN|difference from same-grid raw R10|relative|
|---:|---:|---:|---:|
|48|48.96003337|+0.5203710|+1.0743%|
|96|48.60847719|+0.1688148|+0.3485%|
|144|48.50930612|+0.0696437|+0.1438%|
|192|48.46888919|+0.0292268|+0.0603%|
|240|48.46413079|+0.0244684|+0.0505%|
|288|48.45880247|+0.0191401|+0.0395%|

The earlier literal single-N48 wide-domain error is therefore removed by the N48-family refinement.

## 6. Higher-resolution N192-N288 gate

At 64x64x26 + face-12 audit resolution:

```text
raw R10 peak = 48.40515087 MN
N192 peak    = 48.42896188 MN   (+0.0492%)
N240 peak    = 48.42159977 MN   (+0.0340%)
N288 peak    = 48.41599214 MN   (+0.0224%)
```

Representative N240 state:

```text
D = 1.36084551
q = 0.0264712930
lambda_Airy = 0.786756642
P = 48.4215998 MN
Pc_eff = 22.8331231 MN
Ps_face = 18.5563166 MN
Pw = 7.0321601 MN
material lambda_min = -1.66254
material lambda_max = +1.35182
face steel VM/fy max ~= 1.94585
```

The material-domain margins at this state are approximately

```text
lower margin: -1.66254 - (-1.75) = +0.08746
upper margin: +1.45 - 1.35182 = +0.09818
```

## 7. Current engineering Z6 value

The raw-R10 oracle and converged N48-family are now clustered in

```text
48.405 ... 48.429 MN
```

and the N240/N288 results differ by only about `0.00561 MN`.

The present corrected engineering prediction is therefore

\[
\boxed{P_u(Z6,a=24000)\approx48.42\ \mathrm{MN}.}
\]

A representative state is

\[
\boxed{D_u\approx1.361,\quad q_u\approx0.02647,\quad \lambda_A\approx0.787.}
\]

With `b=12000 mm`,

```text
A_increment = q*b ~= 317.7 mm
A_total = A0 + A_increment ~= 365.7 mm
```

## 8. Post-solve comparison

Using `48.42 MN` only after the branch is frozen:

```text
vs Zhou = about -2.15%
vs Winter = about -3.52%
```

This is qualitatively different from the erroneous 9000-mm ~43 MN branch and from the historical free-five ~43.76 MN branch.

## 9. Formal-integration status

The source compiler has been rebuilt in a form that remains termwise compatible with `2x2 CH -> General-D15` finite exact moments. A direct N48 CH/D15 regression was also retained from the historical implementation. However the present high-block N192-N288 capacity numbers above were evaluated with the direct continuum oracle to establish material-family convergence; therefore this report does **not** relabel the 64/72-point audit grids as formal spatial quadrature.

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

The engineering mechanics result `~48.42 MN` is released here; high-block exact-D15 contraction remains an implementation promotion step, not a change of physical path.
