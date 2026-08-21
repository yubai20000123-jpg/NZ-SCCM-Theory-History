# NZ-SCCM — Swartz配筋率来源修正与多轴容量诊断附录

**时间：2026-08-21 22:05 +08:00**  
**身份：对 `MARGUERRE_AIRY_EXPLICIT_LIMIT_THEORY_V1` 的来源修正与诊断边界附录。**  
**不修改：** `D_x,D_y,H,P_cr,C,G,J,P_pb(q),q0`；不使用试验荷载选根或反标。

---

## 1. Swartz配筋率来源解释修正

`20260821_1733__NZSCCM__MARGUERRE_AIRY_EXPLICIT_LIMIT_THEORY_V1.md` 第2节曾将 Swartz 表中的配筋率解释为两方向合计并采用

\[
\rho_{s,x}=\rho_{s,y}=\rho_{s,table}/2.
\]

该 Swartz 专属解释现在正式 **SUPERSEDED**。

Swartz 原始钢丝直径、间距、层数可直接反算：表中 `0.20%,0.50%,0.75%,1.00%` 是**每一正交方向、跨全部钢筋层合计的配筋率**。因此 Swartz 试件应采用

\[
\boxed{\rho_{s,x}=\rho_{s,y}=\rho_{s,table}}.
\]

若有 `L` 个对称层，则该每方向总配筋率再按来源层数分配至各层；不是再在两个方向之间除2。

这一修正只修正 Swartz 原始输入翻译，不改变一般 RC 公式。

### 1.1 相体积守恒继续保持

当前一般 RC 公式已经正确扣除两个方向钢筋占据的混凝土面积：

\[
A_{c,eff}=t-\sum_l(a_{xl}+a_{yl}).
\]

最终加载方向轴力容量：

\[
\boxed{
n_u=N_c^g-\sum_{y_l<c}(a_{xl}+a_{yl})\sigma_{cl}+\sum_l a_{yl}\sigma_{sl}
}
\]

因此“横向钢筋虽然不直接承担加载方向轴力，但仍替代混凝土体积”已经计入；不得再次重复扣减。

---

## 2. 用户边界：不得为了Swartz实验Pcr修改稳定前端

后续 Swartz 极限承载力误差诊断正式遵守：

```text
DO_NOT_CALIBRATE_D_TO_EXPERIMENTAL_PCR = TRUE
DO_NOT_CALIBRATE_PCR_TO_EXPERIMENTAL_PCR = TRUE
DO_NOT_CHANGE_MODE_ONLY_TO_MATCH_SWARTZ_BUCKLING_OBSERVATION = TRUE
INITIAL_IMPERFECTION_PRESENT_FROM_LOAD_START = TRUE
Pcr_ROLE_IN_CURRENT_THEORY = INTERNAL_ELASTIC_SCALE_IN_Ppb
```

原因：Swartz 的实验“起屈荷载”采用 Southwell、挠度曲线和双面应变分叉等不同识别方法；本显式理论又预置无应力初始缺陷，因此极限承载力诊断不把实验 Pcr 作为必须拟合的统一事件。

---

## 3. Swartz24误差诊断改为参数匹配优先

禁止先对24块不加区分地做误差机制推断。当前优先级：

1. 结构参数相同/几乎相同的重复对；
2. 其余参数几乎相同的控制变量对；
3. 最后才做24块总体统计。

当前高可信重复/准重复设计点：

- `Case1/2`：同厚度、同0.20%每方向、单层中面钢筋；试验相差约3.36%；当前理论同样判断为近似相同承载水平，但成对整体偏高约13%。
- `Case9/10`：同厚度、同0.20%每方向、单层中面钢筋，主要为混凝土批次差异；试验 Case10>Case9，理论方向相同，但两块均明显低估，成对约低20%。
- `Case19/20`：厚度、材料、0.50%每方向、单层中面钢筋均高度接近；试验变化约-1.30%，理论约-1.23%，但成对整体低约10%。
- `Case21/22`：参数高度接近，0.75%每方向、单层中面钢筋；理论与试验均处于相近承载水平，整体偏差较小。

控制变量对 `Case18/23`：厚度完全相同、混凝土参数很接近、均单层中面钢筋，主要差异是每方向配筋率0.20%→1.00%；当前相体积守恒理论给出温和正增益，而试验反向变化，说明 Swartz 单板极限荷载存在不能由表内主要参数完全解释的离散，不能据此反标钢筋模型。

