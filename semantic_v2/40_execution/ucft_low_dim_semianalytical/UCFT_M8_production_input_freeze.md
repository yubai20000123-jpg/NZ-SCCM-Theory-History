# UCFT M8 — production input freeze / recovery audit

更新时间：2026-09-30 19:01 +08:00

状态：M0–M7 已通过。本文件是 M8 正式九试件 connected-q path 的输入冻结审计；不使用 FEM target，不以 Pu 误差拟合任何输入。

---

## 1. M8 的执行原则

M8 不是重新建立理论，而是把 M0–M7 已闭合的方程投入九试件计算。

因此生产计算只能使用：

1. 已被项目正式锁定并可追溯的共同材料参数；
2. 已被项目正式锁定并可追溯的试件几何参数；
3. 可由上述输入和既定理论唯一计算得到的派生量；
4. 若某个参数存在多个历史版本而当前版本未唯一指定，则必须标成 unresolved，不能默选一个旧版本；
5. 不能用 FEM 峰值荷载或误差最小原则补齐 unresolved input。

---

## 2. 已恢复并冻结的共同材料输入

钢材：

\[
\boxed{E_s=206000\ {\rm MPa}}
\]

\[
\boxed{\nu_s=0.30}
\]

\[
\boxed{f_y=355\ {\rm MPa}}
\]

UHPC：

\[
\boxed{E_c=43400\ {\rm MPa}}
\]

\[
\boxed{\nu_c=0.20}
\]

\[
\boxed{f_c=141.1\ {\rm MPa}}
\]

\[
\boxed{\varepsilon_{c0}=0.0035}
\]

厚度：

\[
\boxed{t_s=4\ {\rm mm}}
\]

\[
\boxed{t_c=42\ {\rm mm}}
\]

初始整体缺陷：

\[
\boxed{q_0=0.0025}
\]

PBL/web 等效钢面积：

\[
\boxed{A_w=1332\ {\rm mm^2}}.
\]

这些参数来自当前项目既有 solver/state；本轮没有按九试件 Pu 修改。

---

## 3. 钢材 equivalent uniaxial law 的正式冻结

M5 已经把钢壳二维 finite stress 改造成 consistent secant-Mises deformation theory：

\[
\bar\varepsilon_i
=
\sqrt{\boldsymbol\varepsilon^T\mathbf H_\nu\boldsymbol\varepsilon},
\]

\[
\boldsymbol\sigma
=
E_{\rm sec}\mathbf C_0\boldsymbol\varepsilon,
\]

\[
E_{\rm sec}
=
\frac{P_s(\bar\varepsilon_i)}{\bar\varepsilon_i}.
\]

此前唯一未冻结的是单轴 equivalent post-yield law \(P_s\)。

本轮检索当前项目旧锁定材料合同，能够明确恢复的项目原生钢材 law 是：

\[
\boxed{
\text{ideal elastic-perfectly plastic steel}
}
\]

因此无需引入外部 hardening 参数，可以把它作为 M5 的 degree-0 polynomial plastic branch：

\[
\boxed{
P_s(\bar\varepsilon_i)
=
\begin{cases}
E_s\bar\varepsilon_i,
&
0\le\bar\varepsilon_i\le f_y/E_s,
\\[1mm]
f_y,
&
\bar\varepsilon_i>f_y/E_s.
\end{cases}
}
\]

塑性 branch：

\[
\boxed{
E_{\rm sec}
=
\frac{f_y}{\bar\varepsilon_i}
}
\]

\[
\boxed{
E_{\rm tan}=0.
}
\]

因此 steel production material input 从本轮起可以冻结，不再是 M8 blocker。

这不会人为制造下降段。钢壳分项下降仍必须来自：

\[
q-A
\text{ coupling}
+
\text{local buckling}
+
\text{plastic-zone growth}
+
\text{redistribution}.
\]

---

## 4. 九试件几何输入冻结表

当前能够可靠恢复：

| Case | \(b\)/mm | \(a_h=2b\)/mm | \(t_c\)/mm | \(t_s\)/mm |
|---|---:|---:|---:|---:|
| BH005 | 250 | 500 | 42 | 4 |
| BH010 | 500 | 1000 | 42 | 4 |
| BH020 | 1000 | 2000 | 42 | 4 |
| BH032 | 1600 | 3200 | 42 | 4 |
| BH050 | 2500 | 5000 | 42 | 4 |
| BH060 | 3000 | 6000 | 42 | 4 |
| BH070 | 3500 | 7000 | 42 | 4 |
| BH085 | 4250 | 8500 | 42 | 4 |
| BH100 | 5000 | 10000 | 42 | 4 |

---

## 5. PBL/web reaction correction 已可逐件冻结

当前：

\[
A_c=bt_c
\]

并且：

