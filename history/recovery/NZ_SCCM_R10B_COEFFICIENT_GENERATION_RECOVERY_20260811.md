# NZ-SCCM R10B 系数生成链完整恢复

**日期：2026-08-11**  
**身份：RECOVERY / REPRODUCIBILITY NOTE；不改变当前 R10/R10B 理论状态，不重构或替代原执行核心。**

## 0. 恢复结论

当前 GitHub 可以完整恢复 R10B 的**数学系数生成谱系**，但不能恢复原 `07_R10B_zero_spatial_compiler_core.py` 的 byte-identical 实现，也不能恢复当次 N48 的实际 coefficient arrays。原执行包只在 artifact manifest 中保留哈希。

因此本文把信息分成四类：

```text
A. EXACT_CURRENT_GITHUB
   当前仓库直接冻结的材料公式、R10 平滑、谱域、Cayley-Hamilton 代数、精确矩、求导原则。

B. EXACT_DERIVED_FROM_CURRENT_FORMULAS
   由 A 中公式唯一代数推出、无需猜测的变量映射与递推。

C. STRONGLY_RECOVERED_ARCHITECTURE
   由 R10B 理论 + 既有 coefficient-algebra 前驱实现共同确认的 U/C/T 编译—矩阵函数重构链。

D. ORIGINAL_EXECUTION_DETAIL_UNRESOLVED
   原 R10B 一维 Chebyshev coefficient generator 的具体节点/投影 convention、当次 N48 数组、空间截断/dealiasing 的逐行实现和原 core 字节。
```

**不得把 D 类未恢复事项用新生成的相似代码冒充原 R10B。**

---

# 1. 第一层：材料原始参数 -> R10 一维物理公式

Case21 ordinary concrete 基准材料参数：

\[
f_c=21.23\ \mathrm{MPa},\qquad
E_0=20321\ \mathrm{MPa},\qquad
\varepsilon_0=0.00209,\qquad
\nu=0.18.
\]

固定：

\[
\rho=0.1,
\]

\[
\kappa=\frac{E_0\varepsilon_0}{f_c}
=2.0005129533678754,
\]

\[
x_{cr}=\frac{\rho}{\kappa}
=0.04998717945397425,
\]

\[
\eta=\frac{x_{cr}}{20}
=0.0024993589726987125.
\]

正/负平滑坐标：

\[
\Pi_\eta(z)=
\frac{z^2\left(\sqrt{z^2+\eta^2}+z\right)}{2(z^2+\eta^2)},
\]

\[
t(\lambda)=\Pi_\eta(\lambda),\qquad
c(\lambda)=\Pi_\eta(-\lambda).
\]

压缩标量：

\[
\boxed{
C(\lambda)=
\frac{\kappa c(\lambda)}
{1+(\kappa-2)c(\lambda)+c(\lambda)^2}
}.
\]

R10 仅修改 tensile scalar，不改二维 interaction。

## 1.1 R10 rise branch

定义

\[
0\le t\le x_{cr},\qquad \tau=\frac{t}{x_{cr}},
\]

则

\[
\boxed{
\begin{aligned}
u_{rise}(t)={}&
\rho\tau
+(10h-6\rho)\tau^3
+(8\rho-15h)\tau^4
+(6h-3\rho)\tau^5.
\end{aligned}
}
\]

这三个高次系数由端点 C2 条件唯一确定，不是自由材料回归参数。

## 1.2 R10 fall branch

令残余

\[
u_r=0.03,
\]

对

\[
x_{cr}\le t\le10x_{cr},\qquad
\tau_f=\frac{t-x_{cr}}{9x_{cr}},
\]

有

\[
\boxed{
u_{fall}(t)=
h+(u_r-h)
\left(10\tau_f^3-15\tau_f^4+6\tau_f^5\right).
}
\]

## 1.3 h 由材料功唯一决定

R10 冻结：

\[
W_{src}=0.031741235181249904.
\]

rise 段：

\[
\int_0^{x_{cr}}u_{rise}(t)\,dt
=x_{cr}\left(\frac h2+\frac{\rho}{10}\right).
\]

fall 段：

\[
\int_{x_{cr}}^{10x_{cr}}u_{fall}(t)\,dt
=9x_{cr}\frac{h+u_r}{2}.
\]

因此

