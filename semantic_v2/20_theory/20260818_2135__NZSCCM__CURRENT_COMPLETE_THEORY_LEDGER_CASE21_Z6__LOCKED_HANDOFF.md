# NZ-SCCM 当前完整理论总账：Case21 + Z6

**时间戳：2026-08-18 21:35 +08:00**  
**定位：CURRENT CONSOLIDATION / CHAT-LENGTH HANDOFF / NO NEW THEORY BRANCH**  
**用途：在当前聊天长度再次接近上限前，把本轮已经恢复、修正、展开并核对的理论、公式、算例、边界和剩余事项一次性固化。**

> 本文件是“当前共享理论基线/交接总账”，不是对历史原始证据文件的删除或改写。历史 2026-08-17 的 execution / audit / REPRO 文件继续保留各自的证据身份；本文件负责把当前聊天中已经补齐的公式和后续修正集中到一个可继续工作的入口。

---

## 0. 当前最高层结论与执行边界

当前正式母链为：

```text
原始试件参数
-> 控制完整代表半波
-> Nguyen/von Karman 连续二阶应变场
-> 各材料 current material operator
-> 材料坐标真无限解析表示
-> 每个解析项的 2x2 Cayley-Hamilton 降幂
-> General-D15 精确空间矩
-> n -> infinity
-> P(D,q,alpha), Rq(D,q,alpha), Ralpha(D,q,alpha) 及同源一阶导数
-> 直接联立极限方程
-> (Du,qu,alphau)
-> Pu=P(Du,qu,alphau)
-> 试验/周思铭/Winter 仅后比较
```

