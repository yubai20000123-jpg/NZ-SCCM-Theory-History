# NZ-SCCM — Z1/Z4 unified Yun + ideal-EP local-amplitude full recalculation

**Timestamp:** 2026-08-18 14:21 +08:00  
**Identity:** CURRENT YUN-IEP RECALCULATION / CONTINUOUS LOCAL AMPLITUDE / ZERO-SPATIAL FORMAL TARGET  
**Calibration to Zhou/FE/test:** NO  
**Comparator used in solve:** NO

## 0. Supersession correction

This file explicitly supersedes the overly restrictive interpretation in

`20260818_1401__NZSCCM__Z1_Z4__DIRECT_YUN_EVENT_ORDERING_AND_RECALC_EXECUTION.md`.

The numerical statement `sigma_cr,Yun^E > fy` remains true for Z1/Z4, but the inference `Yun geometry/local-amplitude equation must be disabled` is withdrawn.

Correct current interpretation:

```text
YIELD FIRST changes the steel material state;
it does NOT delete the Yun/Karman local-amplitude geometry or membrane redistribution.
```

The executed route is the already-developed unified local residual used in the later UCFT/R04 theory lineage:

`actual scalar ideal-EP steel stress field + one continuous Yun Galerkin residual R_Ai for every local subpanel`.

There is no S0/S1/S2 activity switch in the equations used here.

## 1. Formal counters

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

The production target equations below consist only of finite trigonometric fields, the frozen current material functions, Yun finite-harmonic Galerkin expressions and exact General-D15 moments/analytic-series limits.

For this execution, a direct-continuum high-order evaluator was used only as a decimal root/peak localizer and convergence oracle after the target equations were frozen. It has no formal integration identity and does not change the above counters.

## 2. Inputs

Common:

```text
Es = 206000 MPa
nu_s = 0.30
nu_c = 0.18
fc = 30.4 MPa
E0 = 32500 MPa
eps0 = 0.0018712490394580678
rho_w = 0.02
q0 = 0.004
local subpanel width Bs = 200 mm
local steel thickness ts = 4 mm
```

Z1:

```text
b = ell = 6000 mm
a_physical_modified = 12000 mm
tc = 92 mm
h = 100 mm
fy = 235 MPa
number of 200-mm transverse local strips in one representative halfwave = 30
```

Z4:

```text
b = ell = 8000 mm
a_physical_modified = 16000 mm
tc = 192 mm
h = 200 mm
fy = 355 MPa
number of 200-mm transverse local strips in one representative halfwave = 40
```

Local Yun initial-imperfection convention retained from the existing local-shell lineage:

```text
local peak imperfection = Bs/400 = 0.5 mm
Yun coefficient A0 = peak/4 = Bs/1600 = 0.125 mm
```

No experimental bulge amplitude is fitted.

## 3. Global representative-halfwave kinematics

Use

\[
X=\pi x/b,\qquad Y=\pi y/\ell,\qquad \ell=b,
\]

\[
w_0^g=q_0b\sin X\sin Y,\qquad
\Delta w^g=qb\sin X\sin Y.
\]

Define

\[
M=\frac{\pi^2}{\varepsilon_0}\left(q_0q+\frac{q^2}{2}\right),
\qquad
M_q=\frac{\pi^2}{\varepsilon_0}(q_0+q),
\]

\[
B=\frac{\pi^2h}{2\varepsilon_0b}q,
\qquad
\alpha=\lambda_A M.
\]

For `u=sin X`, `v=sin Y`, the current normalized strain field is

\[
e_x=\nu D+M(v^2-u^2v^2)+\alpha B_A^x+Buv\zeta,
\]

\[
e_y=-D+M(u^2-u^2v^2)+\alpha B_A^y+Buv\zeta,
\]

\[
\gamma=2\cos X\cos Y[(M-\alpha)uv-B\zeta].
\]

Physical strain is `eps0 * e`.

Concrete remains the frozen R10 current operator; the 2% web/PBL-equivalent longitudinal steel remains the inherited scalar ideal-EP phase.

## 4. Yun finite local geometry inside the same global halfwave

Each 200-mm strip `i` uses one local amplitude `A_i` on each face. The Yun local field is

\[
\phi_i=
\left(1-\cos\frac{2\pi x_i}{B_s}\right)
\left(1-\cos\frac{2m_i\pi y}{\ell}\right),
\]

with the energy-minimum integer

\[
m_i=\ell/B_s.
\]

Thus `m_i=30` for Z1 and `m_i=40` for Z4, and in both cases

