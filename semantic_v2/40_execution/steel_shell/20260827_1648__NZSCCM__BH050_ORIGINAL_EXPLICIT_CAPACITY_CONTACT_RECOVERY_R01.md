# NZ-SCCM — BH050 原始显式 demand–capacity contact 恢复与 qU 校核 R01

**Time:** 2026-08-27 16:48 +08:00  
**Status:** `SOURCE RELATION RECOVERED / RECENT COMMON-KAPPA INTERPRETATION RETRACTED / CURRENT-MOMENT FEEDBACK NOT USED / qU PRE-CERTIFIED RECALC COMPLETE`  

---

## 0. 本节点回答的问题

本节点不建立新理论，不引入 full-current virtual work，不修改 UHPC、web 或 R06 物理概念。

只回答：

> 2026-08-25 已冻结的 Marguerre–Airy 显式理论 + terminal N–M + R02/R06 中，BH050 所需的显式闭合关系是否本来就存在？近期为什么会把 BH050 越修越偏？

结论：

```text
MISSING_NEW_STRUCTURAL_EQUATION = NO
ORIGINAL_MISSING/LOST_RELATION = AIRY RESULTANT DEMAND <-> TERMINAL N-M CAPACITY CONTACT
TERMINAL_Ax,Bx,Ay,By_ROLE = CAPACITY-SURFACE PARAMETERS
TERMINAL_Bx,By_ARE_GLOBAL_CURVATURE = NO
q_TO_COMMON_CURVATURE_AS_TERMINAL_CONSTRAINT = RETRACTED
CURRENT_MOMENT_FEEDBACK_INTO_AIRY = RETRACTED_FOR_THIS ROUTE
qU_STEEL_LOCAL_REPAIR = RETAIN
FORMAL_SPATIAL_QUADRATURE = 0
```

---

# 1. 原始显式理论已经把结构层和容量层分开

来源：

- `semantic_v2/20_theory/20260821_1733__NZSCCM__MARGUERRE_AIRY_EXPLICIT_LIMIT_THEORY_V1.md`
- `current/MILESTONE_RC_SSNC_FINAL_THEORY_20260825.md`
- `semantic_v2/20_theory/20260825_1530__NZSCCM__STEEL_SHELL_COMMON_R06_LOCAL_YIELD_RESULTANT_GATE_V1.md`

原始显式 V1 明确：

```text
Airy/Galerkin -> structural resultant demand
terminal section -> resultant capacity
Pu = first admissible demand-capacity contact
```

并明确写出 RC 原型：

\[
F_N=n_d(q,s)-n_u(c)=0,
\qquad
F_M=m_d(q,s)-m_u(c)=0.
\]

其中 `c` 是生成 N-M 容量曲线的内部截面参数，不要求等于全局板的实际曲率参数。

20260825 milestone 将这一思想推广到二维 steel-shell terminal：

```text
initial full-composite ABD
-> Marguerre–Airy structural demand
-> common terminal strain state
-> phase current material maps
-> terminal resultant equilibrium/capacity
-> Pu
```

同一 milestone 明确冻结：

```text
CURRENT_MATERIAL_IN_AIRY_COMPATIBILITY = NO
NONLINEAR_CURRENT_MATERIAL_GLOBAL_WORK_CLOSURE = RETRACTED
```

R06 又明确说明：

> common terminal theory is a direct capacity-contact theory rather than an incremental material history model.

因此 terminal strain state 的主要身份是**容量面参数化坐标**，不是必须与全局 `q` 运动学逐点相等的 actual deformation state。

---

# 2. 近期真正的偏离发生在哪里

20260827 之前为解释 BH050 上/下钢面应力差异，将 terminal `kappa_x,kappa_y` 解释成了必须与全局面外模态相同的实际截面曲率，并强制

\[
\kappa_x=\kappa_y=\pi^2q/b.
\]

这一步混淆了两个层次：

1. `q` 的全局几何曲率：属于 Airy/Galerkin 结构需求生成；
2. terminal `B_x,B_y`：属于生成当前截面 N-M 容量边界的内部参数。

原始 capacity-contact 理论并没有要求二者相等。

强制相等之后，原来的四个 resultant contact equations 无法同时保留，于是随后又继续引入 `current moment -> global q equilibrium`。这正是理论层级被连续升级的起点。

因此本节点正式撤回：

```text
TERMINAL_Bx = pi^2 q/b = NO
TERMINAL_By = pi^2 q/b = NO
ANTINODE_CURRENT_MOMENT_AS_GLOBAL_HARMONIC = NO
CURRENT_MOMENT_HARMONIC_CLOSURE_1710 = NOT CURRENT PRODUCTION
```

注意：这并不否认全局 `q` 本身存在几何曲率；只是它不再被错误地拿来替代 terminal capacity-surface parameter。

---

# 3. 恢复后的 BH/SSUHPC 显式结构前端

对于 BH：

\[
ell=b,
\qquad
\alpha=\beta=\pi/b.
\]

定义

\[
Q_q=q(q+2q_0).
\]

