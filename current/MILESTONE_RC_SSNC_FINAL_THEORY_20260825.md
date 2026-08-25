# NZ-SCCM Milestone — 钢筋混凝土（RC）与钢壳混凝土（SSNC）最终阶段理论总账

**Date:** 2026-08-25  
**Identity:** `RC + STEEL-SHELL CONCRETE FINAL-STAGE THEORY MILESTONE / CHAT HANDOFF MEMORY`  
**Purpose:** 把当前聊天结束时已确认的钢筋混凝土与钢壳混凝土理论主线、求解流程、结果身份、已淘汰路径和下一步边界冻结到一个文件，供后续聊天直接恢复。  

---

# 0. 总结性结论

当前项目已经形成两条彼此一致、但终端材料形式不同的极限承载力理论主线：

```text
共同结构骨架：
原始试件参数
-> 控制代表半波
-> 初始弹性复合刚度
-> Marguerre–Airy / Galerkin 连续结构需求
-> terminal material/resultant capacity
-> Pu

共同治理：
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_THICKNESS_QUADRATURE = 0（在当前最终端点可退化时）
MATERIAL_POINTS = 0
EXPERIMENT_IN_ROOT_SELECTION = 0
FEM_IN_ROOT_SELECTION = 0
EFFECTIVE_WIDTH/AREA_PRODUCTION = PROHIBITED
CURRENT_MATERIAL_TANGENT_INTO_AIRY = NO
```

钢筋混凝土（RC）当前锁定的结构思想是：

\[
\boxed{
\text{Airy/Galerkin global structural demand}
\to
\text{reinforced-concrete terminal resultant capacity}
\to P_u
}
\]

钢壳混凝土（SSNC）在此基础上进一步闭合为：

\[
\boxed{
\text{Airy demand}
\to
\text{common terminal strain bridge}
\to
\text{NC-M6 concrete}
+
\text{R02 PBL steel-face trial}
+
\text{R04 ideal-EP cap}
+
\text{web steel}
\to
\text{section resultants}
\to P_u
}
\]

当前两个代表性最终结果为：

```text
RC Case21 authoritative blind global baseline:
Pu = 368.189337 kN
experiment post-check = 368.312749744 kN
error = -0.0335 %

SSNC Z6 R05 final independent endpoint:
Pu = 49.45439833719624 MN
Zhou post-check = 49.48676675 MN      -> -0.0654082 %
Winter post-check = 50.18585413 MN    -> -1.4574940 %
```

重要：RC 的 `368.189337 kN` 是当前结构架构恢复后保留的权威 blind/global 回归基线；NC-M6 作为终端材料层的 Panel1/14/21 共架构批量重算仍是 RC 后续任务。不能把后来被否决的 local `det Jsec=0` 结果当作 RC 最终 Pu。

---

# PART A — 钢筋混凝土 RC

# 1. RC 当前最终理论架构

## 1.1 结构层：Marguerre–Airy 只负责结构需求

结构层使用几何与初始弹性刚度，先求连续后屈曲需求。当前基本后屈曲荷载族写为

\[
\boxed{
P_{pb}(q)=P_{cr}\frac{q}{q+q_0}+Cq(q+2q_0).
}
\]

对单代表半波的典型局部截面需求：

\[
\boxed{
n(s;q)=\frac{P_{pb}(q)}b+Gq(q+2q_0)(1-2s^2),}
\]

\[
\boxed{m(s;q)=Jqs.}
\]

`Ppb(q)` 在 admissible `q>=0` 上单调，这一事实仅用于消除无必要的加载路径追踪；**不意味着必须通过 `dP/dq=0` 才能得到 Pu**。

RC 当前明确：

```text
MA_V1_MONOTONE_POSTBUCKLING = TRUE
MA_V1_GLOBAL_FOLD_REQUIRED_FOR_Pu = FALSE
CURRENT_MATERIAL_IN_AIRY_COMPATIBILITY = NO
NONLINEAR_CURRENT_MATERIAL_GLOBAL_WORK_CLOSURE = RETRACTED
```

## 1.2 终端层：材料只决定当前 Airy demand 是否达到容量边界

