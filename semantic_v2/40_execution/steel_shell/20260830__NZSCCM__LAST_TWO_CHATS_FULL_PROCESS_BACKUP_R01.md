# NZ-SCCM — 最近两个对话全过程恢复备份 R01

**Date:** 2026-08-30  
**Branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Status:** `DIALOGUE/DECISION BACKUP ONLY / PRODUCTION MAIN UNCHANGED`  

> 本文件用于防止聊天长度中断导致理论链、纠错过程、用户意见和阶段结论遗失。它不是新的生产理论合同，也不修改 `main`。记录以当前可恢复的用户可见对话、项目已冻结文件和本轮重新核验内容为基础；不把无法访问的隐藏推理伪装成逐字聊天记录。

---

# 0. 两个最近对话的连续主线

最近两个对话的核心不是重新建立一套新理论，而是连续完成以下三件事：

1. 审计并恢复 BH032/BH050 以后大宽厚比板的显式 Airy + current section + R02/R06 + R4/J4 路线；
2. 发现此前解释中仍有若干“backend coefficient / black-box”没有向用户展开，用户明确要求“不许再留黑箱”；
3. 因此从板弯曲算子、闭口截面扭转、局部钢板 R02 形函数、LL/GL Airy compatibility 一直推到可以手工/程序逐项实现的有限解析系数。

用户反复强调的执行纪律：

- 不因聊天中断而重开已淘汰路线；
- 不把数值后端当理论身份；
- 不用经验系数掩盖推导缺口；
- 不使用正式空间 Gauss/Simpson/材料点离散；
- 不用 FEM/试验参与选根或反标；
- 不修改 production `main`，诊断工作留在 diagnostic branch；
- 对“看不见的 backend”必须拆成公式、来源、输入和有限求值过程。

---

# 1. 当前高 B/H 主线：R4–J4，而不是历史 L5

当前恢复并继续使用的大宽厚比主线为：

```text
initial full-composite Marguerre–Airy demand
    -> current SSUHPC section/resultant capacity
    -> R4 = 0
    -> R06 internal events
    -> J4-fold
```

核心结构需求前端：

\[
Q_q=q(q+2q_0),
\]

\[
P^A(q)=P_{cr}\frac{q}{q+q_0}+CQ_q,
\]

\[
N_x^A(q,s)=K_xQ_q,
\]

\[
N_y^A(q,s)=-\left[\frac{P^A(q)}{b}+GQ_q(1-2s^2)\right],
\]

\[
M_x^A(q,s)=J_xqs,\qquad M_y^A(q,s)=J_yqs.
\]

当前 section state：

\[
\mathbf x=(\varepsilon_T^0,\kappa_T,\varepsilon_L^0,\kappa_L)^T.
\]

桥接方程：

\[
\boxed{\mathbf R_4(\mathbf x;q)=\mathbf S(\mathbf x)-\mathbf D(q)=\mathbf0.}
\]

终点：

\[
\boxed{\det J_4=0,\qquad J_4=\partial\mathbf R_4/\partial\mathbf x.}
\]

沿与 \(q=0\) 连通的主支继续，R06 lower/upper 只是内部 active-set event，不是极限承载力终点。

此前 20260827_1135 文件尝试过 fully compatible generalized-work state

\[
[q,\alpha,U_+,U_-]
\]

并提出 bordered \(L_5=0\)。后续 compatibility audit 说明 old frozen-Airy demand 与 current nonlinear section 不能无条件组成一个 exact one-state kinematic/constitutive theory。当前生产诊断路线没有恢复 L5，而继续 R4–J4。1135/1240 文件只继续作为 R02 局部两尺度运动学和 Airy compatibility 的理论证据。

---

# 2. 最近对话中关于“为什么还有黑箱”的纠错

用户指出：虽然此前已经解释了 global Airy、R02/R06、UHPC N–M 和 R4/J4，但若仍然出现

