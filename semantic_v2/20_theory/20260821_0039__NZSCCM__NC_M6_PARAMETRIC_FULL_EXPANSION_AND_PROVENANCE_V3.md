# NZ-SCCM — NC-M6 参数化全展开与系数来源总账 V3

时间：2026-08-21 00:39 +08:00

状态：`PARAMETRIC_FIRST / EXPAND_UNTIL_ALGEBRAIC_TERMINAL / NO_CASE21 / NO_LIMIT_DERIVATIVES`

## 0. 本节点的展开规则

1. 所有物理/结构参数尽量保持符号形式，不把 Case21 数值代入。
2. 纯代数整数/有理数（2,4,8,16, 1/2 等）明确标记为坐标变换、二阶运动学或多项式展开产生，不视为拟合参数。
3. NC-M6 物理系数若有数值，先给参数来源再给当前冻结数值。
4. “展开到展不开”为：
   - 三角函数全部半角有理化；
   - 基础多项式全部展开成单项式；
   - 唯一平方根保留为 `R=sqrt(Q)`；
   - 任何 `A+B R` 的有限乘积/幂全部按二次扩张配对公式展开；
   - compression rational 通过共轭完全有理化；
   - 厚度 Euler 变换后成为普通有理函数；
   - 对一般 5 次及以上不可用统一根式表达的分母，RootSum 作为严格解析终点（不是数值积分）。

## 1. 参数来源分层

### 1.1 原始/物理参数

\[
b,\quad \ell,\quad t_r,\quad q_0,\quad E_0,\quad f_c,\quad f_t,\quad \varepsilon_{c0},\quad \nu .
\]

几何派生：
\[
k=\frac b\ell.
\]

材料派生：
\[
\kappa=\frac{E_0\varepsilon_{c0}}{f_c},\qquad
\rho=\frac{f_t}{f_c},\qquad
x_{cr}=\frac{\rho}{\kappa}
=\frac{f_t}{E_0\varepsilon_{c0}}.
\]

CC interaction 不应把小数作为理论定义。定义 conservative CC ellipse 参数
\[
\alpha_{CC}^{NC},
\]
则
\[
\boxed{
a_{cc}=\frac1{\sqrt{2-\alpha_{CC}^{NC}}}-1.
}
\]
当前冻结
\[
\alpha_{CC}^{NC}=1.1843158623045873
\]
来自 G18 conservative CC ellipse；代入才得到
\[
a_{cc}=0.1072329249362415.
\]
所以正式推导保留 \(a_{cc}=a_{cc}(\alpha_{CC}^{NC})\)，不把 0.107... 当成原始常数。

TT interaction：
\[
\boxed{a_t=1-2^{-1/8}}
\]
来自 p=8 conservative TT superellipse 的等双拉点；小数
\[
a_t\approx0.08299595679532878
\]
只作显示。

### 1.2 结构全局变量

\[
D,\qquad q,\qquad \alpha.
\]

\[
M(q)=\frac{\pi^2}{\varepsilon_0}\left(q_0q+\frac12q^2\right),
\qquad
B(q)=\frac{\pi^2t_r}{2\varepsilon_0 b}q.
\]

其中 \(1/2\) 来自 von Karman 二阶项，\(\pi^2\) 来自单半波正弦函数二阶/乘积导数，不是经验数字。

## 2. 半角坐标与所有基础多项式

\[
\xi=\tan\frac X2,\qquad \eta=\tan\frac Y2,
\]
\[
U=1+\xi^2,\qquad V=1+\eta^2,\qquad
\mathscr D=U^2V^2.
\]

完全展开：

\[
\mathscr D=\eta^{4} \xi^{4} + 2 \eta^{4} \xi^{2} + \eta^{4} + 2 \eta^{2} \xi^{4} + 4 \eta^{2} \xi^{2} + 2 \eta^{2} + \xi^{4} + 2 \xi^{2} + 1.
\]

\[
F_x^\#=4 \eta^{2} \xi^{4} - 8 \eta^{2} \xi^{2} + 4 \eta^{2},
\]

\[
F_y^\#=4 \eta^{4} \xi^{2} - 8 \eta^{2} \xi^{2} + 4 \xi^{2},
\]

\[
H^\#=4 \eta^{3} \xi^{3} + 4 \eta^{3} \xi + 4 \eta \xi^{3} + 4 \eta \xi.
\]

