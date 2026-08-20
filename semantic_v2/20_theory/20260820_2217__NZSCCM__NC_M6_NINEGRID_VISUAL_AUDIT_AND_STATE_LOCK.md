# NZ-SCCM — NC-M6 九宫格曲线审计 + 当前状态锁定

时间：2026-08-20 22:17 +08:00

状态：`NC_M6_ARCHITECTURE_CANDIDATE_LOCKED / NINEGRID_VISUAL_AUDIT_COMPLETED / NO_CASE21_SOLVE / NO_T5_REFIT / NO_NEW_REPAIR_TERM`

## 0. 治理边界

本节点只做 NC-M6 材料函数的曲线可视化与状态固化。

明确不做：

- 不计算 Case21；
- 不重新拟合 T5；
- 不改变唯一参考 `NC-基准本构`；
- 不改变 CC/TC/CT/TT 冻结物理目标；
- 不恢复旧 NC-M4 的 `beta=1/(1+0.15 t^2)`；
- 不恢复 additive `Pi_i`；
- 不新增 C1/C2 sector-front 材料修复项；
- 不修改结构运动学或虚功场。

NC-M6 当前材料接口仍为：

\[
(\varepsilon_x,\varepsilon_y,\gamma_{xy})
\to(\varepsilon_1,\varepsilon_2,\theta)
\to(\bar\varepsilon_1,\bar\varepsilon_2)
\to(\lambda_1,\lambda_2)
\to(\sigma_1,\sigma_2)
\to(\sigma_x,\sigma_y,\tau_{xy}).
\]

其中 Poisson 只作一次显式代数消元：

\[
\bar\varepsilon_1=\frac{\varepsilon_1+\nu\varepsilon_2}{1-\nu^2},\qquad
\bar\varepsilon_2=\frac{\varepsilon_2+\nu\varepsilon_1}{1-\nu^2},
\]

不是新增材料自由度或第二状态网格。

## 1. 九宫格采用的材料尺度

为与此前 ordinary-concrete 曲线审计保持同一尺度，仅用一组已有材料参数作可视化归一化，不进行结构求解：

- `fc = 21.23 MPa`
- `E0 = 20321 MPa`
- `eps_c0 = 0.00209`
- `nu = 0.18`
- `ft = 0.1 fc = 2.123 MPa`

派生：

\[
\kappa=\frac{E_0\varepsilon_{c0}}{f_c}=2.00051295337,
\]

\[
\rho=\frac{f_t}{f_c}=0.1,
\qquad
x_{cr}=\frac{\rho}{\kappa}=0.04998717945.
\]

这些数值只给九宫格曲线提供实际材料尺度，不用于反标或 Case21 Pu。

## 2. 固定 NC 拉伸参考 T_NC

NC-M6 的物理定义仍使用固定 `T_NC(r)`；T5 只保留为以后解析编译候选，本节点不重新拟合。

固定 C2-regularized target：

\[
T_{NC}(r)=r,\qquad 0\le r\le0.7.
\]

在 `0.7<r<1.5`，令

\[
t=\frac{r-0.7}{0.8},
\]

由两端值、斜率以及与相邻线性段 C2 匹配的零二阶导数唯一得到 quintic bridge：

\[
T_{NC}=0.7+0.8t-1.94t^3+2.04777777778t^4-0.646666666667t^5.
\]

中段：

\[
T_{NC}(r)=1-\frac7{90}(r-1),\qquad1.5\le r\le9.
\]

在 `9<r<11`，令

\[
u=\frac{r-9}{2},
\]

C2 bridge 为

\[
T_{NC}=0.377777777778-0.155555555556u+0.155555555556u^3-0.0777777777778u^4.
\]

最后：

\[
T_{NC}=0.3,\qquad r\ge11.
\]

数值检查：

\[
T_{NC,\max}\approx0.97786211\quad(r\approx1.23539),
\]

因此全域保持

\[
0\le T_{NC}<1.
\]

## 3. 九宫格定义

### Panel 1 — 单轴压缩 primitive

\[
C(c)=\frac{\kappa c}{1+(\kappa-2)c+c^2}.
\]

展示 `|sigma|/fc=C(c)`，覆盖峰值与远端软化。

### Panel 2 — 单轴拉伸 T_NC

展示 `sigma_t/ft=T_NC(r)`，覆盖弹性、C2 峰值桥、tension-stiffening 下降与 residual 0.3。

