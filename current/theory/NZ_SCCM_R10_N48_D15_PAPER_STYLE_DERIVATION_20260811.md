# NZ-SCCM：闭式 R10 → N48 解析编译 → D15 精确矩的论文式理论推导

**日期：2026-08-11**  
**身份：CURRENT GOVERNING PAPER-STYLE DERIVATION**  
**目的：只说明“材料参数 → 闭式 R10 → N48 通用系数公式 → current-map 代数 → D15 精确矩”的理论链；不计算 Case21，不研究更高阶次，不列长小数系数表。**

---

## 1 理论路线与基本原则

普通混凝土的正式理论链写为

\[
\boxed{
\text{材料参数}
\rightarrow
\text{Foster 一维拉伸源函数}
\rightarrow
\text{R10 能量闭合}
\rightarrow
\{U,C,T,T^7\}
\rightarrow
N_M=48\text{ 有限解析编译}
\rightarrow
\text{二维 current-map 代数}
\rightarrow
\text{D15 完整半波精确矩}
}
\tag{1}
\]

式中，R10 为材料关系本身；N48 仅为把已经闭合的材料关系转换成可进入 D15 的有限解析表达；D15 为完整连续半波上的解析积分算子。N48 系数不是材料参数，也不需要在理论正文中逐项列出长小数。

