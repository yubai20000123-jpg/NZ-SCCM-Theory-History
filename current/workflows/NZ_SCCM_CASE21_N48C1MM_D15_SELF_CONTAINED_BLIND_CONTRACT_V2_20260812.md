# NZ-SCCM Case21 N48-C1/MM + D15 自包含独立盲算合同 V2

**日期：2026-08-12**  
**用途：第二次空白聊天独立复算。**  
**本文件不提供 Case21 理论答案，不提供实验破坏荷载，不提供历史 Case21 根、荷载或路径。**

## 0. 隔离纪律

```text
只允许使用本文件
历史 Case21 D/q/Pu/root/path = 禁止
旧 direct-N48 Case21 结果 = 禁止
历史 FE/Gauss/Simpson 结果 = 禁止
实验荷载参与求解 = 禁止
正式空间 Gauss/Simpson/adaptive quadrature = 0
正式空间 Chebyshev collocation = 0
正式空间 material-point grid/cells = 0
```

一维 N48 材料坐标只用于生成/验证材料解析系数，不属于结构空间离散。如任何必要定义仍缺失，必须在首次缺口处 `BLOCKED`，不得从外部知识补齐。

---

## 1. Case21 原始输入

\[
b=\ell=1220\ {\rm mm},\qquad t_p=19.30\ {\rm mm}.
\]

\[
f_c=21.23\ {\rm MPa},\qquad E_0=20321\ {\rm MPa},\qquad \varepsilon_0=0.00209,\qquad \nu=0.18.
\]

\[
q_0=1/400=0.0025.
\]

总双向配筋率为 0.75%，两个方向均分：

\[
\rho_{s,x}=\rho_{s,y}=\rho_s=0.00375.
\]

Case21 为中面单层钢筋：

\[
z_s=0,\qquad \zeta_s=0.
\]

\[
E_s=200000\ {\rm MPa},\qquad \varepsilon_y=0.00265,\qquad f_y=530\ {\rm MPa}.
\]

R10 固定常数：

\[
\rho=0.1,\qquad m_t=-7/90,\qquad \eta_r=0.05,\qquad u_r=0.03,
\]

\[
a_{cc}=0.1072329249362415,\qquad a_t=1-2^{-1/8}.
\]

本次 compiler 区间在求解前固定：

\[
\boxed{\lambda\in[\lambda_a,\lambda_b]=[-1.15,0.12]}.
\]

该区间是盲算合同的先验输入，不允许根据理论答案或实验值调整。

---

## 2. R10 基本参数

\[
\boxed{\kappa=\frac{E_0\varepsilon_0}{f_c}},\qquad
\boxed{x_{cr}=\frac{\rho}{\kappa}},\qquad
\boxed{\eta=\frac{x_{cr}}{20}}.
\]

---

## 3. 平滑正部函数与压缩 primitive

对任意实数 \(z\)，

\[
\boxed{\Pi_\eta(z)=\frac{z^2\left(\sqrt{z^2+\eta^2}+z\right)}{2(z^2+\eta^2)}}.
\]

对任意主等效应变 \(\lambda\)，定义

\[
\boxed{c(\lambda)=\Pi_\eta(-\lambda)},\qquad
\boxed{t(\lambda)=\Pi_\eta(\lambda)}.
\]

压缩 primitive：

\[
\boxed{C(\lambda)=\frac{\kappa c(\lambda)}{1+(\kappa-2)c(\lambda)+c(\lambda)^2}}.
\]

---

## 4. Foster 源拉伸函数：完整定义

令

\[
r=t/x_{cr}.
\]

平滑铰函数：

\[
\boxed{H(r,r_0)=\frac12\left[(r-r_0)+\sqrt{(r-r_0)^2+\eta_r^2}\right]-\frac12\left[-r_0+\sqrt{r_0^2+\eta_r^2}\right]}.
\]

Foster 源拉伸利用函数：

\[
\boxed{T_{src}(r)=r+(m_t-1)H(r,1)-m_tH(r,10)}.
\]

源归一化拉应力：

\[
\boxed{u_{t,src}(t)=\rho\,T_{src}(t/x_{cr})}.
\]

源材料功：

\[
\boxed{W_{src}=\rho x_{cr}\int_0^{10}T_{src}(r)\,dr}.
\]

该积分是一维材料积分。必须由上述完整定义重新生成；允许符号积分、高精度一维材料积分或闭式原函数，不属于结构空间积分。