### Panel 3 — primitive tangent

展示

\[
C'(c)/\kappa
\]

与

\[
T'_{NC}(r)
\]

的有限性、压缩峰值切线过零和拉伸 C2 过渡。

### Panel 4 — 自由单轴压缩物理路径

物理主应变取

\[
\varepsilon_t=\nu e,\qquad \varepsilon_c=-e.
\]

Poisson 消元严格给

\[
\lambda_t=0,
\qquad
\lambda_c=-e/\varepsilon_{c0},
\]

因此横向应力严格为零，轴向曲线严格退化为 `C(c)`。

### Panel 5 — TC 压缩响应

固定若干真实材料拉伸坐标 `r`，展示

\[
|s_c|=C\{c[1-T_{NC}(r)]\}.
\]

本图直接显示 NC-M6 不再使用旧 NC-M4 的独立 beta 函数；TC 削弱只来自固定 NC 基准 `c*=c(1-tau)`，并且只有真正材料拉伸 `lambda_t>0` 才会触发。

### Panel 6 — 自由单轴拉伸物理路径

物理应变取

\[
\varepsilon_t=e,\qquad\varepsilon_c=-\nu e,
\]

Poisson 消元严格给

\[
\lambda_t=e/\varepsilon_{c0},\qquad\lambda_c=0,
\]

横向应力严格为零，轴向曲线严格退化为 `T_NC`。

### Panel 7 — 等双压 CC

\[
h=1+a_{cc}c^2,
\qquad
|s|=C(ch).
\]

同时画出单轴 `C(c)` 作为对照。该冻结 CC target 通过等效压缩坐标改变峰值位置；本节点不重新解释或更改其物理身份。

### Panel 8 — 等双拉 TT

\[
tau^*=tau(1-a_t tau^8),
\qquad tau=T_{NC}(r).
\]

与单轴 `T_NC` 对照，显示双拉 interaction 始终有界。

### Panel 9 — finite sector-front one-sided tangent

以 CC→TC 边界 `lambda1=0` 为例展示 material-coordinate one-sided tangent：

\[
K_{21}^{CC,-}=a_{cc}c^2C'(c),
\]

\[
K_{21}^{TC,+}=\frac{c}{x_{cr}}C'(c).
\]

二者一般不相等，但对任意有限 `c` 都有限，且远端趋于零。本节点继续按 NC-M6 治理：sector-front tangent jump 不是材料物理 FAIL，不因此增加 C1/C2 修复项。

## 4. 曲线审计结论

1. `COMPRESSION_STRESS_CURVE = PASS`：单峰、有界、远端软化至 0。
2. `TENSION_STRESS_CURVE = PASS`：C2 reference 连续光滑、峰值小于 1、远端残余 0.3。
3. `PRIMITIVE_TANGENT_BOUNDEDNESS = PASS`。
4. `UNIAXIAL_COMPRESSION_DEGENERATION = PASS`：Poisson 横向膨胀不触发假 TC。
5. `UNIAXIAL_TENSION_DEGENERATION = PASS`。
6. `TC_CURVE = PASS_WITH_FROZEN_NC_TARGET`：旧 beta 已删除，不重新引入。
7. `CC_CURVE = PASS_WITH_FROZEN_NC_TARGET`。
8. `TT_CURVE = PASS_WITH_FROZEN_NC_TARGET`。
9. `FINITE_FRONT_STRESS_CONTINUITY = PASS`；`ONE_SIDED_TANGENT_FINITE = PASS`；不要求有限 sector front 的两侧 tangent 相等。
10. `FULL_DOMAIN_STRESS_BOUNDEDNESS = PASS`。
11. `VIRTUAL_WORK_INTERFACE = READY`。

## 5. 当前锁定状态

\[
\boxed{\texttt{NC_M6_ARCHITECTURE_CANDIDATE = LOCKED}}
\]

\[
\boxed{\texttt{NC_M6_NINEGRID_VISUAL_AUDIT = PASS}}
\]

当前材料主线：

`NC-基准本构 (frozen)`
`-> NC-M6 NC-M4-R12-style direct physical-principal current operator`
`-> explicit Poisson algebraic elimination`
`-> frozen CC/TC/CT/TT interactions`
`-> physical stress + exact consistent tangent`
`-> continuous virtual-work field`.

下一步允许进入连续结构虚功场；除非新的直接数学矛盾被证明，否则不再回到材料层增加修复项。
