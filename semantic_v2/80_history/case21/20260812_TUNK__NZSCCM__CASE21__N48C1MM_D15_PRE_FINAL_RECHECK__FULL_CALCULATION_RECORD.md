# NZ-SCCM Case21 更新后完整计算闭合
## 闭式 R10 → N48-C1/MM → Cayley–Hamilton → Nguyen 完整半波 → D15 → \(R_q=0,L=0\) → 最后才与试验比较

## 0. fresh closure 隔离规则

```text
历史 Case21 计算荷载 = 不读取
历史 Case21 D/q 根 = 不读取
历史 Case21 荷载路径 = 不读取
历史 FE / Gauss / Simpson 计算 = 不读取
试验破坏荷载 = 求解期间不读取
空间 Gauss = 0
空间 Simpson = 0
空间 adaptive quadrature = 0
空间 Chebyshev collocation = 0
空间材料点网格 = 0
```

程序后台可使用 FFT convolution 加速**解析系数序列的卷积**；它不在物理空间取样，因此不是空间 Fourier collocation。最终空间积分仍由 D15 解析矩完成。浮点卷积使用 \(10^{-5}\) 的系数噪声清理阈值，该阈值只清理 FFT 浮点噪声，不获得理论参数身份。

---

# 1. 原始输入

\[
b=\ell=1220\ {\rm mm},\qquad t_p=19.30\ {\rm mm}.
\]

式中，\(b\) 为一个完整代表半波的横向宽度；\(\ell\) 为轴压方向代表半波长度；\(t_p\) 为板厚。

\[
f_c=21.23\ {\rm MPa},\quad E_0=20321\ {\rm MPa},\quad
\varepsilon_0=0.00209,\quad \nu=0.18.
\]

式中，\(f_c\) 为混凝土单轴抗压强度；\(E_0\) 为初始弹性模量；\(\varepsilon_0\) 为参考压缩应变；\(\nu\) 为泊松比。

\[
q_0=1/400=0.0025.
\]

总双向配筋率为 \(0.75\%\)，两个方向均分：

\[
\rho_{s,x}=\rho_{s,y}=0.00375.
\]

Case21 为中面单层钢筋。钢筋参数为

\[
E_s=200000\ {\rm MPa},\qquad
\varepsilon_y=0.00265,\qquad
f_y=530\ {\rm MPa}.
\]

---

# 2. R10 基本参数

\[
\kappa=\frac{E_0\varepsilon_0}{f_c}
=\frac{20321\times0.00209}{21.23}
=\boxed{2.000512953368}.
\]

式中，\(\kappa\) 为归一化初始切线。

\[
x_{cr}=\frac{0.1}{\kappa}
=\boxed{0.049987179454}.
\]

式中，\(x_{cr}\) 为 R10 拉伸特征材料坐标。

\[
\eta=\frac{x_{cr}}{20}
=\boxed{0.002499358973}.
\]

式中，\(\eta\) 为拉、压平滑分离尺度。

---

# 3. Foster 源材料功

取

\[
m_t=-\frac7{90},\qquad \eta_r=0.05.
\]

Foster 源函数为

\[
T_{src}(r)
=r+(m_t-1)H(r,1)-m_tH(r,10).
\]

对平滑铰函数作闭式积分得到

\[
\int_0^{10}T_{src}(r)dr
=\boxed{6.349875213599}.
\]

于是

\[
W_{src}
=\rho x_{cr}\int_0^{10}T_{src}(r)dr
=\boxed{0.031741235181}.
\]

取 \(u_r=0.03\)，材料功闭合：

\[
h=\frac15\left(
\frac{W_{src}}{x_{cr}}
-\frac{\rho}{10}
-\frac92u_r
\right)
=\boxed{0.097997504272}.
\]

这里没有结构试验荷载。

---

# 4. R10 四个材料 primitive

压缩函数：

\[
C(\lambda)
=
\frac{\kappa\Pi_\eta(-\lambda)}
{1+(\kappa-2)\Pi_\eta(-\lambda)+[\Pi_\eta(-\lambda)]^2}.
\]

拉伸上升支：

\[
u_1(\tau)
=\rho\tau
+(10h-6\rho)\tau^3
+(8\rho-15h)\tau^4
+(6h-3\rho)\tau^5.
\]

下降支：

\[
u_2(s)
=h+(u_r-h)(10s^3-15s^4+6s^5).
\]

