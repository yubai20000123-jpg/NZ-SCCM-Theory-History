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

## Active extension

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

## Only new open item before production Pu

```text
STEEL_SHELL_2D_CURRENT_OPERATOR = SOURCE-CONSISTENT FREEZE PENDING
```

The steel operator must be plane-stress, full 2D, provide a consistent directional tangent, remain compatible with finite analytic compilation/general-D15, and must not be selected using structural test Pu.
