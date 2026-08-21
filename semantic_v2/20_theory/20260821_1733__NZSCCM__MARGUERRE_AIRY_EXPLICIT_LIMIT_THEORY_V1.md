# NZ-SCCM — Marguerre–Airy 显式后屈曲 + 显式 N–M 截面极限理论 V1

**时间：2026-08-21 17:33 +08:00**  
**状态：`EXPLICIT_FORMULATION_GATE = PASS`**  
**验证状态：`PREDICTION_BIAS_REPAIR = NOT_STARTED`**  
**身份：项目派生的低阶解析极限承载力理论；不是周思铭、Nguyen、Attard 任一文献的原式照搬。**

---

# 0. 本文件只解决一个问题

本文件不处理 Swartz24 的预测偏差，不拟合参数，不修改材料强度，不用试验荷载选择根。

本文件只回答：

> 当前新路线能否从原始几何/材料参数出发，形成一个没有 Ritz 阶数、没有空间材料点、没有加载步、没有路径追踪、没有正式空间数值积分的有限显式计算理论？

结论：

```text
GEOMETRIC_POSTBUCKLING_EXPLICIT = PASS
Z_SECTION_CAPACITY_EXPLICIT = PASS
RC_SECTION_CAPACITY_EXPLICIT = PASS
FINITE_CONTROL_LOCATION_CANDIDATES = PASS
LOAD_PATH_TRACKING_REQUIRED = NO
RITZ_ORDER_REQUIRED = NO
FORMAL_SPATIAL_QUADRATURE_REQUIRED = NO
SINGLE_ELEMENTARY_CLOSED_FORM_Pu_FOR_ALL_PARAMETERS = NOT_CLAIMED
```

最后一条必须保留：本理论可以化成有限低阶有理/多项式方程和有限候选根集合，但对任意参数并不保证存在一个用初等函数或根式写出的单行 `Pu(raw inputs)`。正式求值允许使用一次性有限代数全根求解；这不等于增量加载、路径追踪或非线性结构迭代。

---

# 1. 来源边界

## 1.1 周思铭来源

仅继承：

- 四边简支正交各向异性板稳定骨架；
- `Dx, Dy, Dxy, Dmu, H=Dxy+Dmu` 的刚度语言；
- Navier 双正弦模态；
- steel-shell 初始刚度的来源公式。

周思铭原文没有给出本文件的后屈曲三次方程或本文件的 Z/RC 极限截面方程。

## 1.2 Nguyen 来源

仅继承：

- 初始缺陷 + 有限面外位移的 von Kármán / 二阶几何思想；
- 普通混凝土峰值应变 `eps0`、初始模量 `E0` 与钢筋双线性材料来源；
- 混凝土压缩上升支采用抛物线形式的来源依据；
- Swartz24 原始几何/材料/钢筋层输入。

Nguyen 的 FE 网格、Gauss 积分、加载步和材料点状态更新不进入本理论。

## 1.3 Marguerre–Airy 部分

Airy 应力函数自动满足膜平衡；单一物理面外模态 + 同模态初始缺陷使兼容方程只产生二倍频膜应力。下面的具体正交各向异性专门化和与截面极限的联立是项目派生。

---

# 2. 适用结构域和原始输入

坐标：

- `x`：板宽方向；
- `y`：轴向加载方向；
- `z`：厚度方向。

完整物理板：

\[
0\le x\le b,\qquad 0\le y\le a_{phys}.
\]

本 V1 的结构域：

1. 四边面外简支；
2. 轴向均匀压缩；
3. 截面对中面对称，故 `B=0`；
4. 正交材料轴与 `(x,y)` 一致，`A16=A26=D16=D26=0`；
5. 采用弹性前端自己选出的整数完整半波数 `m*`；
6. 后屈曲只保留该物理控制模态，不再增加 Ritz 膜内阶数。

原始输入分两类。

### Z steel-shell concrete

\[
\{a_{phys},b,t_c,t_s,\rho_w,E_c^0,E_s,\nu_c^A,\nu_s^A,
\mu_c^Z,\mu_s^Z,f_c,f_y,A_{0,imp}\}.
\]

其中：

- `nu_c^A, nu_s^A`：Marguerre–Airy 面内 plane-stress 刚度参数；当前 Z 基线分别为 0.18、0.30；
- `mu_c^Z, mu_s^Z`：周思铭 steel-shell 初始弯曲/扭转刚度参数；当前分别为 0.20、0.30；
- 二者语义不得混用。

### RC wall plate

\[
\{a_{phys},b,t,E_0,\nu,f_c,\varepsilon_0,E_s,f_y,A_{0,imp},
(a_{x\ell},a_{y\ell},z_\ell)_{\ell=1}^{L}\}.
\]

`a_xl,a_yl` 均为单位板宽内该层两个方向的钢筋面积，单位 mm²/mm = mm。

若输入的是配筋率：

\[
a_{x\ell}=\rho_{x\ell}t,\qquad a_{y\ell}=\rho_{y\ell}t.
\]

Swartz 输入若给总双向配筋率 `rho_s,tot`，当前冻结解释为两方向均分：

\[
\rho_{s,x}=\rho_{s,y}=\frac{\rho_{s,tot}}2,
\]

若有 `L` 个对称层，再按来源层数分配至各层。

---

# 3. 弹性前端：半波数必须由试件自身决定

定义候选轴向波数：

\[
\alpha=\frac{\pi}{b},\qquad
\beta_j=\frac{j\pi}{a_{phys}},\qquad j=1,2,3,\ldots
\]

候选临界膜力：

