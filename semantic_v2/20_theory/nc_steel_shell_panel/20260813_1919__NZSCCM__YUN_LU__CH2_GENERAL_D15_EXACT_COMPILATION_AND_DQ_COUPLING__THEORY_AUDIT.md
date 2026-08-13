# NZ-SCCM — 云露第二章原始大挠度钢壳模型 general-D15 精确编译与全局 D-q 耦合审计

**Timestamp:** 2026-08-13 19:19 +08:00  
**Status:** SOURCE-GROUNDED THEORY AUDIT + EXACT SYMBOLIC COMPILATION + D-q COUPLING DERIVATION  
**Parent governance:** `20260813_1834__NZSCCM__NC_PANEL__ENERGY_MINIMUM_HALFWAVE_R10_N48C1MM_D15_DIRECT_LIMIT__LOCKED_BASELINE.md`  
**Formal spatial quadrature:** 0  
**Structural calibration:** NO

---

## 0. 本轮目标与边界

严格以云露硕士论文第二章 2.2 节为原始局部钢壳理论来源，从：

```text
挠曲函数 2-19 / 初始缺陷 2-20
-> Karman 平衡式 2-22
-> 变形协调式 2-23
-> Airy 应力函数 2-25~2-27 / Table 2-1
-> Galerkin 2-28~2-31
-> 闭式路径 2-32~2-34
-> 轴向应力场 2-35~2-37
-> 最大应力达到 fy 的极限定义
```

逐式改写为 current NZ-SCCM `ONE_CONTINUOUS_COMPLETE_HALFWAVE + general-D15` 解析形式，并证明得到的 `k_crx`、`k_p` 与云露闭式表达完全一致。

本轮同时接受用户指定的钢材简化：

```text
STEEL = IDEAL ELASTIC-PERFECTLY-PLASTIC
YUN_LU_ELASTIC_LARGE_DEFLECTION_PATH = retained until first local yield
NO_STRAIN_HARDENING = YES
```

云露正文的极限定义本身就是“板面最大轴向压应力首先达到 fy 时达到极限，忽略塑性发挥带来的微弱提高”。因此首版理想弹塑性接口采用 `first-yield cap / zero hardening`，不在本轮发明屈服区继续扩展后的新应力重分布理论。

---

# 1. 从全板 m 波改写为一个连续完整代表半波

云露式 (2-19)、(2-20)：

\[
w=A\left(1-\cos\frac{2m\pi x}{a}\right)\left(1-\cos\frac{2\pi y}{b}\right),
\]

\[
w_0=A_0\left(1-\cos\frac{2m\pi x}{a}\right)\left(1-\cos\frac{2\pi y}{b}\right).
\]

令纵向一个完整局部屈曲波的长度

\[
\boxed{\ell=\frac{a}{m}},
\]

并在单个代表完整半波内定义

\[
X=\frac{\pi x}{\ell},\qquad Y=\frac{\pi y}{b},\qquad X,Y\in[0,\pi].
\]

则云露形函数严格变成

\[
\boxed{w=A(1-\cos2X)(1-\cos2Y)=4A\sin^2X\sin^2Y},
\]

\[
\boxed{w_0=4A_0\sin^2X\sin^2Y}.
\]

因此它不是近似落入 general-D15，而是**本身就是有限三角多项式**。

注意：云露参数 `A` 不是最大挠度本身；在波峰 `X=Y=pi/2`：

\[
\boxed{w_{\max}=4A},\qquad \boxed{w_{0,\max}=4A_0}.
\]

这是后续与全局 `q=A_g/b_g` 映射时必须保留的 1/4 因子。

更重要的是，云露原式中的 `m` 和 `a` 只通过局部半波长 `ell=a/m` 进入。定义局部半波长宽比

\[
\boxed{r=\frac{\ell}{b}=\frac{a/b}{m}},
\]

则后续全部闭式系数只依赖 `r`。这与 NZ-SCCM 的“只计算一个连续完整代表半波”完全一致；重复的纵向相同半波不产生新的理论自由度或空间积分点。

---

# 2. 云露 Karman 兼容方程的有限谐波闭合

令

\[
\psi=(1-\cos2X)(1-\cos2Y),\qquad w=A\psi,\qquad w_0=A_0\psi,
\]

