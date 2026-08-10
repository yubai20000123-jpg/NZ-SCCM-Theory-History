# NZ-SCCM 项目优先级调整：Case21 工程解析收口、材料 operator 重构与总体 solution-operator 架构比较

**日期：2026-08-10**

## 0. 本轮治理结论

当前正式空间约束继续保持：

- ONE_CONTINUOUS_COMPLETE_HALFWAVE
- N_formal_spatial_sampling = 0
- N_formal_spatial_quadrature = 0
- N_formal_spatial_subdomains = 1

但 `TIGHT_STRICT_REMAINDER_CERTIFICATE` 从 Case21 工程生产硬门槛降级为可选数学附录。Case21 正式收口改用 `ENGINEERING_ANALYTIC_CONVERGENCE`：解析阶次由内部收敛指标决定，独立高精度数值积分只在收敛之后用于 audit，不参与选阶、调参或选根。

当前 frozen Nguyen/Foster operator 不再被视为永久最终材料理论。它继续作为 Case21/Swartz benchmark 与解析求解回归基准；新的普通混凝土材料 operator 可以在“只用材料级证据、不用结构承载力反标”的条件下重建。

长期建议采用“双层体系”：

1. Physics / analytic core：材料状态更新 + 连续结构方程 + 规则问题的解析/全局谱求解；
2. General operator surrogate：针对任意几何、边界和荷载的近似 solution operator；它不能被称作严格解析理论。

---

## 1. Case21 工程解析收口规则

### 1.1 正式 evaluator 身份

保持一个完整代表半波、一个统一解析表示。禁止空间 cells、Gauss/Simpson/adaptive quadrature、Chebyshev collocation、material-point grid 进入正式 evaluator。

### 1.2 阶次选择不得参考历史 338/342 或独立 audit

采用纯内部 p-refinement。每一级只增加全域解析阶次，不增加空间子域。解析阶次方向可依据“最后若干 coefficient shells 的内部衰减”选择，但不得依据 audit 误差选择。

### 1.3 建议工程停止准则

对连续三个已接受的全域阶次 N1<N2<N3，要求每次相邻阶次均同时满足：

- Pu 相对变化 <= 0.05%；
- Pc 相对变化 <= 0.05%；
- D 和 q 的相对变化 <= 0.10%；
- 在同一候选根处，Rq 的跨阶次差异除以三个能量项绝对值之和 <= 5e-4；
- 极限条件 L 的归一化残量达到非线性求根内部容差，并且根随阶次稳定。

只有三次连续满足才记为 `ENGINEERING_ANALYTIC_CONVERGENCE_PASS`。

### 1.4 audit 规则

内部 PASS 之后才做独立高精度空间数值积分。audit 不改变阶次、不改变根、不改变材料参数。建议验收：Pu/Pc 正式解析值与 audit 差异 <=0.2%，且远小于材料/模型误差；若超限，则回到解析表示诊断，而不是按 audit 选择“更接近”的阶次。

### 1.5 RC

钢筋保持 exact Ps(D,q), Rq,s(D,q)。RC 重新做同样的三个连续阶次 root convergence；最后重新核验所有钢筋 |eps_s|<0.00265。

---

## 2. strict certificate 的新身份

严格 outward-rounded、theorem-level remainder certificate 不删除，但移入可选数学附录/方法学支线。它适合：

- 给代表算例建立“严格存在区间”；
- 发表解析方法学论文时证明误差；
- 审计新的 coefficient algebra。

它不再阻断 Case21、Swartz 工程验证，只要正式解析误差经内部 p-refinement 和独立 audit 显著小于材料/模型误差。

---

## 3. 材料 operator 与结构 solution operator 必须分离

### 3.1 Material operator

对于一般路径依赖材料，正确接口应是状态更新：

`(sigma_{n+1}, z_{n+1}, C_alg) = M(epsilon_{n+1}, z_n, Delta t, material parameters)`

其中 z 是塑性、损伤、裂缝、硬化等内部变量。只有在单调、无路径依赖的特殊 current-law 近似中，才可以退化成 memoryless `sigma=M(epsilon)`。

