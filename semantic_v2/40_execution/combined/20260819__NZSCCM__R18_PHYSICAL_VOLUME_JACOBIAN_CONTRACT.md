# NZ-SCCM R18 — physical-volume Jacobian contract

R17/R18 use three different coordinate layers. This file fixes their scale factors before `P`, `Rq`, `Ralpha`, and `Jlim` are assembled.

## 1. Physical representative halfwave

R15 physical coordinates on the single representative halfwave are

```text
0 <= x_phys <= b,
0 <= y_phys <= ell.
```

The nondimensional trigonometric coordinates are

```text
X = pi*x_phys/b,
Y = pi*y_phys/ell,
```

so

```text
dx_phys dy_phys = (b*ell/pi^2) dX dY.
```

## 2. R17 tangent-half-angle coordinates

R17 uses

```text
x = tan(X/2),
y = tan(Y/2),
```

hence

```text
dX dY = 4/((1+x^2)(1+y^2)) dx dy.
```

## 3. R18 bounded global compactification

R18 then applies exactly

```text
x = u/(1-u),
y = v/(1-v),
0 <= u,v <= 1.
```

Therefore

```text
dX dY = 4/[(2u^2-2u+1)(2v^2-2v+1)] du dv.
```

Define

```text
Juv = 4/[(2u^2-2u+1)(2v^2-2v+1)].
```

Then the physical in-plane area element is

```text
dA_phys = (b*ell/pi^2) Juv du dv.
```

## 4. Core thickness coordinate

For the R17 Z1 core constructor,

```text
z_phys = (tc/2) z,
-1 <= z <= 1,
```

so

```text
dz_phys = (tc/2) dz.
```

Thus the full physical core volume measure is

```text
dV_core = [b*ell*tc/(2*pi^2)] Juv du dv dz.
```

All exact core contributions to `P`, `Rq`, `Ralpha`, and their same-source derivatives must include this scale exactly once.

For a discrete reinforcing layer or a steel face represented as a physical area/surface phase in the R15 ledger, its own physical thickness/area factor replaces `tc/2`; it must not inherit the core thickness factor by accident.

## 5. Axis-force normalization

R15 defines

```text
P_p = -(1/ell) integral_Vp sigma_y dV.
```

Therefore, for a core phase spanning the complete representative halfwave,

```text
P_core = -[b*tc/(2*pi^2)] integral_{0..1,0..1,-1..1} sigma_y * Juv du dv dz.
```

The factor `ell` cancels exactly. This formula is the bounded R18 form of the unchanged R15 definition.

## 6. Governance

The transformations are one-to-one global coordinate maps (up to measure-zero endpoints). They do not create spatial subdomains.

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_material_points = 0
FINITE_PREFIX = 0
```
