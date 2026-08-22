# NZ-SCCM — UHPC Zhang 单轴压缩 backbone + Liu 2024 CC 连续 source-min 容量门禁

**Date:** 2026-08-22 12:40 +08:00  
**Status:** `MATERIAL_ONLY / G6_EXPLICIT_PRESERVED / STRUCTURAL_PU_RERUN_NOT_AUTHORIZED`

## 0. Scope

本文件继续 11:51 七门禁材料重组与 12:05 NC-TC Appendix-B 修正。只处理 UHPC：

1. 冻结一个不再依赖胡文旭的单轴压缩 backbone；
2. 处理 Liu 2024 literal Eq.(4) CC 两段在 `f1/f2=0.5` 处不连续的问题；
3. 证明上述选择不要求材料点、加载历史或数值厚度积分；
4. 保持结构主线和既有 Pu 表冻结。

```text
STRUCTURAL_BACKBONE_CHANGED = FALSE
STRUCTURAL_PU_RERUN = NOT_AUTHORIZED
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_material_points = 0
LOAD_PATH_TRACKING = 0
HISTORY_STATE_MACHINE = OFF_MAINLINE
```

---

# 1. UHPC uniaxial compression backbone: Zhang 2023

当前生产候选正式选用项目 D16 已登记的 Zhang 2023 显式全过程压缩关系，而不再以胡文旭早期单轴曲线为默认生产 backbone。

材料标量：

\[
f_c=141.1\ \mathrm{MPa},
\qquad
E_c=43.4\ \mathrm{GPa},
\qquad
\varepsilon_{c0}=0.0035,
\qquad
\nu=0.20,
\qquad
V_f=0.02.
\]

其中 `fc=141.1 MPa` 为用户强制保留；`Ec, eps_c0, nu` 是此前材料级复审后保留值，不是由 T120/T360/BH 或任何结构 Pu 反标。

令

\[
x=\frac{|\varepsilon_c|}{\varepsilon_{c0}},
\qquad
\kappa_U=\frac{E_c\varepsilon_{c0}}{f_c}=1.07654146,
\]

\[
r=\frac{E_c}{E_c-f_c/\varepsilon_{c0}}
=\frac{\kappa_U}{\kappa_U-1}
\approx14.0648.
\]

## 1.1 Ascending branch

\[
\boxed{
g_a(x)=\frac{r x}{r-1+x^r},\qquad 0\le x\le1.}
\]

\[
\sigma_c=f_c g_a(x).
\]

同源导数：

\[
\boxed{
g_a'(x)=
\frac{r(r-1)(1-x^r)}{(r-1+x^r)^2}.}
\]

因此：

\[
g_a(0)=0,
\quad
g_a'(0)=\frac{r}{r-1}=\kappa_U,
\quad
g_a(1)=1,
\quad
g_a'(1)=0.
\]

物理初始切线严格为

\[
\frac{d\sigma_c}{d\varepsilon_c}\bigg|_0=E_c.
\]

## 1.2 Descending branch under zero confinement

Zhang 2023：

\[
\sigma=f_{cr}+\frac{f_{cc}-f_{cr}}{1+n(x-1)^2},
\qquad
n=\frac{2}{1+100V_f}.
\]

无围压时：

\[
f_{cc}=f_c,
\qquad
f_{cr}/f_c=9V_f=0.18,
\qquad
n=\frac23.
\]

因此

\[
\boxed{
g_d(x)=0.18+\frac{0.82}{1+\frac23(x-1)^2},\qquad x\ge1.}
\]

同源导数：

\[
\boxed{
g_d'(x)=
-\frac{2n(1-0.18)(x-1)}{[1+n(x-1)^2]^2}.}
\]

在峰值：

\[
g_d(1)=1,
\qquad
g_d'(1)=0.
\]

故 ascending/descending 在峰值 **stress C1 连续**。

全域：

\[
0.18<g_d(x)\le1,
\qquad
\lim_{x\to\infty}g_d(x)=0.18.
\]

没有 pole，没有负残余，没有人为平台跳变。

## 1.3 G6: finite direct analytic thickness primitives

即使后续 1D section capacity 需要对 affine through-thickness strain 直接积分，也不需要 Gauss/material points。

Ascending branch 定义

