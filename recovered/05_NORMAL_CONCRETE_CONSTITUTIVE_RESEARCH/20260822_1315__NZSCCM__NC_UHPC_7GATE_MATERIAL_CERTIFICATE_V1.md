# NZ-SCCM — NC/UHPC seven-gate explicit material certificate V1

**Date:** 2026-08-22 13:15 +09:00  
**Status:** `MATERIAL_FORM_7GATE_CERTIFICATE = PASS_WITH_DECLARED_SOURCE_KINKS_AND_PARAMETER_CAVEATS`  
**Structural status:** `UNCHANGED / Pu RERUN NOT PERFORMED`

## 0. Scope and hard boundary

This certificate consolidates:

- `20260822_1151__NZSCCM__NC_UHPC_7GATE_EXPLICIT_MATERIAL_REORGANIZATION_V1.md`;
- `20260822_1205__NZSCCM__NC_TC_APPENDIXB_SOURCE_CORRECTION_ADDENDUM.md`;
- `20260822_1240__NZSCCM__UHPC_ZHANG_BACKBONE_AND_LIU_CC_CONTINUOUS_SOURCE_MIN_GATE.md`;
- `20260822_1255__NZSCCM__NC_TC_FAILURE_ENVELOPE_VS_APPENDIXB_CONSTITUTIVE_PEAK_RESOLUTION.md`.

