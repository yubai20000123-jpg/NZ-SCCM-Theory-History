# NZ-SCCM — R10-MSAC-RC1 multiscale compiler reconnection execution report

**Timestamp:** 2026-08-16 17:34 +08:00  
**Gate:** `UNIFIED_V1_PARAMETER_DERIVED_DOMAIN_PLUS_HISTORICAL_MULTISCALE_COMPILER_RECONNECTION_GATE`  
**Result:** `PASS_MATERIAL_LEVEL_Z0_Z6 / STRUCTURAL_NESTED_D15_ADAPTER_OPEN / NO Pu RUN`

## 1. Why this gate was executed

The 17:20 gate corrected the project governance error that had forced every NC specimen to carry one identical material interval. The same source/design-side domain rule now generates a specimen-specific certified material domain.

However the one-global-lambda polynomial remained expensive even after that correction. The present gate therefore reconnects the earlier R3/R4/R5 multiscale/source-landmark compiler architecture to the corrected specimen-derived domains before any R10 material change is considered.

## 2. Historical architecture restored

The recovered history establishes four useful rules:

1. compile the difficult source factors in coordinates matched to their physical scale;
2. derive the compiler interval from an analytic structural reachability certificate, not from plate Pu;
3. keep source landmarks such as zero strain and cracking/tension-stiffening scales explicit;
4. never expand the complete nested compiler into a huge spatial polynomial before D15; contract the factor graph into the target moments instead.

The current candidate is named `R10-MSAC-RC1`. It is a deterministic reconstruction of those principles on the current R10 source and current Z0-Z6 domains; it is not claimed to be a byte-for-byte recovery of an old NC-MSAC-v1 executable.

## 3. RC1 finite analytic factor graph

For each specimen-derived guard `[a,b]`:

\[
s=(\lambda-a)/(b-a),\qquad s_0=-a/(b-a).
\]

A finite beta lens is centered near `s0` by the universal rule

```text
Fraction(s0).limit_denominator(32)=p_g/(p_g+q_g)
alpha_g=30
```

and defines

\[
\chi_g(s)=-1+2\frac{s+30I_{p_g,q_g}(s)}{1+30I_{p_g,q_g}(1)}.
\]

The two R10 sign-split factors are then compiled as

\[
\hat c(\lambda)=\sum_{n=0}^{N_g}c_nT_n[\chi_g(s)],
\qquad
\hat t(\lambda)=\sum_{n=0}^{N_g}t_nT_n[\chi_g(s)],
\]

with exact origin C1 constraints.

The compression factor is compiled in its natural nonnegative coordinate:

\[
\hat C(c)=\sum_{n=0}^{N_c}a_nT_n(\xi_c),
\]

with `C(0)=0`, `C_c(0)=kappa`.

The tension coordinate uses source landmarks `t=xcr` and `t=10*xcr` whenever present. Their normalized positions are converted by the same rational-center rule; each beta lens uses `alpha_t=50`. `uR(t)` and `T7(t)` are then compiled directly in that multi-lens coordinate.

Finally

\[
T=\hat u_R/\rho,
\qquad
\boxed{\hat U=\kappa\lambda-\hat C+\kappa\hat c+\hat u_R-\kappa\hat t}.
\]

`U` is not independently fitted.

## 4. Common source-only resolution ladder

The same ladder was used for every specimen:

|level|Ng|Nc|Nt|
|---|---:|---:|---:|
|L0|256|10|128|
|L1|384|12|192|
|L2|512|14|256|
|L3|640|14|320|
|L4|768|14|384|
|L5|896|14|448|
|L6|1024|14|512|
|L7|1152|16|576|
|L8|1280|16|640|

Acceptance requires

```text
E_sigma <= .005
E_tangent <= .05
E_divided_difference <= .05
```

for the complete two-principal-value R10 current master. The next ladder level after the first pass must also pass.

## 5. Z0-Z6 material result

|case|first level|Ng|Nc|Nt|finite scalar coeffs|E_sigma|E_tangent|E_div|next level|
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
|Z0|L2|512|14|256|1555|6.2615e-4|3.1169e-2|5.1875e-3|L3 PASS|
|Z1|L3|640|14|320|1939|5.0341e-4|2.6679e-2|3.3291e-3|L4 PASS|
|Z2|L2|512|14|256|1555|6.2615e-4|3.1169e-2|5.1875e-3|L3 PASS|
|Z3|L2|512|14|256|1555|6.1103e-4|3.0264e-2|3.7782e-3|L3 PASS|
|Z4|L2|512|14|256|1555|7.4547e-4|3.7915e-2|4.6746e-3|L3 PASS|
|Z5|L6|1024|14|512|3091|6.4896e-4|3.6084e-2|2.2104e-2|L7 PASS|
|Z6|L7|1152|16|576|3477|8.8611e-4|3.7454e-2|1.4228e-2|L8 PASS|

Worst first-pass values are therefore