正式空间计数锁定：

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
N_formal_material_points = 0
```

这里的“1 个 spatial subdomain”只表示**一个完整连续代表半波**，不是空间 cell。

正式理论继续禁止：

- 空间 Gauss/Simpson/自适应积分作为正式算子；
- 材料点网格、空间 cells、Chebyshev spatial collocation；
- 通过试验荷载、周思铭值或 Winter 值反标材料或选择非线性根；
- 把有限 prefix `N` 当成材料模型阶数；
- 把 raw-R10 连续数值 oracle 当成正式积分；
- 把逐 `D` 加载/延拓写成正式 `Pu` 生产算法。

当前纠正后的正式极限求解为：

\[
\boxed{
R_q(D,q,\alpha)=0,\qquad
R_\alpha(D,q,\alpha)=0,\qquad
\mathcal L(D,q,\alpha)=0
}
\]

其中

\[
\boxed{
\mathcal L=
\det\begin{bmatrix}
P_D&P_q&P_\alpha\\
R_{q,D}&R_{q,q}&R_{q,\alpha}\\
R_{\alpha,D}&R_{\alpha,q}&R_{\alpha,\alpha}
\end{bmatrix}.
}
\]

求得

\[
\boxed{(D_u,q_u,\alpha_u)}
\]

后，直接

\[
\boxed{P_u=P(D_u,q_u,\alpha_u).}
\]

所谓 Newton / trust-region / interval root isolation 如果出现，只是**三个全局代数未知量的求根后端**，不是空间离散、材料点迭代或加载历史。

逐 `D` continuation 只保留为：

\[
\boxed{\text{ROOT IDENTITY / CONNECTED-BRANCH AUDIT}}
\]

用于在多根时确认候选根属于原点连续物理分支，不能取代直接三元极限方程。

---

# 1. 坐标、符号与语义约定

结构坐标：

\[
0\le x\le b,\qquad 0\le y\le \ell.
\]

轴压方向为 `y`，横向为 `x`，厚度方向为 `z`。

标准化面内坐标：

\[
X=\frac{\pi x}{b},\qquad Y=\frac{\pi y}{\ell},\qquad k=\frac b\ell.
\]

记

\[
s_X=\sin X,\quad c_X=\cos X,\quad
s_Y=\sin Y,\quad c_Y=\cos Y,
\]

\[
\boxed{H_s=s_Xs_Y.}
\]

这里使用 `H_s` 表示形函数乘积，避免与正交各向异性板刚度 `H` 混淆。

物理应变向量：

\[
\boldsymbol\varepsilon=
\begin{bmatrix}
\varepsilon_x&\varepsilon_y&\gamma_{xy}
\end{bmatrix}^{T}.
\]

物理应力向量：

\[
\boldsymbol\sigma=
\begin{bmatrix}
\sigma_x&\sigma_y&\tau_{xy}
\end{bmatrix}^{T}.
\]

正式全局广义变量：

\[
\boxed{(D,q,\alpha)}.
\]

其中：

- `D`：平均轴向压缩状态；
- `q=A/b`：新增局部挠曲幅值；
- `alpha`：Airy 膜内重分布广义变量。

历史报告量：

\[
\boxed{\lambda_A=\alpha/M}\qquad(M\ne0).
\]

`lambda_A` 不是原点处的正式工作坐标，因为在 `q=0` 时 `M=0`、`alpha=0`，从而 `lambda_A=0/0` 无定义。

轴向力定义：

\[
\boxed{
P=-\frac1\ell\int_V\sigma_y\,dV.
}
\]

---

# 2. 原始试件 -> 控制完整代表半波

整板长度为 `a`，宽度为 `b`。对 SSSS 正交各向异性候选模态：

\[
w_j=W_j\sin\frac{\pi x}{b}\sin\frac{j\pi y}{a}.
\]

定义：

\[
\alpha_x=\frac\pi b,\qquad
\beta_j=\frac{j\pi}{a}.
\]

候选弹性屈曲膜力：

\[
\boxed{
N_{cr,j}=
\frac{D_x\alpha_x^4+2H\alpha_x^2\beta_j^2+D_y\beta_j^4}{\beta_j^2}.
}
\]

等价地：

\[
\boxed{
N_{cr,j}=\pi^2\left[
\frac{D_xa^2}{j^2b^4}
+\frac{2H}{b^2}
+\frac{D_yj^2}{a^2}
\right].
}
\]

整板控制半波数：

\[
\boxed{m_*=\arg\min_{j\in\mathbb N^+}N_{cr,j}.}
\]

代表半波长度：

\[
\boxed{\ell=\frac a{m_*}.}
\]

连续最优近似：

\[
\boxed{
j_0=\frac ab\left(\frac{D_x}{D_y}\right)^{1/4},
\qquad
\ell_0=b\left(\frac{D_y}{D_x}\right)^{1/4}.
}
\]

初始缺陷：

\[
\boxed{q_0=\frac{A_0}{b}.}
\]

整个非线性理论只对**一个完整代表半波**计算。重复半波不建立独立材料点，也不把轴力乘 `m_*`：

\[
\boxed{P_{\rm whole}=P_{\rm halfwave}.}
\]

残量若按整板重复，只整体乘共同正因子，不改变零点。

## 2.1 Case21

\[
a=b=1220\ {\rm mm},\qquad m_*=1,
\]

\[
\boxed{\ell=1220\ {\rm mm},\quad k=1.}
\]

\[
A_0=3.05\ {\rm mm},\qquad q_0=0.0025.
\]

## 2.2 Z6

真实整壁：

\[
a=24000\ {\rm mm},\qquad b=12000\ {\rm mm}.
\]

冻结弹性刚度：

\[
D_x=11\,461\,031\,000\ {\rm Nmm},
\]

\[
D_y=11\,986\,113\,713.333336\ {\rm Nmm},
\]

\[
H=12\,160\,676\,566.638557\ {\rm Nmm}.
\]

连续最优：

\[
j_0=1.9777268929582714.
\]

候选：

\[
P_{cr,1}=60.17333767361622\ {\rm MN},
\]
\[
P_{cr,2}=39.288014715027835\ {\rm MN},
\]
\[
P_{cr,3}=46.3738994131663\ {\rm MN},
\]
\[
P_{cr,4}=61.79282475438204\ {\rm MN}.
\]

因此：

\[
\boxed{m_*=2,\qquad \ell=12000\ {\rm mm},\qquad k=1.}
\]

初始缺陷：

\[
A_0=48\ {\rm mm},\qquad \boxed{q_0=0.004}.
\]

## 2.3 当前前端尚待补齐的通用接口

对 Case21/Z6，`D_x,D_y,H` 已有历史冻结值/半波结论，所以不影响已释放结果；但对于**任意新试件从原始材料几何参数开始**，仍需把

\[
\boxed{\text{原始 }E,t,\nu,\rho_s,\text{钢壳/web 几何}\to D_x,D_y,H}
\]

逐式写成统一前端账本。这是当前 `DOCUMENTATION GAP A`，不是 Case21/Z6 结果漏洞。

---

# 3. Nguyen / von Karman 连续二阶运动学

初始挠曲：

\[
\boxed{w_0=bq_0H_s.}
\]

新增挠曲：

\[
\boxed{\Delta w=bqH_s.}
\]

总挠曲：

\[
\boxed{w=b(q_0+q)H_s.}
\]

几何膜尺度：

\[
\boxed{
M(q)=\frac{\pi^2}{\varepsilon_0}
\left(q_0q+\frac12q^2\right).
}
\]

\[
\boxed{M_q=\frac{\pi^2}{\varepsilon_0}(q_0+q),\qquad M_{qq}=\frac{\pi^2}{\varepsilon_0}.}
\]

定义：

\[
F_x=s_Y^2-s_X^2s_Y^2,
\]

\[
F_y=s_X^2-s_X^2s_Y^2.
\]

增量几何膜应变：

\[
\boxed{\Delta\varepsilon_x^g=\varepsilon_0MF_x,}
\]

\[
\boxed{\Delta\varepsilon_y^g=\varepsilon_0k^2MF_y,}
\]

\[
\boxed{\Delta\gamma_{xy}^g=2\varepsilon_0kMH_sc_Xc_Y.}
\]

对于参考厚度 `t_r`，定义：

\[
\boxed{B=\frac{\pi^2t_rq}{2\varepsilon_0b},\qquad B_q=\frac{\pi^2t_r}{2\varepsilon_0b}.}
\]

厚度标准坐标：

\[
\zeta=\frac{2z}{t_r},\qquad -1\le\zeta\le1.
\]

弯曲应变：

\[
\varepsilon_x^b=\varepsilon_0BH_s\zeta,
\]

\[
\varepsilon_y^b=\varepsilon_0k^2BH_s\zeta,
\]

\[
\gamma_{xy}^b=-2\varepsilon_0kB\zeta c_Xc_Y.
\]

均匀轴压场：

\[
\boxed{e_x^D=\nu D,\qquad e_y^D=-D,\qquad \gamma^D=0.}
\]

## 3.1 矩形 Airy 膜内重分布场

定义：

\[
A_x=b_0+b_{20}\cos2X+b_{22}\cos2X\cos2Y,
\]

\[
A_y=c_{02}\cos2Y+c_{22}\cos2X\cos2Y,
\]

\[
A_\gamma=d_{22}\sin2X\sin2Y,
\]

其中：

\[
b_0=-\frac{1+\nu k^2}{4},
\]

\[
b_{20}=\frac{\nu k^2-1}{4},\qquad b_{22}=\frac14,
\]

\[
c_{02}=\frac{\nu-k^2}{4},\qquad c_{22}=\frac{k^2}{4},
\]

\[
d_{22}=-\frac k2.
\]

等价 sine-square 形式：

\[
\boxed{
A_x=-\frac14-\frac{\nu k^2}{2}s_X^2-\frac12s_Y^2+s_X^2s_Y^2,
}
\]

\[
\boxed{
A_y=\frac\nu4-\frac{k^2}{2}s_X^2-\frac\nu2s_Y^2+k^2s_X^2s_Y^2,
}
\]

\[
\boxed{A_\gamma=-2kH_sc_Xc_Y.}
\]

Airy 应变：

\[
\varepsilon_x^A=\varepsilon_0\alpha A_x,
\]

\[
\varepsilon_y^A=\varepsilon_0\alpha A_y,
\]

\[
\gamma_{xy}^A=\varepsilon_0\alpha A_\gamma.
\]

## 3.2 总归一化应变

\[
\boxed{
e_x=\nu D+MF_x+\alpha A_x+BH_s\zeta,
}
\]

\[
\boxed{
e_y=-D+k^2MF_y+\alpha A_y+k^2BH_s\zeta,
}
\]

\[
\boxed{
\gamma=2kc_Xc_Y\left[(M-\alpha)H_s-B\zeta\right].
}
\]

实际：

\[
\boxed{
\varepsilon_x=\varepsilon_0e_x,\qquad
\varepsilon_y=\varepsilon_0e_y,\qquad
\gamma_{xy}=\varepsilon_0\gamma.
}
\]

## 3.3 一阶运动学导数

\[
\boxed{
\varepsilon_{x,D}=\varepsilon_0\nu,
\quad
\varepsilon_{y,D}=-\varepsilon_0,
\quad
\gamma_{xy,D}=0.
}
\]

固定 `alpha`：

\[
\boxed{
\varepsilon_{x,q}=\varepsilon_0(M_qF_x+B_qH_s\zeta),
}
\]

\[
\boxed{
\varepsilon_{y,q}=\varepsilon_0k^2(M_qF_y+B_qH_s\zeta),
}
\]

\[
\boxed{
\gamma_{xy,q}=2\varepsilon_0kc_Xc_Y(M_qH_s-B_q\zeta).
}
\]

\[
\boxed{
\varepsilon_{x,\alpha}=\varepsilon_0A_x,
\quad
\varepsilon_{y,\alpha}=\varepsilon_0A_y,
\quad
\gamma_{xy,\alpha}=-2\varepsilon_0kH_sc_Xc_Y.
}
\]

## 3.4 二阶运动学导数

\[
\boxed{
\varepsilon_{x,qq}=\varepsilon_0M_{qq}F_x,
}
\]

\[
\boxed{
\varepsilon_{y,qq}=\varepsilon_0k^2M_{qq}F_y,
}
\]

\[
\boxed{
\gamma_{xy,qq}=2\varepsilon_0kM_{qq}H_sc_Xc_Y.
}
\]

其余二阶运动学导数为零。

---

# 4. 普通混凝土 R10 当前状态材料映射

## 4.1 从物理应变到等效材料矩阵

物理面内应变张量：

\[
\mathbf E^{phys}=\begin{bmatrix}
\varepsilon_x&\gamma_{xy}/2\\
\gamma_{xy}/2&\varepsilon_y
\end{bmatrix}.
\]

定义归一化等效材料矩阵：

\[
\boxed{
E_{11}=\frac{e_x+\nu e_y}{1-\nu^2},
}
\]

\[
\boxed{
E_{22}=\frac{\nu e_x+e_y}{1-\nu^2},
}
\]

\[
\boxed{
E_{12}=\frac{\gamma}{2(1+\nu)}.
}
\]

\[
\boxed{
\mathbf E_u=\begin{bmatrix}E_{11}&E_{12}\\E_{12}&E_{22}\end{bmatrix}.
}
\]

在 `q=alpha=0`：

\[
\boxed{\mathbf E_u=\operatorname{diag}(0,-D).}
\]

进一步显式：

\[
\boxed{
E_{11}=\frac{
M(F_x+\nu k^2F_y)+\alpha(A_x+\nu A_y)+B(1+\nu k^2)H_s\zeta
}{1-\nu^2},
}
\]

\[
\boxed{
E_{22}=-D+\frac{
M(\nu F_x+k^2F_y)+\alpha(\nu A_x+A_y)+B(\nu+k^2)H_s\zeta
}{1-\nu^2},
}
\]

\[
\boxed{
E_{12}=\frac{k c_Xc_Y[(M-\alpha)H_s-B\zeta]}{1+\nu}.
}
\]

## 4.2 主材料坐标

\[
\mu_E=\frac{E_{11}+E_{22}}2,
\]

\[
d_E=\frac{E_{11}-E_{22}}2,
\]

\[
r_E=\sqrt{d_E^2+E_{12}^2},
\]

\[
\boxed{\lambda_1=\mu_E+r_E,\qquad \lambda_2=\mu_E-r_E.}
\]

## 4.3 冻结材料常数

\[
\kappa=\frac{E_0\varepsilon_0}{f_c},
\]

\[
\rho=0.1,
\]

\[
x_{cr}=\frac\rho\kappa,
\]

\[
\eta=\frac{x_{cr}}{20}.
\]

当前冻结：

\[
\boxed{\kappa=2.0005129533678754,}
\]

\[
\boxed{x_{cr}=0.0499871794539743,}
\]

\[
\boxed{\eta=0.0024993589726987125,}
\]

\[
\boxed{H_R=0.09799750427197301,\qquad U_R=0.03,}
\]

\[
\boxed{a_{cc}=0.1072329249362415,}
\]

\[
\boxed{a_t=1-2^{-1/8}=0.0829959567953288.}
\]

## 4.4 平滑正投影器

\[
\boxed{
\Pi_\eta(z)=
\frac{z^2\big(\sqrt{z^2+\eta^2}+z\big)}{2(z^2+\eta^2)}.
}
\]

对主材料坐标：

\[
\boxed{c_i=\Pi_\eta(-\lambda_i),\qquad t_i=\Pi_\eta(\lambda_i).}
\]

## 4.5 压缩标量

\[
\boxed{
C_i=\frac{\kappa c_i}{1+(\kappa-2)c_i+c_i^2}.
}
\]

## 4.6 拉伸标量

定义：

\[
a_R=x_{cr}=\frac\rho\kappa,
\qquad r=\frac{t}{a_R}.
\]

第一段 `0<=r<=1`：

\[
\boxed{
u_R(t)=
\rho r+(10H_R-6\rho)r^3+(8\rho-15H_R)r^4+(6H_R-3\rho)r^5.
}
\]

数值：

\[
u_R=0.1r+0.379975042719730r^3-0.669962564079595r^4+0.287985025631838r^5.
\]

第二段 `1<r<=10`，令

\[
s=\frac{r-1}{9},
\]

\[
\boxed{
u_R=H_R+(U_R-H_R)(10s^3-15s^4+6s^5).
}
\]

第三段 `r>10`：

\[
\boxed{u_R=U_R=0.03.}
\]

定义：

\[
\boxed{T_i=\frac{u_R(t_i)}\rho.}
\]

以及：

\[
\boxed{
U_i=\kappa\lambda_i-C_i+\kappa c_i+u_R(t_i)-\kappa t_i.
}
\]

## 4.7 主应力

\[
\boxed{
s_1=U_1-a_{cc}C_1^2C_2+C_1T_2-\rho a_tT_1T_2^8,
}
\]

\[
\boxed{
s_2=U_2-a_{cc}C_2^2C_1+C_2T_1-\rho a_tT_2T_1^8.
}
\]

## 4.8 谱返回到物理坐标

令

\[
\Delta\lambda=\lambda_1-\lambda_2.
\]

\[
P_1=\frac{E_u-\lambda_2I}{\Delta\lambda},\qquad P_2=I-P_1.
\]

对不重复主值：

\[
\boxed{
S_{xx}=s_2+\frac{s_1-s_2}{\Delta\lambda}(E_{11}-\lambda_2),
}
\]

\[
\boxed{
S_{yy}=s_2+\frac{s_1-s_2}{\Delta\lambda}(E_{22}-\lambda_2),
}
\]

\[
\boxed{
S_{xy}=\frac{s_1-s_2}{\Delta\lambda}E_{12}.
}
\]

实际应力：

\[
\boxed{
\sigma_x=f_cS_{xx},\quad
\sigma_y=f_cS_{yy},\quad
\tau_{xy}=f_cS_{xy}.
}
\]

重复主值用连续极限：

\[
\boxed{S=sI\qquad(s_1=s_2=s).}
\]

## 4.9 `H_R` 的来源平滑能量账本

这里只用于复现冻结 `H_R`，不是每块试件运行时再标定。

定义：

\[
r=t/x_{cr},\qquad m_t=-7/90,\qquad \eta_r=0.05.
\]

\[
H_F(r,r_0)=\frac12[(r-r_0)+\sqrt{(r-r_0)^2+\eta_r^2}]
-\frac12[-r_0+\sqrt{r_0^2+\eta_r^2}].
\]

\[
T_{src}(r)=r+(m_t-1)H_F(r,1)-m_tH_F(r,10).
\]

\[
W_{src}=\rho x_{cr}\int_0^{10}T_{src}(r)\,dr
=0.0317412351812499.
\]

\[
\boxed{
H_R=\frac15\left[
\frac{W_{src}}{x_{cr}}-\frac\rho{10}-\frac92U_R
\right]
=0.097997504271973.
}
\]

## 4.10 同源局部材料导数

令

\[
R_\eta(z)=\sqrt{z^2+\eta^2}.
\]

当前使用的投影导数写法：

\[
\Pi_\eta'(z)=
\frac z{R_\eta}
-\frac{z^3}{2R_\eta^3}
+\frac{3z^2}{2R_\eta^2}
-\frac{z^4}{R_\eta^4}.
\]

于是：

\[
c_i'=-\Pi_\eta'(-\lambda_i),\qquad t_i'=\Pi_\eta'(\lambda_i).
\]

\[
\boxed{
\frac{dC}{dc}=\frac{\kappa(1-c^2)}{[1+(\kappa-2)c+c^2]^2}.
}
\]

\[
C_i'=\left.\frac{dC}{dc}\right|_{c_i}c_i'.
\]

第一拉伸段：

\[
u_R'(t)=\frac1{x_{cr}}
\left[\rho+3A_3r^2+4A_4r^3+5A_5r^4\right].
\]

第二段：

\[
u_R'(t)=\frac{U_R-H_R}{9x_{cr}}
(30s^2-60s^3+30s^4).
\]

第三段：

\[
u_R'(t)=0.
\]

\[
T_i'=\frac1\rho u_R'(t_i)t_i'.
\]

\[
U_i'=\kappa-C_i'+\kappa c_i'+u_R'(t_i)t_i'-\kappa t_i'.
\]

主应力偏导：

\[
s_{1,1}=U_1'-2a_{cc}C_1C_1'C_2+C_1'T_2-\rho a_tT_1'T_2^8,
\]

\[
s_{1,2}=-a_{cc}C_1^2C_2'+C_1T_2'-8\rho a_tT_1T_2^7T_2',
\]

\[
s_{2,2}=U_2'-2a_{cc}C_2C_2'C_1+C_2'T_1-\rho a_tT_2'T_1^8,
\]

\[
s_{2,1}=-a_{cc}C_2^2C_1'+C_2T_1'-8\rho a_tT_2T_1^7T_1'.
\]

物理应变增量到材料矩阵：

\[
dE_{11}=\frac{d\varepsilon_x+\nu d\varepsilon_y}{(1-\nu^2)\varepsilon_0},
\]

\[
dE_{22}=\frac{\nu d\varepsilon_x+d\varepsilon_y}{(1-\nu^2)\varepsilon_0},
\]

\[
dE_{12}=\frac{d\gamma_{xy}}{2(1+\nu)\varepsilon_0}.
\]

通过 `d lambda_i -> ds_i -> dP_i -> dS` 得到与同一 R10 映射一致的切线；不允许另拟合切线。

---

# 5. R10 真无限材料解析编译

## 5.1 材料谱区间，不是空间分区

对当前需要覆盖的材料主坐标：

\[
\boxed{L\le\lambda\le U.}
\]

定义：

\[
\boxed{c_0=\frac{L+U}{2},\qquad h=\frac{U-L}{2}.}
\]

\[
\boxed{\xi=\frac{\lambda-c_0}{h}\in[-1,1].}
\]

\[
\lambda=c_0+h\xi=c_0+h\cos\theta.
\]

Case21 历史材料区间：

\[
\boxed{[L,U]=[-1.15,0.12],\quad c_0=-0.515,\quad h=0.635.}
\]

Z6 Stage-I 区间：

\[
\boxed{[L,U]=[-1.75,1.45],\quad c_0=-0.15,\quad h=1.60.}
\]

这些区间都是**材料坐标包络**，不增加空间 subdomain。

## 5.2 Chebyshev 约定

\[
T_n(\cos\theta)=\cos(n\theta).
\]

采用：

\[
\boxed{
F(\lambda)=a_0^{(F)}+\sum_{n=1}^{\infty}a_n^{(F)}T_n(\xi).
}
\]

系数唯一定义：

\[
\boxed{
a_0^{(F)}=\frac1\pi\int_0^\pi F(c_0+h\cos\theta)\,d\theta,
}
\]

\[
\boxed{
a_n^{(F)}=\frac2\pi\int_0^\pi F(c_0+h\cos\theta)\cos(n\theta)\,d\theta,
\quad n\ge1.
}
\]

这里的 `theta` 是一维材料坐标，不是结构空间积分坐标。

有限 prefix：

\[
F^{[N]}=a_0+\sum_{n=1}^Na_nT_n.
\]

正式对象：

\[
\boxed{F=\lim_{N\to\infty}F^{[N]}.}
\]

`N48/N64/N96/...` 只是同一解析流的部分和检查点，不是材料模型度数。

## 5.3 两个通用核

\[
Q_\eta(\lambda)=\lambda^2+\eta^2.
\]

\[
\boxed{f(\lambda)=Q_\eta^{-1/2},\qquad r(\lambda)=Q_\eta^{-1}.}
\]

投影器精确代数：

\[
\boxed{
t(\lambda)=\frac{\lambda^2}{2}f(\lambda)+\frac{\lambda^3}{2}r(\lambda),
}
\]

\[
\boxed{
c(\lambda)=\frac{\lambda^2}{2}f(\lambda)-\frac{\lambda^3}{2}r(\lambda).
}
\]

## 5.4 平方根核五项递推

定义：

\[
\boxed{A_{rec}=c_0^2+\eta^2+\frac{h^2}{2}.}
\]

若

\[
f=\sum a_nT_n,
\]

则：

\[
\boxed{
\frac{h^2}{4}(n-1)a_{n-2}
+hc_0\left(n-\frac12\right)a_{n-1}
+A_{rec}na_n
+hc_0\left(n+\frac12\right)a_{n+1}
+\frac{h^2}{4}(n+1)a_{n+2}=0.
}
\]

递推本身是精确传播/审计恒等式；系数序列的唯一归一化仍由上述 Chebyshev 系数定义给出，不能把递推独立当成无 seed 的唯一序列定义。

Z6：

\[
\frac{h^2}{4}=0.64,\qquad hc_0=-0.24,
\]

\[
\boxed{A_{rec}=1.30250624679527.}
\]

所以：

\[
0.64(n-1)a_{n-2}
-0.24\left(n-\frac12\right)a_{n-1}
+1.30250624679527\,na_n
-0.24\left(n+\frac12\right)a_{n+1}
+0.64(n+1)a_{n+2}=0.
\]

## 5.5 有理核有限带递推

若

\[
r=\sum b_nT_n,
\]

由于

\[
(\lambda^2+\eta^2)r=1,
\]

远离低阶 forcing：

\[
\boxed{
\frac{h^2}{4}(b_{n-2}+b_{n+2})
+hc_0(b_{n-1}+b_{n+1})
+A_{rec}b_n=0.
}
\]

Z6：

\[
0.64(b_{n-2}+b_{n+2})
-0.24(b_{n-1}+b_{n+1})
+1.30250624679527b_n=0.
\]

## 5.6 乘以 `lambda` 的系数算子

若

\[
G=\sum_{n=0}^\infty g_nT_n(\xi),
\]

定义材料乘法算子 `\mathfrak L_\lambda`，使 `lambda G` 的系数为 `(\mathfrak L_\lambda g)_n`：

\[
\boxed{(\mathfrak L_\lambda g)_0=c_0g_0+\frac h2g_1,}
\]

\[
\boxed{(\mathfrak L_\lambda g)_1=c_0g_1+h\left(g_0+\frac12g_2\right),}
\]

\[
\boxed{(\mathfrak L_\lambda g)_n=c_0g_n+\frac h2(g_{n-1}+g_{n+1}),\quad n\ge2.}
\]

因此：

\[
\boxed{
\mathbf a^{(t)}=\frac12\mathfrak L_\lambda^2\mathbf a^{(f)}+\frac12\mathfrak L_\lambda^3\mathbf a^{(r)},
}
\]

\[
\boxed{
\mathbf a^{(c)}=\frac12\mathfrak L_\lambda^2\mathbf a^{(f)}-\frac12\mathfrak L_\lambda^3\mathbf a^{(r)}.
}
\]

## 5.7 Chebyshev Cauchy product

\[
\boxed{T_mT_n=\frac12(T_{m+n}+T_{|m-n|}).}
\]

若

\[
F=\sum f_mT_m,\qquad G=\sum g_nT_n,
\]

则

\[
FG=\sum h_kT_k,
\]

\[
\boxed{
h_k=\frac12\sum_{m=0}^{\infty}\sum_{n=0}^{\infty}
f_mg_n\left[\delta_{k,m+n}+\delta_{k,|m-n|}\right].
}
\]

记作：

\[
\boxed{\mathbf h=\mathbf f\star\mathbf g.}
\]

## 5.8 压缩函数的全局几何级数

定义：

\[
s_c=\frac{c}{(1+c)^2}.
\]

有：

\[
1+(\kappa-2)c+c^2=(1+c)^2[1-(4-\kappa)s_c].
\]

因此：

\[
\boxed{
C=\kappa\sum_{m=1}^{\infty}(4-\kappa)^{m-1}s_c^m.
}
\]

由于对 `c>=0`：

\[
0\le s_c\le\frac14,
\]

且当前

\[
\boxed{\frac{4-\kappa}{4}=0.499871761658031<0.5,}
\]

所以该几何级数全局绝对收敛。

## 5.9 拉伸结点与全局 C2 拼接

材料分支结点满足：

\[
t(\lambda_1)=x_{cr},
\]

\[
t(\lambda_{10})=10x_{cr}.
\]

Z6 Stage-I：

\[
\boxed{\lambda_1=0.0500805176491376,}
\]

\[
\boxed{\lambda_{10}=0.499881166745393.}
\]

定义材料阶跃：

\[
\mathcal H_k(\lambda)=0\ (\lambda<\lambda_k),\qquad
\mathcal H_k(\lambda)=1\ (\lambda\ge\lambda_k).
\]

全局拉伸函数：

\[
\boxed{
T(\lambda)=T_L+\mathcal H_1(T_M-T_L)+\mathcal H_{10}(T_H-T_M).
}
\]

\[
T_H=U_R/\rho=0.3.
\]

若

\[
\xi_k=\frac{\lambda_k-c_0}{h},\qquad \theta_k=\arccos\xi_k,
\]

则阶跃系数：

\[
\boxed{h_0^{(k)}=\frac{\theta_k}{\pi},}
\]

\[
\boxed{h_n^{(k)}=\frac{2\sin(n\theta_k)}{\pi n},\qquad n\ge1.}
\]

Z6：

\[
\xi_1=0.125050323530711,\qquad \theta_1=1.44541777411337,
\]

\[
\xi_{10}=0.406175729215871,\qquad \theta_{10}=1.15253121911414.
\]

两个分支差分别具有三次接触：

\[
T_M-T_L\propto(r_t-1)^3,
\]

\[
T_H-T_M\propto(r_t-10)^3.
\]

所以：

\[
\boxed{T\in C^2,\qquad a_n^{(T)}=O(n^{-4}).}
\]

Stage-I 尾部主项：

\[
\boxed{
a_n=\frac{2}{\pi n^4}\left[
\Delta g_1^{(3)}\cos(n\theta_1)+
\Delta g_{10}^{(3)}\cos(n\theta_{10})
\right]+\cdots.
}
\]

Z6：

\[
\Delta g_1^{(3)}=-1\,122\,509.44854571,
\]

\[
\Delta g_{10}^{(3)}=1400.46250338021.
\]

## 5.10 `U` 与 `T^7`

\[
\boxed{
U(\lambda)=\kappa\lambda-C(\lambda)+\kappa c(\lambda)+\rho T(\lambda)-\kappa t(\lambda).
}
\]

因此系数：

\[
\boxed{
\mathbf a^{(U)}=\kappa\mathbf a^{(\lambda)}-\mathbf a^{(C)}+\kappa\mathbf a^{(c)}+\rho\mathbf a^{(T)}-\kappa\mathbf a^{(t)}.
}
\]

\[
\boxed{T^7(\lambda)=[T(\lambda)]^7,}
\]

\[
\boxed{
\mathbf a^{(T^7)}=
\underbrace{\mathbf a^{(T)}\star\cdots\star\mathbf a^{(T)}}_{7\text{ 次}}.
}
\]

正式四通道：

\[
\boxed{U,\quad C,\quad T,\quad T^7.}
\]

---

# 6. 二维 Cayley-Hamilton 降幂

定义：

\[
\boxed{
Y=\frac{E_u-c_0I}{h}.
}
\]

\[
Y_{11}=\frac{E_{11}-c_0}{h},\quad
Y_{22}=\frac{E_{22}-c_0}{h},\quad
Y_{12}=\frac{E_{12}}h.
\]

不变量：

\[
\boxed{\tau_Y=\operatorname{tr}Y=Y_{11}+Y_{22},}
\]

\[
\boxed{\delta_Y=\det Y=Y_{11}Y_{22}-Y_{12}^2.}
\]

二维 CH：

\[
\boxed{Y^2=\tau_YY-\delta_YI.}
\]

定义：

\[
\boxed{T_n(Y)=p_nI+r_nY.}
\]

初值：

\[
p_0=1,\ r_0=0,\qquad p_1=0,\ r_1=1.
\]

递推：

\[
\boxed{p_{n+1}=-2\delta_Yr_n-p_{n-1},}
\]

\[
\boxed{r_{n+1}=2p_n+2\tau_Yr_n-r_{n-1}.}
\]

低阶：

\[
T_2(Y)=(-1-2\delta_Y)I+2\tau_YY,
\]

\[
T_3(Y)=-4\tau_Y\delta_YI+(4\tau_Y^2-4\delta_Y-3)Y.
\]

若：

\[
F(\lambda)=\sum f_nT_n(\widehat\lambda),
\]

则：

\[
\boxed{F(E_u)=A_FI+B_FY,}
\]

\[
A_F=\sum f_np_n,\qquad B_F=\sum f_nr_n.
\]

## 6.1 pair 代数

记：

\[
[A,B]\equiv AI+BY.
\]

乘法：

\[
\boxed{
[A,B]\odot[C,D]=
[AC-BD\delta_Y,\ AD+BC+BD\tau_Y].
}
\]

行列式：

\[
\boxed{\det(AI+BY)=A^2+AB\tau_Y+B^2\delta_Y.}
\]

伴随：

\[
\boxed{\operatorname{adj}(AI+BY)=(A+B\tau_Y)I-BY.}
\]

## 6.2 R10 矩阵恒等式

这里 `C,T,U,T^7` 是相应标量谱函数的 `2x2` 矩阵提升，不是单个 `C_i,T_i,U_i`。

\[
\boxed{
S=U-a_{cc}\det(C)C+C\operatorname{adj}(T)-\rho a_t\det(T)\operatorname{adj}(T^7).
}
\]

其中 `T^7` 是矩阵 `T` 的七次幂，其主值为 `T_1^7,T_2^7`，从而

\[
\det(T)\operatorname{adj}(T^7)
\]

的两个主值正是：

\[
T_1T_2^8,\qquad T_2T_1^8.
\]

若：

\[
C=[A_C,B_C],\quad T=[A_T,B_T],\quad U=[A_U,B_U],\quad T^7=[A_{T7},B_{T7}],
\]

则：

\[
d_C=A_C^2+A_CB_C\tau_Y+B_C^2\delta_Y,
\]

\[
d_T=A_T^2+A_TB_T\tau_Y+B_T^2\delta_Y.
\]

\[
A_{CT}=A_C(A_T+B_T\tau_Y)+B_CB_T\delta_Y,
\]

\[
\boxed{B_{CT}=A_TB_C-A_CB_T.}
\]

最终：

\[
\boxed{
A_S=A_U-a_{cc}d_CA_C+A_{CT}-\rho a_td_T(A_{T7}+B_{T7}\tau_Y),
}
\]

\[
\boxed{
B_S=B_U-a_{cc}d_CB_C+B_{CT}+\rho a_td_TB_{T7}.
}
\]

\[
\boxed{S=A_SI+B_SY.}
\]

三个归一化应力分量：

\[
\boxed{S_{xx}=A_S+B_SY_{11},}
\]

\[
\boxed{S_{yy}=A_S+B_SY_{22},}
\]

\[
\boxed{S_{xy}=B_SY_{12}.}
\]

## 6.3 CH 多项式系数通项递推

展开：

\[
p_n=\sum_{a,b\ge0}P_n[a,b]\tau_Y^a\delta_Y^b,
\]

\[
r_n=\sum_{a,b\ge0}Q_n[a,b]\tau_Y^a\delta_Y^b.
\]

则：

\[
\boxed{
P_{n+1}[a,b]=-2Q_n[a,b-1]-P_{n-1}[a,b],
}
\]

\[
\boxed{
Q_{n+1}[a,b]=2P_n[a,b]+2Q_n[a-1,b]-Q_{n-1}[a,b].
}
\]

约定：

\[
Q_n[a,-1]=0,\qquad Q_n[-1,b]=0.
\]

初值：

\[
\boxed{P_0[0,0]=1,\quad Q_1[0,0]=1,}
\]

其余初始系数为零。

---

# 7. General-D15 精确空间矩

固定 `n` 后，CH 项始终是有限三角—厚度多项式，可以写成有限和：

\[
\sum C_{p,r,u,v,k}\sin^pX\cos^rX\sin^uY\cos^vY\zeta^k.
\]

定义：

\[
\boxed{
\mathscr D_{15}[\sin^pX\cos^rX\sin^uY\cos^vY\zeta^k]
=I_{pr}I_{uv}Z_k.
}
\]

\[
I_{pr}=\int_0^\pi\sin^pX\cos^rX\,dX.
\]

若 `r` 为奇数：

\[
\boxed{I_{pr}=0.}
\]

若 `r` 为偶数：

\[
\boxed{
I_{pr}=B\left(\frac{p+1}{2},\frac{r+1}{2}\right).
}
\]

`Y` 方向同理。

厚度：

\[
\boxed{Z_k=0\quad(k\text{ 奇}),}
\]

\[
\boxed{Z_k=\frac2{k+1}\quad(k\text{ 偶}).}
\]

示例：

\[
C\sin^4X\cos^2X\sin^6Y\zeta^2
\]

得到：

\[
\boxed{
\mathscr D_{15}=C\frac{5\pi^2}{384}.
}
\]

## 7.1 Stage-II 目标通式

给定结构权矩阵 `W`：

\[
\boxed{
A_{ab}^{(W)}=D15[(W:I)\tau_Y^a\delta_Y^b],
}
\]

\[
\boxed{
B_{ab}^{(W)}=D15[(W:Y)\tau_Y^a\delta_Y^b].
}
\]

第 `n` 项：

\[
\boxed{
J_n^{(W)}=\sum_{a,b}P_n[a,b]A_{ab}^{(W)}+\sum_{a,b}Q_n[a,b]B_{ab}^{(W)}.
}
\]

材料函数最终目标：

\[
\boxed{
J_F^{(W)}=\sum_{n=0}^{\infty}f_nJ_n^{(W)}.
}
\]

所有 `a,b,n` 求和都是解析级数/代数索引，不是空间网格。

## 7.2 物理体积变换

对于核心厚度 `t`：

\[
\boxed{
dV=\frac{b\ell t}{2\pi^2}\,dX\,dY\,d\zeta.
}
\]

混凝土轴力：

\[
\boxed{
P_c=-\frac{f_cbt}{2\pi^2}D15[S_{yy}].
}
\]

混凝土 `q` 残量：

\[
\boxed{
R_q^c=
\frac{f_c\varepsilon_0b\ell t}{2\pi^2}
D15\Big[
S_{xx}(M_qF_x+B_qH_s\zeta)
+S_{yy}k^2(M_qF_y+B_qH_s\zeta)
+S_{xy}\,2kc_Xc_Y(M_qH_s-B_q\zeta)
\Big].
}
\]

混凝土 Airy 残量：

\[
\boxed{
R_\alpha^c=
\frac{f_c\varepsilon_0b\ell t}{2\pi^2}
D15[S_{xx}A_x+S_{yy}A_y+S_{xy}A_\gamma].
}
\]

## 7.3 真无限极限

\[
\boxed{
S_N\to S_{R10},
}
\]

且一阶同源方向导数流收敛。

因此：

\[
\boxed{
\lim_{N\to\infty}D15[W:S_N]=D15[W:S_{R10}].
}
\]

\[
\boxed{
\lim_{N\to\infty}D15[W:dS_N]=D15[W:dS_{R10}].
}
\]

当前不再把 `TIGHT_STRICT_REMAINDER_CERTIFICATE` 作为 Case21/Z6 工程验证的硬门槛；但解析极限身份与零空间数值积分边界不变。

---

# 8. CH 同源一阶导数递推

对 `g in {D,q,alpha}`：

\[
\boxed{Y_{,g}=E_{u,g}/h.}
\]

材料区间在一次试件求解中固定，故：

\[
c_{0,g}=h_{,g}=0.
\]

\[
\boxed{\tau_{,g}=Y_{11,g}+Y_{22,g}.}
\]

\[
\boxed{
\delta_{,g}=Y_{22}Y_{11,g}+Y_{11}Y_{22,g}-2Y_{12}Y_{12,g}.
}
\]

CH 导数递推：

\[
\boxed{
p_{n+1,g}=-2\delta_{,g}r_n-2\delta r_{n,g}-p_{n-1,g},
}
\]

\[
\boxed{
r_{n+1,g}=2p_{n,g}+2\tau_{,g}r_n+2\tau r_{n,g}-r_{n-1,g}.
}
\]

初值：

\[
\boxed{p_{0,g}=r_{0,g}=p_{1,g}=r_{1,g}=0.}
\]

因此：

\[
\boxed{
\frac{\partial T_n(Y)}{\partial g}
=p_{n,g}I+r_{n,g}Y+r_nY_{,g}.
}
\]

同一个材料系数流直接生成应力与切线；没有第二个切线材料模型。

---

# 9. RC 钢筋相完整解析账本

## 9.1 两方向钢筋

配筋率：

\[
\rho_{s,x},\qquad \rho_{s,y}.
\]

钢筋层位置：

\[
z_{s,x},\qquad z_{s,y}.
\]

等效钢筋体积厚度：

\[
\rho_st.
\]

当前 Case21 实际使用弹性钢筋分支：

\[
\boxed{\sigma_s=E_s\varepsilon_s,\qquad E_{t,s}=E_s.}
\]

该分支足以复现 Case21；若未来 RC 试件出现钢筋屈服，则需要先冻结属于 RC 钢筋自身的屈服后 current operator，不能直接套用 Z6 face radial-cap。

## 9.2 任意钢筋层应变

定义物理弯曲尺度：

\[
\boxed{
\beta_s(q)=\frac{\pi^2q}{\varepsilon_0b},\qquad
\beta_{s,q}=\frac{\pi^2}{\varepsilon_0b}.
}
\]

`x` 向钢筋：

\[
\boxed{
e_{s,x}=\nu D+MF_x+\alpha A_x+\beta_s z_{s,x}H_s.
}
\]

`y` 向钢筋：

\[
\boxed{
e_{s,y}=-D+k^2MF_y+\alpha A_y+k^2\beta_s z_{s,y}H_s.
}
\]

## 9.3 基本二维闭式矩

定义：

\[
\langle f\rangle=\frac1{\pi^2}\int_0^\pi\int_0^\pi f\,dX\,dY.
\]

有：

\[
\boxed{\langle F_x\rangle=\langle F_y\rangle=\frac14,}
\]

\[
\boxed{\langle H_s\rangle=\frac4{\pi^2},}
\]

\[
\boxed{\langle A_x\rangle=-\frac{1+\nu k^2}{4},\qquad \langle A_y\rangle=0,}
\]

\[
\boxed{\langle F_x^2\rangle=\langle F_y^2\rangle=\frac9{64},}
\]

\[
\boxed{\langle F_xA_x\rangle=-\frac{2\nu k^2+7}{64},}
\]

\[
\boxed{\langle F_yA_y\rangle=-\frac{3k^2-2\nu}{64},}
\]

\[
\boxed{\langle A_x^2\rangle=\frac{6k^4\nu^2+4k^2\nu+7}{64},}
\]

\[
\boxed{\langle A_y^2\rangle=\frac{3k^4-4k^2\nu+2\nu^2}{64},}
\]

\[
\boxed{\langle F_xH_s\rangle=\langle F_yH_s\rangle=\frac8{9\pi^2},}
\]

\[
\boxed{\langle A_xH_s\rangle=-\frac{12\nu k^2+5}{9\pi^2},}
\]

\[
\boxed{\langle A_yH_s\rangle=\frac{4k^2-3\nu}{9\pi^2},}
\]

\[
\boxed{\langle H_s^2\rangle=\frac14.}
\]

## 9.4 钢筋广义残量

定义：

\[
\mathcal C_{s,x}=\rho_{s,x}tE_s\varepsilon_0^2b\ell,
\]

\[
\mathcal C_{s,y}=\rho_{s,y}tE_s\varepsilon_0^2b\ell.
\]

`x` 向：

\[
R_q^{s,x}=\mathcal C_{s,x}\langle e_{s,x}e_{s,x,q}\rangle,
\]

其中：

\[
e_{s,x,q}=M_qF_x+\beta_{s,q}z_{s,x}H_s.
\]

全部展开：

\[
\begin{aligned}
\frac{R_q^{s,x}}{\mathcal C_{s,x}}={}&
\nu D[M_q\langle F_x\rangle+\beta_{s,q}z_{s,x}\langle H_s\rangle]\\
&+M[M_q\langle F_x^2\rangle+\beta_{s,q}z_{s,x}\langle F_xH_s\rangle]\\
&+\alpha[M_q\langle A_xF_x\rangle+\beta_{s,q}z_{s,x}\langle A_xH_s\rangle]\\
&+\beta_sz_{s,x}[M_q\langle H_sF_x\rangle+\beta_{s,q}z_{s,x}\langle H_s^2\rangle].
\end{aligned}
\]

\[
\boxed{
R_\alpha^{s,x}=\mathcal C_{s,x}\left[
\nu D\langle A_x\rangle+M\langle F_xA_x\rangle+\alpha\langle A_x^2\rangle+\beta_sz_{s,x}\langle H_sA_x\rangle
\right].
}
\]

`y` 向：

\[
e_{s,y,q}=k^2(M_qF_y+\beta_{s,q}z_{s,y}H_s).
\]

\[
\begin{aligned}
\frac{R_q^{s,y}}{\mathcal C_{s,y}}={}&k^2\Big\{
-D[M_q\langle F_y\rangle+\beta_{s,q}z_{s,y}\langle H_s\rangle]\\
&+k^2M[M_q\langle F_y^2\rangle+\beta_{s,q}z_{s,y}\langle F_yH_s\rangle]\\
&+\alpha[M_q\langle A_yF_y\rangle+\beta_{s,q}z_{s,y}\langle A_yH_s\rangle]\\
&+k^2\beta_sz_{s,y}[M_q\langle H_sF_y\rangle+\beta_{s,q}z_{s,y}\langle H_s^2\rangle]
\Big\}.
\end{aligned}
\]

\[
\boxed{
R_\alpha^{s,y}=\mathcal C_{s,y}\left[
-D\langle A_y\rangle+k^2M\langle F_yA_y\rangle+\alpha\langle A_y^2\rangle+k^2\beta_sz_{s,y}\langle H_sA_y\rangle
\right].
}
\]

## 9.5 钢筋轴力

`x` 向钢筋直接轴力：

\[
\boxed{P_{s,x}=0.}
\]

`y` 向：

\[
\boxed{
P_{s,y}=\rho_{s,y}tbE_s\varepsilon_0\left[
D-\frac{k^2M}{4}-\frac{4k^2qz_{s,y}}{\varepsilon_0b}
\right].
}
\]

## 9.6 钢筋一致切线

对任意一维弹性钢筋相：

\[
R_g^s=\mathcal C_s\langle ee_g\rangle,
\]

\[
\boxed{
R_{g,h}^s=\mathcal C_s[\langle e_he_g\rangle+\langle ee_{g,h}\rangle].
}
\]

由于只有 `qq` 二阶运动学项非零：

\[
R_{q,q}^s=\mathcal C_s[\langle e_q^2\rangle+\langle ee_{qq}\rangle],
\]

\[
R_{q,D}^s=\mathcal C_s\langle e_qe_D\rangle,
\]

\[
R_{q,\alpha}^s=\mathcal C_s\langle e_qe_\alpha\rangle,
\]

\[
R_{\alpha,D}^s=\mathcal C_s\langle e_\alpha e_D\rangle,
\]

\[
R_{\alpha,q}^s=\mathcal C_s\langle e_\alpha e_q\rangle,
\]

\[
R_{\alpha,\alpha}^s=\mathcal C_s\langle e_\alpha^2\rangle.
\]

---

# 10. Case21 钢筋闭式退化

Case21：

\[
k=1,\quad z_{s,x}=z_{s,y}=0,\quad
\rho_{s,x}=\rho_{s,y}=0.00375.
\]

\[
\boxed{
C_R=\frac{\rho_sE_s\varepsilon_0^2b\ell t}{32\times1000}=2.94090386184375.
}
\]

总钢筋 `q` 残量：

\[
\boxed{
R_q^s=C_RM_q[8D(\nu-1)+9M-5\alpha].
}
\]

等价历史报告形式：

\[
R_q^s=C_RM_q[8D(\nu-1)+M(9-5\lambda_A)].
\]

Airy：

\[
\boxed{
R_\alpha^s=-C_R[8D\nu(\nu+1)+5M-(4\nu^2+5)\alpha].
}
\]

报告形式：

\[
R_\alpha^s=-C_R[8D\nu(\nu+1)+M\{5-(4\nu^2+5)\lambda_A\}].
\]

轴向钢筋：

\[
\boxed{
P_s=\rho_{s,y}tbE_s\varepsilon_0\left(D-\frac M4\right).
}
\]

Case21 最终：

\[
R_q^{s,x}=+75.2380445433\ {\rm kN\,mm},
\]

\[
R_q^{s,y}=-369.9418579065\ {\rm kN\,mm},
\]

\[
\boxed{R_q^s=-294.7038133632\ {\rm kN\,mm}.}
\]

\[
R_\alpha^{s,x}=-4.2271807372\ {\rm kN\,mm},
\]

\[
R_\alpha^{s,y}=-0.1042072304\ {\rm kN\,mm},
\]

\[
\boxed{R_\alpha^s=-4.3313879676\ {\rm kN\,mm}.}
\]

最终钢筋全域最大应变审计：

\[
|\varepsilon_{s,x}|_{max}\approx3.53571\times10^{-4},
\]

\[
|\varepsilon_{s,y}|_{max}\approx1.64881\times10^{-3},
\]

均小于冻结屈服应变：

\[
\varepsilon_y=0.00265.
\]

所以 Case21 使用弹性钢筋分支是合法的。

---

# 11. 钢壳混凝土四材料相

当前 Z6 材料相：

1. 有效普通混凝土核心；
2. 上钢面板 `+`；
3. 下钢面板 `-`；
4. 纵向 web/PBL 等效钢相 `w`。

总轴力：

\[
\boxed{
P=(1-\rho_w)P_c^{full}+P_++P_-+P_w.
}
\]

总残量：

\[
\boxed{
R_q=(1-\rho_w)R_q^c+R_q^++R_q^-+R_q^w,
}
\]

\[
\boxed{
R_\alpha=(1-\rho_w)R_\alpha^c+R_\alpha^++R_\alpha^-+R_\alpha^w.
}
\]

Z6：

\[
t_c=122\ {\rm mm},\qquad t_s^+=t_s^-=4\ {\rm mm},
\]

\[
\rho_w=0.02.
\]

等效 web 钢面积：

\[
\boxed{A_{w,eq}=\rho_wbt_c=29280\ {\rm mm^2}.}
\]

有效混凝土面积：

\[
\boxed{A_{c,eff}=(1-\rho_w)bt_c=1\,434\,720\ {\rm mm^2}.}
\]

外钢面总面积：

\[
\boxed{A_{face}=2bt_s=96000\ {\rm mm^2}.}
\]

web 所占核心体积从混凝土中扣除，禁止 `100% concrete + 2% web steel` 双计。

---

# 12. Z6 上下钢面板 current map

核心中面 `z=0`。

核心：

\[
-61\le z\le61\ {\rm mm}.
\]

上钢面：

\[
61\le z\le65\ {\rm mm}.
\]

下钢面：

\[
-65\le z\le-61\ {\rm mm}.
\]

定义物理弯曲尺度：

\[
\boxed{\beta_f=\frac{\pi^2q}{\varepsilon_0b},\qquad \beta_{f,q}=\frac{\pi^2}{\varepsilon_0b}.}
\]

钢面继承同一个结构应变场：

\[
\boxed{
e_x^f=\nu_cD+MF_x+\alpha A_x+\beta_fzH_s,
}
\]

\[
\boxed{
e_y^f=-D+k^2MF_y+\alpha A_y+k^2\beta_fzH_s,
}
\]

\[
\boxed{
\gamma^f=2kc_Xc_Y[(M-\alpha)H_s-\beta_fz].
}
\]

其中 `nu_c` 出现在结构兼容应变场；钢材自身 `nu_s` 进入钢材平面应力关系。

钢材弹性 trial：

\[
\boxed{
C_s^{el}=\frac{E_s}{1-\nu_s^2}
\begin{bmatrix}
1&\nu_s&0\\
\nu_s&1&0\\
0&0&(1-\nu_s)/2
\end{bmatrix}.
}
\]

\[
\boldsymbol\sigma^{tr}=C_s^{el}\boldsymbol\varepsilon_f.
\]

展开：

\[
\sigma_x^{tr}=\frac{E_s}{1-\nu_s^2}(\varepsilon_x^f+\nu_s\varepsilon_y^f),
\]

\[
\sigma_y^{tr}=\frac{E_s}{1-\nu_s^2}(\nu_s\varepsilon_x^f+\varepsilon_y^f),
\]

\[
\tau^{tr}=\frac{E_s}{2(1+\nu_s)}\gamma_{xy}^f.
\]

von Mises trial：

\[
\boxed{
v=\sqrt{(\sigma_x^{tr})^2-\sigma_x^{tr}\sigma_y^{tr}+(\sigma_y^{tr})^2+3(\tau^{tr})^2}.
}
\]

定义材料标量：

\[
\boxed{\chi_f=\frac{v^2}{f_y^2}.}
\]

冻结 radial-cap 当前状态映射：

\[
\boxed{
g_f(\chi_f)=
\begin{cases}
1,&\chi_f\le1,\\
\chi_f^{-1/2},&\chi_f>1.
\end{cases}}
\]

\[
\boxed{\boldsymbol\sigma_f=g_f\boldsymbol\sigma^{tr}.}
\]

这是 path-independent current map，不是完整增量 J2 flow-history solver。

## 12.1 yield boundary 仅是物理审计方程

由于 trial stress 关于物理 `z` 为线性：

\[
\sigma_x^{tr}=a_x+b_xz,
\]

\[
\sigma_y^{tr}=a_y+b_yz,
\]

\[
\tau^{tr}=a_\tau+b_\tau z,
\]

所以：

\[
v^2=\mathcal A_fz^2+\mathcal B_fz+\mathcal C_f,
\]

其中：

\[
\mathcal A_f=b_x^2-b_xb_y+b_y^2+3b_\tau^2,
\]

\[
\mathcal B_f=2a_xb_x-a_xb_y-a_yb_x+2a_yb_y+6a_\tau b_\tau,
\]

\[
\mathcal C_f=a_x^2-a_xa_y+a_y^2+3a_\tau^2.
\]

局部 trial yield 边界：

\[
\boxed{
\mathcal A_fz^2+\mathcal B_fz+\mathcal C_f-f_y^2=0.
}
\]

但这**不是正式空间域切分要求**。当前正式路线明确不建立 spatial elastic/plastic cells。

## 12.2 face 同源 tangent

弹性：

\[
C_t^f=C_s^{el}.
\]

cap 分支：

\[
\mathbf n=\frac{\partial v}{\partial\boldsymbol\sigma^{tr}}
=\begin{bmatrix}
(2\sigma_x^{tr}-\sigma_y^{tr})/(2v)\\
(2\sigma_y^{tr}-\sigma_x^{tr})/(2v)\\
3\tau^{tr}/v
\end{bmatrix}.
\]

\[
\boxed{
C_t^f=\left[g_fI-\frac{g_f}{v}\boldsymbol\sigma^{tr}\mathbf n^T\right]C_s^{el}.
}
\]

没有独立的钢材切线拟合系数。

## 12.3 face 材料坐标解析流

对覆盖真实 `chi_f` 的材料区间：

\[
\chi_L\le\chi_f\le\chi_U,
\]

\[
\widehat\chi=\frac{\chi_f-c_\chi}{h_\chi},
\]

\[
\boxed{g_f(\chi_f)=\sum_{n=0}^{\infty}g_nT_n(\widehat\chi).}
\]

系数唯一由材料坐标积分定义。

若区间跨越 `chi=1`，定义：

\[
\theta_y=\arccos\frac{1-c_\chi}{h_\chi}.
\]

则：

\[
 g_0=\frac1\pi\left[
\int_0^{\theta_y}\frac{d\theta}{\sqrt{c_\chi+h_\chi\cos\theta}}
+(\pi-\theta_y)
\right],
\]

\[
 g_n=\frac2\pi\left[
\int_0^{\theta_y}\frac{\cos n\theta}{\sqrt{c_\chi+h_\chi\cos\theta}}\,d\theta
-\frac{\sin(n\theta_y)}n
\right].
\]

这些切分在**一维材料坐标**内，不是 `X,Y,z` 空间分区。

## 12.4 face exact-D15 value 通项

每一面 `s=+/-`：

\[
\boxed{
P_{s,n}=-\frac{bt_s}{2\pi^2}
 g_nD15_s[T_n(\widehat\chi_f)\sigma_y^{tr}].
}
\]

\[
\boxed{P_s=\sum_{n=0}^{\infty}P_{s,n}.}
\]

\[
\boxed{
R_{q,s,n}=\frac{b\ell t_s}{2\pi^2}g_nD15_s\left[
T_n(\widehat\chi_f)(\sigma_x^{tr}\varepsilon_{x,q}+\sigma_y^{tr}\varepsilon_{y,q}+\tau^{tr}\gamma_{,q})
\right].
}
\]

\[
\boxed{R_q^s=\sum_{n=0}^{\infty}R_{q,s,n}.}
\]

\[
\boxed{
R_{\alpha,s,n}=\frac{b\ell t_s}{2\pi^2}g_nD15_s\left[
T_n(\widehat\chi_f)(\sigma_x^{tr}\varepsilon_{x,\alpha}+\sigma_y^{tr}\varepsilon_{y,\alpha}+\tau^{tr}\gamma_{,\alpha})
\right].
}
\]

\[
\boxed{R_\alpha^s=\sum_{n=0}^{\infty}R_{\alpha,s,n}.}
\]

当前 `DOCUMENTATION GAP B`：把 face/web **同源 tangent** 也按上述逐 `n` 材料级数 -> D15 的格式完整打印；物理 current map 和 tangent 已经存在，不需要新钢材理论或 spatial yield-front。

---

# 13. Z6 web/PBL 等效纵向钢相

web 不建立离散线单元/条带/材料点。

\[
\boxed{dV_w^{eq}=\rho_w\,dV_c.}
\]

只读取纵向应变：

\[
\boxed{
e_y^w=-D+k^2MF_y+\alpha A_y+k^2BH_s\zeta.
}
\]

一维冻结 current law：

\[
\boxed{
u_w=\frac{E_s\varepsilon_y^w}{f_y},\qquad \chi_w=u_w^2.}
\]

\[
\boxed{
g_w(\chi_w)=
\begin{cases}
1,&\chi_w\le1,\\
\chi_w^{-1/2},&\chi_w>1.
\end{cases}}
\]

\[
\boxed{
\sigma_y^w=E_s\varepsilon_y^wg_w(\chi_w)
=\operatorname{clip}(E_s\varepsilon_y^w,-f_y,+f_y).
}
\]

一致切线：

\[
\boxed{E_t^w=E_s\quad(|E_s\varepsilon_y^w|<f_y),}
\]

\[
\boxed{E_t^w=0\quad(|E_s\varepsilon_y^w|>f_y).}
\]

轴力：

\[
\boxed{
P_w=-\frac{\rho_w}{\ell}\int_{V_c}\sigma_y^w\,dV.
}
\]

残量：

\[
\boxed{
R_q^w=\rho_w\int_{V_c}\sigma_y^w\varepsilon_{y,q}\,dV,
}
\]

\[
\boxed{
R_\alpha^w=\rho_w\int_{V_c}\sigma_y^w\varepsilon_{y,\alpha}\,dV.
}
\]

同源切线：

\[
R_{q,q}^w=\rho_w\int_{V_c}[E_t^w(\varepsilon_{y,q})^2+\sigma_y^w\varepsilon_{y,qq}]\,dV,
\]

\[
R_{q,\alpha}^w=\rho_w\int_{V_c}E_t^w\varepsilon_{y,q}\varepsilon_{y,\alpha}\,dV,
\]

\[
R_{\alpha,\alpha}^w=\rho_w\int_{V_c}E_t^w(\varepsilon_{y,\alpha})^2\,dV,
\]

\[
R_{q,D}^w=\rho_w\int_{V_c}E_t^w\varepsilon_{y,q}\varepsilon_{y,D}\,dV,
\]

\[
R_{\alpha,D}^w=\rho_w\int_{V_c}E_t^w\varepsilon_{y,\alpha}\varepsilon_{y,D}\,dV.
\]

\[
P_{w,g}=-\frac{\rho_w}{\ell}\int_{V_c}E_t^w\varepsilon_{y,g}\,dV.
\]

web 同样可在材料坐标 `chi_w` 上解析表示，再逐项 D15；不需要空间弹塑性分区。

---

# 14. 正式三元极限方程

经过材料解析与 D15 后，空间坐标已经从数值未知量中消失，得到：

\[
\boxed{P=P(D,q,\alpha),}
\]

\[
\boxed{R_q=R_q(D,q,\alpha),}
\]

\[
\boxed{R_\alpha=R_\alpha(D,q,\alpha).}
\]

同源一阶导数：

\[
P_D,P_q,P_\alpha,
\]

\[
R_{q,D},R_{q,q},R_{q,\alpha},
\]

\[
R_{\alpha,D},R_{\alpha,q},R_{\alpha,\alpha}.
\]

定义：

\[
\boxed{
J_{lim}=\begin{bmatrix}
P_D&P_q&P_\alpha\\
R_{q,D}&R_{q,q}&R_{q,\alpha}\\
R_{\alpha,D}&R_{\alpha,q}&R_{\alpha,\alpha}
\end{bmatrix}.
}
\]

\[
\boxed{\mathcal L=\det J_{lim}.}
\]

正式极限状态：

\[
\boxed{
F_{lim}(D,q,\alpha)=
\begin{bmatrix}
R_q\\R_\alpha\\\mathcal L
\end{bmatrix}=0.
}
\]

三个方程对应三个未知量；没有第四个“峰值搜索自由度”。

## 14.1 与平衡支路导数的等价性

定义平衡残量 Jacobian：

\[
J_c=\begin{bmatrix}
R_{q,q}&R_{q,\alpha}\\
R_{\alpha,q}&R_{\alpha,\alpha}
\end{bmatrix}.
\]

若 `det J_c != 0`，则：

\[
\begin{bmatrix}dq/dD\\d\alpha/dD\end{bmatrix}
=-J_c^{-1}\begin{bmatrix}R_{q,D}\\R_{\alpha,D}\end{bmatrix}.
\]

沿平衡流形：

\[
\boxed{
\frac{dP}{dD}=P_D+P_q\frac{dq}{dD}+P_\alpha\frac{d\alpha}{dD}.
}
\]

并有：

\[
\boxed{\mathcal L=\det(J_c)\frac{dP}{dD}.}
\]

所以在 `det J_c != 0` 的普通 fold 类型：

\[
\boxed{\mathcal L=0\iff dP/dD=0.}
\]

若同时 `det J_c=0`，则 `L=0` 可能代表不同的平衡奇异事件，必须做事件分类，不能自动当作普通荷载极大点。

## 14.2 多根身份规则

若三元系统有多个实根，禁止：

- 选最大 `P`；
- 选最接近试验；
- 按根序号任选。

正式身份：

\[
\boxed{
\text{与原点平衡状态连续连通的物理分支上的第一个可达荷载极大根}.
}
\]

必要时 continuation/homotopy 只用于连通性审计，不用于重新定义 `Pu`。

---

# 15. Case21 完整算例账本

## 15.1 输入

\[
b=\ell=1220\ {\rm mm},\quad t=19.30\ {\rm mm},
\]

\[
q_0=0.0025,
\]

\[
f_c=21.23\ {\rm MPa},\quad E_0=20321\ {\rm MPa},
\]

\[
\varepsilon_0=0.00209,\quad \nu=0.18,
\]

\[
\rho_{s,x}=\rho_{s,y}=0.00375,
\]

\[
E_s=200000\ {\rm MPa},\quad f_y=530\ {\rm MPa},
\]

\[
z_s=0.
\]

## 15.2 释放极限根

\[
\boxed{D_u=0.7887924801,}
\]

\[
\boxed{q_u=0.0018083572562965242,}
\]

\[
\boxed{\lambda_{A,u}=0.08623596353826937.}
\]

几何量：

\[
\boxed{M_u=0.02907033478365149,}
\]

\[
\boxed{M_{q,u}=20.345350113975815,}
\]

\[
\boxed{B_u=0.06754686155676540,}
\]

\[
\boxed{B_q=37.352609016594364,}
\]

\[
\boxed{\alpha_u=0.002506908330448254,}
\]

\[
\boxed{M_u-\alpha_u=0.026563426453203236.}
\]

## 15.3 极限连续应变场

令 `u=sin X, v=sin Y`：

\[
\boxed{
e_x=0.141355919335388
-0.000225621749740u^2
+0.027816880618427v^2
-0.026563426453203u^2v^2
+0.067546861556765uv\zeta.
}
\]

\[
\boxed{
e_y=-0.788679669225130
+0.027816880618427u^2
-0.000225621749740v^2
-0.026563426453203u^2v^2
+0.067546861556765uv\zeta.
}
\]

\[
\boxed{
\gamma=2\cos X\cos Y[0.026563426453203uv-0.067546861556765\zeta].
}
\]

## 15.4 R10 点值检查

中心中面 `X=Y=pi/2, zeta=0`：

\[
e_x=0.142383751750872,\qquad e_y=-0.787651836809646,\qquad \gamma=0.
\]

\[
E_{11}=0.000626727082612,
\]

\[
E_{22}=-0.787539025934776,
\]

\[
\lambda_1=0.000626727082612,
\qquad
\lambda_2=-0.787539025934776.
\]

最终：

\[
\boxed{\sigma_x=0.0266178\ {\rm MPa},}
\]

\[
\boxed{\sigma_y=-20.600016\ {\rm MPa},}
\]

\[
\boxed{\tau=0.}
\]

中心顶面 `zeta=+1`：

\[
\lambda_1=0.08300094849,
\qquad
\lambda_2=-0.70516480452,
\]

\[
t_1=0.08294454907,
\qquad r_1=1.65931645,
\]

所以进入第二拉伸段：

\[
u_R(t_1)=0.09775868960,
\qquad T_1=0.9775868960.
\]

\[
\boxed{\sigma_x=2.077812\ {\rm MPa},}
\]

\[
\boxed{\sigma_y=-0.448574\ {\rm MPa}.}
\]

## 15.5 真无限混凝土 D15

\[
\boxed{D15[S_{yy}]=-13.3438268630311.}
\]

\[
\boxed{P_c=337.92303037\ {\rm kN}.}
\]

有限 prefix 仅作无限流检查：

| N | Pc kN | Rq,c kN mm | Ralpha,c kN mm |
|---:|---:|---:|---:|
|32|331.443627|378.538431|2.254350|
|40|334.154393|342.519618|3.267325|
|48|335.940747|319.785778|3.831990|
|56|336.426240|311.550875|3.992162|
|64|336.647977|307.153494|4.061389|
|72|336.877977|304.229288|4.125324|
|80|337.035449|302.694835|4.162767|
|88|337.223247|300.447436|4.211845|
|96|337.340135|299.263517|4.240358|
|104|337.422904|298.294019|4.260083|

最终平衡要求：

\[
R_q^c\approx+294.703813363\ {\rm kN\,mm},
\]

\[
R_\alpha^c\approx+4.331387968\ {\rm kN\,mm}.
\]

## 15.6 钢筋贡献

\[
\rho_{s,y}tbE_s\varepsilon_0=36908.355\ {\rm N}.
\]

\[
\boxed{P_s=28.844798318\ {\rm kN}.}
\]

\[
\boxed{R_q^s=-294.703813363\ {\rm kN\,mm}.}
\]

\[
\boxed{R_\alpha^s=-4.331387968\ {\rm kN\,mm}.}
\]

因此：

\[
R_q=0,\qquad R_\alpha=0
\]

到求根精度。

## 15.7 历史保存的极限 Jacobian

历史发布列为 `(D,q,lambda_A)`：

\[
\boxed{
J_{21,\lambda}\approx
\begin{bmatrix}
140.016244 & -70566.7765 & 75.4429339\\
-1587.62545 & 920049.913 & -1213.05\\
6.41847002 & -10550.5046 & 25.2481285
\end{bmatrix}.
}
\]

正式坐标转换：

\[
\alpha=\lambda_AM,
\]

\[
d\alpha=M\,d\lambda_A+\lambda_AM_q\,dq.
\]

所以：

\[
F_{,\alpha}=F_{,\lambda_A}/M,
\]

\[
F_{,q}|_\alpha=F_{,q}|_{\lambda_A}-\frac{\lambda_AM_q}{M}F_{,\lambda_A}.
\]

转换后的正式 `(D,q,alpha)` Jacobian 约：

\[
\boxed{
J_{21,\alpha}\approx
\begin{bmatrix}
140.016244&-75120.03308&2595.186277\\
-1587.62545&993261.9106&-41728.10561\\
6.41847002&-12074.32136&868.518670
\end{bmatrix}.
}
\]

由于历史保存 Jacobian 只有有限显示精度，以其重构 `dP/dD` 会残留约 `-0.047 kN`，不能把这一显示舍入误差当作正式极限条件失效；正式释放条件仍是 exact 同源目标上的 `L=0`。

## 15.8 Case21 最终承载力

\[
\boxed{
P_u=P_c+P_s=366.7678286852115\ {\rm kN}.
}
\]

试验仅后比较：

\[
P_f=368.3127497435694\ {\rm kN},
\]

\[
\boxed{\text{error}=-0.419459\%.}
\]

## 15.9 continuation/localizer 的当前身份

本轮曾重新执行 `64x64x26` / `80x80x32` raw-current localizer 以重放连接支路。它们只能记为：

```text
AUDIT_LOCALIZER_REPLAY
```

不能改写正式积分身份。

例如 `64x64x26` 自己定位的峰：

\[
D_{u,64}=0.789051374193,
\]

\[
q_{u,64}=0.001807783150613,
\]

\[
\alpha_{u,64}=0.002482974980309,
\]

\[
P_{u,64}^{loc}=366.777033047\ {\rm kN}.
\]

`80x80x32`：

\[
D_{u,80}=0.788903626024,
\]

\[
q_{u,80}=0.001807976548337,
\]

\[
\alpha_{u,80}=0.002493599209932,
\]

\[
P_{u,80}^{loc}=366.773347617\ {\rm kN}.
\]

二者向正式 exact-D15 极限靠近，但**不用于外推新的 `Pu`**。

---

# 16. Z6 完整算例账本

## 16.1 输入

\[
a=24000\ {\rm mm},\qquad b=\ell=12000\ {\rm mm},\qquad m_*=2,
\]

\[
q_0=0.004,
\]

\[
t_c=122\ {\rm mm},\qquad t_s=4\ {\rm mm},\qquad \rho_w=0.02,
\]

\[
f_c=30.4\ {\rm MPa},\qquad \varepsilon_0=0.0018712490394580678,
\]

\[
\nu_c=0.18,
\]

\[
E_s=206000\ {\rm MPa},\qquad f_y=355\ {\rm MPa},\qquad \nu_s=0.30.
\]

## 16.2 释放极限根

\[
\boxed{D_u=1.36180798,}
\]

\[
\boxed{q_u=0.0264854039,}
\]

\[
\boxed{\lambda_{A,u}=0.786915819.}
\]

\[
\boxed{M_u=2.4086853792820073,}
\]

\[
\boxed{M_{q,u}=160.79039729931628,}
\]

\[
\boxed{M_{qq}=5274.340396694442,}
\]

\[
\boxed{\alpha_u=1.8954326279510263,}
\]

\[
\boxed{M_u-\alpha_u=0.513252751330981.}
\]

核心：

\[
\boxed{B_u=0.7101062648720707,}
\]

\[
\boxed{B_q=26.81123034986341.}
\]

钢面物理弯曲：

\[
\boxed{\beta_f=0.0116410863093782\ {\rm mm^{-1}}.}
\]

在 `z=61 mm`：

\[
\beta_fz=0.710106264872070,
\]

与核心 `B` 在表面连续。

## 16.3 极限连续应变场

令 `u=sin X, v=sin Y`：

\[
\boxed{
e_x=-0.228732720587757
-0.170588936515592u^2
+1.460969065306494v^2
-0.513252751330981u^2v^2
+0.710106264872071uv\zeta.
}
\]

\[
\boxed{
e_y=-1.276513511742204
+1.460969065306494u^2
-0.170588936515592v^2
-0.513252751330981u^2v^2
+0.710106264872071uv\zeta.
}
\]

\[
\boxed{
\gamma=2\cos X\cos Y[0.513252751330981uv-0.710106264872071\zeta].
}
\]

## 16.4 R10 点值检查

中心中面：

\[
e_x=0.548394656872,
\qquad e_y=-0.499386134282,
\]

\[
E_{11}=0.473858156988,
\qquad E_{22}=-0.414091666024.
\]

\[
\lambda_1=0.473858156988,
\qquad \lambda_2=-0.414091666024.
\]

\[
\boxed{\sigma_x=0.9162631\ {\rm MPa},}
\]

\[
\boxed{\sigma_y=-15.0197503\ {\rm MPa}.}
\]

## 16.5 混凝土真无限 D15

\[
\boxed{D15[S_{yy}]=-10.32641404844.}
\]

全核心：

\[
\boxed{P_{c,full}=23.2827595918\ {\rm MN}.}
\]

扣除 web 占据的 `2%` 核心体积：

\[
\boxed{P_{c,eff}=0.98P_{c,full}=22.8171044\ {\rm MN}.}
\]

prefix 检查：

| N | Pc,full MN | Rq,c GN mm | Ralpha,c GN mm |
|---:|---:|---:|---:|
|12|23.065253|-10.867190|0.0293100|
|16|23.384713|-10.904430|0.0303091|
|20|23.414507|-10.854997|0.0304573|
|24|23.348197|-10.844512|0.0305887|
|28|23.321494|-10.846732|0.0305357|
|32|23.310103|-10.849719|0.0304506|
|36|23.297615|-10.845237|0.0303836|
|40|23.269059|-10.828061|0.0302653|

有限 prefix 的振荡来自物理 C2 结点 `n^-4` 尾和附近复平方根奇点；不选择“最佳有限 N”。

## 16.6 钢面与 web

最终 trial face：

\[
\boxed{\max\sigma_{VM}^{tr}/f_y\approx1.9474.}
\]

说明钢面局部已进入 cap，但不建立空间塑性区 cell。

历史最终文件只冻结两块钢面**合计**：

\[
\boxed{P_{face}=P_++P_-=18.5564373\ {\rm MN}.}
\]

没有冻结 `P_+` 和 `P_-` 的最终独立 exact-limit 数字，因此不得假定二者各占一半或自行制造数值。

web：

\[
\boxed{P_w=7.0325797\ {\rm MN}.}
\]

## 16.7 Z6 最终承载力

\[
\boxed{
P_u=P_{c,eff}+P_{face}+P_w
=48.4061215\ {\rm MN}.
}
\]

后比较：

\[
P_{Zhou}=49.4867667519\ {\rm MN},
\]

\[
\boxed{\text{error}=-2.183706\%.}
\]

\[
P_{Winter}=50.1858541295\ {\rm MN},
\]

\[
\boxed{\text{error}=-3.546283\%.}
\]

## 16.8 峰值邻域支路只作为机制审计

历史保存：

| D | q | lambda_A | Pc,eff MN | Pface MN | Pw MN | Ptotal MN |
|---:|---:|---:|---:|---:|---:|---:|
|1.34|0.02617602|0.78719647|22.79690|18.58797|7.01927|48.40413|
|1.35|0.02631834|0.78707112|22.80669|18.57343|7.02547|48.40558|
|1.36|0.02645989|0.78694020|22.81558|18.55903|7.03151|48.40612|
|1.37|0.02660070|0.78680459|22.82371|18.54473|7.03737|48.40581|
|1.38|0.02674068|0.78665901|22.83114|18.53052|7.04311|48.40477|

它说明峰值机制：

- `Pc,eff` 在增加；
- `Pw` 在增加；
- `Pface` 在下降；
- 三相路径贡献在极限附近相互抵消。

但该表不是正式 `Pu` 求解必经加载步。

---

# 17. Case21 与 Z6 的统一结构母理论

Case21 材料相：

\[
\boxed{\text{R10 concrete}+s_x+s_y.}
\]

Z6 材料相：

\[
\boxed{0.98\,\text{R10 concrete}+\text{upper face}+\text{lower face}+\text{web}.}
\]

二者共享：

\[
\boxed{(D,q,\alpha)}
\]

\[
\Downarrow
\]

\[
\boxed{\text{Nguyen continuous halfwave kinematics}}
\]

\[
\Downarrow
\]

\[
\boxed{\text{current material operators}}
\]

\[
\Downarrow
\]

\[
\boxed{\text{material analytic streams}}
\]

\[
\Downarrow
\]

\[
\boxed{\text{CH + exact D15}}
\]

\[
\Downarrow
\]

\[
\boxed{P,R_q,R_\alpha,\text{same-source first derivatives}}
\]

\[
\Downarrow
\]

\[
\boxed{R_q=0,\ R_\alpha=0,\ \det J_{lim}=0}
\]

\[
\Downarrow
\]

\[
\boxed{P_u.}
\]

因此：

\[
\boxed{\text{Case21 与 Z6 不是两套求解器。}}
\]

改变的是物理材料相，不是结构层求解逻辑。

---

# 18. 直接联立 vs 迭代：正式定位

需要永久区分三种“迭代”：

### A. 空间/材料点加载迭代

例如：

```text
Gauss point -> material state update -> load increment -> history update
```

正式理论：

\[
\boxed{\text{PROHIBITED}.}
\]

### B. 逐 `D` continuation

```text
D0 -> solve q,alpha -> D1 -> solve q,alpha -> ... -> peak
```

正式定位：

\[
\boxed{\text{AUDIT ONLY / ROOT IDENTITY}.}
\]

### C. 三元代数非线性求根器内部迭代

\[
F_{lim}(D,q,\alpha)=0.
\]

可以使用 Newton、trust-region、interval solver 等。

正式定位：

\[
\boxed{\text{ALLOWED MATHEMATICAL BACKEND}.}
\]

它不引入任何空间离散，也不改变正式三元联立理论。

---

# 19. 当前完整性审计

| 模块 | 当前状态 | 说明 |
|---|---|---|
| 原始输入 -> `Dx,Dy,H` | **待补 A** | Case21/Z6 不受影响；新试件前端仍需统一展开 |
| 半波选择 | PASS | `m*`,`ell`,`k`,`q0` 明确 |
| `(D,q,alpha)` 工作坐标 | PASS | `lambda_A` 降为报告量 |
| 连续二阶运动学 | PASS | 一、二阶导数已显式 |
| R10 普通混凝土 | PASS | current map 与局部切线已显式 |
| 真无限材料解析流 | PASS | 系数唯一定义、递推、尾部和 `n->infty` 身份明确 |
| CH 降幂 | PASS | `p_n,r_n` 与 `P_n,Q_n` 通项递推已补齐 |
| D15 | PASS | 单项、结构目标、体积因子明确 |
| RC 钢筋 Case21 分支 | PASS | 弹性适用域已验证 |
| 任意 RC 屈服后钢筋 | DOMAIN BOUNDARY | 未冻结，不能借 Z6 face law |
| Z6 face current law | PASS | radial-cap 与物理 tangent 明确 |
| Z6 face/web tangent -> 逐 `n` D15 | **待补 B** | 文档层补齐，不是新材料理论 |
| 三元极限方程 | PASS | `Rq=Ralpha=L=0` |
| 多根身份 | **协议待冻结 C** | continuation 仅必要时用于连通性审计 |
| Case21 Pu | RELEASED | `366.767828685 kN` |
| Z6 Pu | RELEASED | `48.4061215 MN` |

因此当前真正剩下的工作不是“重新发明理论”，而是：

\[
\boxed{A:\ \text{原始截面参数}\to D_x,D_y,H}
\]

\[
\boxed{B:\ \text{Z6 face/web same-source tangent 的材料级数逐项 D15 账本}}
\]

\[
\boxed{C:\ \text{三元直接求根后的多根连通性审计协议}}
\]

---

# 20. 已纠正/废止的理解

以下解释不得再复活：

1. `R10 本身是无限本构模型` —— **FALSE**。R10 是有限 current operator；无限性属于连续复合场的解析表示。
2. `必须为 full R10 再发明独立无限 recurrence` —— **FALSE**。
3. `N48/N192/N240/N288 是正式材料阶数` —— **FALSE**。只是一致无限流的部分和。
4. `Z6 radial-cap 必须先做空间弹/塑区 yield-front 切分` —— **FALSE**。yield boundary 只作物理审计，正式使用统一材料坐标函数。
5. `Gauss/Simpson/material-point grid 是正式算子` —— **FALSE**。
6. `Case21/Z6 必须从低 D 一步步加载到峰值` —— **FALSE**。正式生产直接解 `Rq=Ralpha=L=0`。
7. `Newton 迭代出现就意味着加载步理论` —— **FALSE**。三元代数根求解器内部迭代允许。
8. `选最大根/最接近试验的根` —— **FALSE**。
9. `Case21 与 Z6 使用两套不同极限求解器` —— **FALSE**。
10. `Z6 face 已屈服就必须整个面板降为 Et=0` —— **FALSE**。face 使用二维 radial-cap current tangent。
11. `web 只是最后额外加 2% 钢力` —— **FALSE**。web 同时进入 `P,Rq,Ralpha,Jacobian`，且混凝土体积先扣除其占据份额。
12. `lambda_A 是原点正式自由度` —— **FALSE**。正式坐标是 `alpha`。

---

# 21. 当前正式主流程（以后新聊天优先加载）

```text
[INPUT]
  a,b,A0,thicknesses,material parameters,phase geometry
        |
        v
