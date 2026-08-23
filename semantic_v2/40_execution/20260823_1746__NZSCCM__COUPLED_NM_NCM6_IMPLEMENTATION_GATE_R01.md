# NZ-SCCM — Airy锁定下耦合 Nx–Mx / Ny–My 的 NC-M6 implementation gate R01

**Time:** 2026-08-23 17:46 +08:00  
**Status:** `IMPLEMENTATION_GATE = FAIL_PARTIAL / AIRY_LOCKED / NO_PRODUCTION_SWARTZ8_Pu / NO_CURRENT_STATE_CHANGE`

## 0. 本轮边界

本轮执行上一节点约定的 implementation gate：

1. 不修改 Airy 形函数、Airy 显式膜应力和 Marguerre–Airy `P_pb(q)`；
2. 只在原一维 `N_y-M_y` 终端截面层引入 `(N_x,M_x) <-> (N_y,M_y)` 耦合；
3. 使用当前仓库锁定的 `NC_M6_2D_TC_CRACK_FRONT` 候选材料映射；
4. 保留 affine-through-thickness、finite branch fronts、exact primitives、zero formal thickness quadrature；
5. 不以 `det J_sec=0` 作为板件 Pu；
6. 不使用试验 `Pf` 选根或调参。

当前 `RC_CURRENT_STATE_20260822.md` 明确锁定：Airy retained、current material 不进入 Airy compatibility、`NC_M6_2D_TC_CRACK_FRONT = RETAIN_AS_TERMINAL_MATERIAL_CANDIDATE`、exact section primitive retained。

---

# 1. 实现时发现并纠正一个重要坐标问题

历史 full-2D two-slope / NC-M6 代码中的 affine variables `lambda_x, lambda_y` **不是物理应变本身**。其物理应变定义为

\[
\boxed{\varepsilon_x=\varepsilon_0(\lambda_x-\nu\lambda_y)},
\qquad
\boxed{\varepsilon_y=\varepsilon_0(\lambda_y-\nu\lambda_x)}.
\]

因此，前一轮若直接写 `b_x:b_y = kappa_x:kappa_y`，在 NC-M6 的实际坐标中并不严格正确。

Airy 实际曲率要求的是物理应变斜率比

\[
\frac{b_x-\nu b_y}{b_y-\nu b_x}
= r
=\frac{\kappa_x}{\kappa_y}.
\]

故 material-coordinate slope ratio 应为

\[
\boxed{
\frac{b_x}{b_y}
=\frac{r+\nu}{1+\nu r}
}.
\]

更稳健的向量写法是：若 Airy 给出的物理曲率方向为

\[
\mathbf k=(\kappa_x,\kappa_y)^T,
\]

则材料坐标斜率方向可取

\[
\boxed{
\mathbf d_\lambda
=\begin{bmatrix}
\kappa_x+\nu\kappa_y\\
\nu\kappa_x+\kappa_y
\end{bmatrix}
}
\]

（公共比例因子可由终端条件消去）。

这一修正保证：

\[
\frac{b_x-\nu b_y}{b_y-\nu b_x}
=\frac{\kappa_x}{\kappa_y}
\]

达到机器精度。对 Case 4/8/14/21/23 的多处 `u` 检查，误差量级约 `1e-16`。

因此：

```text
INDEPENDENT_bx_by = FALSE
AIRY_PHYSICAL_CURVATURE_DIRECTION = EXACTLY_ENFORCED
POISSON_TRANSFORM_BETWEEN_LAMBDA_AND_PHYSICAL_STRAIN = REQUIRED
```

---

# 2. 原一维终端 T 按“物理压应变达到 eps0”原样保留

原 V1 的一维 RC N-M 容量以受压面

\[
|\varepsilon_c|=\varepsilon_0
\]

作为峰值压缩上升支终端参数化。

因此在本轮二维嵌入中，不改成新的经验判据，而保留为有限候选：

\[
\boxed{
\frac{\varepsilon_j(z_c)}{\varepsilon_0}=-1,
\qquad j\in\{x,y\},\quad z_c=\pm h.
}
\]

其中

\[
\frac{\varepsilon_x}{\varepsilon_0}=\lambda_x-\nu\lambda_y,
\qquad
\frac{\varepsilon_y}{\varepsilon_0}=\lambda_y-\nu\lambda_x.
\]

给定 `(a_x,a_y)`、Airy 曲率方向和一个有限 terminal candidate `(j,z_c)` 后，公共 slope scale 唯一消去；因此截面仍只保留两个内层未知量 `(a_x,a_y)`。

---

# 3. NC-M6 全部当前 branch 的厚度 exact closure

现有 NC-M6 已有下列 scalar exact primitives：

- `C_RESIDUAL`；
- `C_POSTPEAK`；
- `C_SAENZ`；
- `T_ELASTIC`；
- `T_FOSTER_SOFTEN`；
- `T_RESIDUAL`。

TC crack-front 还包含：

