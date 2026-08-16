# NZ-SCCM — parameter-derived material domain and compiler execution report

**Timestamp:** 2026-08-16 17:20 +08:00  
**Gate:** `UNIFIED_V1_PARAMETER_DERIVED_MATERIAL_DOMAIN_AND_COMPILER_GATE`  
**Result:** `PASS_DOMAIN_RULE / FAIL_SINGLE_GLOBAL_LAMBDA_LOW_COMPLEXITY / NO Pu RUN`

## 1. What was corrected and executed

The preceding project correction restored the intended meaning of a unified workflow:

> the governing calculation rules are common, but numerical boundary/domain values may change as deterministic consequences of specimen geometry, physical boundary, halfwave selection and source material parameters.

This run therefore does **not** impose the old family-wide `[-2.35,+1.90]` interval on every Z specimen. Instead it derives a source/design-side reachable material domain for each specimen using one common rule, and only then applies one common R10 source-fidelity convergence policy.

No new `Pu` is solved in this gate.

## 2. Common mechanics retained

```text
Z0-Z6 boundary = theoretical four-edge SSSS/Navier
AR2 representative geometry: m*=2, ell=b
one continuous complete representative halfwave
Nguyen second-order continuous kinematics
membrane-stress redistribution retained
R10 physical current operator unchanged
current stress + same-map consistent tangent
General-D15 / zero formal spatial-thickness numerical integration
experiment/Zhou/Winter excluded from compiler fitting
```

Formal counters remain:

```text
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
N_formal_thickness_quadrature=0
```

All coefficient generation and fidelity grids used below are material-coordinate operations only.

## 3. Common generalized-coordinate envelope rule

The initial imperfection ratio is

\[
q_0=A_0/b=.004.
\]

The normalized compression search envelope is

\[
0\le D\le2.
\]

`D=2` is a source-side post-peak allowance, not a fitted failure strain. If a connected production branch later reaches this bound before a valid limit point, the same algorithm expands `D_max` by 25% and recompiles; the bound is not adjusted from observed capacity error.

For transverse amplitude, use the same classical postbuckling design-side envelope for every specimen:

\[
k_p=\frac{3(1-\nu^2)}8,
\]

\[
\frac{A_{pb}}{t_c}=
\sqrt{\frac{\max(P_{yth}/P_{cr}-1,0)}{k_p}},
\]

\[
q_{pb}=\frac{t_c}{b}\frac{A_{pb}}{t_c},
\qquad
q_{max}=1.25\max(q_0,q_{pb}).
\]

The factor 1.25 is one project-level envelope guard applied uniformly. `Pcr` and `Pyth` are theoretical scales already available from specimen parameters; they are not experimental calibration values.

This automatically distinguishes the current Z-series regimes:

- Z0-Z5 have `Pcr>Pyth`, hence `q_pb=0` and `q_max=.005`;
- Z6 has `Pyth/Pcr=2.242157`, hence `A_pb/t=1.850225`, `q_pb=.0188106`, and `q_max=.0235133`.

## 4. Analytic continuous material-domain certificate

For the square representative halfwave, the normalized equivalent-uniaxial tensor can be decomposed into:

\[
\mathbf X=\operatorname{diag}(0,-D)+\mathbf X_m+\mathbf X_b.
\]

The membrane physical strain is rank-one positive semidefinite. At `q=q_max`, define

\[
C_m^{max}=\frac{\pi^2}{\varepsilon_0}
\left(q_0q_{max}+\frac12q_{max}^2\right),
\]

\[
C_b^{max}=\frac{\pi^2}{2\varepsilon_0}\frac{t_c}{b}q_{max},
\]

and

\[
A=\frac{C_m^{max}}{1-\nu^2},\quad
B_1=\frac{C_b^{max}}{1-\nu},\quad
B_2=\frac{C_b^{max}}{1+\nu}.
\]

The lower spectral bound follows from the positive-semidefinite membrane part and the bounded bending operator:

\[
\lambda_{min}\ge-D_{max}-B_1.
\]

For the upper bound, the Rayleigh quotient can be reduced to the continuous envelope

\[
A(1-u^2-v^2)+B_1u+B_2v,
\qquad u^2+v^2\le1,\quad u,v\ge0.
\]

Hence

\[
\lambda_{max}\le
A+\frac{B_1^2+B_2^2}{4A}
\]

when the unconstrained stationary point lies inside the disk; otherwise the disk-boundary result is `sqrt(B1^2+B2^2)`.

This domain certificate uses no spatial sampling.

A 5% padding of the certified core width is then added to each side for coefficient generation.

## 5. Resulting specimen-derived domains

