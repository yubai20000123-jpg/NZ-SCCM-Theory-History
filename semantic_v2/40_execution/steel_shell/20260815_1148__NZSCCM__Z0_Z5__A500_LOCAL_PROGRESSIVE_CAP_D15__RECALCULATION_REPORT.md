# NZ-SCCM Z0–Z5 — a/500 imperfection + local progressive steel-yield recalculation

**Timestamp:** 2026-08-15 11:48 +08:00  
**Identity:** USER-DIRECTED RECALCULATION / ENGINEERING DIAGNOSTIC / ZERO FORMAL SPATIAL QUADRATURE  
**Parent Z6 mechanism execution:** `20260815_1058__NZSCCM__Z6__LOCAL_PROGRESSIVE_RADIAL_CAP_D15__EXECUTION_REPORT.md`

---

## 0. Purpose

The user requested that the two issues exposed by Z6 be applied to Z0–Z5:

1. replace the batch-wide engineering imperfection `q0=1/400` by the source-method-aligned sensitivity `A0=a/500`, expressed in the NZ normalization as `q0=a/(500b)`;
2. replace the whole-shell post-yield radial scaling by the local progressive radial-cap current-map diagnostic used in Z6-C.

This is a recalculation, not a calibration. The Zhou comparator load is never used to select a root or tune a coefficient.

The result identity is deliberately **not** promoted to a new production certification because:

- Chapter 2 and Chapter 6 source evidence confirms the `a/500` FE imperfection convention, but a Chapter-5 Table-5.1 sentence explicitly restating it has still not been directly recovered;
- the local radial cap is a path-independent diagnostic current map, not a full incremental J2 flow-history operator;
- degree 24/32/40 sensitivity is non-negligible for several Z0–Z5 cases, so the degree-32 checkpoints are engineering diagnostics rather than strict same-expression production roots.

---

