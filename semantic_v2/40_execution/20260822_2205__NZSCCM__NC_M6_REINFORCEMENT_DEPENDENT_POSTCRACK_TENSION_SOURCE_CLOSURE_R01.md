# NZ-SCCM — NC-M6 reinforcement-dependent postcrack tension source-closure R01

**Time:** 2026-08-22 22:05 +08:00  
**Status:** `EXECUTED / EXPLICIT_STRUCTURAL_PATH_UNCHANGED / EXACT_PRIMITIVE_PASS / SAME_LAW_JACOBIAN_PASS / TC_ONLY_SOURCE_CLOSURE_NOT_PROMOTED`

## 0. Hard boundary

This execution keeps the current explicit structural path unchanged:

\[
P_\Phi(q)=P_{cr,\Phi}\frac{q}{q+q_0}+C_\Phi q(q+2q_0),
\]

with the same frozen source waveforms and the same full two-slope section interface

\[
\lambda_x=a_x+b_xz,\qquad \lambda_y=a_y+b_yz.
\]

The section equilibrium remains the four-vector `(Nx,Ny,Mx,My)`. The following are not changed:

- source waveform coefficients;
- structural explicit operator;
- NC CC law;
- locked TT law;
- Vecchio–Collins gamma physics and its `10/17` activation;
- bare EPP reinforcement law;
- root/event definition.

No spatial quadrature or material-point integration is introduced. Experimental `Pf` is comparison-only after the theoretical event is fixed.

```text
EXPLICIT_STRUCTURAL_PATH_CHANGED = FALSE
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_MATERIAL_POINTS = 0
Pf_IN_ROOT_SELECTION = 0
NC_CC_CHANGED = FALSE
NC_TT_CHANGED = FALSE
VC_GAMMA_CHANGED = FALSE
```

---

## 1. Source facts recovered

### 1.1 Foster/Nguyen

Nguyen, following Foster, gives

\[
\alpha_1=10,
\]

and states that `alpha2` varies from approximately `0.3` for lightly reinforced concrete to `0.7` for more heavily reinforced concrete. However, no deterministic transferable rule

\[
\alpha_2=\alpha_2(\rho,d_b,\text{bond})
\]

is supplied in the available Foster/Nguyen source chain. Nguyen's own Swartz calculations used `alpha2=0.3` for all 24 panels, despite the reinforcement ratio varying between 0.2%, 0.5%, 0.75% and 1.0%.

Therefore a direct interpolation of Foster `alpha2` from the Swartz failure loads is prohibited and is not source closure.

### 1.2 Swartz reinforcement geometry

A secondary source documenting the Swartz tests reports No.12 gage wire with diameter

\[
\boxed{d_b=2.7\ \mathrm{mm}}
\]

and yield stress 530 MPa. The locked panel registry gives

\[
\rho_1=0.0020,
\qquad
\rho_{14}=\rho_{21}=0.0075.
\]

At the present controlling source-wave sections `Nxy=Mxy=0`, so the principal tensile direction aligns with one orthogonal mesh family. For the Bentz bond parameter this gives

\[
\frac1m=\frac{4\rho}{d_b},
\qquad
m=\frac{d_b}{4\rho}.
\]

Hence

\[
\boxed{m_1=337.5\ \mathrm{mm}},
\qquad
\boxed{m_{14}=m_{21}=90.0\ \mathrm{mm}}.
\]

### 1.3 Bentz bond-dependent tension stiffening

The Bentz family expresses the postcrack average tensile stress by a bond parameter. The original form uses a denominator coefficient `3.6 m`. The Modified Bentz formulation used in VecTor2 uses

\[
c_t=3.6 t_d m,
\qquad t_d=0.6,
\]

with

\[
\frac1m=\sum_i\frac{4\rho_i}{d_{bi}}
\left|\cos(\theta-\alpha_i)\right|.
\]

This provides a source-based reinforcement/bond descriptor independent of Swartz `Pf`.

---

## 2. First projection — direct panel-specific Foster alpha2 target

To keep the existing finite Foster grammar, the Bentz retained stress at the Foster endpoint `alpha1 eps_cr = 10 eps_cr` was first used only as a source-to-source diagnostic target:

\[
\alpha_{2,B}
=
\frac{1}
{1+\sqrt{c_t\,10 f_t/E_0}}.
\]

Two source variants were checked:

- `B99`: `c_t=3.6m`;
- `B03`: `c_t=3.6(0.6)m`, with the result capped at the Foster stated upper range `0.7`.

The resulting targets are:

|Panel|B99 alpha2 target|B03 alpha2 target|
|---:|---:|---:|
|1|0.469631|0.533397|
|14|0.645031|0.700000|
|21|0.632191|0.689341|

This target is not fitted to any failure load.

