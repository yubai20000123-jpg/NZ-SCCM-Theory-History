# NZ-SCCM — NC-M6 finite exact-period 三函数编译 V7

时间：2026-08-21 01:33 +08:00

状态：
`ONE_CONTINUOUS_COMPLETE_HALFWAVE / NC_M6_FROZEN / PARAMETRIC_COEFFICIENT_RULES / THICKNESS_EXACT / SURFACE_EXACT_PERIOD_COMPILED / P_Rq_Ralpha_CLOSED / CASE21_NOT_RUN / LIMIT_DERIVATIVES_NOT_YET_APPLIED`

## 0. 本节点只做一件事

严格照 NC-M4 的最终积分模板，把厚度凝聚后的三个板面双重积分直接编译成有限 relative/incomplete Aomoto–Gelfand / GKZ exact-period 三函数：

\[
P(D,q,\alpha),\qquad
R_q(D,q,\alpha),\qquad
R_\alpha(D,q,\alpha).
\]

不要求继续约成初等函数，不新建 evaluator 门禁，不改材料，不引入新空间离散。

---

## 1. 厚度凝聚后的统一输入

对每个 NC-M6 解析 branch \(b\) 和结构核
\[
j\in\{P,q,\alpha\},
\]
厚度方向已经得到 exact primitive
\[
F_{jb}(\xi,\eta,\zeta;D,q,\alpha),
\]
其中所有系数由 V6 的参数化规则生成。

每个 branch 的有效厚度贡献定义为
\[
\Delta F_{jb}
=
F_{jb}(\xi,\eta,\zeta_{b,+};D,q,\alpha)
-
F_{jb}(\xi,\eta,\zeta_{b,-};D,q,\alpha).
\]

\(\zeta_{b,\pm}\) 是由 NC-M6 sector/T-branch front 的二次方程得到的代数端点；它们属于 relative algebraic cycle，不是人为 thickness cells。

于是厚度凝聚后的三个板面核为
\[
\boxed{
\mathcal T_j(\xi,\eta;D,q,\alpha)
=
\sum_{b\in\mathcal B}
\Delta F_{jb}(\xi,\eta;D,q,\alpha),
}
\]
其中
\[
\mathcal B=
\{\mathrm{CC},\mathrm{TC}\!-\!T_1,\ldots,\mathrm{TC}\!-\!T_5,
\mathrm{TT}\!-\!T_iT_j\ (1\le j\le i\le5)\}.
\]

\(|\mathcal B|=21\)。

---

## 2. 板面紧化

半角变量
\[
\xi,\eta\in[0,\infty)
\]
用
\[
\boxed{
\xi=\frac{r}{1-r},\qquad
\eta=\frac{s}{1-s}
}
\]
映射到
\[
(r,s)\in[0,1]^2.
\]

Jacobian：
\[
d\xi\,d\eta
=
\frac{dr\,ds}{(1-r)^2(1-s)^2}.
\]

因此定义紧化后的三核
\[
\boxed{
\widehat{\mathcal T}_j(r,s;D,q,\alpha)
=
\frac{
\mathcal T_j\!\left(\frac r{1-r},\frac s{1-s};D,q,\alpha\right)
}{
(1-r)^2(1-s)^2
}.
}
\]

---

## 3. 有限因子标准形

厚度 primitive 只含有限次组合的：

- rational/algebraic terms；
- algebraic front roots；
- \(\log\)；
- \(\arctan\)（等价于复对数）。

因此每个紧化后的 term 都可唯一整理为有限线性组合
\[
C_\nu(D,q,\alpha)
r^{a_{\nu0}}
(1-r)^{a_{\nu1}}
s^{a_{\nu2}}
(1-s)^{a_{\nu3}}
\prod_{h=1}^{M_\nu}
P_{\nu h}(r,s;D,q,\alpha)^{\lambda_{\nu h}}
\]
以及上述对象对若干 \(\lambda_{\nu h}\) 的有限阶参数导数。

其中：