\[
\boxed{
N_{cr,j}
=
\frac{
D_x\alpha^4+2H\alpha^2\beta_j^2+D_y\beta_j^4
}{\beta_j^2}
}
\]

总轴力：

\[
\boxed{P_{cr,j}=bN_{cr,j}}.
\]

整数控制半波数：

\[
\boxed{m_*=\arg\min_{j\in\mathbb N^+}P_{cr,j}}.
\]

代表完整半波长度：

\[
\boxed{\ell=\frac{a_{phys}}{m_*}},\qquad
\boxed{\beta=\frac{\pi}{\ell}=\frac{m_*\pi}{a_{phys}}}.
\]

初始缺陷无量纲幅值：

\[
\boxed{q_0=\frac{A_{0,imp}}{b}}.
\]

重复半波串联，不把轴力乘 `m*`。

---

# 4. RC 的 A/D 刚度从原始钢筋层显式生成

定义混凝土 plane-stress 常数：

\[
Q_c=\frac{E_0}{1-\nu^2},\qquad
Q_{c12}=\frac{\nu E_0}{1-\nu^2},\qquad
Q_{c66}=\frac{E_0}{2(1+\nu)}.
\]

第 `l` 层总钢筋占据面积：

\[
\boxed{a_\ell=a_{x\ell}+a_{y\ell}}.
\]

为了相体积守恒，钢筋占据的混凝土面积从混凝土相扣除。

## 4.1 面内刚度

\[
\boxed{
A_{11}
=
\frac{E_0}{1-\nu^2}
\left[t-\sum_{\ell=1}^{L}(a_{x\ell}+a_{y\ell})\right]
+E_s\sum_{\ell=1}^{L}a_{x\ell}
}
\]

\[
\boxed{
A_{22}
=
\frac{E_0}{1-\nu^2}
\left[t-\sum_{\ell=1}^{L}(a_{x\ell}+a_{y\ell})\right]
+E_s\sum_{\ell=1}^{L}a_{y\ell}
}
\]

\[
\boxed{
A_{12}
=
\frac{\nu E_0}{1-\nu^2}
\left[t-\sum_{\ell=1}^{L}(a_{x\ell}+a_{y\ell})\right]
}
\]

\[
\boxed{
A_{66}
=
\frac{E_0}{2(1+\nu)}
\left[t-\sum_{\ell=1}^{L}(a_{x\ell}+a_{y\ell})\right]
}
\]

## 4.2 弯曲刚度

忽略钢筋自身截面关于其杆轴中心的微小二次矩，只保留层位置 `z_l²`：

\[
\boxed{
D_x
=
\frac{E_0}{1-\nu^2}
\left[
\frac{t^3}{12}-\sum_{\ell=1}^{L}(a_{x\ell}+a_{y\ell})z_\ell^2
\right]
+E_s\sum_{\ell=1}^{L}a_{x\ell}z_\ell^2
}
\]

\[
\boxed{
D_y
=
\frac{E_0}{1-\nu^2}
\left[
\frac{t^3}{12}-\sum_{\ell=1}^{L}(a_{x\ell}+a_{y\ell})z_\ell^2
\right]
+E_s\sum_{\ell=1}^{L}a_{y\ell}z_\ell^2
}
\]

\[
\boxed{
D_\mu=D_{12}
=
\frac{\nu E_0}{1-\nu^2}
\left[
\frac{t^3}{12}-\sum_{\ell=1}^{L}(a_{x\ell}+a_{y\ell})z_\ell^2
\right]
}
\]

\[
\boxed{
D_{66}
=
\frac{E_0}{2(1+\nu)}
\left[
\frac{t^3}{12}-\sum_{\ell=1}^{L}(a_{x\ell}+a_{y\ell})z_\ell^2
\right]
}
\]

\[
\boxed{H=D_\mu+2D_{66}}.
\]

单层中面钢筋 `z_l=0` 时，自动退化为：

\[
D_x=D_y=H=\frac{E_0t^3}{12(1-\nu^2)}.
\]

---

# 5. Z steel-shell 的弯曲刚度按 Zhou-source 正向生成

定义总厚度：

\[
h=t_c+2t_s,\qquad z_f=\frac{t_c}{2}+\frac{t_s}{2}.
\]

外钢面与核心的整壁截面二次矩：

\[
\boxed{
I_f=2b\left(\frac{t_s^3}{12}+t_sz_f^2\right)
}
\]

\[
\boxed{I_c=\frac{bt_c^3}{12}}.
\]

次方向弯曲刚度：

\[
\boxed{
D_x=\frac{E_sI_f+E_c^0I_c}{b}
}
\]

主方向分项：

\[
\boxed{
D_{y,s}=\frac{E_sI_f+\rho_wE_sI_c}{b}
}
\]

\[
\boxed{
D_{y,c}=\frac{(1-\rho_w)E_c^0I_c}{b}
}
\]

\[
\boxed{D_y=D_{y,s}+D_{y,c}}.
\]

剪切模量：

\[
G_s^Z=\frac{E_s}{2(1+\mu_s^Z)},\qquad
G_c^Z=\frac{E_c^0}{2(1+\mu_c^Z)}.
\]

钢箱中线围成面积：

\[
\boxed{A_\Box=(b-t_s)(h-t_s)}.
\]

薄壁闭口积分：

\[
\boxed{
\oint_s\frac{ds}{t_s}
=
\frac{2[(b-t_s)+(h-t_s)]}{t_s}
}
\]

核心矩形宽厚比：

\[
r_h=\frac{h-2t_s}{b-2t_s}
=\frac{t_c}{b-2t_s}.
\]

