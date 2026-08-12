# NZ-SCCM NC + Rebar 正式闭合理论推导（Canonical）
## 材料参数 → R10 → N48-C1/MM → Cayley–Hamilton → Nguyen 二阶连续完整半波 → D15 广义精确矩 → Rebar → P、R_q、L → NC-R1 极限根

**日期：2026-08-12**  
**身份：CURRENT GOVERNING FORMAL THEORY-WRITING BASELINE — CANONICAL FORMAL CLOSURE**

本稿吸收独立理论审计的有效意见，只修复正式表达和接口闭合，不重新打开 R10，不提高 N48 阶数，不引入空间 Gauss/Simpson/材料点网格，不新建第二套极限承载力求解器。

---

# 0 基本思想与理论边界

当前轴压极限承载力理论的核心链为

\[
\boxed{
\text{材料/几何输入}
\rightarrow R10
\rightarrow N48\text{-}C1/MM
\rightarrow \mathrm{CH}
\rightarrow \mathrm{Nguyen\ 二阶连续完整半波}
\rightarrow \mathrm{D15\ 精确矩}
\rightarrow P(D,q),R_q(D,q),L(D,q)
\rightarrow P_u}
\tag{1}
\]

式中，R10 为当前冻结的普通混凝土 current material target；N48-C1/MM 为 48 阶有限材料解析编译层；CH 为二维 Cayley–Hamilton 张量提升；Nguyen 二阶连续完整半波为含初始缺陷的二阶运动学；D15 为精确三角—厚度矩引擎；\(D\) 为平均轴压广义变量；\(q\) 为加载后附加局部挠曲无量纲幅值；\(P\) 为代表半波平均轴向荷载观测量；\(R_q\) 为与 \(q\) 共轭的广义平衡残量；\(L\) 为 \(P\) 沿平衡支的切向驻值函数；\(P_u\) 为 NC-R1 生产定义下的极限承载力。

