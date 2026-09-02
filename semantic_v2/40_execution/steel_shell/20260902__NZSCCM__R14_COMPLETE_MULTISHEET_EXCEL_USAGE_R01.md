# NZ-SCCM R14 多页完整人工计算 Excel — 使用说明 R01

**适用工作簿**

`NZSCCM_R14_多页完整人工计算Excel_R01_20260902.xlsx`

## 1. 这版 Excel 的定位

这一版已经把物理输入、A/D、整数模态、Airy、UHPC、web、R04、R02/R06、总截面 N/M、R4 残量、人工 Newton/J4 推荐、q 路径记录和终点判断放在**同一个工作簿**中。

不再要求同时打开另一份“单页主表”。

R14 相对 R13 只做一个理论修正：

\[
\varepsilon_y^-=-\varepsilon_{c0}
\]

不再作为所有试件必须满足的 universal terminal 方程。

正确外层问题是：

\[
\mathbf R_4(\mathbf x;q)=0,
\qquad
\mathbf x=(\varepsilon_x^0,\kappa_x,\varepsilon_y^0,\kappa_y)^T
\]

沿与 \(q=0,\mathbf x=0\) 连通的平衡支前进，同时监测 current material-domain boundary 和 \(J_4\)-fold，谁先到谁控制当前 \(P_u\)。

R04、R02、R06、UHPC、web 和 section N/M 公式没有因为本次修正而改变。

---

## 2. 各页用途

| 页 | 用途 |
|---|---|
| `00_说明` | 工作簿身份、允许/禁止事项 |
| `01_输入全局` | **新试件唯一物理输入页**；同时自动计算 A/D、m*、Pcr、Airy、R04/R06 gate |
| `02_UHPC材料` | Hiew 拉伸 cubic-Hermite 系数及 F0/F1 原函数，通常只读 |
| `03_状态R4` | **当前 q + 四个截面状态变量的完整物理评价页**；输出 N/M、R4、material margins、root objective |
| `04_R06上` | 上钢面 R04 或 R02/R06 当前算子与局部求根 |
| `05_R06下` | 下钢面 R04 或 R02/R06 当前算子与局部求根 |
| `06_R4推荐` | 四变量有限差分 Jacobian / Newton 推荐；同时给 J4 |
| `07_q路径终点` | 人工记录 q=0 连通主平衡支与 terminal 演化 |
| `08_BH回归` | BH005–BH100 回归结果，只用于核验，**不被运行时公式读取** |
| `09_使用说明` | 工作簿内置逐格说明 |
| `10_Solver设置` | 可选的 Excel 原生 Solver 设置 |

---

# 3. 新试件：第一步只改 `01_输入全局`

## 3.1 黄色物理输入 `B5:B20`

依次为：

| 单元格 | 参数 |
|---|---|
| B5 | b |
| B6 | a |
| B7 | tc |
| B8 | ts |
| B9 | A0g |
| B10 | Aw |
| B11 | Es |
| B12 | nu_s |
| B13 | fy |
| B14 | Ec |
| B15 | nu_c |
| B16 | fc |
| B17 | eps_c0 |
| B18 | Lx |
| B19 | Ly |
| B20 | A0_local |

黄色格可以修改；绿色公式格不要手改。

## 3.2 UHPC 拉伸锚点 `B24:C28`

若继续使用当前冻结 UHPC 材料，保持默认值：

```text
0          0
0.000420   9.767718
0.003800  10.734818
0.006900  10.347978
0.007590   0
```

只有材料来源本身改变时才改，不能为了匹配某块试件的 Pu 调整。

## 3.3 输入以后先看

- `01_输入全局!B38`：`material_gate`
- `01_输入全局!B60`：`m*`
- `01_输入全局!B61`：`Pcr / MN`
- `01_输入全局!B81`：`sigma_cr_E`
- `01_输入全局!B82`：`steel_branch`

其中 `R04_YIELD_FIRST` 表示当前钢面用 R04；`R06_LOCAL_FIRST` 表示当前钢面需要 R02/R06。分支由公式自动决定，不人工指定。

---

# 4. `03_状态R4`：每一个 q 点的外层四平衡

黄色格：

```text
B5 = q
B6 = eps_x0
B7 = kappa_x
B8 = eps_y0
B9 = kappa_y
```

这里**不能再固定** `eps_y_minus = -eps_c0`。

Excel 自动得到四个 scaled residual：

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

重点读取：

```text
B58 = R4_norm
B59 = min compression margin
B60 = min tension margin
B61 = material_domain
B63 = upper local norm
B64 = lower local norm
B65 = current_state_status
B66 = root_objective
```

其中：

\[
\text{root objective}=\|R_4\|^2+\|r_{\rm upper}\|^2+\|r_{\rm lower}\|^2.
\]

---

# 5. R04 情况

若 `01!B82 = R04_YIELD_FIRST`，则上下钢面页自动按 R04 返回钢面平均应力，不需要求 lambda/u/v。

固定 q 下只需要解 `03!B6:B9` 四个截面变量，使 `03!E53:E56 ≈ 0`。

可以使用 `06_R4推荐` 人工 Newton，或按 `10_Solver设置` 使用 Excel 原生 Solver。

