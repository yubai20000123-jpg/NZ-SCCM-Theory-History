# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-22  
**Status:** `MARGUERRE_AIRY_EXPLICIT / POST_7GATE_STRUCTURAL_RERUN_EXECUTED_PARTIAL / SUHPC_2D_UPDATED / Z0_Z6_FINAL_POSTCRACK_2D_PU_OPEN / USER_ACCEPTANCE_PENDING`

## 0. Governing structural mainline

The governing structural theory remains:

`semantic_v2/20_theory/20260821_1733__NZSCCM__MARGUERRE_AIRY_EXPLICIT_LIMIT_THEORY_V1.md`

Current post-seven-gate structural execution:

`semantic_v2/40_execution/20260822_1315__NZSCCM__POST_7GATE_STRUCTURAL_RERUN_SUHPC_AND_Z_NC_TC_SOURCE_ROLE_AUDIT.md`

Current result summary:

`current/results/NZ_SCCM_POST_7GATE_STRUCTURAL_RERUN_CURRENT_20260822.md`

Z0–Z6 finite source-transition reproduction:

`semantic_v2/40_execution/steel_shell/20260822_1315__NZSCCM__Z0_Z6_NC_TC_SOURCE_TRANSITION_REPRO.py`

The governing sequence remains

\[
\boxed{
\text{1D explicit structural/capacity root}
\to
\text{Airy 2D membrane demand}
\to
\text{finite 2D material-capacity / transition judgment}
}
\]

