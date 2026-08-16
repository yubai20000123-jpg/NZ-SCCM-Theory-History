# NZ-SCCM — Z0–Z5 fixed-N48 current-operator fidelity rebuild lock

**Timestamp:** 2026-08-16 11:34 +08:00  
**Status:** CURRENT GOVERNANCE LOCK

## User order constraint

By explicit user instruction, the material compiler order is fixed:

```text
MATERIAL_COMPILER_ORDER = 48
U  = degree 48
C  = degree 48
T  = degree 48
T7 = degree 48
```

No primitive-specific order escalation is permitted unless the user explicitly reopens the order decision.

The 11:10 multirate candidate `R10-MR-C1(256,1024,1280,512)` remains historical diagnostic evidence only and is not current production.

## Frozen physical / structural boundary

```text
R10 physical current operator = FROZEN / UNCHANGED
PRODUCTION_BOUNDARY = THEORETICAL_FOUR_EDGE_SIMPLY_SUPPORTED
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
Nguyen second-order kinematics = ACTIVE
Cayley-Hamilton = ACTIVE
General D15 exact moments = ACTIVE
A0=a/500
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
Zhou/Winter calibration=PROHIBITED
```

## Gate question

Can the already-fixed single global degree-48 Chebyshev space, with exact R10 C1 anchors at `lambda=0`, be repaired **only by coefficient generation** so that the frozen R10 current operator is materially faithful over conservative Z0–Z5 AR2 material envelopes?

This gate does not solve Pu. It first determines whether coefficient-only repair inside the same N48 polynomial space is representationally adequate.

## Conservative source-only material intervals

The following intervals are inherited from the 10:54 source-only precheck. They envelope the challenged continuous material ranges with engineering margins and do not use experimental loads or Zhou/Winter capacities:

```text
Z0 [-1.25,+0.30]
Z1 [-0.85,+0.25]
Z2 [-1.50,+0.35]
Z3 [-0.95,+0.25]
Z4 [-1.25,+0.25]
Z5 [-1.15,+0.15]
```

## Strongest coefficient-only test

For each primitive `F in {U,C,T,T7}`, solve the source-only degree-48 constrained minimax problem

`min ||p48-F_R10||_infinity`

subject to the exact R10 C1 conditions at `lambda=0`.

For T this is the strongest possible value-fidelity coefficient-only test within the fixed degree-48 C1 affine space. If even this near-minimax solve retains order-0.1 source error in the occupied mixed tension/compression region, the old N48 coefficient generator cannot be repaired merely by changing weights, sampling density or least-squares details.

Material-coordinate LP/exchange nodes are coefficient-generation/audit coordinates only; they are not structural spatial points.

## Fail-fast rule

If fixed single-global N48 coefficient-only fidelity fails, do not compute corrected Z0–Z5 Pu and do not increase degree. Preserve N48 and move only to a fixed-order multiscale/analytic representation gate that retains the same order ceiling and zero structural spatial integration.