\[
T(\lambda)
=\frac{u_{sm}[\Pi_\eta(\lambda)]}{\rho},
\qquad
T^{(7)}(\lambda)=[T(\lambda)]^7.
\]

current master：

\[
U(\lambda)
=
\kappa\lambda-C(\lambda)
+\kappa\Pi_\eta(-\lambda)
+\rho T(\lambda)
-\kappa\Pi_\eta(\lambda).
\]

因此材料编译目标只有

\[
\boxed{F\in\{U,C,T,T^7\}}.
\]

---

# 5. 本次 fresh compiler

求解前固定

\[
\boxed{\lambda\in[-1.15,0.12]}.
\]

它不由历史 Case21 根确定。

\[
\lambda_c=-0.515000000000,\qquad
\lambda_h=0.635000000000,
\]
\[
\xi_0=-\lambda_c/\lambda_h=0.811023622047.
\]

---

# 6. direct N48 与 N48-C1

49 个一维材料根点：

\[
\theta_j=\frac{(j+1/2)\pi}{49},
\qquad
\lambda_j=\lambda_c+\lambda_h\cos\theta_j.
\]

direct N48：

\[
a_n^{(F,0)}
=
\frac{2-\delta_{n0}}{49}
\sum_{j=0}^{48}
F(\lambda_j)\cos(n\theta_j).
\]

R10 的严格锚点为

\[
U(0)=0,\quad U'(0)=\kappa,
\]
\[
C(0)=T(0)=T^7(0)=0,
\]
\[
C'(0)=T'(0)=(T^7)'(0)=0.
\]

对 \(U,C,T^7\)：

\[
\mathbf a^{(F,C1)}
=
\mathbf a^{(F,0)}
+\mathbf H^{-1}\mathbf G^T
(\mathbf G\mathbf H^{-1}\mathbf G^T)^{-1}
(\mathbf d_F-\mathbf G\mathbf a^{(F,0)}).
\]

该修正只含一个 \(2\times2\) 小矩阵求逆。

---

# 7. T constrained-minimax

仍使用单一48阶：

\[
T_{48}^{MM}(\lambda)
=
\sum_{n=0}^{48}
a_n^{(T,MM)}
\mathcal C_n[\xi(\lambda)].
\]

\[
\min_{\mathbf a}
\left\|
T_{48}^{MM}-T_{R10}
\right\|_{L^\infty[-1.15,0.12]}
\]

同时严格满足

\[
T_{48}^{MM}(0)=0,\qquad
(T_{48}^{MM})'(0)=0.
\]

独立一维材料验证：

| primitive | max abs error |
|---|---:|
| U | 0.002453604 |
| C | 0.014012978 |
| T | 0.089860050 |
| T7 | 0.112735998 |

\[
e_{\infty,T}=\boxed{0.089569236}.
\]

---

# 8. 前8个系数作为 generator 快速核验

- \(U\): -0.594171824, 0.586405144, 0.192941567, -0.0195747305, -0.0348885968, -0.0196127025, -0.0116456752, -0.00750416271
- \(C\): 0.611670879, -0.553227047, -0.164946234, 0.0399831952, 0.0466773499, 0.02323503, 0.00884001271, 0.000833055209
- \(T\): 0.175897098, 0.332737307, 0.279535776, 0.202350329, 0.115570227, 0.0343308429, -0.0285757588, -0.0655147784
- \(T^7\): 0.134789345, 0.257254571, 0.222201376, 0.169836479, 0.108115656, 0.0461258587, -0.00751265222, -0.0461367665

完整49×4系数另附 CSV；独立盲算不应直接使用答案系数表，而应从上述公式重新生成。

---

# 9. Cayley–Hamilton

\[
\mathbf Y
=\frac{\mathbf X-\lambda_c\mathbf I}{\lambda_h},
\quad
K_1=\operatorname{tr}\mathbf Y,
\quad
K_2=\det\mathbf Y.
\]

\[
\mathbf Y^2-K_1\mathbf Y+K_2\mathbf I=0.
\]

\[
\mathcal C_n(\mathbf Y)
=A_n\mathbf I+B_n\mathbf Y.
\]

初值：

\[
A_0=1,\ B_0=0,\quad
A_1=0,\ B_1=1.
\]

递推：

\[
A_{n+1}=-2K_2B_n-A_{n-1},
\]

\[
B_{n+1}=2A_n+2K_1B_n-B_{n-1}.
\]

所以每一个材料系数逐项进入二维张量：

