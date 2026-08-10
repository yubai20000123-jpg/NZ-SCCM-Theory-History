# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-10 21:02 +08:00  
**Purpose:** 唯一当前工作入口。详细推导、历史偏离/恢复、失败 compiler 与执行证据留在 canonical governance/theory/history/evidence 文件中。

## 0. 最高优先级：EXPLICIT END-TO-END CAPACITY

Canonical：

- `governance/EXPLICIT_END_TO_END_CAPACITY_DOCTRINE_20260810.md`
- `governance/EXPLICIT_SURFACE_GLOBAL_TARGET_R07R_RULE_20260810.md`
- `current/theory/NZ_SCCM_EXPLICIT_SURFACE_SIMPLIFICATION_AND_CAPACITY_CHAIN_R07R_20260810.md`
- `current/theory/NZ_SCCM_EXPLICIT_SURFACE_SIMPLIFICATION_AND_CAPACITY_CHAIN_R07R_results.json`
- `current/theory/NZ_SCCM_R07R_EXPLICIT_GLOBAL_P_RQ_COEFFICIENTS.json`
- `history/NZ_SCCM/R07R_EXPLICIT_SURFACE_AND_CAPACITY_CHAIN_20260810.md`

用户当前最高要求：

```text
最终极限承载力必须由显式公式及同一公式的显式导数得到。
```

允许使用 4D stress-strain manifold、invariant/spectral current map、whole-structure global target、低秩面、polynomial/rational/algebraic formula、named special functions、局部 analytic patch 等。材料 pointwise regression error 不再是首要目标；允许 deliberate under-use / smoothing / trimming 局部尖峰，只要后果透明、导数显式、最终结构验证可审计。

---

## 1. 最终容量方程

\[
P(D,q),\qquad R_q(D,q)=0,
\]

\[
L(D,q)=P_{,D}R_{q,q}-P_{,q}R_{q,D}=0,
\]

\[
P_u=P(D^*,q^*).
\]

`P,Rq,P_,D,P_,q,Rq_,D,Rq_,q` 必须来自同一显式数学表示。