并定义

\[
\boxed{K=A^2+2A_0A}.
\]

云露式 (2-23) 的右端可严格因式分解为

\[
E_sK\left(\psi_{,xy}^2-\psi_{,xx}\psi_{,yy}\right).
\]

将其展开到有限谐波族

\[
\cos(2qX)\cos(2sY),\qquad q,s\in\{0,1,2\},
\]

右端系数在提取公共因子

\[
\frac{8\pi^4E_sK}{\ell^2b^2}
\]

后得到严格的 3x3 矩阵

\[
\boxed{
M=
\begin{bmatrix}
0&1&-1\\
1&-2&1\\
-1&1&0
\end{bmatrix}
}
\]

其中行为 `s=0,1,2`，列为 `q=0,1,2`。

对每个非零谐波，双调和算子的本征因子为

\[
\boxed{\Lambda_{qs}=16\pi^4\left(\frac{q^2}{\ell^2}+\frac{s^2}{b^2}\right)^2}.
\]

因此应力函数特解

\[
F_p=K\sum_{q=0}^{2}\sum_{s=0}^{2}f_{qs}\cos(2qX)\cos(2sY)
\]

的系数直接是

\[
\boxed{
f_{qs}=\frac{8\pi^4E_s}{\ell^2b^2}\frac{M_{sq}}{\Lambda_{qs}}
}
\]

（`q=s=0` 项为 0）。

展开后得到：

\[
f_{01}=\frac{b^2E_s}{2\ell^2},\qquad
f_{02}=-\frac{b^2E_s}{32\ell^2},
\]

\[
f_{10}=\frac{\ell^2E_s}{2b^2},\qquad
f_{11}=-\frac{\ell^2b^2E_s}{(\ell^2+b^2)^2},
\]

\[
f_{12}=\frac{\ell^2b^2E_s}{2(4\ell^2+b^2)^2},
\]

\[
f_{20}=-\frac{\ell^2E_s}{32b^2},\qquad
f_{21}=\frac{\ell^2b^2E_s}{2(\ell^2+4b^2)^2},\qquad
f_{22}=0.
\]

将 `ell=a/m` 代回，即逐项恢复云露 Table 2-1。

```text
TABLE_2_1_FROM_GENERAL_D15_HARMONIC_COMPILATION = EXACT PASS
```

---

# 3. 为什么这些积分是 general-D15，而不是新的 Fourier 数值积分

所有云露谐波都可有限代数化：

\[
\cos2X=1-2\sin^2X,
\]

\[
\cos4X=1-8\sin^2X\cos^2X,
\]

\[
\sin2X=2\sin X\cos X,
\]

Y 方向同理。

因此任何 Karman / Airy / Galerkin 被积项最终都属于

\[
Q(X,Y)=\sum c_{prus}\sin^pX\cos^rX\sin^uY\cos^sY,
\]

其积分就是 current general-D15 的

\[
\mathscr D[Q]=\sum c_{prus}J_{pr}J_{us}.
\]

本轮实际推导只需要三组归一化一维矩：

\[
I_1(j)=\frac1\pi\int_0^\pi\cos(2jX)\cos2X(1-\cos2X)dX,
\]

\[
I_2(j)=\frac1\pi\int_0^\pi\cos(2jX)(1-\cos2X)^2dX,
\]

\[
I_3(j)=\frac1\pi\int_0^\pi\sin(2jX)\sin2X(1-\cos2X)dX.
\]

由 D15 的 Beta/三角矩逐项得到

\[
\boxed{I_1=(-1/2,\ 1/2,\ -1/4)},
\]

\[
\boxed{I_2=(3/2,\ -1,\ 1/4)},
\]

\[
\boxed{I_3=(0,\ 1/2,\ -1/4)},
\]

对应 `j=0,1,2`。

没有使用 Gauss、Simpson、adaptive quadrature 或空间采样点。

---

# 4. Galerkin 弯曲项：精确恢复 k_crx

云露式 (2-28) 的试函数就是

\[
\psi=(1-\cos2X)(1-\cos2Y).
\]

定义

\[
k_x=\frac{2\pi}{\ell},\qquad k_y=\frac{2\pi}{b}.
\]

抗弯项的 D15 精确投影为