\[
A=r-1,
\]

\[
I_m(x)=
\int\frac{x^m}{A+x^r}\,dx
=
\frac{x^{m+1}}{(m+1)A}
{}_2F_1\left(
1,\frac{m+1}{r};1+\frac{m+1}{r};-\frac{x^r}{A}
\right).
\]

则

\[
\int g_a(x)dx=rI_1(x),
\qquad
\int xg_a(x)dx=rI_2(x).
\]

对 affine `x(z)=x_0+kz`，轴力和一阶弯矩只需要这些端点 primitive 的有限差。

Descending branch 的 primitives 仅含 elementary `atan` 和 `log`：

\[
\int g_d(x)dx
=0.18x+
\frac{0.82}{\sqrt n}
\arctan[\sqrt n(x-1)],
\]

\[
\int xg_d(x)dx
=0.09x^2+0.82
\left[
\frac{1}{2n}\ln(1+n(x-1)^2)
+
\frac1{\sqrt n}\arctan(\sqrt n(x-1))
\right].
\]

因此：

```text
UHPC_ZHANG_COMPRESSION_SOURCE = PASS
UHPC_ZHANG_STRESS_C1_AT_PEAK = PASS
UHPC_ZHANG_FULL_DOMAIN_BOUNDEDNESS = PASS
UHPC_ZHANG_FINITE_ANALYTIC_SECTION_PRIMITIVES = PASS
UHPC_ZHANG_G6 = PASS
```

---

# 2. Liu 2024 CC literal source issue

Liu 2024 给出：

elliptic candidate / final Eq.(4) branch:

\[
x^2-1.49xy+y^2-1=0,
\]

parabolic candidate / final Eq.(4) branch:

\[
(x+1.85y)^2+x+7.98y=0.
\]

论文 literal Eq.(4) 规定在 stress ratio `0.5` / `2.0` 切换；但按正压幅值计算，在 `r=p_m/p_M=0.5`：

\[
K_E(0.5)=1.40719509,
\qquad
K_P(0.5)=1.53553644.
\]

因此 literal piecewise criterion 存在约 9.12% value gap，不能作为项目要求的连续 capacity gate 直接冻结。

---

# 3. Project conservative source-min reduction

不修改 Liu 的任何曲线系数，不使用任何结构 Pu/FEM comparator。只把 Liu 自己给出的两条候选曲线取**较低容量包络**，得到无自由参数的 conservative project reduction。

对 CC demand 排序：

\[
0\le p_m\le p_M,
\qquad
r=p_m/p_M\in[0,1].
\]

elliptic radial capacity：

\[
\boxed{
K_E(r)=\frac1{\sqrt{r^2-1.49r+1}}.}
\]

parabolic radial capacity：

\[
\boxed{
K_P(r)=\frac{r+7.98}{(r+1.85)^2}.}
\]

定义：

\[
\boxed{
K_{CC,U}^{\min}(r)=\min[K_E(r),K_P(r)].}
\]

这不是把 Eq.(4) 偷换掉，而是明确标记为：

```text
PROJECT_DERIVED_CONSERVATIVE_SOURCE_MIN_REDUCTION
```

其唯一正域交点：

\[
\boxed{r_*=0.576358545117484.}
\]

交点容量：

\[
K_E(r_*)=K_P(r_*)=1.45337946681509.
\]

因此：

- `r<r*`：elliptic 控制；
- `r>r*`：parabolic 控制；
- `r=r*`：两者容量严格相同。

## 3.1 Axis / equal-biaxial / continuity

\[
K^{\min}(0)=1,
\]

故单轴压缩严格退化。

\[
K^{\min}(1)=1.10557094491,
\]

保留 Liu 试验所显示的等双压小幅增强。

在 `r=r*`：capacity value C0 连续，没有 0.5 处的源式跳跃。

## 3.2 Same-source branch derivatives

\[
K_E'(r)
=-\frac12(2r-1.49)(r^2-1.49r+1)^{-3/2},
\]

\[
K_P'(r)
=
\frac{(r+1.85)-2(r+7.98)}{(r+1.85)^3}.
\]

在交点：

\[
K_E'(r_*)=+0.517727699,
\qquad
K_P'(r_*)=-1.028132753.
\]