\[
K_A,\quad K_{d\Delta},\quad K_{\Delta\Delta},\quad h_x,h_y,h_\gamma
\]

等“由 backend 计算”的说法，本质上仍然没有达到可手算审计要求。

本轮因此重新打开并核验：

- `20260827_1135__NZSCCM__UNIFIED_Q_U_EXPLICIT_KINEMATIC_LEDGER_AND_GENERALIZED_WORK_R01.md`
- `20260827_1240__NZSCCM__EXPLICIT_AIRY_Q_U_COMMON_CURVATURE_REPAIR_WITH_UNCHANGED_NM_R02.md`

确认它们已经给出：

- local mode shape；
- LL mean shortening；
- LL Airy harmonic set；
- GL exact compatibility source；
- exact harmonic/sinc integration identity；
- BH032/BH050 的 R02 LL regression；

但 `K_{dDelta}` 和 `K_{DeltaDelta}` 当时仍被称为 “Airy backend task”。因此本轮继续将其拆成 finite harmonic double sum，而不是接受为隐藏常数。

---

# 3. kx, ky 的身份：纯几何波数，不是经验参数

R02 local shape：

\[
\boxed{\phi(\xi,\eta)=(1-\cos k_x\xi)(1-\cos k_y\eta).}
\]

对于一个完整 local cell：

\[
\boxed{k_x=\frac{2\pi}{L_x},\qquad k_y=\frac{2\pi}{L_y}.}
\]

若写成包含整数局部纵向波数 \(m\) 的整板形式，则等价地可出现

\[
k_x=\frac{2m\pi}{a_\ell},
\]

本质仍由真实几何/选定整数物理波数确定。

这里“R02 regression / source regression”中的 regression 是**回归测试、退化一致性检验**，不是统计回归、拟合或经验标定。

例如冻结 BH032 geometry：

\[
L_x=360\ \mathrm{mm},\quad L_y=355.5555556\ \mathrm{mm},
\]

因此直接有

\[
k_x=2\pi/360=0.01745329252\ \mathrm{mm}^{-1},
\]

\[
k_y=2\pi/355.5555556=0.01767145868\ \mathrm{mm}^{-1}.
\]

冻结 BH050 geometry：

\[
L_x=562.5\ \mathrm{mm},\quad L_y=555.5555556\ \mathrm{mm},
\]

因此

\[
k_x=0.01117010721,\quad k_y=0.01130973355\ \mathrm{mm}^{-1}.
\]

这些数值没有经过试验荷载/FEM拟合。

---

# 4. 全局正交板弯曲算子从弯矩平衡展开

曲率：

\[
\kappa_x=-w_{,xx},\qquad \kappa_y=-w_{,yy},\qquad \kappa_{xy}=-2w_{,xy}.
\]

正交板：

\[
\begin{bmatrix}M_x\\M_y\\M_{xy}\end{bmatrix}
=
\begin{bmatrix}
D_x&D_\mu&0\\
D_\mu&D_y&0\\
0&0&D_{66}
\end{bmatrix}
\begin{bmatrix}\kappa_x\\\kappa_y\\\kappa_{xy}\end{bmatrix}.
\]

板元弯矩平衡：

\[
M_{x,xx}+2M_{xy,xy}+M_{y,yy}+p=0.
\]

代入后得到：

\[
D_xw_{,xxxx}+2(D_\mu+2D_{66})w_{,xxyy}+D_yw_{,yyyy}=p.
\]

因此：

\[
\boxed{H=D_\mu+2D_{66}.}
\]

当前项目符号定义

\[
\boxed{D_{xy}\equiv2D_{66}},
\]

故：

\[
\boxed{H=D_\mu+D_{xy}.}
\]

必须避免误读：当前项目的 \(D_{xy}\) 不是经典层合板的 \(D_{12}\)；\(D_\mu\) 才对应等效 \(D_{12}\)。

---

# 5. Dt -> Dxy 的闭口截面扭转来源

