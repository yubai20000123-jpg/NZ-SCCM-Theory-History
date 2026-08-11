# NZ-SCCM 三个代表板独立复算与可行性审计包
## Case 1、Case 14、Case 21：闭式 R10 → N48 → Cayley–Hamilton → D15 → \(R_q=0,L=0\)

**用途**：供另一个全新聊天/独立审计者从公式重新实现并复算，用于判断当前零空间解析计算是否真正闭合、是否存在明显量纲错误、共轭错误、错误积分或把历史结果偷偷作为输入的问题。

**为什么选 Case 1、14、21**：Nguyen 对 Swartz 24 块板的三组分别以 panel 1、panel 14、panel 21 展示/讨论代表性屈曲形态；三者分别对应约 \(b/t\approx48\)、\(38\)、\(63\)，跨越三个板厚/宽厚比组。

## 0. 执行合同

\[
\text{DOMAIN}=\text{ONE CONTINUOUS COMPLETE HALFWAVE},\qquad m=1
\]

\[
N_{\rm formal,spatial\,sampling}=0,\quad N_{\rm formal,spatial\,quadrature}=0,\quad N_{\rm formal,spatial\,subdomains}=1.
\]

正式结构积分禁止 Gauss、Simpson、adaptive quadrature、空间 Chebyshev collocation、材料点网格和空间 cells。允许一维材料坐标 N48 编译、有限系数代数、Cayley–Hamilton 递推、D15 闭式矩以及最终在广义变量 \(D,q\) 上低维求根。试验值只能在理论结果冻结以后比较。

# 1. 闭式 R10 current material operator

\[
\kappa=\frac{E_0\varepsilon_0}{f_c},\qquad x_{cr}=\frac{\rho}{\kappa},\qquad \rho=0.1,\qquad \eta=\frac{x_{cr}}{20}.
\]

\[
\mathbf E=\begin{bmatrix}\varepsilon_x&\gamma_{xy}/2\\\gamma_{xy}/2&\varepsilon_y\end{bmatrix},\qquad
\mathbf E_u=\frac{(1-\nu)\mathbf E+\nu\,{\rm tr}(\mathbf E)\mathbf I}{1-\nu^2},\qquad
\mathbf X=\frac{\mathbf E_u}{\varepsilon_0}.
\]

\[
\mu=\frac{X_{11}+X_{22}}2,\quad \delta=\frac{X_{11}-X_{22}}2,\quad r_X=\sqrt{\delta^2+X_{12}^2},\quad \lambda_\pm=\mu\pm r_X.
\]

\[
\Pi_\eta(z)=\frac{z^2(\sqrt{z^2+\eta^2}+z)}{2(z^2+\eta^2)},\qquad t_i=\Pi_\eta(\lambda_i),\quad c_i=\Pi_\eta(-\lambda_i).
\]

\[
C_i=\frac{\kappa c_i}{1+(\kappa-2)c_i+c_i^2}.
\]

Foster 源拉伸：
\[
r=t/x_{cr},\qquad m_t=-7/90,\qquad \eta_r=0.05,
\]
\[
H(r,r_0)=\frac12[(r-r_0)+\sqrt{(r-r_0)^2+\eta_r^2}]-\frac12[-r_0+\sqrt{r_0^2+\eta_r^2}],
\]
\[
T_{\rm src}(r)=r+(m_t-1)H(r,1)-m_tH(r,10).
\]

\[
W_{\rm src}=\rho x_{cr}\int_0^{10}T_{\rm src}(r)\,dr,\qquad \int_0^{10}T_{\rm src}(r)\,dr\approx6.349875.
\]

取 \(u_r=0.03\)：
\[
h=\frac15\left[\frac{W_{\rm src}}{x_{cr}}-\frac{\rho}{10}-\frac92u_r\right].
\]

上升支：
\[
u_1(\tau)=\rho\tau+(10h-6\rho)\tau^3+(8\rho-15h)\tau^4+(6h-3\rho)\tau^5.
\]

下降支：
\[
u_2(s)=h+(u_r-h)(10s^3-15s^4+6s^5).
\]