### 3.2 Structural solution operator

`S(geometry, material, BC, load fields, imperfections, load history) -> displacement/stress/internal-variable fields, equilibrium path, stability, ultimate load`。

任意边界、任意荷载主要属于结构边值问题的 solution operator 能力，而不是材料函数本身的能力。

---

## 4. A-F 路线结论

### A. 当前 Nguyen algebraic Foster current operator

优点：可解释、低成本、二维多轴 current response 明确、解析矩阵友好，已经形成 Case21/Swartz benchmark。

缺点：当前 frozen 版本是 memoryless current operator，不是任意加载路径材料；没有 free-energy/dissipation 结构；只覆盖当前二维板所需状态；UHPC 不能只换 fc 后直接继承。

**建议身份：长期 benchmark，不再作为“最终统一材料理论”的默认冠军。**

### B. 文献约束的 compact symbolic/rational analytic law

可由三应力不变量的光滑压力敏感强度面（Menetrey-Willam、Ottosen、Bigoni-Piccolroaz 类）+ 少参数 hardening/softening 构成。优点是多轴、光滑、可解释、可能非常适合解析矩阵和全域积分。

但若只做 current envelope，就不能正确描述卸载/重载；若加入塑性/损伤内部变量，它逐渐变成 C 类。

**建议身份：近期最重要的“解析材料桥梁候选”，尤其适合单调稳定/极限问题；不能单独承担一般循环材料。**

### C. generalized-standard-material / energy+dissipation / internal variables

优点：history、热力学和一致切线最完整。Nguyen & Houlsby 2008 已有混凝土专用、基于两个势函数的 coupled damage-plasticity 模型，参数强调从材料试验识别。

关键风险：经典 GSM 的 normality/associated structure 对 concrete dilatancy 可能过强。Grassl-Jirasek/CDPM2 为了混凝土多轴压缩的体积膨胀采用 non-associated flow。因此最终更合理的是“thermodynamic internal-variable core + 可证明 admissible 的 non-associated extension/bipotential/variational extension”，而不是机械地要求所有混凝土必须是 classical GSM。

**建议身份：长期 physics material core 的首选框架，但应允许 C+ 非关联热力学扩展。**

### D. physics-constrained symbolic regression

EUCLID 已演示从 kinematics/reaction data 中发现 free energy、dissipation potential 和 internal variables；2026 的 grammar-based symbolic regression 已直接针对 thermodynamically admissible dissipation potentials。优势是可得到紧凑、可解释的闭式形式。

当前对普通/UHPC 混凝土的直接成熟证据仍不足。因此不能直接生产部署，但非常适合作为“材料级数据 -> compact potential”的发现工具。

**建议身份：作为 C/E 的模型发现工具，而不是自由搜索结构 Pu 的拟合器。**

### E. invariant / tensor-basis constitutive representation

这不是独立材料物理，而是强大的表示层。它把 isotropic/objective tensor map 写成少数 invariants 的标量函数和固定 tensor basis，可显著减少自由度，并有利于 objectivity、symmetry、一致切线和解析矩阵。

**建议身份：应嵌入 B/C/D/F，作为新的材料 operator 的默认表示骨架。**

### F. physics-augmented neural constitutive model

TANN/iCANN/PANN 已展示把 free energy、dissipation、objectivity、convexity 等直接编码到网络结构，并能处理 internal variables/history。能力强，但并不产生适合 Case21 全域解析积分的有限 symbolic operator；训练数据需求和解释成本也更高。

**建议身份：暂不作为 analytic core；以后作为复杂材料 surrogate、跨材料 family surrogate 或 Route 3 solution-operator 的组成部分。**

---

## 5. 普通混凝土/UHPC 材料候选建议

### 5.1 近期 benchmark 组

- A: 当前 frozen Nguyen/Foster current operator；
- CDPM2: 作为成熟 multiaxial damage-plasticity benchmark；
- Nguyen-Houlsby 2008 thermodynamic coupled damage-plasticity：作为 thermodynamic benchmark；
- B 类 smooth invariant elastoplastic/rational law：作为 analytic-compact benchmark。

