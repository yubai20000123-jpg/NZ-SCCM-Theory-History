# NZ-SCCM Case21 N48-C1/MM + D15 自包含独立盲算合同 V2

**日期：2026-08-12**  
**用途：第二次空白聊天独立复算。**  
**本文件不提供任何 Case21 理论答案，不提供实验破坏荷载，不提供历史 Case21 根、荷载或路径。**

---

# 0. 隔离纪律

```text
只允许使用本文件
历史 Case21 D/q/Pu/root/path = 禁止
旧 direct-N48 Case21 结果 = 禁止
历史 FE/Gauss/Simpson 结果 = 禁止
实验荷载参与求解 = 禁止

正式空间 Gauss = 0
正式空间 Simpson = 0
正式空间 adaptive quadrature = 0
正式空间 Chebyshev collocation = 0
正式空间 material-point grid = 0
正式空间 cells = 0

材料坐标上的一维 N48 系数生成/验证点不是空间离散
```

如任何必要定义仍缺失，必须在**首次缺口**处报告 `BLOCKED`，不得从外部知识补齐。

---

# 1. Case21 原始输入

几何：

\[
b=\ell=1220\ {\rm mm},\qquad
t_p=19.30\ {\rm mm}.
\]

混凝土：

\[
f_c=21.23\ {\rm MPa},
\qquad
E_0=20321\ {\rm MPa},
\]

\[
\varepsilon_0=0.00209,
\qquad
\nu=0.18.
\]

初始缺陷：

\[
q_0=\frac1{400}=0.0025.
\]

钢筋总双向配筋率：

\[
\rho_{s,tot}=0.0075.
\]

两个方向均分：

\[
\rho_{s,x}=\rho_{s,y}=0.00375.
\]

Case21 采用中面单层钢筋：

\[
z_s=0,\qquad \zeta_s=0.
\]

钢筋材料：

\[
E_s=200000\ {\rm MPa},
\qquad
\varepsilon_y=0.00265,
\qquad
f_y=530\ {\rm MPa}.
\]

R10 固定常数：

\[
\rho=0.1,\qquad
m_t=-\frac7{90},
\qquad
\eta_r=0.05,
\qquad
u_r=0.03,
\]

\[
a_{cc}=0.1072329249362415,
\qquad
a_t=1-2^{-1/8}.
\]

本次 compiler 区间在求解前固定：

\[
\boxed{\lambda\in[\lambda_a,\lambda_b]=[-1.15,0.12]}.
\]

该区间是本盲算合同的先验输入，不允许根据求解答案或实验值调整。

---

# 2. R10 基本无量纲参数

\[
\boxed{
\kappa=\frac{E_0\varepsilon_0}{f_c}
}
\]

\[
\boxed{
x_{cr}=\frac{\rho}{\kappa}
}
\]

\[
\boxed{
\eta=\frac{x_{cr}}{20}
}
\]

---

# 3. 平滑正部函数 \(\Pi_\eta\)

对任意实数 \(z\)，定义

\[
\boxed{
\Pi_\eta(z)=
\frac{
z^2\left(\sqrt{z^2+\eta^2}+z\right)
}
{2(z^2+\eta^2)}
}
\]

对任意一维主等效应变 \(\lambda\)，定义

\[
\boxed{
c(\lambda)=\Pi_\eta(-\lambda),
\qquad
t(\lambda)=\Pi_\eta(\lambda)
}.
\]

---

# 4. R10 压缩 primitive

\[
\boxed{
C(\lambda)=
\frac{
\kappa c(\lambda)
}
{
1+(\kappa-2)c(\lambda)+c(\lambda)^2
}
}
\]

---

# 5. Foster 源拉伸函数：完整定义

定义

\[
r=\frac{t}{x_{cr}}.
\]

平滑铰函数为

\[
\boxed{
H(r,r_0)=
\frac12
\left[
(r-r_0)+\sqrt{(r-r_0)^2+\eta_r^2}
\right]
-
\frac12
\left[
-r_0+\sqrt{r_0^2+\eta_r^2}
\right]
}
\]

