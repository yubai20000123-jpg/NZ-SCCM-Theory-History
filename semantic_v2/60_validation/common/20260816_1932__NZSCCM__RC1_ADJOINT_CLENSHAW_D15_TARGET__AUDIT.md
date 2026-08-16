# NZ-SCCM — RC1 adjoint-Clenshaw / D15 target gate audit

**Timestamp:** 2026-08-16 19:32 +08:00

## A. Frozen mechanics audit

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = PRESERVED
Nguyen second-order = PRESERVED
five internal membrane coordinates = PRESERVED
R10 physical current law = UNCHANGED
reinforcement current adapter = UNCHANGED
General-D15 = PRESERVED
P,Rq,L root topology = PRESERVED
same-state tangent/KZ requirement = PRESERVED
```

No new structural response parameter was fitted.

## B. Material compiler identity

`R10-MSAC-RC1` remains the active material-level source-fidelity representation. Its Z0-Z6 first-pass levels, beta maps and source-fidelity acceptance are inherited from the 17:34 gate and are not reopened.

```text
R10_MSAC_RC1_MATERIAL_SOURCE_FIDELITY = PASS_RETAINED
```

The present failure is strictly the structural exact-moment adapter.

## C. Adjoint algebra audit

The transpose of the standard Clenshaw recurrence was derived and tested against an independently expanded exact nested polynomial under a closed D15 moment formula.

```text
DIRECT_MINUS_ADJOINT = 0 exactly
LOW_ORDER_TARGET_IDENTITY = PASS_EXACT
```

Thus `adjoint Clenshaw` is not rejected mathematically.

## D. Closure audit

The exact low-order test also showed the target kernel support increasing with composed degree:

```text
final nested polynomial degree = 192
contributing adjoint target degrees = 65,129,193
```

Therefore an adjoint graph is only a reorientation of the polynomial evaluation graph. Without an additional exact moment primitive for multiplication by a nested RC1 atom, it does not close in a finite low-order General-D15 target state.

```text
RC1_NESTED_ATOM_MOMENT_RULE = ABSENT
```

## E. Active-order deterministic preflight

The integer beta maps have exact degree `p+q+1`. Using the active first-pass RC1 orders gives:

```text
Z0 DuR=125,435,904; DTT~376,307,712
Z1 DuR= 77,414,400; DTT~232,243,200
Z2 DuR=125,435,904; DTT~376,307,712
Z3 DuR= 71,565,312; DTT~214,695,936
Z4 DuR=117,440,512; DTT~352,321,536
Z5 DuR=364,904,448; DTT~1,094,713,344
Z6 DuR=569,327,616; DTT~1,707,982,848
```

These are composition-degree diagnostics, not production polynomial orders. They establish that resolving the adjoint target all the way back to ordinary polynomial D15 leaves recreates the exact degree explosion RC1 was designed to avoid.

The gate correctly stops before a forbidden full flattening allocation.

## F. Spatial-integration audit

```text
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
N_formal_thickness_quadrature=0
Gauss=0
Simpson=0
adaptive=0
collocation=0
material-point grid=0
```

The low-order D15 check uses the closed analytic sine moment, not numerical quadrature.

## G. Capacity audit

```text
new current membrane r(D,q) solve = NOT_RUN
new Case21 Pu = NOT_RUN
new Z0-Z6 Pu = NOT_RUN
```

Existing historical/current-support capacities retain their previous identities only.

## H. Final verdict

```text
ADJOINT_CLENSHAW_ALGEBRA = PASS_EXACT
LOW_ORDER_GENERAL_D15_TARGET_IDENTITY = PASS_EXACT
ACTIVE_RC1_NESTED_TARGET_RUNTIME = FAIL_PREFLIGHT
RC1_STRUCTURAL_PRODUCTION_PROMOTION = FAIL_AT_THIS_GATE
R10_PHYSICAL_OPERATOR = NOT_REJECTED
RC1_MATERIAL_SOURCE_FIDELITY = NOT_REJECTED
```

## I. Next unique gate

```text
UNIFIED_V1_NC_EXACT_NESTED_ATOM_MOMENT_CLOSURE_OR_STRUCTURALLY_CLOSED_COMPILER_REDESIGN_GATE
```

The next gate must either add a true closed exact moment transform for the beta/natural-coordinate atoms or replace the compiler at family level with a source-faithful analytic/rational/special-function basis whose structural target moments close directly. Re-running forward or adjoint polynomial Clenshaw without such a closure is prohibited as a duplicate route.
