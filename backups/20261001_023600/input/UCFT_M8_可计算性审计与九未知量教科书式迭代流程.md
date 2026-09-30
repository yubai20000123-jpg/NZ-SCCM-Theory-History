# UCFT M8 可计算性审计与九未知量 fixed-q 教科书式计算流程

时间：2026-10-01 01:32 +08:00

## 1. 审计结论

当前“还不能直接跑完 BH005 乃至九试件全过程”的主要原因不是未知量离散化爆炸。

正式 fixed-q 体系仍只有九个未知量：

\[
E_x,\ E_y,\ B_x,\ B_y,\ H_x,\ H_y,\ P,\ A^+,\ A^-.
\]

M3 candidate harmonics 当前没有默认实例化，因此不存在 31DOF、41DOF、57DOF 那种自由度膨胀。

真正存在两个实现级卡点：

1. 旧 perfect-local 模态识别在 \(A_0^\pm=0,A^\pm=0,q>0\) 的非平衡点上评估局部切线。已经实际算得 \(R_{A^\pm}\neq0\)，所以必须改成 candidate-wise forced-response equilibrium branch，再在真实 \(R_{A^\pm}=0\) 状态上评估局部切线。
2. M5 已把钢壳厚度 \(\zeta\) 方向 elastic/plastic active-set 完全解析闭合；M4/M8 也已经把 UHPC 的 \(z\) 与 \(y\) 积分闭合到只剩一个确定性 \(x\) 积分。但当前正式文件只说明钢壳“厚度解析积分”，尚未给出 steel-local + Mises deformation theory 在 \(x,y\) 面内的同等级 production reduction。进入钢材塑性以后，厚度积分结果含有由 \(\sqrt{\varepsilon^T H\varepsilon}\) 产生的根式与反双曲函数，并且局部多波 \(N,m\) 使其系数成为高频三角函数；不能直接宣称其 \(y\) 积分仍为 UHPC 那样的有理原函数。若又禁止用二维 Gauss 作为理论定义，就必须先把这一层明确降成至多一个确定性一维积分。这个接口尚未正式写完。

因此：
- 不是“大矩阵解不动”；
- 也不是“材料点离散太多”；
- 是 **mode-identification 的平衡路径定义 + nonlinear steel 的面内积分闭合** 两个接口没有完成。
- 其中第一项已经知道如何修正；第二项才是完整全过程 evaluator 的主要数学实现瓶颈。

---

## 2. 不使用组合中间参数的几何与 C1 中面应变

区域：

\[
0\le x\le b,\qquad 0\le y\le a_h.
\]

整体初始面外几何：

\[
W_0(x,y)=bq_0
\sin\frac{\pi x}{b}
\sin\frac{\pi y}{a_h}.
\]

当前整体面外几何：

\[
W_g(x,y)=b(q_0+q)
\sin\frac{\pi x}{b}
\sin\frac{\pi y}{a_h}.
\]

加载新增整体面外位移：

\[
w_g(x,y)=bq
\sin\frac{\pi x}{b}
\sin\frac{\pi y}{a_h}.
\]

C1 中面应变直接写为：

\[
\begin{aligned}
\varepsilon_x^0(x,y)
={}&E_x
+B_x\cos\frac{2\pi x}{b}
-\frac{\pi^2}{8}(q^2+2q_0q)
\cos\frac{2\pi y}{a_h}\\
&+H_x
\cos\frac{2\pi x}{b}
\cos\frac{2\pi y}{a_h},
\end{aligned}
\]

\[
\begin{aligned}
\varepsilon_y^0(x,y)
={}&E_y
-\frac{\pi^2b^2}{8a_h^2}(q^2+2q_0q)
\cos\frac{2\pi x}{b}
+B_y\cos\frac{2\pi y}{a_h}\\
&+H_y
\cos\frac{2\pi x}{b}
\cos\frac{2\pi y}{a_h},
\end{aligned}
\]

\[
\gamma_{xy}^0(x,y)
=
-\left(
\frac{b}{a_h}H_x+\frac{a_h}{b}H_y
\right)
\sin\frac{2\pi x}{b}
\sin\frac{2\pi y}{a_h}.
\]

整体加载新增曲率：

\[
\kappa_x^g(x,y)
=
\frac{\pi^2q}{b}
\sin\frac{\pi x}{b}
\sin\frac{\pi y}{a_h},
\]

