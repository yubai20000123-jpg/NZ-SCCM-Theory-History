# R06 POSTPEAK C2 AND COMPILER HEAD-TO-HEAD — 2026-08-10

## Context

R05 correctly moved spectral qualification from Swartz-defined ranges to material-native constitutive ranges and found that a simple Saenz continuation cannot reproduce Nguyen's 10% post-crushing residual at the source landmark `gamma2=10`.

R06 therefore had two locked tasks:

1. close the ordinary-concrete deep-postpeak scalar target at material level;
2. test whether the compactified scalar candidates actually improve D15 production complexity.

No Case21/Swartz Pu was allowed.

## Source correction

Recovered Nguyen source implementation confirms the post-crushing branch is linear from the peak to `0.1 sigma_p` at `gamma2 eps_p`, followed by a zero-tangent residual plateau. The prior R05 observation that pure Saenz gives about `0.198 fc` magnitude at `lambda=-10` is therefore a genuine source/target mismatch, not a numerical artifact.

## R06 C2 resolution

A C2 endpoint bridge was introduced only around the two tangent jumps while retaining the exact source linear branch in the middle.

```text
g(tau)=3 tau^5-8 tau^4+6 tau^3
delta_s=0.05
Delta_lambda=0.45 per endpoint
```

The bridge-width rule was material-only: extra compression relative to the exact source line <=1% fc. The executed maximum is `0.888889% fc`.

Thus the NC postpeak target is now closed at material-target level without restoring a runtime crushing state machine.

## Compiler screen outcome

Three existing representation ideas were compared on the material-native domain.

### Direct lambda polynomial

Degree 64 reached:

```text
stress max = 1.981970% fc
stress P95 = 0.185018% fc
tangent P95 = 3.365831% initial tangent
```

It has guaranteed finite D15 closure but generic Cayley-Hamilton reduction exposes 1088 unique `(J1,J2)` monomial pairs. Therefore it is not yet accepted under Gate C.

### Softsign

Degree 48 reached about 0.988% max stress error with 1.991% tangent P95, but its algebraic degree-4 structural kernel remains unclosed.

### Möbius

The new identity

```text
chi_M(E)=E(I-E)^-1=(E-J2 I)/(1-J1+J2)
```

eliminates explicit spectral square roots and leaves one invariant denominator

```text
Delta_M=1-J1+J2.
```

On the NC material-native square the pole is safely outside the domain. After Case21 substitution `Delta_M` is quadratic in thickness, making thickness integration elementary-recursive. The remaining in-plane master is not yet classified as a small named kernel.

## Decision

```text
R06 = PASS_POSTPEAK_C2__HOLD_FINAL_COMPILER
NC_POSTPEAK_C2_SCALAR_TARGET = PASS
GLOBAL_LAMBDA_N64 = PASS_MATERIAL_SCREEN / HOLD_GATE_C
SOFTSIGN_N48 = PASS_MATERIAL_SCREEN / HOLD_KERNEL
MOBIUS_N24_N48 = PROMISING / HOLD_KERNEL
```

No compiler winner is frozen.

## Next

```text
R07_HEAD_TO_HEAD_KERNEL_COMPLEXITY_DECISION_GLOBAL_POLY64_VS_MOBIUS24
```

R07 is forbidden to introduce another material family. It must decide whether the guaranteed-but-large direct polynomial D15 contraction is preferable to the lower-order Möbius representation after exact master-kernel reduction.
