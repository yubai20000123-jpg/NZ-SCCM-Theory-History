> **GitHub migration note (2026-08-10):** This is a full-text normalized mirror of the local historical artifact. The local source SHA-256 is `1b045d3a248564d69bd063a765bd5a757d3c42db8b918a71c638e8179e50f655`. Five historical form-feed corruption sequences preceding `rac` were normalized to LaTeX `\frac`. Therefore this GitHub text is not claimed byte-exact; the original SHA remains authoritative for byte identity.

# NZ-SCCM Case21 完整显式代数积分：零空间采样有限解析级数求解结果

**日期：2026-08-09**  
**理论合同：** `NZ_SCCM_CURRENT_OPERATOR_EXPLICIT_NC_REBAR_V1_20260809.md`  
**exact 输入：** `fP_alg_sympy.txt`、`fR_alg_sympy.txt`  
**本轮正式空间采样数：** `0`  
**本轮正式空间 quadrature 点数：** `0`

> **最终状态：** `ZERO_SPATIAL_ANALYTIC_SERIES_SOLUTION_OBTAINED / TIGHT_STRICT_CERTIFICATE_UNRESOLVED`。
>
> 本轮已经完全移除 3D Chebyshev-Lobatto、DCT、Gauss、Simpson、adaptive spatial quadrature、material-point grid 和 panel-level fitted surrogate。Concrete-only 与 RC Case21 均由“原始显式 algebraic current operator → 有限解析 Taylor/binomial recurrence → 单项闭式矩积分 → 参数空间求根”重新得到。当前仍未关闭的是**足够紧且经严格 interval/ball 机器认证的全局截断误差证书**；现有解析余项传播有显式上界，但过度保守，不能据此证明下文全部小数位。

---

## 1. Theory contract check

冻结 ordinary-concrete current operator 原样采用：

\[
(\varepsilon_x,\varepsilon_y,\gamma_{xy})
\to(X_{11},X_{22},X_{12})
\to(\lambda_+,\lambda_-)
\to(c_\pm,t_\pm)
\to(C_\pm,T_\pm,U_\pm)
\to(s_+,s_-)
\to(\sigma_x,\sigma_y,\tau_{xy}).
\]

正式 tension law 为 Foster 代数平滑：

\[
H(r,r_0)=\frac12\left[(r-r_0)+\sqrt{(r-r_0)^2+0.05^2}\right]
-\frac12\left[-r_0+\sqrt{r_0^2+0.05^2}\right].
\]

没有使用 `tanh` 双 sigmoid。

Case21：

\[
f_c=21.23\ \mathrm{MPa},\quad E_0=20321\ \mathrm{MPa},\quad
\varepsilon_0=0.00209,\quad \nu=0.18,
\]

\[
b=\ell=1220\ \mathrm{mm},\quad t=19.30\ \mathrm{mm},\quad
q_0=\frac1{400}.
\]

exact 输入 SHA-256：

```text
fP_alg_sympy.txt
6486b8d8d7e21daf453cc3f70c04de89f03d3c20f5b346f9cd17e5bb4151e5a4

fR_alg_sympy.txt
0d07af9d6abecaa658266206ba6979d6b8b7c891f7a636f02d164560a48b7d2e

frozen MD
98483fa75e828f57916b06fc708fc35fc7960fabbdebf4edb3e04aba10061bc6
```

因此本轮不是重建材料 surrogate，而是直接处理已冻结的 exact structural integrands。

---

# 2. 从 tangent-half-angle exact integrand 压缩 11 个 radical

## 2.1 原始 exact integrand

上一阶段 tangent-half-angle：

\[
u=\tan\frac X2,\qquad v=\tan\frac Y2,
\]

\[
\sin X=\frac{2u}{1+u^2},\quad
\cos X=\frac{1-u^2}{1+u^2},
\]

\[
\sin Y=\frac{2v}{1+v^2},\quad
\cos Y=\frac{1-v^2}{1+v^2},
\]

\[
dX\,dY=\frac{4\,du\,dv}{(1+u^2)(1+v^2)}.
\]

所以：

\[
f_{P,\mathrm{alg}}=\sigma_y\frac{4}{(1+u^2)(1+v^2)},
\]

\[
f_{R,\mathrm{alg}}
=(\sigma_xe_{x,q}+\sigma_ye_{y,q}+\tau_{xy}g_{xy,q})
\frac{4}{(1+u^2)(1+v^2)}.
\]

