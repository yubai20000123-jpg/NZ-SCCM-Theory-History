# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-12 17:34 +08:00  
**Purpose:** 唯一当前工作入口；采用“内容描述 + YYYYMMDD_HHMM”时间戳命名，不再用 V1/V2/R1/R2 作为当前正式主线标识。

## 0. Current naming governance

Current naming decision:

- `current/governance/NZ_SCCM_TIMESTAMP_NAMING_AND_BASELINE_DECISION_20260812_1734.md`

Rule:

```text
<clear-content-description>_YYYYMMDD_HHMM.<ext>
```

Old V/R/NC-R numbered files remain history only unless explicitly requested for historical audit.

---

## 1. Current governing theory baseline

Formal name:

**NZ-SCCM 普通混凝土钢筋板零空间解析极限承载力—切线稳定统一理论**

Current governing file:

- `current/theory/NZ_SCCM_NC_REBAR_ZERO_SPATIAL_ANALYTIC_LIMIT_TANGENT_UNIFIED_THEORY_20260812_1734.md`

Core chain:

\[
\boxed{
\text{raw input}
\to R10
\to N48\text{-}C1/MM
\to \text{Cayley--Hamilton}
\to \text{Nguyen complete halfwave}
\to \text{general D15 exact moments}
\to P,R_q,L
\to \Gamma_0
\to \{\text{limit point},K_Z\text{ tangent loss}\}
}
\]

Highest-priority invariants:

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
ACTIVE_MODE = m=1
KINEMATICS = NGUYEN_SECOND_ORDER
R10_MATERIAL_TARGET = FROZEN
N48_ORDER = 48
CAYLEY_HAMILTON = GOVERNING
EXACT_MOMENT_ENGINE = D15_GENERAL_TRIG_MOMENTS
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
STRUCTURAL_CALIBRATION = NO
PANEL_LEVEL_SURROGATE = NO
```

Production prohibits spatial Gauss/Simpson/adaptive quadrature, spatial Chebyshev collocation, material-point grids/cells, experiment-driven parameter tuning and experiment-driven root selection.

---

## 2. General D15 identity

Governing structural scalar basis:

\[
Q(X,Y,\zeta)=\sum c_{prush}\sin^pX\cos^rX\sin^uY\cos^sY\zeta^h.
\]

Exact moments:

\[
J_{pr}=\int_0^\pi\sin^pX\cos^rX\,dX,
\qquad
Z_h=\int_{-1}^{1}\zeta^h\,d\zeta,
\]

\[
\mathscr D[Q]=\sum c_{prush}J_{pr}J_{us}Z_h.
\]

This governs `Syy`, `Qq`, all same-expression derivatives used in `L`, and all Zhou/Navier current-tangent modal integrands.

```text
FORMAL_SPATIAL_SAMPLING = 0
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_SPATIAL_SUBDOMAINS = 1
```

---

## 3. Primary equilibrium branch and limit candidate

\[
P=P_c+P_s,
\qquad
R_q=R_{q,c}+R_{q,s}.
\]

\[
\Gamma_0=\operatorname{Conn}_{(0,0)}(\{R_q=0\}\cap\mathcal A).
\]

At regular points,

\[
L=P_DR_{q,q}-P_qR_{q,D}=\nabla P\cdot(R_{q,q},-R_{q,D}).
\]

The first `+ -> -` local maximum along the correct `Gamma0` is only a **limit-point candidate** until the tangent gate has been completed.

Maximum-among-all-roots, experiment-nearest-root and historical-root targeting remain prohibited.

---

## 4. Zhou/Navier current-tangent gate

The same current material operator must generate

\[
\mathbb C_t=\frac{\partial\boldsymbol\sigma}{\partial\mathbf E}.
\]

Total modal current tangent:

\[
K_Z=K_{Z,c}^{mat}+K_{Z,c}^{geo}+K_{Z,s}^{mat}+K_{Z,s}^{geo}.
\]

Because

\[
\mathbf X=\mathbf E_u/\varepsilon_0,
\]

the tangent directional derivative must obey

\[
\delta\mathbf X=\delta\mathbf E_u/\varepsilon_0.
\]

For Case21 the unloaded square-halfwave regression is

\[
\boxed{K_Z(0,0)=\frac{E_0t_p^3\pi^4}{12(1-\nu^2)b^2}=823.416805665\ \mathrm{N/mm}.}
\]

```text
ZERO_STATE_TANGENT_REGRESSION = PASS
```

Local `t_p^3 Ct/12` formulas are not the governing definition for a nonuniform current tangent field; they remain only the uniform-tangent degeneration.

---

## 5. Current Case21 execution contract

Formal name:

**NZ-SCCM Case21 零空间解析极限—切线稳定统一计算合同**

Current governing file:

- `current/workflows/NZ_SCCM_CASE21_ZERO_SPATIAL_ANALYTIC_EXECUTION_CONTRACT_20260812_1734.md`

Mandatory order:

```text
raw Case21 inputs
-> fresh R10 material functions
-> fresh N48-C1/MM coefficients
-> Cayley-Hamilton
-> Nguyen complete continuous halfwave
-> general-D15 Syy
-> general-D15 Qq
-> fresh Rq(D,q)
-> corrected Gamma0 from (0,0)
-> first +->- limit candidate
-> zero-state tangent regression
-> KZ,c^mat + KZ,c^geo + KZ,s^mat + KZ,s^geo
-> K_Z along the same corrected Gamma0
-> determine whether tangent loss occurs before limit point
-> theory-result freeze
-> experiment-only comparison
```

A calculation cannot receive `CALCULATION_CLOSURE = PASS` before every mandatory gate is reported.

---

## 6. Current Case21 blocker

Current audit record:

- `current/audits/NZ_SCCM_CASE21_TANGENT_GATE_AND_GENERAL_D15_RECHECK_20260812.md`

The previous Case21 fresh result remains historical/audit evidence only. Under the governing general-D15 recheck:

```text
GENERAL_D15_Syy_RECHECK = PASS
GENERAL_D15_Qq_RECHECK = FAIL AGAINST PREVIOUS EXECUTION
PREVIOUS_CASE21_GAMMA0 = NOT CURRENTLY ACCEPTED
PREVIOUS_CASE21_LIMIT_LOAD = AUDIT RECORD ONLY / NOT CURRENT PRODUCTION RESULT
ZERO_STATE_TANGENT_REGRESSION = PASS
PRODUCTION_TANGENT_GATE = NOT YET REACHED ON A CORRECTED BRANCH
CASE21_COMPLETE_CLOSURE = BLOCKED
```

The blocker is execution consistency, not reopening of the material/current-tangent theory.

---

## 7. Current next task

Only authorized next execution:

\[
\boxed{
\text{fresh general-D15 }Q_q
\to R_q(D,q)
\to \Gamma_0
\to \text{first }+\to-\text{ limit candidate}
\to K_Z\text{ on same }\Gamma_0
\to \text{final control classification}
}
\]

No historical Case21 roots/loads/paths, no historical FE/Gauss/Simpson/material-point results, and no experimental load may participate in that calculation. Experimental data may be opened only after the new theory result is frozen.