```text
E_sigma = .0008861083
E_tangent = .0379151680
E_divided_difference = .0221037356
```

All are inside the previously frozen source-fidelity gates.

## 6. Maps generated automatically from each specimen domain

|case|zero gate beta lens|tension beta lenses|
|---|---|---|
|Z0|B23,5|B3,29 ; B29,2|
|Z1|B11,2|B3,23|
|Z2|B23,5|B3,29 ; B29,2|
|Z3|B17,3|B3,22|
|Z4|B25,6|B2,23 ; B22,5|
|Z5|B16,7|B1,27 ; B5,9|
|Z6|B14,11|B1,31 ; B4,15|

These are not case-ID choices. They are deterministic outputs of the same domain-normalization, source-landmark and denominator-32 rational-center rules.

The exact compiler parameters, natural-coordinate domains, anchor residuals, coefficient hashes and full order histories are stored in the JSON intermediate ledger.

## 7. Complexity reduction relative to the corrected one-global-lambda baseline

Previous first passing single-global-lambda results on the same specimen-derived domains were:

```text
Z0 1792 / 7172 coefficients
Z1 1536 / 6148
Z2 1792 / 7172
Z3 1536 / 6148
Z4 1792 / 7172
Z5 3072 / 12292
Z6 3840 / 15364
```

RC1 gives maximum outer orders from 512 to 1152 and coefficient counts from 1555 to 3477.

Coefficient-count reduction ranges from approximately

\[
\boxed{3.17\times\text{ to }4.61\times}.
\]

For Z6 specifically:

```text
old: N=3840, 15364 scalar coefficients
RC1: Ng=1152, Nc=16, Nt=576, 3477 scalar coefficients
```

so the stored coefficient count is reduced by approximately `4.42x`.

This is not yet the final structural cost, because the representation must remain nested.

## 8. Origin anchors

The constrained compiler restores the required R10 origin conditions to roundoff. For example Z6 first-pass RC1 gives approximately

```text
c_hat(0) = -7.63e-17
t_hat(0) = +4.86e-17
c_hat'(0)= -2.77e-14
t_hat'(0)= -2.68e-14
C_hat(0) = +2.22e-16
uR_hat(0)= +1.11e-16
T7_hat(0)= +4.44e-16
U_hat(0) = -3.61e-16
U_hat'(0)= 2.000512953368
```

Thus the tangent improvement is not obtained by relaxing the elastic origin identity.

## 9. Why full expansion is explicitly rejected

A beta-lens map is itself a finite polynomial. If the nested Chebyshev object were expanded into ordinary powers, the apparent degree would multiply.

At the first-pass settings the naive ordinary-polynomial degrees are approximately:

|case|gate-expanded degree|tension-expanded degree|
|---|---:|---:|
|Z0|14848|8448|
|Z1|8960|8640|
|Z2|14848|8448|
|Z3|10752|6656|
|Z4|16384|7168|
|Z5|24576|14848|
|Z6|29952|19008|

These numbers are **not** the theory order. They are a warning that `expand-all-then-D15` would recreate the exact historical expression-swell problem.

Therefore the finite object must stay in the form

```text
R10 source
 -> beta-lens gate
 -> natural-coordinate factors
 -> nested Chebyshev/Clenshaw factor graph
 -> target-functional moment contraction
```

rather than becoming a 30,000-degree ordinary polynomial.

## 10. Formal integration status

This gate is entirely material-level. All coefficient and audit grids are material-coordinate operations only.

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

No `P`, `Rq`, `L`, `KZ` or new `Pu` was computed in this gate.

## 11. Gate decision

```text
PARAMETER_DERIVED_DOMAINS = RETAINED_PASS
R10_PHYSICAL_OPERATOR = UNCHANGED
R10_MSAC_RC1_HISTORICAL_MULTISCALE_RECONNECTION = PASS_MATERIAL_LEVEL
R10_MSAC_RC1_FULL_2D_SOURCE_FIDELITY = PASS_Z0_Z6
FIRST_PASS_NEXT_LEVEL_CONFIRMATION = PASS_Z0_Z6
MAX_FIRST_PASS_OUTER_ORDER = 1152
MAX_FIRST_PASS_SCALAR_COEFFICIENT_COUNT = 3477
FULL_MONOMIAL_EXPANSION = PROHIBITED
NESTED_FACTOR_GRAPH_REQUIRED = YES
STRUCTURAL_NESTED_GENERAL_D15_ADAPTER = OPEN
NEW_Z0_Z6_Pu = NOT_RUN
```

## 12. Next unique gate

```text
UNIFIED_V1_R10_MSAC_RC1_NESTED_CLENSHAW_QNM_D15_CONTRACTION_GATE
```

The next gate must reconnect the historical `Q_nm` / target-functional moment-first contraction to the RC1 factor graph. It should first prove nested algebra identity and fixed-state exact-moment tractability, then use the same backend for the common `P,Rq,L,KZ` path. No full monomial expansion and no structural spatial numerical integration are allowed.
