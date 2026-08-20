# NZ-SCCM — 普通混凝土单一参考基准治理纠正 + direct2D 后续修复路线

时间：2026-08-20 21:04 +08:00

状态：`REFERENCE_GOVERNANCE_CORRECTION / SINGLE_REFERENCE_BASELINE_LOCK`

## 0. 本次纠正

此前 direct2D 九宫格审计中，错误地把当前候选函数一会儿与 Nguyen/Saenz 比、一会儿与 Foster/Kupfer 比、一会儿又与 G21 历史目标比，造成“构造基准”和“验收基准”不一致。

从本节点起，普通混凝土不再按作者名字切换参考。唯一参考对象固定为项目自己的：

`NC_REFERENCE_G21_LOCKED_TARGET`

它不是“Nguyen 模型”或“Foster 模型”的别名，而是 2026-08-08 G21 已冻结的普通混凝土低参数物理目标；外部文献只用于说明该目标的来源链，不再作为后续逐轮可切换的比较对象。

## 1. 单一普通混凝土参考基准 NC_REFERENCE_G21_LOCKED_TARGET

### 1.1 单轴压缩骨架

采用此前 G20/G21 已锁定的普通混凝土压缩目标。当前解析形式可写为 Saenz 型：

\[
C(c)=\frac{\kappa c}{1+(\kappa-2)c+c^2},
\qquad
\kappa=\frac{E_0\varepsilon_{c0}}{f_c}.
\]

这只是 `NC_REFERENCE_G21_LOCKED_TARGET` 的压缩轴公式；后续比较只和此目标比较，不再临时换其他压缩曲线。

### 1.2 单轴拉伸骨架

G20/G21 已锁定：

- 开裂前保持真实弹性斜率；
- 若来源缺少 `f_t`，当前治理规则取 `f_t=0.1 f_c`；
- \(\varepsilon_{cr}=f_t/E_0\)；
- post-cracking tension-stiffening 取 `alpha1=10`, `alpha2=0.3` 的保守项目目标；
- 原斜率突变点可做材料级窄 C2 正则化，但参考目标本身不因正则化而换模型。

未正则化的归一化参考可写为

\[
T_{ref}(r)=
\begin{cases}
r,&0\le r\le1,\\
1-\dfrac{7}{90}(r-1),&1<r<10,\\
0.3,&r\ge10,
\end{cases}
\qquad r=\varepsilon_t/\varepsilon_{cr}.
\]

后续任何新的单式拉伸候选，都只与 `T_ref` 比，不再与另一作者的拉伸曲线切换比较。

### 1.3 CC 参考目标

G21 冻结：

\[
c_i^*=c_i\left(1+a_{cc}c_1c_2\right),
\qquad
a_{cc}=0.1072329249362415.
\]

即 `CC_a` 的唯一参考值与函数形式固定为 G21 target。后续 direct2D 的 CC 候选只比较它是否复现该目标，而不再改用另一条等双压包络作验收基准。

### 1.4 TC/CT 参考目标

G21 冻结：

\[
c^*=c(1-\tau),
\]

且 tensile component 不做人工放大。这是当前 ordinary-concrete TC/CT 的唯一参考目标。后续 `Gamma_T`, `k_tc` 或任何替代函数，只能作为对这一 target 的解析实现/正则化，不再切换到 Nguyen Eq.3.43、MCFT 或其他 TC 曲线作为新的验收基准。

### 1.5 TT 参考目标

G21 冻结：

\[
\tau_i^*=\tau_i\left(1-a_t\tau_j^8\right),
\qquad
a_t=1-2^{-1/8}=0.08299595679532878.
\]

后续 TT 比较只以该目标为准。

### 1.6 单轴轴线门禁

继续保持 G27 轴线退化原则：

\[
s_1=U(x),\qquad s_2=0
\]

在相应单轴应力路径上必须严格恢复单轴参考骨架。不得为了二维耦合在有限应变上追加一个无界线性应力项，从而破坏单轴/软化轴线。

## 2. 对此前 direct2D 曲线审计的重新定性

此前图中：

