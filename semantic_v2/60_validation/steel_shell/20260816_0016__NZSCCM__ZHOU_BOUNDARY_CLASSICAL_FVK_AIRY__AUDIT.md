# NZ-SCCM — Zhou four-edge mixed in-plane boundary classical FvK/Airy audit

**Timestamp:** 2026-08-16 00:16 +08:00

## 1. Question

After the 00:07 classical postbuckling limit passed, test whether that Airy membrane closure is itself admissible under Zhou's actual four-edge wall in-plane boundary conditions, without any spatial numerical integration.

No new Z6 ultimate load is calculated in this audit.

## 2. Direct source check

Zhou thesis Table 1.3 gives for the four-edge simply-supported wall:

```text
loaded top:    ux=0, uy=unset, uz=0
loaded bottom: ux=0, uy=0,     uz=0
left/right:    ux=unset, uy=unset, uz=0
```

Thus the loaded ends suppress transverse in-plane displacement, while the lateral sides remain in-plane free. This directly supports the earlier diagnosis that a globally uniform free-Poisson state is not the exact Zhou pre/postbuckling in-plane field.

## 3. Particular Airy field audit

The 00:07 compatibility particular solution

```text
Phi_p=C20 cos(2 alpha x)+C02 cos(2 beta y)
```

has

```text
Nx=-4 beta^2 C02 cos(2 beta y)
```

which does not vanish on the lateral sides. Therefore:

```text
PARTICULAR_AIRY_AS_ZHOU_BOUNDARY_SOLUTION = FAIL
```

This does not invalidate the 00:07 classical sign gate; it only proves the particular solution was not boundary complete.

## 4. Exact lateral-side correction

A homogeneous biharmonic correction was solved analytically for the `(0,2)` forcing component. In nondimensional variables `s=2 beta (x-b/2)`, `z=beta b`, the corrected amplitude is

```text
G(s)=1-Az cosh(s)+Bz s sinh(s)
Az=(z cosh z+sinh z)/(z+sinh z cosh z)
Bz=sinh z/(z+sinh z cosh z)
```

and exactly satisfies

```text
G(+/-z)=0
G'(+/-z)=0
=> Nx=Nxy=0 on x=0,b
```

so:

```text
EXACT_LATERAL_SIDE_TRACTION_CORRECTION = PASS
```

No spatial quadrature or spatial sample grid is involved.

## 5. Loaded-end compatibility audit

At a loaded end the nonlinear `w_x` strain contribution vanishes. Since `u=0` along the complete edge, the elastic membrane condition is pointwise

```text
epsilon_x=0
=> Nx-nu Ny=0.
```

For the side-corrected Airy field, after removing the one constant that can be shifted by mean axial resultant `N`, the residual is

```text
H(X)=-chi^2*(G+nu G'')+nu chi^4 cos(2X)
```

with `chi=b/ell`.

For original Z6 (`chi=4/3`) the exact formula gives:

```text
nu=.18: H_side=+0.251345415562366
        H_center=-2.037087472469174
        difference=2.288432888031540

nu=.30: H_side=+0.418909025937277
        H_center=-2.395786001921834
        difference=2.814695027859111
```

Because this residual is not spatially constant, no choice of the single mean `N` can satisfy the loaded-edge `u=0` condition pointwise.

Therefore:

```text
SIDE_FREE_CORRECTION_AS_FULL_ZHOU_CLOSURE = FAIL
SECOND_HOMOGENEOUS_END_RESTRAINT_FAMILY = REQUIRED
```

## 6. Positive-sign gate under the actual essential BC

The classical isotropic membrane energy is positive definite. For each fixed FvK source amplitude `S`, minimizing over all in-plane fields that satisfy Zhou's essential loaded-end condition gives

```text
U_m^Zhou = K_Z S^2
```

with `K_Z>0` whenever `S!=0`; otherwise zero strain would contradict the nonzero FvK compatibility source.

Consequently for `A>0,A0>=0`:

```text
dU_m^Zhou/dA > 0.
```

So the actual Zhou end restraint cannot turn the classical membrane effect into the artificial softening produced by the retired free `p20,p02` system.

Gate:

```text
ZHOU_BOUNDARY_CLASSICAL_POSTBUCKLING_SIGN = PASS_POSITIVE
```

## 7. Finite exact Ritz cross-check

A three-parameter displacement trial satisfying `u=0` at the loaded ends was minimized using exact symbolic moments only. For original Z6 `chi=4/3`:

```text
nu=.18:
r0=.699436656466086
r2=1.081366761351356
s2=1.072663180284274
kp_trial=4.91147853093745 > 0

nu=.30:
r0=.820658109922641
r2=.959792698594651
s2=1.086743159321920
kp_trial=5.23972966834637 > 0
```

These are trial diagnostics, not the exact Zhou coefficient and not production inputs.

## 8. m>1 / representative-halfwave audit

The physical end restraint `ux=0` exists only at `y=0,a`. It does not exist at an internal nodal line between repeated out-of-plane halfwaves.

Therefore the previous AR2 comparison object

```text
a=24000 mm
b=12000 mm
m=2
ell=12000 mm
```

cannot obtain the Zhou end-restraint correction by simply imposing `ux=0` at both ends of the representative `ell=12000` halfwave. That would create a fictitious restraint at `y=a/2`.

The global end-restraint boundary layer must instead be analytically condensed onto the representative halfwave if the project is to keep `ONE_CONTINUOUS_COMPLETE_HALFWAVE` without spatial subdivision.

## 9. Final audit status

```text
DIRECT_ZHOU_BC_SOURCE = PASS
PARTICULAR_FVK_COMPATIBILITY = PASS
PARTICULAR_SIDE_TRACTION = FAIL
EXACT_SIDE_TRACTION_CORRECTION = PASS
LOADED_END_UX_ZERO_AFTER_SIDE_CORRECTION = FAIL
FULL_MIXED_BOUNDARY_AIRY_CLOSURE = OPEN
CLASSICAL_MEMBRANE_STIFFENING_SIGN_WITH_ZHOU_BC = PASS_POSITIVE
ZERO_SPATIAL_INTEGRATION = PASS
AR2_ONE_HALFWAVE_END_RESTRAINT_MAPPING = OPEN
R10/N48 NONLINEAR MAPPING = BLOCKED
NEW Pu = NOT CALCULATED
```

## 10. Required next task

```text
ZHOU_MIXED_END_RESTRAINT_HOMOGENEOUS_BIHARMONIC_SERIES_ZERO_QUADRATURE
```

The next work must close the second homogeneous Airy family and the physical-end-to-representative-halfwave condensation analytically before any new nonlinear-material Z6 capacity path is released.