固定边界为

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
ACTIVE_MODE = m=1
KINEMATICS = NGUYEN_SECOND_ORDER
R10_MATERIAL_TARGET = FROZEN
N48_ORDER = 48
U_COMPILER  = N48-C1
C_COMPILER  = N48-C1
T7_COMPILER = N48-C1
T_COMPILER  = N48-C1-CONSTRAINED-MINIMAX
CAYLEY_HAMILTON = GOVERNING
EXACT_MOMENT_ENGINE = D15_GENERAL_TRIG_MOMENTS
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
STRUCTURAL_CALIBRATION = NO
```

这里“不依赖迭代得到极限承载力”的准确含义是：材料解析系数一旦由材料参数生成并冻结，结构层不再采用“加载步 → 空间积分点 → 材料历史更新”的推进方式，而直接形成有限的 \(P(D,q),R_q(D,q),L(D,q)\)；联合根可由 resultant、Gröbner/elimination、all-real-root isolation 等低维代数后端直接隔离。数学后端内部是否使用 Newton/exchange 等算法不改变理论的零空间离散和非加载步历史身份。

本文使用以下来源身份：

```text
[MATERIAL_INPUT]          材料输入
[GEO_INPUT]               几何输入
[R10_PROJECT_FROZEN]      当前项目冻结 R10 物理目标/常数
[R10_DERIVED]             R10 派生量
[COMPILER_CONTRACT]       N48-C1/MM 材料编译合同
[MATHEMATICAL_IDENTITY]   数学恒等式
[NGUYEN_SOURCE]           Nguyen 二阶运动学/钢筋来源物理
[D15_EXACT_MOMENT]        D15 历史精确三角矩
[PROJECT_REBAR_MAPPING]   当前连续/弥散钢筋解析映射
[NC_R1_GOVERNANCE]        NC-R1 根生产合同
[ZHOU_SOURCE]             周思铭正交各向异性稳定刚度语言
[PROJECT_ZHOU_AUDIT]      当前 current-tangent 的 Zhou-form 解析投影审计
```

---

# 1 普通混凝土基本材料参数

\[
\boxed{f_c,\qquad E_0,\qquad \varepsilon_0,\qquad \nu}
\tag{2}
\]

式中，\(f_c\) 为普通混凝土单轴抗压强度，MPa，[MATERIAL_INPUT]；\(E_0\) 为初始弹性模量，MPa，[MATERIAL_INPUT]；\(\varepsilon_0\) 为 R10 参考压缩应变，无量纲，[MATERIAL_INPUT]；\(\nu\) 为泊松比，无量纲，[MATERIAL_INPUT]。上述量不得由板级 \(P_u\) 反标。

\[
\boxed{\kappa=\frac{E_0\varepsilon_0}{f_c}}
\tag{3}
\]

式中，\(\kappa\) 为 R10 无量纲初始斜率，[R10_DERIVED]；\(E_0,\varepsilon_0,f_c\) 见式（2）。

\[
\boxed{\rho=0.1}
\tag{4}
\]

式中，\(\rho\) 为 R10 归一化拉伸强度尺度，[R10_PROJECT_FROZEN]；它不是结构承载力修正系数。

\[
\boxed{x_{cr}=\frac{\rho}{\kappa}}
\tag{5}
\]

式中，\(x_{cr}\) 为无量纲拉伸特征材料坐标，[R10_DERIVED]；\(\rho\) 与 \(\kappa\) 分别见式（4）、（3）。

\[
\boxed{\eta=\frac{x_{cr}}{20}}
\tag{6}
\]

式中，\(\eta\) 为 R10 零主应变附近的平滑尺度，[R10_DERIVED]。

---

# 2 二维应变与等效单轴应变

\[
\boxed{\mathbf E=
\begin{bmatrix}
\varepsilon_x&\gamma_{xy}/2\\
\gamma_{xy}/2&\varepsilon_y
\end{bmatrix}}
\tag{7}
\]

式中，\(\mathbf E\) 为二维物理面内应变张量；\(\varepsilon_x,\varepsilon_y\) 为法向应变；\(\gamma_{xy}\) 为工程剪应变，因此张量剪应变为 \(\gamma_{xy}/2\)。

\[
\boxed{\mathbf E_u=
\frac{(1-\nu)\mathbf E+\nu\operatorname{tr}(\mathbf E)\mathbf I}{1-\nu^2}}
\tag{8}
\]

式中，\(\mathbf E_u\) 为 R10 等效单轴应变张量，[R10_PROJECT_FROZEN]；\(\operatorname{tr}(\mathbf E)\) 为迹；\(\mathbf I\) 为二维单位张量；\(\nu\) 见式（2）。

\[
\boxed{\mathbf X=\frac{\mathbf E_u}{\varepsilon_0}}
\tag{9}
\]

式中，\(\mathbf X\) 为无量纲等效应变张量，[R10_DERIVED]；\(\varepsilon_0\) 见式（2）。

\[
\boxed{X_{11}=\frac{\varepsilon_x+\nu\varepsilon_y}{(1-\nu^2)\varepsilon_0},\qquad
X_{22}=\frac{\nu\varepsilon_x+\varepsilon_y}{(1-\nu^2)\varepsilon_0}}
\tag{10}
\]

式中，\(X_{11},X_{22}\) 为 \(\mathbf X\) 的两个法向分量；其余符号见式（2）、（7）。

\[
\boxed{X_{12}=X_{21}=\frac{\gamma_{xy}}{2(1+\nu)\varepsilon_0}}
\tag{11}
\]

式中，\(X_{12}\) 为等效应变剪切分量；式中 2 来自工程剪应变与张量剪应变换算。

\[
\boxed{\mu=\frac{X_{11}+X_{22}}2,\qquad
\delta=\frac{X_{11}-X_{22}}2,\qquad
r_X=\sqrt{\delta^2+X_{12}^2}}
\tag{12}
\]

式中，\(\mu\) 为主值均值；\(\delta\) 为两个法向分量半差；\(r_X\) 为二维对称张量主值半径，[MATHEMATICAL_IDENTITY]。

\[
\boxed{\lambda_\pm=\mu\pm r_X}
\tag{13}
\]

式中，\(\lambda_+,\lambda_-\) 分别为 \(\mathbf X\) 的较大与较小主值，[MATHEMATICAL_IDENTITY]。

---

# 3 R10 平滑拉压坐标与压缩 primitive

\[
\boxed{\Pi_\eta(z)=\frac{z^2(\sqrt{z^2+\eta^2}+z)}{2(z^2+\eta^2)}}
\tag{14}
\]

式中，\(z\) 为任意无量纲主应变坐标；\(\Pi_\eta(z)\ge0\) 为项目定义的 smooth nonnegative one-sided coordinate，[R10_PROJECT_FROZEN]；\(\eta\) 见式（6）。其满足 \(\Pi_\eta(0)=\Pi_\eta'(0)=0\)，正大 \(z\) 时渐近于 \(z\)，负大 \(z\) 时趋于 0；不宣称它是全域严格单调 softplus，也不要求 \(\Pi_\eta(z)-\Pi_\eta(-z)=z\)。

\[
\boxed{c(\lambda)=\Pi_\eta(-\lambda),\qquad t(\lambda)=\Pi_\eta(\lambda)}
\tag{15}
\]

式中，\(c(\lambda)\) 为平滑压缩坐标；\(t(\lambda)\) 为平滑拉伸坐标；二者均为非负材料坐标，[R10_DERIVED]。

\[
\boxed{C(\lambda)=\frac{\kappa c(\lambda)}{1+(\kappa-2)c(\lambda)+c(\lambda)^2}}
\tag{16}
\]

式中，\(C(\lambda)\) 为无量纲压缩 primitive，[R10_PROJECT_FROZEN]；\(\kappa\) 见式（3）；\(c(\lambda)\) 见式（15）。

---

# 4 Foster 源拉伸材料功与 R10 C2 重构

\[
\boxed{r=\frac{t}{x_{cr}}}
\tag{17}
\]

式中，\(r\) 为按 \(x_{cr}\) 归一化的拉伸材料坐标；\(t\) 见式（15）；\(x_{cr}\) 见式（5）。

\[
\boxed{m_t=-\frac7{90},\qquad \eta_r=0.05}
\tag{18}
\]

式中，\(m_t\) 为 source-informed Foster 下降段斜率参数；\(\eta_r\) 为源平滑铰宽度；二者属于 [R10_PROJECT_FROZEN]。

\[
\boxed{H(r,r_0)=\frac12[(r-r_0)+\sqrt{(r-r_0)^2+\eta_r^2}]-\frac12[-r_0+\sqrt{r_0^2+\eta_r^2}]}
\tag{19}
\]

式中，\(H(r,r_0)\) 为平滑铰函数；\(r_0\) 为铰中心，当前使用 \(1\) 与 \(10\)；\(\eta_r\) 见式（18）。

\[
\boxed{T_{src}(r)=r+(m_t-1)H(r,1)-m_tH(r,10)}
\tag{20}
\]

式中，\(T_{src}(r)\) 为 Foster 源拉伸利用函数；\(m_t,H\) 见式（18）、（19）。

\[
\boxed{u_{t,src}(t)=\rho T_{src}(t/x_{cr})}
\tag{21}
\]

式中，\(u_{t,src}\) 为源归一化拉应力；\(\rho\) 见式（4）；\(t/x_{cr}=r\)。

\[
\boxed{W_{src}=\int_0^{10x_{cr}}u_{t,src}(t)dt=\rho x_{cr}\int_0^{10}T_{src}(r)dr}
\tag{22}
\]

式中，\(W_{src}\) 为一维材料坐标上的源材料功，[R10_DERIVED]；该积分不是 \(x,y,z\) 结构空间求积。

\[
\boxed{\tau=\frac{t}{x_{cr}},\qquad0\le\tau\le1}
\tag{23}
\]

式中，\(\tau\) 为 R10 C2 上升段局部材料坐标。

\[
\boxed{u_1(\tau)=\rho\tau+(10h-6\rho)\tau^3+(8\rho-15h)\tau^4+(6h-3\rho)\tau^5}
\tag{24}
\]

式中，\(u_1\) 为上升段归一化拉应力；\(h\) 为待由材料功确定的峰值；\(\rho\) 见式（4）；\(\tau\) 见式（23）。

\[
\boxed{s=\frac{t-x_{cr}}{9x_{cr}},\qquad0\le s\le1}
\tag{25}
\]

式中，\(s\) 为下降段局部材料坐标。

\[
\boxed{u_r=0.03}
\tag{26}
\]

式中，\(u_r\) 为 R10 C2 重构的残余归一化拉应力，[R10_PROJECT_FROZEN]。

\[
\boxed{u_2(s)=h+(u_r-h)(10s^3-15s^4+6s^5)}
\tag{27}
\]

式中，\(u_2\) 为下降段归一化拉应力；\(h,u_r,s\) 分别见式（24）、（26）、（25）。

\[
\boxed{h=\frac15\left(\frac{W_{src}}{x_{cr}}-\frac{\rho}{10}-\frac92u_r\right)}
\tag{28}
\]

式中，\(h\) 为 R10 拉伸峰值，[R10_DERIVED]；\(W_{src}\) 见式（22）；\(x_{cr}\) 见式（5）；\(\rho\) 见式（4）；\(u_r\) 见式（26）。该值由材料功闭合，不使用板级承载力。

\[
\boxed{u_{sm}(t)=
\begin{cases}
u_1(t/x_{cr}),&0\le t\le x_{cr},\\
u_2[(t-x_{cr})/(9x_{cr})],&x_{cr}<t\le10x_{cr},\\
u_r,&t>10x_{cr}.
\end{cases}}
\tag{29}
\]

式中，\(u_{sm}\) 为完整 R10 C2 拉伸函数；\(u_1,u_2,u_r\) 分别见式（24）、（27）、（26）。

\[
\boxed{T(\lambda)=\frac{u_{sm}[\Pi_\eta(\lambda)]}{\rho}}
\tag{30}
\]

式中，\(T(\lambda)\) 为无量纲拉伸 primitive；\(u_{sm}\) 见式（29）；\(\Pi_\eta\) 见式（14）；\(\rho\) 见式（4）。

\[
\boxed{T^{(7)}(\lambda)=[T(\lambda)]^7}
\tag{31}
\]

式中，\(T^{(7)}\) 为双拉相互作用使用的独立七次 primitive。

---

# 5 一维 current master 与二维相互作用

\[
\boxed{U(\lambda)=\kappa\lambda-C(\lambda)+\kappa c(\lambda)+\rho T(\lambda)-\kappa t(\lambda)}
\tag{32}
\]

式中，\(U\) 为一维 current master；\(\kappa\) 见式（3）；\(C\) 见式（16）；\(c,t\) 见式（15）；\(T\) 见式（30）；\(\rho\) 见式（4）。

\[
\boxed{a_{cc}=0.1072329249362415}
\tag{33}
\]

式中，\(a_{cc}\) 为当前 NC 双压低参数物理目标系数，[R10_PROJECT_FROZEN]。项目冻结依据为：等双压目标点接触当前保守 CC 包络，同时保持单轴坐标轴不变；该值不是 Nguyen/Foster 原式中的 verbatim 常数，也不是用板级 \(P_u\) 反标的结构参数。

\[
\boxed{a_t=1-2^{-1/8}}
\tag{34}
\]

式中，\(a_t\) 为双拉低参数物理目标系数，[R10_PROJECT_FROZEN]；该取值保持单轴轴线不变，并定义当前 \(p=8\) 等双拉包络尺度。

\[
\boxed{s_+=U_+-a_{cc}C_+^2C_-+C_+T_- -\rho a_tT_+T_-^8}
\tag{35}
\]

式中，\(s_+\) 为 \(\lambda_+\) 主方向无量纲应力；\(U_+,C_+,T_+\) 为把 \(\lambda_+\) 代入式（32）、（16）、（30）所得；下标 \(-\) 类似；\(a_{cc},a_t,\rho\) 见式（33）、（34）、（4）。

\[
\boxed{s_-=U_- -a_{cc}C_-^2C_+ +C_-T_+ -\rho a_tT_-T_+^8}
\tag{36}
\]

式中，\(s_-\) 为 \(\lambda_-\) 主方向无量纲应力；其余符号同式（35）。

\[
\boxed{\sigma_\pm=f_cs_\pm}
\tag{37}
\]

式中，\(\sigma_\pm\) 为物理主应力，MPa；\(f_c\) 见式（2）；\(s_\pm\) 见式（35）、（36）。

\[
\boxed{U(0)=0,\qquad U'(0)=\kappa}
\tag{38}
\]

式中，撇号表示对真实材料坐标 \(\lambda\) 求导；\(\kappa\) 见式（3）。

\[
\boxed{C(0)=T(0)=T^{(7)}(0)=0}
\tag{39}
\]

式中，\(C,T,T^{(7)}\) 分别见式（16）、（30）、（31）。

\[
\boxed{C'(0)=T'(0)=[T^{(7)}]'(0)=0}
\tag{40}
\]

式中，导数均相对真实 \(\lambda\)；式（38）—（40）是 N48-C1/MM 的严格 C1 材料锚点。

---

# 6 N48 direct coefficient

\[
\boxed{\lambda\in[\lambda_a,\lambda_b],\qquad\lambda_a<\lambda_b}
\tag{41}
\]

式中，\(\lambda_a,\lambda_b\) 为结构计算前冻结的主等效应变材料编译域下、上界，[COMPILER_CONTRACT]；不得由试验荷载或历史根事后调整。

\[
\boxed{\lambda_c=\frac{\lambda_a+\lambda_b}{2},\qquad\lambda_h=\frac{\lambda_b-\lambda_a}{2}}
\tag{42}
\]

式中，\(\lambda_c\) 为 compiler 中心；\(\lambda_h>0\) 为半宽。

\[
\boxed{\xi(\lambda)=\frac{\lambda-\lambda_c}{\lambda_h}}
\tag{43}
\]

式中，\(\xi\in[-1,1]\) 为标准 Chebyshev 材料坐标。

\[
\boxed{\mathcal C_n(\xi)=\cos[n\arccos(\xi)]}
\tag{44}
\]

式中，\(\mathcal C_n\) 为第 \(n\) 阶第一类 Chebyshev 多项式；当前 \(n=0,\ldots,48\)。

\[
\boxed{\theta_j=\frac{(j+1/2)\pi}{49},\qquad\lambda_j=\lambda_c+\lambda_h\cos\theta_j,\quad j=0,\ldots,48}
\tag{45}
\]

式中，\(j\) 为材料节点索引；\(\theta_j\) 为 Chebyshev 根角度；\(\lambda_j\) 为一维材料坐标；它们不是结构空间积分点。

\[
\boxed{a_n^{(F,0)}=\frac{2-\delta_{n0}}{49}\sum_{j=0}^{48}F(\lambda_j)\cos(n\theta_j),\quad F\in\{U,C,T,T^{(7)}\}}
\tag{46}
\]

式中，\(a_n^{(F,0)}\) 为 primitive \(F\) 的 direct N48 第 \(n\) 阶系数；\(\delta_{n0}\) 为 Kronecker delta；\(F(\lambda_j)\) 来自闭式 R10。

\[
\boxed{F_{48}^{(0)}(\lambda)=\sum_{n=0}^{48}a_n^{(F,0)}\mathcal C_n[\xi(\lambda)]}
\tag{47}
\]

式中，\(F_{48}^{(0)}\) 为 direct N48 基准表示；当前只作为 C1/MM 的起点。

---

# 7 N48-C1 coefficient

\[
\boxed{V_{jn}=\cos(n\theta_j)}
\tag{48}
\]

式中，\(\mathbf V\) 为 \(49\times49\) Chebyshev 根点矩阵。

\[
\boxed{\mathbf H=\mathbf V^T\mathbf V=\operatorname{diag}\left(49,\frac{49}{2},\ldots,\frac{49}{2}\right)}
\tag{49}
\]

式中，\(\mathbf H\) 为 C1 最小扰动问题的正定权矩阵，[MATHEMATICAL_IDENTITY]。

\[
\boxed{\mathbf H^{-1}=\frac1{49}\operatorname{diag}(1,2,\ldots,2)}
\tag{50}
\]

式中，\(\mathbf H^{-1}\) 为式（49）的显式逆。

\[
\boxed{\xi_0=-\frac{\lambda_c}{\lambda_h}}
\tag{51}
\]

式中，\(\xi_0=\xi(0)\) 为零主等效应变在标准 compiler 区间中的位置。

\[
\boxed{\mathbf G=
\begin{bmatrix}
\mathcal C_0(\xi_0)&\cdots&\mathcal C_{48}(\xi_0)\\
\lambda_h^{-1}\mathcal C_0'(\xi_0)&\cdots&\lambda_h^{-1}\mathcal C_{48}'(\xi_0)
\end{bmatrix}}
\tag{52}
\]

式中，\(\mathbf G\) 为 \(2\times49\) C1 约束矩阵；第一行约束函数值；第二行约束真实 \(d/d\lambda\) 一阶导数；\(\lambda_h^{-1}\) 来自链式法则。

\[
\boxed{\mathbf d_U=(0,\kappa)^T,\qquad\mathbf d_C=\mathbf d_T=\mathbf d_{T^{(7)}}=(0,0)^T}
\tag{53}
\]

式中，\(\mathbf d_F\) 为各 primitive 的零点函数值/一阶导数目标，直接来自式（38）—（40）。

\[
\boxed{\mathbf a^{(F,C1)}=\mathbf a^{(F,0)}+\mathbf H^{-1}\mathbf G^T(\mathbf G\mathbf H^{-1}\mathbf G^T)^{-1}(\mathbf d_F-\mathbf G\mathbf a^{(F,0)})}
\tag{54}
\]

式中，\(\mathbf a^{(F,C1)}\) 为 \(F\in\{U,C,T^{(7)}\}\) 的 49 维最终 C1 系数；\(\mathbf a^{(F,0)}\) 见式（46）；\(\mathbf H,\mathbf G,\mathbf d_F\) 见式（49）、（52）、（53）。该式是严格凸二次最小扰动问题在等式约束下的唯一解。

---

# 8 T constrained-minimax 唯一生产系数

\[
\boxed{\mathcal F_T=\{\mathbf a\in\mathbb R^{49}:\mathbf G\mathbf a=\mathbf d_T\}}
\tag{55}
\]

式中，\(\mathcal F_T\) 为满足严格 \(T(0)=T'(0)=0\) 的 48 阶 coefficient 可行集。

\[
\boxed{p_{\mathbf a}(\lambda)=\sum_{n=0}^{48}a_n\mathcal C_n[\xi(\lambda)]}
\tag{56}
\]

式中，\(p_{\mathbf a}\) 为系数向量 \(\mathbf a\) 对应的 48 阶材料多项式；\(a_n\) 为第 \(n\) 个系数。

\[
\boxed{E_T^*=\min_{\mathbf a\in\mathcal F_T}\|p_{\mathbf a}-T_{R10}\|_{L^\infty([\lambda_a,\lambda_b])}}
\tag{57}
\]

式中，\(E_T^*\) 为严格 C1 条件下 degree-48 空间的主最小极大误差；\(T_{R10}\) 为式（30）的闭式 R10 拉伸 primitive。

\[
\boxed{\mathcal S_T^*=\{\mathbf a\in\mathcal F_T:\|p_{\mathbf a}-T_{R10}\|_\infty=E_T^*\}}
\tag{58}
\]

式中，\(\mathcal S_T^*\) 为所有 primary minimax 最优 coefficient 构成的闭凸集合。

先由式（54）同样生成 T 的 C1 参考向量 \(\mathbf a^{(T,C1)}\)，再定义唯一 production T coefficient

\[
\boxed{\mathbf a^{(T,MM)}=\underset{\mathbf a\in\mathcal S_T^*}{\operatorname{argmin}}\frac12(\mathbf a-\mathbf a^{(T,C1)})^T\mathbf H(\mathbf a-\mathbf a^{(T,C1)})}
\tag{59}
\]

式中，\(\mathbf a^{(T,MM)}\) 为最终唯一 T-minimax coefficient；\(\mathbf H\) 正定，因此 secondary objective 严格凸；该 tie-break 不改变主 minimax 最优值 \(E_T^*\)，也不增加材料机制或阶数。

\[
\boxed{\mathbf a^{(F,*)}=\begin{cases}\mathbf a^{(F,C1)},&F\in\{U,C,T^{(7)}\},\\\mathbf a^{(T,MM)},&F=T.\end{cases}}
\tag{60}
\]

式中，上标 \((*)\) 表示当前最终 governing coefficient identity。

\[
\boxed{F_{48}(\lambda)=\sum_{n=0}^{48}a_n^{(F,*)}\mathcal C_n[\xi(\lambda)]}
\tag{61}
\]

式中，\(F_{48}\) 为最终 48 阶一维材料解析 primitive。

\[
\boxed{E_F^{(0)}=\|F_{48}-F_{R10}\|_{L^\infty([\lambda_a,\lambda_b])}}
\tag{62}
\]

式中，\(E_F^{(0)}\) 为 primitive \(F\) 的全 compiler-hull 最大绝对值误差；它是材料表示审计量。

\[
\boxed{E_F^{(1)}=\lambda_h\|F_{48}'-F_{R10}'\|_{L^\infty([\lambda_a,\lambda_b])}}
\tag{63}
\]

式中，\(E_F^{(1)}\) 为尺度化全域一阶切线误差；\(\lambda_h\) 见式（42）。当前不新增未经审计的 theorem-level 全域硬阈值；保留既有 exact C1 anchor、near-zero T、O(1) coefficient、CH/D15 compatibility 和 current-tangent diagnostic 工程门，并要求新 compiler 区间重新报告式（62）—（63）。

---

# 9 Cayley–Hamilton 二维提升

\[
\boxed{\mathbf Y=\frac{\mathbf X-\lambda_c\mathbf I}{\lambda_h}}
\tag{64}
\]

式中，\(\mathbf Y\) 为标准化二维等效应变张量；\(\mathbf X\) 见式（9）；\(\lambda_c,\lambda_h\) 见式（42）。

\[
\boxed{K_1=\operatorname{tr}(\mathbf Y),\qquad K_2=\det(\mathbf Y)}
\tag{65}
\]

式中，\(K_1,K_2\) 分别为 \(\mathbf Y\) 的迹和行列式。

\[
\boxed{\mathbf Y^2-K_1\mathbf Y+K_2\mathbf I=\mathbf0}
\tag{66}
\]

式中，\(\mathbf0\) 为二维零张量；式（66）为二维 Cayley–Hamilton 恒等式。

\[
\boxed{\mathcal C_n(\mathbf Y)=A_n\mathbf I+B_n\mathbf Y}
\tag{67}
\]

式中，\(A_n=A_n(K_1,K_2)\)、\(B_n=B_n(K_1,K_2)\) 为 CH 标量系数。

\[
\boxed{A_0=1,\ B_0=0,\qquad A_1=0,\ B_1=1}
\tag{68}
\]

式中，\(A_0,B_0,A_1,B_1\) 对应 \(\mathcal C_0(\mathbf Y)=\mathbf I\)、\(\mathcal C_1(\mathbf Y)=\mathbf Y\)。

\[
\boxed{A_{n+1}=-2K_2B_n-A_{n-1}}
\tag{69}
\]

式中，\(A_{n+1}\) 为下一阶单位张量系数；\(K_2,B_n,A_{n-1}\) 见式（65）、（67）。

\[
\boxed{B_{n+1}=2A_n+2K_1B_n-B_{n-1}}
\tag{70}
\]

式中，\(B_{n+1}\) 为下一阶 \(\mathbf Y\) 系数；\(K_1,A_n,B_n,B_{n-1}\) 见式（65）、（67）。

\[
\boxed{\mathbf F_{48}^{(n)}=a_n^{(F,*)}(A_n\mathbf I+B_n\mathbf Y)}
\tag{71}
\]

式中，\(\mathbf F_{48}^{(n)}\) 为 primitive \(F\) 的第 \(n\) 个二维张量项；\(a_n^{(F,*)}\) 见式（60）。

\[
\boxed{\mathbf F_{48}=\sum_{n=0}^{48}\mathbf F_{48}^{(n)}=A_F\mathbf I+B_F\mathbf Y}
\tag{72}
\]

式中，\(\mathbf F_{48}\) 可为 \(\mathbf U,\mathbf C,\mathbf T,\mathbf T^{(7)}\)；\(A_F=\sum a_n^{(F,*)}A_n\)，\(B_F=\sum a_n^{(F,*)}B_n\)。

---

# 10 二维 current stress tensor

\[
\boxed{\mathbf{CC}=\det(\mathbf C)\mathbf C}
\tag{73}
\]

式中，\(\mathbf{CC}\) 为双压相互作用张量；\(\mathbf C\) 为二维压缩 primitive。

\[
\boxed{\mathbf{TC}=\mathbf C[\operatorname{tr}(\mathbf T)\mathbf I-\mathbf T]}
\tag{74}
\]

式中，\(\mathbf{TC}\) 为拉压相互作用张量；\(\mathbf T\) 为二维拉伸 primitive。

\[
\boxed{\mathbf{TT}=\det(\mathbf T)[\operatorname{tr}(\mathbf T^{(7)})\mathbf I-\mathbf T^{(7)}]}
\tag{75}
\]

式中，\(\mathbf{TT}\) 为双拉相互作用张量；\(\mathbf T^{(7)}\) 为独立七次拉伸二维 primitive。

\[
\boxed{\mathbf S=\mathbf U-a_{cc}\mathbf{CC}+\mathbf{TC}-\rho a_t\mathbf{TT}}
\tag{76}
\]

式中，\(\mathbf S\) 为无量纲 current stress tensor；\(\mathbf U,\mathbf{CC},\mathbf{TC},\mathbf{TT}\) 见式（72）—（75）；\(a_{cc},\rho,a_t\) 见式（33）、（4）、（34）。

\[
\boxed{\boldsymbol\sigma=f_c\mathbf S}
\tag{77}
\]

式中，\(\boldsymbol\sigma\) 为物理二维应力张量；\(f_c\) 见式（2）。所有 primitive 均为同一个 \(\mathbf Y\) 的多项式，因此彼此可交换；式（73）—（77）与主值式（35）—（37）严格等价。

---

# 11 Nguyen 二阶连续完整半波

\[
\boxed{X=\frac{\pi x}{b},\qquad Y=\frac{\pi y}{\ell},\qquad\zeta=\frac{2z}{t_p}}
\tag{78}
\]

式中，\(x,y,z\) 为物理坐标；\(b\) 为完整代表半波宽度；\(\ell\) 为半波轴向长度；\(t_p\) 为板厚，[GEO_INPUT]；\(X,Y\in[0,\pi]\)，\(\zeta\in[-1,1]\)。

\[
\boxed{w_0=A_0\sin X\sin Y,\qquad w_1=A\sin X\sin Y}
\tag{79}
\]

式中，\(w_0\) 为 stress-free initial imperfection；\(w_1\) 为加载后 added displacement；\(A_0,A\) 为对应物理幅值，[NGUYEN_SOURCE]。

\[
\boxed{q_0=\frac{A_0}{b},\qquad q=\frac{A}{b}}
\tag{80}
\]

式中，\(q_0\) 为初始缺陷比；\(q\) 为加载后附加挠曲广义变量；因此无载状态是 \((D,q)=(0,0)\)。

\[
\boxed{\chi_q=q_0q+\frac12q^2}
\tag{81}
\]

式中，\(\chi_q\) 为 Nguyen/von Kármán 二阶几何组合；\(q_0q\) 为初始缺陷—附加挠曲交叉项；\(q^2/2\) 为附加挠曲自身二阶项。

\[
\boxed{e_x^{(0)}=\nu D,\qquad e_y^{(0)}=-D}
\tag{82}
\]

式中，\(D>0\) 为平均轴向压缩广义变量；\(e_x^{(0)},e_y^{(0)}\) 为按 \(\varepsilon_0\) 归一化的基础膜应变。

\[
\boxed{C_{mx}=\frac{\pi^2}{\varepsilon_0}\chi_q,\quad C_{my}=\frac{\pi^2b^2}{\varepsilon_0\ell^2}\chi_q,\quad C_{mxy}=\frac{2\pi^2b}{\varepsilon_0\ell}\chi_q}
\tag{83}
\]

式中，\(C_{mx},C_{my},C_{mxy}\) 分别为两个法向及工程剪切二阶膜系数；\(b,\ell,\varepsilon_0,\chi_q\) 见式（78）、（2）、（81）。

\[
\boxed{C_{bx}=\frac{\pi^2t_p}{2\varepsilon_0b}q,\quad C_{by}=\frac{\pi^2t_pb}{2\varepsilon_0\ell^2}q,\quad C_{bxy}=-\frac{\pi^2t_p}{\varepsilon_0\ell}q}
\tag{84}
\]

式中，\(C_{bx},C_{by}\) 为法向弯曲系数；\(C_{bxy}\) 为工程剪切弯曲系数；负号来自 \(-2zw_{,xy}\) 约定。

\[
\boxed{e_x=\nu D+C_{mx}\cos^2X\sin^2Y+C_{bx}\sin X\sin Y\,\zeta}
\tag{85}
\]

式中，\(e_x=\varepsilon_x/\varepsilon_0\) 为归一化横向应变；各系数见式（82）—（84）。

\[
\boxed{e_y=-D+C_{my}\sin^2X\cos^2Y+C_{by}\sin X\sin Y\,\zeta}
\tag{86}
\]

式中，\(e_y=\varepsilon_y/\varepsilon_0\) 为归一化轴向应变。

\[
\boxed{g_{xy}=C_{mxy}\sin X\cos X\sin Y\cos Y+C_{bxy}\cos X\cos Y\,\zeta}
\tag{87}
\]

式中，\(g_{xy}=\gamma_{xy}/\varepsilon_0\) 为归一化工程剪应变。

\[
\boxed{\varepsilon_x=\varepsilon_0e_x,\qquad\varepsilon_y=\varepsilon_0e_y,\qquad\gamma_{xy}=\varepsilon_0g_{xy}}
\tag{88}
\]

式中，\(\varepsilon_0\) 见式（2）；\(e_x,e_y,g_{xy}\) 见式（85）—（87）。给定 \((D,q)\) 后，完整连续半波应变场唯一确定。

---

# 12 D15 广义三角—厚度精确矩

真正需要积分的任一标量 integrand 写成

\[
\boxed{Q(X,Y,\zeta)=\sum_{p,r,u,s,h}c_{prush}\sin^pX\cos^rX\sin^uY\cos^sY\zeta^h}
\tag{89}
\]

式中，\(Q\) 可为 \(S_{yy}\)、\(Q_q\) 或 Zhou modal second variation integrand；\(c_{prush}\) 为有限解析系数；\(p,r,u,s,h\) 为非负整数幂次。这里用 \(u\) 作为 \(Y\) 向正弦幂次索引，避免与结构广义变量 \(q\) 混淆。

\[
\boxed{J_{pr}=\int_0^\pi\sin^pX\cos^rX\,dX}
\tag{90}
\]

式中，\(J_{pr}\) 为 D15 一般面内三角精确矩；\(p,r\) 分别为正弦、余弦幂次，[D15_EXACT_MOMENT]。

\[
\boxed{J_{pr}=\begin{cases}0,&r\text{ 为奇数},\\B\!\left(\dfrac{p+1}{2},\dfrac{r+1}{2}\right),&r\text{ 为偶数}.\end{cases}}
\tag{91}
\]

式中，\(B(a,b)\) 为 Beta 函数；完整 \([0,\pi]\) 半波上的余弦奇次因对称性精确为零。

\[
\boxed{B(a,b)=\frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}}
\tag{92}
\]

式中，\(\Gamma\) 为 Gamma 函数；对当前非负整数幂，式（91）—（92）化为有理数与 \(\pi\) 的精确组合。

\[
\boxed{Z_h=\int_{-1}^{1}\zeta^h d\zeta=\begin{cases}0,&h\text{ 为奇数},\\\dfrac{2}{h+1},&h\text{ 为偶数}.\end{cases}}
\tag{93}
\]

式中，\(Z_h\) 为归一化厚度第 \(h\) 阶精确矩；\(h\) 为非负整数。

\[
\boxed{J_\Omega=\frac{b\ell t_p}{2\pi^2}}
\tag{94}
\]

式中，\(J_\Omega\) 为 \((X,Y,\zeta)\to(x,y,z)\) 的体积 Jacobian；\(b,\ell,t_p\) 见式（78）。

\[
\boxed{\mathscr D[Q]=\sum_{p,r,u,s,h}c_{prush}J_{pr}J_{us}Z_h}
\tag{95}
\]

式中，\(\mathscr D[Q]\) 为 \(Q\) 在标准完整半波域上的精确解析积分；\(J_{pr},J_{us},Z_h\) 见式（90）—（93）。

\[
\boxed{a_n^{(F,*)}\rightarrow a_n^{(F,*)}(A_n\mathbf I+B_n\mathbf Y)\rightarrow\mathbf F^{(n)}\rightarrow\mathbf S\rightarrow\{c_{prush}\}\rightarrow\{c_{prush}J_{pr}J_{us}Z_h\}}
\tag{96}
\]

式中，\(a_n^{(F,*)}\) 为第 \(n\) 个材料 coefficient；\(A_n,B_n,\mathbf Y\) 见式（64）—（71）；\(\mathbf F^{(n)}\) 为二维 primitive 项；\(\mathbf S\) 见式（76）；\(c_{prush}\) 为真正 scalar integrand 的有限三角—厚度系数。中间 \(Y_{xy},S_{xy}\) 可以含裸余弦；D15 不要求所有中间张量分量落入只含 \(\sin X,\sin Y\) 的 restricted basis。

因此正式结构身份仍为

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
```

