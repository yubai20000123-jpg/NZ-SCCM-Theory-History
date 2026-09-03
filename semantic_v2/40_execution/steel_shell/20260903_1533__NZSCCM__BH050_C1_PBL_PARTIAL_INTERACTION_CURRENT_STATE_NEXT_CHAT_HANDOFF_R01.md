# NZ-SCCM / BH050 — C1-PBL 纵向部分组合当前状态与下一聊天交接 R01

- 日期：2026-09-03 15:33 +08:00
- 仓库：`yubai20000123-jpg/NZ-SCCM-Theory-History`
- 分支：`diagnostic/bh032-bh050-mode-projection-20260827`
- 文件性质：**diagnostic / theory-development next-chat handoff，非 production 冻结稿**
- 写入前 branch head：`b2f2f8437f46dd51b159cac16f75abf19325214b`
- production/main：**不修改**

---

## 0. 本交接文件的作用

本文件把 2026-09-03 11:32 的 C1-PBL 力流备份之后继续完成的“纵向部分组合 / PBL slip-force-transfer”工作固定下来，供下一聊天直接恢复。

**不要从旧的 force-share 假设重新开始。** 当前已经完成了截面设计基线、连续全长度 partial-interaction 控制方程、`C_P` 参数扫参与 Schur 凝聚结构的理论总账。下一步应直接把纵向 partial interaction 插入 C1 current operator 的 local amplitude stationarity，而不是继续把 `C_P` 当成 UHPC 受力比例旋钮。

---

## 1. 当前应优先读取的文件链

按以下顺序恢复，不要只读旧 11:32 backup：

1. `20260903_1132__NZSCCM__BH050_C1_PBL_FORCE_FLOW_PHYSICS_AND_CURRENT_DIAGNOSTIC_BACKUP_R01.md`
   - 固定 C1-PBL、bay independent amplitude、R14 global N-M balance、15.36 MN 仅 provisional diagnostic 等基础状态。
2. `20260903__NZSCCM__BH050_C_PBL_PARTIAL_INTERACTION_TECHNICAL_LEDGER_R01.md`
   - 纵向 slip / partial interaction 的第一版技术账本。
3. `20260903__NZSCCM__BH050_C_PBL_EXACT_KERNEL_R01.py`
   - R01 exact-kernel implementation；代码不拥有独立理论身份。
4. **`20260903__NZSCCM__BH050_C_PBL_FULL_LENGTH_FORCE_FLOW_TECHNICAL_LEDGER_R02.md`**
   - 当前纵向 partial-interaction **最高优先级理论总账**。
   - 该文件明确规定：**理论文件 > 同名实现代码 > CSV 数值输出**。
5. `20260903__NZSCCM__BH050_C_PBL_FULL_LENGTH_FORCE_FLOW_KERNEL_R02.py`
   - R02 全长度闭式核实现。
6. `20260903__NZSCCM__BH050_C_PBL_FULL_LENGTH_CP_SWEEP_R02.csv`
   - 5000 mm 全长度 `C_P` continuation 数值审计。

---

## 2. 仍然冻结的理论边界

以下不重开：

- R14 global demand / backbone：
  \[
  Q=q(q+2q_0),
  \qquad
  P(q)=P_{cr}\frac{q}{q+q_0}+C_AQ.
  \]
- 四个 outer generalized N-M balance：
  \[
  R_1=N_x-N_x^A,
  \quad
  R_2=M_x-M_x^A,
  \quad
  R_3=N_y-N_y^A,
  \quad
  R_4=M_y-M_y^A.
  \]
- UHPC current material operator：FROZEN。
- web/PBL longitudinal steel operator：保留当前 R14 constituent identity，不用经验有效面积替代。
- steel material/yield：保留 R06 current material architecture、plane-stress/von-Mises、first-radial-yield、finite harmonic Airy 架构。
- C1-PBL：
  \[
  w_s(x_i,y)=W_c(x_i,y),
  \qquad
  w_{s,n}(x_i,y)=W_{c,n}(x_i,y),
  \]
  不恢复 `w_{s,nn}=W_{c,nn}`。
- 每个 bay 独立 local amplitude `A_b`，不得恢复 common local-wave amplitude / common phase。