Saint-Venant 形状系数：

\[
\boxed{
\beta_{shape}
=
\frac13\left(1-0.63r_h+0.052r_h^5\right)
}
\]

自由扭转刚度：

\[
\boxed{
D_t
=
\frac{4G_s^ZA_\Box^2}
{b\displaystyle\oint_s ds/t_s}
+
\frac{G_c^Z}{b}
\beta_{shape}(b-2t_s)(h-2t_s)^3
}
\]

\[
\boxed{D_{xy}=\frac{D_t}{2}}.
\]

泊松附加刚度：

\[
\boxed{
D_\mu
=
\mu_s^ZD_{y,s}+\mu_c^ZD_{y,c}
}
\]

\[
\boxed{H=D_{xy}+D_\mu}.
\]

---

# 6. Z steel-shell 的 Marguerre 面内 A 刚度显式前端

这一部分是项目派生的 Zhou-compatible extensional companion，不冒充周思铭原式。

使用面内 plane-stress 参数 `nu_c^A,nu_s^A`：

\[
Q_{s11}=Q_{s22}=\frac{E_s}{1-(\nu_s^A)^2},
\]

\[
Q_{s12}=\frac{\nu_s^AE_s}{1-(\nu_s^A)^2},
\qquad
Q_{s66}=\frac{E_s}{2(1+\nu_s^A)},
\]

\[
Q_{c11}=Q_{c22}=\frac{E_c^0}{1-(\nu_c^A)^2},
\]

\[
Q_{c12}=\frac{\nu_c^AE_c^0}{1-(\nu_c^A)^2},
\qquad
Q_{c66}=\frac{E_c^0}{2(1+\nu_c^A)}.
\]

web 等效钢相只沿 `y` 方向增加轴向伸缩刚度：

\[
\boxed{
A_{11}
=
2t_s\frac{E_s}{1-(\nu_s^A)^2}
+(1-\rho_w)t_c\frac{E_c^0}{1-(\nu_c^A)^2}
}
\]

\[
\boxed{
A_{22}
=
2t_s\frac{E_s}{1-(\nu_s^A)^2}
+(1-\rho_w)t_c\frac{E_c^0}{1-(\nu_c^A)^2}
+\rho_wt_cE_s
}
\]

\[
\boxed{
A_{12}
=
2t_s\frac{\nu_s^AE_s}{1-(\nu_s^A)^2}
+(1-\rho_w)t_c\frac{\nu_c^AE_c^0}{1-(\nu_c^A)^2}
}
\]

\[
\boxed{
A_{66}
=
2t_s\frac{E_s}{2(1+\nu_s^A)}
+(1-\rho_w)t_c\frac{E_c^0}{2(1+\nu_c^A)}
}
\]

---

# 7. A 矩阵的逆不再保留为黑盒

由于 `A16=A26=0`，定义：

\[
\boxed{\Delta_A=A_{11}A_{22}-A_{12}^2}.
\]

则：

\[
\boxed{\bar A_{11}=\frac{A_{22}}{\Delta_A}},\qquad
\boxed{\bar A_{22}=\frac{A_{11}}{\Delta_A}},
\]

\[
\boxed{\bar A_{12}=-\frac{A_{12}}{\Delta_A}},\qquad
\boxed{\bar A_{66}=\frac1{A_{66}}}.
\]

后续所有公式可直接消去 `bar A`：

\[
\frac1{\bar A_{11}}=\frac{\Delta_A}{A_{22}},\qquad
\frac1{\bar A_{22}}=\frac{\Delta_A}{A_{11}}.
\]

---

# 8. 单一物理模态与初始缺陷

定义：

\[
\phi(x,y)=\sin(\alpha x)\sin(\beta y).
\]

无应力初始缺陷：

\[
\boxed{w_i=bq_0\phi}.
\]

加载后新增挠曲：

\[
\boxed{w=bq\phi},\qquad q\ge0.
\]

注意：截面弯曲应变来自相对于初始无应力几何的新增曲率，因此后续弯矩需求使用 `q`，而几何膜项使用 `q(q+2q0)`。

---

# 9. Airy 膜平衡与兼容方程完全显式化

Airy 应力函数：

\[
N_x=\theta_{,yy},\qquad
N_y=\theta_{,xx},\qquad
N_{xy}=-\theta_{,xy}.
\]

所以：

\[
N_{x,x}+N_{xy,y}=0,
\qquad
N_{xy,x}+N_{y,y}=0
\]

自动满足。

正交板兼容方程：

\[
\bar A_{22}\theta_{,xxxx}
+(2\bar A_{12}+\bar A_{66})\theta_{,xxyy}
+\bar A_{11}\theta_{,yyyy}
=
\mathcal G(w,w_i).
\]

对当前同模态 `w,wi`，右端精确化为：

\[
\boxed{
\mathcal G
=
\frac12b^2q(q+2q_0)\alpha^2\beta^2
[\cos(2\alpha x)+\cos(2\beta y)]
}.
\]

因此一个精确 Airy 特解为：

\[
\boxed{
\theta_p
=
b^2q(q+2q_0)
\left[
\frac{\beta^2}{16\bar A_{22}\alpha^2}\cos^2(\alpha x)
+
\frac{\alpha^2}{16\bar A_{11}\beta^2}\cos^2(\beta y)
\right]
}
\]

均匀轴压膜力 `N=P/b>0` 的齐次项：

\[
\boxed{\theta_h=-\frac12Nx^2=-\frac12\frac{P}{b}x^2}.
\]

完整：

\[
\boxed{\theta=\theta_h+\theta_p}.
\]

---

