# NZ-SCCM — Airy + current N–M 统一变形–应力理论兼容门禁 R01

**日期：2026-08-28**  
**身份：THEORY AUDIT / DIAGNOSTIC ONLY / NOT PRODUCTION**  
**分支：** `diagnostic/bh032-bh050-mode-projection-20260827`  
**执行纪律：** THEORY FIRST / NO FEM / NO TEST / FAIL FAST / FIRST FAILED GATE STOPS EXECUTION

---

## 0. 本轮唯一问题

检验以下设想能否直接成为同一个物理状态的统一理论：

\[
q\to w(q),\kappa(q)
\]

\[
\text{Airy}\to \mathbf N^A(P,q)
\]

\[
(\boldsymbol\varepsilon^0,\boldsymbol\kappa)\xrightarrow{\text{current section operator}}(\mathbf N,\mathbf M)
\]

并令 current `N-M` 状态随 `q` 到达材料/截面包络，或在此前出现结构极限点，从而定义 `Pu`。

本轮不允许：

```text
FEM/test in theory selection = NO
fitted stiffness/curvature factor = NO
effective width/area = NO
new local mode as workaround = NO
full material virtual-work path as workaround = NO
production modification = NO
```

一旦首个理论门禁失败，立即停止，不继续构造 Pu。

---

# G0 — q -> common curvature

保留当前 Marguerre–Airy 单模态：

\[
w_i=bq_0\phi,\qquad w_d=bq\phi,
\qquad \phi=\sin\alpha x\sin\beta y.
\]

因此新增曲率唯一：

\[
\kappa_x=-w_{d,xx}=bq\alpha^2\phi,
\]

\[
\kappa_y=-w_{d,yy}=bq\beta^2\phi,
\]

\[
\kappa_{xy}=-2w_{d,xy}=-2bq\alpha\beta\cos\alpha x\cos\beta y.
\]

对 BH 控制反节点且 `ell=b`：

\[
\kappa_x=\kappa_y=\pi^2q/b.
\]

```text
G0_Q_TO_KAPPA = PASS
```

---

# G1 — 给定 midplane strain + curvature 是否存在 frozen current N-M map

在当前接受的 SSUHPC terminal/material architecture 内，UHPC directional section operator 已定义：

\[
(\varepsilon_i^0,\kappa_i)\mapsto(N_i^{UHPC},M_i^{UHPC}),\qquad i=x,y,
\]

钢面采用当前冻结 R02/R06 terminal operator，web 采用冻结 exact resultant law。因而在当前已接受的 operator domain 内，可把 phase resultants 组装为

\[
(\boldsymbol\varepsilon^0,\boldsymbol\kappa)\mapsto(\mathbf N^{sec},\mathbf M^{sec}).
\]

这里仅承认现有 operator 的既定身份；不把 R06 扩张成未经来源定义的 post-yield history law。

```text
G1_CURRENT_SECTION_NM_OPERATOR = PASS_WITHIN_FROZEN_OPERATOR_DOMAIN
```

---

# G2 — old explicit Airy membrane field 与 current section constitutive state 是否是同一个兼容状态

## G2.1 old Airy compatibility 的来源

当前显式 Airy 特解不是纯几何恒等式。它来自 frozen initial full-composite extensional compliance：

\[
\bar A_{22}\theta_{,xxxx}
+(2\bar A_{12}+\bar A_{66})\theta_{,xxyy}
+\bar A_{11}\theta_{,yyyy}
=\mathcal G(w,w_i).
\]

其中

\[
N_x=\theta_{,yy},\qquad N_y=\theta_{,xx},\qquad N_{xy}=-\theta_{,xy}.
\]

该 PDE 能被写成上述常系数线性形式，依赖于 membrane constitutive closure

\[
\boldsymbol\varepsilon^0_{el}=\bar{\mathbf A}_0\mathbf N
\]

与 von Karman metric compatibility 的组合。

所以 frozen Airy 给出的 `N^A(P,q)` 与其兼容应变并不是独立的两个任意对象；它们已经通过 `A0^{-1}` 绑定。

## G2.2 若把同一个 N^A 再送入 nonlinear/current N-M operator

统一理论要求同一状态同时满足

\[
\boxed{\mathbf N^{sec}(\boldsymbol\varepsilon^0,\boldsymbol\kappa(q))=\mathbf N^A(P,q)}.
\]

若从此式反求

\[
\boldsymbol\varepsilon^0
=\mathcal C_N^{-1}[\mathbf N^A(P,q),\boldsymbol\kappa(q)],
\]