继续禁止：effective width / effective area、FE back-calibration、stored Pu root selection、经验 reduction factor、用 force-share 百分比直接反标连接参数。

---

## 3. BH050 当前 source-locked 基本输入

R02 采用当前 R13/R14 同源输入：

- `B = 2500 mm`
- `L = 5000 mm`
- `t_c = 42 mm`
- `t_s = 4 mm`
- `A_w = 1332 mm²`
- `E_s = 206000 MPa`
- `nu_s = 0.30`
- `f_y = 355 MPa`
- `E_c = 43400 MPa`
- `nu_c = 0.20`
- `f_c = 141.1 MPa`
- `epsilon_c0 = 0.0035`
- `L_x = 562.5 mm`
- `L_y = 5000/9 = 555.555555556 mm`
- `A_{0,l} = 0.3515625 mm`

其中 `A_w=1332 mm²` 是 R14 的 longitudinal web/PBL steel area 输入，不得改写成经验 `A_eff`。

---

## 4. 已经完成的截面设计受力比例基线

用户上一节点问“这个比例是不是可以从截面设计中得到？”，该问题已经在 R02 中完成 source-consistent 计算。

在纯弹性、共同轴向应变的截面设计基线下，BH050 当前结果为：

\[
\boxed{\eta_c^{sec}=50.589\%}
\]

\[
\boxed{\eta_{steel\ faces}^{sec}=46.326\%}
\]

\[
\boxed{\eta_{web}^{sec}=3.085\%}
\]

即当前 C1 diagnostic 的 UHPC `54.23%` 并不是一个离截面设计初始分担非常远的状态。

R02 还用冻结 R02 amplitudes 做了 cross-ledger forcing-scale audit，得到：

\[
\boxed{\eta_c^{forcing\ audit}\approx53.912\%}
\]

与当前 C1 diagnostic：

\[
\eta_c^{C1,diag}\approx54.23\%
\]

处于同一量级。

因此当前最重要的解释变化是：**不能再从“54% 看起来偏低”直接推出必须靠一个 slip 参数把 UHPC 平均分担调到 60–65%。**

---

## 5. R02 最重要的新理论结论

定义 longitudinal relative slip：

\[
s(y)=u_s(y)-u_c(y),
\]

PBL distributed line coupling：

\[
t_P(y)=k_Ps(y),
\]

reference cell stiffness：

\[
\boxed{C_P=k_PL_r},
\qquad L_r=L_y=5000/9.
\]

最小两相能量：