[HALFWAVE]
  Dx,Dy,H -> m* -> ell=a/m* -> k=b/ell -> q0=A0/b
        |
        v
[GLOBAL UNKNOWN]
  x=(D,q,alpha)
        |
        v
[KINEMATICS]
  continuous Nguyen/von-Karman halfwave strain field
  + first/second kinematic derivatives
        |
        v
[MATERIAL PHASES]
  concrete R10
  RC rebar / face steel / web as applicable
        |
        v
[MATERIAL-COORDINATE ANALYTIC STREAM]
  U,C,T,T7 or steel cap/clip streams
        |
        v
[2x2 CH]
  T_n(Y)=p_n I+r_n Y
        |
        v
[GENERAL-D15]
  exact nth structural moments
        |
        v
[n -> infinity]
  P(D,q,alpha), Rq(D,q,alpha), Ralpha(D,q,alpha)
  same-source first derivatives
        |
        v
[DIRECT LIMIT SYSTEM]
  Rq=0
  Ralpha=0
  det J_lim=0
        |
        v
[ROOT IDENTITY AUDIT IF NEEDED]
  connected to origin, first reachable maximum
        |
        v
[RESULT]
  (Du,qu,alphau)
  Pu=P(Du,qu,alphau)
        |
        v
[POST-SOLVE COMPARISON ONLY]
  experiment / Zhou / Winter