结构前端保持 20260825 原式不变：

\[
\boxed{P(q)=P_{cr}\frac{q}{q+q_0}+CQ_q}
\]

\[
\boxed{N_x^d=K_xQ_q}
\]

\[
\boxed{N_y^d=-\left[\frac{P(q)}b+GQ_q(1-2s^2)\right]}
\]

\[
\boxed{M_x^d=J_xqs,
\qquad
M_y^d=J_yqs}
\]

BH050 控制 station 保持既有 blind-search 结果：

\[
\boxed{s=1}.
\]

没有 current material 反写 Airy。

---

# 4. terminal N-M 容量面保持原来的 5 参数形式

对固定 `s=1`，terminal capacity 由

\[
(q,A_x,B_x,A_y,B_y)
\]

参数化。

截面仿射应变只是生成容量 resultants 的参数：

\[
\varepsilon_x(z)=A_x+B_xz,
\qquad
\varepsilon_y(z)=A_y+B_yz.
\]

UHPC 使用现有 exact `S0,S1` primitives；web 使用现有 affine ideal-EP exact primitives；钢面使用 R02/R06。

总 resultants：

\[
N_x^{sec}=N_x^U+N_{x,+}^s+N_{x,-}^s,
\]

\[
M_x^{sec}=M_x^U+z_fN_{x,+}^s-z_fN_{x,-}^s,
\]

\[
N_y^{sec}=N_y^U+N_y^w+N_{y,+}^s+N_{y,-}^s,
\]

\[
M_y^{sec}=M_y^U+M_y^w+z_fN_{y,+}^s-z_fN_{y,-}^s.
\]

极限状态恢复为 milestone 的原始 resultant contact：

\[
\boxed{N_x^{sec}=N_x^d}
\]

\[
\boxed{M_x^{sec}=M_x^d}
\]

\[
\boxed{N_y^{sec}=N_y^d}
\]

\[
\boxed{M_y^{sec}=M_y^d}
\]

再加一个 finite material endpoint。

BH050 既有 governing candidate：

\[
\boxed{A_y-\frac{t_c}{2}B_y=-\varepsilon_{c0}}.
\]

所以仍然是一个有限 5×5 terminal system；不需要空间积分、load stepping 或 current-global feedback。

---

# 5. qU 应该加在哪里

qU 保留，但只属于 steel-face local operator。

对每个实际注册 local cell：

\[
d=U^2-A_0^2,
\]

\[
\Delta=b[(q_0+q)U-q_0A_0].
\]

并使用已建立的 exact GL coefficients：

\[
m_x=e_x-c_xd-h_x\Delta,
\]

\[
m_y=e_y-c_yd-h_y\Delta,
\]

\[
m_\gamma=\gamma-h_\gamma\Delta.
\]

local amplitude 仍来自已推导的一般三次：

\[
B_3U^3+B_2U^2+B_1U+B_0=0.
\]

因此 qU 的正确角色是：

```text
global q
  -> qU changes local steel capacity operator
  -> changes terminal resultant capacity
  -> changes demand-capacity contact root q_u
```

而不是：

```text
q -> force terminal Bx,By -> destroy original N-M contact
```

---

# 6. BH050 qU-OFF regression：严格恢复 frozen common R06 root

为了验证恢复架构没有漂移，先关闭 GL/qU 项，只保留 20260825 common R06。

重新解同一五方程 terminal system 得到：

\[
q=0.00477281964582,
\]

\[
A_x=2.82043141\times10^{-5},
\qquad
B_x=4.40275833779\times10^{-5}\;\mathrm{mm^{-1}},
\]

\[
A_y=-0.00213545798802,
\qquad
B_y=6.49781910467\times10^{-5}\;\mathrm{mm^{-1}},
\]

\[
\boxed{P_u=13.35637635453\;\mathrm{MN}}.
\]

与 20260825 frozen R06：

\[
13.3563763545430\;\mathrm{MN}
\]

一致到显示精度。

对应 R06 regression：

```text
TOP:    eta=1,
        U=0.16926688579 mm,
        mean=(+190.7746096,-75.7434492,0) MPa
BOTTOM: eta=0.38446506838,
        U=2.93984591447 mm,
        mean=(-62.4713151,-222.0555706,0) MPa
```

因此：

```text
RESTORED_FIVE_EQUATION_ARCHITECTURE_REGRESSION = PASS
```

---

# 7. BH050 qU-ON restored-capacity-contact recalculation

在上述原始 5×5 contact system 中打开已存在的 exact qU GL coefficients，不施加 common-kappa identity，不引入 current-moment feedback。

得到当前 pre-certified root：

\[
\boxed{q_u=0.004715120492577262}
\]

\[
\boxed{A_x=1.98641610447\times10^{-5}}
\]

\[
\boxed{B_x=4.42205818884\times10^{-5}\;\mathrm{mm^{-1}}}
\]

\[
\boxed{A_y=-0.00213259496557}
\]

\[
\boxed{B_y=6.51145254490\times10^{-5}\;\mathrm{mm^{-1}}}
\]

