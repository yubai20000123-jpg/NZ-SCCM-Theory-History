# NZ-SCCM — BH050 单一路径显式 current-moment 完整计算账本 R01

**Execution time:** 2026-08-27 16:23 +08:00  
**Parent theory:** `semantic_v2/20_theory/20260827_1710__NZSCCM__SINGLE_EXPLICIT_BH_CURRENT_MOMENT_HARMONIC_CLOSURE_R01.md`  
**R02 active-set completion:** `semantic_v2/20_theory/20260827_1623__NZSCCM__R02_NONNEGATIVE_AMPLITUDE_ACTIVESET_COMPLETION_R01.md`  
**Reusable solver:** `semantic_v2/40_execution/steel_shell/20260827_1623__NZSCCM__BH_EXPLICIT_CURRENT_MOMENT_SOLVER_R01.py`  
**Status:** `BH050 EXECUTED / TWO-UNKNOWN ENDPOINT ROOT CLOSED / PARAMETER PROVENANCE SAVED / COMPARATOR OPENED ONLY AFTER ROOT / PREDICTION GATE FAIL`

---

# 0. 本账本保存什么

本文件不是只保存一个 `Pu`。为以后把完全相同的方法应用到 BH032/BH020/BH010/BH005 或同拓扑新试件，下面逐项保存：

1. 每一个参数第一次进入计算的阶段；
2. 它是原始输入、几何派生量、材料派生量还是求解内部量；
3. 计算公式/求解方法；
4. 是否需要求根、解析原函数、三次凝聚或 R06 极值；
5. BH050 实际数值；
6. 最终根及所有残差；
7. 求根之后才打开的 Abaqus comparator；
8. 当前方法还没有解决的预测偏差，不用 comparator 反调任何系数。

正式空间积分仍为零：

```text
FORMAL_SPATIAL_QUADRATURE = 0
MATERIAL_POINTS = 0
EFFECTIVE_WIDTH = 0
COMPARATOR_IN_ROOT_SELECTION = 0
```

R06 的 GL+LL 局部应力场是连续解析谐波场；本次数值执行用确定性的驻值优化定位连续最大 Mises，应力-resultant 本身没有空间数值积分。该数值极值后端已经对 20260827 13:35 BH050 状态逐项回归到原 `eta/U/stress`；正式有限代数 resultant certificate 仍可在不改变本理论/根的情况下替换此执行后端。

---

# 1. 参数引入时间总表

这里的“时间”指**计算链中的首次引入阶段**，不是为了得到结果后回填。