这些模型必须只用材料级数据校准/识别，不使用 Case21 或 Swartz Pu。

### 5.2 新 operator 的推荐骨架

`invariant/tensor basis (E) + thermodynamic internal variables (C+) + compact scalar potentials (B/D)`。

核心变量建议至少考虑：elastic strain、plastic strain 或等价 inelastic strain、tensile damage、compressive damage、pressure/confinement-sensitive hardening variable；若未来需要循环加载，再加入 crack closure/stiffness recovery 或 kinematic-type history。具体变量数量应由材料试验和 identifiability 决定，不宜提前堆叠。

### 5.3 UHPC

已有上传材料试验证据显示 UHPC 三轴行为显著受围压和钢纤维参数影响，且已有 Willam-Warnke / Drucker-Prager 类 failure criteria 拟合。因此 UHPC 不应仅通过替换普通混凝土的 fc/Ec 来获得。新框架应共享 C+/E 的“理论骨架”，但 scalar potentials/parameters 必须使用 UHPC 自己的单轴、双轴/三轴和拉伸/断裂材料数据确定。

---

## 6. 任意边界/荷载的总体理论架构

### Route 1：一个完整半波 + 全域解析矩阵

定位：规则矩形板、轴压稳定、单/少数已知全局模态。

优势：可审计、物理透明、最快、最接近解析理论。

局限：不应被强迫承担任意几何/边界/荷载。

### Route 2：global Ritz / spectral / operator basis

定位：扩展到更多边界条件、荷载分布和光滑参数化几何。只增加全局解析模态；如果材料有内部变量，相应内部变量场也用全局 basis 表示。

优势：仍保留“全局而非空间 cell”的理论身份，能系统逼近不同 BC/load。

局限：强局部化裂缝、尖角、任意拓扑会使 global basis 阶数快速增长；不能保证成为真正 universal exact solver。

### Route 3：modern neural/operator-learning solver

定位：geometry/BC/load/material parameter -> solution field 的近似 solution operator。

DeepONet/FNO 已奠定 function-to-function operator learning；更新的 geometry-aware/boundary-conditioned neural operators正在针对可变几何和边界条件扩展。

优势：重复推断极快、可覆盖大参数空间。

局限：它是训练分布上的近似 operator；存在 generalization、training-data 和 verification 问题，不能改名为“严格解析理论”。

---

## 7. 推荐双层体系

### Layer A — Physics / analytic core

- C+/E 材料状态更新；
- Route 1 Case21/规则板 exact/engineering-analytic benchmark；
- Route 2 global Ritz/spectral 扩展；
- 输出 residual、energy、tangent、stability、limit state；
- 为实验和高保真 FE 提供物理一致的中间标准。

### Layer B — General operator surrogate

- 学习完整 structural solution operator；
- 输入 geometry/BC/load/material parameters/history；
- 输出 field/path/ultimate-load surrogate；
- 训练数据来自 analytic core + validated FE + experiments；
- 使用 physics residual、energy/dissipation 和 invariance 作为 hard/soft constraints；
- 必须保留 uncertainty/OOD detection，不能覆盖 Layer A 的物理身份。

最终不应强迫 Case21 的一个积分公式承担 arbitrary geometry/BC/load。

---

## 8. 下一阶段路线图

### Phase 0：现在
关闭 Case21 `ENGINEERING_ANALYTIC_CONVERGENCE`：不再死磕 theorem-level tail，按预注册三阶内部收敛准则求 concrete 与 RC root，最后做 audit。

### Phase 1：材料证据矩阵
整理普通混凝土和 UHPC 的材料级证据；明确可用于参数识别的单轴压、单轴拉、双轴压、拉压、三轴围压、卸载/重载、断裂能数据。结构 Pu 全部排除在 calibration 外。