对原始单轴/弯曲 RC 终端，V1 形式为

\[
F_N(q,s,c)=n_d(s,q)-n_u(c)=0,
\]

\[
F_M(q,s,c)=m_d(s,q)-m_u(c)=0.
\]

若控制点位于内部，还需

\[
F_S(q,s,c)=0,
\]

即

\[
\boxed{F_N=F_M=F_S=0}
\]

或相应 endpoint / active-set 方程。

对真正的二维材料状态，终端必须同时满足纵向与横向 resultant capacity；若 shear demand 非零，还需同步进入终端约束。NC-M6 可以用于这个 terminal layer，但不能反向改写 Airy 初始兼容方程。

---

# 2. RC 连续运动学与材料层

## 2.1 代表半波

物理域首先由初始弹性板稳定确定控制整数模态

\[
N_{cr,j}=\pi^2\left[
\frac{D_xa_{phys}^2}{j^2b^4}
+\frac{2H}{b^2}
+\frac{D_yj^2}{a_{phys}^2}
\right],
\qquad P_{cr,j}=bN_{cr,j}.
\]

\[
\boxed{m_* = \arg\min_j P_{cr,j},\qquad \ell=a_{phys}/m_*.}
\]

Case21 从真实全长 `a_phys=2440 mm` 起算，得到

\[
\boxed{m_*=2,\qquad \ell=1220\ \mathrm{mm},\qquad k=b/\ell=1.}
\]

正式非线性理论只处理一个连续完整代表半波；重复半波不建立独立空间材料点。

## 2.2 Nguyen 二阶运动学 / 项目兼容面内场

令

\[
X=\pi x/b,\qquad Y=\pi y/\ell,
\]

\[
w_0=bq_0\sin X\sin Y,
\qquad
\Delta w=bq\sin X\sin Y.
\]

定义

\[
M(q)=\frac{\pi^2}{\varepsilon_0}\left(q_0q+\frac12q^2\right),
\qquad
\beta(q)=\frac{\pi^2q}{\varepsilon_0b}.
\]

统一归一化应变写为

\[
e_x=\nu D+MF_x+\alpha A_x+\beta zH_s,
\]

\[
e_y=-D+k^2MF_y+\alpha A_y+k^2\beta zH_s,
\]

\[
\gamma=2kc_Xc_Y[(M-\alpha)H_s-\beta z],
\]

物理应变为 `eps0 * e`。

## 2.3 普通混凝土与钢筋

当前理论历史中已有完整 finite current-map / NC-M6 两个层次：

- R15 从零计算账本保留 finite global R10 current operator，作为完整连续三变量理论规范；
- RC 当前架构修正后，NC-M6 被保留为**终端材料候选**，不进入 Airy compatibility。

Case21 钢筋源参数：

```text
rho_sx = rho_sy = 0.00375
z_sx = z_sy = 0
Es = 200000 MPa
fy = 530 MPa
```

在释放的 Case21 状态，钢筋仍处于弹性，因此钢筋相可直接得到闭式轴力与广义残量贡献。

---

# 3. RC 最终求解流程

当前必须按以下顺序理解：

```text
[RC-1] 原始试件参数
    ↓
[RC-2] 初始弹性 A/D/H 与整数半波筛选
    ↓
[RC-3] 一个连续完整代表半波
    ↓
[RC-4] Nguyen 二阶运动学 + 兼容 Airy 面内场
    ↓
[RC-5] Marguerre–Airy / Galerkin 得到 Ppb(q) 与局部 resultant demand
    ↓
[RC-6] terminal RC capacity：混凝土 + 双向钢筋
    ↓
[RC-7] N-M contact；二维状态时扩展为 Nx/Ny/Mx/My/必要 shear capacity contact
    ↓
[RC-8] 全部理论根先固定
    ↓
[RC-9] 才打开 Pf / comparator 做后验验证
```

禁止替换为：

```text
local section det(Jsec)=0 -> plate Pu
```