\[
\kappa_y^g(x,y)
=
\frac{\pi^2qb}{a_h^2}
\sin\frac{\pi x}{b}
\sin\frac{\pi y}{a_h},
\]

\[
\kappa_{xy}^g(x,y)
=
-\frac{2\pi^2q}{a_h}
\cos\frac{\pi x}{b}
\cos\frac{\pi y}{a_h}.
\]

对固定 \(q\) Newton，整体中面应变对 \(q\) 的显式导数是：

\[
\frac{\partial\varepsilon_x^0}{\partial q}
=
-\frac{\pi^2}{4}(q+q_0)
\cos\frac{2\pi y}{a_h},
\]

\[
\frac{\partial\varepsilon_y^0}{\partial q}
=
-\frac{\pi^2b^2}{4a_h^2}(q+q_0)
\cos\frac{2\pi x}{b},
\]

\[
\frac{\partial\gamma_{xy}^0}{\partial q}=0.
\]

曲率对 \(q\) 的导数：

\[
\frac{\partial\kappa_x^g}{\partial q}
=
\frac{\pi^2}{b}
\sin\frac{\pi x}{b}
\sin\frac{\pi y}{a_h},
\]

\[
\frac{\partial\kappa_y^g}{\partial q}
=
\frac{\pi^2b}{a_h^2}
\sin\frac{\pi x}{b}
\sin\frac{\pi y}{a_h},
\]

\[
\frac{\partial\kappa_{xy}^g}{\partial q}
=
-\frac{2\pi^2}{a_h}
\cos\frac{\pi x}{b}
\cos\frac{\pi y}{a_h}.
\]

---

## 3. 上钢壳局部多波构形及全部导数

\[
\psi_\ell^+(x,y)
=
\left[
1-\cos\frac{2\pi N^+x}{b}
\right]
\left[
1-\cos\frac{2\pi m^+y}{a_h}
\right].
\]

\[
\frac{\partial\psi_\ell^+}{\partial x}
=
\frac{2\pi N^+}{b}
\sin\frac{2\pi N^+x}{b}
\left[
1-\cos\frac{2\pi m^+y}{a_h}
\right].
\]

\[
\frac{\partial\psi_\ell^+}{\partial y}
=
\frac{2\pi m^+}{a_h}
\left[
1-\cos\frac{2\pi N^+x}{b}
\right]
\sin\frac{2\pi m^+y}{a_h}.
\]

\[
\frac{\partial^2\psi_\ell^+}{\partial x^2}
=
\left(\frac{2\pi N^+}{b}\right)^2
\cos\frac{2\pi N^+x}{b}
\left[
1-\cos\frac{2\pi m^+y}{a_h}
\right].
\]

\[
\frac{\partial^2\psi_\ell^+}{\partial y^2}
=
\left(\frac{2\pi m^+}{a_h}\right)^2
\left[
1-\cos\frac{2\pi N^+x}{b}
\right]
\cos\frac{2\pi m^+y}{a_h}.
\]

\[
\frac{\partial^2\psi_\ell^+}{\partial x\partial y}
=
\frac{4\pi^2N^+m^+}{ba_h}
\sin\frac{2\pi N^+x}{b}
\sin\frac{2\pi m^+y}{a_h}.
\]

上钢壳 local-extra 中面应变：

\[
\begin{aligned}
\Delta\varepsilon_x^{\ell,+}
={}&
\pi(q_0A^+ +qA_0^+ +qA^+)
\cos\frac{\pi x}{b}
\sin\frac{\pi y}{a_h}
\frac{\partial\psi_\ell^+}{\partial x}\\
&+\frac12
\left[(A^+)^2+2A_0^+A^+\right]
\left(\frac{\partial\psi_\ell^+}{\partial x}\right)^2,
\end{aligned}
\]

\[
\begin{aligned}
\Delta\varepsilon_y^{\ell,+}
={}&
\frac{\pi b}{a_h}(q_0A^+ +qA_0^+ +qA^+)
\sin\frac{\pi x}{b}
\cos\frac{\pi y}{a_h}
\frac{\partial\psi_\ell^+}{\partial y}\\
&+\frac12
\left[(A^+)^2+2A_0^+A^+\right]
\left(\frac{\partial\psi_\ell^+}{\partial y}\right)^2,
\end{aligned}
\]