其中 \(r_0\) 为铰激活位置。

Foster 源拉伸利用函数：

\[
\boxed{
T_{src}(r)
=
r+(m_t-1)H(r,1)-m_tH(r,10)
}
\]

源归一化拉应力：

\[
\boxed{
u_{t,src}(t)
=
\rho\,T_{src}\!\left(\frac{t}{x_{cr}}\right)
}
\]

源材料功：

\[
\boxed{
W_{src}
=
\rho x_{cr}
\int_0^{10}T_{src}(r)\,dr
}
\]

该一维材料积分必须从上式重新计算。允许使用符号积分、高精度一维材料积分或直接对闭式 \(H\) 求原函数；这不是结构空间积分。

---

# 6. R10 拉伸 rise / fall / residual 的完整定义

定义上升支局部坐标

\[
\boxed{
\tau(t)=\frac{t}{x_{cr}}
}
\]

在

\[
0\le t\le x_{cr}
\]

时

\[
\boxed{
u_1(t)=
\rho\tau
+(10h-6\rho)\tau^3
+(8\rho-15h)\tau^4
+(6h-3\rho)\tau^5
}
\]

其中 \(\tau=\tau(t)\)。

定义下降支坐标

\[
\boxed{
s(t)=\frac{t-x_{cr}}{9x_{cr}}
}
\]

在

\[
x_{cr}<t\le10x_{cr}
\]

时

\[
\boxed{
u_2(t)
=
h+(u_r-h)
\left[
10s^3-15s^4+6s^5
\right]
}
\]

其中 \(s=s(t)\)。

R10 拉伸峰值由材料功闭合：

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
\]

完整拉伸归一化应力为

\[
\boxed{
u_{sm}(t)=
\begin{cases}
u_1(t),&0\le t\le x_{cr},\\[1mm]
u_2(t),&x_{cr}<t\le10x_{cr},\\[1mm]
u_r,&t>10x_{cr}.
\end{cases}
}
\]

因为 \(t(\lambda)=\Pi_\eta(\lambda)\ge0\)，不需要负 \(t\) 分支。

最终拉伸 primitive：

\[
\boxed{
T(\lambda)=
\frac{
u_{sm}[t(\lambda)]
}{\rho}
}
\]

独立七次 primitive：

\[
\boxed{
T^{(7)}(\lambda)=[T(\lambda)]^7
}
\]

current master：

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
\]

---

# 7. R10 严格 \(C^1\) 锚点

必须独立检查：

\[
\boxed{
U(0)=0,\qquad U'(0)=\kappa
}
\]

\[
\boxed{
C(0)=T(0)=T^{(7)}(0)=0
}
\]

\[
\boxed{
C'(0)=T'(0)=(T^{(7)})'(0)=0
}
\]

撇号均表示对真实材料坐标 \(\lambda\) 求导。

---

# 8. N48 标准坐标和 direct coefficients

\[
\lambda_c=\frac{\lambda_a+\lambda_b}{2},
\qquad
\lambda_h=\frac{\lambda_b-\lambda_a}{2},
\]

\[
\boxed{
\xi(\lambda)=
\frac{\lambda-\lambda_c}{\lambda_h}
}
\]

第一类 Chebyshev 多项式：

\[
\boxed{
\mathcal C_n(\xi)=\cos[n\arccos(\xi)]
}
\]

49 个材料根点：

\[
\boxed{
\theta_j=
\frac{(j+\frac12)\pi}{49},
\qquad
j=0,\ldots,48
}
\]

\[
\boxed{
\lambda_j=
\lambda_c+\lambda_h\cos\theta_j
}
\]

对

\[
F\in\{U,C,T,T^{(7)}\}
\]

direct N48 系数为

\[
\boxed{
a_n^{(F,0)}
=
\frac{2-\delta_{n0}}{49}
\sum_{j=0}^{48}
F(\lambda_j)\cos(n\theta_j),
\qquad n=0,\ldots,48
}
\]

---

# 9. N48-C1：\(\mathbf H,\mathbf G,\mathbf d_F\) 完整定义

定义

\[
V_{jn}=\cos(n\theta_j).
\]

