可以。先把我上一轮那个 **“compatible + Multiwave = 10.1626 MN”** 的计算过程完全摊开。这里我先纠正一个表达：那一轮是**诊断耦合版**，不是已经完成的最终新理论。它做到了“全局曲率兼容”，但钢壳端仍然沿用了旧 Multiwave 的**每个钢面一个宏观平均应变 → R02/R06 平均应力**接口。这个接口正是我们现在最应该一起审的地方。

当前 R02 的正式源公式本身很清楚：局部单元以 `e_x,e_y,\gamma` 三个标量作为宏观输入，局部能量为 quartic，`\partial\Pi/\partial U` 为 cubic；若进入 R06，则缩放 face strain 和 `q`，每次重新凝聚 `U`，再由完整局部场找 first-local-yield。 原 Multiwave05 也是把每个钢面的条带平均应力加权后送回 section resultant。

下面严格按上一轮 BH050 的实际逻辑来。

---

# 1. 输入

BH050：

```math
b=2500\ {\rm mm},\qquad a=5000\ {\rm mm},
```

```math
t_c=42\ {\rm mm},\qquad t_s=4\ {\rm mm},
```

```math
A_w=1332\ {\rm mm^2},
```

```math
E_s=206000\ {\rm MPa},\quad \nu_s=0.30,\quad f_y=355\ {\rm MPa},
```

```math
E_c=43400\ {\rm MPa},\quad \nu_c=0.20,\quad f_c=141.1\ {\rm MPa},
```

```math
\varepsilon_{c0}=0.0035, \qquad A_{0g}=6.25\ {\rm mm}.
```

所以：

```math
q_0=\frac{A_{0g}}b =\frac{6.25}{2500} =0.0025.
```

Multiwave 条带：

```math
\text{TOP}:\quad n=(3,4,5,6),
```

```math
\omega=(0.225,0.225,0.225,0.325),
```

```math
\text{BOTTOM}:\quad n=(3,4,5,20),
```

```math
\omega=(0.225,0.45,0.225,0.10).
```

共同：

```math
L_x=562.5\ {\rm mm}, \qquad A_{0\ell}=0.3515625\ {\rm mm}.
```

这些就是当前 BH050 Multiwave smoke-test 的输入。

---

# 2. 线弹性前端只负责确定 global mode

由初始 `A/D`：

```math
m^*=2,
```

因此：

```math
\alpha=\frac{\pi}{2500},
```

```math
\beta=\frac{2\pi}{5000} =\frac{\pi}{2500}.
```

所以 BH050 恰好：

```math
\boxed{\alpha=\beta}.
```

原线性临界荷载：

```math
P_{cr}=19.5818772367\ {\rm MN}.
```

这一值和原 Multiwave05 一致。

到这里仍然没有改变旧 Airy 的线性前端。

---

# 3. 上一轮比较为什么取 `q=0.00516361`

这一步非常重要：**这个** **`q`** **不是新理论求出来的极限根。**

为了先检查“同一个实际几何变形状态下内部受力能不能对”，我使用 FEM 的 global U2 曲率：

```math
\kappa_{y,FEM} = 2.03851\times10^{-5}\ {\rm mm^{-1}}.
```

最新 strain-origin audit 对 BH050 给出的 R4 / geometric / FEM 曲率分别为：

```math
6.5610\times10^{-5}, \quad 1.94665\times10^{-5}, \quad 2.03851\times10^{-5}\ {\rm mm^{-1}},
```

而且明确证明 R4 的曲率不是 `q` 的几何曲率。

新兼容模型规定：

```math
\kappa_{y,\max} = bq\beta^2 = \frac{\pi^2q}{b}.
```

因此同 FEM 曲率状态：

```math
q= \frac{\kappa_{y,FEM}b}{\pi^2}
```

得到：

```math
\boxed{ q=0.00516361. }
```

所以这一轮回答的问题只是：

> 若 global deformation 已经与 FEM 一致，compatible + Multiwave 内部受力会得到什么？

不是用 FEM 选择 Pu。

---

# 4. 总面外位移和曲率

定义：

```math
\psi(x,y) = \sin\alpha x\sin\beta y.
```

新增位移：

```math
w_d=bq\psi.
```

初始位移：

```math
w_0=bq_0\psi.
```

因此：

```math
Q=q(q+2q_0).
```

代数值：

```math
Q = 0.00516361 (0.00516361+0.005)
```

