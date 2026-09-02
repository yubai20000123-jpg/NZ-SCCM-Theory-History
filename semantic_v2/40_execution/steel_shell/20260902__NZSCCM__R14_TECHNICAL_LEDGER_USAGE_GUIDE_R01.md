# NZ-SCCM R14 技术总账使用说明 R01

## 0. 与旧 R13 使用说明的唯一关键区别

旧说明错误地要求：

```text
固定 eps_y^-=-eps_c0
-> 解一个 capacity-contact root
-> 在 contact roots 中取最小正 q
```

R14 改为：

```text
q=0 主平衡点
-> 给 q
-> 联立解四个 R4 平衡变量
-> 沿同一连通支增加 q
-> 同时监测材料域边界和 J4 fold
-> 谁先到谁控制
```

材料、R04、R02、R06、UHPC、web 的计算方法全部保持不变。

---

# 1. 新试件输入

仍输入：

```text
b,a,tc,ts,A0g,Aw
Es,nu_s,fy
Ec,nu_c,fc,eps_c0
Lx,Ly,A0_local
UHPC five tensile anchors
```

先做 R14 input gates。

---

# 2. 先算一次不随求根改变的量

计算：

```text
q0,rho_w,zf
A11,A22,A12
Dx,Dy,Dmu,D66,H
m*
Pcr,Kx,G,C,Jx,Jy
steel_branch = R04 or R06
```

这些与旧 R13 完全相同。

---

# 3. 正确的外层未知量

给定一个 q 后，四个未知量是：

\[
\boxed{\varepsilon_x^0,\kappa_x,\varepsilon_y^0,\kappa_y}
\]

不能再固定

\[
\varepsilon_y^-=-\varepsilon_{c0}.
\]

为了人工 Excel 更稳定，可以把曲率换成等价的“半厚度应变差”：

\[
\chi_x=\frac{t_c}{2}\kappa_x,\qquad \chi_y=\frac{t_c}{2}\kappa_y.
\]

于是人工求根变量可写

\[
(\varepsilon_x^0,\chi_x,\varepsilon_y^0,\chi_y).
\]

恢复曲率：

\[
\kappa_x=\frac{2\chi_x}{t_c},\qquad \kappa_y=\frac{2\chi_y}{t_c}.
\]

这只是数值缩放，不改变理论。

---

# 4. 每个 q 下怎样联立求 R4

先计算截面应变：

\[
\varepsilon_x^\pm=\varepsilon_x^0\pm\chi_x,\qquad
\varepsilon_y^\pm=\varepsilon_y^0\pm\chi_y.
\]

钢面中心：

\[
e_x^{s,\pm}=\varepsilon_x^0\pm\frac{2z_f}{t_c}\chi_x,
\]

\[
e_y^{s,\pm}=\varepsilon_y^0\pm\frac{2z_f}{t_c}\chi_y.
\]

然后照旧依次算：

```text
upper/lower R04 or R06
UHPC F0/F1 resultants
web exact resultants
total Nx,Mx,Ny,My
```

全局 demand：

```text
NxA(q), MxA(q), NyA(q), MyA(q)
```

四残量：

\[
R_1=N_x-N_x^A,
\]

\[
R_2=(M_x-M_x^A)/z_f,
\]

\[
R_3=N_y-N_y^A,
\]

\[
R_4=(M_y-M_y^A)/z_f.
\]

求

\[
R_1=R_2=R_3=R_4=0.
\]

---

# 5. 人工 Excel 的一轮 Newton 修正

当前

\[
\mathbf x=(\varepsilon_x^0,\chi_x,\varepsilon_y^0,\chi_y)^T.
\]

把四个当前残量记下，然后每次只扰动一个变量：

```text
epsx0 + h1
chi_x + h2
epsy0 + h3
chi_y + h4
```

分别得到四组新残量。

构造

\[
J_{ij}\approx\frac{R_i(x_j+h_j)-R_i(x_j)}{h_j}.
\]

解

\[
\boxed{J\Delta x=-R}.
\]

先试 \(x+\Delta x\)。如果残量变差，再试

\[
x+\frac12\Delta x,\quad x+\frac14\Delta x,\quad x+\frac18\Delta x.
\]