# 10. 膜应力重分布直接由 Airy 解得到

加载方向采用压缩为正的局部膜力 `n=-Ny`。

从 `theta` 直接得到：

\[
\boxed{
N_y
=-\frac{P}{b}
-
\frac{\beta^2b^2\Delta_A}{8A_{11}}
q(q+2q_0)\cos(2\alpha x)
}
\]

所以压缩膜力：

\[
\boxed{
n(x;P,q)
=
\frac{P}{b}
+
\frac{\beta^2b^2\Delta_A}{8A_{11}}
q(q+2q_0)\cos(2\alpha x)
}
\]

横向膜力：

\[
\boxed{
N_x
=-
\frac{\alpha^2b^2\Delta_A}{8A_{22}}
q(q+2q_0)\cos(2\beta y)
}
\]

\[
\boxed{N_{xy}=0}.
\]

在一个纵向半波中心 `|sin(beta y)|=1`，定义：

\[
\boxed{s=\sin(\alpha x)},\qquad 0\le s\le1,
\]

因为：

\[
\cos(2\alpha x)=1-2s^2,
\]

所以：

\[
\boxed{
n(s;P,q)
=
\frac{P}{b}
+Gq(q+2q_0)(1-2s^2)
}
\]

其中不再隐藏 `G`：

\[
\boxed{
G=\frac{\beta^2b^2(A_{11}A_{22}-A_{12}^2)}{8A_{11}}
}.
\]

---

# 11. 面外 Galerkin 平衡严格降为三次

定义：

\[
\boxed{
K_b
=
D_x\alpha^4+2H\alpha^2\beta^2+D_y\beta^4
}
\]

\[
\boxed{
K_m
=
\frac{\Delta_A}{16}
\left(
\frac{\alpha^4}{A_{22}}+
\frac{\beta^4}{A_{11}}
\right)
}.
\]

精确三角投影后：

\[
\boxed{
K_mb^3q(q+q_0)(q+2q_0)
+K_bbq
-\frac{P}{b}\beta^2b(q+q_0)=0
}
\]

整理：

\[
\boxed{
P(q)
=
\frac{bK_b}{\beta^2}\frac{q}{q+q_0}
+
\frac{b^3K_m}{\beta^2}q(q+2q_0)
}.
\]

定义两个完全可回代的系数：

\[
\boxed{
P_{cr}
=
\frac{b}{\beta^2}
[D_x\alpha^4+2H\alpha^2\beta^2+D_y\beta^4]
}
\]

\[
\boxed{
C
=
\frac{b^3(A_{11}A_{22}-A_{12}^2)}{16\beta^2}
\left(
\frac{\alpha^4}{A_{22}}+
\frac{\beta^4}{A_{11}}
\right)
}
\]

最终：

\[
\boxed{
P_{pb}(q)
=
P_{cr}\frac{q}{q+q_0}
+Cq(q+2q_0)
}.
\]

等价三次：

\[
\boxed{
Cq^3+3Cq_0q^2+(2Cq_0^2+P_{cr}-P)q-Pq_0=0
}.
\]

---

# 12. 关键证明：这里不需要“路径追踪”

对 `q>=0,q0>0,Pcr>0,C>0`：

\[
\boxed{
\frac{dP_{pb}}{dq}
=
\frac{P_{cr}q_0}{(q+q_0)^2}
+2C(q+q_0)
>0
}.
\]

因此：

\[
\boxed{q\leftrightarrow P_{pb}(q)\text{ 在物理域内一一对应}}.
\]

这意味着正式极限计算不需要从小荷载逐步推进，也不需要寻找“路径尽头”。

所有截面极限候选可以直接代入同一个显式 `P_pb(q)`，一次性求全部有限代数根，然后按无试验信息的 admissibility 规则选最小正 `q`。

---

# 13. 当前局部弯矩需求也显式

在纵向半波中心，加载方向弯矩增量：

\[
\boxed{
m(s;q)=Jqs}
\]

其中：

\[
\boxed{
J=b(D_\mu\alpha^2+D_y\beta^2)
}.
\]

- RC：`Dmu=D12`，按第 4 节生成；
- Z：`Dmu` 使用第 5 节 Zhou-source 公式。

至此结构需求完全由 `q,s` 决定：

\[
\boxed{
P=P_{pb}(q),
}
\]

\[
\boxed{
n(s;q)
=
\frac{P_{pb}(q)}{b}
+Gq(q+2q_0)(1-2s^2),
}
\]

\[
\boxed{m(s;q)=Jqs}.
\]

---

# 14. Z steel-shell 显式 N–M 容量

单位板宽，定义：

\[
h_c=\frac{t_c}{2},\qquad
z_f=h_c+\frac{t_s}{2}.
\]

有效混凝土压缩强度密度：

\[
\boxed{a_c=(1-\rho_w)f_c}.
\]

core 全压、web 全压、两面板一压一拉时：

\[
\boxed{
N_0=[(1-\rho_w)f_c+\rho_wf_y]t_c
}.
\]

全截面 squash：

\[
\boxed{
N_p=[(1-\rho_w)f_c+\rho_wf_y]t_c+2f_yt_s
}.
\]

## 14.1 Regime A：`0 <= n <= N0`

中性轴位于 core：

\[
\boxed{
z_n
=
\frac{(1-\rho_w)f_ch_c-n}
{(1-\rho_w)f_c+2\rho_wf_y}
}.
\]

截面塑性弯矩：