当前 SymPy 表示中：

- `fP_alg`: 64,682 operations；
- `fR_alg`: 161,886 operations；
- `fP_alg` textual unique square roots: 11。

operation 数与上一阶段报告中的 58,452 / 146,231 略有变化仅来自 SymPy 当前 expression representation；exact 文件 SHA-256 未改变。

## 2.2 11 个 textual radicals 的真正生成元

文本中 11 个 `sqrt` 可压缩为：

### coefficient field 中的常数根式

\[
K_1=\sqrt{1+0.05^2}=\frac{\sqrt{401}}{20},
\]

\[
K_{10}=\sqrt{100+0.05^2}=\frac{\sqrt{40001}}{20},
\]

以及

\[
s=2^{1/8},\qquad s^8-2=0,
\]

因为 \(a_t=1-s^{-1}\)。

### 7 个随 \(\zeta\) 变化的生成元

\[
R^2-(\delta^2+X_{12}^2)=0,
\]

\[
A_\pm^2-(\lambda_\pm^2+\eta^2)=0,
\]

\[
B_{\pm,1}^2-
\left[\left(\frac{t_\pm}{x_{cr}}-1\right)^2+\eta_r^2\right]=0,
\]

\[
B_{\pm,10}^2-
\left[\left(\frac{t_\pm}{x_{cr}}-10\right)^2+\eta_r^2\right]=0.
\]

注意：文本中正负写法导致 \(\sqrt{(-\lambda)^2+\eta^2}\) 和
\(\sqrt{\lambda^2+\eta^2}\) 重复出现，但数学上是同一个 \(A_\pm\)。

## 2.3 嵌套依赖

生成元不是七个互不相干的平方根：

\[
R\to\lambda_\pm=\mu\pm R,
\]

\[
\lambda_\pm\to A_\pm\to(c_\pm,t_\pm),
\]

\[
t_\pm\to B_{\pm,1},B_{\pm,10}.
\]

因此它是一个**嵌套 algebraic extension tower**。若七个 quadratic extensions generic 独立，粗上界为：

\[
[\mathcal K:\mathcal K_0]\le 2^7=128.
\]

后文把 spectral root \(R\) rationalize 后，上界降为 \(2^6=64\)。

---

# 3. Case21 关于 \(\zeta\) 的真正低阶 algebraic 骨架

冻结运动学可精确整理成：

\[
\mu=a_0+a_1\zeta,
\]

\[
\delta=\delta_0,
\]

\[
X_{12}=b_0+b_1\zeta.
\]

于是：

\[
R^2=\delta_0^2+(b_0+b_1\zeta)^2,
\]

关于 \(\zeta\) 仅为二次根式。这是本轮 algebraic compression 的首要结构，而不是把 60 万字符表达式整体 expand。

还有两个 exact simplifications 很重要。

## 3.1 Smooth positive/negative coordinates 的共享根式

令

\[
A=\sqrt{\lambda^2+\eta^2}.
\]

则

\[
c=\frac{\lambda^2(A-\lambda)}{2A^2},\qquad
 t=\frac{\lambda^2(A+\lambda)}{2A^2}.
\]

因此：

\[
t-c=\frac{\lambda^3}{\lambda^2+\eta^2}.
\]

冻结的

\[
U=\kappa\lambda-C+\kappa c+\rho T-\kappa t
\]

可以原样代数化简为：

\[
\boxed{
U=-C+\rho T+\frac{\kappa\lambda\eta^2}{\lambda^2+\eta^2}
}.
\]

这不是改材料关系，而是同一函数的恒等变形。

## 3.2 Foster H 的重复项压缩

\[
H(r,a)=\frac12\left[r+\sqrt{(r-a)^2+\eta_r^2}
-\sqrt{a^2+\eta_r^2}\right].
\]

使用 \(m_t=-7/90\)：

\[
\boxed{
T=\frac12r-\frac{97}{180}(B_1-K_1)
+\frac7{180}(B_{10}-K_{10})
}.
\]

因此每个 principal direction 只需两个 Foster variable radicals，而不是多次展开同一根式。

---

# 4. Spectral radical 的 exact rationalization

为了避免把第一个二次 radical 带进后续全部层级，做一个精确变量整理。

先在后面的 quadrant-sine 表示中定义：

\[
w=C_b\zeta-C_mab,
\]

