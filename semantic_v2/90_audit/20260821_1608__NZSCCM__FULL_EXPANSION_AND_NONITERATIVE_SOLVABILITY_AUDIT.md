# NZ-SCCM — PMV1-C73 FULL EXPANSION AND NONITERATIVE SOLVABILITY AUDIT

时间：2026-08-21 16:08 +08:00
状态：`FORMAL_EXPANSION_CLOSED / GENERIC_NONITERATIVE_PRODUCTION_SOLVE_FAIL`

## 0. 审计问题

本文件只回答两个问题：

1. 能否把 PMV1-C73 从 Nguyen 二阶运动学一直写成只含原始输入、D、q 的两个有限解析方程，而不留下未定义的场变量、Ritz 系数、空间积分点或经验修正？
2. 这两个方程对陌生试件能否进一步变成一个工程上可用的、无需路径追踪和非线性迭代的“一次直接求 Pu”算法？

结论先行：

```text
QUESTION 1 = PASS
QUESTION 2 = FAIL FOR GENERIC PMV1-C73
```

即：理论在形式上可以完全有限代数闭合；但闭合后的通用二元多项式阶数过高，不能合理宣称存在一个工程上可接受的通用 resultant/companion 一次求根器。

---

## 1. 原始输入与唯一结构未知量

钢箱类原始输入：

```text
b, ell, tc, tf, tw, ls,
fc, E0, eps0, nu,
Es, nu_s, fy,
A0
```

RC 类原始输入：

```text
b, ell, tp,
fc, E0, eps0, nu,
Es, fy,
A0,
{rho_sx,l, rho_sy,l, z_l}
```

唯一结构未知量：

```text
D, q
```

并且 `q0=A0/b` 必须立刻代回；它不是独立待定参数。

---

## 2. 基础多项式系数，不保留空间函数占位符

统一取

\[
u=\sin(\pi x/b),\quad v=\sin(\pi y/\ell),\quad \zeta=2z/t_c.
\]

任意场只允许以系数数组表示：

\[
F(u,v,\zeta)=\sum_{i,j,k\ge0}F_{ijk}(D,q)u^iv^j\zeta^k.
\]

乘法系数严格定义为有限卷积：

\[
(FG)_{ijk}=\sum_{p=0}^{i}\sum_{r=0}^{j}\sum_{s=0}^{k}
F_{prs}G_{i-p,j-r,k-s}.
\]

导数不数值差分：

\[
(F_{,D})_{ijk}=\partial F_{ijk}/\partial D,
\qquad
(F_{,q})_{ijk}=\partial F_{ijk}/\partial q.
\]

### 2.1 concrete-core strain coefficients

除下列项外全部为零：

\[
(e_x)_{000}=\nu D,
\]
\[
(e_x)_{020}=\frac{\pi^2q(q+2A_0/b)}{2\varepsilon_0},
\]
\[
(e_x)_{220}=-\frac{\pi^2q(q+2A_0/b)}{2\varepsilon_0},
\]
\[
(e_x)_{111}=\frac{\pi^2t_cq}{2\varepsilon_0b},
\]

\[
(e_y)_{000}=-D,
\]
\[
(e_y)_{200}=\frac{\pi^2b^2q(q+2A_0/b)}{2\varepsilon_0\ell^2},
\]
\[
(e_y)_{220}=-\frac{\pi^2b^2q(q+2A_0/b)}{2\varepsilon_0\ell^2},
\]
\[
(e_y)_{111}=\frac{\pi^2bt_cq}{2\varepsilon_0\ell^2}.
\]

剪应变只通过 `g^2,gg_q,g_q^2,gg_qq` 进入正式代数；其系数均由

\[
\frac{\pi^4}{\varepsilon_0^2\ell^2}(1-u^2)(1-v^2)
[bq(q+2A_0/b)uv-t_cq\zeta]^2
\]

