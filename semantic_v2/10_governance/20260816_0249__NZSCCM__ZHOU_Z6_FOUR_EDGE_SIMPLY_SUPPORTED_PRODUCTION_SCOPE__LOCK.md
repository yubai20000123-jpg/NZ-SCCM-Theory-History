# NZ-SCCM — Z6 theoretical four-edge simply-supported production scope lock

**Timestamp:** 2026-08-16 02:49 +08:00  
**User correction controlling this stage:** Zhou explicitly classifies the wall as four-edge simply supported; Z6 production shall use the theoretical four-edge simply-supported/Navier boundary. Detailed FE translational restraint implementation is not part of this analytical capacity task.

## 1. Governing production boundary

```text
Z6_PRODUCTION_BOUNDARY = THEORETICAL_FOUR_EDGE_SIMPLY_SUPPORTED
NAVIER_COMPLETE_HALFWAVE = GOVERNING
ZHOU_FE_UX_UY_TRANSLATIONAL_IMPLEMENTATION = OUT_OF_SCOPE_FOR_Z6_PRODUCTION
```

The analytical production field therefore uses

\[
w_0=A_0\sin X\sin Y,\qquad w=A\sin X\sin Y,
\]

\[
X=\pi x/b,\qquad Y=\pi y/\ell,
\]

with the ordinary simply-supported membrane baseline

\[
e_x=\nu D+e_x^{(g)}+e_x^{(b)},\qquad
 e_y=-D+e_y^{(g)}+e_y^{(b)},
\]

and the Nguyen second-order shear term.

No FE-end warp coordinate, Papkovich-Fadle end layer, axial trace-condensation coordinate, or free `p20,p02` membrane coordinate is used in Z6 production.

## 2. Status of the 00:16–01:21 FE-boundary detour

The files created from 2026-08-16 00:16 through 01:21 remain preserved as historical boundary-implementation audits. They are **superseded for Z6 production** by the present user boundary-scope instruction.

```text
20260816_0016_TO_0121_FE_BOUNDARY_DETOUR = SUPERSEDED_FOR_Z6_PRODUCTION
DELETE_HISTORY = NO
USE_AS_Z6_PRODUCTION_BC = NO
```

This supersession does not alter the prior conclusion that free independent `p20,p02` amplitudes are not an accepted membrane closure.

## 3. Frozen computational identity retained

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order kinematics
R10 material target unchanged
N48-C1/MM unchanged
Cayley-Hamilton unchanged
General D15 exact moments unchanged
A0=a/500
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
Gauss/Simpson/adaptive/collocation/cells/material-point-grid=PROHIBITED
out-of-plane multimode production expansion=PROHIBITED
Zhou/Winter calibration=PROHIBITED
```

The historical Gauss-based AR2 value `Pu=40.97334 MN` remains retracted and invalid.

## 4. Z6 object calculated under this lock

```text
a = 24000 mm
b = 12000 mm
a/b = 2
m* = 2
ell = a/m* = 12000 mm = b
A0 = a/500 = 48 mm
q0 = A0/b = 0.004
```

The integer `m*=2` is the preselected minimum-energy halfwave count; production still evaluates one continuous complete representative halfwave of length `ell`.

## 5. Section/material scope

The full section includes:

- ordinary-concrete core current operator R10 -> N48-C1/MM -> CH -> General D15;
- two face steel plates, ideal elastic-perfectly-plastic current cap;
- equivalent longitudinal web/PBL steel phase with `rho_w=ts/ls=0.02`;
- concrete volume reduced by `(1-rho_w)` when the homogenized web phase occupies that volume.

No test load enters material generation, root selection, or capacity evaluation.

## 6. Current task

The project priority is now direct:

```text
TASK = CALCULATE_Z6_ULTIMATE_CAPACITY
DO_NOT_REOPEN_FE_BOUNDARY_IMPLEMENTATION = YES
```

The production limit remains the first `+ -> -` maximum on the connected positive-amplitude `Rq=0` branch under the frozen zero-spatial-integration theory contract.