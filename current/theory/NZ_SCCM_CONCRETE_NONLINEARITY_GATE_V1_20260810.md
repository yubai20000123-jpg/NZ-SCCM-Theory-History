# NZ-SCCM 混凝土强非线性解析材料门禁 V1

**日期：2026-08-10**  
**身份：CURRENT MATERIAL-ARCHITECTURE GATE / USER CORRECTION INCORPORATED**

## 0. 为什么必须新增此门禁

用户明确指出：本项目目标是混凝土板极限承载力；混凝土在峰值附近及峰后具有很强非线性，因此不能先用一个 generic low-order material law 把数学流程做通，再假定真实混凝土以后自然可以塞进去。

本文件据此修正执行策略：

```text
LOW_ORDER_GENERIC_MATERIAL = ALGEBRA_UNIT_TEST_ONLY
LOW_ORDER_GENERIC_MATERIAL != ARCHITECTURE_FEASIBILITY_PROOF
```

新的解析矩体系只有在**真实强非线性材料层也能闭合**时才可进入生产。

---

## 1. 两个门槛必须同时满足

### Gate A — exact analytic integration

正式结构结果必须满足：

```text
one continuous complete halfwave
zero spatial sampling
zero spatial quadrature
one spatial subdomain
no element integration
finite exact analytic moments
```

### Gate B — concrete nonlinear adequacy

候选材料 operator 必须在材料级证据上同时表达极限承载力真正需要的非线性，而不是只有小应变弹性或弱非线性。

至少需要覆盖：

1. 初始弹性刚度与 Poisson coupling；
2. 单轴压缩明显非线性上升段；
3. 压缩峰值强度与峰值应变；
4. 峰后下降 / softening；
5. 单轴拉伸开裂前、峰值及开裂后软化或 UHPC strain-hardening/localization；
6. 双轴压缩强度增强；
7. tension-compression coupling / compression softening；
8. 必要的 TT / confinement / triaxial 约束；
9. 与同一 stress law 一致的解析 tangent；
10. 若最终材料证据要求 history/path dependence，则必须有有限全局解析 internal-variable representation，不能退回材料点状态机。

具体误差阈值必须按材料级试验散布和来源精度制定；不得用 Case21、Swartz24、UCFT 的结构 Pu 反标或选阶。

---

## 2. 对 V1 `sigma=A I+B X` 的修正理解

二维各向同性同轴映射写成

\[
\widehat{\boldsymbol\sigma}=A(I_1,I_2)\mathbf I+B(I_1,I_2)\mathbf X
\]

只是**张量表示定理/接口骨架**，不等于要求 `A,B` 必须是低阶二维自由多项式。

真正材料模型可采用更有物理结构、但最终仍能化为有限矩阵/不变量多项式的形式，例如：

### 2.1 强非线性一维骨架 + 低阶多轴修正

\[
\widehat{\boldsymbol\sigma}
=p(\mathbf X)
+A_c(I_1,I_2)\mathbf I
+B_c(I_1,I_2)\mathbf X,
\]

其中

\[
p(\mathbf X)=\sum_{k=0}^{p}c_k\mathbf X^k
\]

负责压缩峰值/峰后与拉伸非线性主形状；二维 Cayley-Hamilton 可把任意有限 `X^k` 重新压缩到 `I` 与 `X` 两个张量基，因此不会破坏精确矩闭合。

### 2.2 shape-constrained global polynomial / Bernstein basis

可在单一材料 invariant domain 上采用 Bernstein、Chebyshev 或其他有限 polynomial basis。其选择目的不是空间逼近，而是材料级非线性表示；所有 basis 必须最终有限展开为 `I1,I2` 多项式并进入 exact moments。

Bernstein 类 basis 的潜在优势是可以在材料参数识别中施加单调性、峰值、softening 等 shape constraints，避免自由高阶 monomial 的严重振荡。

### 2.3 禁止用 material piecewise branch 重新制造空间分区

如果一个材料分段定义要求在结构域中先寻找 `TT/TC/CC/...` 区域并分别积分，那么它会重新引入未知空间 branch front / subdomain integration。

V1 优先寻找**单一全局解析 material map**。若以后必须引入内部状态，则状态场也必须使用有限全局解析 basis，而不是 material-point grid。

---

## 3. 立即执行的 frozen-NC 强非线性诊断

### 3.1 目的

不是把 frozen Nguyen/Foster current operator 继续指定为最终材料真理，而是利用它已经具备的强 tension/compression/biaxial nonlinear response，测试“低阶 generic invariant A/B surface 足够”这一假设。

