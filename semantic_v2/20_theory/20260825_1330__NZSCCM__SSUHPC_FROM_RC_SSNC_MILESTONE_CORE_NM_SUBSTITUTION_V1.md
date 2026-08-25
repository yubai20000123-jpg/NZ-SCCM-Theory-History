# NZ-SCCM — 钢壳 UHPC：基于 RC–SSNC Unified Terminal-Capacity Milestone 的核心 N-M 替换 V1

**Time:** 2026-08-25 13:30 +08:00  
**Parent milestone:** `current/MILESTONE_RC_SSNC_FINAL_THEORY_20260825.md`  
**Identity:** `SSUHPC = SSNC_MILESTONE + CORE_NM_SUBSTITUTION_ONLY`  
**Status:** `CORRECTED THEORY ANCHOR / NUMERICAL EXECUTION NOT YET PERFORMED`

---

# 0. 最高优先级裁决

钢壳 UHPC **不是独立新建的一套钢壳理论**。

唯一允许的构造是：

\[
\boxed{
\text{RC–SSNC Unified Terminal-Capacity Milestone 中的 SSNC}
\quad\xrightarrow{\text{只替换 core terminal}}\quad
\text{SSUHPC}
}
\]

具体只允许：

\[
\boxed{
\mathcal C_{c}^{NC}(N_x,M_x;N_y,M_y)
\longrightarrow
\mathcal C_{c}^{UHPC}(N_x,M_x;N_y,M_y)
}
\]

即把普通混凝土核心的**横向与纵向 N-M terminal relations**替换为 UHPC 的横向与纵向 N-M terminal relations。

除此以外，SSNC milestone 中的结构层、钢壳层、web 层、common terminal architecture、求根纪律全部原样保留。

---

# 1. 严格继承 SSNC milestone，不重新建立

以下全部直接继承，不得从历史 UHPC 对话中覆盖：

```text
STRUCTURAL_FRONT = MARGUERRE_AIRY / GALERKIN
AIRY_STIFFNESS = INITIAL FULL-COMPOSITE ABD
CONTROL_HALFWAVE_SELECTION = SAME AS SSNC MILESTONE
COMMON_TERMINAL_STRAIN/RESULTANT ARCHITECTURE = RETAIN
STEEL_FACE_LOCAL_OPERATOR = R02
STEEL_FACE_TERMINAL_CAP = R04
LONGITUDINAL_WEB = RETAIN
STEEL_FACE_OFFSET_STIFFNESS = RETAIN ONCE ONLY
R03_AS_Pu_GATE = NO
CURRENT_MATERIAL_TANGENT_INTO_AIRY = NO
FORMAL_SPATIAL_QUADRATURE = 0
MATERIAL_POINTS = 0
EXPERIMENT/FEM/COMPARATOR_IN_ROOT_SELECTION = 0
EFFECTIVE_WIDTH/AREA_PRODUCTION = PROHIBITED
```

因此历史 UHPC 对话中出现过的：

- 旧 1600×1600 结构域；
- 旧 m*；
- 32 mm / 37 mm web rebase；
- 旧 R-O / Yun-only steel terminal；
- 旧 T120/T360/BH Pu；
- Zhang/Liu/FHWA/R08 等后续分支；

都**不能因为“UHPC 替换”而反向覆盖当前 SSNC milestone**。

历史对话在本分支只用于恢复 UHPC 材料单元及其 N-M 生成关系。

---

# 2. 结构前端保持 SSNC milestone

结构需求仍由 milestone 的 full-composite initial elastic front 生成：

\[
P(q),\quad N_x^d(q,s),\quad N_y^d(q,s),\quad M_x^d(q,s),\quad M_y^d(q,s)
\]

以及必要 shear resultant demand。

材料非线性不回灌 Airy compatibility。

把 NC 换成 UHPC 后，唯一允许对初始刚度发生的变化是：

> 在**同一套** full-composite ABD 公式中，把 core 的初始弹性常数从 NC 参数换成 UHPC 参数。

这叫**同一结构公式的材料参数代入**，不叫建立新的结构前端。