\[
A_x^\#=- \frac{\eta^{4} \xi^{4}}{4} - \frac{\eta^{4} \xi^{2}}{2} - \frac{\eta^{4}}{4} - 2 \eta^{2} k^{2} \nu \xi^{4} - 4 \eta^{2} k^{2} \nu \xi^{2} - 2 \eta^{2} k^{2} \nu - \frac{5 \eta^{2} \xi^{4}}{2} + 11 \eta^{2} \xi^{2} - \frac{5 \eta^{2}}{2} - \frac{\xi^{4}}{4} - 2 k^{2} \nu \xi^{2} - \frac{\xi^{2}}{2} - \frac{1}{4},
\]

\[
A_y^\#=\frac{\eta^{4} \nu \xi^{4}}{4} - 2 \eta^{4} k^{2} \xi^{2} + \frac{\eta^{4} \nu \xi^{2}}{2} + \frac{\eta^{4} \nu}{4} - \frac{3 \eta^{2} \nu \xi^{4}}{2} + 12 \eta^{2} k^{2} \xi^{2} - 3 \eta^{2} \nu \xi^{2} - \frac{3 \eta^{2} \nu}{2} + \frac{\nu \xi^{4}}{4} - 2 k^{2} \xi^{2} + \frac{\nu \xi^{2}}{2} + \frac{\nu}{4},
\]

\[
A_\gamma^\#=- 8 \eta^{3} k \xi^{3} + 8 \eta^{3} k \xi + 8 \eta k \xi^{3} - 8 \eta k \xi.
\]

\[
A_\Sigma^\#=A_x^\#+A_y^\#=- \frac{\eta^{4} \xi^{4}}{4} + \frac{\eta^{4} \nu \xi^{4}}{4} - 2 \eta^{4} k^{2} \xi^{2} + \frac{\eta^{4} \nu \xi^{2}}{2} - \frac{\eta^{4} \xi^{2}}{2} + \frac{\eta^{4} \nu}{4} - \frac{\eta^{4}}{4} - 2 \eta^{2} k^{2} \nu \xi^{4} - \frac{3 \eta^{2} \nu \xi^{4}}{2} - \frac{5 \eta^{2} \xi^{4}}{2} - 4 \eta^{2} k^{2} \nu \xi^{2} + 12 \eta^{2} k^{2} \xi^{2} - 3 \eta^{2} \nu \xi^{2} + 11 \eta^{2} \xi^{2} - 2 \eta^{2} k^{2} \nu - \frac{3 \eta^{2} \nu}{2} - \frac{5 \eta^{2}}{2} + \frac{\nu \xi^{4}}{4} - \frac{\xi^{4}}{4} - 2 k^{2} \nu \xi^{2} - 2 k^{2} \xi^{2} + \frac{\nu \xi^{2}}{2} - \frac{\xi^{2}}{2} + \frac{\nu}{4} - \frac{1}{4},
\]

\[
A_\Delta^\#=A_x^\#-A_y^\#=- \frac{\eta^{4} \nu \xi^{4}}{4} - \frac{\eta^{4} \xi^{4}}{4} + 2 \eta^{4} k^{2} \xi^{2} - \frac{\eta^{4} \nu \xi^{2}}{2} - \frac{\eta^{4} \xi^{2}}{2} - \frac{\eta^{4} \nu}{4} - \frac{\eta^{4}}{4} - 2 \eta^{2} k^{2} \nu \xi^{4} + \frac{3 \eta^{2} \nu \xi^{4}}{2} - \frac{5 \eta^{2} \xi^{4}}{2} - 4 \eta^{2} k^{2} \nu \xi^{2} - 12 \eta^{2} k^{2} \xi^{2} + 3 \eta^{2} \nu \xi^{2} + 11 \eta^{2} \xi^{2} - 2 \eta^{2} k^{2} \nu + \frac{3 \eta^{2} \nu}{2} - \frac{5 \eta^{2}}{2} - \frac{\nu \xi^{4}}{4} - \frac{\xi^{4}}{4} - 2 k^{2} \nu \xi^{2} + 2 k^{2} \xi^{2} - \frac{\nu \xi^{2}}{2} - \frac{\xi^{2}}{2} - \frac{\nu}{4} - \frac{1}{4}.
\]

## 3. 应变分子完全展开

\[
e_x=\frac{E_x}{\mathscr D},\qquad
e_y=\frac{E_y}{\mathscr D},\qquad
\gamma=\frac{G}{\mathscr D}.
\]

