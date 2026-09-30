# UCFT M7 theory self-audit

更新时间：2026-09-30 18:15 +08:00

M7 只做 M0–M6 理论内部自检，不使用 FEM/试验目标，不拟合九试件。

## 1. 总裁决

检查：
- zero-load；
- linear elastic；
- q->0；
- A->0；
- TOP/BOTTOM parity；
- dimensional consistency；
- current virtual-work / Jacobian；
- branch continuity。

M7 发现两项需要修正但不改变总体路线的问题：

1. raw odd-odd S_y compatible mode 对 uniform axial traction 有非零 loading-edge generalized work；
2. equilibrium generalized load P_eq 与 PBL/web reaction-corrected P_report 必须分离。

两项均已精确修正。最终：
\[
\boxed{\mathrm{M7}=PASS}.
\]

## 2. zero-load

取
\[
q=0,\quad P_{eq}=0,\quad A^+=A^-=0,\quad \xi=0.
\]
则
\[
Q(0)=0,\quad \kappa^g=0,
\]
且
\[
q_0A+qA_0+qA=0,\qquad A^2+2A_0A=0.
\]
因此 loading-induced UHPC/steel strain 与 curvature 全为零。数值代入检查最大 loading-induced local strain = 0。PASS。

## 3. linear elastic / q->0

M6 退化回 M1 Chen-Ji/Airy zero-shear solution。C1 H-block 在独立正定 benchmark 中最小特征值
\[
1.748459\times10^7>0,
\]
故 Hx=Hy=0 为唯一线弹性解。

线弹性 imperfect branch：
\[
P(q)=P_{cr}\frac q{q+q_0}+C_A(q^2+2q_0q).
\]
q->0 时
\[
P/q\to P_{cr}/q_0+2C_Aq_0.
\]
q=1e-8 的 benchmark 相对误差 3.999787e-6；Bx,By=O(q)。PASS。

## 4. A->0

当 A0=0,A=0 时 local extra finite strain 与 local curvature 严格消失，退化为 global-only state。

但 R_A 在 q>0 时不必恒为零，因为 B_A 在 A=0 仍含 global-local interaction，current global stress 可以驱动 local response。这是 q->A 从属机制，不是理论错误。PASS。

## 5. TOP/BOTTOM parity

同一 local geometry 下：
- global-local contribution 对 TOP/BOTTOM 为奇；
- local-local A² contribution 为偶；
- local curvature derivative 反对称。

数值恒等检查最大误差
\[
5.421011\times10^{-20}.
\]
PASS。

## 6. raw S-family boundary-work correction

raw S_y basis：
\[
B_{S_y}^{raw}
=
[0,\sin kX\sin lY,-k/(lr)\cos kX\cos lY]^T
\]
对应
\[
v_{S_y}^{raw}
=
-\frac{a_h}{l\pi}S_y\sin kX\cos lY.
\]

loading-edge mean displacement coefficient：
\[
\boxed{
c_{kl}
=
\frac{[1-(-1)^k][1-(-1)^l]}{kl\pi^2}.
}
\]

qA S-family 全部为 odd-odd pair，因此
\[
c_{kl}=4/(kl\pi^2)\neq0.
\]
本轮候选最大 c_kl=0.05789782，不能忽略。

raw residual 应含
\[
+P_{eq}a_hc_{kl}.
\]

由于 Ey 已存在，采用 exact traction-orthogonal basis：
\[
\boxed{
\widetilde B_{S_y}
=
B_{S_y}^{raw}
-c_{kl}B_{E_y}.
}
\]
即
\[
\widetilde B_{S_y}
=
[0,\sin kX\sin lY-c_{kl},-k/(lr)\cos kX\cos lY]^T.
\]

其 loading-edge mean displacement = 0，并有
\[
G_{\widetilde S_y}
=
G_{S_y}^{raw}-c_{kl}G_{E_y}.
\]
所以 root set、compatible subspace、M3 spectrum 与 structural variables 全部不变。

数值 edge-work correction 残差 7.500001e-11。已修正。

## 7. virtual work / Jacobian

