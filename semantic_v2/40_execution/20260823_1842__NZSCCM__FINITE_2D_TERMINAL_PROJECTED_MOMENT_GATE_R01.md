# NZ-SCCM — Airy锁定下有限二维终端容量 projected-moment gate R01

**Time:** 2026-08-23 18:42 +08:00  
**Status:** `ARCHITECTURE_GATE = PASS_DIAGNOSTIC / PRODUCTION_Pu = NOT_FROZEN / AIRY_UNCHANGED / NO_FULL_DOMAIN_CURRENT_MATERIAL`

## 0. 本轮目的

执行当前新分支最后一个结构化问题：

> Airy 已给出真实二维变形/曲率方向；材料二维化只发生在有限控制截面的厚度方向；如何把 `(Nx,Mx)` 与 `(Ny,My)` 合成一个不过约束、且严格服从单一 Airy 形函数的有限终端容量系统？

本轮不修改 Airy/Marguerre 显式后屈曲 `P_pb(q)`，不把 current material 放回全板 Airy compatibility，不建立全域 CC/TC/TT 空间分区，不采用 `det Jsec`，不使用试验 `Pf` 选根。

---

## 1. 关键纠正：单一 Airy 弯曲模态只有一个弯曲广义自由度

在代表半波控制位置，Airy 形函数给出曲率向量

\[
\boldsymbol\kappa_A(q,s,u)
=
\begin{bmatrix}\kappa_x\\\kappa_y\end{bmatrix}
=
q\,\widehat{\boldsymbol\kappa}(s,u).
\]

定义单位曲率方向

\[
\mathbf d
=\frac{\widehat{\boldsymbol\kappa}}
{\|\widehat{\boldsymbol\kappa}\|}
=\begin{bmatrix}d_x\\d_y\end{bmatrix}.
\]

由于形函数锁定，`d_x:d_y` 不是自由变量。此时材料终端截面只允许沿这一条曲率射线弯曲。于是与该唯一弯曲广义坐标功共轭的弯矩不是 `Mx` 和 `My` 两个独立标量，而是

\[
\boxed{M_\parallel=d_xM_x+d_yM_y}.
\]

与之正交的

\[
M_\perp=d_yM_x-d_xM_y
\]

在单一锁定模态内是对“禁止正交曲率”的反力；它不是额外独立的 Galerkin 平衡方程。只有在以后引入第二个独立弯曲模态/曲率自由度时，`M_perp` 才必须获得自己的平衡方程。

因此，上一节点强制同时要求

\[
M_x^u=M_x^d,\qquad M_y^u=M_y^d
\]

对单一 Airy bending DOF 属于多施加了一个独立弯曲条件；Case14 的 `+/-` 近等幅 moment residual 正是这一过约束的典型信号。

---

## 2. 有限二维终端截面族

在固定候选控制位置 `(s,u)`，Airy 只规定曲率方向，不再引入两个独立斜率。写物理应变：

\[
\boxed{\varepsilon_x(z)=\varepsilon_x^0+\lambda d_x z},
\]
\[
\boxed{\varepsilon_y(z)=\varepsilon_y^0+\lambda d_y z}.
\]

若该控制位置存在 `gamma_xy/kappa_xy`，按同一 Airy 形函数增加其固定方向项；对当前单正弦半波中心 `Nxy=Mxy=0`，可先用上述二维法向系统。

未知量只为

\[
\boxed{(\varepsilon_x^0,\varepsilon_y^0,\lambda,q)}.
\]

材料只在这一条厚度线 `z in [-h,h]` 上评价。二维 current law 产生

\[
\sigma_x(z),\sigma_y(z)
\]

及钢筋层应力，从而得到有限截面结果量

\[
N_x^u,N_y^u,M_x^u,M_y^u.
\]

厚度应变仍是 affine；CC/TC/TT/TCX 等 branch fronts 仍是有限标量 roots，故可继续使用 existing exact-section finite-front primitives。没有全板 `(x,y)` 材料状态划分。

---

## 3. 终端条件沿用原 V1，不新增经验参数

当前 V1 RC `N-M` 容量采用压缩控制面达到上升支峰值应变的参数化。二维有限终端中仍保留同一语义：

\[
\boxed{T_j^{\pm}=\varepsilon_j(\pm h)+\varepsilon_0=0},
\qquad j\in\{x,y\}.
\]

四个候选只是有限 active-set candidates。Admissibility 要求被选 candidate 确实是当前最压缩的控制面，且其他面/方向没有先超过 `-eps0`。

---

## 4. 最小有限二维终端方程：4×4

Airy/Marguerre 结构侧仍显式给出

\[
N_x^d(q,s,u),\quad N_y^d(q,s,u),
\]

周思铭刚度 + 同一个 Airy 曲率给出

\[
M_x^d(q,s,u),\quad M_y^d(q,s,u).
\]

定义 demand projected moment

\[
\boxed{M_\parallel^d=d_xM_x^d+d_yM_y^d}.
\]

材料 section 给

\[
\boxed{M_\parallel^u=d_xM_x^u+d_yM_y^u}.
\]

固定 `(s,u)` 和一个 terminal candidate 后，完整系统为

\[
\boxed{R_{Nx}=N_x^u-N_x^d=0},
\]
\[
\boxed{R_{Ny}=N_y^u-N_y^d=0},
\]
\[
\boxed{R_{M\parallel}=M_\parallel^u-M_\parallel^d=0},
\]
\[
\boxed{T_j^{\pm}=0}.
\]

正好四方程、四未知：

\[
\boxed{(\varepsilon_x^0,\varepsilon_y^0,\lambda,q)}.
\]

因此不需要：