\[
\chi_w
=
1+\frac{A_w}{A_c}
\left(
\frac{E_s}{E_c}-1
\right).
\]

代入：

\[
E_s=206000,
\quad
E_c=43400,
\quad
t_c=42,
\quad
A_w=1332
\]

得到：

| Case | \(\chi_w\) |
|---|---:|
| BH005 | 1.475275839 |
| BH010 | 1.237637920 |
| BH020 | 1.118818960 |
| BH032 | 1.074261850 |
| BH050 | 1.047527584 |
| BH060 | 1.039606320 |
| BH070 | 1.033948274 |
| BH085 | 1.027957402 |
| BH100 | 1.023763792 |

因此 M8 最终报告反力严格使用：

\[
\boxed{
P_{\rm report}
=
\chi_wP_c+P_s^++P_s^-.
}
\]

---

## 6. 已恢复的 local imperfection 几何尺度，但暂不冒充 whole-face amplitude

旧 steel-local segmentation 工作中能够追溯到：

\[
L_x=0.225b
\]

以及：

\[
A_0^{strip}=\frac{L_x}{1600}
=
\frac{0.225b}{1600}.
\]

于是：

| Case | \(A_0^{strip}\)/mm |
|---|---:|
| BH005 | 0.03515625 |
| BH010 | 0.07031250 |
| BH020 | 0.14062500 |
| BH032 | 0.22500000 |
| BH050 | 0.35156250 |
| BH060 | 0.42187500 |
| BH070 | 0.49218750 |
| BH085 | 0.59765625 |
| BH100 | 0.70312500 |

BH100 的：

\[
A_0^{strip}=0.703125\ {\rm mm}
\]

与历史工作中出现过的该值一致。

但必须区分：

\[
\boxed{
A_0^{strip}
}
\]

和当前 M3/M6 whole-face：

\[
\boxed{
(A_0^\pm,N^\pm,m^\pm).
}
\]

旧 segmentation 中 TOP/BOTTOM 的非等宽 strip 配置不能在没有显式映射的情况下偷偷等价成一个 uniform whole-face integer \(N\)。

因此以上 \(A_0^{strip}\) 目前只冻结为“可追溯的 imperfection scale/provenance”，尚不升级为当前 whole-face production \(A_0^\pm\)。

---

## 7. UHPC tension：完成了源追踪，但尚未达到唯一 production freeze

当前项目路线明确锁定：

\[
\boxed{f_t\sim 7\ {\rm MPa}}
\]

并禁止恢复历史约 10 MPa 级旧 PCHIP。

本轮项目内检索找到两条有价值证据。

### 7.1 UCFT/U180 项目材料信息

项目手稿给出 U180：

\[
E\approx48\ {\rm GPa},
\qquad
f_c\approx130\ {\rm MPa},
\qquad
f_t=7\ {\rm MPa}.
\]

这支持“7 MPa 量级”的目标，但它的 \(E,f_c\) 与当前生产：

\[
43.4\ {\rm GPa},
\qquad
141.1\ {\rm MPa}
\]

不完全相同，不能把整个曲线无条件搬入。

### 7.2 2% steel-fibre UHPC 邻近材料证据

项目 Library 中胡文旭试验材料给出：

\[
f_{c,axial}=136.9\ {\rm MPa},
\qquad
f_t=7.2\ {\rm MPa},
\qquad
E=45.1\ {\rm GPa},
\]

且 steel fibre volume fraction：

\[
V_f=2\%.
\]

它与当前材料：

\[
f_c=141.1,\quad
f_t\sim7,\quad
E_c=43.4\ {\rm GPa}
\]

非常接近。

该论文采用的受拉模型又明确追溯到：

\[
\text{杨简，基于钢纤维增强作用的 UHPC 基本材性预测研究，2021}.
\]

并使用 steel-fibre factor：

\[
K=(l_f/d_f)V_f
\]

以及 damage coefficient \(m(K)\)。

但是当前 Library 中没有恢复到该 2021 学位论文完整的 tensile curve equations / 当前试件对应 \(l_f,d_f\) 的唯一组合。

### 7.3 外部公开检索的作用边界

本轮还检查了公开 direct-tension UHPC constitutive literature。

可获得的 Hiew 等 2024 直接拉伸数据表明，2% steel-fibre UHPC 的典型模型具有：

\[
\text{elastic}
\rightarrow
\text{strain hardening}
\rightarrow
\text{softening}
\]

完整阶段，且 peak tensile strain 可以达到千分之几。

但其 2% fibre specimen 的 peak strengths 大约在 11 MPa 量级，明显高于当前项目锁定的约 7 MPa。

因此：

\[
\boxed{
\text{不能直接把该曲线当成本项目 production curve}
}
\]