### Phase 2：三模型并行 benchmark
A frozen Nguyen；B compact invariant analytic；C+ thermodynamic internal-variable。E 作为共同 representation。只在材料级测试上比较。

### Phase 3：选材料 core
选择材料精度/解释性/热力学/解析成本的 Pareto winner；D symbolic regression 只在 constrained grammar 中帮助压缩 potentials；F 暂不作为主模型。

### Phase 4：回到结构
将 winner 接入 Route 1 Case21/Swartz，然后推广到 UHPC；对比材料改变是否改善全样本，而不是逐板调参。

### Phase 5：Route 2
建立 general global Ritz/spectral basis，扩展边界、荷载和模态；保持全局 basis 理论，不以空间 cells 为核心。

### Phase 6：Route 3
在物理 core 已稳定后研究 geometry/BC/load neural operator；作为 general surrogate，不冒充 analytic theory。

---

## 9. 最终推荐

1. Case21：立即按 engineering analytic convergence 收口；strict theorem certificate 降级为可选附录。
2. 当前 Nguyen/Foster：保留为 benchmark/regression，不再视为永久 final material law。
3. 新材料长期主线：`C+ thermodynamic internal-variable framework + E invariant/tensor basis`。
4. B compact symbolic/rational law：作为解析友好、单调多轴问题的重要竞争候选/桥梁。
5. D：作为 constrained discovery layer；禁止使用结构 Pu 训练。
6. F：后置；只有材料数据和物理基准足够时再研究。
7. 总体结构：Route 1 + Route 2 组成 physics/analytic core，Route 3 为独立近似 solution-operator layer。

---

## 10. 主要文献索引（用于后续独立审核）

- Menétrey, P.; Willam, K.J. (1995). *Triaxial Failure Criterion for Concrete and its Generalization*. ACI Structural Journal 92(3), 311–318.
- Ottosen, N.S. (1977). *A Failure Criterion for Concrete*. Journal of Engineering Mechanics 103(4), 527–535.
- Poltronieri, F.; Piccolroaz, A.; Bigoni, D. (2014/2016). *A simple and robust elastoplastic constitutive model for concrete*.
- Grassl, P.; Jirásek, M. (2006). *Damage-plastic model for concrete failure*. International Journal of Solids and Structures 43, 7166–7196.
- Grassl, P.; Xenos, D.; Nyström, U.; Rempling, R.; Gylltoft, K. (2013). *CDPM2: A damage-plasticity approach to modelling the failure of concrete*. International Journal of Solids and Structures 50, 3805–3816.
- Einav, I.; Houlsby, G.T.; Nguyen, G.D. (2007). *Coupled damage and plasticity models derived from energy and dissipation potentials*. International Journal of Solids and Structures 44, 2487–2508.
- Nguyen, G.D.; Houlsby, G.T. (2008). *A coupled damage–plasticity model for concrete based on thermodynamic principles: Part I: model formulation and parameter identification*. IJNAMG 32, 353–389.
- Flaschel, M.; Kumar, S.; De Lorenzis, L. (2023). *Automated discovery of generalized standard material models with EUCLID*. CMAME 405, 115867.
- Califano, F.; Ciambella, J. (2026). *Discovering Thermodynamically Admissible Dissipation Potentials via Grammar-Based Symbolic Regression*.
- Fuhg, J.N.; Bouklas, N.; Jones, R.E. (2022/2023). tensor-basis constitutive representation papers.
- Masi, F.; Stefanou, I.; Vannucci, P.; Maffi-Berthier, V. (2020). *Thermodynamics-based Artificial Neural Networks for constitutive modeling*.
- Holthusen, H. et al. (2024). *Theory and implementation of inelastic Constitutive Artificial Neural Networks*. CMAME 428, 117063.
- Lu, L. et al. (2021). *Learning nonlinear operators via DeepONet based on the universal approximation theorem of operators*.
- Li, Z. et al. (2021). *Fourier Neural Operator for Parametric Partial Differential Equations*.
- Zhong, W.; Meidani, H. (2024). *Physics-Informed Geometry-Aware Neural Operator*.
