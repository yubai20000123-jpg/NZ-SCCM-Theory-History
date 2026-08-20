# NZ-SCCM — TC 厚度方向 θ 代换有理化与逐项解析积分执行

时间：2026-08-20 17:16 +08:00

状态：`EXECUTED / TC_THICKNESS_EXACT / THETA_SUBSTITUTION / ZERO_QUADRATURE`

## 0. 任务

从当前已经显式展开的三个实际被积函数出发，先对最关键的 TC 区执行厚度方向解析积分。目标是验证用户提出的“TC 可直接通过 θ 解决”是否真的把根号问题消掉，并把 `R_m`、`P`、`R_A` 的 TC 厚度积分变成有限低阶有理积分。

本节点不引入 I1/I2，不建立新的理论变量。唯一新符号 `χ=tan θ` 是对当前派生角 θ 的积分代换变量。

以下恒等式已用 SymPy 符号核验：

1. `ζ(χ)` 与 `dζ/dχ` 的反解；
2. `ε1(χ), ε2(χ)` 的二次多项式/二次多项式表达；
3. `β(t)` 的共轭分式分解；
4. `C(c)` 的共轭分式分解。

---

## 1. 固定板面位置 (X,Y)，把当前应变写成 ζ 的一次式

由 Nguyen 二阶运动学：

\[
\varepsilon_x=e_{x0}+e_{x1}\zeta,
\qquad
\varepsilon_y=e_{y0}+e_{y1}\zeta,
\qquad
\gamma_{xy}=g_0+g_1\zeta,
\]

其中每个系数都显式为

\[
e_{x0}=\varepsilon_m+\frac{\pi^2S}{b^2}\cos^2X\sin^2Y,
\]

\[
e_{x1}=\frac{hA\pi^2}{2b^2}\sin X\sin Y,
\]

\[
e_{y0}=-\frac{\Delta}{\ell}+\frac{\pi^2S}{\ell^2}\sin^2X\cos^2Y,
\]

\[
e_{y1}=\frac{hA\pi^2}{2\ell^2}\sin X\sin Y,
\]

\[
g_0=\frac{2\pi^2S}{b\ell}\cos X\sin X\sin Y\cos Y,
\]

\[
g_1=-\frac{hA\pi^2}{b\ell}\cos X\cos Y,
\]

且

\[
S=A_0A+\frac12A^2.
\]

为了做 θ 代换，只作代数记账：

\[
s_0=e_{x0}+e_{y0}
=\varepsilon_m-\frac{\Delta}{\ell}
+\frac{\pi^2S}{b^2}\cos^2X\sin^2Y
+\frac{\pi^2S}{\ell^2}\sin^2X\cos^2Y,
\]

\[
s_1=e_{x1}+e_{y1}
=\frac{hA\pi^2}{2}\left(\frac1{b^2}+\frac1{\ell^2}\right)\sin X\sin Y,
\]

\[
d_0=e_{x0}-e_{y0}
=\varepsilon_m+\frac{\Delta}{\ell}
+\frac{\pi^2S}{b^2}\cos^2X\sin^2Y
-\frac{\pi^2S}{\ell^2}\sin^2X\cos^2Y,
\]

\[
d_1=e_{x1}-e_{y1}
=\frac{hA\pi^2}{2}\left(\frac1{b^2}-\frac1{\ell^2}\right)\sin X\sin Y.
\]

这里 `s0,s1,d0,d1` 不是新的理论状态变量，只是把现有显式应变系数整理成和 θ 方程直接匹配的形式。

---

## 2. 用 χ=tan θ 直接反解 ζ

当前主方向满足

\[
\tan 2\theta
=\frac{g_0+g_1\zeta}{d_0+d_1\zeta}.
\]

令

\[
\chi=\tan\theta,
\qquad
\tan2\theta=\frac{2\chi}{1-\chi^2}.
\]

于是

\[
(g_0+g_1\zeta)(1-\chi^2)
=2\chi(d_0+d_1\zeta).
\]

直接解得

\[
\boxed{
\zeta(\chi)
=\frac{N_\theta(\chi)}{D_\theta(\chi)}
}
\]

其中

\[
\boxed{
N_\theta(\chi)=g_0\chi^2+2d_0\chi-g_0
}
\]