| case | q_max | Cm_max | Cb_max | certified core lambda | compiler guard lambda |
|---|---:|---:|---:|---:|---:|
| Z0 | .005000 | .171416 | .268112 | [-2.326966,+.398162] | [-2.463222,+.534419] |
| Z1 | .005000 | .171416 | .202183 | [-2.246565,+.304377] | [-2.374112,+.431924] |
| Z2 | .005000 | .171416 | .268112 | [-2.326966,+.398162] | [-2.463222,+.534419] |
| Z3 | .005000 | .126559 | .197951 | [-2.241404,+.293969] | [-2.368172,+.420738] |
| Z4 | .005000 | .171416 | .316460 | [-2.385927,+.469962] | [-2.528721,+.612756] |
| Z5 | .005000 | .171416 | .804337 | [-2.980899,+1.194486] | [-3.189668,+1.403255] |
| Z6 | .0235133 | 1.954092 | .630420 | [-2.768805,+2.128027] | [-3.013646,+2.372868] |

The values above are generated before checking any previously calculated structural state.

## 6. Post-generation containment check only

After the domains were fixed, the prior diagnostic/engineering envelopes were compared only as a containment audit:

```text
Z0 old diagnostic [-1.07019,+.16276]  -> inside
Z1 old diagnostic [-.75095,+.15841]   -> inside
Z2 old diagnostic [-1.39935,+.26556]  -> inside
Z3 old diagnostic [-.78827,+.12055]   -> inside
Z4 old diagnostic [-1.03594,+.10360]  -> inside
Z5 old diagnostic [-1.03404,+.03614]  -> inside
Z6 old engineering [-2.2937,+1.8232]  -> inside
```

These old states did not generate the domains.

## 7. Same compiler/convergence policy on every derived domain

The baseline screen retains the former source-fidelity rules only as a diagnostic compiler grammar:

```text
channels: U,C,T,T7
single global Chebyshev polynomial per channel
same N for the four channels
M=8*(N+1) material-coordinate projection nodes
C1 anchors at lambda=0
E_sigma <= .005
E_tangent <= .05
E_divided_difference <= .05
```

Order sequence:

```text
48,96,192,384,768,1024,1280,1536,1792,2048,
2304,2560,2816,3072,3328,3584,3840,4096
```

The first passing order is therefore produced by the same rule, not chosen by specimen ID.

## 8. First passing orders and source errors

| case | first N | coefficient count 4(N+1) | E_sigma | E_tangent | E_div |
|---|---:|---:|---:|---:|---:|
| Z0 | 1792 | 7172 | 9.454e-4 | 4.173e-2 | 3.472e-3 |
| Z1 | 1536 | 6148 | 1.064e-3 | 4.453e-2 | 3.946e-3 |
| Z2 | 1792 | 7172 | 9.454e-4 | 4.173e-2 | 3.472e-3 |
| Z3 | 1536 | 6148 | 1.008e-3 | 4.334e-2 | 3.810e-3 |
| Z4 | 1792 | 7172 | 1.301e-3 | 4.851e-2 | 4.669e-3 |
| Z5 | 3072 | 12292 | 1.258e-3 | 4.779e-2 | 4.439e-3 |
| Z6 | 3840 | 15364 | 1.310e-3 | 4.840e-2 | 4.671e-3 |

The full order-by-order convergence history is preserved in the JSON intermediate ledger.

## 9. Interpretation

This gate resolves the previous governance error without hiding the underlying mathematical difficulty.

### What the correction fixes

```text
all specimens no longer carry one identical family-wide interval
boundary/domain values can vary from specimen parameters
orders can differ when the same deterministic convergence rule produces them
```

### What the correction does not fix

Even on the corrected parameter-derived domains, the **single-wide-global lambda polynomial remains a high-order representation**. In particular:

```text
Z5 -> N=3072
Z6 -> N=3840
```

Thus the old family-wide fixed domain was part of the problem, but not the whole problem. The narrow intrinsic R10 transitions still make a one-global-lambda polynomial a poor final theory grammar.

This is consistent with the earlier R5/MSAC history: the project should next restore a common multiscale/source-landmark analytic compiler on the corrected domains rather than reopen the R10 material law or return to a giant coefficient tensor.

## 10. Gate decision

```text
PARAMETER_DERIVED_DOMAIN_RULE = PASS
SAME_RULE_APPLIED_Z0_Z6 = PASS
OLD_FIXED_FAMILY_DOMAIN_AS_PRODUCTION_REQUIREMENT = RETIRED
SINGLE_GLOBAL_LAMBDA_CHEBYSHEV_LOW_COMPLEXITY = FAIL
R10_MATERIAL_PHYSICS = UNCHANGED
NEW_Z0_Z6_Pu = NOT RUN
```

## 11. Next unique gate

```text
UNIFIED_V1_PARAMETER_DERIVED_DOMAIN_PLUS_HISTORICAL_MULTISCALE_COMPILER_RECONNECTION_GATE
```

That gate must begin from the specimen-derived domains above and reconnect the historical R5/MSAC + moment-first strategy. The next candidate compiler must use one source-landmark/intrinsic-scale rule across Z0-Z6, preserve source stress+tangent gates, remain General-D15 compatible, and use no spatial cells/quadrature or case-ID tuning.