因此 source-min gate 在唯一交点存在**有限容量 cusp**，不是 C1。这里不做任意宽度的平滑桥，因为：

1. 该对象是 2D ultimate-capacity judgment，不是 structural elastic/material tangent backbone；
2. branchwise re-cut 是有限解析的；
3. 任意 C1 smoothing width 会引入新的非来源参数。

若未来某个 bordered root 恰好落在该唯一比例，可将该点作为有限 event 同时评价两分支，而不是建立材料点或空间网格。

## 3.3 Direct re-cut

\[
\boxed{
\lambda_{CC,U}
=
\frac{f_cK_{CC,U}^{\min}(r)}{p_M^d}.
}
\]

只需一次排序、一个应力比、两个有限闭式容量值和一个 `min`。

因此：

```text
UHPC_CC_LITERAL_LIU_EQ4 = SOURCE_DISCONTINUOUS_AT_STATED_SWITCH
UHPC_CC_PROJECT_SOURCE_MIN_VALUE_CONTINUITY = PASS
UHPC_CC_PROJECT_SOURCE_MIN_BRANCH_DERIVATIVES = PASS
UHPC_CC_PROJECT_SOURCE_MIN_C1 = SOURCE_CUSP_ACCEPTED_AS_FINITE_CAPACITY_EVENT
UHPC_CC_PROJECT_SOURCE_MIN_G6 = PASS
UHPC_CC_PU_BACKFIT = ZERO
```

---

# 4. TC current-strain softening: preserve uniaxial axis

Diab/Ferche-type current softening may only use **excess transverse tension**, not total positive Poisson lateral strain.

For signed principal strains with compression \(\varepsilon_c<0\) and transverse tensile direction \(\varepsilon_t\ge0\)，定义

\[
\boxed{
\varepsilon_{t,ex}
=
\max(0,\varepsilon_t+\nu\varepsilon_c).
}
\]

严格单轴压缩时

\[
\varepsilon_t=-\nu\varepsilon_c
\Rightarrow
\varepsilon_{t,ex}=0.
\]

因此

\[
\beta_{TC}(0)=1
\]

不会把纯单轴压缩峰错误软化。

候选 current softening 仍为

\[
\boxed{
\beta_{TC}
=
\max\left[0.55,(1+2500\varepsilon_{t,ex})^{-0.20}\right].
}
\]

这只是一项 G6-compatible current interaction component；Liu 2024 TC sequential envelope 继续作为 ultimate capacity gate。二者职责不混淆。

---

# 5. UHPC seven-gate status after this execution

| Gate | Result |
|---|---|
| G1 uniaxial compression | PASS — Zhang 2023 + material-only retained parameters |
| G2 uniaxial tension | PASS component — Hiew 2024 |
| G3 CC/TC/CT/TT source | PASS at capacity-source level — Liu 2024 |
| G4 plane stress / Poisson | PASS — existing architecture + excess-strain TC trigger |
| G5 same-source derivative | PASS branchwise; Zhang stress C1; CC capacity has one explicit source-min cusp |
| G6 finite direct calculation | PASS — no material points/history/spatial quadrature; finite analytic primitives available |
| G7 no Pu backfit | PASS |

Current identity:

```text
UHPC_COMPRESSION_BACKBONE = ZHANG_2023
HU_WENXU = HISTORICAL_UNIAXIAL_COMPARATOR_ONLY
UHPC_CC_CAPACITY = LIU2024_SOURCE_MIN_PROJECT_REDUCTION
UHPC_TC_CT_CAPACITY = LIU2024_SEQUENTIAL_CONSERVATIVE_ENVELOPE
UHPC_TT_CAPACITY = LIU2024_UNIAXIAL_TENSILE_CAP
UHPC_TENSION_BACKBONE = HIEW_2024
UHPC_TC_CURRENT_SOFTENING = DIAB_FERCHE_ON_EXCESS_TENSION_ONLY
UHPC_CAPACITY_7GATE = PASS_WITH_ONE_FINITE_CC_CAPACITY_CUSP
STRUCTURAL_PU_RERUN = NOT_AUTHORIZED
```

The remaining pre-Pu material task is to finish the NC TC Appendix-B source interpretation audit and issue one combined NC/UHPC material certificate. Only then may the structural 1D->2D tables be regenerated.