\[
\boxed{
D_\theta(\chi)=g_1(1-\chi^2)-2d_1\chi.
}
\]

并且导数发生一个非常重要的简化：

\[
\boxed{
\frac{d\zeta}{d\chi}
=\frac{2\Omega(1+\chi^2)}{D_\theta(\chi)^2}
}
\]

其中

\[
\boxed{
\Omega=d_0g_1-d_1g_0.
}
\]

所以只要 `Ω != 0`，厚度坐标 ζ 与方向变量 χ 之间是纯有理变换。

若 `Ω=0`，则 θ 沿厚度不变，此时不需要该代换：`p,q` 为常数，`ε1,ε2` 直接是 ζ 的一次式，材料函数本身已是 ζ 的有理函数，积分反而更简单。

---

## 3. 主应变也完全有理化

用

\[
p^2=\frac1{1+\chi^2},
\qquad
q^2=\frac{\chi^2}{1+\chi^2},
\qquad
pq=\frac{\chi}{1+\chi^2},
\]

直接代入主应变旋转式，可严格化为

\[
\boxed{
\varepsilon_1(\chi)=\frac{E_1(\chi)}{2D_\theta(\chi)},
\qquad
\varepsilon_2(\chi)=\frac{E_2(\chi)}{2D_\theta(\chi)}.
}
\]

其中 `E1,E2` 都只是二次多项式：

\[
\begin{aligned}
E_1(\chi)={}&
(d_0g_1-d_1g_0+g_0s_1-g_1s_0)\chi^2\\
&+2(d_0s_1-d_1s_0)\chi\\
&+(d_0g_1-d_1g_0-g_0s_1+g_1s_0),
\end{aligned}
\]

\[
\begin{aligned}
E_2(\chi)={}&
(-d_0g_1+d_1g_0+g_0s_1-g_1s_0)\chi^2\\
&+2(d_0s_1-d_1s_0)\chi\\
&+(-d_0g_1+d_1g_0-g_0s_1+g_1s_0).
\end{aligned}
\]

因此 TC 中

\[
t_1=\frac{E_1}{2\varepsilon_{t0}D_\theta},
\qquad
c_2=-\frac{E_2}{2\varepsilon_{c0}D_\theta}.
\]

到这里没有任何平方根。

---

## 4. 三个 A 方向核也变成有理函数

先写

\[
G_x=G_{x0}+G_{x1}\zeta,
\qquad
G_y=G_{y0}+G_{y1}\zeta,
\qquad
G_\gamma=G_{\gamma0}+G_{\gamma1}\zeta,
\]

其中

\[
G_{x0}=\frac{\pi^2H}{b^2}\cos^2X\sin^2Y,
\qquad
G_{x1}=\frac{h\pi^2}{2b^2}\sin X\sin Y,
\]

\[
G_{y0}=\frac{\pi^2H}{\ell^2}\sin^2X\cos^2Y,
\qquad
G_{y1}=\frac{h\pi^2}{2\ell^2}\sin X\sin Y,
\]

\[
G_{\gamma0}=\frac{2\pi^2H}{b\ell}\cos X\sin X\sin Y\cos Y,
\qquad
G_{\gamma1}=-\frac{h\pi^2}{b\ell}\cos X\cos Y,
\]

以及

\[
H=A_0+A.
\]

代入 `ζ=Nθ/Dθ`：

\[
G_x=\frac{G_{x0}D_\theta+G_{x1}N_\theta}{D_\theta},
\]

\[
G_y=\frac{G_{y0}D_\theta+G_{y1}N_\theta}{D_\theta},
\]

\[
G_\gamma=\frac{G_{\gamma0}D_\theta+G_{\gamma1}N_\theta}{D_\theta}.
\]

定义两个直接对应主方向虚应变的有限多项式：

\[
\boxed{
\begin{aligned}
F_1(\chi)={}&
\left(G_{x0}+\chi^2G_{y0}+\chi G_{\gamma0}\right)D_\theta\\
&+\left(G_{x1}+\chi^2G_{y1}+\chi G_{\gamma1}\right)N_\theta,
\end{aligned}
}
\]

\[
\boxed{
\begin{aligned}
F_2(\chi)={}&
\left(\chi^2G_{x0}+G_{y0}-\chi G_{\gamma0}\right)D_\theta\\
&+\left(\chi^2G_{x1}+G_{y1}-\chi G_{\gamma1}\right)N_\theta.
\end{aligned}
}
\]

