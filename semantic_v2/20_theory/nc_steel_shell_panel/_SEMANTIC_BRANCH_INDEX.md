# Concrete + steel-shell semantic branch

## Parent theory

Locked parent governance:

- `semantic_v2/10_governance/20260813_1834__NZSCCM__NC_PANEL__ENERGY_MINIMUM_HALFWAVE_R10_N48C1MM_D15_DIRECT_LIMIT__LOCKED_BASELINE.md`

The parent locks:

```text
one theoretical energy-minimum complete halfwave
D,q Nguyen second-order kinematics with membrane terms included
energy-fitted R10 concrete target
current N48-C1/MM compiler with specimen/design-dependent material interval
Cayley-Hamilton 2D lift
full directional current tangent
general-D15 exact multiple integrals
zero formal spatial quadrature
direct Rq=0,L=0 first +->- limit solve
same-branch Zhou/Navier stability check
```

## Active structural extension

- `20260813_1834__NZSCCM__NC_STEEL_SHELL_PANEL__REBAR_REPLACEMENT_GENERAL_D15__THEORY_EXTENSION_CONTRACT.md`

The extension removes the reinforcement contribution and replaces it by one or more bonded finite-thickness continuous steel-shell layers.

Structurally closed identities:

```text
P = Pc + Psh
Rq = Rq,c + Rq,sh
L = P_D Rq,q - P_q Rq,D
KZ = KZ,c + KZ,sh
```

Each steel-shell layer is integrated exactly through its own thickness coordinate; no shell Gauss points or material-point grid are introduced.

## Active steel-material derivation

- `20260813_1834__NZSCCM__STEEL_SHELL__J2_DEFORMATION_THEORY_SOURCE_CURVE_PLANE_STRESS__MATERIAL_OPERATOR_DERIVATION.md`

This derives a path-independent full 2D plane-stress current operator by lifting an approved uniaxial steel source curve through J2 deformation theory. The map reduces the multiaxial update to one scalar equivalent-stress constitutive equation, exactly recovers the uniaxial source curve, exactly degenerates to standard elastic plane stress, and provides an analytic consistent tangent by implicit differentiation.

The structural test set is not used in this derivation.

## Remaining gate before production Pu

The steel operator is **not yet production-frozen**. Required source-only gates include:

```text
freeze steel-grade uniaxial source curve
verify full material-only tangent
freeze invariant material compiler/domain
verify general-D15 coefficient closure
check monotonic/proportional suitability
```

After these pass, the operator can be inserted directly into `Psh,Rq,sh,L,KZ,sh` without reopening the locked concrete theory.
