# Zhou Z0-Z6 raw FE point recovery and H0 comparison audit

**Timestamp:** 2026-08-15 14:07 +08:00  
**Status:** SOURCE SEMANTICS CORRECTED / RAW FE NUMERIC MAPPING OPEN / NO MODEL RETUNE

## 0. Audit question

After the H0 homogenized-web-steel activation, Z0-Z5 same-D `Rq=0` diagnostic states lie mostly above the previously replayed Zhou curve. This audit asks whether that means NZ-SCCM is above Zhou finite-element predictions, or whether the comparator is a conservative design lower envelope.

The second interpretation is supported by the source chain.

---

## 1. Source identity

Zhou's dissertation Chapter 5 explicitly separates:

- §5.3.2: four-edge axial elastoplastic numerical analysis;
- §5.3.4: four-edge axial stability curve based on numerical simulation;
- §5.3.5: four-edge axial stability curve based on theoretical derivation.

The figure list identifies Figure 5.8 as `四边简支钢管束拟合轴压稳定曲线`.

The associated 2021 Thin-Walled Structures article (`10.1016/j.tws.2021.107966`) states in its abstract that the design curve was established from numerous FE models using `w0=a/500` and is capable of **conservatively predicting** ultimate axial resistance.

Accordingly:

```text
ZHOU_EQ_5_87_5_88 = FE-INFORMED CONSERVATIVE DESIGN / LOWER-ENVELOPE REFERENCE
ZHOU_EQ_5_87_5_88 != INDIVIDUAL RAW FE RESULT
```

This is a comparator-semantic correction, not a recalculation of Zhou's formulas.

---

## 2. What remains numerically valid from the 12:33 replay

All existing full-section quantities remain valid:

- original `Ac`, `As`, `Pyth`;
- `Dx`, `Dy`, `Dxy`, `Dmu`, `H`;
- integer-halfwave minimum and `Pcr`;
- `lambda_n`;
- Eqs. (5-87)-(5-88) curve value.

Only the active interpretation changes. The value previously named `Pu_Zhou_original` is now called

\[
\boxed{P_{Zhou,lower}=\phi_{lower}P_{yth}}.
\]

It is a design lower reference, not FE truth.

---

## 3. H0 comparison after semantic correction

H0 exactly restores the original full-section material bookkeeping, so for all Z0-Z6

\[
P_{yth,H0}=P_{yth,Zhou,full}.
\]

For Z0-Z5 the current H0 values below are **same-D re-equilibrated branch-location diagnostics**, not final `Rq=0,L=0` ultimate loads.

|case|Pyth MN|Zhou lower φ|Zhou lower P MN|H0 diagnostic P MN|H0 φ|margin above lower curve|
|---|---:|---:|---:|---:|---:|---:|
|Z0|44.044944|0.838815|36.945541|40.952338|0.929785|+10.845%|
|Z1|30.319584|0.782380|23.721432|24.877713|0.820516|+4.874%|
|Z2|50.622144|0.814137|41.213379|44.936813|0.887691|+9.035%|
|Z3|54.948816|0.806574|44.320271|49.496423|0.900773|+11.679%|
|Z4|79.386112|0.884125|70.187272|77.297084|0.973685|+10.130%|
|Z5|14.681648|1.000000|14.681648|14.963289|1.019183|+1.918%|

Therefore the previous statement that Z0-Z4 are "too strong by roughly 5-12%" is not supported. The source-consistent statement is:

> Z0-Z5 H0 branch diagnostics are roughly 2-12% above Zhou's conservative FE-informed design reference; their error relative to Zhou's individual FE simulations is presently unknown.

For Z6, the only admissible H0 comparison remains the old fixed state:

```text
D = 0.705
q = 0.0058975999
Pfixed,H0 = 44.506184 MN
Zhou lower-envelope design P = 49.672436 MN
margin = -10.401%
```

This Z6 point is neither a new H0 equilibrium state nor a final Pu. The current N48-domain blocking gate remains valid.

---

## 4. Raw FE recovery attempt

### 4.1 Dissertation

The uploaded dissertation was searched around Chapter 5, §5.3.2-§5.3.5, Table 5.1, and Figure 5.8.

Recovered:

- the parameter-design structure and source parameter ranges;
- the existence and identity of Figure 5.8;
- the separate numerical-analysis and fitted-design-curve roles.

Not recovered:

- a table listing each nonlinear FE model's full input tuple and ultimate axial resistance;
- a direct source case ID corresponding one-to-one with project labels Z0-Z6.

Table 5.1 is a **parameter design table**, not a model-by-model FE output table.

### 4.2 Public article / data search

The primary journal article page confirms the refined FE model, parametric study, numerous FE models, `w0=a/500`, and conservative design-curve role. ResearchGate exposes metadata/abstract but not the full article. Searches for a supplementary/public model-by-model dataset did not locate one.

Therefore:

```text
ZHOU_RAW_FE_Z0_Z6_NUMERIC_VALUES = NOT RECOVERED
PUBLIC_SUPPLEMENTARY_DATASET = NOT FOUND
```

This is not permission to manufacture values from the design curve.

---

## 5. Why Figure 5.8 cannot yet be blindly digitized into Z0-Z6

Z0-Z6 are project representative parameter combinations assembled from Zhou's parameter space. They are not known literal source specimen/model IDs.

Figure 5.8 is a stability-plane point cloud. A point at approximately the same `lambda_n` does not uniquely identify the full tuple

\[
(n_s,l_s,h,t_s,f_y,f_{cu},a,b).
\]

Therefore nearest-point visual assignment is forbidden.

Digitization becomes admissible only when the source figure legend/series or another source record provides a unique parameter mapping. Any such value must be labeled

```text
DIGITIZED_FROM_SOURCE_FIGURE
```

and must not be represented as a tabulated source value.

---

## 6. Current interpretation of H0

The evidence now supports three statements simultaneously:

1. `rho_w=ts/ls` H0 material bookkeeping is geometrically exact and zero-discretization compatible.
2. H0 has **not** been shown to overpredict Zhou FE merely because Z0-Z5 exceed the design curve.
3. H0 has **not** yet been validated against Zhou FE either, because raw case-matched FE values remain unavailable.

Thus:

```text
H0_MECHANICAL_FEASIBILITY = PASS
H0_SECTION_MATERIAL_CONSERVATION = PASS
H0_ZERO_STRUCTURAL_DISCRETIZATION = PASS
H0_OVERPREDICTION_AGAINST_ZHOU_FE = NOT ESTABLISHED
H0_VALIDATION_AGAINST_ZHOU_FE = OPEN
H0_PRODUCTION_PROMOTION = NO
```

No web-steel reduction coefficient is introduced.

---

## 7. Effect on task ordering

The Z6 material-domain preflight remains a genuine mathematical gate, but comparator-truth recovery is now logically prior for validation. Before spending effort widening the same R10/N48 material compilation for the H0 Z6 branch, the project should first seek source-identifiable raw FE points or a legitimate Figure-5.8 series mapping.

```text
CURRENT_NEXT_TASK = ZHOU_FOUR_EDGE_RAW_FE_PRIMARY_DATA_OR_FIG5_8_POINT_MAPPING_RECOVERY
```

If raw FE values are recovered, perform the three-way comparison:

\[
P_{Zhou,lower}\quad\leftrightarrow\quad P_{NZ-H0}\quad\leftrightarrow\quad P_{Zhou,FE}.
\]

Only after that comparison should H0 be retained, rejected, or further audited. No R10/N48/steel/web-fraction parameter may be tuned to Zhou's lower envelope.