以及对 q 的解析导数直接卷积得到，不需要 `g` 的独立空间采样。

---

## 3. I1/I2 的系数生成完全闭合

### 3.1 I1

\[
(I_1)_{ijk}=\frac{(e_x)_{ijk}+(e_y)_{ijk}}{1-\nu}.
\]

因此每个 `I1_ijk` 已只含原始输入、D、q。

### 3.2 I2

\[
I_2=\frac{\nu e_x^2+(1+\nu^2)e_xe_y+\nu e_y^2}{(1-\nu^2)^2}
-\frac{g^2}{4(1+\nu)^2}.
\]

故每个系数严格为

\[
\boxed{
(I_2)_{ijk}=\frac{1}{(1-\nu^2)^2}
\left[
\nu\sum_{a\le(i,j,k)}(e_x)_a(e_x)_{(i,j,k)-a}
+(1+\nu^2)\sum_{a\le(i,j,k)}(e_x)_a(e_y)_{(i,j,k)-a}
+\nu\sum_{a\le(i,j,k)}(e_y)_a(e_y)_{(i,j,k)-a}
\right]
-\frac{(g^2)_{ijk}}{4(1+\nu)^2}.
}
\]

这已消除 `I2` 作为黑盒。

---

## 4. N48 每个材料系数的生成式

对 F=U,C,T^7，根点与约束式采用最终理论文件的 C1 constrained normal-equation 公式：

\[
a_n^{(F)}=h_n^{-1}g_n^{(F)}-h_n^{-1}\sum_{\alpha=1}^2A_{\alpha n}
\sum_{\beta=1}^2(G^{-1})_{\alpha\beta}
\left[\sum_{m=0}^{48}A_{\beta m}h_m^{-1}g_m^{(F)}-b_\beta^{(F)}\right].
\]

其中每个 `g_n` 是 49 项明确有限和，`G^{-1}` 是显式 2x2 逆矩阵。因此这些系数不存在未定义数值表。

### 4.1 T 的 minimax 系数

T 不能诚实地写成简单闭式数列。它的每个 `a_n^(T)` 是唯一 C1 约束 minimax 多项式的系数。完全有限定义为：

未知

\[
a_0,\ldots,a_{48},E,\lambda_0^*,\ldots,\lambda_{46}^*.
\]

满足两个 C1 约束，及 47 个 alternation 条件

\[
T(\lambda_j^*)-\sum_{n=0}^{48}a_n\mathcal C_n(\xi(\lambda_j^*))=(-1)^jE,
\]

并满足内部 alternation 点的驻值条件

\[
T'(\lambda_j^*)-\sum_{n=0}^{48}a_n\frac{2n}{\lambda_b-\lambda_a}
\mathcal U_{n-1}(\xi(\lambda_j^*))=0.
\]

端点按 alternation 定理纳入。该材料编译系统只由 R10 材料函数和声明区间决定，与任何结构荷载无关。

因此：`T minimax coefficient generation = finite deterministic material preprocessing`，但不是 elementary closed-form coefficients。

---

## 5. Cayley-Hamilton pair 的每个空间系数

定义

\[
(K_1)_{ijk}=\frac{2(I_1)_{ijk}-2(\lambda_a+\lambda_b)\delta_{i0}\delta_{j0}\delta_{k0}}
{\lambda_b-\lambda_a},
\]

\[
(K_2)_{ijk}=\frac{4(I_2)_{ijk}-2(\lambda_a+\lambda_b)(I_1)_{ijk}
+(\lambda_a+\lambda_b)^2\delta_{i0}\delta_{j0}\delta_{k0}}
{(\lambda_b-\lambda_a)^2}.
\]

对 n>=1：

\[
(A_{n+1})_{ijk}=-2\sum_{a\le(i,j,k)}(K_2)_a(B_n)_{(i,j,k)-a}-(A_{n-1})_{ijk},
\]