\[
\boxed{
\begin{aligned}
m_u^{A}(n)
={}&
\frac{(1-\rho_w)f_c+2\rho_wf_y}{2}h_c^2\\
&-\frac{[(1-\rho_w)f_ch_c-n]^2}
{2[(1-\rho_w)f_c+2\rho_wf_y]}\\
&+2f_yt_s\left(h_c+\frac{t_s}{2}\right).
\end{aligned}
}
\]

这是 `n` 的二次式。

## 14.2 Regime B：`N0 <= n <= Np`

低压侧面板的反号厚度：

\[
\boxed{
\delta
=
\frac{N_p-n}{2f_y}
}.
\]

\[
\boxed{
m_u^{B}(n)
=
f_y\delta[2(h_c+t_s)-\delta]}
\]

完全代回：

\[
\boxed{
\begin{aligned}
m_u^{B}(n)
={}&
\frac{N_p-n}{2}
\left[
2(h_c+t_s)-\frac{N_p-n}{2f_y}
\right].
\end{aligned}
}
\]

同样是 `n` 的二次式。

若 `n>Np`，直接为 squash failure。

---

# 15. Z 的控制位置也是有限代数问题

对任一固定强度 regime，写：

\[
m_u(n)=u_2n^2+u_1n+u_0.
\]

其系数并非黑盒：

### Regime A

\[
\boxed{
u_2^A=-\frac1{2[(1-\rho_w)f_c+2\rho_wf_y]}}
\]

\[
\boxed{
u_1^A=\frac{(1-\rho_w)f_ch_c}
{(1-\rho_w)f_c+2\rho_wf_y}}
\]

\[
\boxed{
\begin{aligned}
u_0^A={}&
\frac{[(1-\rho_w)f_c+2\rho_wf_y]h_c^2}{2}\\
&-\frac{[(1-\rho_w)f_ch_c]^2}
{2[(1-\rho_w)f_c+2\rho_wf_y]}\\
&+2f_yt_s\left(h_c+\frac{t_s}{2}\right).
\end{aligned}
}
\]

### Regime B

直接由第 14.2 节展开，或保留完全显式的 `Np` 代回式；`Np` 已由原始参数给出。

定义：

\[
Q(q)=q(q+2q_0),
\]

\[
n_a(q)=\frac{P_{pb}(q)}b+GQ(q),
\qquad
n_b(q)=2GQ(q).
\]

于是：

\[
\boxed{n(s;q)=n_a(q)-n_b(q)s^2}.
\]

容量裕度：

\[
\Phi_Z(s,q)=m_u[n(s;q)]-Jqs.
\]

在固定 regime：

\[
\boxed{
\Phi_Z
=A_4s^4+A_2s^2+A_1s+A_0
}
\]

其中：

\[
\boxed{A_4=u_2n_b^2}
\]

\[
\boxed{A_2=-2u_2n_an_b-u_1n_b}
\]

\[
\boxed{A_1=-Jq}
\]

\[
\boxed{A_0=u_2n_a^2+u_1n_a+u_0}.
\]

内部控制点：

\[
\boxed{
4A_4s^3+2A_2s+A_1=0
}.
\]

因此 Z 的完整有限候选集合只有：

1. `s=0`；
2. `s=1`；
3. 上述三次式在 `(0,1)` 的全部实根；
4. `n(s,q)=N0` 的 regime 边界；
5. `n(s,q)=Np` 的 squash 边界。

对每个候选联立 `Phi_Z=0`，一次性求全部正根。不存在空间网格或空间搜索。

---

# 16. RC 显式 N–M 容量：从 Nguyen 型抛物线压缩上升支直接积分

取当前弯矩符号对应的一侧为受压面。

\[
h=\frac t2.
\]

从受压面向内量深度 `y`，中性轴深度 `c>0`。

平截面应变：

\[
\boxed{
\varepsilon_c(y)=\varepsilon_0\left(1-\frac yc\right)
}.
\]

在混凝土受压区：

\[
\boxed{
\sigma_c(y)
=f_c\left[2\frac{\varepsilon_c}{\varepsilon_0}
-\left(\frac{\varepsilon_c}{\varepsilon_0}\right)^2\right]
=f_c\left[1-\left(\frac yc\right)^2\right]
}.
\]

混凝土拉区取零。

第 `l` 层：

\[
\boxed{y_\ell=h-z_\ell}.
\]

钢筋应变：

\[
\boxed{
\varepsilon_{s\ell}
=\varepsilon_0\left(1-\frac{y_\ell}{c}\right)
}.
\]

钢筋：

\[
\boxed{
\sigma_{s\ell}(c)
=
\operatorname{clip}
\left[
E_s\varepsilon_0\left(1-\frac{y_\ell}{c}\right),
-f_y,+f_y
\right]
}.
\]

注意：只有 `y` 向钢筋面积 `a_yl` 直接承担轴向 `N,M`；两个方向钢筋都占据混凝土体积，因此混凝土扣除使用 `a_xl+a_yl`。

---

# 17. RC Gross concrete 积分已经完全闭式

## 17.1 中性轴在板内 `0<c<=t`

\[
\boxed{
N_c^g(c)=\frac23f_cc
}
\]

\[
\boxed{
M_c^g(c)=\frac23f_chc-\frac14f_cc^2
}
\]

## 17.2 中性轴在板外 `c>=t`

\[
\boxed{
N_c^g(c)=f_c\left(t-\frac{t^3}{3c^2}\right)
}
\]

\[
\boxed{
M_c^g(c)=\frac{f_ct^4}{12c^2}
}
\]

没有截面数值积分。

---

# 18. RC 相体积守恒后的完整截面容量

定义受压混凝土中实际被钢筋占据的层集合：