- `current compression vs Nguyen/Saenz`：名称错误；应改为 `current compression vs NC_REFERENCE_G21 compression target`。当前 Saenz 型压缩式实际上就是 G21 target 的轴向解析实现，可判定 `PASS`。
- `T4 vs Nguyen/Foster`：比较对象治理错误；以后改为 `T4 vs NC_REFERENCE_G21 T_ref`。T4 是否保留，只由它对 `T_ref` 的误差决定。
- `Gamma_T vs Nguyen Eq.3.43`：该比较不再作为验收。所有由 Eq.3.43 推出来的 `k_tc=0.08307/0.10452/0.14` 均撤销正式候选身份，因为它们来自错误的比较基准。
- `k_eta=0.1625 from Foster equal-biaxial point`：撤销“已闭合”身份。后续 CC 只按 G21 的 `a_cc=0.1072329249362415` 目标闭合。
- additive Pi 有限应变无界问题：这个 FAIL 不依赖参考作者，属于候选自身数学缺陷，因此结论保留：`ADDITIVE_PI = REJECT`。

## 3. 后续几个问题怎样修改

### 3.1 拉伸 T4

状态：`REOPEN_FOR_G21_TARGET_ONLY`。

目标不是恢复 Nguyen/Foster 原式，而是构造一个单一、低阶、解析可积的 `T_new(r)`，使其在统一参考域内逼近 G21 的 `T_ref(r)`：

\[
T_{ref}(r)=r\ (0\le r\le1),\qquad
T_{ref}(r)=1-\frac7{90}(r-1)\ (1<r<10),\qquad
T_{ref}(r)=0.3\ (r\ge10).
\]

必须保持：

- `T_new(0)=0`；
- `T_new'(0)=1` with respect to `r`，因此物理初始斜率为 `E0`；
- `T_new(1)≈1`；
- post-cracking 不得无界；
- 正式候选只和 `T_ref` 比较。

### 3.2 TC/CT

状态：`REOPEN_FOR_G21_TARGET_ONLY`。

撤销此前以 Nguyen Eq.3.43 面积/点值闭合 `k_tc` 的方法。

唯一 target 改回：

\[
c^*=c(1-\tau).
\]

下一步若仍使用平滑单式 `Gamma_T`, 其参数必须由该 G21 target 自身产生。例如定义材料域及一个固定的材料级误差泛函，再求唯一最小误差参数；不得用 Case21 Pu 或其他结构试验反标。

### 3.3 CC

状态：`RETURN_TO_G21_CC_TARGET`。

撤销 `k_eta=0.1625` 的新锁定。唯一目标恢复为：

\[
c_i^*=c_i(1+a_{cc}c_1c_2),
\qquad a_{cc}=0.1072329249362415.
\]

若 direct2D 想用 `eta(c1,c2)` 形式，则应从此 target 代数推导/最小化得到，而不是再去取另一个等双压包络峰值。

### 3.4 二维 Poisson coupling

状态：`ZERO_TANGENT_REQUIREMENT_RETAIN / ADDITIVE_PI_REJECT`。

保留唯一要求：原点必须满足

\[
D_0=\frac{E_0}{1-\nu^2}
\begin{bmatrix}
1&\nu\\\nu&1
\end{bmatrix}.
\]

但不再采用全域无界

\[
\Pi_i\propto\varepsilon
\]

的 additive correction。下一候选必须同时满足：

1. 原点 plane-stress tangent；
2. 单轴应力路径严格恢复 G21 单轴骨架；
3. finite strain coupling 有界或随材料 secant/tangent degradation 衰减；
4. 不改变 G21 CC/TC/TT target；
5. 仍属于有限代数/有理 current map，可进入现有解析积分框架。

## 4. 治理规则

从本节点起：

- `REFERENCE_MODEL_SWITCHING = PROHIBITED`；
- 普通混凝土统一比较基准只有 `NC_REFERENCE_G21_LOCKED_TARGET`；
- 外部普通混凝土文献只可用来解释来源、检查数量级或提出新候选，不能在同一候选的验收阶段替换 reference；
- 如果未来确需更换 reference，必须先单独建立 `REFERENCE_CHANGE_PROPOSAL`，说明旧基准为何失效，并由用户明确批准后整体 supersede；不得在一次材料曲线比较中偷偷更换。

## 5. 当前下一步

唯一下一步：

1. 按 G21 `T_ref` 重构一个新的单一拉伸解析式；
2. 按 G21 `c*=c(1-tau)` 重构/闭合 TC 单式；
3. 按 G21 `a_cc` 恢复 CC interaction；
4. 在这三个 sector target 均固定后，再设计一个有限应变有界的 Poisson coupling，使原点 tangent 正确但不改变三个 sector target。

暂不重算 Case21，直到上述 material-only gate 完成。
