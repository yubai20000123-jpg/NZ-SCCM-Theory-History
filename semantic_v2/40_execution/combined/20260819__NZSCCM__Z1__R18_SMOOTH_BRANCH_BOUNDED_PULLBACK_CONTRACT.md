# NZ-SCCM Z1 R18 — smooth-branch bounded pullback contract

The current R17 `ore_algebra` smooth-branch probe deliberately constructs an annihilator in

```text
x = tan(X/2) in [0,+infinity).
```

R18 has already compactified the same single continuous halfwave globally by

```text
x = u/(1-u),  u in [0,1].
```

Therefore the R17 x-annihilator is a **constructor feasibility result**, not yet the final bounded-domain operator consumed by the Oaku integration stage.

The exact relation is

```text
dx/du = 1/(1-u)^2,
du/dx = (1-u)^2,
D_x = (1-u)^2 D_u.
```

Because differential operators are noncommutative, a final operator must not be produced by naive commutative string substitution. After the R17 smooth branch annihilator passes, the bounded operator must be obtained by one of two mathematically identical exact operations:

1. Ore-algebra rational pullback of the x-annihilator under `x=u/(1-u)`; or
2. direct reconstruction of the identical three-radical smooth branch after substituting `x=u/(1-u)`, followed by annihilator construction in `u`.

The second route is preferred for implementation auditing because it avoids any ambiguity in operator ordering while remaining exactly the same R17 spectral branch and R18 coordinate map.

The final analytic and Heaviside D-modules must therefore share the variables

```text
(u,v,z,D,q,alpha, ...)
```

before Oaku product/intersection and bounded integration.

No spatial subdivision is introduced:

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_material_points = 0
FINITE_PREFIX = 0
```
