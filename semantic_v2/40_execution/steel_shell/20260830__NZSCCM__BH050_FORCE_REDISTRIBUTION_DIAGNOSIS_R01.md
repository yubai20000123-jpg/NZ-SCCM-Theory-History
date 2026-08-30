# NZ-SCCM — BH050 受力分配问题机理诊断 R01

**Date:** 2026-08-30  
**Branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Status:** `DIAGNOSTIC INTERPRETATION / NO CALIBRATION / PRODUCTION MAIN UNCHANGED`

## 1. Question

BH050 中出现的理论/FEM constituent force split 与 deformation mechanism 不一致，究竟主要来自：

- Airy 不能考虑 nonlinear stiffness；
- current section / R4 bridge；
- local R02/R06；
- 还是其他结构耦合缺失？

## 2. Main conclusion

最准确的说法不是 “Airy 理论不能考虑非线性刚度”。

Airy stress-function method 本身可以和 current/tangent stiffness、nonlinear constitutive response 联立。当前限制来自本项目当前架构：

\[
\boxed{
\text{initial full-composite elastic Airy demand}
\rightarrow
\text{downstream current nonlinear section}
}
\]

是一个主要单向耦合链。

Global Airy coefficients

\[
P_{cr},C,K_x,G,J_x,J_y
\]

由 initial full-composite A/D 生成；当 BH050 中 steel face 因局部屈曲/屈服显著降刚度后，current constituent tangent stiffness 并没有反向进入 global Airy PDE 去重新生成 membrane redistribution 和 bending demand。

因此 primary suspect 是：

\[
\boxed{
\text{FROZEN INITIAL-STIFFNESS AIRY DEMAND}
+
\text{DOWNSTREAM CURRENT-SECTION RESULTANT MATCHING}
}
\]

而不是 Airy 数学本身的缺陷。

## 3. Why BH050 amplifies the issue

已有诊断量表明，从 BH032 到 BH050：

- steel local-buckling ratio 约 1.203 -> 1.880；
- local-wave amplitude 约 11.32 -> 15.95 mm；
- UHPC peak compression magnitude 约 0.00515362 -> 0.00281273；
- total-load theory/FEM error 从约 -0.45% 变为 +6.08%。

这些现象共同说明 BH050 已更深进入 local-steel degradation + constituent redistribution regime。

在该阶段，真实结构应发生：

```text
steel face local stiffness loss
    -> face membrane/bending tangent changes
    -> steel/UHPC/web load redistribution
    -> effective composite A/D changes
    -> global membrane stress pattern and curvature demand change
```

当前模型却主要执行：

```text
initial A/D
    -> frozen Airy demand pattern
    -> current section adjusts eps0/kappa to match that demand
```

因此 downstream current section 可以找到一个 resultant-equilibrium state，但该 state 不一定对应真实结构在 current stiffness 下重新分配后的同一 kinematic state。

## 4. Deeper compatibility issue in R4

Current R4 state：

\[
\mathbf x=(\varepsilon_T^0,\kappa_T,\varepsilon_L^0,\kappa_L)^T.
\]

R4：

\[
\mathbf S(\mathbf x)=\mathbf D^A(q).
\]

其中 section curvatures are independent unknowns，而 global Airy q 同时来自一个 global deformation mode。此前 compatibility audit 已证明：

1. frozen-A Airy compatibility；
2. current nonlinear section N-M；
3. exact one-state geometric/constitutive compatibility；

不能在当前架构下无条件同时满足。

因此 R4 当前是 **force/resultant compatibility bridge**，不是 exact deformation compatibility closure。

这对 total P 可能不非常敏感，却可以明显改变 constituent split，因为独立 \(\kappa_T,\kappa_L\) 可以通过 section state 去满足 frozen resultants，而不强制等于 current global q 对应的真实 common curvature。

Hence secondary major suspect：

\[
\boxed{\text{R4 independent-section compatibility relaxation}.}
\]

## 5. Local steel q-U / GL coupling

Old R02 local operator already contains LL terms：

\[
d=U^2-A_0^2,
\]

but originally lacks exact GL coupling：

\[
\Delta=s_fb[qU+q_0(U-A_0)].
\]