## 1. Frozen parent theory

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
GENERALIZED_COORDINATES = D,q
KINEMATICS = NGUYEN_SECOND_ORDER
R10 = FROZEN
N48-C1/MM = FROZEN
CAYLEY_HAMILTON = GOVERNING
GENERAL_D15 = GOVERNING
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
STRUCTURAL_CALIBRATION = NO
EXPERIMENTAL/COMPARATOR_LOAD_IN_ROOT_SELECTION = NO
```

The old Z1/Z3/Z4/Z5 same-expression Rq-L certificates remain valid records of the **old** `q0=1/400 + whole-shell-cap` identity. They are not overwritten by the present diagnostic identity.

---

## 2. Initial-imperfection transformation

The new sensitivity uses

\[
A_0=\frac{a}{500},\qquad q_0=\frac{A_0}{b}=\frac{a}{500b}.
\]

|case|old q0|old A0 mm|new q0=a/(500b)|new A0=a/500 mm|
|---|---:|---:|---:|---:|
|Z0|0.0025|15|0.0020|12|
|Z1|0.0025|15|0.0020|12|
|Z2|0.0025|15|0.0020|12|
|Z3|0.0025|15|0.0020|12|
|Z4|0.0025|20|0.0015|12|
|Z5|0.0025|5|0.0030|6|

Thus Z0–Z4 become less imperfect than the old batch assumption; Z5 becomes slightly more imperfect.

---

## 3. Local progressive steel-yield operator

The elastic trial von-Mises invariant defines

\[
r(X,Y,z;D,q)=\frac{[\sigma_{VM}^{E}]^2}{f_y^2}.
\]

The local current-map diagnostic is

\[
\alpha_{loc}(r)=\begin{cases}
1,&r\le1,\\
r^{-1/2},&r>1,
\end{cases}
\]

\[
\boldsymbol\sigma_s^{loc}=\alpha_{loc}(r)\boldsymbol\sigma_s^E.
\]

`alpha_loc` is compiled only in the material coordinate `r`, then composed with the finite continuous Nguyen strain field and contracted by exact D15 moments. The formal structural spatial grid remains zero.

Primary material compiler checkpoint:

```text
r range = [0, 6.25]
degree = 32
material-coordinate nodes = 3001
pre-yield weight = 100
degree checks = 24,32,40
formal structural quadrature = 0
```

---

## 4. First-yield events under a/500

Before local plastic spreading, the source-method-aligned elastic branches first reach steel yield at:

|case|D at first yield|q|Pc MN|Ps MN|P MN|
|---|---:|---:|---:|---:|---:|
|Z0|0.89605090|0.000838604|18.48832|17.16473|35.65305|
|Z1|0.57048758|0.001255424|11.33485|10.85829|22.19314|
|Z2|1.16061454|0.001095301|17.36451|22.22704|39.59155|
|Z3|0.65488028|0.001005892|26.16593|16.97349|43.13942|
|Z4|0.89269223|0.000427479|42.28103|22.84004|65.12107|
|Z5|0.90305468|0.000128406|6.96820|5.78275|12.75095|

Unlike the old global-cap model, first local yield is not automatically declared the ultimate state. Each connected branch is continued with the local cap.

---

## 5. Degree-32 connected-branch first maxima

|case|D|q|Pc MN|Ps MN|Pu,diag MN|old Pu MN|current transferred Zhou comparator MN|new error|
|---|---:|---:|---:|---:|---:|---:|---:|---:|
|Z0|0.9821872|0.000952683|18.05936|18.55997|**36.61933**|34.29760|33.42912|+9.543%|
|Z1|0.6330140|0.001482312|11.26847|11.92199|**23.19047**|20.89869|22.20815|+4.423%|
|Z2|1.2428525|0.001246887|16.54937|23.65870|**40.20807**|37.74634|36.85884|+9.087%|
|Z3|0.7382990|0.001172560|26.36143|18.66136|**45.02278**|42.33906|41.15815|+9.390%|
|Z4|0.9952684|0.000470329|41.94543|24.94141|**66.88685**|62.03715|62.04303|+7.807%|
|Z5|1.0049145|0.000146274|6.90704|6.27053|**13.17757**|12.87876|13.09760|+0.611%|

Old Z0–Z5 MAPE against the transferred Zhou comparator was approximately

\[
2.575\%.
\]

The new degree-32 diagnostic MAPE is approximately

\[
\boxed{6.810\%}.
\]

All six new signed errors are positive.

This is an important result: the previously attractive Z0/Z2/Z3/Z4 agreement depended materially on the old common `b/400` imperfection and whole-shell-cap identity. Applying the source-method-aligned `a/500` sensitivity and local spreading does **not** produce a universal accuracy improvement. Z1 improves materially, Z5 becomes nearly exact, while Z0/Z2/Z3/Z4 become clear overpredictions relative to the presently transferred comparator.

---

## 6. Branch-control notes

### Z2

Near `D≈1.28`, `Rq(D,q)` has multiple roots. A blind secant step can jump to a lower-q branch. The calculation therefore retained continuity from the first connected branch. The peak bracket used was approximately:

```text
D=1.2350   q=0.001225123   P=40.20003 MN
D=1.2475   q=0.001260685   P=40.20595 MN
D=1.2600   q=0.001303251   P=40.16564 MN
```

The localized first maximum is `D≈1.24285`, not a switched lower-q root.

### Z3

Later roots can show a secondary re-rise in load. The governing diagnostic retained the **first connected +->- maximum** near `D≈0.7383`; later branch roots were not substituted merely because they carry large load.

---

## 7. Local-cap material-compiler sensitivity

At each degree-32 peak D, q equilibrium was recomputed with degrees 24, 32 and 40:

|case|P degree24 MN|P degree32 MN|P degree40 MN|24→40 spread MN|
|---|---:|---:|---:|---:|
|Z0|36.76017|36.61933|36.47248|0.28768|
|Z1|23.28770|23.19047|23.08948|0.19822|
|Z2|40.29004|40.20822|40.11935|0.17068|
|Z3|45.30833|45.02278|44.74958|0.55875|
|Z4|67.14541|66.88685|66.63268|0.51272|
|Z5|13.24687|13.17757|13.10958|0.13729|

This sensitivity is larger than the Z6 near-state degree sensitivity previously observed. Therefore:

```text
Z0_Z5_NEW_RESULTS = ENGINEERING_DIAGNOSTIC
LOCAL_CAP_DEGREE32 = PRIMARY_CHECKPOINT
STRICT_NEW_RQ_L_CERTIFICATION = NOT CLAIMED
LOCAL_CAP_COMPILER_CONVERGENCE = OPEN BEFORE PRODUCTION PROMOTION
```

No R10 or N48 concrete change is inferred from this steel-local-cap compiler sensitivity.

---

## 8. Interpretation before Z6-D1

The recalculation changes the evidentiary picture in two ways.

First, `a/500` is not merely a Z6-specific remedy. Its geometry-dependent normalization shifts the other cases materially; using one universal `q0=1/400` had hidden that sensitivity.

Second, because the recalculated Z0–Z4 now tend to exceed the current Zhou comparator, while Z6 remains substantially below it even after the same mechanism corrections, the Z6 discrepancy becomes even less consistent with a single universal material-strength defect. The comparator/topology/slenderness identity must be audited before using Zhou's current reduced empirical values as validation truth.

---

## 9. Persisted companion files

- `semantic_v2/40_execution/steel_shell/20260815_1148__NZSCCM__Z0_Z5__A500_LOCAL_PROGRESSIVE_CAP_D15__PARAMS_AND_INTERMEDIATES.json`
- `semantic_v2/50_results/steel_shell/20260815_1148__NZSCCM__Z0_Z5__A500_LOCAL_PROGRESSIVE_CAP__RESULT.csv`
- this report

A reproduction kernel is persisted separately with the local-cap polynomial/D15 construction and q0 parameterization.