\[
\mu=\mu_0+\gamma w,
\qquad
\gamma=\frac{ab}{1-\nu},
\]

\[
X_{12}=-k_sw,
\qquad
k_s=\frac{\sqrt{(1-a^2)(1-b^2)}}{1+\nu}.
\]

所以：

\[
R=\sqrt{\delta^2+k_s^2w^2}.
\]

在 Case21 physical peak branch 上 \(\delta>0\)，采用 Euler parameter：

\[
\theta=\frac{k_sw+R}{\delta}.
\]

则：

\[
w=\frac{\delta}{2k_s}(\theta-\theta^{-1}),
\]

\[
R=\frac\delta2(\theta+\theta^{-1}),
\]

\[
dw=\frac\delta{2k_s}(1+\theta^{-2})d\theta.
\]

于是 principal values 变成 Laurent-rational：

\[
\lambda_+=\mu_0+\frac\delta2
\left[
\left(1+\frac\gamma{k_s}\right)\theta
+\left(1-\frac\gamma{k_s}\right)\theta^{-1}
\right],
\]

\[
\lambda_-=\mu_0+\frac\delta2
\left[
\left(\frac\gamma{k_s}-1\right)\theta
-\left(\frac\gamma{k_s}+1\right)\theta^{-1}
\right].
\]

因此 spectral root 已完全消失。

---

# 5. 为什么剩余 exact \(\zeta\) primitive generic 不是 elementary / elliptic

这是本轮能够精确定位的真实数学阻断项。

对任一 principal \(\lambda\)，再次 rationalize smooth coordinate：

\[
y=\frac{\sqrt{\lambda^2+\eta^2}+\lambda}{\eta}.
\]

则：

\[
\lambda=\frac\eta2(y-y^{-1}),
\qquad
A=\frac\eta2(y+y^{-1}).
\]

进一步：

\[
c=\frac{\eta (y^2-1)^2}{2y(y^2+1)^2},
\]

\[
t=\frac{\eta y(y^2-1)^2}{2(y^2+1)^2}.
\]

因 \(\eta=x_{cr}/20\)：

\[
\boxed{
\frac{t}{x_{cr}}
=\frac{y(y^2-1)^2}{40(y^2+1)^2}
}.
\]

因此 Foster radical \(B_{r_0}\) 可写成一个 degree-10 hyperelliptic radical：

\[
B_{r_0}
=
\frac{\sqrt{G_{r_0}(y)}}{40(y^2+1)^2},
\]

其中

\[
G_{r_0}(y)=
\left[y(y^2-1)^2-40r_0(y^2+1)^2\right]^2
+4(y^2+1)^4.
\]

对于 \(r_0=1\)：

\[
\begin{aligned}
G_1(y)=&\ y^{10}-80y^9+1600y^8+6422y^6+160y^5\\
&+9620y^4+6417y^2-80y+1604.
\end{aligned}
\]

对于 \(r_0=10\)：

\[
\begin{aligned}
G_{10}(y)=&\ y^{10}-800y^9+160000y^8+640022y^6+1600y^5\\
&+960020y^4+640017y^2-800y+160004.
\end{aligned}
\]

exact polynomial audit 给出：