\[
\begin{aligned}
\Delta\gamma_{xy}^{\ell,+}
={}&
\pi(q_0A^+ +qA_0^+ +qA^+)
\left[
\cos\frac{\pi x}{b}\sin\frac{\pi y}{a_h}
\frac{\partial\psi_\ell^+}{\partial y}
+
\frac{b}{a_h}\sin\frac{\pi x}{b}\cos\frac{\pi y}{a_h}
\frac{\partial\psi_\ell^+}{\partial x}
\right]\\
&+
\left[(A^+)^2+2A_0^+A^+\right]
\frac{\partial\psi_\ell^+}{\partial x}
\frac{\partial\psi_\ell^+}{\partial y}.
\end{aligned}
\]

上钢壳加载新增局部曲率：

\[
\kappa_x^{\ell,+}
=
-A^+
\frac{\partial^2\psi_\ell^+}{\partial x^2},
\]

\[
\kappa_y^{\ell,+}
=
-A^+
\frac{\partial^2\psi_\ell^+}{\partial y^2},
\]

\[
\kappa_{xy}^{\ell,+}
=
-2A^+
\frac{\partial^2\psi_\ell^+}{\partial x\partial y}.
\]

---

## 4. 下钢壳局部多波构形及全部导数

\[
\psi_\ell^-(x,y)
=
\left[
1-\cos\frac{2\pi N^-x}{b}
\right]
\left[
1-\cos\frac{2\pi m^-y}{a_h}
\right].
\]

其一阶、二阶导数与上式同型，只需将 \(N^+,m^+\) 换成 \(N^-,m^-\)。

下钢壳 local-extra 中面应变：

\[
\begin{aligned}
\Delta\varepsilon_x^{\ell,-}
={}&
-\pi(q_0A^- +qA_0^- +qA^-)
\cos\frac{\pi x}{b}
\sin\frac{\pi y}{a_h}
\frac{\partial\psi_\ell^-}{\partial x}\\
&+\frac12
\left[(A^-)^2+2A_0^-A^-\right]
\left(\frac{\partial\psi_\ell^-}{\partial x}\right)^2,
\end{aligned}
\]

\[
\begin{aligned}
\Delta\varepsilon_y^{\ell,-}
={}&
-\frac{\pi b}{a_h}(q_0A^- +qA_0^- +qA^-)
\sin\frac{\pi x}{b}
\cos\frac{\pi y}{a_h}
\frac{\partial\psi_\ell^-}{\partial y}\\
&+\frac12
\left[(A^-)^2+2A_0^-A^-\right]
\left(\frac{\partial\psi_\ell^-}{\partial y}\right)^2,
\end{aligned}
\]

\[
\begin{aligned}
\Delta\gamma_{xy}^{\ell,-}
={}&
-\pi(q_0A^- +qA_0^- +qA^-)
\left[
\cos\frac{\pi x}{b}\sin\frac{\pi y}{a_h}
\frac{\partial\psi_\ell^-}{\partial y}
+
\frac{b}{a_h}\sin\frac{\pi x}{b}\cos\frac{\pi y}{a_h}
\frac{\partial\psi_\ell^-}{\partial x}
\right]\\
&+
\left[(A^-)^2+2A_0^-A^-\right]
\frac{\partial\psi_\ell^-}{\partial x}
\frac{\partial\psi_\ell^-}{\partial y}.
\end{aligned}
\]

下钢壳加载新增局部曲率：

\[
\kappa_x^{\ell,-}
=
+A^-
\frac{\partial^2\psi_\ell^-}{\partial x^2},
\]

\[
\kappa_y^{\ell,-}
=
+A^-
\frac{\partial^2\psi_\ell^-}{\partial y^2},
\]

\[
\kappa_{xy}^{\ell,-}
=
+2A^-
\frac{\partial^2\psi_\ell^-}{\partial x\partial y}.
\]

---

## 5. UHPC 与上下钢壳厚度应变

UHPC，\(-t_c/2\le z\le t_c/2\)：

\[
\varepsilon_x^U
=
\varepsilon_x^0
+
z\kappa_x^g,
\]

\[
\varepsilon_y^U
=
\varepsilon_y^0
+
z\kappa_y^g,
\]

\[
\gamma_{xy}^U
=
\gamma_{xy}^0
+
z\kappa_{xy}^g.
\]