因为 Panel21 A/B/D regression 已证明，这一局部 singularity 架构会把同一尺度的 Case21 预测从约 `368 kN` 拉低到约 `161–173 kN`，而改变 source waveform 只造成约 `+7.7%` 的相对变化，不能解释约 50% 的塌降。

因此：

```text
LOCAL_detJsec_AS_PRIMARY_PLATE_Pu = REJECTED
SOURCE_WAVEFORM_DETAIL_AS_PRIMARY_COLLAPSE_CAUSE = REJECTED
AIRY_GLOBAL_DEMAND_THEN_TERMINAL_CAPACITY = RESTORED
```

---

# 4. RC 当前有效计算结果

## 4.1 Case21 权威 blind/global 回归基线

当前 RC 总账明确保留：

\[
\boxed{P_u=368.189337\ \mathrm{kN}}.
\]

该结果是在试验值读取前得到的，之后才与

\[
P_f=368.3127497435694\ \mathrm{kN}
\]

比较：

\[
\boxed{\text{error}=-0.0335\%.}
\]

独立新鲜 N48-C1/MM 复算：

\[
\boxed{P_u=365.607776\ \mathrm{kN}},
\]

与试验差约

\[
\boxed{-0.734\%}.
\]

这两项共同证明：历史 global branch 的近准确结果不是根据试验选出的偶然根。

## 4.2 R15 三变量从零账本的 sealed regression target

R15 完整三变量理论账本还保留另一套 sealed regression target：

```text
Du     = 0.7887924801
qu     = 0.0018083572562965242
alphau = 0.002506908330448254
Pc     = 337.92303037 kN
Ps     = 28.844798318 kN
Pu     = 366.7678286852115 kN
experiment post-check = 368.3127497435694 kN
error = -0.419459 %
```

该数值必须保持其证据身份：它是 R15 的 sealed regression target，不是当前 RC 架构中用于替代 `368.189337 kN` blind/global baseline 的新 production 数值。

## 4.3 被否决的 local-fold 结果只作反例

```text
ideal m=2 + local detJsec: 160.778280 kN
source waveform + local detJsec: 173.209915 kN
```

它们当前只用于证明 `detJsec` 不能自动当作板 Pu；不得重新提升为最终 RC 结果。

---

# 5. RC 当前尚未完成的唯一主任务

当前 RC 文件已经明确：

```text
NEXT_RC_TASK =
RECOMPUTE PANEL1 / PANEL14 / PANEL21
WITH MARGUERRE-AIRY DEMAND + NC-M6 TERMINAL CAPACITY
```

严格要求：

```text
AIRY structural demand unchanged
NC-M6 only in terminal capacity layer
uniaxial -> N-M contact
biaxial -> longitudinal + transverse resultant capacity
NO detJsec as plate Pu
zero formal spatial quadrature/material points
no Pf in operator/root selection
```

因此本里程碑对 RC 的身份是：

\[
\boxed{\text{理论架构已纠正并冻结；Case21 global blind基线已验证；NC-M6终端三板批算尚待执行。}}
\]

---

# PART B — 钢壳混凝土 SSNC

# 6. SSNC 当前最终理论架构

钢壳混凝土保留与 RC 一致的结构/材料角色分离：

```text
initial full composite ABD
-> Marguerre–Airy structural demand
-> common terminal strain state
-> phase current material maps
-> terminal resultant equilibrium/capacity
-> Pu
```

Airy 初始刚度已经完整包含外钢面偏心平行轴贡献：

\[
D_s^0=2Q_s\left(t_sz_f^2+\frac{t_s^3}{12}\right).
\]

2026-08-25 Z0–Z6 audit 已证明 archived/current Airy 刚度对七块试件均包含该项。因此：

```text
R07_AIRY_OFFSET_CORRECTION_NEEDED = NO
ADD_STEEL_OFFSET_AGAIN = PROHIBITED_DOUBLE_COUNTING
```

R03 的 current 6x6 tangent 保持诊断价值，但不是当前 Pu gate；R05 没有重开 R03。

---

# 7. SSNC Z6 R05 common-endpoint 闭合

## 7.1 独立根来源

在 R05 之前已完成广域 multi-seed endpoint 搜索：

