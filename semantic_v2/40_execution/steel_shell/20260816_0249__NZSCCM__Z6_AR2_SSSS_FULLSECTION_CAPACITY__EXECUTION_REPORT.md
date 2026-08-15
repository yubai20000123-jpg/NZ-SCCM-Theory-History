# NZ-SCCM — Z6 AR2 theoretical four-edge simply-supported full-section capacity

**Timestamp:** 2026-08-16 02:49 +08:00  
**Status:** CURRENT Z6 PRODUCTION CALCULATION UNDER USER-CONFIRMED SSSS SCOPE

## 1. Boundary scope correction

The Z6 analytical production problem is now evaluated as the theoretical **four-edge simply-supported plate** stated by Zhou, rather than reproducing Zhou's FE-specific translational `ux/uy` constraints.

Therefore the 00:16–01:21 FE-boundary implementation detour is superseded for Z6 production. No PF end layer, FE warp coordinate, axial-trace condensation or free `p20,p02` coordinate enters this calculation.

The production field is the standard Navier one-complete-halfwave field

\[
w_0=A_0\sin X\sin Y,\qquad
w=A\sin X\sin Y,
\]

with

\[
X=\pi x/b,\qquad Y=\pi y/\ell,
\]

and Nguyen second-order membrane/bending strains with uniform free-Poisson prebuckling baseline

\[
e_x=\nu D+\cdots,\qquad e_y=-D+\cdots.
\]

## 2. AR2 Z6 input

```text
a       = 24000 mm
b       = 12000 mm
a/b     = 2
m*      = 2
ell     = a/m* = 12000 mm = b
A0      = a/500 = 48 mm
q0      = A0/b = 0.004

tc      = 122 mm
ts      = 4 mm
h       = 130 mm
ns      = 60
ls      = 200 mm
rho_w   = ts/ls = 0.02

fc      = 30.4 MPa
eps0    = 0.0018712490394580678
nu_c    = 0.18
Es      = 206000 MPa
fy      = 355 MPa
nu_s    = 0.30
```

Reference loads retained only for post-solve comparison:

```text
Pcr_AR2                  = 39.2880147150 MN
Pyth_reduced             = 78.585600 MN
Pyth_full_with_web       = 88.089888 MN
Zhou Eq.(5-87)/(5-88)    = 49.4867667519 MN
Winter                   = 50.1858541295 MN
```

No reference load entered the solve or root selection.

## 3. Frozen current-material / exact-moment chain

Concrete:

```text
R10 target
-> N48-C1 for U,C,T7
-> N48-C1-CONSTRAINED-MINIMAX for T
-> Cayley-Hamilton 2D current map
-> General D15 exact moments
```

Steel:

- two face steel plates;
- ideal elastic-perfectly-plastic coefficient-space cap;
- longitudinal web/PBL phase homogenized at `rho_w=.02`;
- concrete contribution multiplied by `1-rho_w` to avoid double-counting the web volume.

Formal structural integration identity:

```text
N_formal_spatial_sampling   = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
```

The material-coordinate nodes used to create N48 or the steel analytic cap are not structural spatial points.

## 4. Declared compiler interval and coverage

Before the final capacity root, the declared material compiler interval was

\[
\lambda\in[-2.35,1.90].
\]

At the final state,

```text
lambda_min = -2.2936943231
lambda_max = +1.8232424497
```

so the interval margins are

```text
lower margin = +0.0563056769
upper margin = +0.0767575503
```

and the reachable state is inside the declared compiler hull.

The wide interval produces relatively large N48 full-hull fidelity errors. They are recorded in the companion JSON rather than hidden. In particular, `T` full-hull value error is approximately `0.7046`. Under the frozen 2026-08-12 production contract, these full-hull errors are fidelity information and there is no new universal reject threshold; therefore this is retained as the principal representation uncertainty, not converted into a new blocker.

## 5. Connected positive-amplitude equilibrium branch

Using the same SSSS field and fixed compiler interval, the connected `Rq=0` branch near its first capacity peak gave the following degree-40 steel-cap locator states:

```text
D       q                    P(MN)
1.48    .02039459040056      51.05435793
1.52    .02090144997010      51.22444971
1.56    .02138000258240      51.23273135
1.58    .02160717788487      51.31276663
1.60    .02183032559053      51.28835746
```

Thus the branch increases through `D=1.58` and has decreased by `D=1.60`; the first local `+ -> -` capacity maximum is bracketed in this interval.

A local quadratic peak locator gave

```text
D_peak ~= 1.5853259043
```

before the final steel-cap degree refinement.

## 6. Degree-48 final state

At the local peak coordinate, increasing the steel/web coefficient cap to degree 48 and re-solving the local q equilibrium gives

```text
D       = 1.5853259043
q       = 0.02166488056895
A=q*b   = 259.9785668 mm
A+A0    = 307.9785668 mm

Pc_full = 21.15062146 MN
Pc_eff  = 20.72760903 MN
Ps      = 21.59547236 MN
Pw      =  8.97221193 MN
--------------------------------
P       = 51.29529333 MN
```

Generalized-equilibrium components:

```text
Rc_eff = -6874.83772494 MN mm
Rs     = +11434.15920607 MN mm
Rw     = -4559.32179230 MN mm
Rq     = -311.161 N mm
```

Using the sum of absolute component generalized works as the local scale,

\[
R_{norm}\approx1.36\times10^{-8}.
\]

The degree-48 refinement reduces the degree-40 local peak load by only about `0.0202 MN`, so it does not change the engineering-rounded peak.

## 7. Frozen Z6 capacity result

The present four-edge simply-supported zero-spatial-integration production result is therefore frozen at engineering precision as

\[
\boxed{P_u\approx51.30\ \mathrm{MN}}.
\]

Associated state:

\[
\boxed{D_u\approx1.585,\qquad q_u\approx0.021665,\qquad A_u\approx260\ \mathrm{mm}}.
\]

Load decomposition at the final state:

```text
concrete effective core = 20.728 MN   40.41%
face steel plates       = 21.595 MN   42.10%
web/PBL steel phase     =  8.972 MN   17.49%
```

## 8. Mechanical comparisons

Relative to the AR2 elastic critical load,

\[
\frac{P_u}{P_{cr}}=1.30562,
\]

so the theoretical SSSS branch carries about `30.6%` above the elastic critical load before its first ultimate-load maximum.

Relative to the full-section squash load,

\[
\frac{P_u}{P_{yth,full}}=0.58231.
\]

Post-solve comparison only:

```text
vs Zhou Eq.(5-87)/(5-88): +1.80853 MN = +3.65%
vs Winter:                 +1.10944 MN = +2.21%
```

No Zhou/Winter value was used to choose the branch, material parameters, compiler coefficients, or capacity root.

## 9. Status of previous values

```text
historical q-only reduced audit 44.552919 MN = historical audit only, not this full-section result
historical Gauss/free-p20-p02 40.97334 MN = RETRACTED / INVALID
current SSSS full-section Pu = 51.30 MN
```

The current result includes the longitudinal web/PBL steel phase and follows the user-confirmed theoretical four-edge simply-supported boundary scope.

## 10. Current uncertainty statement

The principal remaining numerical/theory-representation uncertainty in this specific AR2 run is the relatively wide `[-2.35,1.90]` N48-C1/MM material compiler hull. It is **not** a spatial-integration uncertainty and it is **not** a boundary-condition uncertainty under the present user-confirmed SSSS scope.

No further FE-boundary reverse engineering is required for the Z6 capacity task.