Bredt–Batho 单闭口薄壁截面：

\[
T=2A_mq_s,
\]

\[
\theta'=\frac{q_s}{2A_mG}\oint\frac{ds}{t},
\]

所以：

\[
\boxed{J=\frac{4A_m^2}{\oint ds/t}.}
\]

定义单位板宽 torsional stiffness：

\[
D_t=\frac{GJ}{b}.
\]

由板纯扭曲能量与 Saint-Venant 截面扭转能量等价：

\[
\boxed{D_t=4D_{66}},
\]

因此：

\[
\boxed{D_{xy}=2D_{66}=D_t/2.}
\]

钢箱中线面积：

\[
A_\Box=(b-t_s)(h-t_s),
\]

统一壳厚时：

\[
\oint\frac{ds}{t_s}
=\frac{2[(b-t_s)+(h-t_s)]}{t_s}.
\]

实心 UHPC 矩形 core 使用 Saint-Venant rectangle torsion approximation：

\[
J_c=\beta_{shape}(b-2t_s)(h-2t_s)^3,
\]

\[
\beta_{shape}=\frac13(1-0.63r_h+0.052r_h^5).
\]

因此：

\[
D_t=
\frac{4G_sA_\Box^2}{b\oint ds/t_s}
+
\frac{G_c}{b}\beta_{shape}(b-2t_s)(h-2t_s)^3.
\]

---

# 6. R02 local shape 的全部基础导数

定义：

\[
X=k_x\xi,\qquad Y=k_y\eta.
\]

则：

\[
\phi_x=k_x\sin X(1-\cos Y),
\]

\[
\phi_y=k_y(1-\cos X)\sin Y,
\]

\[
\phi_{xx}=k_x^2\cos X(1-\cos Y),
\]

\[
\phi_{yy}=k_y^2(1-\cos X)\cos Y,
\]

\[
\phi_{xy}=k_xk_y\sin X\sin Y.
\]

cell average：

\[
\langle f\rangle=\frac1{L_xL_y}\int_0^{L_x}\int_0^{L_y}f\,d\eta d\xi.
\]

由完整周期正交性：

\[
\boxed{c_x=\frac12\langle\phi_x^2\rangle=\frac38k_x^2},
\]

\[
\boxed{c_y=\frac12\langle\phi_y^2\rangle=\frac38k_y^2},
\]

\[
\boxed{\langle\phi_x\phi_y\rangle=0.}
\]

这些是解析几何常数，不是经验系数。

---

# 7. local bending coefficient Kb 的闭式

局部钢板弹性弯曲刚度：

\[
D_s=\frac{E_st_s^3}{12(1-\nu_s^2)}.
\]

局部增量挠度：

\[
\Delta w_\ell=(U-A_0)\phi.
\]

积分局部 isotropic plate bending energy 后：

\[
\boxed{
K_b^\ell
=
D_s\left[\frac34(k_x^4+k_y^4)+\frac12k_x^2k_y^2\right].
}
\]

与

\[
\frac12K_b^\ell(U-A_0)^2
\]

对应。

其弹性小幅值退化可得到云露四边固结局部板系数：

\[
\boxed{k_{crx}=4\frac{\beta_\ell^2}{m^2}+\frac83+4\frac{m^2}{\beta_\ell^2}.}
\]

因此当前 R02 shape-energy 与云露 local elastic buckling skeleton 可逐项退化一致，而不是经验拼接。

---

# 8. LL Airy compatibility 与 KA 的完整解析闭合

定义

\[
d=U^2-A_0^2.
\]

LL compatibility：

\[
\boxed{\nabla^4F_{LL}=-E_sd(\phi_{xx}\phi_{yy}-\phi_{xy}^2).}
\]

右端精确展开产生固定七个 harmonic：

```text
(0,1) +1/2
(0,2) -1/2
(1,0) +1/2
(1,1) -1
(1,2) +1/2
(2,0) -1/2
(2,1) +1/2
```

