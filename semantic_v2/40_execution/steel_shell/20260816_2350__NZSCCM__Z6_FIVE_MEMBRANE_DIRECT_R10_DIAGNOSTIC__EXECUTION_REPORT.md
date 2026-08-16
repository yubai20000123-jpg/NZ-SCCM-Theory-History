# NZ-SCCM — Z6 five-membrane redistribution direct-R10 diagnostic

**Timestamp:** 2026-08-16 23:50 +08:00  
**Status:** AUDIT-ONLY / NOT FORMAL ZERO-INTEGRATION PRODUCTION

## Purpose

This execution was triggered by the concern that the newly released Case21 five-membrane result moved from the previous r=0 prediction to a substantially lower capacity, suggesting a possible systematic downward shift caused by the membrane-redistribution module.

The objective here is NOT to release a new formal Z6 Pu. It is to isolate the mechanical effect of freeing the same five membrane coordinates in Z6 while holding the physical R10 operator and full-section steel/web model fixed.

## Frozen Z6 inputs

```text
a=24000 mm
b=ell=12000 mm
m*=2
A0=48 mm
q0=0.004
tc=122 mm
ts=4 mm
rho_w=0.02
fc=30.4 MPa
eps0=0.0018712490394580678
nu_c=0.18
Es=206000 MPa
fy=355 MPa
nu_s=0.30
```

## Five membrane coordinates

The audit uses the same five-term compatible membrane family now active in Case21:

```text
r=[r0,r20,r22,s02,s22]
```

with the same generalized-equilibrium structure:

```text
Rq=0
Rm0=0
Rm20=0
Rmu22=0
Rm02=0
Rmv22=0
```

The full-section audit includes effective concrete `(1-rho_w)`, two face steel plates, and the longitudinal web/PBL phase. The web phase uses the frozen homogenized ratio `rho_w=0.02` over the concrete-core depth, which reproduces the previously frozen r=0 web contribution to engineering precision.

## IMPORTANT method identity

This is an independent direct-R10 numerical audit using Gauss-Legendre evaluation only as an external oracle. It is NOT the formal structural integration method and does not change:

```text
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
N_formal_thickness_quadrature=0
```

No Gauss result is promoted to formal production.

## Same-evaluator r=0 baseline

To remove compiler/backend differences from the comparison, the same direct-R10 audit evaluator was first run with all membrane redistribution coordinates fixed to zero.

High-resolution audit (`56x56x18` oracle grid), local peak:

```text
D_peak ~= 1.593887
q_peak ~= 0.021556525
P_r0 ~= 51.480540 MN
Pc ~= 20.585826 MN
Ps ~= 21.876769 MN
Pw ~=  9.017946 MN
lambda ~= [-2.28755,+1.80286]
```

This is close to the historical N48/D15 SSSS full-section engineering baseline `51.295293 MN`, showing that the old peak load itself is not strongly changed by replacing the broad N48 representation with direct R10 in this r=0 comparison.

## Five-membrane redistributed branch

Using the same direct-R10 evaluator and freeing only the five membrane coordinates, the high-resolution audit gives a first local load maximum near:

```text
D_peak ~= 1.15617344
q_peak ~= 0.02401533
A_increment ~= 288.184 mm
A_total ~= 336.184 mm
r0   ~= -0.37472588
r20  ~= -0.37684276
r22  ~= +0.39596319
s02  ~= -0.25455699
s22  ~= +0.67363743
```

At that state:

```text
P ~= 43.762840 MN
Pc ~= 19.982876 MN
Ps ~= 17.392895 MN
Pw ~=  6.387069 MN
Rq ~= -1.34e-11 MN mm
||Rm||2 ~= 1.18e-16 in the scaled 1e9 residual coordinates
lambda ~= [-1.54031,+1.36017]
face-steel trial von-Mises ratio max ~= 1.970
```

A nearby high-resolution three-point peak bracket was:

```text
D=1.155 -> P=43.762818 MN
D=1.160 -> P=43.762665 MN
D=1.165 -> P=43.761935 MN
```

A quadratic local locator gives `D_peak ~= 1.15617` and `P ~= 43.76283 MN`.

## Isolated membrane-redistribution effect

Because both values below use the SAME direct-R10 full-section audit evaluator, their difference isolates the membrane-redistribution release much better than comparing different compilers:

```text
r=0 direct-R10 audit peak          = 51.480540 MN
five-membrane direct-R10 audit     = 43.762840 MN
change                             = -7.717700 MN
relative change                    = -14.9915 %
```

This is consistent in sign and scale with Case21:

```text
Case21 r=0 -> five-membrane change = -12.2630 %
Z6 same-direct-R10 change          = -14.9915 %
```

Therefore there is now evidence for a systematic DOWNWARD SHIFT caused by the membrane-redistribution module relative to the previous constrained-membrane model.

This is NOT yet equivalent to proving a systematic experimental underprediction, because Z6's retained external comparators are Zhou/Winter rather than an independent experiment in this branch.

## External comparison, audit-only

```text
Zhou Eq.(5-87)/(5-88) = 49.486767 MN
Winter                  = 50.185854 MN
five-membrane audit     = 43.762840 MN
error vs Zhou            = -11.5666 %
error vs Winter          = -12.7985 %
```

The historical r=0 SSSS value was approximately +3.65% vs Zhou and +2.21% vs Winter. The five-membrane release therefore reverses the sign and creates a substantial low-side shift.

## Interpretation

The current evidence is no longer consistent with treating the Case21 decrease as an isolated numerical accident. Both Case21 and Z6 show a similar 12–15% loss when the membrane redistribution coordinates are released.

The Z6 redistributed coordinates are also large relative to D, especially `s22 ~= +0.674` at `D ~= 1.156`. This indicates that the five-term membrane family has enough freedom to substantially reshape the axial membrane strain field and unload steel/web participation.

The correct next scientific question is therefore not "can we force the formal Z6 solver to produce a number?" but "are all five membrane coordinates physically admissible under the intended in-plane boundary/work constraints, or is the current condensation over-releasing the membrane field?"

## Formal Z6 production status

No new formal Z6 Pu is released here.

The existing family evidence still gives:

```text
wide-family N48 source fidelity = FAIL
N3584 source fidelity candidate = PASS
current N3584 coefficient-tensor structural backend = FAIL_COMMON_TRACTABILITY
```

Therefore the formal five-membrane Z6 capacity remains BLOCKED under the current common-family zero-integration rules. This execution deliberately stops here instead of opening another symbolic/backend loop.