则

\[
\boxed{
\mathbf H=\mathbf V^T\mathbf V
=
\operatorname{diag}
\left(
49,\frac{49}{2},\ldots,\frac{49}{2}
\right)
}
\]

以及

\[
\boxed{
\mathbf H^{-1}
=
\frac1{49}
\operatorname{diag}(1,2,\ldots,2)
}
\]

零点标准坐标：

\[
\boxed{
\xi_0=-\frac{\lambda_c}{\lambda_h}
}
\]

定义

\[
\boxed{
\mathbf G=
\begin{bmatrix}
\mathcal C_0(\xi_0)&\cdots&\mathcal C_{48}(\xi_0)\\
\lambda_h^{-1}\mathcal C_0'(\xi_0)&\cdots&
\lambda_h^{-1}\mathcal C_{48}'(\xi_0)
\end{bmatrix}
}
\]

其中 \(\mathcal C'_n\) 为对 \(\xi\) 的导数。

目标向量：

\[
\boxed{
\mathbf d_U=
\begin{bmatrix}0\\\kappa\end{bmatrix}
}
\]

\[
\boxed{
\mathbf d_C=
\mathbf d_T=
\mathbf d_{T^{(7)}}=
\begin{bmatrix}0\\0\end{bmatrix}
}
\]

对

\[
F\in\{U,C,T^{(7)}\}
\]

使用

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
\]

---

# 10. \(T\) strict-C1 constrained-minimax：生产数值合同

理论目标：

\[
\boxed{
\min_{\mathbf a\in\mathbb R^{49}}
\left\|
\sum_{n=0}^{48}a_n\mathcal C_n[\xi(\lambda)]
-
T_{R10}(\lambda)
\right\|_{L^\infty([\lambda_a,\lambda_b])}
}
\]

严格约束：

\[
\boxed{
\mathbf G\mathbf a=\mathbf d_T
}
\]

为使空白聊天得到可重复的数值系数，采用以下**确定性材料坐标 exchange contract**。这些坐标只属于一维材料系数生成，不是结构空间离散。

### 10.1 初始 material exchange set

取 \(N_0=4096\)，定义 Chebyshev–Lobatto 材料坐标

\[
\lambda_k^{(0)}
=
\lambda_c+\lambda_h
\cos\frac{k\pi}{N_0},
\qquad k=0,\ldots,N_0.
\]

将以下点强制加入集合：

- \(\lambda=0\)；
- 区间端点 \(\lambda_a,\lambda_b\)；
- 若位于区间内，满足 \(\Pi_\eta(\lambda)=x_{cr}\) 的正根；
- 若位于区间内，满足 \(\Pi_\eta(\lambda)=10x_{cr}\) 的正根。

### 10.2 每轮 LP

未知量为

\[
(a_0,\ldots,a_{48},E).
\]

最小化

\[
\boxed{\min E}
\]

对当前 exchange set 中每个 \(\lambda_k\) 施加

\[
-E
\le
\sum_{n=0}^{48}a_n\mathcal C_n[\xi(\lambda_k)]
-
T_{R10}(\lambda_k)
\le E
\]

并同时施加

\[
\mathbf G\mathbf a=\mathbf d_T.
\]

采用确定性 primal linear programming；若使用 SciPy，则指定 `scipy.optimize.linprog(method="highs")`。若环境无 HiGHS，可使用任一 LP 求解器，但必须满足下述残量门。

### 10.3 独立 verification material set

取 \(N_v=131072\)：

\[
\lambda_m^{(v)}
=
\lambda_c+\lambda_h
\cos\frac{m\pi}{N_v},
\qquad m=0,\ldots,N_v.
\]

加入与 10.1 相同的特殊材料点。

计算残差

\[
r(\lambda)=T_{48}(\lambda)-T_{R10}(\lambda).
\]

在 verification set 上找到全部离散局部极值候选；对每个候选相邻区间，用确定性 bounded scalar minimization 对 \(-|r(\lambda)|\) 做局部精化，得到材料残差极值候选。

### 10.4 exchange

若存在候选点满足

