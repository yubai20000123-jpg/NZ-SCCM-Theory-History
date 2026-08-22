# NZ-SCCM — 七门禁材料重组后的结构重算：SUHPC 更新 + Z0–Z6 NC-TC 来源角色审计

**Date:** 2026-08-22  
**Status:** `EXECUTED_PARTIAL / SUHPC_POST_7GATE_RERUN_RESOLVED / Z0_Z6_NC_TC_TRANSITION_SOLVED / Z0_Z6_FINAL_POSTCRACK_2D_PU_OPEN`

## 0. 本轮任务与硬边界

本轮承接当前材料来源链：

1. `semantic_v2/20_theory/20260822_1151__NZSCCM__NC_UHPC_7GATE_EXPLICIT_MATERIAL_REORGANIZATION_V1.md`；
2. `semantic_v2/20_theory/20260822_1240__NZSCCM__UHPC_ZHANG_BACKBONE_AND_LIU_CC_CONTINUOUS_SOURCE_MIN_GATE.md`；
3. `semantic_v2/20_theory/20260822_1255__NZSCCM__NC_TC_FAILURE_ENVELOPE_VS_APPENDIXB_CONSTITUTIVE_PEAK_RESOLUTION.md`；
4. `semantic_v2/20_theory/20260822_1315__NZSCCM__NC_UHPC_7GATE_MATERIAL_CERTIFICATE_V1.md`；
5. `semantic_v2/20_theory/20260822_1320__NZSCCM__NC_CC_EQ317_PRINTED_TYPO_VS_FIG32_APPENDIXB_RESOLUTION.md`。

结构骨架保持：

\[
P_{pb}(q)=P_{cr}\frac{q}{q+q_0}+Cq(q+2q_0),
\]

\[
n(s;q)=\frac{P_{pb}(q)}b+Gq(q+2q_0)(1-2s^2),\qquad m(s;q)=Jqs,
\]