---

# 13 混凝土轴向荷载与 q-残量

\[
\boxed{N_{y,c}(D,q)=-\frac1{b\ell}\int_{\Omega_h}\sigma_{yy}dV}
\tag{97}
\]

式中，\(N_{y,c}\) 为完整代表半波平均轴向膜力，N/mm；\(\Omega_h\) 为完整半波体积；\(\sigma_{yy}\) 为物理轴向应力；负号使压缩取正。它是当前降维理论的 load observable 定义，不宣称任意截面局部反力恒等于该值。

\[
\boxed{P_c=bN_{y,c}=-\frac1\ell\int_{\Omega_h}\sigma_{yy}dV}
\tag{98}
\]

式中，\(P_c\) 为混凝土平均轴向荷载观测量，N；\(b\) 为半波宽；\(N_{y,c}\) 见式（97）。

\[
\boxed{P_c=-\frac{f_cbt_p}{2\pi^2}\mathscr D[S_{yy}]}
\tag{99}
\]

式中，\(S_{yy}\) 为式（76）的无量纲轴向应力分量；\(f_c,b,t_p\) 见式（2）、（78）；\(\mathscr D\) 见式（95）。

\[
\boxed{\mathbf e=\frac{\mathbf E}{\varepsilon_0}}
\tag{100}
\]