正式空间边界保持

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
```

---

# 2 普通混凝土闭式 R10 材料关系

## 2.1 基本材料参数

定义

\[
\kappa=\frac{E_0\varepsilon_0}{f_c},
\qquad
\rho=0.1,
\qquad
x_{cr}=\frac{\rho}{\kappa},
\qquad
\eta=\frac{x_{cr}}{20}.
\tag{2}
\]

式中：

- \(f_c\) —— 混凝土单轴抗压强度；
- \(E_0\) —— 混凝土初始弹性模量；
- \(\varepsilon_0\) —— 压缩主曲线的参考应变；
- \(\nu\) —— 混凝土泊松比；
- \(\kappa\) —— 归一化初始切线斜率；
- \(\rho\) —— 拉伸标量的归一化强度尺度，当前固定为 0.1；
- \(x_{cr}\) —— 拉伸峰值附近的特征归一化应变坐标；
- \(\eta\) —— 正、负主应变平滑分离的固定尺度。

## 2.2 二维应变到主等效应变

采用工程剪应变 \(\gamma_{xy}\)，物理应变张量写为

\[
\mathbf E=
\begin{bmatrix}
\varepsilon_x & \gamma_{xy}/2\\
\gamma_{xy}/2 & \varepsilon_y
\end{bmatrix}.
\tag{3}
\]

等效单轴应变张量为

\[
\mathbf E_u=
\frac{(1-\nu)\mathbf E+\nu\,\operatorname{tr}(\mathbf E)\mathbf I}
{1-\nu^2},
\qquad
\mathbf X=\frac{\mathbf E_u}{\varepsilon_0}.
\tag{4}
\]

写成分量形式：

\[
X_{11}=\frac{\varepsilon_x+\nu\varepsilon_y}
{(1-\nu^2)\varepsilon_0},
\qquad
X_{22}=\frac{\nu\varepsilon_x+\varepsilon_y}
{(1-\nu^2)\varepsilon_0},
\tag{5}
\]

\[
X_{12}=\frac{\gamma_{xy}}
{2(1+\nu)\varepsilon_0}.
\tag{6}
\]

令

\[
\mu=\frac{X_{11}+X_{22}}2,
\qquad
\delta=\frac{X_{11}-X_{22}}2,
\qquad
r_X=\sqrt{\delta^2+X_{12}^2},
\tag{7}
\]

则两个主等效应变为

\[
\boxed{
\lambda_+=\mu+r_X,
\qquad
\lambda_-=\mu-r_X.
}
\tag{8}
\]

式中：

- \(\mathbf I\) —— 二阶单位张量；
- \(\mathbf E_u\) —— 等效单轴应变张量；
- \(\mathbf X\) —— 以 \(\varepsilon_0\) 归一化后的等效单轴张量；
- \(\lambda_+,\lambda_-\) —— \(\mathbf X\) 的两个主值；
- \(\mu\) —— 两个主值的平均量；
- \(\delta\) —— 对角分量半差；
- \(r_X\) —— 二维主值半径。

## 2.3 拉、压标量坐标

定义平滑正部函数

\[
\Pi_\eta(z)=
\frac{z^2\left(\sqrt{z^2+\eta^2}+z\right)}
{2(z^2+\eta^2)}.
\tag{9}
\]

对任一主方向 \(i\in\{+,-\}\)，定义

\[
\boxed{
c_i=\Pi_\eta(-\lambda_i),
\qquad
t_i=\Pi_\eta(\lambda_i).
}
\tag{10}
\]

式中，\(c_i\) 为压缩标量坐标，\(t_i\) 为拉伸标量坐标；二者由同一个平滑函数生成，不需要按空间位置建立 TT、TC、CC 材料分区。

## 2.4 压缩标量函数

采用闭式压缩函数

\[
\boxed{
C_i=
\frac{\kappa c_i}
{1+(\kappa-2)c_i+c_i^2}.
}
\tag{11}
\]

式中，\(C_i\) 为第 \(i\) 个主方向上的归一化压缩应力幅值。

---

# 3 Foster 拉伸源函数与 R10 能量闭合

## 3.1 Foster 一维拉伸源函数

定义

\[
r=\frac{t}{x_{cr}},
\qquad
m_t=-\frac7{90},
\qquad
\eta_r=0.05,
\tag{12}
\]

以及代数平滑函数

\[
H(r,r_0)=
\frac12\left[(r-r_0)+\sqrt{(r-r_0)^2+\eta_r^2}\right]
-
\frac12\left[-r_0+\sqrt{r_0^2+\eta_r^2}\right].
\tag{13}
\]

Foster 拉伸利用系数写为

\[
\boxed{
T_{src}(r)=
r+(m_t-1)H(r,1)-m_tH(r,10).
}
\tag{14}
\]

对应的归一化拉伸应力为

\[
\boxed{u_{t,src}(t)=\rho T_{src}(t/x_{cr}).}
\tag{15}
\]

式中：

- \(r\) —— 以 \(x_{cr}\) 归一化后的拉伸坐标；
- \(m_t\) —— Foster 软化段斜率参数；
- \(\eta_r\) —— Foster 代数转折的固定平滑宽度；
- \(r_0\) —— 转折位置，当前公式中分别取 1 和 10；
- \(T_{src}\) —— Foster 一维拉伸利用系数；
- \(u_{t,src}\) —— 进入 current operator 前的归一化拉伸应力标量。

## 3.2 源材料功

保留拉伸区间 \(0\le t\le10x_{cr}\)。定义源材料功

\[
\boxed{
W_{src}
=\int_0^{10x_{cr}}u_{t,src}(t)\,dt
=\rho x_{cr}\int_0^{10}T_{src}(r)\,dr.
}
\tag{16}
\]

式中，\(W_{src}\) 为 Foster 拉伸标量在保留区间内的归一化应力—应变功；它由源材料公式直接积分得到，不由结构承载力反标。

## 3.3 R10 上升支

在

\[
0\le t\le x_{cr},
\qquad
\tau=\frac{t}{x_{cr}},
\tag{17}
\]

设五次多项式

\[
u_1(\tau)=b_0+b_1\tau+b_2\tau^2+b_3\tau^3+b_4\tau^4+b_5\tau^5.
\tag{18}
\]

施加六个条件

\[
u_1(0)=0,
\qquad
\frac{du_1}{dt}(0)=\kappa,
\qquad
\frac{d^2u_1}{dt^2}(0)=0,
\tag{19}
\]

\[
u_1(1)=h,
\qquad
\frac{du_1}{d\tau}(1)=0,
\qquad
\frac{d^2u_1}{d\tau^2}(1)=0.
\tag{20}
\]

由于 \(\kappa x_{cr}=\rho\)，由式（19）有

\[
b_0=0,
\qquad
b_1=\rho,
\qquad
b_2=0.
\tag{21}
\]

再由式（20）解得

\[
\boxed{
b_3=10h-6\rho,\qquad
b_4=8\rho-15h,\qquad
b_5=6h-3\rho.}
\tag{22}
\]

因此

\[
\boxed{u_1(\tau)=
\rho\tau
+(10h-6\rho)\tau^3
+(8\rho-15h)\tau^4
+(6h-3\rho)\tau^5.}
\tag{23}
\]

式中，\(h\) 为 R10 拉伸支在 \(t=x_{cr}\) 处的峰值；\(b_0\sim b_5\) 不是独立拟合参数，而是由端点值、端点切线和端点曲率条件唯一确定。

## 3.4 R10 下降支

在

\[
x_{cr}\le t\le10x_{cr},
\qquad
s=\frac{t-x_{cr}}{9x_{cr}},
\tag{24}
\]

令残余拉伸水平为 \(u_r\)，并要求在 \(s=0\) 和 \(s=1\) 两端的一阶、二阶导数均为零。唯一五次平滑连接式为

\[
\boxed{u_2(s)=
h+(u_r-h)(10s^3-15s^4+6s^5).}
\tag{25}
\]

式中：

- \(s\) —— 下降支的局部无量纲坐标；
- \(u_r\) —— 在 \(t=10x_{cr}\) 处保留的归一化残余拉伸水平；
- \(10s^3-15s^4+6s^5\) —— 满足两端一阶、二阶导数均为零的五次平滑连接函数。

## 3.5 由材料功直接求峰值 h

由式（23），上升支材料功为

\[
\int_0^{x_{cr}}u_1(t)\,dt
=x_{cr}\left(\frac h2+\frac{\rho}{10}\right).
\tag{26}
\]

由式（25），下降支材料功为

\[
\int_{x_{cr}}^{10x_{cr}}u_2(t)\,dt
=\frac{9x_{cr}}2(h+u_r).
\tag{27}
\]

R10 要求总材料功等于 Foster 源材料功：

\[
\int_0^{x_{cr}}u_1(t)\,dt
+
\int_{x_{cr}}^{10x_{cr}}u_2(t)\,dt
=W_{src}.
\tag{28}
\]

将式（26）、式（27）代入式（28），得到

\[
W_{src}
=x_{cr}\left(5h+\frac{\rho}{10}+\frac92u_r\right).
\tag{29}
\]

故峰值 \(h\) 直接写成

\[
\boxed{
h=
\frac15\left(
\frac{W_{src}}{x_{cr}}
-\frac{\rho}{10}
-\frac92u_r
\right).
}
\tag{30}
\]

式中，\(h\) 完全由源材料功 \(W_{src}\)、特征坐标 \(x_{cr}\)、拉伸尺度 \(\rho\) 和残余水平 \(u_r\) 决定，不需要结构试验承载力参与。

## 3.6 R10 拉伸函数

定义

\[
u_{sm}(t)=
\begin{cases}
u_1(t/x_{cr}),&0\le t\le x_{cr},\\
u_2[(t-x_{cr})/(9x_{cr})],&x_{cr}<t\le10x_{cr}.
\end{cases}
\tag{31}
\]

则第 \(i\) 个主方向上的拉伸利用系数为

\[
\boxed{
T_i=\frac{u_{sm}(t_i)}{\rho}.
}
\tag{32}
\]

---

# 4 重新嵌入原二维 current material operator

## 4.1 一维 current master

每个主方向定义

\[
\boxed{
U_i=
\kappa\lambda_i-C_i+\kappa c_i+\rho T_i-\kappa t_i.
}
\tag{33}
\]

式中，\(U_i\) 为第 \(i\) 个主方向的归一化 current master；\(C_i\) 为压缩标量；\(T_i\) 为 R10 拉伸利用系数。

## 4.2 双轴相互作用

保持源 current operator 的相互作用形式

\[
\boxed{
s_+=U_+
-a_{cc}C_+^2C_-
+C_+T_-
-\rho a_tT_+T_-^8,}
\tag{34}
\]

\[
\boxed{
s_-=U_-
-a_{cc}C_-^2C_+
+C_-T_+
-\rho a_tT_-T_+^8.}
\tag{35}
\]

式中：

- \(s_+,s_-\) —— 两个主方向的归一化主应力；
- \(a_{cc}\) —— 源 current operator 中冻结的双压相互作用参数；
- \(a_t=1-2^{-1/8}\) —— 双拉相互作用参数；
- \(C_+^2C_-\)、\(C_-^2C_+\) —— 双压耦合项；
- \(C_+T_-\)、\(C_-T_+\) —— 拉压耦合项；
- \(T_+T_-^8\)、\(T_-T_+^8\) —— 双拉耦合项。

物理应力最终为

\[
\boldsymbol\sigma=f_c\mathbf S,
\tag{36}
\]

其中 \(\mathbf S\) 为由 \(s_+,s_-\) 谱返回得到的归一化应力张量。

---

# 5 N48：只把闭合材料写成一个有限解析公式

## 5.1 编译坐标

在所需主等效应变包络 \([\lambda_a,\lambda_b]\) 上定义

\[
\lambda_c=\frac{\lambda_a+\lambda_b}{2},
\qquad
\lambda_h=\frac{\lambda_b-\lambda_a}{2},
\tag{37}
\]

\[
\boxed{
\xi(\lambda)=\frac{\lambda-\lambda_c}{\lambda_h}\in[-1,1].
}
\tag{38}
\]

式中：

- \(\lambda_a,\lambda_b\) —— 当前结构问题所需的一维主等效应变编译区间下、上界；
- \(\lambda_c\) —— 编译区间中心；
- \(\lambda_h\) —— 编译区间半宽；
- \(\xi\) —— 映射到 \([-1,1]\) 的 Chebyshev 材料坐标。

为避免与拉伸利用系数 \(T\) 混淆，以下把第一类 Chebyshev 多项式记为 \(\mathcal C_n\)：

\[
\mathcal C_n(\xi)=\cos[n\arccos(\xi)],
\tag{39}
\]

\[
\mathcal C_0=1,
\qquad
\mathcal C_1=\xi,
\qquad
\mathcal C_{n+1}=2\xi\mathcal C_n-\mathcal C_{n-1}.
\tag{40}
\]

## 5.2 四个一维标量对象

N48 只编译

\[
\boxed{F\in\{U,C,T,T^7\}.}
\tag{41}
\]

对任一 \(F\)，写成

\[
\boxed{
F_{48}(\lambda)
=\sum_{n=0}^{48}a_n^{(F)}\mathcal C_n[\xi(\lambda)].
}
\tag{42}
\]

式中：

- \(F\) —— 待编译的一维闭式材料函数；
- \(F_{48}\) —— N48 有限解析表示；
- \(a_n^{(F)}\) —— 第 \(n\) 个 Chebyshev 编译系数；
- \(n\) —— 材料解析项编号，\(n=0,1,\ldots,48\)；
- \(N_M=48\) —— 当前冻结的材料编译阶次。

## 5.3 每一个系数的统一计算式

取 \(\mathcal C_{49}\) 的 49 个根点

\[
\theta_j=\frac{(j+\tfrac12)\pi}{49},
\qquad
\lambda_j=\lambda_c+\lambda_h\cos\theta_j,
\qquad
j=0,1,\ldots,48.
\tag{43}
\]

则所有系数统一由

\[
\boxed{
a_n^{(F)}=
\frac{2-\delta_{n0}}{49}
\sum_{j=0}^{48}
F(\lambda_j)\cos(n\theta_j),
\qquad
n=0,1,\ldots,48.
}
\tag{44}
\]

给出。

式中：

- \(j\) —— Chebyshev 根点编号；
- \(\theta_j\) —— 第 \(j\) 个角坐标；
- \(\lambda_j\) —— 第 \(j\) 个材料坐标；
- \(\delta_{n0}\) —— Kronecker 符号，\(n=0\) 时为 1，否则为 0；
- \(F(\lambda_j)\) —— 直接由式（11）、式（31）—式（33）等闭式材料公式算出的函数值。

特别地，

\[
a_0^{(F)}=\frac1{49}\sum_{j=0}^{48}F(\lambda_j),
\tag{45}
\]

\[
a_1^{(F)}=\frac2{49}\sum_{j=0}^{48}F(\lambda_j)\cos\theta_j,
\tag{46}
\]

\[
a_2^{(F)}=\frac2{49}\sum_{j=0}^{48}F(\lambda_j)\cos2\theta_j,
\tag{47}
\]

直至

\[
a_{48}^{(F)}=\frac2{49}\sum_{j=0}^{48}F(\lambda_j)\cos48\theta_j.
\tag{48}
\]

因此，“49 个系数”不是 49 个需要人工拟合的材料参数，而是同一个公式（44）在 \(n=0\sim48\) 上的 49 次直接计算结果。

---

# 6 每一个 N48 项如何进入二维 current-map

## 6.1 从标量坐标提升到二维矩阵坐标

定义

\[
\boxed{
\mathbf Y=\frac{\mathbf X-\lambda_c\mathbf I}{\lambda_h}.
}
\tag{49}
\]

则 \(\mathbf Y\) 的两个特征值就是 \(\xi_+,\xi_-\)。定义

\[
K_1=\operatorname{tr}\mathbf Y,
\qquad
K_2=\det\mathbf Y.
\tag{50}
\]

根据二维 Cayley–Hamilton 定理，

\[
\boxed{
\mathbf Y^2-K_1\mathbf Y+K_2\mathbf I=\mathbf0.
}
\tag{51}
\]

因此任意 \(\mathcal C_n(\mathbf Y)\) 都只需要写成

\[
\boxed{
\mathcal C_n(\mathbf Y)
=A_n(K_1,K_2)\mathbf I+B_n(K_1,K_2)\mathbf Y.
}
\tag{52}
\]

式中，\(A_n,B_n\) 为第 \(n\) 个矩阵 Chebyshev 项的两个标量系数函数。

## 6.2 A_n、B_n 的递推式

初值为

\[
A_0=1,\quad B_0=0,
\qquad
A_1=0,\quad B_1=1.
\tag{53}
\]

由

\[
\mathcal C_{n+1}(\mathbf Y)
=2\mathbf Y\mathcal C_n(\mathbf Y)-\mathcal C_{n-1}(\mathbf Y)
\tag{54}
\]

以及式（51）可得

\[
\boxed{
A_{n+1}=-2K_2B_n-A_{n-1},
}
\tag{55}
\]

\[
\boxed{
B_{n+1}=2A_n+2K_1B_n-B_{n-1}.
}
\tag{56}
\]

这两条递推式就是从第 0 项一直生成到第 48 项的完整矩阵代数。

## 6.3 单个材料系数项的进入方式

式（42）中的第 \(n\) 项为

\[
F_{48}^{(n)}
=a_n^{(F)}\mathcal C_n(\mathbf Y).
\tag{57}
\]

代入式（52）：

\[
\boxed{
F_{48}^{(n)}
=a_n^{(F)}A_n\mathbf I
+a_n^{(F)}B_n\mathbf Y.
}
\tag{58}
\]

因此每一个 \(a_n^{(F)}\) 的作用完全透明：它只分别乘到该阶的 \(A_n\) 和 \(B_n\) 上。求和后

\[
\boxed{
\mathbf F_{48}=A_F\mathbf I+B_F\mathbf Y,
}
\tag{59}
\]

其中

\[
\boxed{
A_F=\sum_{n=0}^{48}a_n^{(F)}A_n,
\qquad
B_F=\sum_{n=0}^{48}a_n^{(F)}B_n.
}
\tag{60}
\]

式中，\(A_F,B_F\) 分别为材料函数 \(F\) 在二维矩阵空间中的单位张量系数和 \(\mathbf Y\) 系数。

---

# 7 双轴相互作用也只做有限代数，不再重新拟合

由式（59）分别得到矩阵函数

\[
\mathbf U,\qquad \mathbf C,\qquad \mathbf T,\qquad \mathbf T^{(7)}.
\tag{61}
\]

在主方向对角基下，有恒等式

\[
\boxed{
\mathbf{CC}=\det(\mathbf C)\,\mathbf C,
}
\tag{62}
\]

\[
\boxed{
\mathbf{TC}=\mathbf C
\left[\operatorname{tr}(\mathbf T)\mathbf I-\mathbf T\right],
}
\tag{63}
\]

\[
\boxed{
\mathbf{TT}=\det(\mathbf T)
\left[\operatorname{tr}(\mathbf T^{(7)})\mathbf I-\mathbf T^{(7)}\right].
}
\tag{64}
\]

式中：

- \(\mathbf{CC}\) —— 对应主方向项 \((C_+^2C_-,\,C_-^2C_+)\)；
- \(\mathbf{TC}\) —— 对应主方向项 \((C_+T_-,\,C_-T_+)\)；
- \(\mathbf{TT}\) —— 对应主方向项 \((T_+T_-^8,\,T_-T_+^8)\)；
- \(\mathbf T^{(7)}\) —— 对一维函数 \(T^7\) 进行同一 N48 编译后得到的矩阵函数。

于是归一化 current 应力张量直接写成

\[
\boxed{
\mathbf S
=\mathbf U
-a_{cc}\mathbf{CC}
+\mathbf{TC}
-\rho a_t\mathbf{TT}.
}
\tag{65}
\]

式（65）与式（34）、式（35）完全对应，只是把两个主方向公式改写为不需要显式逐点求特征向量的二维矩阵代数。

---

# 8 从连续半波运动学进入 D15

## 8.1 完整半波坐标

采用一个连续完整半波，定义

\[
X=\frac{\pi x}{b},
\qquad
Y=\frac{\pi y}{\ell},
\qquad
\zeta=\frac{2z}{t_p},
\tag{66}
\]

则

\[
0\le X\le\pi,
\qquad
0\le Y\le\pi,
\qquad
-1\le\zeta\le1.
\tag{67}
\]

物理体积元为

\[
\boxed{
d\Omega
=J_\Omega\,dX\,dY\,d\zeta,
\qquad
J_\Omega=\frac{b\ell t_p}{2\pi^2}.
}
\tag{68}
\]

式中：

- \(x,y,z\) —— 板的物理空间坐标；
- \(b\) —— 半波横向宽度；
- \(\ell\) —— 半波轴向长度；
- \(t_p\) —— 混凝土板厚度；
- \(X,Y\) —— 完整半波无量纲平面坐标；
- \(\zeta\) —— 厚度无量纲坐标；
- \(J_\Omega\) —— 从 \((x,y,z)\) 到 \((X,Y,\zeta)\) 的体积 Jacobian。

Nguyen 二阶运动学给出连续应变场

\[
\mathbf E=\mathbf E(X,Y,\zeta;D,q),
\tag{69}
\]

进而通过式（4）得到

\[
\mathbf X=\mathbf X(X,Y,\zeta;D,q).
\tag{70}
\]

式中，\(D\) 为轴向广义压缩变量；\(q=A/b\) 为局部挠曲无量纲幅值；\(A\) 为当前局部挠曲幅值。

## 8.2 有限空间解析表达

将式（70）代入式（49）—式（65），所有保留项最终写成有限空间系数形式。对任一待积分量 \(Q\)，记

\[
\boxed{
Q(X,Y,\zeta)
=\sum_{i,j,k}c_{ijk}
\mathcal C_i(\sin X)
\mathcal C_j(\sin Y)
\mathcal C_k(\zeta).
}
\tag{71}
\]

式中：

- \(Q\) —— 任一需要进入结构积分的有限解析量，例如 \(S_{yy}\) 或 \(\mathbf S:\mathbf X_{,q}\)；
- \(c_{ijk}\) —— 由 Nguyen 运动学、N48 材料系数及 current-map 有限代数共同生成的空间解析系数；
- \(i,j,k\) —— 三个解析基方向上的项编号；
- \(\mathcal C_i(\sin X)\)、\(\mathcal C_j(\sin Y)\) —— 两个完整半波方向的有限解析基；
- \(\mathcal C_k(\zeta)\) —— 厚度方向有限解析基。

这里的 \(c_{ijk}\) 是解析系数，不是空间积分点值。

---

# 9 D15：每一个空间项如何被精确积分

## 9.1 完整半波基础矩

定义

\[
M_n=\int_0^\pi\mathcal C_n(\sin X)\,dX.
\tag{72}
\]

则

\[
\boxed{
M_n=
\begin{cases}
\pi,&n=0,\\
\dfrac{2\sin(n\pi/2)}{n},&n\ge1.
\end{cases}}
\tag{73}
\]

厚度方向定义

\[
Z_k=\int_{-1}^{1}\mathcal C_k(\zeta)\,d\zeta,
\tag{74}
\]

则

\[
\boxed{
Z_k=
\begin{cases}
0,&k\text{ 为奇数},\\
\dfrac{2}{1-k^2},&k\text{ 为偶数}.
\end{cases}}
\tag{75}
\]

式中，\(M_n\) 为完整半波方向的第 \(n\) 阶精确矩；\(Z_k\) 为厚度方向的第 \(k\) 阶精确矩。

## 9.2 单项进入 D15 的规则

对式（71）中的单独一项

\[
Q_{ijk}
=c_{ijk}\mathcal C_i(\sin X)
\mathcal C_j(\sin Y)
\mathcal C_k(\zeta),
\tag{76}
\]

其完整连续域积分严格等于

\[
\boxed{
\mathscr D[Q_{ijk}]
=c_{ijk}M_iM_jZ_k.
}
\tag{77}
\]

式中，\(\mathscr D[\cdot]\) 表示 D15 完整半波精确矩算子。

因此总量只需逐项相加：

\[
\boxed{
\mathscr D[Q]
=\sum_{i,j,k}c_{ijk}M_iM_jZ_k.
}
\tag{78}
\]

这就是“每一个 N48 材料项最终如何进入 D15”的核心：

\[
\boxed{
a_n^{(F)}
\rightarrow
(A_n,B_n)
\rightarrow
\mathbf F_{48}
\rightarrow
\mathbf S
\rightarrow
c_{ijk}
\rightarrow
c_{ijk}M_iM_jZ_k.}
\tag{79}
\]

全过程只是有限代数与精确矩收缩，不出现空间 Gauss 点、Simpson 点、材料点网格或空间子域切分。

---

# 10 轴力与幅值平衡量的 D15 表达

## 10.1 混凝土轴力

将归一化轴向应力场记为

\[
S_{yy}(X,Y,\zeta)
=\sum_{i,j,k}p_{ijk}
\mathcal C_i(\sin X)
\mathcal C_j(\sin Y)
\mathcal C_k(\zeta).
\tag{80}
\]

则按压缩为正的符号约定，混凝土轴力为

\[
\boxed{
P_c
=-f_cJ_\Omega
\sum_{i,j,k}p_{ijk}M_iM_jZ_k.
}
\tag{81}
\]

式中：

- \(P_c\) —— 混凝土承担的轴向力；
- \(p_{ijk}\) —— \(S_{yy}\) 的空间解析系数；
- \(f_c\) —— 将归一化应力恢复为物理应力的强度尺度；
- 负号 —— 与当前“压缩荷载取正”的轴力符号约定对应。

## 10.2 幅值平衡量

定义

\[
Q_q=\mathbf S:\mathbf X_{,q},
\tag{82}
\]

并写成

\[
Q_q
=\sum_{i,j,k}r_{ijk}
\mathcal C_i(\sin X)
\mathcal C_j(\sin Y)
\mathcal C_k(\zeta).
\tag{83}
\]

则混凝土对广义幅值 \(q\) 的平衡量为

\[
\boxed{
R_{q,c}
=f_c\varepsilon_0J_\Omega
\sum_{i,j,k}r_{ijk}M_iM_jZ_k.
}
\tag{84}
\]

式中：

- \(R_{q,c}\) —— 混凝土部分对局部幅值 \(q\) 的广义平衡量；
- \(\mathbf X_{,q}=\partial\mathbf X/\partial q\) —— 归一化等效应变张量对幅值变量的解析导数；
- \(r_{ijk}\) —— \(\mathbf S:\mathbf X_{,q}\) 的空间解析系数；
- 冒号“:” —— 二阶张量双重内积。

## 10.3 同源导数

由于 \(p_{ijk}\) 和 \(r_{ijk}\) 都由同一有限解析表达生成，故

\[
P_{c,D},\quad P_{c,q},\quad R_{q,c,D},\quad R_{q,c,q}
\tag{85}
\]

均可对系数表达直接求导，再使用完全相同的 \(M_iM_jZ_k\) 收缩。正式理论不需要有限差分导数。

---

# 11 与周思铭式理论表达的对应关系

经典板理论常把挠度写成模态级数

\[
w=\sum A_{mn}\phi_{mn}(x,y),
\tag{86}
\]

再将每一项的导数代入总势能，利用正交积分得到有限或无限代数式。当前 NZ-SCCM 的写法完全对应这一思想，但级数对象发生了变化：

\[
\boxed{
\underbrace{a_n^{(F)}}_{\text{材料解析系数}}
\times
\underbrace{\mathcal C_n}_{\text{材料解析基}}
\rightarrow
\underbrace{c_{ijk}}_{\text{结构空间解析系数}}
\times
\underbrace{\mathcal C_i(\sin X)\mathcal C_j(\sin Y)\mathcal C_k(\zeta)}_{\text{完整半波解析基}}
\rightarrow
\underbrace{M_iM_jZ_k}_{\text{精确积分矩}}.
}
\tag{87}
\]

因此理论正文真正需要展示的是：

1. 材料闭式参数关系；
2. 一个统一的 N48 系数计算式；
3. 一个统一的 Cayley–Hamilton 递推式；
4. 一个统一的 D15 精确矩公式。

不需要展示几十个或几百个长小数系数。

---

# 12 参数与符号总表

| 符号 | 含义 |
|---|---|
| \(f_c\) | 混凝土单轴抗压强度 |
| \(E_0\) | 混凝土初始弹性模量 |
| \(\varepsilon_0\) | 混凝土参考压缩应变 |
| \(\nu\) | 混凝土泊松比 |
| \(\kappa\) | 归一化初始切线斜率 \(E_0\varepsilon_0/f_c\) |
| \(\rho\) | 拉伸归一化强度尺度 |
| \(x_{cr}\) | 拉伸特征坐标 \(\rho/\kappa\) |
| \(\eta\) | 正负标量坐标平滑尺度 |
| \(\eta_r\) | Foster 转折平滑尺度 |
| \(m_t\) | Foster 软化段斜率参数 |
| \(W_{src}\) | Foster 拉伸标量保留区间的材料功 |
| \(h\) | R10 拉伸峰值，由材料功能量等价式唯一确定 |
| \(u_r\) | R10 保留的残余拉伸水平 |
| \(t_i,c_i\) | 第 \(i\) 主方向上的拉、压标量坐标 |
| \(T_i\) | R10 拉伸利用系数 |
| \(C_i\) | 归一化压缩应力幅值 |
| \(U_i\) | 一维 current master |
| \(a_{cc}\) | 双压相互作用参数 |
| \(a_t\) | 双拉相互作用参数 |
| \(\lambda_\pm\) | 两个主等效应变 |
| \(\lambda_a,\lambda_b\) | 一维材料编译区间下、上界 |
| \(\lambda_c,\lambda_h\) | 编译区间中心和半宽 |
| \(\xi\) | Chebyshev 材料坐标 |
| \(\mathcal C_n\) | 第 \(n\) 阶第一类 Chebyshev 多项式 |
| \(a_n^{(F)}\) | 函数 \(F\) 的第 \(n\) 个 N48 编译系数 |
| \(N_M\) | 材料解析编译阶次，当前固定 48 |
| \(\mathbf Y\) | 归一化到 Chebyshev 区间的二维等效应变矩阵 |
| \(K_1,K_2\) | \(\mathbf Y\) 的迹与行列式 |
| \(A_n,B_n\) | 第 \(n\) 阶矩阵 Chebyshev 项的 Cayley–Hamilton 两系数 |
| \(\mathbf S\) | 归一化二维 current 应力张量 |
| \(b\) | 完整半波横向宽度 |
| \(\ell\) | 完整半波轴向长度 |
| \(t_p\) | 混凝土板厚度 |
| \(X,Y,\zeta\) | 完整半波无量纲坐标 |
| \(D\) | 轴向广义压缩变量 |
| \(q\) | 局部挠曲无量纲幅值 \(A/b\) |
| \(c_{ijk}\) | 任一结构量的有限空间解析系数 |
| \(M_i,M_j\) | 两个完整半波方向的 D15 精确矩 |
| \(Z_k\) | 厚度方向 D15 精确矩 |
| \(J_\Omega\) | 无量纲坐标到物理体积的 Jacobian |
| \(P_c\) | 混凝土轴向力 |
| \(R_{q,c}\) | 混凝土局部幅值广义平衡量 |

---

# 13 最终紧凑公式链

整套理论可以压缩为四组公式。

**第一组：材料闭合**

\[
W_{src}=\rho x_{cr}\int_0^{10}T_{src}(r)dr,
\qquad
h=\frac15\left(\frac{W_{src}}{x_{cr}}-\frac{\rho}{10}-\frac92u_r\right),
\tag{88}
\]

\[
u_1=\rho\tau+(10h-6\rho)\tau^3+(8\rho-15h)\tau^4+(6h-3\rho)\tau^5,
\tag{89}
\]

\[
u_2=h+(u_r-h)(10s^3-15s^4+6s^5).
\tag{90}
\]

**第二组：N48 编译**

\[
F_{48}=\sum_{n=0}^{48}a_n^{(F)}\mathcal C_n(\xi),
\tag{91}
\]

\[
a_n^{(F)}=
\frac{2-\delta_{n0}}{49}
\sum_{j=0}^{48}F(\lambda_j)\cos(n\theta_j).
\tag{92}
\]

**第三组：二维 current-map**

\[
\mathcal C_n(\mathbf Y)=A_n\mathbf I+B_n\mathbf Y,
\tag{93}
\]

\[
A_{n+1}=-2K_2B_n-A_{n-1},
\qquad
B_{n+1}=2A_n+2K_1B_n-B_{n-1},
\tag{94}
\]

\[
\mathbf S=\mathbf U-a_{cc}\mathbf{CC}+\mathbf{TC}-\rho a_t\mathbf{TT}.
\tag{95}
\]

**第四组：D15 精确矩**

\[
Q=\sum c_{ijk}\mathcal C_i(\sin X)\mathcal C_j(\sin Y)\mathcal C_k(\zeta),
\tag{96}
\]

\[
\boxed{
\mathscr D[Q]=\sum c_{ijk}M_iM_jZ_k.
}
\tag{97}
\]

因此正式理论的核心不是一张长系数表，而是

\[
\boxed{
\text{闭式材料公式}
+\text{一个 N48 系数通式}
+\text{一个二维矩阵递推式}
+\text{一个 D15 精确矩通式}.
}
\tag{98}
\]

---

## 14 当前边界

本文只完成理论表达，不执行任何 Case21 数值闭合。当前不允许因为追求更小编译误差而自动提高 N48，也不允许把长小数 coefficient table 当作材料理论。后续若需要计算，必须直接使用本文公式链，不重新打开材料路线。