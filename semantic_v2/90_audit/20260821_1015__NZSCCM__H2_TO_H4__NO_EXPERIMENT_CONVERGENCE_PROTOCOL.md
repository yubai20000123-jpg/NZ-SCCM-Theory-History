# NZ-SCCM H2 -> H4 无试验值收敛审计协议

- Date frozen: 2026-08-21 10:15 +08:00
- Status: PRE-NUMERICAL GATE CONTRACT
- Purpose: 决定 H2 是否可冻结为 production in-plane subspace；不评价材料 M6，不使用试验承载力选阶数。

## 1. 禁止事项

在 H2/H4 convergence decision 中：

- 不读取/使用 `P_f`、Zhou reference load 或任何试验极限荷载作为选阶依据。
- 不以“哪个阶次更接近试验”作为 PASS/FAIL。
- 不修改 NC-M6。
- 不增加经验 restraint factor。
- 不把 audit quadrature 升格为 formal operator。
- H2 未通过时只允许升到预定义 H4；不得直接堆任意 Ritz modes。

## 2. 空间定义

H2 = `H_{2N}` with `N=1`。

H4 = 同一 nested compatible family with `N=2`。

两者：

- 相同 `w0 + Delta w` 单完整半波；
- 相同 q0；
- 相同 NC-M6 / steel / reinforcement current operators；
- 相同多相组装；
- 只改变面内 Ritz truncation order。

## 3. 结构族边界条件

### Swartz24

- `eta=0` essential side restraint。
- solve `Rq = Ra_{2m,2n} = Rb_{2m,2n} = 0`。

### Z0-Z5

- `eta` active。
- solve `Rq=Reta=Ra=Rb=0`。
- `Reta=0` gives transverse resultant natural equilibrium within the active Ritz space。

## 4. Audit-only 数值评价器身份

允许使用高阶 direct-current continuum quadrature 仅用于：

1. H2/H4 root/path 定位；
2. peak 小数定位；
3. residual 检查；
4. 比较 H2 与 H4 field convergence。

其身份明确为 `AUDIT_ONLY_NOT_FORMAL_THEORY`。

正式理论依然保持 D15/GKZ zero-spatial-integration。

## 5. 分支规则

1. 从 `(D,q,modes)=(0,0,0)` 原点连接分支开始。
2. 沿单调轴向缩短 `D` 追踪同一连续物理解。
3. 不以试验荷载选择 root。
4. 若 D-control 遇到 fold/bifurcation，切换到 augmented continuation / limit determinant，但仍保持 origin-connected branch identity。
5. 记录所有发现的结构分岔；不得因另一个 root 给出更接近试验的 P 而换支。

## 6. 数值精度门禁

对 H2 与 H4 各自的 peak 状态，必须满足：

### G0-1 equilibrium

\[
\|\widehat{\mathbf R}\|_2 \le 10^{-7}.
\]

其中各 residual 按冻结的 `fc*t` / `fc*t*eps0` 同量纲尺度归一化。

### G0-2 audit evaluator refinement

使用至少两个 direct-current quadrature resolution 复核 peak。要求

\[
\delta_{quad}P_u \le 0.05\%.
\]

若不满足，只提高 audit evaluator resolution；不得改变正式理论。

## 7. H2 -> H4 收敛门禁

在同一试件、同一 origin-connected peak 上定义

\[
\delta_P=
\frac{|P_u^{H4}-P_u^{H2}|}{|P_u^{H4}|},
\]

\[
\delta_D=
\frac{|D_u^{H4}-D_u^{H2}|}{\max(|D_u^{H4}|,10^{-12})},
\]

\[
\delta_w=
\frac{|q_u^{H4}-q_u^{H2}|}{q_0+|q_u^{H4}|}.
\]

同时对 peak 中面膜应变场定义面积 L2 差：

\[
\delta_{\varepsilon}=
\frac{\|\boldsymbol\varepsilon_{m}^{H4}-\boldsymbol\varepsilon_{m}^{H2}\|_{L^2(A)}}
{\max(\|\boldsymbol\varepsilon_{m}^{H4}\|_{L^2(A)},\varepsilon_{floor})}.
\]

**H2 对一个试件 PASS 当且仅当四项同时满足：**

- `delta_P <= 0.5%`
- `delta_D <= 0.5%`
- `delta_w <= 1.0%`
- `delta_epsilon <= 2.0%`

这些阈值在完整批量结果产生前冻结；后续不得因为试验吻合度改变阈值。

## 8. 样本门禁

收敛审计覆盖全部当前结构族，而不是挑对 H2 有利的代表板：

- Z0-Z5：6/6 全部。
- Swartz1-24：24/24 全部。

`H2_GLOBAL_PASS` 当且仅当 30/30 全部通过第 7 节门禁。

若任一试件 FAIL：

`H2_GLOBAL_FREEZE = NO`。

随后 H4 成为新的最低候选；是否还需 H6 必须另建预冻结 H4->H6 协议后才能计算，不能自动无限升阶。

## 9. 输出要求

每个试件必须输出：

- H2: `Du, qu, Pu, residual norm, audit quadrature refinement error`
- H4: 同上
- `delta_P, delta_D, delta_w, delta_epsilon`
- PASS/FAIL
- 若失败：标明首先失败的 gate，不用试验值解释原因。

批量总表输出：

- 30/30 pass count
- max / median `delta_P`
- max / median `delta_D`
- max / median `delta_w`
- max / median `delta_epsilon`
- `H2_GLOBAL_FREEZE = YES/NO`

## 10. 后续验证与收敛严格分离

只有 H2/H4 truncation order 被上述内部收敛门禁裁决后，才允许另开 validation 表与试验值比较。

因此：

`convergence decision != experimental validation`。