式中，\(\mathbf e\) 为归一化物理应变张量；\(\mathbf E\) 见式（7）。

\[
\boxed{\mathbf e=(1+\nu)\mathbf X-\nu\operatorname{tr}(\mathbf X)\mathbf I}
\tag{101}
\]

式中，\(\mathbf X\) 见式（9）；\(\nu\) 见式（2）；式（101）为式（8）的代数逆关系。

\[
\boxed{Q_q=\mathbf S:\frac{\partial\mathbf e}{\partial q}}
\tag{102}
\]

式中，\(Q_q\) 为无量纲 q-广义功密度；\(\mathbf S\) 见式（76）；冒号为二阶张量双点积；\(\partial\mathbf e/\partial q\) 由 Nguyen 场解析求导。

\[
\boxed{R_{q,c}=f_c\varepsilon_0J_\Omega\mathscr D[Q_q]}
\tag{103}
\]

式中，\(R_{q,c}\) 为混凝土 q-广义残量，N·mm；\(f_c,\varepsilon_0,J_\Omega\) 见式（2）、（94）；\(\mathscr D[Q_q]\) 由式（95）精确计算。

---

# 14 钢筋 current operator 与解析闭合

\[
\boxed{E_s,\qquad f_y,\qquad\varepsilon_y,\qquad\varepsilon_f,\qquad\rho_{s,\alpha}^{(r)},\qquad z_s^{(r)}}
\tag{104}
\]