---

## 5. R10 拉伸 rise/fall/residual：完整定义

上升支局部坐标：

\[
\boxed{\tau(t)=t/x_{cr}}.
\]

当 \(0\le t\le x_{cr}\) 时，

\[
\boxed{u_1(t)=\rho\tau+(10h-6\rho)\tau^3+(8\rho-15h)\tau^4+(6h-3\rho)\tau^5},\qquad \tau=\tau(t).
\]

下降支局部坐标：

\[
\boxed{s(t)=\frac{t-x_{cr}}{9x_{cr}}}.
\]

当 \(x_{cr}<t\le10x_{cr}\) 时，

\[
\boxed{u_2(t)=h+(u_r-h)(10s^3-15s^4+6s^5)},\qquad s=s(t).
\]

R10 拉伸峰值由材料功闭合：

\[
\boxed{h=\frac15\left(\frac{W_{src}}{x_{cr}}-\frac{\rho}{10}-\frac92u_r\right)}.
\]

完整拉伸归一化应力：

\[
\boxed{u_{sm}(t)=\begin{cases}u_1(t),&0\le t\le x_{cr},\\u_2(t),&x_{cr}<t\le10x_{cr},\\u_r,&t>10x_{cr}.\end{cases}}
\]

因为 \(t(\lambda)=\Pi_\eta(\lambda)\ge0\)，不需要负 \(t\) 分支。

最终拉伸 primitive：

\[
\boxed{T(\lambda)=\frac{u_{sm}[t(\lambda)]}{\rho}}.
\]

独立七次 primitive：

\[
\boxed{T^{(7)}(\lambda)=[T(\lambda)]^7}.
\]

current master：

\[
\boxed{U(\lambda)=\kappa\lambda-C(\lambda)+\kappa c(\lambda)+\rho T(\lambda)-\kappa t(\lambda)}.
\]

---

## 6. R10 严格 C1 锚点

必须独立检查：

