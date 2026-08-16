# NZ-SCCM governance lock — source-regular matrix DAG + factorised algebraic-period target

**Timestamp:** 2026-08-17 01:00 +08:00

## 1. Boundary correction

```text
Z6_BOUNDARY = FOUR_EDGE_SIMPLY_SUPPORTED / SSSS
```

Current-mainline references that describe Z6 as a mixed in-plane-boundary specimen are superseded.

## 2. Retained physical/theory backbone

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = RETAIN
NGUYEN_SECOND_ORDER = RETAIN
R10_PHYSICAL_CURRENT_OPERATOR = FROZEN
REINFORCEMENT_BEFORE_COUPLED_ROOT = RETAIN
MEMBRANE_STRESS_REDISTRIBUTION = RETAIN
GENERAL_D15_TARGET_PHILOSOPHY = RETAIN
FORMAL_SPATIAL_SAMPLING = 0
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_SPATIAL_SUBDOMAINS = 1
FORMAL_THICKNESS_QUADRATURE = 0
```

Formal infinite/high-order analytic representation remains allowed; direct production enumeration of thousands of coefficients remains prohibited.

## 3. Source-level regularization decision

The 21:36 `c0,c1` apparent pole is not a physical source singularity.

At `x*=21/260`, the principal matrix square root is regular and its Sylvester derivative operator has condition number 1 in the retained prototype.

Therefore:

```text
OLD_RATIONALIZED_c0_c1_CONNECTION = RETIRED_AS_PRODUCTION_DIFFERENTIAL_REPRESENTATION
HAND_PATCHED_INTEGRAL_BASIS_ITERATION_ON_c0_c1 = DO_NOT_OPEN
```

Production source evaluation/tangent must stay at matrix/source level:

```text
smooth sqrt node:
    R=sqrt(M)
    RR'+R'R=M'

source spline knot powers:
    D_+^p=((D+sqrt(D^2))/2)^p, p=3,4,5
    tangent by finite divided-difference/Frechet derivative of z_+^p

T^7 interaction:
    exact 2x2 Cayley-Hamilton reduction
```

The true Foster knot events remain source-defined material events. They are not spatial cells and are not to be smoothed away by a compiler approximation.

## 4. Real-target preflight decision

The actual compression stress subtarget

`Yc = det(C)*Cyy`

was executed in the retained smooth four-state algebraic field and has an exact algebraic characteristic polynomial of degree 4 in `Y`.

Thus compact algebraic target closure is real, not toy-only.

However, explicitly canonicalizing a scalar differential annihilator over `Q(x)` exceeded the fail-fast symbolic runtime in multiple equivalent SymPy implementations.

Therefore:

```text
TARGET_ALGEBRAICITY = RETAIN
EXPLICIT_GIANT_RATIONAL_ANNIHILATOR_COEFFICIENTS = NOT_A_PRODUCTION_REQUIREMENT
INCREASE_SYMPY_TIMEOUT_AND_KEEP_EXPANDING = PROHIBITED
HIGH_ORDER_CHEBYSHEV_ESCAPE = PROHIBITED
```

## 5. Selected production representation

The next target runtime shall retain a **factorised algebraic-period / descriptor object** rather than flattening it into a giant coefficient vector.

Conceptually:

```text
regular R10 source matrix DAG
 -> finite algebraic target object
 -> factorised period/descriptor contraction
 -> actual thickness P/Rm target value + same-source derivative
```

The old 64-state result remains the finite algebraic-degree/state bound and closure proof. The runtime is not required to canonicalize all 64 coefficient functions individually.

## 6. Anti-loop termination contract

The next execution is allowed to implement only one remaining thickness target layer:

`FULL_COMPACT_R10_FACTOR_GRAPH_ALGEBRAIC_PERIOD_TARGET_EVALUATOR`

It must attempt an actual full 21:18 `Syy` or `Rm` target.

Pass only if it returns:

```text
1. a bounded finite algebraic/descriptor state;
2. complete-thickness target value without formal numerical quadrature;
3. consistent derivative information from the same source DAG;
4. no N1000/N3000/etc coefficient enumeration;
5. no new spatial cells/subdomains/material points.
```

If that cannot be achieved, stop at the mathematical blocker. Do not automatically create another exact-backend layer.

## 7. Capacity status

```text
NEW_CORRECTED_MEMBRANE_Pu = NOT_RUN
CASE21 = CONTROL CASE AFTER TARGET EVALUATOR CLOSES
Z6 = SSSS HIGH-MEMBRANE-EFFECT CASE AFTER CONTROL
```