\[
|r(\lambda_*)|>E+10^{-10},
\]

则把最大违反点加入 exchange set，重新解 LP。

### 10.5 停止条件

同时满足：

\[
\max_{\lambda\in V_{verify}}|r(\lambda)|-E
\le10^{-10}
\]

以及

\[
\max_n|a_n^{(k)}-a_n^{(k-1)}|
\le10^{-12}
\]

连续两轮时停止。

最大 exchange 轮数为 50。超过 50 轮未满足则报告

```text
BLOCKED_AT_T_MINIMAX
```

不得擅自改阶次或松动 C1 约束。

### 10.6 接受门

最终必须报告：

\[
|T_{48}(0)|\le10^{-12},
\qquad
|T'_{48}(0)|\le10^{-12}.
\]

并报告最终

\[
E_\infty
=
\max_{\lambda\in V_{verify}}|r(\lambda)|.
\]

该门是工程可重复系数合同，不宣称 theorem-level 连续余项证书。

---

# 11. 最终四个 N48 primitive

统一记

\[
\mathbf a^{(F,*)}
=
\begin{cases}
\mathbf a^{(F,C1)},
&F\in\{U,C,T^{(7)}\},\\
\mathbf a^{(T,MM)},
&F=T.
\end{cases}
\]

\[
\boxed{
F_{48}(\lambda)
=
\sum_{n=0}^{48}
a_n^{(F,*)}
\mathcal C_n[\xi(\lambda)]
}
\]

必须输出完整 49×4 系数表，但不能从历史文件读取。

---

# 12. 二维等效应变 current-map

物理面内应变张量

\[
\mathbf E=
\begin{bmatrix}
\varepsilon_x&\gamma_{xy}/2\\
\gamma_{xy}/2&\varepsilon_y
\end{bmatrix}.
\]

等效单轴应变：

\[
\boxed{
\mathbf E_u=
\frac{(1-\nu)\mathbf E+
\nu\,\operatorname{tr}(\mathbf E)\mathbf I}
{1-\nu^2}
}
\]

\[
\boxed{
\mathbf X=\frac{\mathbf E_u}{\varepsilon_0}
}
\]

因此

\[
X_{11}
=
\frac{\varepsilon_x+\nu\varepsilon_y}
{(1-\nu^2)\varepsilon_0},
\]

\[
X_{22}
=
\frac{\nu\varepsilon_x+\varepsilon_y}
{(1-\nu^2)\varepsilon_0},
\]

\[
X_{12}
=
\frac{\gamma_{xy}}
{2(1+\nu)\varepsilon_0}.
\]

---

# 13. Cayley–Hamilton 二维提升

\[
\boxed{
\mathbf Y=
\frac{\mathbf X-\lambda_c\mathbf I}{\lambda_h}
}
\]

\[
K_1=\operatorname{tr}\mathbf Y,
\qquad
K_2=\det\mathbf Y.
\]

\[
\mathbf Y^2-K_1\mathbf Y+K_2\mathbf I=0.
\]

\[
\boxed{
\mathcal C_n(\mathbf Y)=A_n\mathbf I+B_n\mathbf Y
}
\]

初值：

\[
A_0=1,\ B_0=0,\qquad
A_1=0,\ B_1=1.
\]

递推：

\[
\boxed{
A_{n+1}=-2K_2B_n-A_{n-1}
}
\]

\[
\boxed{
B_{n+1}=2A_n+2K_1B_n-B_{n-1}
}
\]

从而

\[
\mathbf F_{48}
=
\sum_{n=0}^{48}
a_n^{(F,*)}
(A_n\mathbf I+B_n\mathbf Y).
\]

分别得到

\[
\mathbf U,\mathbf C,\mathbf T,\mathbf T^{(7)}.
\]

---

# 14. 二维应力张量

\[
\boxed{
\mathbf{CC}=\det(\mathbf C)\mathbf C
}
\]

\[
\boxed{
\mathbf{TC}
=
\mathbf C[
\operatorname{tr}(\mathbf T)\mathbf I-\mathbf T]
}
\]