\[
T_i=u_{\rm sm}(t_i)/\rho,
\qquad
U_i=\kappa\lambda_i-C_i+\kappa c_i+\rho T_i-\kappa t_i.
\]

\[
s_+=U_+-a_{cc}C_+^2C_-+C_+T_- -\rho a_tT_+T_-^8,
\]
\[
s_-=U_--a_{cc}C_-^2C_+ + C_-T_+ -\rho a_tT_-T_+^8,
\]
其中 \(a_{cc}=0.1072329249\)，\(a_t=1-2^{-1/8}\)。谱返回后物理应力为 \(\boldsymbol\sigma=f_c\mathbf S\)。

# 2. N48 材料解析目标函数

唯一编译目标：
\[
F\in\{U,C,T,T^7\}.
\]

\[
\lambda_c=(\lambda_a+\lambda_b)/2,\qquad \lambda_h=(\lambda_b-\lambda_a)/2,\qquad \xi=(\lambda-\lambda_c)/\lambda_h.
\]

\[
F_{48}(\lambda)=\sum_{n=0}^{48}a_n^{(F)}\mathcal C_n(\xi).
\]

\[
\theta_j=\frac{(j+1/2)\pi}{49},\qquad \lambda_j=\lambda_c+\lambda_h\cos\theta_j.
\]

\[
\boxed{a_n^{(F)}=\frac{2-\delta_{n0}}{49}\sum_{j=0}^{48}F(\lambda_j)\cos(n\theta_j)}.
\]

这里没有结构 \(P_u\) 拟合；只有材料函数的有限解析编译。

# 3. Cayley–Hamilton 提升

\[
\mathbf Y=(\mathbf X-\lambda_c\mathbf I)/\lambda_h,\quad K_1={\rm tr}\mathbf Y,\quad K_2=\det\mathbf Y.
\]

\[
\mathbf Y^2-K_1\mathbf Y+K_2\mathbf I=0.
\]

\[
\mathcal C_n(\mathbf Y)=A_n\mathbf I+B_n\mathbf Y,
\]
\[
A_0=1,\ B_0=0,\quad A_1=0,\ B_1=1,
\]
\[
A_{n+1}=-2K_2B_n-A_{n-1},\qquad B_{n+1}=2A_n+2K_1B_n-B_{n-1}.
\]

再构造
\[
\mathbf{CC}=\det(\mathbf C)\mathbf C,
\]
\[
\mathbf{TC}=\mathbf C[{\rm tr}(\mathbf T)\mathbf I-\mathbf T],
\]
\[
\mathbf{TT}=\det(\mathbf T)[{\rm tr}(\mathbf T^{(7)})\mathbf I-\mathbf T^{(7)}],
\]
\[
\mathbf S=\mathbf U-a_{cc}\mathbf{CC}+\mathbf{TC}-\rho a_t\mathbf{TT}.
\]

# 4. Nguyen 连续二阶完整半波运动学

三个代表板均采用
\[
b=\ell=1220\ {\rm mm},\qquad q_0=1/400.
\]

\[
X=\pi x/b,\quad Y=\pi y/\ell,\quad \zeta=2z/t_p,\quad q=A/b.
\]

\[
C_m=\frac{\pi^2}{\varepsilon_0}\left(q_0q+\frac12q^2\right),\qquad C_b=\frac{\pi^2}{2\varepsilon_0}\frac{t_p}{b}q.
\]

\[
e_x=\nu D+C_m\cos^2X\sin^2Y+C_b\sin X\sin Y\,\zeta,
\]
\[
e_y=-D+C_m\sin^2X\cos^2Y+C_b\sin X\sin Y\,\zeta,
\]
\[
g_{xy}=2C_m\sin X\cos X\sin Y\cos Y-2C_b\cos X\cos Y\,\zeta.
\]

\[
\varepsilon_x=\varepsilon_0e_x,\quad \varepsilon_y=\varepsilon_0e_y,\quad \gamma_{xy}=\varepsilon_0g_{xy}.
\]

# 5. D15 零空间解析积分

\[
Q=\sum_{ijk}c_{ijk}\mathcal C_i(\sin X)\mathcal C_j(\sin Y)\mathcal C_k(\zeta).
\]

