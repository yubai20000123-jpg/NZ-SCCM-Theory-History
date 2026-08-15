# NZ-SCCM — 最小 FvK 膜力重分布补全执行报告

**Timestamp:** 2026-08-15 21:34 +08:00  
**Stage:** no-Pu theory-space execution  
**Question:** should the next step merely audit the current theory, or establish the missing membrane system while preserving the exact-moment integration form?

## 1. Decision

The preceding 21:18 audit already established that Nguyen second-order geometry is present but complete postbuckling membrane equilibrium is not certified. This execution therefore performs the narrowest decisive gate first: an exact function-space/rank audit of the current `D+c` in-plane space against the two single-halfwave FvK source directions.

Result:

```text
CURRENT_DQC_EXACT_FVK_MEMBRANE_SOURCE_COMPLETENESS = FAIL
```

Because the failure is exact and structural, not numerical, there is no reason to continue treating `D+q+c` as potentially complete. The minimum missing analytic system is therefore constructed immediately, still without solving a new nonlinear state or Pu.

## 2. Exact reason the current theory fails the completeness gate

The existing boundary-current implementation has independent in-plane normalized virtual directions

```text
D: ex_D = 0, ey_D = -1
c: ex_c = (4/pi) sinX sin^2Y
   ey_c = (8 k^2/pi) sinX cos2Y
```

Hence its independent X-harmonics are only `0` and `1`.

The single `(1,1)` out-of-plane halfwave under Nguyen/FvK second-order compatibility forces independent membrane redistribution content associated with `cos2X` and `cos2Y`.

No constant linear combination of `D` and `c` can make `cos2X`, because that would require `cos2X=C sinX` for every X. Likewise a pure `cos2Y` redistribution with zero `ex` cannot use `c`, leaving only uniform D, which cannot reproduce `cos2Y`.

This is an exact span failure before any material calculation.

## 3. Minimum added basis

Two in-plane coordinates are introduced only at the theory-space level:

```text
p20 : X-second-harmonic admissible redistribution direction
p02 : Y-second-harmonic admissible redistribution direction
```

with

```text
U20 = b/(2pi) sin(2X) sin^2(Y)
V20 = b^2/(4pi a) cos(2X) sin(2Y)

U02 = 0
V02 = a/(2pi) sin(2Y)
```

Per unit dimensionless generalized coordinate, the normalized strains are

```text
e20x = cos(2X) sin^2(Y)
e20y = (k^2/2) cos(2X) cos(2Y)
g20  = 0

e02x = 0
e02y = cos(2Y)
g02  = 0
```

Symbolic verification gives exactly zero displacement warping on both loaded edges and exactly zero linear shear for both directions.

## 4. Exact-moment compatibility

Using `xs=sinX`, `ys=sinY`:

```text
e20x = ys^2 - 2 xs^2 ys^2
e20y = (k^2/2)(1-2xs^2)(1-2ys^2)
e02y = 1-2ys^2
```

Thus the new virtual strains are finite polynomial fields in the same variables already used by the D15 compiler. No structural point, cell or quadrature is required.

For Z6 (`k=b/a=4/3`) the exact polynomial coefficients are:

```text
c:
 ex_x1y2 = +1.27323954473516
 ey_x1y0 = +4.52707393683613
 ey_x1y2 = -9.05414787367227

p20:
 ex_y2    = +1
 ex_x2y2  = -2
 ey_const = +0.888888888888889
 ey_x2    = -1.77777777777778
 ey_y2    = -1.77777777777778
 ey_x2y2  = +3.55555555555556

p02:
 ey_const = +1
 ey_y2    = -2
```

The coefficient-space rank of `[D,c,p20,p02]` is 4 for generic nonzero `k`.

## 5. Resulting minimum nonlinear system

Keep D as loading coordinate and q as the single out-of-plane halfwave amplitude. Define the membrane coordinate vector

```text
m = [c,p20,p02]^T.
```

At each fixed `(D,q)`, enforce

```text
Rm = [Rc,R20,R02]^T = 0
```

using the same generalized virtual-work definition

```text
Rr = integral sigma(epsilon)^T * epsilon_,r dV.
```

The same `sigma=M(epsilon)` current operator remains unchanged.

To preserve low-dimensional matrix governance, use the flat membrane Jacobian

```text
Jmm = dRm/dm   # 3x3
```

and directional/static condensation

```text
dm/dq = -Jmm^{-1} Jmq
Lcond = Rq,q - Rq,m Jmm^{-1} Jm,q.
```

Thus the formal theory does not need a monolithic 4x4 nested matrix even though four equilibrium directions `(q,c,p20,p02)` exist.

## 6. Existing states retained only as future projection checkpoints

No new state was solved. The only Z6 states carried into the next gate are pre-existing:

```text
D=.50 q=.007244278905 c=-.0154563484942 P=37.345137133 MN
D=.55 q=.008198205    c=-.02004071      P=38.41062 MN
D=.60 q=.009177472    c=-.02655088      P=39.12698 MN
```

They will be used only to evaluate `R20` and `R02` with the unchanged current stress operator.

## 7. Gate result

```text
NGUYEN_SECOND_ORDER = RETAIN
ONE_OUT_OF_PLANE_COMPLETE_HALFWAVE = RETAIN
CURRENT_D_PLUS_C_MEMBRANE_COMPLETENESS = FAIL
MINIMUM_ADDED_MEMBRANE_COORDINATES = p20,p02
MINIMUM_MEMBRANE_JACOBIAN = 3x3
GENERAL_D15_FORM = UNCHANGED
FORMAL_SPATIAL_SAMPLING = 0
FORMAL_SPATIAL_QUADRATURE = 0
NEW_Pu = NONE
NEW_ROOT = NONE
```

## 8. Immediate next execution

The next execution is not Pu continuation. It is:

```text
EXISTING_STATE_R20_R02_D15_PROJECTION_GATE
```

At the already stored D=.50/.55/.60 states, use the frozen R10/N48/Cayley-Hamilton + local steel current operator and exactly contract

```text
R20 = integral sigma : epsilon_,p20 dV
R02 = integral sigma : epsilon_,p02 dV.
```

If both are negligible under a stated dimensionless work normalization, the minimum completion may be unnecessary in practice despite formal span deficiency. If either is materially nonzero, the 3-coordinate membrane subsystem is activated and solved before any new Pu calculation.