1. \(P_{\nu h}\) 是由
   \[
   U,V,\mathscr D,F_x^\#,F_y^\#,H^\#,
   A_x^\#,A_y^\#,A_\gamma^\#,
   X_i,Y_i,G_i,
   \mathcal Q_i,
   \text{front quadratics},
   \text{Euler/Hermite factors}
   \]
   经 V6 参数化代数规则和 \(\xi,\eta\to r,s\) 紧化生成的有限多项式；

2. \(C_\nu\) 不是拟合系数，完全由原始几何/材料参数、\((D,q,\alpha)\) 及有限代数卷积产生；

3. \(\lambda_{\nu h}\) 是 exact-period 的指数参数，不是结构未知量。

---

## 4. 标准 exact-period 对象

定义标准 relative/incomplete period

\[
\boxed{
\mathfrak A_\nu(D,q,\alpha)
=
\mathfrak A[
\mathbf a_\nu,\boldsymbol\lambda_\nu;
\mathcal C_\nu
](\mathbf c_\nu)
}
\]

其标准积分定义为
\[
\mathfrak A[
\mathbf a,\boldsymbol\lambda;\mathcal C
](\mathbf c)
=
\int_{\mathcal C}
r^{a_0}(1-r)^{a_1}
s^{a_2}(1-s)^{a_3}
\prod_{h=1}^{M}
P_h(r,s;\mathbf c)^{\lambda_h}
\,dr\,ds.
\]

这里的 \(\mathcal C_\nu\) 是由连续完整半波和解析材料 front 决定的 relative algebraic cycle。

对数项不用重新定义新积分：
\[
\boxed{
\log P_k\,
P_k^{\lambda_k}
=
\frac{\partial}{\partial\lambda_k}
P_k^{\lambda_k}.
}
\]

若存在多个 log 因子，则用有限多重参数导数
\[
\partial_{\boldsymbol\lambda}^{\mathbf m_\nu}.
\]

\(\arctan\) 用复对数恒等式编入同一 period family，因此不增加新的积分类型。

---

## 5. 有限 index set 的生成规则

对
\[
j\in\{P,q,\alpha\},
\]
定义有限索引集
\[
\boxed{
I_j
=
\bigcup_{b\in\mathcal B}
I_{jb}.
}
\]

其中 \(I_{jb}\) 由如下确定性流程生成：

\[
K_{jb}
\rightarrow
\text{Euler rationalization}
\rightarrow
\text{Hermite/RootSum primitive}
\rightarrow
\text{front endpoint difference}
\rightarrow
(r,s)\text{ compactification}
\rightarrow
\text{factor expansion}
\rightarrow
\text{period term descriptor}.
\]

没有人工删项、没有拟合、没有空间采样。

因此 \(I_j\) 必为有限集合。

---

## 6. 三个已经编译完成的 exact functions

定义三类总体物理 prefactor：

\[
\boxed{
C_P^{(0)}=
-\frac{f_cb t_r}{\pi^2},
}
\]

\[
\boxed{
C_q^{(0)}=
\frac{f_c\varepsilon_0b\ell t_r}{\pi^2},
}
\]

\[
\boxed{
C_\alpha^{(0)}=
\frac{f_c\varepsilon_0b\ell t_r}{\pi^2}.
}
\]

于是 NC-M6 的最终轴力函数为

\[
\boxed{
P(D,q,\alpha)
=
C_P^{(0)}
\sum_{\nu\in I_P}
C_{P\nu}(D,q,\alpha)\,
\partial_{\boldsymbol\lambda}^{\mathbf m_{P\nu}}
\mathfrak A_{P\nu}(D,q,\alpha).
}
\]

面外广义平衡函数为

\[
\boxed{
R_q(D,q,\alpha)
=
C_q^{(0)}
\sum_{\nu\in I_q}
C_{q\nu}(D,q,\alpha)\,
\partial_{\boldsymbol\lambda}^{\mathbf m_{q\nu}}
\mathfrak A_{q\nu}(D,q,\alpha).
}
\]

膜内重分布平衡函数为