\[
M_n=\begin{cases}\pi,&n=0,\\2\sin(n\pi/2)/n,&n\ge1,\end{cases}\qquad
Z_k=\begin{cases}0,&k\text{ odd},\\2/(1-k^2),&k\text{ even}.\end{cases}
\]

\[
\boxed{\mathscr D[Q]=\sum c_{ijk}M_iM_jZ_k}.
\]

混凝土轴力：
\[
\boxed{P_c=-\frac{f_cbt_p}{2\pi^2}\mathscr D[S_{yy}]}.
\]

物理功共轭：
\[
\mathbf e=\mathbf E/\varepsilon_0=(1+\nu)\mathbf X-\nu{\rm tr}(\mathbf X)\mathbf I,
\]
\[
Q_q=\mathbf S:\mathbf e_{,q}.
\]

\[
R_{q,c}=f_c\varepsilon_0J_\Omega\mathscr D[Q_q],\qquad J_\Omega=\frac{b\ell t_p}{2\pi^2}.
\]

# 6. 钢筋与极限联立

\[
E_s=200000\ {\rm MPa},\qquad \varepsilon_y=0.00265,\qquad f_y=530\ {\rm MPa}.
\]

若最终连续钢筋场满足 \(|\varepsilon_s|<\varepsilon_y\)，则 \(\sigma_s=E_s\varepsilon_s\)。加载方向总钢筋轴力为
\[
P_s=\rho_{s,y}bt_pE_s\varepsilon_0\left(D-\frac{C_m}{4}\right).
\]

钢筋幅值广义残量：
\[
R_{q,s}=\sum_{\alpha,\ell}\int_\Omega\sigma_{s,\alpha}^{(\ell)}\frac{\partial\varepsilon_{s,\alpha}^{(\ell)}}{\partial q}\,dA.
\]

\[
P=P_c+P_s,\qquad R_q=R_{q,c}+R_{q,s}.
\]

\[
\boxed{R_q(D,q)=0},
\]
\[
\boxed{L(D,q)=P_{,D}R_{q,q}-P_{,q}R_{q,D}=0}.
\]

# Case 1：逐项复算记录

## 1.1 输入
\[
t_p=25.40\ {\rm mm},\quad f_c=22.81\ {\rm MPa},\quad E_0=21730\ {\rm MPa},\quad \varepsilon_0=0.00210,\quad \nu=0.18.
\]
\[
\rho_{s,tot}=0.20\%,\qquad \text{中面单层钢筋 }z=0,
\]
\[
[\lambda_a,\lambda_b]=[-1.12,0.105].
\]

## 1.2 R10
\[
\kappa=2.000570,\quad x_{cr}=0.0499858,\quad \eta=0.0024993,
\]
\[
W_{src}=0.03174033,\qquad h=0.0979975.
\]

## 1.3 N48
\[
\lambda_c=-0.5075,\qquad \lambda_h=0.6125.
\]

|函数|a0|a1|a2|a3|
|---|---:|---:|---:|---:|
|U|-0.5961799|0.5817486|0.1886941|-0.0140869|
|C|0.6126927|-0.5502477|-0.1615733|0.0347070|
|T|0.1654462|0.3151309|0.2707760|0.2053650|
|T^7|0.1288327|0.2475590|0.2186527|0.1749495|

## 1.4 联立极限状态
\[
D_u=0.9940492,\qquad q_u=0.000773995,\qquad A_u=0.9443\ {\rm mm}.
\]
\[
C_m=0.0105018,\qquad C_b=0.0378671.
\]
\[
\lambda\in[-1.0447,0.0506]\subset[-1.12,0.105].
\]

## 1.5 D15 混凝土轴力
\[
K_P=\frac{f_cbt_p}{2\pi^2}/1000=35.808744\ {\rm kN},
\]
\[
\mathscr D[S_{yy}]=-16.3818242,
\]
\[
P_c=586.613\ {\rm kN}.
\]

## 1.6 D15 幅值残量
\[
J_\Omega=1915241.9\ {\rm mm^3},\qquad K_R=91.742003\ {\rm kN\,mm},
\]
\[
\mathscr D[Q_q]=1.1231377,
\]
\[
R_{q,c}=103.039\ {\rm kN\,mm}.
\]

