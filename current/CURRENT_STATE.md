# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-22 13:20 +09:00  
**Status:** `MARGUERRE_AIRY_EXPLICIT / MATERIAL_FORM_7GATE_CERTIFIED / STRUCTURAL_RERUN_NOT_YET_PERFORMED / USER_ACCEPTANCE_PENDING`

## 0. Governing structural mainline is unchanged

The current structural theory remains the finite explicit Marguerre–Airy path.

Canonical structural theory:

`semantic_v2/20_theory/20260821_1733__NZSCCM__MARGUERRE_AIRY_EXPLICIT_LIMIT_THEORY_V1.md`

Last executed structural acceptance baseline:

`semantic_v2/40_execution/20260822_0745__NZSCCM__EXPLICIT_1D_2D_ASSESSMENT_RC_Z0Z6_SUHPC.md`

The governing execution sequence remains

\[
\boxed{
\text{1D explicit structural/capacity root}
\to
\text{Airy 2D membrane demand}
\to
\text{finite 2D material-capacity judgment}
}
\]

and not a second material-point solver.

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
STRUCTURAL_PU_RERUN = NOT_YET_PERFORMED
USER_ACCEPTANCE = PENDING
```

## 1. Current material source-of-truth chain

1. `semantic_v2/20_theory/20260822_1151__NZSCCM__NC_UHPC_7GATE_EXPLICIT_MATERIAL_REORGANIZATION_V1.md`
2. `semantic_v2/20_theory/20260822_1205__NZSCCM__NC_TC_APPENDIXB_SOURCE_CORRECTION_ADDENDUM.md`
3. `semantic_v2/20_theory/20260822_1240__NZSCCM__UHPC_ZHANG_BACKBONE_AND_LIU_CC_CONTINUOUS_SOURCE_MIN_GATE.md`
4. `semantic_v2/20_theory/20260822_1255__NZSCCM__NC_TC_FAILURE_ENVELOPE_VS_APPENDIXB_CONSTITUTIVE_PEAK_RESOLUTION.md`
5. `semantic_v2/20_theory/20260822_1315__NZSCCM__NC_UHPC_7GATE_MATERIAL_CERTIFICATE_V1.md`
6. `semantic_v2/20_theory/20260822_1320__NZSCCM__NC_CC_EQ317_PRINTED_TYPO_VS_FIG32_APPENDIXB_RESOLUTION.md`

The 13:15 certificate plus the 13:20 source-discrepancy addendum are the current consolidated material truth. Earlier temporary `OPEN` statuses are superseded where explicitly resolved.

## 2. Seven-gate result

```text
MATERIAL_FORM_7GATE_CERTIFICATE = PASS_WITH_DECLARED_SOURCE_KINKS_AND_PARAMETER_CAVEATS
NC_MATERIAL_FORM_7GATE = PASS
UHPC_MATERIAL_FORM_7GATE = PASS_WITH_DECLARED_FINITE_CC_CAPACITY_CUSP
```

`G6` remains the hard production constraint: every admitted material object is a finite algebraic/analytic stress/capacity relation, branch check, or finite analytic section primitive.

## 3. Normal concrete (NC)

### 3.1 Swartz parameter identity

- panel-specific `fcyl` and `eps0` are companion-cylinder measured anchors;
- Nguyen explicitly uses

\[
\boxed{f_c=0.85f'_{cyl}}
\]

as the panel in-situ analysis strength to account for the difference from standard cylinders;
- `E0` belongs to the same derived source lineage and is not treated as a third independent panel measurement;
- Swartz specimen-specific tensile strength was not reported, therefore `ft=0.10fc` remains a transparent project assumption when required.

```text
NC_SWARTZ_COMPRESSION_STRENGTH = 0.85_FCYL_SOURCE_IN_SITU_PANEL_STRENGTH
NC_SWARTZ_SPECIMEN_FT = SOURCE_OPEN
```

### 3.2 NC uniaxial/current backbones

```text
NC_COMPRESSION_BACKBONE = SAENZ_RETAINED_FOR_SWARTZ_RANGE
NC_TENSION_BACKBONE = T5_FOSTER_PROJECT_REDUCTION_RETAINED
```

No single-axis model is changed because of structural error sign.

### 3.3 NC CC

The accepted source form is

\[
\boxed{
K_{CC}^{NC}(a)=\frac{1+3.65a}{(1+a)^2},
\qquad a=p_m/p_M.
}
\]

The direct capacity factor is

\[
\lambda_{CC}^{NC}=\frac{f_cK_{CC}^{NC}(a)}{p_M^d}.
\]

Important source audit: the typeset text of Nguyen Eq. (3.17) prints `1+alpha^2`, but Nguyen Figure 3.2 and the executable Appendix-B `stmoduc` both use `(1+alpha)^2`. The latter two are mutually consistent and give the physically plotted equal-biaxial value `1.1625`; the printed Eq. (3.17) is therefore recorded as a thesis typesetting inconsistency.

```text
NGUYEN_EQ317_PRINTED_DENOMINATOR = SOURCE_TYPO_INCONSISTENT
NGUYEN_FIG32_APPENDIXB_DENOMINATOR = (1+alpha)^2 / ACCEPTED
NC_CC_CAPACITY = PASS_G6
```

### 3.4 NC TC/CT

The source failure envelope is

\[
\frac{p}{f_c}+\frac{t}{3f_t}=1
\]

and

\[
\frac{p}{2f_c}+\frac{t}{f_t}=1,
\]

meeting at

\[
(p/f_c,t/f_t)=(0.8,0.6).
\]

The Appendix-B extra minor-compressive `sig2p` relation is resolved as an equivalent-uniaxial constitutive peak/modulus object, not a second replacement capacity envelope.

```text
NC_TC_CT_CAPACITY = NGUYEN_EQ318_319 / PASS_G6
NC_TC_SOURCE_KINK = RETAINED
NC_FULL_INCREMENTAL_NGUYEN = ORACLE_ONLY
```

### 3.5 NC TT

The previously source-qualified finite T5-based project TT reduction is retained; no new TT coefficient is fitted or identified in the present round.

## 4. UHPC

### 4.1 Uniaxial compression

```text
UHPC_COMPRESSION_BACKBONE = ZHANG_2023
HU_WENXU = HISTORICAL_UNIAXIAL_COMPARATOR_ONLY
```

Current material-level values:

\[
f_c=141.1\ \mathrm{MPa},
\quad E_c=43.4\ \mathrm{GPa},
\quad \varepsilon_{c0}=0.0035,
\quad \nu=0.20,
\quad V_f=2\%.
\]

Ascending:

\[
g_a(x)=\frac{rx}{r-1+x^r},
\qquad r=\frac{E_c}{E_c-f_c/\varepsilon_{c0}}.
\]

Zero-confinement descending:

\[
g_d(x)=0.18+\frac{0.82}{1+\frac23(x-1)^2}.
\]

The two branches are stress-and-tangent continuous at the peak, globally bounded, and have finite analytic section primitives. Formal quadrature remains zero.

### 4.2 Uniaxial tension

```text
UHPC_TENSION_BACKBONE = HIEW_2024
```

The monotonic fibre-bridged sequence is retained: elastic -> strain hardening -> peak -> localization -> pull-out softening.

### 4.3 UHPC CC

Liu 2024 literal Eq. (4) has a source-level switch inconsistency: Table 5 reports an independently fitted ellipse coefficient `1.33`, while final Eq. (4) is machine-readable as `1.49`, and the stated switch at ratio `0.5` is not value-continuous.

No coefficient is modified. The project uses the conservative lower envelope of Liu's two own source curves:

\[
K_E(r)=\frac1{\sqrt{r^2-1.49r+1}},
\]

\[
K_P(r)=\frac{r+7.98}{(r+1.85)^2},
\]

\[
\boxed{K_{CC,U}(r)=\min[K_E(r),K_P(r)].}
\]

The unique crossover is

\[
r_*=0.576358545117484,
\qquad K(r_*)=1.45337946681509.
\]

Value continuity is restored without a fitted smoothing parameter; one finite capacity-gradient cusp is retained as a finite branch event.

```text
UHPC_CC_CAPACITY = LIU2024_SOURCE_MIN_PROJECT_REDUCTION / PASS_G6
UHPC_CC_VALUE_CONTINUITY = PASS
UHPC_CC_C1 = FINITE_SOURCE_MIN_CUSP
```

### 4.4 UHPC TC/CT and TT

TC/CT uses the Liu 2024 conservative sequential-loading capacity envelope. Any current-strain softening component may use only excess transverse tension

\[
\varepsilon_{t,ex}=\max(0,\varepsilon_t+\nu\varepsilon_c),
\]

so pure uniaxial Poisson expansion does not cause false TC softening.

TT uses the Liu 2024 conservative biaxial tensile cap equal to the uniaxial tensile capacity; Hiew remains the tensile stress backbone.

```text
UHPC_TC_CT_CAPACITY = LIU2024_SEQUENTIAL_CONSERVATIVE_ENVELOPE / PASS_G6
UHPC_TT_CAPACITY = LIU2024_UNIAXIAL_TENSILE_CAP / PASS_G6
UHPC_TC_CURRENT_SOFTENING = EXCESS_TENSION_ONLY
```

## 5. Current stop/go decision

The material-form gate now permits a subsequent structural 1D -> Airy 2D -> finite-capacity re-evaluation, but that re-evaluation has not yet been executed.

Any next structural run must preserve:

```text
NO_MATERIAL_POINTS
NO_SPATIAL_QUADRATURE
NO_HISTORY_STATE_MACHINE
NO_EXPERIMENT_OR_FEM_ROOT_SELECTION
NO_PU_MATERIAL_CALIBRATION
```

and must report the Swartz specimen-specific `ft` source uncertainty rather than hide it by calibration.