也不能为了得到 7 MPa 简单把整条曲线按比例缩放后宣称“已恢复真实材料”。

它只能证明当前“7 MPa peak + post-peak softening”的材料架构是合理的外部候选形态，而不能唯一确定：

\[
e_{tp},
\quad
e_{tu},
\quad
P_{t1},
\quad
P_{t2}.
\]

因此 UHPC tensile production polynomial 当前状态必须继续标记：

\[
\boxed{
\mathrm{UNRESOLVED\_PRODUCTION\_INPUT}.
}
\]

---

## 8. whole-face steel local wave-number 审计

当前 M3/M6 锁定 whole-face：

\[
\psi_\ell
=
[1-\cos(2N X)]
[1-\cos(2m Y)].
\]

M8 必须给每个钢面确定：

\[
N^+,\quad m^+,\quad N^-,\quad m^-.
\]

本轮检索到历史上存在多个不同阶段的 wave-number 定义：

- 旧 strip/local-cell 模型按多个子板宽度和局部长度分别计算；
- 某些历史 diagnostic 使用过固定 \(m\)；
- 某些 whole-face diagnostic 出现过具体 N/m；
- M3 最终理论故意保留 \(N^\pm,m^\pm\) 为符号通式。

这些历史数值的理论身份并不相同。

因此若现在直接选择：

\[
N=m=4
\]

或把 strip 数直接转换成 whole-face \(N,m\)，都会把历史 diagnostic 误升格为 production input。

本轮没有这样做。

当前结论：

\[
\boxed{
N^\pm,m^\pm
=
\mathrm{UNRESOLVED\_PRODUCTION\_INPUT}.
}
\]

---

## 9. 当前 M8 readiness

已经完成：

\[
\boxed{
\text{common material constants}
}
\]

\[
\boxed{
\text{nine specimen }b,a_h,t_c,t_s
}
\]

\[
\boxed{
\chi_w
}
\]

\[
\boxed{
\text{steel ideal-plastic equivalent law}
}
\]

\[
\boxed{
\text{archived local imperfection scale provenance}.
}
\]

尚缺两个真正不可替代的 production interfaces：

### Blocker 1

\[
\boxed{
P_{t1}(e),
\quad
P_{t2}(e),
\quad
e_{tp},
\quad
e_{tu}
}
\]

即当前约 7 MPa UHPC 的正式 tension law。

### Blocker 2

\[
\boxed{
N^\pm,
\quad
m^\pm,
\quad
A_0^\pm
}
\]

从旧 segmented local geometry 到 current whole-face mode 的正式映射 / 选择规则。

因此：

\[
\boxed{
\mathrm{M8\_INPUT\_FREEZE}
=
\mathrm{PARTIAL}.
}
\]

以及：

\[
\boxed{
\mathrm{M8\_FULL\_PATH}
=
\mathrm{NOT\ STARTED}
}
\]

不是求解器失败，而是 production input 尚未唯一闭合。

---

## 10. 为什么本轮不能用“先跑起来再说”的 diagnostic 参数替代

如果现在为了得到九条曲线，直接采用：

- M2 的 temporary tensile family；
- 旧 10.7 MPa PCHIP；
- Hiew 11 MPa 曲线按比例缩放；
- 任取 \(N=m=4\)；
- 根据 FEM Pu 选择最合适的 \(N,m\)；

都会使 M8 从：

\[
\text{prediction}
\]

变成：

\[
\text{unacknowledged calibration / arbitrary input selection}.
\]

这违反当前路线合同。

因此本轮停止位置是一个真正的 production-data boundary，而不是人为增加理论 Gate。

---

## 11. M8 production contract 已建立

已建立脚本：

`UCFT_M8_material_geometry_contract.py`

其中所有已恢复输入均写死为可追溯常量。

钢材：

\[
P_s(\bar\varepsilon_i)
=
\min(E_s\bar\varepsilon_i,f_y)
\]

被正式实现。

尚未恢复的输入统一使用：

`None / UNRESOLVED`

并由：

`assert_production_ready()`

显式阻止 solver 在缺失输入时静默使用 diagnostic defaults。

因此以后任何正式 M8 solver 都必须通过该 contract 后才能启动九试件 connected branch。

---

## 12. 唯一 NEXT_ACTION

继续 M8，不回到理论路线讨论。

下一步唯一任务为：

\[
\boxed{
\text{恢复/构造具有明确来源的 7 MPa UHPC production tensile polynomial，}
}
\]

并同步从 current whole-face local geometry 的历史推导中恢复：

\[
\boxed{
N^\pm,m^\pm,A_0^\pm
}
\]

的正式选择规则。

执行顺序不是“任选其一”，而是把这两个 production input interface 在同一 M8 输入冻结阶段闭合；一旦闭合，立即启动九试件 connected \(q\)-path，不再增加理论门。