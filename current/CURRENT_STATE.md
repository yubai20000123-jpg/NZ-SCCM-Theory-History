# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-10 20:56 +08:00  
**Purpose:** 唯一当前工作入口。详细推导、失败路线和执行历史留在 canonical theory/history/evidence 文件中。

## 0. 最高优先级：EXPLICIT END-TO-END CAPACITY

Canonical governance：

- `governance/EXPLICIT_END_TO_END_CAPACITY_DOCTRINE_20260810.md`
- `history/NZ_SCCM/EXPLICIT_CAPACITY_PRIORITY_AND_MATERIAL_UNDERUSE_RESET_20260810.md`

用户最新澄清覆盖此前对 compiler/current-map 形式的过度执着：

```text
唯一最高要求 = 最终极限承载力必须由显式公式及同一公式的显式导数得到。
```

允许的中间数学表示不再预先锁死。可以使用：

- 4D `(eps1,eps2,sigma1,sigma2)` stress-strain manifold；
- invariant current map；
- principal/spectral representation；
- whole-domain/global target function；
- low-rank/separable surface；
- polynomial/rational/algebraic formula；
- named special functions with explicit derivatives；
- local analytic patches；
- 其他能够显式传播到最终容量方程的数学表示。

材料曲面中的局部尖峰、切口、脊线、过窄 transition、局部振荡不再要求逐点复现。允许像处理试验尖峰一样，**有意不使用全部峰值/局部尖锐能力**，通过简单显式曲线/曲面做 controlled under-use / smoothing / contraction。每次简化必须报告其力学后果：压缩降低、拉伸降低、TT/TC 降低、增强或 mixed，以及导数变化。

材料拟合的目标不再是最小 pointwise regression error，而是：

```text
物理可控 + 透明 + 导数显式 + 最终容量显式 + 结构验证可接受
```

---

## 1. 最终结构目标

当前容量方程仍采用：

\[
P(D,q),\qquad R_q(D,q)=0,
\]

\[
L(D,q)=P_{,D}R_{q,q}-P_{,q}R_{q,D}=0,
\]

最终：

\[
P_u=P(D^*,q^*)
\]

其中 `(D*,q*)` 必须来自显式平衡/驻值方程的 admissible real root。`P,Rq` 及 `P_,D,P_,q,Rq_,D,Rq_,q` 必须从同一显式数学表示解析获得。