| Stage | 第一次引入的量 | BH050 值 | 引入/求解方法 | 后续用途 |
|---|---|---:|---|---|
| S00 RAW | `B` | 2500 mm | 原始几何 | 所有尺度 |
| S00 RAW | `a_phys` | 5000 mm | 原始几何 | 全局半波选择 |
| S00 RAW | `ts` | 4 mm | 原始几何 | steel face / ABD / R02 |
| S00 RAW | `tc` | 42 mm | 原始几何 | UHPC / web / zf |
| S00 RAW | `Aw` | 1332 mm² | 9 个 longitudinal webs 净面积 | `rho_w` |
| S00 RAW | `q0` | 0.0025 | 全局无应力缺陷 | Airy + qU |
| S00 RAW | `Es,nu_s,fy` | 206000 MPa, 0.30, 355 MPa | steel material | ABD/R02/R06/web |
| S00 RAW | `Ec,nu_c,fc,epsc0` | 43400 MPa, 0.20, 141.1 MPa, 0.0035 | UHPC frozen material | ABD + UHPC N-M |
| S00 RAW | `fct,eps_t0,mt` | 4.51313398 MPa, 0.001, 0.4418 | frozen UHPC tension branch | x-direction tension part |
| S10 GEOM | `rho_w` | 0.0126857142857 | `Aw/(B tc)` | core/web phase assembly |
| S10 GEOM | `zf` | 23 mm | `tc/2+ts/2` | steel eccentric moment |
| S20 ABD | `A11` | 3,685,652.010989 N/mm | phase plane-stress sum | Airy |
| S20 ABD | `A22` | 3,795,408.810989 N/mm | `A11+rho_w tc Es` | Airy |
| S20 ABD | `A12` | 918,229.303297 N/mm | phase plane-stress sum | Airy |
| S20 ABD | `A66` | 1,383,711.353846 N/mm | phase plane-stress sum | audit |
| S20 ABD | `Delta_A` | 1.314541106331431e13 | `A11 A22-A12²` | Airy |
| S20 ABD | `Dx` | 1.236003299828e9 N mm | initial full-composite | elastic regression |
| S20 ABD | `Dy` | 1.252137549428e9 N mm | + web longitudinal term | elastic regression |
| S20 ABD | `Dmu` | 3.432434438484e8 N mm | initial composite | elastic regression |
| S20 ABD | `D66^0` | 4.463799279897e8 N mm | initial composite shear/twist | retained twist harmonic |
| S20 MODE | `ell` | 2500 mm | BH `a_phys=2B,m*=2` | global mode |
| S20 MODE | `alpha=beta` | 0.001256637061436 mm⁻¹ | `pi/B` | Airy + curvature |
| S20 AIRY | `Kx` | 4.272925966136e6 N/mm | closed form | `Nx^d` |
| S20 AIRY | `G` | 4.400171479083e6 N/mm | closed form | `Ny^d` |
| S20 AIRY | `Km` | 1.095680521170e-6 | closed form | membrane hardening |
| S20 AIRY | `C` | 1.084137180652e10 N = 10841.3718065 MN | `B³ Km/beta²` | load equation |
| S20 REG | elastic `Pcr` | 19.581877236731 MN | full initial ABD | elastic degeneration gate only |
| S30 R02 | `Lx` | 562.5 mm | `0.225B` | local PBL |
| S30 R02 | `Ly` | 555.555555556 mm | `2B/9` | local PBL |
| S30 R02 | `A0` | 0.3515625 mm | `Lx/1600` | local imperfection |
| S30 R02 | `cx` | 4.678923567924e-5 mm⁻² | `3kx²/8` | LL mean |
| S30 R02 | `cy` | 4.796627738929e-5 mm⁻² | `3ky²/8` | LL mean |
| S30 R02 | `Kb_local` | 0.038545572914 | exact R02 local bending coefficient | cubic energy |
| S30 R02 | `sigma_cr_local` | 100.449667484 MPa | Yun elastic local buckling | selects R06 local-buckling-first |
| S40 qU TOP | `hx=hy` | 1.530251331862e-6 mm⁻² | exact rational harmonic | GL mean |
| S40 qU TOP | `KA` | 2.658832895996e-9 mm⁻⁴ | exact harmonic | LL Airy energy |
| S40 qU TOP | `KdDelta` | 6.028529628699e-11 mm⁻⁴ | exact harmonic | LL×GL energy |
| S40 qU TOP | `KDeltaDelta` | 1.461159027099e-12 mm⁻⁴ | exact harmonic | GL energy |
| S40 qU BOT | `hx=hy` | 1.435668541336e-6 mm⁻² | exact rational harmonic | GL mean |
| S40 qU BOT | `|hgamma|` | 1.867817909316e-7 mm⁻² | exact rational harmonic | GL shear mean |
| S40 qU BOT | `KdDelta` | 5.655914265997e-11 mm⁻⁴ | exact harmonic | cubic |
| S40 qU BOT | `KDeltaDelta` | 1.297175736660e-12 mm⁻⁴ | exact harmonic | cubic |
| S50 UHPC | `S0,S1` | analytic primitives | rational-log compression + incomplete-gamma tension | exact thickness N-M |
| S60 WEB | `Ny^w,My^w` | state-dependent | affine strain + ideal-EP exact piecewise primitives | section assembly |
| S70 R02 | `U+`,`U-` | state-dependent | constrained minimum of augmented cubic energy over `U>=0`; candidates = positive cubic roots + `U=0` | steel trial state |
| S80 R06 | `eta+`,`eta-` | state-dependent | first continuous local-Mises contact along `q(eta)=eta q, eps(eta)=eta eps` | whole-width steel resultant |
| S90 CURV | `kappa` | state-dependent | `pi²q/B` | UHPC/web/face common curvature |
| S90 LOAD | `P(q,Ax,Ay)` | state-dependent | current `Mx+My` + retained elastic twist + Airy membrane hardening | global axial load |
| S100 LIMIT | `Ay(q)` | state-dependent | y-bottom UHPC endpoint `Ay-21kappa=-0.0035` | eliminate one unknown |
| S100 ROOT | `(q,Ax)` | solved simultaneously | `Rx=0,Ry=0`, multi-seed least-squares, comparator blind | final root |