The structural backbone is not changed. No Case21, Z0-Z6, T120/T360 or BH Pu is recalculated in this certificate.

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_material_points = 0
RITZ_ORDER = NONE
LOAD_PATH_TRACKING = 0
HISTORY_STATE_MACHINE = OFF_MAINLINE
EXPERIMENT_IN_ROOT_SELECTION = 0
FEM_IN_ROOT_SELECTION = 0
STRUCTURAL_BACKBONE_CHANGED = FALSE
STRUCTURAL_PU_RERUN = NOT_PERFORMED
```

The material architecture is intentionally separated into:

\[
\boxed{
\text{uniaxial/current stress backbone + same-source tangent}
}
\]

and

\[
\boxed{
\text{finite 2D CC/TC/CT/TT capacity/admissibility gates + branch gradients}.
}
\]

A capacity gate is not silently reinterpreted as a second nonlinear material-point stress solver.

---

# 1. Seven gates

\[
\begin{array}{ll}
G_1:&\text{uniaxial compression reduction and parameter identity}\\
G_2:&\text{uniaxial tension reduction}\\
G_3:&CC/TC/CT/TT\text{ source support}\\
G_4:&\text{plane-stress / Poisson consistency}\\
G_5:&\text{same-source stress derivative or capacity gradient closure}\\
G_6:&\text{finite direct algebraic/analytic calculation}\\
G_7:&\text{no structural Pu backfit}
\end{array}
\]

`G6` remains the hard production gate.

---

# Part A — Normal concrete (NC)

## 2. Swartz material parameter identity

For Swartz panels the measured source anchors remain the panel-specific companion-cylinder values:

\[
f'_{cyl},\qquad \varepsilon_0.
\]

Nguyen explicitly states that the concrete strength used in the panel analysis is

\[
\boxed{f_c=0.85 f'_{cyl}}
\]

**to account for the difference between in-situ panel strength and standard cylinder strength**.

Therefore the current default Swartz NC compression-strength identity is source-restored as:

```text
SWARTZ_FCYL = MEASURED_COMPANION_CYLINDER_STRENGTH
SWARTZ_NC_FC = 0.85 * FCYL
SWARTZ_NC_FC_ROLE = SOURCE_PANEL_IN_SITU_ANALYSIS_STRENGTH
```

This is not introduced from the sign of the Pu error.

The source Young modulus used in the Swartz/Nguyen lineage is approximately derived from the selected analysis strength and peak strain, so it is not treated as a third independent material test anchor.

Swartz did not report specimen-specific direct/splitting tensile strength for the 24 panels. Hence a common project choice such as

\[
f_t=0.10f_c
\]

must remain explicitly marked as a **tensile-source assumption**, not a panel-specific measured parameter.

## 3. NC uniaxial/current backbones

Compression: retain the Saenz-type source backbone for the Swartz strength range:

\[
C(c)=\frac{\kappa c}{1+(\kappa-2)c+c^2},
\qquad
\kappa=\frac{E_0\varepsilon_0}{f_c}.
\]

Tension: retain the current T5 / Foster-type tension-stiffening reduction already qualified for value, derivative and boundedness. This is a project analytic reduction of the source tension-stiffening architecture, not a claim that Swartz measured `ft`.

## 4. NC CC capacity gate — Nguyen/Foster-Kupfer

For ordered positive compression magnitudes

\[
0\le p_m\le p_M,
\qquad a=p_m/p_M,
\]

Nguyen Eq. (3.17) gives

\[
\boxed{
K_{CC}^{NC}(a)=\frac{1+3.65a}{(1+a)^2}.}
\]

The finite capacity factor is

\[
\boxed{
\lambda_{CC}^{NC}
=\frac{f_cK_{CC}^{NC}(a)}{p_M^d}.}
\]

Axis and equal-biaxial checks:

\[
K(0)=1,
\qquad K(1)=1.1625.
\]

Same-source derivative:

\[
K'(a)=\frac{1.65-3.65a}{(1+a)^3}.
\]

`NC_CC_CAPACITY = PASS_G6`.

## 5. NC TC/CT capacity gate — Nguyen Eqs. (3.18)-(3.19)

Using positive tension/compression magnitudes \((t,p)\), the TC failure envelope is exactly:

\[
\boxed{
\frac{p}{f_c}+\frac{t}{3f_t}=1
}
\]

on the compression-axis segment and

\[
\boxed{
\frac{p}{2f_c}+\frac{t}{f_t}=1
}
\]

on the tension-axis segment.

They meet at

\[
\boxed{(p/f_c,t/f_t)=(0.8,0.6).}
\]

The source is C0 at this join and has a finite intentional gradient kink.

The Appendix-B extra minor-compressive `sig2p` relation belongs to the equivalent-uniaxial constitutive peak/modulus construction and is retained as an oracle, not added as a second unrelated capacity constraint.

`CT` is obtained by principal-direction exchange.

```text
NC_TC_CAPACITY = PASS_G6
NC_CT_CAPACITY = PASS_G6
NC_TC_SOURCE_KINK = RETAINED
```

## 6. NC TT

The current task did not reopen the previously qualified NC TT project reduction. Nguyen provides both the TT failure-envelope source and the cracked TT constitutive branch; the current production keeps the already-qualified finite T5-based TT reduction whose axes reduce to the uniaxial tension law and whose coefficients are material-level, not Pu-fitted.

```text
NC_TT = RETAINED_PROJECT_REDUCTION_WITH_NGUYEN_SOURCE_SUPPORT
```

No new TT coefficient is identified in this round.

## 7. NC seven-gate result

| Gate | NC result |
|---|---|
| G1 | PASS for Swartz compression identity: `fc=0.85 fcyl`; `E0` derived lineage stated |
| G2 | PASS functional reduction; specimen-specific Swartz `ft` remains source-open |
| G3 | PASS: CC and TC/CT source envelope recovered; TT retained source-qualified project reduction |
| G4 | PASS: existing plane-stress/Poisson architecture unchanged |
| G5 | PASS branchwise: axis stress tangent same-source; capacity gradients analytic; source kinks explicit |
| G6 | PASS: finite ratios/rational laws/branch checks only |
| G7 | PASS: no Pf/Pu/comparator parameter fitting |

```text
NC_MATERIAL_FORM_7GATE = PASS
NC_SWARTZ_SPECIMEN_TENSILE_STRENGTH_SOURCE = OPEN
```

The remaining `ft` uncertainty is an input/source uncertainty, not a failure of the explicit material architecture.

---

# Part B — UHPC

## 8. UHPC uniaxial compression — Zhang 2023

The production compression backbone is now:

```text
UHPC_COMPRESSION_BACKBONE = ZHANG_2023
HU_WENXU = HISTORICAL_UNIAXIAL_COMPARATOR_ONLY
```

Project material values retained by material-level audit:

\[
f_c=141.1\ \mathrm{MPa},
\quad
E_c=43.4\ \mathrm{GPa},
\quad
\varepsilon_{c0}=0.0035,
\quad
\nu=0.20,
\quad
V_f=0.02.
\]

Only `fc=141.1 MPa` is user-immutable; the other values were retained after source review, not because of structural load matching.

Ascending:

\[
\boxed{
g_a(x)=\frac{rx}{r-1+x^r}},
\qquad
r=\frac{E_c}{E_c-f_c/\varepsilon_{c0}}.
\]

Zero-confinement descending:

\[
\boxed{
g_d(x)=0.18+\frac{0.82}{1+\frac23(x-1)^2}}.
\]

Both stress and same-source derivative meet at the peak with zero slope; the postpeak is globally bounded and tends to the source residual level 0.18.

Finite analytic section primitives were established in the 12:40 report, using a finite Gauss hypergeometric primitive for the ascending branch and elementary `atan/log` primitives for the descending branch. Thus the noninteger power does not force spatial or material-point quadrature.

`UHPC_ZHANG_G6 = PASS`.

## 9. UHPC uniaxial tension — Hiew 2024

The fibre-bridged monotonic tensile backbone remains Hiew 2024:

\[
\text{elastic}
\to
\text{strain hardening}
\to
\text{peak}
\to
\text{localization}
\to
\text{fiber pull-out softening}.
\]

Current 2%-fibre material-level anchors are retained; no structural Pu is used to identify them.

`UHPC_TENSION_BACKBONE = HIEW_2024`.

## 10. UHPC CC — Liu 2024 source-min project capacity reduction

Liu 2024 reports two fitted CC source curves and a literal final piecewise Eq. (4). The machine-readable final Eq. (4) uses ellipse coefficient `1.49`, while Table 5 reports the independently fitted ellipse coefficient `1.33`; the literal stated switch at stress ratio 0.5 does not produce a continuous value.

No source coefficient is altered.

For ordered compression ratio

\[
r=p_m/p_M\in[0,1],
\]

define the literal source candidate radial capacities

\[
K_E(r)=\frac1{\sqrt{r^2-1.49r+1}},
\]

\[
K_P(r)=\frac{r+7.98}{(r+1.85)^2}.
\]

The project capacity gate is the conservative lower source envelope

\[
\boxed{
K_{CC,U}(r)=\min[K_E(r),K_P(r)].}
\]

This has no fitted coefficient and no structural comparator. The unique intersection is

\[
r_*=0.576358545117484,
\]

where both capacities equal

\[
1.45337946681509.
\]

Thus the value is continuous. The lower envelope retains a finite derivative cusp at this single ratio. It is handled as a finite capacity event, not smoothed by an arbitrary-width bridge.

Direct re-cut:

\[
\boxed{
\lambda_{CC,U}
=\frac{f_cK_{CC,U}(r)}{p_M^d}.}
\]

```text
UHPC_CC_CAPACITY = LIU2024_SOURCE_MIN_PROJECT_REDUCTION
UHPC_CC_VALUE_CONTINUITY = PASS
UHPC_CC_C1 = FINITE_SOURCE_MIN_CUSP
UHPC_CC_G6 = PASS
```

## 11. UHPC TC/CT — Liu 2024 capacity + excess-strain current softening

Liu 2024 shows that loading path matters and adopts a conservative sequential-loading TC envelope. The finite capacity gate is:

\[
\frac{t}{f_t}=1,
\qquad 0\le p/f_c\le0.352,
\]

followed by

\[
\frac{t}{f_t}+1.542\frac{p}{f_c}-1.542=0,
\qquad 0.352\le p/f_c\le1.
\]

This gives a finite scalar ray re-cut with no history solver.

For any optional current-stress softening component, total positive Poisson lateral strain is not allowed to drive TC softening. Use excess transverse tension:

\[
\varepsilon_{t,ex}=\max(0,\varepsilon_t+\nu\varepsilon_c),
\]

so pure uniaxial compression gives \(\varepsilon_{t,ex}=0\).

The G6-compatible candidate remains

\[
\beta_{TC}
=
\max[0.55,(1+2500\varepsilon_{t,ex})^{-0.20}].
\]

`CT` follows by principal-direction exchange.

## 12. UHPC TT

Liu 2024 conservatively takes biaxial tensile strength equal to the uniaxial tensile strength. Hence

\[
\boxed{
\lambda_{TT,U}=rac{f_t}{\max(t_1^d,t_2^d)}.
}
\]

This is a capacity boundary; it does not replace Hiew's uniaxial/fibre-bridged stress backbone with a fictitious full two-direction history model.

## 13. UHPC seven-gate result

| Gate | UHPC result |
|---|---|
| G1 | PASS — Zhang 2023 compression + source-reviewed material parameters |
| G2 | PASS — Hiew 2024 monotonic tension |
| G3 | PASS at 2D capacity level — Liu 2024 CC/TC/CT/TT |
| G4 | PASS — existing plane-stress architecture; TC uses excess, not Poisson, tension |
| G5 | PASS branchwise — Zhang C1 peak; Hiew branch derivatives; capacity gradients explicit; one declared CC cusp |
| G6 | PASS — finite algebraic/analytic capacity and section primitives; no material points/history/spatial quadrature |
| G7 | PASS — no T/BH/FEM/Pu calibration |

```text
UHPC_MATERIAL_FORM_7GATE = PASS_WITH_DECLARED_FINITE_CC_CAPACITY_CUSP
```

---

# 14. Combined nine-grid / sector certificate

| Material | C | T | CC | TC | CT | TT |
|---|---|---|---|---|---|---|
| NC | Saenz retained | T5/Foster retained | Nguyen/Foster-Kupfer Eq3.17 PASS | Nguyen Eq3.18-3.19 PASS | symmetric PASS | retained T5-based project reduction, source-supported |
| UHPC | Zhang 2023 PASS | Hiew 2024 PASS | Liu2024 source-min PASS, one finite cusp | Liu2024 capacity PASS + excess-strain softening component | symmetric PASS | Liu2024 capacity PASS + Hiew axis backbone |

Origin/axes:

- existing plane-stress Poisson initialization is unchanged;
- all adopted capacity gates recover their uniaxial axes;
- UHPC TC softening does not activate from pure Poisson lateral expansion;
- no new material state variable is introduced.

Boundedness:

- NC Saenz/T5 existing bounds retained;
- NC CC/TC capacity gates finite on their physical ratio domains;
- Zhang UHPC postpeak tends to finite 0.18 residual;
- UHPC CC source-min gate is finite on `r in [0,1]`;
- UHPC TC capacity is finite piecewise;
- UHPC TT is bounded by `ft`.

---

# 15. Final decision

```text
MATERIAL_FORM_7GATE_CERTIFICATE = PASS_WITH_DECLARED_SOURCE_KINKS_AND_PARAMETER_CAVEATS

