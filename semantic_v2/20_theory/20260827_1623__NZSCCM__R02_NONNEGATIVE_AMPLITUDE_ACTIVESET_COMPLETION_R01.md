# NZ-SCCM — R02 非负局部幅值的 active-set 完备化 R01

**Time:** 2026-08-27 16:23 +08:00  
**Parent:** `semantic_v2/20_theory/20260827_1710__NZSCCM__SINGLE_EXPLICIT_BH_CURRENT_MOMENT_HARMONIC_CLOSURE_R01.md`  
**Status:** `IMPLEMENTATION-CLOSURE / NO NEW MATERIAL LAW / NO NEW STRUCTURAL MODE / NO SPATIAL QUADRATURE`

---

## 0. 本节点只修一个求解定义缺口

现有 qU-augmented R02 把局部幅值定义为非负幅值，并在实现中只从三次驻值方程

\[
B_3U^3+B_2U^2+B_1U+B_0=0
\]

中选取 `U>=0` 的 minimum-energy real root。

BH050 current-moment 显式重算暴露一个纯求解完备性问题：随全局 q 增长，上钢面正驻值根连续下降到 `U=0`，随后三次方程只剩负实根。若继续坚持 `U>=0`，则“只枚举内部驻值根”的实现会返回 `no admissible root`，虽然受约束能量

\[
\min_{U\ge0}\Pi(U)
\]

在数学上仍然存在，其最小值转移到了边界 `U=0`。

这不是新的材料机制，也不是新的局部模态，而是原有 `U>=0` 定义对应的 KKT active-set 边界。

---

## 1. 完整的非负幅值凝聚

正式凝聚定义改写为

\[
\boxed{
U^*=\arg\min_{U\ge0}\Pi_{R02}^{aug}(U)
}
\]

候选集合必须同时包含：

1. 三次方程全部 `U>0` 实根；
2. 非负域边界 `U=0`。

在这些候选中直接比较同一个已经冻结的 condensed energy：

\[
\Pi_{R02}^{aug}
=\frac12K_b(U-A_0)^2
+\frac12t_sQ_s(m_x^2+m_y^2+2\nu_sm_xm_y)
+\frac12t_sG_sm_\gamma^2
+t_sE_s\left[K_Ad^2+2K_{d\Delta}d\Delta+K_{\Delta\Delta}\Delta^2\right].
\]

其中

\[
d=U^2-A_0^2,
\qquad
\Delta=b[(q_0+q)U-q_0A_0].
\]

若 `U=0` 被选中，则其一阶 KKT 条件等价于

\[
\left.\frac{\partial\Pi}{\partial U}\right|_{U=0}=B_0\ge0.
\]

当内部正根恰好与边界相接时：

\[
\boxed{U=0,\qquad B_0=0.}
\]

因此原先出现的 `no positive stationary root` 不是结构无根边界，而只是 active-set 切换。

---

## 2. R06 径向投影同步使用同一 active set

R06 的径向状态保持不变：

\[
q(\eta)=\eta q,
\qquad
\boldsymbol\varepsilon_f(\eta)=\eta\boldsymbol\varepsilon_f,
\]

且 `q0,A0` 保持为无应力初始缺陷。

在每个 `eta` 上，局部幅值统一由

\[
U^*(\eta)=\arg\min_{U\ge0}\Pi_{R02}^{aug}
\]

得到，然后用同一个 GL+LL 连续解析局部应力场寻找第一次

\[
\max\sigma_{VM}=f_y.
\]

因此不会因为某个中间径向状态恰好没有正驻值根而人为中断 R06。

---

## 3. 退化与一致性门禁

本 active-set 完备化必须保持：

```text
U=A0 at q=0, eps=0
GL-off -> frozen R02 energy and cubic
positive stationary branch available -> result unchanged
U=0 selected -> only active-set boundary changes, no material parameter changes
formal spatial quadrature = 0
material points = 0
comparator in operator = 0
```

20260827 13:35 BH050 旧候选在 R06 投影状态的上/下钢面仍选择正内部根，因此本修复对该历史回归点给出完全相同的：

```text
TOP eta = 0.8239874660, U = 0.2911147334 mm
BOTTOM eta = 0.3909289472, U = 2.5951383592 mm
```

即该修复不是为了改变已有结果，而是为了消除后续显式求解中的人工 `no-root` 缺口。

---

## 4. BH050 中 active-set 的实际出现顺序

在 1710 current-moment 显式平衡的 BH050 计算中，上钢面内部正根随 q 增大下降。

在约

\[
q\approx0.00807587
\]

处出现

\[
U_+\to0,
\qquad B_{0,+}\to0.
\]

随后非负受约束最小值位于

\[
\boxed{U_+=0}
\]

而不是宣布结构“无根”。

这一步只改变局部内部变量的 active set；全局未知量、Airy、common curvature、UHPC N-M、web、R06、current-moment q 方程均不改变。

---

## 5. 当前身份

```text
R02_AMPLITUDE_DOMAIN = U >= 0
R02_CONDENSATION = CONSTRAINED_MINIMUM_ENERGY
R02_INTERIOR_CANDIDATES = POSITIVE REAL CUBIC ROOTS
R02_BOUNDARY_CANDIDATE = U = 0
NO_ROOT_FROM_MISSING_POSITIVE_STATIONARY_POINT = PROHIBITED
NEW_MATERIAL_MECHANISM = NO
NEW_GLOBAL_MODE = NO
FORMAL_SPATIAL_QUADRATURE = 0
```

本文件仅用于确保显式求解器对其他试件也不会因为内部幅值 active-set 遗漏而产生人为“无根区”。