\[
\boxed{
R_\alpha(D,q,\alpha)
=
C_\alpha^{(0)}
\sum_{\nu\in I_\alpha}
C_{\alpha\nu}(D,q,\alpha)\,
\partial_{\boldsymbol\lambda}^{\mathbf m_{\alpha\nu}}
\mathfrak A_{\alpha\nu}(D,q,\alpha).
}
\]

这三式是 NC-M6 对应 NC-M4 最终 exact-period 三函数的正式同构形式。

---

## 7. 系数的普适组成规则

任意
\[
C_{j\nu}
\]
必须由下列链唯一生成：

\[
\{b,\ell,t_r,q_0,E_0,f_c,f_t,\varepsilon_{c0},\nu,
\text{NC-M6 material-instance parameters},
D,q,\alpha\}
\]

\[
\Downarrow
\]

\[
\{k,\kappa,\rho,x_{cr},M,B\}
\]

\[
\Downarrow
\]

\[
\{\mathscr D,F_x^\#,F_y^\#,H^\#,
A_x^\#,A_y^\#,A_\gamma^\#\}
\]

\[
\Downarrow
\]

\[
\{X_0,X_1,Y_0,Y_1,G_0,G_1\}
\]

\[
\Downarrow
\]

\[
\{\Delta_0,\Delta_1,\Sigma_0,\Sigma_1,
\mathcal Q_0,\mathcal Q_1,\mathcal Q_2\}
\]

\[
\Downarrow
\]

\[
\{L,\beta,R,\lambda_1,\lambda_2\}
\]

\[
\Downarrow
\]

\[
\{\text{branch material pair},s_1,s_2\}
\]

\[
\Downarrow
\]

\[
\{\Sigma_x,\Sigma_y,\Sigma_{xy}\}
\]

\[
\Downarrow
\]

\[
\{K_P,K_q,K_\alpha\}
\]

\[
\Downarrow
\]

\[
\{\Phi_{jb},\Delta F_{jb}\}
\]

\[
\Downarrow
\]

\[
\{C_{j\nu},\mathbf a_{j\nu},
\boldsymbol\lambda_{j\nu},
\mathbf m_{j\nu},
\mathbf c_{j\nu},
\mathcal C_{j\nu}\}.
\]

任何 coefficient 若不能沿此链回溯，不允许进入正式三函数。

---

## 8. 当前形式已经没有普通空间积分变量

最终三函数中不再出现

\[
x,\ y,\ z,\ X,\ Y,\ \zeta,\ \xi,\ \eta,\ r,\ s
\]

作为待积分变量。

它们只存在于标准特殊函数
\[
\mathfrak A_\nu
\]
的定义层，不属于后续结构求解未知量。

所以当前可正式记为

\[
\boxed{
\texttt{NC\_M6\_FULL\_EXACT\_INTEGRATION\_REPRESENTATION = PASS}.
}
\]

这与 NC-M4 的 `EXACT_ANALYTIC_REPRESENTATION / ZERO_SPATIAL_QUADRATURE` 是同一层级的完成状态。

---

## 9. 后续直接进入极限联立

普通平衡：

\[
\boxed{
R_q(D,q,\alpha)=0,
}
\]

\[
\boxed{
R_\alpha(D,q,\alpha)=0.
}
\]

随后对同一组三函数做同源解析微分，构造

\[
J_{\lim}
=
\begin{bmatrix}
P_D&P_q&P_\alpha\\
R_{q,D}&R_{q,q}&R_{q,\alpha}\\
R_{\alpha,D}&R_{\alpha,q}&R_{\alpha,\alpha}
\end{bmatrix},
\]

极限条件

\[
\boxed{
\det J_{\lim}=0.
}
\]

因此最终三元联立为

\[
\boxed{
\begin{cases}
R_q(D,q,\alpha)=0,\\
R_\alpha(D,q,\alpha)=0,\\
\det J_{\lim}(D,q,\alpha)=0.
\end{cases}
}
\]

求得
\[
(D_u,q_u,\alpha_u),
\]
然后
\[
\boxed{
P_u=P(D_u,q_u,\alpha_u).
}
\]

本节点不执行该求解；这里只完成积分编译。