这个表就是以后换试件时必须保持的“参数什么时候出现”的顺序。任何后续试件都不得提前把后验结果塞进 S00–S100 的某个参数。

---

# 2. S20：全局 Airy 与 common curvature

代表完整半波：

\[
\psi=\sin\alpha x\sin\beta y,
\qquad \alpha=\beta=\pi/B.
\]

\[
Q_q=q(q+2q_0).
\]

在 BH 控制反节点 `s=1`：

\[
N_x^d=K_xQ_q,
\]

\[
N_y^d=-P/B+GQ_q.
\]

共同曲率只由同一个 q 给出：

\[
\boxed{\kappa_x=\kappa_y=\kappa=\pi^2q/B.}
\]

没有独立 `kappa_x,kappa_y` 求解。

---

# 3. S50：UHPC N-M 的求法

对 `i=x,y`：

\[
\varepsilon_i(z)=A_i+\kappa z.
\]

使用已冻结 UHPC stress primitives：

\[
S_0'(\varepsilon)=\sigma_U(\varepsilon),
\qquad
S_1'(\varepsilon)=\varepsilon\sigma_U(\varepsilon).
\]

于是对于 `kappa != 0`：

\[
N_i^U=(1-\rho_w)
\frac{S_0(\varepsilon_+)-S_0(\varepsilon_-)}{\kappa},
\]

\[
M_i^U=(1-\rho_w)
\frac{S_1(\varepsilon_+)-S_1(\varepsilon_-)
-A_i[S_0(\varepsilon_+)-S_0(\varepsilon_-)]}{\kappa^2}.
\]

所以 UHPC 厚度方向没有任何数值积分。

---

# 4. S70：qU-R02 及本次发现的 active-set 缺口

每个钢面：

\[
d=U^2-A_0^2,
\]

\[
\Delta=B[(q_0+q)U-q_0A_0].
\]

\[
m_x=e_x-c_xd-h_x\Delta,
\quad
m_y=e_y-c_yd-h_y\Delta,
\quad
m_\gamma=-h_\gamma\Delta.
\]

局部幅值内部驻值仍为一般三次：

\[
B_3U^3+B_2U^2+B_1U+B_0=0.
\]

严格按旧实现只取 `U>=0` 的**内部驻值根**时，BH050 上钢面正根在

\[
q=0.0080758736\ldots
\]

降到 `U=0`，随后内部三次只剩负实根。若把这里直接报成 `no root`，就会人为制造一个“理论不能计算”的区域。

因此本次把既有 `U>=0` 定义严格补成约束最小化：

\[
\boxed{U^*=\arg\min_{U\ge0}\Pi_{R02}^{aug}}.
\]

候选 = 正内部实根 + 边界 `U=0`。

相接点同时满足：

\[
U_+=0,
\qquad B_{0,+}=0.
\]

该切换点的全局状态为：

```text
q = 0.00807587362235
P = 10.70094787085 MN
Ax = +0.000225425602
Ay = -0.001379289303
TOP max local VM = 228.230 MPa < fy
BOTTOM eta = 0.6592441485
```

所以这里不是钢材破坏点；只是上钢面局部幅值的 active-set 从内部正根转到 `U=0`。本次不会把它误当 Pu。

---

# 5. S80：R06 的执行回归

BH050：

\[
\sigma_{cr,local}=100.4497\ \text{MPa}<355\ \text{MPa},
\]

所以两面均使用 local-buckling-first R06 概念。

为了确认当前执行后端没有改变 13:35 的 R06，先在旧候选状态回归。得到：

```text
TOP    eta = 0.8239874660, U = 0.2911147334 mm
        mean stress = (+207.434813, -199.558150, 0) MPa
BOTTOM eta = 0.3909289472, U = 2.5951383592 mm
        mean stress = (-27.501152, -219.356561, -0.628480) MPa
```