\[
\boxed{
G_w=
\frac{D_s}{t_s}A\frac{\ell b}{4}
\left(3k_x^4+2k_x^2k_y^2+3k_y^4\right)
}.
\]

齐次应力函数

\[
F_h=-\frac{p_x}{2t_s}y^2
\]

对应的精确 Galerkin 投影为

\[
\boxed{
G_h=
\frac{3\ell b k_x^2}{4t_s}\,p_x(A+A_0)
}.
\]

先忽略特解薄膜项，由 `G_w-G_h=0` 得到

\[
p_x^{(b)}=
\frac{\pi^2D_s}{b^2}
\,k_{crx}(r)\frac{A}{A+A_0},
\]

其中

\[
\boxed{
k_{crx}(r)=\frac{4(3r^4+2r^2+3)}{3r^2}
}.
\]

恢复 `r=(a/b)/m=beta/m` 后即为云露式 (2-34)：

\[
\boxed{
k_{crx}=\frac{4(3m^4+2m^2\beta^2+3\beta^4)}{3m^2\beta^2}}.
\]

```text
KCRX_FROM_GENERAL_D15 = EXACT PASS
```

---

# 5. Airy 特解薄膜项：精确恢复 k_p

对单个 Airy 谐波 `cos(2qX)cos(2sY)`，其在云露式 (2-30) 中的 Galerkin 投影可完全由 `I1,I2,I3` 写成：

\[
G_{qs}=-\ell b k_x^2k_y^2
\left[
 s^2 I_1(q)I_2(s)
+q^2 I_2(q)I_1(s)
+2qsI_3(q)I_3(s)
\right].
\]

因此

\[
G_p=K(A+A_0)\sum_{q,s}f_{qs}G_{qs}.
\]

将 Table 2-1 的八个非零系数代入并做**纯代数约化**，可写成

\[
p_x^{(m)}=
\frac{E_st_s\pi^2}{12b^2}K\,k_p(r).
\]

利用

\[
D_s=\frac{E_st_s^3}{12(1-\nu_s^2)},
\]

即

\[
\boxed{
p_x^{(m)}=
\frac{\pi^2D_s}{b^2}
\,k_p(r)(1-\nu_s^2)\frac{2A_0A+A^2}{t_s^2}
}.
\]

D15 得到的系数恰为

\[
\boxed{
k_p(r)=
\frac{
272r^{16}+2856r^{14}+11273r^{12}+23146r^{10}+31506r^8
+23146r^6+11273r^4+2856r^2+272
}
{r^2(r^2+1)^2(r^2+4)^2(4r^2+1)^2}
}.
\]

将 `r=beta/m` 代回，逐项恢复云露论文第 21 页给出的 `k_p(m,beta)` 多项式比值。

```text
KP_FROM_GENERAL_D15 = EXACT SYMBOLIC PASS
```

---

# 6. 云露式 (2-32) 的完整逐项复现

由

\[
G_w-G_p-G_h=0
\]

直接得到

\[
\boxed{
p_x=
\left[
 k_{crx}\frac{A}{A+A_0}
+k_p(1-\nu_s^2)\frac{2A_0A+A^2}{t_s^2}
\right]
\frac{\pi^2D_s}{b^2}
}.
\]

这与云露式 (2-32) 完全一致。

并且在理论最低局部方形半波 `r=1`：

\[
\boxed{k_{crx}(1)=\frac{32}{3}=10.666666\ldots},
\]

\[
\boxed{k_p(1)=\frac{1066}{25}=42.64}.
\]

进一步：

\[
k'_{crx}(1)=0,\qquad k''_{crx}(1)=32>0,
\]

\[
k'_p(1)=0,\qquad k''_p(1)=\frac{75064}{625}>0.
\]

因此云露正文“当 `m=a/b` 时二者同时取最小值，`k_crx=10.67, k_p=42.64`”被 exact D15 独立恢复。

```text
YUN_LU_EQ_2_32 = EXACT PASS
YUN_LU_MINIMUM_HALFWAVE = EXACT PASS
ONE_COMPLETE_HALFWAVE_REDUCTION = EXACT PASS
```

---

# 7. 应力场 2-35~2-37 的 D15 复核与一个源内印刷不一致

由

