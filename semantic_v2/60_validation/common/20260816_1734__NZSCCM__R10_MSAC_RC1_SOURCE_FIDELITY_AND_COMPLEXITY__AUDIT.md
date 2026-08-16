# NZ-SCCM — R10-MSAC-RC1 source-fidelity and complexity audit

**Timestamp:** 2026-08-16 17:34 +08:00  
**Status:** `PASS_MATERIAL_LEVEL / STRUCTURAL_ADAPTER_NOT_YET_CERTIFIED`

## 1. Audit object

`R10-MSAC-RC1` is a reconstructed multiscale finite analytic material representation built on the already-certified specimen-derived material domains.

It keeps R10 physics unchanged and reconstructs the historical architecture:

```text
source gate -> natural compression/tension coordinates -> U reassembly
```

with finite beta-lens coordinate maps around source landmarks.

## 2. Common-policy audit

The following are identical for Z0-Z6:

```text
zero-gate rational-center rule: limit denominator 32
alpha_g = 30
source tension landmarks = xcr, 10*xcr when present
landmark rational-center rule = limit denominator 32
alpha_t = 50 for each tension lens
origin C1 constraints
projection node rule M=8*(N+1)
full 2D source-current stress/tangent/divided-difference gates
common resolution ladder L0-L8
first-pass + next-level-pass requirement
```

No case ID, experiment, Zhou/Winter value or target Pu is used in map/order selection.

## 3. Full 2D source-current qualification

First-pass results:

|case|level|E_sigma|E_tangent|E_div|next-level check|
|---|---|---:|---:|---:|---|
|Z0|L2|6.2615e-4|3.1169e-2|5.1875e-3|PASS|
|Z1|L3|5.0341e-4|2.6679e-2|3.3291e-3|PASS|
|Z2|L2|6.2615e-4|3.1169e-2|5.1875e-3|PASS|
|Z3|L2|6.1103e-4|3.0264e-2|3.7782e-3|PASS|
|Z4|L2|7.4547e-4|3.7915e-2|4.6746e-3|PASS|
|Z5|L6|6.4896e-4|3.6084e-2|2.2104e-2|PASS|
|Z6|L7|8.8611e-4|3.7454e-2|1.4228e-2|PASS|

Gates:

```text
E_sigma <= .005
E_tangent <= .05
E_divided_difference <= .05
```

All first passing candidates satisfy all gates. All immediately subsequent ladder levels also pass. Therefore no isolated one-level accidental pass controls the decision.

## 4. Complexity audit

Previous one-global-lambda first-pass coefficient counts on the corrected domains were 6148-15364. RC1 uses 1555-3477 finite scalar coefficients.

```text
minimum reduction ratio = 3.1707x
maximum reduction ratio = 4.6122x
```

The largest current compiler is Z6:

```text
Ng=1152
Nc=16
Nt=576
finite scalar coefficients=3477
```

This is still machine-code complexity rather than material-parameter count. The physical R10 parameters remain the source constants.

## 5. Origin consistency

The constrained factor compiler restores the required origin conditions to roundoff. Z6 first-pass values include

```text
|c_hat(0)| < 1e-16
|t_hat(0)| < 1e-16
|c_hat'(0)| < 3e-14
|t_hat'(0)| < 3e-14
|U_hat(0)| < 4e-16
U_hat'(0)=2.000512953368
```

Hence the tangent qualification is not purchased by relaxing the initial elastic slope.

## 6. Full-expansion rejection

The nested beta-lens/Chebyshev object is finite, but ordinary-polynomial expansion would multiply degrees. First-pass naive expanded gate degrees range from 8960 to 29952; tension-map degrees reach up to 19008.

Therefore:

```text
FINITE_ANALYTIC_FACTOR_GRAPH = YES
NAIVE_FULL_MONOMIAL_EXPANSION = REJECTED
```

This is not a contradiction. The production object is the nested finite factor graph, not its catastrophically expanded monomial form.

## 7. Structural integration boundary

This audit does not certify the RC1-to-D15 structural adapter.

The historical Case21 route already demonstrated the correct mathematical pattern:

```text
nested scalar basis / Q_nm
 -> target-functional moment contraction
 -> immediately discard spatial field
```

The current RC1 object must now be connected to that moment-first backend without full expansion.

Formal counters in this gate remain:

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

Material-coordinate coefficient/audit nodes are excluded from these structural counters.

## 8. Final audit verdict

```text
R10_PHYSICS = PASS_UNCHANGED
PARAMETER_DERIVED_DOMAIN = PASS_RETAINED
COMMON_RC1_MAP_POLICY = PASS
FULL_2D_STRESS_GATE_Z0_Z6 = PASS
FULL_2D_CONSISTENT_TANGENT_GATE_Z0_Z6 = PASS
DIVIDED_DIFFERENCE_GATE_Z0_Z6 = PASS
NEXT_LEVEL_CONFIRMATION_Z0_Z6 = PASS
ORIGIN_C1 = PASS_ROUNDOFF
COMPLEXITY_REDUCTION_VS_GLOBAL = PASS_MATERIAL_REPRESENTATION
FULL_EXPANSION = PROHIBITED
NESTED_D15_STRUCTURAL_ADAPTER = OPEN
NEW_Pu = NOT_RUN
```

Next gate:

```text
UNIFIED_V1_R10_MSAC_RC1_NESTED_CLENSHAW_QNM_D15_CONTRACTION_GATE
```
