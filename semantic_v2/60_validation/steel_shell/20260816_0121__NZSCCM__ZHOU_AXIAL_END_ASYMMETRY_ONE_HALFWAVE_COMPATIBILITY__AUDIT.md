# NZ-SCCM — audit: Zhou axial-end asymmetry vs one-halfwave condensation

**Timestamp:** 2026-08-16 01:21 +08:00

## Audit scope

Audit the single question left open by the 01:02 PF-to-current-material mapping stage: whether Zhou's `bottom uy=0 / top uy=unset` condition can be treated as a pure axial datum without altering the one-halfwave axial membrane space.

## Evidence chain

1. Source boundary retained from Zhou Table 1.3:

```text
loaded top:    ux=0, uy=unset, uz=0
loaded bottom: ux=0, uy=0,     uz=0
lateral sides: ux=unset, uy=unset, uz=0
```

2. A rigid-body axial datum removes only a spatial constant.

3. Exact conforming full-panel test mode:

`v_A=(b/pi)eta*cos(2X)*(1-cos Z)`

has bottom trace zero, top trace proportional to `cos 2X`, and zero width mean.

4. Therefore this mode is not a rigid translation and is not the scalar mean-shortening coordinate D.

5. Its exact m=2 FvK generalized forcing is

`<B_A,G>=pi/120 != 0`.

6. Its exact self stiffness is

`<B_A,B_A>=pi^2(25-24nu)/16 > 0`.

7. Its lower-half restriction contains `cos(Y/2)`, so it is not a finite member of the 01:02 integer-harmonic `sin(sY)` axial family.

## Audit verdict

```text
SOURCE_BOUNDARY_IDENTITY = PASS
BOTTOM_UY0_AS_ONLY_GLOBAL_RIGID_DATUM = FAIL
EXISTENCE_OF_NONRIGID_X_DEPENDENT_AXIAL_TRACE = PASS_EXACT
M2_FVK_DIRECT_FORCING_OF_TRACE_MODE = PASS_EXACT_NONZERO
CURRENT_0102_AXIAL_RITZ_SPACE_FULL_ZHOU_EQUIVALENCE = FAIL
TRANSVERSE_UX0_PF_CLOSURE = RETAIN
AR2_M2_ONE_OUT_OF_PLANE_HALFWAVE_MAPPING = RETAIN
ONE_CONTINUOUS_COMPLETE_HALFWAVE_GOVERNANCE = RETAIN
GENERAL_D15_GOVERNANCE = RETAIN
ZERO_SPATIAL_QUADRATURE = PASS
NEW_PU = NOT_AUTHORIZED
```

## Scope correction to 01:02 stage

The 01:02 statement `AR2_PF_TO_NONLINEAR_KINEMATIC_MAPPING = PASS_ARCHITECTURE` remains valid **for the transverse-end-restraint/PF subproblem** and for the general idea of mapping boundary physics into compatible displacement coordinates before R10.

It must no longer be read as full all-in-plane Zhou boundary equivalence. The missing axial top-trace family is real and mechanically excited.

## Next required evidence

Before any generic multi-coordinate R10/N48 implementation, construct

`ZHOU_AXIAL_TOP_TRACE_TO_ONE_HALFWAVE_SCHUR_CONDENSATION_ZERO_QUADRATURE_GATE`.

That gate must map the global asymmetric axial-end response to the single formal production halfwave without introducing spatial quadrature, spatial cells, or a second formal spatial subdomain.