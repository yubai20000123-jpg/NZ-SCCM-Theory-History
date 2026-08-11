# NZ-SCCM 更新版理论推导：材料参数 → 闭式 R10 → N48-C1/MM 通用系数 → Cayley–Hamilton → D15

**日期：2026-08-12**  
**身份：CURRENT PAPER-STYLE DERIVATION**  
**理论边界：R10 材料目标不变；材料编译阶次固定为 48；U/C/T^7 采用 N48-C1；T 采用 N48-C1-CONSTRAINED-MINIMAX；正式结构积分仍为一个连续完整代表半波、零空间数值积分。**

---

# 1 理论基本假定与计算链

当前普通混凝土连续解析理论采用如下计算链：

\[
\boxed{
\text{材料参数}
\rightarrow
\text{闭式 R10 current material operator}
\rightarrow
\{U,C,T,T^7\}
\rightarrow
\text{N48-C1/MM 有限解析表示}
\rightarrow
\text{二维 Cayley--Hamilton 提升}
\rightarrow
\text{连续应力/切线场}
\rightarrow
\text{D15 完整半波精确矩}
}
\tag{1}
\]

式中，R10 表示当前冻结的普通混凝土闭式 current material operator；\(U,C,T,T^7\) 为进入二维 current-map 的四个一维标量材料函数；N48-C1/MM 表示保持 48 阶、严格保持零点函数值及一阶切线锚点的有限解析编译层；Cayley--Hamilton 表示将一维主值函数提升为二维张量函数；D15 表示完整半波有限解析矩收缩引擎。

