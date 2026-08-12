# NZ-SCCM NC + Rebar 更新理论正式逐式推导
## 材料参数 → 闭式 R10 → N48-C1/MM 通用系数 → Cayley–Hamilton → Nguyen 二阶完整半波 → D15 精确矩 → P、R_q、L → NC-R1 极限根生产定义

**日期：2026-08-12**  
**身份：CURRENT GOVERNING FORMAL THEORY-WRITING BASELINE**  
**写作方式：参照周思铭博士论文的理论章节组织方式——先给出研究对象与假定，再逐式推导，并在公式后逐项解释“式中，……表示……”及其来源身份。**

---

# 0 适用范围、理论身份与固定边界

本文只对当前已经冻结的普通混凝土（NC）+钢筋（Rebar）理论链进行正式展开，不新增任何材料机制，也不改变现有求解边界。当前固定条件为

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
ACTIVE_MODE = m=1
KINEMATICS = NGUYEN_SECOND_ORDER
R10_MATERIAL_TARGET = FROZEN
MATERIAL_COMPILER_ORDER = 48
U_COMPILER  = N48-C1
C_COMPILER  = N48-C1
T7_COMPILER = N48-C1
T_COMPILER  = N48-C1-CONSTRAINED-MINIMAX
CAYLEY_HAMILTON = GOVERNING
EXACT_MOMENT_ENGINE = D15
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
STRUCTURAL_CALIBRATION = NO
```

需要特别说明的是，**NC-R1 并不是 R10、N48 或 D15 的新版本名称**。本文所称 NC-R1，仅指理论链末端已经冻结的“极限根生产合同”，即对可接受域、主平衡支、唯一极限根、平衡残量和极限残量的定义。本文把这一生产合同与其全部上游理论统一写成一套完整、可引用、可逐式审计的 NC + Rebar 理论表达。

为避免把来源参数、数学参数和治理参数混为一谈，本文采用下列来源身份：

```text
[GEO_INPUT]              几何输入或试件几何量
[MATERIAL_INPUT]         材料基本输入量
[R10_FROZEN]             当前冻结 R10 材料源常数/合同常数
[R10_DERIVED]            由 R10 已冻结关系推导得到的材料量
[COMPILER_CONTRACT]      N48-C1/MM 解析编译合同量
[MATHEMATICAL_IDENTITY]  纯数学恒等式或解析矩
[NGUYEN_SOURCE]          Nguyen 二阶运动学来源
[REBAR_SOURCE]           当前钢筋材料/几何来源
[ZHOU_STABILITY]         周思铭/Navier 稳定刚度语言
[NC_R1_GOVERNANCE]       NC-R1 极限根生产合同
```

这些标签只说明参数和公式的来源身份，不构成新的物理模型。

---

# 1 理论总体计算链

当前普通混凝土钢筋板的理论链写为

\[
\boxed{
\text{材料与几何参数}
\rightarrow
\text{闭式 R10 current operator}
\rightarrow
\{U,C,T,T^7\}
\rightarrow
\text{N48-C1/MM}
\rightarrow
\text{Cayley--Hamilton 二维提升}
\rightarrow
\text{Nguyen 二阶连续完整半波}
\rightarrow
\text{有限解析系数场}
\rightarrow
\text{D15 精确矩}
\rightarrow
P(D,q),\ R_q(D,q),\ L(D,q)
\rightarrow
\text{NC-R1 主支第一个 }+\!\to\!-\text{ 极大值}
}
\tag{1}
\]

式中，\(U,C,T,T^7\) 表示构成普通混凝土二维 current material map 的四个一维材料 primitive；N48-C1/MM 表示保持 48 阶不变、同时满足 R10 零点函数值和一阶导数锚点的材料解析编译层；Cayley–Hamilton 二维提升表示把一维标量 Chebyshev primitive 提升为二维张量函数；Nguyen 二阶连续完整半波表示当前固定的含初始缺陷 von Kármán 二阶运动学；D15 表示完整代表半波上的有限解析精确矩引擎；\(P\) 表示总轴向荷载；\(R_q\) 表示与局部附加挠曲广义坐标 \(q\) 共轭的平衡残量；\(L\) 表示轴力在平衡支上的切向驻值函数。式（1）的来源身份为当前 NZ-SCCM governing chain。

---

# 2 普通混凝土基本材料参数及归一化

普通混凝土的基本输入定义为

\[
\boxed{f_c,\qquad E_0,\qquad \varepsilon_0,\qquad \nu}
\tag{2}
\]

式中，\(f_c\) 表示普通混凝土单轴抗压强度，[MATERIAL_INPUT]；\(E_0\) 表示混凝土初始弹性模量，[MATERIAL_INPUT]；\(\varepsilon_0\) 表示当前 R10 采用的参考压缩应变，[MATERIAL_INPUT]；\(\nu\) 表示混凝土泊松比，[MATERIAL_INPUT]。这些量均来自具体板的材料输入或盲算合同，不由结构极限荷载反标。

定义归一化初始斜率

\[
\boxed{
\kappa=\frac{E_0\varepsilon_0}{f_c}
}
\tag{3}
\]

式中，\(\kappa\) 表示 R10 无量纲单轴初始斜率，[R10_DERIVED]；\(E_0,\varepsilon_0,f_c\) 的含义见式（2）。

R10 当前冻结的拉伸强度尺度取

\[
\boxed{\rho=0.1}
\tag{4}
\]

式中，\(\rho\) 表示 R10 拉伸应力相对于 \(f_c\) 的冻结无量纲尺度，[R10_FROZEN]。该值属于当前 R10 材料合同，不是由 Case21 或 Swartz 极限承载力拟合得到。

定义拉伸特征材料坐标

\[
\boxed{
x_{cr}=\frac{\rho}{\kappa}
}
\tag{5}
\]

式中，\(x_{cr}\) 表示 R10 拉伸上升段的特征无量纲应变坐标，[R10_DERIVED]；\(\rho\) 和 \(\kappa\) 分别由式（4）和式（3）确定。

定义拉压平滑尺度

\[
\boxed{
\eta=\frac{x_{cr}}{20}
}
\tag{6}
\]

式中，\(\eta\) 表示 R10 主等效应变在零点附近进行平滑拉压分解的材料尺度，[R10_DERIVED]；\(x_{cr}\) 由式（5）确定。

---

# 3 物理面内应变与等效单轴应变张量

板内任一点的物理面内应变张量写为

\[
\boxed{
\mathbf E=
\begin{bmatrix}
\varepsilon_x & \gamma_{xy}/2\\
\gamma_{xy}/2 & \varepsilon_y
\end{bmatrix}
}
\tag{7}
\]

式中，\(\mathbf E\) 表示物理面内小应变张量；\(\varepsilon_x\) 和 \(\varepsilon_y\) 分别表示 \(x\) 与 \(y\) 方向的法向应变；\(\gamma_{xy}\) 表示工程剪应变，因此张量剪应变分量为 \(\gamma_{xy}/2\)。这些量由后续 Nguyen 连续二阶运动学给出。

当前 R10 使用的等效单轴应变张量定义为

\[
\boxed{
\mathbf E_u
=
\frac{(1-\nu)\mathbf E+\nu\,\operatorname{tr}(\mathbf E)\mathbf I}
{1-\nu^2}
}
\tag{8}
\]

式中，\(\mathbf E_u\) 表示等效单轴应变张量，[R10_FROZEN]；\(\operatorname{tr}(\mathbf E)\) 表示物理应变张量的迹；\(\mathbf I\) 表示二维二阶单位张量；\(\nu\) 为式（2）的泊松比。

进一步定义无量纲等效应变张量

\[
\boxed{
\mathbf X=\frac{\mathbf E_u}{\varepsilon_0}
}
\tag{9}
\]

式中，\(\mathbf X\) 表示 R10 current operator 的无量纲二维等效应变张量，[R10_DERIVED]；\(\varepsilon_0\) 为式（2）的参考压缩应变。

由式（7）—式（9）可得

\[
\boxed{
X_{11}=\frac{\varepsilon_x+\nu\varepsilon_y}
{(1-\nu^2)\varepsilon_0},
\qquad
X_{22}=\frac{\nu\varepsilon_x+\varepsilon_y}
{(1-\nu^2)\varepsilon_0}
}
\tag{10}
\]

\[
\boxed{
X_{12}=\frac{\gamma_{xy}}
{2(1+\nu)\varepsilon_0}
}
\tag{11}
\]

式中，\(X_{11},X_{22}\) 表示 \(\mathbf X\) 的两个法向分量；\(X_{12}=X_{21}\) 表示其对称剪切分量；其余符号含义同式（7）—式（9）。

定义

\[
\boxed{
\mu=\frac{X_{11}+X_{22}}2,
\qquad
\delta=\frac{X_{11}-X_{22}}2,
\qquad
r_X=\sqrt{\delta^2+X_{12}^2}
}
\tag{12}
\]

式中，\(\mu\) 表示二维对称张量 \(\mathbf X\) 两个主值的平均值；\(\delta\) 表示两个法向分量的半差；\(r_X\) 表示主值半径。这三个量均为二维对称张量主值计算的数学量，[MATHEMATICAL_IDENTITY]。

因此两个主等效应变为

\[
\boxed{
\lambda_\pm=\mu\pm r_X
}
\tag{13}
\]

式中，\(\lambda_+\) 与 \(\lambda_-\) 分别表示 \(\mathbf X\) 的较大和较小主值，[MATHEMATICAL_IDENTITY]；\(\mu,r_X\) 由式（12）给出。

---

# 4 R10 主值拉压平滑分解

定义平滑正部函数

\[
\boxed{
\Pi_\eta(z)
=
\frac{z^2\left(\sqrt{z^2+\eta^2}+z\right)}
{2(z^2+\eta^2)}
}
\tag{14}
\]

式中，\(z\) 表示任意无量纲主应变材料坐标；\(\Pi_\eta(z)\) 表示当前 R10 冻结的平滑正部算子，[R10_FROZEN]；\(\eta\) 为式（6）的平滑尺度。

对任一主值 \(\lambda\)，定义压缩与拉伸材料坐标

\[
\boxed{
c(\lambda)=\Pi_\eta(-\lambda),
\qquad
t(\lambda)=\Pi_\eta(\lambda)
}
\tag{15}
\]

式中，\(c(\lambda)\) 表示主等效应变的平滑压缩部分；\(t(\lambda)\) 表示其平滑拉伸部分；两者均由式（14）确定，[R10_DERIVED]。

---

# 5 R10 压缩 primitive

当前压缩 primitive 定义为

\[
\boxed{
C(\lambda)
=
\frac{\kappa c(\lambda)}
{1+(\kappa-2)c(\lambda)+c(\lambda)^2}
}
\tag{16}
\]

式中，\(C(\lambda)\) 表示一维无量纲压缩材料 primitive，[R10_FROZEN]；\(\kappa\) 为式（3）的归一化初始斜率；\(c(\lambda)\) 为式（15）的平滑压缩坐标。该式属于当前冻结 R10 材料目标，不在本文通过结构试验重新识别。

---

# 6 Foster 源拉伸函数与 R10 材料功闭合

定义归一化拉伸横坐标

\[
\boxed{
r=\frac{t}{x_{cr}}
}
\tag{17}
\]

式中，\(t\) 表示式（15）的非负拉伸材料坐标；\(r\) 表示按 \(x_{cr}\) 归一化的拉伸材料横坐标；\(x_{cr}\) 由式（5）确定。

当前 Foster 源函数使用的冻结常数为

\[
\boxed{
m_t=-\frac{7}{90},
\qquad
\eta_r=0.05
}
\tag{18}
\]

式中，\(m_t\) 表示当前 Foster 源拉伸下降段的冻结斜率参数，[R10_FROZEN]；\(\eta_r\) 表示 Foster 源函数在转折位置附近的平滑尺度，[R10_FROZEN]。二者属于 R10 源材料合同，不由结构荷载拟合。

定义平滑铰函数

\[
\boxed{
H(r,r_0)
=
\frac12\left[(r-r_0)+\sqrt{(r-r_0)^2+\eta_r^2}\right]
-
\frac12\left[-r_0+\sqrt{r_0^2+\eta_r^2}\right]
}
\tag{19}
\]

式中，\(H(r,r_0)\) 表示 Foster 源函数使用的平滑铰函数，[R10_FROZEN]；\(r_0\) 表示铰激活中心；当前分别取 \(r_0=1\) 与 \(r_0=10\)；\(\eta_r\) 见式（18）。

由此定义 Foster 源拉伸利用函数

\[
\boxed{
T_{src}(r)
=
r+(m_t-1)H(r,1)-m_tH(r,10)
}
\tag{20}
\]

式中，\(T_{src}(r)\) 表示保存上游 Foster 拉伸材料功形状的源利用函数，[R10_FROZEN]；\(m_t\) 为式（18）的源下降斜率；\(H\) 为式（19）的平滑铰函数。

源归一化拉应力写为

\[
\boxed{
u_{t,src}(t)
=
\rho\,T_{src}\!\left(\frac{t}{x_{cr}}\right)
}
\tag{21}
\]

式中，\(u_{t,src}\) 表示 Foster 源归一化拉应力；\(\rho\) 为式（4）的冻结拉伸应力尺度；\(T_{src}\) 为式（20）的源利用函数。

定义源材料功

\[
\boxed{
W_{src}
=
\int_0^{10x_{cr}}u_{t,src}(t)\,dt
=
\rho x_{cr}\int_0^{10}T_{src}(r)\,dr
}
\tag{22}
\]

式中，\(W_{src}\) 表示一维 Foster 源材料关系在规定拉伸区间内的无量纲材料功，[R10_DERIVED]；该积分只发生在一维材料坐标上，不是板面或厚度空间积分，因此不计入 formal spatial quadrature。

---

# 7 R10 拉伸上升支、下降支及峰值

定义上升支局部坐标

\[
\boxed{
\tau=\frac{t}{x_{cr}},
\qquad 0\le\tau\le1
}
\tag{23}
\]

式中，\(\tau\) 表示 R10 拉伸上升支的局部无量纲材料坐标，[R10_DERIVED]；\(t\) 为拉伸材料坐标；\(x_{cr}\) 见式（5）。

当前上升支写为

\[
\boxed{
u_1(\tau)
=
\rho\tau
+(10h-6\rho)\tau^3
+(8\rho-15h)\tau^4
+(6h-3\rho)\tau^5
}
\tag{24}
\]

式中，\(u_1\) 表示 R10 拉伸上升支的归一化应力；\(h\) 表示待由材料功闭合确定的峰值；\(\rho\) 为式（4）的冻结拉伸强度尺度。式（24）来自零点初始斜率、峰点零一阶/二阶导数等冻结端点条件的五次多项式闭合，[R10_FROZEN/R10_DERIVED]。

定义下降支局部坐标

\[
\boxed{
s=\frac{t-x_{cr}}{9x_{cr}},
\qquad 0\le s\le1
}
\tag{25}
\]

式中，\(s\) 表示 R10 拉伸下降支的局部无量纲材料坐标；下降支对应 \(x_{cr}<t\le10x_{cr}\)。

当前冻结残余拉应力尺度为

\[
\boxed{u_r=0.03}
\tag{26}
\]

式中，\(u_r\) 表示 R10 在 \(t=10x_{cr}\) 处的残余归一化拉应力，[R10_FROZEN]；该值属于当前材料合同，不由结构极限荷载反标。

下降支定义为

\[
\boxed{
u_2(s)
=
h+(u_r-h)(10s^3-15s^4+6s^5)
}
\tag{27}
\]

式中，\(u_2\) 表示 R10 拉伸下降支；\(h\) 为拉伸峰值；\(u_r\) 为式（26）的残余拉应力；括号内多项式为满足两端平滑条件的五次 smoothstep，[R10_FROZEN]。

由上升支和下降支的材料功与式（22）的 Foster 源材料功相等，得到

\[
\boxed{
h
=
\frac15\left(
\frac{W_{src}}{x_{cr}}
-\frac{\rho}{10}
-\frac92u_r
\right)
}
\tag{28}
\]

式中，\(h\) 表示 R10 拉伸峰值，[R10_DERIVED]；\(W_{src}\) 为式（22）的源材料功；\(x_{cr}\) 为式（5）的特征坐标；\(\rho\) 为式（4）的拉伸强度尺度；\(u_r\) 为式（26）的残余拉应力。式（28）只使用材料源关系，不包含任何 Case21 或 Swartz 结构试验承载力。

因此完整归一化拉伸关系定义为

\[
\boxed{
u_{sm}(t)=
\begin{cases}
u_1(t/x_{cr}),&0\le t\le x_{cr},\\[2mm]
u_2[(t-x_{cr})/(9x_{cr})],&x_{cr}<t\le10x_{cr},\\[2mm]
u_r,&t>10x_{cr}.
\end{cases}
}
\tag{29}
\]

式中，\(u_{sm}(t)\) 表示完整 R10 归一化拉伸应力；\(u_1,u_2,u_r\) 分别见式（24）、式（27）和式（26）。

定义拉伸 primitive

\[
\boxed{
T(\lambda)
=
\frac{u_{sm}[\Pi_\eta(\lambda)]}{\rho}
}
\tag{30}
\]

式中，\(T(\lambda)\) 表示一维无量纲拉伸 primitive，[R10_DERIVED]；\(\Pi_\eta\) 为式（14）的平滑正部函数；\(u_{sm}\) 为式（29）；\(\rho\) 为式（4）。

双拉相互作用所需的独立 primitive 定义为

\[
\boxed{
T^{(7)}(\lambda)=[T(\lambda)]^7
}
\tag{31}
\]

式中，\(T^{(7)}\) 表示 R10 双拉相互作用使用的七次拉伸 primitive，[R10_DERIVED]。正式编译时，它作为独立标量目标进行 48 阶解析编译，而不是在截断后的二维张量上再数值七次幂。

---

# 8 一维 current master 与二维主应力关系

定义一维 current master

\[
\boxed{
U(\lambda)
=
\kappa\lambda
-C(\lambda)
+\kappa c(\lambda)
+\rho T(\lambda)
-\kappa t(\lambda)
}
\tag{32}
\]

式中，\(U(\lambda)\) 表示 R10 一维 current master，[R10_FROZEN/R10_DERIVED]；\(C\) 为式（16）的压缩 primitive；\(c,t\) 为式（15）的平滑拉压坐标；\(T\) 为式（30）的拉伸 primitive；\(\kappa,\rho\) 分别见式（3）和式（4）。

当前双拉相互作用常数定义为

\[
\boxed{
a_t=1-2^{-1/8}
}
\tag{33}
\]

式中，\(a_t\) 表示 R10 双拉相互作用冻结系数，[R10_FROZEN]。

双压相互作用系数记为

\[
\boxed{a_{cc}}
\tag{34}
\]

式中，\(a_{cc}\) 表示当前 R10 已冻结的双压相互作用系数，[R10_FROZEN]。其具体数值由当前 R10 材料合同提供；本文只继承该值，不根据板级承载力重新识别，也不在本篇理论推导中重开其上游材料来源。

对两个主等效应变 \(\lambda_+,\lambda_-\)，分别计算 \(U_\pm,C_\pm,T_\pm\)，则两个主方向的无量纲应力写为

\[
\boxed{
s_+
=
U_+
-a_{cc}C_+^2C_-
+C_+T_-
-\rho a_tT_+T_-^8
}
\tag{35}
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
\tag{36}
\]

式中，\(s_+,s_-\) 分别表示两个主方向的无量纲 current stress；\(U_\pm,C_\pm,T_\pm\) 表示相应主等效应变代入式（16）、式（30）和式（32）后的材料 primitive；\(a_{cc},a_t,\rho\) 分别见式（34）、式（33）和式（4）。式（35）—式（36）属于当前冻结 R10 二维主应力相互作用关系。

物理主应力为

\[
\boxed{
\sigma_\pm=f_c s_\pm
}
\tag{37}
\]

式中，\(\sigma_\pm\) 表示两个主方向的物理应力；\(f_c\) 为式（2）的混凝土抗压强度；\(s_\pm\) 为式（35）—式（36）的无量纲主应力。

---

# 9 R10 的严格零点 C1 锚点

当前 R10 在 \(\lambda=0\) 必须满足

\[
\boxed{
U(0)=0,
\qquad
U'(0)=\kappa
}
\tag{38}
\]

\[
\boxed{
C(0)=T(0)=T^{(7)}(0)=0
}
\tag{39}
\]

\[
\boxed{
C'(0)=T'(0)=(T^{(7)})'(0)=0
}
\tag{40}
\]

式中，撇号表示对真实材料坐标 \(\lambda\) 求导；\(\kappa\) 为式（3）的无量纲初始斜率。式（38）—式（40）是 R10 材料目标的严格函数值—一阶切线身份，也是后续 N48-C1/MM 的强制约束来源，[R10_FROZEN]。

---

# 10 N48 材料编译区间及 direct N48 通用系数

设当前材料编译区间为

\[
\boxed{
\lambda\in[\lambda_a,\lambda_b]
}
\tag{41}
\]

式中，\(\lambda_a\) 和 \(\lambda_b\) 分别表示当前板在盲算/生产合同中事先冻结的材料主等效应变编译区间下界和上界，[COMPILER_CONTRACT]。该区间必须覆盖生产状态中完整连续半波上的全部主等效应变，不能根据实验破坏荷载或历史理论根事后调整。

定义区间中心、半宽和标准坐标

\[
\boxed{
\lambda_c=\frac{\lambda_a+\lambda_b}{2},
\qquad
\lambda_h=\frac{\lambda_b-\lambda_a}{2},
\qquad
\xi(\lambda)=\frac{\lambda-\lambda_c}{\lambda_h}
}
\tag{42}
\]

式中，\(\lambda_c\) 表示材料编译区间中心；\(\lambda_h>0\) 表示区间半宽；\(\xi\in[-1,1]\) 表示标准 Chebyshev 材料坐标，均为 [COMPILER_CONTRACT/MATHEMATICAL_IDENTITY]。

第一类 Chebyshev 多项式定义为

\[
\boxed{
\mathcal C_n(\xi)=\cos[n\arccos(\xi)]
}
\tag{43}
\]

式中，\(\mathcal C_n\) 表示第 \(n\) 阶第一类 Chebyshev 多项式，[MATHEMATICAL_IDENTITY]；当前 \(n=0,1,\ldots,48\)。

定义 49 个 Chebyshev 根材料坐标

\[
\boxed{
\theta_j=\frac{(j+\tfrac12)\pi}{49},
\qquad
\lambda_j=\lambda_c+\lambda_h\cos\theta_j,
\qquad j=0,\ldots,48
}
\tag{44}
\]

式中，\(\theta_j\) 表示第 \(j\) 个 Chebyshev 根角度；\(\lambda_j\) 表示对应的一维材料坐标；\(j\) 只是材料系数生成索引，[COMPILER_CONTRACT]。这些 \(\lambda_j\) **不是**板面或厚度上的空间积分点，因此 \(49\) 个材料坐标不构成 formal spatial discretization。

对任意

\[
F\in\{U,C,T,T^{(7)}\},
\]

direct N48 的通用系数为

\[
\boxed{
a_n^{(F,0)}
=
\frac{2-\delta_{n0}}{49}
\sum_{j=0}^{48}
F(\lambda_j)\cos(n\theta_j),
\qquad n=0,\ldots,48
}
\tag{45}
\]

式中，\(F\) 表示四个 R10 一维 primitive 中任意一个；\(a_n^{(F,0)}\) 表示其 direct N48 第 \(n\) 阶基准系数；\(\delta_{n0}\) 表示 Kronecker delta，当 \(n=0\) 时取 1，否则取 0；\(\lambda_j,\theta_j\) 由式（44）确定。式（45）属于 [COMPILER_CONTRACT/MATHEMATICAL_IDENTITY]。

对应 direct N48 标量函数为

\[
\boxed{
F_{48}^{(0)}(\lambda)
=
\sum_{n=0}^{48}
a_n^{(F,0)}\mathcal C_n[\xi(\lambda)]
}
\tag{46}
\]

式中，\(F_{48}^{(0)}\) 表示 direct N48 解析表示；其当前身份只作为 N48-C1/MM 的基准系数起点，而不是最终 governing tangent representation。

---

# 11 N48-C1：保持 48 阶的函数值—切线约束修正

定义根点矩阵

\[
\boxed{
V_{jn}=\cos(n\theta_j)
}
\tag{47}
\]

式中，\(\mathbf V\) 表示 49 个材料根坐标到 49 个 Chebyshev 系数之间的离散正交矩阵；\(j,n=0,\ldots,48\)；\(\theta_j\) 由式（44）给出，[MATHEMATICAL_IDENTITY]。

由 Chebyshev 根点离散正交性可得

\[
\boxed{
\mathbf H=\mathbf V^T\mathbf V
=
\operatorname{diag}
\left(49,\frac{49}{2},\ldots,\frac{49}{2}\right)
}
\tag{48}
\]

\[
\boxed{
\mathbf H^{-1}
=
\frac1{49}\operatorname{diag}(1,2,\ldots,2)
}
\tag{49}
\]

式中，\(\mathbf H\) 表示 N48-C1 最小扰动问题的正规矩阵；\(\mathbf H^{-1}\) 为其显式逆；二者均来自 Chebyshev 根点正交性，[MATHEMATICAL_IDENTITY]。

材料坐标 \(\lambda=0\) 对应的标准坐标为

\[
\boxed{
\xi_0=-\frac{\lambda_c}{\lambda_h}
}
\tag{50}
\]

式中，\(\xi_0\) 表示零主等效应变在标准 Chebyshev 区间中的位置；\(\lambda_c,\lambda_h\) 由式（42）给出。

定义严格 C1 约束矩阵

\[
\boxed{
\mathbf G=
\begin{bmatrix}
\mathcal C_0(\xi_0)&\cdots&\mathcal C_{48}(\xi_0)\\
\lambda_h^{-1}\mathcal C_0'(\xi_0)&\cdots&\lambda_h^{-1}\mathcal C_{48}'(\xi_0)
\end{bmatrix}
}
\tag{51}
\]

式中，\(\mathbf G\) 表示 \(2\times49\) 的函数值—真实材料坐标一阶导数约束矩阵，[COMPILER_CONTRACT]；第一行约束 \(F(0)\)，第二行约束 \(dF/d\lambda|_{0}\)；\(\lambda_h^{-1}\) 来自 \(d/d\lambda=\lambda_h^{-1}d/d\xi\) 的链式法则。

目标向量取

\[
\boxed{
\mathbf d_U=\begin{bmatrix}0\\\kappa\end{bmatrix},
\qquad
\mathbf d_C=
\mathbf d_T=
\mathbf d_{T^{(7)}}=
\begin{bmatrix}0\\0\end{bmatrix}
}
\tag{52}
\]

式中，\(\mathbf d_F\) 表示 R10 在 \(\lambda=0\) 的严格函数值和一阶导数目标；其数值直接来自式（38）—式（40），[R10_FROZEN → COMPILER_CONTRACT]。

对于

\[
F\in\{U,C,T^{(7)}\},
\]

最终 C1 系数写为

\[
\boxed{
\mathbf a^{(F,C1)}
=
\mathbf a^{(F,0)}
+
\mathbf H^{-1}\mathbf G^T
(\mathbf G\mathbf H^{-1}\mathbf G^T)^{-1}
\left(
\mathbf d_F-\mathbf G\mathbf a^{(F,0)}
\right)
}
\tag{53}
\]

式中，\(\mathbf a^{(F,C1)}\) 表示 primitive \(F\) 的最终 N48-C1 系数向量；\(\mathbf a^{(F,0)}\) 表示式（45）的 direct N48 基准系数；\(\mathbf H,\mathbf G,\mathbf d_F\) 分别由式（48）、式（51）、式（52）给出。式（53）只需要求解一个 \(2\times2\) 约束系统；阶数仍为 48，材料坐标仍为 49 个，没有引入新的材料机制，[COMPILER_CONTRACT]。

---

# 12 T primitive 的 strict-C1 constrained-minimax 修正

R10 近零拉伸边界层内，严格恢复 \(T(0)=T'(0)=0\) 后，direct N48 的点插值优势与全域值误差发生竞争。因此当前只对 \(T\) 修改系数生成目标，不修改 R10，也不提高阶数。

最终 \(T\) 系数定义为

\[
\boxed{
\mathbf a^{(T,MM)}
=
\underset{\mathbf a\in\mathbb R^{49}}
{\operatorname{argmin}}
\left\|
\sum_{n=0}^{48}a_n\mathcal C_n[\xi(\lambda)]
-T_{R10}(\lambda)
\right\|_{L^\infty([\lambda_a,\lambda_b])}
}
\tag{54}
\]

并满足

\[
\boxed{
\mathbf G\mathbf a^{(T,MM)}=\mathbf d_T
}
\tag{55}
\]

式中，\(\mathbf a^{(T,MM)}\) 表示 \(T\) primitive 的 49 维 strict-C1 constrained-minimax 系数；\(T_{R10}\) 表示式（30）的闭式 R10 拉伸 primitive；\(L^\infty\) 表示完整材料编译区间上的最大绝对误差范数；\(\mathbf G\) 与 \(\mathbf d_T\) 分别见式（51）和式（52）。式（54）—式（55）属于 [COMPILER_CONTRACT]，不是结构板级拟合。

因此当前四个最终系数统一记为

\[
\boxed{
\mathbf a^{(F,*)}
=
\begin{cases}
\mathbf a^{(F,C1)},&F\in\{U,C,T^{(7)}\},\\
\mathbf a^{(T,MM)},&F=T.
\end{cases}
}
\tag{56}
\]

式中，上标 \((*)\) 表示当前 governing 的 N48-C1/MM 系数身份；\(U,C,T^{(7)}\) 使用式（53），\(T\) 使用式（54）—式（55）。

最终一维材料解析表达为

\[
\boxed{
F_{48}(\lambda)
=
\sum_{n=0}^{48}
a_n^{(F,*)}\mathcal C_n[\xi(\lambda)]
}
\tag{57}
\]

式中，\(F_{48}\) 表示当前 governing 的第 \(F\) 个一维 N48 primitive；\(a_n^{(F,*)}\) 为式（56）的最终材料系数。最终系数仍为固定的有限 49 项，因此正式结构复杂度不随空间积分点数增长。

---

# 13 Cayley–Hamilton 二维提升

为把式（57）的一维标量材料函数直接作用于二维对称张量 \(\mathbf X\)，定义标准化张量

\[
\boxed{
\mathbf Y
=
\frac{\mathbf X-\lambda_c\mathbf I}{\lambda_h}
}
\tag{58}
\]

式中，\(\mathbf Y\) 表示把无量纲等效应变张量 \(\mathbf X\) 映射到 Chebyshev 标准区间后的二维对称张量，[MATHEMATICAL_IDENTITY]；\(\lambda_c,\lambda_h\) 见式（42）。

定义二维不变量

\[
\boxed{
K_1=\operatorname{tr}(\mathbf Y),
\qquad
K_2=\det(\mathbf Y)
}
\tag{59}
\]

式中，\(K_1\) 和 \(K_2\) 分别表示 \(\mathbf Y\) 的迹和行列式，[MATHEMATICAL_IDENTITY]。

二维 Cayley–Hamilton 恒等式为

\[
\boxed{
\mathbf Y^2-K_1\mathbf Y+K_2\mathbf I=\mathbf0
}
\tag{60}
\]

式中，\(\mathbf0\) 表示二维零张量；其余符号见式（58）—式（59）。

因此任意阶 Chebyshev 矩阵多项式均可写为

\[
\boxed{
\mathcal C_n(\mathbf Y)=A_n\mathbf I+B_n\mathbf Y
}
\tag{61}
\]

式中，\(A_n=A_n(K_1,K_2)\) 和 \(B_n=B_n(K_1,K_2)\) 表示由二维 Cayley–Hamilton 降阶得到的两个标量多项式，[MATHEMATICAL_IDENTITY]。

初值取

\[
\boxed{
A_0=1,\ B_0=0,
\qquad
A_1=0,\ B_1=1
}
\tag{62}
\]

递推关系为

\[
\boxed{
A_{n+1}=-2K_2B_n-A_{n-1}
}
\tag{63}
\]

\[
\boxed{
B_{n+1}=2A_n+2K_1B_n-B_{n-1}
}
\tag{64}
\]

式中，\(n\ge1\)；\(A_n,B_n\) 表示式（61）的两个 Cayley–Hamilton 标量系数；\(K_1,K_2\) 由式（59）给出。式（62）—式（64）来自 Chebyshev 递推与二维 Cayley–Hamilton 恒等式，[MATHEMATICAL_IDENTITY]。

---

# 14 每一个 N48 材料系数如何形成二维 primitive

式（57）中的第 \(n\) 个材料系数对二维 primitive \(\mathbf F\) 的贡献为

\[
\boxed{
\mathbf F_{48}^{(n)}
=
a_n^{(F,*)}\mathcal C_n(\mathbf Y)
=
a_n^{(F,*)}(A_n\mathbf I+B_n\mathbf Y)
}
\tag{65}
\]

式中，\(\mathbf F_{48}^{(n)}\) 表示 primitive \(F\) 的第 \(n\) 阶二维张量贡献；\(a_n^{(F,*)}\) 为式（56）的材料系数；\(A_n,B_n\) 为式（63）—式（64）的 Cayley–Hamilton 系数；\(\mathbf Y\) 为式（58）的标准化应变张量。

将全部 49 项相加得

\[
\boxed{
\mathbf F_{48}
=
\sum_{n=0}^{48}\mathbf F_{48}^{(n)}
}
\tag{66}
\]

式中，\(\mathbf F_{48}\) 依次可表示 \(\mathbf U,\mathbf C,\mathbf T,\mathbf T^{(7)}\) 四个二维 current material primitive。

也可定义

\[
\boxed{
A_F=\sum_{n=0}^{48}a_n^{(F,*)}A_n,
\qquad
B_F=\sum_{n=0}^{48}a_n^{(F,*)}B_n
}
\tag{67}
\]

从而

\[
\boxed{
\mathbf F_{48}=A_F\mathbf I+B_F\mathbf Y
}
\tag{68}
\]

式中，\(A_F,B_F\) 分别表示 primitive \(F\) 汇总后的两个标量系数；式（68）与式（66）完全等价。

需要强调：式（65）给出了**一个 N48 系数进入二维材料张量的第一步**。后续若 \(\mathbf C,\mathbf T\) 发生乘积，则不同 \(n\) 项之间通过有限系数卷积产生交叉项，但仍然不需要任何物理空间取样。

---

# 15 二维 current stress tensor

定义双压相互作用张量

\[
\boxed{
\mathbf{CC}=\det(\mathbf C)\,\mathbf C
}
\tag{69}
\]

式中，\(\mathbf{CC}\) 表示双压相互作用张量；\(\mathbf C\) 为式（66）得到的二维压缩 primitive；\(\det(\mathbf C)\) 表示其行列式。

定义拉压相互作用张量

\[
\boxed{
\mathbf{TC}
=
\mathbf C
\left[
\operatorname{tr}(\mathbf T)\mathbf I-\mathbf T
\right]
}
\tag{70}
\]

式中，\(\mathbf{TC}\) 表示拉压相互作用张量；\(\mathbf C\) 与 \(\mathbf T\) 分别为二维压缩和拉伸 primitive；\(\operatorname{tr}(\mathbf T)\) 表示 \(\mathbf T\) 的迹。

定义双拉相互作用张量

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
\tag{71}
\]

式中，\(\mathbf{TT}\) 表示双拉相互作用张量；\(\mathbf T\) 为二维拉伸 primitive；\(\mathbf T^{(7)}\) 为独立编译的二维七次拉伸 primitive。

因此无量纲二维 current stress tensor 为

\[
\boxed{
\mathbf S
=
\mathbf U
-a_{cc}\mathbf{CC}
+\mathbf{TC}
-\rho a_t\mathbf{TT}
}
\tag{72}
\]

式中，\(\mathbf S\) 表示无量纲二维 current stress tensor；\(\mathbf U\) 为二维 current master；\(\mathbf{CC},\mathbf{TC},\mathbf{TT}\) 分别由式（69）—式（71）给出；\(a_{cc},\rho,a_t\) 分别见式（34）、式（4）、式（33）。

物理应力张量为

\[
\boxed{
\boldsymbol\sigma=f_c\mathbf S
}
\tag{73}
\]

式中，\(\boldsymbol\sigma\) 表示物理面内应力张量；\(f_c\) 为式（2）的混凝土抗压强度；\(\mathbf S\) 为式（72）的无量纲应力张量。

---

# 16 Nguyen 二阶连续完整代表半波

取一个连续完整代表半波，定义无量纲坐标

\[
\boxed{
X=\frac{\pi x}{b},
\qquad
Y=\frac{\pi y}{\ell},
\qquad
\zeta=\frac{2z}{t_p}
}
\tag{74}
\]

式中，\(x,y,z\) 表示板的物理坐标；\(b\) 表示完整代表半波横向宽度，[GEO_INPUT]；\(\ell\) 表示完整代表半波轴向长度，[GEO_INPUT]；\(t_p\) 表示板厚，[GEO_INPUT]；因此 \(X,Y\in[0,\pi]\)，\(\zeta\in[-1,1]\)。

初始缺陷和加载后附加挠曲采用同一完整半波形函数

\[
\boxed{
w_0=A_0\sin X\sin Y,
\qquad
w_1=A\sin X\sin Y
}
\tag{75}
\]

式中，\(w_0\) 表示无载参考构形中的初始几何缺陷；\(w_1\) 表示加载后相对于初始构形的附加挠曲；\(A_0\) 和 \(A\) 分别表示两者的幅值，[NGUYEN_SOURCE]。

定义无量纲幅值

\[
\boxed{
q_0=\frac{A_0}{b},
\qquad
q=\frac{A}{b}
}
\tag{76}
\]

式中，\(q_0\) 表示初始缺陷无量纲幅值，[GEO_INPUT/NGUYEN_SOURCE]；\(q\) 表示加载后的附加局部挠曲广义坐标，[NGUYEN_SOURCE]。因此无载初始状态是 \((D,q)=(0,0)\)，而不是 \(q=q_0\)，因为 \(q_0\) 已经包含在参考几何中。

定义二阶几何组合量

\[
\boxed{
\chi_q=q_0q+\frac12q^2
}
\tag{77}
\]

式中，\(\chi_q\) 表示 Nguyen/von Kármán 二阶运动学中初始缺陷—附加挠曲耦合项与附加挠曲平方项的组合，[NGUYEN_SOURCE]。

令 \(D>0\) 表示轴压 \(y\) 方向的无量纲平均压缩广义变量，则基础膜应变取

\[
\boxed{
e_x^{(0)}=\nu D,
\qquad
e_y^{(0)}=-D
}
\tag{78}
\]

式中，\(e_x^{(0)}\) 和 \(e_y^{(0)}\) 分别表示除局部挠曲贡献外的归一化基础膜应变；\(D\) 表示平均轴向压缩广义变量；\(\nu\) 表示混凝土泊松比。

二阶膜应变系数为

\[
\boxed{
C_{mx}=\frac{\pi^2}{\varepsilon_0}\chi_q,
\qquad
C_{my}=\frac{\pi^2b^2}{\varepsilon_0\ell^2}\chi_q,
\qquad
C_{mxy}=\frac{2\pi^2b}{\varepsilon_0\ell}\chi_q
}
\tag{79}
\]

式中，\(C_{mx},C_{my},C_{mxy}\) 分别表示 \(x\)、\(y\) 法向及工程剪切二阶膜应变项的无量纲系数，[NGUYEN_SOURCE]；\(b,\ell\) 为式（74）的完整半波宽度与长度；\(\varepsilon_0\) 为式（2）的参考压缩应变；\(\chi_q\) 由式（77）给出。

线性弯曲应变系数为

\[
\boxed{
C_{bx}=\frac{\pi^2t_p}{2\varepsilon_0b}q,
\qquad
C_{by}=\frac{\pi^2t_pb}{2\varepsilon_0\ell^2}q,
\qquad
C_{bxy}=-\frac{\pi^2t_p}{\varepsilon_0\ell}q
}
\tag{80}
\]

式中，\(C_{bx},C_{by}\) 分别表示 \(x,y\) 法向弯曲应变系数；\(C_{bxy}\) 表示扭曲曲率产生的工程剪应变系数；\(t_p,b,\ell,q,\varepsilon_0\) 的含义见式（74）、式（76）和式（2）；负号来自板弯曲工程剪应变的曲率符号约定，[NGUYEN_SOURCE]。

于是归一化连续应变场为

\[
\boxed{
e_x
=
\nu D
+C_{mx}\cos^2X\sin^2Y
+C_{bx}\sin X\sin Y\,\zeta
}
\tag{81}
\]

\[
\boxed{
e_y
=
-D
+C_{my}\sin^2X\cos^2Y
+C_{by}\sin X\sin Y\,\zeta
}
\tag{82}
\]

\[
\boxed{
g_{xy}
=
C_{mxy}\sin X\cos X\sin Y\cos Y
+C_{bxy}\cos X\cos Y\,\zeta
}
\tag{83}
\]

式中，\(e_x=\varepsilon_x/\varepsilon_0\)、\(e_y=\varepsilon_y/\varepsilon_0\)、\(g_{xy}=\gamma_{xy}/\varepsilon_0\) 分别表示归一化的两个法向应变和工程剪应变；\(C_{m*}\) 和 \(C_{b*}\) 分别由式（79）—式（80）给出；\(X,Y,\zeta\) 由式（74）定义。

物理应变为

\[
\boxed{
\varepsilon_x=\varepsilon_0e_x,
\qquad
\varepsilon_y=\varepsilon_0e_y,
\qquad
\gamma_{xy}=\varepsilon_0g_{xy}
}
\tag{84}
\]

式中，\(\varepsilon_0\) 为参考压缩应变；\(e_x,e_y,g_{xy}\) 见式（81）—式（83）。至此，给定 \((D,q)\) 后整个完整半波的连续应变场已唯一确定。

---

# 17 从 N48 项到有限三角—厚度系数场

由于式（81）—式（83）由有限三角函数和一次厚度坐标 \(\zeta\) 构成，\(\mathbf X\)、\(\mathbf Y\)、\(K_1\)、\(K_2\)、\(A_n\)、\(B_n\) 都可通过有限代数运算转化为有限解析三角—厚度系数场。

对任一 primitive \(F\) 的第 \(n\) 项、任一张量分量 \(a,b\in\{x,y\}\)，写成

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
\tag{85}
\]

式中，\(\delta_{ab}\) 表示 Kronecker delta；\(Y_{ab}\) 表示式（58）的标准化二维应变张量分量；\(\phi_{ijk,ab}^{(F,n)}\) 表示第 \(n\) 个 Cayley–Hamilton 项在 \((i,j,k)\) 解析基上的有限系数；\(i,j,k\) 分别表示 \(X,Y,\zeta\) 三个方向的解析基阶次。式（85）是有限代数展开，不包含空间取样。

因此式（65）中的材料系数 \(a_n^{(F,*)}\) 对该空间解析项的实际贡献为

\[
\boxed{
c_{ijk,ab}^{(F,n)}
=
a_n^{(F,*)}\phi_{ijk,ab}^{(F,n)}
}
\tag{86}
\]

式中，\(c_{ijk,ab}^{(F,n)}\) 表示 primitive \(F\) 的第 \(n\) 个 N48 材料系数对解析基 \((i,j,k)\) 的实际贡献；\(a_n^{(F,*)}\) 为式（56）的材料系数；\(\phi_{ijk,ab}^{(F,n)}\) 为式（85）的结构—材料代数系数。

不同 primitive 或不同阶次之间的乘积由 Chebyshev 乘积恒等式

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
\tag{87}
\]

进行有限系数卷积。

式中，\(\chi\) 表示任一标准 Chebyshev 自变量；\(m,n\) 表示两个基函数阶次；式（87）为第一类 Chebyshev 多项式的乘积恒等式，[MATHEMATICAL_IDENTITY]。因此 \(\mathbf{CC},\mathbf{TC},\mathbf{TT}\) 中的所有乘法都可转化为有限系数卷积，不需要在物理空间逐点相乘。

把所有 primitive 和相互作用项组装后，定义系数映射算子 \(\mathfrak C\)，则

\[
\boxed{
\mathfrak C[\mathbf S]
=
\mathfrak C[\mathbf U]
-a_{cc}\mathfrak C[\mathbf{CC}]
+\mathfrak C[\mathbf{TC}]
-\rho a_t\mathfrak C[\mathbf{TT}]
}
\tag{88}
\]

式中，\(\mathfrak C[\cdot]\) 表示把连续解析张量场转化为有限 \((i,j,k)\) 系数集合的代数算子；\(\mathbf S\) 由式（72）给出；所有内部乘积均通过式（87）的有限卷积完成。

---

# 18 D15 完整代表半波精确矩

从 \((x,y,z)\) 到 \((X,Y,\zeta)\) 的体积 Jacobian 为

\[
\boxed{
J_\Omega
=
\frac{b\ell t_p}{2\pi^2}
}
\tag{89}
\]

式中，\(J_\Omega\) 表示完整代表半波的坐标变换体积 Jacobian；\(b,\ell,t_p\) 分别为式（74）的半波宽度、长度和板厚，[GEO_INPUT/MATHEMATICAL_IDENTITY]。

设任一待积标量场已经通过式（85）—式（88）化为有限形式

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
\tag{90}
\]

式中，\(Q\) 表示任一需要在完整半波上积分的标量场；\(c_{ijk}\) 表示其有限解析系数；\(i,j,k\) 分别表示三个解析基阶次。式（90）是 D15 的输入语法。

完整半波面内精确矩为

\[
\boxed{
M_n
=
\int_0^\pi\mathcal C_n(\sin X)\,dX
=
\begin{cases}
\pi,&n=0,\\[1mm]
\dfrac{2\sin(n\pi/2)}{n},&n\ge1.
\end{cases}
}
\tag{91}
\]

式中，\(M_n\) 表示第 \(n\) 阶完整半波面内 Chebyshev 精确矩，[MATHEMATICAL_IDENTITY/D15]；\(n\) 表示面内解析基阶次。

厚度方向精确矩为

\[
\boxed{
Z_k
=
\int_{-1}^{1}\mathcal C_k(\zeta)\,d\zeta
=
\begin{cases}
0,&k\text{ 为奇数},\\[1mm]
\dfrac{2}{1-k^2},&k\text{ 为偶数}.
\end{cases}
}
\tag{92}
\]

式中，\(Z_k\) 表示第 \(k\) 阶厚度 Chebyshev 精确矩，[MATHEMATICAL_IDENTITY/D15]；\(k\) 表示厚度解析基阶次。

因此 D15 精确矩收缩算子定义为

\[
\boxed{
\mathscr D[Q]
=
\sum_{i,j,k}c_{ijk}M_iM_jZ_k
}
\tag{93}
\]

式中，\(\mathscr D[Q]\) 表示标量场 \(Q\) 在一个完整代表半波标准域上的精确解析矩；\(c_{ijk}\) 来自式（90）；\(M_i,M_j,Z_k\) 分别由式（91）—式（92）给出。式（93）不含 Gauss、Simpson、自适应积分、空间 Chebyshev collocation 或材料点网格。

---

# 19 每一个 N48 系数如何最终进入 D15

结合式（65）、式（85）、式（86）和式（93），primitive \(F\) 的第 \(n\) 个材料系数对任一张量分量精确矩的贡献为

\[
\boxed{
\mathscr D[F_{ab}^{(n)}]
=
a_n^{(F,*)}
\sum_{i,j,k}
\phi_{ijk,ab}^{(F,n)}M_iM_jZ_k
}
\tag{94}
\]

式中，\(\mathscr D[F_{ab}^{(n)}]\) 表示第 \(n\) 个 N48 材料项对最终完整半波积分的贡献；\(a_n^{(F,*)}\) 表示式（56）的第 \(n\) 个最终材料系数；\(\phi_{ijk,ab}^{(F,n)}\) 表示式（85）的结构—材料解析系数；\(M_i,M_j,Z_k\) 表示 D15 的精确面内和厚度矩。

因此一个材料系数从 R10 到结构积分的完整路径为

\[
\boxed{
a_n^{(F,*)}
\rightarrow
a_n^{(F,*)}(A_n\mathbf I+B_n\mathbf Y)
\rightarrow
\mathbf F_{48}^{(n)}
\rightarrow
\{c_{ijk,ab}^{(F,n)}\}
\rightarrow
\{c_{ijk,ab}^{(F,n)}M_iM_jZ_k\}
}
\tag{95}
\]

式中，第一箭头表示 Cayley–Hamilton 二维提升；第二箭头表示 primitive 张量项；第三箭头表示有限三角—厚度系数展开；第四箭头表示 D15 精确矩收缩。式（95）正是“每一个 N48 通用系数如何进入 D15”的正式理论链。

需要进一步说明的是，\(\mathbf{CC},\mathbf{TC},\mathbf{TT}\) 中的乘积会使多个 \(a_m^{(*)},a_n^{(*)}\) 通过式（87）发生有限卷积，因此最终 \(\mathbf S\) 的某个 \(c_{ijk}\) 可以含多个材料系数的有限代数组合。但该过程仍完全发生在有限系数空间中，正式空间积分次数始终为零。

---

# 20 混凝土轴向荷载

混凝土对轴向承载力的贡献定义为

\[
\boxed{
P_c
=-\frac1\ell
\int_{\Omega_h}\sigma_{yy}\,dV
}
\tag{96}
\]

式中，\(P_c\) 表示混凝土轴向荷载贡献；\(\Omega_h\) 表示一个完整代表半波体积；\(\sigma_{yy}\) 表示物理轴向应力；\(\ell\) 表示完整代表半波长度；负号用于把压应力对应的轴向承载力记为正。

若无量纲轴向应力展开为

\[
\boxed{
S_{yy}
=
\sum_{i,j,k}p_{ijk}
\mathcal C_i(\sin X)
\mathcal C_j(\sin Y)
\mathcal C_k(\zeta)
}
\tag{97}
\]

式中，\(p_{ijk}\) 表示最终无量纲轴向 current stress \(S_{yy}\) 的有限解析系数，由式（72）、式（85）—式（88）确定。

代入式（73）、式（89）和式（93），得到

\[
\boxed{
P_c
=
-\frac{f_cbt_p}{2\pi^2}
\mathscr D[S_{yy}]
}
\tag{98}
\]

式中，\(P_c\) 表示混凝土轴力；\(f_c\) 为混凝土抗压强度；\(b,t_p\) 为半波宽度和板厚；\(\mathscr D[S_{yy}]\) 为式（93）的完整半波精确矩。式（98）中不存在空间数值积分点。

---

# 21 混凝土幅值广义残量

定义归一化物理应变张量

\[
\boxed{
\mathbf e=\frac{\mathbf E}{\varepsilon_0}
}
\tag{99}
\]

式中，\(\mathbf e\) 表示按参考压缩应变 \(\varepsilon_0\) 归一化后的物理应变张量；\(\mathbf E\) 由式（7）和式（81）—式（84）确定。

由式（8）—式（9）可反写为

\[
\boxed{
\mathbf e
=(1+\nu)\mathbf X
-\nu\operatorname{tr}(\mathbf X)\mathbf I
}
\tag{100}
\]

式中，\(\mathbf X\) 为式（9）的无量纲等效应变张量；\(\nu\) 为泊松比；式（100）为式（8）的代数逆关系。

与广义幅值 \(q\) 共轭的无量纲功密度定义为

\[
\boxed{
Q_q
=
\mathbf S:\frac{\partial\mathbf e}{\partial q}
}
\tag{101}
\]

式中，\(Q_q\) 表示混凝土无量纲幅值广义功密度；\(\mathbf S\) 为式（72）的无量纲 current stress；冒号“\(:\)”表示二阶张量双点积；\(\partial\mathbf e/\partial q\) 由 Nguyen 二阶连续应变场式（81）—式（83）解析求导得到。

于是混凝土幅值残量为

\[
\boxed{
R_{q,c}
=
f_c\varepsilon_0J_\Omega\,\mathscr D[Q_q]
}
\tag{102}
\]

式中，\(R_{q,c}\) 表示混凝土对广义坐标 \(q\) 的功共轭平衡残量；\(f_c\varepsilon_0J_\Omega\) 表示材料—几何自然广义功尺度；\(J_\Omega\) 见式（89）；\(\mathscr D[Q_q]\) 由 D15 式（93）精确计算。

---

# 22 钢筋贡献

对第 \(r\) 层、方向 \(\alpha\in\{x,y\}\) 的钢筋，定义其配筋率、位置和材料参数为

\[
\boxed{
\rho_{s,\alpha}^{(r)},
\qquad
z_s^{(r)},
\qquad
E_s,
\qquad
\varepsilon_y,
\qquad
f_y
}
\tag{103}
\]

式中，\(\rho_{s,\alpha}^{(r)}\) 表示第 \(r\) 层 \(\alpha\) 方向钢筋相对于混凝土板截面的配筋率，[REBAR_SOURCE/MATERIAL_INPUT]；\(z_s^{(r)}\) 表示该钢筋层相对于板中面的厚度坐标，[REBAR_SOURCE/GEO_INPUT]；\(E_s\) 表示钢筋弹性模量，[MATERIAL_INPUT]；\(\varepsilon_y\) 表示钢筋屈服应变，[MATERIAL_INPUT]；\(f_y\) 表示钢筋屈服强度，[MATERIAL_INPUT]。

钢筋方向应变由同一 Nguyen 连续应变场在相应钢筋层位置解析评价。若当前生产合同规定钢筋保持弹性，则

\[
\boxed{
\sigma_{s,\alpha}=E_s\varepsilon_{s,\alpha}
}
\tag{104}
\]

式中，\(\sigma_{s,\alpha}\) 表示 \(\alpha\) 方向钢筋应力；\(\varepsilon_{s,\alpha}\) 表示由式（81）—式（84）在钢筋位置投影得到的钢筋轴向应变；\(E_s\) 为式（103）的钢筋弹性模量，[REBAR_SOURCE]。

该弹性支必须满足

\[
\boxed{
\max_{\Omega_h,r,\alpha}
|\varepsilon_{s,\alpha}|<\varepsilon_y
}
\tag{105}
\]

式中，左端表示整个连续完整半波、全部钢筋层和方向上的最大钢筋应变；\(\varepsilon_y\) 为钢筋屈服应变。若式（105）不满足，而当前合同没有冻结相应塑性钢筋支，则必须停止于 `BLOCKED_AT_STEEL_BRANCH`，不能临时创造钢筋塑性公式。

总钢筋轴力和幅值残量分别记为

\[
\boxed{
P_s=P_s(D,q),
\qquad
R_{q,s}=R_{q,s}(D,q)
}
\tag{106}
\]

式中，\(P_s\) 表示全部钢筋对轴向荷载的解析贡献；\(R_{q,s}\) 表示全部钢筋对广义幅值 \(q\) 的功共轭残量；两者均由钢筋应力与同一连续半波应变/虚功关系解析积分得到。对于具体盲算合同，可进一步代入钢筋层数、方向和位置得到显式闭式公式，但本文不把 Case21 的具体数值写入一般理论定义。

---

# 23 总荷载与总平衡方程

结构总轴向荷载定义为

\[
\boxed{
P(D,q)=P_c(D,q)+P_s(D,q)
}
\tag{107}
\]

式中，\(P\) 表示 NC + Rebar 板的总轴向荷载；\(P_c\) 为式（98）的混凝土贡献；\(P_s\) 为式（106）的钢筋贡献；当前结构未知广义变量只有 \(D\) 与 \(q\)。

总幅值平衡残量定义为

\[
\boxed{
R_q(D,q)=R_{q,c}(D,q)+R_{q,s}(D,q)
}
\tag{108}
\]

式中，\(R_q\) 表示与附加挠曲广义坐标 \(q\) 共轭的总平衡残量；\(R_{q,c}\) 为式（102）的混凝土贡献；\(R_{q,s}\) 为式（106）的钢筋贡献。

因此非线性平衡集合满足

\[
\boxed{
R_q(D,q)=0
}
\tag{109}
\]

式中，满足式（109）的所有 \((D,q)\) 只是数学平衡状态。**式（109）本身既不定义稳定性，也不唯一指定极限承载力。** 生产意义上的主支和极限点还必须经过后续 NC-R1 定义。

---

# 24 同源导数与极限函数 L

由同一有限解析表达对 \(D,q\) 求导，定义

\[
\boxed{
P_D=\frac{\partial P}{\partial D},
\qquad
P_q=\frac{\partial P}{\partial q}
}
\tag{110}
\]

\[
\boxed{
R_{q,D}=\frac{\partial R_q}{\partial D},
\qquad
R_{q,q}=\frac{\partial R_q}{\partial q}
}
\tag{111}
\]

式中，\(P_D,P_q\) 分别表示总轴力对 \(D,q\) 的偏导数；\(R_{q,D},R_{q,q}\) 分别表示幅值平衡残量对 \(D,q\) 的偏导数。生产导数必须由同一有限解析式解析求导或 forward automatic differentiation 得到，不能用有限差分替代 current tangent identity。

在正则平衡点

\[
\boxed{
\nabla R_q=(R_{q,D},R_{q,q})\ne\mathbf0
}
\tag{112}
\]

式中，\(\nabla R_q\) 表示平衡 level set 在 \((D,q)\) 平面内的梯度；非零条件表示该点附近的平衡集合是正则一维曲线。

该 level set 的一个自然切向量为

\[
\boxed{
\mathbf t_0
=
(R_{q,q},-R_{q,D})
}
\tag{113}
\]

式中，\(\mathbf t_0\) 表示 \(R_q=0\) 平衡曲线的非单位切向量，[MATHEMATICAL_IDENTITY/NC_R1_GOVERNANCE]。因为

\[
\nabla R_q\cdot\mathbf t_0
=R_{q,D}R_{q,q}-R_{q,q}R_{q,D}=0,
\]

所以式（113）确为 level set 切向量。

总轴力沿该切向量的一阶变化为

\[
\boxed{
\nabla P\cdot\mathbf t_0
=
P_D R_{q,q}-P_qR_{q,D}
}
\tag{114}
\]

式中，\(\nabla P=(P_D,P_q)\) 表示总轴力在 \((D,q)\) 平面中的梯度。由此定义极限函数

\[
\boxed{
L(D,q)
=
P_D R_{q,q}-P_qR_{q,D}
}
\tag{115}
\]

式中，\(L\) 表示总轴力在正则平衡支切向方向上的非归一化一阶导数，[MATHEMATICAL_IDENTITY/NC_R1_GOVERNANCE]。因此 \(L=0\) 的本质是“\(P\) 在平衡支上的切向驻值”，不是第二套材料模型或经验稳定折减。

当局部 \(R_{q,q}\neq0\) 时，也可写成

\[
\boxed{
\frac{dq}{dD}
=-\frac{R_{q,D}}{R_{q,q}},
\qquad
\frac{dP}{dD}
=
\frac{L}{R_{q,q}}
}
\tag{116}
\]

式中，\(dq/dD\) 表示局部把平衡支写成 \(q(D)\) 时的路径斜率；\(dP/dD\) 表示该局部参数化下的轴力路径切线。式（116）只是式（113）—式（115）的一个局部图表示；即使 \(R_{q,q}=0\)，只要 \(\nabla R_q\neq0\)，level-set 切向定义仍然有效。

---

# 25 NC-R1 可接受域

NC + Rebar 当前生产可接受域定义为

\[
\boxed{
\mathcal A
=
\left\{(D,q):
\begin{array}{l}
D\ge0,\\
q\ge0,\\
P(D,q)\ge0,\\
\text{continuous compiler-domain certificate = PASS},\\
\text{all frozen NC material/source-range gates = PASS},\\
\text{active rebar branch gate = PASS},\\
P,R_q\text{ 及其一阶导数均有限}
\end{array}
\right\}
}
\tag{117}
\]

式中，\(\mathcal A\) 表示 NC-R1 的物理/来源可接受 \((D,q)\) 域，[NC_R1_GOVERNANCE]；\(D\ge0\) 表示只考虑当前单调轴压方向；\(q\ge0\) 表示当前正初始缺陷 \(q_0>0\) 下只接受与初始缺陷同向增长的附加挠曲生产主支；continuous compiler-domain certificate 表示整个连续完整半波的主等效应变必须位于式（41）的编译区间内；active rebar branch gate 表示钢筋必须处于当前已冻结的材料支中。

式（117）不人为设置由 Case21 历史答案反推的 \(D_{max}\) 或 \(q_{max}\)。其上边界只由冻结材料来源、连续 compiler certificate 和当前钢筋来源合同决定。

---

# 26 NC-R1 主平衡支

定义数学平衡集合

\[
\boxed{
\mathcal E
=
\{(D,q):R_q(D,q)=0\}
}
\tag{118}
\]

式中，\(\mathcal E\) 表示式（109）的全部数学平衡状态集合；其中可以同时包含主支、断开高幅值支、负 \(q\) 支以及其他数学根。

无载初始状态为

\[
\boxed{
(D,q)=(0,0)
}
\tag{119}
\]

式中，\(D=0\) 表示无平均轴向压缩；\(q=0\) 表示没有加载后附加挠曲；初始缺陷 \(q_0\) 已通过式（75）—式（77）包含在参考几何中，因此式（119）并不代表完美板。

NC-R1 的唯一 primary equilibrium branch 定义为

\[
\boxed{
\Gamma_0
=
\operatorname{Conn}_{(0,0)}
\left(
\mathcal E\cap\mathcal A
\right)
}
\tag{120}
\]

式中，\(\Gamma_0\) 表示可接受平衡集合中与无载状态 \((0,0)\) 连通的唯一连通分支，[NC_R1_GOVERNANCE]；\(\operatorname{Conn}_{(0,0)}\) 表示取包含 \((0,0)\) 的 connected component；\(\mathcal E\) 和 \(\mathcal A\) 分别由式（118）和式（117）定义。

因此，与 \((0,0)\) 不连通的高幅值正根无论荷载多大，都只能记录为 `REJECTED_DISCONNECTED_BRANCH`；负 \(q\) 根在当前正初始缺陷生产合同下记录为 `REJECTED_WRONG_IMPERFECTION_DIRECTION`。这两个分类都不允许取得 \(P_u\) 身份。

---

# 27 主支方向、弧长与分支奇点

在 \(\Gamma_0\) 的正则部分定义单位切向量

\[
\boxed{
\widehat{\mathbf t}
=
\pm
\frac{(R_{q,q},-R_{q,D})}
{\sqrt{R_{q,q}^2+R_{q,D}^2}}
}
\tag{121}
\]

式中，\(\widehat{\mathbf t}\) 表示主平衡支的单位切向量；符号在无载端选取使路径进入 \(D>0\) 的方向，之后连续选择使相邻切向量方向保持一致，[NC_R1_GOVERNANCE]。

定义有向弧长 \(s\)

\[
\boxed{
s=0\quad\text{at }(D,q)=(0,0),
\qquad
s>0\quad\text{along loading direction}
}
\tag{122}
\]

式中，\(s\) 表示沿 \(\Gamma_0\) 从无载状态向加载方向增长的有向弧长参数，[NC_R1_GOVERNANCE]。

若在第一个 admissible maximum 之前出现

\[
\boxed{
\nabla R_q=\mathbf0
}
\tag{123}
\]

式中，式（123）表示 level set 失去正则性，局部平衡分支拓扑可能不再唯一。此时必须输出 `BLOCKED_AT_PRIMARY_BRANCH_SINGULARITY`，不得由 Newton 初值、最大荷载或最接近历史根等数值规则替代物理分支选择。

---

# 28 第一个 +→− 局部最大值与唯一 P_u

沿有向主支定义轴力切线

\[
\boxed{
g(s)
=
\frac{dP}{ds}
=
\nabla P\cdot\widehat{\mathbf t}
}
\tag{124}
\]

式中，\(g(s)\) 表示总轴力沿加载方向有向主支的弧长导数，[NC_R1_GOVERNANCE]；\(\nabla P\) 由式（110）确定；\(\widehat{\mathbf t}\) 由式（121）确定。

在正则点上

\[
\boxed{
g(s)=0\iff L(D,q)=0}
\tag{125}
\]

式中，等价关系来自式（114）—式（115），因为单位化只对 \(\mathbf t_0\) 乘以非零标量，不改变驻值条件。

但驻值不自动等于极大值。生产意义上的 maximum limit root 必须满足

\[
\boxed{
g(s)>0\quad\text{在根的加载前侧}}
\tag{126}
\]

\[
\boxed{
g(s)<0\quad\text{在根的加载后侧}}
\tag{127}
\]

式中，式（126）—式（127）共同表示轴力沿主支经历 \(+\to-\) 的切线变号，因此该驻值为局部最大值；\(-\to+\) 对应局部最小值；无符号改变的 \(g=0\) 对应退化驻值点。

定义主支上全部 admissible maximum 集合

\[
\boxed{
\mathcal M
=
\left\{
s_i>0:
R_q=0,\ L=0,\ g:+\to-
\right\}
}
\tag{128}
\]

式中，\(\mathcal M\) 表示沿 \(\Gamma_0\) 出现的全部可接受局部最大值的弧长位置集合，[NC_R1_GOVERNANCE]。

最终生产极限点定义为

\[
\boxed{
s_u=\min\mathcal M}
\tag{129}
\]

\[
\boxed{
(D_u,q_u)=\Gamma_0(s_u)
}
\tag{130}
\]

\[
\boxed{
P_u=P(D_u,q_u)
}
\tag{131}
\]

式中，\(s_u\) 表示从无载状态沿主平衡支首先遇到的局部最大值位置；\(D_u,q_u\) 表示该极限点的两个广义坐标；\(P_u\) 表示当前 NC-R1 定义下唯一的生产极限承载力。

因此当前正式定义可以压缩为

\[
\boxed{
P_u
=
\text{从 }(0,0)\text{ 出发沿可接受主平衡支 }\Gamma_0
\text{ 首先遇到的 }P\text{ 的 }+\to-\text{ 局部最大值}
}
\tag{132}
\]

式中，式（132）是 NC-R1 极限根生产合同的核心定义。它明确排除“全部数学根中最大荷载”“最接近试验的根”“最接近历史 Case21 的根”“跳过第一个最大值选择后续最大值”和“跳到断开高幅值根”等规则。

---

# 29 平衡残量 R_norm

定义材料自然广义功尺度

\[
\boxed{
R_{mat}=f_c\varepsilon_0J_\Omega
}
\tag{133}
\]

式中，\(R_{mat}\) 表示 NC + Rebar 幅值平衡的材料自然广义功尺度，[NC_R1_GOVERNANCE]；\(f_c\) 为混凝土抗压强度；\(\varepsilon_0\) 为参考压缩应变；\(J_\Omega\) 为式（89）的完整半波体积 Jacobian。

定义平衡残量尺度

\[
\boxed{
R_{scale}
=
\max
\left(
R_{mat},
|R_{q,c}|+|R_{q,s}|
\right)
}
\tag{134}
\]

式中，\(R_{scale}\) 表示平衡残量的归一化尺度；第一项防止在内力贡献很小时尺度退化；第二项直接反映混凝土和钢筋两个广义功大项的相消量级，[NC_R1_GOVERNANCE]。

统一平衡残量定义为

\[
\boxed{
R_{norm}
=
\frac{|R_q|}{R_{scale}}
=
\frac{|R_q|}
{\max(f_c\varepsilon_0J_\Omega,|R_{q,c}|+|R_{q,s}|)}
}
\tag{135}
\]

式中，\(R_{norm}\) 表示无量纲总平衡残量，[NC_R1_GOVERNANCE]；\(R_q\) 为式（108）的总幅值残量。

当前生产接受门为

\[
\boxed{
R_{norm}\le10^{-5}
}
\tag{136}
\]

式中，\(10^{-5}\) 表示 NC-R1 在读取任何 Case21/Swartz 实验极限荷载以前冻结的工程数值闭合容差，[NC_R1_GOVERNANCE]；该数值不是材料参数。

---

# 30 极限残量 L_norm 及重标度不变性

定义

\[
\boxed{
A_L=P_DR_{q,q},
\qquad
B_L=P_qR_{q,D}
}
\tag{137}
\]

式中，\(A_L\) 与 \(B_L\) 表示构成极限函数 \(L=A_L-B_L\) 的两个大项；\(P_D,P_q,R_{q,D},R_{q,q}\) 分别见式（110）—式（111）。

NC-R1 的 signed normalized limit residual 定义为

\[
\boxed{
L_{norm}
=
\frac{L}{|A_L|+|B_L|}
=
\frac{P_DR_{q,q}-P_qR_{q,D}}
{|P_DR_{q,q}|+|P_qR_{q,D}|}
}
\tag{138}
\]

式中，\(L_{norm}\) 表示无量纲极限残量，[NC_R1_GOVERNANCE]；分母直接采用式（115）中两个相消大项的自然尺度。

当前生产接受门为

\[
\boxed{
|L_{norm}|\le10^{-5}
}
\tag{139}
\]

式中，\(10^{-5}\) 表示 NC-R1 冻结的极限条件数值闭合容差，[NC_R1_GOVERNANCE]；该数值不参与材料拟合。

为验证式（138）不依赖广义坐标单位，令

\[
\boxed{
D'=aD,
\qquad
q'=bq,
\qquad a>0,\ b>0
}
\tag{140}
\]

式中，\(a,b\) 表示对 \(D,q\) 的任意独立正线性重标度常数，[MATHEMATICAL_IDENTITY]。

根据链式法则

\[
\boxed{
P_{D'}=\frac1aP_D,
\quad
P_{q'}=\frac1bP_q,
\quad
R_{q,D'}=\frac1aR_{q,D},
\quad
R_{q,q'}=\frac1bR_{q,q}
}
\tag{141}
\]

式中，各偏导数均按新坐标 \((D',q')\) 求导。

因此式（138）的分子和分母均整体乘以 \(1/(ab)\)，得到

\[
\boxed{
L_{norm}'=L_{norm}
}
\tag{142}
\]

式中，式（142）表明 \(L_{norm}\) 对 \(D,q\) 的独立正线性重标度保持不变，[MATHEMATICAL_IDENTITY]。

若式（138）的分母为零，不得人为令 \(L_{norm}=0\)；必须进一步检查 \(\nabla R_q=0\)、\(\nabla P=0\) 或其他退化驻值状态，并按 NC-R1 对应分类处理。

---

# 31 根的记录与重复性

NC-R1 要求所有发现的 \(R_q=L=0\) 数学根均保留记录，其允许分类为

```text
PRIMARY_FIRST_MAXIMUM_LIMIT_ROOT
PRIMARY_LATER_MAXIMUM_ROOT
PRIMARY_MINIMUM_STATIONARY_ROOT
PRIMARY_DEGENERATE_STATIONARY_ROOT
REJECTED_DISCONNECTED_BRANCH
REJECTED_WRONG_IMPERFECTION_DIRECTION
REJECTED_OUTSIDE_COMPILER_DOMAIN
REJECTED_MATERIAL_SOURCE_EXHAUSTED
REJECTED_STEEL_BRANCH_UNSUPPORTED
REJECTED_DUPLICATE_ROOT
REJECTED_NUMERICAL_ARTIFACT
```

其中只有 `PRIMARY_FIRST_MAXIMUM_LIMIT_ROOT` 具有式（131）的生产 \(P_u\) 身份。

对于两个独立低维数学后端得到的两个候选根 \(i,j\)，定义归一化根距离

\[
\boxed{
d_{ij}
=
\max\left[
|D_i-D_j|,
\frac{|q_i-q_j|}{q_0},
\frac{|P_i-P_j|}{\max(|P_i|,|P_j|,1\ \mathrm{kN})}
\right]
}
\tag{143}
\]

式中，\(d_{ij}\) 表示两个独立数值结果是否代表同一物理根的归一化距离，[NC_R1_GOVERNANCE]；\(q_0\) 为式（76）的初始缺陷无量纲幅值；\(1\,\mathrm{kN}\) 只用于防止荷载尺度在接近零时退化。

当前重复性接受门为

\[
\boxed{
d_{ij}\le10^{-4}}
\tag{144}
\]

式中，\(10^{-4}\) 表示 NC-R1 冻结的独立根后端重复性门，[NC_R1_GOVERNANCE]。若两个声称的生产根不满足式（144），不得取平均值。

---

# 32 周思铭/Navier current-tangent 稳定刚度门

当前材料一致切线由同一 current operator 解析求导

\[
\boxed{
\mathbb C_t
=
\frac{\partial\boldsymbol\sigma}{\partial\mathbf E}
}
\tag{145}
\]

式中，\(\mathbb C_t\) 表示普通混凝土当前二维一致材料切线；\(\boldsymbol\sigma\) 为式（73）的 current stress；\(\mathbf E\) 为式（7）的物理应变张量。该切线必须与应力来自同一 R10→N48-C1/MM 表达，不能另建“稳定专用切线”。

记其当前工程分量为

\[
\boxed{
C_{xx,t},\ C_{yy,t},\ C_{xy,t},\ C_{yx,t},\ G_t
}
\tag{146}
\]

式中，\(C_{xx,t}\) 与 \(C_{yy,t}\) 分别表示两个法向 current tangent；\(C_{xy,t},C_{yx,t}\) 表示交叉法向 current tangent；\(G_t\) 表示工程剪切 current tangent。

按周思铭正交各向异性板稳定“方向弯曲刚度 + 交叉/扭转刚度共同控制”的语言，当前项目定义等效稳定刚度

\[
\boxed{
D_x=\frac{t_p^3}{12}C_{xx,t},
\qquad
D_y=\frac{t_p^3}{12}C_{yy,t}
}
\tag{147}
\]

式中，\(D_x\) 和 \(D_y\) 分别表示当前 RC 板抵抗 \(x\)、\(y\) 方向曲率的等效 current bending stiffness，[ZHOU_STABILITY]；\(t_p\) 为板厚。这里继承的是周思铭的方向刚度稳定骨架，不是其钢管混凝土束组合墙截面常数。

定义交叉法向等效刚度和工程剪切等效刚度

\[
\boxed{
D_{\mu,eff}
=
\frac{t_p^3}{24}(C_{xy,t}+C_{yx,t}),
\qquad
D_{66}=\frac{t_p^3}{12}G_t
}
\tag{148}
\]

式中，\(D_{\mu,eff}\) 表示对两个交叉法向 current tangent 对称化后的泊松/耦合刚度；\(D_{66}\) 表示 current shear tangent 对稳定扭转刚度的贡献，[ZHOU_STABILITY]。

当前项目的 Zhou-form 组合刚度定义为

\[
\boxed{
H_{eff}=D_{\mu,eff}+2D_{66}
}
\tag{149}
\]

式中，\(H_{eff}\) 表示进入当前 Navier 正交稳定表达的组合交叉—扭转刚度，[ZHOU_STABILITY]。它是将当前 R10 current tangent 映射到周思铭稳定语言后的等效量；**不能把式（149）反向解释为周思铭原组合墙截面常数的直接移植**。

对基本完整半波定义

\[
\boxed{
\alpha=\frac{\pi}{b},
\qquad
\beta=\frac{\pi}{\ell}
}
\tag{150}
\]

式中，\(\alpha,\beta\) 分别表示 \(x,y\) 方向的基本 Navier 波数；\(b,\ell\) 为完整代表半波宽度和长度，[ZHOU_STABILITY/MATHEMATICAL_IDENTITY]。

对应轴压方向的 Zhou-form current-tangent 临界膜力写为

\[
\boxed{
N_{y,cr}^{Z}
=
\frac{
D_x\alpha^4
+2H_{eff}\alpha^2\beta^2
+D_y\beta^4
}{\beta^2}
}
\tag{151}
\]

式中，\(N_{y,cr}^{Z}\) 表示把当前 R10/N48-C1/MM 一致切线投影到周思铭/Navier 正交稳定骨架后得到的轴压方向临界膜力；\(D_x,D_y,H_{eff}\) 分别见式（147）—式（149）；\(\alpha,\beta\) 见式（150）。式（151）在当前 NZ-SCCM 中只作为 current tangent 稳定性验收和物理解释门，不取代式（107）—式（132）的非线性极限承载力体系。

---

# 33 参数与符号来源总表

| 符号 | 物理/数学含义 | 来源身份 | 是否允许由结构试验反标 |
|---|---|---|---|
| \(f_c\) | NC 单轴抗压强度 | [MATERIAL_INPUT] | 否 |
| \(E_0\) | NC 初始弹性模量 | [MATERIAL_INPUT] | 否 |
| \(\varepsilon_0\) | R10 参考压缩应变 | [MATERIAL_INPUT] | 否 |
| \(\nu\) | NC 泊松比 | [MATERIAL_INPUT] | 否 |
| \(\kappa\) | \(E_0\varepsilon_0/f_c\) | [R10_DERIVED] | 否 |
| \(\rho\) | R10 冻结拉伸强度尺度，当前 0.1 | [R10_FROZEN] | 否 |
| \(x_{cr}\) | R10 拉伸特征坐标 | [R10_DERIVED] | 否 |
| \(\eta\) | R10 拉压平滑尺度 | [R10_DERIVED] | 否 |
| \(m_t\) | Foster 源下降斜率参数 | [R10_FROZEN] | 否 |
| \(\eta_r\) | Foster 源铰平滑尺度 | [R10_FROZEN] | 否 |
| \(u_r\) | R10 残余拉应力尺度 | [R10_FROZEN] | 否 |
| \(W_{src}\) | Foster 源材料功 | [R10_DERIVED] | 否 |
| \(h\) | 由材料功闭合得到的 R10 拉伸峰值 | [R10_DERIVED] | 否 |
| \(a_{cc}\) | R10 双压相互作用冻结系数 | [R10_FROZEN] | 否 |
| \(a_t\) | R10 双拉相互作用系数 \(1-2^{-1/8}\) | [R10_FROZEN] | 否 |
| \(\mathbf E\) | 物理面内应变张量 | Nguyen 连续场输入 current operator | 否 |
| \(\mathbf E_u\) | R10 等效单轴应变张量 | [R10_FROZEN] | 否 |
| \(\mathbf X\) | 无量纲等效应变张量 | [R10_DERIVED] | 否 |
| \(\lambda_\pm\) | \(\mathbf X\) 的两个主值 | [MATHEMATICAL_IDENTITY] | 否 |
| \(\Pi_\eta\) | R10 平滑正部函数 | [R10_FROZEN] | 否 |
| \(C,T,T^7,U\) | R10 四个一维 primitive | [R10_FROZEN/R10_DERIVED] | 否 |
| \(\lambda_a,\lambda_b\) | 先验材料编译区间 | [COMPILER_CONTRACT] | 不得按实验结果调整 |
| \(\lambda_c,\lambda_h,\xi\) | 编译区间中心、半宽、标准坐标 | [MATHEMATICAL_IDENTITY] | 否 |
| \(N=48\) | 当前材料编译阶数 | [COMPILER_CONTRACT] | 否 |
| \(\theta_j,\lambda_j\) | 49 个 Chebyshev 材料根坐标 | [COMPILER_CONTRACT] | 否 |
| \(a_n^{(F,0)}\) | direct N48 基准系数 | [COMPILER_CONTRACT] | 否 |
| \(\mathbf H,\mathbf G,\mathbf d_F\) | C1 最小扰动约束对象 | [COMPILER_CONTRACT] | 否 |
| \(a_n^{(F,C1)}\) | U/C/T7 的 N48-C1 系数 | [COMPILER_CONTRACT] | 否 |
| \(a_n^{(T,MM)}\) | T 的 strict-C1 minimax 系数 | [COMPILER_CONTRACT] | 否 |
| \(\mathbf Y,K_1,K_2,A_n,B_n\) | Cayley–Hamilton 二维提升量 | [MATHEMATICAL_IDENTITY] | 否 |
| \(b,\ell,t_p\) | 完整代表半波宽度、长度、板厚 | [GEO_INPUT] | 否 |
| \(q_0\) | 初始缺陷无量纲幅值 | [GEO_INPUT/NGUYEN_SOURCE] | 否 |
| \(D\) | 平均轴向压缩广义变量 | [NGUYEN_SOURCE] | 求解未知量 |
| \(q\) | 加载后附加挠曲无量纲幅值 | [NGUYEN_SOURCE] | 求解未知量 |
| \(\chi_q\) | \(q_0q+q^2/2\) 二阶几何组合量 | [NGUYEN_SOURCE] | 否 |
| \(M_n,Z_k\) | D15 完整半波与厚度精确矩 | [MATHEMATICAL_IDENTITY/D15] | 否 |
| \(J_\Omega\) | 完整半波体积 Jacobian | [MATHEMATICAL_IDENTITY] | 否 |
| \(\rho_s,z_s,E_s,\varepsilon_y,f_y\) | 钢筋率、位置、模量、屈服应变、屈服强度 | [REBAR_SOURCE/MATERIAL_INPUT] | 否 |
| \(P_c,P_s,P\) | 混凝土、钢筋及总轴力 | 理论输出 | 不参与材料反标 |
| \(R_{q,c},R_{q,s},R_q\) | 混凝土、钢筋及总幅值残量 | 理论输出 | 不参与材料反标 |
| \(L\) | 平衡支上的轴力切向驻值函数 | [MATHEMATICAL_IDENTITY/NC_R1_GOVERNANCE] | 否 |
| \(\mathcal A\) | NC+Rebar 物理/来源可接受域 | [NC_R1_GOVERNANCE] | 否 |
| \(\Gamma_0\) | 与 \((0,0)\) 连通的主平衡支 | [NC_R1_GOVERNANCE] | 否 |
| \(g(s)\) | 轴力沿有向主支弧长的导数 | [NC_R1_GOVERNANCE] | 否 |
| \(R_{norm}\) | 无量纲平衡残量 | [NC_R1_GOVERNANCE] | 否 |
| \(L_{norm}\) | 无量纲极限残量 | [NC_R1_GOVERNANCE] | 否 |
| \(10^{-5}\) | \(R_{norm},L_{norm}\) 生产接受门 | [NC_R1_GOVERNANCE] | 不得按试验调节 |
| \(10^{-4}\) | 独立根后端重复性门 | [NC_R1_GOVERNANCE] | 不得按试验调节 |
| \(D_x,D_y,D_{\mu,eff},D_{66},H_{eff}\) | 当前 tangent 的 Zhou-form 方向/耦合稳定刚度 | [ZHOU_STABILITY] | 否 |

---

# 34 理论继承边界

本文正式理论成立时必须同时保持以下区分：

1. **R10 是普通混凝土 current material target。** N48-C1/MM 只负责有限解析表示，不取得新的材料理论身份。
2. **49 个 Chebyshev 坐标是材料坐标，不是空间积分点。**
3. **Cayley–Hamilton 是二维张量降阶恒等式，不是空间近似。**
4. **Nguyen 提供二阶连续运动学与初始缺陷耦合，不要求继承其历史 FE/Gauss production route。**
5. **D15 是精确矩数学引擎。** D15 数学正确不等于历史 UHPC Layer-0 材料正确；旧 UHPC Layer-0 不在本文理论中恢复。
6. **周思铭提供正交各向异性稳定刚度骨架和 Navier 解释语言。** 当前项目只把 R10 current tangent 映射为 \(D_x,D_y,H_{eff}\) 等等效稳定量，不搬用其组合墙截面常数，也不把 Zhou 变成第二套 \(P_u\) 求解器。
7. **NC-R1 是根生产拓扑合同。** 它规定哪一个数学驻值根具有 \(P_u\) 身份，但不修改 R10、N48、Nguyen 或 D15。
8. **正式结构空间积分始终为零。** 允许一维材料坐标上的系数生成/验证，但不允许正式空间 Gauss、Simpson、自适应积分、spatial Chebyshev collocation、material-point grid、spatial cells 或 adaptive subdivision。
9. **实验值不得参与材料参数调整、branch identification、root selection、求根初始目标或容差选择。**

---

# 35 最终正式理论链

将全文压缩，可写成如下唯一 governing chain：

\[
\boxed{
\begin{aligned}
&\{f_c,E_0,\varepsilon_0,\nu,\text{R10 frozen constants}\}\\
&\quad\rightarrow
\{U,C,T,T^7\}_{R10}\\
&\quad\rightarrow
\{a_n^{(U,C1)},a_n^{(C,C1)},a_n^{(T,MM)},a_n^{(T^7,C1)}\}_{n=0}^{48}\\
&\quad\rightarrow
\mathcal C_n(\mathbf Y)=A_n\mathbf I+B_n\mathbf Y\\
&\quad\rightarrow
\mathbf S(X,Y,\zeta;D,q)\\
&\quad\rightarrow
\{c_{ijk}\}\\
&\quad\rightarrow
\mathscr D[Q]=\sum c_{ijk}M_iM_jZ_k\\
&\quad\rightarrow
P(D,q),\ R_q(D,q),\ L(D,q)\\
&\quad\rightarrow
\mathcal A,
\quad
\Gamma_0=\operatorname{Conn}_{(0,0)}(\{R_q=0\}\cap\mathcal A)\\
&\quad\rightarrow
P_u=
\text{沿 }\Gamma_0\text{ 首先遇到的 }g:+\to-\text{ 局部最大值}.
\end{aligned}
}
\tag{152}
\]

式中，第一行表示普通混凝土材料和 R10 冻结输入；第二行表示闭式 R10 一维材料 primitive；第三行表示当前 N48-C1/MM 最终 49×4 材料系数；第四行表示 Cayley–Hamilton 二维提升；第五行表示 Nguyen 二阶连续完整半波上的 current stress field；第六行表示有限三角—厚度解析系数；第七行表示 D15 精确矩；第八行表示两自由度总荷载、平衡残量和极限函数；第九行表示 NC-R1 可接受主平衡支；第十行表示唯一生产极限承载力定义。

当前理论状态为

```text
R10 = GOVERNING / FROZEN
N48-C1/MM = GOVERNING
CAYLEY_HAMILTON = GOVERNING
NGUYEN_SECOND_ORDER = GOVERNING
D15 = GOVERNING
REBAR_SOURCE = GOVERNING UNDER ACTIVE BRANCH CONTRACT
ZHOU Dx-Dy-H = TANGENT-STABILITY ACCEPTANCE / INTERPRETATION
NC-R1 LIMIT-ROOT PRODUCTION CONTRACT = GOVERNING
FORMAL_SPATIAL_QUADRATURE = 0
CASE21 NEW INDEPENDENT REPRODUCTION UNDER NC-R1 = NOT EXECUTED IN THIS DOCUMENT
SWARTZ24 RECALCULATION = NOT AUTHORIZED IN THIS DOCUMENT
```

本文只完成正式理论写作与来源参数整理，不包含新的 Case21 数值求解，也不使用实验值对任何参数或根进行校准。