以及同源 Airy 横向膜力。

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_material_points = 0
RITZ_ORDER = NONE
LOAD_PATH_TRACKING = 0
HISTORY_STATE_MACHINE = OFF_MAINLINE
EXPERIMENT_IN_ROOT_SELECTION = 0
FEM_IN_ROOT_SELECTION = 0
STRUCTURAL_BACKBONE_CHANGED = FALSE
```

本轮允许一次性有限非线性代数根求解；它不是荷载步推进、不是材料点迭代、不是空间求积。

---

# 1. SUHPC：Zhang 2023 + Liu 2024 后的结构重算

UHPC 单轴压缩由历史 Hu 曲线切换为当前正式 Zhang 2023 backbone：

\[
g_a(x)=\frac{rx}{r-1+x^r},\qquad
r=\frac{E_c}{E_c-f_c/\varepsilon_{c0}},
\]

并保留其零围压下降支。截面原函数由材料证书中已建立的有限解析 primitive 计算，不使用厚度 Gauss 点。

二维容量门禁采用 Liu 2024：

- CC：Liu 两条来源曲线的 conservative source-min project reduction；
- TC/CT：Liu conservative sequential-loading envelope；
- TT：双轴拉强度保守取单轴拉强度；
- 不使用结构 Pu 反标材料参数。

## 1.1 新 1D 结果

| Case | 旧 Hu 1D / MN | 新 Zhang 1D / MN | 变化 |
|---|---:|---:|---:|
|T120|12.3480|12.41101|+0.51%|
|T360|11.2978|11.36533|+0.60%|
|BH005|2.41999|2.42351|+0.15%|
|BH010|4.45287|4.46632|+0.30%|
|BH020|8.17466|8.21925|+0.55%|
|BH032|11.14350|11.21046|+0.60%|
|BH050|13.61827|13.67770|+0.44%|

结论：Hu -> Zhang 的单轴压缩 backbone 替换只造成约 `0.1%–0.6%` 的结构承载力变化；此前二维异常并非主要由该单轴曲线选择造成。

## 1.2 T120：Liu TC 活动

新 Zhang 1D 根的恢复状态使 Liu-TC 组合门禁略超界，因此释放压侧峰值应变幅值并解有限未知量

\[
(q,c,\varepsilon_c^*)
\]

满足轴力、弯矩和活动 TC 门禁。

结果：

\[
q_u=0.00164175827,
\qquad c_u\approx78.2327\ \mathrm{mm},
\]

\[
\varepsilon_c^*\approx0.00335035,
\]

控制 UHPC 状态约为

\[
p\approx67.343\ \mathrm{MPa},\qquad t\approx7.8732\ \mathrm{MPa}.
\]

最终

\[
\boxed{P_{u,T120}^{2D}=12.22252\ \mathrm{MN}}.
\]

相对新 1D 值下降约 `1.519%`。

## 1.3 T360 与 BH005–BH032

这些试件在新 Zhang 1D 根处不触发更早的 Liu 2D 容量门禁，因此保持 1D 根。

## 1.4 BH050：旧 `Pu OPEN` 闭合

新 Zhang 1D：

\[
P_{u,BH050}^{1D}=13.67770\ \mathrm{MN}.
\]

其 TC 状态进入 Liu 第一段，以

\[
t=f_t
\]

为活动边界。有限三未知量重解给出

\[
q_u\approx0.00425789621,
\qquad c_u\approx55.6101\ \mathrm{mm},
\]

\[
\varepsilon_c^*\approx0.00295398,
\]

\[
p\approx31.3766\ \mathrm{MPa},
\qquad t=9.7677\ \mathrm{MPa}.
\]

因此

\[
\boxed{P_{u,BH050}^{2D}=12.77154\ \mathrm{MN}},
\]

相对新 1D 值下降约 `6.625%`。旧 `TRIGGERED / unique Pu OPEN` 在当前 Liu capacity architecture 下关闭。

## 1.5 SUHPC 当前新表

| Case | Zhang 1D / MN | post-7gate 2D / MN | Abaqus comparator / MN | 2D-comparator difference |
|---|---:|---:|---:|---:|
|T120|12.41101|**12.22252**|12.6378|−3.286%|
|T360|11.36533|**11.36533**|10.9688|+3.615%|
|BH005|2.42351|**2.42351**|2.3558|+2.874%|
|BH010|4.46632|**4.46632**|4.3043|+3.764%|
|BH020|8.21925|**8.21925**|8.0076|+2.643%|
|BH032|11.21046|**11.21046**|10.9905|+2.001%|
|BH050|13.67770|**12.77154**|12.2198*|+4.515%|

`*` BH050 comparator 仍按既有审计标记为较低置信度的诊断模型族；任何 comparator 均未参与根求解。

```text
SUHPC_POST_7GATE_RERUN = EXECUTED
SUHPC_BH050_UNIQUE_2D_PU = RESOLVED_UNDER_CURRENT_LIU_CAPACITY_ARCHITECTURE
HU_WENXU = HISTORICAL_UNIAXIAL_COMPARATOR_ONLY
```

---

# 2. Z0–Z6：新 NC source gate 的有限兼容重算

## 2.1 为什么旧 Z6 51.345 MN 不能直接沿用

旧 Z6 UMCG 根

\[
P_u=51.3450217892\ \mathrm{MN}
\]

使用了历史项目 TC current reduction

\[
c^*=c(1-\tau).
\]

当前 11:51 材料重组已经将该式降级为历史 project reduction，不再作为 NC 二维 source identity。

旧 Z6 根的混凝土状态约为

\[
\sigma_y^c=-30.4\ \mathrm{MPa},\qquad
\sigma_x^c=+0.912\ \mathrm{MPa}.
\]

用当前正式 Nguyen TC failure envelope 检查：

\[
\frac{p}{f_c}+\frac{t}{3f_t}
=1+\frac{0.912}{3\times3.04}
\approx1.10>1.
\]

因此：

```text
OLD_Z6_51_345 = NOT_CURRENT_SOURCE_ADMISSIBLE
```

它只能保留为历史旧 current-map 执行结果。

## 2.2 s=0 有限相兼容系统

为了不引入材料点，本轮首先在旧 Z6 已证明的关键横向膜力 endpoint `s=0` 上建立完全有限系统。

物理 bonded strains 由两个 NC material coordinates 给出：

\[
\frac{\varepsilon_x}{\varepsilon_0}=\lambda_x-\nu_c\lambda_y,
\qquad
\frac{\varepsilon_y}{\varepsilon_0}=\lambda_y-\nu_c\lambda_x.
\]

NC current axis backbones：

- 压缩：Saenz；
- 拉伸：T5/Foster project reduction；
- 不再把旧 `c(1-tau)` 当作二维 source identity。

外钢面使用 plane-stress elastic trial + von-Mises radial cap；纵向 web 使用 y-only clip law。

相平衡：

\[
N_x^{sec}(\lambda_x,\lambda_y)=K_xq(q+2q_0),
\]

\[
N_y^{sec}(\lambda_x,\lambda_y)
=-\left[\frac{P_{pb}(q)}b+Gq(q+2q_0)\right].
\]

第三式为当前 NC-TC source envelope 的活动分支：

压轴段 A：

\[
\frac{p}{f_c}+\frac{t}{3f_t}=1,
\]

拉轴段 B：

\[
\frac{p}{2f_c}+\frac{t}{f_t}=1.
\]

本轮取从原点连续进入的压缩上升支；不通过试验或 Zhou/Winter 选择根。

## 2.3 Z0–Z6 第一次 TC source-transition 根

有限兼容方程给出：

|Case|q at TC transition|P at TC transition / MN|source segment|lambda_x|lambda_y|p/fc|t/ft|vs 1D Pu|
|---|---:|---:|---|---:|---:|---:|---:|---:|
|Z0|0.002007624998|27.033151885|B|0.0310131|−0.4594515|0.7587838|0.6206081|−28.53%|
|Z1|0.002653115864|17.093528920|B|0.0345810|−0.3438529|0.6150531|0.6924735|−30.83%|
|Z2|0.002007624998|27.033151885|B|0.0310131|−0.4594515|0.7587838|0.6206081|−37.07%|
|Z3|0.003023358231|36.744639968|B|0.0317598|−0.4323697|0.7285937|0.6357031|−20.97%|
|Z4|0.001755102366|56.203522296|A|0.0259798|−0.5292564|0.8269272|0.5192183|−20.01%|
|Z5|0.000194052923|10.747333454|A|0.0226245|−0.5557318|0.8492317|0.4523048|−23.88%|
|Z6|0.004014855283|23.832330467|B|0.0400238|−0.2121687|0.4061203|0.7969399|−57.73%|

所有根均满足各自 source segment 的分支范围：

- A：`p/fc >= 0.8` 且 `t/ft <= 0.6`；
- B：`p/fc <= 0.8` 且 `t/ft >= 0.6`。

对相反 Airy 符号的 CC 方向进行了 origin-connected 审计；在当前 1D 候选之前未发现由 Nguyen/Foster-Kupfer CC envelope 控制的更早 source boundary。当前问题来自 TC，而非 CC 强围压。

---

# 3. 关键裁决：上述 Z 数值是 cracking/state-transition，不是 final Pu

这一点由 Nguyen 来源角色直接决定，而不是由计算值“偏低”决定。

`20260822_1255__...NC_TC_FAILURE_ENVELOPE...` 已重新核实：Nguyen 将 Eqs. (3.17)–(3.20) 明确作为 **Failure Envelope**；TC 象限越过 Eqs. (3.18)–(3.19) 后，混凝土单元**改变状态并开裂**。随后才进入 modified compression field / tension-stiffening 等开裂后 constitutive continuation。

因此本轮解出的

\[
P_{TC-transition}
\]

是当前 source-closed 的**状态转换/开裂边界**。

如果把它直接解释为 steel-shell concrete 的 ultimate hard cap，会得到 Z0–Z6 全部提前 `20%–58%` 截断。这不是足够的来源依据，因为来源本身在此处并未终止材料承载，而是切换到开裂后本构。

所以正式裁决是：

```text
NC_TC_SOURCE_FORM_G6 = PASS
NC_TC_SOURCE_ROLE = CRACKING / STATE-TRANSITION BOUNDARY
TC_FULL_FAILURE_ENVELOPE_AS_SC_ULTIMATE_HARD_CAP = REJECTED
Z0_Z6_NC_TC_TRANSITION = SOLVED
Z0_Z6_FINAL_POSTCRACK_2D_PU = OPEN
```

这不撤销 NC-TC source envelope；撤销的是“把该 transition envelope 直接当作钢壳混凝土最终 Pu 截止”的错误角色解释。

---

# 4. Z6 后续数学交点不能因接近 comparator 而升级为 Pu

Z6 在越过第一次 B 段 transition 后，有限方程还存在其它数学交点。例如上升压缩支的一条 A 段交点约为

\[
q\approx0.01155435,
\qquad P\approx48.63142\ \mathrm{MN},
\]

其

\[
p/f_c\approx0.8996,
\qquad t/f_t\approx0.3012.
\]

该数值**不得**升级为生产 Pu，因为到达它必须先越过 `q≈0.00401486` 的 cracking/state-transition；当前 stripped mainline 尚没有 source-closed 的开裂后有限 continuation 把两个状态连接起来。

即使该 48.63 MN 与某些 Zhou/Winter comparator 数量级接近，也不构成选根依据。

```text
Z6_LATER_A_BRANCH_INTERSECTION = DIAGNOSTIC_ONLY
COMPARATOR_BASED_ROOT_SELECTION = PROHIBITED
```

---

# 5. 与旧结构表的关系

旧 07:45 结构表仍是材料重组前的历史执行基线。材料重组后：

- selected Swartz RC：此前有限 TC re-cut 数值保持为诊断工作值；Swartz specimen-specific `ft` 仍 source-open；
- SUHPC：本文件第 1 节的新 Zhang/Liu 表替代旧 Hu-based / BH050-open 工作表；
- Z0–Z5：旧 “2D unchanged” 不再宣告为当前 final 2D Pu；
- Z6：旧 `51.3450 MN` 被当前 source-role audit supersede；
- Z0–Z6 当前已 source-close 的是 **TC transition boundary**，不是 post-crack ultimate capacity。

---

# 6. 当前真实状态

```text
POST_7GATE_STRUCTURAL_RERUN = EXECUTED_PARTIAL