\[
F=F_p-\frac{p_x}{2t_s}y^2,
\qquad
\sigma_x=\frac{\partial^2F}{\partial y^2},
\]

Table 2-1 唯一导出的轴向应力场，在一个代表完整半波内为

\[
\boxed{
\begin{aligned}
\sigma_x={}&
-\frac{2KE_s\pi^2}{\ell^2}\cos2Y
+\frac{KE_s\pi^2}{2\ell^2}\cos4Y\\
&+\frac{4\ell^2KE_s\pi^2}{(\ell^2+b^2)^2}\cos2X\cos2Y\\
&-\frac{2\ell^2KE_s\pi^2}{(\ell^2+4b^2)^2}\cos4X\cos2Y\\
&-\frac{8\ell^2KE_s\pi^2}{(4\ell^2+b^2)^2}\cos2X\cos4Y
-\frac{p_x}{t_s}.
\end{aligned}
}
\]

把 `ell=a/m` 代回后，前四项与云露式 (2-36) 一致。

但是论文印刷版式 (2-36) 的最后一个交叉谐波写成了与 Table 2-1 不一致的形式：其打印项表现为重复 `cos(2m pi x/a) cos(2 pi y/b)` 并带 `4a^2+4b^2m^2` 型分母。

这个打印项**不能**由 Table 2-1 和式 (2-27) 推出。

反之，由 Table 2-1 唯一导出的正确第五谐波应为

\[
\boxed{
-\frac{8a^2KE_sm^2\pi^2}{(4a^2+b^2m^2)^2}
\cos\frac{2m\pi x}{a}\cos\frac{4\pi y}{b}
}.
\]

最关键的是：云露紧接着给出的式 (2-37) 在 `x=a/(2m),y=0` 的最大压应力表达**恰好与这一 Table-2-1 唯一导出的形式一致**，而与式 (2-36) 打印的最后一项不一致。

因此本项目保留来源层级：

```text
TABLE_2_1 + EQ_2_27 + EQ_2_37 = internally consistent
EQ_2_36_LAST_CROSS_TERM_AS_PRINTED = SOURCE TYPO / INTERNAL INCONSISTENCY
PRODUCTION_COMPILATION = derive from Table_2_1, not silently copy the typo
```

这不是修改云露物理理论，而是对论文内部代数链做一致性恢复。

最大压应力位置按云露为 `x=ell/2,y=0`，其 D15 结果：

\[
\boxed{
\begin{aligned}
\sigma_{x,\min}={}&
-\frac{3KE_s\pi^2}{2\ell^2}
-\frac{4\ell^2KE_s\pi^2}{(\ell^2+b^2)^2}\\
&+\frac{8\ell^2KE_s\pi^2}{(4\ell^2+b^2)^2}
-\frac{2\ell^2KE_s\pi^2}{(\ell^2+4b^2)^2}
-\frac{p_x}{t_s}.
\end{aligned}
}
\]

代回 `ell=a/m` 即逐项恢复云露式 (2-37)。

---

# 8. 理想弹塑性钢材：与云露极限定义的直接一致接口

云露第二章明确采用：板面最大轴向压应力达到 `fy` 时取为极限承载力，并忽略之后塑性发挥带来的小幅承载力增长。

因此本轮采用理想弹塑性：

\[
\sigma_s=E_s\varepsilon_s\quad (|\sigma_s|<f_y),
\]

达到

\[
\boxed{-\sigma_{x,\min}=f_y}
\]

后进入理想塑性平台，无强化。

对云露局部解析路径，第一版 formal control 采用**首个局部屈服事件**：

\[
\boxed{
Y_s(D,q)=f_y+\sigma_{x,\min}(D,q)=0
}
\]

（当前压应力采用负号记号）。

如果只研究云露独立子板，代入式 (2-32) 后，乘去 `A+A0`，该方程对 `A>0` 恰为三次代数方程，和云露式 (2-38) 的描述一致。

```text
IDEAL_EP = elastic until first yield + zero hardening
POST_FIRST_YIELD_STRESS-REDISTRIBUTION = not invented in this audit
YUN_LU_ULTIMATE_EVENT = first local max stress reaches fy
```

这样保持：

```text
formal spatial quadrature = 0
formal yield-zone spatial grid = 0
```