\[
(B_{n+1})_{ijk}=2(A_n)_{ijk}
+2\sum_{a\le(i,j,k)}(K_1)_a(B_n)_{(i,j,k)-a}-(B_{n-1})_{ijk}.
\]

初值：`A0_000=1, B1_000=1`，其余初值系数为零。

故

\[
(A_F)_{ijk}=\sum_{n=0}^{48}a_n^{(F)}(A_n)_{ijk},
\]

\[
(B_F)_{ijk}=\sum_{n=0}^{48}a_n^{(F)}(B_n)_{ijk}.
\]

所有 CC/TC/TT pair 均只使用上述有限卷积，不再存在未定义 `A_S,B_S`：例如

\[
(A_{CC})_{ijk}=\sum_{a+b+c=(i,j,k)}(A_C)_a(A_C)_b(A_C)_c
+\sum_{a+b+c+d=(i,j,k)}(A_C)_a(B_C)_b(K_1)_c(A_C)_d
+\sum_{a+b+c+d=(i,j,k)}(B_C)_a(B_C)_b(K_2)_c(A_C)_d,
\]

其余 `B_CC,A_TC,B_TC,A_TT,B_TT` 逐项由最终理论文件 14.1--14.8 的有限乘法式和本节卷积定义唯一生成。

最终每个 `A_S,ijk,B_S,ijk` 因而只依赖：

```text
raw geometry/material inputs, D,q,
N48 material coefficients generated above.
```

---

## 6. Concrete axial-stress and q-work coefficients

因为

\[
Y_{yy}=\frac{2X_{yy}-(\lambda_a+\lambda_b)}{\lambda_b-\lambda_a},
\]

每个轴向归一化应力系数为

\[
\boxed{
(S_{yy})_{ijk}=(A_S)_{ijk}
+\sum_{a\le(i,j,k)}(B_S)_a(Y_{yy})_{(i,j,k)-a}.
}
\]

`Yyy_ijk` 由原始 `ex,ey` 系数直接线性生成。

混凝土 q-work 每个系数完全写为最终理论 15.1 中各项的卷积，例如

\[
(Q_c)_{ijk}=(1+\nu)
\left[(A_S*I_{1,q})_{ijk}
+\frac{2}{\lambda_b-\lambda_a}
(B_S*(I_1I_{1,q}-I_{2,q}-\tfrac{\lambda_a+\lambda_b}{2}I_{1,q}))_{ijk}
\right]
-\nu(I_{1,q}*(2A_S+B_SK_1))_{ijk},
\]

而每个乘积符号 `*` 均严格等于第 2 节的三重有限和。因此不存在未计算的空间函数。

---

## 7. CAP-C73 每个钢材系数

物理 target：

\[
\alpha(r)=1\ (r\le1),\qquad \alpha(r)=r^{-1/2}\ (r>1).
\]

在 `0<=r<=25/4`：

\[
\alpha_{73}(r)=\sum_{n=0}^{73}d_n\mathcal C_n(8r/25-1),
\]

其中每个 `d_n` 已有闭式有限和；不存在拟合节点。

对任意钢相位，trial strain/stress 系数由 Nguyen 基础系数直接生成；von-Mises ratio 系数：

\[
(r_s)_{ijk}=\frac1{f_y^2}
\left[(\sigma_x^{tr}*\sigma_x^{tr})_{ijk}
-(\sigma_x^{tr}*\sigma_y^{tr})_{ijk}
+(\sigma_y^{tr}*\sigma_y^{tr})_{ijk}
+3(\tau^{tr}*\tau^{tr})_{ijk}\right].
\]

定义 `G0_000=1`，

\[
(G_1)_{ijk}=\frac8{25}(r_s)_{ijk}-\delta_{i0}\delta_{j0}\delta_{k0},
\]

\[
(G_{n+1})_{ijk}=2\sum_{a\le(i,j,k)}(G_1)_a(G_n)_{(i,j,k)-a}-(G_{n-1})_{ijk}.
\]