上钢壳，\(-t_s/2\le\zeta\le t_s/2\)：

\[
\varepsilon_x^{s,+}
=
\varepsilon_x^0
+\Delta\varepsilon_x^{\ell,+}
+\left(\frac{t_c+t_s}{2}+\zeta\right)\kappa_x^g
+\zeta\kappa_x^{\ell,+},
\]

\[
\varepsilon_y^{s,+}
=
\varepsilon_y^0
+\Delta\varepsilon_y^{\ell,+}
+\left(\frac{t_c+t_s}{2}+\zeta\right)\kappa_y^g
+\zeta\kappa_y^{\ell,+},
\]

\[
\gamma_{xy}^{s,+}
=
\gamma_{xy}^0
+\Delta\gamma_{xy}^{\ell,+}
+\left(\frac{t_c+t_s}{2}+\zeta\right)\kappa_{xy}^g
+\zeta\kappa_{xy}^{\ell,+}.
\]

下钢壳：

\[
\varepsilon_x^{s,-}
=
\varepsilon_x^0
+\Delta\varepsilon_x^{\ell,-}
+\left(-\frac{t_c+t_s}{2}+\zeta\right)\kappa_x^g
+\zeta\kappa_x^{\ell,-},
\]

\[
\varepsilon_y^{s,-}
=
\varepsilon_y^0
+\Delta\varepsilon_y^{\ell,-}
+\left(-\frac{t_c+t_s}{2}+\zeta\right)\kappa_y^g
+\zeta\kappa_y^{\ell,-},
\]

\[
\gamma_{xy}^{s,-}
=
\gamma_{xy}^0
+\Delta\gamma_{xy}^{\ell,-}
+\left(-\frac{t_c+t_s}{2}+\zeta\right)\kappa_{xy}^g
+\zeta\kappa_{xy}^{\ell,-}.
\]

---

## 6. UHPC active-set：最终 INP 分段线性 law 的人工复算方式

方向性材料输入：

\[
e_x^U=
\frac{\varepsilon_x^U+0.30\varepsilon_y^U}{1-0.30^2},
\]

\[
e_y^U=
\frac{\varepsilon_y^U+0.30\varepsilon_x^U}{1-0.30^2}.
\]

剪切：

\[
\tau_{xy}^U
=
\frac{43400}{2(1+0.30)}
\gamma_{xy}^U.
\]

对最终 INP 中相邻两个总应变—应力点
\((e_j,\sigma_j)\)、\((e_{j+1},\sigma_{j+1})\)，该材料段直接是：

\[
\sigma(e)
=
\sigma_j+
\frac{\sigma_{j+1}-\sigma_j}{e_{j+1}-e_j}(e-e_j).
\]

固定 \(x,y\) 后，\(e_x^U(z)\) 与 \(e_y^U(z)\) 都是 \(z\) 的一次函数。
任何材料阈值 \(e_j\) 的厚度边界直接由：

\[
\frac{
\varepsilon_x^0+z\kappa_x^g
+0.30(\varepsilon_y^0+z\kappa_y^g)
}{0.91}
=e_j
\]

或：

\[
\frac{
\varepsilon_y^0+z\kappa_y^g
+0.30(\varepsilon_x^0+z\kappa_x^g)
}{0.91}
=e_j
\]

解出。
所有位于 \((-t_c/2,t_c/2)\) 内的根与两端 \(-t_c/2,t_c/2\) 排序。

在任一已确定材料段 \([z_a,z_b]\) 内：

\[
\int_{z_a}^{z_b}\sigma(e_m+\chi z)\,dz
\]

就是一次多项式的原函数差；

\[
\int_{z_a}^{z_b}z\,\sigma(e_m+\chi z)\,dz
\]

就是二次多项式的原函数差。

所以 UHPC 厚度不需要离散材料点。

M8 已进一步证明，在固定 \(x\) 后把
\(\sin(\pi y/a_h)\)、\(\cos(2\pi y/a_h)\) 等有限三角项用
\(\tan[\pi y/(2a_h)]\) 有理化，可以解析确定所有 \(y\) 向材料活动区边界并完成 \(y\) 积分，最终只剩一个 \(x\) 向确定积分。

---

## 7. Q355 钢材 active-set：厚度已经完全解析

对 \(\nu_s=0.30\)，当前 M5 equivalent strain 可直接写成：

