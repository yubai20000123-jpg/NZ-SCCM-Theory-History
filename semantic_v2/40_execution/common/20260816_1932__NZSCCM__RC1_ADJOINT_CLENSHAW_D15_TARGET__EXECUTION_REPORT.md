# NZ-SCCM — RC1 adjoint-Clenshaw / D15 target-functional execution report

**Timestamp:** 2026-08-16 19:32 +08:00  
**Requested gate:** `UNIFIED_V1_RC1_ADJOINT_CLENSHAW_GENERAL_D15_TARGET_FUNCTIONAL_EXECUTION_GATE`  
**Result:** `LOW_ORDER_EXACT_PASS / ACTIVE_ORDER_PREFLIGHT_FAIL / NO Pu RUN`

## 1. Inputs retained

The run inherits without modification:

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order continuous kinematics
five compatible internal membrane coordinates
R10 physical current operator
R10-MSAC-RC1 material-level source fidelity PASS
reinforcement current adapter
Cayley-Hamilton
General-D15 exact moments
P,Rq,L connected-branch topology
same-state current tangent/KZ requirement
```

The first-pass RC1 settings are retained exactly from the 17:34 material gate:

```text
Z0 L2: Ng=512,  Nc=14, Nt=256, gate B23,5, tension B3,29;B29,2
Z1 L3: Ng=640,  Nc=14, Nt=320, gate B11,2, tension B3,23
Z2 L2: Ng=512,  Nc=14, Nt=256, gate B23,5, tension B3,29;B29,2
Z3 L2: Ng=512,  Nc=14, Nt=256, gate B17,3, tension B3,22
Z4 L2: Ng=512,  Nc=14, Nt=256, gate B25,6, tension B2,23;B22,5
Z5 L6: Ng=1024, Nc=14, Nt=512, gate B16,7, tension B1,27;B5,9
Z6 L7: Ng=1152, Nc=16, Nt=576, gate B14,11, tension B1,31;B4,15
```

No experiment, Zhou/Winter result or desired Pu entered the calculation.

## 2. Exact adjoint-Clenshaw implementation check

For a target functional `L_K`, the transpose of the ordinary backward Clenshaw graph was derived and executed.

A symbolic exact-rational low-order nested beta/Chebyshev test was constructed over the exact D15 moment oracle

```text
int_0^pi sin^(2m) X dX = pi*C(2m,m)/4^m.
```

Test configuration:

```text
base s = 1/3 + z/5, z=sin^2 X
first beta lens: p=2,q=1,alpha=3
first outer Chebyshev degree=4
second beta lens: p=1,q=2,alpha=2
second outer Chebyshev degree=3
target kernel K=1+2z
all test coefficients exact rationals
```

Observed exact degrees:

```text
first warp degree       4
first composed degree  16
second warp degree     64
final nested degree   192
```

Direct exact expansion and adjoint-target evaluation gave

```text
DIRECT_MINUS_ADJOINT = 0 exactly
functional/pi = 0.11633931515896061
```

The contributing adjoint target kernels had degrees

```text
k=1 -> 65
k=2 -> 129
k=3 -> 193
```

The symbolic run completed in approximately `3.73 s` in the present Python/SymPy environment.

Decision:

```text
ADJOINT_CLENSHAW_ALGEBRA = PASS_EXACT
LOW_ORDER_GENERAL_D15_TARGET_IDENTITY = PASS_EXACT
```

## 3. Exact beta degree rule

For integer beta lens `B(p,q)`, the normalized antiderivative is a finite polynomial of degree

```text
d_beta=p+q+1.
```

Therefore the active RC1 nested degree propagation can be calculated exactly before attempting any giant structural object.

For a case with `dg` and maximum tension-lens degree `dt`:

```text
Dg = Ng*dg
DC = Nc*Dg
Dt_nat = Nt*dt
DuR = DT7 = Dg*Dt_nat
DCC ~= 3*DC
DTC ~= DC+DuR
DTT ~= 3*DuR
```

The last three are nominal total-degree scales of the two-principal-value R10 interaction graph, not proposed solver orders.

## 4. Z0-Z6 active-order preflight

|case|Dg|DC|Dt_nat|DuR=DT7|DTT nominal|1D float64 DTT-equivalent|
|---|---:|---:|---:|---:|---:|---:|
|Z0|14,848|207,872|8,448|125,435,904|376,307,712|3.01 GB|
|Z1|8,960|125,440|8,640|77,414,400|232,243,200|1.86 GB|
|Z2|14,848|207,872|8,448|125,435,904|376,307,712|3.01 GB|
|Z3|10,752|150,528|6,656|71,565,312|214,695,936|1.72 GB|
|Z4|16,384|229,376|7,168|117,440,512|352,321,536|2.82 GB|
|Z5|24,576|344,064|14,848|364,904,448|1,094,713,344|8.76 GB|
|Z6|29,952|479,232|19,008|569,327,616|1,707,982,848|13.66 GB|

The memory column is only a one-dimensional dense float64 degree-index equivalent. It is **not** an estimate of the actual production storage. Actual CH/invariant/D15 states have more analytic indices, and TT is a cross-principal-value interaction, so naive exact flattening is more expensive.

Z6 is the clearest fail-fast example:

```text
gate/c,t lambda-equivalent degree  = 29,952
C lambda-equivalent degree         = 479,232
uR/T7 lambda-equivalent degree     = 569,327,616
TT nominal total-degree scale      = 1,707,982,848
```

A target-side recurrence with no special nested-atom moment rule postpones this growth but does not eliminate it. The low-order exact run explicitly demonstrated the same mechanism: target support increased by the nested composed degree.

## 5. Why no active-order giant allocation was attempted

The project explicitly prohibits full nested flattening. Allocating hundreds of millions to billions of exact degree states merely to confirm the already-determined degree propagation would both violate the intended RC1 factorized architecture and waste resources.

The gate therefore uses the deterministic polynomial-degree preflight as a fail-fast condition before creating the forbidden giant representation.

This is analogous to rejecting an FE/material-point path before running it when its discretization identity violates the project contract; it is not an unexecuted guess.

## 6. Structural interpretation

The adjoint idea was useful but insufficient:

```text
forward Clenshaw:
  stores high-order materialized stress/CH fields -> known swell

