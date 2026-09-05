# NZ-SCCM — 2026-09-05 对话后当前状态与下一执行入口 R01

## 0. 证据优先级

本目录中的 `DIALOGUE_VERBATIM_*` 文件为本节点原始对话证据；本文件只是状态整理，若与逐字原文冲突，以逐字原文为准。

## 1. 当前根本路线切换

对话节点之后，正式主线不再让 Airy / 截面力反演来产生全局应变和曲率。

当前上游运动学固定为：

- 端缩 `Delta` / `lambda=Delta/a` 是加载路径变量；
- `u(x,y), v(x,y), w(x,y)` 是结构位移场；
- Nguyen / Marguerre-von Karman 二阶运动学直接给 `epsilon_x^0, epsilon_y^0, gamma_xy^0`；
- Kirchhoff-Love 几何直接给 `kappa_x, kappa_y, kappa_xy`；
- `q` 是面外位移响应，由 current out-of-plane equilibrium 求得；
- 平均纵向应变由端缩与几何伸长直接给出，不能再由 Airy compatibility 或膜力平衡反求零阶轴向应变。

BH050 的关键运动学证据：

`q=0.00516361, q0=0.0025` 时，

`Q=q(q+2q0)=5.2480918e-5`，

`<0.5(w_y^2-w0_y^2)>=pi^2 Q/8=6.4746e-5`。

采用 FEM 端缩 `lambda=0.00187381` 仅作后验诊断时，

`eps_y_mean^kin=-0.00187381+0.000064746=-0.00180906`，

与 FEM UHPC 体积平均 `LE33=-0.00179690` 相差约 0.68%。

因此当前主线必须是：

`Delta -> q(Delta), compatible in-plane displacement/harmonics -> current material response -> P(Delta)`。

## 2. Airy 的当前唯一职责

Airy 只负责二维膜力平衡的表示和相关审计：

`Nx=F,yy`, `Ny=F,xx`, `Nxy=-F,xy`。

Airy 不再负责：

- 生成应变；
- 生成曲率；
- 决定零阶轴向缩短；
- 生成固定 nonlinear `P(q)`；
- 作为独立极限判据。

旧 `R4/J4`、独立 `kappa^R4`、冻结的 nonlinear `Kx/G/CA/Jx/Jy/P(q)` 均不得恢复为当前 nonlinear 主线。

## 3. 当前钢壳判断

同一 BH050 FEM 几何状态 `q=0.00516361` 下，compatible + Multiwave 得：

- upper steel `2.016 MN`；
- lower steel `2.134 MN`；
- total steel `4.150 MN`。

FEM 对应约：

- upper steel `2.174 MN`；
- lower steel `2.114 MN`；
- total steel `4.289 MN`。

总钢壳误差约 `-3.2%`。

因此钢壳目前不是第一矛盾；在新的 `Delta`-controlled kinematic branch 尚未重新跑通前，不优先重开 R02/R06/Multiwave。

纵向 PBL/web 钢必须单列。BH050 使用 `Aw=1332 mm^2`，其理想塑性轴力硬上界为 `Aw*fy=0.47286 MN`，无法解释此前约 2.41 MN 的总差额。

## 4. 当前 UHPC “超级脑洞”必须完整保留

当前 UHPC 主线不是简单的“几条折线”，而是：

1. 来源约束的一维压缩/拉伸曲线转为有限 PWL / hinge material spectrum；
2. M3 equivalent-uniaxial plane-stress Poisson closure：
   `e1*=eps1+(nu/E)sigma2`, `e2*=eps2+(nu/E)sigma1`；
3. 每个当前线性 branch 组合内部用显式 `2x2` 逆矩阵求 `sigma1,sigma2`，不使用材料 Newton；
4. current consistent tangent 同源显式给出，并包含主方向旋转处理；
5. 不在板面建立运行时 `CC/TC/CT/TT` 空间分区；
6. 材料非线性通过 positive-part / hinge 产生 Fourier stress spectrum；
7. Fourier-Bessel modal projection toy gate 已证明：二维四状态 coexistence 不要求显式空间分区；
8. interaction branches 仍可通过材料谱卷积表达，不要求空间区域几何；
9. V0 采用轻量 TC interaction：`K_TC` 约 `1.5~1.54 GPa`；第一版 `K_CC=0`, `K_TT=0`；
10. 当前诊断材料近似曾使用 6 段压缩 PWL + 17 段拉伸 PWL，压缩最大误差约 1.84%，拉伸约 3.38%；
11. 不把 smooth positive-part 代理升级为物理本构；
12. 最终目标仍是 `material spectrum -> spatial spectrum -> exact moments`，不是材料点网格或板级 surrogate。

## 5. 当前 BH050 已知关键输入

- `a=5000 mm`
- `b=2500 mm`
- `tc=42 mm`
- `ts=4 mm`
- `Aw=1332 mm^2`
- `A0g=6.25 mm=b/400`
- `Es=206000 MPa`
- `nu_s=0.30`
- `fy=355 MPa`
- `Ec=43400 MPa`
- `nu_c=0.20`
- `fc=141.1 MPa`
- `eps_c0=0.0035`
- initial global mode `m*=2`

已恢复的 UHPC 拉伸锚点：

- `(0,0)`
- `(0.00042, 9.767718 MPa)`
- `(0.0038, 10.734818 MPa)`
- `(0.0069, 10.347978 MPa)`
- `(0.00759, 0)`

## 6. 当前真正缺少的不是“材料/几何数据”，而是两个实现闭合项

### A. 新 `Delta`-controlled equilibrium branch 的完整显式实现

需要把现有位移运动学、current UHPC、当前 Multiwave、web 与 current out-of-plane virtual work 统一组装，直接求：

`lambda -> {u/v harmonic coefficients, q, local U_i} -> P`。

这里平均轴向应变必须由端缩运动学约束，不允许再由 Airy 零空间反求。

### B. 正式零空间数值积分要求下的完整 UHPC modal kernel

toy 层面的 positive-part / Fourier-Bessel 变换已经 PASS；但完整 `PWL + Poisson coupling + principal rotation + TC interaction` 的 production modal kernel 尚需整理为唯一闭式/特殊函数/递推解析算子，才能严格满足正式 `N_spatial_quadrature=0`。

这属于数学编译工作，不是缺失材料参数。

## 7. 目前不作为 blocker 的历史开放项

以下内容暂时不应抢在新 `Delta` branch 之前重开：

- Multiwave qU registration / phase；
- R06 中历史 `q -> eta q` 规则；
- mean-face steel harmonic upgrade；
- 更高 global basis 阶数；
- CC/TT 额外 UHPC interaction；
- 三轴 confinement current law。

只有新的 displacement-controlled branch 仍明显失配时，才按证据逐项重新打开。

## 8. 下一执行入口

下一次执行不再扫 `q`、不再反求 `e_y0`。

从：

`lambda=0, q=0`

开始，以端缩增量推进：

1. 由位移场直接形成 current strain/curvature；
2. UHPC 用完整 V0 material-spectrum operator；
3. steel 用当前已验证 Multiwave operator；
4. web 单列；
5. Airy 只检查/表示膜力平衡；
6. `Rq=0` 求 `q(lambda)`；
7. 反力输出 `P(lambda)=PU+Ps+ + Ps- + Pw`；
8. 最终稳定终点用与该 equilibrium 同源的 condensed current tangent singularity；`dP/dlambda=0` 只作路径 observable / limit-point audit，不恢复旧 J4。
