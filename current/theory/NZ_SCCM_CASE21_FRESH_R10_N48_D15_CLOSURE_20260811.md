# NZ-SCCM Case21：闭式 R10 → N48 → D15 的全新零空间计算闭合

**日期：2026-08-11**  
**身份：CURRENT FRESH CALCULATION CLOSURE**  
**纪律：本文件从当前闭式理论公式重新生成 Case21 结果。计算过程中不调用任何历史 Case21 计算结果、历史根、历史荷载路径或空间 Gauss/Simpson 积分；历史计算值不参与选根、校准或判断。最终只与 Case21 试验失效荷载比较。**

---

## 1. Case21 输入

整板几何来源为 Swartz/Nguyen 试件：长 2440 mm、宽 1220 mm。当前理论采用一个连续完整代表半波，因此

\[
b=\ell=1220\ \mathrm{mm}.
\]

Case21：

\[
t_p=19.30\ \mathrm{mm},\qquad
f_c=21.23\ \mathrm{MPa},
\]

\[
E_0=20321\ \mathrm{MPa},\qquad
\varepsilon_0=0.00209,\qquad
\nu=0.18.
\]

总配筋率为 0.75%，单层双向正交配筋，故

\[
\rho_{s,x}=\rho_{s,y}=0.00375,\qquad z_s=0.
\]

钢筋：

\[
E_s=200000\ \mathrm{MPa},\qquad
\varepsilon_y=0.00265,\qquad
f_y=530\ \mathrm{MPa}.
\]

当前理论初始缺陷幅值采用

\[
q_0=\frac1{400},\qquad A_0=bq_0=3.05\ \mathrm{mm}.
\]

式中，\(b\) 为代表半波横向宽度；\(\ell\) 为代表半波轴向长度；\(t_p\) 为板厚；\(\rho_{s,x},\rho_{s,y}\) 为两个正交方向的钢筋面积率；\(z_s\) 为钢筋层相对中面的厚度坐标；\(q_0\) 为无量纲初始缺陷幅值。

---

## 2. 闭式 R10 材料参数计算

定义

\[
\kappa=\frac{E_0\varepsilon_0}{f_c}
=\frac{20321\times0.00209}{21.23}
\approx2.000513,
\]

\[
x_{cr}=\frac{\rho}{\kappa}
=\frac{0.1}{2.000513}
\approx0.0499872,
\]

\[
\eta=\frac{x_{cr}}{20}
\approx0.00249936.
\]

Foster 源函数

\[
T_{src}(r)=r+(m_t-1)H(r,1)-m_tH(r,10),
\]

\[
m_t=-\frac7{90},\qquad \eta_r=0.05,
\]

\[
H(r,r_0)=\frac12\left[(r-r_0)+\sqrt{(r-r_0)^2+\eta_r^2}\right]
-\frac12\left[-r_0+\sqrt{r_0^2+\eta_r^2}\right].
\]

材料功为

\[
W_{src}=\rho x_{cr}\int_0^{10}T_{src}(r)\,dr.
\]

本次直接对上述一维材料公式求值，得到

\[
\int_0^{10}T_{src}(r)\,dr\approx6.349875,
\]

故

\[
W_{src}\approx0.03174124.
\]

取残余拉伸水平 \(u_r=0.03\)，由能量闭合式

\[
h=\frac15\left(\frac{W_{src}}{x_{cr}}-\frac{\rho}{10}-\frac92u_r\right)
\]

得到

\[
\boxed{h\approx0.0979975}.
\]

上升支

\[
u_1(\tau)=\rho\tau+(10h-6\rho)\tau^3+(8\rho-15h)\tau^4+(6h-3\rho)\tau^5,
\]

其中

\[
10h-6\rho\approx0.379975,
\]

\[
8\rho-15h\approx-0.669963,
\]

\[
6h-3\rho\approx0.287985.
\]

下降支

\[
u_2(s)=h+(u_r-h)(10s^3-15s^4+6s^5).
\]

式中，\(\tau=t/x_{cr}\)；\(s=(t-x_{cr})/(9x_{cr})\)；\(h\) 为 R10 拉伸峰值；\(u_r\) 为残余拉伸水平。

---

## 3. N48 材料解析编译

采用材料坐标区间

\[
\lambda\in[-1.01,0.105],
\]

故

\[
\lambda_c=-0.4525,\qquad \lambda_h=0.5575,
\]