\[
E_x=D \eta^{4} \nu \xi^{4} + 2 D \eta^{4} \nu \xi^{2} + D \eta^{4} \nu + 2 D \eta^{2} \nu \xi^{4} + 4 D \eta^{2} \nu \xi^{2} + 2 D \eta^{2} \nu + D \nu \xi^{4} + 2 D \nu \xi^{2} + D \nu + 4 B \eta^{3} \xi^{3} \zeta + 4 B \eta^{3} \xi \zeta + 4 B \eta \xi^{3} \zeta + 4 B \eta \xi \zeta + 4 M \eta^{2} \xi^{4} - 8 M \eta^{2} \xi^{2} + 4 M \eta^{2} - \frac{\alpha \eta^{4} \xi^{4}}{4} - \frac{\alpha \eta^{4} \xi^{2}}{2} - \frac{\alpha \eta^{4}}{4} - 2 \alpha \eta^{2} k^{2} \nu \xi^{4} - 4 \alpha \eta^{2} k^{2} \nu \xi^{2} - 2 \alpha \eta^{2} k^{2} \nu - \frac{5 \alpha \eta^{2} \xi^{4}}{2} + 11 \alpha \eta^{2} \xi^{2} - \frac{5 \alpha \eta^{2}}{2} - \frac{\alpha \xi^{4}}{4} - 2 \alpha k^{2} \nu \xi^{2} - \frac{\alpha \xi^{2}}{2} - \frac{\alpha}{4}.
\]

\[
E_y=- D \eta^{4} \xi^{4} - 2 D \eta^{4} \xi^{2} - D \eta^{4} - 2 D \eta^{2} \xi^{4} - 4 D \eta^{2} \xi^{2} - 2 D \eta^{2} - D \xi^{4} - 2 D \xi^{2} - D + 4 B \eta^{3} k^{2} \xi^{3} \zeta + 4 B \eta^{3} k^{2} \xi \zeta + 4 B \eta k^{2} \xi^{3} \zeta + 4 B \eta k^{2} \xi \zeta + 4 M \eta^{4} k^{2} \xi^{2} - 8 M \eta^{2} k^{2} \xi^{2} + 4 M k^{2} \xi^{2} + \frac{\alpha \eta^{4} \nu \xi^{4}}{4} - 2 \alpha \eta^{4} k^{2} \xi^{2} + \frac{\alpha \eta^{4} \nu \xi^{2}}{2} + \frac{\alpha \eta^{4} \nu}{4} - \frac{3 \alpha \eta^{2} \nu \xi^{4}}{2} + 12 \alpha \eta^{2} k^{2} \xi^{2} - 3 \alpha \eta^{2} \nu \xi^{2} - \frac{3 \alpha \eta^{2} \nu}{2} + \frac{\alpha \nu \xi^{4}}{4} - 2 \alpha k^{2} \xi^{2} + \frac{\alpha \nu \xi^{2}}{2} + \frac{\alpha \nu}{4}.
\]

\[
G=- 2 B \eta^{4} k \xi^{4} \zeta + 2 B \eta^{4} k \zeta + 2 B k \xi^{4} \zeta - 2 B k \zeta - 8 M \eta^{3} k \xi^{3} + 8 M \eta^{3} k \xi + 8 M \eta k \xi^{3} - 8 M \eta k \xi + 8 \alpha \eta^{3} k \xi^{3} - 8 \alpha \eta^{3} k \xi - 8 \alpha \eta k \xi^{3} + 8 \alpha \eta k \xi.
\]

## 4. 和、差及唯一根式的完全单项式系数

定义
\[
\Delta_E=E_x-E_y=\Delta_0+\Delta_1\zeta,
\]
\[
\Sigma_E=E_x+E_y=\Sigma_0+\Sigma_1\zeta,
\]
\[
G=G_0+G_1\zeta.
\]

### 4.1 $\Delta_0$ 的 9 个单项式

| 幂次 $(i,j)$ | 系数 $c_{ij}$，即 $c_{ij}\xi^i\eta^j$ |
|---:|---|
| (4, 4) | $ D \nu + D - \frac{\alpha \nu}{4} - \frac{\alpha}{4} $ |
| (4, 2) | $ 2 D \nu + 2 D - 2 \alpha k^{2} \nu + \frac{3 \alpha \nu}{2} - \frac{5 \alpha}{2} $ |
| (4, 0) | $ D \nu + D - \frac{\alpha \nu}{4} - \frac{\alpha}{4} $ |
| (2, 4) | $ 2 D \nu + 2 D - 4 M k^{2} + 2 \alpha k^{2} - \frac{\alpha \nu}{2} - \frac{\alpha}{2} $ |
| (2, 2) | $ 4 D \nu + 4 D + 4 \alpha k^{2} \nu - 12 \alpha k^{2} + 3 \alpha \nu + 11 \alpha - 8 M + 8 M k^{2} $ |
| (2, 0) | $ 2 D \nu + 2 D - 4 M k^{2} + 2 \alpha k^{2} - \frac{\alpha \nu}{2} - \frac{\alpha}{2} $ |
| (0, 4) | $ D \nu + D - \frac{\alpha \nu}{4} - \frac{\alpha}{4} $ |
| (0, 2) | $ 2 D \nu + 2 D + 4 M - 2 \alpha k^{2} \nu + \frac{3 \alpha \nu}{2} - \frac{5 \alpha}{2} $ |
| (0, 0) | $ D \nu + D - \frac{\alpha \nu}{4} - \frac{\alpha}{4} $ |

