# NZ-SCCM — 钢壳-UHPC Hu早期替换理论 V1

**Time:** 2026-08-25 13:00 +08:00  
**Identity:** `CURRENT STEEL-SHELL FRONT + EARLY HU-UHPC REPLACEMENT / SSUHPC-HU-R01`  
**Status:** `THEORY ESTABLISHED / NUMERICAL RE-EXECUTION PENDING`  

---

# 0. 本轮边界

本轮从 2026-08-25 已闭合的钢壳-普通混凝土（SSNC）理论出发，只替换核心材料：

```text
普通混凝土 NC-M6
            ↓ replace only
UHPC — Hu Wenxu early uniaxial terminal
```

钢壳侧和结构侧不回退：

```text
initial full composite ABD                 RETAIN
Marguerre–Airy / Galerkin structural front RETAIN
R02 finite 2D PBL steel-face trial         RETAIN
R04 path-free ideal-EP radial Mises cap     RETAIN
longitudinal web steel                      RETAIN
steel-face parallel-axis stiffness          RETAIN ONCE ONLY
R03 current 6x6 tangent as Pu gate          NO
```

UHPC 只恢复 2026-08-21 最初成功的替换层：Hu 单轴压缩骨架 + 显式截面容量 + 有限二维预检查。后续因为大宽厚比问题引出的材料重构链本轮全部关闭。

明确不引入：

- 37 mm web 后续 rebase（历史回归若复现 2026-08-21，则仍用当时 32 mm 净高合同）；
- Zhang 2023 新压缩 backbone；
- Liu CC/TC/TT sequential gates / crack-history state machine；
- DP / Willam–Warnke 作为 production terminal；
- FHWA/Hiew 替换曲线；
- R08 rectangular UHPC resultant block；
- D15/Gxx 高阶材料曲面；
- effective width / b/t 经验修正；
- FEM/试验反标；
- current material tangent 回灌 Airy。

因此本文件的 UHPC 身份是：

```text
EARLY_HU_UHPC_LAYER = ACTIVE
LATER_UHPC_REPAIR_CHAIN = OFF
LARGE_B_OVER_T_DEFICIENCY = PRESERVED_AS_DIAGNOSTIC, NOT REPAIRED
```

---

# 1. 统一结构链

新的钢壳-UHPC 理论统一写成：