与 13:35 账本逐项一致，所以新的计算结果不是由 R06 后端漂移造成。

---

# 6. S90：current-moment 显式轴力

总截面：

\[
N_x=N_x^U+N_{x,+}^s+N_{x,-}^s,
\]

\[
N_y=N_y^U+N_y^w+N_{y,+}^s+N_{y,-}^s,
\]

\[
M_x=M_x^U+z_fN_{x,+}^s-z_fN_{x,-}^s,
\]

\[
M_y=M_y^U+M_y^w+z_fN_{y,+}^s-z_fN_{y,-}^s.
\]

BH current-moment load：

\[
\boxed{
P=\frac{M_x+M_y+4BqD_{66}^0\alpha^2}{q+q_0}
+Cq(q+2q_0).
}
\]

如果全部材料回到初始弹性，该式严格退化回

\[
P=P_{cr}\frac{q}{q+q_0}+Cq(q+2q_0).
\]

本次没有 fitted degradation factor。

---

# 7. S100：BH050 两未知量终端系统

按 y-bottom UHPC first compression-peak candidate：

\[
A_y-21\kappa=-0.0035,
\]

所以

\[
\boxed{A_y(q)=-0.0035+21\pi^2q/2500.}
\]

最终只剩：

\[
(q,A_x).
\]

两个方程：

\[
R_x=N_x^{sec}-K_xQ_q=0,
\]

\[
R_y=N_y^{sec}-[-P/B+GQ_q]=0.
\]

求解方式：

```text
unknown count = 2
method = deterministic multi-seed nonlinear least-squares / simultaneous root
seeds = theory-domain seeds only
load stepping = NO
FEM/test seed = NO
comparator in residual = NO
```

根先冻结，然后才打开 comparator。

---

# 8. BH050 最终 blind root

得到：

\[
\boxed{q_u=0.0199244069774625}
\]

\[
\boxed{A_x=+0.003611017619024}
\]

\[
\boxed{A_y=-0.001848173475732}
\]

\[
\boxed{\kappa=7.865840591754\times10^{-5}\ \mathrm{mm^{-1}}}
\]

UHPC 四个端点应变：

```text
x top    = +0.00526284414329
x bottom = +0.00195919109476
y top    = -0.000196346951463
y bottom = -0.003500000000000   ACTIVE
```

最终轴力：

\[
\boxed{P_u=15.1330065506692\ \mathrm{MN}}
\]

其中 current-moment load 的两部分为：

```text
Mx+My+twist numerator = 218618.630104 N
bending/current-moment contribution /(q+q0) = 9.74913763935 MN
Airy membrane-hardening C Qq                    = 5.38386891132 MN
---------------------------------------------------------------
P                                                   15.13300655067 MN
```

同一 q 若仍错误使用 frozen-elastic `Pcr q/(q+q0)`，则会给出约 `22.78265 MN`；因此 current-moment feedback 在本根处确实发生了大幅降载，并非没有作用。

---

# 9. 最终 phase resultants

## UHPC

```text
Nx_U = +122.247722591 N/mm
Mx_U = -291.566386529 N
Ny_U = -3269.852167918 N/mm
My_U = +20003.452669375 N
```

## web

```text
Ny_w = -150.412980518 N/mm
My_w = +562.729812345 N
```

## TOP steel face

```text
U+       = 0.000000000 mm       [R02 active-set boundary]
R06 eta+ = 0.324627367985
mean physical stress = (+394.750086, +113.901046, 0) MPa
local max Mises      = 355.000000 MPa
N+ = (+1579.000344, +455.604182, 0) N/mm
```

## BOTTOM steel face

```text
U-       = 1.490147421 mm
R06 eta- = 0.383109059566
mean physical stress = (+105.176045, -225.849693, -0.526140) MPa
local max Mises      = 355.000000 MPa
N- = (+420.704180, -903.398772, -2.104559) N/mm
```

总截面：

```text
Nx_sec = +2121.952247371 N/mm
Ny_sec = -3868.059738600 N/mm
Mx_sec = +26349.245390192 N
My_sec = +51823.250436861 N
retained twist numerator term = 140446.134277045 N
```

---

# 10. 方程残差

Airy demand：

```text
Nx_d = +2121.952247372 N/mm
Ny_d = -3868.059738585 N/mm
```

