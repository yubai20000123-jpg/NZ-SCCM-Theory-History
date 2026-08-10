# NZ-SCCM Case21 单完整半波零空间离散解析求解：总体审核交接包

**日期：2026-08-09**  
**用途：供新的独立对话只读审核当前 NZ-SCCM Case21 数学求解链。**  
**要求审核者：不要默认相信本文件结论；应逐项核对冻结理论、源码、数学变换、被废止路径与当前未闭合项。**

---

## A. 唯一理论合同

唯一正式材料/结构合同：`NZ_SCCM_CURRENT_OPERATOR_EXPLICIT_NC_REBAR_V1_20260809.md`。

普通混凝土必须原样使用：equivalent-uniaxial tensor → λ± → Pi_eta → Saenz C → Foster algebraic H/T → U → CC/TC/TT interaction → spectral return。正式 tension law 为 algebraic Foster H(r,r0;0.05)，严禁 tanh variant。

Case21 结构目标是完整连续半波上的 Pc(D,q) 与 Rq,c(D,q)。钢筋采用冻结 Nguyen bilinear law；Case21 两向每层钢筋率各 0.00375，z_s=0。

---

## B. 当前正式空间合同

自 2026-08-09 最新修正起，正式空间身份永久按当前分支锁定：

- `ONE_CONTINUOUS_COMPLETE_HALFWAVE`；
- `N_formal_spatial_sampling = 0`；
- `N_formal_spatial_quadrature = 0`；
- `N_formal_spatial_subdomains = 1`。

这里的 subdomain=1 指完整连续代表半波本身。任何 fixed/adaptive analytic cells、seed partition、NeedSplit、convergence/branch-driven spatial subdivision 都不具有正式身份。

---

## C. 历史数值只允许做 verification

历史不同实现曾得到大致：

- concrete-only ~338.318 kN；
- RC ~342.334 kN；
- 更早 moment-first D15 concrete ~339.1 kN。

这些数值不得用于当前全域表示的系数生成、阶数选择、根选择、材料校准或反标，只能在最终正式结果完成后核对。

---

## D. 已保留且通过的代数成果

1. tangent-half-angle exact transformation；
2. quadrant-sine exact transformation；
3. 11 textual radicals 压缩为依赖明确的 algebraic generator tower；
4. `t-c` exact identity；
5. simplified U identity；
6. simplified Foster T identity；
7. spectral radical rationalization；
8. Foster degree-10 branch polynomials；
9. generic high-genus Abelian-integral diagnosis；
10. exact elastic reinforcement Ps(D,q), Rq,s(D,q)。

上述均是同一个 frozen operator 的恒等整理，不是材料 surrogate。

---

## E. 谱表观奇异性已正式消除

原 spectral return 中 `(s+ - s-)/(2R)` 在 R→0 看似 0/0。现已改写为 symmetric divided difference：

- even part A_F(mu,R²)；
- divided-difference part D_F(mu,R²)。

D_F 在 R²=0 有正常解析极限 F'(mu)。

更进一步，完整 frozen interaction 可写成无 1/R 的等价矩阵函数：

`S = U - acc det(C) C + tr(T) C - C T - rho_m a_t det(T)[tr(T^7) I - T^7]`。

因此 R≈0 不能再成为任何 spatial split 的理由。

---

## F. 当前单域全局解析表示

当前 prototype 在整个 `[0,1]×[0,1]×[-1,1]` 只使用一个 multivariate Chebyshev series：

`F = Σ c_ijk T_i(2a-1) T_j(2b-1) T_k(zeta)`。

**关键区别：系数不是空间节点采样/DCT得到。** 系数由 frozen algebraic formulas 在 coefficient space 中通过加法、Chebyshev convolution、reciprocal/sqrt/power recurrences、pair algebra 构造。

积分使用 exact analytic moments，因此正式空间 sampling/quadrature 均为 0。

---

## G. 已完成的独立实现诊断

独立状态 D=0.75,q=0.002，不靠 Case21 历史 peak 构造。

### G1. Scalar frozen material convergence

统一 scalar spectral interval 上 C/T/U tail 随 degree 1024→1536→2048 从约 1e-4 降至约 1e-7。这证明 scalar Foster material map 本身可做高精度全域解析系数表示。

### G2. 单域 Pc

旧 isotropic global degree 20：Pc≈335.141710 kN；独立 numerical audit only≈335.13308 kN，显示 Pc 已接近。

### G3. 单域 Rq

