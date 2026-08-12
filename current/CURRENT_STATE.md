# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-12 16:53 +08:00  
**Purpose:** 唯一当前工作入口；反映 NC-R1 正式闭合理论、Case21 general-D15/tangent 复核后的真实状态。

## 0. Highest-priority invariants

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
ACTIVE_MODE = m=1
KINEMATICS = NGUYEN_SECOND_ORDER
R10_MATERIAL_TARGET = FROZEN
N48_ORDER = 48
U_COMPILER  = N48-C1
C_COMPILER  = N48-C1
T7_COMPILER = N48-C1
T_COMPILER  = N48-C1-CONSTRAINED-MINIMAX
CAYLEY_HAMILTON = GOVERNING
EXACT_MOMENT_ENGINE = D15_GENERAL_TRIG_MOMENTS
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
STRUCTURAL_CALIBRATION = NO
```

Formal production prohibits spatial Gauss/Simpson/adaptive quadrature, spatial Chebyshev collocation, material-point grids/cells, panel-level P/R surrogates, experiment-driven material tuning and experiment-driven root selection.

---

## 1. Governing formal theory

Current canonical theory-writing baseline:

- `current/theory/NZ_SCCM_NC_R1_FORMAL_CLOSURE_ZHOU_STYLE_CANONICAL_20260812.md`
- `current/theory/NZ_SCCM_NC_R1_FORMAL_CLOSURE_CANONICAL_ERRATA_20260812.md`

Governing formal chain:

\[
\boxed{
\text{material/geometric input}
\to R10
\to N48\text{-}C1/MM
\to \text{Cayley--Hamilton}
\to \text{Nguyen complete halfwave}
\to \text{general D15 exact moments}
\to P(D,q),R_q(D,q),L(D,q)
\to \Gamma_0
\to \text{first }+\to-\text{ limit candidate}.}
\]

The independent theory audit did not overturn this central zero-spatial analytic architecture. No result authorizes reopening R10 or raising N48 order.

---

## 2. General D15 identity

The governing structural integration basis is

\[
Q=\sum c_{prush}\sin^pX\cos^rX\sin^uY\cos^sY\zeta^h,
\]

with

\[
J_{pr}=\int_0^\pi\sin^pX\cos^rX\,dX,
\qquad
Z_h=\int_{-1}^{1}\zeta^h\,d\zeta,
\]

\[
\mathscr D[Q]=\sum c_{prush}J_{pr}J_{us}Z_h.
\]

This general-D15 form governs `Syy`, `Qq`, all derivatives used in `L`, and all Zhou/Navier current-tangent modal integrands.

```text
D15_GENERAL_EXACT_TRIG_MOMENTS = GOVERNING
FORMAL_SPATIAL_QUADRATURE = 0
```

---

## 3. NC-R1 root topology

\[
\mathcal A=\{D\ge0,q\ge0,\text{ all compiler/material/rebar/source gates pass}\},
\]

\[
\Gamma_0=\operatorname{Conn}_{(0,0)}(\{R_q=0\}\cap\mathcal A).
\]

At regular points,

\[
\mathbf t_0=(R_{q,q},-R_{q,D}),
\]

\[
L=P_DR_{q,q}-P_qR_{q,D}=\nabla P\cdot\mathbf t_0.
\]

The NC-R1 limit candidate remains the first `+ -> -` local maximum encountered from `(0,0)` along the admissible connected branch.

Maximum-among-all-roots, experiment-nearest-root and historical-root targeting remain prohibited.

---

## 4. Zhou/Navier current-tangent gate — now mandatory in the Case21 execution contract

The canonical theory defines

\[
\mathbb C_t=\frac{\partial\boldsymbol\sigma}{\partial\mathbf E},
\]

and

\[
K_Z=K_{Z,c}^{mat}+K_{Z,c}^{geo}+K_{Z,s}^{mat}+K_{Z,s}^{geo}.
\]

All four terms must be generated from the same current state and contracted by general D15 exact moments.

Because

\[
\mathbf X=\mathbf E_u/\varepsilon_0,
\]

the tangent directional derivative must include

\[
\delta\mathbf X=\delta\mathbf E_u/\varepsilon_0.
\]

Case21 unloaded-state regression:

\[
\boxed{K_Z(0,0)=\frac{E_0t_p^3\pi^4}{12(1-\nu^2)b^2}=823.416805665\ \mathrm{N/mm}.}
\]

```text
ZERO_STATE_TANGENT_REGRESSION = PASS
```

Current governing Case21 execution contract:

- `current/workflows/NZ_SCCM_CASE21_NC_R1_FORMAL_CLOSURE_PRODUCTION_CONTRACT_WITH_TANGENT_GATE_20260812.md`

A Case21 result cannot receive `CALCULATION_CLOSURE = PASS` unless the corrected general-D15 primary branch and the pre-limit `K_Z` history are both resolved.

---

## 5. Case21 tangent/general-D15 audit — CURRENT BLOCKER

Audit:

- `current/audits/NZ_SCCM_CASE21_TANGENT_GATE_AND_GENERAL_D15_RECHECK_20260812.md`

The previous fresh Case21 report is retained only as an audit record:

- `current/results/NZ_SCCM_CASE21_NC_R1_FORMAL_CLOSURE_FRESH_CALCULATION_20260812.md`

The tangent audit first rechecked the reported state using the governing **general D15** contraction.

At the previously reported candidate

\[
D=0.8903314709224796,
\qquad
q=0.0018331919936158214,
\]

the axial-stress contraction is reproduced:

\[
\mathscr D[S_{yy}]\approx-13.43326517,
\]

consistent with the previous axial-load calculation.

However the generalized-work contraction is not reproduced:

\[
\boxed{\mathscr D[Q_q]\approx3.57804}
\]

instead of the previously reported

\[
5.195117174559211.
\]

Using the same exact prefactor gives approximately

\[
R_{q,c}\approx2.3104\times10^5\ \mathrm{N\,mm},
\]

while the closed reinforcement term remains approximately

\[
R_{q,s}\approx-3.35459\times10^5\ \mathrm{N\,mm}.
\]

Therefore

\[
\boxed{R_q\approx-1.04418\times10^5\ \mathrm{N\,mm}},
\]

so that state is not an equilibrium state under the current canonical general-D15 `Q_q` contraction.

A second recheck at the previously reported lower branch state

\[
D=0.5,\qquad q=0.0013204714709
\]

also gives approximately

\[
\boxed{R_q\approx-8.81625\times10^4\ \mathrm{N\,mm}}.
\]

Thus the discrepancy affects the previously reported branch, not only its nominal limit point.

```text
FIRST_SUBSTANTIVE_BLOCKER = GENERAL_D15_Qq_CONTRACTION_MISMATCH
```

---

## 6. Tangent result at the old candidate — diagnostic only

With the mandatory `1/epsilon_0` tangent scaling, the old reported candidate gives the approximate decomposition

\[
K_{Z,c}^{mat}\approx693.62\ \mathrm{N/mm},
\]

\[
K_{Z,c}^{geo}\approx-731.14\ \mathrm{N/mm},
\]

\[
K_{Z,s}^{mat}=0
\]

for the mid-surface reinforcement layer, and

\[
K_{Z,s}^{geo}\approx-52.01\ \mathrm{N/mm}.
\]

Hence

\[
K_Z\approx-89.5\ \mathrm{N/mm}.
\]

This is **diagnostic only** because Section 5 shows that the state is not on the current canonical equilibrium branch. It cannot be used to declare a production tangent loss or a production capacity.

---

## 7. Required next execution order

The next Case21 calculation must use only the raw Case21 input + canonical theory + freshly generated current material coefficients and must execute:

```text
1. rebuild general-D15 Qq(D,q)
2. rebuild the connected equilibrium branch Gamma0 from (0,0)
3. recompute the first +->- NC-R1 limit candidate
4. compute KZ,c^mat, KZ,c^geo, KZ,s^mat, KZ,s^geo on that corrected branch
5. determine whether an admissible K_Z=0 occurs before the first load maximum
6. only after all production gates pass, freeze the theory result
7. only then compare with the experimental load
```

No historical Case21 root/path or historical Gauss/FE result may be used as a target.

---

## 8. Current status

```text
CORE_ZERO_SPATIAL_ANALYTIC_IDEA = RETAINED
R10 = FROZEN / GOVERNING
N48_C1_MM = GOVERNING
CAYLEY_HAMILTON = GOVERNING
NGUYEN_SECOND_ORDER = GOVERNING
D15_GENERAL_EXACT_TRIG_MOMENTS = GOVERNING
NC_R1_ROOT_TOPOLOGY = GOVERNING
ZERO_STATE_TANGENT_REGRESSION = PASS

PREVIOUS_372p775725_kN = AUDIT RECORD / NOT CURRENT PRODUCTION Pu
PREVIOUS_FRESH_GAMMA0 = NOT CURRENTLY ACCEPTED
GENERAL_D15_Qq_BRANCH = MUST BE REBUILT
PRODUCTION_TANGENT_GATE = NOT YET REACHED
CASE21_CALCULATION_CLOSURE = BLOCKED
CASE21_UNIQUE_PRODUCTION_Pu = NOT CURRENTLY FROZEN

HISTORICAL_GAUSS_FE_RESULT_USED_IN_CURRENT_RECHECK = NO
SWARTZ24_RECALCULATION = NOT AUTHORIZED / NOT PERFORMED
CURRENT_NEXT_TASK = REBUILD CASE21 FROM CANONICAL GENERAL-D15 CONTRACT
```