\[
\boxed{
\mathbf F_{48}^{(n)}
=
a_n^{(F,*)}(A_n\mathbf I+B_n\mathbf Y)
}.
\]

---

# 10. 二维 current-map

\[
\mathbf{CC}
=\det(\mathbf C)\mathbf C,
\]

\[
\mathbf{TC}
=\mathbf C[\operatorname{tr}(\mathbf T)\mathbf I-\mathbf T],
\]

\[
\mathbf{TT}
=\det(\mathbf T)
[\operatorname{tr}(\mathbf T^{(7)})\mathbf I-\mathbf T^{(7)}].
\]

最终：

\[
\boxed{
\mathbf S
=
\mathbf U-a_{cc}\mathbf{CC}
+\mathbf{TC}
-\rho a_t\mathbf{TT}
}.
\]

其中

\[
a_{cc}=0.107232924936241,\qquad
a_t=0.082995956795329.
\]

---

# 11. Nguyen 二阶完整方形半波

\[
X=\frac{\pi x}{b},\quad
Y=\frac{\pi y}{\ell},\quad
\zeta=\frac{2z}{t_p}.
\]

\[
C_m
=
\frac{\pi^2}{\varepsilon_0}
\left(q_0q+\frac12q^2\right),
\]

\[
C_b
=
\frac{\pi^2}{2\varepsilon_0}\frac{t_p}{b}q.
\]

本次 fresh 极限状态：

\[
D=\boxed{0.78234000},\qquad
q=\boxed{0.0017704700},
\]
\[
A=bq=\boxed{2.159973\ {\rm mm}}.
\]

\[
C_m=\boxed{0.028302894588},\qquad
C_b=\boxed{0.066131673686}.
\]

连续应变场：

\[
e_x
=\nu D+C_m\cos^2X\sin^2Y
+C_b\sin X\sin Y\zeta,
\]

\[
e_y
=-D+C_m\sin^2X\cos^2Y
+C_b\sin X\sin Y\zeta,
\]

\[
g_{xy}
=
2C_m\sin X\cos X\sin Y\cos Y
-2C_b\cos X\cos Y\zeta.
\]

---

# 12. 连续谱域证书

不使用空间采样点。对 \(I_1=\operatorname{tr}\mathbf X\)、\(I_2=\det\mathbf X\) 和

\[
\Delta=I_1^2-4I_2
\]

采用低阶多项式 Bernstein 包络，得到整个连续半波

\[
\boxed{
-0.874981134\le\lambda\le0.092641134
}.
\]

因此

\[
[-0.874981134,0.092641134]\subset[-1.15,0.12],
\]

compiler-domain gate 通过。

---

# 13. D15 精确矩

任何待积场写为

\[
Q(X,Y,\zeta)
=
\sum_{i,j,k}
c_{ijk}
\mathcal C_i(\sin X)
\mathcal C_j(\sin Y)
\mathcal C_k(\zeta).
\]

\[
M_n=
\begin{cases}
\pi,&n=0,\\
2\sin(n\pi/2)/n,&n\ge1,
\end{cases}
\]

\[
Z_k=
\begin{cases}
0,&k\text{ 为奇数},\\
2/(1-k^2),&k\text{ 为偶数}.
\end{cases}
\]

\[
\boxed{
\mathscr D[Q]
=
\sum c_{ijk}M_iM_jZ_k
}.
\]

程序实现先在 \(u=\sin X,v=\sin Y,\zeta\) 的有限幂系数上做解析卷积，再用有限 power-to-Chebyshev 恒等转换。该做法与 \(M_iM_jZ_k\) 完全等价，不在物理空间取点。

最终：

\[
\boxed{
\mathscr D[S_{yy}]=-13.307143369080
},
\]

\[
\boxed{
\mathscr D[Q_q]=4.479986884859
}.
\]

---

# 14. 混凝土轴力

\[
P_c
=
-\frac{f_cbt_p}{2\pi^2}
\mathscr D[S_{yy}]
=
\boxed{336.994047\ {\rm kN}}.
\]

---

# 15. 混凝土幅值残量

\[
\mathbf e
=(1+\nu)\mathbf X
-\nu\operatorname{tr}(\mathbf X)\mathbf I.
\]

\[
Q_q
=
\mathbf S:\mathbf e_{,q}.
\]

\[
J_\Omega
=\frac{b\ell t_p}{2\pi^2}
=\boxed{1455282.239926\ {\rm mm^3}}.
\]