这仍是四个未知量的**联立修正**，不是逐变量独立求解。

---

# 6. 从 q=0 开始怎样走主平衡支

理论起点：

\[
q=0,\qquad \varepsilon_x^0=\kappa_x=\varepsilon_y^0=\kappa_y=0.
\]

实际计算时：

1. 给一个很小的正 q；
2. 用上一点状态作为新一点首猜；
3. 联立解 R4=0；
4. 保存该点；
5. 再略增 q；
6. 重复。

q 步只是 branch identity / 数值 continuation。它不是材料历史加载步；每个点仍由同一 current-state 显式算子独立评价。

---

# 7. 每个平衡点必须同时监测什么

UHPC compression margins：

\[
g_{c,i}^{\pm}=\varepsilon_i^\pm+\varepsilon_{c0}\ge0.
\]

UHPC tension margins：

\[
g_{t,i}^{\pm}=\varepsilon_{t,lim}-\varepsilon_i^\pm\ge0.
\]

以及四个外层变量有限差分得到的同一个 4×4 Jacobian：

\[
J_4.
\]

记录 `det(J4)`，有条件时同时记录 smallest singular value。

---

# 8. 什么时候得到 Pu

## A. 材料域边界先到

如果在 J4 fold 前某个当前 UHPC 材料域 margin 首先变成 0，则精化

\[
R_4=0,\qquad g=0.
\]

该点是当前 R14 material-domain terminal。

BH005–BH070 当前属于这种情况。

这不等于“理论永远规定 eps_y^-=-eps_c0”，而是这些特定试件的主平衡支恰好先碰到当前材料域边界。

## B. J4 fold 先到

如果材料 margins 仍为正，而

\[
\det J_4\to0,
\]

则精化 fold。形式上最好解：

\[
R_4=0,\quad J_4v=0,\quad v^Tv=1.
\]

人工 Excel 可以先用 det / smallest singular value 定位并加密 q。

BH085、BH100 当前属于这一类。

最终：

\[
\boxed{P_u=P(q_{\rm first\ terminal})}.
\]

---

# 9. R06 怎么使用

完全沿用 R13：

- 给当前某个 steel-face centroid strain；
- 解 R02 cubic 的全部非负根 + `U=0`；
- 按最低 condensed energy 取 `U*`；
- 构造完整二维 `Phi(u,v)`；
- 检查 interior / four edges / corners；
- 若 `Phi_max(1)>fy^2`，沿 current strain ray 求 first `lambda_y`；
- 返回 R06 mean face stress。

`u,v,lambda` 仍然只是局部算子内部变量。

---

# 10. 人工计算推荐的 q 步长策略

不要规定固定“加载步数”。开始阶段可用较粗 q 间隔；当出现任一情况时自动减小：

```text
R4 Newton 需要明显更多轮
det(J4) 快速减小
smallest singular value 快速减小
某个 material margin 接近 0
R06 upper/lower event 刚发生
```

靠近 terminal 时可用

```text
q interval -> 1/2 -> 1/4 -> 1/8
```

直到 terminal 的 q 和 Pu 达到所需数值精度。

---

# 11. AI 最短执行指令

> 只使用 R14 技术总账和给定物理输入。不得预设 `eps_y^-=-eps_c0`。从 `q=0, x=0` 出发，对每个 q 联立求 `R4(x;q)=0`，continuation 只用于识别与 unloaded state 连通的平衡支。R04/R06、R02、UHPC、web 和所有 resultants 严格沿用总账。沿主支同时监测 UHPC material-domain margins 与 `J4=dR4/dx`。若材料域边界先到，精化 `R4+g=0`；若 J4 fold 先到，精化 `R4=0, J4 v=0, vTv=1`。取首先到达的 admissible closed terminal 的 q，并报告 `Pu=P(q)`。不得使用 FEM、试验 Pu、历史 Pu 或 specimen_id 选根或选 terminal。

---

# 12. 与 R13 旧使用说明的废止关系

旧说明中以下操作全部废止：

```text
固定 epsy_minus=-eps_c0
只求 epsx_minus/epsx_plus/epsy_plus 三变量
在 compression-contact roots 中取 min positive q
把 contact-root 不存在解释为 B/H 无根边界
```

其余材料与局部算子操作说明继续有效。
