# NZ-SCCM — 三阶 vs 五阶 Marguerre–Airy 结构骨架理论门禁：BH032 / BH050 R02

**日期：2026-08-28**  
**身份：THEORY AUDIT / NOT PRODUCTION**  
**父文件：** `20260828__NZSCCM__FINITE_MULTIMODE_MARGUERRE_AIRY_EXPLICITNESS_AND_MINIMAL_ENRICHMENT_R01.md`  
**production 基线：** `20260821_1733__NZSCCM__MARGUERRE_AIRY_EXPLICIT_LIMIT_THEORY_V1.md` + current common-R06 terminal architecture  

本文件只回答一个问题：

> 当前结构骨架应继续保持三阶单模态 `N=1`，还是为了第一代非线性模态反馈升级为五阶意义下的 `N=3`？

本门禁严格不用 FEM/试验决定阶次、选模态或修正系数；BH032/BH050 只使用冻结理论输入和冻结理论 terminal 根作为“当前理论有效区间的末端状态”。

```text
FEM_USED_IN_ORDER_GATE = NO
TEST_USED_IN_ORDER_GATE = NO
N_CONVERGENCE_USED = NO
FORMAL_SPATIAL_QUADRATURE = 0
TERMINAL_CAPACITY_REPARAMETERIZED = NO
qU_REOPENED = NO
AIRY_ROLE_CHANGED = NO

THIRD_ORDER_N1_ASYMPTOTIC_GATE_BH032 = PASS
THIRD_ORDER_N1_ASYMPTOTIC_GATE_BH050 = PASS
FIRST_GENERATION_N2_REDUCTION = NOT_JUSTIFIED
FIFTH_ORDER_N3_PROMOTION_TO_PRODUCTION = NOT_REQUIRED
CURRENT_PRODUCTION_N = 1_RETAIN
N3_STATUS = THEORY_AUDIT / OPTIONAL_HIGHER_ORDER_EXTENSION
```

---

## 1. 先修正一个表述：terminal capacity 不是“三阶”或“五阶”

current terminal capacity 层是给定材料/截面假设下的有限解析/分段解析 resultant closure。它不是关于全局模态幅值 `epsilon` 的渐近级数，因此不能把它标成“三阶 terminal”或“五阶 terminal”。

所以不能用

```text
structural polynomial degree == terminal polynomial degree
```

作为阶次选择原则。

正确门禁是：

1. 当前单模态结构骨架截去的第一代 secondary amplitudes 是否在整个理论 admissible path 上保持高阶小量；
2. secondary mode 是否远离自己的线性临界/近共振；
3. 把第一代两个 secondary modes 完整加入后，对同一主模态幅值下的结构载荷关系修正是否仍为明确的高阶小量。

若三项均通过，则三阶 `N=1` 有受控渐近依据；不需要因为完整 PDE 会继续生成更高谐波而做 `N`-convergence。

---

## 2. 当前有限多模态结论

代表完整半波上：

\[
\phi_1=\sin X\sin Y,
\qquad X=\pi x/b,
\qquad Y=\pi y/\ell.
\]

current primary 在完整物理板索引为 `(1,m_*)`。

R01 已从 Marguerre bracket 直接证明，主模态第一代非线性同时生成

\[
\boxed{\phi_x=\sin 3X\sin Y}
\]

和

\[
\boxed{\phi_y=\sin X\sin 3Y},
\]

即完整板索引

\[
\boxed{(3,m_*),\quad(1,3m_*)}.
\]

因此若结构理论真的升级到第一代完整富集，最小集合是

\[
\boxed{N=3:\ (1,m_*),(3,m_*),(1,3m_*)}.
\]

仅从 nonlinear selection 不能任意挑一个组成 `N=2`。

---

## 3. 纯理论 leading-order secondary amplitudes

取初始缺陷仅在 primary mode：

\[
q_{01}=q_0,\qquad q_{0x}=q_{0y}=0.
\]

定义