正式空间积分身份保持

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
ACTIVE_MODE = m=1
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
```

材料坐标上生成 N48 系数所使用的有限材料横坐标不属于结构空间积分点。

---

# 2 基本材料参数与无量纲化

定义普通混凝土基本参数

\[
\boxed{
\kappa=\frac{E_0\varepsilon_0}{f_c}
}
\tag{2}
\]

式中，\(E_0\) 表示混凝土初始弹性模量；\(\varepsilon_0\) 表示参考压缩应变；\(f_c\) 表示当前分析采用的混凝土单轴抗压强度；\(\kappa\) 表示归一化初始切线斜率。

取冻结的归一化拉伸强度尺度

\[
\boxed{\rho=0.1}
\tag{3}
\]

并定义

\[
\boxed{
x_{cr}=\frac{\rho}{\kappa}
}
\tag{4}
\]

\[
\boxed{
\eta=\frac{x_{cr}}{20}
}
\tag{5}
\]

式中，\(\rho\) 表示归一化拉伸强度尺度；\(x_{cr}\) 表示 R10 拉伸特征坐标；\(\eta\) 表示主值正、负部分平滑分离的材料尺度。

---

# 3 物理应变、等效单轴张量与主值

面内物理应变张量写为

\[
\boxed{
\mathbf E=
\begin{bmatrix}
\varepsilon_x & \gamma_{xy}/2\\
\gamma_{xy}/2 & \varepsilon_y
\end{bmatrix}
}
\tag{6}
\]

式中，\(\varepsilon_x\) 与 \(\varepsilon_y\) 分别表示两个板面主坐标方向的正应变；\(\gamma_{xy}\) 表示工程剪应变；\(\mathbf E\) 表示物理面内应变张量。

考虑泊松效应，定义等效单轴应变张量

\[
\boxed{
\mathbf E_u=
\frac{(1-\nu)\mathbf E+\nu\,\operatorname{tr}(\mathbf E)\mathbf I}
{1-\nu^2}
}
\tag{7}
\]

并进一步定义无量纲等效应变张量

\[
\boxed{
\mathbf X=\frac{\mathbf E_u}{\varepsilon_0}
}
\tag{8}
\]

式中，\(\nu\) 表示混凝土泊松比；\(\mathbf I\) 表示二阶单位张量；\(\operatorname{tr}(\cdot)\) 表示张量迹；\(\mathbf X\) 表示进入 current material operator 的无量纲等效单轴张量。

其分量为

\[
X_{11}=\frac{\varepsilon_x+\nu\varepsilon_y}
{(1-\nu^2)\varepsilon_0},
\tag{9}
\]

\[
X_{22}=\frac{\nu\varepsilon_x+\varepsilon_y}
{(1-\nu^2)\varepsilon_0},
\tag{10}
\]

\[
X_{12}=\frac{\gamma_{xy}}
{2(1+\nu)\varepsilon_0}.
\tag{11}
\]

定义

\[
\mu=\frac{X_{11}+X_{22}}{2},
\qquad
\delta=\frac{X_{11}-X_{22}}{2},
\tag{12}
\]

\[
r_X=\sqrt{\delta^2+X_{12}^2},
\tag{13}
\]

则 \(\mathbf X\) 的两个主值为

\[
\boxed{
\lambda_\pm=\mu\pm r_X
}
\tag{14}
\]

式中，\(\mu\) 表示两个主值的均值；\(\delta\) 表示两个法向分量半差；\(r_X\) 表示二维等效应变张量的主值半径；\(\lambda_+\) 与 \(\lambda_-\) 表示当前两个主等效单轴应变坐标。

---

# 4 主值正负部分的闭式平滑分解

定义平滑正部函数

\[
\boxed{
\Pi_\eta(z)=
\frac{z^2\left(\sqrt{z^2+\eta^2}+z\right)}
{2(z^2+\eta^2)}
}
\tag{15}
\]

对每个主值 \(\lambda_i\)（\(i\in\{+,-\}\)），定义压缩与拉伸材料坐标

\[
\boxed{
c_i=\Pi_\eta(-\lambda_i)
}
\tag{16}
\]

\[
\boxed{
t_i=\Pi_\eta(\lambda_i)
}
\tag{17}
\]

式中，\(c_i\) 表示与第 \(i\) 个主值对应的平滑压缩坐标；\(t_i\) 表示对应的平滑拉伸坐标；\(\eta\) 控制零点附近正负部分的平滑过渡尺度。

由于式（15）在零点保持平滑，闭式 R10 在 \(\lambda=0\) 处具有明确的函数值与一阶切线锚点，这些锚点后续直接用于 N48 约束编译。

---

# 5 R10 压缩标量函数

压缩标量定义为

\[
\boxed{
C_i=
\frac{\kappa c_i}
{1+(\kappa-2)c_i+c_i^2}
}
\tag{18}
\]

式中，\(C_i\) 表示第 \(i\) 个主方向的无量纲压缩材料响应；\(c_i\) 为式（16）的平滑压缩坐标；\(\kappa\) 为式（2）的归一化初始斜率。

---

# 6 Foster 源拉伸关系与 R10 材料功闭合

定义拉伸归一化坐标

\[
\boxed{
r=\frac{t}{x_{cr}}
}
\tag{19}
\]

并取

\[
\boxed{
m_t=-\frac{7}{90},\qquad \eta_r=0.05}
\tag{20}
\]

式中，\(t\) 表示一般拉伸材料坐标；\(r\) 表示相对 \(x_{cr}\) 的无量纲拉伸坐标；\(m_t\) 表示 Foster 源拉伸下降段斜率参数；\(\eta_r\) 表示源拉伸转折位置的平滑尺度。

定义平滑转折函数

\[
\boxed{
H(r,r_0)=
\frac12\left[(r-r_0)+\sqrt{(r-r_0)^2+\eta_r^2}\right]
-
\frac12\left[-r_0+\sqrt{r_0^2+\eta_r^2}\right]
}
\tag{21}
\]

式中，\(r_0\) 表示转折位置；\(H(r,r_0)\) 表示从 \(r_0\) 附近平滑激活的铰式函数。

Foster 源拉伸利用函数为

\[
\boxed{
T_{src}(r)=
r+(m_t-1)H(r,1)-m_tH(r,10)
}
\tag{22}
\]

对应的源归一化拉应力为

\[
\boxed{
u_{t,src}(t)=\rho T_{src}(t/x_{cr})
}
\tag{23}
\]

式中，\(T_{src}\) 表示仅用于定义源材料功的 Foster 拉伸利用函数；\(u_{t,src}\) 表示源归一化拉应力。

在保留区间 \(0\le t\le10x_{cr}\) 上定义源材料功

\[
\boxed{
W_{src}
=
\int_0^{10x_{cr}}u_{t,src}(t)\,dt
=
\rho x_{cr}\int_0^{10}T_{src}(r)\,dr
}
\tag{24}
\]

式中，\(W_{src}\) 表示由源材料关系本身确定的无量纲材料功；该量不含结构试验荷载，也不由 \(P_u\) 反标。

---

# 7 R10 拉伸上升支

令

\[
\boxed{
\tau=\frac{t}{x_{cr}},\qquad 0\le\tau\le1
}
\tag{25}
\]

设上升支为五次多项式

\[
 u_1(\tau)=
 b_0+b_1\tau+b_2\tau^2+b_3\tau^3+b_4\tau^4+b_5\tau^5.
\tag{26}
\]

式中，\(u_1\) 表示 R10 拉伸上升支的无量纲应力；\(b_0\sim b_5\) 表示待由端点条件确定的五次多项式系数。

在 \(\tau=0\) 处施加

\[
 u_1(0)=0,
\qquad
\frac{du_1}{dt}(0)=\kappa,
\qquad
\frac{d^2u_1}{dt^2}(0)=0,
\tag{27}
\]

在 \(\tau=1\) 处施加

\[
 u_1(1)=h,
\qquad
u'_{1,\tau}(1)=0,
\qquad
u''_{1,\tau}(1)=0.
\tag{28}
\]

式中，\(h\) 表示 R10 拉伸峰值；\(u'_{1,\tau}\) 与 \(u''_{1,\tau}\) 分别表示对 \(\tau\) 的一阶和二阶导数。

由

\[
\kappa x_{cr}=\rho
\tag{29}
\]

可得

\[
 b_0=0,\qquad b_1=\rho,\qquad b_2=0,
\tag{30}
\]

以及

\[
\boxed{
 b_3=10h-6\rho
}
\tag{31}
\]

\[
\boxed{
 b_4=8\rho-15h
}
\tag{32}
\]

\[
\boxed{
 b_5=6h-3\rho
}
\tag{33}
\]

因此 R10 上升支写成

\[
\boxed{
 u_1(\tau)=
 \rho\tau
 +(10h-6\rho)\tau^3
 +(8\rho-15h)\tau^4
 +(6h-3\rho)\tau^5
}
\tag{34}
\]

式中，各系数均由 \(h\) 与 \(\rho\) 直接给出，不需要另列长小数系数表。

---

# 8 R10 拉伸下降支

当 \(x_{cr}\le t\le10x_{cr}\) 时，定义

\[
\boxed{
 s=\frac{t-x_{cr}}{9x_{cr}},\qquad0\le s\le1
}
\tag{35}
\]

取冻结残余拉伸水平 \(u_r\)，当前

\[
\boxed{u_r=0.03}
\tag{36}
\]

下降支采用唯一满足两端函数值、一阶导数和二阶导数连续的五次 smoothstep：

\[
\boxed{
 u_2(s)=
 h+(u_r-h)(10s^3-15s^4+6s^5)
}
\tag{37}
\]

式中，\(u_2\) 表示 R10 拉伸下降支；\(s\) 为下降支局部坐标；\(u_r\) 表示残余拉伸水平。

---

# 9 由材料功确定 R10 峰值 h

上升支材料功为

\[
\boxed{
\int_0^{x_{cr}}u_1(t)\,dt
=
x_{cr}\left(\frac{h}{2}+\frac{\rho}{10}\right)
}
\tag{38}
\]

下降支材料功为

\[
\boxed{
\int_{x_{cr}}^{10x_{cr}}u_2(t)\,dt
=
\frac{9x_{cr}}{2}(h+u_r)
}
\tag{39}
\]

由材料功闭合条件

\[
\int_0^{x_{cr}}u_1(t)\,dt
+
\int_{x_{cr}}^{10x_{cr}}u_2(t)\,dt
=W_{src}
\tag{40}
\]

得到

\[
 W_{src}
=
x_{cr}\left(
5h+\frac{\rho}{10}+\frac92u_r
\right),
\tag{41}
\]

从而

\[
\boxed{
 h=
\frac15
\left(
\frac{W_{src}}{x_{cr}}
-\frac{\rho}{10}
-\frac92u_r
\right)
}
\tag{42}
\]

式中，\(h\) 完全由材料源函数功 \(W_{src}\)、\(x_{cr}\)、\(\rho\) 与 \(u_r\) 决定，不含结构试验结果。

---

# 10 完整 R10 拉伸标量与 current master

定义完整拉伸标量

\[
\boxed{
 u_{sm}(t)=
\begin{cases}
 u_1(t/x_{cr}), & 0\le t\le x_{cr},\\
 u_2[(t-x_{cr})/(9x_{cr})], & x_{cr}<t\le10x_{cr},\\
 u_r, & t>10x_{cr}.
\end{cases}
}
\tag{43}
\]

归一化拉伸利用函数定义为

\[
\boxed{
T_i=\frac{u_{sm}(t_i)}{\rho}
}
\tag{44}
\]

式中，\(T_i\) 表示第 \(i\) 个主方向的归一化 R10 拉伸利用函数。

随后定义 current master

\[
\boxed{
U_i
=
\kappa\lambda_i
-C_i
+\kappa c_i
+\rho T_i
-\kappa t_i
}
\tag{45}
\]

式中，\(U_i\) 表示在第 \(i\) 个主值 \(\lambda_i\) 上的统一一维 current master；\(C_i\) 与 \(T_i\) 分别表示压缩与拉伸分支的材料贡献。

---

# 11 二维主应力 current-map

保留原二维双压、拉压和双拉相互作用，定义

\[
\boxed{
 s_+
=
U_+
-a_{cc}C_+^2C_-
+C_+T_-
-\rho a_tT_+T_-^8
}
\tag{46}
\]

\[
\boxed{
 s_-
=
U_-
-a_{cc}C_-^2C_+
+C_-T_+
-\rho a_tT_-T_+^8
}
\tag{47}
\]

其中

\[
\boxed{
 a_t=1-2^{-1/8}
}
\tag{48}
\]

式中，\(s_+\) 与 \(s_-\) 表示两个主方向的无量纲主应力；\(a_{cc}\) 表示冻结的双压相互作用系数；\(a_t\) 表示双拉相互作用系数；\(C_+^2C_-\) 与 \(C_-^2C_+\) 表示双压相互作用；\(C_+T_-\) 与 \(C_-T_+\) 表示拉压相互作用；\(T_+T_-^8\) 与 \(T_-T_+^8\) 表示双拉相互作用。

物理应力张量最终由

\[
\boxed{
\boldsymbol\sigma=f_c\mathbf S
}
\tag{49}
\]

得到。

式中，\(\mathbf S\) 表示二维无量纲 current stress tensor；\(\boldsymbol\sigma\) 表示物理应力张量。

---

# 12 R10 在零点的精确 C1 锚点

由式（15）至式（45）可得 R10 的零点锚点

\[
\boxed{
U(0)=0,
\qquad
U'(0)=\kappa
}
\tag{50}
\]

以及

\[
\boxed{
C(0)=T(0)=T^7(0)=0
}
\tag{51}
\]

\[
\boxed{
C'(0)=T'(0)=(T^7)'(0)=0
}
\tag{52}
\]

式中，\((\cdot)'\) 表示对主材料坐标 \(\lambda\) 的一阶导数；\(T^7\) 表示标量函数 \([T(\lambda)]^7\)，它作为独立 primitive 直接编译，而不是先截断 \(T\) 再做七次幂。

式（50）至式（52）是更新后 N48 编译层必须严格保持的材料 C1 条件。

---

# 13 N48 材料坐标及第一类 Chebyshev 基

在某一板件当前需要覆盖的主材料坐标区间

\[
\lambda\in[\lambda_a,\lambda_b]
\tag{53}
\]

上定义

\[
\boxed{
\lambda_c=\frac{\lambda_a+\lambda_b}{2},
\qquad
\lambda_h=\frac{\lambda_b-\lambda_a}{2}
}
\tag{54}
\]

\[
\boxed{
\xi(\lambda)=\frac{\lambda-\lambda_c}{\lambda_h}
\in[-1,1]
}
\tag{55}
\]

式中，\(\lambda_a\) 与 \(\lambda_b\) 分别表示当前材料 compiler 区间下限与上限；\(\lambda_c\) 表示区间中心；\(\lambda_h\) 表示区间半宽；\(\xi\) 表示标准化 Chebyshev 材料坐标。

为避免与材料拉伸函数 \(T\) 混淆，将第一类 Chebyshev 多项式记为

\[
\boxed{
\mathcal C_n(\xi)=\cos[n\arccos(\xi)]
}
\tag{56}
\]

满足

\[
\mathcal C_0=1,
\qquad
\mathcal C_1=\xi,
\tag{57}
\]

\[
\boxed{
\mathcal C_{n+1}=2\xi\mathcal C_n-\mathcal C_{n-1}
}
\tag{58}
\]

式中，\(n\) 表示材料解析阶次；当前固定 \(0\le n\le48\)。

---

# 14 旧 direct N48 通用系数公式

取 \(\mathcal C_{49}\) 的 49 个根

\[
\boxed{
\theta_j=\frac{(j+\tfrac12)\pi}{49},
\qquad j=0,1,\ldots,48
}
\tag{59}
\]

并定义材料横坐标

\[
\boxed{
\lambda_j=\lambda_c+\lambda_h\cos\theta_j
}
\tag{60}
\]

式中，\(\theta_j\) 表示第 \(j\) 个 Chebyshev 根角度；\(\lambda_j\) 表示对应的材料坐标。它们仅用于生成材料解析系数，不是结构空间积分点。

对任意

\[
F\in\{U,C,T,T^7\}
\tag{61}
\]

旧 direct N48 系数为

\[
\boxed{
 a_n^{(F,0)}
=
\frac{2-\delta_{n0}}{49}
\sum_{j=0}^{48}
F(\lambda_j)\cos(n\theta_j),
\quad n=0,\ldots,48
}
\tag{62}
\]

式中，\(a_n^{(F,0)}\) 表示旧 direct N48 的第 \(n\) 阶系数；\(\delta_{n0}\) 表示 Kronecker delta，当 \(n=0\) 时取1，否则取0。

对应旧表示为

\[
F_{48}^{(0)}(\lambda)
=
\sum_{n=0}^{48}
a_n^{(F,0)}\mathcal C_n[\xi(\lambda)].
\tag{63}
\]

式（62）保留为 N48-C1 的基础系数公式，但不再单独作为最终 production compiler，因为其一阶切线不保持式（50）至式（52）的 R10 锚点。

---

# 15 N48-C1：严格函数值—一阶切线约束修正

定义 49×49 材料基矩阵

\[
\boxed{
V_{jn}=\mathcal C_n(\xi_j)=\cos(n\theta_j)
}
\tag{64}
\]

式中，\(V\) 表示 49 个材料横坐标与 49 个 Chebyshev 基函数之间的值映射矩阵；\(\xi_j=\cos\theta_j\)。

由于这些横坐标为 Chebyshev 根点，具有

\[
\boxed{
\mathbf H=V^TV
=
\operatorname{diag}
\left(
49,\frac{49}{2},\ldots,\frac{49}{2}
\right)
}
\tag{65}
\]

从而

\[
\boxed{
\mathbf H^{-1}
=
\frac1{49}
\operatorname{diag}(1,2,\ldots,2)
}
\tag{66}
\]

式中，\(\mathbf H\) 表示材料节点最小二乘的 Gram 矩阵。

在 \(\lambda=0\) 处定义

\[
\boxed{
\xi_0=-\frac{\lambda_c}{\lambda_h}
}
\tag{67}
\]

构造函数值/一阶导数约束矩阵

\[
\boxed{
\mathbf G=
\begin{bmatrix}
\mathcal C_0(\xi_0)&\cdots&\mathcal C_{48}(\xi_0)\\
\lambda_h^{-1}\mathcal C'_0(\xi_0)&\cdots&
\lambda_h^{-1}\mathcal C'_{48}(\xi_0)
\end{bmatrix}
}
\tag{68}
\]

式中，\(\mathbf G\) 表示将 49 个系数映射到 \(\lambda=0\) 的函数值和一阶材料切线的 2×49 约束矩阵；\(\mathcal C'_n\) 表示第一类 Chebyshev 多项式对 \(\xi\) 的导数。

四个 primitive 的目标向量为

\[
\boxed{
\mathbf d_U=
\begin{bmatrix}
0\\\kappa
\end{bmatrix}
}
\tag{69}
\]

\[
\boxed{
\mathbf d_C
=
\mathbf d_T
=
\mathbf d_{T^7}
=
\begin{bmatrix}
0\\0
\end{bmatrix}
}
\tag{70}
\]

式中，\(\mathbf d_F\) 表示第 \(F\) 个 primitive 在 \(\lambda=0\) 应严格满足的 R10 函数值与一阶导数。

对旧 direct 系数向量

\[
\mathbf a^{(F,0)}=
[a_0^{(F,0)},a_1^{(F,0)},\ldots,a_{48}^{(F,0)}]^T
\tag{71}
\]

施加最小节点扰动的 C1 约束，得到显式修正式

\[
\boxed{
\mathbf a^{(F,C1)}
=
\mathbf a^{(F,0)}
+
\mathbf H^{-1}\mathbf G^T
\left(
\mathbf G\mathbf H^{-1}\mathbf G^T
\right)^{-1}
\left(
\mathbf d_F-\mathbf G\mathbf a^{(F,0)}
\right)
}
\tag{72}
\]

式中，\(\mathbf a^{(F,C1)}\) 表示严格保持 R10 零点函数值及一阶切线的 48 阶系数向量。由于括号内只需逆一个 2×2 矩阵，式（72）保持了低复杂度和可手算审计性。

当前

\[
\boxed{
F\in\{U,C,T^7\}
\Rightarrow
\mathbf a^{(F,*)}=\mathbf a^{(F,C1)}
}
\tag{73}
\]

式中，上标 \((*)\) 表示当前正式使用的更新后 N48 系数身份。

---

# 16 T primitive 的 N48-C1 constrained-minimax 更新

由于 R10 的 \(T\) 在 \(\lambda\approx0\) 存在很窄的拉伸边界层，单纯式（72）的最小节点扰动虽然能精确保持 C1 锚点，但会牺牲较多 \(T\) 的函数值精度。因此只对 \(T\) 进一步使用严格 C1 约束下的全域最小极大表示。

定义

\[
\boxed{
T_{48}^{MM}(\lambda)
=
\sum_{n=0}^{48}
a_n^{(T,MM)}\mathcal C_n[\xi(\lambda)]
}
\tag{74}
\]

系数向量定义为

\[
\boxed{
\mathbf a^{(T,MM)}
=
\underset{\mathbf a\in\mathbb R^{49}}{\operatorname{argmin}}
\left\|
\sum_{n=0}^{48}a_n\mathcal C_n[\xi(\lambda)]
-T_{R10}(\lambda)
\right\|_{L^\infty([\lambda_a,\lambda_b])}
}
\tag{75}
\]

并严格满足

\[
\boxed{
\mathbf G\mathbf a^{(T,MM)}
=
\begin{bmatrix}0\\0\end{bmatrix}
}
\tag{76}
\]

即

\[
\boxed{
T_{48}^{MM}(0)=0,
\qquad
\left(T_{48}^{MM}\right)'(0)=0
}
\tag{77}
\]

式中，\(\|\cdot\|_{L^\infty}\) 表示整个材料 compiler 区间上的最大绝对误差；\(T_{R10}(\lambda)\) 表示式（44）给出的闭式 R10 拉伸 primitive；\(\mathbf a^{(T,MM)}\) 表示在 48 阶空间内满足严格 C1 锚点的最小极大系数向量。

式（75）可以由 Remez/exchange 或等价连续最小极大后端求得；这些操作只发生在一维材料坐标，不改变最终解析形式。最终结构计算中仍然只有式（74）这一组有限系数。

当前 T 的正式系数身份为

\[
\boxed{
\mathbf a^{(T,*)}=\mathbf a^{(T,MM)}
}
\tag{78}
\]

因此更新后的四个 primitive 统一写为

\[
\boxed{
F_{48}^{*}(\lambda)
=
\sum_{n=0}^{48}
a_n^{(F,*)}
\mathcal C_n[\xi(\lambda)]
}
\tag{79}
\]

其中

\[
\boxed{
\mathbf a^{(F,*)}
=
\begin{cases}
\mathbf a^{(F,C1)},&F\in\{U,C,T^7\},\\
\mathbf a^{(T,MM)},&F=T.
\end{cases}
}
\tag{80}
\]

式（79）和式（80）即为当前更新后 N48 compiler 的统一理论表达。

---

# 17 R10 近零拉伸边界层的身份

为审计而不新增经验尺度，直接使用 R10 自身的 \(\eta\) 定义边界层

\[
\boxed{
\mathcal B_\eta
=
\left\{
\lambda\ge0:
0\le\Pi_\eta(\lambda)\le\eta
\right\}
}
\tag{81}
\]

令 \(\lambda_\eta>0\) 满足

\[
\boxed{
\Pi_\eta(\lambda_\eta)=\eta
}
\tag{82}
\]

式中，\(\mathcal B_\eta\) 表示 R10 自身平滑尺度所定义的近零拉伸边界层；\(\lambda_\eta\) 表示该边界层右端点。当前 24 板材料参数下 \(\lambda_\eta\) 约为 \(3.42\times10^{-3}\)，该量只用于 compiler 审计，不进入结构求解自由度。

---

# 18 一维 N48 primitive 到二维矩阵函数的 Cayley--Hamilton 提升

对当前二维无量纲等效应变张量 \(\mathbf X\)，定义

\[
\boxed{
\mathbf Y
=
\frac{\mathbf X-\lambda_c\mathbf I}{\lambda_h}
}
\tag{83}
\]

式中，\(\mathbf Y\) 表示标准化后的二维材料张量；其两个特征值正好为 \(\xi(\lambda_+)\) 与 \(\xi(\lambda_-)\)。

定义两个二维不变量

\[
\boxed{
K_1=\operatorname{tr}(\mathbf Y),
\qquad
K_2=\det(\mathbf Y)
}
\tag{84}
\]

式中，\(K_1\) 与 \(K_2\) 分别表示 \(\mathbf Y\) 的迹与行列式。

二维 Cayley--Hamilton 恒等式为

\[
\boxed{
\mathbf Y^2-K_1\mathbf Y+K_2\mathbf I=\mathbf0
}
\tag{85}
\]

因此任意阶矩阵 Chebyshev 多项式均可压缩为

\[
\boxed{
\mathcal C_n(\mathbf Y)
=
A_n(K_1,K_2)\mathbf I
+
B_n(K_1,K_2)\mathbf Y
}
\tag{86}
\]

式中，\(A_n\) 与 \(B_n\) 表示第 \(n\) 阶矩阵 Chebyshev 多项式对应的两个标量不变量系数。

初值为

\[
A_0=1,
\quad B_0=0,
\qquad
A_1=0,
\quad B_1=1.
\tag{87}
\]

由式（58）和式（85）得到递推

\[
\boxed{
A_{n+1}=-2K_2B_n-A_{n-1}
}
\tag{88}
\]

\[
\boxed{
B_{n+1}=2A_n+2K_1B_n-B_{n-1}
}
\tag{89}
\]

式中，\(n=1,2,\ldots,47\)。

---

# 19 每一个 N48 系数项如何进入二维 current-map

对任一 primitive \(F\)，第 \(n\) 阶材料项为

\[
\boxed{
\mathbf F_{48}^{(n)}
=
a_n^{(F,*)}\mathcal C_n(\mathbf Y)
}
\tag{90}
\]

将式（86）代入得

\[
\boxed{
\mathbf F_{48}^{(n)}
=
a_n^{(F,*)}A_n\mathbf I
+
a_n^{(F,*)}B_n\mathbf Y
}
\tag{91}
\]

式中，\(a_n^{(F,*)}\) 表示更新后第 \(F\) 个 primitive 的第 \(n\) 阶 N48 系数；式（91）即单个材料系数进入二维 current-map 的最基本形式。

对 \(n=0\sim48\) 求和

\[
\boxed{
\mathbf F_{48}^{*}
=
\sum_{n=0}^{48}\mathbf F_{48}^{(n)}
=
A_F\mathbf I+B_F\mathbf Y
}
\tag{92}
\]

其中

\[
\boxed{
A_F
=
\sum_{n=0}^{48}a_n^{(F,*)}A_n
}
\tag{93}
\]

\[
\boxed{
B_F
=
\sum_{n=0}^{48}a_n^{(F,*)}B_n
}
\tag{94}
\]

式中，\(A_F\) 与 \(B_F\) 表示 primitive \(F\) 经过完整 48 阶求和后的两个二维不变量系数。

因此分别得到

\[
\mathbf U,
\qquad
\mathbf C,
\qquad
\mathbf T,
\qquad
\mathbf T^{(7)}.
\tag{95}
\]

式中，\(\mathbf U\)、\(\mathbf C\)、\(\mathbf T\) 与 \(\mathbf T^{(7)}\) 分别表示四个一维 primitive 经二维谱提升后的矩阵函数。

---

# 20 双压、拉压和双拉项的矩阵重构

二维双压项写为

\[
\boxed{
\mathbf{CC}
=
\det(\mathbf C)\mathbf C
}
\tag{96}
\]

在主坐标系中，式（96）对应

\[
(C_+^2C_-,\ C_-^2C_+).
\]

拉压项写为

\[
\boxed{
\mathbf{TC}
=
\mathbf C
\left[
\operatorname{tr}(\mathbf T)\mathbf I-\mathbf T
\right]
}
\tag{97}
\]

在主坐标系中，式（97）对应

\[
(C_+T_-,\ C_-T_+).
\]

双拉项写为

\[
\boxed{
\mathbf{TT}
=
\det(\mathbf T)
\left[
\operatorname{tr}(\mathbf T^{(7)})\mathbf I
-\mathbf T^{(7)}
\right]
}
\tag{98}
\]

在主坐标系中，式（98）对应

\[
(T_+T_-^8,\ T_-T_+^8).
\]

式中，\(\mathbf{CC}\)、\(\mathbf{TC}\)、\(\mathbf{TT}\) 分别表示双压、拉压和双拉相互作用矩阵。

最终无量纲应力张量为

\[
\boxed{
\mathbf S
=
\mathbf U
-a_{cc}\mathbf{CC}
+\mathbf{TC}
-\rho a_t\mathbf{TT}
}
\tag{99}
\]

物理应力仍由式（49）得到。

---

# 21 N48 解析切线

因为式（79）仍是有限 Chebyshev 多项式，其一阶材料导数为

\[
\boxed{
\frac{dF_{48}^{*}}{d\lambda}
=
\frac1{\lambda_h}
\sum_{n=0}^{48}
a_n^{(F,*)}
\mathcal C'_n[\xi(\lambda)]
}
\tag{100}
\]

式中，\(dF_{48}^{*}/d\lambda\) 表示与函数值完全同源的材料一阶切线；不存在有限差分生产导数。

由于式（72）或式（76）严格约束 \(\lambda=0\) 的函数值和导数，式（100）在零点严格恢复式（50）至式（52）的 R10 C1 锚点。

二维一致切线由

\[
\boxed{
\mathbb D
=
\frac{\partial\boldsymbol\sigma}{\partial\mathbf E}
=
f_c
\frac{\partial\mathbf S}{\partial\mathbf X}
:
\frac{\partial\mathbf X}{\partial\mathbf E}
}
\tag{101}
\]

获得。

式中，\(\mathbb D\) 表示当前二维一致材料切线张量；\(\partial\mathbf S/\partial\mathbf X\) 由式（88）至式（100）解析求导；\(\partial\mathbf X/\partial\mathbf E\) 由式（7）和式（8）直接得到。

---

# 22 连续完整半波坐标与 D15 接口

定义一个连续完整代表半波的无量纲坐标

\[
\boxed{
X=\frac{\pi x}{b},
\qquad
Y=\frac{\pi y}{\ell},
\qquad
\zeta=\frac{2z}{t_p}
}
\tag{102}
\]

其定义域为

\[
0\le X\le\pi,
\qquad
0\le Y\le\pi,
\qquad
-1\le\zeta\le1.
\tag{103}
\]

式中，\(x\) 与 \(y\) 分别表示板面两个物理坐标；\(z\) 表示厚度坐标；\(b\) 表示代表半波横向宽度；\(\ell\) 表示代表半波轴向长度；\(t_p\) 表示混凝土板厚；\(X,Y,\zeta\) 表示 D15 使用的无量纲连续坐标。

物理体积微元为

\[
\boxed{
d\Omega
=J_\Omega\,dX\,dY\,d\zeta,
\qquad
J_\Omega=\frac{b\ell t_p}{2\pi^2}
}
\tag{104}
\]

式中，\(J_\Omega\) 表示物理坐标至完整半波无量纲坐标的 Jacobian。

Nguyen 二阶运动学提供连续应变场

\[
\boxed{
\mathbf E=\mathbf E(X,Y,\zeta;D,q)
}
\tag{105}
\]

从而

\[
\boxed{
\mathbf X=\mathbf X(X,Y,\zeta;D,q)
}
\tag{106}
\]

式中，\(D\) 表示轴向广义压缩变量；\(q=A/b\) 表示局部挠曲无量纲幅值；\(A\) 表示当前局部挠曲幅值。式（105）仍采用项目冻结的 Nguyen 二阶运动学，本轮材料 compiler 更新不修改该运动学。

---

# 23 有限解析空间基与乘法规则

由于式（105）是有限三角—厚度代数，而式（88）至式（99）只包含有限加、乘和二维不变量递推，因此最终待积量仍可写为有限解析系数场

\[
\boxed{
Q(X,Y,\zeta)
=
\sum_{i,j,k}
 c_{ijk}
 \mathcal C_i(\sin X)
 \mathcal C_j(\sin Y)
 \mathcal C_k(\zeta)
}
\tag{107}
\]

式中，\(Q\) 表示任一最终需要积分的解析量，例如 \(S_{yy}\) 或 \(\mathbf S:\mathbf e_{,q}\)；\(c_{ijk}\) 表示有限解析系数；\(i,j,k\) 表示三个方向的有限基函数阶次。

同一变量上的 Chebyshev 乘积严格使用

\[
\boxed{
\mathcal C_m(\chi)\mathcal C_n(\chi)
=
\frac12
\left[
\mathcal C_{m+n}(\chi)
+
\mathcal C_{|m-n|}(\chi)
\right]
}
\tag{108}
\]

式中，\(\chi\) 表示任一标准化解析变量；式（108）使所有 nonlinear current-map 项在系数空间完成有限卷积，而不需要结构空间取点。

---

# 24 单个 N48 材料项如何形成 D15 系数

对第 \(n\) 阶 primitive 项的某一矩阵分量 \((a,b)\)，由式（91）有

\[
F_{ab}^{(n)}
=
a_n^{(F,*)}
\left[
A_n\delta_{ab}+B_nY_{ab}
\right].
\tag{109}
\]

式中，\(\delta_{ab}\) 表示 Kronecker delta；\(Y_{ab}\) 表示标准化材料张量 \(\mathbf Y\) 的第 \((a,b)\) 个分量。

把括号内的有限解析量展开为

\[
\boxed{
A_n\delta_{ab}+B_nY_{ab}
=
\sum_{i,j,k}
\phi_{ijk,ab}^{(F,n)}
\mathcal C_i(\sin X)
\mathcal C_j(\sin Y)
\mathcal C_k(\zeta)
}
\tag{110}
\]

式中，\(\phi_{ijk,ab}^{(F,n)}\) 表示第 \(F\) 个 primitive、第 \(n\) 阶材料项、矩阵分量 \((a,b)\) 在 D15 空间解析基中的系数。

因此第 \(n\) 阶材料系数对空间解析场的贡献为

\[
\boxed{
 c_{ijk,ab}^{(F,n)}
=
a_n^{(F,*)}\phi_{ijk,ab}^{(F,n)}
}
\tag{111}
\]

式中，\(c_{ijk,ab}^{(F,n)}\) 表示第 \(n\) 阶材料系数真正进入 D15 之前的空间解析系数。

这给出了最基本的逐项链：

\[
\boxed{
a_n^{(F,*)}
\rightarrow
(A_n,B_n)
\rightarrow
\phi_{ijk,ab}^{(F,n)}
\rightarrow
c_{ijk,ab}^{(F,n)}
}
\tag{112}
\]

所有双压、拉压和双拉 nonlinear 组合均先通过式（108）在系数空间有限卷积，最终仍得到同类 \(c_{ijk}\) 系数。

---

# 25 D15 完整半波精确矩

定义板面方向基础矩

\[
\boxed{
M_n
=
\int_0^\pi
\mathcal C_n(\sin X)\,dX
}
\tag{113}
\]

其闭式结果为

\[
\boxed{
M_n=
\begin{cases}
\pi, & n=0,\\
\dfrac{2\sin(n\pi/2)}{n}, & n\ge1.
\end{cases}
}
\tag{114}
\]

式中，\(M_n\) 表示完整半波平面方向第 \(n\) 阶 Chebyshev 解析矩。

定义厚度方向基础矩

\[
\boxed{
Z_k
=
\int_{-1}^{1}
\mathcal C_k(\zeta)\,d\zeta
}
\tag{115}
\]

其闭式结果为

\[
\boxed{
Z_k=
\begin{cases}
0, & k\ \text{为奇数},\\
\dfrac{2}{1-k^2}, & k\ \text{为偶数}.
\end{cases}
}
\tag{116}
\]

式中，\(Z_k\) 表示厚度方向第 \(k\) 阶 Chebyshev 解析矩。

因此任意单项

\[
Q_{ijk}
=
c_{ijk}
\mathcal C_i(\sin X)
\mathcal C_j(\sin Y)
\mathcal C_k(\zeta)
\tag{117}
\]

的完整半波积分严格为

\[
\boxed{
\mathscr D[Q_{ijk}]
=
c_{ijk}M_iM_jZ_k
}
\tag{118}
\]

式中，\(\mathscr D[\cdot]\) 表示 D15 完整半波精确矩算子。

总量直接线性叠加为

\[
\boxed{
\mathscr D[Q]
=
\sum_{i,j,k}
c_{ijk}M_iM_jZ_k
}
\tag{119}
\]

式（119）不存在 Gauss、Simpson、自适应积分、空间 collocation 或材料点求和。

---

# 26 从单个 N48 系数直接到 D15 的最终通式

将式（111）代入式（118），第 \(F\) 个 primitive 的第 \(n\) 阶材料系数对矩阵分量 \((a,b)\) 的 D15 贡献为

\[
\boxed{
\mathscr D[F_{ab}^{(n)}]
=
a_n^{(F,*)}
\sum_{i,j,k}
\phi_{ijk,ab}^{(F,n)}
M_iM_jZ_k
}
\tag{120}
\]

式中，\(a_n^{(F,*)}\) 为更新后 N48-C1/MM 材料系数；\(\phi_{ijk,ab}^{(F,n)}\) 为由 Cayley--Hamilton 与 Nguyen 连续运动学共同产生的空间解析系数；\(M_i,M_j,Z_k\) 为 D15 精确矩。

因此更新后的完整逐项理论链最终写为

\[
\boxed{
\text{R10 参数}
\rightarrow
a_n^{(F,*)}
\rightarrow
(A_n,B_n)
\rightarrow
\mathbf F_{48}^{(n)}
\rightarrow
\mathbf S
\rightarrow
c_{ijk}
\rightarrow
c_{ijk}M_iM_jZ_k
}
\tag{121}
\]

式（121）即为“材料参数 → 闭式 R10 → N48 通用系数 → 每一项进入 D15”的最简完整表达。

---

# 27 混凝土轴力的 D15 闭合

把加载方向无量纲应力分量展开为

\[
S_{yy}
=
\sum_{i,j,k}
p_{ijk}
\mathcal C_i(\sin X)
\mathcal C_j(\sin Y)
\mathcal C_k(\zeta),
\tag{122}
\]

式中，\(p_{ijk}\) 表示加载方向无量纲应力 \(S_{yy}\) 的有限解析系数。

轴力为截面力，因此完整半波 D15 形式为

\[
\boxed{
P_c
=
-\frac{f_cb t_p}{2\pi^2}
\sum_{i,j,k}
p_{ijk}M_iM_jZ_k
}
\tag{123}
\]

式中，\(P_c\) 表示混凝土承担的轴向压力；负号用于将压应力对应为正的轴向承载力；\(b\) 与 \(t_p\) 分别表示板宽和板厚。

---

# 28 幅值广义功与 D15 闭合

定义物理归一化应变

\[
\boxed{
\mathbf e
=\frac{\mathbf E}{\varepsilon_0}
=(1+\nu)\mathbf X
-\nu\operatorname{tr}(\mathbf X)\mathbf I
}
\tag{124}
\]

式中，\(\mathbf e\) 表示与物理应力 \(\boldsymbol\sigma\) 共轭的无量纲物理应变张量。

对广义幅值 \(q\) 求导

\[
\boxed{
\mathbf e_{,q}
=\frac{\partial\mathbf e}{\partial q}
}
\tag{125}
\]

幅值广义功密度定义为

\[
\boxed{
Q_q
=
\mathbf S:\mathbf e_{,q}
}
\tag{126}
\]

式中，冒号“:”表示二阶张量双点积；\(Q_q\) 表示混凝土无量纲应力与广义幅值应变增量之间的功共轭密度。

若

\[
Q_q
=
\sum_{i,j,k}
r_{ijk}
\mathcal C_i(\sin X)
\mathcal C_j(\sin Y)
\mathcal C_k(\zeta),
\tag{127}
\]

则混凝土幅值广义残量为

\[
\boxed{
R_{q,c}
=
f_c\varepsilon_0J_\Omega
\sum_{i,j,k}
r_{ijk}M_iM_jZ_k
}
\tag{128}
\]

式中，\(r_{ijk}\) 表示 \(Q_q\) 的有限解析系数；\(R_{q,c}\) 表示混凝土对广义局部幅值 \(q\) 的内部广义力。

---

# 29 同源导数与切线稳定

由于 \(P_c\) 与 \(R_{q,c}\) 均由有限解析系数和固定精确矩组成，因此其导数仍直接对同一解析系数求导：

\[
\boxed{
P_{c,D}
=
-\frac{f_cb t_p}{2\pi^2}
\sum_{i,j,k}
\frac{\partial p_{ijk}}{\partial D}
M_iM_jZ_k
}
\tag{129}
\]

\[
\boxed{
P_{c,q}
=
-\frac{f_cb t_p}{2\pi^2}
\sum_{i,j,k}
\frac{\partial p_{ijk}}{\partial q}
M_iM_jZ_k
}
\tag{130}
\]

\[
\boxed{
R_{q,c,D}
=
f_c\varepsilon_0J_\Omega
\sum_{i,j,k}
\frac{\partial r_{ijk}}{\partial D}
M_iM_jZ_k
}
\tag{131}
\]

\[
\boxed{
R_{q,c,q}
=
f_c\varepsilon_0J_\Omega
\sum_{i,j,k}
\frac{\partial r_{ijk}}{\partial q}
M_iM_jZ_k
}
\tag{132}
\]

式中，\(D\) 与 \(q\) 分别表示两个全局广义变量；所有导数来自同一 N48-C1/MM current-map，不使用有限差分生产导数。

---

# 30 周思铭式 Dx--Dy--H 切线稳定验收门

为了像周思铭正交各向异性板稳定理论那样明确检查不同方向刚度对轴压稳定的贡献，将当前二维一致切线按板稳定语言投影为

\[
\boxed{
D_x=\frac{t_p^3}{12}C_{xx,t}
}
\tag{133}
\]

\[
\boxed{
D_y=\frac{t_p^3}{12}C_{yy,t}
}
\tag{134}
\]

\[
\boxed{
D_{\mu,\mathrm{eff}}
=\frac{t_p^3}{24}
(C_{xy,t}+C_{yx,t})
}
\tag{135}
\]

\[
\boxed{
D_{66}=\frac{t_p^3}{12}G_t
}
\tag{136}
\]

并定义

\[
\boxed{
H_{\mathrm{eff}}
=D_{\mu,\mathrm{eff}}+2D_{66}
}
\tag{137}
\]

式中，\(C_{xx,t}\)、\(C_{yy,t}\) 表示当前两个法向方向的材料切线；\(C_{xy,t}\)、\(C_{yx,t}\) 表示法向耦合切线；\(G_t\) 表示当前剪切切线；\(D_x,D_y\) 分别表示两个板面方向的等效切线弯曲刚度；\(D_{\mu,\mathrm{eff}}\) 表示泊松/法向耦合对应的等效扭转刚度；\(D_{66}\) 表示剪切对应的扭转刚度；\(H_{\mathrm{eff}}\) 表示进入 Navier 正交各向异性稳定方程的综合扭转刚度。

对于单完整代表半波，令

\[
\alpha=\frac{\pi}{b},
\qquad
\beta=\frac{\pi}{\ell},
\tag{138}
\]

则 Zhou/Navier 形式的切线稳定组合写为

\[
\boxed{
N_{y,cr}^{Z}
=
\frac{
D_x\alpha^4
+2H_{\mathrm{eff}}\alpha^2\beta^2
+D_y\beta^4
}{\beta^2}
}
\tag{139}
\]

式中，\(\alpha\) 与 \(\beta\) 分别表示完整半波两个方向的 Navier 波数；\(N_{y,cr}^{Z}\) 表示用于 compiler tangent fidelity 审计的 Zhou/Navier 正交各向异性临界膜力组合。

式（133）至式（139）只作为更新后 N48 切线是否忠实恢复 R10 的稳定性验收门，不替代当前完整 nonlinear \(P,R_q,L\) 求解体系。

---

# 31 更新后 N48-C1/MM 的理论身份

当前 compiler 正式身份归纳为

```text
R10_MATERIAL_TARGET = FROZEN
MATERIAL_COMPILER_ORDER = 48