\[
\Pi_{ax}
=
\frac12\int_0^L K_s(u_s'+g)^2dy
+
\frac12\int_0^L K_cu_c'^2dy
+
\frac12\int_0^L k_P(u_s-u_c)^2dy.
\]

变分得到：

\[
\boxed{N_s'=t_P=k_Ps},
\]

\[
\boxed{N_c'=-t_P=-k_Ps},
\]

因此：

\[
\boxed{(N_s+N_c)'=0}.
\]

### 5.1 已证明的关键边界

在：

- steel 与 UHPC 两条纵向路径的端部位移相同；
- local geometric shortening mismatch `g(y)` 已经固定；

的条件下，改变 `C_P`：

- 会改变 slip `s(y)`；
- 会改变 PBL transfer shear `t_P(y)`；
- 会改变 steel/core 局部轴力起伏；
- 会改变 local / condensed tangent；
- **但不能改变两相的全长度平均轴力分担。**

因此已经正式否定以下 shortcut：

\[
C_P \rightarrow \text{直接把 UHPC 平均受力比例从 54\% 调到 60\%-65\%}.
\]

`C_P` 不是这个意义上的 force-share knob。

---

## 6. 60–65% UHPC 分担假设的当前身份

此前曾做过纯 force-transfer continuation，用临时 `rho` 检查“如果 UHPC 分担真的升到 60–65%，承载力尺度可能如何变化”。该分析只能作为一阶 sensitivity / rejection screen，不能视为本构或连接定律。

R02 之后，应按以下方式解释：

- 60–65% 可以继续作为**待观察的 current-state 输出区间**；
- 不再作为 `C_P` 的目标值；
- 只有当 `C_P` 通过 C1 local amplitude、steel current tangent、UHPC nonlinear state 或端部力流条件改变 `g(y)` / current operator 后，平均 force share 才可能真正变化；
- 因此下一步必须把 partial interaction 放进 C1 local stationarity，而不是在最终 resultants 上手工重分配。

---

## 7. `C_P` 的 source status 与真实几何缺口

当前：

- `A_w = 1332 mm²`：LOCKED；
- `A_weld`：BH050 SOURCE-UNLOCKED；
- `A_emb`：BH050 SOURCE-UNLOCKED；
- PBL 孔径 `d_h`：SOURCE-UNLOCKED；
- 孔洞/混凝土榫轴向间距 `s_h`：SOURCE-UNLOCKED；
- reference cell 内参与传力的孔/榫数 `n_h`：SOURCE-UNLOCKED；
- PBL rib/web 实际厚度与具体传力细节：尚需 source lock。

所以当前 `C_P` 是：

\[
\boxed{\text{physically interpretable continuation parameter}}
\]

而不是已经由 BH050 构造细节确定的 source-grade design stiffness。

如果 sequential path 为：

`steel shell -> weld -> PBL rib -> embedded/dowel transfer -> UHPC`，

则一个 path 的串联柔度满足：

\[
\boxed{
\frac1{C_{P,path}}
=
\frac1{C_w}
+
\frac1{C_e}
}
\]

必要时再加入 rib compliance；多条独立 path 再并联求和。

不得把 `C_w+C_e` 无条件作为 `C_P`。

---

## 8. 已执行的 full-length `C_P` sweep 的身份

已对 BH050 `L=5000 mm` 全长度 harmonic partial-interaction kernel 做 continuation sweep。

同步数值文件：

`20260903__NZSCCM__BH050_C_PBL_FULL_LENGTH_CP_SWEEP_R02.csv`

其字段包括：

- `Lambda_cell`
- `Lambda_full`
- `C_P_N_per_mm`
- `eta`
- `slip_relief`
- `transfer_length_mm`
- `s_max_mm`
- `t_max_N_per_mm`
- `delta_Ns_amp_N`
- `delta_Ns_amp_per_width_N_per_mm`
- `eta_full_check`

代表性 continuation 点：

- `Lambda_cell=10` -> `eta=0.0595544`, transfer length `175.682 mm`；
- `Lambda_cell=20` -> `eta=0.1124141`, transfer length `124.226 mm`；
- `Lambda_cell=40` -> `eta=0.2021083`, transfer length `87.841 mm`；
- `Lambda_cell=80` -> `eta=0.3362564`, transfer length `62.113 mm`；
- `Lambda_cell=157.9136704` -> `eta=0.5`, transfer length `44.2097 mm`；
- `Lambda_cell=200` -> `eta=0.5587940`, transfer length `39.2837 mm`；
- `Lambda_cell=500` -> `eta=0.7599781`, transfer length `24.8452 mm`；
- `Lambda_cell=1000` -> `eta=0.8636222`, transfer length `17.5682 mm`。

这些结果只说明在固定 forcing `g(y)` 下 connector stiffness 如何改变 slip relief、transfer length、line shear 与 local force oscillation；**它们不是 `P_u(C_P)`，也不是平均 UHPC force-share 曲线。**

---

## 9. partial interaction 与 C1 真正耦合的位置

每个 bay 的 geometric mismatch 必须写成：

\[
\boxed{g_b=g_b(A_b,q,\mathbf x)}.
\]

于是：

\[
\Pi_{ax}
=
\Pi_{ax}(\mathbf x,\mathbf A,\mathbf s;C_P).
\]

local amplitude stationarity：

\[
\boxed{R_{A_b}=\frac{\partial\Pi}{\partial A_b}=0}.
\]

slip stationarity：

\[
\boxed{R_s=\frac{\partial\Pi}{\partial\mathbf s}=0}.
\]

`C_P` 只有通过：

\[
\frac{\partial R_A}{\partial s},
\qquad
\frac{\partial R_s}{\partial A},
\qquad
\frac{\partial R_s}{\partial\mathbf x}
\]

反馈到 `A_b` 与 outer state，才可能改变实际 terminal。

---

## 10. upper/lower/core 多路径必须保留

正式 C1-PBL 至少允许：

\[
s_+=u_+-u_c,
\qquad
s_-=u_--u_c.
\]

不能再用一个 aggregate steel path 隐藏上下钢面显著不对称。

可作解释性分解：

\[
u_a=\frac{u_++u_-}{2},
\qquad
\delta=\frac{u_+-u_-}{2},
\]

\[
g_a=\frac{g_++g_-}{2},
\qquad
g_d=\frac{g_+-g_-}{2}.
\]

其中 symmetric mode 控制 steel aggregate ↔ UHPC 纵向重分配，antisymmetric mode 控制 upper/lower steel face 的轴向不对称。

正式实现必须使用 current consistent tangent resultants，不能把 `K_s,K_c` 永久固定为初始 `EA`；web/PBL longitudinal operator 不能重复计入 connector stiffness。

---

## 11. exact Schur condensation 已固定

outer variables：

\[
\mathbf x=
[\varepsilon_x^0,\kappa_x,\varepsilon_y^0,\kappa_y]^T.
\]

内部变量：

- `A`：全部 C1 bay local amplitudes；
- `s`：全部 longitudinal partial-interaction internal coordinates。

完整 current Jacobian：

\[
\mathbf J=
\begin{bmatrix}
\mathbf J_{xx}&\mathbf J_{xA}&\mathbf J_{xs}\\
\mathbf J_{Ax}&\mathbf J_{AA}&\mathbf J_{As}\\
\mathbf J_{sx}&\mathbf J_{sA}&\mathbf J_{ss}
\end{bmatrix}.
\]

内部块：

\[
\mathbf J_{ll}=
\begin{bmatrix}
\mathbf J_{AA}&\mathbf J_{As}\\
\mathbf J_{sA}&\mathbf J_{ss}
\end{bmatrix}.
\]

精确凝聚：

\[
\boxed{
\mathbf J_{4,cond}
=
\mathbf J_{xx}
-
\begin{bmatrix}\mathbf J_{xA}&\mathbf J_{xs}\end{bmatrix}
\mathbf J_{ll}^{-1}
\begin{bmatrix}\mathbf J_{Ax}\\\mathbf J_{sx}\end{bmatrix}
}.
\]

后续 structural fold 必须用 `J4_cond`，不能继续用未凝聚的旧 `J4`。

terminal 仍按当前 R14 rule：connected equilibrium branch 上 first material-domain event 与 first admissible condensed-J4 fold 谁先发生谁控制。

---

## 12. 当前已经完成 / 尚未完成

### 已完成

1. C1-PBL 力流物理边界固定；full-curvature equality 已降级。
2. 截面弹性设计 force-share baseline 已算出：UHPC 50.589% / steel faces 46.326% / web 3.085%。
3. frozen-amplitude forcing audit 得到 UHPC 53.912%，并与当前 C1 diagnostic 54.23% 对照。
4. `C_w,C_e,C_P` 的串并联身份、单位与几何 source boundary 已闭合。
5. `K_s,K_c,K_eq`、`s(y)`、`t_P(y)`、`Delta N_s/Delta N_c` 的全长度连续控制方程已闭合。
6. 证明固定 `g(y)` + common end displacement 时平均 force share 对 `C_P` 不敏感。
7. 完成 5000 mm full-length harmonic `C_P` sweep。
8. exact line integration identities 与最终 global Schur condensation 已给出。

### 尚未完成，因此绝对不能称为 `P_u(C_P)`

1. BH050 current C1 全部 `A_b(q,x,C_P)` 尚未 source-locked / synchronized 成同一个可执行 residual family；
2. BH050 exact `A_weld,A_emb,d_h,s_h,n_h` 尚未 source-lock，因此 `C_P` 还不是唯一物理设计值；
3. R06 steel current tangent 尚未与 C1 amplitude + slip stationarity 同源接入；
4. full multi-bay / upper-lower asymmetric internal block 尚未 exact compile / condense；
5. 尚未对任意 `C_P` 沿同一 connected branch 找 first admissible terminal。

因此：

\[
\boxed{\text{当前没有 source-grade }P_u(C_P).}
\]

---

## 13. 下一聊天唯一主任务

### NEXT-1：把 longitudinal partial interaction 插入 C1 current operator 本身

不是再做 `C_P -> force-share percentage` 扫描，而是执行：

\[
\boxed{
C_P
\rightarrow
\text{C1 bay amplitude stationarity}
\rightarrow
\bar g(A_b)
\rightarrow
\text{steel/core current resultants}
\rightarrow
J_{4,cond}
\rightarrow
q_*/P_*
}
\]

具体执行顺序：

1. 恢复 BH050 exact C1 multi-bay residual family，并保持每 bay 独立 `A_b`；
2. 把 upper/lower longitudinal internal coordinates `s_+,s_-` 放入同一 current energy/residual family；
3. 让 R06 steel current consistent tangent、C1 geometric shortening `g_b(A_b,q,x)`、UHPC current resultants 与 slip stationarity 同源；
4. 编译 `J_AA,J_As,J_ss` 及与 outer `x` 的所有 coupling blocks；
5. exact Schur condense 得到 `J4_cond`；
6. 仅在上述完成后，对 `C_P` 做 continuation；每个 `C_P` 都沿 connected equilibrium branch 找 first material-domain event / first admissible condensed fold；
7. 此时 UHPC/steel/web force share 只作为 state observable 输出，不作为 calibration target。

### NEXT-2：source-lock 真实 BH050 PBL connector geometry

为把 continuation `C_P` 最终变成 source-grade connector stiffness，需要继续从真实 BH050 构造资料锁定：

`A_weld,A_emb,d_h,s_h,n_h` 以及 rib/weld/embedded sequential transfer geometry。

该任务可与 NEXT-1 的 diagnostic continuation 并行，但在 source lock 完成前不得把任何某个 `C_P` 标成“设计真实值”。

---

## 14. 下一聊天恢复口令

建议新聊天直接输入：

> 读取 GitHub `diagnostic/bh032-bh050-mode-projection-20260827` 最新的 `20260903_1533__NZSCCM__BH050_C1_PBL_PARTIAL_INTERACTION_CURRENT_STATE_NEXT_CHAT_HANDOFF_R01.md`，按其中文件链恢复状态；不要重开 R14 global demand、UHPC material、PBL full-curvature equality、effective width 或 `C_P -> force-share` 旋钮路线。从 NEXT-1 开始，把 longitudinal partial interaction 正式插入 C1 bay amplitude stationarity 与 current operator，构造并凝聚 `J4_cond`，再进入 `P_u(C_P)` continuation。

---

## 15. 状态标签

- `R14_GLOBAL_DEMAND`: FROZEN
- `UHPC_CURRENT_OPERATOR`: FROZEN
- `WEB_LONGITUDINAL_OPERATOR`: PRESERVE / NO DOUBLE COUNT
- `STEEL_R06_CURRENT_ARCHITECTURE`: PRESERVE
- `C1_PBL_W_THETA_COMPATIBILITY`: PRIMARY
- `PBL_FULL_CURVATURE_EQUALITY`: DOWNGRADED / DO NOT REOPEN
- `BAY_INDEPENDENT_AMPLITUDE`: REQUIRED
- `BH050_SECTION_ELASTIC_SHARE`: UHPC 50.589% / STEEL FACES 46.326% / WEB 3.085%
- `FROZEN_AMPLITUDE_FORCE_SHARE_AUDIT`: UHPC 53.912%
- `C1_CURRENT_DIAGNOSTIC_SHARE`: UHPC ~54.23%
- `CP_DIRECT_FORCE_SHARE_KNOB`: REJECTED AT FIXED g / COMMON END DISPLACEMENT
- `CP_IDENTITY`: PHYSICALLY INTERPRETABLE CONTINUATION PARAMETER, NOT YET SOURCE-GRADE DESIGN VALUE
- `CP_FULL_LENGTH_SWEEP_R02`: COMPLETED
- `PU_CP`: NOT YET AVAILABLE
- `NEXT_PRIMARY`: COUPLE CP INTO C1 A_b + SLIP STATIONARITY, EXACT SCHUR CONDENSE J4
- `PRODUCTION`: UNCHANGED