\[
W_{sm}=x_{cr}
\left[
5h+\frac{\rho}{10}+\frac92u_r
\right].
\]

由 \(W_{sm}=W_{src}\)：

\[
\boxed{
h=\frac15
\left[
\frac{W_{src}}{x_{cr}}
-\frac{\rho}{10}
-\frac92u_r
\right]
=0.09799750427197301.
}
\]

故 R10 理论层没有需要人工录入的自由五次系数。

## 1.4 R10 主标量 U/C/T

定义

\[
\boxed{T^{R10}(\lambda)=\frac{u_{sm}(t(\lambda))}{\rho}}
\]

以及

\[
\boxed{
U^{R10}(\lambda)=
\kappa\lambda
-C(\lambda)
+\kappa c(\lambda)
+u_{sm}(t(\lambda))
-\kappa t(\lambda).
}
\]

于是 R10B 最小材料编译对象为同一 current-map 所需的三个一维 scalar functions：

\[
\boxed{U(\lambda),\qquad C(\lambda),\qquad T(\lambda).}
\]

`C^2`、`T^7`、`T^8`、CC/TC/TT 不需要作为自由材料拟合对象；它们可在 coefficient algebra 中由 C/T 乘法与幂递推产生。原 core 是否为了效率缓存额外 primitive 数组属于 ORIGINAL_EXECUTION_DETAIL_UNRESOLVED。

---

# 2. 第二层：Case21 谱域 -> 唯一一维 Chebyshev 坐标

R10B Case21 认证区间：

\[
\lambda_+\in[-0.0956591207,0.1029457518],
\]

\[
\lambda_-\in[-1.0029457518,-0.6843408793].
\]

安全 compiler intervals：

```text
lambda+ : [-0.10,  0.105]
lambda- : [-1.01, -0.68]
```

并置于一个统一 scalar hull：

\[
\boxed{\lambda\in[\lambda_a,\lambda_b]=[-1.01,0.105].}
\]

精确写成：

\[
\lambda_a=-\frac{101}{100},\qquad
\lambda_b=\frac{21}{200}.
\]

中心与半宽：

\[
\lambda_c=\frac{\lambda_a+\lambda_b}{2}
=-\frac{181}{400},
\]

\[
\lambda_s=\frac{\lambda_b-\lambda_a}{2}
=\frac{223}{400}.
\]

定义材料 Chebyshev 坐标：

\[
\boxed{
\xi(\lambda)=\frac{\lambda-\lambda_c}{\lambda_s}
=\frac{400\lambda+181}{223}
\in[-1,1].
}
\]

这一步由 R10B 的统一 hull 唯一确定，不涉及拟合。

---

# 3. 第三层：一维材料函数 -> N48 编译系数

对任一 frozen scalar

\[
F\in\{U,C,T\},
\]

R10B 的有限表示写为

\[
\boxed{
F_N(\lambda)=
\sum_{n=0}^{N}\widehat F_n
T_n\!\left(\frac{400\lambda+181}{223}\right).
}
\]

在正式 N48 中：

\[
N=48.
\]

因此每一个 scalar function 有

\[
\boxed{49\text{ 个 }(n=0,\ldots,48)\text{ Chebyshev coefficients}.}
\]

不是“48 个系数”。若采用最小 \(U,C,T\) 集，则有 3×49=147 个**一级材料编译系数**；这些都是由 frozen material functions 派生的 compiler data，不是独立材料参数。

## 3.1 已恢复到的确定程度

当前仓库明确冻结：

```text
1D material-coordinate Chebyshev compiler
material degree = 48
material-coordinate samples may be used only to derive fixed compiler coefficients
```

但当前 GitHub 未保存原 `07_R10B_zero_spatial_compiler_core.py` 和 `03_material_compiler_N48_metrics.csv` 的内容，只保存 SHA-256。因此原 R10B 究竟使用：

- Chebyshev-Gauss projection / DCT-II；
- Chebyshev-Lobatto interpolation / DCT-I；
- 或同族的等价高分辨率 projection convention；

**不能仅凭当前文本唯一判定。**

故把原 coefficient operator 记为：

\[
\boxed{
\widehat F_n=\mathcal C^{R10B}_{n,48}
\left[F(\lambda_c+\lambda_s\xi)\right].
}
\]