外钢面偏心项仍只计一次：

\[
D_s^0=2Q_s\left(t_sz_f^2+\frac{t_s^3}{12}\right).
\]

禁止再次加入 offset stiffness。

---

# 3. 钢壳与 web 完全不动

SSUHPC 的钢相继续严格采用 milestone：

```text
upper external face -> R02 -> R04
lower external face -> R02 -> R04
longitudinal web -> milestone web law
```

R02 接收 common terminal face strain，输出有限 PBL/Yun mean-face trial state；R04 对其施加 path-free ideal-EP Mises cap。

SSUHPC 不允许因为历史 UHPC 文件曾经使用 R-O 或早期 Yun scalar cap，就把当前 R02/R04 撤回。

---

# 4. 唯一替换模块：NC core N-M -> UHPC core N-M

## 4.1 共同截面运动学

在 terminal section，沿厚度坐标 z：

\[
\varepsilon_x(z)=\varepsilon_x^0+z\kappa_x,
\qquad
\varepsilon_y(z)=\varepsilon_y^0+z\kappa_y.
\]

这一应变场来自 milestone 的 common terminal strain / section kinematics，不由 UHPC 材料重新定义。

## 4.2 UHPC 材料单元

上传的历史 UHPC 记录只恢复材料单元。当前可确认的早期 UHPC 参数记忆为：

\[
f_c=141.1\ \mathrm{MPa},
\qquad
E_c=43.4\ \mathrm{GPa},
\qquad
\varepsilon_{c0}=0.0035,
\qquad
\nu_c=0.20.
\]

Hu-source compression backbone：

\[
\sigma_c=
\begin{cases}
 f_c\dfrac{n\xi-\xi^2}{1+(n-2)\xi}, & \xi\le1,\\[8pt]
 f_c\dfrac{\xi}{2(\xi-1)^2+\xi}, & \xi>1,
\end{cases}
\]

其中

\[
\xi=\frac{|\varepsilon|}{\varepsilon_{c0}},
\qquad
n=\frac{E_c\varepsilon_{c0}}{f_c}.
\]

若某一方向截面出现拉区，则只能调用历史记录中已存在的 Hu-source UHPC tensile branch；不得用普通混凝土拉伸关系替代，也不得自行发明新的 TC/TT 多轴 law。

历史记录中的 tensile branch 形式为

\[
\sigma_t=f_{ct}e^{1/m}\,\xi_t\exp\!\left(-\frac{\xi_t^m}{m}\right),
\]

\[
K=\left(\frac{l_f}{d_f}\right)V_f,
\qquad
m=0.85-0.47K+0.12K^2,
\]

其具体 `f_ct, xi_t, lf, df, Vf` 必须来自相应 UHPC 来源/试件输入，不能为完成求解而猜值。

---

# 5. UHPC 横向与纵向 N-M relation

核心替换的数学对象不是新的二维材料点状态机，而是两个 section-resultant maps。

对 `i in {x,y}`：

\[
\boxed{
N_i^{UHPC}(\varepsilon_i^0,\kappa_i)
=(1-\rho_w)\int_{-t_c/2}^{t_c/2}
\sigma_U[\varepsilon_i^0+z\kappa_i]\,dz
}
\]

\[
\boxed{
M_i^{UHPC}(\varepsilon_i^0,\kappa_i)
=(1-\rho_w)\int_{-t_c/2}^{t_c/2}
z\,\sigma_U[\varepsilon_i^0+z\kappa_i]\,dz
}
\]

从而分别定义：

\[
\boxed{\mathcal C_x^{UHPC}: (\varepsilon_x^0,\kappa_x)\mapsto(N_x^{UHPC},M_x^{UHPC})}
\]

和

\[
\boxed{\mathcal C_y^{UHPC}: (\varepsilon_y^0,\kappa_y)\mapsto(N_y^{UHPC},M_y^{UHPC})}.
\]

UHPC 为同一各向同性材料单元，所以 x/y 使用同一材料曲线；方向差异来自结构 demand、曲率、web/steel phase 组成，而不是给 UHPC 再造两套材料本构。

