# NZ-SCCM NC family compiler freeze — execution report

**Timestamp:** 2026-08-16 12:29 +08:00  
**Executed gate:** `UNIFIED_PRODUCTION_WORKFLOW_V1_IMPLEMENTATION_AND_NC_FAMILY_COMPILER_FREEZE`

## 1. Result

The material-compiler/source-fidelity part of the gate **passes**.

```text
NC_R10_SOURCE_OPERATOR = UNCHANGED / FROZEN
NC_OPERATIONAL_CORE = [-2.35,+1.90]
NC_COEFFICIENT_GUARD = [-2.60,+2.15]
NC_COMPILER_FIDELITY_THRESHOLDS = FROZEN
NC_FAMILY_ORDER = 3584
NC_SOURCE_FIDELITY_GATE = PASS
```

The high-order Cayley-Hamilton / moment-first General-D15 structural backend has **not yet** been executed at `N=3584`, so no new Z0-Z6 `Pu` is released in this step.

## 2. Why the core/guard distinction is required

The earlier Z6-wide N48 calculation compiled directly on `[-2.35,+1.90]`. That interval is wide enough to contain all current Z0-Z6 envelopes, but a polynomial fitted directly to its endpoints can have large derivative error at the boundaries.

The V1 family compiler therefore distinguishes:

```text
production/audit core  = [-2.35,+1.90]
coefficient guard      = [-2.60,+2.15]
```

The guard remains one material-coordinate interval. It is not a structural cell and does not change

```text
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
```

## 3. Compiler used in this execution

For each frozen R10 channel `U,C,T,T7`, use one global degree-`N` Chebyshev polynomial on the guard interval.

Coefficient generation uses `M=8(N+1)` Gauss-Chebyshev material coordinates and the exact C1 equality constraints at `lambda=0` through the diagonal-normal-matrix + `2x2` Schur correction.

All four channels use the **same candidate order**. No multirate/ad hoc channel order was used in this freeze.

## 4. Source-fidelity gates

The numerical compiler contract is evaluated on the assembled R10 spectral current map, not on structural loads.

```text
E_sigma <= 0.005
E_tan   <= 0.05
E_div   <= 0.05
```

where `E_sigma` is normalized maximum spectral stress error, `E_tan` is normalized maximum spectral-Jacobian error, and `E_div` audits the spectral divided difference required by the consistent tensor tangent.

No experiment, Zhou/Winter value, desired `Pu`, specimen error sign, or Z-series result enters the objective.

## 5. Deterministic order convergence

Candidate sequence:

```text
48, 96, 192, 384, 768,
1024, 1280, 1536, ... with +256 thereafter
```

Reference R10 (`kappa=2.0005129533678754`) audit:

|N|E_sigma|E_tan|decision|
|---:|---:|---:|---|
|48|0.817103|0.954681|FAIL|
|96|0.637393|0.817270|FAIL|
|192|0.291443|0.684920|FAIL|
|384|0.091792|0.535536|FAIL|
|768|0.040464|0.409641|FAIL|
|1024|0.026292|0.333013|FAIL|
|1280|0.018035|0.274678|FAIL|
|1536|0.012512|0.221212|FAIL|
|1792|0.009137|0.173176|FAIL|
|2048|0.006374|0.147591|FAIL|
|2304|0.004807|0.120729|FAIL tangent|
|2560|0.003527|0.102574|FAIL tangent|
|2816|0.002504|0.080082|FAIL tangent|
|3072|0.001837|0.069753|FAIL tangent|
|3328|0.001414|0.055699|FAIL tangent|
|3584|0.001072|0.040665|**PASS**|

At `N=3584`, the divided-difference relative error is approximately

```text
E_div = 0.003814
```

so the rotational/eigenprojector tangent term also passes.

Hence the first passing order on the declared ladder is

\[
\boxed{N_{NC}=3584}.
\]

## 6. NC source-parameter envelope audit

The current Swartz NC records give the R10 `kappa` range

```text
1.9993148515 <= kappa <= 2.0008935611
```

The same `N=3584`, core, guard, algorithm and thresholds were checked at both extremes and the reference value:

|kappa|E_sigma|E_tan|max|a_n||
|---:|---:|---:|---:|
|1.9993148515|0.0010695|0.0406008|0.511589|
|2.0005129533678754|0.0010722|0.0406652|0.511651|
|2.0008935611|0.0010730|0.0406856|0.511671|

No coefficient blow-up occurs; the maximum sum of absolute coefficients is about `2.082`.

## 7. Reference C1 / coefficient diagnostics

At the reference `kappa`, numerical residuals are at roundoff / low `10^-12` level:

```text
U(0)  = 5.55e-16
U'(0) = 2.00051295336788
C(0)  = 6.38e-16
C'(0) = 1.82e-13
T(0)  = 1.94e-16
T'(0) = 1.82e-12
T7(0) = 4.44e-16
T7'(0)= -1.35e-14
```

Reference little-endian float64 coefficient hashes:

```text
U  4a04909f645d74e25ea66d848c95a9eae647724cea78be41058ab742e70be063
C  f6979a8591db6e165eac1f1fd9d797ddbe39d34a486ec88c7e2cc8eaf25689af
T  54a305629bca62dcc47f0fab3484f9d5aa7b61d310812e60dc8c66dc931da1a7
T7 143ff63f0fd7c5f34e18f36128ec2a12b08b092a38cce40d7099321c412cd3c1
```

The hashes are reproducibility diagnostics, not physics gates.

## 8. What is now uniform and what is parameterized

The frozen NC **compiler protocol** is common to every NC specimen:

```text
same R10 source family
same core/guard policy
same Chebyshev+C1 algorithm
same fidelity metrics
same order-selection algorithm
same frozen family order N=3584
same matrix-lift / D15 / P,Rq,L backend
```

The actual coefficients may depend on the source material parameter `kappa` (and therefore on the physical NC input), exactly as the source current operator does. This is not a specimen-specific method change. If a future NC material parameter exits the audited family envelope, it triggers a family-level compiler audit rather than a case-by-case order change.

## 9. Structural zero-integration status

Nothing in this execution changes the structural integration identity:

```text
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
N_formal_thickness_quadrature=0
```

Material-coordinate coefficient/audit nodes are not spatial material points.

## 10. Gate decision / next step

```text
UNIFIED_V1_COMMON_MECHANICS = RETAINED
NC_FAMILY_SOURCE_COMPILER_FREEZE = PASS
NC_FAMILY_ORDER = 3584
HIGH_ORDER_CH_D15_BACKEND = NOT_YET_EXECUTED
NEW_Z0_Z6_Pu = NOT_CALCULATED
```

Unique next gate:

`UNIFIED_V1_N3584_CH_MOMENT_FIRST_D15_BACKEND_AND_Z0_Z6_RERUN_GATE`

This next gate must implement the order-agnostic/factorized Cayley-Hamilton recurrence into moment-first General-D15 without naive full stress-field expansion, verify computational tractability, then rerun Z0-Z6 through exactly the same NC family compiler/root/tangent workflow.