- source A/B cracking envelope front；
- crack-to-softening front；
- residual-tension front；
- `lambda_t = 10/17` compression-softening onset。

历史 `20260822_2130__...EXACT_SECTION.py` 在 `lambda_t>10/17` 时会停止，因为尚未装入 exact gamma primitive。本轮补做了这个纯数学闭合，不修改材料公式。

源式为

\[
\gamma(\lambda_t)=\frac{1}{0.8+0.34\lambda_t},
\qquad
\sigma_c^{eff}=\gamma(\lambda_t)\sigma_c(\lambda_c).
\]

由于

\[
\lambda_t=a_t+b_tz,\qquad
\lambda_c=a_c+b_cz,
\]

且每个固定 compression branch 上 `sigma_c(lambda_c)` 为常数、一次函数或 Saenz 有理函数，所以

\[
\frac{\sigma_c(a_c+b_cz)}{0.8+0.34(a_t+b_tz)}
\]

始终是有限有理函数。

对 Saenz branch，其分母至多为“一次 × 二次”，即三次多项式；采用有限部分分式/留数原函数即可精确评价 `N` 与 `M`，不需要厚度数值积分。

### 数值审计（仅验证 exact primitive，不进入正式 operator）

用高精度 adaptive quadrature 对若干 gamma-active TC branch 做离线审计：

- gamma-active force primitive 最大差约 `1.2e-12`；
- gamma-active moment primitive 最大差约 `3.7e-10`；
- 随机完整 section resultants（含 phase-volume correction + bars）与直接数值积分最大绝对差约 `4.4e-7`。

正式 operator 本身仍为：

```text
FORMAL_THICKNESS_QUADRATURE = 0
FORMAL_MATERIAL_POINTS = 0
FINITE_BRANCH_FRONTS = YES
EXACT_BRANCH_PRIMITIVES = YES
```

因此“缺 gamma primitive”不再是本轮失败原因。

---

# 4. 一维退化门：严格 PASS

关闭 transverse material channel，使

\[
\lambda_x(z)\equiv0,
\]

并只保留 y 向 `N_y,M_y` 时，本轮二维 section implementation 的 y-resultants 与同一 NC-M6 scalar branch 的一维 phase-corrected section 逐项相同。

对 Cases 4、14、21，在多组小应变、压缩、弯曲和拉伸 affine states 上检查：

\[
\boxed{\Delta N_y=0},\qquad
\boxed{\Delta M_y=0}
\]

达到双精度逐项零误差。

故：

```text
1D_DEGENERATION = EXACT_PASS
OLD_SCALAR_NM_SECTION_IS_RECOVERED = YES
```

---

# 5. 内层 2×2 膜力求解确实存在连续 admissible branch，但并非无限延伸

固定 `(q,u)` 和 terminal candidate 后，内层只解

\[
N_x^c(a_x,a_y)=N_x^d(q,u),
\qquad
N_y^c(a_x,a_y)=N_y^d(q,u).
\]

在 `u=0.5`、y-direction physical compression-face terminal 的 continuation audit 中：

- Cases 4/5/6/8/21/23 均可从 `q=0.0002` 连续跟踪至少到 `q=0.0015`；
- Case 9 可连续跟踪到约 `q=0.00147`；
- Case 14 可连续跟踪到约 `q=0.00085`，再往上该 terminal branch 不再给出精确 `Nx,Ny` 根。

这说明内层并不是“求不出来”；它形成有限连续 capacity branch。branch 终止可以是物理容量边界的一部分，不能自动当作数值失败。

---

# 6. 真正的 common-set gate：Case 14 无法同时闭合 Mx 与 My

在内层 `Nx,Ny` 平衡后，要求同一 section state 同时满足

\[
M_x^c=M_x^d,
\qquad
M_y^c=M_y^d.
\]

本轮对保留的共同验证集

\[
\{4,5,6,8,9,14,21,23\}
\]

使用相同 Airy demand、相同 NC-M6、相同 terminal enumeration、无 Pf 选根进行 exploratory root search。

Cases 4/5/6/8/9/21/23 均能找到至少一个 coupled resultant root；Case 14 在 y/x terminal、两面 terminal 与多组初值下均未找到精确 simultaneous root。

这不是单独围绕 Case21 的判断，而是 common 8-panel gate。

### Case 14 的近闭合点

在 y-terminal branch 上，最接近 simultaneous moment closure 的状态约为

\[
q\approx0.00083917,\qquad u\approx0.50,
\]

对应

\[
P\approx694.798\ \mathrm{kN}.
\]

膜力已经闭合到约 `1e-6`：

\[
N_x^c\approx N_x^d\approx3.6339\ \mathrm{N/mm},
\]

\[
N_y^c\approx N_y^d\approx-568.598\ \mathrm{N/mm}.
\]

但两方向弯矩出现相反残差：

\[
M_x^c\approx403.191,
\qquad
M_x^d\approx390.235,
\]

\[
M_y^c\approx143.488,
\qquad
M_y^d\approx156.344.
\]

即