这就是本轮“普通混凝土纵横向 N-M -> UHPC 纵横向 N-M”的完整替换定义。

不额外叠加：

```text
CC/TC/TT runtime state machine
Liu sequential gate
DP/W-W production surface
FHWA design compression replacement
R08 rectangular block
material-point history
```

---

# 6. 总截面 terminal resultants

SSNC milestone 的 phase assembly 原样保留，只把 core 项改名/改值。

\[
\boxed{
N_x^{sec}
=N_x^{UHPC}+N_{x,+}^{face}+N_{x,-}^{face}+N_x^{web}
}
\]

\[
\boxed{
M_x^{sec}
=M_x^{UHPC}+M_{x,+}^{face}+M_{x,-}^{face}+M_x^{web}
}
\]

\[
\boxed{
N_y^{sec}
=N_y^{UHPC}+N_y^{web}+N_{y,+}^{face}+N_{y,-}^{face}
}
\]

\[
\boxed{
M_y^{sec}
=M_y^{UHPC}+M_y^{web}+M_{y,+}^{face}+M_{y,-}^{face}
}
\]

按 milestone 的纵向 web 定义，若 web 不承担 x-direction resultant，则

\[
N_x^{web}=M_x^{web}=0.
\]

这不是 UHPC 新假设，而是继承 steel-shell phase definition。

---

# 7. 最终求解系统保持 milestone identity

对一般二维 terminal：

\[
\boxed{
N_x^{sec}=N_x^d,
\qquad
M_x^{sec}=M_x^d,
\qquad
N_y^{sec}=N_y^d,
\qquad
M_y^{sec}=M_y^d
}
\]

若 shear demand 非零，则按 milestone 同步加入对应 terminal resultant/capacity condition。

对特定 endpoint/active-set，按 milestone 自身的退化条件减少方程，不能人为先删维。

特别地，Z6 R05 的 SSNC 已证明在其 governing symmetric endpoint：

\[
s=0,\qquad M_y^d=0,
\]

并存在 common strain degeneration。若未来某个 SSUHPC 算例也由自身理论解证明落在同一类 endpoint，才可采用相应退化；不得把 Z6 的 endpoint 预设给所有 UHPC 板。

---

# 8. 历史 UHPC 对话的允许用途与禁止用途

## 允许

只用于恢复：

- UHPC `fc, Ec, epsc0, nu` 材料单位；
- Hu-source compression backbone；
- Hu-source tension backbone 及其来源参数接口；
- 由材料曲线生成 section N-M 的解析/有限积分思想。

## 禁止

不得从历史 UHPC 对话带回：

- 旧结构域/旧半波；
- 旧 Airy 系数；
- 旧 web 几何假设；
- 旧钢面 R-O/Yun-only terminal；
- 旧 Pu 数值作为新理论目标；
- 后来为大宽厚比误差展开的任何修正链。

因此：

\[
\boxed{
\text{HISTORY ROLE = UHPC MATERIAL UNIT MEMORY ONLY}
}
\]

---

# 9. 当前理论身份

```text
ANCHOR = RC_SSNC_UNIFIED_TERMINAL_CAPACITY_MILESTONE_20260825
PARENT_THEORY = SSNC_FROM_MILESTONE
STRUCTURAL_ARCHITECTURE_CHANGED = NO
STEEL_ARCHITECTURE_CHANGED = NO
WEB_ARCHITECTURE_CHANGED = NO
ROOT_SELECTION_DISCIPLINE_CHANGED = NO
CORE_TERMINAL_CHANGED = YES
CORE_CHANGE = NC longitudinal/transverse N-M -> UHPC longitudinal/transverse N-M
UHPC_HISTORY_USED_FOR = MATERIAL_UNIT_ONLY
LATER_UHPC_REPAIR_CHAIN = NOT_IMPORTED
NUMERICAL_RECALCULATION = NOT_YET_EXECUTED
```

这才是当前钢壳 UHPC 的唯一正式理论起点。
