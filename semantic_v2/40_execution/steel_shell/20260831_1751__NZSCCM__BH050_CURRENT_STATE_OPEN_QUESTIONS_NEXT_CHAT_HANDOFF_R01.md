# NZ-SCCM — BH050 当前进度、核心疑问与下一聊天接续手册 R01

**Time:** 2026-08-31 17:51 +08:00  
**Branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Pre-handoff branch HEAD:** `57f55afc3e03919f06e4cf6f813a7df58a9f40a4`  
**Production main:** `c8927c79298e78deb2450efc51d7674060988eec` — unchanged  
**Status:** `CURRENT STATE / OPEN QUESTIONS / NEXT-CHAT HANDOFF ONLY`  

> 本文件用于在更换聊天前冻结当前真实进度、已纠正的变量身份、已完成诊断、尚未证明的假设和下一步唯一可执行问题。它不是新的 production theory，不改变 `main`，不把尚未完成的 deformation-compatible current-section solve 或 structural tangent solve 伪装成已完成结果。

---

# 0. 本轮真正要解决的物理问题

用户将问题重新压缩到了最本质的受力层：

> BH050 为什么会出现明显异常的“偏压”/上下钢面不对称？外部是轴心受压，那么内部偏压从哪里来？其本质是什么？

当前应避免继续只讨论 `J4 fold`、某个局部材料点、某个后端系数等下游现象。真正要区分的是：

1. **物理允许的变形诱导压弯**：轴压 + 初始缺陷 + 面外挠曲自然产生 `N+M`；
2. **理论异常的内部偏压/中性轴迁移**：current terminal section 中 UHPC、上钢面、下钢面、web 的轴力和弯矩分配明显偏离 FEM，同一总 `N,M` 被一种很不自然的内部应力梯度实现。

本轮用户关注的是第 2 项的根因。

---

# 1. 最新且必须保留的变量身份纠正

来源：

- `semantic_v2/40_execution/steel_shell/20260831__NZSCCM__CURVATURE_CAPACITY_COORDINATE_CORRECTION_AND_BH050_RECALC_R02.md`

已经冻结：

```text
q = sole global structural postbuckling amplitude
kappa_geo(q) = actual physical structural curvature from w_d
Bx_cap, By_cap = terminal N-M capacity-surface affine coordinates
Bx_cap, By_cap != actual physical global curvature observables
```

因此：

\[
w_d=bq\sin(\alpha x)\sin(\beta y),
\]

在 BH 控制 antinode 且 `ell=b`：

\[
\boxed{\Delta\kappa_x=\Delta\kappa_y=\pi^2q/b}.
\]

同时冻结 Airy bending demand 本身已经包含：

\[
\boxed{M_y^d=D_\mu\Delta\kappa_x+D_y\Delta\kappa_y}.
\]

所以后续 **禁止** 再把历史 `(Bx_cap,By_cap)` 与 `kappa_geo` 直接比较并据此宣称“物理曲率错了”，也禁止简单强制：

\[
B_x^{cap}=\kappa_x^{geo},\qquad B_y^{cap}=\kappa_y^{geo}.
\]

那会构成一套新的 deformation-compatible theory，必须重新推导 equilibrium，不能作为旧 R4 的变量替换。

---

# 2. BH050 source-audited frozen input

```text
b = 2500 mm
a_phys = 5000 mm
tc = 42 mm
ts = 4 mm
zf = 23 mm
9 longitudinal webs
net web height = 37 mm
Aw = 1332 mm2
rho_w = 0.0126857142857143
q0 = 0.0025
s = 1

Es = 206000 MPa
nu_s = 0.30
fy = 355 MPa

Ec = 43400 MPa
nu_c = 0.20
fc = 141.1 MPa
eps_c0 = 0.0035
fct = 4.513133983249735 MPa
eps_t0 = 0.001
mt = 0.4418

R02 local cell:
Lx = 562.5 mm
Ly = 555.555555555556 mm
A0 = 0.3515625 mm
```

注意：`b=1600 mm` 属于 BH032，不是 BH050。

冻结 initial full-composite stiffness / Airy numbers（来自 source-audited R02）：

\[
D_x=1.236003299827839\times10^9\;Nmm,
\]
\[
D_y=1.252137549427839\times10^9\;Nmm,
\]
\[
D_\mu=3.432434438483517\times10^8\;Nmm,
\]
\[
D_{66}=4.463799279897436\times10^8\;Nmm,
\]
\[
H=1.236003299827839\times10^9\;Nmm.
\]

Mode scan：`m*=2`, `ell=2500 mm`, `alpha=beta=pi/2500`.