这不是回避定义，而是对当前缺失原 core 的证据边界的精确记录。

## 3.2 两个数学上标准、但不能冒充原 core 的 convention

连续 Chebyshev projection：

\[
\widehat F_0=
\frac1\pi\int_0^\pi
F(\lambda_c+\lambda_s\cos\theta)\,d\theta,
\]

\[
\widehat F_n=
\frac2\pi\int_0^\pi
F(\lambda_c+\lambda_s\cos\theta)
\cos(n\theta)\,d\theta,\qquad n\ge1.
\]

Chebyshev-Lobatto/DCT-I interpolation则取

\[
\xi_j=\cos\frac{j\pi}{N},\qquad j=0,\ldots,N,
\]

并由离散余弦变换唯一恢复系数。

历史相邻执行中两类 convention 都曾出现，因此在找回原 core 前，不选择其中之一作为“原 R10B 的逐字 convention”。

---

# 4. 第四层：一维系数 -> 2×2 矩阵函数系数

将归一化 equivalent-uniaxial tensor 记为 \(X\)，其主值即 \(\lambda_\pm\)。

由同一 affine map：

\[
\boxed{
Y=\frac{X-\lambda_cI}{\lambda_s}
=\frac{400X+181I}{223}
=aI+bX,
}
\]

其中

\[
a=\frac{181}{223},\qquad b=\frac{400}{223}.
\]

Y 的两个不变量：

\[
K_1=\operatorname{tr}Y,
\qquad
K_2=\det Y.
\]

Cayley-Hamilton：

\[
Y^2-K_1Y+K_2I=0.
\]

故每一个矩阵 Chebyshev 多项式都可唯一写成：

\[
\boxed{
T_n(Y)=A_n(K_1,K_2)I+B_n(K_1,K_2)Y.
}
\]

初值：

\[
(A_0,B_0)=(1,0),
\qquad
(A_1,B_1)=(0,1).
\]

利用

\[
T_{n+1}(Y)=2YT_n(Y)-T_{n-1}(Y)
\]

以及

\[
Y(AI+BY)=(-BK_2)I+(A+BK_1)Y,
\]

得到显式递推：

\[
\boxed{
A_{n+1}=-2K_2B_n-A_{n-1},
}
\]

\[
\boxed{
B_{n+1}=2A_n+2K_1B_n-B_{n-1}.
}
\]

因此任一材料函数的 N48 矩阵形式是：

\[
\boxed{
F_{48}(Y)=
\left(\sum_{n=0}^{48}\widehat F_nA_n\right)I
+
\left(\sum_{n=0}^{48}\widehat F_nB_n\right)Y.
}
\]

定义：

\[
A_F=\sum_{n=0}^{48}\widehat F_nA_n,
\qquad
B_F=\sum_{n=0}^{48}\widehat F_nB_n,
\]

则

\[
F(Y)=A_FI+B_FY.
\]

此处开始，原来的 49 个一维 scalar coefficients 已经被自动提升为二维 objective matrix function；**没有二维材料面重新拟合。**

---

# 5. Pair algebra：U/C/T -> CC/TC/TT -> 总应力

用 pair

\[
F\equiv(A_F,B_F)
\]

代表

\[
F=A_FI+B_FY.
\]

若

\[
F=(A,B),\qquad G=(C,D),
\]

则

\[
\boxed{
FG=
(AC-BDK_2,\ AD+BC+BDK_1).
}
\]

此外：

\[
\boxed{\operatorname{tr}F=2A+BK_1}
\]

\[
\boxed{
\det F=A^2+ABK_1+B^2K_2.
}
\]

于是所有 interaction 可直接 coefficient-algebra 生成。

## 5.1 CC

对 \(C=(A_C,B_C)\)：

\[
d_C=A_C^2+A_CB_CK_1+B_C^2K_2.
\]

R10B：

\[
CC=\det(C)C,
\]

故

\[
\boxed{
CC=(d_CA_C,\ d_CB_C).
}
\]

## 5.2 TC

\[
\operatorname{tr}T=2A_T+B_TK_1.
\]

\[
\operatorname{tr}(T)I-T
=(A_T+B_TK_1,-B_T).
\]

于是

\[
\boxed{
TC=C\,[\operatorname{tr}(T)I-T]
}
\]