active endpoint：

\[
A_y-21B_y=-0.0035.
\]

Airy load：

\[
\boxed{P_u=13.29348446718\;\mathrm{MN}}.
\]

相对 qU-OFF frozen R06：

\[
\boxed{\Delta P_u/P_u=-0.47088\%}.
\]

四个 resultant contact residual 在本次数值求根精度下均约 `1e-11` 或更小：

```text
Nx_sec = Nx_d = 195.7340376453 N/mm
Ny_sec = Ny_d = -5115.8308913846 N/mm
Mx_sec = Mx_d = 29396.9668188203 N
My_sec = My_d = 29697.2986080338 N
```

phase resultants：

```text
Ny_UHPC = -3770.1940103185 N/mm
Ny_faces = -1174.9135738390 N/mm
Ny_web = -170.7233072271 N/mm
```

internal terminal-capacity coordinates at the root：

```text
TOP:    eta = 1.0
        U = 0.01727562617 mm
        mean stress = (+189.0570,-75.8976,0) MPa
BOTTOM: eta = 0.38380722563
        U = 2.84115552117 mm
        mean stress = (-59.1766,-217.8308,-0.4205) MPa
```

重要：这些 `A/B/U/mean stress` 是**terminal capacity construction 的内部状态**。本理论当前只声称 resultant capacity contact 与 Pu；不得再把这些内部容量参数直接解释成 FEM 的 actual deformation/stress field，再据此强制 `B=pi^2q/b`。

---

# 8. comparator 只在 root freeze 后打开

当前 equal-contract BH050 Abaqus peak：

\[
P_{FE}=12.591227\;\mathrm{MN}.
\]

所以 qU-ON restored contact root 后验误差：

\[
\boxed{+5.5774\%}.
\]

这比 frozen qU-OFF common R06 的约 `+6.08%` 略有改善，但 qU 不是大幅修正项；这与其作为遗漏的 GL coupling 而非经验容量折减相一致。

本节点不依据该 comparator 修改任何理论系数。

---

# 9. 为什么近期 BH050“异常”被放大

近期诊断曾把 terminal capacity internal states 与 Abaqus actual local response 直接比较，例如：

- terminal `kappa_x,kappa_y` versus FEM/global geometric curvature；
- terminal upper/lower face mean stress versus FEM physical face stress field。

在 direct capacity-contact 理论中，这种比较不是同一物理对象。

一旦把这种差异错误解释成“运动学不一致”，就会强制 `terminal B=q-curvature`，随后破坏四-resultant N-M contact；再为了补回 moment balance，又继续发明 current-global feedback。BH050 因此从原本约 13.36 MN 的 capacity-contact root 被推到 17.98 MN，再进入 15.13 MN 的 experimental harmonic closure。

因此 BH050 的主要近期问题不是原显式理论缺一条高阶方程，而是：

\[
\boxed{\text{capacity parameterization 被误当成 actual response kinematics。}}
\]

---

# 10. 数值积分/求值身份

本节点的结构、UHPC N-M、web、qU coefficient 均没有数值积分：

```text
SPATIAL_NUMERICAL_QUADRATURE = 0
THICKNESS_NUMERICAL_QUADRATURE = 0
MATERIAL_POINTS = 0
```

qU-ON R06 的 GL+LL local Mises maximum 在本次复算中仍使用连续解析谐波场上的 numerical stationary-point locator；这不是数值积分，但 formal finite-algebraic global-maximum certificate 尚未重新发出。

因此：

```text
qU_OFF_13.35637635453 = FORMAL FROZEN R06 REGRESSION
qU_ON_13.29348446718 = PRE-CERTIFIED RECALC ROOT
```

正式 production 只剩一个 backend certification task：把 qU GL+LL R06 maximum 换成已经定义好的 finite-algebraic candidate enumeration。该任务不得改变本文件的结构方程、材料关系或 root-selection 规则。

---

# 11. 当前裁决

```text
AIRY_P(q) = RETAIN
AIRY_Nx_Ny_Mx_My_DEMAND = RETAIN
TERMINAL_5EQ_RESULTANT_CONTACT = RESTORED
TERMINAL_Bx_By_AS_CAPACITY_PARAMETERS = RESTORED
qU_GL_STEEL_LOCAL = RETAIN
R06_DIRECT_CAPACITY_GATE = RETAIN
q_TO_TERMINAL_COMMON_KAPPA = RETRACTED
CURRENT_MOMENT_GLOBAL_FEEDBACK = RETRACTED
R02_U0_ACTIVESET_EXTENSION = NOT NEEDED FOR RESTORED BH050 ROOT
BH050_qU_OFF_REGRESSION = 13.35637635453 MN
BH050_qU_ON_PRECERTIFIED = 13.29348446718 MN
BH050_EQUAL_CONTRACT_POSTCHECK = +5.5774%
NEXT = FORMAL GL+LL R06 FINITE-ALGEBRAIC MAX CERTIFICATE ONLY
```