令

\[
\Lambda_{pq}=[(pk_x)^2+(qk_y)^2]^2,
\]

则每个 harmonic 直接除以 \(\Lambda_{pq}\) 得 Airy 特解。plane-stress complementary energy 利用 Fourier 正交性可化成有限和，最终：

\[
\boxed{
K_A=k_x^4k_y^4\left[
\frac{17}{256k_y^4}
+\frac{17}{256k_x^4}
+\frac1{8(k_x^2+k_y^2)^2}
+\frac1{32(k_x^2+4k_y^2)^2}
+\frac1{32(4k_x^2+k_y^2)^2}
\right].
}
\]

BH032：

\[
K_A=1.58478790282955\times10^{-8}\ \mathrm{mm}^{-4}.
\]

BH050：

\[
K_A=2.65883289599584\times10^{-9}\ \mathrm{mm}^{-4}.
\]

与冻结 R02 公式和独立 exact harmonic Airy-energy 评价机器精度一致。这叫 regression test：新推导必须退回旧冻结结果，不是统计回归。

---

# 9. GG / GL / LL 两尺度运动学

钢面总场：

\[
w_f=w_g+w_{\ell f}.
\]

全局初始/当前幅值：

\[
W_0=bq_0,\qquad W=b(q_0+q).
\]

local initial/current：

\[
w_\ell^0=s_fA_0\phi,\qquad w_\ell=s_fU\phi.
\]

定义：

\[
\boxed{d=U^2-A_0^2},
\]

\[
\boxed{\Delta=s_f(WU-W_0A_0)=s_fb[qU+q_0(U-A_0)].}
\]

总 von Karman membrane geometric increment 精确分为：

```text
GG : global-global
GL : global-local
LL : local-local
```

GL：

\[
\Delta\varepsilon_{xx}^{GL}=\Delta\psi_x\phi_x,
\]

\[
\Delta\varepsilon_{yy}^{GL}=\Delta\psi_y\phi_y,
\]

\[
\Delta\gamma_{xy}^{GL}=\Delta(\psi_x\phi_y+\psi_y\phi_x).
\]

LL：

\[
\Delta\varepsilon_{xx}^{LL}=\frac12d\phi_x^2,
\]

\[
\Delta\varepsilon_{yy}^{LL}=\frac12d\phi_y^2,
\]

\[
\Delta\gamma_{xy}^{LL}=d\phi_x\phi_y.
\]

R02 已经含 LL mean shortening 与 LL Airy fluctuation，因此禁止再增加独立 U^2 修正，否则 double count。

---

# 10. hx, hy, hgamma：位置相关的解析几何矩，不是拟合系数

定义 global shape：

\[
\psi(x,y)=\sin\alpha x\sin\beta y.
\]

cell registration：

\[
x=x_0+\xi,\qquad y=y_0+\eta,
\]

\[
\delta_x=\alpha x_0,\qquad \delta_y=\beta y_0.
\]

定义：

\[
\boxed{h_x=\langle\psi_x\phi_x\rangle},
\]

\[
\boxed{h_y=\langle\psi_y\phi_y\rangle},
\]

\[
\boxed{h_\gamma=\langle\psi_x\phi_y+\psi_y\phi_x\rangle}.
\]

这些量随 actual PBL cell origin/phase 改变，正负号也可改变；这是纯几何相位效应，不能用 FEM agreement 选符号。

基本 exact endpoint moments：

\[
C(\omega,\delta;L)=\frac{\sin(\omega L+\delta)-\sin\delta}{\omega L},
\]

\[
S(\omega,\delta;L)=\frac{\cos\delta-\cos(\omega L+\delta)}{\omega L},
\]

并在 \(\omega=0\) 取连续极限。

再定义：

\[
\mathcal C_s=\frac12[S(\omega+k)-S(\omega-k)],
\]