\[
\begin{aligned}
\bar\varepsilon_s^2
={}&
\frac{7900}{8281}
\left[
(\varepsilon_x^s)^2+(\varepsilon_y^s)^2
\right]\\
&+
\frac{1100}{8281}
\varepsilon_x^s\varepsilon_y^s
+
\frac{75}{169}
(\gamma_{xy}^s)^2.
\end{aligned}
\]

屈服条件：

\[
\bar\varepsilon_s
=
\frac{355}{206000}.
\]

因为三个钢材应变都对 \(\zeta\) 一次，所以把上一节上/下钢壳的完整应变式直接代入以后：

\[
\frac{7900}{8281}
\left[
(\varepsilon_x^{s,\pm})^2+(\varepsilon_y^{s,\pm})^2
\right]
+
\frac{1100}{8281}
\varepsilon_x^{s,\pm}\varepsilon_y^{s,\pm}
+
\frac{75}{169}
(\gamma_{xy}^{s,\pm})^2
-
\left(\frac{355}{206000}\right)^2
=0
\]

严格是关于 \(\zeta\) 的二次方程。

因此每一个固定 \(x,y\) 的钢壳厚度最多两个内部屈服根，最多三个 elastic/plastic 厚度区间。

弹性段：

\[
\sigma_x^s
=
206000
\left(
\frac{100}{91}\varepsilon_x^s+
\frac{30}{91}\varepsilon_y^s
\right),
\]

\[
\sigma_y^s
=
206000
\left(
\frac{30}{91}\varepsilon_x^s+
\frac{100}{91}\varepsilon_y^s
\right),
\]

\[
\tau_{xy}^s
=
206000\frac{5}{13}\gamma_{xy}^s.
\]

塑性平台段：

\[
\sigma_x^s
=
\frac{355}{\bar\varepsilon_s}
\left(
\frac{100}{91}\varepsilon_x^s+
\frac{30}{91}\varepsilon_y^s
\right),
\]

\[
\sigma_y^s
=
\frac{355}{\bar\varepsilon_s}
\left(
\frac{30}{91}\varepsilon_x^s+
\frac{100}{91}\varepsilon_y^s
\right),
\]

\[
\tau_{xy}^s
=
\frac{355}{\bar\varepsilon_s}
\frac{5}{13}\gamma_{xy}^s.
\]

由于 \(\bar\varepsilon_s^2\) 是 \(\zeta\) 的二次式，
塑性厚度积分只涉及：

\[
\int\frac{1}{\sqrt{\text{二次式}}}\,d\zeta,\qquad
\int\frac{\zeta}{\sqrt{\text{二次式}}}\,d\zeta,\qquad
\int\frac{\zeta^2}{\sqrt{\text{二次式}}}\,d\zeta,
\]

它们均有对数或 \(\operatorname{asinh}\) 闭式。
所以 M5 的 \(\zeta\) 方向不存在离散爆炸。

真正尚未正式闭合的是：将这些包含
\(\sqrt{\cdot}\)、\(\operatorname{asinh}(\cdot)\)
而其系数又含 \(N,m\) 多波三角函数的钢壳厚度结果，再对整个 \(x,y\) 面进行 residual 和 Jacobian 积分时，当前项目尚没有像 UHPC rational-\(y\) 那样正式证明只剩一个确定性一维积分。

---

## 8. 九个 fixed-q 平衡方程

先把每层厚度积分后的膜力记为物理结果量
\(N_x^U,N_y^U,N_{xy}^U\)、
\(N_x^{s,+},N_y^{s,+},N_{xy}^{s,+}\)、
\(N_x^{s,-},N_y^{s,-},N_{xy}^{s,-}\)。
这些不是新增未知量，而是前面应力沿厚度的直接积分结果。

### 8.1 横向平均平衡

\[
\int_0^b\int_0^{a_h}
\left[
N_x^U+N_x^{s,+}+N_x^{s,-}
\right]dy\,dx
=0.
\]

### 8.2 轴向平均平衡

\[
\int_0^b\int_0^{a_h}
\left[
N_y^U+N_y^{s,+}+N_y^{s,-}
\right]dy\,dx
+
Pa_h
=0.
\]

### 8.3 \(B_x\) 谐波平衡

\[
\int_0^b\int_0^{a_h}
\left[
N_x^U+N_x^{s,+}+N_x^{s,-}
\right]
\cos\frac{2\pi x}{b}
\,dy\,dx
=0.
\]