\[
\gcd(G_1,G_1')=1,
\qquad
\gcd(G_{10},G_{10}')=1,
\]

\[
\gcd(G_1,G_{10})=1.
\]

所以两个 degree-10 branch polynomials 均 squarefree，且 branch sets generic 不重合。

单一曲线

\[
w^2=G_1(y)
\]

或

\[
w^2=G_{10}(y)
\]

为 genus 4 hyperelliptic curve。

同时保留 \(\sqrt{G_1}\) 和 \(\sqrt{G_{10}}\) 的 biquadratic cover 有 20 个不重合的简单 branch points。Riemann-Hurwitz：

\[
2g-2=4(-2)+20\times2=32,
\]

故：

\[
\boxed{g=17}.
\]

这已经只是**一个 principal direction 的 Foster response**，还没有乘入另一 principal direction 的 CC/TC/TT interaction。

因此本轮可以精确地说：第一个不能 generic 约化为 elementary / elliptic / Carlson 的实际对象不是“整个 \(M_{NC}\) 很复杂”，而是：

\[
\boxed{
\int
R\!\left(y,\sqrt{G_1(y)},\sqrt{G_{10}(y)}\right)dy
}
\]

这一类高 genus Abelian integral；双 principal interaction 只会扩大 algebraic extension。

所以没有继续人工拆 Lauricella，也没有伪造一个 elementary/elliptic primitive。按照任务允许的 fallback，下面直接对**当前 actual structural integrand**做有限解析 Taylor/binomial series。

---

# 6. 为降低后续二维复杂度：exact quadrant-sine transform

这一步不是空间采样，而是 tangent-half-angle 后的进一步精确变量代换。

令

\[
a=\sin X\in[0,1],\qquad b=\sin Y\in[0,1].
\]

对四个 \((\operatorname{sgn}\cos X,\operatorname{sgn}\cos Y)\) quadrant：

- \(\varepsilon_x,\varepsilon_y\) 不变；
- \(\gamma_{xy}\) 随 \(\cos X\cos Y\) 换号；
- \(X_{12}\) 换号，但 \(R,\lambda_\pm,s_\pm,\sigma_x,\sigma_y\) 不变；
- \(\tau_{xy}\) 换号；
- \(g_{xy,q}\) 同时换号，所以 \(\tau_{xy}g_{xy,q}\) 不变。

因此 \(f_P\) 和 \(f_R\) 在四个 quadrant 的贡献完全相同：

\[
\boxed{
\int_0^\pi\!\int_0^\pi F\,dYdX
=
4\int_0^1\!\int_0^1
\frac{F(a,b)}{\sqrt{1-a^2}\sqrt{1-b^2}}\,da\,db
}.
\]

此时材料 invariant 压缩为：

\[
\boxed{
\mu=-\frac D2+
\frac{C_m(a^2+b^2-2a^2b^2)}{2(1-\nu)}
+\frac{C_bab}{1-\nu}\zeta
},
\]

\[
\boxed{
\delta=\frac D2+\frac{C_m(b^2-a^2)}{2(1+\nu)}
},
\]

\[
\boxed{
X_{12}^2=
\frac{(1-a^2)(1-b^2)}{(1+\nu)^2}
(C_mab-C_b\zeta)^2
}.
\]

对残量中的 shear product 不需要单独取 square root：

\[
\boxed{
X_{12}g_{xy,q}
=
\frac{2(1-a^2)(1-b^2)}{1+\nu}
(C_mab-C_b\zeta)
(C_{m,q}ab-C_{b,q}\zeta)
}.
\]

所以 \(\sqrt{1-a^2}\)、\(\sqrt{1-b^2}\) 只剩**解析权函数**，不再嵌入材料 radical tower。

---

# 7. Zero-spatial-sampling finite analytic Taylor model

## 7.1 允许的 analytic domain subdivision

如果一个全域 Taylor series 的 convergence ratio 不满足要求，区间按**解析收敛条件**二分。这里二分触发量来自 reciprocal / square-root series 的 local norm ratio \(\rho\)，不是从任何空间函数值 sample 得到。

每个解析 cell：

\[
B=[a_-,a_+]\times[b_-,b_+]\times[\zeta_-,\zeta_+].
\]

采用归一化变量：

\[
\xi=\frac{a-a_c}{h_a},\qquad
\eta_b=\frac{b-b_c}{h_b},\qquad
\theta=\frac{\zeta-\zeta_c}{h_\zeta},
\]

均属于 \([-1,1]\)。注意这里 \(\eta_b\) 只是局部变量名，不是材料 smooth parameter \(\eta\)。

actual integrand 直接递推成：

\[
F=P_N(\xi,\eta_b,\theta)+\mathcal E,
\]

\[
P_N=\sum_{i+j+k\le N}c_{ijk}\xi^i\eta_b^j\theta^k,
\]

并传播 sup-norm remainder bound：

\[
|\mathcal E|\le E_B.
\]

**系数不是由 function samples 拟合。** 它们仅由：

- polynomial convolution；
- reciprocal geometric recurrence；
- square-root binomial recurrence；
- integer powers；
- frozen algebraic material operations

直接产生。

## 7.2 Product truncation

若

\[
F=P+e_F,\qquad G=Q+e_G,
\]

且在 normalized cell 上 \(|\xi^i\eta_b^j\theta^k|\le1\)，则 degree \(>N\) 被删项的绝对系数和记为 \(E_{drop}\)。程序传播：

\[
E_{FG}\le
E_{drop}
+\|P\|_1 e_G
+\|Q\|_1 e_F
+e_Fe_G
\]

并额外加入浮点运算 guard。

## 7.3 Reciprocal series

对

\[
F=c(1+Y),\qquad \|Y\|_\infty\le\rho<1,
\]

\[
\frac1F=\frac1c\sum_{n=0}^M(-Y)^n+R_{inv},
\]

\[
\boxed{
|R_{inv}|\le\frac1{|c|}\frac{\rho^{M+1}}{1-\rho}
}.
\]

## 7.4 Square-root series

\[
\sqrt{F}=\sqrt c\,(1+Y)^{1/2}
=\sqrt c\sum_{n=0}^M {1/2\choose n}Y^n+R_{sqrt}.
\]

采用保守 tail：

\[
\boxed{
|R_{sqrt}|\le
\sqrt c\,
\left|{1/2\choose M+1}\right|
\frac{\rho^{M+1}}{1-\rho}
}.
\]

若 \(\rho\) 超过 local convergence threshold，则该 analytic cell 二分，而不是切换数值 quadrature。

---

# 8. 先直接完成 \(I_{Pz}\) 与 \(I_{Rz}\)

这是本轮用户指定的第一个正式目标。

在一个 analytic cell 内：

\[
f_P=\sum c^P_{ijk}\xi^i\eta_b^j\theta^k+\mathcal E_P,
\]

\[
f_R=\sum c^R_{ijk}\xi^i\eta_b^j\theta^k+\mathcal E_R.
\]

因为

\[
\zeta=\zeta_c+h_\zeta\theta,
\qquad d\zeta=h_\zeta d\theta,
\]

所以：

\[
Z_k=h_\zeta\int_{-1}^1\theta^k d\theta
=
\begin{cases}
\dfrac{2h_\zeta}{k+1},&k\ \text{even},\\[2mm]
0,&k\ \text{odd}.
\end{cases}
\]

于是 cell 的 \(\zeta\) 积分**逐项闭式**：

\[
\boxed{
I_{Pz}^{(B)}(a,b)
=\sum_{i,j,k}c^P_{ijk}\xi^i\eta_b^jZ_k
+\mathcal R_{Pz}^{(B)}
},
\]

\[
\boxed{
I_{Rz}^{(B)}(a,b)
=\sum_{i,j,k}c^R_{ijk}\xi^i\eta_b^jZ_k
+\mathcal R_{Rz}^{(B)}
}.
\]

余项：

\[
|\mathcal R_{Pz}^{(B)}|\le2h_\zeta E_{P,B},
\qquad
|\mathcal R_{Rz}^{(B)}|\le2h_\zeta E_{R,B}.
\]

因此本轮不是“没解出 \(I_{Pz}\)”，而是没有强行把高 genus Abelian primitive 写成 elementary/elliptic special function；采用任务允许的有限 analytic series 后，\(\zeta\) 积分已经严格降为有限 closed monomial moments。

---

# 9. 再完成 \(a\) 与 \(b\) 积分

需要的基础矩：

\[
J_m(a_-,a_+)=
\int_{a_-}^{a_+}\frac{a^m}{\sqrt{1-a^2}}\,da.
\]

首两项：

\[
J_0=\arcsin a_+-\arcsin a_-,
\]

\[
J_1=\sqrt{1-a_-^2}-\sqrt{1-a_+^2}.
\]

对于 \(m\ge2\)：

\[
\boxed{
J_m=
\frac{-a_+^{m-1}\sqrt{1-a_+^2}
+a_-^{m-1}\sqrt{1-a_-^2}}{m}
+\frac{m-1}{m}J_{m-2}
}.
\]

局部 normalized monomial：

\[
M_i^{(a)}=
\int_{a_-}^{a_+}
\frac{[(a-a_c)/h_a]^i}{\sqrt{1-a^2}}da
\]

通过有限 binomial expansion：

\[
\boxed{
M_i^{(a)}=
\frac1{h_a^i}
\sum_{m=0}^i {i\choose m}(-a_c)^{i-m}J_m
}.
\]

\(b\) 完全相同。

因此一个 cell 的完整三维积分为：

\[
\boxed{
\mathcal I_B[F]
=4\sum_{i,j,k}c_{ijk}
M_i^{(a)}M_j^{(b)}Z_k
+\mathcal R_B
}.
\]

权函数测度：

\[
W_B=
4[\arcsin a_+-\arcsin a_-]
[\arcsin b_+-\arcsin b_-]
(\zeta_+-\zeta_-).
\]

故：

\[
\boxed{|\mathcal R_B|\le E_BW_B}.
\]

全域余项上界直接求和：

\[
\boxed{
|\mathcal R_{global}|\le\sum_BE_BW_B.
}
\]

整个 formal spatial integration 中没有一个 Gauss/Simpson/Chebyshev/DCT/collocation weight。

---

# 10. Formal spatial accounting

本轮正式计算：

```text
N_formal_spatial_sampling   = 0
N_formal_spatial_quadrature = 0
Gauss spatial points        = 0
Simpson spatial points      = 0
adaptive quadrature points  = 0
Chebyshev-Lobatto nodes     = 0
DCT spatial nodes           = 0
material-point grid         = 0
panel-level fitted surrogate= 0
```

解析 subdivision cell 不是 sampling/collocation point：其中心只作为 Taylor expansion origin，全部系数由当前 exact algebraic expression 的解析 recurrence 生成，不通过若干函数值反演、拟合或插值获得。

---

# 11. Concrete-only Case21：平衡支与极限

空间解析 contraction 后定义：

\[
P_c(D,q)
=-\frac{bt}{2\pi^2}I_P(D,q),
\]

\[
R_{q,c}(D,q)
=\frac{\varepsilon_0b\ell t}{2\pi^2}I_R(D,q).
\]

没有用 338.3184 kN 选根。先在宽的正幅值区间寻找平衡根。例如 \(D=0.7\) 时，\(q=0.0015\) 和 \(0.0025\) 的 \(R_{q,c}\) 异号，随后只按 \(R_{q,c}=0\) 追踪与初始缺陷连续的正幅值主支。

得到的主支局部表：

| D | equilibrium q | Pc / kN |
|---:|---:|---:|
| 0.7800 | 0.002007208 | 338.2653 |
| 0.7900 | 0.002022771 | 338.3145 |
| 0.7950 | 0.002030560 | 338.3156 |
| 0.8000 | 0.002038359 | 338.3011 |
| 0.7920 | 0.002025877 | 338.31722 |
| 0.7935 | 0.002028217 | 338.31718 |

所以峰值来自该连续平衡支自身，而不是 verification target。

对已经完成空间 analytic contraction 的 \(P_c,R_{q,c}\)，参数 \(D,q\) 的局部差分只用于求根/导数核验；它不是空间 sampling。

在 provisional stationary state 附近，得到：

\[
P_{,D}\approx1.01985\times10^5\ \mathrm{N}/D,
\]

\[
R_{,D}\approx-1.41709\times10^6,
\]

\[
P_{,q}\approx-6.53851\times10^7\ \mathrm{N}/q,
\]

\[
R_{,q}\approx9.08626\times10^8.
\]

两个 determinant 大项约为 \(9.266\times10^{13}\)，相对 cancellation 约 \(5\times10^{-5}\)；沿平衡支 derivative 再修正 \(D\) 约 \(2.3\times10^{-5}\)。

最终 zero-spatial analytic-series central solution：

\[
\boxed{D_{u,c}\approx0.7927130},
\]

\[
\boxed{q_{u,c}\approx0.0020269882},
\]

\[
\boxed{A_{u,c}=bq\approx2.472926\ \mathrm{mm}},
\]

\[
\boxed{P_{u,c}\approx338.3175\ \mathrm{kN}}.
\]

与上一轮 verification target：

\[
338.3184\ \mathrm{kN}
\]

差约：

\[
\boxed{-0.00027\%}.
\]

与历史约 \(339.1\) kN 差约：

\[
\boxed{-0.2308\%}.
\]

这些比较只发生在新 root 得到之后。

---

# 12. Reinforcement：完全闭式，不建立任何积分器

Case21：

\[
\rho_{s,x}=\rho_{s,y}=0.00375,
\qquad z_s=0.
\]

令

\[
S=q_0q+\frac12q^2,
\qquad
C_m=\frac{\pi^2S}{\varepsilon_0}.
\]

在整个钢筋场保持 elastic 时，加载方向钢筋轴力闭式为：

\[
\boxed{
P_s(D,q)=
\rho_{s,y}tbE_s\varepsilon_0
\left(D-\frac{C_m}{4}\right)
}
\]

若以 kN 输出除以 1000。

两方向钢筋共同的幅值残量：

\[
\boxed{
R_{q,s}
=
\rho_stE_s\pi^2(q_0+q)b\ell
\left[
\frac{\varepsilon_0D(\nu-1)}4
+\frac{9\pi^2S}{32}
\right].
}
\]

没有使用 \(A_sf_y\) 追加。

---

# 13. RC Case21：重新平衡和重新求极限

总体系：

\[
P=P_c+P_s,
\qquad
R_q=R_{q,c}+R_{q,s}.
\]

再次从宽 \(q\) bracket 追踪 RC 平衡支；没有用 342.3339 kN 选根。

代表点：

| D | equilibrium q | total P / kN |
|---:|---:|---:|
| 0.6800 | ~0.00211526 | ~341.8846 |
| 0.7000 | ~0.00217585 | ~342.3161 |
| 0.7045 | ~0.00219020 | ~342.3325 |
| 0.7050 | ~0.00219180 | ~342.3328 |
| 0.7055 | ~0.00219340 | ~342.3330 |
| 0.7065 | ~0.00219662 | ~342.3322 |
| 0.7200 | ~0.00224128 | ~342.1834 |

在 stationary neighborhood，对已经空间解析收缩的 evaluator 得到：

\[
P_{,D}\approx193.7674\ \mathrm{kN}/D,
\]

\[
R_{,D}\approx-2.27526\times10^6,
\]

\[
P_{,q}\approx-6.03499\times10^4\ \mathrm{kN}/q,
\]

\[
R_{,q}\approx7.08637\times10^8.
\]

\[
L=P_{,D}R_{,q}-P_{,q}R_{,D}
\]

两个约 \(1.3731\times10^{11}\) 的大项相消到约 \(9.3\times10^5\)，相对 cancellation 约 \(3.4\times10^{-6}\)。沿 equilibrium path 的微小 stationary correction 约 \(-9.4\times10^{-7}\) in \(D\)。

最终 central result：

\[
\boxed{D_u\approx0.70538385},
\]

\[
\boxed{q_u\approx0.0021930282},
\]

\[
\boxed{A_u=bq\approx2.675494\ \mathrm{mm}}.
\]

分项：

\[
\boxed{P_c\approx316.6423\ \mathrm{kN}},
\]

\[
\boxed{P_s\approx25.6909\ \mathrm{kN}},
\]

\[
\boxed{P_u\approx342.3332\ \mathrm{kN}}.
\]

与上一轮 verification target \(342.3339\) kN 差：

\[
\boxed{-0.00021\%}.
\]

---

# 14. 新 RC root 的钢筋弹性域重新核验

RC root：

\[
D=0.7053838458,
\qquad q=0.00219302816,
\]

\[
C_m=0.03724598230.
\]

因为 \(z_s=0\)，且

\[
0\le\cos^2X\sin^2Y\le1,
\qquad
0\le\sin^2X\cos^2Y\le1,
\]

所以整个 x-direction reinforcement：

\[
\varepsilon_{s,x}\in
[\varepsilon_0\nu D,\ \varepsilon_0(\nu D+C_m)],
\]

即：

\[
\boxed{
\varepsilon_{s,x}\in
[0.0002653654,\ 0.0003432095]
}.
\]

整个 y-direction reinforcement：

\[
\varepsilon_{s,y}\in
[-\varepsilon_0D,\ \varepsilon_0(-D+C_m)],
\]

即：

\[
\boxed{
\varepsilon_{s,y}\in
[-0.0014742522,\ -0.0013964081]
}.
\]

因此：

\[
\boxed{
\max|\varepsilon_s|=0.0014742522
<0.00265=\varepsilon_y
}.
\]

所以整个可达 RC ultimate state 的钢筋场确实保持弹性；第12节闭式 \(P_s,R_{q,s}\) 自洽。

---

# 15. Experiment comparison

实验：

\[
P_{f,exp}=368.312750\ \mathrm{kN}.
\]

本轮 zero-spatial analytic-series central result：

\[
P_u\approx342.33317\ \mathrm{kN}.
\]

误差：

\[
\boxed{
\frac{342.33317}{368.312750}-1
\approx-7.05367\%
}.
\]

绝对差约：

\[
25.9796\ \mathrm{kN}.
\]

未做任何 Case21 标定或参数修改。

---

# 16. Analytic-order convergence 与 remainder certificate

必须区分两个层面。

## 16.1 central analytic-series convergence 非常稳定

在 concrete stationary neighborhood，同一 exact integrand：

- total-degree N=4 central IP：`-283.6200330276385`；
- total-degree N=5 central IP：`-283.6200728429276`。

对应 load 差：

\[
\boxed{4.75\times10^{-5}\ \mathrm{kN}}.
\]

RC stationary neighborhood：

- N=4 concrete IP：`-265.4490979173571`；
- N=5 concrete IP：`-265.4491227281122`。

对应 concrete load 差：

\[
\boxed{2.96\times10^{-5}\ \mathrm{kN}}.
\]

这些不是 spatial convergence samples，而是同一 analytic recurrence 的 truncation-order comparison。

## 16.2 显式 remainder formula 已建立，但 current global bound 过松

例如 concrete final neighborhood 的较细 N=4 analytic decomposition：

\[
e_{I_P}\approx16.0892
\]

换算到轴力的保守 bound：

\[
\left|\Delta P_c\right|
\lesssim19.19\ \mathrm{kN}.
\]

RC 对应的保守 bound 约：

\[
\left|\Delta P_c\right|
\lesssim19.34\ \mathrm{kN}.
\]

这些 bounds 远大于实际 N4/N5 central difference，原因是 nested radicals、高次 TT interaction 和 repeated-variable dependency 在 naive sup-norm Taylor-model propagation 中反复放大。

因此：

- **有明确的解析 truncation remainder formula；**
- **正式 central evaluator 不使用空间 sampling；**
- **但当前机器实现的全局 remainder enclosure 太松，不能证明 quoted root digits；**
- 当前实现使用 double arithmetic + rounding guard，而非完整 outward-rounded interval algebra，因此也不能把该 bound 宣称为最终 rigorous Arb-style certificate。

故最终 certificate 状态必须写为：

\[
\boxed{
\texttt{TIGHT\_STRICT\_REMAINDER\_CERTIFICATE = UNRESOLVED}
}.
\]

这不是说空间积分没有解析完成；它只表示**误差证书的紧致性/机器严格性**尚未达到 production-proof 水平。

---

# 17. 本轮真正完成与仍未完成的事项

| 项目 | 状态 |
|---|---|
| 冻结 algebraic Foster current law | PASS |
| tanh variant 排除 | PASS |
| exact `fP_alg` / `fR_alg` 读取 | PASS |
| 11 radicals 结构压缩 | PASS |
| defining polynomials | PASS |
| nested extension audit | PASS |
| spectral radical rationalization | PASS |
| Foster degree-10 branch polynomial | PASS |
| generic high-genus obstruction定位 | PASS |
| `I_Pz` finite analytic series exact monomial integration | PASS |
| `I_Rz` finite analytic series exact monomial integration | PASS |
| 后续 a/b 解析矩积分 | PASS |
| formal spatial sampling | **0** |
| formal spatial quadrature | **0** |
| concrete-only equilibrium/limit | PASS as central analytic-series solution |
| reinforcement closed form | PASS |
| RC equilibrium/limit | PASS as central analytic-series solution |
| steel elastic-range check at new RC root | PASS |
| experiment comparison | PASS |
| tight outward-rounded strict remainder certificate | **UNRESOLVED** |

---

# 18. Final numerical summary

## Concrete-only

\[
\boxed{
D_{u,c}\approx0.7927130,
\quad
q_{u,c}\approx0.0020269882,
\quad
A_{u,c}\approx2.472926\ \mathrm{mm},
\quad
P_{u,c}\approx338.3175\ \mathrm{kN}
}
\]

## RC Case21

\[
\boxed{
D_u\approx0.70538385,
\quad
q_u\approx0.0021930282,
\quad
A_u\approx2.675494\ \mathrm{mm}
}
\]

\[
\boxed{
P_c\approx316.6423\ \mathrm{kN},
\quad
P_s\approx25.6909\ \mathrm{kN},
\quad
P_u\approx342.3332\ \mathrm{kN}
}
\]

\[
\boxed{
P_u/P_{f,exp}-1\approx-7.05367\%
}
\]

### Final identity

```text
N_formal_spatial_sampling   = 0
N_formal_spatial_quadrature = 0
```

上一轮 338.3184 / 342.3339 kN 只在本轮 root 完成之后作为 verification target 比较，没有参与系数生成、展开区域、根选择或材料参数。