\[
\boxed{R_{Mx}\approx+12.956},
\qquad
\boxed{R_{My}\approx-12.856}.
\]

两者不能同时降到 0；outer solver 稳定停留在这个相反符号的 mismatch 附近。

该状态的两面 material coordinates 约为：

- lower face: `(lambda_x,lambda_y)≈(-0.158,-1.028)`；
- upper face: `(lambda_x,lambda_y)≈(+0.670,-0.688)`。

lower face 为 CC，upper face 为 TC；且上表面 `lambda_t≈0.670>10/17`，所以本状态明确调用了本轮新增的 exact gamma-active primitive。

因此 Case 14 的 failure **不是因为 gamma-active branch 没有解析闭合**。

---

# 7. 一个不能忽略的材料身份问题

当前 repo 锁定名称虽然叫 `NC_M6_2D_TC_CRACK_FRONT`，但其实际 `point_map` 在同号区域采用：

```text
CC: sigma_x = scalar(lambda_x), sigma_y = scalar(lambda_y)
TT: sigma_x = scalar(lambda_x), sigma_y = scalar(lambda_y)
```

即同号 CC/TT 当前仍是两个 scalar branches；真正显式二维 coupling 主要装在 TC crack-front / compression-softening 部分。

因此，本轮已经证明：

- exact integration infrastructure 可以承载真正的 coupled `Nx-Mx / Ny-My`；
- Airy curvature / Zhou stiffness coupling 可以严格施加；
- 1D degeneration 正确；
- 但当前冻结的 **M6-TC candidate 本身并不是四象限都具有完整二维相互作用的 operator**。

Case 14 近闭合状态一面处于 CC、一面处于 TC，所以当前 `Mx/My` mismatch 与“CC side 仍为 separable scalar map”在力学上高度相关，但本轮不能把相关性升级为因果证明，也不能违反 `NC_CC_REOPEN=NO` 私自修改 CC。

---

# 8. exploratory roots（非生产 Pu）

为确认问题不是 Case21-specific，本轮使用同一实现对 common set 做了 exploratory root search。下列值只表明“存在 simultaneous coupled resultant root”，不是正式 Pu，也未进行完整 root-exhaustion / location proof：

| Case | exploratory coupled root P / kN | Pf 仅后验对照 / kN | 后验差值 |
|---:|---:|---:|---:|
|4|590.672|534.231|+10.56%|
|5|570.502|623.641|-8.52%|
|6|639.833|691.698|-7.50%|
|8|502.658|455.053|+10.46%|
|9|557.868|625.865|-10.86%|
|14|**NO EXACT COUPLED ROOT**|716.164|—|
|21|552.655|368.313|+50.05%|
|23|455.748|346.961|+31.35%|

`Pf` 未进入任何 coefficient、initial guess acceptance、root selection 或 material law；这里只在 root 固定之后显示误差。

这些值不能用于调参。它们只说明：即使 integration 和 slope constraint 都闭合，当前 M6 terminal material candidate 仍不足以让 common-set coupled N-M 成为 production theory。

---

# 9. Gate verdict

```text
AIRY_SHAPE_FUNCTION = LOCKED_PASS
AIRY_EXPLICIT_MEMBRANE_DEMAND = LOCKED_PASS
POISSON_CORRECTED_SLOPE_CONSTRAINT = PASS
INDEPENDENT_bx_by = PROHIBITED_PASS
FINITE_BRANCH_FRONTS = PASS
GAMMA_ACTIVE_TC_EXACT_PRIMITIVE = PASS
ZERO_FORMAL_THICKNESS_QUADRATURE = PASS
ONE_DIMENSIONAL_DEGENERATION = EXACT_PASS
INNER_2x2_CONTINUOUS_CAPACITY_BRANCH = PASS_WITH_FINITE_ENDPOINTS
COMMON_8_SIMULTANEOUS_Mx_My_CLOSURE = FAIL_CASE14
CURRENT_M6_AS_FULL_2D_TERMINAL_OPERATOR = NOT_PROVEN
FORMAL_SWARTZ8_Pu = NOT_STARTED
IMPLEMENTATION_GATE = FAIL_PARTIAL
```

---

# 10. 下一步边界

本轮失败不允许通过以下方式修复：

- 不改 Airy；
- 不加入经验 transverse coefficient；
- 不调 Case14；
- 不恢复独立 `b_x,b_y`；
- 不用 `det Jsec`；
- 不用 Pf 选根。

唯一合理的下一步是先做 **material-identity audit**：确认本项目已经冻结/认可的 NC 二维 operator 中，哪一个具有 CC/TC/TT 全域二维 coupling，同时又满足当前“不要重新开发材料”的治理边界；若已有这样的 frozen operator，则仅替换 terminal material map，完全复用本轮 Airy、slope constraint、exact integration 和 root system，再重新跑同一个 common-8 gate。

如果不存在已有的 full-domain frozen operator，则本轮应停在这里，不能以 Case14 mismatch 为理由现场发明一个 CC coupling coefficient。