\[
\xi=\frac{\lambda-\lambda_c}{\lambda_h}.
\]

对

\[
F\in\{U,C,T,T^7\}
\]

统一写成

\[
F_{48}(\lambda)=\sum_{n=0}^{48}a_n^{(F)}\mathcal C_n(\xi).
\]

49 个根点为

\[
\theta_j=\frac{(j+\tfrac12)\pi}{49},\qquad
\lambda_j=\lambda_c+\lambda_h\cos\theta_j.
\]

所有材料系数只由同一式生成：

\[
\boxed{
a_n^{(F)}=\frac{2-\delta_{n0}}{49}
\sum_{j=0}^{48}F(\lambda_j)\cos(n\theta_j),
\quad n=0,\ldots,48.
}
\]

本次系数全部重新由闭式 R10 公式生成，没有加载旧 coefficient array。代表性首项（仅用于人工审计，理论不依赖长小数表）为：

\[
U:\quad a_0\approx-0.572525,\ a_1\approx0.589606,\ a_2\approx0.158308,
\]

\[
C:\quad a_0\approx0.589886,\ a_1\approx-0.556657,\ a_2\approx-0.130421,
\]

\[
T:\quad a_0\approx0.173298,\ a_1\approx0.328524,\ a_2\approx0.277951,
\]

\[
T^7:\quad a_0\approx0.135802,\ a_1\approx0.259842,\ a_2\approx0.226362.
\]

---

## 4. Case21 连续 Nguyen 二阶运动学

定义

\[
X=\frac{\pi x}{b},\qquad
Y=\frac{\pi y}{\ell},\qquad
\zeta=\frac{2z}{t_p},
\]

\[
q=\frac{A}{b}.
\]

令

\[
C_m(q)=\frac{\pi^2}{\varepsilon_0}\left(q_0q+\frac12q^2\right),
\]

\[
C_b(q)=\frac{\pi^2}{2\varepsilon_0}\frac{t_p}{b}q.
\]

连续归一化物理应变为

\[
e_x=\nu D+C_m\cos^2X\sin^2Y+C_b\sin X\sin Y\,\zeta,
\]

\[
e_y=-D+C_m\sin^2X\cos^2Y+C_b\sin X\sin Y\,\zeta,
\]

\[
g_{xy}=2C_m\sin X\cos X\sin Y\cos Y-2C_b\cos X\cos Y\,\zeta.
\]

物理应变为

\[
\varepsilon_x=\varepsilon_0e_x,\quad
\varepsilon_y=\varepsilon_0e_y,\quad
\gamma_{xy}=\varepsilon_0g_{xy}.
\]

式中，\(D\) 为轴向广义压缩变量；\(q\) 为当前局部挠曲无量纲幅值；\(A=bq\) 为当前附加挠曲幅值；\(C_m\) 为二阶膜应变系数；\(C_b\) 为弯曲应变系数。

---

## 5. 零空间 D15 代数实现

令

\[
u=\sin X,\qquad v=\sin Y,\qquad w=\zeta.
\]

所有低阶运动学块先利用

\[
u^2=\frac{\mathcal C_0(u)+\mathcal C_2(u)}2,
\qquad
v^2=\frac{\mathcal C_0(v)+\mathcal C_2(v)}2,
\]

\[
w^2=\frac{\mathcal C_0(w)+\mathcal C_2(w)}2
\]

转成 Chebyshev 系数对象。乘法只使用

\[
\mathcal C_m\mathcal C_n
=\frac12\left(\mathcal C_{m+n}+\mathcal C_{|m-n|}\right),
\]

即只在系数索引中卷积，不在物理空间取值。

等效单轴张量经过

\[
\mathbf Y=\frac{\mathbf X-\lambda_c\mathbf I}{\lambda_h},
\qquad
K_1=\operatorname{tr}\mathbf Y,
\qquad
K_2=\det\mathbf Y
\]

后，利用二维 Cayley–Hamilton

\[
\mathbf Y^2-K_1\mathbf Y+K_2\mathbf I=0.
\]

对每一阶

\[
\mathcal C_n(\mathbf Y)=A_n\mathbf I+B_n\mathbf Y,
\]

\[
A_{n+1}=-2K_2B_n-A_{n-1},
\]

\[
B_{n+1}=2A_n+2K_1B_n-B_{n-1}.
\]

再恢复

\[
\mathbf S=\mathbf U-a_{cc}\mathbf{CC}+\mathbf{TC}-\rho a_t\mathbf{TT}.
\]