- 独立 `bx,by`；
- 任意 4D capacity surface；
- `F_parallel + F_perp` 两个弯矩平衡；
- full-domain current material；
- `det Jsec`。

---

## 5. 周思铭耦合仍完整保留

对单正弦半波中心，

\[
\kappa_x:\kappa_y=\alpha^2:\beta^2.
\]

令 `d` 为其单位方向。周思铭正交板弯矩

\[
\begin{bmatrix}M_x^d\\M_y^d\end{bmatrix}
=
\begin{bmatrix}D_x&D_\mu\\D_\mu&D_y\end{bmatrix}
\begin{bmatrix}\kappa_x\\\kappa_y\end{bmatrix}.
\]

所以

\[
\boxed{M_\parallel^d
=\mathbf d^T\mathbf D\boldsymbol\kappa_A}.
\]

两向 bending 贡献没有被删除，而是按唯一 admissible Airy 曲率方向做 work-conjugate 合成。`Mx/My` 仍可全部输出审计；只是 `M_perp` 不再被误当成第二独立 bending equilibrium equation。

---

## 6. 一维退化

关闭 transverse material/action channel，并令

\[
\mathbf d\to(0,1)^T,
\]

则

\[
M_\parallel\to M_y.
\]

`R_Nx=0` 只负责横向 plane-stress/Poisson condensation；`T` 消去 curvature scale；剩余

\[
N_y^u=N_y^d,\qquad M_y^u=M_y^d
\]

即回到原 V1 的加载方向 `Ny-My` terminal contact。故 projected-moment 架构不是新的经验 interaction formula，而是单一 Airy bending DOF 的二维 extension。

---

## 7. 共同 8 板快速数值 topology diagnostic

为验证该 4×4 是否至少具有共同可计算根，本轮对核心分析集

\[
\{4,5,6,8,9,14,21,23\}
\]

使用同一规则作快速 diagnostic：

- frozen single-halfwave Airy demand；
- 已冻结 representative halfwave lengths；
- corrected reinforcement mapping `rho_direction = p/2`；
- current NC-M6/TC point map；
- `s=1`、纵向半波中心；
- 四个 `T_j^+/-` 候选全部求根；
- 仅保留 candidate 确实为全截面最先达到 `-eps0` 的 admissible root；
- `Pf` 仅在求根完成后比较。

**重要：** 为快速检查 root topology，本轮数值实现对厚度材料积分采用高阶 Gauss 作为离线 diagnostic。它不是 formal operator，不改变项目 `N_formal_thickness_quadrature=0`；若该架构晋级，正式版必须换回 existing finite-front exact primitives。

共同 admissible candidate 均为 `y, z=-h`，八板均获得正根：

| Case | q | diagnostic P / kN | Pf / kN | post-check error |
|---:|---:|---:|---:|---:|
| 4 | 0.00138783 | 470.64 | 534.23 | -11.90% |
| 5 | 0.00155337 | 460.63 | 623.64 | -26.14% |
| 6 | 0.00202180 | 512.37 | 691.70 | -25.93% |
| 8 | 0.00109019 | 437.05 | 455.05 | -3.96% |
| 9 | 0.00098544 | 464.11 | 625.86 | -25.84% |
| 14 | 0.00084054 | 695.65 | 716.16 | -2.86% |
| 21 | 0.00418577 | 280.08 | 368.31 | -23.96% |
| 23 | 0.00244639 | 298.07 | 346.96 | -14.09% |

8板 mean signed = `-16.84%`, MAE = `16.84%`, RMSE = `19.24%`。

对比旧 1D baseline 的共同8板 MAE `14.29%`、RMSE `16.66%`，**预测统计没有改善**，因此这些数值不得晋级为 production Pu。

但 topology 结果非常关键：上一轮 full `Mx=...` + `My=...` 同时匹配时 Case14 无根；改为唯一 Airy bending DOF 的 projected-moment 后，Case14 与其余七板一样获得 admissible root。故此前 Case14 “二维闭合失败”不能继续作为反对 finite 2D terminal architecture 的证据。

---

## 8. 当前判定

```text
AIRY_SHAPE_AND_Ppb = UNCHANGED
FULL_DOMAIN_CURRENT_MATERIAL = NO
TERMINAL_MATERIAL_DIMENSION = THICKNESS_ONLY
AIRY_CURVATURE_DIRECTION = LOCKED
INDEPENDENT_bx_by = NO
Nx_EQUILIBRIUM = YES
Ny_EQUILIBRIUM = YES
INDEPENDENT_Mx_AND_My_EQUILIBRIUM = NO
BENDING_EQUILIBRIUM = ONE WORK-CONJUGATE M_parallel
M_perp = REACTION_TO_FROZEN_ORTHOGONAL_CURVATURE
TERMINAL_T = ORIGINAL_V1_PEAK_COMPRESSION_SEMANTICS
FINITE_TERMINAL_SYSTEM = 4x4
COMMON_8_ROOT_TOPOLOGY = PASS_DIAGNOSTIC
COMMON_8_PREDICTION_ACCURACY = NOT_IMPROVED
PRODUCTION_PROMOTION = NO
```

## 9. 下一门

如果继续，应只做两件事，不再改结构架构：

1. 把本轮 4×4 中的 diagnostic thickness Gauss 全部换成 existing exact finite-front section primitives，证明 formal `N_thickness_quadrature=0`；
2. 对每块板执行完整有限 location/terminal-candidate root family 与 admissibility audit，再判断为何 Cases 5/6/9/21/23 仍偏低。

在这两门之前，不得用试验值调整 material parameter，也不得重新引入 `M_perp=0` 或 independent `Mx/My` capacity checks。