### 2.1 Why direct insertion is rejected

Directly inserting these targets only in TC appears numerically attractive in preliminary calculations, especially for Panel21. It is nevertheless inadmissible while the locked TT law remains unchanged.

At the TC-to-TT boundary, simultaneous compression tends to zero, so the source TC crack front tends to

\[
f_{cr}^{TC}\to f_t.
\]

A direct TC residual with panel-specific `alpha2_B` tends to

\[
\sigma_t^{TC}\to\alpha_{2,B}f_t,
\]

whereas the locked TT scalar branch tends to

\[
\sigma_t^{TT}=0.3f_t.
\]

Thus for `alpha2_B != 0.3` a finite stress jump is created at the TC/TT boundary. This violates the current-map continuity and same-law tangent requirement. The apparently improved direct-target loads are therefore not promoted.

```text
DIRECT_TC_ALPHA2_BENTZ_TARGET = REJECTED_AS_PRODUCTION
REASON = FINITE_TC_TT_STRESS_JUMP_WHILE_TT_IS_LOCKED
```

---

## 3. Minimum continuity-preserving diagnostic

A TC-only reinforcement correction compatible with the locked TT branch must vanish as simultaneous compression vanishes. The already-locked NC-M6 crack front itself supplies a dimensionless source activation:

\[
\boxed{
w_{TC}=1-\frac{f_{cr}^{TC}}{f_t}
}
\]

so that

\[
w_{TC}=0
\quad\text{when}\quad p_0=0.
\]

The continuity-preserving effective Foster endpoint is then defined diagnostically as

\[
\boxed{
\alpha_2^{TC}
=0.3+w_{TC}(\alpha_{2,B}-0.3)
}
\]

or, equivalently, as a stress blend between the locked `alpha2=0.3` NC-M6 branch and the bond target.

This is explicitly a **project-derived source-anchored diagnostic**, not a newly claimed Foster or Bentz law.

### 3.1 Exact primitive remains finite

On each NC-M6 TC crack-front segment,

\[
f_{cr}^{TC}=F_0+B_f\sigma_c.
\]

Therefore `w_TC` is affine in the current compression stress. The blended Foster softening/residual stress expands into a finite combination of

\[
1,\quad \lambda_t,\quad \sigma_c,\quad
\sigma_c^2,\quad \sigma_c\lambda_t.
\]

The current compression branch is a rational Saenz function of affine `lambda_c(z)`. Consequently the required through-thickness resultants reduce to finite rational primitives. No thickness quadrature is required.

The unchanged gamma branch

\[
\gamma=\frac1{0.8+0.34\lambda_t}
\]

also remains rational in `z` when active and therefore has a finite exact primitive.

```text
EXACT_SECTION_PRIMITIVE = PASS
SAME_LAW_CROSS_COUPLED_JACOBIAN = PASS
```

### 3.2 Continuity check

At `p0=0`:

\[
f_{cr}^{TC}=f_t,
\qquad
w_{TC}=0,
\qquad
\alpha_2^{TC}=0.3.
\]

Direct evaluations at `1.1, 3, 9, 12` times the uniaxial cracking strain reproduce the locked `alpha2=0.3` tensile stress to floating-point roundoff. Therefore the TC-to-TT boundary stress is continuous without changing the TT branch.

### 3.3 Jacobian audit

For the smooth Panel1 and Panel21 terminal states, the analytic same-law section Jacobian was independently checked by centered directional finite differences. The diagnostic finite differences are not used by the formal solver.

Representative relative matrix errors are:

- Panel1: approximately `3e-8`;
- Panel21: approximately `1e-9` to `3e-9`.

Panel14 terminates exactly on a steel active-set kink, so a centered derivative is not meaningful there; its one-sided active-set audit is reported below.

---

## 4. Three-panel execution

### 4.1 B99 target: `c_t = 3.6 m`

|Panel|alpha2_B|u|q|theoretical event|P_event / kN|post-solution error vs Pf|
|---:|---:|---:|---:|---|---:|---:|
|1|0.469631|0.63222422|0.001077101|current-map section fold|**465.5091**|**-5.036%**|
|14|0.645031|0.74890405|0.000934928|lower y-rebar compression-yield active-set terminal|**770.7595**|**+7.623%**|
|21|0.632191|0.35603385|0.001441194|current-map section fold|**181.2290**|**-50.795%**|

### 4.2 Modified Bentz target: `c_t = 3.6(0.6)m`

|Panel|alpha2_B|u|q|theoretical event|P_event / kN|post-solution error vs Pf|
|---:|---:|---:|---:|---|---:|---:|
|1|0.533397|0.63229262|0.001080866|current-map section fold|**466.6620**|**-4.801%**|
|14|0.700000|0.74889155|0.000934926|lower y-rebar compression-yield active-set terminal|**770.7582**|**+7.623%**|
|21|0.689341|0.35606883|0.001443573|current-map section fold|**181.4247**|**-50.742%**|