用上面的 pair product 一次得到，不需要主值逐点计算。

## 5.3 TT

先用 pair product 的 binary powering 或逐次乘法得到：

\[
T^2,T^3,\ldots,T^7.
\]

每一级仍是一个 pair。

设

\[
T^7=(A_7,B_7),
\]

则

\[
\operatorname{tr}(T^7)=2A_7+B_7K_1.
\]

\[
\det T=A_T^2+A_TB_TK_1+B_T^2K_2.
\]

故

\[
\boxed{
TT=\det(T)[\operatorname{tr}(T^7)I-T^7]
}
\]

亦完全在有限 pair algebra 中生成。

## 5.4 总归一化应力 pair

R10B：

\[
\boxed{
S=U-a_{cc}CC+TC-\rho a_tTT.
}
\]

若

\[
S=(A_S,B_S),
\]

则物理应力为：

\[
\boxed{\boldsymbol\sigma=f_c\,[A_SI+B_SY].}
\]

由于

\[
Y=aI+bX,
\]

还可回写为

\[
\boxed{
\boldsymbol\sigma=f_c
\left[(A_S+aB_S)I+bB_SX\right].
}
\]

这就是一维 material coefficients 到二维 current stress tensor 的完整代数桥梁。

---

# 6. 第五层：Nguyen 场 -> 稀疏不变量系数

Case21 定义：

\[
u=\sin X,\qquad v=\sin Y,\qquad z=\zeta,
\]

\[
M=C_m(q),\qquad B=C_b(q).
\]

Nguyen 归一化物理应变：

\[
e_x=\nu D+M(1-u^2)v^2+Buvz,
\]

\[
e_y=-D+Mu^2(1-v^2)+Buvz,
\]

\[
g=2Muv\sqrt{1-u^2}\sqrt{1-v^2}
-2B\sqrt{1-u^2}\sqrt{1-v^2}z.
\]

先定义物理应变迹与行列式：

\[
p=e_x+e_y,
\qquad
d=e_xe_y-\frac{g^2}{4}.
\]

Equivalent-uniaxial normalized tensor \(X\) 的不变量可直接化为：

\[
\boxed{
J_1=\operatorname{tr}X=\frac{p}{1-\nu},
}
\]

\[
\boxed{
J_2=\det X=
\frac{d+\nu J_1^2}{(1+\nu)^2}.
}
\]

这避免显式求 \(\lambda_\pm\) 和谱平方根。

## 6.1 J1 的完整稀疏 Chebyshev 展开

物理迹：

\[
p=(\nu-1)D+M(u^2+v^2-2u^2v^2)+2Buvz.
\]

记

\[
U_n=T_n(u),\quad V_n=T_n(v),\quad Z_n=T_n(z).
\]

利用

\[
u^2=\frac{U_2+1}{2},\qquad
v^2=\frac{V_2+1}{2},
\]

有

\[
u^2+v^2-2u^2v^2
=\frac12-\frac12U_2V_2.
\]

所以

\[
\boxed{
J_1=
-D
+\frac{M}{2(1-\nu)}
-\frac{M}{2(1-\nu)}U_2V_2
+\frac{2B}{1-\nu}U_1V_1Z_1.
}
\]

只有四个基础 coefficient blocks。

## 6.2 d 的完整有限 Chebyshev 展开

已有 exact invariant identity：

\[
\begin{aligned}
d={}&-\nu D^2
+DMK
+BD(\nu-1)W\\
&+BMW(2-u^2-v^2)
+B^2z^2(u^2+v^2-1),
\end{aligned}
\]

其中

\[
W=uvz,
\]

\[
K=\nu u^2-v^2+(1-\nu)u^2v^2.
\]

K 展开为：

\[
\boxed{
K=
\frac{\nu-1}{4}
+\frac{1+\nu}{4}U_2
-\frac{1+\nu}{4}V_2
+\frac{1-\nu}{4}U_2V_2.
}
\]

并有：

\[
\boxed{
W(2-u^2-v^2)=
\frac12U_1V_1Z_1
-\frac14U_3V_1Z_1
-\frac14U_1V_3Z_1.
}
\]

以及

\[
\boxed{
z^2(u^2+v^2-1)=
\frac14
(U_2+V_2+U_2Z_2+V_2Z_2).
}
\]

故