则除非 current operator 恰好退化为 frozen initial elastic law，通常有

\[
\boldsymbol\varepsilon^0
\ne \bar{\mathbf A}_0\mathbf N^A.
\]

但是 old Airy `theta` 本身正是由后一个 frozen elastic compliance compatibility 方程产生的。

于是新反求的 `epsilon0` 没有理由继续满足生成该 `theta` 的几何兼容方程。

定义 current compatibility residual：

\[
\mathcal R_{comp}^{cur}
=\varepsilon_{x,yy}^0
+\varepsilon_{y,xx}^0
-\gamma_{xy,xy}^0
-\mathcal G(w,w_i).
\]

old Airy 只保证在 frozen elastic relation 下

\[
\mathcal R_{comp}^{el}\equiv0.
\]

它**没有证明**

\[
\mathcal R_{comp}^{cur}\equiv0
\]

for

\[
\boldsymbol\varepsilon^0
=\mathcal C_N^{-1}[\mathbf N^A,\boldsymbol\kappa(q)].
\]

由于当前 UHPC/steel operators 在非弹性域明确不是 `A0` 的常系数线性关系，因此二者不能作为同一状态自动等同。

## G2.3 反过来也不成立

如果坚持使用 old Airy-compatible strain

\[
\boldsymbol\varepsilon^0=\bar{\mathbf A}_0\mathbf N^A
\]

并把它与 `kappa(q)` 输入 current section operator，则一般得到

\[
\mathbf N^{sec}_{cur}
\ne
\mathbf N^A.
\]

于是面内平衡/resultant field 与 current constitutive response 又不再是同一个状态。

因此不能同时保留以下三项为 exact identities：

1. old frozen-A explicit Airy `theta(P,q)`；
2. current nonlinear section `N(epsilon0,kappa)`；
3. one-state geometric/constitutive compatibility。

只有在 current operator 的 elastic degeneration

\[
\mathbf N^{sec}=\mathbf A_0\boldsymbol\varepsilon^0
\]

时三者重新严格一致。

```text
G2_OLD_AIRY_CURRENT_NM_ONE_STATE_COMPATIBILITY = FAIL
FAIL_TYPE = CONSTITUTIVE_COMPATIBILITY, NOT NUMERICAL
ELASTIC_LIMIT = EXACT_PASS
NONLINEAR_CURRENT_DOMAIN = NOT_CLOSED
```

---

# STOP — 按 fail-fast 纪律不得继续

本轮执行在 G2 立即停止。

因此以下步骤均 **NOT EXECUTED**：

```text
G3 current M -> exact q-equilibrium
G4 finite explicit harmonic closure
G5 material-envelope contact
G6 structural limit/tangent singularity
G7 Pu root selection
BH032/BH050 recalculation
```

没有 Pu 候选、没有修正系数、没有 FEM 比较。

---

# 门禁的准确含义

本门禁**不证明**“Airy 不能与 current N-M 结合”。

它只证明：

\[
\boxed{
\text{不能把由 frozen }A_0^{-1}\text{ compatibility 得到的 old closed-form Airy field}
\text{ 与 nonlinear current }N-M\text{ 简单串联，并同时称其为同一个兼容状态。}
}
\]

若未来重新开启该方向，理论上必须先重新建立满足 current constitutive relation 的 membrane compatibility closure；是否仍能保持有限显式，要在那个新 closure 上重新证明，不能预设。

已有 `20260827_1400__...CURRENT_BENDING_GLOBAL_RQ...` 的 exact current-bending generalized-work derivation并未解决本门禁：该文件在 nonlinear full-halfwave stage 明确回到 compatible global strain coordinates `(D,a_parallel,q)`，而不是证明 old frozen-A Airy `N^A` 经 current inverse 后仍满足原 compatibility。

已有 direct Airy -> N-M capacity path 可以继续作为其既定的 **capacity-contact approximation architecture**，但不能据此宣称它已经形成完全统一的 `w-epsilon-sigma-N-M` one-state theory。

---

# 本轮裁决

```text
THEORY_ONLY = YES
FEM_USED = NO
TEST_USED = NO
PRODUCTION_CHANGED = NO
Q_TO_KAPPA = PASS
CURRENT_NM_OPERATOR = PASS_WITHIN_FROZEN_DOMAIN
OLD_EXPLICIT_AIRY + CURRENT_NM ONE_STATE COMPATIBILITY = FAIL
EXECUTION_STOPPED_AT_FIRST_FAILED_GATE = YES
PU_COMPUTED = NO
```