\[
R_{q,c}
=f_c\varepsilon_0J_\Omega
\mathscr D[Q_q]
=
\boxed{289.281228\ {\rm kN\,mm}}.
\]

---

# 16. 钢筋

轴向钢筋力：

\[
P_s
=
\rho_sbt_pE_s\varepsilon_0
\left(D-\frac{C_m}{4}\right)
=
\boxed{28.613729\ {\rm kN}}.
\]

中面单层两方向钢筋广义功：

\[
R_{q,s}
=
\rho_st_pE_s\pi^2(q_0+q)b\ell
\left[
\frac{\varepsilon_0D(\nu-1)}4
+
\frac{9\pi^2}{32}
\left(q_0q+\frac12q^2\right)
\right].
\]

所以

\[
R_{q,s}
=
\boxed{-289.268074\ {\rm kN\,mm}}.
\]

连续应变证书：

\[
\boxed{
\max|\varepsilon_s|=0.001635091<\varepsilon_y=0.00265
}.
\]

因此最终钢筋支为弹性支。

---

# 17. 联立 \(R_q=0,L=0\)

\[
P=P_c+P_s
=336.994047+28.613729
=
\boxed{365.607776\ {\rm kN}}.
\]

\[
R_q
=R_{q,c}+R_{q,s}
=
\boxed{1.315371e-02\ {\rm kN\,mm}}.
\]

\[
\frac{|R_q|}
{|R_{q,c}|+|R_{q,s}|}
=
\boxed{2.273568e-05}.
\]

同一系数表达采用方向自动微分：

\[
P_{,D}=\boxed{144.713767326},
\quad
P_{,q}=\boxed{-79494.930315266},
\]

\[
R_{q,D}=\boxed{-1865.424753305},
\quad
R_{q,q}=\boxed{1024243.336025845}.
\]

\[
L
=
P_{,D}R_{q,q}
-
P_{,q}R_{q,D}
=
\boxed{-69698.957493}.
\]

采用

\[
L_{norm}
=
\frac{L}
{|P_{,D}R_{q,q}|+|P_{,q}R_{q,D}|}
\]

得到

\[
\boxed{
L_{norm}=-2.350613e-04
}.
\]

沿平衡支

\[
\left.\frac{dP}{dD}\right|_{R_q=0}
=
P_{,D}
-
P_{,q}
\frac{R_{q,D}}{R_{q,q}}
=
\boxed{-0.068049}.
\]

因此本次 fresh closure 报告

\[
\boxed{
D_u\approx0.78234,\qquad
q_u\approx0.00177047
},
\]

\[
\boxed{
P_{u,th}\approx365.61\ {\rm kN}
}.
\]

鉴于极限点处 \(R_{q,c}\) 与 \(R_{q,s}\) 是两个约 \(289\ {\rm kN\,mm}\) 的大数相消，最终结果按 \(0.1\ {\rm kN}\) 精度解释，不赋予更多无意义有效数字。

---

# 18. 所有理论量冻结以后，才读取试验值

Swartz Case21：

\[
P_{f,exp}
=
82.8\ {\rm kip}
=
\boxed{368.312750\ {\rm kN}}.
\]

理论：

\[
P_{u,th}
=
365.607776\ {\rm kN}.
\]

\[
\frac{P_{u,th}}{P_{f,exp}}
=
\boxed{0.992655769}.
\]

\[
P_{u,th}-P_{f,exp}
=
\boxed{-2.704974\ {\rm kN}}.
\]

\[
\boxed{
\text{signed error}=-0.734423\%
}.
\]

本节不列任何历史 Case21 计算值。

---

# 19. 本次计算闭合判定

```text
SOURCE INPUT = PASS
R10 = PASS
N48-C1 U/C/T7 = PASS
N48-C1 CONSTRAINED-MINIMAX T = PASS
STRICT C1 ANCHORS = PASS
CONTINUOUS COMPILER DOMAIN = PASS
CAYLEY-HAMILTON = PASS
FORMAL SPATIAL QUADRATURE = 0
D15 MOMENT CLOSURE = PASS
STEEL BRANCH = ELASTIC
Rq=0 = PASS_ENGINEERING
L=0 = PASS_ENGINEERING
HISTORICAL CASE21 COMPUTED VALUE USED = NO
HISTORICAL GAUSS HISTORY USED = NO
EXPERIMENT USED DURING SOLVE = NO
FINAL COMPARISON = EXPERIMENT ONLY
```
