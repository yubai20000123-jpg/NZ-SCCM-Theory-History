# NZ-SCCM Case21 concrete：全路径第一拉伸段解析证书与纯代数 Picard–Fuchs 输入 R07

**时间：2026-08-19 02:05 +08:00**  
**身份：R06 NEXT STEP EXECUTED / ZERO DISCRETIZATION / PURE ANALYTIC CERTIFICATE**

---

## 0. 目标

R06 已把完整 Case21 concrete current map 写成 finite algebraic / semialgebraic period，但原 R10 拉伸三段 law 仍通过阈值条件表示。

本文件对 R06 的 pilot generalized state

\[
D=0.600,\qquad q=0.000600,\qquad \alpha=0.000500
\]

以及整条纯数学辅助路径

\[
0\le\tau\le1,
\quad q(\tau)=\tau q,
\quad \alpha(\tau)=\tau\alpha
\]

给出一个**全连续域解析证书**：两个拉伸 projector eigenvalues `theta_±` 在整个完整半波、整个厚度、整个 `tau` 路径上都严格小于第一阈值 `xcr`。

因此该 pilot 不需要 Heaviside、不需要材料状态分区、不需要 semi-algebraic material branches；完整 R10 直接退化为一个**纯 algebraic matrix function**。

---

# 1. 路径参数

Case21：

\[
\nu=0.18,
\quad q_0=0.0025,
\quad \varepsilon_0=0.00209,
\quad t=19.30\ \mathrm{mm},
\quad b=1220\ \mathrm{mm}.
\]

定义

\[
M(\tau)=m_1\tau+m_2\tau^2,
\]

\[
m_1=\frac{\pi^2q_0q}{\varepsilon_0}
=0.007083448134753128\ldots,
\]

\[
m_2=\frac{\pi^2q^2}{2\varepsilon_0}
=0.0008500137761703754\ldots,
\]

所以

\[
0\le M(\tau)\le M(1)
=0.007933461910923504\ldots.
\]

\[
B(\tau)=B_1\tau,
\qquad
B_1=0.02241156540995662\ldots.
\]

且

\[
M(\tau)-\alpha(\tau)
=\tau(m_1-\alpha)+m_2\tau^2>0,
\]

因此

\[
0\le M(\tau)-\alpha(\tau)
\le M(1)-\alpha
=0.007433461910923504\ldots.
\]

R10 第一拉伸阈值

\[
x_{cr}=\frac{\rho}{\kappa}
=0.04998717945397425\ldots.
\]

---

# 2. 对 `lambda_max(E)` 的连续解析上界

令

\[
x=\sin^2X,\qquad y=\sin^2Y,
\]

\[
H=\sin X\sin Y,
\qquad C=|\cos X\cos Y|.
\]

有

\[
0\le x,y,H,C\le1,
\]

以及关键恒等界

\[
\boxed{H^2+C^2\le1},
\]

因为

\[
H^2+C^2
=\sin^2X\sin^2Y+\cos^2X\cos^2Y
=1-\sin^2X\cos^2Y-\cos^2X\sin^2Y\le1.
\]

还因为

\[
|HC|=|\sin X\cos X\sin Y\cos Y|\le\frac14.
\]

对等效矩阵第一对角元，`M` 部分满足

\[
F_x+\nu F_y
=y(1-x)+\nu x(1-y)\le1,
\]

所以

\[
E_{11}^{(M)}\le\frac{M}{1-\nu^2}.
\]

`alpha` 部分是双线性函数；其在单位方形上的最大值出现在角点 `(x,y)=(1,1)`，精确给出

\[
E_{11}^{(\alpha)}\le\frac{\alpha}{4}.
\]

弯曲 `B` 对 `E11` 与 `E12` 的贡献不能独立取最大；利用 `H^2+C^2<=1`，得到

\[
\frac{BH}{1-\nu}
+\frac{BC}{1+\nu}
\le
B\sqrt{\frac1{(1-\nu)^2}+\frac1{(1+\nu)^2}}.
\]

膜内剪切部分满足

\[
\left|E_{12}^{(M-\alpha)}\right|
\le\frac{M-\alpha}{4(1+\nu)}.
\]

由 Gershgorin / symmetric row bound，第一行给出

\[
\lambda_{max}(\mathbf E)
\le E_{11}+|E_{12}|.
\]

因此整条 `tau` 路径有统一上界

\[
\boxed{
\lambda_{max}(\mathbf E)
\le
\frac{M(1)}{1-\nu^2}
+\frac{\alpha}{4}
+\frac{M(1)-\alpha}{4(1+\nu)}
+B_1\sqrt{\frac1{(1-\nu)^2}+\frac1{(1+\nu)^2}}
}.
\]

代入数值：

\[
\boxed{
\lambda_{max}(\mathbf E)
\le 0.04318145225417163\ldots
}.
\]

而

\[
0.04318145225417163
<0.04998717945397425=x_{cr}.
\]

第二 Gershgorin 行甚至满足