于是

\[
p^2G_x+q^2G_y+pqG_\gamma
=\frac{F_1}{D_\theta(1+\chi^2)},
\]

\[
q^2G_x+p^2G_y-pqG_\gamma
=\frac{F_2}{D_\theta(1+\chi^2)}.
\]

`F1,F2` 最高仅四次。

---

## 5. 把 NC-M4 材料函数先做低阶分式分解

### 5.1 拉伸函数 T4

令固定材料三次多项式

\[
d_T(r)=1-0.83r+1.04r^2+0.14r^3.
\]

其三个固定根记为

\[
r_1,r_2,r_3,
\qquad d_T(r_k)=0.
\]

定义固定材料系数

\[
\boxed{
a_k=1.07515\frac{r_k(r_k+0.09)}{d_T'(r_k)}
}
\]

其中

\[
d_T'(r)=-0.83+2.08r+0.42r^2.
\]

则严格有

\[
\boxed{
T_4(t)=\sum_{k=1}^3\frac{a_k}{t-r_k}.
}
\]

定义

\[
R_t(\chi)=2\varepsilon_{t0}D_\theta(\chi),
\]

\[
Q_k(\chi)=E_1(\chi)-r_kR_t(\chi).
\]

由于 `E1` 与 `Dθ` 都二次，三个 `Qk` 也都二次。于是

\[
\boxed{
T_4(t_1)=\sum_{k=1}^3 a_k\frac{R_t}{Q_k}.
}
\]

### 5.2 beta

令

\[
a_\beta=\sqrt{0.15}.
\]

则

\[
\boxed{
\beta(t)=\frac12\left(\frac1{1-ia_\beta t}+\frac1{1+ia_\beta t}\right).
}
\]

定义两个二次多项式

\[
B_\pm(\chi)=R_t(\chi)\pm ia_\beta E_1(\chi).
\]

于是

\[
\boxed{
\beta(t_1)=\frac{R_t}{2}\left(\frac1{B_-}+\frac1{B_+}\right).
}
\]

### 5.3 压缩函数 C

利用

\[
\boxed{
C(c)=\frac1{c-i}+\frac1{c+i},
}
\]

定义

\[
R_c(\chi)=2\varepsilon_{c0}D_\theta(\chi),
\]

\[
C_\pm(\chi)=E_2(\chi)\pm iR_c(\chi).
\]

由于

\[
c_2=-\frac{E_2}{R_c},
\]

故

\[
\boxed{
C(c_2)=-R_c\left(\frac1{C_+}+\frac1{C_-}\right).
}
\]

因此

\[
\boxed{
\beta(t_1)C(c_2)
=-\frac{R_tR_c}{2}
\sum_{\epsilon=\pm1}\sum_{\tau=\pm1}
\frac1{B_\epsilon C_\tau}.
}
\]

这里虽然用了共轭复因子，但最后四项成共轭对，实部严格还原原来的实函数；也可以最后组合成实 `log+arctan`。

---

## 6. R_m 的 TC 厚度积分已经变成有限低阶有理积分

TC 中

\[
\sigma_x^{TC}=\frac{f_tT_4(t_1)-f_c\beta(t_1)C(c_2)\chi^2}{1+\chi^2}.
\]

乘以

\[
\frac{d\zeta}{d\chi}=\frac{2\Omega(1+\chi^2)}{D_\theta^2},
\]

得到

\[
\boxed{
\mathcal I_m^{TC}(\chi)
=\sigma_x^{TC}\frac{d\zeta}{d\chi}
}
\]

并且材料分式全部代入后严格化为

\[
\boxed{
\mathcal I_m^{TC}
=4\Omega f_t\varepsilon_{t0}
\sum_{k=1}^3\frac{a_k}{D_\theta Q_k}
+4\Omega f_c\varepsilon_{t0}\varepsilon_{c0}\chi^2
\sum_{\epsilon=\pm1}\sum_{\tau=\pm1}
\frac1{B_\epsilon C_\tau}.
}
\]

每一项分母仅是两个二次多项式的乘积。

因此任一 TC 厚度段 `ζa -> ζb` 的横向膜力贡献为

\[
\boxed{
N_x^{TC}(X,Y;\zeta_a,\zeta_b)
=\int_{\chi_a}^{\chi_b}\mathcal I_m^{TC}(\chi)\,d\chi,
}
\]

其中

\[
\chi_a=\tan\theta(X,Y,\zeta_a),
\qquad
\chi_b=\tan\theta(X,Y,\zeta_b).
\]

---

## 7. P 的 TC 厚度核同样完全有理

TC 中

\[
\sigma_y^{TC}=\frac{f_tT_4(t_1)\chi^2-f_c\beta(t_1)C(c_2)}{1+\chi^2}.
\]

故

\[
\boxed{
\mathcal I_y^{TC}(\chi)
=\sigma_y^{TC}\frac{d\zeta}{d\chi}
}
\]

严格化为

\[
\boxed{
\mathcal I_y^{TC}
=4\Omega f_t\varepsilon_{t0}\chi^2
\sum_{k=1}^3\frac{a_k}{D_\theta Q_k}
+4\Omega f_c\varepsilon_{t0}\varepsilon_{c0}
\sum_{\epsilon=\pm1}\sum_{\tau=\pm1}
\frac1{B_\epsilon C_\tau}.
}
\]

所以 TC 段的轴向厚度应力积分为

\[
\boxed{
N_y^{TC}(X,Y;\zeta_a,\zeta_b)
=\int_{\chi_a}^{\chi_b}\mathcal I_y^{TC}(\chi)\,d\chi.
}
\]

全板轴力仍为

\[
P=-\frac{K_0}{\ell}\int_0^\pi\int_0^\pi N_y(X,Y)\,dY\,dX,
\]

其中每个厚度位置只使用唯一实际状态。

---

## 8. R_A 的 TC 厚度核也完全有理

TC 的主方向虚功形式：

\[
r_A^{TC}
=f_tT_4(t_1)\left[p^2G_x+q^2G_y+pqG_\gamma\right]
-f_c\beta(t_1)C(c_2)\left[q^2G_x+p^2G_y-pqG_\gamma\right].
\]

代入 `F1,F2` 与 `dζ/dχ`，得到

\[
\boxed{
\mathcal I_A^{TC}(\chi)
=r_A^{TC}\frac{d\zeta}{d\chi}
}
\]

且严格化为

\[
\boxed{
\begin{aligned}
\mathcal I_A^{TC}
={}&4\Omega f_t\varepsilon_{t0}
\sum_{k=1}^3\frac{a_kF_1(\chi)}{D_\theta(\chi)^2Q_k(\chi)}\\
&+4\Omega f_c\varepsilon_{t0}\varepsilon_{c0}
\frac{F_2(\chi)}{D_\theta(\chi)}
\sum_{\epsilon=\pm1}\sum_{\tau=\pm1}
\frac1{B_\epsilon(\chi)C_\tau(\chi)}.
\end{aligned}
}
\]

这里：

- `Dθ` 二次；
- `Qk` 二次；
- `B±` 二次；
- `C±` 二次；
- `F1,F2` 最高四次。

因此没有任何高次代数根式。

TC 段对 `R_A` 的厚度贡献为

\[
\boxed{
\mathcal R_A^{TC}(X,Y;\zeta_a,\zeta_b)
=\int_{\chi_a}^{\chi_b}\mathcal I_A^{TC}(\chi)\,d\chi.
}
\]

---

## 9. 每一项如何真正积分：只需要二次分母的标准原函数

设任意二次多项式

\[
Q(\chi)=A\chi^2+B\chi+C,
\qquad \Delta_Q=4AC-B^2.
\]

对线性分子，有标准原函数

\[
\boxed{
\begin{aligned}
\int\frac{u\chi+v}{Q(\chi)}d\chi
={}&\frac{u}{2A}\ln Q(\chi)\\
&+\frac{2Av-uB}{A\sqrt{\Delta_Q}}
\arctan\frac{2A\chi+B}{\sqrt{\Delta_Q}},
\end{aligned}
}
\]

当 `ΔQ<0` 时用等价的实 `artanh/log` 形式；复共轭二次因子最终也成对还原为实 `log+arctan`。

对重复二次分母还需要

\[
\boxed{
\begin{aligned}
\int\frac{u\chi+v}{Q(\chi)^2}d\chi
={}&-\frac{u}{2A\,Q(\chi)}\\
&+\left(v-\frac{uB}{2A}\right)
\left[
\frac{2A\chi+B}{\Delta_Q Q(\chi)}
+\frac{4A}{\Delta_Q^{3/2}}
\arctan\frac{2A\chi+B}{\sqrt{\Delta_Q}}
\right].
\end{aligned}
}
\]

因此所有 TC 厚度项都只需有限次使用这两个原函数。

---

## 10. 实际部分分式结构：项数固定且很低

### 10.1 R_m / P 的拉伸项

每个 `k=1,2,3` 都是

\[
\frac{\text{0次或2次多项式}}{D_\theta Q_k}.
\]

必可唯一写成

\[
\boxed{
\frac{n_2\chi^2+n_1\chi+n_0}{D_\theta Q_k}
=\frac{a\chi+b}{D_\theta}+\frac{c\chi+d}{Q_k}.
}
\]

四个系数由恒等式

\[
n_2\chi^2+n_1\chi+n_0
=(a\chi+b)Q_k+(c\chi+d)D_\theta
\]

逐次比较 `χ^3,χ^2,χ,1` 四个系数直接得到。

### 10.2 R_m / P 的压缩项

每个 `(ε,τ)` 都是

\[
\frac{\text{0次或2次多项式}}{B_\epsilon C_\tau},
\]

同样分成两个二次分母：

\[
\boxed{
\frac{n_2\chi^2+n_1\chi+n_0}{B_\epsilon C_\tau}
=\frac{a\chi+b}{B_\epsilon}+\frac{c\chi+d}{C_\tau}.
}
\]

### 10.3 R_A 的拉伸项

每个 `k` 是

\[
\frac{F_1(\chi)}{D_\theta^2Q_k}.
\]

必可写成

\[
\boxed{
\frac{F_1}{D_\theta^2Q_k}
=\frac{a\chi+b}{D_\theta}
+\frac{c\chi+d}{D_\theta^2}
+\frac{e\chi+f}{Q_k}.
}
\]

六个系数由

\[
F_1
=(a\chi+b)D_\theta Q_k
+(c\chi+d)Q_k
+(e\chi+f)D_\theta^2
\]

比较 `χ^5,...,χ^0` 六个系数直接确定。

### 10.4 R_A 的压缩项

每个 `(ε,τ)` 是

\[
\frac{F_2(\chi)}{D_\theta B_\epsilon C_\tau}.
\]

必可写成

\[
\boxed{
\frac{F_2}{D_\theta B_\epsilon C_\tau}
=\frac{a\chi+b}{D_\theta}
+\frac{c\chi+d}{B_\epsilon}
+\frac{e\chi+f}{C_\tau}.
}
\]

六个系数由

\[
F_2
=(a\chi+b)B_\epsilon C_\tau
+(c\chi+d)D_\theta C_\tau
+(e\chi+f)D_\theta B_\epsilon
\]

比较六个幂次系数得到。

所以 TC 厚度解析积分根本不需要八次/十次代数根：通过 θ 与材料函数自身的固定分式分解，所有实际积分最终只剩二次多项式原函数。

---

## 11. 本节点结论

本轮真正执行后，TC 的解析困难发生了根本性变化：

\[
\boxed{
\text{TC 厚度积分不是“二次根式积分”，而是通过 }\chi=\tan\theta\text{ 直接变成低阶有理积分。}
}
\]

具体地：

1. `ζ(χ)` 是二次/二次有理函数；
2. `ε1(χ),ε2(χ)` 都是二次/二次有理函数；
3. NC-M4 的 `T4,beta,C` 可分解为有限个固定材料极点；
4. `R_m` 与 `P` 的每一个 TC 厚度项只涉及两个二次分母；
5. `R_A` 的每一个 TC 厚度项最多涉及三个二次分母，或一个重复二次分母；
6. 所有原函数严格是有限的 `有理项 + log + arctan/artanh`；
7. 无正式空间 quadrature、无 material-point grid、无 I1/I2 理论层。

因此用户提出的“TC 是否可以由 θ 直接解决”在厚度积分层面得到 **PASS**。

下一唯一任务：用完全相同的方法补齐 CT（方向交换即可）以及 CC/TT 的厚度原函数，然后把厚度积分结果代回 `X,Y` 面积分。