式中，\(E_s\) 为钢筋弹性模量，MPa；\(f_y\) 为屈服应力，MPa；\(\varepsilon_y\) 为屈服应变；\(\varepsilon_f\) 为来源定义的应变上限，[NGUYEN_SOURCE/MATERIAL_INPUT]；\(\rho_{s,\alpha}^{(r)}\) 为第 \(r\) 层、\(\alpha\) 方向的方向配筋率；\(z_s^{(r)}\) 为钢筋层相对板中面的物理位置。

\[
\boxed{\sigma_s(\varepsilon_s)=\begin{cases}E_s\varepsilon_s,&|\varepsilon_s|\le\varepsilon_y,\\f_y\operatorname{sgn}(\varepsilon_s),&\varepsilon_y<|\varepsilon_s|\le\varepsilon_f.\end{cases}}
\tag{105}
\]

式中，\(\sigma_s\) 为钢筋轴向应力；\(\varepsilon_s\) 为钢筋方向应变；\(\operatorname{sgn}\) 为符号函数；当前 post-yield tangent 为 0。超过 \(\varepsilon_f\) 时当前来源支耗尽，不临时创造新材料关系。

\[
\boxed{\mathbf n_\alpha=(\cos\theta_\alpha,\sin\theta_\alpha)^T}
\tag{106}
\]

式中，\(\mathbf n_\alpha\) 为钢筋方向单位向量；\(\theta_\alpha\) 为其相对 \(x\) 轴方向角。

\[
\boxed{\zeta_r=\frac{2z_s^{(r)}}{t_p},\qquad\varepsilon_{s,\alpha}^{(r)}=\mathbf n_\alpha^T\mathbf E(X,Y,\zeta_r)\mathbf n_\alpha}
\tag{107}
\]

式中，\(\zeta_r\) 为第 \(r\) 层归一化厚度位置；\(\varepsilon_{s,\alpha}^{(r)}\) 为该层该方向钢筋应变；\(\mathbf E\) 由式（7）、（85）—（88）确定。

\[
\boxed{\varepsilon_{s,\alpha}^{(r)}=\varepsilon_x\cos^2\theta_\alpha+\varepsilon_y\sin^2\theta_\alpha+\gamma_{xy}\sin\theta_\alpha\cos\theta_\alpha}
\tag{108}
\]

式中，\(\varepsilon_x,\varepsilon_y,\gamma_{xy}\) 见式（88）；\(\theta_\alpha\) 见式（106）。

\[
\boxed{t_{s,\alpha}^{(r)}=\rho_{s,\alpha}^{(r)}t_p}
\tag{109}
\]

式中，\(t_{s,\alpha}^{(r)}\) 为均匀弥散钢筋层的等效钢筋片厚，mm；\(\rho_{s,\alpha}^{(r)}\) 为方向配筋率；\(t_p\) 为板厚。[PROJECT_REBAR_MAPPING]

\[
\boxed{P_s(D,q)=-\sum_r\frac{t_{s,y}^{(r)}}{\ell}\int_0^b\int_0^\ell\sigma_{s,y}^{(r)}(x,y;D,q)\,dy\,dx}
\tag{110}
\]

式中，\(P_s\) 为全部 \(y\) 向钢筋的轴向荷载贡献，N；\(t_{s,y}^{(r)}\) 见式（109）；\(\sigma_{s,y}^{(r)}\) 由式（105）、（107）给出；\(b,\ell\) 见式（78）。该式是历史离散线族表达 \(-\sum A_{s,r}\ell^{-1}\int_{\Gamma_r}\sigma_sds\) 的均匀弥散等价形式。

\[
\boxed{R_{q,s}(D,q)=\sum_{r,\alpha}t_{s,\alpha}^{(r)}\int_0^b\int_0^\ell\sigma_{s,\alpha}^{(r)}\frac{\partial\varepsilon_{s,\alpha}^{(r)}}{\partial q}\,dy\,dx}
\tag{111}
\]

式中，\(R_{q,s}\) 为全部钢筋 q-广义残量，N·mm；\(r,\alpha\) 遍历钢筋层和方向；\(t_s\) 见式（109）；\(\sigma_s\) 见式（105）；\(\partial\varepsilon_s/\partial q\) 由式（107）解析求导。

若整个连续完整半波上的某钢筋层/方向都处在同一已支持材料支，式（110）—（111）的 integrand 为有限三角解析式，直接用式（89）—（95）闭合。若同一层在空间上跨越多个未预先闭合的钢筋材料支，则输出 `BLOCKED_AT_STEEL_BRANCH`，不得建立空间材料点或 cells。

---

# 15 总荷载、总平衡与极限函数

\[
\boxed{P(D,q)=P_c(D,q)+P_s(D,q)}
\tag{112}
\]

式中，\(P\) 为 NC+Rebar 总轴向荷载观测量；\(P_c\) 见式（99）；\(P_s\) 见式（110）。

\[
\boxed{R_q(D,q)=R_{q,c}(D,q)+R_{q,s}(D,q)}
\tag{113}
\]

式中，\(R_q\) 为总 q-广义平衡残量；\(R_{q,c}\) 见式（103）；\(R_{q,s}\) 见式（111）。

\[
\boxed{R_q(D,q)=0}
\tag{114}
\]

式中，式（114）为 q-广义平衡方程；它只定义数学平衡状态，不单独定义极限承载力。

\[
\boxed{P_D=\frac{\partial P}{\partial D},\quad P_q=\frac{\partial P}{\partial q},\quad R_{q,D}=\frac{\partial R_q}{\partial D},\quad R_{q,q}=\frac{\partial R_q}{\partial q}}
\tag{115}
\]

式中，四个偏导全部由同一个有限解析 \(P,R_q\) 表达解析求导或同表达 AD 得到。

\[
\boxed{L(D,q)=P_DR_{q,q}-P_qR_{q,D}}
\tag{116}
\]

式中，\(L\) 为轴力在平衡 level set 切向方向上的非归一化驻值函数；其几何意义见式（121）—（123）。

在材料 coefficients 冻结并且钢筋保持单一受支持支时，结构函数为有限二维代数式：

\[
\boxed{P(D,q)=\sum_{i,j}p_{ij}D^iq^j,\qquad R_q(D,q)=\sum_{i,j}r_{ij}D^iq^j}
\tag{117}
\]

式中，\(p_{ij},r_{ij}\) 为由材料 coefficients、几何、钢筋映射和 D15 精确矩一次性生成的有限常系数；\(i,j\) 为有限非负整数阶次。