\[
\mathcal S_{1-c}=S(\omega)-\frac12[S(\omega+k)+S(\omega-k)],
\]

\[
\mathcal C_{1-c}=C(\omega)-\frac12[C(\omega+k)+C(\omega-k)],
\]

\[
\mathcal S_s=\frac12[C(\omega-k)-C(\omega+k)].
\]

于是：

\[
\boxed{h_x=\alpha k_x\mathcal C_s^x\mathcal S_{1-c}^y},
\]

\[
\boxed{h_y=\beta k_y\mathcal S_{1-c}^x\mathcal C_s^y},
\]

\[
\boxed{h_\gamma=\alpha k_y\mathcal C_{1-c}^x\mathcal S_s^y+\beta k_x\mathcal S_s^x\mathcal C_{1-c}^y}.
\]

全部为 sine/cosine endpoint expressions，不需要数值积分。

---

# 11. GL Airy compatibility 以及 KdDelta / KDeltaDelta

GL compatibility source：

\[
\boxed{
\mathcal C_{GL}
=\psi_{xx}\phi_{yy}+\phi_{xx}\psi_{yy}-2\psi_{xy}\phi_{xy}.
}
\]

局部 GL Airy：

\[
\boxed{\nabla^4F_{GL}=-E_s\Delta\mathcal C_{GL}.}
\]

由于 global frequency \((\alpha,\beta)\) 与 local frequency \((k_x,k_y)\) 的乘积只产生有限组合频率，GL source 可写成有限指数和：

\[
\mathcal C_{GL}=\sum_r c_re^{i(\lambda_r\xi+\mu_r\eta)}.
\]

频率只来自有限集合：

\[
\lambda\in\{\pm\alpha,\ \pm\alpha\pm k_x\},
\]

\[
\mu\in\{\pm\beta,\ \pm\beta\pm k_y\}.
\]

每个 mode 的 biharmonic 特解：

\[
F_{GL,r}=-E_s\Delta\frac{c_r}{(\lambda_r^2+\mu_r^2)^2}e^{i(\lambda_r\xi+\mu_r\eta)}.
\]

令归一化应力：

\[
\boldsymbol\sigma^{LL}=E_sd\hat{\boldsymbol\sigma}^{LL},
\]

\[
\boldsymbol\sigma^{GL}=E_s\Delta\hat{\boldsymbol\sigma}^{GL},
\]

plane-stress energy metric：

\[
\mathbf H_\nu=
\begin{bmatrix}
1&-\nu_s&0\\
-\nu_s&1&0\\
0&0&2(1+\nu_s)
\end{bmatrix}.
\]

则：

\[
\boxed{K_{d\Delta}=\frac12\langle(\hat\sigma^{LL})^T\mathbf H_\nu\hat\sigma^{GL}\rangle},
\]

\[
\boxed{K_{\Delta\Delta}=\frac12\langle(\hat\sigma^{GL})^T\mathbf H_\nu\hat\sigma^{GL}\rangle}.
\]

对于任意 real frequency，cell exact moment：

\[
\frac1L\int_{x_0}^{x_0+L}e^{i\omega x}dx
=e^{i\omega(x_0+L/2)}\operatorname{sinc}(\omega L/2).
\]

因此这两个系数最终是有限 double harmonic sum × exact sinc moments，不是数值积分、不是经验拟合、也不是不可审计 backend。

---

# 12. R02 augmented energy 的完整物理解释

\[
\boxed{
\begin{aligned}
\Pi_{R02}^{aug}(U)={}&
\frac12K_b^\ell(U-A_0)^2\\
&+\frac12t_sQ_s(m_x^2+m_y^2+2\nu_sm_xm_y)\\
&+\frac12t_sG_sm_\gamma^2\\
&+t_sE_s[K_Ad^2+2K_{d\Delta}d\Delta+K_{\Delta\Delta}\Delta^2].
\end{aligned}}
\]

其中：

\[
m_x=e_x-c_xd-h_x\Delta,
\]