### 4.2 $\Delta_1$ 的 4 个单项式

| 幂次 $(i,j)$ | 系数 $c_{ij}$，即 $c_{ij}\xi^i\eta^j$ |
|---:|---|
| (3, 3) | $ - 4 B \left(k - 1\right) \left(k + 1\right) $ |
| (3, 1) | $ - 4 B \left(k - 1\right) \left(k + 1\right) $ |
| (1, 3) | $ - 4 B \left(k - 1\right) \left(k + 1\right) $ |
| (1, 1) | $ - 4 B \left(k - 1\right) \left(k + 1\right) $ |

### 4.3 $\Sigma_0$ 的 9 个单项式

| 幂次 $(i,j)$ | 系数 $c_{ij}$，即 $c_{ij}\xi^i\eta^j$ |
|---:|---|
| (4, 4) | $ D \nu - D + \frac{\alpha \nu}{4} - \frac{\alpha}{4} $ |
| (4, 2) | $ 2 D \nu - 2 D - 2 \alpha k^{2} \nu - \frac{3 \alpha \nu}{2} - \frac{5 \alpha}{2} $ |
| (4, 0) | $ D \nu - D + \frac{\alpha \nu}{4} - \frac{\alpha}{4} $ |
| (2, 4) | $ 2 D \nu - 2 D + 4 M k^{2} - 2 \alpha k^{2} + \frac{\alpha \nu}{2} - \frac{\alpha}{2} $ |
| (2, 2) | $ 4 D \nu - 4 D - 4 \alpha k^{2} \nu + 12 \alpha k^{2} - 3 \alpha \nu + 11 \alpha - 8 M - 8 M k^{2} $ |
| (2, 0) | $ 2 D \nu - 2 D + 4 M k^{2} - 2 \alpha k^{2} + \frac{\alpha \nu}{2} - \frac{\alpha}{2} $ |
| (0, 4) | $ D \nu - D + \frac{\alpha \nu}{4} - \frac{\alpha}{4} $ |
| (0, 2) | $ 2 D \nu - 2 D + 4 M - 2 \alpha k^{2} \nu - \frac{3 \alpha \nu}{2} - \frac{5 \alpha}{2} $ |
| (0, 0) | $ D \nu - D + \frac{\alpha \nu}{4} - \frac{\alpha}{4} $ |

### 4.4 $\Sigma_1$ 的 4 个单项式

| 幂次 $(i,j)$ | 系数 $c_{ij}$，即 $c_{ij}\xi^i\eta^j$ |
|---:|---|
| (3, 3) | $ 4 B \left(k^{2} + 1\right) $ |
| (3, 1) | $ 4 B \left(k^{2} + 1\right) $ |
| (1, 3) | $ 4 B \left(k^{2} + 1\right) $ |
| (1, 1) | $ 4 B \left(k^{2} + 1\right) $ |

### 4.5 $G_0$ 的 4 个单项式

| 幂次 $(i,j)$ | 系数 $c_{ij}$，即 $c_{ij}\xi^i\eta^j$ |
|---:|---|
| (3, 3) | $ - 8 k \left(M - \alpha\right) $ |
| (3, 1) | $ 8 k \left(M - \alpha\right) $ |
| (1, 3) | $ 8 k \left(M - \alpha\right) $ |
| (1, 1) | $ - 8 k \left(M - \alpha\right) $ |

### 4.6 $G_1$ 的 4 个单项式

| 幂次 $(i,j)$ | 系数 $c_{ij}$，即 $c_{ij}\xi^i\eta^j$ |
|---:|---|
| (4, 4) | $ - 2 B k $ |
| (4, 0) | $ 2 B k $ |
| (0, 4) | $ 2 B k $ |
| (0, 0) | $ - 2 B k $ |

唯一根：
\[
R=\sqrt{Q},\qquad
Q=\Delta_E^2+G^2
=\mathcal Q_2\zeta^2+\mathcal Q_1\zeta+\mathcal Q_0.
\]
注意这里使用 \(\mathcal Q_i\) 避免和初始缺陷 \(q_0\) 混淆。