Exact total von Karman geometry requires GL membrane and GL Airy compatibility terms. Their coefficients depend on actual PBL-cell global registration.

For BH050, where U is large, omitted/incompletely activated GL can directly distort：

- local amplitude equilibrium；
- steel-face full-width mean resultant；
- R06 event location；
- load transferred from steel face to UHPC/web.

因此 third suspect：

\[
\boxed{\text{incomplete local GL(qU) coupling in production R02/R06 path}.}
\]

This can be amplified with increasing local amplitude and is more plausible for BH050 than for low-B/H cases.

## 6. R06 contribution

R06 radial projection is a current-state active-set/resultant rule. Once active, the exact work-conjugacy/tangent symmetry with q-U generalized coordinates is not currently claimed as proven.

Potential consequence：

- projected local Mises boundary is internally admissible；
- full-width mean resultant is returned；
- but the derivative of that returned resultant with respect to global/local generalized deformation may not coincide with a globally conservative tangent.

This can affect redistribution after local buckling/yielding. It is a likely secondary contributor, but current evidence does not justify calling it the primary cause before the frozen-Airy/R4 mismatch is quantified.

## 7. What is probably NOT the first suspect

### 7.1 “Airy mathematics cannot do nonlinear stiffness”

False as a general statement. Current Airy front is frozen by model choice.

### 7.2 UHPC scalar N-M law alone

Current discrepancy has a strong geometry/local-steel/BH dependence. Material backend may affect magnitude, but no evidence currently shows UHPC N-M itself is the root architecture error.

### 7.3 Single global mode alone

Existing BH032/BH050 N=1 asymptotic audit did not justify immediate promotion to higher mode. Higher-order modes remain an optional audit, not the primary explanation.

### 7.4 FEM/test calibration

Forbidden for causal identification/root selection. FEM may be used only after theoretical states are frozen as a post-check of force shares and deformation fields.

## 8. Ranked causal hypothesis

Current priority ranking：

1. **Frozen initial-stiffness Airy demand lacks current tangent-stiffness feedback** — PRIMARY.
2. **R4 resultant matching does not enforce exact q-common-curvature/current-section kinematic identity** — PRIMARY/COUPLED.
3. **Exact local GL(qU) coupling absent or incomplete in active production R02/R06** — IMPORTANT, likely grows with BH050 local amplitude.
4. **R06 projected-resultant tangent/work consistency** — SECONDARY, post-event contributor.
5. **Material-law details / higher global mode** — do not promote without separate evidence.

## 9. Clean diagnostic decomposition

Without changing material parameters or using FEM to choose results, perform:

### D1 — baseline

Run current frozen-Airy R4/J4 and record at BH050 terminal:

- Airy demand vector;
- each constituent N/M share;
- current tangent/secant stiffness of upper steel, lower steel, UHPC, web;
- R06 states.

### D2 — stiffness mismatch audit only

At same blind state, compare current section tangent stiffness matrix with the initial A/D weights that generated Airy demand. Do not change root yet.

This measures how far current load-sharing stiffness has drifted from the frozen Airy stiffness basis.

### D3 — kinematic mismatch audit

Compute global q-derived common curvature \(\kappa^g(q)\) and compare with R4-solved \(\kappa_T,\kappa_L\). Treat mismatch as diagnostic residual only; do not force a new equation in the same run.

### D4 — local GL activation audit

Using exact registered PBL-cell phase, add GL(qU) augmentation only to R02 and recompute steel-face local equilibrium/resultants at the same gross state. Quantify delta in steel force share and R06 event.

### D5 — post-check against FEM

Only after D1-D4 are frozen, compare FEM constituent axial-force shares, local-wave amplitudes, gross curvature/deflection and contact/PBL response.

If D2/D3 mismatch grows sharply from BH032 to BH050, frozen-Airy/R4 architecture is confirmed as principal cause. If D4 alone removes most steel-share mismatch, local qU coupling is dominant. If neither explains it, then open R06 tangent/work and FEM boundary/contact geometry audit.

## 10. Governance

No change to `main`. No trial/test calibration. No new material mechanism. No effective width. No spatial quadrature. This file freezes a causal diagnosis and the next discriminating audit, not a new production theory.
