# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-22 12:05 +08:00  
**Status:** `MARGUERRE_AIRY_EXPLICIT / EXPLICIT_1D_TO_2D_MATERIAL_JUDGMENT / MATERIAL_REORGANIZATION_7GATE_PARTIAL / USER_ACCEPTANCE_PENDING`

## 0. Current mainline

The current structural backbone is the finite explicit Marguerre–Airy formulation:

\[
P_{pb}(q)=P_{cr}\frac{q}{q+q_0}+Cq(q+2q_0),
\]

\[
n(s;q)=\frac{P_{pb}(q)}b+Gq(q+2q_0)(1-2s^2),
\qquad
m(s;q)=Jqs,
\]

with the Airy transverse membrane resultant

\[
N_x=-\frac{\alpha^2b^2\Delta_A}{8A_{22}}q(q+2q_0)\cos(2\beta y),
\qquad N_{xy}=0.
\]

Canonical structural theory:

`semantic_v2/20_theory/20260821_1733__NZSCCM__MARGUERRE_AIRY_EXPLICIT_LIMIT_THEORY_V1.md`

Latest acceptance package:

`semantic_v2/40_execution/20260822_0745__NZSCCM__EXPLICIT_1D_2D_ASSESSMENT_RC_Z0Z6_SUHPC.md`

The current interpretation is deliberately narrow:

\[
\boxed{
\text{1D explicit structural/capacity root}
\to
\text{Airy 2D membrane demand}
\to
\text{finite 2D material-capacity judgment}
}
\]