baseline external potential derivative同时恢复：
\[
\partial\Phi_{ext}/\partial E_y=P_{eq}a_h,
\]
\[
\partial\Phi_{ext}/\partial q=-P_{eq}a_hr^2C_q',
\]
以及 raw S_y generalized work。有限差分最大相对误差 4.262074e-10。

另用 nonlinear conservative surrogate 检查 M6 的 full residual/Jacobian，包括 qA、A²、epsilon_qA、epsilon_AA 与一对 corrected S modes。

解析 Jacobian vs residual finite difference：
\[
3.862825\times10^{-6}
\]
最大 scaled relative error。

physics-shaped full Newton vs exact Schur：
\[
\max|\Delta \xi_{full}-\Delta\xi_{Schur}|=4.054916\times10^{-17},
\]
\[
\max|\Delta z_{full}-\Delta z_{Schur}|=2.273737\times10^{-13}.
\]

PASS。

## 8. dimensional consistency / scaling

\[
[q]=1,\quad [A]=L,\quad [\xi]=1,\quad [P_{eq}]=F.
\]
\[
[G_\xi]=FL,\quad [R_q]=FL,\quad [R_A]=F.
\]

所以 full/condensed Jacobian 是 mixed-unit matrix。raw condition number 随单位改变，不可直接解释为 branch singularity。

以后定义
\[
\widehat J=S_F^{-1}JS_x
\]
并只保存 scaled condition/singular values。

单位转换 benchmark 中 dimensionless cond=4.0，单位改变前后 dimensionless matrix 最大差
\[
4.440892\times10^{-16}.
\]

## 9. branch continuity

Steel production polynomial 必须满足
\[
P_s(\epsilon_y)=f_y=E_s\epsilon_y.
\]
tangent 可以跳变。

UHPC production branches 必须满足 finite-stress continuity：
\[
P_c(0)=P_{t1}(0)=0,
\]
\[
P_{t1}(e_{tp})=P_{t2}(e_{tp})=f_t,
\]
若 e>=e_tu 后设零应力：
\[
P_{t2}(e_{tu})=0,
\]
若 e<=e_z 后设零应力：
\[
P_c(e_z)=0.
\]

tangent continuity 不作为必要条件；active topology switch 用 event localization / semismooth Newton。

Dynamic C/S/B enrichment 只扩充 inner space，新变量从 0 初始化并在同一 q,P_eq,A+,A- state 重求 G=0，不重置 structural branch。

## 10. P_eq 与 P_report

M6 equilibrium unknown 改记：
\[
\boxed{P_{eq}}.
\]

PBL/web report correction：
\[
\boxed{
P_{report}
=
\chi_wP_c+P_s^++P_s^-.
}
\]

M8 起最终项目输出记号定义：
\[
\boxed{P(q)\equiv P_{report}(q)}.
\]

Schur 第一分量给 dP_eq/dq，不再直接作为最终 Pu 条件。

最终：
\[
\frac{dP_{report}}{dq}
=
\chi_w\frac{dP_c}{dq}
+\frac{dP_s^+}{dq}
+\frac{dP_s^-}{dq},
\]
各 constituent derivative 由同一 xi_q,z_q chain rule 得到。

因此：
\[
\boxed{
P_u=\max_qP_{report}(q)
}
\]
或 regular q branch 上
\[
dP_{report}/dq=0.
\]

## 11. M7 后的唯一 NEXT_ACTION

进入 M8 准备/执行起点：先从现有 Project/Library 恢复并冻结九试件正式材料与几何输入。

特别需要恢复而不是重新拟合：
- UHPC e_tp,e_tu,Pt1,Pt2；
- Q355 production equivalent polynomial Ps；
- 九试件 geometry/local-wave inputs。

只要项目资料中已经存在，直接读取并运行 connected q-path；不得向用户重复索要。

M8 每件必须保存 q、P_eq、P_report、Pc、Ps+/Ps-、A+/A-、inner state、active regions、plastic regions、residuals、scaled Jacobian diagnostics、dP_report/dq 和 derived Delta。