---

# 6. R06 情况

若 `01!B82 = R06_LOCAL_FIRST`，上、下钢面分别在 `04_R06上!B5:B7` 和 `05_R06下!B5:B7` 输入当前 `lambda,u,v`。

Excel 自动完成：R02 cubic 全部实根、加入 U=0、最低能量 U*、七谐波局部场、Phi/Phi_u/Phi_v、局部残量以及最终钢面平均应力。

关键位置：

```text
B27 = U_selected
B29:B30 = R02 mean_sx / mean_sy
B59 = Phi
B62:B64 = r0,r1,r2
B65 = local_norm
B66 = VM
B73:B74 = final_sx/final_sy
```

局部合格要求：

```text
local_norm ≈ 0
0 <= lambda <= 1
-1 <= u,v <= 1
```

u/v 到 ±1 是统一定义域边界根，不是人工 topology 选择。

单个 lambda/u/v 驻点不自动等于全域控制最大值；正式使用需要若干有规律的局部首猜，去重所有收敛候选，再比较 first-radial-yield / global-max 身份。

---

# 7. `04/05` 页人工局部 Newton

当前局部残量自动显示在 `R5:R7`，扰动量在 `R10:T10`。

分别只扰动 lambda、u、v，把三组新残量填到 `S5:U7`。Excel 自动形成 3×3 Jacobian，并在 `R19:T22` 给出 full、1/2、1/4、1/8 四组推荐。先试 full；残量变差再减步。

---

# 8. `06_R4推荐`：四变量联立修正

数值坐标采用：

\[
\chi_x=\frac{t_c\kappa_x}{2},\qquad
\chi_y=\frac{t_c\kappa_y}{2}.
\]

分别对 eps_x0、chi_x、eps_y0、chi_y 做一次小扰动；R06 情况下每次外层扰动后都必须重新收敛上下钢面 R06。把四次扰动后的四残量填到 `C12:F15`。

Excel 自动给：

```text
H12:K15 = 4×4 J4
L12:L15 = Newton correction
B23:E26 = full / 1/2 / 1/4 / 1/8 推荐
B19 = det(J4)
```

接受第一个能明显降低 `03!B58 R4_norm` 的步长。

---

# 9. 一个 q 点什么时候完成

至少要求：

```text
03!B61 = PASS
R4_norm 足够小
R06时 upper/lower local_norm 足够小
```

建议人工执行初始可用 `1E-6` 量级作为求根停止指标，终点精化继续压低。该容差只是执行值，不是理论参数。

---

# 10. `07_q路径终点`：找最终 Pu

从

\[
q=0,\qquad \varepsilon_x^0=\kappa_x=\varepsilon_y^0=\kappa_y=0
\]

连通支开始。实际操作用一个很小正 q，联立求当前 R4；收敛后记录一行，再略增 q，并以上一点状态作为下一点首猜。

记录 q、P、四截面变量、R4 norm、detJ4、material margins、上下 lambda、branch/event。

这只是有限维代数平衡支 continuation，不是材料历史加载步。

---

# 11. 最终 terminal

若 material margin 先到 0，且此前没有 admissible J4 fold，则精化：

\[
R_4=0,\qquad g=0.
\]

若 material margin 仍为正，而 J4 先趋于奇异，则精化 structural fold。`06!B19 detJ4` 只用于定位；正式 fold 应满足：

\[
R_4=0,\qquad J_4v=0,\qquad v^Tv=1.
\]

最终：

\[
\boxed{P_u=P(q_{\rm first\ admissible\ terminal})}.
\]

不能再预设 eps_y_minus=-eps_c0 一定控制所有试件。

---

# 12. 可选：Excel Solver

见 `10_Solver设置`。

R04 固定 q：目标 `03_状态R4!B66` 最小化到 0；可变 `03_状态R4!B6:B9`；方法 `GRG Nonlinear`。

R06 固定 q：目标仍为 `03_状态R4!B66`；可变 `03!B6:B9 + 04!B5:B7 + 05!B5:B7`；约束 `0<=lambda<=1`、`-1<=u,v<=1`、material margins>=0。

Solver 只是有限维显式方程 evaluator；R06 仍需要多首猜/global-max 身份检查。

---

# 13. 默认开箱核验

工作簿预填 BH050 当前 R14 material-boundary terminal，只用于公式链回归。正常打开应看到大致：

```text
P = 13.5247819548 MN
R4_norm ≈ 2.36E-8
upper local norm ≈ 1.6E-17
lower local norm ≈ 4.3E-12
material_domain = PASS
current_state_status = CURRENT_EQUILIBRIUM_PASS
```

做新试件时先改 `01_输入全局` 黄色物理输入，再从自己的小 q 状态重新求解。不要使用 `08_BH回归` 中的 q/Pu 作为新试件的根或首猜目标。

---

# 14. 三句核心

\[
\boxed{\text{Excel 中求的是同一套非线性联立方程，不是另一套理论。}}
\]

\[
\boxed{\text{R06 的迭代是局部显式方程求根；R4 的迭代是四平衡求根。}}
\]

\[
\boxed{\text{最终 Pu 来自连通平衡支上第一个 admissible terminal，而不是预设 compression contact。}}
\]