### 3.2 严格避免结构反标

本诊断：

- 不使用 Case21 `Pu`；
- 不使用 Swartz24；
- 不使用空间 `X,Y,zeta`；
- 不根据结构应力状态选材料系数；
- 仅在**材料主应变空间**调用 frozen NC operator。

### 3.3 诊断域

采用归一化原始主应变

\[
e_i=\varepsilon_i/\varepsilon_0,
\]

并取一个故意较宽的材料诊断方域

\[
(e_1,e_2)\in[-2.0,0.6]^2.
\]

这不是正式材料有效域冻结，只是覆盖明显压缩峰后、拉伸与多轴组合的 stress-test domain。

使用对称 invariant coordinates

\[
\mu=(e_1+e_2)/2,
\qquad
r^2=((e_1-e_2)/2)^2,
\]

其中 `mu,r^2` 与 `I1,I2` 多项式等价。

拟合

\[
s_i=A(\mu,r^2)+B(\mu,r^2)e_i
\]

并让 `A,B` 使用总阶 `p` 的全局 Chebyshev polynomial basis。训练和检验都仅发生在材料空间。

### 3.4 结果

误差以下均为归一化应力 `sigma/fc` 的绝对误差：

| total degree p | total A+B coefficients | design-matrix cond. | mean abs. error | 95% abs. error | max abs. error |
|---:|---:|---:|---:|---:|---:|
| 2 | 12 | 5.23e1 | 0.1319 | 0.3025 | 0.6156 |
| 4 | 30 | 8.24e2 | 0.0709 | 0.2636 | 0.5819 |
| 6 | 56 | 1.73e4 | 0.0485 | 0.1995 | 0.4903 |
| 8 | 90 | 3.79e5 | 0.0424 | 0.1778 | 0.4625 |
| 10 | 132 | 8.17e6 | 0.0329 | 0.1257 | 0.4268 |
| 12 | 182 | 1.99e8 | 0.0316 | 0.1326 | 0.4157 |

### 3.5 本诊断允许得到的结论

\[
\boxed{
\text{naive low/moderate-degree free A/B surface is rejected as the architecture proof}
}
\]

即：虽然所有有限阶 polynomial 都可精确积分，但“可积”不等于“足以描述混凝土极限状态”。总阶提高到 10–12 后，误差改善已经变慢，而且自由系数问题的条件数恶化很快。

### 3.6 本诊断不能得到的结论

它**不能证明所有 global polynomial concrete laws 都失败**，因为：

- frozen NC operator 本身不是最终材料真理；
- 诊断域是人为 stress-test domain；
- 本次只测试了自由 total-degree surface，没有加入 peak/softening/strength-envelope 等物理结构；
- 没有测试 shape-constrained Bernstein、structured matrix polynomial、internal-variable compact law。

因此下一步不是放弃解析矩，而是设计**物理结构化的强非线性有限解析材料 basis**。

---

## 4. 新材料候选的正式验收顺序

每个 NC/UHPC 候选必须按以下顺序：

1. **材料来源冻结**：确定允许用于识别的单轴压、单轴拉、CC、TC、TT、三轴/围压、峰后数据；
2. **material-domain representation**：构造 finite analytic law；
3. **材料非线性 Gate B**：检查 peak、postpeak、tension、biaxial interaction、tangent；
4. **exact-moment Gate A**：证明与 Case21 finite kinematics 复合后属于 finite exact moment algebra；
5. 只有 A+B 都通过，才进入 Case21；
6. Case21/Swartz 只做结构验证，不反馈修改材料参数。

---

## 5. 下一步具体研究对象

不再做 generic low-order material toy 作为主任务。

下一步直接比较两种强非线性、同时保持 exact moments 的材料骨架：

### Candidate M1 — structured matrix polynomial

- 高阶一维/矩阵 polynomial 捕捉 tension/compression peak/postpeak；
- 低阶 invariant corrections 捕捉 CC/TC/TT interaction；
- 全部通过 Cayley-Hamilton 化为有限 `A I+B X`；
- 参数来自材料级来源。

### Candidate M2 — global shape-constrained invariant Bernstein

- 单一材料域；
- 全局 polynomial，因此严格 exact-moment compatible；
- 用 control coefficients 施加初始刚度、peak、softening、biaxial-strength 等 shape constraints；
- 不做 material-state spatial partition。

如果 M1/M2 在材料级强非线性 gate 下都需要不可接受的阶次或不能保持物理一致性，则当前 memoryless current-map V1 应判失败，转入有限全局 internal-variable C+ architecture；**失败也不允许回到 element/material-point integration。**