### 8.4 \(B_y\) 谐波平衡

\[
\int_0^b\int_0^{a_h}
\left[
N_y^U+N_y^{s,+}+N_y^{s,-}
\right]
\cos\frac{2\pi y}{a_h}
\,dy\,dx
=0.
\]

### 8.5 \(H_x\) compatible mixed/shear 平衡

\[
\begin{aligned}
0={}&
\int_0^b\int_0^{a_h}
\Bigg\{
\left[
N_x^U+N_x^{s,+}+N_x^{s,-}
\right]
\cos\frac{2\pi x}{b}
\cos\frac{2\pi y}{a_h}\\
&-
\frac{b}{a_h}
\left[
N_{xy}^U+N_{xy}^{s,+}+N_{xy}^{s,-}
\right]
\sin\frac{2\pi x}{b}
\sin\frac{2\pi y}{a_h}
\Bigg\}
dy\,dx.
\end{aligned}
\]

### 8.6 \(H_y\) compatible mixed/shear 平衡

\[
\begin{aligned}
0={}&
\int_0^b\int_0^{a_h}
\Bigg\{
\left[
N_y^U+N_y^{s,+}+N_y^{s,-}
\right]
\cos\frac{2\pi x}{b}
\cos\frac{2\pi y}{a_h}\\
&-
\frac{a_h}{b}
\left[
N_{xy}^U+N_{xy}^{s,+}+N_{xy}^{s,-}
\right]
\sin\frac{2\pi x}{b}
\sin\frac{2\pi y}{a_h}
\Bigg\}
dy\,dx.
\end{aligned}
\]

### 8.7 整体 \(q\) 虚功平衡

UHPC 部分直接为：

\[
\begin{aligned}
0={}&
\int_0^b\int_0^{a_h}\int_{-t_c/2}^{t_c/2}
\Bigg[
\sigma_x^U
\left(
-\frac{\pi^2}{4}(q+q_0)
\cos\frac{2\pi y}{a_h}
+
z\frac{\pi^2}{b}
\sin\frac{\pi x}{b}
\sin\frac{\pi y}{a_h}
\right)\\
&+
\sigma_y^U
\left(
-\frac{\pi^2b^2}{4a_h^2}(q+q_0)
\cos\frac{2\pi x}{b}
+
z\frac{\pi^2b}{a_h^2}
\sin\frac{\pi x}{b}
\sin\frac{\pi y}{a_h}
\right)\\
&+
\tau_{xy}^U
\left(
-z\frac{2\pi^2}{a_h}
\cos\frac{\pi x}{b}
\cos\frac{\pi y}{a_h}
\right)
\Bigg]dz\,dy\,dx
\\
&+\text{上钢壳同样的 current-stress × 对 \(q\) 的显式应变导数积分}\\
&+\text{下钢壳同样的 current-stress × 对 \(q\) 的显式应变导数积分}\\
&-
P\frac{\pi^2b^2}{4a_h}(q+q_0).
\end{aligned}
\]

上钢壳在这一式中的 local-extra 对 \(q\) 导数是：

\[
\frac{\partial\Delta\varepsilon_x^{\ell,+}}{\partial q}
=
\pi(A_0^++A^+)
\cos\frac{\pi x}{b}
\sin\frac{\pi y}{a_h}
\frac{\partial\psi_\ell^+}{\partial x},
\]

\[
\frac{\partial\Delta\varepsilon_y^{\ell,+}}{\partial q}
=
\frac{\pi b}{a_h}(A_0^++A^+)
\sin\frac{\pi x}{b}
\cos\frac{\pi y}{a_h}
\frac{\partial\psi_\ell^+}{\partial y},
\]

\[
\begin{aligned}
\frac{\partial\Delta\gamma_{xy}^{\ell,+}}{\partial q}
={}&
\pi(A_0^++A^+)
\left[
\cos\frac{\pi x}{b}
\sin\frac{\pi y}{a_h}
\frac{\partial\psi_\ell^+}{\partial y}
+
\frac{b}{a_h}
\sin\frac{\pi x}{b}
\cos\frac{\pi y}{a_h}
\frac{\partial\psi_\ell^+}{\partial x}
\right].
\end{aligned}
\]

下钢壳对应三式仅把最前面的正号改成负号并使用 \(A_0^-,A^-,N^-,m^-\)。