## 1.7 钢筋
\[
\bar\varepsilon_{s,y}=-0.0020820,
\]
\[
P_s=12.903\ {\rm kN},\qquad R_{q,s}=-103.039\ {\rm kN\,mm},
\]
\[
R_q=-2.799\times10^{-5}\ {\rm kN\,mm}.
\]

## 1.8 同源导数与极限式
\[
P_{,D}=18.6177,\quad P_{,q}=-150824,
\]
\[
R_{q,D}=-836.875,\quad R_{q,q}=6.77957\times10^6.
\]
\[
P_{,D}R_{q,q}\approx1.262200\times10^8,\qquad P_{,q}R_{q,D}\approx1.262209\times10^8.
\]
\[
L=-911.212,\qquad L_{norm}=-3.610\times10^{-6}.
\]
\[
\boxed{P_u=599.516\ {\rm kN}}.
\]

## 1.9 最后比较试验
\[
P_{f,exp}=490.194\ {\rm kN},\qquad \text{error}=+22.30\%.
\]

# Case 14：逐项复算记录

## 14.1 输入
\[
t_p=32.26\ {\rm mm},\quad f_c=16.82\ {\rm MPa},\quad E_0=17995\ {\rm MPa},\quad \varepsilon_0=0.00187,\quad \nu=0.18.
\]
\[
\rho_{s,tot}=0.75\%,\qquad \text{对称双层钢筋 }z=\pm12.63\ {\rm mm},
\]
\[
[\lambda_a,\lambda_b]=[-1.17,0.105].
\]

## 14.2 R10
\[
\kappa=2.000633,\quad x_{cr}=0.0499842,\quad \eta=0.0024992,
\]
\[
W_{src}=0.03173933,\qquad h=0.0979975.
\]

## 14.3 N48
\[
\lambda_c=-0.5325,\qquad \lambda_h=0.6375.
\]

|函数|a0|a1|a2|a3|
|---|---:|---:|---:|---:|
|U|-0.6049691|0.5761272|0.2018389|-0.0101496|
|C|0.6211847|-0.5451431|-0.1750202|0.0307626|
|T|0.1622382|0.3095869|0.2675999|0.2054050|
|T^7|0.1258480|0.2422806|0.2152898|0.1742890|

## 14.4 联立极限状态
\[
D_u=1.0872558,\qquad q_u=0.000441917,\qquad A_u=0.5391\ {\rm mm}.
\]
\[
C_m=0.0063463,\qquad C_b=0.0308371.
\]
\[
\lambda\in[-1.1276,0.0403]\subset[-1.17,0.105].
\]

## 14.5 D15 混凝土轴力
\[
K_P=33.536709\ {\rm kN},\qquad \mathscr D[S_{yy}]=-17.0003013,
\]
\[
P_c=570.134\ {\rm kN}.
\]

## 14.6 D15 幅值残量
\[
J_\Omega=2432508.0\ {\rm mm^3},\qquad K_R=76.510648\ {\rm kN\,mm},
\]
\[
\mathscr D[Q_q]=4.5647994,
\]
\[
R_{q,c}=349.256\ {\rm kN\,mm}.
\]

## 14.7 钢筋
\[
\bar\varepsilon_{s,y}=-0.0020302,
\]
\[
P_s=59.927\ {\rm kN},\qquad R_{q,s}=-349.256\ {\rm kN\,mm},
\]
\[
R_q=-2.550\times10^{-6}\ {\rm kN\,mm}.
\]

## 14.8 同源导数与极限式
\[
P_{,D}=12.6193,\quad P_{,q}=-174080,
\]
\[
R_{q,D}=-967.805,\quad R_{q,q}=1.33507\times10^7.
\]
\[
P_{,D}R_{q,q}\approx1.684760\times10^8,\qquad P_{,q}R_{q,D}\approx1.684760\times10^8.
\]
\[
L=0.00902644,\qquad L_{norm}=2.679\times10^{-11}.
\]
\[
\boxed{P_u=630.061\ {\rm kN}}.
\]

## 14.9 最后比较试验
\[
P_{f,exp}=716.164\ {\rm kN},\qquad \text{error}=-12.02\%.
\]

# Case 21：逐项复算记录