For reference, the current NC-M6 `alpha2=0.3` results were:

- Panel1: 462.6313 kN;
- Panel14: 770.7674 kN;
- Panel21: 180.1593 kN.

Thus the continuity-preserving bond dependence changes Panel1 only modestly and leaves the severe Panel21 premature transverse-tension fold essentially intact.

---

## 5. Why Panel21 hardly moves

The result is not a numerical failure. It follows directly from the continuity constraint.

At the Panel21 B99 fold, representative TC states give approximately:

- tensile face: `w_TC=0.0536`, so `alpha2_eff=0.3178` even though the full Bentz target is `0.6322`;
- mid-plane: `w_TC=0.1645`, so `alpha2_eff=0.3547`.

For the modified-Bentz target the corresponding effective values are only about `0.3208` and `0.3641`.

The Panel21 early fold occurs in a weakly compressed TC state close to the TC/TT boundary. Because TT is locked at the `alpha2=0.3` postcrack branch, any continuous TC-only correction is forced back toward `0.3` precisely in the state that controls Panel21.

This explains why a direct `alpha2=0.63-0.69` insertion can apparently delay the fold, while the admissible continuity-preserving version cannot.

---

## 6. Panel14 active-set gate remains unchanged

At the Panel14 lower longitudinal rebar yield terminal, one-sided derivatives of the yield function with respect to the structural amplitude remain opposite in sign.

B99:

\[
\left.\frac{dh}{dq}\right|_{elastic}
\approx +4.48346\times10^6,
\qquad
\left.\frac{dh}{dq}\right|_{capped}
\approx -5.03387\times10^6.
\]

Modified Bentz:

\[
\left.\frac{dh}{dq}\right|_{elastic}
\approx +4.48386\times10^6,
\qquad
\left.\frac{dh}{dq}\right|_{capped}
\approx -5.03364\times10^6.
\]

The perfect-plastic capped continuation still points back across its own yield surface. Panel14 therefore remains a steel active-set diagnostic, not a clean NC tension-stiffening discriminator.

---

## 7. Main verdict

### A. The explicit structural path remains valid and unchanged

The source-wave explicit operator, full two-slope section kinematics, exact section primitives and same-law Jacobian all remain usable. No structural rewrite is required by this audit.

### B. Reinforcement/bond dependence is physically/source motivated

Foster explicitly distinguishes lightly and more heavily reinforced tension stiffening, and Bentz supplies a quantitative bond parameter depending on reinforcement ratio, bar diameter and direction. The missing mechanism is real.

### C. A direct TC-only strong reinforcement correction is incompatible with the locked TT law

If `alpha2_TC` remains above `0.3` as compression tends to zero, a finite TC/TT stress jump is unavoidable. Such a result cannot be promoted merely because its Panel21 load is closer to the test.

### D. The minimum continuous TC-only source-anchored correction is mathematically admissible but does not solve Panel21

The continuity-preserving blend passes the exact-primitive and same-law-Jacobian gates, but Panel21 remains near 181 kN, about 51% below the measured failure load.

Therefore the current task is **not source-closed as a TC-only modification under the simultaneous constraint `TT unchanged`**.

```text
NC_M6_TC_ONLY_REINFORCEMENT_DEPENDENT_TENSION = DIAGNOSTIC_PASS_PHYSICS_MOTIVATION
NC_M6_TC_ONLY_REINFORCEMENT_DEPENDENT_TENSION = FAIL_AS_PRODUCTION_CLOSURE
PANEL21_EARLY_FOLD_REMOVED = FALSE
DIRECT_ALPHA2_TARGET_ROOT_SELECTION_BY_Pf = PROHIBITED
```

---

## 8. Boundary for the next decision

No automatic next material change is authorized by this execution.

The evidence leaves two logically clean options:

1. retain NC-M6 with the existing universal `alpha2=0.3` and explicitly accept that Panel21 remains outside the current material capability; or
2. explicitly reopen the **postcrack tensile response across the TC/TT transition as one continuous material layer**, while still leaving the TT biaxial strength envelope, CC, VC gamma and the explicit structural path unchanged.

Option 2 is the only route by which the bond-dependent tension-stiffening source can remain finite at weak compression without being forced back to `alpha2=0.3` at the controlling Panel21 state. It is a material-layer decision, not a structural-path decision.

No such reopening is performed in this R01 execution.

---

## Reproduction

`semantic_v2/40_execution/rc/20260822_2205__NZSCCM__NC_M6_BOND_DEPENDENT_TC_TENSION_CONTINUITY_DIAGNOSTIC.py`