\[
\boxed{L(D,q)=\sum_{i,j}\ell_{ij}D^iq^j}
\tag{118}
\]

式中，\(\ell_{ij}\) 由式（116）对式（117）解析求导并做有限多项式乘法生成。因此极限问题不是空间加载迭代问题，而是有限二维联合根问题。

---

# 16 NC-R1 可接受域、主平衡支和唯一极限根

\[
\boxed{\mathcal A=\{(D,q):D\ge0,\ q\ge0,\ P\ge0,\ \text{compiler/material/rebar/source gates all pass}\}}
\tag{119}
\]

式中，\(\mathcal A\) 为 NC-R1 可接受状态域；\(D\ge0\) 为当前单调轴压方向；\(q\ge0\) 为正初始缺陷 \(q_0>0\) 下同向附加挠曲；不得由实验/历史根定义人为 \(D_{max},q_{max}\)。

\[
\boxed{\mathcal E=\{(D,q):R_q(D,q)=0\}}
\tag{120}
\]

式中，\(\mathcal E\) 为全部数学平衡状态集合。

\[
\boxed{\nabla R_q=(R_{q,D},R_{q,q})\ne\mathbf0}
\tag{121}
\]

式中，\(\nabla R_q\) 为平衡残量梯度；非零为正则 level-set 条件。

\[
\boxed{\mathbf t_0=(R_{q,q},-R_{q,D})}
\tag{122}
\]

式中，\(\mathbf t_0\) 为 \(R_q=0\) 的非单位切向量，因为 \(\nabla R_q\cdot\mathbf t_0=0\)。

\[
\boxed{\nabla P\cdot\mathbf t_0=P_DR_{q,q}-P_qR_{q,D}=L}
\tag{123}
\]

式中，\(\nabla P=(P_D,P_q)\)；\(L\) 与式（116）相同。\(R_{q,q}=0\) 只使局部 \(q(D)\) 图表示失效，不使 level-set tangent 定义失效。

\[
\boxed{(D,q)=(0,0)}
\tag{124}
\]

式中，式（124）为无载参考点；\(q_0\) 已属于初始几何，因此不要求 \(q=q_0\)。

\[
\boxed{\Gamma_0=\operatorname{Conn}_{(0,0)}(\mathcal E\cap\mathcal A)}
\tag{125}
\]

式中，\(\Gamma_0\) 为包含无载点的可接受连通平衡支；\(\operatorname{Conn}_{(0,0)}\) 表示取相应 connected component。

\[
\boxed{\widehat{\mathbf t}=\pm\frac{(R_{q,q},-R_{q,D})}{\sqrt{R_{q,q}^2+R_{q,D}^2}}}
\tag{126}
\]

式中，\(\widehat{\mathbf t}\) 为单位有向切向量；在无载端选取使路径进入 \(D>0\) 的方向，随后保持方向连续。

\[
\boxed{g(s)=\frac{dP}{ds}=\nabla P\cdot\widehat{\mathbf t}}
\tag{127}
\]

式中，\(s\) 为沿 \(\Gamma_0\) 的有向弧长；\(g(s)\) 为轴力沿主支的一阶导数。

\[
\boxed{g(s)=0\iff L(D,q)=0}
\tag{128}
\]

式中，该等价在正则主支点成立，因为 \(\widehat{\mathbf t}\) 与 \(\mathbf t_0\) 仅差非零归一化因子。

\[
\boxed{g(s_u^-)>0,\qquad g(s_u^+)<0}
\tag{129}
\]

式中，\(s_u^-\)、\(s_u^+\) 为候选驻值点加载方向前、后邻域；式（129）定义 \(+\to-\) 局部最大值。

\[
\boxed{\mathcal M=\{s_i>0:R_q=0,\ L=0,\ g:+\to-\}}
\tag{130}
\]

式中，\(\mathcal M\) 为主支全部可接受局部最大值弧长位置集合。

\[
\boxed{s_u=\min\mathcal M}
\tag{131}
\]

式中，\(s_u\) 为从无载状态首先遇到的可接受局部最大值位置。

\[
\boxed{(D_u,q_u)=\Gamma_0(s_u),\qquad P_u=P(D_u,q_u)}
\tag{132}
\]

式中，\(D_u,q_u\) 为生产极限点；\(P_u\) 为当前 NC-R1 唯一极限承载力。

\[
\boxed{\nabla R_q=\mathbf0}
\tag{133}
\]

式中，若式（133）在首个 admissible maximum 前出现并导致支路拓扑无法按现有合同唯一解析，则输出 `BLOCKED_AT_PRIMARY_BRANCH_SINGULARITY`，不得用最大荷载、试验最近或历史根最近规则选支。

---

# 17 NC-R1 残量、坐标重标度与根重复性

\[
\boxed{R_{mat}=f_c\varepsilon_0J_\Omega}
\tag{134}
\]

式中，\(R_{mat}\) 为 q-广义残量自然功尺度，N·mm；\(f_c,\varepsilon_0,J_\Omega\) 见式（2）、（94）。

\[
\boxed{R_{norm}=\frac{|R_q|}{\max(R_{mat},|R_{q,c}|+|R_{q,s}|)}}
\tag{135}
\]

式中，\(R_{norm}\) 为无量纲平衡残量；\(R_q,R_{q,c},R_{q,s}\) 见式（113）、（103）、（111）。

\[
\boxed{R_{norm}\le10^{-5}}
\tag{136}
\]

式中，\(10^{-5}\) 为 NC-R1 工程平衡数值门，不是材料参数。

\[
\boxed{L_{norm}=\frac{P_DR_{q,q}-P_qR_{q,D}}{|P_DR_{q,q}|+|P_qR_{q,D}|}}
\tag{137}
\]

式中，\(L_{norm}\) 为无量纲极限残量；分子即 \(L\)；分母为两个相消大项的自然尺度。

\[
\boxed{|L_{norm}|\le10^{-5}}
\tag{138}
\]

式中，\(10^{-5}\) 为冻结的极限条件数值门。

\[
\boxed{D'=aD,\qquad q'=b_q q,\qquad a>0,\quad b_q>0}
\tag{139}
\]

式中，\(D',q'\) 为重标度坐标；\(a,b_q\) 为任意正比例因子；\(b_q\) 与板宽 \(b\) 无关。

\[
\boxed{\widetilde R(D',q')=R_q(D'/a,q'/b_q)}
\tag{140}
\]

式中，\(\widetilde R\) 是同一平衡零集合的 scalar defining function 在新坐标中的重表达；这里没有重新定义新的能量共轭残量。

\[
\boxed{P_{D'}=\frac1aP_D,\quad P_{q'}=\frac1{b_q}P_q,\quad\widetilde R_{,D'}=\frac1aR_{q,D},\quad\widetilde R_{,q'}=\frac1{b_q}R_{q,q}}
\tag{141}
\]