\[
m_y=e_y-c_yd-h_y\Delta,
\]

\[
m_\gamma=\gamma-h_\gamma\Delta.
\]

各项身份：

- `Kb`: local steel plate incremental bending energy；
- `mean membrane`: full-width mean local membrane energy；
- `KA d^2`: LL incompatibility Airy fluctuation energy；
- `2 KdDelta dDelta`: LL–GL Airy cross energy；
- `KDeltaDelta Delta^2`: GL Airy self energy。

因为 \(d\) 为 U 的二次函数、\(\Delta\) 为 U 的一次函数，整个能量最高四次：

\[
\Pi(U)=a_4U^4+a_3U^3+a_2U^2+a_1U+a_0.
\]

所以：

\[
\boxed{R_U=\partial\Pi/\partial U=B_3U^3+B_2U^2+B_1U+B_0=0.}
\]

R02 cubic 是二阶几何 + 二次能量的代数结果，不是拟合 cubic。

---

# 13. 当前 BH050 受力分配问题的诊断边界

已知现象：BH050 相比 BH032 出现更明显的局部钢面屈曲/非线性，同时理论总承载力仍可接近 FEM，但 constituent load split / deformation mechanism 不一致。

当前最重要的理论结构事实：

1. global Airy front 的 \(A,D,P_{cr},C,K_x,G,J_x,J_y\) 仍由 **initial full-composite elastic stiffness** 生成；
2. current UHPC / steel / web response 在 downstream section operator 中处理；
3. R4 是 resultant matching：\(\mathbf S(\mathbf x)=\mathbf D^A(q)\)；
4. current nonlinear tangent stiffness 没有返回 global Airy PDE 去重新改变 global membrane redistribution / bending demand；
5. section state 中 \(\kappa_T,\kappa_L\) 为 independent unknowns，而 old Airy q also has its own kinematic curvature content；此前 compatibility audit 已证明不能简单同时坚持 frozen Airy、current nonlinear section 和 exact one-state kinematics；
6. old R02 若不包含 GL(qU) 时，local steel mode 只通过 external face state 感知 global deformation，缺少 exact global-local geometric cross coupling；这一缺口在 BH050 大 local amplitude 下比 BH032 更可能放大；
7. R06 active projection 在进入局部屈曲/屈服后改变 steel resultant branch，其与完整 global q/U work-conjugate tangent 的一致性尚不是生产理论已证明项。

因此当前优先诊断结论是：

```text
BH050 redistribution mismatch
    is NOT simply “Airy theory cannot be nonlinear”.

Primary suspect:
    frozen-initial-stiffness Airy demand + downstream current-section matching
    forms a one-way / partially coupled architecture.

Secondary coupled suspect:
    loss or incomplete activation of exact GL(qU) local-steel coupling and
    R06 current-state work/tangent consistency.
```

Airy method itself可以用 current/tangent stiffness 重建；当前限制来自本项目这一版 Airy front 被有意冻结为 initial full-composite elastic skeleton，而不是 Airy 数学本身天生只能弹性。

对于 BH050，这会造成：钢面局部屈曲/屈服使当前 tangent stiffness 显著下降后，真实结构应发生 steel -> UHPC / other steel/web 的重新分配并改变 global stress pattern；但 frozen Airy demand coefficients 仍按初始 composite stiffness 继续给出 \(N_x^A,N_y^A,M_x^A,M_y^A\)。downstream section 可以通过调整 independent section strain/curvature 去“满足”这些 resultants，却不能反过来改写 global Airy distribution。因此 total P 可能偶然仍接近，而 constituent force split 和 deformation state 先出现系统偏差。

这被列为下一步应优先做的 component-by-component audit，而不是先调材料参数、试验反标或改 q-root。

---

# 14. 当前高 B/H 诊断参考点

现有 BH005–BH050 FEM peaks：