\[
\boxed{
\begin{aligned}
d={}&-\nu D^2\\
&+DM\left[
\frac{\nu-1}{4}
+\frac{1+\nu}{4}U_2
-\frac{1+\nu}{4}V_2
+\frac{1-\nu}{4}U_2V_2
\right]\\
&+BD(\nu-1)U_1V_1Z_1\\
&+BM\left[
\frac12U_1V_1Z_1
-\frac14U_3V_1Z_1
-\frac14U_1V_3Z_1
\right]\\
&+\frac{B^2}{4}
(U_2+V_2+U_2Z_2+V_2Z_2).
\end{aligned}
}
\]

再由

\[
J_2=\frac{d+\nu J_1^2}{(1+\nu)^2}
\]

构造 J2。J1² 不需要手写长多项式，因 Chebyshev product identity 是精确有限卷积：

\[
\boxed{
T_m(x)T_n(x)=\frac12
\left[T_{m+n}(x)+T_{|m-n|}(x)\right].
}
\]

## 6.3 K1/K2

由

\[
Y=aI+bX,
\quad a=181/223,\quad b=400/223,
\]

有

\[
\boxed{K_1=2a+bJ_1}
\]

\[
\boxed{K_2=a^2+abJ_1+b^2J_2}.
\]

因此 \(K_1,K_2\) 本身都是 \((U_i,V_j,Z_k)\) 上的有限 coefficient arrays。

---

# 7. 第六层：空间 coefficient algebra

所有场统一写成：

\[
\boxed{
F(X,Y,z)=
\sum_{i,j,k}
c_{ijk}
T_i(\sin X)
T_j(\sin Y)
T_k(z).
}
\]

系数乘法不需要空间节点。每一维使用：

\[
T_mT_n=\frac12(T_{m+n}+T_{|m-n|}).
\]

三维乘积就是三个一维有限卷积的张量积。

R10B 记录：FFT 只用于 coefficient-index convolution 加速；FFT 不在物理空间评价 integrand。

N48 formal root 对应：

```text
material degree       = 48
spatial Chebyshev deg = 28
```

`28` 的身份是保留的空间 coefficient-basis degree，不是 28 个空间 collocation points。

原 core 的逐级 truncation/dealiasing 次序当前未恢复，故不得声称 byte-identical reproduction；但最终数学对象确定是有限 \(c_{ijk}\) arrays。

---

# 8. 第七层：系数 -> P 与 R 的精确完整半波矩

定义

\[
M_n=\int_0^\pi T_n(\sin X)\,dX,
\]

则

\[
\boxed{
M_n=
\begin{cases}
\pi,&n=0,\\
2\sin(n\pi/2)/n,&n\ge1.
\end{cases}
}
\]

厚度矩：

\[
Z_k=\int_{-1}^{1}T_k(z)\,dz,
\]

\[
\boxed{
Z_k=
\begin{cases}
0,&k\text{ odd},\\
2/(1-k^2),&k\text{ even}.
\end{cases}
}
\]

若轴力 integrand 的有限 coefficient array 为

\[
f_P=\sum c^P_{ijk}U_iV_jZ_k,
\]

则

\[
\boxed{
\mathcal I_P=
\sum_{ijk}c^P_{ijk}M_iM_jZ_k.
}
\]

因此

\[
\boxed{
P_c(D,q)=
-\frac{bt}{2\pi^2}\mathcal I_P.
}
\]

若幅值残量 integrand coefficient array 为

\[
f_R=\sum c^R_{ijk}U_iV_jZ_k,
\]

则

\[
\boxed{
\mathcal I_R=
\sum_{ijk}c^R_{ijk}M_iM_jZ_k,
}
\]

\[
\boxed{
R_{q,c}(D,q)=
\frac{\varepsilon_0b\ell t}{2\pi^2}\mathcal I_R.
}
\]

正式结构积分至此仅是有限系数 contraction：

```text
N_formal_spatial_sampling   = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
```

---

# 9. 第八层：same-expression derivative coefficients

R10B 不对最终 P/R 做有限差分。每个 coefficient object 同时携带对 D、q 的 forward jets。

例如标量 coefficient objects \(F,G\) 的乘积 \(H=FG\)：

\[
\boxed{H_D=F_DG+FG_D}
\]

\[
\boxed{H_q=F_qG+FG_q}
\]