adjoint Clenshaw:
  stores/propagates target kernels instead
  -> algebraically exact
  -> but target kernels still require multiplication by nested RC1 atoms
  -> without a closed atom-moment rule, they eventually expand into the same base D15 degree hierarchy
```

Thus the missing structural object is not another Clenshaw direction. It is an exact finite moment closure for the nested atom itself.

## 7. Five membrane targets

The five current membrane targets remain valid and unchanged:

```text
Rm0   : D15[Sxx]
Rm20  : D15[Sxx*cos2X]
Rmu22 : D15[Sxx*cos2X*cos2Y-Sxy*sin2X*sin2Y]
Rm02  : D15[Syy*cos2Y]
Rmv22 : D15[Syy*cos2X*cos2Y-Sxy*sin2X*sin2Y]
```

They are not the cause of the failure. The same material closure problem already occurs for `P` and `Rq`.

## 8. Formal integration counters

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
spatial_Gauss = 0
spatial_Simpson = 0
spatial_adaptive = 0
spatial_collocation = 0
material_point_grid = 0
```

The symbolic low-order test used exact analytic D15 moments only.

## 9. Gate decision

```text
R10_MSAC_RC1_MATERIAL_SOURCE_FIDELITY = RETAIN_PASS
FIVE_TERM_MEMBRANE_D15_CLOSURE = RETAIN_PASS
ADJOINT_CLENSHAW_TARGET_RECURRENCE = PASS_EXACT_ALGEBRA
LOW_ORDER_NESTED_TARGET_IDENTITY = PASS_EXACT
ACTIVE_RC1_NESTED_TARGET_PREFLIGHT = FAIL
RC1_NESTED_ATOM_MOMENT_CLOSURE = NOT_AVAILABLE
RC1_STRUCTURAL_PRODUCTION_PROMOTION = FAIL_AT_THIS_GATE
NEW_CURRENT_MEMBRANE_r_SOLVE = NOT_RUN
NEW_Pu = NOT_RUN
```

## 10. Current unique next gate

```text
UNIFIED_V1_NC_EXACT_NESTED_ATOM_MOMENT_CLOSURE_OR_STRUCTURALLY_CLOSED_COMPILER_REDESIGN_GATE
```

The next gate may not repeat ordinary forward/adjoint polynomial Clenshaw and call it a new route. It must either:

1. derive an exact closed target-moment transform for beta/natural-coordinate RC1 atoms, or
2. redesign the NC analytic compiler at family level into a source-faithful basis whose moments are directly closed by General-D15/CAS/special-function algebra.

No specimen-only fallback, spatial quadrature, coefficient threshold pruning or new Pu release is permitted.