- 不使用历史 provisional `Pu/X/q` 作种子；
- 不读取 Zhou/Winter 选根；
- 得到唯一正根聚类约

\[
X\approx0.97579742,
\qquad
q\approx0.01180088.
\]

R05 只对该独立根做高精度精化。

## 7.2 common terminal strain bridge

Z6 当前控制点为对称 endpoint：

\[
\boxed{s=0,\qquad M_y^d=0.}
\]

R05 明确冻结

\[
\boxed{
Y\equiv\frac{\varepsilon_y}{\varepsilon_0}=-1,
\qquad
\gamma_{xy}=0,
\qquad
X\equiv\frac{\varepsilon_x}{\varepsilon_0}.
}
\]

因此上下钢面具有完全相同的平均膜应变，平行轴 moment 自动反号抵消。

这一 endpoint degeneration 正式 supersede 了早前

```text
R02-R04_DIRECT_INTERFACE_BLOCKED_AT_FACE_STRAIN_MAP
```

但 supersession 仅针对 Z6 R05 对称 endpoint，不自动推广到所有 `s!=0` 或所有 Z0–Z5。

---

# 8. SSNC Z6 R05 材料与钢面求解

## 8.1 精化根

\[
\boxed{X=0.975797415476470457703134943536555645461}
\]

\[
\boxed{q=0.01180088028170258636542452885480436575091}
\]

R02 condensed total local amplitude：

\[
\boxed{U=0.1270986806879544830159288254178676823454\ \mathrm{mm}}.
\]

物理应变：

\[
\boxed{\varepsilon_x=+0.00182595997641601044644,}
\]

\[
\boxed{\varepsilon_y=-0.0018712490394580678,}
\qquad
\boxed{\gamma_{xy}=0.}
\]

## 8.2 NC-M6 concrete

Poisson-neutral coordinates：

\[
\boxed{\lambda_t=0.822444621203462647482,}
\]

\[
\boxed{\lambda_c=-0.851959968183376723453.}
\]

当前状态：

```text
TC branch = TC-B
T branch  = RESID
gamma     = ACTIVE
```

具体：

\[
s_c=-30.0140575986534918155\ \mathrm{MPa},
\]

\[
f_{cr}=0.115782720403952455364\ \mathrm{MPa},
\]

\[
\gamma_c=0.926242245191947267213.
\]

\[
\boxed{\sigma_x^c=+0.0347348161211857366092\ \mathrm{MPa},}
\]

\[
\boxed{\sigma_y^c=-27.8002880974972355703\ \mathrm{MPa}.}
\]

## 8.3 R02 PBL/Yun face operator

R02 使用 compression-positive mean strain convention：

\[
(e_x,e_y,\gamma)_{R02}=(-\varepsilon_x,-\varepsilon_y,0).
\]

固定根处：

\[
L_0=0.00493280024998645449729,
\]

\[
B_3=1.17975350735700040389,
\]

\[
B_1=2.29419452855441005419,
\]

\[
B_0=-0.294011322388344352684.
\]

明确 cubic：

\[
\boxed{
1.17975350735700040389U^3
+2.29419452855441005419U
-0.294011322388344352684=0.
}
\]

因为

\[
3B_3U^2+B_1>0
\]

对全部实数成立，所以只有一个实根：

\[
\boxed{U=0.127098680687954483016\ \mathrm{mm}}.
\]

其 R02 condensed-energy functional：

\[
2.16666537729371273899
\]

（保持 R02 源归一化身份）。

## 8.4 R04 ideal-EP 2D terminal cap

R02 trial stress 转为物理 tension-positive convention：

\[
\boxed{
\boldsymbol\sigma^{tr}
=(+286.326378023188732292,
-299.539050646088282145,0)\ \mathrm{MPa}.
}
\]

trial Mises：

\[
\boxed{\sigma_{VM}^{tr}=507.417351951859018137\ \mathrm{MPa}}.
\]

R04 radial scale：

\[
\boxed{\lambda_p=0.699621324801837792705.}
\]

capped stress：