Materials are judgment/capacity objects inside the explicit path, not a second structural solver.

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_material_points = 0
RITZ_ORDER = NONE
LOAD_PATH_TRACKING = 0
HISTORY_STATE_MACHINE = OFF_MAINLINE
HARD_ENVELOPE_HISTORY_OVERLAY = OFF_MAINLINE_DIAGNOSTIC
EXPERIMENT_IN_ROOT_SELECTION = 0
FEM_IN_ROOT_SELECTION = 0
CURRENT_ASSESSMENT = EXPLICIT_1D_TO_2D_MATERIAL_JUDGMENT
USER_ACCEPTANCE = PENDING
```

## 1. Off-mainline diagnostic branches

The following 2026-08-22 branches are retained only as diagnostics/provenance and are not part of the current explicit acceptance path:

- `semantic_v2/40_execution/20260822_0015__NZSCCM__STRICT_HARD_ADMISSIBILITY_CASE1_CASE2_Z6_AUDIT.md`
- `semantic_v2/40_execution/20260822_0105__NZSCCM__NGUYEN_POST_ENVELOPE_CONTINUATION_CASE1_CASE2_Z6_AUDIT.md`

They must not introduce material points, moving history fronts, post-envelope state machines, or extra runtime hard caps into the current calculation package.

## 2. Selected Swartz RC — current acceptance table

Correct reinforcement source interpretation:

\[
\rho_x=\rho_y=p_{table}.
\]

The current 2D RC judgment uses the already-derived finite TC capacity criterion with the common project ordinary-concrete input \(f_t=0.10f_c\). Because Swartz did not report specimen-specific tensile strength, Case1/2 2D values are working common-material predictions, not specimen-specific tensile calibration.

|Case|1D Pu kN|2D Pu kN|Pf kN|1D error|2D error|
|---:|---:|---:|---:|---:|---:|
|1|567.712|495.989|490.194|+15.814%|+1.182%|
|2|561.638|501.025|506.652|+10.853%|−1.111%|
|9|515.424|515.424|625.865|−17.646%|−17.646%|
|10|534.711|534.711|696.147|−23.190%|−23.190%|
|19|339.177|339.177|377.654|−10.188%|−10.188%|
|20|335.013|335.013|372.761|−10.127%|−10.127%|
|21|350.460|350.460|368.313|−4.847%|−4.847%|
|22|351.679|351.679|355.858|−1.174%|−1.174%|

Interpretation remains for user acceptance: the 2D judgment selectively re-cuts Case1/2 and leaves the other selected 1D biases visible.

## 3. Z0–Z6 — current explicit 1D/2D comparison

The values below are freshly regenerated with the current 2026-08-21 Marguerre–Airy explicit formulation. They supersede use of the older AR2 `31.99/20.02/...` numbers as the current 1D column.

|Case|1D Pu MN|2D Pu MN|Zhou MN|Winter MN|ordering|
|---|---:|---:|---:|---:|---|
|Z0|37.8257|37.8257|36.9455|41.5008|Zhou < 2D < Winter|
|Z1|24.7141|24.7141|23.7214|26.1001|Zhou < 2D < Winter|
|Z2|42.9590|42.9590|41.2134|45.7333|Zhou < 2D < Winter|
|Z3|46.4949|46.4949|44.3203|49.0469|Zhou < 2D < Winter|
|Z4|70.2657|70.2657|69.3399|79.3861|Zhou < 2D < Winter|
|Z5|14.1182|14.1182|14.6816|14.6816|2D < Zhou = Winter|
|Z6|56.3794|51.3450|49.4868|50.1859|Zhou < Winter < 2D|

Z6 is the only current Z case whose explicit 2D judgment materially changes the 1D root:

\[
56.3794\to51.3450\ \mathrm{MN},
\]

or \(-8.9295\%\). It remains `+2.310%` above Winter and is not adjusted to enter the Zhou–Winter bracket.

## 4. Steel-shell UHPC — corrected geometry acceptance table

T120/T360 retain the current web-corrected geometry/results.

For BH005–BH050, the current geometry rebase uses the 37-mm net web height indicated by the Codex geometry audit:

\[
A_{w,total}=9\times4\times37=1332\ \mathrm{mm^2},
\qquad
\rho_w=1332/(42B).
\]

Fresh corrected-geometry 1D explicit values and finite 2D precheck:

|Case|1D Pu MN|2D Pu MN|Abaqus MN|2D status|
|---|---:|---:|---:|---|
|T120|12.3480|12.3480|12.6378|PASS / unchanged|
|T360|11.2978|11.2978|10.9688|PASS / unchanged|
|BH005|2.41999|2.41999|2.3558|PASS / unchanged|
|BH010|4.45287|4.45287|4.3043|PASS / unchanged|
|BH020|8.17466|8.17466|8.0076|PASS / unchanged|
|BH032|11.14350|11.14350|10.9905|PASS / unchanged|
|BH050|13.61827|TRIGGERED / unique Pu OPEN|12.2198*|UHPC transverse-tension criterion active|

Current UHPC tensile judgment anchor:

\[
f_{t,cr}=9.7677\ \mathrm{MPa}.
\]

Approximate maximum transverse UHPC tensile stresses at the 1D candidates:

- T120: 8.06 MPa;
- T360: 7.27 MPa;
- BH005: −0.52 MPa;
- BH010: 1.26 MPa;
- BH020: 4.62 MPa;
- BH032: 7.34 MPa;
- BH050: 11.69 MPa.

Thus BH050 is the only current corrected-geometry SUHPC case whose 1D candidate is rejected by the finite 2D tensile judgment. The stripped explicit path does not yet contain a unique finite UHPC TC re-cut formula, so no replacement Pu is invented.

`*` BH050 Abaqus comparator belongs to a different diagnostic model family and has lower validation confidence.

## 5. Decision state before material reorganization

No theory expansion is authorized by the result tables above. They remain retained as the pre-reorganization acceptance baseline and are not silently overwritten by the material-source work below.

```text
SELECTED_RC_1D_2D_TABLE = EXECUTED
Z0_Z6_1D_2D_ZHOU_WINTER_TABLE = EXECUTED
SUHPC_37MM_1D_2D_ABAQUS_TABLE = EXECUTED
HISTORY_DETOUR = EXCLUDED_FROM_CURRENT_MAINLINE
USER_ACCEPTANCE = PENDING
```

## 6. 2026-08-22 11:51–12:05 — NC/UHPC seven-gate material reorganization checkpoint

Material-only reports:

- `semantic_v2/20_theory/20260822_1151__NZSCCM__NC_UHPC_7GATE_EXPLICIT_MATERIAL_REORGANIZATION_V1.md`
- `semantic_v2/20_theory/20260822_1205__NZSCCM__NC_TC_APPENDIXB_SOURCE_CORRECTION_ADDENDUM.md`

These reports preserve the structural backbone and recover finite source-level 2D capacity objects without material points or loading-history state machines.

### NC

Nguyen/Foster–Kupfer source recovery establishes:

- CC: Nguyen Eq. (3.17) gives a finite rational ray gate and passes G6.
- TC/CT major tensile peak: Nguyen Eqs. (3.18)–(3.19) reduce to two straight finite branches meeting at `(p/fc,t/ft)=(0.8,0.6)`.
- Direct Appendix-B audit shows the same TC route also computes a separate minor-compressive peak branch:

\[
\sigma_{2p}
=
\begin{cases}
\dfrac{1-3.28\alpha}{(1-\alpha)^2}f_c,&\alpha>-0.2,\\[2mm]
0.5375f_c,&\alpha\le-0.2.
\end{cases}
\]

This extra branch is itself finite/G6-compatible, but the combined physical admissibility meaning of the two directional peak quantities must be source-audited before declaring the complete TC peak-pair capacity gate closed.

The old project `c*=c(1-tau)` and low-parameter CC interaction remain demoted from source identity and retained only as historical project reductions.

```text
NC_CC_SOURCE_CAPACITY_GATE = PASS
NC_TC_EQ318_319_TENSILE_PEAK_GATE = PASS_G6
NC_TC_APPENDIXB_COMPRESSIVE_PEAK_BRANCH = RECOVERED_G6
NC_TC_COMPLETE_PEAK_PAIR_CAPACITY_INTERPRETATION = SOURCE_AUDIT_PENDING
NC_FULL_INCREMENTAL_NGUYEN = ORACLE_ONLY
```

### UHPC

Liu 2024 full biaxial source was recovered far enough to establish:

- CC final proposed piecewise ellipse/parabola Eq. (4): finite G6 ray reduction exists;
- TT conservative capacity: biaxial tensile capacity taken as uniaxial tensile strength;
- TC/CT conservative sequential-loading piecewise capacity: finite direct re-cut exists;
- Hiew remains the tensile-backbone source; Diab/Ferche current-strain TC softening remains a G6-compatible component candidate.

A source-level CC issue remains before full lock:

- Table 5 fitted ellipse coefficient: `c=1.33`;
- final Eq. (4) machine-readable ellipse coefficient: `1.49`;
- literal Eq. (4) ellipse/parabola pieces do not meet continuously at the stated `f1/f2=0.5` transition (about 9.12% difference in normalized major compression capacity).

No coefficient is altered to hide this source issue, and no structural comparator is used to resolve it.

```text
MATERIAL_REORGANIZATION_7GATE = EXECUTED_PARTIAL
STRUCTURAL_BACKBONE_CHANGED = FALSE
NC_CC_SOURCE_FINITE_GATE = PASS
NC_TC_SOURCE_FINITE_COMPONENTS = PASS_G6
NC_TC_COMPLETE_CAPACITY_INTERPRETATION = OPEN
UHPC_CC_SOURCE_FORM = RECOVERED
UHPC_CC_G6_FINITE_REDUCTION = PASS
UHPC_CC_INTERNAL_JOIN_C0 = PENDING_SOURCE_RECONCILIATION
UHPC_TC_CT_CAPACITY_GATE = PASS_G6
UHPC_TT_CAPACITY_GATE = PASS_G6
UHPC_COMPRESSION_BACKBONE_FINAL_SELECTION = OPEN
UHPC_FULL_7GATE = NOT_YET_LOCKED
STRUCTURAL_PU_RERUN = NOT_AUTHORIZED
```

The next allowed action is material-only: (1) reconcile the Nguyen Appendix-B TC peak-pair interpretation, (2) reconcile the Liu 2024 CC source join, and (3) freeze one UHPC uniaxial compression backbone. Structural Pu tables stay frozen until the resulting material certificate passes.
