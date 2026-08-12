# NZ-SCCM 普通混凝土钢筋板零空间解析极限承载力—切线稳定统一理论

**时间基线：2026-08-12 17:34 +08:00**  
**文件身份：CURRENT GOVERNING THEORY BASELINE**  
**命名原则：自本文件起，正式理论、合同、审计和结果文件不再使用 V1/V2/R1/R2 等容易混淆的序号作为主识别符，统一采用“内容描述 + YYYYMMDD_HHMM”时间戳。旧文件保留为历史证据，不删除。**

---

# 0. 理论目标、主题思想与固定边界

本理论针对普通混凝土钢筋板在轴压作用下的连续完整代表半波，建立“材料 current operator → 有限材料解析编译 → 二维张量提升 → Nguyen 二阶连续运动学 → D15 一般三角精确矩 → 平衡/极限 → Zhou/Navier current-tangent 稳定审计”的统一解析体系。

核心链为

\[
\boxed{
\text{材料与几何输入}
\rightarrow R10
\rightarrow N48\text{-}C1/MM
\rightarrow \mathrm{Cayley\!\!-​Hamilton}
\rightarrow \mathrm{Nguyen\ 二阶完整半波}
\rightarrow \mathrm{D15\ 一般三角精确矩}
\rightarrow P(D,q),R_q(D,q),L(D,q)
\rightarrow \Gamma_0
\rightarrow \{\text{极限点},\,K_Z\text{切线临界}\}
}
\tag{1}
\]

式中，R10 表示当前冻结的普通混凝土 current material target；N48-C1/MM 表示 48 阶一维材料解析编译；Cayley–Hamilton 表示二维对称张量函数的有限降阶；Nguyen 二阶完整半波表示含初始缺陷的连续二阶运动学；D15 表示一般有限三角—厚度精确矩；\(D\) 表示平均轴压广义变量；\(q\) 表示加载后附加局部挠曲无量纲幅值；\(P\) 表示代表半波平均轴向荷载 observable；\(R_q\) 表示与 \(q\) 共轭的广义平衡残量；\(L\) 表示荷载沿平衡支的切向驻值函数；\(\Gamma_0\) 表示从无载点出发的主连通平衡支；\(K_Z\) 表示 Zhou/Navier 基本模态 full-field current tangent。