## 21.1 输入
\[
t_p=19.30\ {\rm mm},\quad f_c=21.23\ {\rm MPa},\quad E_0=20321\ {\rm MPa},\quad \varepsilon_0=0.00209,\quad \nu=0.18.
\]
\[
\rho_{s,tot}=0.75\%,\qquad \text{中面单层钢筋 }z=0,
\]
\[
[\lambda_a,\lambda_b]=[-1.01,0.105].
\]

## 21.2 R10
\[
\kappa=2.000513,\quad x_{cr}=0.0499872,\quad \eta=0.0024994,
\]
\[
W_{src}=0.03174124,\qquad h=0.0979975.
\]

## 21.3 N48
\[
\lambda_c=-0.4525,\qquad \lambda_h=0.5575.
\]

|函数|a0|a1|a2|a3|
|---|---:|---:|---:|---:|
|U|-0.5725245|0.5896062|0.1583082|-0.0213950|
|C|0.5898865|-0.5566570|-0.1304207|0.0418748|
|T|0.1732978|0.3285239|0.2779514|0.2042676|
|T^7|0.1358016|0.2598423|0.2263622|0.1762424|

## 21.4 联立极限状态
\[
D_u=0.8359179,\qquad q_u=0.001789789,\qquad A_u=2.1835\ {\rm mm}.
\]
\[
C_m=0.0286934,\qquad C_b=0.0668533.
\]
\[
\lambda\in[-0.9296,0.0937]\subset[-1.01,0.105].
\]

## 21.5 D15 混凝土轴力
\[
K_P=25.324297\ {\rm kN},\qquad \mathscr D[S_{yy}]=-13.3311398,
\]
\[
P_c=337.602\ {\rm kN}.
\]

## 21.6 D15 幅值残量
\[
J_\Omega=1455282.2\ {\rm mm^3},\qquad K_R=64.571892\ {\rm kN\,mm},
\]
\[
\mathscr D[Q_q]=4.8210841,
\]
\[
R_{q,c}=311.307\ {\rm kN\,mm}.
\]

## 21.7 钢筋
\[
\bar\varepsilon_{s,y}=-0.0017321,
\]
\[
P_s=30.588\ {\rm kN},\qquad R_{q,s}=-311.307\ {\rm kN\,mm},
\]
\[
R_q=1.346\times10^{-9}\ {\rm kN\,mm}.
\]

## 21.8 同源导数与极限式
\[
P_{,D}=111.46,\quad P_{,q}=-75581.6,
\]
\[
R_{q,D}=-1417.52,\quad R_{q,q}=961233.
\]
\[
P_{,D}R_{q,q}\approx1.071388\times10^8,\qquad P_{,q}R_{q,D}\approx1.071387\times10^8.
\]
\[
L=49.7771,\qquad L_{norm}=2.323\times10^{-7}.
\]
\[
\boxed{P_u=368.189\ {\rm kN}}.
\]

## 21.9 最后比较试验
\[
P_{f,exp}=368.313\ {\rm kN},\qquad \text{error}=-0.03\%.
\]

# 7. 独立审计时必须逐项检查

1. \(x_{cr}=\rho/\kappa\) 是否写反；
2. \(T=u_{\rm sm}/\rho\) 是否写反；
3. \(h\) 是否只由材料功得到；
4. N48 根点是否只是材料坐标点；
5. \(T^7\) 是否作为标量目标函数直接编译；
6. \(q_0q+\frac12q^2\) 是否保留；
7. \(P_c\) 是否保持截面力量纲；
8. \(Q_q=\mathbf S:\mathbf e_{,q}\) 是否保持物理功共轭；
9. D15 是否只有 \(M_iM_jZ_k\) 收缩；
10. 钢筋是否在求 \(R_q,L\) 前已进入总体系；
11. 导数是否来自同一解析表达而不是有限差分；
12. 是否同时满足 \(R_q=0\) 与 \(L=0\)；
13. 是否在理论冻结后才读取试验值。

若独立复算与这里不同，必须指出首次分歧层级：`R10 / N48 / CH / KINEMATICS / D15 / STEEL / Rq / L`，不得通过调参把最后 \(P_u\) 调回来。