则

\[
(\alpha_{73})_{ijk}=\sum_{n=0}^{73}d_n(G_n)_{ijk}.
\]

最终钢轴向应力系数：

\[
(\sigma_y^s)_{ijk}=\sum_{a\le(i,j,k)}(\alpha_{73})_a(\sigma_y^{tr})_{(i,j,k)-a}.
\]

钢 q-work 系数同理：

\[
(Q_s)_{ijk}=\sum_{a\le(i,j,k)}(\alpha_{73})_a(Q_s^{tr})_{(i,j,k)-a}.
\]

腹板和钢筋仅将 trial stress 换为一维 `Es*eps0*e_y` 或相应方向应变，系数公式完全相同。

---

## 8. D15 之后不再保留 Pc/Pw/Psh 中间黑盒

定义精确矩：

\[
M_i=\sqrt\pi\frac{\Gamma((i+1)/2)}{\Gamma((i+2)/2)},
\quad
Z_k=\frac{1+(-1)^k}{k+1}.
\]

### 8.1 steel-shell final coefficient sums

总轴力直接写为

\[
\boxed{
P(D,q)=
-\frac{f_cb t_c}{2\pi^2}\left(1-\frac{t_w}{l_s}\right)
\sum_{ijk}(S_{yy})_{ijk}M_iM_jZ_k
-\frac{bt_ct_w}{2\pi^2l_s}
\sum_{ijk}(\sigma_y^w)_{ijk}M_iM_jZ_k
-\frac{bt_f}{2\pi^2}\sum_{s=\pm1}\sum_{ijk}(\sigma_y^{f,s})_{ijk}M_iM_jZ_k.
}
\]

总 q 平衡式直接写为

\[
\boxed{
R(D,q)=
\frac{f_c\varepsilon_0b\ell t_c}{2\pi^2}\left(1-\frac{t_w}{l_s}\right)
\sum_{ijk}(Q_c)_{ijk}M_iM_jZ_k
+\frac{b\ell t_ct_w}{2\pi^2l_s}
\sum_{ijk}(Q_w)_{ijk}M_iM_jZ_k
+\frac{b\ell t_f}{2\pi^2}\sum_{s=\pm1}\sum_{ijk}(Q_{f,s})_{ijk}M_iM_jZ_k.
}
\]

此处出现的每个 coefficient array 已在 2--7 节给出从原始输入出发的有限和/递推计算式。

### 8.2 RC final coefficient sums

令

\[
\chi_c=1-\sum_l(\rho_{s,x,l}+\rho_{s,y,l}).
\]

但最终必须代回，不把 `chi_c` 当输入。于是

\[
\boxed{
P(D,q)=
-\frac{f_cb t_p}{2\pi^2}
\left[1-\sum_l(\rho_{s,x,l}+\rho_{s,y,l})\right]
\sum_{ijk}(S_{yy})_{ijk}M_iM_jZ_k
-\frac{bt_p}{\pi^2}\sum_l\rho_{s,y,l}\sum_{ij}(\sigma_{s,y,l})_{ij}M_iM_j.
}
\]

\[
\boxed{
R(D,q)=
\frac{f_c\varepsilon_0b\ell t_p}{2\pi^2}
\left[1-\sum_l(\rho_{s,x,l}+\rho_{s,y,l})\right]
\sum_{ijk}(Q_c)_{ijk}M_iM_jZ_k
+\frac{b\ell t_p}{\pi^2}\sum_l\sum_{d=x,y}\rho_{s,d,l}\sum_{ij}(Q_{s,d,l})_{ij}M_iM_j.
}
\]

---

## 9. 最终两个联立方程已经可以不保留 Pc/Rc/As/Bs 等整体黑盒

对任意 phase-summed `P(D,q),R(D,q)` 上式，直接逐项微分有限系数：