- 若 `c<t`：只包含 `y_l<c` 的层；
- 若 `c>=t`：所有层均在受压混凝土厚度内。

不把该集合当黑盒；每个层的进入边界就是显式条件 `c=y_l`。

对每个 `y_l<c`：

\[
\boxed{
\sigma_{c\ell}(c)
=f_c\left(1-\frac{y_\ell^2}{c^2}\right)
}.
\]

完整轴力容量：

\[
\boxed{
\begin{aligned}
n_u(c)
={}&N_c^g(c)\\
&-\sum_{y_\ell<c}(a_{x\ell}+a_{y\ell})
 f_c\left(1-\frac{y_\ell^2}{c^2}\right)\\
&+\sum_{\ell=1}^{L}a_{y\ell}\sigma_{s\ell}(c).
\end{aligned}
}
\]

完整弯矩容量：

\[
\boxed{
\begin{aligned}
m_u(c)
={}&M_c^g(c)\\
&-\sum_{y_\ell<c}(a_{x\ell}+a_{y\ell})
 f_c\left(1-\frac{y_\ell^2}{c^2}\right)z_\ell\\
&+\sum_{\ell=1}^{L}a_{y\ell}\sigma_{s\ell}(c)z_\ell.
\end{aligned}
}
\]

这两个式子已经只含原始截面参数与一个中性轴变量 `c`。

---

# 19. RC 钢筋屈服也不需要历史状态机

定义：

\[
\varepsilon_y=\frac{f_y}{E_s},\qquad
r_y=\frac{f_y}{E_s\varepsilon_0}.
\]

每层钢筋状态只由当前 `c` 直接决定：

\[
E_s\varepsilon_0\left(1-\frac{y_\ell}{c}\right)>f_y
\quad\Rightarrow\quad \sigma_{s\ell}=+f_y,
\]

\[
\left|E_s\varepsilon_0\left(1-\frac{y_\ell}{c}\right)\right|\le f_y
\quad\Rightarrow\quad
\sigma_{s\ell}=E_s\varepsilon_0\left(1-\frac{y_\ell}{c}\right),
\]

\[
E_s\varepsilon_0\left(1-\frac{y_\ell}{c}\right)<-f_y
\quad\Rightarrow\quad \sigma_{s\ell}=-f_y.
\]

状态切换的 `c` 值显式为：

\[
\boxed{
c=\frac{y_\ell}{1-r_y}}
\quad(1-r_y>0,\;\text{压屈服边界}),
\]

\[
\boxed{
c=\frac{y_\ell}{1+r_y}}
\quad(\text{拉屈服边界}).
\]

所以钢筋屈服只增加有限个代数 active-set 边界，不需要加载历史。

---

# 20. Swartz 当前主要 elastic-steel branch 的多项式完全展开

这一节不是用 Swartz 结果反标，只是把最常用的 elastic branch 化成显式多项式。

固定一个 `c` 区间，使哪些 `y_l<c` 已知，并且所有 y 向钢筋满足弹性。

定义以下有限求和只是书写缩短；每个量右端已完全给出：

\[
S_0=\sum_{y_\ell<c}(a_{x\ell}+a_{y\ell}),
\]

\[
S_2=\sum_{y_\ell<c}(a_{x\ell}+a_{y\ell})y_\ell^2,
\]

\[
Z_0=\sum_{y_\ell<c}(a_{x\ell}+a_{y\ell})z_\ell,
\]

\[
Z_2=\sum_{y_\ell<c}(a_{x\ell}+a_{y\ell})y_\ell^2z_\ell,
\]

\[
Y_0=\sum_{\ell=1}^{L}a_{y\ell},
\qquad
Y_1=\sum_{\ell=1}^{L}a_{y\ell}y_\ell,
\]

\[
Y_{z0}=\sum_{\ell=1}^{L}a_{y\ell}z_\ell,
\qquad
Y_{zy}=\sum_{\ell=1}^{L}a_{y\ell}y_\ell z_\ell.
\]

## 20.1 `0<c<=t`

\[
\boxed{
\begin{aligned}
n_u(c)
={}&\frac23f_cc-f_cS_0+\frac{f_cS_2}{c^2}\\
&+E_s\varepsilon_0Y_0
-\frac{E_s\varepsilon_0Y_1}{c}.
\end{aligned}
}
\]

\[
\boxed{
\begin{aligned}
m_u(c)
={}&-\frac14f_cc^2+\frac23f_chc\\
&-f_cZ_0+\frac{f_cZ_2}{c^2}\\
&+E_s\varepsilon_0Y_{z0}
-\frac{E_s\varepsilon_0Y_{zy}}{c}.
\end{aligned}
}
\]

与 demand 联立并乘 `c²`：

\[
\boxed{
\begin{aligned}
0={}&\frac23f_cc^3
+[-f_cS_0+E_s\varepsilon_0Y_0-n(s;q)]c^2\\
&-E_s\varepsilon_0Y_1c+f_cS_2.
\end{aligned}
}
\]

这是 `c` 的三次式。

弯矩：

\[
\boxed{
\begin{aligned}
0={}&-\frac14f_cc^4+\frac23f_chc^3\\
&+[-f_cZ_0+E_s\varepsilon_0Y_{z0}-Jqs]c^2\\
&-E_s\varepsilon_0Y_{zy}c+f_cZ_2.
\end{aligned}
}
\]

这是 `c` 的四次式。

## 20.2 `c>=t`

此时所有钢筋层均处于 concrete thickness 内，因此 `S0,S2,Z0,Z2` 对全部层求和。

