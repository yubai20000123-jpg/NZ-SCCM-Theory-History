# NZ-SCCM 三个代表板独立复算与可行性审计包
## Case 1、Case 14、Case 21：闭式 R10 → N48 → Cayley–Hamilton → D15 → \(R_q=0,L=0\)

**用途**：供另一个全新聊天/独立审计者从公式重新实现并复算，用于判断当前零空间解析计算是否真正闭合、是否存在明显量纲错误、共轭错误、错误积分或把历史结果偷偷作为输入的问题。

**为什么选 Case 1、14、21**：Nguyen 对 Swartz 24 块板的三组分别以 panel 1、panel 14、panel 21 展示/讨论代表性屈曲形态；三者分别对应约 \(b/t\approx48\)、\(38\)、\(63\)，跨越三个板厚/宽厚比组。

## 0. 执行合同

\[
\text{DOMAIN}=\text{ONE CONTINUOUS COMPLETE HALFWAVE},\qquad m=1
\]

\[
N_{\rm formal,spatial\,sampling}=0,\quad
N_{\rm formal,spatial\,quadrature}=0,\quad
N_{\rm formal,spatial\,subdomains}=1.
\]

正式结构积分禁止 Gauss、Simpson、adaptive quadrature、空间 Chebyshev collocation、材料点网格和空间 cells。允许一维材料坐标 N48 编译、有限系数代数、Cayley–Hamilton 递推、D15 闭式矩以及最终在广义变量 \(D,q\) 上低维求根。

试验值只能在理论结果冻结以后比较。

# 1. 闭式 R10 current material operator

\[
\kappa=\frac{E_0\varepsilon_0}{f_c},\qquad
x_{cr}=\frac{\rho}{\kappa},\qquad
\rho=0.1,\qquad
\eta=\frac{x_{cr}}{20}.
\]

物理面内应变：
\[
\mathbf E=\begin{bmatrix}\varepsilon_x&\gamma_{xy}/2\\\gamma_{xy}/2&\varepsilon_y\end{bmatrix}.
\]

等效单轴张量：
\[
\mathbf E_u=\frac{(1-\nu)\mathbf E+\nu\,{\rm tr}(\mathbf E)\mathbf I}{1-\nu^2},\qquad
\mathbf X=\frac{\mathbf E_u}{\varepsilon_0}.
\]

主值：
\[
\mu=\frac{X_{11}+X_{22}}2,\quad
\delta=\frac{X_{11}-X_{22}}2,\quad
r_X=\sqrt{\delta^2+X_{12}^2},\qquad
\lambda_\pm=\mu\pm r_X.
\]

平滑拉压坐标：
\[
\Pi_\eta(z)=\frac{z^2(\sqrt{z^2+\eta^2}+z)}{2(z^2+\eta^2)},
\]
\[
t_i=\Pi_\eta(\lambda_i),\qquad c_i=\Pi_\eta(-\lambda_i).
\]

压缩函数：
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

材料功：
\[
W_{\rm src}=\rho x_{cr}\int_0^{10}T_{\rm src}(r)\,dr,\qquad
\int_0^{10}T_{\rm src}(r)\,dr\approx6.349875.
\]

R10：
\[
h=\frac15\left[\frac{W_{\rm src}}{x_{cr}}-\frac{\rho}{10}-\frac92u_r\right],\qquad u_r=0.03.
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
\]
\[
U_i=\kappa\lambda_i-C_i+\kappa c_i+\rho T_i-\kappa t_i.
\]

二维主应力：
\[
s_+=U_+-a_{cc}C_+^2C_-+C_+T_- -\rho a_tT_+T_-^8,
\]
\[
s_-=U_--a_{cc}C_-^2C_+ +C_-T_+ -\rho a_tT_-T_+^8,
\]
其中 \(a_{cc}=0.1072329249\)，\(a_t=1-2^{-1/8}\)。谱返回后 \(\boldsymbol\sigma=f_c\mathbf S\)。

# 2. N48 材料解析目标函数

唯一编译目标：
\[
F\in\{U,C,T,T^7\}.
\]

\[
\lambda_c=(\lambda_a+\lambda_b)/2,\qquad
\lambda_h=(\lambda_b-\lambda_a)/2,\qquad
\xi=(\lambda-\lambda_c)/\lambda_h.
\]

\[
F_{48}(\lambda)=\sum_{n=0}^{48}a_n^{(F)}\mathcal C_n(\xi).
\]

\[
\theta_j=\frac{(j+1/2)\pi}{49},\qquad
\lambda_j=\lambda_c+\lambda_h\cos\theta_j.
\]