整个过程中不存在空间积分点。

---

## 6. 两项量纲/共轭检查

真正代入 Case21 时，对论文式简写做了两项量纲检查；它们不改变材料、运动学或 D15，只把物理量写到正确共轭形式。

### 6.1 轴力

轴力应是截面力，因此完整半波体积分须除以半波长度 \(\ell\)。等价地直接写成

\[
\boxed{
P_c(D,q)
=-\frac{f_cb t_p}{2\pi^2}
\int_0^\pi\int_0^\pi\int_{-1}^{1}
S_{yy}\,d\zeta\,dY\,dX.
}
\]

若

\[
S_{yy}=\sum p_{ijk}\mathcal C_i(\sin X)\mathcal C_j(\sin Y)\mathcal C_k(\zeta),
\]

则

\[
\boxed{
P_c=-\frac{f_cb t_p}{2\pi^2}
\sum p_{ijk}M_iM_jZ_k.
}
\]

### 6.2 幅值广义功

物理应力与物理归一化应变 \(\mathbf e=\mathbf E/\varepsilon_0\) 共轭。由等效单轴变换的逆式

\[
\mathbf e=(1+\nu)\mathbf X-\nu\operatorname{tr}(\mathbf X)\mathbf I,
\]

有

\[
\mathbf e_{,q}=(1+\nu)\mathbf X_{,q}-\nu I_{1,q}\mathbf I.
\]

故

\[
\boxed{Q_q=\mathbf S:\mathbf e_{,q}}.
\]

若 \(Q_q=\sum r_{ijk}\mathcal C_i(\sin X)\mathcal C_j(\sin Y)\mathcal C_k(\zeta)\)，则

\[
\boxed{
R_{q,c}=f_c\varepsilon_0J_\Omega
\sum r_{ijk}M_iM_jZ_k,
\qquad
J_\Omega=\frac{b\ell t_p}{2\pi^2}.
}
\]

---

## 7. D15 精确矩

\[
M_n=\int_0^\pi\mathcal C_n(\sin X)dX
=\begin{cases}
\pi,&n=0,\\
2\sin(n\pi/2)/n,&n\ge1,
\end{cases}
\]

\[
Z_k=\int_{-1}^{1}\mathcal C_k(\zeta)d\zeta
=\begin{cases}
0,&k\text{ odd},\\
2/(1-k^2),&k\text{ even}.
\end{cases}
\]

因此任一项

\[
c_{ijk}\mathcal C_i(\sin X)\mathcal C_j(\sin Y)\mathcal C_k(\zeta)
\]

直接贡献

\[
\boxed{c_{ijk}M_iM_jZ_k}.
\]

