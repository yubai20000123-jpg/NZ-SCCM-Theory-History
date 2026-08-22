# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-22 13:15 +09:00  
**Status:** `MARGUERRE_AIRY_EXPLICIT / MATERIAL_FORM_7GATE_CERTIFIED / STRUCTURAL_RERUN_NOT_YET_PERFORMED / USER_ACCEPTANCE_PENDING`

## 0. Governing structural mainline remains unchanged

Current structural theory remains the finite explicit Marguerre–Airy formulation:

\[
P_{pb}(q)=P_{cr}\frac{q}{q+q_0}+Cq(q+2q_0),
\]

\[
n(s;q)=\frac{P_{pb}(q)}b+Gq(q+2q_0)(1-2s^2),
\qquad
m(s;q)=Jqs,
\]

with

\[
N_x=-\frac{\alpha^2b^2\Delta_A}{8A_{22}}q(q+2q_0)\cos(2\beta y),
\qquad N_{xy}=0.
\]

Canonical structural theory:

`semantic_v2/20_theory/20260821_1733__NZSCCM__MARGUERRE_AIRY_EXPLICIT_LIMIT_THEORY_V1.md`

Pre-material-reorganization 1D/2D acceptance baseline:

`semantic_v2/40_execution/20260822_0745__NZSCCM__EXPLICIT_1D_2D_ASSESSMENT_RC_Z0Z6_SUHPC.md`

That package and its RC / Z0–Z6 / steel-shell-UHPC result tables remain the last executed structural results. They have **not** been silently overwritten by the material work below.

The formal execution architecture is still:

\[
\boxed{
\text{1D explicit structural/capacity root}
\to
\text{Airy 2D membrane demand}
\to
\text{finite 2D material-capacity judgment}
}
\]

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

## 1. 2026-08-22 material reorganization chain

Current material chain, in order:

1. `semantic_v2/20_theory/20260822_1151__NZSCCM__NC_UHPC_7GATE_EXPLICIT_MATERIAL_REORGANIZATION_V1.md`
2. `semantic_v2/20_theory/20260822_1205__NZSCCM__NC_TC_APPENDIXB_SOURCE_CORRECTION_ADDENDUM.md`
3. `semantic_v2/20_theory/20260822_1240__NZSCCM__UHPC_ZHANG_BACKBONE_AND_LIU_CC_CONTINUOUS_SOURCE_MIN_GATE.md`
4. `semantic_v2/20_theory/20260822_1255__NZSCCM__NC_TC_FAILURE_ENVELOPE_VS_APPENDIXB_CONSTITUTIVE_PEAK_RESOLUTION.md`
5. `semantic_v2/20_theory/20260822_1315__NZSCCM__NC_UHPC_7GATE_MATERIAL_CERTIFICATE_V1.md`

The 13:15 certificate is the current consolidated material source of truth. Earlier temporary `OPEN` statuses are superseded where explicitly resolved below.

## 2. Seven-gate contract

\[
\begin{array}{ll}
G_1:&\text{uniaxial compression reduction and parameter identity}\\
G_2:&\text{uniaxial tension reduction}\\
G_3:&CC/TC/CT/TT\text{ source support}\\
G_4:&\text{plane-stress / Poisson consistency}\\
G_5:&\text{same-source stress derivative or capacity-gradient closure}\\
G_6:&\text{finite direct algebraic/analytic calculation}\\
G_7:&\text{no structural Pu backfit}
\end{array}
\]

`G6` remains the hard production constraint.

## 3. NC — current material identity

### 3.1 Swartz parameter identity

For Swartz panels:

- `fcyl` and `eps0` are panel-specific companion-cylinder measured anchors;
- Nguyen explicitly uses