- BH005 2.355811 MN
- BH010 4.304329 MN
- BH020 8.007901 MN
- BH032 10.990480 MN
- BH050 12.591227 MN

此前 theory–FEM total-load difference：

- BH005 +4.52%
- BH010 +6.48%
- BH020 +6.87%
- BH032 -0.45%
- BH050 +6.08%

UHPC peak compression magnitudes：

- BH005 0.00808897
- BH010 0.00792807
- BH020 0.00769249
- BH032 0.00515362
- BH050 0.00281273

steel local-buckling ratios：

- 0.188
- 0.376
- 0.752
- 1.203
- 1.880

local-wave amplitudes：

- BH005–BH010 <= 0.23 mm
- BH020 ~2.84 mm
- BH032 ~11.32 mm
- BH050 ~15.95 mm

解释边界：这些数据支持“BH050 进入更强 local steel / composite redistribution regime”，但不能单独证明某一个 theoretical term 是唯一原因。

---

# 15. 试件拓展设计的最近决定

用户后来明确撤回此前人为设计的 16-case local-ratio 156.25 / 312.50 factorial practical specimens，要求回到 existing Abaqus model parameters，设计 whole-plate B/H > 50 并扩展至 100；local subplate pattern 参考现有 T120/T360 两类。

当前建议但尚未由用户再次逐项锁定的 new cases：

\[
B/H=60,70,85,100
\]

×

```text
T120
T360
```

即 8 个 new specimens。

existing baseline：

\[
H=50\ \mathrm{mm},\quad t_s=4\ \mathrm{mm},\quad t_c\approx42\ \mathrm{mm},\quad L=3000\ \mathrm{mm}.
\]

T120 nominal local spacing ratio：

\[
s_{PBL}/t_s=120/4=30.
\]

T360：

\[
s_{PBL}/t_s=360/4=90.
\]

但 precise theoretical local `Bs` definition must be checked against actual geometry before replacing it by spacing automatically.

Suggested widths if H=50 mm：

- BH060: B=3000 mm
- BH070: B=3500 mm
- BH085: B=4250 mm
- BH100: B=5000 mm

Current recommendation keeps L=3000 mm to change B only, but this L-freeze is a recommendation rather than an independently re-approved lock.

---

# 16. Explicit exclusions / anti-drift ledger

```text
NO FEM/test in root selection
NO fitted qU coefficient
NO fitted curvature factor
NO empirical Kx/Ky local wave numbers
NO statistical regression in R02 regression tests
NO spatial Gauss/Simpson/material-point grid in formal operator
NO effective width production reduction
NO extra U^2 correction beyond existing LL terms
NO revival of historical L5 as current high-B/H terminal without explicit reopening
NO automatic main-branch modification
NO assumption that Airy mathematics itself cannot support nonlinear/current stiffness
```

---

# 17. Next diagnostic question frozen by the conversation

The immediate structural question after this backup is:

> For BH050, quantify how much of the constituent load-split discrepancy is caused by the frozen initial-stiffness Airy demand front, how much by the R4 independent-section compatibility relaxation, and how much by local steel GL(qU)/R06 coupling.

Recommended decomposition without FEM calibration:

1. baseline frozen-Airy R4/J4;
2. same frozen material operators but expose `q -> kappa^g` mismatch as an audit residual, without forcing a new root;
3. add exact local GL(qU) term to R02 only and quantify steel-face resultant change;
4. compare current constituent tangent stiffness ratios with initial Airy A/D weights at the same blind state;
5. only after theoretical states are frozen, compare FEM constituent force shares / deformation fields as a post-check.

This is a diagnosis of architecture, not a parameter-fitting program.

---

# 18. Backup identity

This file is a continuity record for the two most recent dialogue stages. It preserves user objections, corrections, active theory, abandoned branches, explicit formulas, black-box elimination, BH050 diagnosis direction, and current T120/T360 specimen-design decision so that a new chat can resume without reconstructing the project from filenames alone.