\[
\boxed{S(q)=q(q+q_0)(q+2q_0)}.
\]

第一代 secondary forcing 为

\[
F_x=-\frac{b^3\beta^4}{16\bar A_{22}}S(q),
\]

\[
F_y=-\frac{b^3\alpha^4}{16\bar A_{11}}S(q).
\]

其中

\[
\alpha=\pi/b,\qquad \beta=\pi/\ell.
\]

沿 primary path 的 leading-order secondary response 为

\[
\boxed{
q_x^{(1)}=
\frac{b^2\beta^4}
{16\bar A_{22}[K_{31}-N\beta^2]}
S(q)
}
\]

\[
\boxed{
q_y^{(1)}=
\frac{b^2\alpha^4}
{16\bar A_{11}[K_{13}-9N\beta^2]}
S(q)
}
\]

其中 `N=P/b`，且

\[
K_{31}=81D_x\alpha^4+18H\alpha^2\beta^2+D_y\beta^4,
\]

\[
K_{13}=D_x\alpha^4+18H\alpha^2\beta^2+81D_y\beta^4.
\]

secondary 自身的线性临界总轴力为

\[
\boxed{P_{cr,31}=bK_{31}/\beta^2}
\]

和

\[
\boxed{P_{cr,13}=bK_{13}/(9\beta^2)}.
\]

这两个量直接给出 detuning；若 current path 接近其中任一值，则普通 `O(epsilon^3)` secondary ordering 可能失效，必须提升该模态。

---

## 4. 为什么只检查 terminal 理论点就是 current path 的最不利 leading-order 检查

current 单模态结构关系为

\[
P(q)=P_{cr}\frac{q}{q+q_0}+Cq(q+2q_0).
\]

对 `q>=0,q0>0,C>0`：

\[
\frac{dP}{dq}
=P_{cr}\frac{q_0}{(q+q_0)^2}+2C(q+q_0)>0.
\]

同时

\[
\frac{S(q)}q=(q+q_0)(q+2q_0)
\]

随 `q` 严格增加。

只要 secondary detuning denominators 在路径内保持正值，则 `|q_x^{(1)}/q|`、`|q_y^{(1)}/q|` 随 `q` 增大。因此在 current production 路径 `0<=q<=q_u` 上，冻结 theory terminal `q_u` 是 leading-order secondary-smallness 的最不利端点。

这里使用 `q_u` 的身份只是“当前理论 admissible path 的上界”；没有使用 comparator。

---

## 5. 冻结结构输入：BH032

来源：current common-R06 BH032 blind execution。

```text
b = 1600 mm
ell = 1600 mm
a_phys = 3200 mm
m* = 2
q0 = 0.0025
q_u = 0.00137889961633743
P_u(N1) = 10.9405345132294 MN
rho_w = 0.0198214285714286
tc = 42 mm
ts = 4 mm
Es = 206000 MPa
nu_s = 0.30
Ec = 43400 MPa
nu_c = 0.20
```

由冻结 initial full-composite ABD 公式得到

\[
A_{11}=3.67210307348901\times10^6\ \mathrm{N/mm},
\]
\[
A_{22}=3.84359807348901\times10^6\ \mathrm{N/mm},
\]
\[
A_{12}=9.15519515796703\times10^5\ \mathrm{N/mm},
\]
\[
A_{66}=1.37829177884615\times10^6\ \mathrm{N/mm}.
\]

其逆矩阵分量

\[
\bar A_{11}=2.89516681208732\times10^{-7}\ \mathrm{mm/N},
\]
\[
\bar A_{22}=2.76598924904722\times10^{-7}\ \mathrm{mm/N}.
\]

弯曲刚度

\[
D_x=1.23401160601534\times10^9\ \mathrm{N\,mm},
\]
\[
D_y=1.25922137101534\times10^9\ \mathrm{N\,mm},
\]
\[
H=1.23401160601534\times10^9\ \mathrm{N\,mm}.
\]

这些量回代 primary elastic front 给出

