# NZ-SCCM execution report — dual-holonomic regularity audit and anti-loop production pivot

**Timestamp:** 2026-08-16 21:36 +08:00

## Executed gate

`UNIFIED_V1_FULL_R10_DUAL_HOLONOMIC_THICKNESS_MOMENT_RUNTIME_GATE`

## Result

The proposed denominator-gauge connection between the compact x-dependent dual target and the finite holonomic state was derived exactly:

\[
 dV'=BV,\quad W=V/G
\quad\Longrightarrow\quad
(dG)W'=(BG-dG'I)W.
\]

This provides an exact polynomial moment recurrence whenever the target denominator signature `G` is globally nonzero on the complete thickness interval.

However, the retained rationalized quadratic-tower basis fails that global-regularity requirement even for the standard noncommuting smooth prototype. The basis discriminant factors as

\[
A^2-4Q=\frac{(260x-21)^2(28624x^2+47880x+50121)}{31116960000},
\]

so an apparent basis pole occurs at `x=21/260` inside `[-1,1]`. The physical atom remains finite there and

\[
\lim(c_0+c_1q)=29577184/61042095.
\]

Therefore denominator-tagging the rationalized pieces separately can break a removable algebraic cancellation.

## Local derivative-matrix erratum

For `v=(1,q,s,qs)^T`, the correct exact local matrix is

```text
[0, 0,    0,            0]
[0, ell,  0,            0]
[0, 0,    c0,           c1]
[0, 0,    c1*Q,         ell+c0]
```

The earlier 20:59 displayed matrix interchanged `c1` and `c1*Q` in the last two rows. The stated differential equations were correct. State dimension `4^3=64` and sparsity count `159/4096` are unchanged.

## Anti-loop decision

A further exact production continuation would require a regular algebraic basis / Hermite-reduction layer to remove apparent poles before moment contraction. That is a legitimate mathematical research direction, but opening it now would create another backend layer rather than advance the structural calculation.

The following production decision is therefore locked:

```text
EXACT_ALGEBRAIC_HOLONOMIC_Pu_ROUTE = PAUSED_RESEARCH_BRANCH
NO_AUTOMATIC_INTEGRAL_BASIS/HERMITE_BACKEND = YES
N48_C1_MM_GENERAL_D15_PRODUCTION = REACTIVATED
FIVE_TERM_MEMBRANE_REDISTRIBUTION = REQUIRED
```

The reactivated production contract is the already successful repository contract:

`current/theory/NZ_SCCM_NC_REBAR_ZERO_SPATIAL_PRODUCTION_THEORY_CONTRACT_20260812_2245.md`

with the current five internal membrane coordinates

`[r0,r20,r22,s02,s22]`

inserted before the outer `(D,q)` limit solve and consistently Schur-condensed.

## Formal counters

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

## Capacity status

```text
NEW membrane-redistributed Case21 Pu = NOT RUN IN THIS GATE
```

## Unique next production gate

`UNIFIED_V1_CASE21_MEMBRANE_REDISTRIBUTED_N48_PRODUCTION_GATE`

This next gate is an actual structural production calculation gate, not another integration-backend gate.