最终残差：

\[
\boxed{R_x=-7.75\times10^{-10}\ \mathrm{N/mm}}
\]

\[
\boxed{R_y=-1.55\times10^{-8}\ \mathrm{N/mm}}
\]

以及 active UHPC endpoint：

\[
\boxed{\varepsilon_y(-21)=-0.003500000000000.}
\]

数值求根本身闭合。

---

# 11. 纵向荷载分担

最终：

```text
UHPC       = -3269.852168 N/mm   -> 84.534686 %
steel faces=  -447.794590 N/mm   -> 11.576724 %
web        =  -150.412981 N/mm   ->  3.888590 %
TOTAL      = -3868.059739 N/mm
```

这部分非常重要，因为它说明即使方程残差完全闭合，结果的内部力学状态仍然可能不对。

---

# 12. 只有现在才打开 BH050 equal-contract Abaqus comparator

已接受 comparator：

\[
P_{FE}=12.591227\ \mathrm{MN}.
\]

因此：

\[
\boxed{\frac{15.13300655}{12.591227}-1=+20.1869\%.}
\]

accepted FEM longitudinal load shares 约：

```text
UHPC / steel faces / web = 55.80% / 40.61% / 3.58%
```

本计算：

```text
84.53% / 11.58% / 3.89%
```

所以当前结论不能写成“BH050 已经预测正确”。

---

# 13. 本次执行真正解决了什么、没有解决什么

## 已解决

```text
BH050 explicit equations are executable = YES
new 2D material integration required = NO
common curvature = retained
qU exact geometry = retained
UHPC exact N-M = retained
web exact integration = retained
R06 continuous field = retained
artificial no-positive-R02-root gap = removed by U>=0 active-set completion
parameter introduction order = fully persisted
root residual closure = PASS
```

## 仍然失败

```text
BH050 Pu prediction = +20.19% HIGH
BH050 internal load share = FAIL HARD
PRODUCTION_ACCEPTANCE = NO
```

也就是说：

> `1710 current-moment single-harmonic closure + existing UHPC/R02/R06` 现在已经**可以一直显式计算到终端，不再因求解器缺口中断**；但它并没有把 BH050 的物理分担和 Pu 预测修好。

这次不能再把“能算通”和“算对了”混为一谈。

---

# 14. 对后续其他试件的固定复用顺序

以后每个 BH-family 新试件严格按以下顺序建立，不再临时插入新步骤：

```text
01 raw geometry/material
02 rho_w, zf
03 initial full-composite A/D
04 m*, representative halfwave
05 Kx,G,C,D66^0
06 actual local PBL registration
07 exact qU coefficients
08 common kappa(q)
09 UHPC exact N-M
10 web exact affine EP
11 upper/lower R02 constrained-energy condensation
12 R06 first-local-Mises projection
13 assemble Nx,Ny,Mx,My
14 explicit current-moment P
15 enumerate finite terminal candidates
16 solve comparator-blind roots
17 freeze all roots and residuals
18 only then compare FEM/test
```

每个量必须在它所在 stage 首次出现；不允许从第 18 步把任何试验/FEM信息反向写回第 1–16 步。

---

# 15. 当前冻结状态

```text
METHOD = SINGLE_HARMONIC_EXPLICIT_CURRENT_MOMENT_R01
BH050_CALCULABILITY = PASS
BH050_ROOT = 15.1330065506692 MN
ROOT_RESIDUAL_GATE = PASS
R02_ACTIVESET_COMPLETENESS = PASS
R06_1335_REGRESSION = PASS
FORMAL_SPATIAL_QUADRATURE = 0
MATERIAL_POINTS = 0
COMPARATOR_IN_ROOT_SELECTION = 0
BH050_COMPARATOR_ERROR = +20.1869%
BH050_INTERNAL_SHARE_GATE = FAIL
BH050_PRODUCTION_GATE = FAIL
NO_POST_COMPARISON_RETUNING_PERFORMED = TRUE
```

本节点的作用是把**完整可复算的方法和失败位置一起冻结**。后续若改理论，只允许针对已经暴露的具体力学缺口作单一、显式、可退化的修改；不得重新回到 full-current 2D integration、D15、材料点或 comparator 拟合。