\[
E_{22}+|E_{12}|\le-0.5436519714524844\ldots<0,
\]

所以不控制最大主值。

这整个证明没有任何采样、网格或离散搜索。

---

# 3. 从 principal `lambda` 上界到 R10 projector `theta` 上界

R10 positive projector 为

\[
\Pi_\eta(z)=
\frac{z^2(\sqrt{z^2+\eta^2}+z)}{2(z^2+\eta^2)}.
\]

### 3.1 `z>=0`

要证明

\[
\Pi_\eta(z)<z.
\]

对 `z>0`，等价于

\[
z\sqrt{z^2+\eta^2}<z^2+2\eta^2.
\]

两边均为正，平方后差值为

\[
(z^2+2\eta^2)^2-z^2(z^2+\eta^2)
=3z^2\eta^2+4\eta^4>0.
\]

所以

\[
\boxed{0\le\Pi_\eta(z)<z\qquad(z>0)}.
\]

### 3.2 `z<=0`

令 `z=-a`, `a>=0`，则

\[
\Pi_\eta(-a)
=\frac{a^2(\sqrt{a^2+\eta^2}-a)}{2(a^2+\eta^2)}
=\frac{a^2\eta^2}{2(a^2+\eta^2)(\sqrt{a^2+\eta^2}+a)}.
\]

因为

\[
\frac{a^2}{a^2+\eta^2}\le1,
\qquad
\sqrt{a^2+\eta^2}+a\ge\eta,
\]

所以

\[
\boxed{
0\le\Pi_\eta(z)\le\frac\eta2\qquad(z\le0).
}
\]

而 `eta=xcr/20`，故

\[
\frac\eta2=\frac{x_{cr}}{40}<x_{cr}.
\]

综合正、负主值：

\[
\boxed{
0\le\theta_\pm=\Pi_\eta(\lambda_\pm)<x_{cr}
}
\]

在全部

\[
(X,Y,\zeta,\tau)\in[0,\pi]^2\times[-1,1]\times[0,1]
\]

严格成立。

---

# 4. 结果：R10 三段拉伸 law 在 pilot 上全局退化为第一段有限多项式

因此不再需要

\[
H(\theta-x_{cr}),\qquad H(\theta-10x_{cr}).
\]

全域严格使用

\[
\boxed{
\mathbf u_R(\mathbf t)
=\rho\mathbf r
+(10H_R-6\rho)\mathbf r^3
+(8\rho-15H_R)\mathbf r^4
+(6H_R-3\rho)\mathbf r^5,
\qquad
\mathbf r=\mathbf t/x_{cr}.
}
\]

于是

\[
\mathbf T=\mathbf u_R/\rho,
\]

\[
\mathbf U=\kappa\mathbf E-\mathbf C+\kappa\mathbf c+\mathbf u_R-\kappa\mathbf t,
\]

\[
\mathbf S=\mathbf U-a_{cc}\det(\mathbf C)\mathbf C
+\mathbf C\operatorname{adj}(\mathbf T)
-\rho a_t\det(\mathbf T)\operatorname{adj}(\mathbf T^7)
\]

全部成为有限 algebraic matrix expressions。

对该 pilot，R06 §6 中为材料 branch 引入的

```text
delta_t
theta_+
theta_-
Heaviside threshold conditions
```

不再是 creative-telescoping 必要输入。

最小 algebraic generators 可缩减为

\[
\boxed{
\mathcal G_{pilot}=\{\omega,\Delta_A,s_A\}
}
\]

及三条核心关系

\[
\boxed{\omega^2-r(1-r)s(1-s)=0},
\]

\[
\boxed{\Delta_A^2-\det(\mathbf E^2+\eta^2\mathbf I)=0},
\]

\[
\boxed{s_A^2-[\operatorname{tr}(\mathbf E^2+\eta^2\mathbf I)+2\Delta_A]=0}.
\]

因此完整 `Pc(tau)` pilot 是一个**纯 algebraic period**，不是 semialgebraic material-state integral。

---

# 5. 对 Picard–Fuchs gate 的推进

本轮把 R06 的状态进一步推进为：

```text
PILOT_GLOBAL_FIRST_TENSION_BRANCH_CERTIFICATE = PASS
PILOT_HEAVISIDE_MATERIAL_BRANCHES_REQUIRED = NO
PILOT_PURE_ALGEBRAIC_PERIOD = PASS
PILOT_MINIMAL_RADICAL_GENERATORS = {omega, Delta_A, s_A}
FULL_Pc_TAU_TELESCOPER_GENERATED = NO
```

所以当前下一步已经变得更小、更明确：

\[
\boxed{
\text{只对三生成元 pure algebraic period }P_c(\tau)
\text{ 做 creative telescoping / Picard--Fuchs reduction。}
\]

如果当前符号后端无法生成 finite telescoper，应报告 `ANALYTIC_CLOSURE_BACKEND_BLOCK`；禁止离散 fallback。