---

## 4. 当前Airy二维应力恢复诊断边界

Airy 结果量严格来自当前显式理论：

\[
N_x=-\frac{\alpha^2b^2\Delta_A}{8A_{22}}q(q+2q_0)\cos(2\beta y),\qquad N_{xy}=0.
\]

在纵向半波中心，`cos(2 beta y)=-1`，因此当前控制区 `N_x>0`（横向拉膜力）。

V1 尚未冻结一个完整二维厚度材料算子，因此从 `N_x,N_y` 到 `sigma_x(z),sigma_y(z)` 的当前恢复仅是诊断闭合：

\[
\varepsilon_x^0=\frac{N_x+\nu N_{c,net}}{E_0(t-a_x-a_y)+E_sa_x},
\]

\[
\sigma_x(z)=E_0\varepsilon_x^0-\nu\sigma_y^{(+)}(z).
\]

该恢复只用于判断 CC/TC 象限和强度门禁量级，不获得正式 production-material-operator 身份。

---

## 5. CC诊断结果：Case9/10并非强围压解释

在当前未加TC/CC容量修正的极限根处：

|Case|Nx N/mm|受压面 sigma_x MPa|CC厚度比例|Nguyen/Foster CC峰值增强约|
|---:|---:|---:|---:|---:|
|1|+17.11|-0.396|36.3%|2.7%|
|2|+14.82|-0.396|37.9%|2.8%|
|9|+5.83|-0.302|48.7%|3.2%|
|10|+5.56|-0.300|48.9%|3.0%|

Case9/10 的 CC 区更厚，但净横向膜力仍是拉力，局部横向压应力也只有约0.30 MPa。采用 Nguyen/Foster CC 包络

\[
\frac{f_{2p}}{f_c}=\frac{1+3.65\alpha}{(1+\alpha)^2}
\]

只产生约3%的局部轴压峰值增强。因此：

```text
STRONG_BIAXIAL_CONFINEMENT_AS_PRIMARY_CASE9_10_EXPLANATION = REJECTED
SMALL_CC_ENHANCEMENT = RETAINED
```

---

## 6. TC gate：来源形式可用，但Swartz ft未源闭合

Nguyen/Foster 的 tension-compression 峰值包络为来源允许的容量门禁候选。当前 Swartz 试件表没有逐板实测抗拉强度 `ft`，所以数值 TC 校正不能直接晋升正式结果。

项目历史临时诊断值：

\[
\boxed{f_t=0.10f_c}
\]

只具有 `TEMPORARY_DIAGNOSTIC / NOT_CALIBRATED_TO_TEST` 身份。

在当前 Case1/2 的 `c>t` 分支，保持整个结构层冻结，只让混凝土轴向压应力容量乘状态因子 `lambda`，并同时满足：

\[
F_N(q,c,\lambda)=0,\qquad F_M(q,c,\lambda)=0,
\]

与对侧 TC 峰值门禁。对于当前活动 Eq.(3.19) 分支可写成

\[
\boxed{\frac{t_o}{\kappa}+\frac12s_o=f_c},\qquad \kappa=f_t/f_c.
\]

当临时取 `kappa=0.10`：

|Case|q|c mm|lambda|TC诊断Pu kN|Pf kN|误差|
|---:|---:|---:|---:|---:|---:|---:|
|1|0.00235505964|31.2212|0.849431|495.989|490.194|+1.18%|
|2|0.00213053653|31.8407|0.873780|501.025|506.652|-1.11%|

原未加TC门禁根的 tensile-envelope utilization：

- Case1: 1.279 > 1
- Case2: 1.216 > 1
- Case9: 0.910 < 1
- Case10: 0.890 < 1

因此此来源门禁具有很强的**选择性**：会下修 Case1/2，而不会在当前根先截断 Case9/10。

但对 `ft/fc` 敏感：

|ft/fc|Case1 TC诊断Pu kN|Case2 TC诊断Pu kN|
|---:|---:|---:|
|0.08|442.12|445.19|
|0.09|470.18|474.24|
|0.10|495.99|501.02|
|0.11|519.93|525.92|
|0.12|542.29|549.21|