完整的 \(\mathcal Q_0,\mathcal Q_1,\mathcal Q_2\) 单项式系数表保存在本节点的本地完整稿中；其定义严格为
\[
\mathcal Q_0=\Delta_0^2+G_0^2,
\qquad
\mathcal Q_1=2(\Delta_0\Delta_1+G_0G_1),
\qquad
\mathcal Q_2=\Delta_1^2+G_1^2.
\]
其中单项式数分别为 25、16、17。

## 5. 主材料坐标：已经到不可再消去的单一二次根层

\[
L=\frac{\Sigma_E}{2(1-\nu)\mathscr D},
\qquad
\beta=\frac1{2(1+\nu)\mathscr D},
\]
则
\[
\boxed{\lambda_1=L+\beta R,\qquad
\lambda_2=L-\beta R.}
\]

这是后续所有材料项唯一的代数生成元。

## 6. 冻结拉伸函数：源式与完全展开式

令
\[
r=\lambda/x_{cr}.
\]

第一段：
\[
T_1(r)=r,\qquad 0\le r\le\frac7{10}.
\]

第二段的源式（优先用于审计）：
\[
\chi=\frac{r-\frac7{10}}{\frac45}
=\frac54\left(r-\frac7{10}\right),
\]
\[
T_2=
\frac7{10}+\frac45\chi
-\frac{97}{50}\chi^3
+\frac{1843}{900}\chi^4
-\frac{97}{150}\chi^5.
\]
完全展开为
\[
T_2(r)=- \frac{12125 r^{5}}{6144} + \frac{438925 r^{4}}{36864} - \frac{1012195 r^{3}}{36864} + \frac{241045 r^{2}}{8192} - \frac{20346463 r}{1474560} + \frac{8351021}{2949120}.
\]

第三段源式：
\[
T_3(r)=1-\frac7{90}(r-1),
\qquad \frac32\le r\le9,
\]
即
\[
T_3(r)=\frac{97}{90} - \frac{7 r}{90}.
\]

第四段源式：
\[
\psi=\frac{r-9}{2},
\]
\[
T_4=
\frac{17}{45}
-\frac7{45}\psi
+\frac7{45}\psi^3
-\frac7{90}\psi^4,
\qquad 9<r<11.
\]
完全展开为
\[
T_4(r)=- \frac{7 r^{4}}{1440} + \frac{7 r^{3}}{36} - \frac{231 r^{2}}{80} + \frac{847 r}{45} - \frac{64787}{1440}.
\]

第五段：
\[
T_5(r)=\frac3{10},\qquad r\ge11.
\]

所有出现的十进制旧写法均应还原为上述有理数；这些数来自冻结 \(T_{NC}\) 分段 target，不来自 Case21 极限荷载拟合。

## 7. 二次扩张的“展开到头”规则

对任意
\[
Z=A+BR,
\qquad R^2=Q,
\]
记
\[
[Z]=(A,B).
\]

加法：
\[
(A,B)+(C,D)=(A+C,B+D).
\]

乘法：
\[
\boxed{
(A,B)\odot(C,D)
=
(AC+BDQ,\ AD+BC).
}
\]

因此任何有限乘积都不会产生第二个根。

### 7.1 任意多项式 \(P(r)\) 的完全参数展开

若
\[
P(r)=\sum_{m=0}^n a_m r^m,\qquad r=A+BR,
\]
则
\[
P(r)=P_0+P_1R,
\]
其中
\[
\boxed{
P_0=
\sum_{m=0}^n a_m
\sum_{j=0}^{\lfloor m/2\rfloor}
\binom{m}{2j}
A^{m-2j}B^{2j}Q^j,
}
\]
\[
\boxed{
P_1=
\sum_{m=0}^n a_m
\sum_{j=0}^{\lfloor(m-1)/2\rfloor}
\binom{m}{2j+1}
A^{m-2j-1}B^{2j+1}Q^j.
}
\]
把第 6 节每段的 \(a_m\) 代入即得到 \(T_i(\lambda_1/x_{cr})\) 或 \(T_j(\lambda_2/x_{cr})\) 的最终 \(P_0+P_1R\) 形式；没有隐藏 `T_i` 函数调用。

### 7.2 八次 interaction 的完全展开

若
\[
t=A+BR,
\]
则
\[
\boxed{
\begin{aligned}
t^8={}&
A^8+28A^6B^2Q+70A^4B^4Q^2+28A^2B^6Q^3+B^8Q^4\\
&+\left(
8A^7B+56A^5B^3Q+56A^3B^5Q^2+8AB^7Q^3
\right)R.
\end{aligned}}
\]

