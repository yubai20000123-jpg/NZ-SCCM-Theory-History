# NZ-SCCM — full R10 quadratic-tower 64-state compositum audit

**Timestamp:** 2026-08-16 20:59 +08:00

## A. Frozen mechanics

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = PRESERVED
Nguyen second-order = PRESERVED
five internal membrane coordinates = PRESERVED
R10 physical current law = UNCHANGED
reinforcement adapter = UNCHANGED
outer root topology = (D,q) after condensation
P,Rq,L topology = PRESERVED
same-state KZ requirement = PRESERVED
```

## B. Zero-integration audit

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

No structural production quadrature was used.

## C. Algebraic field audit

The retained atom set `s_eta,s_1,s_10` has been represented as three nested quadratic pairs `(q,s)`:

```text
q^2=Q
s^2=A+2q
```

so each local basis is exactly `[1,q,s,qs]` and the total basis is `4^3=64`.

The derivative formulas were derived directly from the defining quadratic identities, not fitted from values.  They close inside the same local basis.

```text
THREE_GENERATOR_QUADRATIC_TOWER = PASS_EXACT_PARAMETRIC
FULL_64_STATE_DERIVATIVE_CLOSURE = PASS_EXACT
```

## D. Sparsity audit

The full derivative operator is a Kronecker sum of three local 4x4 operators.  Pattern enumeration gives exactly

```text
63 diagonal/self entries
96 off-diagonal q-toggle entries
159 total nonzeros / 4096 possible
```

A dense 64x64 field matrix is therefore not required.

## E. Moment audit

For `d V'=B V`, the vector moment identity

```text
[x^n d V]_-1^1
= sum_j (n+j)d_j M_(n+j-1)
+ sum_j B_j M_(n+j)
```

follows exactly by one integration-by-parts operation.  No spatial/thickness quadrature enters the formal operator.

```text
FULL_64_STATE_VECTOR_MOMENT_FORM = PASS_EXACT
```

## F. Actual R10 source-graph audit

The executable prototype assembled the actual source chain through `T^7` in the quadratic-tower field.

Observed support:

```text
t: 3 states/entry
H1: 2-3 states/entry
uR: 20 states/entry
T7: 64 states/entry
tr(T7): 64 states
```

Therefore the actual R10 graph reaches the complete compositum.

The prototype knot values were rationalized only for symbolic runtime timing.  That rationalization is not accepted as a production material representation and does not replace the exact R10 algebraic knot roots.

## G. Fail-fast audit

Naive flattened canonicalization of the complete `tr(T7)` rational coefficient vector with `SymPy.cancel` did not complete within the 60 s execution limit.  The smaller `tr(uR)` flattening also exceeded the same limit.

This does not invalidate the 64-state field closure.  It rejects only this implementation route:

```text
factorized 64-state field
 -> flatten all coefficient DAGs
 -> canonicalize giant rational expressions
```

The next implementation must preserve the factor graph and perform target-side/adjoint reduction in the fixed finite state.

## H. Distinction from old RC1 adjoint failure

The old adjoint-Clenshaw failure retained an ordinary-polynomial terminal algebra, so target support inherited nested material composition degree.

The present field satisfies six exact quadratic relations and every product is reduced back to 64 states immediately.  Thus target-side propagation on this field cannot create an unbounded polynomial-degree hierarchy.

## I. Capacity audit

```text
new current membrane r(D,q) solve = NOT_RUN
new Case21 Pu = NOT_RUN
new Z0-Z6 Pu = NOT_RUN
```

Historical/current-support capacities retain their prior identities only.

## J. Final verdict

```text
THREE_GENERATOR_QUADRATIC_TOWER = PASS_EXACT_PARAMETRIC
FULL_64_STATE_DERIVATIVE_CLOSURE = PASS_EXACT
FULL_64_STATE_VECTOR_MOMENT_FORM = PASS_EXACT
FULL_R10_T7_64_BASIS_SUPPORT = PASS_EXECUTED_DIAGNOSTIC
NAIVE_FLATTENED_RATIONAL_COEFFICIENT_NORMALIZATION = FAIL_TRACTABILITY
FULL_R10_THICKNESS_TARGET_CONTRACTION = PARTIAL_PASS_TO_ADJOINT_DAG_BOUNDARY
BETA_WEIGHTED_XY_CREATIVE_TELESCOPING = OPEN
NEW_Pu = NOT_RUN
```

## K. Next unique gate

```text
UNIFIED_V1_FULL_R10_64_STATE_ADJOINT_RATIONAL_TARGET_REDUCTION_GATE
```