\[
P_{cr}=19.5818772367311\;MN,
\]
\[
G=4.400171479082513\times10^6\;N/mm,
\]
\[
C=10841.3718065234\;MN,
\]
\[
J_x=6.234616244717026\times10^6\;N,
\qquad
J_y=6.298311709061200\times10^6\;N.
\]

---

# 3. 现有合法结果：Airy–N/M capacity-contact terminal

当前 source-audited terminal：

\[
q_{cap}=0.004772819645833164,
\]

\[
\kappa_{geo}=\pi^2q/b
=1.88423367128\times10^{-5}\;mm^{-1},
\]

\[
Q_q=q(q+2q_0)=4.664390560081682\times10^{-5},
\]

\[
\boxed{P_u^{capacity-contact}=13.3563763545430\;MN}.
\]

Demand resultants：

\[
N_x^d=+199.305955403735\;N/mm,
\]
\[
N_y^d=-5137.30935871948\;N/mm,
\]
\[
M_x^d=29756.6988970160\;N,
\qquad
M_y^d=30060.7058605883\;N.
\]

这个结果目前只允许称为：

```text
source-audited Airy–N/M capacity-contact prediction
```

不得称为已证明的 deformation-compatible structural Pu。

---

# 4. 同一 terminal 的完整局部截面力账本

UHPC：

\[
N_y^U=-3775.20864050157\;N/mm,
\qquad
M_y^U=16306.0755102416\;N.
\]

Web/PBL：

\[
N_y^w=-170.904638861559\;N/mm,
\qquad
M_y^w=293.915178045378\;N.
\]

Upper steel face：

\[
N_{y,+}^{s}=-302.97379680\;N/mm.
\]

Lower R06 steel face：

\[
N_{y,-}^{s}=-888.22228255\;N/mm.
\]

两钢面：

\[
N_y^{faces}=-1191.19607935637\;N/mm.
\]

严格轴力 closure：

\[
-3775.20864050157-1191.19607935637-170.904638861559
=-5137.30935871949\;N/mm.
\]

局部 terminal share：

```text
UHPC       = 73.4861 %
steel faces= 23.1872 %
web/PBL    = 3.3267 %
upper face = 5.8975 % of section total
lower face = 17.2896 % of section total
```

这些是 **terminal N-M capacity-contact section shares**，不是已证明的实际 deformation-path global constituent shares。

---

# 5. 用户提出“本质上是不是产生了偏压？”后的力学拆解

总截面当前 terminal：

\[
N_y=-5137.3094\;N/mm,
\qquad
M_y=30060.7059\;N.
\]

因此等效总偏心距：

\[
\boxed{e_{total}=M_y/|N_y|\approx5.8515\;mm}.
\]

总 `N+M` 本身并不反常；轴心加载板在初始缺陷和面外挠曲后自然可出现 deformation-induced eccentric compression / `P-Delta` 型压弯。

**真正异常的是这个总偏心如何在 UHPC、钢面和 web 内部实现。**

由 terminal ledger：

\[
e_U=|M_y^U/N_y^U|\approx4.32\;mm,
\]

\[
e_w=|M_y^w/N_y^w|\approx1.72\;mm.
\]

钢面承担的剩余 longitudinal moment：

\[
M_y^{faces}=M_y^d-M_y^U-M_y^w
\approx13460.7\;N,
\]

故：

\[
\boxed{e_{faces}=|M_y^{faces}/N_y^{faces}|\approx11.30\;mm}.
\]

也就是说：

```text
steel faces carry ~23.2% of longitudinal axial force
but must carry ~44.8% of longitudinal moment
```

于是两钢面被迫形成很强的内部力偶。

当前理论钢面平均应力：

```text
upper: -75.743 MPa
lower: -222.056 MPa
```

其 mean / antisymmetric decomposition：

\[
\bar\sigma_s^{th}\approx-148.90\;MPa,
\]

\[
\sigma_{b,s}^{th}\approx+73.16\;MPa.
\]

当前 FEM equal-contract post-check（只作事后诊断，不参与 root selection / calibration）：

```text
upper steel ~ -256.87 MPa
lower steel ~ -226.94 MPa
```

对应：

\[
\bar\sigma_s^{FE}\approx-241.91\;MPa,
\]

\[
\sigma_{b,s}^{FE}\approx-14.97\;MPa.
\]

所以 BH050 的差异不是简单的“upper 少压了约 181 MPa”，而是同时存在：

1. **steel faces 整体平均压缩明显不足**；
2. **理论上下钢面反对称弯曲分量过大，且与 FEM 方向不一致**。

这使当前最有力的物理描述变成：