因此 TT 中的 \(\tau_j^8\) 已经可以完全展开，不需要幂运算黑箱。

## 8. compression primitive 的完全共轭展开

若压缩输入
\[
c=c_0+c_1R,
\]
原始
\[
C(c)=\frac{\kappa c}{1+(\kappa-2)c+c^2}.
\]

先定义
\[
d_0=
1+(\kappa-2)c_0+c_0^2+c_1^2Q,
\]
\[
d_1=
c_1(\kappa-2+2c_0).
\]

则分母
\[
1+(\kappa-2)c+c^2=d_0+d_1R.
\]

乘共轭后
\[
\boxed{
C(c)=C_0+C_1R,
}
\]
其中
\[
\boxed{
C_0=
\frac{\kappa(c_0d_0-c_1d_1Q)}
{d_0^2-d_1^2Q},
}
\]
\[
\boxed{
C_1=
\frac{\kappa(c_1d_0-c_0d_1)}
{d_0^2-d_1^2Q}.
}
\]

这已经把 `C(c)` 展开到底；剩余对象全是根式自由的有理函数。

## 9. 三类材料 sector 的最终 pair 形式

### 9.1 CC

\[
\lambda_1=L+\beta R,\qquad
\lambda_2=L-\beta R.
\]

\[
p=\lambda_1\lambda_2=L^2-\beta^2Q,
\]
根式已消失。

\[
h=1+a_{cc}p.
\]

\[
u_1=(-\lambda_1)h=-Lh-\beta hR,
\]
\[
u_2=(-\lambda_2)h=-Lh+\beta hR.
\]

将 \((c_0,c_1)=(-Lh,-\beta h)\) 代入第8节，得到
\[
C(u_1)=C_0+C_1R,
\]
而共轭性直接给
\[
C(u_2)=C_0-C_1R.
\]

所以
\[
s_1=-C_0-C_1R,\qquad
s_2=-C_0+C_1R,
\]
\[
\boxed{s_+=-2C_0,\qquad s_-=-2C_1R.}
\]

### 9.2 TC-Ti

正主值拉伸：
\[
r_1=\frac{L}{x_{cr}}+\frac{\beta}{x_{cr}}R.
\]
用第7.1节和第6节第 i 段系数得到
\[
t_1=T_i(r_1)=t_{10}+t_{11}R.
\]

压主值：
\[
c_2=-\lambda_2=-L+\beta R.
\]

\[
1-t_1=(1-t_{10})-t_{11}R.
\]

压缩输入
\[
u_2=c_2(1-t_1)=u_{20}+u_{21}R
\]
其中
\[
\boxed{
u_{20}=-L(1-t_{10})-\beta t_{11}Q,
}
\]
\[
\boxed{
u_{21}=Lt_{11}+\beta(1-t_{10}).
}
\]

将 \((u_{20},u_{21})\) 代第8节：
\[
C(u_2)=C_{20}+C_{21}R.
\]

于是
\[
s_1=\rho(t_{10}+t_{11}R),
\]
\[
s_2=-C_{20}-C_{21}R.
\]

故
\[
\boxed{
s_+=(\rho t_{10}-C_{20})+(\rho t_{11}-C_{21})R,
}
\]
\[
\boxed{
s_-=(\rho t_{10}+C_{20})+(\rho t_{11}+C_{21})R.
}
\]

### 9.3 TT-TiTj

\[
t_1=t_{10}+t_{11}R,
\qquad
t_2=t_{20}+t_{21}R,
\]
两者分别由第7.1节把 \(T_i,T_j\) 完全展开得到。

用第7.2节：
\[
t_1^8=u_{10}+u_{11}R,\qquad
t_2^8=u_{20}+u_{21}R.
\]

\[
g_1=1-a_t t_2^8=(1-a_tu_{20})-a_tu_{21}R,
\]
\[
g_2=1-a_t t_1^8=(1-a_tu_{10})-a_tu_{11}R.
\]

于是
\[
s_1=\rho\,t_1g_1,\qquad
s_2=\rho\,t_2g_2,
\]
并按 pair 乘法完全展开：
\[
\boxed{
\begin{aligned}
s_1=\rho\left[
&t_{10}(1-a_tu_{20})-a_tt_{11}u_{21}Q\\
&+\left(t_{11}(1-a_tu_{20})-a_tt_{10}u_{21}\right)R
\right],
\end{aligned}}
\]
\[
\boxed{
\begin{aligned}
s_2=\rho\left[
&t_{20}(1-a_tu_{10})-a_tt_{21}u_{11}Q\\
&+\left(t_{21}(1-a_tu_{10})-a_tt_{20}u_{11}\right)R
\right].
\end{aligned}}
\]