\[
\boxed{
H_{Dq}=F_{Dq}G+F_DG_q+F_qG_D+FG_{Dq}
}
\]

\[
\boxed{
H_{qq}=F_{qq}G+2F_qG_q+FG_{qq}.
}
\]

同一规则逐层作用于：

```text
M(q), B(q)
-> J1,J2
-> K1,K2
-> matrix Chebyshev recurrence
-> U/C/T pairs
-> CC/TC/TT
-> S
-> sigma
-> fP,fR coefficient arrays
```

由于 exact moment contraction 是线性的：

\[
\boxed{
P_D=
-\frac{bt}{2\pi^2}
\sum_{ijk}(c^P_{ijk})_D M_iM_jZ_k
}
\]

\[
\boxed{
P_q=
-\frac{bt}{2\pi^2}
\sum_{ijk}(c^P_{ijk})_q M_iM_jZ_k
}
\]

同理得到 \(R_D,R_q\)。

然后：

\[
\boxed{L=P_DR_q-P_qR_D.}
\]

极限点求解：

\[
\boxed{R(D,q)=0,\qquad L(D,q)=0.}
\]

数值根算法只解已经显式形成的有限方程，不回到空间积分。

---

# 10. R10B N48 已执行结果作为链路闭合证据

当前 canonical result：

```text
material degree = 48
spatial degree  = 28
D_u  = 0.8449505
q_u  = 0.001779254542005754
A_u  = 2.1706905412470197 mm
Pc   = 337.39660909142 kN
Ps   = 30.922943404456966 kN
Pu   = 368.31955249587696 kN
R    = -2.2383016926141863e-05 kN mm
P_D  = 106.58759351383472
P_q  = -75105.39767023241
R_D  = -1376.335532846137
R_q  = 969815.5988960797
L    = 83.31643116474152
L_normalized = 4.029999719717427e-07
```

N96 fixed-D equilibrium audit：

```text
q_eq = 0.0017855282237914806
P    = 368.50804285212683 kN
Delta P from N48 = 0.18849035625 kN = 0.0511757671 %
```

这说明有限解析 compiler order 的工程敏感度，而不是空间 quadrature 误差。

---

# 11. 目前到底缺什么

已恢复：

```text
PASS: material parameters -> kappa/xcr/eta
PASS: Wsrc -> h
PASS: R10 rise/fall coefficients as parameter formulas
PASS: U/C/T physical scalar definitions
PASS: Case21 compiler hull
PASS: exact lambda -> xi affine map
PASS: exact X -> Y affine matrix map
PASS: matrix-Chebyshev Cayley-Hamilton recurrence
PASS: pair product / trace / determinant
PASS: CC/TC/TT algebra
PASS: sparse J1 and d coefficient expansions
PASS: J2,K1,K2 construction
PASS: tensor-Chebyshev finite coefficient algebra
PASS: exact complete-halfwave moment contraction
PASS: same-expression derivative genealogy
PASS: N48/N96 canonical numerical results
```

未恢复：

```text
OPEN: exact original R10B 1D coefficient-node/projection convention
OPEN: original N48 coefficient arrays
OPEN: original 03_material_compiler_N48_metrics.csv bytes
OPEN: original 07_R10B_zero_spatial_compiler_core.py bytes
OPEN: exact internal spatial truncation/dealiasing scheduling
```

Artifact manifest 已冻结原文件哈希，因此以后若找回本地 ZIP/core，可逐文件 SHA-256 验证并把 OPEN 项升级为 EXACT_EXECUTION_RECOVERY。

---

# 12. 论文表达建议

正式论文不应把几十个 Chebyshev 小数当作材料参数。推荐层次：

\[
\boxed{
\text{material parameters}
\to
\text{R10 physical scalar formula}
\to
\text{coefficient operator }\mathcal C_N
\to
\{\widehat U_n,\widehat C_n,\widehat T_n\}
\to
\text{Cayley-Hamilton coefficient algebra}
\to
\{c^P_{ijk},c^R_{ijk}\}
\to
\text{exact moments}
\to
P,R,L.
}
\]

理论正文给参数公式和 coefficient-generation operator；附录/补充材料保存 machine coefficient tables。这样材料物理和解析编译层完全分离，也避免人工抄录十几位小数。
