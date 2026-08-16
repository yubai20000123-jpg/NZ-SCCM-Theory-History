# NZ-SCCM — R10 global-order historical reconnection and intrinsic-scale execution report

**Timestamp:** 2026-08-16 13:55 +08:00  
**Result:** `PASS_DIAGNOSTIC / N3584 DEMOTED FROM NEXT-PRODUCTION BASIS / NO Pu RUN`

## 1. Question executed

The execution asks whether the current `N=3584` result is an unavoidable expression of R10 material complexity or a consequence of forcing a multiscale low-parameter material law into one wide single-global lambda-space polynomial.

The calculation deliberately stops before any new Z0-Z6 ultimate-load solve.

## 2. Historical evidence reconnected

The repository history shows the same failure pattern several times:

- R5: high-order factorized material object passed material qualification, while naive nested expansion into D15 suffered expression swell. The accepted remedy was moment-first target-functional contraction.
- M1R/PF1/P2A: compiler grammars failed while the invariant current-map/D15 architecture remained active.
- NC energy-potential gate: low-order global polynomials failed in stress/tangent and the governance explicitly prohibited hidden high-degree/global-coefficient inflation as a rescue.
- R10: the successful simplification was a material-level low-parameter C2 quintic energy smoothing, then reinsertion into the same multidimensional operator.

This historical chain means the current task must first diagnose representation coordinates before investing further in a high-order backend.

## 3. Current R10 intrinsic scales

Reference constants:

```text
kappa = 2.0005129533678754
rho   = 0.1
xcr   = 0.04998717945397425
eta   = 0.0024993589726987125
h     = 0.09799750427197301
ur    = 0.03
```

Wide family domains inherited from the 12:29 source screen:

```text
core  = [-2.35,+1.90], width = 4.25
guard = [-2.60,+2.15], width = 4.75
```

Scale ratios:

```text
core_width/eta  = 1700.43601036
guard_width/eta = 1900.48730570
```

Thus the global polynomial sees an interval roughly 1700-1900 times the sign-split scale.

## 4. R10 tensile scalar is locally low-order

In its natural local variables the source tensile scalar is exactly quintic on each active branch.

For `tau=t/xcr`:

```text
u1(tau)=0.1*tau
       +0.37997504271973004*tau^3
       -0.6699625640795952*tau^4
       +0.28798502563183803*tau^5
```

For `s=(t-xcr)/(9*xcr)`:

```text
u2(s)=0.09799750427197301
     -0.6799750427197302*s^3
     +1.0199625640795953*s^4
     -0.4079850256318381*s^5
```

For `t>10*xcr`, `u_R=0.03`.

The joins are C2. The exact third-derivative jumps are approximately:

```text
t=xcr:    -27905.0340327
t=10xcr:  +44.8064770
```

This finite-smoothness structure also slows global spectral convergence, but the strongest current lambda-space derivative pressure is even more localized at the `Pi_eta` sign split.

## 5. Single-global lambda-space primitive convergence

Using the same guard interval, `M=8*(N+1)` material-coordinate coefficient generation and exact C1 zero anchors as the 12:29 screen, independent core audits give:

|N|C value max|C derivative max|T value max|T derivative max|T7 value max|T7 derivative max|
|---:|---:|---:|---:|---:|---:|---:|
|48|8.9853e-2|2.1408|9.0036e-1|28.4998|8.1455e-1|54.5286|
|384|1.0690e-2|1.6915|1.0119e-1|16.0868|8.4776e-2|17.9656|
|768|4.5598e-3|1.2613|4.4668e-2|12.3268|8.8860e-3|3.2222|
|1536|1.4269e-3|0.6711|1.4059e-2|6.6153|6.7592e-4|0.5202|
|2048|7.3610e-4|0.4443|7.2746e-3|4.3866|2.8342e-4|0.2912|
|3072|2.1401e-4|0.2088|2.1294e-3|2.0756|8.3662e-5|0.1281|
|3584|1.1786e-4|0.1377|1.1813e-3|1.3749|5.2678e-5|0.09368|

At N=3584 the dominant derivative-error locations are:

```text
C: lambda ~= -0.00283125
T: lambda ~= +0.00290625
T7: lambda ~= +0.04955
```

The first two coincide with the intrinsic `eta=0.00249936` sign-split scale.

## 6. Direct `Pi_eta` isolation

The exact scalar splitter is

```text
Pi_eta(z)=z^2*(sqrt(z^2+eta^2)+z)/(2*(z^2+eta^2)).
```

When `Pi_eta(lambda)` itself is forced into the same wide single-global polynomial, the maximum derivative errors remain:

|N|t=Pi(lambda)|c=Pi(-lambda)|
|---:|---:|---:|
|48|0.65443|0.65388|
|384|0.58699|0.58747|
|768|0.48696|0.48654|
|1536|0.29796|0.29734|
|2048|0.20413|0.20458|
|3072|0.08984|0.09020|
|3584|0.05858|0.05831|

This isolates the major source of the huge global order: a broad lambda polynomial is spending most of its resolution on the narrow algebraic sign split.

## 7. Natural-coordinate screens

### 7.1 Compression factor `C(c)`

When the same compression law is represented in its own nonnegative compression coordinate `c`, convergence is rapid:

|N|value max|derivative max|derivative error / peak|
|---:|---:|---:|---:|
|4|1.8461e-2|4.8360e-1|24.17%|
|6|2.5418e-3|7.7671e-2|3.8826%|
|10|4.1998e-5|3.4588e-3|0.1729%|
|16|2.0633e-7|5.0633e-5|0.00253%|

### 7.2 Tensile scalar `u_R(t)`

When represented directly in tensile coordinate `t` over the current core-reachable range:

|N|value max|derivative max|derivative error / peak|
|---:|---:|---:|---:|
|48|5.4886e-4|0.57121|19.33%|
|64|2.9834e-4|0.10599|3.5857%|
|96|8.5649e-5|0.08116|2.7457%|
|192|1.1510e-5|0.00902|0.3053%|

The source therefore does not intrinsically require thousands of degrees once the narrow sign split is not folded into the same wide polynomial coordinate.

## 8. Combined intrinsic-factor material-only screen

A diagnostic factorization was then tested:

```text
Pi_eta(lambda) = exact source formula
C(c)            = Chebyshev in c
u_R(t)          = Chebyshev in t
T               = u_R/rho
T7              = T^7
U               = rebuilt from the same factors
```

The 2D spectral current operator and its consistent derivative chain were then assembled exactly as in the source audit.

The tested pair

```text
N_C = 6
N_u = 64
```

uses only `7+65=72` fitted scalar coefficients and gives:

```text
E_sigma = 0.003337
E_tangent = 0.030469
E_divided_difference = 0.046869
```

All three pass the existing source-material gates.

For comparison, the N3584 four-channel object contains

```text
4*(3584+1)=14340 coefficients.
```

The coefficient-count ratio is approximately `199.17:1`.

This is a **material-only diagnostic**. It is not a production compiler because the exact algebraic `Pi_eta` factor has not yet been passed through a zero-spatial-integration General-D15-compatible adapter.

## 9. Interpretation

The executed evidence supports:

```text
R10 intrinsic material complexity = LOW/MODERATE
single-global lambda-space representation mismatch = CONTROLLING
Pi_eta narrow sign split = PRIMARY GLOBAL-ORDER PRESSURE
C2 tensile joins = SECONDARY GLOBAL-SPECTRAL PRESSURE
N3584 = SOURCE-REPRESENTABILITY WITNESS, NOT DESIRABLE THEORY ORDER
```

This is consistent with the historical R5/G26 lesson: complexity must remain in a small factor graph and be contracted into target moments without manufacturing a huge global intermediate representation.

## 10. Current stop and next gate

No new Pu, `L`, or `KZ` is calculated here.

The new unique next gate is:

```text
UNIFIED_V1_R10_INTRINSIC_SCALE_FACTORIZED_PI_ADAPTER_GATE
```

It must preserve exact R10 physics and determine whether the exact/low-parameter `Pi_eta -> c,t -> C,u_R -> current map` factor graph can be contracted through the existing zero-spatial-integration machinery without returning to a thousands-order global lambda polynomial.