\[
\boxed{U(0)=0,\qquad U'(0)=\kappa},
\]

\[
\boxed{C(0)=T(0)=T^{(7)}(0)=0},
\]

\[
\boxed{C'(0)=T'(0)=(T^{(7)})'(0)=0}.
\]

撇号均表示对真实材料坐标 \(\lambda\) 求导。

---

## 7. direct N48

\[
\lambda_c=(\lambda_a+\lambda_b)/2,\qquad \lambda_h=(\lambda_b-\lambda_a)/2,
\]

\[
\boxed{\xi(\lambda)=(\lambda-\lambda_c)/\lambda_h}.
\]

第一类 Chebyshev 多项式：

\[
\boxed{\mathcal C_n(\xi)=\cos[n\arccos(\xi)]}.
\]

49 个材料根点：

\[
\boxed{\theta_j=(j+1/2)\pi/49},\qquad
\boxed{\lambda_j=\lambda_c+\lambda_h\cos\theta_j},\qquad j=0,\ldots,48.
\]

对 \(F\in\{U,C,T,T^{(7)}\}\)：

\[
\boxed{a_n^{(F,0)}=\frac{2-\delta_{n0}}{49}\sum_{j=0}^{48}F(\lambda_j)\cos(n\theta_j)},\qquad n=0,\ldots,48.
\]

---

## 8. N48-C1：H、G、dF 完整定义

定义 \(V_{jn}=\cos(n\theta_j)\)。则

\[
\boxed{\mathbf H=\mathbf V^T\mathbf V=\operatorname{diag}(49,49/2,\ldots,49/2)},
\]

\[
\boxed{\mathbf H^{-1}=\frac1{49}\operatorname{diag}(1,2,\ldots,2)}.
\]

零点标准坐标：

\[
\boxed{\xi_0=-\lambda_c/\lambda_h}.
\]

约束矩阵：

\[
\boxed{\mathbf G=\begin{bmatrix}\mathcal C_0(\xi_0)&\cdots&\mathcal C_{48}(\xi_0)\\\lambda_h^{-1}\mathcal C_0'(\xi_0)&\cdots&\lambda_h^{-1}\mathcal C_{48}'(\xi_0)\end{bmatrix}}.
\]

目标向量：

\[
\boxed{\mathbf d_U=[0,\kappa]^T},
\]

\[
\boxed{\mathbf d_C=\mathbf d_T=\mathbf d_{T^{(7)}}=[0,0]^T}.
\]

对 \(F\in\{U,C,T^{(7)}\}\)：

\[
\boxed{\mathbf a^{(F,C1)}=\mathbf a^{(F,0)}+\mathbf H^{-1}\mathbf G^T(\mathbf G\mathbf H^{-1}\mathbf G^T)^{-1}(\mathbf d_F-\mathbf G\mathbf a^{(F,0)})}.
\]

---

## 9. T strict-C1 constrained-minimax：确定性生产合同

理论目标：

\[
\boxed{\min_{\mathbf a\in\mathbb R^{49}}\left\|\sum_{n=0}^{48}a_n\mathcal C_n[\xi(\lambda)]-T_{R10}(\lambda)\right\|_{L^\infty([\lambda_a,\lambda_b])}}
\]

严格约束：

\[
\boxed{\mathbf G\mathbf a=\mathbf d_T}.
\]

以下材料坐标仅用于一维材料系数生成，不属于结构空间离散。

### 9.1 初始 exchange set

取 \(N_0=4096\)：

\[
\lambda_k^{(0)}=\lambda_c+\lambda_h\cos(k\pi/N_0),\qquad k=0,\ldots,N_0.
\]

另外强制加入 \(\lambda_a,\lambda_b,0\)，以及位于区间内的 \(\Pi_\eta(\lambda)=x_{cr}\) 和 \(\Pi_\eta(\lambda)=10x_{cr}\) 的正根。

### 9.2 每轮 LP

未知量为 \((a_0,\ldots,a_{48},E)\)。求

\[
\boxed{\min E}
\]

并对 exchange set 中每个 \(\lambda_k\) 施加

\[
-E\le\sum_{n=0}^{48}a_n\mathcal C_n[\xi(\lambda_k)]-T_{R10}(\lambda_k)\le E,
\]

以及 \(\mathbf G\mathbf a=\mathbf d_T\)。

若用 SciPy，指定 `scipy.optimize.linprog(method="highs")`。

### 9.3 verification set 与 exchange

取 \(N_v=131072\)：

\[
\lambda_m^{(v)}=\lambda_c+\lambda_h\cos(m\pi/N_v),\qquad m=0,\ldots,N_v.
\]

加入 9.1 的全部特殊材料点。令

\[
r(\lambda)=T_{48}(\lambda)-T_{R10}(\lambda).
\]

在 verification set 上找全部离散局部极值候选；对每个候选的相邻材料区间，用 bounded scalar minimization 对 \(-|r(\lambda)|\) 做局部精化。

若最大违反点满足

\[
|r(\lambda_*)|>E+10^{-10},
\]

把该点加入 exchange set 后重解 LP。

### 9.4 停止条件

以下两项连续两轮同时满足即停止：

\[
\max|r|-E\le10^{-10},
\]

\[
\max_n|a_n^{(k)}-a_n^{(k-1)}|\le10^{-12}.
\]

最多 50 轮；否则 `BLOCKED_AT_T_MINIMAX`。最终还必须满足

\[
|T_{48}(0)|\le10^{-12},\qquad |T'_{48}(0)|\le10^{-12}.
\]

并报告最终材料验证误差 \(E_\infty=\max|r|\)。这是工程可重复系数合同，不宣称 theorem-level 连续余项证书。

---

## 10. 最终四个 N48 primitive

\[
\mathbf a^{(F,*)}=\begin{cases}\mathbf a^{(F,C1)},&F\in\{U,C,T^{(7)}\},\\\mathbf a^{(T,MM)},&F=T.\end{cases}
\]

\[
\boxed{F_{48}(\lambda)=\sum_{n=0}^{48}a_n^{(F,*)}\mathcal C_n[\xi(\lambda)]}.
\]

独立复算必须输出完整 49×4 系数表，不得从历史文件读取。

---

## 11. 二维等效应变 current-map

物理面内应变张量：

\[
\mathbf E=\begin{bmatrix}\varepsilon_x&\gamma_{xy}/2\\\gamma_{xy}/2&\varepsilon_y\end{bmatrix}.
\]

\[
\boxed{\mathbf E_u=\frac{(1-\nu)\mathbf E+\nu\,\operatorname{tr}(\mathbf E)\mathbf I}{1-\nu^2}},\qquad
\boxed{\mathbf X=\mathbf E_u/\varepsilon_0}.
\]

\[
X_{11}=\frac{\varepsilon_x+\nu\varepsilon_y}{(1-\nu^2)\varepsilon_0},\qquad
X_{22}=\frac{\nu\varepsilon_x+\varepsilon_y}{(1-\nu^2)\varepsilon_0},
\]

\[
X_{12}=\frac{\gamma_{xy}}{2(1+\nu)\varepsilon_0}.
\]

---

## 12. Cayley–Hamilton 二维提升

\[
\boxed{\mathbf Y=(\mathbf X-\lambda_c\mathbf I)/\lambda_h},\qquad K_1=\operatorname{tr}\mathbf Y,\qquad K_2=\det\mathbf Y.
\]

\[
\mathbf Y^2-K_1\mathbf Y+K_2\mathbf I=0.
\]

\[
\boxed{\mathcal C_n(\mathbf Y)=A_n\mathbf I+B_n\mathbf Y}.
\]

初值：\(A_0=1,B_0=0,A_1=0,B_1=1\)。递推：

\[
\boxed{A_{n+1}=-2K_2B_n-A_{n-1}},
\]

\[
\boxed{B_{n+1}=2A_n+2K_1B_n-B_{n-1}}.
\]

从而

\[
\mathbf F_{48}=\sum_{n=0}^{48}a_n^{(F,*)}(A_n\mathbf I+B_n\mathbf Y),
\]

分别得到 \(\mathbf U,\mathbf C,\mathbf T,\mathbf T^{(7)}\)。

---

## 13. 二维应力张量

\[
\boxed{\mathbf{CC}=\det(\mathbf C)\mathbf C},
\]

\[
\boxed{\mathbf{TC}=\mathbf C[\operatorname{tr}(\mathbf T)\mathbf I-\mathbf T]},
\]

\[
\boxed{\mathbf{TT}=\det(\mathbf T)[\operatorname{tr}(\mathbf T^{(7)})\mathbf I-\mathbf T^{(7)}]}.
\]

\[
\boxed{\mathbf S=\mathbf U-a_{cc}\mathbf{CC}+\mathbf{TC}-\rho a_t\mathbf{TT}},\qquad
\boxed{\boldsymbol\sigma=f_c\mathbf S}.
\]

---

## 14. Nguyen 一个连续完整方形半波

\[
X=\pi x/b,\qquad Y=\pi y/\ell,\qquad \zeta=2z/t_p.
\]

\[
w_0=A_0\sin X\sin Y,\qquad w_1=A\sin X\sin Y,
\]

\[
q_0=A_0/b,\qquad q=A/b.
\]

\[
\boxed{C_m=\frac{\pi^2}{\varepsilon_0}(q_0q+q^2/2)},\qquad
\boxed{C_b=\frac{\pi^2}{2\varepsilon_0}\frac{t_p}{b}q}.
\]

归一化物理应变：

\[
\boxed{e_x=\nu D+C_m\cos^2X\sin^2Y+C_b\sin X\sin Y\,\zeta},
\]

\[
\boxed{e_y=-D+C_m\sin^2X\cos^2Y+C_b\sin X\sin Y\,\zeta},
\]

\[
\boxed{g_{xy}=2C_m\sin X\cos X\sin Y\cos Y-2C_b\cos X\cos Y\,\zeta}.
\]

\[
\varepsilon_x=\varepsilon_0e_x,\qquad \varepsilon_y=\varepsilon_0e_y,\qquad \gamma_{xy}=\varepsilon_0g_{xy}.
\]

未知量只有 \(D,q\)。

---

## 15. D15 精确矩合同

任何待积量必须先化为

\[
\boxed{Q(X,Y,\zeta)=\sum_{i,j,k}c_{ijk}\mathcal C_i(\sin X)\mathcal C_j(\sin Y)\mathcal C_k(\zeta)}.
\]

\[
\boxed{M_n=\begin{cases}\pi,&n=0,\\2\sin(n\pi/2)/n,&n\ge1,\end{cases}}
\]

\[
\boxed{Z_k=\begin{cases}0,&k\text{ odd},\\2/(1-k^2),&k\text{ even}.\end{cases}}
\]

\[
\boxed{\mathscr D[Q]=\sum_{i,j,k}c_{ijk}M_iM_jZ_k}.
\]

允许有限解析幂基/三角基/FFT **系数卷积**加速代数，但禁止在物理空间取样；任何后端最终必须等价于上述有限矩收缩。

---

## 16. 混凝土轴力与幅值残量

\[
\boxed{P_c=-\frac{f_cbt_p}{2\pi^2}\mathscr D[S_{yy}]}.
\]

定义 \(\mathbf e=\mathbf E/\varepsilon_0\)，等价地

\[
\boxed{\mathbf e=(1+\nu)\mathbf X-\nu\operatorname{tr}(\mathbf X)\mathbf I}.
\]

\[
\boxed{Q_q=\mathbf S:\frac{\partial\mathbf e}{\partial q}},\qquad
\boxed{J_\Omega=\frac{b\ell t_p}{2\pi^2}},
\]

\[
\boxed{R_{q,c}=f_c\varepsilon_0J_\Omega\mathscr D[Q_q]}.
\]

---

## 17. Case21 中面单层钢筋解析式

弹性支下：

\[
\boxed{P_s=\rho_sbt_pE_s\varepsilon_0\left(D-\frac{C_m}{4}\right)}.
\]

\[
\boxed{R_{q,s}=\rho_st_pE_s\pi^2(q_0+q)b\ell\left[\frac{\varepsilon_0D(\nu-1)}4+\frac{9\pi^2}{32}\left(q_0q+\frac12q^2\right)\right]}.
\]

最终必须独立证明全域钢筋应变满足

\[
\max|\varepsilon_s|<\varepsilon_y.
\]

若不满足，本合同没有塑性钢筋支的生产定义，必须 `BLOCKED_AT_STEEL_BRANCH`，不得自行创造塑性公式。

---

## 18. 总平衡与极限条件

\[
\boxed{P(D,q)=P_c(D,q)+P_s(D,q)},
\]

\[
\boxed{R_q(D,q)=R_{q,c}(D,q)+R_{q,s}(D,q)}.
\]

平衡：

\[
\boxed{R_q(D,q)=0}.
\]

同源导数：

\[
P_{,D}=\partial P/\partial D,\qquad P_{,q}=\partial P/\partial q,
\]

\[
R_{q,D}=\partial R_q/\partial D,\qquad R_{q,q}=\partial R_q/\partial q.
\]

生产导数只能由同一有限解析表达解析求导或 forward AD。若使用 forward AD，每个标量携带 \((x,x_{,D},x_{,q})\)，按乘积、商和链式法则传播；禁止有限差分生产导数。

极限函数：

\[
\boxed{L(D,q)=P_{,D}R_{q,q}-P_{,q}R_{q,D}}.
\]

最终联立

\[
\boxed{R_q(D,q)=0,\qquad L(D,q)=0}
\]

得到 fresh 理论 \(D_u,q_u,P_u\)。

---

## 19. 连续 compiler-domain 证书

最终状态必须证明整个连续完整半波满足

\[
\boxed{-1.15\le\lambda_-(X,Y,\zeta)\le\lambda_+(X,Y,\zeta)\le0.12}.
\]

不得用有限物理空间点扫描作为正式证书。允许：continuous algebraic invariant bound、single-domain Bernstein coefficient envelope 或其他全局有效解析界。若无法在单一完整半波上给出全域证书，必须 `BLOCKED_AT_CONTINUOUS_SPECTRAL_CERTIFICATE`，不得用 spatial cells/subdomains/collocation 补救。

---

## 20. 独立复算必须输出

1. \(\kappa,x_{cr},\eta\)；
2. \(H,T_{src},W_{src},h\) 的重新生成；
3. \(U,C,T,T^7\)；
4. 完整 49×4 N48-C1/MM 系数；
5. 全部严格 C1 锚点残量；
6. T-minimax exchange 轮数和最终 \(E_\infty\)；
7. \(D,q,A,C_m,C_b\)；
8. 连续 compiler-domain 证书；
9. \(\mathscr D[S_{yy}]\)、\(\mathscr D[Q_q]\)；
10. \(P_c,P_s,P\)；
11. \(R_{q,c},R_{q,s},R_q\)；
12. \(P_{,D},P_{,q},R_{q,D},R_{q,q}\)；
13. \(L\) 与归一化 \(L\)；
14. 连续钢筋应变证书；
15. `PASS / FAIL / BLOCKED` 及首次分歧层级。

理论 \(D_u,q_u,P_u\) 冻结后立即停止。**不得自行寻找实验值。**
