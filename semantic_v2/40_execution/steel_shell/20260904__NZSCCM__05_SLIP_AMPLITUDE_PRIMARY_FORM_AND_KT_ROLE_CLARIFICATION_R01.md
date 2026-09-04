# NZ-SCCM 多波钢壳05：滑移幅值主表达与 Kt 角色澄清 R01

## 0. 目的

本节点不建立新的 06 理论，也不修改 production R14。它只对 05 的表达层级做一次收敛：

- 保留原 R14 主位移/曲率形函数不变；
- 保留 05 已有的双界面滑移控制方程；
- 将 `S_+, S_-` 明确为 primary partial-interaction unknowns；
- 将 `c_+, c_-` 与 `z_c^{PI}, z_+^{PI}, z_-^{PI}` 降级为求解后的 derived reporting quantities；
- 明确 `K_t` 只进入滑移平衡矩阵，决定滑移幅值，不决定父 R14 的形函数。

这一步用于消除“抗剪刚度改变形函数”的表述歧义。

---

## 1. 原 R14 形函数保持不变

父理论仍取

\[
\kappa_y(y)=\widehat\kappa_y\sin(\beta y),\qquad \beta=\frac{m^*\pi}{a}.
\]

其中 `m*` 由原整体板稳定问题先求得，与 `K_t` 无关。

完全组合参考应变为

\[
\varepsilon_{y,+}^{FC}=\varepsilon_y^0+z_f\kappa_y,
\]

\[
\varepsilon_{y,c}^{FC}=\varepsilon_y^0,
\]

\[
\varepsilon_{y,-}^{FC}=\varepsilon_y^0-z_f\kappa_y.
\]

---

## 2. 有限滑移只增加相对位移修正

定义相对于完全组合参考态的位移修正

\[
r_+(y),\quad r_c(y),\quad r_-(y).
\]

于是

\[
\varepsilon_{y,+}=\varepsilon_y^0+z_f\kappa_y+r_+',
\]

\[
\varepsilon_{y,c}=\varepsilon_y^0+r_c',
\]

\[
\varepsilon_{y,-}=\varepsilon_y^0-z_f\kappa_y+r_-'.
\]

两个实际界面滑移为

\[
s_+=r_+-r_c,\qquad s_-=r_--r_c.
\]

界面剪流关系保持

\[
q_+=k_+s_+,\qquad q_-=k_-s_-.
\]

其中 `k_+, k_-` 与输入 `K_t` 的关系由 05 连接几何定义给出。

---

## 3. 固定滑移基函数，不让 Kt 改变空间形状

父 R14 只有一个整体纵向模态，因此 05 继续采用同频 Galerkin：

\[
s_+(y)=S_+\cos(\beta y),
\]

\[
s_-(y)=S_-\cos(\beta y).
\]

这里

\[
\boxed{\phi_s(y)=\cos(\beta y)}
\]

是固定基函数。

`K_t` 不进入 `\phi_s(y)`；它只通过滑移平衡决定 `S_+,S_-`。

---

## 4. 两个滑移幅值的 2×2 显式方程

定义相刚度

\[
\mathcal K_+,\quad \mathcal K_c,\quad \mathcal K_-.
\]

以及

\[
B_{11}=k_+\left(\frac1{\mathcal K_+}+\frac1{\mathcal K_c}\right),
\]

\[
B_{12}=\frac{k_-}{\mathcal K_c},
\]

\[
B_{21}=\frac{k_+}{\mathcal K_c},
\]

\[
B_{22}=k_-\left(\frac1{\mathcal K_-}+\frac1{\mathcal K_c}\right).
\]

令

\[
A_{11}=\beta^2+B_{11},\quad A_{12}=B_{12},
\]

\[
A_{21}=B_{21},\quad A_{22}=\beta^2+B_{22}.
\]

则

\[
\boxed{
\begin{bmatrix}
A_{11}&A_{12}\\
A_{21}&A_{22}
\end{bmatrix}
\begin{bmatrix}
S_+\\S_-
\end{bmatrix}
=z_f\beta\widehat\kappa_y
\begin{bmatrix}
1\\-1
\end{bmatrix}
}
\]

定义

\[
\Delta_\beta=A_{11}A_{22}-A_{12}A_{21},
\]

得到

\[
\boxed{S_+=z_f\beta\widehat\kappa_y\frac{A_{22}+A_{12}}{\Delta_\beta}}
\]