NC_MATERIAL_FORM_7GATE = PASS
NC_SWARTZ_COMPRESSION_STRENGTH = 0.85_FCYL_SOURCE_IN_SITU_PANEL_STRENGTH
NC_SWARTZ_SPECIMEN_FT = SOURCE_OPEN
NC_CC_CAPACITY = NGUYEN_EQ317
NC_TC_CT_CAPACITY = NGUYEN_EQ318_319
NC_TT = RETAINED_SOURCE_QUALIFIED_PROJECT_REDUCTION

UHPC_MATERIAL_FORM_7GATE = PASS_WITH_DECLARED_FINITE_CC_CAPACITY_CUSP
UHPC_COMPRESSION_BACKBONE = ZHANG_2023
UHPC_TENSION_BACKBONE = HIEW_2024
UHPC_CC_CAPACITY = LIU2024_SOURCE_MIN_PROJECT_REDUCTION
UHPC_TC_CT_CAPACITY = LIU2024_SEQUENTIAL_CONSERVATIVE_ENVELOPE
UHPC_TT_CAPACITY = LIU2024_UNIAXIAL_TENSILE_CAP
UHPC_TC_CURRENT_SOFTENING = EXCESS_TENSION_ONLY

N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_material_points = 0
LOAD_PATH_TRACKING = 0
HISTORY_STATE_MACHINE = OFF_MAINLINE
STRUCTURAL_BACKBONE_CHANGED = FALSE
STRUCTURAL_PU_RERUN = NOT_PERFORMED
```

The explicit material-form gate is now complete enough to permit a subsequent structural 1D->2D reevaluation. That reevaluation must preserve the same finite capacity architecture and must report the Swartz `ft` source uncertainty rather than using experimental Pu to choose it.