得到：

```math
\boxed{ Q=5.24809182\times10^{-5}. }
```

曲率**不再作为未知变量求解**：

```math
\kappa_x=bq\alpha^2\psi,
```

```math
\kappa_y=bq\beta^2\psi.
```

因为 `\alpha=\beta`：

```math
\boxed{ \kappa_{x,\max} = \kappa_{y,\max} = 2.03851152\times10^{-5}\ {\rm mm^{-1}}. }
```

这一步是新体系和 R4 最大的区别。

---

# 5. compatibility 本身直接确定两个膜应变谐波

最低 compatible field 写成：

```math
\varepsilon_x^0 = e_{x0} + e_{x\alpha}\cos2\alpha x + e_{x\beta}\cos2\beta y,
```

```math
\varepsilon_y^0 = e_{y0} + e_{y\alpha}\cos2\alpha x + e_{y\beta}\cos2\beta y.
```

第一版取：

```math
\gamma_{xy}^0=0.
```

Marguerre compatibility：

```math
\varepsilon_{x,yy}^0 + \varepsilon_{y,xx}^0 = \Gamma(w,w_0),
```

其中：

```math
\Gamma = \frac{ b^2\alpha^2\beta^2Q }{2} \left( \cos2\alpha x+ \cos2\beta y \right).
```

逐谐波比较：

```math
-4\beta^2e_{x\beta} = \frac{b^2\alpha^2\beta^2Q}{2},
```

所以：

```math
\boxed{ e_{x\beta} = -\frac{b^2\alpha^2Q}{8}. }
```

同理：

```math
\boxed{ e_{y\alpha} = -\frac{b^2\beta^2Q}{8}. }
```

BH050 因为：

```math
b^2\alpha^2=b^2\beta^2=\pi^2,
```

所以：

```math
\boxed{ e_{x\beta} = e_{y\alpha} = -6.47457377\times10^{-5}. }
```

这是非常值得注意的一步：

```math
\boxed{ e_{x\beta},e_{y\alpha} }
```

不是材料反求出来的。

不是钢壳反求出来的。

不是 FEM 拟合出来的。

而是 compatibility 强制给定。

---

# 6. 剩下的全局未知量

固定 `q` 后，真正需要解的是：

```math
e_{x0}, \quad e_{x\alpha}, \quad e_{y0}, \quad e_{y\beta},
```

以及 Airy 膜力：

```math
n_x,\quad n_y,\quad N_0.
```

其中：

```math
N_x^A=n_x\cos2\beta y,
```

```math
N_y^A=-N_0+n_y\cos2\alpha x.
```

最终：

```math
\boxed{ P=bN_0. }
```

所以 fixed-`q` 主系统一共是：

```math
\boxed{7\text{ 个未知量}.}
```

这一点与旧 R4：

```math
(\varepsilon_x^0,\kappa_x,\varepsilon_y^0,\kappa_y)
```

完全不同。

---

# 7. 全截面的真实 strain field

UHPC 任意厚度 `z`：

```math
\boxed{ \varepsilon_x(x,y,z) = \varepsilon_x^0(x,y) + z\kappa_x(x,y) }
```

```math
\boxed{ \varepsilon_y(x,y,z) = \varepsilon_y^0(x,y) + z\kappa_y(x,y) }
```

并保持：

```math
\kappa=\kappa(q).
```

不存在第二套独立曲率。

对于 embedded FEM 的这一轮对比，我没有让 PI 改写钢面几何位置，而按 perfect-bond benchmark：

```math
z_f=\frac{42+4}{2}=23\ {\rm mm}.
```

所以：

```math
\boxed{ e_{x,s}^{\pm}(x,y) = \varepsilon_x^0(x,y) \pm23\kappa_x(x,y) }
```

```math
\boxed{ e_{y,s}^{\pm}(x,y) = \varepsilon_y^0(x,y) \pm23\kappa_y(x,y). }
```

这里和原 05 的 PI 有意不同；原 05 smoke test 有 `z_+^{PI}=20.917` mm、`z_-^{PI}=-21.136` mm。

---

# 8. UHPC 在这一轮怎样算

这一轮不是旧 R14 的单一厚度 section inverse。

对每一个 compatible strain state 使用我们刚才建立的 AC-UHPC V0：

```math
\varepsilon \rightarrow \text{PWL uniaxial branch} \rightarrow \text{Poisson-coupled plane stress} \rightarrow \sigma_x,\sigma_y.
```