同一 degree 20：Rq≈39678，而 audit only≈38989，约 1.8% 差异。因此尚不能正式求 Rq=0。

### G4. 各向异性 p-refinement

若只增加全域 degree、不切空间，部分 degree 组合可使 Rq 接近 audit，但变化非单调；因此不允许按“最接近 audit”选择 degree。

---

## H. 本轮严格尾项尝试与否定结果

### H1. 单一 Chebyshev l1 Banach tail

建立 finite coefficients + scalar l1 tail，严格覆盖 high-high→low feedback。数学上安全，但对 Rq 的界极端过宽（数量级百万），不能作为有效 certificate。

**结论：不是 Banach algebra 思想错误，而是把所有空间方向/谱分支/模态结构压成一个标量 tail 太粗。**

### H2. Padded nonlinear multiplication

仅扩大 nonlinear product 工作 degree 而不补真实输入高阶 modes，会产生严重伪反馈甚至爆炸，已废止。

### H3. Direct radical Newton/Zolotarev-like iteration on truncated fields

低阶 truncated global fields 不能保证正 radicand 的 positivity，迭代可发散。未经过 validated tail 前不得作为正式路径。

---

## I. 关键新结构：两个 principal spectral intervals 分离

对 D=0.75,q=0.002 可用纯解析界获得 λ+ 与 λ- 的两个分离区间。甚至在较宽参数盒 D∈[0.5,0.9], q∈[0,0.003]，delta 的解析下界仍约 0.22599>0。

这意味着：当前 scalar material series 若覆盖从 λ- 最小值到 λ+ 最大值的整段连续区间，会无谓逼近一个实际不访问的大空白谱区间。

**建议下一数学主线：** 在不做空间 sampling、不分空间域的前提下，对两个分离谱区间建立具有显式统一误差的 rational / polynomial functional calculus；优先研究 Zolotarev/Akhiezer 类 minimax rational representation 或等价的 disconnected-set approximation。它不是空间分片；被逼近对象仍是同一个 frozen material function，空间域仍为一个完整半波。

必须防止它退化为“拟合材料 surrogate”：系数必须来自解析公式/定理，误差必须有全域显式界，不得来自空间采样或 Case21 peak calibration。

---

## J. 当前未实现目标

目前**尚未**得到同时满足以下全部条件的 production evaluator：

1. one complete halfwave；
2. zero spatial sampling/quadrature；
3. one spatial subdomain；
4. Pc 与 Rq,c 均达到正式收敛；
5. nonlinear coefficient truncation 有足够紧的严格 global bound；
6. 可据此正式求 concrete root 和 RC root。

因此当前没有发布新的正式 Case21 Pu。

---

## K. 下一步建议与审核重点

审核者应重点判断：

1. spectral regularization 是否严格等价于 frozen M_NC；
2. 当前 coefficient generation 是否真的没有空间 sampling；
3. analytic moment contraction 是否保持 subdomains=1；
4. 单一 l1 tail 为何过松；
5. 两个 principal spectral intervals 的解析分离是否在所需 `(D,q)` root enclosure 内成立；
6. 是否可以利用 disconnected spectral set 的 theorem-based rational approximation，在不制造材料 surrogate 的前提下显著降低全域 degree；
7. 后续 certificate 应优先使用 a-posteriori residual/radii-polynomial 型验证，还是更细的 multi-index/anisotropic weighted Banach tail；
8. 在 certificate 关闭以前不得借用历史 338/342 数字选根。

---

## L. 推荐给新审核对话的首条指示词

> 你现在是“NZ-SCCM Case21 单完整半波零空间离散解析理论独立审计助手”。请把上传的 `NZ_SCCM_CASE21_GLOBAL_AUDIT_HANDOFF_20260809.md` 作为阶段事实索引，但不要默认其结论正确。首先读取冻结 `NZ_SCCM_CURRENT_OPERATOR_EXPLICIT_NC_REBAR_V1_20260809.md`，然后逐项审计 spectral regularization、single-domain coefficient construction、exact moment contraction、tail propagation 失败诊断和 principal spectral interval separation。严格检查当前路径是否真正满足 `N_formal_spatial_sampling=0`, `N_formal_spatial_quadrature=0`, `N_formal_spatial_subdomains=1`。尤其判断下一步使用 theorem-based Zolotarev/Akhiezer rational functional calculus 与 a-posteriori/radii-polynomial validation 是否仍保持 frozen material identity，而不是形成 material surrogate。不要使用历史 338.3175/342.3332 kN 来选方法或选根；它们仅可在最终独立结果形成后核验。
