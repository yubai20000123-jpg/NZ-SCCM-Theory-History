# NC ENERGY POTENTIAL + D15 GATE DECISION

**Date:** 2026-08-10

## Decision

```text
NC_ENERGY_POTENTIAL_AND_D15_FEASIBILITY_GATE = FAIL__STOP_AT_GATE
```

The gate was executed exactly at material + D15-feasibility level. No Case21/Swartz structural solution followed.

## What passed

- material-energy contract: PASS;
- energy-equivalent tensile preprocessing: PASS;
- single global current-work potential concept: PASS IN PRINCIPLE;
- finite polynomial potential -> invariant polynomial -> D15 exact moments: PASS;
- formal structural spatial quadrature count: ZERO.

For a 2x2 equivalent-uniaxial strain tensor `Eu`, Cayley-Hamilton gives

\[
E_u^2-J_1E_u+J_2I=0,
\]

so with `s_n=tr(Eu^n)`:

\[
s_0=2,\qquad s_1=J_1,\qquad s_n=J_1s_{n-1}-J_2s_{n-2}.
\]

Thus any finite polynomial material potential reduces exactly to a finite polynomial in `J1,J2`; after inserting the frozen Nguyen second-order kinematics, D15 exact moments close it with zero spatial numerical quadrature.

## What failed

### Anchor-exact low-parameter global polynomial

A degree-7 stress polynomial uniquely fixed by compression peak/residual anchors plus retained tensile work developed catastrophic interior oscillation:

```text
minimum stress ≈ -12965.289 fc at lambda ≈ -7.2363
```

Therefore anchor exactness does not make a low-order global polynomial mechanically admissible.

### Energy-first low-order global potential

A single global Chebyshev potential was fitted to MATERIAL work only, while exact anchor constraints were enforced. Only degrees 8, 10 and 12 were tested. At N=12 the potential error was much smaller, but derivatives were still mechanically unacceptable:

```text
stress max abs error     ≈ 0.879 fc
stress P95 abs error     ≈ 0.406 fc
tangent max abs error    ≈ 9.919 (normalized)
spurious compression in tension ≈ 0.810 fc
```

Hence an energy function can look much better than its first/second derivatives. This directly confirms the need to gate the derivative chain, not only the energy fit.

## Fail-fast boundary

No attempt was made to increase global polynomial degree beyond N=12.

No structural global target was fitted.

No offline spatial quadrature was used to generate a production structural operator.

No Case21 ultimate load and no Swartz24 load was calculated after this failure.

## Current consequence

The energy-potential philosophy remains valid, but the **current low-order global polynomial grammar is rejected**.

A new material-potential grammar may only be explored after explicit user approval. Any future grammar must first prove:

1. few physically meaningful material parameters;
2. no runtime TT/TC/CC spatial material partition;
3. explicit stress and tangent from the same potential;
4. zero-spatial-quadrature closure before structural calculation;
5. no rescue by hidden high-degree/global coefficient inflation.