若未来明确要求在局部首屈服之后继续追踪逐渐扩展的塑性区，则那是新的“屈服区域解析边界”问题，不得假装已经由云露第二章给出。

---

# 9. 从云露局部模型补出 displacement-control 接口：仍为 exact D15

为了把云露 `p_x(A)` 接入全局 `D,q`，需要把局部加载从单纯 `p_x` 控制改写为与全局轴向缩短兼容。

云露边界假定加载边保持直线并允许轴向压缩。对局部完整半波，von Karman 轴向中面关系写为

\[
\varepsilon_x=u_{,x}+w_{0,x}w_{,x}+\frac12w_{,x}^2.
\]

由 Airy 应力场有

\[
\langle\sigma_x\rangle=-\frac{p_x}{t_s},\qquad
\langle\sigma_y\rangle=0.
\]

又由 D15：

\[
\left\langle\psi_{,x}^2\right\rangle=\frac{3\pi^2}{\ell^2}.
\]

所以加载边平均压缩应变（压缩取正）严格为

\[
\boxed{
\varepsilon_{c,s}
=\frac{p_x}{E_st_s}
+\frac{3\pi^2}{\ell^2}\left(A_0A+\frac12A^2\right)
}.
\]

这一步是**基于云露同一 Karman 运动学和同一 Airy 场的项目闭合推导**，不是论文中直接印出的新公式。

于是给定全局轴向压缩变量 `D` 后，如果 shell 纵向与全局轴向一致：

\[
\varepsilon_{c,s}^{global}=\varepsilon_0D,
\]

可得到局部钢壳的 displacement-compatible 平均轴力：

\[
\boxed{
p_x^{comp}(D,A)
=E_st_s\left[
\varepsilon_0D
-\frac{3\pi^2}{\ell^2}\left(A_0A+\frac12A^2\right)
\right].
}
\]

这使云露模块真正能够进入当前全局 `D,q`，不再需要历史路径中无法闭合的空间 Airy/材料点接口。

---

# 10. 云露局部幅值到全局 q 的映射

云露 coefficient `A` 的波峰最大挠度是 `4A`。

如果一个局部钢壳子板的加载后最大局部鼓曲幅值按设计侧映射写为

\[
W_{s,\max}(q)=\omega_s A_g=\omega_s b_gq,
\]

则云露系数必须取

\[
\boxed{A_s(q)=\frac{\omega_sb_g}{4}q},
\qquad
\boxed{A_{s,q}=\frac{\omega_sb_g}{4}}.
\]

局部初始缺陷仍是独立物理输入：

\[
\boxed{A_{s0}=\frac{W_{s0,\max}}4},
\]

不得因为整体形函数权重而把局部初始缺陷再乘 `omega_s`。

如果某一设计中 `omega_s` 的定义尚未冻结，则上述式保留为接口，不使用试验 `Pu` 或试验鼓曲形状反求 `omega_s`。

---

# 11. 云露 Galerkin 残量直接变成全局 q 残量

云露 Galerkin 方程本身可写成

\[
\mathcal G_Y(A,A_0,p_x)=G_w-G_p-G_h.
\]

由于它对 `p_x` 是线性的，并且 `p_x^Y(A)` 正是令 Galerkin 残量为 0 的式 (2-32)，可精确整理为

\[
\boxed{
\mathcal G_Y=
\frac{3\pi^2b}{t_s\ell}(A+A_0)
\left[p_x^Y(A)-p_x\right]
}.
\]

云露式 (2-22) 已除以 `t_s`。恢复物理虚功并令 `A=A(q)`，钢壳对全局 `q` 的广义残量贡献为

\[
\boxed{
R_{q,sh}
=t_sA_{,q}\mathcal G_Y
=\frac{3\pi^2b}{\ell}
A_{,q}(A+A_0)
\left[p_x^Y(A)-p_x^{comp}(D,A)\right].
}
\]

这就是新的**零空间积分、两全局变量 D-q 接口**。

对于多个 PBL 之间的局部钢壳子板：

\[
\boxed{
R_{q,sh}=\sum_i
\frac{3\pi^2b_i}{\ell_i}
A_{i,q}(A_i+A_{0i})
\left[p_{x,i}^Y(A_i)-p_{x,i}^{comp}(D,A_i)\right].
}
\]

没有增加材料点，也没有引入外层数值积分。