然后厚度积分：

```math
N_x^U(x,y) = (1-\rho_w) \int_{-t_c/2}^{t_c/2} \sigma_x(x,y,z)\,dz,
```

```math
N_y^U(x,y) = (1-\rho_w) \int_{-t_c/2}^{t_c/2} \sigma_y(x,y,z)\,dz.
```

web 另算：

```math
N_y^w(x,y).
```

再作 modal projection。

因此 UHPC 不需要去满足一个预先规定的：

```math
N_y^A(q)
```

截面数值。

它首先由 compatible strain 自己产生一个二维膜力场。

---

# 9. 然后是现在最值得你看的地方：我当时怎么把 Multiwave 接进去的

这里确实有一个**降阶**。

当前正式 R02 的输入仍然是三个宏观 scalar：

```math
e_x,\qquad e_y,\qquad\gamma.
```

其基本局部运动学为：

```math
k_x=\frac{2\pi}{L_x}, \qquad k_y=\frac{2\pi}{L_y},
```

```math
\phi = (1-\cos k_x\xi) (1-\cos k_y\eta),
```

```math
c_x=\frac38k_x^2, \qquad c_y=\frac38k_y^2.
```

局部幅值：

```math
d=U^2-A_0^2.
```

qU-off 时我令：

```math
\boxed{\Delta=0}.
```

所以：

```math
m_x=e_x-c_xd,
```

```math
m_y=e_y-c_yd,
```

```math
m_\gamma=\gamma.
```

局部能量：

```math
\boxed{ \begin{aligned} \Pi(U)=& \frac12K_b(U-A_0)^2\\ &+\frac12t_sQ_s (m_x^2+m_y^2+2\nu_sm_xm_y)\\ &+\frac12t_sG_sm_\gamma^2\\ &+t_sE_sK_Ad^2. \end{aligned} }
```

这正是完整 R02 在关闭 GL `qU` 后的退化式；完整源式还包括 `d\Delta` 和 `\Delta^2` 两项。

然后：

```math
\frac{\partial\Pi}{\partial U}=0
```

仍然是 cubic。

candidate set：

```math
\boxed{ \{U=0\} + \{\text{所有正实驻点根}\}. }
```

取：

```math
\boxed{ U_*=\arg\min \Pi. }
```

这部分没有按 FEM 选根。

---

# 10. 关键问题：compatible steel field 被怎样压成 R02 的 scalar `e_x,e_y`

这正是上一轮**最不完整的一步**。

compatible 理论实际给的是：

```math
e_{x,s}^{\pm}(x,y), \qquad e_{y,s}^{\pm}(x,y).
```

但是旧 R02 接口只接受：

```math
(e_x,e_y,\gamma)^\pm.
```

因此上一轮诊断实现做的是：

```math
\boxed{ e_{x,s}^{\pm}(x,y) \longrightarrow \bar e_{x,s}^{\pm} }
```

```math
\boxed{ e_{y,s}^{\pm}(x,y) \longrightarrow \bar e_{y,s}^{\pm} }
```

再把同一面的这对宏观平均量送给其所有 `n`-条带。

也就是说，TOP 的：

```math
n=3,4,5,6
```

共享同一：

```math
\bar e_x^+,\bar e_y^+,
```

BOTTOM 的：

```math
n=3,4,5,20
```

共享另一：

```math
\bar e_x^-,\bar e_y^-.
```

不同条带只通过：

```math
L_y=\frac{L_G}{n}, \quad k_y, \quad K_b, \quad K_A, \quad A_{0\ell}
```

区别。

**这就是我现在最希望你一起审的地方。**

因为：

```math
\boxed{ \text{global field 已经恢复成二维场，} }
```

但进入钢壳时又重新变成：

```math
\boxed{ \text{一个 face 一个平均 strain state}. }
```

---

# 11. 每个条带随后怎么出平均钢应力

给定 `U_*`：

```math
\bar\sigma_x^{R02} = Q_s(m_x+\nu_sm_y),
```

```math
\bar\sigma_y^{R02} = Q_s(m_y+\nu_sm_x),
```

```math
\bar\tau^{R02} = G_sm_\gamma.
```

然后检查局部完整 LL 场的 Mises。

如果局部 first-yield 不触发，直接返回。

如果触发 R06，则定义：

```math
0<\eta\le1.
```

按冻结规则：