\[
\boxed{
\mathbf{TT}
=
\det(\mathbf T)
[
\operatorname{tr}(\mathbf T^{(7)})\mathbf I-\mathbf T^{(7)}
]
}
\]

\[
\boxed{
\mathbf S
=
\mathbf U-a_{cc}\mathbf{CC}
+\mathbf{TC}
-\rho a_t\mathbf{TT}
}
\]

\[
\boxed{
\boldsymbol\sigma=f_c\mathbf S
}
\]

---

# 15. Nguyen 一个连续完整方形半波

\[
X=\frac{\pi x}{b},
\qquad
Y=\frac{\pi y}{\ell},
\qquad
\zeta=\frac{2z}{t_p}.
\]

\[
w_0=A_0\sin X\sin Y,
\qquad
w_1=A\sin X\sin Y.
\]

\[
q_0=A_0/b,\qquad q=A/b.
\]

定义

\[
\boxed{
C_m=
\frac{\pi^2}{\varepsilon_0}
\left(
q_0q+\frac12q^2
\right)
}
\]

\[
\boxed{
C_b=
\frac{\pi^2}{2\varepsilon_0}
\frac{t_p}{b}q
}
\]

归一化物理应变：

\[
\boxed{
e_x=
\nu D
+
C_m\cos^2X\sin^2Y
+
C_b\sin X\sin Y\,\zeta
}
\]

\[
\boxed{
e_y=
-D
+
C_m\sin^2X\cos^2Y
+
C_b\sin X\sin Y\,\zeta
}
\]

\[
\boxed{
g_{xy}
=
2C_m\sin X\cos X\sin Y\cos Y
-
2C_b\cos X\cos Y\,\zeta
}
\]

物理应变：

\[
\varepsilon_x=\varepsilon_0e_x,
\qquad
\varepsilon_y=\varepsilon_0e_y,
\qquad
\gamma_{xy}=\varepsilon_0g_{xy}.
\]

未知量只有

\[
\boxed{D,\ q}.
\]

---

# 16. D15 精确矩合同

任何待积量必须先化为有限解析系数

\[
\boxed{
Q(X,Y,\zeta)=
\sum_{i,j,k}
c_{ijk}
\mathcal C_i(\sin X)
\mathcal C_j(\sin Y)
\mathcal C_k(\zeta)
}
\]

定义

\[
\boxed{
M_n=
\begin{cases}
\pi,&n=0,\\
\dfrac{2\sin(n\pi/2)}{n},&n\ge1
\end{cases}
}
\]

\[
\boxed{
Z_k=
\begin{cases}
0,&k\ {\rm odd},\\
\dfrac{2}{1-k^2},&k\ {\rm even}
\end{cases}
}
\]

\[
\boxed{
\mathscr D[Q]
=
\sum_{i,j,k}
c_{ijk}M_iM_jZ_k
}
\]

允许用有限解析幂基/三角基/FFT **系数卷积**加速代数，但禁止在物理空间取样。任何后端都必须最终等价于上述有限矩收缩。

---

# 17. 混凝土轴力与幅值残量

\[
\boxed{
P_c=
-\frac{f_cbt_p}{2\pi^2}
\mathscr D[S_{yy}]
}
\]

定义归一化物理应变张量

\[
\mathbf e=\mathbf E/\varepsilon_0.
\]

等价地

\[
\boxed{
\mathbf e
=
(1+\nu)\mathbf X
-\nu\operatorname{tr}(\mathbf X)\mathbf I
}
\]

定义

\[
\boxed{
Q_q=
\mathbf S:\frac{\partial\mathbf e}{\partial q}
}
\]

\[
\boxed{
J_\Omega=
\frac{b\ell t_p}{2\pi^2}
}
\]

\[
\boxed{
R_{q,c}
=
f_c\varepsilon_0J_\Omega
\mathscr D[Q_q]
}
\]

---

# 18. Case21 中面单层钢筋的解析式

每方向配筋率

\[
\rho_s=0.00375.
\]

在钢筋保持弹性时，轴向钢筋力：