and not a second material-point/history solver.

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
STRUCTURAL_BACKBONE_CHANGED = FALSE
STRUCTURAL_PU_RERUN = EXECUTED_PARTIAL
USER_ACCEPTANCE = PENDING
```

---

## 1. Current material source-of-truth chain

1. `semantic_v2/20_theory/20260822_1151__NZSCCM__NC_UHPC_7GATE_EXPLICIT_MATERIAL_REORGANIZATION_V1.md`
2. `semantic_v2/20_theory/20260822_1205__NZSCCM__NC_TC_APPENDIXB_SOURCE_CORRECTION_ADDENDUM.md`
3. `semantic_v2/20_theory/20260822_1240__NZSCCM__UHPC_ZHANG_BACKBONE_AND_LIU_CC_CONTINUOUS_SOURCE_MIN_GATE.md`
4. `semantic_v2/20_theory/20260822_1255__NZSCCM__NC_TC_FAILURE_ENVELOPE_VS_APPENDIXB_CONSTITUTIVE_PEAK_RESOLUTION.md`
5. `semantic_v2/20_theory/20260822_1315__NZSCCM__NC_UHPC_7GATE_MATERIAL_CERTIFICATE_V1.md`
6. `semantic_v2/20_theory/20260822_1320__NZSCCM__NC_CC_EQ317_PRINTED_TYPO_VS_FIG32_APPENDIXB_RESOLUTION.md`

```text
MATERIAL_FORM_7GATE_CERTIFICATE = PASS_WITH_DECLARED_SOURCE_KINKS_AND_PARAMETER_CAVEATS
NC_MATERIAL_FORM_7GATE = PASS
UHPC_MATERIAL_FORM_7GATE = PASS_WITH_DECLARED_FINITE_CC_CAPACITY_CUSP
```

Important distinction introduced by the structural rerun:

```text
NC_TC_SOURCE_FORM_G6 = PASS
NC_TC_SOURCE_ROLE = CRACKING / STATE-TRANSITION BOUNDARY
NC_TC_AS_STEEL_SHELL_FINAL_ULTIMATE_CLOSURE = OPEN
```

A source-closed finite transition boundary is not automatically a source-closed final post-crack ultimate law.

---

## 2. Normal concrete (NC)

### 2.1 Current axis backbones and parameter identity

```text
NC_COMPRESSION_BACKBONE = SAENZ_RETAINED_FOR_SWARTZ_RANGE
NC_TENSION_BACKBONE = T5_FOSTER_PROJECT_REDUCTION_RETAINED
NC_SWARTZ_COMPRESSION_STRENGTH = 0.85_FCYL_SOURCE_IN_SITU_PANEL_STRENGTH
NC_SWARTZ_SPECIMEN_FT = SOURCE_OPEN
```

For Swartz, panel-specific companion-cylinder `fcyl` and `eps0` remain measured anchors; `ft=0.10fc` remains a transparent project assumption when required because specimen-specific tensile strength was not reported.

### 2.2 NC CC

Accepted source form:

\[
K_{CC}^{NC}(a)=\frac{1+3.65a}{(1+a)^2},\qquad a=p_m/p_M.
\]

The printed Nguyen Eq. (3.17) denominator `1+alpha^2` remains recorded as a thesis typesetting inconsistency; Figure 3.2 and Appendix-B consistently use `(1+alpha)^2`, which is the accepted source implementation.

### 2.3 NC TC/CT

Current source failure/state-transition envelope:

\[
\frac{p}{f_c}+\frac{t}{3f_t}=1
\]

and

\[
\frac{p}{2f_c}+\frac{t}{f_t}=1,
\]

joining at

\[
(p/f_c,t/f_t)=(0.8,0.6).
\]

Nguyen source-role audit establishes that breaching this envelope changes the concrete state and causes cracking. The Appendix-B extra `sig2p` and post-crack modified-compression-field response remain constitutive-oracle material, not a second runtime history solver.

---

## 3. Selected Swartz RC current numerical status

The post-seven-gate run did not identify a new specimen-specific `ft`, so the previously executed selected-set TC results remain **working diagnostics**, not newly specimen-source-closed values:

|Case|1D / kN|2D working / kN|Pf / kN|
|---:|---:|---:|---:|
|1|567.712|495.989|490.194|
|2|561.638|501.025|506.652|
|9|515.424|515.424|625.865|
|10|534.711|534.711|696.147|
|19|339.177|339.177|377.654|
|20|335.013|335.013|372.761|
|21|350.460|350.460|368.313|
|22|351.679|351.679|355.858|

```text
RC_SELECTED_NUMERICAL_STATUS = RETAINED_WORKING_DIAGNOSTIC
RC_SWARTZ_SPECIMEN_FT_SOURCE = OPEN
```

---

## 4. UHPC current production working material identity

```text
UHPC_COMPRESSION_BACKBONE = ZHANG_2023
HU_WENXU = HISTORICAL_UNIAXIAL_COMPARATOR_ONLY
UHPC_TENSION_BACKBONE = HIEW_2024
UHPC_CC_CAPACITY = LIU2024_SOURCE_MIN_PROJECT_REDUCTION
UHPC_TC_CT_CAPACITY = LIU2024_SEQUENTIAL_CONSERVATIVE_ENVELOPE
UHPC_TT_CAPACITY = LIU2024_UNIAXIAL_TENSILE_CAP
```

Current material-level values remain

\[
f_c=141.1\ \mathrm{MPa},\quad E_c=43.4\ \mathrm{GPa},\quad
\varepsilon_{c0}=0.0035,\quad \nu=0.20,\quad V_f=2\%.
\]

Only `fc=141.1 MPa` is user-immutable; other retained values remain material-source choices rather than structural-load fits.

---

## 5. SUHPC post-seven-gate structural results

| Case | Zhang 1D / MN | Current 2D / MN | status |
|---|---:|---:|---|
|T120|12.41101|**12.22252**|Liu TC active / finite re-cut|
|T360|11.36533|**11.36533**|2D gate inactive|
|BH005|2.42351|**2.42351**|2D gate inactive|
|BH010|4.46632|**4.46632**|2D gate inactive|
|BH020|8.21925|**8.21925**|2D gate inactive|
|BH032|11.21046|**11.21046**|2D gate inactive|
|BH050|13.67770|**12.77154**|Liu TC active / finite re-cut|

The former BH050 status `TRIGGERED / unique Pu OPEN` is closed under the current Liu finite-capacity architecture.

```text
SUHPC_POST_7GATE_RERUN = EXECUTED
SUHPC_CURRENT_2D_TABLE = RESOLVED
BH050_CURRENT_2D_PU = 12.77154 MN
```

The old `current/results/NZ_SCCM_STEEL_SHELL_UHPC_T120_T360_BH005_BH050_CURRENT_SUMMARY_20260821.md` has been explicitly marked superseded and now points here.

---

## 6. Z0–Z6 NC source-transition execution

The old material-reorganization-preceding Z table had 1D roots:

|Case|1D Pu / MN|
|---|---:|
|Z0|37.82571|
|Z1|24.71413|
|Z2|42.95901|
|Z3|46.49489|
|Z4|70.26572|
|Z5|14.11819|
|Z6|56.37942|

The old Z6 2D value `51.3450217892 MN` used the historical project TC reduction `c*=c(1-tau)`. That reduction is no longer the current NC source identity, and the old Z6 concrete state violates the newly frozen Nguyen TC source envelope. Therefore:

```text
OLD_Z6_51_345 = SUPERSEDED_BY_CURRENT_NC_SOURCE_ROLE
```

### 6.1 Finite compatible s=0 TC transition roots

Using bonded physical strains, Saenz/T5 NC axis maps, plane-stress steel radial cap, web y-clip, Airy `Nx`, and the Nguyen source TC equality gives:

|Case|q_TC|P_TC-transition / MN|segment|p/fc|t/ft|
|---|---:|---:|---|---:|---:|
|Z0|0.002007624998|27.033151885|B|0.7587838|0.6206081|
|Z1|0.002653115864|17.093528920|B|0.6150531|0.6924735|
|Z2|0.002007624998|27.033151885|B|0.7587838|0.6206081|
|Z3|0.003023358231|36.744639968|B|0.7285937|0.6357031|
|Z4|0.001755102366|56.203522296|A|0.8269272|0.5192183|
|Z5|0.000194052923|10.747333454|A|0.8492317|0.4523048|
|Z6|0.004014855283|23.832330467|B|0.4061203|0.7969399|

These values are source transition/cracking loads, **not final post-crack Pu**.

If the Nguyen TC transition envelope is incorrectly treated as a terminal steel-shell ultimate hard cap, all Z cases collapse 20–58% below their 1D roots. The source itself does not justify this terminal interpretation: after envelope breach it enters a cracked constitutive continuation.

Therefore:

```text
Z0_Z6_NC_TC_TRANSITION = SOLVED
TC_FULL_FAILURE_ENVELOPE_AS_SC_ULTIMATE_HARD_CAP = REJECTED
Z0_Z6_FINAL_POSTCRACK_2D_PU = OPEN
```

A later Z6 A-segment mathematical intersection near `48.63 MN` is diagnostic only and must not be promoted because reaching it requires continuation beyond the earlier cracking transition. Comparator proximity is not a root-selection rule.

---

## 7. Current stop/go decision

### Closed

- material-form seven-gate certificate;
- NC CC and TC/CT source envelopes as finite source boundaries;
- UHPC Zhang compression / Hiew tension / Liu finite capacity architecture;
- SUHPC post-seven-gate structural rerun, including finite T120 and BH050 re-cuts;
- Z0–Z6 finite NC-TC transition equations and source-role diagnosis.

### Open

\[
\boxed{\text{Z0--Z6 final post-crack 2D ultimate capacity}}
\]

because the source-required post-TC-transition continuation has not yet been reduced to a monotonic, history-free, finite G6-compatible operator.

### Next task

Extract from the Nguyen post-crack TC continuation a source-grounded reduced operator that:

1. connects continuously at the TC transition boundary;
2. represents post-crack compression softening / tensile bridging sufficiently for ultimate capacity;
3. remains finite and directly integrable/solvable with zero formal spatial quadrature and zero material points;
4. transfers across RC and steel-shell NC without Z-specific factors;
5. uses no structural Pu/comparator data for material identification.

Until this is source-closed, Z0–Z6 final post-crack 2D Pu remains explicitly `OPEN` rather than being filled by a later mathematical intersection or comparator-nearest root.