\[
P_D=\sum \frac{\partial P_{ijk}}{\partial D}\,M_iM_jZ_k,
\quad
P_q=\sum \frac{\partial P_{ijk}}{\partial q}\,M_iM_jZ_k,
\]

\[
R_D=\sum \frac{\partial R_{ijk}}{\partial D}\,M_iM_jZ_k,
\quad
R_q=\sum \frac{\partial R_{ijk}}{\partial q}\,M_iM_jZ_k.
\]

最终未知量仅为 D,q：

\[
\boxed{F_1(D,q)=R(D,q)=0,}
\]

\[
\boxed{F_2(D,q)=P_D(D,q)R_q(D,q)-P_q(D,q)R_D(D,q)=0.}
\]

这两式中的每个系数均由本文件 2--8 节有限和/递推产生；不再需要空间离散、Ritz、膜自由度或加载路径。

因此“完全展开为有限系数计算理论”这一任务通过。

---

## 10. 但是：generic direct noniterative Pu solve 的阶数审计失败

形式闭合不等于工程求解闭合。

按原始 D,q 最高次数传播：

### 10.1 concrete

- `ex,ey`: deg_D<=1, deg_q<=2
- `I1`: <=(1,2)
- `I2,K2`: <=(2,4)
- 48 阶 CH：`A_48 <= (48,96)`, `B_48 <= (47,94)`
- CC/TT interaction 后 concrete stress：最高约 `(144,288)`
- concrete axial P：最高约 `(144,288)`
- concrete q-work R：最高约 `(145,289)`

### 10.2 C73 steel phases

- trial stress: <=(1,2)
- von-Mises r: <=(2,4)
- degree-73 alpha polynomial: <=(146,292)
- capped axial stress: <=(147,294)
- capped q-work: <=(147,295)

故总体系保守上界：

\[
\deg_D P\le147,\qquad \deg_qP\le294,
\]

\[
\deg_D R\le147,\qquad \deg_qR\le295.
\]

极限式

\[
L=P_D R_q-P_q R_D
\]

最高约

\[
\deg_D L\le293,\qquad \deg_qL\le588.
\]

若机械地对 q 做 resultant，`Res_q(R,L)` 的 D 次数保守上界可达到

\[
295\times293+588\times147=172871.
\]

这意味着 generic companion/resultant 一次全根方案可能对应十万量级以上的单变量代数次数。即使实际稀疏性会大幅降低有效规模，也没有依据声称所有陌生试件都能以一个小型非迭代矩阵直接解决。

因此：

```text
FINITE FORMAL THEORY = YES
LOW-ORDER CLOSED PU FORMULA = NO
GENERIC SMALL COMPANION MATRIX = NO
NO-NONLINEAR-SOLVE PRODUCTION CLAIM = REJECTED
```

---

## 11. 最严格的最终裁决

PMV1-C73 已经达到：

1. 从二阶运动学到材料 current map 完全有限解析；
2. 从材料到空间积分完全精确矩；
3. 从多相组装到 F1,F2 完全有限代数；
4. 不依赖已知 Pu、试验值、Zhou 值或路径追踪来定义极限。

但是它没有达到用户真正希望的最后一步：

> 对任意陌生试件，不进行大规模非线性/代数求根，也能像设计公式一样直接得到 Pu。

高阶材料编译与非线性交互使最终 F1,F2 的通用代数阶数太高。若继续坚持当前 PMV1-C73 材料复杂度，则求解后端仍不可避免需要高阶多项式根隔离、同伦、区间 Newton 或其他数值代数方法之一。

这和有限元加载追踪不同，但仍然是一个数值求根问题；不能把它包装成低成本闭式极限公式。

因此本分支的最终身份应为：

`FORMALLY_COMPLETE_ANALYTIC-SPECTRAL THEORY, BUT NOT THE DESIRED SIMPLE DIRECT ULTIMATE-LOAD THEORY`.