\[
\boxed{
\text{raw specimen}
\to
\text{initial full-composite ABD}
\to
\text{controlling complete halfwave}
\to
\text{Marguerre–Airy demand}
\to
\text{common section strain/plane-section bridge}
\to
\left\{
\begin{array}{l}
\text{Hu UHPC terminal}\cr
\text{R02 steel faces}\cr
\text{R04 steel cap}\cr
\text{web steel}
\end{array}
\right.
\to
\text{resultant contact}
\to P_u .
}
\]

治理保持：

```text
FORMAL_SPATIAL_QUADRATURE = 0
MATERIAL_POINTS = 0
LOAD_PATH_TRACKING = 0
EXPERIMENT_IN_ROOT_SELECTION = 0
FEM_IN_ROOT_SELECTION = 0
CURRENT_MATERIAL_TANGENT_INTO_AIRY = NO
```

厚度方向：UHPC 用解析原函数，web 用分段解析 clip 积分，钢面为有限层；因此正式 thickness quadrature 仍为 0。

---

# 2. 相组成与几何

对单位板宽，截面由四类相组成：

\[
\boxed{
\text{top steel face}
+
\text{UHPC core}
+
\text{longitudinal web steel}
+
\text{bottom steel face}.
}
\]

设：

- 核心厚度 `t_c`；
- 外钢面厚度 `t_s`；
- 钢面质心距中面
\[
z_f=\frac{t_c}{2}+\frac{t_s}{2};
\]
- 纵向 web 净钢面积 `A_{w,net}`；
- 当前板宽 `b`。

等效 web 体积分数：

\[
\boxed{\rho_w=\frac{A_{w,net}}{b t_c}.}
\]

UHPC 实体占比为 `1-rho_w`，web 钢占比为 `rho_w`。二者不得重复占据同一核心体积。

历史 2026-08-21 BH 回归合同若需要原样复现：

\[
A_{w,net}=9\times4\times32=1152\ \mathrm{mm^2},
\qquad
\rho_w=\frac{1152}{42B}.
\]

这只是历史 regression geometry；新试件必须从其自身几何直接生成 `A_w,net`，不得把 32 mm 当通用常数。

---

# 3. 材料输入

## 3.1 UHPC — 本轮早期冻结值

为复现最初成功替换层，采用当时 Hu-source 项目参数：

\[
\boxed{f_c=141.1\ \mathrm{MPa}},
\qquad
\boxed{E_c=43.4\ \mathrm{GPa}},
\]

\[
\boxed{\varepsilon_{c0}=0.0035},
\qquad
\boxed{\nu_c=0.20}.
\]

其中 `f_c` 为峰值抗压强度，`eps_c0` 为对应峰值压应变。

## 3.2 Steel

\[
E_s=206\ \mathrm{GPa},\qquad
\nu_s=0.30,\qquad
f_y=355\ \mathrm{MPa}.
\]

钢面 current terminal 使用当前 R02 + R04，而不是回退到 2026-08-21 的 R-O/Yun-only production law。Yun 来源身份已经被 R02 能量式吸收；R04 负责当前 ideal-EP Mises cap。

---

# 4. 初始 full-composite ABD

Airy 前端始终使用初始弹性 full-composite ABD。对任一均匀层 `p`：

\[
\mathbf Q_p=
\begin{bmatrix}
E_p/(1-\nu_p^2) & \nu_pE_p/(1-\nu_p^2) & 0\\
\nu_pE_p/(1-\nu_p^2) & E_p/(1-\nu_p^2) & 0\\
0&0&E_p/[2(1+\nu_p)]
\end{bmatrix}.
\]

\[
\mathbf A=\sum_p\int_{z_p^-}^{z_p^+}\mathbf Q_p\,dz,
\]

\[
\mathbf B=\sum_p\int_{z_p^-}^{z_p^+}z\mathbf Q_p\,dz,
\]

\[
\mathbf D=\sum_p\int_{z_p^-}^{z_p^+}z^2\mathbf Q_p\,dz.
\]

UHPC/core 项乘以 `(1-rho_w)`；纵向 web 只补入其真实纵向轴向刚度/相应 Zhou-source 初始方向刚度，不伪造横向连续钢层。

上下钢面对称时 `B=0`。

外钢面弯曲刚度必须完整保留：

\[
\boxed{
D_s^0
=2\mathbf Q_s\left(t_sz_f^2+\frac{t_s^3}{12}\right).
}
\]

2026-08-25 已证明该偏心项已在 current steel-shell front 中存在，所以：

```text
ADD_STEEL_OFFSET_AGAIN = PROHIBITED_DOUBLE_COUNTING
```

把普通混凝土换成 UHPC 后，只重算核心 `Ec,nu` 导致的 A/D/H 和由此得到的 `Pcr,C,G,J,Kx`；绝不在已有钢面偏心项之外再加一次 offset stiffness。

---

# 5. 控制完整半波与 Marguerre–Airy demand

候选模态：

\[
N_{cr,j}=\pi^2\left[
\frac{D_xa_{phys}^2}{j^2b^4}
+\frac{2H}{b^2}
+\frac{D_yj^2}{a_{phys}^2}
\right],
\qquad
P_{cr,j}=bN_{cr,j}.
\]

\[
\boxed{m_*=\arg\min_{j\ge1}P_{cr,j}},
\qquad
\boxed{\ell=a_{phys}/m_*}.
\]

只计算一个连续完整代表半波。

结构后屈曲荷载：

\[
\boxed{
P(q)=P_{cr}\frac{q}{q+q_0}+Cq(q+2q_0).
}
\]

轴向局部 resultant demand：

\[
\boxed{
n_y(s;q)=\frac{P(q)}{b}
+Gq(q+2q_0)(1-2s^2).
}
\]

弯矩 demand：

\[
\boxed{m_y(s;q)=J_yqs.}
\]

Airy 同时给出横向膜力 `n_x(s;q)`（或完整解析位置函数）。其来源保持 current full-2D Marguerre–Airy，不由 UHPC 非线性材料反向修改。

---

# 6. Hu UHPC 单轴受压 backbone

使用压应变幅值 `e_c>=0`：

\[
\xi=\frac{e_c}{\varepsilon_{c0}},
\qquad
n=\frac{E_c\varepsilon_{c0}}{f_c}.
\]

峰前：

\[
\boxed{
\widehat\sigma_c(e_c)
=f_c\frac{n\xi-\xi^2}{1+(n-2)\xi},
\qquad 0\le\xi\le1.
}
\]

Hu 来源还存在峰后下降段

\[
\widehat\sigma_c
=f_c\frac{\xi}{2(\xi-1)^2+\xi},\qquad\xi>1,
\]

但**本轮早期极限理论不利用峰后段延长 Pu**。主 terminal 定义为压侧 UHPC 首次达到

\[
\boxed{e_c=\varepsilon_{c0},\quad \widehat\sigma_c=f_c.}
\]

这样保持 2026-08-21 的 first-peak section-capacity identity，不恢复材料历史或峰后路径。

物理 tension-positive 应力写为

\[
\sigma_y^{U}=-\widehat\sigma_c(-\varepsilon_y),
\qquad \varepsilon_y\le0.
\]

纵向拉区在本 early N-M terminal 中不计 UHPC 拉力：

\[
\boxed{\sigma_y^U=0\quad(\varepsilon_y>0).}
\]

这不是宣称 UHPC 无抗拉，而是忠实保留最初轴压截面容量的保守边界。

---

# 7. UHPC 厚度积分严格闭式

令

\[
a=n-2.
\]

定义峰前 backbone 的两个原函数：

\[
\boxed{
F_0(\xi)=
-\frac{\xi^2}{2a}
+\frac{(n-1)^2}{a^2}\xi
-\frac{(n-1)^2}{a^3}\ln(1+a\xi),
}
\]

\[
\boxed{
F_1(\xi)=
-\frac{\xi^3}{3a}
+\frac{(n-1)^2}{2a^2}\xi^2
-\frac{(n-1)^2}{a^3}\xi
+\frac{(n-1)^2}{a^4}\ln(1+a\xi).
}
\]

以受压 UHPC 表面为 `y=0`，中性轴深度为 `c>0`。terminal 时：

\[
\varepsilon_y(y)=-\varepsilon_{c0}\left(1-\frac{y}{c}\right).
\]

压区下限：

\[
\boxed{\xi_b=\max\left(0,1-\frac{t_c}{c}\right).}
\]

考虑 web 体积置换后的 UHPC 轴力：

\[
\boxed{
N_y^U(c)=
-(1-\rho_w) f_c c
\left[F_0(1)-F_0(\xi_b)\right].
}
\]

关于核心中面的弯矩：

\[
\boxed{
M_y^U(c)=
(1-\rho_w)f_cc
\left\{
\left(\frac{t_c}{2}-c\right)
\left[F_0(1)-F_0(\xi_b)\right]
+c\left[F_1(1)-F_1(\xi_b)\right]
\right\},
}
\]

符号按具体正弯矩约定统一；求解时只允许一套固定符号。

因此：

```text
UHPC_THICKNESS_QUADRATURE = 0
```

---

# 8. 与当前 R02/R04 钢面的共同应变桥

## 8.1 plane-section terminal

若受压 UHPC 表面 `y=0` 达到 `eps_c0`，则外钢面质心轴向应变由同一平截面场给出。

上钢面中心位于 `y=-t_s/2`：

\[
\varepsilon_{y,+}
=-\varepsilon_{c0}
\left(1+\frac{t_s}{2c}\right).
\]

下钢面中心位于 `y=t_c+t_s/2`：

\[
\varepsilon_{y,-}
=-\varepsilon_{c0}
\left(1-\frac{t_c+t_s/2}{c}\right).
\]

横向当前应变 `eps_x` 由横向 resultant equilibrium 决定；若该控制截面无横向曲率，两个外钢面共享同一个 `eps_x`。若 Airy 给出非零 shear，则 `gamma_xy` 同样由当前结构需求供给；本早期 UHPC terminal 本身不新增 shear-history law。

## 8.2 R02 input

R02 使用 compression-positive normal strain：

\[
(e_x,e_y,\gamma)_{R02}
=(-\varepsilon_x,-\varepsilon_y,\gamma_{xy}).
\]

每个外钢面独立用其真实 `eps_y,+/-` 进入 R02，解有限 cubic：

\[
B_3U^3+B_1U+B_0=0.
\]

根选择仍由 R02 condensed energy，在非负代数根中取能量最小根；不得根据 FEM/试验选择。

## 8.3 R04 ideal-EP cap

R02 mean trial stress 转为 physical tension-positive 后：

\[
\sigma_{vm}^{tr}
=\sqrt{\sigma_x^2-\sigma_x\sigma_y+\sigma_y^2+3\tau_{xy}^2}.
\]

\[
\boxed{
\lambda_p=\min\left(1,\frac{f_y}{\sigma_{vm}^{tr}}\right),
\qquad
\boldsymbol\sigma_f=\lambda_p\boldsymbol\sigma_f^{tr}.
}
\]

钢面 resultants：

\[
\mathbf N_f=t_s\boldsymbol\sigma_f,
\qquad
\mathbf M_f=z_f\mathbf N_f.
\]

own-skin `Et_s^3/12` 只在 initial Airy D 中存在，不在 terminal 再造一个塑性厚度块。

---

# 9. Longitudinal web steel

web 只承担纵向轴力。沿核心厚度使用与 UHPC 相同的 plane-section 轴向应变：

\[
\varepsilon_y^w(y)
=-\varepsilon_{c0}\left(1-\frac{y}{c}\right).
\]

当前早期/现行共同的理想弹塑性轴向 law：

\[
\boxed{
\sigma_y^w(y)
=\operatorname{clip}(E_s\varepsilon_y^w(y),-f_y,+f_y).
}
\]

单位总核心宽度：

\[
N_y^w=\rho_w\int_0^{t_c}\sigma_y^w(y)\,dy,
\]

\[
M_y^w=\rho_w\int_0^{t_c}(t_c/2-y)\sigma_y^w(y)\,dy.
\]

因为 integrand 仅为 linear strain + finite clip，屈服 front 可解析求出，两个积分均按有限分段初等函数精确计算：

```text
WEB_THICKNESS_QUADRATURE = 0
```

横向 `N_x^w=0`。

---

# 10. early 2D UHPC transverse companion：只用于闭合/资格检查

最初成功的 UHPC 替换不是完整任意路径二维 current-material state machine。为在 current full-2D Airy front 下保持可计算，同时不引入后续 Liu/DP/W-W 链，本轮只保留其最小 plane-stress companion。

使用 physical tension-positive signs，UHPC 纵向应力 `sigma_y^U<=0` 已由 Hu backbone 给定。横向小变形 companion 定义为：

\[
\boxed{
\sigma_x^U(y)
=E_c\varepsilon_x+\nu_c\sigma_y^U(y).
}
\]

这是 plane-stress compliance

\[
\varepsilon_x=(\sigma_x-\nu_c\sigma_y)/E_c
\]

的直接反解；它不改变 Hu 纵向 backbone，也不宣称是完整 UHPC 双轴非线性本构。

单位宽度横向 UHPC resultant：

\[
\boxed{
N_x^U
=(1-\rho_w)
\int_0^{t_c}
\left(E_c\varepsilon_x+\nu_c\sigma_y^U(y)\right)dy.
}
\]

因为 `∫sigma_y^U dy` 已由 `N_y^U` 闭式给出，所以 `N_x^U` 同样闭式。

若需要保留 2026-08-21/early-08-22 的材料资格检查，可使用当时 UHPC 首裂拉应力锚点约

\[
\boxed{f_{t,cr}\approx9.7677\ \mathrm{MPa}}.
\]

规则：

```text
max tensile sigma_x^U <= f_t,cr -> early-Hu branch admissible
max tensile sigma_x^U >  f_t,cr -> EARLY-HU DOMAIN EXCEEDED
```

若 exceeded：本 V1 **停止并报告**，不得自动调用 Liu TC、DP、W-W、FHWA 或重新拟合 UHPC。本条正是为了保留用户要求的“最初替换方案”，而不是再次启动后来那串修补任务。

---

# 11. terminal resultant equations

## 11.1 一般 bending controller

对给定有限控制位置 `s`，主要未知量可取：

\[
\boxed{(q,c,\varepsilon_x)}.
\]

由第 5 节得到 Airy demand：

\[
N_x^d(q,s),\qquad N_y^d(q,s),\qquad M_y^d(q,s).
\]

截面总量：

\[
N_x^{sec}=N_x^U+N_{x,+}^f+N_{x,-}^f,
\]

\[
N_y^{sec}=N_y^U+N_y^w+N_{y,+}^f+N_{y,-}^f,
\]

\[
M_y^{sec}=M_y^U+M_y^w+M_{y,+}^f+M_{y,-}^f.
\]

正式 terminal root：

\[
\boxed{
F_x=N_x^{sec}-N_x^d=0,
}
\]

\[
\boxed{
F_y=N_y^{sec}-N_y^d=0,
}
\]

\[
\boxed{
F_M=M_y^{sec}-M_y^d=0.
}
\]

这是 current steel-shell 2D front 与 early Hu N-M terminal 的最小闭合。

若控制位置为内部未知 `s`，再增加 contact stationarity：

\[
\boxed{F_S=0}
\]

或等价的有限候选 stationary condition。若是端点 `s=0/1`，直接使用 active boundary，不凭经验扫空间网格。

## 11.2 symmetric membrane endpoint

若某一试件像当前 Z6 R05 一样控制于

\[
s=0,\qquad M_y^d=0,
\]

且上下钢面应变相同，则 `c->infinity` 的 uniform-strain degeneration 可直接使用共同 `(eps_x,eps_y,q)`：

\[
N_x^{sec}=N_x^d,
\qquad
N_y^{sec}=N_y^d,
\qquad
M_y^{sec}=0.
\]

UHPC 纵向应力仍由 Hu scalar backbone，横向由第 10 节 early companion；R02/R04 保持当前 common-strain face bridge。

但该 uniform endpoint 是否实际控制必须由试件自己的有限理论根决定，不能把 Z6 的 `s=0` 先验复制给 T/BH。

---

# 12. Pu 定义与根选择

对所有 finite admissible candidates：

1. raw geometry/material -> initial ABD；
2. independent integer halfwave selection；
3. Airy demand family；
4. solve terminal algebraic/transcendental finite system；
5. enforce R02 nonnegative physical amplitude / minimum condensed energy；
6. enforce R04 Mises cap；
7. enforce web ideal-EP clip；
8. enforce Hu peak-terminal identity；
9. enforce early transverse tensile qualification if activated；
10. 在与低荷载物理支连通的 admissible candidates 中取第一个 terminal contact。

最终：

\[
\boxed{P_u=P(q_u).}
\]

禁止：

- 用 test/FEM Pu 作 seed selection；
- 先看 comparator 再调 `fc, Ec, epsc0, rho_w, A0`；
- 用 effective width multiplier 修大宽厚比；
- 看到 BH050 偏差后直接开启后续材料链。

---

# 13. 2026-08-21 historical regression identity

以下数值只作为本 V1 所恢复材料思想的历史证据，不是本文件使用 current R02/R04 后的新计算结果。

历史 web-corrected early-Hu 结果：

| Case | historical Pu / MN |
|---|---:|
| T120 | 12.3480 |
| T360 | 11.2978 |
| BH005 | 2.3829 |
| BH010 | 4.4173 |
| BH020 | 8.1398 |
| BH032 | 11.1101 |
| BH050 | 13.5946 |

该阶段的核心特征是：T120/T360 与 BH005–BH032 已进入低百分比误差范围，而最大宽厚比端 BH050 暴露明显异常，从而触发了后续 8/22–8/24 的一连串材料重构研究。

本轮明确不继承那些后续修复，只继承导致上述早期结果的 Hu-UHPC 替换思想。

由于 current steel side 已从旧 R-O/Yun-only branch 升级为 R02/R04，本表只能是 regression reference，不能直接当作新 SSUHPC-HU-R01 的 production target。

---

# 14. 与当前 SSNC 的逐项替换表

| Layer | current SSNC | SSUHPC-HU-R01 |
|---|---|---|
| initial structural front | full composite ABD | full composite ABD，core 改用 UHPC elastic constants |
| Airy/Galerkin | retained | retained |
| steel face local PBL | R02 | R02 |
| steel terminal plasticity | R04 | R04 |
| web | longitudinal ideal-EP | longitudinal ideal-EP |
| core longitudinal terminal | NC-M6 current 2D | Hu uniaxial peak-section closed form |
| core transverse role | NC-M6 full current stress | early plane-stress companion + tensile qualification only |
| full UHPC multiaxial state machine | N/A | NO |
| R03 tangent Pu gate | NO | NO |
| effective width / empirical b/t correction | NO | NO |

因此“替换 UHPC”不是新建第二套结构理论；它只改变 core terminal law 和 initial core elastic constants。

---

# 15. 通过条件与下一步

理论建立门禁：

```text
CURRENT_SSNC_STRUCTURAL_FRONT_RETAINED = YES
INITIAL_FULL_COMPOSITE_ABD_RETAINED = YES
STEEL_OFFSET_DOUBLE_COUNT = NO
R02_RETAINED = YES
R04_RETAINED = YES
R03_REOPENED = NO
NC_M6_CORE_REPLACED = YES
HU_EARLY_UHPC_TERMINAL_ACTIVE = YES
HU_THICKNESS_INTEGRAL_CLOSED = YES
WEB_THICKNESS_INTEGRAL_FINITE_ANALYTIC = YES
FULL_UHPC_HISTORY_STATE_MACHINE = NO
LATER_UHPC_REPAIR_CHAIN_IMPORTED = NO
FORMAL_SPATIAL_QUADRATURE = 0
MATERIAL_POINTS = 0
THEORY_ESTABLISHED = PASS
NUMERICAL_REEXECUTION = PENDING
```

下一步唯一建议：

```text
REEXECUTE THE HISTORICAL 7-CASE SUHPC SET
(T120, T360, BH005, BH010, BH020, BH032, BH050)
USING:
  current full-composite Airy front
  + current R02/R04 steel
  + early Hu-UHPC terminal in this file
WITH ALL FEM/TEST COMPARATORS CLOSED UNTIL THE SEVEN ROOTS ARE FIXED.
```

若仅 BH050/最大宽厚比端再次暴露异常，先把异常原样记录为本 early-Hu branch 的适用边界；除非用户明确授权，否则仍不自动恢复 8/22–8/24 后续修复链。