此处已不存在隐藏的八次幂。

## 10. 从 \(s_\pm\) 到物理应力核的最终 pair

写
\[
s_+=a+bR,\qquad
s_-=c+dR.
\]

因为
\[
\frac{s_-}{R}=d+\frac{c}{Q}R,
\]
所以三个无量纲物理应力组合直接是：

\[
\boxed{
\Sigma_x=
(a+d\Delta_E)
+\left(b+\frac{c\Delta_E}{Q}\right)R,
}
\]

\[
\boxed{
\Sigma_y=
(a-d\Delta_E)
+\left(b-\frac{c\Delta_E}{Q}\right)R,
}
\]

\[
\boxed{
\Sigma_{xy}=
dG+\frac{cG}{Q}R.
}
\]

物理应力：
\[
\sigma_x=\frac{f_c}{2}\Sigma_x,\qquad
\sigma_y=\frac{f_c}{2}\Sigma_y,\qquad
\tau_{xy}=\frac{f_c}{2}\Sigma_{xy}.
\]

## 11. 三个结构 kernel 展开到最终 \(K_0+K_1R\)

若
\[
\Sigma_x=X_0+X_1R,\quad
\Sigma_y=Y_0+Y_1R,\quad
\Sigma_{xy}=T_0+T_1R,
\]
则

\[
\boxed{
K_P=
\frac{Y_0}{UV}
+\frac{Y_1}{UV}R.
}
\]

\[
\boxed{
K_\alpha=
\frac{
X_0A_x^\#+Y_0A_y^\#+T_0A_\gamma^\#
}{UV\mathscr D}
+
\frac{
X_1A_x^\#+Y_1A_y^\#+T_1A_\gamma^\#
}{UV\mathscr D}R.
}
\]

定义
\[
M_q=\frac{\pi^2}{\varepsilon_0}(q_0+q),
\qquad
B_q=\frac{\pi^2t_r}{2\varepsilon_0b}.
\]
\[
Q_x^\#=M_qF_x^\#+B_qH^\#\zeta,
\]
\[
Q_y^\#=k^2M_qF_y^\#+k^2B_qH^\#\zeta,
\]
\[
Q_\gamma^\#=
8kM_q\xi\eta(1-\xi^2)(1-\eta^2)
-2kB_q\zeta(1-\xi^2)(1-\eta^2)UV.
\]

则
\[
\boxed{
K_q=
\frac{
X_0Q_x^\#+Y_0Q_y^\#+T_0Q_\gamma^\#
}{UV\mathscr D}
+
\frac{
X_1Q_x^\#+Y_1Q_y^\#+T_1Q_\gamma^\#
}{UV\mathscr D}R.
}
\]

所以每个 branch 的三个 kernel 已严格达到
\[
\boxed{
K_j(\zeta)=K_{j0}(\zeta)+K_{j1}(\zeta)R,
\quad R^2=\mathcal Q_2\zeta^2+\mathcal Q_1\zeta+\mathcal Q_0.
}
\]

## 12. 材料 front 的参数化完整系数

对任意阈值
\[
\lambda_b=\theta_bx_{cr},
\qquad
\theta_b\in\left\{0,\frac7{10},\frac32,9,11\right\},
\]
定义
\[
L_b=(1-\nu^2)\mathscr D\lambda_b.
\]

令
\[
A_0=X_0+\nu Y_0-L_b,\qquad
A_1=X_1+\nu Y_1,
\]
\[
B_0=\nu X_0+Y_0-L_b,\qquad
B_1=\nu X_1+Y_1,
\]
这里本节 \(X_0,X_1,Y_0,Y_1\) 指第3节的 \(E_x,E_y\) 的 \(\zeta\) 系数，不是第10节应力 pair。

则 front 方程
\[
a_b\zeta^2+b_b\zeta+c_b=0
\]
的三个参数系数为
\[
\boxed{
a_b=A_1B_1-\frac{(1-\nu)^2}{4}G_1^2,
}
\]
\[
\boxed{
b_b=A_0B_1+A_1B_0-\frac{(1-\nu)^2}{2}G_0G_1,
}
\]
\[
\boxed{
c_b=A_0B_0-\frac{(1-\nu)^2}{4}G_0^2.
}
\]

端点：
\[
\boxed{
\zeta_b^\pm=
\frac{-b_b\pm\sqrt{b_b^2-4a_bc_b}}{2a_b}.
}
\]

阈值数字全部来自第6节 \(T_{NC}\) 的分段 knot，不是积分拟合。

