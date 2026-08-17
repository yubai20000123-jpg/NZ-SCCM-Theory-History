# NZ-SCCM Z0 — independent AR2/SSSS calculation

**Timestamp:** 2026-08-17 20:30 +08:00  
**Identity:** SINGLE-SPECIMEN INDEPENDENT EXECUTION  
**Membrane closure:** `R_A^Delta = R_A(D,q,alpha)-R_A(D,0,0)=0`  
**Theory:** finite current operators -> true-infinite analytic representation -> exact 2x2 CH -> General-D15 -> infinite target sum

## 1. No cross-case inheritance

```text
SPECIMEN = Z0 ONLY
ROOT_FROM_Z1_Z5 = NOT USED
STATE_FROM_Z1_Z5 = NOT USED
SERIES_PREFIX_FROM_Z1_Z5 = NOT USED
INTERNAL_VARIABLE_FROM_Z1_Z5 = NOT USED
COMPARATOR_USED_FOR_ROOT_SELECTION = NO
```

A fresh Z0 state is initialized at `D=0,q=0,alpha=0` and continued only inside Z0.

## 2. Raw input

```text
b = 6000 mm
a = 12000 mm = 2b
m* = 2
ell = 6000 mm = b
boundary = four-edge simply supported
A0 = a/500 = 24 mm
q0 = 0.004
concrete core tc = 122 mm
outer faceplate ts = 4 mm each face
full depth h = 130 mm
fc = 30.4 MPa
E0 = 32500 MPa
eps0 = 0.0018712490394580678
nu_c = 0.18
Es = 206000 MPa
fy = 355 MPa
nu_s = 0.30
homogenized longitudinal web steel rho_w = 0.02
```

## 3. Formal governing equations

The square complete-halfwave kinematics use

\[
M={\pi^2\over\varepsilon_0}\left(q_0q+{q^2\over2}\right),
\qquad \alpha=\lambda_A M.
\]

All concrete, two outer faceplates, and homogenized longitudinal web steel enter before solving:

\[
P=P_c+P_{face}+P_w,
\]
\[
R_q=R_{q,c}+R_{q,face}+R_{q,w}=0,
\]
\[
R_A^\Delta
=\int_V[\sigma(D,q,\alpha)-\sigma(D,0,0)]:B_A\,dV=0.
\]

The formal material/resultant evaluation remains the true-infinite CH/D15 target. The direct raw-current evaluations below are independent decimal-localization/convergence audits only; they do not change the formal spatial counters.

## 4. Membrane-OFF independent baseline

A fresh OFF branch is solved from the origin with `alpha=0` and `Rq=0`, then the first reachable load maximum is localized.

Primary decimal localization:

```text
D_u = 0.8866120432
q_u = 0.002412061865
M_u = 0.06623130946
Pc = 11.15021212 MN
Pface = 16.50066095 MN
Pw = 4.89480044 MN
Pu_OFF = 32.54567351 MN
Rq = -2.38e-7 N mm  (raw numerical cancellation scale)
max trial VM/fy = 1.08371
```

The Airy residual is intentionally not solved in the OFF branch.

## 5. Membrane-ON independent branch

A separate fresh state again starts from `D=0,q=0,alpha=0`; no OFF root/state is inherited.

Low-load branch identity:

```text
D=0.01: q=3.39814e-5, alpha/M=0.99620
D=0.02: q=6.77931e-5, alpha/M=0.97419
D=0.03: q=1.01062e-4, alpha/M=0.95040
```

Thus the corrected closure leaves the zero-driver state exactly and begins on the classical positive Airy/FvK-connected branch.

First reachable limit:

```text
D_u = 0.8986604833
q_u = 0.003439626859
M_u = 0.1037674990
alpha_u = 0.06411836054
lambda_A = alpha/M = 0.6179040755
Pc = 12.93344616 MN
Pface = 16.42838490 MN
Pw = 4.89300821 MN
Pu_ON = 34.25483926 MN
Rq = -5.96e-8 N mm
RA_delta = 5.59e-9 N mm
max trial VM/fy = 1.13113
```

Neighboring equilibrated points bracket the maximum:

```text
D=0.898: P=34.25478102 MN
D=0.900: P=34.25468025 MN
```

## 6. Same-root independent decimal convergence audit

These are AUDIT-ONLY direct-continuum evaluations, not formal quadrature.

### OFF

|audit order nxy|Pu at re-equilibrated D_u / MN|
|---:|---:|
|24|32.527058|
|32|32.545674|
|40|32.545999|
|48|32.546470|

### ON

|audit order nxy|Pu / MN|q|alpha/M|
|---:|---:|---:|---:|
|24|34.248425|0.003410|0.613022|
|32|34.254839|0.003440|0.617904|
|40|34.263014|0.003452|0.620865|
|48|34.265984|0.003455|0.621775|

The final two audit levels differ by about 0.0030 MN (~0.009%) at the fixed localized D coordinate. The formal governing identity remains the exact true-infinite D15 limit.

## 7. Z0 membrane delta

Using the independently solved same-object OFF and ON branches:

\[
\Delta P_{mem}=P_u^{ON}-P_u^{OFF}\approx1.7092\ \mathrm{MN},
\]

\[
\boxed{\Delta P_{mem}/P_u^{OFF}\approx+5.25\%}.
\]

This is a Z0 result; it was not inferred from any other Z specimen and was not selected to match Zhou or Winter.

## 8. Historical pre-membrane GitHub result kept separate

The earlier homogenized-web H0 file reports for Z0 a `SAME_D_RQ_LOCATED_DIAGNOSTIC` value of approximately `40.95234 MN`, versus Zhou `36.94554 MN`. That historical number is retained only as provenance for the pre-membrane state; it is not the present AR2 independently re-solved OFF ultimate branch and is not used as a target.

## 9. Formal counters

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```