\[
\boxed{
\begin{aligned}
n_u(c)
={}&f_c(t-S_0)+E_s\varepsilon_0Y_0\\
&-\frac{E_s\varepsilon_0Y_1}{c}
+\frac{f_c(S_2-t^3/3)}{c^2}.
\end{aligned}
}
\]

\[
\boxed{
\begin{aligned}
m_u(c)
={}&-f_cZ_0+E_s\varepsilon_0Y_{z0}\\
&-\frac{E_s\varepsilon_0Y_{zy}}{c}
+\frac{f_c(t^4/12+Z_2)}{c^2}.
\end{aligned}
}
\]

乘 `c²` 后：

\[
\boxed{
\begin{aligned}
0={}&[f_c(t-S_0)+E_s\varepsilon_0Y_0-n(s;q)]c^2\\
&-E_s\varepsilon_0Y_1c
+f_c(S_2-t^3/3).
\end{aligned}
}
\]

以及：

\[
\boxed{
\begin{aligned}
0={}&[-f_cZ_0+E_s\varepsilon_0Y_{z0}-Jqs]c^2\\
&-E_s\varepsilon_0Y_{zy}c
+f_c(t^4/12+Z_2).
\end{aligned}
}
\]

因此是 **二次 + 二次**。

---

# 21. RC 的未知控制位置也可以显式消除“空间搜索”

对于任意给定 `q,s`，局部 demand 为：

\[
n_d(s,q)=n(s;q),\qquad m_d(s,q)=Jqs.
\]

截面容量参数化为：

\[
n_u(c),\qquad m_u(c).
\]

截面接触条件：

\[
\boxed{F_N(q,s,c)=n_d(s,q)-n_u(c)=0}
\]

\[
\boxed{F_M(q,s,c)=Jqs-m_u(c)=0}.
\]

如果控制点在 `0<s<1` 内，必须再满足横向一阶接触条件。

由：

\[
\frac{\partial n_d}{\partial s}
=-4Gq(q+2q_0)s
\]

和隐式关系 `n_d=n_u(c)`，有：

