# NZ-SCCM — Zhou bottom-uy0 / top-uyfree one-halfwave compatibility execution report

**Timestamp:** 2026-08-16 01:21 +08:00

## 1. Executed gate

Executed

`ZHOU_BOTTOM_UY0_TOP_UYFREE_ONE_HALFWAVE_COMPATIBILITY_ZERO_QUADRATURE_GATE`.

No new AR2 Pu was calculated.

## 2. Exact source boundary used

The previously source-audited Zhou four-edge wall boundary was retained without reinterpretation:

```text
loaded top:    ux=0, uy=unset, uz=0
loaded bottom: ux=0, uy=0,     uz=0
lateral sides: ux=unset, uy=unset, uz=0
```

The transverse PF closure from 00:47 and its 01:02 D15-compatible kinematic lift remain valid for the `ux=0` subproblem. This execution audited only whether the axial `uy` asymmetry is a removable datum.

## 3. Datum test

A rigid axial gauge removes only one spatial constant. The bottom condition `v(x,0)=0` is pointwise over the complete width, so an x-dependent bottom/top trace cannot be removed by that gauge or by the scalar mean-shortening coordinate D.

For AR2 `a=2b,m=2`, define full-panel coordinates

`X=pi*x/b`, `Z=pi*y/a`.

The conforming axial variation

`v_A=(b/pi)*eta*cos(2X)*(1-cos Z)`

satisfies

```text
v_A(X,0)=0 exactly
v_A(X,pi)=2(b/pi)eta*cos(2X)
int_0^pi cos(2X)dX=0
```

Hence it is not a rigid translation and not a change of the mean D coordinate. Because top `uy` is not an essential displacement condition, this zero-mean x-dependent top trace is admissible.

## 4. Exact strain and geometric-source projection

For unit eta,

```text
B_A:
ex  = 0
ey  = 0.5*cos(2X)*sin Z
gxy = -2*sin(2X)*(1-cos Z)
```

The m=2 unit geometric source is

```text
Gx  = 0.5*cos(X)^2*sin(2Z)^2
Gy  = 0.5*sin(X)^2*cos(2Z)^2
Gxy = sin(X)*cos(X)*sin(2Z)*cos(2Z)
```

Using the exact isotropic plane-stress energy bilinear form and only analytical trigonometric moments gives

```text
fG = <B_A,G> = pi/120 = 0.02617993877991494
fD = <B_A,D> = 0
KA = <B_A,B_A> = pi^2*(25-24nu)/16
```

Therefore the m=2 FvK source has an exact nonzero projection onto an axial-trace direction that is absent from a pure rigid datum.

At `nu=.18`:

```text
KA   = 12.756463688407996
etaG = -fG/KA = -0.002052288112081178
single isolated-mode energy reduction = -5.372877713303245e-5
```

At `nu=.30`:

```text
KA   = 10.979934896211912
etaG = -0.002384343716732514
single isolated-mode energy reduction = -6.242197253433207e-5
```

These are exact gate diagnostics only. They are not production membrane coordinates and not capacity values.

## 5. Direct comparison with the 01:02 one-halfwave axial basis

The 01:02 symmetric axial-correction family is

`v_rs=(b/pi)V_rs*cos(rX)*sin(sY)`, with `Y=pi*y/ell=2Z` and integer `s`.

Every such finite mode vanishes at both ends of the representative halfwave:

`v_rs(X,0)=v_rs(X,pi)=0`.

The lower-half restriction of the admissible full-panel trace mode is instead

`v_A|lower=(b/pi)eta*cos(2X)[1-cos(Y/2)]`.

The factor `cos(Y/2)` is half-integer with respect to Y. It is not a finite member of the current integer-trigonometric D15 coefficient basis.

Thus the 01:02 symmetric axial family is a valid subspace for the transverse-restraint problem but is not an exact representation of Zhou's full axial-end boundary class.

## 6. Gate decision

```text
ZHOU_BOTTOM_UY0_IS_PURE_RIGID_DATUM = FAIL
BOTTOM_POINTWISE_AXIAL_RESTRAINT_HAS_NONRIGID_TRACE_CONTENT = PASS_PROOF
M2_FVK_SOURCE_PROJECTION_ON_ASYMMETRIC_AXIAL_TRACE = NONZERO_EXACT
CURRENT_0102_SYMMETRIC_V_RITZ_FULL_ZHOU_EQUIVALENCE = FAIL
TRANSVERSE_PF_END_RESTRAINT_SUBPROBLEM = RETAINED
ONE_CONTINUOUS_COMPLETE_HALFWAVE = RETAINED
GENERAL_D15 = UNCHANGED
ZERO_SPATIAL_NUMERICAL_INTEGRATION = PASS
MULTICOORDINATE_R10_N48_IMPLEMENTATION = BLOCKED
NEW_AR2_Z6_Pu = NOT_CALCULATED
```

## 7. Why this does not reopen the one-halfwave governance

The failure belongs to the **current axial trace representation**, not to the frozen out-of-plane one-halfwave choice.

The exact lower-half restriction can be represented by an infinite integer-harmonic expansion or, equivalently, by an analytically condensed interface/trace operator. Finite integer-trig levels remain General-D15 compatible. Therefore the project retains

`ONE_CONTINUOUS_COMPLETE_HALFWAVE`

and must next derive the required axial trace condensation without creating a second formal spatial subdomain.

## 8. Fail-fast stop and unique next gate

Because the 01:02 axial membrane space is not yet full-Zhou equivalent, the generic multi-coordinate R10/N48 compiler is not implemented in this execution and no Pu path is started.

Unique next gate:

`ZHOU_AXIAL_TOP_TRACE_TO_ONE_HALFWAVE_SCHUR_CONDENSATION_ZERO_QUADRATURE_GATE`

The next gate must analytically condense the global bottom-fixed/top-free axial trace response onto the single representative halfwave, produce a finite integer-trigonometric coefficient hierarchy with convergence diagnostics, and preserve zero spatial quadrature.