---

# 12. 全局轴力、残量与极限方程保持原来的 D-q 直接联立形式

局部钢壳平均轴力贡献：

\[
\boxed{P_{sh}(D,q)=\sum_i b_i p_{x,i}^{comp}(D,A_i(q))}.
\]

因此总轴力：

\[
\boxed{P(D,q)=P_c(D,q)+P_{sh}(D,q)}.
\]

总 `q` 平衡：

\[
\boxed{R_q(D,q)=R_{q,c}(D,q)+R_{q,sh}(D,q)=0}.
\]

这里 `R_{q,c}` 仍是已经锁定的 R10 -> N48-C1/MM -> CH -> general-D15 concrete residual；完全不改。

所有 shell 函数均为有理/有限解析表达，因此：

\[
P_D,\ P_q,\ R_{q,D},\ R_{q,q}
\]

全部直接解析微分。

例如

\[
\boxed{p_{x,D}^{comp}=E_st_s\varepsilon_0},
\]

\[
\boxed{
p_{x,q}^{comp}
=-E_st_s\frac{3\pi^2}{\ell^2}(A_0+A)A_{,q}
}.
\]

云露闭式路径的导数：

\[
\boxed{
\frac{dp_x^Y}{dA}
=\frac{\pi^2D_s}{b^2}
\left[
 k_{crx}\frac{A_0}{(A+A_0)^2}
+2k_p(1-\nu_s^2)\frac{A_0+A}{t_s^2}
\right].
}
\]

因此 current production limit function 保持：

\[
\boxed{L=P_DR_{q,q}-P_qR_{q,D}}.
\]

正式极限仍直接求：

\[
\boxed{R_q(D,q)=0,\qquad L(D,q)=0},
\]

并取从 `(0,0)` 连通主支上的第一个 `g:+->-` 荷载极值。

除此之外增加 shell 首屈服事件：

\[
Y_{s,i}(D,q)=0.
\]

最终 control ordering 是同一主支上比较：

```text
first coupled load maximum L=0
first global tangent loss KZ=0
first local Yun-Lu shell yield Y_s,i=0
```

不使用试验承载力选根。

---

# 13. general-D15 / zero-quadrature 结论

本轮已经独立完成以下 exact symbolic gates：

```text
YUN_W_W0_FINITE_TRIG = PASS
YUN_COMPATIBILITY_FINITE_HARMONICS = PASS
TABLE_2_1_FROM_D15 = PASS
KCRX_FROM_D15 = PASS
KP_FROM_D15 = PASS
EQ_2_32_FROM_D15 = PASS
MINIMUM_r_1 = PASS
SIGMA_MIN_EQ_2_37 = PASS
EDGE_SHORTENING_FROM_SAME_KARMAN_FIELD = PASS
GLOBAL_DQ_RESIDUAL_INTERFACE = ANALYTICALLY CLOSED
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_SPATIAL_SUBDOMAINS = 1 per representative complete halfwave
```

唯一发现的来源内部问题是式 (2-36) 最后一项的印刷/代数不一致；生产编译由 Table 2-1 + 2-27 唯一生成，并由 2-37 交叉验证。

---

# 14. 当前理论身份

```text
CONCRETE_MOTHER_THEORY = unchanged / locked
GLOBAL_GENERALIZED_COORDINATES = D,q
LOCAL_YUN_LU_AMPLITUDE = analytic function A_i(q), not a spatial DOF grid
STEEL_LOCAL_MODEL = Yun Lu Ch.2 exact large-deflection Galerkin
STEEL_MATERIAL = ideal elastic-perfectly-plastic, no hardening
YUN_LU_FIRST_YIELD = local control event
GENERAL_D15 = exact compiler/integrator
NUMERICAL_SPATIAL_QUADRATURE = prohibited / zero
DIRECT_LIMIT_SOLVE = retained
```

因此下一步已经不是“云露能否接入”，而是：选择第一块 concrete + Yun-Lu steel-shell benchmark 的设计输入，生成全部局部 `k_crx,k_p,A_i(q),p_i^{comp},R_{q,sh}`，与 frozen concrete operator 一起直接联立求 `(D_u,q_u)`，并同时审计 `L=0 / KZ=0 / Y_s=0` 的先后顺序。