\[
\frac{dc}{ds}
=\frac{n_{d,s}}{n_u'(c)}.
\]

令 `m_u(c(s))-Jqs` 在控制点驻值：

\[
\boxed{
F_S(q,s,c)
=-4Gq(q+2q_0)s\,m_u'(c)
-Jq\,n_u'(c)=0
}.
\]

因此 RC interior control 直接由三个有限代数方程决定：

\[
\boxed{F_N=0,\qquad F_M=0,\qquad F_S=0}.
\]

`P` 已经由 `P_pb(q)` 显式消去。

---

# 22. RC derivative 也完全显式

在 fixed active set 中，直接对第 18 节求导即可。

### `0<c<=t`、elastic steel branch

\[
\boxed{
\begin{aligned}
n_u'(c)
={}&\frac23f_c
+\frac{E_s\varepsilon_0Y_1}{c^2}
-\frac{2f_cS_2}{c^3}.
\end{aligned}
}
\]

\[
\boxed{
\begin{aligned}
m_u'(c)
={}&-\frac12f_cc+\frac23f_ch\\
&+\frac{E_s\varepsilon_0Y_{zy}}{c^2}
-\frac{2f_cZ_2}{c^3}.
\end{aligned}
}
\]

所以 `F_S*c³=0` 最高只含 `c^4`。

### `c>=t`、elastic steel branch

\[
\boxed{
 n_u'(c)
=\frac{E_s\varepsilon_0Y_1}{c^2}
-\frac{2f_c(S_2-t^3/3)}{c^3}
}
\]

\[
\boxed{
 m_u'(c)
=\frac{E_s\varepsilon_0Y_{zy}}{c^2}
-\frac{2f_c(t^4/12+Z_2)}{c^3}
}
\]

所以 `F_S*c³=0` 只是一条关于 `q,s,c` 的有限低阶多项式。

若某钢筋层进入 `±fy`，该层对 `n_u,m_u` 的贡献变成常数，导数反而更简单。

---

# 23. RC 完整有限候选集合

对陌生 RC 试件，不允许预设 `s=1`。

必须一次性建立以下有限候选：

1. `s=0`；
2. `s=1`；
3. interior `F_N=F_M=F_S=0` 的全部实根，且 `0<s<1`；
4. concrete branch boundary `c=t`；
5. 每一层的 concrete occupancy boundary `c=y_l`；
6. 每一层钢筋拉/压屈服边界
   \[
   c=y_l/(1+r_y),\quad c=y_l/(1-r_y)
   \]
   （后者仅在 `1-r_y>0` 时存在）；
7. 任何 `c>0`、钢筋状态、压区状态不满足本 branch 假定的根全部剔除。

这是一个**有限 algebraic active-set enumeration**，不是加载历史状态机。

---

# 24. 最终 root-selection：不再使用“追踪到尽头”

由于第 12 节已证明：

\[
P_{pb}'(q)>0,
\]

所以对所有 finite admissible candidates：

\[
\mathcal Q
=
\{q_k>0:\;q_k\text{ 满足相应的显式接触方程和 branch admissibility}\}.
\]

定义：

\[
\boxed{q_u=\min\mathcal Q}
\]

\[
\boxed{P_u=P_{pb}(q_u)}.
\]

该选择规则只使用试件自己的显式方程，不使用：

- 试验荷载；
- Zhou 对比荷载；
- 历史根；
- 某个目标 `Pu`；
- 荷载路径追踪。

如果 `mathcal Q` 为空，则返回 `NO_ADMISSIBLE_CAPACITY_ROOT_IN_V1_DOMAIN`，而不是改参数或继续扫荷载。

---

# 25. 代数次数门禁

## 25.1 Postbuckling

\[
F_{pb}(P,q)\text{ 对 }q\text{ 为三次。}
\]

但实际求极限时优先直接用显式：

\[
P=P_{pb}(q).
\]

## 25.2 Z section

每个固定强度区间：

- `m_u(n)`：二次；
- `n(s)`：`s²`；
- `Phi_Z(s)`：四次；
- interior stationarity：三次。

固定 `s` 后，把 `P_pb(q)` 代入并乘 `(q+q0)^2`，容量方程关于 `q` 的次数不超过 6。

## 25.3 RC section

当前 elastic-steel branch：

- `c<t`：轴力三次、弯矩四次；
- `c>=t`：轴力二次、弯矩二次；
- interior stationarity 清分母后最高只增加到有限低阶。

钢筋屈服只把部分 `1/c` 项改成常数，不会产生高阶材料展开。

因此：

```text
R10 -> N48 -> CH -> C73 HUNDREDS-DEGREE EXPANSION = REMOVED
RITZ H2/H4/H6/... = REMOVED
SPATIAL GRID = REMOVED
LOAD STEP = REMOVED
```

---

# 26. a_phys/b=2 且 m*=2 时的专用短式

此时：

\[
\ell=b,\qquad \alpha=\beta=\frac\pi b.
\]

于是：

\[
\boxed{
P_{cr}=\frac{\pi^2}{b}(D_x+2H+D_y)
}
\]

\[
\boxed{
C
=
\frac{\pi^2b(A_{11}A_{22}-A_{12}^2)}{16}
\left(\frac1{A_{22}}+\frac1{A_{11}}\right)
}
\]

\[
\boxed{
G
=
\frac{\pi^2(A_{11}A_{22}-A_{12}^2)}{8A_{11}}
}
\]

\[
\boxed{
J=\frac{\pi^2}{b}(D_\mu+D_y)
}
\]

\[
\boxed{
P_{pb}(q)
=P_{cr}\frac{q}{q+q_0}+Cq(q+2q_0)
}
\]

\[
\boxed{
n(s;q)
=
\frac{P_{pb}(q)}b+Gq(q+2q_0)(1-2s^2)
}
\]

\[
\boxed{m(s;q)=Jqs}.
\]

这四式是后续 Z0–Z5 和 Swartz24 的共同结构核心。

---

# 27. 两个从零退化校核

## 27.1 完美板 `q0=0`

\[
P_{pb}(q)=P_{cr}+Cq^2
\quad(q>0).
\]

所以：

\[
\boxed{P-P_{cr}\propto q^2}
\]

为稳定单模态后屈曲硬化。

## 27.2 RC 中面单层钢筋 `z=0`

所有 reinforcement bending terms 为零，因此：

\[
D_x=D_y=H=\frac{E_0t^3}{12(1-\nu^2)}.
\]

Case21 原始参数可恢复已冻结 elastic front-end：

\[
D_x=D_y=H\approx1.2581716558\times10^7\;N\,mm,
\]

物理整板 `a_phys=2440 mm,b=1220 mm` 的整数最小候选为 `m*=2`，代表半波 `ell=1220 mm`。

这只作为公式自洽校核，不使用 Case21 极限荷载。

---

# 28. “显式”在本理论中的严格含义

本 V1 宣称的 `EXPLICIT` 是：

1. 所有结构刚度都由 raw parameters 的有限代数式给出；
2. Airy 函数和膜应力重分布有解析式；
3. 后屈曲平衡有显式 `P_pb(q)`；
4. Z section capacity 是二次 interaction；
5. RC section capacity 是有限分段的有理/多项式式；
6. 控制位置由有限端点/三次驻点/active-set boundary 枚举；
7. 最终 `Pu` 是有限 admissible algebraic root set 中最小正 `q` 的 `P_pb(q)`；
8. 不需要荷载增量、路径 continuation、Ritz 阶数或空间离散。

本 V1 **不**宣称：

> 对任意材料参数、任意层数、任意 active set，总能把 `Pu` 写成一条只有四则运算、根号、三角函数的单行初等函数公式。

因为 Z 固定位置消元后即可出现一般六次多项式，RC 多 active-set 联立消元也可超过四次。Abel–Ruffini 意义下，一般根式闭式没有保证。

这不影响它作为有限显式代数计算理论：正式后端可以使用 polynomial `Root` 对象、resultant/companion all-root 等一次性有限代数求根；禁止用加载历史或试验目标选根。

---

# 29. 当前正式裁决

```text
MARGUERRE_AIRY_EXPLICIT_THEORY_V1 = FORMULATED
RAW_INPUT_TO_A_D = EXPLICIT
AIRY_FIELD = EXPLICIT
POSTBUCKLING_P_OF_q = EXPLICIT
Z_NM_CAPACITY = EXPLICIT
RC_NM_CAPACITY = EXPLICIT
CONTROL_LOCATION = FINITE_ALGEBRAIC
ULTIMATE_ROOT_RULE = FINITE_ALGEBRAIC_MIN_POSITIVE_q
PATH_TRACKING = PROHIBITED_NOT_NEEDED
FORMAL_SPATIAL_QUADRATURE = 0
RITZ_ORDER = NONE
EXPERIMENT_IN_ROOT_SELECTION = 0
PREDICTION_BIAS_REPAIR = NOT_STARTED
```

只有在本文件的显式性通过后，后续才允许讨论 Swartz24 的系统偏差来源；任何偏差研究不得回头破坏上述低阶显式架构，除非先证明该架构本身在独立结构门禁上失效。