\[
\boxed{f_c=0.85f'_{cyl}}
\]

as the panel in-situ analysis strength to account for the difference from standard cylinders;
- `E0` belongs to the same source lineage as an approximately derived modulus rather than a third independent measured panel property;
- specimen-specific Swartz tensile strength was not reported, so `ft=0.10fc` remains a transparent common project assumption where a tensile input is required.

```text
NC_SWARTZ_COMPRESSION_STRENGTH = 0.85_FCYL_SOURCE_IN_SITU_PANEL_STRENGTH
NC_SWARTZ_SPECIMEN_FT = SOURCE_OPEN
```

### 3.2 NC stress backbones

```text
NC_COMPRESSION_BACKBONE = SAENZ_RETAINED_FOR_SWARTZ_RANGE
NC_TENSION_BACKBONE = T5_FOSTER_PROJECT_REDUCTION_RETAINED
```

No new single-axis model is selected merely to improve structural error.

### 3.3 NC finite 2D capacity gates

CC from Nguyen/Foster–Kupfer Eq. (3.17):

\[
K_{CC}^{NC}(a)=\frac{1+3.65a}{(1+a)^2},
\qquad a=p_m/p_M,
\]

\[
\lambda_{CC}^{NC}=\frac{f_cK_{CC}^{NC}(a)}{p_M^d}.
\]

TC/CT from Nguyen failure-envelope Eqs. (3.18)–(3.19):

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

The Appendix-B extra minor-compressive `sig2p` branch is now resolved as a constitutive equivalent-uniaxial peak/modulus object, not a second replacement capacity envelope.

TT keeps the previously source-qualified finite T5-based project reduction; the current task did not identify a new TT coefficient.

```text
NC_CC_CAPACITY = NGUYEN_EQ317 / PASS_G6
NC_TC_CT_CAPACITY = NGUYEN_EQ318_319 / PASS_G6
NC_TC_SOURCE_KINK = RETAINED
NC_TT = RETAINED_SOURCE_QUALIFIED_PROJECT_REDUCTION
NC_FULL_INCREMENTAL_NGUYEN = ORACLE_ONLY
NC_MATERIAL_FORM_7GATE = PASS
```

## 4. UHPC — current material identity

### 4.1 Compression backbone

The current production UHPC compression backbone is now Zhang 2023:

\[
g_a(x)=\frac{rx}{r-1+x^r},
\qquad
r=\frac{E_c}{E_c-f_c/\varepsilon_{c0}},
\]

with zero-confinement postpeak

\[
g_d(x)=0.18+\frac{0.82}{1+\frac23(x-1)^2}.
\]

Current material-level values:

\[
f_c=141.1\ \mathrm{MPa},
\quad E_c=43.4\ \mathrm{GPa},
\quad \varepsilon_{c0}=0.0035,
\quad \nu=0.20,
\quad V_f=2\%.
\]

Only `fc=141.1 MPa` is user-immutable; the other values were retained after material-source review.

Finite analytic section primitives exist for both Zhang branches, so this choice does not introduce formal quadrature.

```text
UHPC_COMPRESSION_BACKBONE = ZHANG_2023
HU_WENXU = HISTORICAL_UNIAXIAL_COMPARATOR_ONLY
UHPC_ZHANG_G6 = PASS
```

### 4.2 Tension backbone

```text
UHPC_TENSION_BACKBONE = HIEW_2024
```

The fibre-bridged monotonic sequence remains elastic -> strain hardening -> peak -> localization -> pull-out softening.

### 4.3 UHPC finite 2D capacity gates

CC: Liu 2024 source curves are retained without modifying coefficients. Because the literal published/preprint Eq. (4) switch gives a value discontinuity, the project capacity gate uses the conservative lower envelope of Liu's own two source curves:

\[
K_E(r)=\frac1{\sqrt{r^2-1.49r+1}},
\]

\[
K_P(r)=\frac{r+7.98}{(r+1.85)^2},
\]

\[
\boxed{K_{CC,U}(r)=\min[K_E(r),K_P(r)].}
\]

Unique crossover:

\[
r_*=0.576358545117484,
\qquad K(r_*)=1.45337946681509.
\]

The value is continuous; one finite capacity-gradient cusp remains and is handled as a finite branch event rather than hidden by an arbitrary smoothing width.

TC/CT: Liu 2024 conservative sequential-loading envelope is the capacity gate. An optional current-stress softening component may use only excess transverse tension

\[
\varepsilon_{t,ex}=\max(0,\varepsilon_t+\nu\varepsilon_c),
\]

so pure Poisson expansion under uniaxial compression does not activate TC softening.

TT: Liu 2024 conservative biaxial tensile capacity equals the uniaxial tensile capacity, while Hiew remains the tensile stress backbone.

```text
UHPC_CC_CAPACITY = LIU2024_SOURCE_MIN_PROJECT_REDUCTION / PASS_G6
UHPC_CC_VALUE_CONTINUITY = PASS
UHPC_CC_C1 = FINITE_SOURCE_MIN_CUSP
UHPC_TC_CT_CAPACITY = LIU2024_SEQUENTIAL_CONSERVATIVE_ENVELOPE / PASS_G6
UHPC_TT_CAPACITY = LIU2024_UNIAXIAL_TENSILE_CAP / PASS_G6
UHPC_TC_CURRENT_SOFTENING = EXCESS_TENSION_ONLY
UHPC_MATERIAL_FORM_7GATE = PASS_WITH_DECLARED_FINITE_CC_CAPACITY_CUSP
```

## 5. Combined material certificate

```text
MATERIAL_FORM_7GATE_CERTIFICATE = PASS_WITH_DECLARED_SOURCE_KINKS_AND_PARAMETER_CAVEATS

NC_MATERIAL_FORM_7GATE = PASS
NC_SWARTZ_SPECIMEN_FT = SOURCE_OPEN

UHPC_MATERIAL_FORM_7GATE = PASS_WITH_DECLARED_FINITE_CC_CAPACITY_CUSP

N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_material_points = 0
LOAD_PATH_TRACKING = 0
HISTORY_STATE_MACHINE = OFF_MAINLINE
EXPERIMENT_IN_ROOT_SELECTION = 0
FEM_IN_ROOT_SELECTION = 0
```

The explicit material-form gate is now complete enough to **permit** the next structural 1D -> Airy 2D -> finite capacity re-evaluation. That structural re-evaluation has not yet been performed in this state file and must not use experimental/fem values to choose material parameters or roots.