\[
\boxed{\text{theory places the internal neutral axis / axial-force line incorrectly.}}
\]

即：理论不仅把轴力过度转给 UHPC，还用一个异常强的上下钢面力偶去满足剩余 moment demand。

---

# 6. 已经排除/显著降级的直接嫌疑

以下不应再作为下一聊天的第一调查方向：

- `web` 为 primary cause；
- lower R06 alone；
- upper R02 constitutive tangent 本身导致卸载；
- local `kx,ky` 波数错误；
- `K_A` 错误；
- global integer mode `m*` 选择错误；
- 简单认为 `q -> kappa_geo` 物理曲率链错误；
- 把 `Bx_cap,By_cap` 当物理曲率；
- 简单强制 `Bcap=kappa_geo`；
- 旧 `17.984 MN` hybrid；
- 仅凭 frozen UHPC `-0.0035` contact 当作 BH050 真实 ultimate mechanism；
- 用 FEM/test 调整 terminal strain、选 root、反标参数；
- effective width / empirical b/t repair。

Upper R02 在 BH050 terminal 的 consistent tangent 仍接近 elastic，说明它不会无缘无故把 upper longitudinal stress从更压缩方向“主动卸掉”。

---

# 7. 当前两个最重要、但尚未证明的根因假设

## H1 — force-first `N-M` bridge 导致 neutral-axis / internal-eccentricity misplacement

现有架构本质是：

```text
q
 -> Airy structural demand D^A(q) = [Nx,Ny,Mx,My]
 -> current nonlinear section/capacity map searches a state that matches these resultants
```

而不是先强制 actual deformation state：

\[
\varepsilon_i(z)=\varepsilon_i^0+\kappa_i^{geo}(q)z
\]

再由 current UHPC + steel R02/R06 + web 自然积分得到 `N,M`。

因此存在一个核心疑问：

> 在 BH050 给定真实 `kappa_geo(q)` 和总 `Nx,Ny` 时，current section 自己通过膜应变平衡所选择的 neutral axis / component force split，到底是否仍会给出当前 73.5/23.2/3.3 与 5.9/17.3 的强不对称？

如果不会，则当前 force-first `N,M` matching 在后端人为推动了中性轴/作用线，形成异常 internal eccentricity。

### H1 的唯一直接诊断

在固定 q 下：

\[
\boxed{\kappa_T=\kappa_T^{geo}(q),\qquad \kappa_L=\kappa_L^{geo}(q)}
\]

不再让 curvature/capacity coordinates 自由调整。

只求：

\[
\varepsilon_T^0,\qquad\varepsilon_L^0
\]

使：

\[
N_T^{cur}=N_T^A,
\qquad
N_L^{cur}=N_L^A.
\]

然后 **不强迫 moment matching**，直接读出：

\[
M_T^{dc},\quad M_L^{dc},
\]

以及：

```text
N_U, N_upper, N_lower, N_web
M_U, M_upper, M_lower, M_web
neutral-axis / zero-strain location
```

建议至少做两个 q 状态：

1. current J4/capacity-contact `q=0.004772819645833164`；
2. canonical FEM peak 仅作 post-check 时映回原 Airy curve 的 same-load coordinate：
   `q=0.004117589557476763`。

**注意：第二个 q 不得用于 root selection；只是检查当前理论在真实峰值附近的 deformation-compatible section response。**

当前尚未完成这个 exact registered arbitrary-state evaluator，所以不得伪造 `M_dc` 数值。

---

## H2 — terminal identity misidentification: section capacity fold 可能晚于 full-structure stability loss

当前 R4：

\[
R_4(x,q)=S^{cap}(x)-D^A(q)=0.
\]

因此：

\[
J_4=\partial R_4/\partial x=\partial S^{cap}/\partial x.
\]

所以：

\[
\boxed{\det J_4=0}
\]

严格身份是 **section capacity-resultant map singularity/fold**。

它并没有被证明恒等于：

\[
\boxed{\det K_T^{structure}=0}
\]

或 first full-structure load peak。

这点与 Nguyen 的结构稳定理论有明确区别：Nguyen 用整个结构的 current tangential stiffness matrix 判断 singularity，而不是 section N-M capacity coordinate Jacobian。

当前预审已经得到：

```text
J4 terminal q = 0.004772819645833164
J4 terminal P = 13.3563763545430 MN
canonical FEM peak (post-check only) = 12.591227 MN
same original Airy P(q) inverse coordinate = 0.004117589557476763
q_same-load / q_J4 = 0.86271635
```