U_COMPILER  = N48-C1
C_COMPILER  = N48-C1
T7_COMPILER = N48-C1
T_COMPILER  = N48-C1-CONSTRAINED-MINIMAX

R10_VALUE_ANCHOR_GATE = PASS
R10_FIRST_TANGENT_GATE = PASS
NEAR_ZERO_T_VALUE_GATE = PASS
O1_COEFFICIENT_GATE = PASS
CAYLEY_HAMILTON_COMPATIBILITY = PASS
D15_COMPATIBILITY = PASS
ZHOU_Dx_Dy_H_GATE = PASS
FORMAL_SPATIAL_QUADRATURE = 0
```

同时保留如下表示能力边界：

```text
N48_STRICT_C1_FULL_HULL_DIRECT_VALUE_LEVEL = NOT_FULLY_RECOVERED
```

该边界只说明单一全域 48 阶多项式在严格 C1 条件下不能完全恢复旧 direct N48 的全域 \(T\) 值误差水平；它不构成重新打开 R10 或自动提升阶次的依据。

---

# 32 参数符号总表

| 符号 | 含义 |
|---|---|
| \(f_c\) | 混凝土当前分析抗压强度 |
| \(E_0\) | 混凝土初始弹性模量 |
| \(\varepsilon_0\) | 混凝土参考压缩应变 |
| \(\nu\) | 混凝土泊松比 |
| \(\kappa\) | 归一化初始材料切线斜率 |
| \(\rho\) | 冻结的归一化拉伸强度尺度，当前为0.1 |
| \(x_{cr}\) | R10 拉伸特征坐标 |
| \(\eta\) | 主值正负部分平滑尺度 |
| \(m_t\) | Foster 源拉伸下降段斜率参数 |
| \(\eta_r\) | Foster 源函数转折平滑参数 |
| \(H(r,r_0)\) | Foster 源函数平滑铰 |
| \(T_{src}\) | Foster 源拉伸利用函数 |
| \(W_{src}\) | 由源材料公式积分得到的材料功 |
| \(u_r\) | R10 残余拉伸水平 |
| \(h\) | 由材料功闭合确定的 R10 拉伸峰值 |
| \(u_1,u_2\) | R10 拉伸上升支和下降支 |
| \(u_{sm}\) | R10 完整平滑拉伸标量 |
| \(\mathbf E\) | 物理面内应变张量 |
| \(\mathbf E_u\) | 等效单轴应变张量 |
| \(\mathbf X\) | 无量纲等效单轴张量 |
| \(\lambda_\pm\) | \(\mathbf X\) 的两个主值 |
| \(c_i,t_i\) | 第 \(i\) 主方向的压缩、拉伸平滑坐标 |
| \(C_i\) | 压缩 primitive |
| \(T_i\) | 拉伸 primitive |
| \(U_i\) | 一维 current master |
| \(a_{cc}\) | 冻结的双压相互作用系数 |
| \(a_t\) | 双拉相互作用系数，\(1-2^{-1/8}\) |
| \(\lambda_a,\lambda_b\) | N48 compiler 材料区间上下限 |
| \(\lambda_c,\lambda_h\) | compiler 区间中心及半宽 |
| \(\xi\) | 标准化 Chebyshev 材料坐标 |
| \(\mathcal C_n\) | 第 \(n\) 阶第一类 Chebyshev 多项式 |
| \(\theta_j,\lambda_j\) | 第 \(j\) 个材料 Chebyshev 根角度及对应材料坐标 |
| \(a_n^{(F,0)}\) | 旧 direct N48 第 \(n\) 阶系数 |
| \(V\) | 49×49 材料基值矩阵 |
| \(\mathbf H=V^TV\) | N48-C1 的 Gram 矩阵 |
| \(\mathbf G\) | 零点函数值/一阶切线约束矩阵 |
| \(\mathbf d_F\) | primitive \(F\) 的 R10 C1 目标向量 |
| \(a_n^{(F,C1)}\) | N48-C1 约束系数 |
| \(a_n^{(T,MM)}\) | T 的严格 C1 constrained-minimax 系数 |
| \(a_n^{(F,*)}\) | 当前最终使用的 primitive 系数 |
| \(\mathcal B_\eta\) | R10 近零拉伸边界层 |
| \(\lambda_\eta\) | 近零拉伸边界层右端材料坐标 |
| \(\mathbf Y\) | 标准化二维材料张量 |
| \(K_1,K_2\) | \(\mathbf Y\) 的迹和行列式 |
| \(A_n,B_n\) | Cayley--Hamilton 第 \(n\) 阶矩阵 Chebyshev 标量系数 |
| \(\mathbf U,\mathbf C,\mathbf T,\mathbf T^{(7)}\) | 四个 primitive 的二维矩阵函数 |
| \(\mathbf{CC},\mathbf{TC},\mathbf{TT}\) | 双压、拉压、双拉相互作用矩阵 |
| \(\mathbf S\) | 无量纲二维 current stress tensor |
| \(\boldsymbol\sigma\) | 物理二维应力张量 |
| \(\mathbb D\) | 一致二维材料切线 |
| \(b,\ell,t_p\) | 代表半波横向宽度、轴向长度和板厚 |
| \(X,Y,\zeta\) | 完整半波无量纲空间坐标 |
| \(D,q\) | 轴向广义压缩变量和无量纲局部幅值 |
| \(A\) | 局部挠曲物理幅值，\(A=bq\) |
| \(J_\Omega\) | 完整半波坐标变换 Jacobian |
| \(c_{ijk}\) | D15 有限解析空间系数 |
| \(M_i,M_j,Z_k\) | D15 三个方向的精确解析矩 |
| \(\mathscr D[\cdot]\) | D15 完整半波精确矩算子 |
| \(p_{ijk}\) | \(S_{yy}\) 的 D15 空间解析系数 |
| \(r_{ijk}\) | \(Q_q\) 的 D15 空间解析系数 |
| \(P_c\) | 混凝土轴向承载力 |
| \(R_{q,c}\) | 混凝土局部幅值广义残量 |
| \(D_x,D_y\) | Zhou/Navier 两个方向的等效切线弯曲刚度 |
| \(D_{\mu,eff},D_{66}\) | 泊松耦合和剪切对应的扭转刚度 |
| \(H_{eff}\) | Zhou/Navier 综合扭转刚度 |
| \(\alpha,\beta\) | 两个方向的 Navier 波数 |
| \(N_{y,cr}^{Z}\) | Zhou/Navier 形式的切线稳定审计膜力 |

---

# 33 最终纸面形式

更新后的理论最简纸面表达可归纳为

\[
\boxed{
\begin{aligned}
&\text{材料参数}
\xrightarrow{(2)-(5)}
\kappa,x_{cr},\eta
\\[1mm]
&\xrightarrow{(15)-(45)}
U(\lambda),C(\lambda),T(\lambda),T^7(\lambda)
\\[1mm]
&\xrightarrow{(62),(72),(75)}
a_n^{(F,*)}
\\[1mm]
&\xrightarrow{(83)-(94)}
\mathbf U,\mathbf C,\mathbf T,\mathbf T^{(7)}
\\[1mm]
&\xrightarrow{(96)-(99)}
\mathbf S
\\[1mm]
&\xrightarrow{(107)-(112)}
c_{ijk}
\\[1mm]
&\xrightarrow{(113)-(120)}
c_{ijk}M_iM_jZ_k
\\[1mm]
&\xrightarrow{(123),(128)}
P_c,\ R_{q,c}.
\end{aligned}
}
\tag{140}
\]

这一形式保持了周思铭类解析稳定论文的基本特点：材料参数、方向性刚度、解析模态与积分矩之间的关系逐层显式，不把物理关系隐藏在空间积分点或长小数系数表中。

---

# 34 当前执行边界

本文件只完成更新后的理论纸面化，不重新计算 Case21 或 Swartz24，也不利用已有试验结果修正 N48 系数。

```text
R10 = FROZEN
N48_ORDER = 48
U/C/T7 = N48-C1
T = N48-C1-CONSTRAINED-MINIMAX
CAYLEY_HAMILTON = GOVERNING
D15 = GOVERNING
ZHOU_Dx_Dy_H = TANGENT_STABILITY_ACCEPTANCE_GATE
SWARTZ24_Pu_RECALCULATION = NO
STRUCTURAL_CALIBRATION = NO
```