## 13. Euler 有理化和真正的解析终点

固定 \((\xi,\eta)\) 与一个 branch：
\[
R=\sqrt{\mathcal Q_2\zeta^2+\mathcal Q_1\zeta+\mathcal Q_0}.
\]

若 \(\mathcal Q_2\ne0\)，取
\[
\omega=R+\sqrt{\mathcal Q_2}\zeta.
\]

则
\[
\boxed{
\zeta=
\frac{\omega^2-\mathcal Q_0}
{2\sqrt{\mathcal Q_2}\omega+\mathcal Q_1},
}
\]
\[
\boxed{
R=
\frac{
\sqrt{\mathcal Q_2}\omega^2+
\mathcal Q_1\omega+
\sqrt{\mathcal Q_2}\mathcal Q_0
}{
2\sqrt{\mathcal Q_2}\omega+\mathcal Q_1
},
}
\]
\[
\boxed{
\frac{d\zeta}{d\omega}
=
\frac{
2\left(
\sqrt{\mathcal Q_2}\omega^2+
\mathcal Q_1\omega+
\sqrt{\mathcal Q_2}\mathcal Q_0
\right)
}{
(2\sqrt{\mathcal Q_2}\omega+\mathcal Q_1)^2
}.
}
\]

所以任一
\[
K_j=K_{j0}+K_{j1}R
\]
严格变成普通有理函数
\[
K_j\,d\zeta=
\frac{\mathcal N_j(\omega)}{\mathcal D_j(\omega)}d\omega.
\]

对一般 branch，\(\mathcal D_j\) 的 squarefree 部分次数可以超过4。一般五次及以上多项式根没有统一根式公式，因此此处“继续展开”的严格符号终点是：

\[
\frac{\mathcal N}{\mathcal D}
=
\frac{dH}{d\omega}
+
\frac{R_h}{S_h},
\qquad S_h\ \text{squarefree},
\]

\[
\boxed{
\Phi(\omega)=
H(\omega)
+
\operatorname{RootSum}_{S_h(t)=0}
\left[
\frac{R_h(t)}{S_h'(t)}
\log(\omega-t)
\right].
}
\]

若某个具体 branch 的 \(S_h\) 能分解为一次/二次因子，则进一步化为 rational + log + arctan；若存在一般不可解的五次及以上不可约因子，RootSum 就是“展不开为止”的 exact symbolic form。

## 14. 数字来源总表

| 数字/常数 | 精确形式 | 来源身份 |
|---|---|---|
| \(1/2\) | \(1/2\) | von Karman 二阶几何项 \(q^2/2\) |
| \(2,4,8,16\) | 整数 | 半角恒等式、公共分母清除、二项式展开；非材料参数 |
| \(7/10\) | 0.7 | \(T_{NC}\) 第1/2段 knot |
| \(3/2\) | 1.5 | \(T_{NC}\) 第2/3段 knot |
| \(9\) | 9 | \(T_{NC}\) 第3/4段 knot |
| \(11\) | 11 | \(T_{NC}\) 第4/5段 knot |
| \(97/50\) | 1.94 | \(T_{NC}\) 第二段源多项式 |
| \(1843/900\) | 2.047777... | \(T_{NC}\) 第二段源多项式 |
| \(97/150\) | 0.646666... | \(T_{NC}\) 第二段源多项式 |
| \(17/45\) | 0.377777... | \(T_{NC}\) 第四段端值 |
| \(7/45\) | 0.155555... | \(T_{NC}\) 第四段斜率/形状系数 |
| \(7/90\) | 0.077777... | 第三段线性斜率及第四段四次系数 |
| \(3/10\) | 0.3 | 冻结远端 residual tension |
| \(8\) in \(a_t\) | p=8 | conservative TT superellipse power |
| \(a_t\) | \(1-2^{-1/8}\) | 等双拉点与 p=8 envelope |
| \(\alpha_{CC}^{NC}\) | 1.1843158623045873 | G18 conservative CC ellipse |
| \(a_{cc}\) | \((2-\alpha_{CC}^{NC})^{-1/2}-1\) | 由上项派生；0.107232... 仅为代入后的显示值 |

## 15. 当前边界

本节点只完成“公式与系数来源展开”，不运行 Case21，不求极限 Jacobian，不改变 NC-M6。

21 个 branch 不再需要分别手抄成 63 份巨式：第6节给定每个 \(T_i\) 的精确系数，第7–11节给出从 branch 编号到最终 \(K_{j0}+K_{j1}R\) 的无歧义有限代数展开。对任一指定 branch，逐式代入即得到唯一完全展开式。