\[
\boxed{
\boldsymbol\sigma_s
=(+200.320039918295114535,
-209.563907442901070574,0)\ \mathrm{MPa}
}
\]

并满足

\[
\boxed{\sigma_{VM}=355\ \mathrm{MPa}}.
\]

纵向等效 web 同时达到

\[
\boxed{\sigma_y^w=-355\ \mathrm{MPa}}.
\]

---

# 9. SSNC Z6 phase resultants 与 Airy demand

物理 tension-positive convention，单位 `N/mm`：

| phase | Nx | Ny |
|---|---:|---:|
| concrete core | +4.152894615449 | -3323.802444936769 |
| 2% equivalent longitudinal web | 0 | -866.200000000000 |
| upper external face | +801.280159673180 | -838.255629771604 |
| lower external face | +801.280159673180 | -838.255629771604 |
| **section total** | **+1606.713213961810** | **-5866.513704479978** |
| **Airy demand** | **+1606.713213961810** | **-5866.513704479978** |

因此

\[
\boxed{N_x^{sec}=N_x^d,\qquad N_y^{sec}=N_y^d.}
\]

Z6 face centroid：

\[
z_f=63\ \mathrm{mm}.
\]

upper face：

```text
Mparallel_x = +50480.65005941037 N
Mparallel_y = -52810.10467561107 N
```

lower face：

```text
Mparallel_x = -50480.65005941037 N
Mparallel_y = +52810.10467561107 N
```

故

\[
\boxed{\mathbf M_{parallel}^{top+bottom}=\mathbf0}
\]

与 endpoint `My=0` 一致。

高精度 residual：

```text
R02 cubic residual < 1e-68
|Rx| < 2e-68 N/mm
|Ry| < 1e-68 N/mm
```

普通 double 复核仍保持约 `1e-12 N/mm` 的 force residual。

---

# 10. SSNC Z6 最终 Pu 与比较

最终固定：

\[
\boxed{P_u^{R05}=49.45439833719624\ \mathrm{MN}}.
\]

根、材料状态、R02 root、R04 cap 和 phase resultants 全部固定以后才打开 comparators：

\[
P_{Zhou}=49.48676675\ \mathrm{MN},
\]

\[
P_{Winter}=50.18585413\ \mathrm{MN}.
\]

所以

\[
\boxed{R05-Zhou=-0.0654082\%,}
\]

\[
\boxed{R05-Winter=-1.4574940\%.}
\]

无任何 post-comparison retuning。

---

# 11. Z0–Z6 R07 历史 resultant baseline（仅用于谱系）

R07 在 R05 之前的统一 `Ny-My` resultant baseline 为：

| Case | R07 Pu / MN | status after R05 |
|---|---:|---|
| Z0 | 37.825706787 | retained historical/current R07 baseline; R05 common-endpoint rerun not executed |
| Z1 | 24.714128548 | retained historical/current R07 baseline; R05 common-endpoint rerun not executed |
| Z2 | 42.959011131 | retained historical/current R07 baseline; R05 common-endpoint rerun not executed |
| Z3 | 46.495651955 | retained historical/current R07 baseline; R05 common-endpoint rerun not executed |
| Z4 | 70.265718566 | retained historical/current R07 baseline; R05 common-endpoint rerun not executed |
| Z5 | 14.118193577 | retained historical/current R07 baseline; R05 common-endpoint rerun not executed |
| Z6 | 56.379421090 | **superseded for Z6 by R05 = 49.454398337 MN** |

该表不能误解为七块均已完成 R05。当前只确认 Z6 的 R02/R04 common-endpoint bridge 与独立根。

---

# 12. 两条理论的统一认识

RC 与 SSNC 最终都不再采用“材料当前切线反写 Airy”的思路。二者统一为：

\[
\boxed{
\text{初始弹性稳定/后屈曲结构需求}
\quad + \quad
\text{终端材料/截面容量约束}
\quad \Rightarrow \quad
P_u.
}
\]

不同点只在 terminal material map：

### RC

```text
ordinary concrete terminal map
+ discrete reinforcement phases
-> N-M / biaxial resultant capacity contact
```

### SSNC