\[
\boxed{
P_s
=
\rho_sbt_pE_s\varepsilon_0
\left(
D-\frac{C_m}{4}
\right)
}
\]

中面单层两方向钢筋对 \(q\) 的广义功：

\[
\boxed{
R_{q,s}
=
\rho_st_pE_s\pi^2(q_0+q)b\ell
\left[
\frac{\varepsilon_0D(\nu-1)}4
+
\frac{9\pi^2}{32}
\left(
q_0q+\frac12q^2
\right)
\right]
}
\]

最终必须独立验证钢筋连续应变全域满足

\[
\max|\varepsilon_s|<\varepsilon_y.
\]

若不满足，则本合同缺少塑性钢筋支的生产定义，应报告

```text
BLOCKED_AT_STEEL_BRANCH
```

不得擅自创造塑性公式。

---

# 19. 总平衡与极限条件

\[
\boxed{
P(D,q)=P_c(D,q)+P_s(D,q)
}
\]

\[
\boxed{
R_q(D,q)=R_{q,c}(D,q)+R_{q,s}(D,q)
}
\]

平衡：

\[
\boxed{
R_q(D,q)=0
}
\]

定义同源导数

\[
P_{,D}=\frac{\partial P}{\partial D},
\qquad
P_{,q}=\frac{\partial P}{\partial q},
\]

\[
R_{q,D}=\frac{\partial R_q}{\partial D},
\qquad
R_{q,q}=\frac{\partial R_q}{\partial q}.
\]

生产导数只能来自同一个有限解析表达的解析求导或 forward automatic differentiation。

若使用 forward AD，每个标量 \(x\) 携带

\[
(x,x_{,D},x_{,q})
\]

并逐运算传播：

\[
(ab)_{,\alpha}=a_{,\alpha}b+ab_{,\alpha},
\]

\[
(a/b)_{,\alpha}
=
\frac{a_{,\alpha}b-ab_{,\alpha}}{b^2},
\]

以及链式法则；\(\alpha\in\{D,q\}\)。不得用有限差分生成生产导数。

极限函数：

\[
\boxed{
L(D,q)
=
P_{,D}R_{q,q}
-
P_{,q}R_{q,D}
}
\]

最终联立

\[
\boxed{
R_q(D,q)=0,
\qquad
L(D,q)=0
}
\]

得到 fresh 理论 \(D_u,q_u,P_u\)。

---

# 20. 连续 compiler-domain 证书

最终状态必须证明整个连续完整半波的两个主等效应变均满足

\[
\boxed{
-1.15\le\lambda_-(X,Y,\zeta)
\le
\lambda_+(X,Y,\zeta)
\le0.12
}
\]

不得通过有限物理空间点扫描作为正式证书。

允许的证书路径：

```text
continuous algebraic invariant bound
or
single-domain Bernstein coefficient envelope
or
another globally valid analytic bound
```

若无法仅在一个连续完整半波上给出全域证书，应报告

```text
BLOCKED_AT_CONTINUOUS_SPECTRAL_CERTIFICATE
```

不得用 spatial cells / subdomains / collocation 补救。

---

# 21. 输出要求

必须顺序输出：

1. \(\kappa,x_{cr},\eta\)；
2. \(H,T_{src},W_{src},h\) 的独立生成；
3. \(U,C,T,T^7\)；
4. 49×4 N48-C1/MM 系数；
5. 全部严格 C1 锚点残量；
6. T-minimax exchange 轮数、最终 \(E_\infty\)；
7. \(D,q,A,C_m,C_b\)；
8. 连续 compiler-domain 证书；
9. D15 的 \(\mathscr D[S_{yy}]\)、\(\mathscr D[Q_q]\)；
10. \(P_c,P_s,P\)；
11. \(R_{q,c},R_{q,s},R_q\)；
12. \(P_{,D},P_{,q},R_{q,D},R_{q,q}\)；
13. \(L\) 与归一化 \(L\)；
14. 连续钢筋应变证书；
15. 最终 `PASS / FAIL / BLOCKED` 与首次分歧层级。

理论 \(D_u,q_u,P_u\) 冻结后立即停止。**不得自行寻找实验值。**