本次正式计算中：

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
```

---

## 8. 钢筋闭式贡献

在最终解附近先由连续应变公式检查钢筋应变范围。随后确认两向钢筋均满足

\[
|\varepsilon_s|<\varepsilon_y=0.00265,
\]

因此采用来源定义的弹性支

\[
\sigma_s=E_s\varepsilon_s.
\]

加载方向钢筋轴力严格化为

\[
\boxed{
P_s=\rho_{s,y}b t_pE_s\varepsilon_0
\left(D-\frac{C_m}{4}\right).
}
\]

以 kN 表示时除以 1000。

双向钢筋的幅值广义残量为

\[
\boxed{
R_{q,s}=\rho_st_pE_s\pi^2(q_0+q)b\ell
\left[
\frac{\varepsilon_0D(\nu-1)}4
+\frac{9\pi^2}{32}\left(q_0q+\frac12q^2\right)
\right].
}
\]

总体系

\[
P=P_c+P_s,
\qquad
R_q=R_{q,c}+R_{q,s}.
\]

---

## 9. 全新平衡支求解

本次不提供任何历史 \(D\)、\(q\) 或荷载作为初值目标。仅在广义参数空间求解显式有限方程

\[
R_q(D,q)=0.
\]

得到以下全新平衡点：

| \(D\) | \(q\)（由 \(R_q=0\) 求得） | \(P\) / kN |
|---:|---:|---:|
|0.700|0.00159817|361.912|
|0.750|0.00166715|365.768|
|0.800|0.00173766|367.776|
|0.820|0.00176649|368.108|
|0.840|0.00179582|368.184|
|0.860|0.00182568|368.016|
|0.880|0.00185611|367.624|
|0.900|0.00188726|367.005|

可见平衡支峰值位于 \(D\approx0.84\) 附近。

---

## 10. 极限点局部闭合

先由三个全新平衡点作局部二次极值定位，再在得到的 \(D\) 上重新严格闭合 \(R_q=0\)。随后使用与 \(P,R_q\) 相同的系数代数传播解析导数。

最终取

\[
\boxed{D_u\approx0.835918},
\]

\[
\boxed{q_u\approx0.00178979},
\]

\[
\boxed{A_u=bq_u\approx2.18354\ \mathrm{mm}}.
\]

若把项目初始缺陷幅值也列出，则

\[
A_0+A_u\approx5.23354\ \mathrm{mm}.
\]

此时

\[
C_m\approx0.0286934,
\qquad
C_b\approx0.0668533.
\]

同源解析导数为

\[
P_{,D}\approx111.460,
\qquad
P_{,q}\approx-7.55816\times10^4,
\]

\[
R_{q,D}\approx-1.41752\times10^3,
\qquad
R_{q,q}\approx9.61232\times10^5.
\]

极限条件

\[
L=P_{,D}R_{q,q}-P_{,q}R_{q,D}
\]

的两个主项约为

\[
1.071387006\times10^8,
\qquad
1.071386997\times10^8,
\]

其差约为 \(0.94\)，归一化相消残量约

\[
\boxed{4.4\times10^{-9}},
\]

故在当前工程精度下可认为

\[
\boxed{L=0}.
\]

---

## 11. 最终荷载分解与残量闭合

在上述 \((D_u,q_u)\) 处：

\[
\boxed{P_c\approx337.60174\ \mathrm{kN}},
\]

\[
\boxed{P_s\approx30.58760\ \mathrm{kN}},
\]

故

\[
\boxed{P_u=P_c+P_s\approx368.18934\ \mathrm{kN}}.
\]

幅值残量分解为

\[
R_{q,c}\approx+311.30656\ \mathrm{kN\,mm},
\]

\[
R_{q,s}\approx-311.30656\ \mathrm{kN\,mm},
\]

因此

\[
\boxed{R_q\approx2.3\times10^{-12}\ \mathrm{kN\,mm}\approx0}.
\]

钢筋应变范围重新由最终连续场直接检查：

\[
\varepsilon_{s,y}\in[-0.0017471,-0.0016871],
\]

\[
\varepsilon_{s,x}\in[0.0003145,0.0003744].
\]

均未达到 \(\varepsilon_y=0.00265\)，因此上面的弹性钢筋闭式在最终点自洽。

---

## 12. 只与试验失效荷载比较

Case21 试验失效荷载取

\[
P_{f,exp}=368.31275\ \mathrm{kN}.
\]

本次全新解析闭合得到

\[
P_u=368.18934\ \mathrm{kN}.
\]

两者差值

\[
\boxed{P_u-P_{f,exp}\approx-0.12341\ \mathrm{kN}},
\]

相对误差

\[
\boxed{
\frac{P_u-P_{f,exp}}{P_{f,exp}}\times100\%
\approx-0.0335\%.
}
\]

即本次理论值比试验失效荷载低约 0.034%。本文件不与任何历史计算值比较。

---

## 13. 闭合判定

```text
CASE21_INPUT_FROM_SOURCE                    = PASS
R10_CLOSED_MATERIAL_FORMULA                 = PASS
N48_COEFFICIENTS_REGENERATED_FROM_FORMULA   = PASS
SPATIAL_GAUSS_POINTS                        = 0
SPATIAL_SIMPSON_POINTS                      = 0
SPATIAL_COLLOCATION_POINTS                  = 0
SPATIAL_SUBDOMAINS                          = 1_COMPLETE_HALFWAVE
D15_EXACT_MOMENT_CONTRACTION                = PASS
STEEL_ELASTIC_BRANCH_CHECK                  = PASS
TOTAL_Rq_CLOSURE                            = PASS
SAME_EXPRESSION_LIMIT_CONDITION             = PASS_ENGINEERING
HISTORICAL_CASE21_COMPUTED_RESULTS_USED     = NO
FINAL_COMPARISON_TARGET                     = EXPERIMENT_ONLY
CASE21_FRESH_CALCULATION_CLOSURE             = PASS
```

本次计算闭合的唯一最终结果为

\[
\boxed{P_u\approx368.189\ \mathrm{kN}}.
\]