式中，各偏导按新坐标求导；由此式（137）分子和分母共同乘 \(1/(ab_q)\)。若改用新能量共轭力 \(R_{q'}=R_q/b_q\)，则两项共同再乘 \(1/b_q\)，最终归一化结论仍相同。

\[
\boxed{L_{norm}'=L_{norm}}
\tag{142}
\]

式中，\(L_{norm}'\) 为新坐标下按同一 convention 计算的归一化极限残量。

在当前 \(q_0>0\) 生产合同下：

\[
\boxed{d_{ij}=\max\left(|D_i-D_j|,\frac{|q_i-q_j|}{q_0},\frac{|P_i-P_j|}{\max(|P_i|,|P_j|,1\,\mathrm{kN})}\right)}
\tag{143}
\]

式中，\(d_{ij}\) 为两个独立低维后端候选根的无量纲综合距离；下标 \(i,j\) 表示两个后端；\(q_0>0\) 见式（80）。

\[
\boxed{d_{ij}\le10^{-4}}
\tag{144}
\]

式中，\(10^{-4}\) 为冻结的根重复性门；不满足时不得取平均。

---

# 18 周思铭/Navier current-tangent 广义模态审计

周思铭原博士论文在 §4.2.3 中把 \(D_x\) 定义为次方向抗弯刚度，并定义

\[
H=D_{xy}+D_\mu,
\]

其中 \(D_{xy}\) 为不考虑泊松比的自由扭转刚度，\(D_\mu\) 为泊松效应附加刚度；第 5 章四边简支稳定理论继续以 \(D_x,D_y,H\) 的方向刚度组合控制稳定。当前项目只继承这一正交各向异性/Navier 稳定语言，不搬用周思铭组合墙的截面常数。

\[
\boxed{\mathbb C_t(X,Y,\zeta;D,q)=\frac{\partial\boldsymbol\sigma}{\partial\mathbf E}}
\tag{145}
\]

式中，\(\mathbb C_t\) 为与式（77）同源的二维 current tangent field；其随 \(X,Y,\zeta,D,q\) 变化，[PROJECT_ZHOU_AUDIT]。

\[
\boxed{\varphi(X,Y)=\sin X\sin Y}
\tag{146}
\]

式中，\(\varphi\) 为当前完整代表半波的基本 Navier 微扰形函数。[ZHOU_SOURCE/PROJECT_ZHOU_AUDIT]

\[
\boxed{\alpha=\frac{\pi}{b},\qquad\beta=\frac{\pi}{\ell}}
\tag{147}
\]

式中，\(\alpha,\beta\) 分别为 \(x,y\) 方向基本波数，mm\(^{-1}\)；\(b,\ell\) 见式（78）。

\[
\boxed{\varphi_{,x}=\alpha\cos X\sin Y,\qquad\varphi_{,y}=\beta\sin X\cos Y}
\tag{148}
\]

式中，\(\varphi_{,x},\varphi_{,y}\) 为对物理坐标 \(x,y\) 的一阶导数。

\[
\boxed{\varphi_{,xx}=-\alpha^2\varphi,\qquad\varphi_{,yy}=-\beta^2\varphi,\qquad\varphi_{,xy}=\alpha\beta\cos X\cos Y}
\tag{149}
\]

式中，\(\varphi_{,xx},\varphi_{,yy},\varphi_{,xy}\) 为物理二阶导数。

\[
\boxed{\mathbf b_\varphi=-z\begin{bmatrix}\varphi_{,xx}\\\varphi_{,yy}\\2\varphi_{,xy}\end{bmatrix}}
\tag{150}
\]

式中，\(\mathbf b_\varphi\) 为单位物理微扰幅值产生的弯曲工程应变向量，量纲 mm\(^{-1}\)；\(z=t_p\zeta/2\)；第三分量中的 2 为工程剪切曲率约定。

\[
\boxed{K_{Z,c}^{mat}=\int_{\Omega_h}\mathbf b_\varphi^T\mathbf C_t^{eng}\mathbf b_\varphi dV}
\tag{151}
\]

式中，\(K_{Z,c}^{mat}\) 为混凝土 material-tangent 模态刚度，N/mm；\(\mathbf C_t^{eng}\) 为式（145）按 \((\varepsilon_x,\varepsilon_y,\gamma_{xy})\to(\sigma_x,\sigma_y,\tau_{xy})\) 写成的工程切线矩阵。

\[
\boxed{K_{Z,c}^{geo}=\int_{\Omega_h}(\sigma_x\varphi_{,x}^2+2\tau_{xy}\varphi_{,x}\varphi_{,y}+\sigma_y\varphi_{,y}^2)dV}
\tag{152}
\]

式中，\(K_{Z,c}^{geo}\) 为混凝土 current-stress 几何模态刚度，N/mm；\(\sigma_x,\sigma_y,\tau_{xy}\) 来自式（77）；\(\varphi_{,x},\varphi_{,y}\) 见式（148）。

\[
\boxed{E_{s,t}^{(r,\alpha)}=\frac{d\sigma_{s,\alpha}^{(r)}}{d\varepsilon_{s,\alpha}^{(r)}}}
\tag{153}
\]

式中，\(E_{s,t}^{(r,\alpha)}\) 为钢筋当前一维 tangent；弹性支为 \(E_s\)，当前理想塑性支为 0。

设单位微扰曲率张量为

\[
\boxed{\boldsymbol\kappa_\varphi=-\begin{bmatrix}\varphi_{,xx}&\varphi_{,xy}\\\varphi_{,xy}&\varphi_{,yy}\end{bmatrix}}
\tag{154}
\]

式中，\(\boldsymbol\kappa_\varphi\) 为微扰模态曲率张量；其分量由式（149）确定。

\[
\boxed{K_{Z,s}^{mat}=\sum_{r,\alpha}t_{s,\alpha}^{(r)}\int_A E_{s,t}^{(r,\alpha)}[z_s^{(r)}\mathbf n_\alpha^T\boldsymbol\kappa_\varphi\mathbf n_\alpha]^2dA}
\tag{155}
\]

式中，\(K_{Z,s}^{mat}\) 为钢筋 material-tangent 模态刚度；\(t_s\) 见式（109）；\(A=[0,b]\times[0,\ell]\) 为半波中面；\(z_s^{(r)}\) 见式（104）；\(\mathbf n_\alpha\) 见式（106）。

\[
\boxed{K_{Z,s}^{geo}=\sum_{r,\alpha}t_{s,\alpha}^{(r)}\int_A\sigma_{s,\alpha}^{(r)}(\mathbf n_\alpha\cdot\nabla\varphi)^2dA}
\tag{156}
\]

式中，\(K_{Z,s}^{geo}\) 为钢筋 current-stress 几何模态刚度；\(\nabla\varphi=(\varphi_{,x},\varphi_{,y})\)。

\[
\boxed{K_Z=K_{Z,c}^{mat}+K_{Z,c}^{geo}+K_{Z,s}^{mat}+K_{Z,s}^{geo}}
\tag{157}
\]

式中，\(K_Z\) 为完整代表半波基本 Navier 模态的广义 current tangent，N/mm。所有积分仍由 D15 式（89）—（95）精确闭合。

\[
\boxed{K_Z>0:\ \text{正模态切线};\qquad K_Z=0:\ \text{模态临界};\qquad K_Z<0:\ \text{负模态切线}}
\tag{158}
\]

式中，\(K_Z\) 见式（157）。这是 Zhou-form **stability audit / interpretation**，不作为第二套 \(P_u\) 求解器，也不替代 NC-R1 主支极限根。

为与周思铭 \(D_x-D_y-H\) 语言对应，定义面积归一化量

\[
\boxed{I_\varphi=\int_A\varphi^2dA=\frac{b\ell}{4},\qquad I_\psi=\int_A(\cos X\cos Y)^2dA=\frac{b\ell}{4}}
\tag{159}
\]

式中，\(I_\varphi\) 为双正弦模态平方面积积分；\(I_\psi\) 为双余弦模态平方面积积分。

\[
\boxed{D_x^*=\frac1{I_\varphi}\int_{\Omega_h}z^2C_{xx,t}\varphi^2dV,\qquad D_y^*=\frac1{I_\varphi}\int_{\Omega_h}z^2C_{yy,t}\varphi^2dV}
\tag{160}
\]

式中，\(D_x^*,D_y^*\) 为非均匀 current tangent field 对基本模态的次方向/主方向广义弯曲刚度，N·mm；\(C_{xx,t},C_{yy,t}\) 为式（145）的工程切线分量。

\[
\boxed{D_\mu^*=\frac1{I_\varphi}\int_{\Omega_h}z^2\frac{C_{xy,t}+C_{yx,t}}2\varphi^2dV,\qquad D_{66}^*=\frac1{I_\psi}\int_{\Omega_h}z^2G_t(\cos X\cos Y)^2dV}
\tag{161}
\]

式中，\(D_\mu^*\) 为交叉法向 current tangent 的对称模态投影；\(D_{66}^*\) 为工程剪切 current tangent 模态投影；\(C_{xy,t},C_{yx,t},G_t\) 均来自同一 \(\mathbb C_t\)。

\[
\boxed{H^*=D_\mu^*+2D_{66}^*}
\tag{162}
\]

式中，\(H^*\) 为当前 RC current tangent 对周思铭 \(H=D_{xy}+D_\mu\) 方向刚度语言的项目等效投影；它只用于稳定刚度分解和审计。

由式（149）—（162），混凝土材料模态刚度可以精确重写为

\[
\boxed{K_{Z,c}^{mat}=I_\varphi[D_x^*\alpha^4+2H^*\alpha^2\beta^2+D_y^*\beta^4]}
\tag{163}
\]

式中，\(I_\varphi\) 见式（159）；\(D_x^*,D_y^*,H^*\) 见式（160）—（162）；\(\alpha,\beta\) 见式（147）。式（163）给出当前非均匀 current tangent 到 Zhou/Navier 方向刚度组合的严格模态投影关系。

当 current tangent 在板面和厚度上为常量时，式（160）—（162）退化为

\[
\boxed{D_x^*=\frac{t_p^3}{12}C_{xx,t},\quad D_y^*=\frac{t_p^3}{12}C_{yy,t},\quad D_\mu^*=\frac{t_p^3}{24}(C_{xy,t}+C_{yx,t}),\quad D_{66}^*=\frac{t_p^3}{12}G_t}
\tag{164}
\]

式中，各切线分量均为均匀常量。旧的 \(t_p^3C_t/12\) 写法因此只保留为 uniform-tangent degeneration，而不是非均匀场的一般定义。

若进一步是均匀纯 \(y\) 向压缩膜力，则 \(K_Z=0\) 可退化为 Zhou/Navier 形式

\[
\boxed{N_{y,cr}^{Z,*}=\frac{D_x^*\alpha^4+2H^*\alpha^2\beta^2+D_y^*\beta^4}{\beta^2}}
\tag{165}
\]

式中，\(N_{y,cr}^{Z,*}\) 为均匀纯轴压退化条件下的 Zhou-form 临界膜力，N/mm；对一般非均匀 nonlinear current state，正式审计量仍使用式（157）的 full-field \(K_Z\)，而不是把式（165）当作第二套极限荷载方程。

---

# 19 最终非加载步极限根体系

\[
\boxed{R_q(D,q)=0,\qquad L(D,q)=0}
\tag{166}
\]

式中，未知量只有 \(D,q\)；所有结构空间积分已在形成式（166）前由 D15 精确消去。

\[
\boxed{\mathcal R=\{(D,q)\in\mathbb R^2:R_q(D,q)=0,\ L(D,q)=0\}}
\tag{167}
\]

式中，\(\mathcal R\) 为全部低维联合数学驻值根集合；可由代数消元/全实根隔离或等价低维后端一次性求取，不要求加载步材料历史推进。

\[
\boxed{\mathcal R\rightarrow\Gamma_0\rightarrow s_u=\min\mathcal M\rightarrow(D_u,q_u)\rightarrow P_u}
\tag{168}
\]

式中，\(\Gamma_0\) 见式（125）；\(\mathcal M\) 见式（130）；\(s_u\) 见式（131）；\((D_u,q_u),P_u\) 见式（132）。根分类只使用 NC-R1 拓扑/可接受域规则，不使用试验荷载参与求解和选根。

---

# 20 参数来源总表

| 符号 | 含义 | 量纲 | 来源身份 |
|---|---|---:|---|
| \(f_c\) | NC 单轴抗压强度 | MPa | MATERIAL_INPUT |
| \(E_0\) | NC 初始弹性模量 | MPa | MATERIAL_INPUT |
| \(\varepsilon_0\) | R10 参考压缩应变 | 1 | MATERIAL_INPUT |
| \(\nu\) | 泊松比 | 1 | MATERIAL_INPUT |
| \(\kappa\) | \(E_0\varepsilon_0/f_c\) | 1 | R10_DERIVED |
| \(\rho\) | 拉伸尺度 0.1 | 1 | R10_PROJECT_FROZEN |
| \(x_{cr}\) | 拉伸特征材料坐标 | 1 | R10_DERIVED |
| \(\eta\) | R10 平滑尺度 | 1 | R10_DERIVED |
| \(m_t\) | Foster-informed 下降段参数 \(-7/90\) | 1 | R10_PROJECT_FROZEN |
| \(\eta_r\) | Foster-informed 平滑铰宽 0.05 | 1 | R10_PROJECT_FROZEN |
| \(u_r\) | R10 C2 残余拉应力 0.03 | 1 | R10_PROJECT_FROZEN |
| \(W_{src}\) | 源拉伸材料功 | 1 | R10_DERIVED |
| \(h\) | R10 C2 拉伸峰值 | 1 | R10_DERIVED |
| \(a_{cc}\) | 双压低参数物理目标系数 | 1 | PROJECT_FROZEN_PHYSICAL_TARGET |
| \(a_t\) | 双拉低参数物理目标系数 | 1 | PROJECT_FROZEN_PHYSICAL_TARGET |
| \(\mathbf E\) | 物理面内应变张量 | 1 | continuum/NGUYEN KINEMATICS |
| \(\mathbf E_u\) | 等效单轴应变张量 | 1 | R10_PROJECT_FROZEN |
| \(\mathbf X\) | 无量纲等效应变张量 | 1 | R10_DERIVED |
| \(\lambda_\pm\) | \(\mathbf X\) 主值 | 1 | MATHEMATICAL_IDENTITY |
| \(C,T,T^{(7)},U\) | 四个一维 primitive | 1 | R10 target |
| \(\lambda_a,\lambda_b\) | 先验 compiler 域 | 1 | COMPILER_CONTRACT |
| \(\lambda_c,\lambda_h,\xi\) | compiler 映射量 | 1 | MATHEMATICAL_IDENTITY |
| \(N=48\) | 材料解析阶数 | 1 | COMPILER_CONTRACT |
| \(\theta_j,\lambda_j\) | 49 个材料 Chebyshev 根 | 1 | COMPILER_CONTRACT |
| \(a_n^{(F,0)}\) | direct N48 系数 | 1 | COMPILER_CONTRACT |
| \(\mathbf H,\mathbf G,\mathbf d_F\) | C1 约束对象 | — | COMPILER_CONTRACT |
| \(\mathbf a^{(F,C1)}\) | U/C/T7 C1 系数 | 1 | COMPILER_CONTRACT |
| \(\mathbf a^{(T,MM)}\) | 唯一 T constrained-minimax 系数 | 1 | COMPILER_CONTRACT + secondary tie-break |
| \(E_F^{(0)},E_F^{(1)}\) | compiler 全域值/切线误差报告量 | 1 | COMPILER_AUDIT |
| \(K_1,K_2,A_n,B_n\) | CH 不变量/递推系数 | 1 | MATHEMATICAL_IDENTITY |
| \(b,\ell,t_p\) | 完整半波宽、长、板厚 | mm | GEO_INPUT |
| \(A_0,A\) | 初始缺陷/附加挠曲幅值 | mm | GEO_INPUT/NGUYEN_SOURCE |
| \(q_0,q\) | \(A_0/b,A/b\) | 1 | NGUYEN_SOURCE |
| \(D\) | 平均轴压广义变量 | 1 | CURRENT_REDUCED_KINEMATICS |
| \(\chi_q\) | \(q_0q+q^2/2\) | 1 | NGUYEN_SOURCE |
| \(J_{pr},J_{us}\) | D15 面内三角精确矩 | 1 | D15_EXACT_MOMENT |
| \(Z_h\) | D15 厚度精确矩 | 1 | D15_EXACT_MOMENT |
| \(J_\Omega\) | 体积 Jacobian | mm³ | MATHEMATICAL_IDENTITY |
| \(N_{y,c},P_c\) | 平均混凝土轴向膜力/荷载观测量 | N/mm, N | REDUCED_STRUCTURE_DEFINITION |
| \(Q_q,R_{q,c}\) | 混凝土 q-功密度/广义残量 | 1, N·mm | VIRTUAL_WORK |
| \(E_s,f_y,\varepsilon_y,\varepsilon_f\) | 钢筋材料参数 | MPa/1 | NGUYEN_SOURCE/MATERIAL_INPUT |
| \(\rho_{s,\alpha}^{(r)}\) | 方向配筋率 | 1 | REBAR_INPUT |
| \(z_s^{(r)},\zeta_r\) | 钢筋层位置 | mm/1 | GEO_INPUT |
| \(t_{s,\alpha}^{(r)}\) | 等效弥散钢筋片厚 | mm | PROJECT_REBAR_MAPPING |
| \(P_s,R_{q,s}\) | 钢筋轴力/广义残量 | N, N·mm | REBAR_ANALYTIC_CLOSURE |
| \(P,R_q,L\) | 总轴力、平衡残量、极限函数 | N, N·mm, composite | CURRENT_GOVERNING |
| \(\mathcal A,\mathcal E,\Gamma_0\) | 可接受域、全平衡集、主平衡支 | — | NC_R1_GOVERNANCE/MATH |
| \(g(s)\) | 轴力沿主支导数 | path derivative | NC_R1_GOVERNANCE |
| \(R_{norm},L_{norm},d_{ij}\) | 平衡、极限、重复性无量纲指标 | 1 | NC_R1_GOVERNANCE |
| \(\mathbb C_t\) | current material tangent field | MPa | CURRENT_OPERATOR_DERIVATIVE |
| \(\varphi\) | 基本 Zhou/Navier 微扰模态 | 1 | ZHOU_SOURCE/PROJECT_AUDIT |
| \(\alpha,\beta\) | 基本波数 | mm⁻¹ | ZHOU_SOURCE |
| \(K_Z\) | full-field current-tangent 模态审计量 | N/mm | PROJECT_ZHOU_AUDIT |
| \(D_x^*,D_y^*,D_\mu^*,D_{66}^*,H^*\) | Zhou-form current tangent 模态投影刚度 | N·mm | PROJECT_ZHOU_AUDIT |

---

# 21 正式闭合裁决

独立理论审计暴露的正式问题在本稿中按最小修改闭合：

```text
T minimax non-unique possibility
  -> primary minimax + unique strict-convex H-metric tie-break

D15 restricted basis overclaim
  -> general J_pr exact trigonometric moments

Rebar symbolic placeholder
  -> source steel law + directional strain + smeared-layer Ps/Rq,s equations

Pc/end reaction ambiguity
  -> explicit representative-halfwave average load-observable identity

Pi_eta wording
  -> smooth nonnegative one-sided coordinate

a_cc provenance
  -> project-frozen low-parameter biaxial physical target, not source-verbatim/Pu-calibrated

NC-R1 Eq141 ambiguity
  -> scalar level-set convention and energy-conjugate convention explicitly separated

root metric q0=0 ambiguity
  -> q0>0 precondition explicit

Zhou local t^3 Ct/12 ambiguity
  -> full-field modal second variation + mode-projected Dx*-Dy*-H*

Zhou production-gate overstatement
  -> restored to current-tangent stability AUDIT/INTERPRETATION; not second Pu solver
```

最终主思想保持为

\[
\boxed{
\text{连续完整半波}
\rightarrow
\text{有限材料 coefficient}
\rightarrow
\text{有限 CH/三角代数}
\rightarrow
\text{D15 精确矩}
\rightarrow
\{P(D,q),R_q(D,q),L(D,q)\}
\rightarrow
\text{低维联合根}
\rightarrow
\text{NC-R1 主支首个 }+\to-\text{ 极大值}
\rightarrow P_u}
\tag{169}
\]

式中，所有结构空间积分在低维根求解前已经精确消去；正式理论不需要结构空间 Gauss/Simpson、自适应求积、材料点网格、spatial cells 或材料加载步历史推进。

```text
CORE_ZERO_SPATIAL_ANALYTIC_IDEA = RETAINED / PASS AT FORMAL-ARCHITECTURE LEVEL
R10 = FROZEN
N48_ORDER = 48
D15 = GENERAL EXACT TRIG MOMENTS / GOVERNING
REBAR_FORMAL_CLOSURE = COMPLETE UNDER SUPPORTED SINGLE-BRANCH CONTRACT
NC_R1_ROOT_TOPOLOGY = GOVERNING
ZHOU = FULL-FIELD CURRENT-TANGENT MODAL AUDIT / NOT SECOND Pu SOLVER
CASE21_NEW_CALCULATION = NOT PERFORMED
SWARTZ24_RECALCULATION = NOT PERFORMED
```