所以 FEM 峰值在当前 Airy q-coordinate 上比 J4 fold 早约 13.7%，载荷低约 0.765 MN（约 J4 prediction 的 5.73%）。

这支持、但尚未证明：

> high-B/H BH050 可能先发生整板 current tangent/global-local stability loss，而当前 theory 继续走到更晚的 section capacity fold；terminal 73/23/3 load share 可能是“终点取晚了”的症状。

### H2 的直接诊断

必须分开计算：

\[
g_{cap}(q)=\sigma_{min}[J_4(q)]
\]

和真正物理的：

\[
g_{str}(q)=\phi^T K_T^{structure}(q)\phi
\]

或等价二阶虚功稳定指标。

`K_T^{structure}` 必须由 **physical current state**、current material tangent、current membrane/geometric stiffness、同一真实结构模态构成。

严禁把 `J4` 的 Schur complement 改名后直接当作 physical bending tangent，因为最新 R02 已经确认 `Bcap` 不是物理曲率；对 capacity coordinate 任意重标度会改变这种“刚度”，故其不能是客观结构刚度。

H2 判据：

```text
if g_str(q_s)=0 with q_s<q_J4 and g_cap(q_s)>0:
    terminal-gate misidentification established
elif g_str reaches zero essentially at J4:
    J4 may be a useful numerical proxy but needs corrected physical interpretation
elif g_str remains positive through J4:
    reject H2 and return to force-first/current-feedback/GL issues
```

当前尚未完成 arbitrary-q physical current tangent evaluator，所以不得报告虚构的 `P_s=12.xx MN`。

---

# 8. H1 与 H2 的关系：不要混成一个问题

当前最重要的逻辑区别：

- **H1 回答**：为什么同一 `N,M` terminal state 会出现异常 UHPC/steel load redistribution 和强 internal eccentricity？
- **H2 回答**：为什么 theory 会走到这个 terminal state；这个 state 是否本来已经晚于真实 structural ultimate？

两者可能同时成立。

可能情形 A：

```text
physical structural instability occurs earlier (H2)
=> current 13.356-MN section state is never physically reached
=> extreme 73/23/3 redistribution is mainly a late-state symptom
```

可能情形 B：

```text
even at an earlier q, fixed-kappa current section already disagrees strongly with force-first N-M state (H1)
=> force/moment bridge itself is an upstream incompatibility
=> it may also contaminate any later structural tangent construction
```

所以不要再用单一一句“J4 太晚”或“Airy moment 太大”覆盖两种机制。

---

# 9. 当前最建议的下一聊天执行顺序

## NEXT-1 — 优先执行 fixed-kappa neutral-axis diagnostic（直接回答用户“偏压从哪里来”）

目标不是求新 Pu，而是恢复/组装一个 provenance-complete arbitrary-state current-section evaluator，并在固定 physical `kappa_geo(q)` 下只解两个 membrane strains。

需要的同状态 operators：

- UHPC current section primitive；
- upper registered R02 current operator；
- lower R02→R06 active operator；
- longitudinal web exact operator；
- actual R02 cell registration / finite harmonic coefficients；
- no spatial Gauss/Simpson/material-point grid。

必须输出：

```text
q
kappa_geo_x, kappa_geo_y
solved eps0_x, eps0_y
neutral-axis / zero-strain locations
Nx component ledger and closure
Mx/My component ledger
M_dc - M_A mismatch
upper/lower steel mean stress split
R02/R06 active-state identities
```

PASS/FAIL 不按 FEM 判；FEM 只在理论结果冻结后作 post-check。

## NEXT-2 — 再执行 physical structural tangent two-gate audit

只有在 current physical section operator 可在 arbitrary q 返回一致 tangent 后，才构造：

```text
physical current section tangent
+ plate/global mode work
+ current geometric stiffness
=> K_T^structure / delta^2 Pi
```

然后与 `g_cap(q)` 独立比较。

---

# 10. 已完成但必须避免误用的诊断

## 10.1 R02/GL black-box dissection

已恢复并解析展开：

\[
\phi=(1-\cos k_x\xi)(1-\cos k_y\eta),
\]

\[
c_x=3k_x^2/8,\qquad c_y=3k_y^2/8,
\]

LL Airy compatibility 的 7 个 fixed harmonics，以及 `K_A` finite sum；GL source 和 `qU` 项也已明确为有限解析 harmonic algebra。

BH050 `K_A` 与独立 derivation 一致，当前不是 primary suspect。

## 10.2 qU

`qU` 在 BH050 quantity-level 并非明显可忽略，但 exact resultant effect 依赖 actual cell registration。它仍是 open contributor，不应越过 H1/H2 成为当前第一根因。