\[
P_{cr,1}=30.6035224490574\ \mathrm{MN},
\]

与冻结 BH032 theory 值一致。

---

## 6. BH032 detuning 与 secondary-smallness

secondary critical loads：

\[
\boxed{P_{cr,31}=761.355905112518\ \mathrm{MN}},
\]

\[
\boxed{P_{cr,13}=85.9773806102488\ \mathrm{MN}}.
\]

因此在 current terminal：

\[
\boxed{P_u/P_{cr,31}=0.01436980319},
\]

\[
\boxed{P_u/P_{cr,13}=0.1272489861}.
\]

即两个第一代 secondary 都没有接近自己的线性临界；最接近的 `(1,3m*)` 仍只达到约 `12.725%` 的自身临界荷载。

leading-order secondary amplitudes：

\[
q_x^{(1)}=1.62231242964\times10^{-7},
\]

\[
q_y^{(1)}=1.72224935779\times10^{-7}.
\]

相对 primary：

\[
\boxed{|q_x^{(1)}|/q_u=1.17652685549\times10^{-4}}
\]

\[
\boxed{|q_y^{(1)}|/q_u=1.24900271012\times10^{-4}}.
\]

也就是每一个都只有 primary 的约 `0.012%`。

纯理论 critical-point ranking：

\[
\Gamma_x=3.05182084383\times10^{-5},
\qquad
\Gamma_y=4.27522403105\times10^{-5},
\]

\[
\boxed{\Gamma_x/\Gamma_y=0.7138388121}.
\]

二者同量级，所以：如果决定进入五阶，不能只选一个做 N=2；应保留完整 N=3。

---

## 7. 冻结结构输入：BH050

来源：current common-R06 BH050 blind execution。

```text
b = 2500 mm
ell = 2500 mm
a_phys = 5000 mm
m* = 2
q0 = 0.0025
q_u = 0.004772819645833164
P_u(N1) = 13.3563763545430 MN
rho_w = 0.0126857142857143
tc = 42 mm
ts = 4 mm
Es = 206000 MPa
nu_s = 0.30
Ec = 43400 MPa
nu_c = 0.20
```

冻结 ABD（与 blind execution 中直接打印的 BH050 values 一致）：

\[
A_{11}=3.68565201098901\times10^6\ \mathrm{N/mm},
\]
\[
A_{22}=3.79540881098901\times10^6\ \mathrm{N/mm},
\]
\[
A_{12}=9.18229303296703\times10^5\ \mathrm{N/mm},
\]
\[
A_{66}=1.38371135384615\times10^6\ \mathrm{N/mm},
\]

\[
\bar A_{11}=2.88725000131878\times10^{-7}\ \mathrm{mm/N},
\qquad
\bar A_{22}=2.80375561725474\times10^{-7}\ \mathrm{mm/N},
\]

\[
D_x=1.23600329982784\times10^9\ \mathrm{N\,mm},
\]
\[
D_y=1.25213754942784\times10^9\ \mathrm{N\,mm},
\]
\[
H=1.23600329982784\times10^9\ \mathrm{N\,mm}.
\]

回代 primary front：

\[
P_{cr,1}=19.5818772367311\ \mathrm{MN},
\]

与冻结 BH050 theory 值一致。

---

## 8. BH050 detuning 与 secondary-smallness

secondary critical loads：

\[
\boxed{P_{cr,31}=488.018239774017\ \mathrm{MN}},
\]

\[
\boxed{P_{cr,13}=54.7904307690612\ \mathrm{MN}}.
\]

terminal ratios：

\[
\boxed{P_u/P_{cr,31}=0.02736860073},
\]

\[
\boxed{P_u/P_{cr,13}=0.2437720632}.
\]

BH050 的 `(1,3m*)` 比 BH032 更接近自己的临界，但仍只有约 `24.38%`，不存在 denominator collapse / near resonance。

leading-order：

\[
q_x^{(1)}=3.93090909446\times10^{-6},
\]

\[
q_y^{(1)}=4.85884634590\times10^{-6}.
\]