结构层继续保留：

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
ACTIVE_MODE = m=1
KINEMATICS = NGUYEN_SECOND_ORDER
```

正式 production operator 不得依赖隐藏 material-point propagation、黑箱 numerical differentiation 或黑箱 numerical integral。数值求根可用于求已经显式得到的有限方程。

---

## 2. 材料处理原则

材料 source/experiment feature 分成：

1. `HARD LANDMARKS`：初始切线、主要压缩/拉伸峰、残余水平、必要多轴锚点；
2. `OPTIONAL SHARP FEATURES`：局部尖峰、切口、脊线、过窄 transition、局部振荡；
3. `ANALYTIC UNDER-USE/PATCH`：可主动削低、圆滑或替代 optional feature；
4. `MECHANICAL CONSEQUENCE`：必须报告压缩降低、拉伸降低、TC/TT 改变、enhancement 或 mixed 及导数影响。

允许例如：

```text
source/measured peak = 1.00
explicit analytic target = 0.95
```

结构试验值只能在材料 target 先冻结以后用于 validation，禁止隐蔽反标局部 patch。

---

## 3. MATERIAL-NATIVE DOMAIN GOVERNANCE

```text
PRIMARY_DOMAIN   = MATERIAL_ADMISSIBLE_SPECTRAL_DOMAIN Lambda_M
SECONDARY_DOMAIN = STRUCTURAL_REACHABLE_SUBDOMAIN Lambda_R
MANDATORY        = Lambda_R subset of Lambda_M
```

Case21/Swartz24 不能定义 production material domain。NC 与 UHPC 可有不同 `Lambda_M`、不同 surface/patch 参数，但最终必须进入同一类 explicit-capacity workflow。

NC source-active landmark interval 仍记录为：

\[
\Lambda_{M,NC}^{active}=[-10,0.49987179453974245].
\]

UHPC 禁止继承 NC 数值谱域。

---

## 4. R07R — 显式低参数材料面

R07R 不再超贴合旧 `Pi/H/T/T^8` 尖锐结构。采用最小 scalar spectral family：

\[
u(\lambda)=\lambda\frac{N_5(\lambda)}{D_6(\lambda)},
\]

\[
N_5=\kappa+a_1\lambda+a_2\lambda^2+a_3\lambda^3+a_4\lambda^4+a_5\lambda^5,
\]

\[
D_6=1+b_1\lambda+b_2\lambda^2+b_3\lambda^3+b_4\lambda^4+b_5\lambda^5+b_6\lambda^6.
\]

显式导数：

\[
u'(\lambda)=\frac{(N+\lambda N')D-\lambda ND'}{D^2}.
\]

最小 current surface：

\[
\boxed{\boldsymbol\sigma=f_c\,u(\mathbf E_u)}.
\]

没有 runtime TT/TC/CC state machine；没有额外 `J2/CC/TC` enhancement。后者不是永久删除，而是只有当结构验证证明缺失时才允许最小补充。

R07R 三个候选在查看 Case21 实验值之前冻结：

```text
A_FC100_FT90 : compression peak 100%, tension peak 90%
B_FC97_FT90  : compression peak 97%,  tension peak 90%
C_FC95_FT80  : compression peak 95%,  tension peak 80%
```

执行材料结果：

```text
A: min compression = -1.000300 fc ; max tension = +0.091368 fc
B: min compression = -0.970283 fc ; max tension = +0.091388 fc
C: min compression = -0.950244 fc ; max tension = +0.081494 fc
```

三个候选在材料识别区间内 denominator 均保持正值，无 pole crossing。

---

## 5. R07R — whole-structure 显式 P/Rq target

对每个已冻结材料候选建立：

\[
\boxed{P(D,q)=\sum_{i=0}^{10}\sum_{j=0}^{10}p_{ij}T_i(\xi_D)T_j(\xi_q)}
\]

\[
\boxed{R_q(D,q)=\sum_{i=0}^{10}\sum_{j=0}^{10}r_{ij}T_i(\xi_D)T_j(\xi_q)}
\]

```text
D in [0.35,1.40]
q in [0.003,0.033]
P coefficient count  = 121
Rq coefficient count = 121
```

完整 coefficient matrices 已存：

`current/theory/NZ_SCCM_R07R_EXPLICIT_GLOBAL_P_RQ_COEFFICIENTS.json`

`P_,D,P_,q,Rq_,D,Rq_,q` 均由同一 Chebyshev arrays 解析求导；随后直接形成 `L`。

独立 off-grid 验证：

```text
A: P max abs 3.709 kN; P95 1.644 kN; Rq max 0.448 kN
B: P max abs 3.758 kN; P95 1.619 kN; Rq max 0.455 kN
C: P max abs 3.559 kN; P95 1.906 kN; Rq max 0.421 kN
```

---

## 6. R07R Case21 concrete-only 显式驻值根

从同一显式 `P,Rq,L` 直接求：

| candidate | D* | q* | A* (mm) | Pu explicit (kN) | independent material-surface audit P (kN) |
|---|---:|---:|---:|---:|---:|
| A_FC100_FT90 | 0.914265 | 0.0210447 | 25.6745 | 317.4186 | 317.8396 |
| B_FC97_FT90  | 0.912204 | 0.0211055 | 25.7487 | 309.8781 | 310.2823 |
| C_FC95_FT80  | 0.886755 | 0.0206359 | 25.1758 | 306.1928 | 306.6491 |

Case21 RC 实验值：

\[
P_f=368.312750\ \text{kN}.
\]

该实验值是在三个材料候选冻结之后才用于 scale comparison；没有用于选择 peak retention。

R07R 结果是 **concrete-only diagnostic**，不能标成最终 RC `Pu`。钢筋必须在 root solve 前进入：

\[
P=P_c+P_s,\qquad R_q=R_{q,c}+R_{q,s}.
\]

历史 G31 crack-free concrete-only 基线为 476.935634 kN；因此 deliberate under-use/smoothing 本身已经把 concrete-only stationary capacity 降到约 306–318 kN。说明材料面简化不是 cosmetic change，而会显著改变结构容量。

---

## 7. R07R 最重要的 HOLD 边界

R07R whole-structure `P/Rq` coefficient identification 使用了高精度 full-halfwave numerical integration **offline**。

运行时/最终候选公式本身完全是有限显式多项式及显式导数，但该 coefficient-identification 步骤与此前 pure-D15 zero-quadrature derivation 不同。

因此：

```text
R07R = PASS_PROOF_OF_CONCEPT_EXPLICIT_END_TO_END_CHAIN
FORMAL_ZERO_QUADRATURE_PRODUCTION_STATUS = HOLD
```

下一阶段必须明确二选一：

1. 接受 offline identification of explicit global target 作为类似材料数据处理/拟合的合法步骤；或
2. 用 analytic D15 / named-kernel 重新生成同一类 `P/Rq` coefficients。

该差异不得隐藏。

---

## 8. 旧工具身份

```text
G18/G27 invariant current map = RETAINED TOOL
G20/G21 smooth conservative philosophy = RETAINED
G26 D15 = RETAINED ANALYTIC TOOL
G28/G30 P,Rq,L kernel = RETAINED
R03 exact rank<=4 = RETAINED TOOL
R04 Appell/Carlson = RETAINED KERNEL LIBRARY
R05/R06 softsign/Mobius/global-poly = CANDIDATE EVIDENCE
R07R rational scalar + global target = CURRENT PROOF-OF-CONCEPT
```

不得为了保留任何历史 compiler 而重新增加不必要的材料面复杂度。

---

## 9. UHPC / Swartz24

UHPC：`fc=141.1 MPa` 仍为用户强制值；完整 arbitrary multiaxial current surface 尚未冻结。UHPC 可采用与 NC 相同的 deliberate under-use + explicit-capacity philosophy，但必须从自己的 source landmarks / material-native domain 建立 target。

Swartz24 production Pu 继续暂停，直到 NC explicit RC chain 完成并冻结。

---

## 10. 当前唯一下一任务

```text
CURRENT_RECOMMENDED_NEXT_TASK
= R08_EXPLICIT_REINFORCEMENT_AND_MINIMUM_MULTAXIAL_CORRECTION
```

顺序：

1. 把 Case21 钢筋显式写入同一 `P,Rq`，不得在 concrete-only `Pu` 后加 `As fy`；
2. 从新的显式 RC `P,Rq,L` 求 Case21 RC root；
3. 比较结构验证结果；
4. 只有存在明确 deficiency 时，才加入一个最小、source-grounded 的 multiaxial correction；
5. 不得自动恢复旧 CC/TC/TT 复杂度。

---

## 11. 恢复读取顺序

1. `current/CURRENT_STATE.md`
2. `governance/EXPLICIT_END_TO_END_CAPACITY_DOCTRINE_20260810.md`
3. `governance/EXPLICIT_SURFACE_GLOBAL_TARGET_R07R_RULE_20260810.md`
4. `current/theory/NZ_SCCM_EXPLICIT_SURFACE_SIMPLIFICATION_AND_CAPACITY_CHAIN_R07R_20260810.md`
5. `current/theory/NZ_SCCM_EXPLICIT_SURFACE_SIMPLIFICATION_AND_CAPACITY_CHAIN_R07R_results.json`
6. `current/theory/NZ_SCCM_R07R_EXPLICIT_GLOBAL_P_RQ_COEFFICIENTS.json`
7. `history/NZ_SCCM/R07R_EXPLICIT_SURFACE_AND_CAPACITY_CHAIN_20260810.md`
8. G31 Case21 analytic-chain history + reinforcement note
9. R06/R05/R04/R03/R02/R01 evidence
10. Case21 invariant exact-moment derivation + Nguyen Ch.3 source evidence