\[
\boxed{S_-=-z_f\beta\widehat\kappa_y\frac{A_{11}+A_{21}}{\Delta_\beta}}
\]

因此

\[
\boxed{K_t\rightarrow(k_+,k_-)\rightarrow(S_+,S_-)}
\]

才是 05 的 primary causal chain。

---

## 5. c± 只是由 S± 派生出的无量纲报告量

由于

\[
s_+'=-\beta S_+\sin\beta y,
\qquad
s_-'=-\beta S_-\sin\beta y,
\]

而

\[
\kappa_y=\widehat\kappa_y\sin\beta y,
\]

可定义

\[
\boxed{c_+=1-\frac{\beta S_+}{z_f\widehat\kappa_y}}
\]

\[
\boxed{c_-=1+\frac{\beta S_-}{z_f\widehat\kappa_y}}
\]

于是

\[
\varepsilon_{y,+}-\varepsilon_{y,c}=c_+z_f\kappa_y,
\]

\[
\varepsilon_{y,-}-\varepsilon_{y,c}=-c_-z_f\kappa_y.
\]

所以 `c_+, c_-` 不是新的形函数，也不是经验折减系数；它们只是固定滑移基函数经过 2×2 平衡后得到的幅值比。

---

## 6. zPI 只是截面应变恢复记账量

若为了沿用 R14 的截面接口，需要把 core 的修正写成等效应变臂，可由总轴力守恒得到

\[
z_c^{PI}=-z_f\frac{\mathcal K_+c_+-\mathcal K_-c_-}{\mathcal K_++\mathcal K_c+\mathcal K_-},
\]

再定义

\[
z_+^{PI}=z_c^{PI}+c_+z_f,
\]

\[
z_-^{PI}=z_c^{PI}-c_-z_f.
\]

但从本节点起，`zPI` 只作为 R14 section interface 的 derived bookkeeping quantity，不再作为“Kt 改变了形函数”的表述依据。

---

## 7. 两个严格极限

### 7.1 Kt → ∞

若 `k_+,k_-→∞`，则由 2×2 方程

\[
S_+\to0,\qquad S_-\to0.
\]

因此

\[
c_+\to1,\qquad c_-\to1,
\]

并在对称上下钢面相刚度下

\[
z_c^{PI}\to0,
\]

\[
z_+^{PI}\to+z_f,\qquad z_-^{PI}\to-z_f.
\]

于是严格恢复原 R14 完全组合运动学。

### 7.2 Kt → 0

若 `k_+,k_-→0`，则

\[
S_+\to\frac{z_f\widehat\kappa_y}{\beta},
\qquad
S_-\to-\frac{z_f\widehat\kappa_y}{\beta},
\]

从而

\[
c_+\to0,\qquad c_-\to0.
\]

这表示 steel/core 的弯曲相对应变传递消失，而不是构件本身不发生变形。

---

## 8. 与常规部分相互作用理论的关系

本节点采用的逻辑是：

\[
\boxed{\text{固定形函数} \rightarrow \text{连接刚度进入平衡} \rightarrow \text{求滑移幅值}}
\]

而不是

\[
\boxed{\text{连接刚度} \rightarrow \text{修改父理论形函数}}.
\]

这与组合结构中常见的“位移场先定、滑移由连接刚度和平衡求解”的组织方式一致。

---

## 9. 对当前 05 的治理结论

1. 不建立新的 06。
2. 不废止 05 的双界面控制方程。
3. 不修改 production R14。
4. 后续程序和报告优先输出 `S_+,S_-`，再输出 `c_+,c_-,zPI`。
5. `Kt` 的参数敏感性应解释为“滑移幅值敏感性”，而不是“形函数敏感性”。
6. 下一数值门禁仍是：`Kt→∞` 时完整 `R4/J4/Pu` 是否回归冻结 R14；若不回归，问题必在 05→R14 的后续组装/实现，而不是这组 2×2 滑移方程本身。

## 10. 当前状态

FORMULATION_STATUS = CLARIFIED_NOT_REPLACED

PRIMARY_PI_UNKNOWNS = S_PLUS, S_MINUS

FIXED_SLIP_BASIS = cos(beta*y)

KT_ENTERS_BASIS = NO

KT_ENTERS_AMPLITUDE_EQUILIBRIUM = YES

C_AND_ZPI_ROLE = DERIVED_REPORTING_AND_R14_SECTION_INTERFACE

PRODUCTION_R14_MODIFIED = NO