固定边界：

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
ACTIVE_MODE = m=1
KINEMATICS = NGUYEN_SECOND_ORDER
R10_MATERIAL_TARGET = FROZEN
N48_ORDER = 48
CAYLEY_HAMILTON = GOVERNING
EXACT_MOMENT_ENGINE = D15_GENERAL_TRIG_MOMENTS
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
STRUCTURAL_CALIBRATION = NO
PANEL_LEVEL_SURROGATE = NO
```

这里“零空间解析”表示：结构层不使用 Gauss、Simpson、自适应积分、空间 Chebyshev collocation、材料点网格、空间 cells 或多子域切分作为正式理论。49 个 Chebyshev 根仅是一维材料坐标，用于生成有限材料解析系数，不属于结构空间离散。

这里“非加载步迭代极限理论”表示：材料解析系数冻结后，结构层直接形成有限的 \(P(D,q),R_q(D,q),L(D,q)\) 与 \(K_Z(D,q)\)。求根后端可以采用 resultant、Gröbner/elimination、all-real-root isolation 或其他低维数学方法；某个数学后端内部是否使用 Newton/exchange，不改变理论的零正式空间离散和非材料点历史身份。

来源标签统一为：

```text
[MATERIAL_INPUT]          材料基本输入
[GEO_INPUT]               几何输入
[R10_PROJECT_FROZEN]      当前项目冻结 R10 物理目标/常数
[R10_DERIVED]             由 R10 推导得到
[COMPILER_CONTRACT]       N48-C1/MM 材料编译合同
[MATHEMATICAL_IDENTITY]   数学恒等式
[NGUYEN_SOURCE]           Nguyen 二阶运动学/钢筋来源物理
[D15_EXACT_MOMENT]        D15 一般三角精确矩
[PROJECT_REBAR_MAPPING]   当前连续/弥散钢筋解析映射
[PRIMARY_BRANCH_RULE]     主连通平衡支与首个 +→− 极大值规则
[ZHOU_SOURCE]             周思铭正交各向异性/Navier 稳定语言
[PROJECT_ZHOU_TANGENT]    current tangent 的完整场模态投影
```

---

# 1. 普通混凝土基本材料量

普通混凝土输入为

\[
\boxed{f_c,\qquad E_0,\qquad \varepsilon_0,\qquad \nu}
\tag{2}
\]

式中，\(f_c\) 为单轴抗压强度，MPa，[MATERIAL_INPUT]；\(E_0\) 为初始弹性模量，MPa，[MATERIAL_INPUT]；\(\varepsilon_0\) 为 R10 参考压缩应变，无量纲，[MATERIAL_INPUT]；\(\nu\) 为泊松比，无量纲，[MATERIAL_INPUT]。上述参数不得由板级试验承载力反标。

定义

\[
\boxed{\kappa=\frac{E_0\varepsilon_0}{f_c}}
\tag{3}
\]

式中，\(\kappa\) 为 R10 无量纲初始斜率，[R10_DERIVED]；其余符号见式（2）。

冻结拉伸强度尺度

\[
\boxed{\rho=0.1}
\tag{4}
\]

式中，\(\rho\) 为相对于 \(f_c\) 的无量纲拉伸强度尺度，[R10_PROJECT_FROZEN]；它不是结构承载力折减系数。

定义

\[
\boxed{x_{cr}=\frac{\rho}{\kappa}}
\tag{5}
\]

式中，\(x_{cr}\) 为无量纲拉伸特征材料坐标，[R10_DERIVED]；\(\rho\) 与 \(\kappa\) 见式（4）、（3）。

定义

\[
\boxed{\eta=\frac{x_{cr}}{20}}
\tag{6}
\]

式中，\(\eta\) 为 R10 在零主等效应变附近使用的平滑尺度，[R10_DERIVED]。

---

# 2. 物理应变与等效单轴应变张量

二维物理面内应变张量为

\[
\boxed{
\mathbf E=
\begin{bmatrix}
\varepsilon_x & \gamma_{xy}/2\\
\gamma_{xy}/2 & \varepsilon_y
\end{bmatrix}}
\tag{7}
\]

式中，\(\mathbf E\) 为二维物理应变张量；\(\varepsilon_x,\varepsilon_y\) 分别为 \(x,y\) 方向法向应变；\(\gamma_{xy}\) 为工程剪应变；\(\gamma_{xy}/2\) 为张量剪应变。

定义 R10 等效单轴应变张量

\[
\boxed{
\mathbf E_u=
\frac{(1-\nu)\mathbf E+\nu\operatorname{tr}(\mathbf E)\mathbf I}{1-\nu^2}}
\tag{8}
\]

式中，\(\mathbf E_u\) 为等效单轴应变张量，[R10_PROJECT_FROZEN]；\(\operatorname{tr}(\mathbf E)=\varepsilon_x+\varepsilon_y\)；\(\mathbf I\) 为二维单位张量；\(\nu\) 见式（2）。

定义无量纲等效应变张量

\[
\boxed{\mathbf X=\frac{\mathbf E_u}{\varepsilon_0}}
\tag{9}
\]

式中，\(\mathbf X\) 为 R10 无量纲二维等效应变张量，[R10_DERIVED]；\(\varepsilon_0\) 见式（2）。

其法向分量为

\[
\boxed{
X_{11}=\frac{\varepsilon_x+\nu\varepsilon_y}{(1-\nu^2)\varepsilon_0},
\qquad
X_{22}=\frac{\nu\varepsilon_x+\varepsilon_y}{(1-\nu^2)\varepsilon_0}}
\tag{10}
\]

式中，\(X_{11},X_{22}\) 为 \(\mathbf X\) 的两个法向分量；其余符号见式（2）、（7）。

剪切分量为

\[
\boxed{X_{12}=X_{21}=\frac{\gamma_{xy}}{2(1+\nu)\varepsilon_0}}
\tag{11}
\]

式中，\(X_{12}\) 为等效应变剪切分量；式中 2 来自工程剪应变与张量剪应变换算。

定义

\[
\boxed{
\mu=\frac{X_{11}+X_{22}}2,
\qquad
\delta=\frac{X_{11}-X_{22}}2,
\qquad
r_X=\sqrt{\delta^2+X_{12}^2}}
\tag{12}
\]

式中，\(\mu\) 为两个主值平均值；\(\delta\) 为两个法向分量半差；\(r_X\) 为二维对称张量主值半径，[MATHEMATICAL_IDENTITY]。

主等效应变为

\[
\boxed{\lambda_\pm=\mu\pm r_X}
\tag{13}
\]

式中，\(\lambda_+\) 与 \(\lambda_-\) 分别为 \(\mathbf X\) 的较大与较小主值，[MATHEMATICAL_IDENTITY]。

---

# 3. R10 平滑拉压坐标

定义项目平滑单侧非负坐标

\[
\boxed{
\Pi_\eta(z)=
\frac{z^2\left(\sqrt{z^2+\eta^2}+z\right)}{2(z^2+\eta^2)}}
\tag{14}
\]

式中，\(z\) 为任意无量纲主应变坐标；\(\Pi_\eta(z)\ge0\) 为项目定义的 smooth nonnegative one-sided material coordinate，[R10_PROJECT_FROZEN]；\(\eta\) 见式（6）。本理论不宣称它是严格单调 softplus，也不要求 \(\Pi_\eta(z)-\Pi_\eta(-z)=z\)。

定义

\[
\boxed{c(\lambda)=\Pi_\eta(-\lambda),\qquad t(\lambda)=\Pi_\eta(\lambda)}
\tag{15}
\]

式中，\(c(\lambda)\) 为平滑压缩坐标；\(t(\lambda)\) 为平滑拉伸坐标；二者均非负，[R10_DERIVED]。

---

# 4. R10 压缩 primitive 与拉伸材料功

压缩 primitive 为

\[
\boxed{
C(\lambda)=
\frac{\kappa c(\lambda)}{1+(\kappa-2)c(\lambda)+c(\lambda)^2}}
\tag{16}
\]

式中，\(C(\lambda)\) 为无量纲压缩 primitive，[R10_PROJECT_FROZEN]；\(\kappa\) 见式（3）；\(c(\lambda)\) 见式（15）。

定义拉伸材料坐标

\[
\boxed{r=\frac{t}{x_{cr}}}
\tag{17}
\]

式中，\(r\) 为按 \(x_{cr}\) 归一化的拉伸材料坐标；\(t\) 见式（15）；\(x_{cr}\) 见式（5）。

冻结源参数

\[
\boxed{m_t=-\frac7{90},\qquad \eta_r=0.05}
\tag{18}
\]

式中，\(m_t\) 为 Foster-informed 拉伸下降段参数；\(\eta_r\) 为源平滑铰宽度；二者属于当前 source-informed/project-frozen 材料目标，[R10_PROJECT_FROZEN]。

定义平滑铰函数

\[
\boxed{
H(r,r_0)=
\frac12\left[(r-r_0)+\sqrt{(r-r_0)^2+\eta_r^2}\right]
-\frac12\left[-r_0+\sqrt{r_0^2+\eta_r^2}\right]}
\tag{19}
\]

式中，\(H(r,r_0)\) 为平滑铰函数；\(r_0\) 为铰中心，当前使用 \(r_0=1\) 与 \(r_0=10\)；\(\eta_r\) 见式（18）。

源拉伸利用函数为

\[
\boxed{T_{src}(r)=r+(m_t-1)H(r,1)-m_tH(r,10)}
\tag{20}
\]

式中，\(T_{src}\) 为一维源拉伸利用函数；\(m_t,H\) 见式（18）、（19）。

源归一化拉应力为

\[
\boxed{u_{t,src}(t)=\rho\,T_{src}(t/x_{cr})}
\tag{21}
\]

式中，\(u_{t,src}\) 为 Foster-informed 源归一化拉应力；\(\rho\) 见式（4）；\(t/x_{cr}\) 即式（17）的 \(r\)。

定义一维材料功

\[
\boxed{
W_{src}=\int_0^{10x_{cr}}u_{t,src}(t)\,dt
=\rho x_{cr}\int_0^{10}T_{src}(r)\,dr}
\tag{22}
\]

式中，\(W_{src}\) 为一维材料坐标上的归一化拉伸材料功，[R10_DERIVED]；该积分不是结构空间积分，不计入 formal spatial quadrature。

定义上升段局部坐标

\[
\boxed{\tau=\frac{t}{x_{cr}},\qquad 0\le\tau\le1}
\tag{23}
\]

式中，\(\tau\) 为 R10 C2 重构上升段局部坐标。

上升段为

\[
\boxed{u_1(\tau)=
\rho\tau+(10h-6\rho)\tau^3+(8\rho-15h)\tau^4+(6h-3\rho)\tau^5}
\tag{24}
\]

式中，\(u_1\) 为归一化拉应力上升段；\(h\) 为待由材料功确定的峰值；\(\rho\) 见式（4）；\(\tau\) 见式（23）。

定义下降段坐标

\[
\boxed{s=\frac{t-x_{cr}}{9x_{cr}},\qquad 0\le s\le1}
\tag{25}
\]

式中，\(s\) 为 \(x_{cr}<t\le10x_{cr}\) 上的局部下降段坐标。

冻结残余拉应力尺度

\[
\boxed{u_r=0.03}
\tag{26}
\]

式中，\(u_r\) 为 \(t=10x_{cr}\) 及其后的归一化残余拉应力，[R10_PROJECT_FROZEN]。

下降段为

\[
\boxed{u_2(s)=h+(u_r-h)(10s^3-15s^4+6s^5)}
\tag{27}
\]

式中，\(u_2\) 为归一化拉应力下降段；\(h\) 为峰值；\(u_r\) 见式（26）；\(s\) 见式（25）。

材料功闭合得到

\[
\boxed{h=\frac15\left(\frac{W_{src}}{x_{cr}}-\frac{\rho}{10}-\frac92u_r\right)}
\tag{28}
\]

式中，\(h\) 为 R10 拉伸峰值，[R10_DERIVED]；\(W_{src}\) 见式（22）；\(x_{cr}\) 见式（5）；\(\rho\) 见式（4）；\(u_r\) 见式（26）。该式只由材料功确定，不含板级承载力。

完整拉伸函数为

\[
\boxed{u_{sm}(t)=
\begin{cases}
u_1(t/x_{cr}),&0\le t\le x_{cr},\\[1mm]
u_2[(t-x_{cr})/(9x_{cr})],&x_{cr}<t\le10x_{cr},\\[1mm]
u_r,&t>10x_{cr}.
\end{cases}}
\tag{29}
\]

式中，\(u_{sm}\) 为 R10 C2 重构后的完整归一化拉应力；这里公式中的 \(\nu_1,\nu_2,\nu_r\) 仅为排版符号占位，规范变量名实际为 \(u_1,u_2,u_r\)，其定义分别见式（24）、（27）、（26）。后续程序和正式代数只使用 \(u_1,u_2,u_r\)。

定义拉伸 primitive

\[
\boxed{T(\lambda)=\frac{u_{sm}[\Pi_\eta(\lambda)]}{\rho}}
\tag{30}
\]

式中，\(T(\lambda)\) 为无量纲拉伸 primitive；\(u_{sm}\) 见式（29）；\(\Pi_\eta\) 见式（14）；\(\rho\) 见式（4）。

定义独立七次 primitive

\[
\boxed{T^{(7)}(\lambda)=[T(\lambda)]^7}
\tag{31}
\]

式中，\(T^{(7)}\) 为双拉相互作用使用的七次拉伸 primitive；正式编译时直接把闭式 \(T^7\) 作为独立一维目标。

---

# 5. R10 current master 与二维相互作用

定义

\[
\boxed{U(\lambda)=\kappa\lambda-C(\lambda)+\kappa c(\lambda)+\rho T(\lambda)-\kappa t(\lambda)}
\tag{32}
\]

式中，\(U\) 为一维 current master；\(\kappa\) 见式（3）；\(C\) 见式（16）；\(c,t\) 见式（15）；\(T\) 见式（30）；\(\rho\) 见式（4）。

双压相互作用系数冻结为

\[
\boxed{a_{cc}=0.1072329249362415}
\tag{33}
\]

式中，\(a_{cc}\) 为项目冻结的双压低参数物理目标系数，[R10_PROJECT_FROZEN]；其身份是使等双压目标点接触当前保守 CC 包络并保持单轴坐标轴不变。它不是 Nguyen/Foster 原文直接常数，也不是板级承载力反标参数。

双拉相互作用系数为

\[
\boxed{a_t=1-2^{-1/8}}
\tag{34}
\]

式中，\(a_t\) 为项目冻结的双拉低参数物理目标系数，[R10_PROJECT_FROZEN]。

对 \(\lambda_\pm\) 分别计算 \(U_\pm,C_\pm,T_\pm\)，定义主方向无量纲应力

\[
\boxed{s_+=U_+-a_{cc}C_+^2C_-+C_+T_- -\rho a_tT_+T_-^8}
\tag{35}
\]

式中，\(s_+\) 为较大主等效应变方向无量纲应力；\(U_+,C_+,T_+\) 表示把 \(\lambda_+\) 代入式（32）、（16）、（30）；\(C_-,T_-\) 为 \(\lambda_-\) 对应值；\(a_{cc},a_t,\rho\) 见式（33）、（34）、（4）。

另一主方向为

\[
\boxed{s_-=U_- -a_{cc}C_-^2C_+ +C_-T_+ -\rho a_tT_-T_+^8}
\tag{36}
\]

式中，\(s_-\) 为较小主等效应变方向无量纲应力；其余符号含义同式（35）。

物理主应力为

\[
\boxed{\sigma_\pm=f_cs_\pm}
\tag{37}
\]

式中，\(\sigma_\pm\) 为物理主应力，MPa；\(f_c\) 见式（2）。

R10 零点锚点为

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

式中，各撇号均表示对真实材料坐标 \(\lambda\) 求导。

---

# 6. N48-C1/MM 有限材料解析编译

编译区间预先冻结为

\[
\boxed{\lambda\in[\lambda_a,\lambda_b],\qquad \lambda_a<\lambda_b}
\tag{41}
\]

式中，\(\lambda_a,\lambda_b\) 分别为材料 compiler 下、上界；必须在结构根计算以前给定，不允许根据试验承载力或历史根修改。

定义

\[
\boxed{\lambda_c=\frac{\lambda_a+\lambda_b}{2},\qquad \lambda_h=\frac{\lambda_b-\lambda_a}{2}}
\tag{42}
\]

式中，\(\lambda_c\) 为 compiler 中心；\(\lambda_h>0\) 为 compiler 半宽。

定义标准坐标

\[
\boxed{\xi(\lambda)=\frac{\lambda-\lambda_c}{\lambda_h}}
\tag{43}
\]

式中，\(\xi\in[-1,1]\)；\(\lambda_c,\lambda_h\) 见式（42）。

第一类 Chebyshev 多项式为

\[
\boxed{\mathcal C_n(\xi)=\cos[n\arccos(\xi)]}
\tag{44}
\]

式中，\(n=0,\ldots,48\) 为材料解析阶次索引。

49 个材料根点为

\[
\boxed{\theta_j=\frac{(j+1/2)\pi}{49},\qquad \lambda_j=\lambda_c+\lambda_h\cos\theta_j,\qquad j=0,\ldots,48}
\tag{45}
\]

式中，\(j\) 为一维材料坐标索引；\(\theta_j\) 为 Chebyshev 根角度；\(\lambda_j\) 为材料坐标，不是结构空间坐标。

对 \(F\in\{U,C,T,T^{(7)}\}\)，direct coefficient 为

\[
\boxed{a_n^{(F,0)}=\frac{2-\delta_{n0}}{49}\sum_{j=0}^{48}F(\lambda_j)\cos(n\theta_j)}
\tag{46}
\]

式中，\(a_n^{(F,0)}\) 为第 \(n\) 个 direct N48 coefficient；\(\delta_{n0}\) 为 Kronecker delta；\(F\) 为式（32）、（16）、（30）、（31）中的一维材料目标。

定义根点矩阵

\[
\boxed{V_{jn}=\cos(n\theta_j)}
\tag{47}
\]

式中，\(\mathbf V\) 为 \(49\times49\) 材料根点矩阵。

离散正交性给出

\[
\boxed{\mathbf H=\mathbf V^T\mathbf V=\operatorname{diag}(49,49/2,\ldots,49/2)}
\tag{48}
\]

式中，\(\mathbf H\) 为正定权矩阵，[MATHEMATICAL_IDENTITY]。

其逆为

\[
\boxed{\mathbf H^{-1}=\frac1{49}\operatorname{diag}(1,2,\ldots,2)}
\tag{49}
\]

式中，\(\mathbf H^{-1}\) 为式（48）的逆矩阵。

零材料坐标为

\[
\boxed{\xi_0=-\frac{\lambda_c}{\lambda_h}}
\tag{50}
\]

式中，\(\xi_0\) 为真实材料坐标 \(\lambda=0\) 对应的标准坐标。

约束矩阵为

\[
\boxed{
\mathbf G=
\begin{bmatrix}
\mathcal C_0(\xi_0)&\cdots&\mathcal C_{48}(\xi_0)\\
\lambda_h^{-1}\mathcal C_0'(\xi_0)&\cdots&\lambda_h^{-1}\mathcal C_{48}'(\xi_0)
\end{bmatrix}}
\tag{51}
\]

式中，\(\mathbf G\) 第一行约束 \(F(0)\)，第二行约束真实材料导数 \(dF/d\lambda|_0\)；\(\lambda_h^{-1}\) 来自链式法则。

目标向量为

\[
\boxed{\mathbf d_U=(0,\kappa)^T,\qquad \mathbf d_C=\mathbf d_T=\mathbf d_{T^{(7)}}=(0,0)^T}
\tag{52}
\]

式中，\(\mathbf d_F\) 为各 primitive 的零点值/切线目标；\(\kappa\) 见式（3）。

C1 coefficient 为

\[
\boxed{
\mathbf a^{(F,C1)}=\mathbf a^{(F,0)}+\mathbf H^{-1}\mathbf G^T(\mathbf G\mathbf H^{-1}\mathbf G^T)^{-1}(\mathbf d_F-\mathbf G\mathbf a^{(F,0)})}
\tag{53}
\]

式中，\(\mathbf a^{(F,C1)}\) 为满足零点值和一阶切线约束的 coefficient；\(\mathbf a^{(F,0)}\) 见式（46）；\(\mathbf H,\mathbf G,\mathbf d_F\) 见式（48）、（51）、（52）。

对拉伸 primitive 定义可行集合

\[
\boxed{\mathcal F_T=\{\mathbf a\in\mathbb R^{49}:\mathbf G\mathbf a=\mathbf d_T\}}
\tag{54}
\]

式中，\(\mathcal F_T\) 为满足严格 C1 约束的所有 degree-48 coefficient 集合。

定义

\[
\boxed{p_{\mathbf a}(\lambda)=\sum_{n=0}^{48}a_n\mathcal C_n[\xi(\lambda)]}
\tag{55}
\]

式中，\(p_{\mathbf a}\) 为 coefficient 向量 \(\mathbf a\) 对应的 48 阶一维材料多项式；\(a_n\) 为第 \(n\) 个 coefficient。

主 minimax 误差为

\[
\boxed{E_T^*=\min_{\mathbf a\in\mathcal F_T}\|p_{\mathbf a}-T_{R10}\|_{L^\infty([\lambda_a,\lambda_b])}}
\tag{56}
\]

式中，\(E_T^*\) 为严格 C1 条件下 degree-48 空间的最小最大误差；\(T_{R10}\) 为式（30）的闭式 R10 拉伸 primitive。

定义全部主最优解集合

\[
\boxed{\mathcal S_T^*=\{\mathbf a\in\mathcal F_T:\|p_{\mathbf a}-T_{R10}\|_\infty=E_T^*\}}
\tag{57}
\]

式中，\(\mathcal S_T^*\) 为所有 primary minimax 最优 coefficient 构成的闭凸集合。

最终唯一 production T coefficient 定义为

\[
\boxed{\mathbf a^{(T,MM)}=\underset{\mathbf a\in\mathcal S_T^*}{\operatorname{argmin}}\frac12(\mathbf a-\mathbf a^{(T,C1)})^T\mathbf H(\mathbf a-\mathbf a^{(T,C1)})}
\tag{58}
\]

式中，\(\mathbf a^{(T,MM)}\) 为最终唯一 T-minimax coefficient；\(\mathbf a^{(T,C1)}\) 为按式（53）得到的 T-C1 参考 coefficient；\(\mathbf H\) 见式（48）。由于 \(\mathbf H\) 正定，二级目标严格凸，因此 production coefficient 唯一。

最终 governing coefficient identity 为

\[
\boxed{\mathbf a^{(F,*)}=\begin{cases}\mathbf a^{(F,C1)},&F\in\{U,C,T^{(7)}\},\\\mathbf a^{(T,MM)},&F=T.\end{cases}}
\tag{59}
\]

式中，上标 \((*)\) 表示最终 governing coefficient。

最终一维材料表示为

\[
\boxed{F_{48}(\lambda)=\sum_{n=0}^{48}a_n^{(F,*)}\mathcal C_n[\xi(\lambda)]}
\tag{60}
\]

式中，\(F_{48}\) 为最终 48 阶一维解析 primitive。

材料值误差报告为

\[
\boxed{E_F^{(0)}=\|F_{48}-F_{R10}\|_{L^\infty([\lambda_a,\lambda_b])}}
\tag{61}
\]

式中，\(E_F^{(0)}\) 为整个 compiler 区间上的最大绝对函数值误差。

一阶切线误差报告为

\[
\boxed{E_F^{(1)}=\lambda_h\|F_{48}'-F_{R10}'\|_{L^\infty([\lambda_a,\lambda_b])}}
\tag{62}
\]

式中，\(E_F^{(1)}\) 为按 compiler 半宽尺度化的一阶导数误差；当前不新增 theorem-level 余项硬阈值，但必须报告并通过既有工程 material/tangent gates。

---

# 7. Cayley–Hamilton 二维张量提升

定义

\[
\boxed{\mathbf Y=\frac{\mathbf X-\lambda_c\mathbf I}{\lambda_h}}
\tag{63}
\]

式中，\(\mathbf Y\) 为标准化二维等效应变张量；\(\mathbf X\) 见式（9）；\(\lambda_c,\lambda_h\) 见式（42）。

定义

\[
\boxed{K_1=\operatorname{tr}(\mathbf Y),\qquad K_2=\det(\mathbf Y)}
\tag{64}
\]

式中，\(K_1,K_2\) 分别为 \(\mathbf Y\) 的迹和行列式。

二维 Cayley–Hamilton 恒等式为

\[
\boxed{\mathbf Y^2-K_1\mathbf Y+K_2\mathbf I=\mathbf0}
\tag{65}
\]

式中，\(\mathbf0\) 为二维零张量，[MATHEMATICAL_IDENTITY]。

因此

\[
\boxed{\mathcal C_n(\mathbf Y)=A_n\mathbf I+B_n\mathbf Y}
\tag{66}
\]

式中，\(A_n=A_n(K_1,K_2)\)、\(B_n=B_n(K_1,K_2)\) 为 CH 标量系数。

初值为

\[
\boxed{A_0=1,\ B_0=0,\qquad A_1=0,\ B_1=1}
\tag{67}
\]

式中，初值对应 \(\mathcal C_0(\mathbf Y)=\mathbf I\)、\(\mathcal C_1(\mathbf Y)=\mathbf Y\)。

递推为

\[
\boxed{A_{n+1}=-2K_2B_n-A_{n-1}}
\tag{68}
\]

式中，\(A_{n+1}\) 为下一阶单位张量 coefficient；\(K_2,B_n,A_{n-1}\) 见式（64）、（66）。

\[
\boxed{B_{n+1}=2A_n+2K_1B_n-B_{n-1}}
\tag{69}
\]

式中，\(B_{n+1}\) 为下一阶 \(\mathbf Y\) coefficient；\(K_1,A_n,B_n,B_{n-1}\) 见式（64）、（66）。

第 \(n\) 个材料 coefficient 的二维张量项为

\[
\boxed{\mathbf F_{48}^{(n)}=a_n^{(F,*)}(A_n\mathbf I+B_n\mathbf Y)}
\tag{70}
\]

式中，\(\mathbf F_{48}^{(n)}\) 为 primitive \(F\) 的第 \(n\) 个二维项；\(a_n^{(F,*)}\) 见式（59）。

全部求和得

\[
\boxed{\mathbf F_{48}=\sum_{n=0}^{48}\mathbf F_{48}^{(n)}=A_F\mathbf I+B_F\mathbf Y}
\tag{71}
\]

式中，\(\mathbf F_{48}\) 可为 \(\mathbf U,\mathbf C,\mathbf T,\mathbf T^{(7)}\)；\(A_F=\sum a_n^{(F,*)}A_n\)，\(B_F=\sum a_n^{(F,*)}B_n\)。

---

# 8. 二维 current stress tensor

定义

\[
\boxed{\mathbf{CC}=\det(\mathbf C)\mathbf C}
\tag{72}
\]

式中，\(\mathbf{CC}\) 为双压相互作用张量；\(\mathbf C\) 为二维压缩 primitive。

定义

\[
\boxed{\mathbf{TC}=\mathbf C[\operatorname{tr}(\mathbf T)\mathbf I-\mathbf T]}
\tag{73}
\]

式中，\(\mathbf{TC}\) 为拉压相互作用张量；\(\mathbf T\) 为二维拉伸 primitive。

定义

\[
\boxed{\mathbf{TT}=\det(\mathbf T)[\operatorname{tr}(\mathbf T^{(7)})\mathbf I-\mathbf T^{(7)}]}
\tag{74}
\]

式中，\(\mathbf{TT}\) 为双拉相互作用张量；\(\mathbf T^{(7)}\) 为独立七次二维 primitive。

无量纲 current stress tensor 为

\[
\boxed{\mathbf S=\mathbf U-a_{cc}\mathbf{CC}+\mathbf{TC}-\rho a_t\mathbf{TT}}
\tag{75}
\]

式中，\(\mathbf S\) 为无量纲 current stress tensor；\(\mathbf U,\mathbf{CC},\mathbf{TC},\mathbf{TT}\) 见式（71）—（74）；\(a_{cc},\rho,a_t\) 见式（33）、（4）、（34）。

物理应力为

\[
\boxed{\boldsymbol\sigma=f_c\mathbf S}
\tag{76}
\]

式中，\(\boldsymbol\sigma\) 为二维物理应力张量；\(f_c\) 见式（2）。

---

# 9. Nguyen 二阶连续完整半波运动学

定义无量纲坐标

\[
\boxed{X=\frac{\pi x}{b},\qquad Y=\frac{\pi y}{\ell},\qquad \zeta=\frac{2z}{t_p}}
\tag{77}
\]

式中，\(x,y,z\) 为物理坐标；\(b\) 为完整代表半波宽度；\(\ell\) 为轴向半波长度；\(t_p\) 为板厚，[GEO_INPUT]；\(X,Y\in[0,\pi]\)，\(\zeta\in[-1,1]\)。

初始缺陷与附加挠曲为

\[
\boxed{w_0=A_0\sin X\sin Y,\qquad w_1=A\sin X\sin Y}
\tag{78}
\]

式中，\(w_0\) 为 stress-free initial imperfection；\(w_1\) 为加载后的 added displacement；\(A_0,A\) 为对应物理幅值，[NGUYEN_SOURCE]。

定义

\[
\boxed{q_0=\frac{A_0}{b},\qquad q=\frac{A}{b}}
\tag{79}
\]

式中，\(q_0\) 为初始缺陷比；\(q\) 为加载后附加挠曲广义变量；无载状态为 \((D,q)=(0,0)\)。

定义

\[
\boxed{\chi_q=q_0q+\frac12q^2}
\tag{80}
\]

式中，\(\chi_q\) 为 Nguyen/von Kármán 二阶几何组合；\(q_0q\) 为初始缺陷—附加挠曲交叉项；\(q^2/2\) 为附加挠曲自二阶项。

基础膜应变为

\[
\boxed{e_x^{(0)}=\nu D,\qquad e_y^{(0)}=-D}
\tag{81}
\]

式中，\(D>0\) 为平均轴向压缩广义变量；\(e_x^{(0)},e_y^{(0)}\) 为按 \(\varepsilon_0\) 归一化的基础膜应变。

二阶膜系数为

\[
\boxed{C_{mx}=\frac{\pi^2}{\varepsilon_0}\chi_q,\quad C_{my}=\frac{\pi^2b^2}{\varepsilon_0\ell^2}\chi_q,\quad C_{mxy}=\frac{2\pi^2b}{\varepsilon_0\ell}\chi_q}
\tag{82}
\]

式中，\(C_{mx},C_{my},C_{mxy}\) 分别为两个法向及工程剪切二阶膜系数；\(b,\ell,\varepsilon_0,\chi_q\) 见式（77）、（2）、（80）。

弯曲系数为

\[
\boxed{C_{bx}=\frac{\pi^2t_p}{2\varepsilon_0b}q,\quad C_{by}=\frac{\pi^2t_pb}{2\varepsilon_0\ell^2}q,\quad C_{bxy}=-\frac{\pi^2t_p}{\varepsilon_0\ell}q}
\tag{83}
\]

式中，\(C_{bx},C_{by}\) 为法向弯曲系数；\(C_{bxy}\) 为工程剪切弯曲系数；负号来自 \(-2zw_{,xy}\) 约定。

连续归一化应变场为

\[
\boxed{e_x=\nu D+C_{mx}\cos^2X\sin^2Y+C_{bx}\sin X\sin Y\,\zeta}
\tag{84}
\]

式中，\(e_x=\varepsilon_x/\varepsilon_0\) 为归一化横向应变；各系数见式（81）—（83）。

\[
\boxed{e_y=-D+C_{my}\sin^2X\cos^2Y+C_{by}\sin X\sin Y\,\zeta}
\tag{85}
\]

式中，\(e_y=\varepsilon_y/\varepsilon_0\) 为归一化轴向应变。

\[
\boxed{g_{xy}=C_{mxy}\sin X\cos X\sin Y\cos Y+C_{bxy}\cos X\cos Y\,\zeta}
\tag{86}
\]

式中，\(g_{xy}=\gamma_{xy}/\varepsilon_0\) 为归一化工程剪应变。

物理应变为

\[
\boxed{\varepsilon_x=\varepsilon_0e_x,\qquad \varepsilon_y=\varepsilon_0e_y,\qquad \gamma_{xy}=\varepsilon_0g_{xy}}
\tag{87}
\]

式中，\(\varepsilon_0\) 见式（2）；\(e_x,e_y,g_{xy}\) 见式（84）—（86）。给定 \((D,q)\) 后，完整连续半波应变场唯一确定。

---

# 10. D15 一般三角—厚度精确矩

任何最终结构标量 integrand 必须写成

\[
\boxed{Q(X,Y,\zeta)=\sum_{p,r,u,s,h}c_{prush}\sin^pX\cos^rX\sin^uY\cos^sY\zeta^h}
\tag{88}
\]

式中，\(Q\) 可为 \(S_{yy}\)、\(Q_q\)、其同源导数、current-tangent material integrand 或 current-stress geometric-stiffness integrand；\(c_{prush}\) 为有限解析 coefficient；\(p,r,u,s,h\) 为非负整数幂次。中间张量分量允许含裸 \(\cos X,\cos Y\)，不得再强行使用只含 \(\sin X,\sin Y,\zeta\) 的 restricted basis。

定义一般面内三角矩

\[
\boxed{J_{pr}=\int_0^\pi\sin^pX\cos^rX\,dX}
\tag{89}
\]

式中，\(J_{pr}\) 为 D15 一般面内精确矩；\(p,r\) 分别为正弦、余弦幂次，[D15_EXACT_MOMENT]。

其闭式为

\[
\boxed{J_{pr}=\begin{cases}0,&r\text{ 为奇数},\\B\!\left(\dfrac{p+1}{2},\dfrac{r+1}{2}\right),&r\text{ 为偶数}.\end{cases}}
\tag{90}
\]

式中，\(B(a,b)\) 为 Beta 函数；完整 \([0,\pi]\) 半波上的余弦奇次项因对称性精确为零。

Beta 函数为

\[
\boxed{B(a,b)=\frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}}
\tag{91}
\]

式中，\(\Gamma\) 为 Gamma 函数；对当前非负整数幂，式（90）—（91）化为有理数与 \(\pi\) 的精确组合。

厚度矩为

\[
\boxed{Z_h=\int_{-1}^{1}\zeta^h d\zeta=\begin{cases}0,&h\text{ 为奇数},\\\dfrac{2}{h+1},&h\text{ 为偶数}.\end{cases}}
\tag{92}
\]

式中，\(Z_h\) 为归一化厚度第 \(h\) 阶精确矩；\(h\) 为非负整数。

体积 Jacobian 为

\[
\boxed{J_\Omega=\frac{b\ell t_p}{2\pi^2}}
\tag{93}
\]

式中，\(J_\Omega\) 为 \((X,Y,\zeta)\to(x,y,z)\) 的体积 Jacobian；\(b,\ell,t_p\) 见式（77）。

D15 精确收缩为

\[
\boxed{\mathscr D[Q]=\sum_{p,r,u,s,h}c_{prush}J_{pr}J_{us}Z_h}
\tag{94}
\]

式中，\(\mathscr D[Q]\) 为 \(Q\) 在标准完整半波域上的精确解析积分；\(J_{pr},J_{us},Z_h\) 见式（89）—（92）。

一个材料 coefficient 到结构积分的传播链为

\[
\boxed{a_n^{(F,*)}\rightarrow a_n^{(F,*)}(A_n\mathbf I+B_n\mathbf Y)\rightarrow\mathbf F^{(n)}\rightarrow\mathbf S\rightarrow\{c_{prush}\}\rightarrow\{c_{prush}J_{pr}J_{us}Z_h\}}
\tag{95}
\]

式中，\(a_n^{(F,*)}\) 为第 \(n\) 个材料 coefficient；\(A_n,B_n,\mathbf Y\) 见式（63）—（70）；\(\mathbf F^{(n)}\) 为二维 primitive 项；\(\mathbf S\) 见式（75）；\(c_{prush}\) 为最终 scalar integrand 的有限三角—厚度系数。

---

# 11. 混凝土轴向荷载与 q-广义残量

定义完整半波平均轴向膜力

\[
\boxed{N_{y,c}(D,q)=-\frac1{b\ell}\int_{\Omega_h}\sigma_{yy}dV}
\tag{96}
\]

式中，\(N_{y,c}\) 为完整代表半波平均轴向膜力，N/mm；\(\Omega_h\) 为完整半波体积；\(\sigma_{yy}\) 为物理轴向应力；负号使压缩取正。它是当前降维理论的 load observable 定义，不宣称任意截面局部反力恒等于该值。

轴向荷载 observable 为

\[
\boxed{P_c=bN_{y,c}=-\frac1\ell\int_{\Omega_h}\sigma_{yy}dV}
\tag{97}
\]

式中，\(P_c\) 为混凝土平均轴向荷载，N；\(b\) 为半波宽；\(N_{y,c}\) 见式（96）。

D15 形式为

\[
\boxed{P_c=-\frac{f_cbt_p}{2\pi^2}\mathscr D[S_{yy}]}
\tag{98}
\]

式中，\(S_{yy}\) 为式（75）的无量纲轴向应力分量；\(f_c,b,t_p\) 见式（2）、（77）；\(\mathscr D\) 见式（94）。

定义无量纲物理应变张量

\[
\boxed{\mathbf e=\frac{\mathbf E}{\varepsilon_0}}
\tag{99}
\]

式中，\(\mathbf e\) 为无量纲物理应变张量；\(\mathbf E\) 见式（7）。

由式（8）可反写

\[
\boxed{\mathbf e=(1+\nu)\mathbf X-\nu\operatorname{tr}(\mathbf X)\mathbf I}
\tag{100}
\]

式中，\(\mathbf X\) 见式（9）；\(\nu\) 见式（2）；式（100）为式（8）的代数逆关系。

定义 q-广义功密度

\[
\boxed{Q_q=\mathbf S:\frac{\partial\mathbf e}{\partial q}}
\tag{101}
\]

式中，\(Q_q\) 为无量纲 q-广义功密度；\(\mathbf S\) 见式（75）；冒号表示二阶张量双点积；\(\partial\mathbf e/\partial q\) 由 Nguyen 连续应变场式（84）—（86）解析求导得到。

混凝土 q-广义残量为

\[
\boxed{R_{q,c}=f_c\varepsilon_0J_\Omega\mathscr D[Q_q]}
\tag{102}
\]

式中，\(R_{q,c}\) 为混凝土对无量纲 \(q\) 的广义平衡残量，N·mm；\(f_c,\varepsilon_0\) 见式（2）；\(J_\Omega\) 见式（93）；\(\mathscr D[Q_q]\) 见式（94）、（101）。生产计算中 \(Q_q\) 必须使用 general-D15，不得用旧 restricted basis 静默替换。

---

# 12. 钢筋连续解析闭合

钢筋输入为

\[
\boxed{E_s,\quad f_y,\quad \varepsilon_y,\quad \varepsilon_f,\quad \rho_{s,\alpha}^{(r)},\quad z_s^{(r)}}
\tag{103}
\]

式中，\(E_s\) 为钢筋弹性模量；\(f_y\) 为屈服应力；\(\varepsilon_y\) 为屈服应变；\(\varepsilon_f\) 为来源支允许的最大应变；\(r\) 为钢筋层编号；\(\alpha\) 为钢筋方向；\(\rho_{s,\alpha}^{(r)}\) 为第 \(r\) 层、\(\alpha\) 方向配筋率；\(z_s^{(r)}\) 为相对中面的物理位置，[NGUYEN_SOURCE/PROJECT_REBAR_MAPPING]。

钢筋 current law 为

\[
\boxed{\sigma_s(\varepsilon_s)=\begin{cases}E_s\varepsilon_s,&|\varepsilon_s|\le\varepsilon_y,\\[1mm]f_y\,\operatorname{sgn}(\varepsilon_s),&\varepsilon_y<|\varepsilon_s|\le\varepsilon_f.\end{cases}}
\tag{104}
\]

式中，\(\sigma_s\) 为钢筋轴向应力；\(\operatorname{sgn}\) 为符号函数；其余参数见式（103）。

钢筋方向单位向量为

\[
\boxed{\mathbf n_\alpha=(\cos\theta_\alpha,\sin\theta_\alpha)^T}
\tag{105}
\]

式中，\(\theta_\alpha\) 为钢筋相对 \(x\) 轴的方向角；\(\mathbf n_\alpha\) 为对应单位方向向量。

定义

\[
\boxed{\zeta_r=\frac{2z_s^{(r)}}{t_p},\qquad \varepsilon_{s,\alpha}^{(r)}=\mathbf n_\alpha^T\mathbf E(X,Y,\zeta_r)\mathbf n_\alpha}
\tag{106}
\]

式中，\(\zeta_r\) 为第 \(r\) 层钢筋归一化厚度位置；\(\varepsilon_{s,\alpha}^{(r)}\) 为该层该方向钢筋应变；\(\mathbf E\) 见式（7）、（87）。

展开为

\[
\boxed{\varepsilon_{s,\alpha}^{(r)}=\varepsilon_x\cos^2\theta_\alpha+\varepsilon_y\sin^2\theta_\alpha+\gamma_{xy}\sin\theta_\alpha\cos\theta_\alpha}
\tag{107}
\]

式中，\(\varepsilon_x,\varepsilon_y,\gamma_{xy}\) 见式（87）；\(\theta_\alpha\) 见式（105）。

均匀弥散层等效钢筋片厚为

\[
\boxed{t_{s,\alpha}^{(r)}=\rho_{s,\alpha}^{(r)}t_p}
\tag{108}
\]

式中，\(t_{s,\alpha}^{(r)}\) 为等效钢筋片厚，mm；\(\rho_{s,\alpha}^{(r)}\) 见式（103）；\(t_p\) 见式（77）。

轴向钢筋荷载贡献为

\[
\boxed{P_s(D,q)=-\sum_{r\parallel y}\frac{t_{s,y}^{(r)}}\ell\int_0^b\int_0^\ell\sigma_{s,y}^{(r)}\,dy\,dx}
\tag{109}
\]

式中，\(P_s\) 为钢筋轴向荷载，N；求和遍历全部 \(y\) 向钢筋层；\(t_{s,y}^{(r)}\) 见式（108）；\(\ell,b\) 见式（77）；\(\sigma_{s,y}^{(r)}\) 由式（104）、（107）确定。生产积分仍由 D15 exact moments 闭合。

钢筋 q-广义残量为

\[
\boxed{R_{q,s}(D,q)=\sum_{r,\alpha}t_{s,\alpha}^{(r)}\int_0^b\int_0^\ell\sigma_{s,\alpha}^{(r)}\frac{\partial\varepsilon_{s,\alpha}^{(r)}}{\partial q}\,dy\,dx}
\tag{110}
\]

式中，\(R_{q,s}\) 为钢筋对 \(q\) 的广义残量，N·mm；\(\partial\varepsilon_{s,\alpha}^{(r)}/\partial q\) 由式（107）对 \(q\) 解析求导得到。若一个钢筋方向/层跨越多个尚未正式闭合的材料支，则停止于 `BLOCKED_AT_STEEL_BRANCH`，不得引入空间钢筋材料点网格。

---

# 13. 总平衡、主连通支与极限点

总轴向荷载为

\[
\boxed{P(D,q)=P_c(D,q)+P_s(D,q)}
\tag{111}
\]

式中，\(P\) 为总轴向荷载 observable，N；\(P_c\) 见式（98）；\(P_s\) 见式（109）。

总 q-广义平衡残量为

\[
\boxed{R_q(D,q)=R_{q,c}(D,q)+R_{q,s}(D,q)}
\tag{112}
\]

式中，\(R_q\) 为总 q-广义平衡残量，N·mm；\(R_{q,c}\) 见式（102）；\(R_{q,s}\) 见式（110）。

平衡条件为

\[
\boxed{R_q(D,q)=0}
\tag{113}
\]

式中，式（113）只定义数学平衡集合，不自动给出极限承载力身份。

定义同源偏导

\[
\boxed{P_D=\frac{\partial P}{\partial D},\quad P_q=\frac{\partial P}{\partial q},\quad R_{q,D}=\frac{\partial R_q}{\partial D},\quad R_{q,q}=\frac{\partial R_q}{\partial q}}
\tag{114}
\]

式中，所有偏导必须由同一个有限解析表达直接解析求导或 forward AD 得到，禁止用空间有限差分作为生产导数。

极限函数定义为

\[
\boxed{L(D,q)=P_DR_{q,q}-P_qR_{q,D}}
\tag{115}
\]

式中，\(L\) 为荷载沿 \(R_q=0\) 平衡 level set 的切向驻值函数；各偏导见式（114）。

定义可接受域

\[
\boxed{\mathcal A=\{(D,q):D\ge0,\ q\ge0,\ P\ge0,\ \text{compiler/source/rebar gates 合法},\ P,R_q,\text{及所需导数有限}\}}
\tag{116}
\]

式中，\(\mathcal A\) 为结构生产可接受域；不得根据历史答案人为设置 \(D_{max}\) 或 \(q_{max}\)。

定义全部平衡集合

\[
\boxed{\mathcal E=\{(D,q):R_q(D,q)=0\}}
\tag{117}
\]

式中，\(\mathcal E\) 为二维数学平衡集合。

正则点满足

\[
\boxed{\nabla R_q=(R_{q,D},R_{q,q})\ne\mathbf0}
\tag{118}
\]

式中，\(\nabla R_q\) 为平衡残量梯度；\(\mathbf0\) 为二维零向量。

正则平衡支切向量可取

\[
\boxed{\mathbf t_0=(R_{q,q},-R_{q,D})}
\tag{119}
\]

式中，\(\mathbf t_0\) 与 \(\nabla R_q\) 正交，因此沿 \(R_q=0\) 切向。

有

\[
\boxed{\nabla P\cdot\mathbf t_0=P_DR_{q,q}-P_qR_{q,D}=L}
\tag{120}
\]

式中，\(\nabla P=(P_D,P_q)\)；\(L\) 见式（115）。因此 \(L=0\) 是荷载沿平衡支切向驻值的解析条件。

无载状态为

\[
\boxed{(D,q)=(0,0)}
\tag{121}
\]

式中，初始缺陷 \(q_0\) 已包含在 stress-free 参考几何中，所以无载点不是 \(q=q_0\)。

主连通平衡支定义为

\[
\boxed{\Gamma_0=\operatorname{Conn}_{(0,0)}(\mathcal E\cap\mathcal A)}
\tag{122}
\]

式中，\(\Gamma_0\) 为包含无载点的唯一生产主平衡支；断开的高幅值根不得仅因荷载较大获得生产身份。

定义单位切向量

\[
\boxed{\widehat{\mathbf t}=\pm\frac{(R_{q,q},-R_{q,D})}{\sqrt{R_{q,q}^2+R_{q,D}^2}}}
\tag{123}
\]

式中，正负号在无载点选择使路径进入 \(D>0\) 的方向。

沿支荷载导数为

\[
\boxed{g(s)=\frac{dP}{ds}=\nabla P\cdot\widehat{\mathbf t}}
\tag{124}
\]

式中，\(s\) 为沿 \(\Gamma_0\) 的有向弧长；\(g(s)\) 为平衡支上的荷载切向导数。

正则点上

\[
\boxed{g(s)=0\iff L(D,q)=0}
\tag{125}
\]

式中，等价关系由式（120）、（123）、（124）得到。

极大值要求

\[
\boxed{g(s_u^-)>0,\qquad g(s_u^+)<0}
\tag{126}
\]

式中，\(s_u^-\)、\(s_u^+\) 表示候选点左右两侧；式（126）表示荷载导数发生 \(+\to-\) 符号变化。

定义首个荷载极大值候选集合

\[
\boxed{\mathcal M=\{s_i>0:R_q=0,\ L=0,\ g:+\to-\}}
\tag{127}
\]

式中，\(\mathcal M\) 为主平衡支上的局部最大值候选集合。

首个极大值位置为

\[
\boxed{s_L=\min\mathcal M}
\tag{128}
\]

式中，\(s_L\) 为沿 \(\Gamma_0\) 从无载点出发首先遇到的 \(+\to-\) 极大值位置；这里用下标 \(L\) 表示“limit-point candidate”，避免在完成 tangent gate 前提前写成最终 \(u\)。

对应状态为

\[
\boxed{(D_L,q_L)=\Gamma_0(s_L),\qquad P_L=P(D_L,q_L)}
\tag{129}
\]

式中，\((D_L,q_L)\) 为首个荷载极大值候选；\(P_L\) 为该候选荷载。它在 tangent gate 完成以前只能称为 limit-point candidate，不自动等于最终承载力。

---

# 14. 平衡与极限残量门

定义自然广义功尺度

\[
\boxed{R_{mat}=f_c\varepsilon_0J_\Omega}
\tag{130}
\]

式中，\(R_{mat}\) 为混凝土材料广义功自然尺度，N·mm；\(f_c,\varepsilon_0\) 见式（2）；\(J_\Omega\) 见式（93）。

定义

\[
\boxed{R_{norm}=\frac{|R_q|}{\max(R_{mat},|R_{q,c}|+|R_{q,s}|)}}
\tag{131}
\]

式中，\(R_{norm}\) 为无量纲平衡残量；\(R_q\) 见式（112）；\(R_{q,c},R_{q,s}\) 见式（102）、（110）。

平衡门为

\[
\boxed{R_{norm}\le10^{-5}}
\tag{132}
\]

式中，\(10^{-5}\) 为当前冻结的生产平衡残量门。

定义

\[
\boxed{L_{norm}=\frac{P_DR_{q,q}-P_qR_{q,D}}{|P_DR_{q,q}|+|P_qR_{q,D}|}}
\tag{133}
\]

式中，\(L_{norm}\) 为无量纲极限驻值残量；分子即式（115）的 \(L\)；分母为两个相消大项的自然尺度。

极限驻值门为

\[
\boxed{|L_{norm}|\le10^{-5}}
\tag{134}
\]

式中，\(10^{-5}\) 为当前冻结的极限驻值数值门。

---

# 15. Zhou/Navier full-field current-tangent 稳定审计

定义一致 current tangent field

\[
\boxed{\mathbb C_t(X,Y,\zeta;D,q)=\frac{\partial\boldsymbol\sigma}{\partial\mathbf E}}
\tag{135}
\]

式中，\(\mathbb C_t\) 为与式（76）同源的二维 current tangent field；它可以随 \(X,Y,\zeta,D,q\) 连续变化，[PROJECT_ZHOU_TANGENT]。

定义基本 Navier 微扰形函数

\[
\boxed{\varphi(X,Y)=\sin X\sin Y}
\tag{136}
\]

式中，\(\varphi\) 为与当前完整代表半波一致的基本微扰模态，[ZHOU_SOURCE/PROJECT_ZHOU_TANGENT]。

定义基本波数

\[
\boxed{\alpha=\frac{\pi}{b},\qquad \beta=\frac{\pi}{\ell}}
\tag{137}
\]

式中，\(\alpha,\beta\) 分别为 \(x,y\) 方向基本波数，mm\(^{-1}\)；\(b,\ell\) 见式（77）。

一阶导数为

\[
\boxed{\varphi_{,x}=\alpha\cos X\sin Y,\qquad \varphi_{,y}=\beta\sin X\cos Y}
\tag{138}
\]

式中，\(\varphi_{,x},\varphi_{,y}\) 为对物理坐标 \(x,y\) 的一阶导数。

二阶导数为

\[
\boxed{\varphi_{,xx}=-\alpha^2\varphi,\qquad \varphi_{,yy}=-\beta^2\varphi,\qquad \varphi_{,xy}=\alpha\beta\cos X\cos Y}
\tag{139}
\]

式中，\(\varphi_{,xx},\varphi_{,yy},\varphi_{,xy}\) 为对物理坐标的二阶导数。

定义单位物理微扰幅值对应的弯曲工程应变向量

\[
\boxed{\mathbf b_\varphi=-z\begin{bmatrix}\varphi_{,xx}\\\varphi_{,yy}\\2\varphi_{,xy}\end{bmatrix}}
\tag{140}
\]

式中，\(\mathbf b_\varphi\) 为微扰弯曲工程应变向量，mm\(^{-1}\)；\(z=t_p\zeta/2\)；第三分量中的 2 为工程剪切曲率约定。

混凝土 material-tangent 模态刚度为

\[
\boxed{K_{Z,c}^{mat}=\int_{\Omega_h}\mathbf b_\varphi^T\mathbf C_t^{eng}\mathbf b_\varphi\,dV}
\tag{141}
\]

式中，\(K_{Z,c}^{mat}\) 为混凝土材料切线模态刚度，N/mm；\(\mathbf C_t^{eng}\) 为式（135）按 \((\varepsilon_x,\varepsilon_y,\gamma_{xy})\to(\sigma_x,\sigma_y,\tau_{xy})\) 写成的工程切线矩阵；该积分必须由 general-D15 精确闭合。

混凝土 current-stress 几何模态刚度为

\[
\boxed{K_{Z,c}^{geo}=\int_{\Omega_h}(\sigma_x\varphi_{,x}^2+2\tau_{xy}\varphi_{,x}\varphi_{,y}+\sigma_y\varphi_{,y}^2)\,dV}
\tag{142}
\]

式中，\(K_{Z,c}^{geo}\) 为混凝土几何模态刚度，N/mm；\(\sigma_x,\sigma_y,\tau_{xy}\) 来自式（76）；\(\varphi_{,x},\varphi_{,y}\) 见式（138）；该积分同样由 general-D15 精确闭合。

钢筋 current tangent 为

\[
\boxed{E_{s,t}^{(r,\alpha)}=\frac{d\sigma_{s,\alpha}^{(r)}}{d\varepsilon_{s,\alpha}^{(r)}}}
\tag{143}
\]

式中，\(E_{s,t}^{(r,\alpha)}\) 为第 \(r\) 层、\(\alpha\) 方向钢筋当前一维切线；弹性支为 \(E_s\)，当前理想塑性支为 0。

定义微扰曲率张量

\[
\boxed{\boldsymbol\kappa_\varphi=-\begin{bmatrix}\varphi_{,xx}&\varphi_{,xy}\\\varphi_{,xy}&\varphi_{,yy}\end{bmatrix}}
\tag{144}
\]

式中，\(\boldsymbol\kappa_\varphi\) 为微扰模态曲率张量；其分量由式（139）确定。

钢筋 material-tangent 模态刚度为

\[
\boxed{K_{Z,s}^{mat}=\sum_{r,\alpha}t_{s,\alpha}^{(r)}\int_A E_{s,t}^{(r,\alpha)}[z_s^{(r)}\mathbf n_\alpha^T\boldsymbol\kappa_\varphi\mathbf n_\alpha]^2\,dA}
\tag{145}
\]

式中，\(K_{Z,s}^{mat}\) 为钢筋材料切线模态刚度；\(t_s\) 见式（108）；\(A=[0,b]\times[0,\ell]\) 为半波中面；\(z_s^{(r)}\) 见式（103）；\(\mathbf n_\alpha\) 见式（105）。

钢筋 current-stress 几何模态刚度为

\[
\boxed{K_{Z,s}^{geo}=\sum_{r,\alpha}t_{s,\alpha}^{(r)}\int_A\sigma_{s,\alpha}^{(r)}(\mathbf n_\alpha\cdot\nabla\varphi)^2\,dA}
\tag{146}
\]

式中，\(K_{Z,s}^{geo}\) 为钢筋几何模态刚度；\(\nabla\varphi=(\varphi_{,x},\varphi_{,y})\)；其余符号见式（104）—（108）。

总模态 current tangent 为

\[
\boxed{K_Z=K_{Z,c}^{mat}+K_{Z,c}^{geo}+K_{Z,s}^{mat}+K_{Z,s}^{geo}}
\tag{147}
\]

式中，\(K_Z\) 为完整代表半波基本 Navier 模态的 generalized current tangent，N/mm；四项分别见式（141）、（142）、（145）、（146）。

稳定解释为

\[
\boxed{K_Z>0:\ \text{正模态切线};\qquad K_Z=0:\ \text{模态临界};\qquad K_Z<0:\ \text{负模态切线}}
\tag{148}
\]

式中，\(K_Z\) 见式（147）。Zhou 在这里提供 current-tangent stability audit / interpretation，不单独生成第二套极限承载力根。

必须注意，由于

\[
\boxed{\mathbf X=\frac{\mathbf E_u}{\varepsilon_0}}
\tag{149}
\]

式中，\(\mathbf X\) 见式（9）；\(\mathbf E_u\) 见式（8）；\(\varepsilon_0\) 见式（2），因此做 current tangent 方向导数时必须保留 \(1/\varepsilon_0\) 缩放。

对应增量关系为

\[
\boxed{\delta\mathbf X=\frac{\delta\mathbf E_u}{\varepsilon_0}}
\tag{150}
\]

式中，\(\delta\mathbf X\) 为无量纲等效应变增量；\(\delta\mathbf E_u\) 为等效单轴应变增量；遗漏 \(1/\varepsilon_0\) 会导致 material tangent 整体尺度错误。

---

# 16. 与周思铭方向刚度语言的模态投影

定义面积归一化量

\[
\boxed{I_\varphi=\int_A\varphi^2dA=\frac{b\ell}{4},\qquad I_\psi=\int_A(\cos X\cos Y)^2dA=\frac{b\ell}{4}}
\tag{151}
\]

式中，\(I_\varphi\) 为双正弦模态平方面积积分；\(I_\psi\) 为双余弦模态平方面积积分；\(A\) 为完整半波中面域。

定义非均匀 current tangent 的方向投影

\[
\boxed{D_x^*=\frac1{I_\varphi}\int_{\Omega_h}z^2C_{xx,t}\varphi^2dV,\qquad D_y^*=\frac1{I_\varphi}\int_{\Omega_h}z^2C_{yy,t}\varphi^2dV}
\tag{152}
\]

式中，\(D_x^*,D_y^*\) 分别为次方向和主方向模态投影弯曲刚度，N·mm；\(C_{xx,t},C_{yy,t}\) 为式（135）的工程切线分量。

交叉法向与剪切投影为

\[
\boxed{D_\mu^*=\frac1{I_\varphi}\int_{\Omega_h}z^2\frac{C_{xy,t}+C_{yx,t}}2\varphi^2dV,\qquad D_{66}^*=\frac1{I_\psi}\int_{\Omega_h}z^2G_t(\cos X\cos Y)^2dV}
\tag{153}
\]

式中，\(D_\mu^*\) 为交叉法向 current tangent 的对称投影；\(D_{66}^*\) 为工程剪切 current tangent 模态投影；\(C_{xy,t},C_{yx,t},G_t\) 均来自同一个 \(\mathbb C_t\)。

定义

\[
\boxed{H^*=D_\mu^*+2D_{66}^*}
\tag{154}
\]

式中，\(H^*\) 为当前 RC current tangent 对周思铭 \(H=D_{xy}+D_\mu\) 方向刚度语言的项目等效模态投影，只用于稳定刚度分解和审计。

混凝土材料模态刚度可重写为

\[
\boxed{K_{Z,c}^{mat}=I_\varphi[D_x^*\alpha^4+2H^*\alpha^2\beta^2+D_y^*\beta^4]}
\tag{155}
\]

式中，\(I_\varphi\) 见式（151）；\(D_x^*,D_y^*,H^*\) 见式（152）—（154）；\(\alpha,\beta\) 见式（137）。

当 current tangent 在板面和厚度上为常量时，式（152）—（154）退化为

\[
\boxed{D_x^*=\frac{t_p^3}{12}C_{xx,t},\quad D_y^*=\frac{t_p^3}{12}C_{yy,t},\quad D_\mu^*=\frac{t_p^3}{24}(C_{xy,t}+C_{yx,t}),\quad D_{66}^*=\frac{t_p^3}{12}G_t}
\tag{156}
\]

式中，各切线分量均为均匀常量；旧的 \(t_p^3C_t/12\) 写法只保留为 uniform-tangent degeneration，而不是非均匀场的一般定义。

若进一步为均匀纯 \(y\) 向压缩，则可写 Zhou/Navier 临界膜力形式

\[
\boxed{N_{y,cr}^{Z,*}=\frac{D_x^*\alpha^4+2H^*\alpha^2\beta^2+D_y^*\beta^4}{\beta^2}}
\tag{157}
\]

式中，\(N_{y,cr}^{Z,*}\) 为均匀纯轴压退化情况下的 Zhou/Navier 临界膜力；一般 nonlinear current state 使用完整 \(K_Z\)，不直接套式（157）。

---

# 17. 极限点与 tangent-loss 的统一控制逻辑

沿正确的主平衡支 \(\Gamma_0\) 定义 tangent 临界集合

\[
\boxed{\mathcal T=\{s>0:K_Z[\Gamma_0(s)]=0\}}
\tag{158}
\]

式中，\(\mathcal T\) 为主平衡支上所有 admissible tangent-zero 状态的有向弧长集合；\(K_Z\) 见式（147）；\(\Gamma_0\) 见式（122）。

若 \(\mathcal T\neq\varnothing\)，定义首个 tangent 临界位置

\[
\boxed{s_T=\min\mathcal T}
\tag{159}
\]

式中，\(s_T\) 为从无载点沿正确主平衡支首次遇到 \(K_Z=0\) 的位置。

若在首个荷载极大值之前始终有

\[
\boxed{K_Z[\Gamma_0(s)]>0,\qquad 0<s\le s_L}
\tag{160}
\]

式中，\(s_L\) 见式（128）；则 limit-point candidate 通过 pre-limit tangent-stability gate，可进入最终理论结果冻结。

若存在

\[
\boxed{s_T<s_L}
\tag{161}
\]

式中，\(s_T\) 见式（159）；\(s_L\) 见式（128），则说明基本 Navier 模态的 current tangent 在荷载极大值以前先损失。此时后续 \(P_L\) 不得直接冻结为最终承载力；执行状态为 `BLOCKED_AT_PRELIMIT_TANGENT_LOSS`，直到另有明确治理决定定义该 tangent 临界点是否以及如何获得最终容量身份。本理论不静默建立第二套 Pu solver。

若二者在冻结根重复性容差内重合，则

\[
\boxed{s_T\doteq s_L}
\tag{162}
\]

式中，\(\doteq\) 表示在冻结 root-repeatability tolerance 内相等；此时状态记为 `COUPLED_LIMIT_TANGENT_CONTROL`，并同时保留 \(R_q,L,K_Z\) 三类残量记录。

---

# 18. 完整计算闭合的强制门

任意案例只有在以下链条全部完成后，才允许标记 `CALCULATION_CLOSURE = PASS`：

```text
1. 原始材料与几何输入
2. R10 派生参数
3. fresh 49×4 N48 coefficient table
4. C1/MM 材料值与切线 fidelity records
5. 连续 compiler-domain certificate
6. general-D15 Syy contraction
7. general-D15 Qq contraction
8. 钢筋 supported-branch certificate
9. 用同一 general-D15 Rq 建立正确 Gamma0
10. 首个 +→− limit-point candidate + R_norm/L_norm
11. zero-state K_Z regression
12. KZ,c^mat
13. KZ,c^geo
14. KZ,s^mat
15. KZ,s^geo
16. total K_Z along the same corrected Gamma0
17. 证明首个 K_Z=0 是否早于首个 +→− limit point
18. 最终理论结果冻结
19. 只在第 18 项以后读取试验值作最终比较
```

任何第 6—17 项缺失，都不得把候选荷载称为当前理论最终极限承载力。

---

# 19. 当前 Case21 状态（截至 20260812_1734）

当前已确认：

```text
R10 = FROZEN
N48-C1/MM = GOVERNING
CAYLEY_HAMILTON = GOVERNING
NGUYEN_SECOND_ORDER = GOVERNING
D15_GENERAL_TRIG_MOMENTS = GOVERNING
ZERO_FORMAL_SPATIAL_DISCRETIZATION = PASS
ZERO_STATE_TANGENT_REGRESSION = PASS
```

但在把 tangent gate 正式加入案例合同后，对此前 Case21 候选状态重新用 governing general-D15 检查，发现：

```text
GENERAL_D15_Syy_RECHECK = PASS
GENERAL_D15_Qq_RECHECK = FAIL_AGAINST_PREVIOUS_CASE21_EXECUTION
PREVIOUS_CASE21_GAMMA0 = NOT CURRENTLY ACCEPTED
PREVIOUS_CASE21_LIMIT_LOAD = AUDIT RECORD ONLY / NOT CURRENT PRODUCTION RESULT
PRODUCTION_TANGENT_GATE = NOT YET REACHED ON A CORRECTED BRANCH
CASE21_COMPLETE_CLOSURE = BLOCKED
```

因此下一步唯一正确执行顺序为：

\[
\boxed{
\text{fresh general-D15 }R_q(D,q)
\rightarrow \Gamma_0
\rightarrow \text{first }+\to-\text{ limit candidate}
\rightarrow K_Z\text{ along the same }\Gamma_0
\rightarrow \text{final control classification}
}
\tag{163}
\]

式中，所有量均必须从当前理论与原始 Case21 输入重新产生；不得使用任何历史 Case21 根、历史理论荷载、历史 FE/Gauss/Simpson 结果或试验值作为求根、定参、选根和路径识别依据。