```math
(e_x,e_y,\gamma) \rightarrow \eta(e_x,e_y,\gamma),
```

同时：

```math
q\rightarrow\eta q,
```

而：

```math
q_0,A_0
```

保持不变。

每一个 `\eta` 都重新：

```math
\boxed{ \text{求 R02 cubic} \rightarrow U_*(\eta) }
```

而不是冻结 `U`。

然后重建完整局部应力场：

```math
\sigma_x(u,v), \quad \sigma_y(u,v), \quad \tau_{xy}(u,v),
```

计算：

```math
\Phi = \sigma_x^2-\sigma_x\sigma_y+\sigma_y^2 +3\tau^2.
```

在：

- interior stationary roots；
- edge roots；
- corners；

这个有限候选集里求：

```math
\Phi_{\max}.
```

第一个满足：

```math
\sqrt{\Phi_{\max}}=f_y
```

的 `\eta=\eta_y` 被采用。

这正是当前 R06 的正式规则。

---

# 12. 四个 strip 的结果怎样合成一个钢面

对上钢面：

```math
\bar\sigma_y^+ = \sum_i\omega_i^+\sigma_{y,i}^+.
```

对下钢面：

```math
\bar\sigma_y^- = \sum_i\omega_i^-\sigma_{y,i}^-.
```

于是：

```math
N_y^{s+} = t_s\bar\sigma_y^+,
```

```math
N_y^{s-} = t_s\bar\sigma_y^-.
```

如果转换成整个截面轴力：

```math
P_s^+ = -bt_s\bar\sigma_y^+,
```

```math
P_s^- = -bt_s\bar\sigma_y^-.
```

BH050：

```math
bt_s=2500\times4=10000\ {\rm mm^2}.
```

上一轮得到：

```math
\boxed{ P_s^+=2.016\ {\rm MN} }
```

所以对应：

```math
\boxed{ \bar\sigma_y^+ \approx-201.6\ {\rm MPa}. }
```

下钢面：

```math
\boxed{ P_s^-=2.134\ {\rm MN} }
```

因此：

```math
\boxed{ \bar\sigma_y^- \approx-213.4\ {\rm MPa}. }
```

两钢面：

```math
\boxed{ P_s=4.150\ {\rm MN}. }
```

---

# 13. 和 FEM 的 steel force 直接对比

你最新 ODB 截面结果：

```math
P_{\rm FEM}=12.5727\ {\rm MN}.
```

上钢面：

```math
17.29\%
```

所以：

```math
P_{s,FEM}^+ \approx2.174\ {\rm MN}.
```

下钢面：

```math
16.81\%
```

所以：

```math
P_{s,FEM}^- \approx2.114\ {\rm MN}.
```

总钢：

```math
P_{s,FEM}\approx4.289\ {\rm MN}.
```

因此 compatible + Multiwave：

```math
\frac{2.016-2.174}{2.174} \approx-7.3\%,
```

```math
\frac{2.134-2.114}{2.114} \approx+1.0\%,
```

总钢：

```math
\boxed{ \frac{4.150-4.289}{4.289} \approx-3.2\%. }
```

所以我上一轮说“steel force 量级已经基本正确”，就是由这里来的。

---

# 14. 但 global compatible equilibrium 还要满足什么

我们并不是把钢力算完就结束。

对截面 current resultant field 做三个最低 Airy modal projection。

定义：

```math
\langle f\rangle = \frac1\Omega \int_\Omega f\,d\Omega,
```

```math
\mathcal P_\alpha[f] = 2\langle f\cos2\alpha x \rangle,
```

```math
\mathcal P_\beta[f] = 2\langle f\cos2\beta y \rangle.
```

要求：

### 横向膜力

```math
\boxed{ \langle N_x^{sec}\rangle=0 }
```

```math
\boxed{ \mathcal P_\alpha[N_x^{sec}]=0 }
```

```math
\boxed{ \mathcal P_\beta[N_x^{sec}]=n_x. }
```

### 纵向膜力

```math
\boxed{ \langle N_y^{sec}\rangle=-N_0 }
```

```math
\boxed{ \mathcal P_\alpha[N_y^{sec}]=n_y }
```

```math
\boxed{ \mathcal P_\beta[N_y^{sec}]=0. }
```

这里：

```math
N^{sec} = N^U+N^w+N^{s+}+N^{s-}.
```

然后还有 global `q`-virtual-work equation：

