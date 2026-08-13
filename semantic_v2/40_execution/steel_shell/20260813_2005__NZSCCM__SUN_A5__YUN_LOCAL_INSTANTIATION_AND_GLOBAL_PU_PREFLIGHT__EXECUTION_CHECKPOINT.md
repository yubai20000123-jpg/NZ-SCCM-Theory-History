# NZ-SCCM — Sun A5 concrete + PBL steel-shell / Yun-Lu local instantiation preflight

**Timestamp:** 2026-08-13 20:05 +08:00  
**Status:** EXECUTION CHECKPOINT / FIRST REAL-SOURCE NC+PBL PREFLIGHT / NO FAKE GLOBAL ROOT  
**Formal spatial quadrature:** 0

## 1. Purpose

Use a real ordinary-concrete + PBL-stiffened steel-wall specimen as the first structural preflight after the Yun-Lu Chapter-2 exact general-D15 closure. The goal is to instantiate the actual local shell parameters, determine the local event ordering, and only release a global `(Du,qu,Pu)` if the frozen global concrete operator and the chosen local shell branch are source-complete.

Selected specimen: Sun Lipeng axial-compression specimen **A5**.

## 2. Source design input

From Sun Chapter 4:

```text
steel wall thickness t_s = 6 mm
longitudinal PBL spacing / local panel width b = s_l = 256 mm
transverse PBL spacing s_h = 520 mm
s_h/s_l ≈ 2.0
no studs
```

The longitudinal and transverse PBL ribs are treated as local plate boundaries; PBL steel is not added automatically as an independent axial capacity term.

Steel wall source properties used in the preflight:

```text
E_s = 208000 MPa
f_y = 423 MPa
nu_s = 0.30
```

Concrete source information available for the specimen family includes approximately:

```text
f_c = 46.9 MPa (cylinder)
E_c = 36300 MPa
```

The current frozen R10 ordinary-concrete production operator additionally requires its source-closed peak-strain input `eps0`; that A5-specific value has not yet been recovered/frozen and is therefore not invented here.

## 3. Theoretical local halfwave

For the PBL-bounded local steel panel:

```text
full local axial length = s_h = 520 mm
local width             = 256 mm
s_h/b                    = 2.03125
```

The Yun-Lu/classical energy-minimum integer wave count is therefore `m=2`, giving one representative complete local wave

\[
\ell=s_h/m=260\text{ mm},\qquad r=\ell/b=1.015625.
\]

The experimental bulge pattern is not used to select this halfwave.

## 4. Exact Yun-Lu coefficients

Using the already verified general-D15 closed forms,

\[
k_{crx}(r)=\frac{4(3r^4+2r^2+3)}{3r^2},
\]

\[
k_p(r)=\frac{272r^{16}+2856r^{14}+11273r^{12}+23146r^{10}+31506r^8+23146r^6+11273r^4+2856r^2+272}{r^2(r^2+1)^2(r^2+4)^2(4r^2+1)^2}.
\]

For A5:

```text
r      = 1.015625
k_crx  = 10.670513051651874
k_p    = 42.654436695417374
D_s    = 4.114285714285714e6 N*mm
```

No numerical spatial integration is involved.

## 5. Local elastic-buckling vs yield ordering

The Yun-Lu elastic local-buckling stress is

\[
\sigma_{cr,s}^{E}
=k_{crx}\frac{\pi^2E_s}{12(1-\nu_s^2)}\left(\frac{t_s}{b}\right)^2.
\]

For A5:

```text
sigma_cr_el = 1101.9155543017378 MPa
fy          = 423 MPa
sigma_cr_el/fy = 2.6050013104059992
```

Therefore

```text
YIELD_PRECEDES_ELASTIC_YUN_BUCKLING = YES
YUN_S1_ELASTIC_POSTBUCKLING_AS_FIRST_LOCAL_BRANCH = NO
```

This is a branch-applicability result, not a failure of the Yun-Lu module. The elastic large-deflection postbuckling branch is physically relevant only when the shell reaches elastic local buckling before local yield. Under the adopted ideal elastic-perfectly-plastic steel law, A5 reaches the steel strength boundary first.

## 6. Source experiment check kept strictly post-solution

Sun reports for A5:

```text
experimental ultimate Nu = 7065 kN
reported local-buckling load Nlo = 6210 kN (earlier than Nu)
```

Thus the real specimen clearly continued carrying load after the observed local-buckling event. These values are validation evidence only and were not used to generate `m`, `k_crx`, `k_p`, or `sigma_cr_el`.

## 7. Why a global Du,qu,Pu is not released from A5 in this checkpoint

A full current NZ-SCCM root would require all of the following to be source-complete simultaneously:

1. the frozen ordinary-concrete R10 input set for A5, including `eps0`;
2. the exact wall/component scope entering `P_sh` (main steel wall versus side plates; PBL remains boundary-only under current governance);
3. a local shell branch valid for A5's **yield-first** ordering under ideal elastic-perfectly-plastic steel.

The Yun-Lu `S1` elastic large-deflection path cannot be forced ahead of yield when `sigma_cr_el > fy`. Doing so would manufacture an inadmissible local branch and contaminate the subsequent `L/KZ/Y_s` ordering.

Therefore:

```text
SUN_A5_SELECTED = YES
REAL_SOURCE_GEOMETRY_INSTANTIATED = YES
YUN_LOCAL_D15_COEFFICIENTS = PASS
LOCAL_EVENT_ORDERING_PREFLIGHT = PASS
FULL_Du_qu_Pu = NOT RELEASED
NO_FAKE_ROOT = YES
```

## 8. Immediate implication

A5 is useful as the first **yield-first** NC+PBL benchmark. It shows that the production solver must distinguish two legitimate local regimes:

```text
REGIME E-B:
    elastic local buckling first
    -> Yun-Lu elastic large-deflection postbuckling S1
    -> later first yield

REGIME Y-B:
    local steel yield first
    -> ideal-EP yield boundary reached before elastic Yun bifurcation
    -> do not force Yun S1 as a pre-yield branch
```

The global structure is still allowed to continue after either local event. Local buckling/yield is not automatically the global ultimate load.