相对 primary：

\[
\boxed{|q_x^{(1)}|/q_u=8.23603108048\times10^{-4}}
\]

\[
\boxed{|q_y^{(1)}|/q_u=1.01802429307\times10^{-3}}.
\]

即约 `0.082%` 和 `0.102%`，仍是清楚的高阶小量。

ranking：

\[
\Gamma_x=3.00586159810\times10^{-5},
\qquad
\Gamma_y=4.31503828847\times10^{-5},
\]

\[
\boxed{\Gamma_x/\Gamma_y=0.6966013734}.
\]

仍然同量级；所以五阶若启用，理论上仍要求 N=3 而不是人为 N=2。

---

## 9. 再做一次更强的门禁：完整 first-generation N=3 在同一 q1 下实际改变多少 P？

仅看 leading-order secondary amplitudes 已足以判断层级，但本轮进一步做一个不修改 terminal 的结构骨架诊断。

取

\[
w_d=b[q_1\phi_{11}+q_x\phi_{31}+q_y\phi_{13}],
\]

初始缺陷仍为

\[
w_i=bq_0\phi_{11}.
\]

对这三个模态：

1. 对每一对 `(i,j)` 用 exact Marguerre bracket 和和差频规则生成有限 Airy cosine harmonics；
2. 每个 harmonic 直接除以
   \[
   \Lambda(p,q)=\bar A_{22}(p\alpha)^4+(2\bar A_{12}+\bar A_{66})(p\alpha)^2(q\beta)^2+\bar A_{11}(q\beta)^4;
   \]
3. 用 exact Navier orthogonality / Kronecker selection 投影 transverse equilibrium；
4. 得到三个有限三次残量 `R1=Rx=Ry=0`；
5. 固定 `q1=q_u^(N1)`，仅求 `(qx,qy,P)`。

此过程没有空间数值积分，也没有加载步；它是 finite algebraic N=3 Galerkin solve。

### 9.1 内部一致性检查

把 secondary amplitudes 强制为零时，N=3 residual generator 的 primary equation 严格退化回冻结单模态关系

\[
P=P_{cr}\frac{q}{q+q_0}+Cq(q+2q_0).
\]

数值回归：

```text
BH032 -> 10.94053451322943 MN
BH050 -> 13.35637635454304 MN
```

与 current N=1 值一致到打印精度。

### 9.2 BH032 N=3 structural-only diagnostic

固定

\[
q_1=0.00137889961633743.
\]

三残量 simultaneous root：

\[
q_x=1.62034516978\times10^{-7},
\]

\[
q_y=1.71998375963\times10^{-7},
\]

\[
\boxed{P_{Airy,N3}(q_1)=10.9405228425695\ \mathrm{MN}}.
\]

相对 current N=1：

\[
\boxed{
\frac{P_{Airy,N3}-P_{Airy,N1}}{P_{Airy,N1}}
=-1.06673580857\times10^{-6}
=-0.000106674\%.
}
\]

### 9.3 BH050 N=3 structural-only diagnostic

固定

\[
q_1=0.004772819645833164.
\]

simultaneous root：

\[
q_x=3.88238484502\times10^{-6},
\]

\[
q_y=4.78823322342\times10^{-6},
\]

\[
\boxed{P_{Airy,N3}(q_1)=13.3553970684898\ \mathrm{MN}}.
\]

相对 N=1：

\[
\boxed{
\frac{P_{Airy,N3}-P_{Airy,N1}}{P_{Airy,N1}}
=-7.33197408669\times10^{-5}
=-0.00733197\%.
}
\]

这两个 `P_Airy,N3(q1)` **不是新的 Pu**。若未来正式把 N=3 提升到 production，terminal demand/capacity interface 也必须一致重建并重新联立。这里仅用于隔离“first-generation modal feedback 对当前结构 P(q) 骨架的高阶修正量”。

---

## 10. 三阶还是五阶？

现在可以不用 comparator 作出理论裁决。