RC_SELECTED_NUMERICAL_STATUS = RETAINED_WORKING_DIAGNOSTIC
RC_SWARTZ_SPECIMEN_FT = SOURCE_OPEN

SUHPC_POST_7GATE_RERUN = EXECUTED
SUHPC_CURRENT_2D_TABLE = RESOLVED
BH050_CURRENT_2D_PU = 12.77154 MN

Z0_Z6_NC_TC_TRANSITION = SOLVED
Z0_Z6_FINAL_POSTCRACK_2D_PU = OPEN
OLD_Z6_51_345 = SUPERSEDED_BY_CURRENT_NC_SOURCE_ROLE
TC_FULL_ENVELOPE_AS_SC_ULTIMATE_HARD_CAP = REJECTED

FORMAL_SPATIAL_QUADRATURE = 0
N_MATERIAL_POINTS = 0
LOAD_PATH_TRACKING = 0
HISTORY_STATE_MACHINE = OFF_MAINLINE
STRUCTURAL_BACKBONE_CHANGED = FALSE
```

## 6.1 唯一正确的下一材料/结构任务

不是从 Z6 的后续数学根中挑一个接近 Zhou/Winter 的值，也不是恢复 Nguyen 全材料点历史状态机。

下一步应当是：

\[
\boxed{
\text{从 Nguyen 开裂后 TC continuation 中提取一个 source-grounded、monotonic、finite、G6-compatible reduced operator}
}
\]

要求它：

1. 在 TC source envelope 处与未开裂 current state 对接；
2. 允许开裂后的 compression softening / tension-stiffening 继续承载；
3. 不需要材料点场、加载步或空间数值积分；
4. 同时适用于 RC 与 steel-shell NC，不建立 Z-only 修正；
5. 不用任何 Swartz/Zhou/Winter/Pu 数据确定材料系数。

在该 continuation 被 source-close 之前，Z0–Z6 的最终 post-crack 2D Pu 必须保持 `OPEN`。