\[
\boxed{a_n^{(F)}=\frac{2-\delta_{n0}}{49}\sum_{j=0}^{48}F(\lambda_j)\cos(n\theta_j)}
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
A_{n+1}=-2K_2B_n-A_{n-1},
\]
\[
B_{n+1}=2A_n+2K_1B_n-B_{n-1}.
\]

然后构造 \(\mathbf U,\mathbf C,\mathbf T,\mathbf T^{(7)}\)，以及
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

本三个板：
\[
b=\ell=1220\ {\rm mm},\qquad q_0=1/400.
\]

\[
X=\pi x/b,\qquad Y=\pi y/\ell,\qquad \zeta=2z/t_p,\qquad q=A/b.
\]

\[
C_m=\frac{\pi^2}{\varepsilon_0}\left(q_0q+\frac12q^2\right),
\]
\[
C_b=\frac{\pi^2}{2\varepsilon_0}\frac{t_p}{b}q.
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
\varepsilon_x=\varepsilon_0e_x,\quad\varepsilon_y=\varepsilon_0e_y,\quad\gamma_{xy}=\varepsilon_0g_{xy}.
\]

# 5. D15

\[
Q=\sum_{ijk}c_{ijk}\mathcal C_i(\sin X)\mathcal C_j(\sin Y)\mathcal C_k(\zeta).
\]

\[
M_n=\begin{cases}\pi,&n=0,\\2\sin(n\pi/2)/n,&n\ge1,\end{cases}\qquad
Z_k=\begin{cases}0,&k\ {\rm odd},\\2/(1-k^2),&k\ {\rm even}.\end{cases}
\]

\[
\mathscr D[Q]=\sum c_{ijk}M_iM_jZ_k.
\]

轴力：
\[
P_c=-\frac{f_cbt_p}{2\pi^2}\mathscr D[S_{yy}].
\]

功共轭：
\[
\mathbf e=\mathbf E/\varepsilon_0=(1+\nu)\mathbf X-\nu{\rm tr}(\mathbf X)\mathbf I,
\]
\[
Q_q=\mathbf S:\mathbf e_{,q}.
\]

\[
R_{q,c}=f_c\varepsilon_0J_\Omega\mathscr D[Q_q],\qquad J_\Omega=\frac{b\ell t_p}{2\pi^2}.
\]

# 6. 钢筋与联立

\[
E_s=200000\ {\rm MPa},\qquad \varepsilon_y=0.00265,\qquad f_y=530\ {\rm MPa}.
\]

只要最终连续钢筋场满足 \(|\varepsilon_s|<\varepsilon_y\)，使用 \(\sigma_s=E_s\varepsilon_s\)。

加载方向总钢筋轴力：
\[
P_s=\rho_{s,y}bt_pE_s\varepsilon_0\left(D-\frac{C_m}{4}\right).
\]

钢筋幅值广义残量按所有层与两个方向解析求和：
\[
R_{q,s}=\sum_{\alpha,\ell}\int_\Omega\sigma_{s,\alpha}^{(\ell)}\frac{\partial\varepsilon_{s,\alpha}^{(\ell)}}{\partial q}\,dA.
\]

总体系：
\[
P=P_c+P_s,\qquad R_q=R_{q,c}+R_{q,s}.
\]

极限点：
\[
\boxed{R_q(D,q)=0}
\]
\[
\boxed{L(D,q)=P_{,D}R_{q,q}-P_{,q}R_{q,D}=0.}
\]

# 7. 三板盲算输入（无理论答案、无试验荷载）

|Case|t/mm|fc/MPa|E0/MPa|eps0|nu|总配筋率|层数/位置|N48区间|
|---:|---:|---:|---:|---:|---:|---:|:---|:---|
|1|25.40|22.81|21730|0.00210|0.18|0.20%|1层，z=0|[-1.12,0.105]|
|14|32.26|16.82|17995|0.00187|0.18|0.75%|2层，z=±12.63 mm|[-1.17,0.105]|
|21|19.30|21.23|20321|0.00209|0.18|0.75%|1层，z=0|[-1.01,0.105]|

共同输入：
\[
b=\ell=1220\ {\rm mm},\quad q_0=1/400,
\]
\[
E_s=200000\ {\rm MPa},\quad\varepsilon_y=0.00265,\quad f_y=530\ {\rm MPa}.
\]

请独立生成 N48、独立组装二维 current-map、独立进行 D15 收缩并联立 \(R_q=L=0\)。本文件故意不提供三个板的最终 \(D,q,P_u\) 和试验荷载。