## 10.3 Airy scalar P(q)

现有 frozen Airy scalar branch：

\[
P(q)=P_{cr}\frac{q}{q+q_0}+Cq(q+2q_0)
\]

在 `q>=0` 上：

\[
\frac{dP}{dq}>0.
\]

因此这条 frozen scalar `P(q)` 本身没有普通 scalar load fold。不能把 `dP/dq=0` 当作当前 missing ultimate condition。

---

# 11. 当前严格禁令 / governance

下一聊天必须继承：

```text
PRODUCTION main change = NO unless explicitly promoted later
FEM/test in root selection = 0
load calibration = 0
effective width / empirical b/t fix = 0
formal spatial Gauss/Simpson/adaptive quadrature = 0
material-point grid = 0
Bcap as physical curvature = PROHIBITED
simple Bcap=kappa_geo substitution = PROHIBITED
old 17.984-MN hybrid = INVALID
fake new Pu before same-state force ledger + closure = PROHIBITED
J4 Schur complement as physical structural bending tangent = PROHIBITED
```

如果新 diagnostic 无法从现有 frozen operators 完整闭合，必须明确指出缺失的具体 source/evaluator，而不是换一套理论或借 FEM 补数。

---

# 12. 关键 continuity files / commits

本轮接续时优先读取：

1. `semantic_v2/40_execution/steel_shell/20260831__NZSCCM__CURVATURE_CAPACITY_COORDINATE_CORRECTION_AND_BH050_RECALC_R02.md`
   - correct q/kappa/Bcap identity
   - source-audited BH050 numbers
   - terminal capacity-contact ledger

2. `semantic_v2/40_execution/steel_shell/20260831__NZSCCM__BH050_TERMINAL_IDENTITY_TWO_GATE_PREFLIGHT_R01.md`
   - commit before this handoff: `57f55afc3e03919f06e4cf6f813a7df58a9f40a4`
   - J4 vs structural-tangent two-gate preflight

3. `semantic_v2/40_execution/steel_shell/20260825_1622__NZSCCM__STEEL_SHELL_COMMON_R06_SSUHPC_7CASE_BH050_FULL_EXECUTION_R01.md`
   - complete BH050 old force-first R06 execution
   - upper/lower steel terminal details

4. `semantic_v2/20_theory/20260825_1530__NZSCCM__STEEL_SHELL_COMMON_R06_LOCAL_YIELD_RESULTANT_GATE_V1.md`
   - R06 exact branch identity and path-free radial local-yield projection

5. `semantic_v2/40_execution/steel_shell/20260830__NZSCCM__BH032_BH050_DISCRIMINATING_AUDIT_EXECUTION_R01.md`
   - BH032 vs BH050 force redistribution diagnosis
   - upper-face mismatch / web rejection / R02 tangent audit / qU diagnostic

6. `semantic_v2/90_history/20260830__NZSCCM__RECENT_TWO_CHATS_FULL_PROCESS_BACKUP_R01.md`
   - recent conversation backup and explicit R02/GL derivation continuity

Production main remains:

`c8927c79298e78deb2450efc51d7674060988eec`

Diagnostic pre-handoff HEAD:

`57f55afc3e03919f06e4cf6f813a7df58a9f40a4`

---

# 13. 下一聊天的一句话恢复口令

> **不要重开旧路线。先读 20260831_1751 handoff、20260831 curvature/Bcap R02 和 terminal-identity two-gate preflight。当前核心不是继续猜 J4 或本构参数，而是先回答“BH050 的异常偏压/中性轴迁移从哪里来”：执行 fixed-physical-kappa + membrane-force equilibrium 的 current-section neutral-axis diagnostic；随后才比较 physical structural tangent gate 与 J4 section-capacity fold。**

---

# 14. 当前结论等级

```text
PROVEN:
- q -> kappa_geo physical curvature identity is valid
- Bcap is not physical curvature
- current BH050 capacity-contact state closes N/M resultants internally
- upper R02 itself is not an obvious unloading operator
- BH050 terminal force split is strongly steel-to-UHPC shifted relative to FEM post-check
- J4 is a section capacity/resultant-map Jacobian by construction
- frozen Airy scalar P(q) has no q>=0 scalar fold

STRONGLY MOTIVATED BUT NOT PROVEN:
- force-first N-M bridge misplaces neutral axis / internal eccentricity (H1)
- full-structure tangent stability loss occurs before J4 section fold (H2)

NOT YET EXECUTED:
- exact fixed-kappa arbitrary-state current-section solve
- exact arbitrary-q physical structural tangent / second-variation gate
- new deformation-compatible Pu
```

**End of handoff.**