```math
\boxed{R_q=0.}
```

所以 fixed `q` 下解出的不是旧 Airy：

```math
P(q) = P_{cr}\frac q{q+q_0}+C_AQ.
```

而是：

```math
\boxed{ P=bN_0 }
```

作为 current equilibrium 的输出。

---

# 15. 上一轮 fixed-`q` 解出来的核心数值

在：

```math
q=0.00516361
```

时，compatible + Multiwave 得：

```math
\boxed{ e_{y0}\approx-0.001238 }
```

这里 `e_{y0}` 就是 longitudinal membrane field 的零阶系数，也就是其面积平均值。

最终：

```math
\boxed{ P=10.1626\ {\rm MN}. }
```

因此：

```math
N_0 = \frac{P}{b} = \frac{10.1626\times10^6}{2500}
```

得到：

```math
\boxed{ N_0\approx4065.0\ {\rm N/mm}. }
```

钢面贡献：

```math
P_s=4.150\ {\rm MN}.
```

因此：

```math
N_y^{steel} = -\frac{4.150\times10^6}{2500}
```

即：

```math
\boxed{ N_y^{steel} \approx-1660\ {\rm N/mm}. }
```

剩余 UHPC+web：

```math
P_{U+w} = 10.1626-4.150 = 6.0126\ {\rm MN}.
```

所以：

```math
\boxed{ N_y^{U+w} \approx-2405\ {\rm N/mm}. }
```

闭合：

```math
1660+2405 \approx4065\ {\rm N/mm}.
```

这一层数值是闭合的。

---

# 16. FEM 对应分解

FEM：

```math
P=12.5727\ {\rm MN},
```

钢：

```math
P_s=4.289\ {\rm MN},
```

所以：

```math
P_{U+w} = 12.5727-4.289 \approx8.284\ {\rm MN}.
```

即：

```math
N_y^{U+w,FEM} \approx -\frac{8.284\times10^6}{2500}
```

得到：

```math
\boxed{ -3313.6\ {\rm N/mm}. }
```

而 compatible + Multiwave 是：

```math
-2405\ {\rm N/mm}.
```

少了约：

```math
\boxed{ 909\ {\rm N/mm} }
```

也就是约：

```math
2.27\ {\rm MN}.
```

这几乎就是总荷载差：

```math
12.573-10.163 = 2.410\ {\rm MN}.
```

所以差额的绝大部分确实不是钢面自身。

是：

```math
\boxed{\text{UHPC+web 没有获得足够的压缩。}}
```

---

# 17. 为什么我怀疑这里存在一个很具体的问题

现在把整个计算链连起来：

```math
q
```

↓

```math
w(q)\Rightarrow\kappa(q)
```

↓

compatible：

```math
\varepsilon^0(x,y)
```

↓

UHPC：

```math
\varepsilon(x,y,z) \rightarrow \sigma_U
```

但钢壳这里却做了：

```math
\boxed{ \varepsilon_s(x,y) \rightarrow \bar\varepsilon_s \rightarrow \text{R02/R06} \rightarrow \bar\sigma_s. }
```

然后这个：

```math
\bar\sigma_s
```

又作为钢壳 contribution 返回 global modal equilibrium。

也就是说：

```math
\boxed{ \text{钢壳这一层丢掉了 global harmonic information。} }
```

更严重的是，qU-off 又令：

```math
\boxed{\Delta=0.}
```

因此局部能量中真正体现：

```math
\text{global }q \leftrightarrow \text{local }U
```

的：

```math
2t_sE_sK_{d\Delta}d\Delta
```

和

```math
t_sE_sK_{\Delta\Delta}\Delta^2
```

全部被删除。

完整 R02 源式明确包含这两项，而且还明确要求局部单元的 `x_0,y_0,\mathrm{face\_sign}`；没有 registration 时不能唯一恢复 GL 项。

---

# 18. 所以上一轮 compatible + Multiwave 实际上并不是这个

正确的理想链应该是：

```math
\varepsilon_s(x,y),q
```

↓

```math
\Pi_s[ U;\varepsilon_s(x,y),q ]
```

↓

同一个能量同时产生：

```math
\boxed{ N_s = \frac{\partial\Pi_s} {\partial\varepsilon} }
```

以及：

```math
\boxed{ R_q^s = \frac{\partial\Pi_s} {\partial q}. }
```

但上一轮实际是：

