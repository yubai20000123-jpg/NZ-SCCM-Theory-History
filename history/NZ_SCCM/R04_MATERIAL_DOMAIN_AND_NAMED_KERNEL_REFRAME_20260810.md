# R04 MATERIAL-DOMAIN AND NAMED-KERNEL REFRAME — 2026-08-10

## Trigger

After R03 demonstrated useful spectral separation on the Swartz24 geometry set, the user corrected the intended hierarchy: a production spectral domain should ultimately be based on the selected constitutive model's admissible range, otherwise the method becomes tied to the 24 ordinary-concrete panels and is not cleanly transferable to UHPC.

## Correction

R04 therefore changed the domain hierarchy from an implicit structure-first interpretation to:

```text
material constitutive source/model
-> material-admissible spectral domain Lambda_M   [PRIMARY]
-> scalar/material compiler qualification
-> structural reachable subset Lambda_R          [SECONDARY]
-> structural verification / optional acceleration
```

The Swartz24 R03 spectral certificate remains valid evidence inside its diagnostic D-q box, but is not a production material-domain definition.

## R04 kernel classification

R04 then classified the exact source-shaped rank-4 terms after the principal spectral substitution. The core algebraic observation is:

```text
Pi_eta : quadratic algebraic over lambda
C      : degree <=2
T      : degree <=8 due Pi + H1 + H10 quadratic extensions
U      : degree <=8
```

After `lambda±=mu±sqrt(Q)`, generic extension-degree upper bounds become approximately:

```text
U(lambda+)       <=16
C+^2 C-          <=8
C+ T-            <=32
T+ T-^8          <=128
```

These are upper bounds, not irreducibility theorems.

## Named-function outcome

The previously identified Appell F1 and Carlson symmetric elliptic families remain valuable exact-kernel tools for matching low-degree denominator classes. However the full exact `Pi_eta + H1 + H10` tension tower does not generically reduce to those classes.

```text
FULL_SOURCE_EXACT_APPELL_CLOSURE  = FAIL_GENERIC
FULL_SOURCE_EXACT_CARLSON_CLOSURE = FAIL_GENERIC
```

This is not a route failure. It is a negative result on a specific attempt to wrap the full exact source oracle with a small named special function.

## New problem statement

The remaining bottleneck is now explicitly one-dimensional and material-native:

> construct or select compact scalar principal-branch primitives on the constitutive model's own admissible domain, preserving stress, same-map tangent, conservative target physics and direct D15/small-kernel compatibility.

This formulation is deliberately transferable to UHPC because the architecture stays fixed while the material-domain metadata and scalar law change.

## Status

```text
R04 = PASS_WITH_NEGATIVE_SPECIAL_FUNCTION_RESULT
ROUTE_SWITCH = NO
NEXT = MATERIAL_NATIVE_1D_PRIMITIVE_REFORMULATION_R05
```