```

---

# 22. 当前冻结数值摘要

## Case21

```text
m* = 1
ell = 1220 mm
q0 = 0.0025
Du = 0.7887924801
qu = 0.0018083572562965242
alphau = 0.002506908330448254
lambda_A,u = 0.08623596353826937
Pc = 337.92303037 kN
Ps = 28.844798318 kN
Pu = 366.7678286852115 kN
Pf_exp = 368.3127497435694 kN
error = -0.419459 %
```

## Z6(a=24000)

```text
m* = 2
ell = 12000 mm
q0 = 0.004
Du = 1.36180798
qu = 0.0264854039
alphau = 1.8954326279510263
lambda_A,u = 0.786915819
Pc,full = 23.2827595918 MN
Pc,eff = 22.8171044 MN
Pface = 18.5564373 MN
Pw = 7.0325797 MN
Pu = 48.4061215 MN
Zhou = 49.4867667519 MN, error = -2.183706 %
Winter = 50.1858541295 MN, error = -3.546283 %
```

---

# 23. 历史证据与本文件的关系

本总账优先引用/承接以下历史证据文件，但不删除它们的独立身份：

1. `semantic_v2/40_execution/combined/20260817_1526__NZSCCM__TRUE_INFINITE_R10_D15_LIMIT_Z6_CASE21__EXECUTION_REPORT.md`
   - Stage-I -> Stage-II -> n->infinity -> finite coupled solve；
   - Case21/Z6 真无限目标释放；
   - raw-R10 grid 明确为 audit/localization oracle。

2. `semantic_v2/40_execution/combined/20260817_1526__NZSCCM__TRUE_INFINITE_R10_D15_LIMIT_Z6_CASE21__REPRO.py`
   - raw-R10 audit-only 复算器；
   - Case21 reinforcement 闭式；
   - Z6 face/web audit evaluator；
   - 代码内明确 `FORMAL SPATIAL QUADRATURE = 0`。

3. `semantic_v2/40_execution/combined/20260817_1551__NZSCCM__Z6_CASE21__HUMAN_CALCULABILITY_FULL_CHAIN_AUDIT.md`
   - 提出严格人工可计算性审计；
   - 其中“Z6 必须 spatial yield-front 分区”后来已被 17:30 正式修正，不再作为当前缺口；
   - 其余“公式不能隐藏在程序里”的原则继续保留。

4. `semantic_v2/40_execution/combined/20260817_1730__NZSCCM__CASE21_Z6__FINITE_R10_TRUE_INFINITE_D15_JOINT_EXECUTION.md`
   - 当前 Case21/Z6 最关键联合执行证据；
   - 明确 R10 finite current operator；
   - 明确真无限属于解析表示；
   - 明确 Z6 face radial-cap 可统一解析表示而无需 spatial yield-front；
   - 冻结 Case21/Z6 最终根与 `Pu`。

5. `semantic_v2/40_execution/combined/20260817_1730__NZSCCM__CASE21_Z6__FINITE_R10_TRUE_INFINITE_D15__PARAMS_AND_INTERMEDIATES.json`
   - 最终参数和中间量数值账本。

本文件新增/补齐的当前聊天成果包括：

- 正式工作坐标明确锁定为 `(D,q,alpha)`；
- 直接三元极限方程取代“逐 D 加载生产”叙述；
- rectangular Airy / 全部一、二阶运动学导数；
- R10 点值与同源导数账本；
- 真无限材料系数定义与核递推；
- `P_n[a,b],Q_n[a,b]` CH 多项式通项递推；
- CH 同源导数递推；
- General-D15 通式；
- 一般 RC 两方向钢筋解析矩与 Case21 退化；
- Z6 上/下 face 与 web 的完整物理 current operator；
- face value-target 的材料级数逐项 D15 通式；
- 直接联立 vs continuation vs algebraic root iteration 的正式语义划分；
- 当前剩余 A/B/C 三项文档边界。

---

# 24. 下一步唯一推荐工作

本文件创建后，后续对话不要重新从 Case21/Z6 的 `Pu` 开始推倒重来。

推荐下一步：

\[
\boxed{
\text{GAP A：从原始 RC / steel-shell 截面材料参数显式推导 }D_x,D_y,H
}
\]

目标是彻底闭合：

\[
\boxed{
\text{原始试件输入}\to D_x,D_y,H\to m_*\to\ell\to\text{非线性直接三元极限系统}\to P_u.
}
\]

完成 A 后，再做 B（face/web tangent 的逐 `n` D15 账本），最后冻结 C（多根连通性审计协议）。

---

# 25. 恢复口令 / 新聊天最短入口

如果聊天再次达到长度上限，新对话首先读取本文件，并采用以下恢复口径：

```text
读取 20260818_2135__NZSCCM__CURRENT_COMPLETE_THEORY_LEDGER_CASE21_Z6__LOCKED_HANDOFF.md。
它是当前共享理论基线，不替代历史原始 evidence，但集中包含 2026-08-18 21:35 前已经恢复和修正的 Case21/Z6 理论总账。
正式 Pu 主线是：零空间数值积分的材料解析流 -> CH -> D15 -> P,Rq,Ralpha 及同源一阶导数 -> 直接联立 Rq=0, Ralpha=0, det(J_lim)=0 -> (Du,qu,alphau) -> Pu。
逐 D continuation 仅作 connected-branch/root-identity audit，不作为正式 Pu 生产算法。
下一步从 GAP A：原始截面参数 -> Dx,Dy,H 开始，不重新打开 R10、Case21/Z6 最终根或 spatial quadrature。
```

---

**END OF CURRENT CONSOLIDATED HANDOFF — 2026-08-18 21:35 +08:00**