```math
\boxed{ \bar\varepsilon_s \rightarrow R02/R06 \rightarrow \bar\sigma_s }
```

然后：

```math
\boxed{ N_s\text{ 回去了，} \quad R_q^s\text{ 没有完整回去。} }
```

这就是为什么我上一轮说：

```math
\boxed{ \text{steel force reduction 大致对， 但 local/global work transfer 不闭合。} }
```

---

# 19. 还有一个我现在认为必须一起检查的点：比较位置

你当前最新 FEM 受力占比是：

```math
z/L=0.25
```

截面。

对于 BH050：

```math
m=2,
```

所以：

```math
y=\frac a4
```

正好是第一整体半波的 antinode：

```math
\sin\beta y=1.
```

这一点其实很好，因为：

```math
\kappa_y
```

就在这里达到最大值。

所以如果理论受力分解也是在：

```math
y=a/4
```

做 width resultant，则比较是物理对应的。

但是我上一轮 diagnostic 的 global force balance 中：

```math
P=bN_0
```

是 Airy 的**轴向平均反力**；

而 steel face 那个 `4.150` MN 是由 mean-face Multiwave operator 换算的钢力。

这两个 averaging contract 是否完全和 FEM 的：

```math
y=a/4
```

截面 decomposition 相同，必须重新钉死。

这是第二个可能的问题：

```math
\boxed{ \text{reaction-average quantity} \neq \text{antinode-section component resultant} }
```

不能因为单位都是 MN 就默认等价。

---

# 20. 所以我现在建议我们一起首先盯这四个地方

我不先下结论，你可以一起判断。

**A. 最可疑：**

```math
\boxed{ e_s^\pm(x,y) \rightarrow \bar e_s^\pm }
```

这一步是否根本不该存在？

尤其 compatible Airy 已经恢复二维场之后，为什么 Multiwave 又只吃一个平均 face strain？

---

**B. 第二可疑：**

qU-off：

```math
\boxed{\Delta=0}
```

把：

```math
K_{d\Delta}, \qquad K_{\Delta\Delta}
```

全部删除。

完整 R02 明明规定：

```math
\Delta = s_fb[(q_0+q)U-q_0A_0].
```

所以 local steel 的 `q`-共轭功没有完整进入 global `R_q`。

---

**C. 第三可疑：**

R06 目前做：

```math
e_{\rm face}\rightarrow\eta e_{\rm face}, \qquad q\rightarrow\eta q.
```

这个规则在旧 R4 中是一致的冻结 gate。

但是到了新 compatible theory：

```math
q
```

已经是**真实几何自由度**。

那么为了 local-yield projection 而在钢壳内部使用：

```math
q\rightarrow\eta q
```

是否还具有正确物理意义？

这一条我现在认为也非常值得质疑。

因为全局几何明明是：

```math
q=0.00516361,
```

局部钢壳为了满足 Mises 又偷偷以：

```math
\eta q
```

重建自己的 global-local field。

这可能造成一个钢壳内部使用了“另一个 global curvature”的问题。

---

**D. 第四可疑：**

global reaction `bN_0` 与 FEM `y=a/4` component-section share 的 observable contract 是否严格一致。

---

## 我认为最值得我们先抓的是 C

我上一轮主要盯着 qU generalized work，但现在把整个计算过程完整展开以后，我反而觉得这里出现了一个非常刺眼的问题：

```math
\boxed{ \text{新 compatible theory 已经规定 }q\text{ 是真实几何状态，} }
```

但 R06 仍然沿用旧规则：

```math
\boxed{ q\rightarrow\eta q. }
```

这实际上可能再次制造：

```math
\boxed{ \text{global }q \neq \text{steel local operator 中使用的 }q. }
```

这和刚刚被我们判死的：

```math
\kappa^{R4}\neq\kappa(q)
```

虽然形式不同，但有非常相似的危险。

所以这次把账摊开之后，我现在不会只说“缺 qU generalized work”了。我会把真正需要优先审的三式明确写成：

```math
\boxed{ \text{① }e_s(x,y)\rightarrow\bar e_s }
```

```math
\boxed{ \text{② }\Delta=0 }
```

```math
\boxed{ \text{③ R06 中 }q\rightarrow\eta q }
```

这三步都是**旧 scalar-R4 Multiwave 接口遗留物**，而不是 compatible Airy 本身的必然要求。

我觉得我们现在已经能针对这三步逐个判断了。