### 8.8 上钢壳 \(A^+\) 平衡

\[
\begin{aligned}
0={}&
\int_0^b\int_0^{a_h}\int_{-t_s/2}^{t_s/2}
\Bigg\{
\sigma_x^{s,+}
\Bigg[
\pi(q_0+q)
\cos\frac{\pi x}{b}
\sin\frac{\pi y}{a_h}
\frac{\partial\psi_\ell^+}{\partial x}
+
(A_0^++A^+)
\left(\frac{\partial\psi_\ell^+}{\partial x}\right)^2
-\zeta
\frac{\partial^2\psi_\ell^+}{\partial x^2}
\Bigg]\\
&+
\sigma_y^{s,+}
\Bigg[
\frac{\pi b}{a_h}(q_0+q)
\sin\frac{\pi x}{b}
\cos\frac{\pi y}{a_h}
\frac{\partial\psi_\ell^+}{\partial y}
+
(A_0^++A^+)
\left(\frac{\partial\psi_\ell^+}{\partial y}\right)^2
-\zeta
\frac{\partial^2\psi_\ell^+}{\partial y^2}
\Bigg]\\
&+
\tau_{xy}^{s,+}
\Bigg[
\pi(q_0+q)
\left(
\cos\frac{\pi x}{b}\sin\frac{\pi y}{a_h}
\frac{\partial\psi_\ell^+}{\partial y}
+
\frac{b}{a_h}\sin\frac{\pi x}{b}\cos\frac{\pi y}{a_h}
\frac{\partial\psi_\ell^+}{\partial x}
\right)\\
&\qquad\qquad+
2(A_0^++A^+)
\frac{\partial\psi_\ell^+}{\partial x}
\frac{\partial\psi_\ell^+}{\partial y}
-
2\zeta
\frac{\partial^2\psi_\ell^+}{\partial x\partial y}
\Bigg]
\Bigg\}
d\zeta\,dy\,dx.
\end{aligned}
\]

### 8.9 下钢壳 \(A^-\) 平衡

\[
\begin{aligned}
0={}&
\int_0^b\int_0^{a_h}\int_{-t_s/2}^{t_s/2}
\Bigg\{
\sigma_x^{s,-}
\Bigg[
-\pi(q_0+q)
\cos\frac{\pi x}{b}
\sin\frac{\pi y}{a_h}
\frac{\partial\psi_\ell^-}{\partial x}
+
(A_0^-+A^-)
\left(\frac{\partial\psi_\ell^-}{\partial x}\right)^2
+\zeta
\frac{\partial^2\psi_\ell^-}{\partial x^2}
\Bigg]\\
&+
\sigma_y^{s,-}
\Bigg[
-\frac{\pi b}{a_h}(q_0+q)
\sin\frac{\pi x}{b}
\cos\frac{\pi y}{a_h}
\frac{\partial\psi_\ell^-}{\partial y}
+
(A_0^-+A^-)
\left(\frac{\partial\psi_\ell^-}{\partial y}\right)^2
+\zeta
\frac{\partial^2\psi_\ell^-}{\partial y^2}
\Bigg]\\
&+
\tau_{xy}^{s,-}
\Bigg[
-\pi(q_0+q)
\left(
\cos\frac{\pi x}{b}\sin\frac{\pi y}{a_h}
\frac{\partial\psi_\ell^-}{\partial y}
+
\frac{b}{a_h}\sin\frac{\pi x}{b}\cos\frac{\pi y}{a_h}
\frac{\partial\psi_\ell^-}{\partial x}
\right)\\
&\qquad\qquad+
2(A_0^-+A^-)
\frac{\partial\psi_\ell^-}{\partial x}
\frac{\partial\psi_\ell^-}{\partial y}
+
2\zeta
\frac{\partial^2\psi_\ell^-}{\partial x\partial y}
\Bigg]
\Bigg\}
d\zeta\,dy\,dx.
\end{aligned}
\]

以上九式就是正式 fixed-\(q\) 根问题，没有第十个结构未知量。

---

## 9. Newton 的全部九未知量更新流程

第 \(n\) 次迭代的状态是：

\[
E_x^{(n)},E_y^{(n)},B_x^{(n)},B_y^{(n)},H_x^{(n)},H_y^{(n)},
P^{(n)},A^{+,(n)},A^{-,(n)}.
\]