\[
r=\frac{\ell/m_i}{B_s}=1.
\]

Hence

\[
\boxed{k_{cr}=32/3=10.6666666667},
\qquad
\boxed{k_p=42.64}.
\]

For `Bs=200 mm, ts=4 mm`:

\[
C_\sigma=\frac{\pi^2E_st_s^2}{12(1-\nu_s^2)B_s^2}
=74.4739379716\ \text{MPa},
\]

\[
H=k_p\frac{1-\nu_s^2}{t_s^2}=2.42515\ \text{mm}^{-2}.
\]

The hypothetical pure-elastic Yun bifurcation stress is

\[
C_\sigma k_{cr}=794.388671697\ \text{MPa},
\]

which is above both Z1 and Z4 `fy`. This is retained only as an event-ordering fact; it does not switch off the local amplitude equation.

## 5. Actual steel strain and ideal-EP material response

The local shell field is added to the current global face strain using the incremental von Karman cross terms. In the current loading-direction notation,

\[
\varepsilon_s=arepsilon_y^g
+A_i(w_{0,y}^g+\Delta w_{,y}^g)\phi_{i,y}
+A_{0i}\Delta w_{,y}^g\phi_{i,y}
+\left(A_{0i}A_i+\frac12A_i^2\right)\phi_{i,y}^2.
\]

The face steel material law is directly

\[
\boxed{\sigma_s=\operatorname{clip}(E_s\varepsilon_s,-f_y,+f_y)}.
\]

Thus local points may yield while neighboring points remain elastic. There is no whole-face `Et=0` switch.

## 6. Unified Yun local-amplitude residual

For every local strip on each face, the one and only local row is

\[
\boxed{
R_{A_i}=C_\sigma
\left[k_{cr}A_i+H(2A_{0i}A_i+A_i^2)(A_i+A_{0i})\right]
-\bar\sigma_{c,i}(A_i+A_{0i})=0
}
\]

where

\[
\bar\sigma_{c,i}
=-\frac1{\Omega_i}\int_{\Omega_i}\sigma_s\,d\Omega
\]

is the compression-positive average of the actual ideal-EP current stress in that subpanel.

This equation remains active whether the first local material yield occurs before or after the hypothetical elastic Yun bifurcation. Therefore yield-first and Yun membrane geometry coexist in a single continuous residual system.

## 7. Face phase and global equilibrium

For each face/local strip,

\[
R_{q,s,i}=t_s\int_{\Omega_i}\sigma_s\varepsilon_{s,q}\,d\Omega,
\qquad
R_{A,s,i}=t_s\int_{\Omega_i}\sigma_s\varepsilon_{s,\alpha}\,d\Omega.
\]

The axial force is

\[
P_{face}=-\frac{t_s}{\ell}
\sum_{\pm}\sum_i\int_{\Omega_i}\sigma_s\,d\Omega.
\]

All local amplitudes satisfy their `R_Ai=0` equations at the same `(D,q,alpha)` state. The local coordinates may be mathematically condensed, but they are not deleted.

The global state at each D solves

\[
R_q=R_{q,c}+R_{q,face}+R_{q,w}=0,
\]

\[
R_A^\Delta=R_A(D,q,\alpha)-R_A(D,0,0)=0,
\]

with all three phases assembled before root solution.

The connected branch starts at the origin and the first reachable load maximum is the current limit used here.

## 8. Z1 recalculation

High-order decimal-localization peak neighborhood:

|D|P (MN)|q|alpha|
|---:|---:|---:|---:|
|1.335|14.4468696|0.0283651|2.135783|
|1.340|14.4468824|0.0284351|2.144419|
|1.345|14.4467841|0.0285047|2.152977|
|1.350|14.4466283|0.0285742|2.161500|
|1.355|14.4464392|0.0286433|2.169985|

Three-point local peak interpolation gives `D ~= 1.33808`. Direct re-evaluation at that state gives

```text
Z1 D = 1.33807919
q = 0.0284082291
alpha = 2.1411146461
M = 2.7276075041
lambda_A = alpha/M = 0.784979013
mean axial compression strain eps0*D = 0.00250387940
incremental global amplitude q*b = 170.4494 mm
global initial amplitude q0*b = 24.0 mm
Pc = 7.36427864 MN
Pface = 5.52501512 MN
Pw = 1.55760168 MN
Pu = 14.44689544 MN
```

Local amplitude/yield distribution at this same state:

```text
face -:
  A_i min/max/mean = 0.02780 / 0.05162 / 0.04374 mm
  yielded-area fraction per strip min/max/mean = 0.6077 / 1.0000 / 0.8306

face +:
  A_i min/max/mean = 0 / 0.05162 / 0.02169 mm
  yielded-area fraction per strip min/max/mean = 0 / 1.0000 / 0.5288
```

This directly demonstrates the requested mechanism: substantial local yielding and Yun local amplitudes coexist at the global peak. The steel face is not globally turned off after first yield.

The average compressive face-force stress based only on total two-face area is about `115.10 MPa`; this is not in conflict with local ±fy zones because the continuous field contains strong redistribution and stress-sign variation.

## 9. Z4 recalculation

High-order decimal-localization peak neighborhood:

|D|P (MN)|q|alpha|
|---:|---:|---:|---:|
|0.724|52.4290401|0.002190845|0.0248940|
|0.725|52.4310390|0.002211118|0.0254240|
|0.726|52.4315228|0.002232442|0.0259860|
|0.727|52.4302930|0.002254975|0.0265850|
|0.728|52.4270967|0.002278923|0.0272276|

Three-point local peak interpolation gives `D ~= 0.72578235`. Direct re-evaluation gives

```text
Z4 D = 0.72578235
q = 0.00222770385
alpha = 0.0258607373
M = 0.0600860643
lambda_A = alpha/M = 0.430394928
mean axial compression strain eps0*D = 0.00135811952
incremental global amplitude q*b = 17.82163 mm
global initial amplitude q0*b = 32.0 mm
Pc = 26.58171489 MN
Pface = 17.43310876 MN
Pw = 8.41673219 MN
Pu = 52.43155584 MN
```

Local amplitudes at the same state:

```text
face -:
  A_i min/max/mean = 0.06646 / 0.07471 / 0.07208 mm
face +:
  A_i min/max/mean = 0.05061 / 0.06548 / 0.05653 mm
```

At the first global peak, the high-order decimal localizer reports no face-area point on the ideal-EP plateau for Z4. This is mechanically possible even though the hypothetical pure-elastic Yun bifurcation stress is above fy: the coupled global/local-amplitude solution redistributes strain before the global peak and reaches its global limit while the scalar longitudinal face stress remains below fy. Therefore `sigma_cr^E > fy` is not itself a prescription that the actual connected branch must first hit fy.

The two-face average compressive face-force stress is about `272.39 MPa`.

## 10. Decimal-localizer convergence indication

A lower-order independent continuum localization gave approximately

```text
Z1 Pu = 14.44652 MN
Z4 Pu = 52.59944 MN
```

The higher-order values adopted above are

```text
Z1 Pu = 14.44690 MN
Z4 Pu = 52.43156 MN
```

Relative load changes are approximately

```text
Z1: -0.0026%
Z4: +0.3202% (lower-order relative to higher-order)
```

The Z1 peak is very flat, so the decimal `D_u` location is more evaluator-sensitive than the peak load itself. This does not reopen the physical equations; the formal target remains the zero-spatial analytic/D15 target stated above.

## 11. Comparison with the superseded radial-cap checkpoint

Old radial-cap connected-path checkpoints were

```text
Z1 Pu_old = 20.81204766 MN
Z4 Pu_old = 63.72928932 MN
```

Under the unified Yun + ideal-EP local-amplitude equations, the current recalculated values are

```text
Z1 Pu_Yun-IEP = 14.44689544 MN   (-30.584% vs old radial-cap checkpoint)
Z4 Pu_Yun-IEP = 52.43155584 MN   (-17.728% vs old radial-cap checkpoint)
```

These changes are not fitted to any Zhou/FE/test comparator. They result from replacing the old two-dimensional radial-cap face operator with the already-established scalar longitudinal ideal-EP steel + continuous Yun local-amplitude redistribution route.

## 12. Current interpretation

```text
Yun/Karman geometry = RETAINED continuously
local initial imperfection = RETAINED
local amplitudes A_i = SOLVED continuously
ideal-EP steel clip = ACTIVE pointwise in the analytic target
first yield = diagnostic/material event, NOT a branch-deletion command
whole-face Et=0 switch = NOT USED
old radial-cap = NOT USED in the new Z1/Z4 face phase
R10 concrete = unchanged
2% equivalent web steel = unchanged
all phases assembled before solve = YES
zero formal spatial quadrature = RETAINED
```

The prior `20260818_1401` conclusion that yield-first makes Yun inactive is therefore superseded by this executed unified-residual result.