BH032 terminal 前：

- 最大 first-generation secondary / primary 约 `1.25e-4`；
- 最接近的 secondary 仅达到自身临界荷载的 `12.7%`；
- 完整 first-generation N=3 对同 q1 的结构载荷修正约 `1.07e-6` relative。

BH050 terminal 前：

- 最大 first-generation secondary / primary 约 `1.02e-3`；
- 最接近的 secondary 达到自身临界荷载的 `24.4%`，但仍无 near-resonance；
- 完整 first-generation N=3 对同 q1 的结构载荷修正约 `7.33e-5` relative。

因此，至少对当前两个关键 BH cases，在 **不使用 FEM/试验** 的纯理论门禁下，第一代 modal feedback 在 current terminal 前仍保持明确的高阶尺度分离。

结论：

\[
\boxed{
\text{current structural backbone 保持三阶单模态 }N=1
}
\]

而不是现在就把 production 升级为五阶 N=3。

这个结论的理由已经从旧的

```text
multi-mode cannot remain explicit
```

正式替换为

```text
finite multi-mode is explicit;
N=1 is retained because first-generation modal feedback is asymptotically subordinate on the current admissible path.
```

---

## 11. 为什么这不会重新陷入不断增大 N

当前禁止采用：

```text
N=1 -> N=3 -> N=5 -> ... until Pu convergence
```

正式 structural-order governance 改为：

1. production 目标阶次当前固定为 cubic / `O(epsilon^3)`；
2. first-generation secondary modes 是 `O(epsilon^3)` amplitudes，其对 primary equilibrium 的回馈属于更高阶；
3. 只有出现理论上的 order-promotion event 才重开五阶：
   - secondary detuning denominator 接近零；或
   - secondary/primary 不再保持高阶小量；或
   - 项目明确决定把 structural asymptotic target 从 `O(epsilon^3)` 提升到 `O(epsilon^5)`；
4. 若五阶被正式开启，则第一代完整集合直接固定为 N=3，不用 N-convergence 决定；
5. 再高代模态只有在更高目标阶次或新的近共振事件下才进入。

因此模态数量由 **目标渐近阶次 + 理论近共振门禁** 决定，而不是由数值收敛循环决定。

---

## 12. 当前治理裁决

```text
CURRENT_PRODUCTION_STRUCTURAL_ORDER = CUBIC / THIRD_ORDER
CURRENT_PRODUCTION_MODAL_SET = {(1,m*)}
CURRENT_PRODUCTION_N = 1

FINITE_MULTIMODE_EXPLICITNESS = PASS
FIRST_GENERATION_COMPLETE_SET = {(1,m*),(3,m*),(1,3m*)}
FIRST_GENERATION_COMPLETE_N = 3
FIRST_GENERATION_N2_REDUCTION = NO

BH032_SECONDARY_DETUNING = SAFE
BH050_SECONDARY_DETUNING = SAFE
BH032_FIRST_GENERATION_FEEDBACK = ASYMPTOTICALLY_SUBORDINATE
BH050_FIRST_GENERATION_FEEDBACK = ASYMPTOTICALLY_SUBORDINATE

PROMOTE_TO_FIFTH_ORDER_NOW = NO
N_CONVERGENCE_POLICY = PROHIBITED
FEM_TEST_BASED_ORDER_SELECTION = PROHIBITED

PRODUCTION_Pu_CHANGED_BY_THIS_AUDIT = NO
PRODUCTION_TERMINAL_CHANGED_BY_THIS_AUDIT = NO
qU_STATUS_CHANGED = NO
```

### 下一次只有什么情况才需要重开 N=3？

不是因为 comparator 偏差，而是某个新结构参数使纯理论指标出现下列情形之一：

\[
K_{31}-N\beta^2\to0
\]

或

\[
K_{13}-9N\beta^2\to0,
\]

或者 secondary amplitude 与 primary 失去清楚的高阶尺度分离。

在那之前，N=3 保留为显式五阶扩展储备，不进入 current production。