结构层仍保留：

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
ACTIVE_MODE = m=1
KINEMATICS = NGUYEN_SECOND_ORDER
```

正式 production operator 不得依赖隐藏的 material-point propagation、黑箱 numerical differentiation 或黑箱 numerical integral。数值求根可用于求解已经显式得到的有限方程，但不能替代公式本身。

---

## 2. 旧主线的当前身份

以下均保留为工具/证据，不再拥有“必须继续使用”的排他身份：

```text
G18/G27 invariant current-map architecture = RETAINED TOOL
G20/G21 smooth conservative material philosophy = RETAINED
G26 moment-first D15 architecture = RETAINED TOOL
G28/G30 direct analytic P,Rq,L kernel = RETAINED
R03 exact rank<=4 spectral factorization = RETAINED TOOL
R04 Appell/Carlson classification = RETAINED KERNEL LIBRARY
R05 softsign compactification = CANDIDATE ONLY
R06 direct polynomial / Möbius head-to-head = CANDIDATE EVIDENCE ONLY
```

此前 compiler failure 不得再升级为 material/current-map architecture failure；反之，也不得为了保留某个 compiler 而增加材料面复杂度。

---

## 3. 材料数据处理新原则

一个 source/experiment feature 可以分成：

1. **HARD LANDMARKS**：必须保留或明确给出 deliberate reduction；例如初始切线、主要压缩峰、主要拉伸峰、残余水平、关键多轴强度锚点；
2. **OPTIONAL SHARP FEATURES**：局部尖口、脊线、过窄 transition、测得但不希望完全利用的峰值；
3. **ANALYTIC PATCHES**：用简单显式曲线/曲面替代 optional feature；
4. **MECHANICAL CONSEQUENCE LABEL**：明确该 patch 对 CC/TC/TT、压缩/拉伸、切线和容量的影响。

允许 deliberately under-use material peak，例如：

```text
measured/source peak = 1.00
analytic design target = 0.95
```

只要这种降低是明确、可解释并在结构验证中评估，而不是隐藏调参。

结构试验结果只能在材料 target 冻结以后用于 validation；不得用 Pu 反向决定局部 patch 的隐蔽参数。

---

## 4. MATERIAL-NATIVE DOMAIN GOVERNANCE 保留

```text
PRIMARY_DOMAIN   = MATERIAL_ADMISSIBLE_SPECTRAL_DOMAIN Lambda_M
SECONDARY_DOMAIN = STRUCTURAL_REACHABLE_SUBDOMAIN Lambda_R
MANDATORY        = Lambda_R subset of Lambda_M
```

Case21/Swartz24 不能定义 production material domain。NC 与 UHPC 可以有不同 `Lambda_M` 和不同 surface/patch 参数，但最终必须能通过同一类 explicit-capacity workflow 输出 `P,Rq,L,Pu`。

当前 NC source-active interval 仍保留为材料来源尺度参考：

\[
\Lambda_{M,NC}^{active}=[-\gamma_2,\alpha_1\rho/\kappa]
=[-10,0.49987179453974245].
\]

这不是禁止更简单 target 的拟合域，而是来源 landmark 的材料尺度记录。

UHPC 禁止继承 NC 数值谱域；必须由 UHPC source/model 独立定义。

---

## 5. R06 仍然有效的材料结果

R06 已建立 NC 压缩峰后的 source-faithful C2 endpoint regularization：

```text
g(tau)=3 tau^5-8 tau^4+6 tau^3
delta_s=0.05
max local extra compression vs source = 0.888889% fc
U(-1)=-1, U'(-1)=0
U(-10)=-0.1, U'(-10)=0
```

```text
NC_POSTPEAK_C2_SCALAR_TARGET = PASS AS ONE ACCEPTABLE DATA-PROCESSING OPTION
```

但它不再是唯一允许的 postpeak representation；若后续得到更简单且同样透明的 explicit patch，可替代。

---

## 6. 3D/4D 可视化规则

讨论材料面形状、局部尖口和平滑后果时，优先使用：

1. `sigma1(eps1,eps2)` 三维曲面 + `eps1-eps2 / eps1-sigma1 / eps2-sigma1` 三正交投影；
2. `sigma2(eps1,eps2)` 同样格式；
3. baseline vs patched difference surface；
4. CC/TC/TT 区域机械后果标签。

UHPC 当前完整 `(eps1,eps2)->(sigma1,sigma2)` operator 尚未冻结，禁止为了图形完整性虚构正式 UHPC surface。

---

## 7. Gate 重新解释

### Gate A — END-TO-END EXPLICITNESS

必须得到显式：

\[
\sigma(\varepsilon),\quad \partial\sigma/\partial\varepsilon,
\quad P(D,q),\quad R_q(D,q),
\quad P_{,D},P_{,q},R_{q,D},R_{q,q},L(D,q).
\]

### Gate B — MATERIAL ADEQUACY

不是追求 source pointwise minimum error，而是保留/明确降低关键材料 landmarks，确保 patch 后的压缩、拉伸、TT/TC 后果可解释并在允许误差内。

### Gate C — FORMULA COMPLEXITY

显式公式必须足够透明和可审计。大 PF/Gauss-Manin/隐藏 ODE/黑箱积分仍不应成为 production operator。named special functions 可接受的前提是公式及导数身份直接、有限、稳定。

---

## 8. Case21 / Swartz24 / UHPC status

```text
Case21 = analytic benchmark; no new final RC Pu frozen
old 338/342 kN = audit/reference only
G31 476.936 kN = uncracked chain validation only
Swartz24 production Pu = PAUSED
```

NC：允许 deliberate material under-use / smoothing；下一步先做 explicit surface simplification，再进入 capacity validation。

UHPC：`fc=141.1 MPa` 用户强制保留；完整多轴 current surface 仍 OPEN。UHPC 后续也允许相同“source peak != 必须全部利用”的 data-processing philosophy，但必须从 UHPC source landmarks 自己建立 target。

Reinforcement 仍必须在 root solve 前进入：

\[
P=P_c+P_s,\qquad R_q=R_{q,c}+R_{q,s}.
\]

---

## 9. 当前下一任务

```text
CURRENT_RECOMMENDED_NEXT_TASK
= EXPLICIT_SURFACE_SIMPLIFICATION_AND_CAPACITY_CHAIN_R07R
```

不再把 `GLOBAL_POLY64 vs MOBIUS24` 当唯一下一任务。新的 R07R 先做：

1. NC current surface 上识别少数真正需要处理的局部尖峰/切口/脊线；
2. 对每个 feature 只给 2-3 个低参数显式 patch（例如 polynomial/Hermite/Bernstein/logistic/saddle-like/global surface 等）；
3. 明确 patch 对 `fc/ft/CC/TC/TT/tangent` 的影响方向和幅值；
4. 只保留导数显式且能够直接传播到 `P,Rq,L` 的候选；
5. 选择材料 target 后再做 Case21 -> Swartz24 structural validation；
6. UHPC 在 source-complete 后沿同一显式容量方法建立自己的 surface target。

禁止：为了极小 material regression error 再制造高复杂度 compiler；禁止在材料 target 未冻结前用 Pu 隐蔽调参。

---

## 10. 恢复读取顺序

1. `current/CURRENT_STATE.md`
2. `governance/EXPLICIT_END_TO_END_CAPACITY_DOCTRINE_20260810.md`
3. `history/NZ_SCCM/EXPLICIT_CAPACITY_PRIORITY_AND_MATERIAL_UNDERUSE_RESET_20260810.md`
4. `governance/MATERIAL_NATIVE_SPECTRAL_DOMAIN_RULE_20260810.md`
5. R06 NC postpeak/representation evidence
6. R03-R05 dimensional-reduction / special-function evidence
7. 3D current-map visualization evidence
8. `governance/EXPLICIT_EXECUTION_EVIDENCE_RULE_20260810.md`
9. Case21 invariant derivation + Nguyen Ch.3 source evidence