```text
NC-M6 core
+ R02 local PBL/Yun face redistribution
+ R04 ideal-EP face cap
+ equivalent longitudinal web
-> full phase resultant equilibrium/capacity
```

所以当前项目不需要两套互相矛盾的“结构求解器”。结构前端是共同的 Marguerre–Airy demand；材料区别只进入最后的 capacity layer。

---

# 13. 明确淘汰 / 不得复活

```text
1. local detJsec = 0 直接作为 RC plate Pu
2. current material tangent 回馈 Airy 作为 Pu 必要前置
3. 重开 R03 post-yield 6x6 tangent 作为 Z6 R05 门槛
4. 给 Airy 再加一次 steel-face offset stiffness
5. effective width / effective area production
6. Gauss / Simpson / spatial material-point integration 作为正式理论
7. 用试验 / Zhou / Winter 选根或调参
8. 把旧 provisional Pu / X / q 作为 R05 独立根 seed
9. 把 Z6 R07 56.37942109 MN 当作 R05 后最终值
10. 把 RC local-fold 160–173 kN 当作 Case21 最终结果
```

---

# 14. 本里程碑后的当前状态

```text
RC:
  theory architecture = FROZEN/CORRECTED
  structural front = MARGUERRE_AIRY
  terminal = RESULTANT CAPACITY
  authoritative Case21 blind baseline = 368.189337 kN
  NC-M6 P1/P14/P21 common-architecture rerun = NEXT / NOT YET EXECUTED

SSNC:
  R02 = AVAILABLE
  R04 = AVAILABLE
  common endpoint bridge for Z6 = CLOSED
  independent R05 root = FIXED
  Z6 Pu = 49.45439833719624 MN
  R03 = NOT REOPENED
  offset stiffness correction = NOT NEEDED
```

---

# 15. 关键来源文件

RC：

- `current/RC_CURRENT_STATE_20260822.md`
- `semantic_v2/40_execution/20260823_0322__NZSCCM__MARGUERRE_AIRY_TERMINAL_CAPACITY_ARCHITECTURE_CORRECTION.md`
- `semantic_v2/40_execution/20260823_0058__NZSCCM__PANEL21_GLOBAL_VS_LOCAL_LIMIT_REGRESSION_AUDIT_R01.md`
- `semantic_v2/20_theory/20260819__NZSCCM__R15_FULL_FROM_ZERO_CALCULATION_LEDGER_CASE21_Z6.md`

SSNC：

- `semantic_v2/40_execution/steel_shell/20260825_0130__NZSCCM__SSNC_R02_PBL_2D_FULL_RESULTANT_GATE.py`
- `semantic_v2/40_execution/steel_shell/20260825_0851__NZSCCM__SSNC_R04_IDEAL_EP_2D_TERMINAL_RESULTANT_GATE.py`
- `semantic_v2/40_execution/steel_shell/20260825_1120__NZSCCM__Z6_R05_COMMON_ENDPOINT_R02_R04_REFINEMENT.py`
- `semantic_v2/40_execution/20260825_1120__NZSCCM__Z6_R05_COMMON_ENDPOINT_R02_R04_MANUAL_RECALC.md`
- `current/CURRENT_STATE.md`

---

# 16. 后续聊天恢复口令

新聊天如果需要从本里程碑继续，应先读取本文件，然后以以下状态开始：

```text
MILESTONE = RC_SSNC_FINAL_THEORY_20260825

RC:
  retain Marguerre-Airy structural demand
  retain terminal capacity architecture
  retain Case21 368.189337 kN blind/global baseline
  do not use local detJsec as plate Pu
  next = NC-M6 terminal-capacity rerun of Panel1/14/21

SSNC:
  retain R07 Airy coefficients and full initial composite ABD
  retain R02 + R04
  retain Z6 common endpoint Y=-1, gamma=0
  retain independent R05 root
  X=0.9757974154764704577
  q=0.01180088028170258637
  U=0.1270986806879544830 mm
  Pu=49.45439833719624 MN
  do not reopen R03
  do not add steel offset stiffness again
```

**This file is the chat-handoff milestone.**