所以 `0.10` 时近乎完美匹配不能被当作验证或冻结；当前只允许结论：

```text
TC_GATE_DIRECTION_AND_SELECTIVITY = SUPPORTED
TC_GATE_EXACT_SWARTZ_PU = NOT_SOURCE_CLOSED
BLOCKER = specimen tensile strength ft
```

---

## 7. 0.85圆柱强度转换链：只能做容量侧敏感性，不可统一改参数

Nguyen 对 Swartz 采用

\[
\boxed{f_c^{analysis}=0.85f_{cyl}}
\]

以考虑墙板原位强度与标准圆柱强度差异。这是 Nguyen 分析来源约定，不是本项目用极限承载力拟合得到。

用户明确不允许为此改稳定刚度/Pcr，所以当前敏感性只在最终截面容量层替换基础压缩强度，保持 `Ppb` 全部不动。

若容量层暂时使用完整 `fcyl=fc_analysis/0.85`：

|Case|Pu kN|相对Pf误差|
|---:|---:|---:|
|1|645.565|+31.70%|
|2|641.234|+26.56%|
|9|595.578|-4.84%|
|10|619.458|-11.02%|
|19|376.766|-0.24%|
|20|370.522|-0.60%|
|21|385.768|+4.74%|
|22|388.216|+9.09%|

结论：完整圆柱强度能显著改善 Case9/10，并几乎闭合 Case19/20，但会严重恶化 Case1/2、并过度提高 Case21/22。因此不存在一个可以直接把 `0.85` 改成统一常数的证据。

为精确匹配 Pf 所需的“容量基础强度/圆柱强度”诊断比值分别约：

- Case1 0.712
- Case2 0.752
- Case9 1.058
- Case10 1.140
- Case19 1.004
- Case20 1.010
- Case21 0.924
- Case22 0.866

这些数只用于证明“单一强度转换系数无法解释全部可信设计点”，禁止用作逐板标定。

---

## 8. 完整圆柱基础强度 + 小CC增强的量级

仍保持结构层冻结，若仅作诊断地采用 `fcyl` 作为容量基础，再施加受压面 Nguyen/Foster CC 包络：

- Case9: `lambda_CC≈1.03222`, `Pu≈612.407 kN`, 对 Pf 误差约 `-2.15%`；
- Case10: `lambda_CC≈1.03100`, `Pu≈636.653 kN`, 对 Pf 误差约 `-8.55%`。

要在此基础上精确达到试验，Case9/10 仍分别需要约 `1.025 fcyl` 与 `1.105 fcyl` 的基础容量强度。因此 Case10 仍是当前可信设计点中最明显的容量异常之一。

---

## 9. 当前允许的机制结论

目前不支持一个统一修正系数。工作分解为：

\[
\boxed{\text{base-strength conversion}+\text{TC weakening}+\text{small CC enhancement}}
\]

- Case1/2：TC削弱是强候选；当前 `ft=0.1fc` 的数值近闭合仅是诊断，不能冻结。
- Case9/10：强围压解释已排除；基础强度转换接近圆柱强度 + 小CC增强能解释 Case9 大部分缺口，Case10仍有约8%级剩余异常。
- Case19/20：完整圆柱强度容量敏感性几乎闭合，但当前二维恢复为TC主导；未来正式TC门禁不能不加审计地继续降低这一对。
- Case21/22：现有0.85基础理论已较接近试验，完整圆柱强度会过修。

---

## 10. 正式边界

```text
SWARTZ_REINFORCEMENT_MAPPING_CORRECTED = YES
RHO_X_EQUALS_RHO_Y_EQUALS_TABLE_RATIO = YES
REBAR_CONCRETE_VOLUME_REPLACEMENT = ALREADY_INCLUDED
D_PCR_PPB_MODIFICATION = PROHIBITED_FOR_THIS_DIAGNOSTIC
TC_GATE_SOURCE_FORM = AVAILABLE
SWARTZ_SPECIMEN_FT = NOT_SOURCE_CLOSED
TC_CORRECTED_PU = DIAGNOSTIC_ONLY
CC_ENHANCEMENT = SMALL_DIAGNOSTIC
UNIVERSAL_FC_SCALE_CORRECTION = REJECTED
EXPERIMENT_IN_ROOT_SELECTION = 0
```
