# UCFT M6 — inner membrane condensation + outer \(R_q,R_{A^+},R_{A^-}\) + exact Schur Jacobian

更新时间：2026-09-30 17:05 +08:00

状态：M0–M5 已完成；本文件正式完成 M6 的方程组组装。M6 不运行九试件，不调用 FEM 目标值，不冻结尚未给定的 UHPC tensile polynomial 或 Q355 plastic polynomial 数值系数。

---

# 1. M6 唯一任务

M6 只做三件事：

\[
\boxed{
\text{M3 compatible inner membrane space}
+
\text{M4 UHPC current operator}
+
\text{M5 steel current operator}
}
\]

组装成为一个统一的 current virtual-work system；

给定：

\[
\boxed{q}
\]

以后求解：

\[
\boxed{
P,\qquad A^+,\qquad A^-,
}
\]

同时内部凝聚：

\[
\boxed{
\boldsymbol\xi
}
\]

其中 \(\boldsymbol\xi\) 只包含 compatible membrane variables，不属于结构级路径自由度。

M6 最终方程组是：

\[
\boxed{
\mathbf G(\boldsymbol\xi,P,A^+,A^-;q)=\mathbf0
}
\]

以及：

\[
\boxed{
R_q(\boldsymbol\xi,P,A^+,A^-;q)=0,
}
\]

\[
\boxed{
R_{A^+}(\boldsymbol\xi,P,A^+,A^-;q)=0,
}
\]

\[
\boxed{
R_{A^-}(\boldsymbol\xi,P,A^+,A^-;q)=0.
}
\]

---

# 2. 坐标、整体构形和 global curvature

定义：

\[
X=\frac{\pi x}{b},
\qquad
Y=\frac{\pi y}{a_h},
\qquad
r=\frac{b}{a_h}.
\]

整体 stress-free initial geometry：

\[
W_0=bq_0\sin X\sin Y.
\]

当前整体构形：

\[
W_g=b(q_0+q)\sin X\sin Y.
\]

loading-induced global displacement：

\[
w_g=bq\sin X\sin Y.
\]

仍定义：

\[
Q(q)=q^2+2q_0q,
\]

\[
C_q=\frac{\pi^2}{8}(q^2+2q_0q),
\]

\[
C_q'=\frac{\pi^2}{4}(q+q_0),
\]

\[
C_q''=\frac{\pi^2}{4}.
\]

当前 global loading-induced curvature vector定义为：

\[
\boldsymbol\kappa^g
=
\begin{bmatrix}
\kappa_x^g\\
\kappa_y^g\\
\kappa_{xy}^g
\end{bmatrix},
\]

其中：

\[
\boxed{
\kappa_x^g
=
\frac{\pi^2q}{b}\sin X\sin Y
}
\]

\[
\boxed{
\kappa_y^g
=
\frac{\pi^2q}{b}r^2\sin X\sin Y
}
\]

\[
\boxed{
\kappa_{xy}^g
=
-\frac{2\pi^2q}{b}r\cos X\cos Y.
}
\]

所以：

\[
\boxed{
\boldsymbol\kappa^g_{,q}
=
\begin{bmatrix}
\dfrac{\pi^2}{b}\sin X\sin Y\\[2mm]
\dfrac{\pi^2r^2}{b}\sin X\sin Y\\[2mm]
-\dfrac{2\pi^2r}{b}\cos X\cos Y
\end{bmatrix}
}
\]

并且：

\[
\boldsymbol\kappa^g_{,qq}=\mathbf0.
\]

---

# 3. baseline C1 membrane field

M6 的 production superspace 使用 C1；C0 仍是删除 \(H_x,H_y\) 后的严格降阶版本。

baseline C1：

\[
\boxed{
\varepsilon_x^0
=
E_x+B_x\cos2X-C_q\cos2Y
+H_x\cos2X\cos2Y
}
\]

\[
\boxed{
\varepsilon_y^0
=
E_y-C_qr^2\cos2X+B_y\cos2Y
+H_y\cos2X\cos2Y
}
\]

\[
\boxed{
\gamma_{xy}^0
=
-
\left(
rH_x+\frac1rH_y
\right)
\sin2X\sin2Y.
}
\]

因此：

\[
\boxed{
\boldsymbol\varepsilon^0_{,q}
=
\begin{bmatrix}
-C_q'\cos2Y\\
-C_q'r^2\cos2X\\
0
\end{bmatrix}
}
\]

以及：

\[
\boxed{
\boldsymbol\varepsilon^0_{,qq}
=
\begin{bmatrix}
-C_q''\cos2Y\\
-C_q''r^2\cos2X\\
0
\end{bmatrix}.
}
\]

---

# 4. inner membrane variables 的完整身份

baseline C1 的六个 inner variables 是：

\[
E_x,\quad E_y,\quad B_x,\quad B_y,\quad H_x,\quad H_y.
\]

对应 generalized virtual-strain basis：

\[
\boxed{
\mathbf B_{E_x}
=
\begin{bmatrix}
1\\0\\0
\end{bmatrix}
}
\]

\[
\boxed{
\mathbf B_{E_y}
=
\begin{bmatrix}
0\\1\\0
\end{bmatrix}
}
\]

\[
\boxed{
\mathbf B_{B_x}
=
\begin{bmatrix}
\cos2X\\0\\0
\end{bmatrix}
}
\]

\[
\boxed{
\mathbf B_{B_y}
=
\begin{bmatrix}
0\\\cos2Y\\0
\end{bmatrix}
}
\]

\[
\boxed{
\mathbf B_{H_x}
=
\begin{bmatrix}
\cos2X\cos2Y\\
0\\
-r\sin2X\sin2Y
\end{bmatrix}
}
\]

\[
\boxed{
\mathbf B_{H_y}
=
\begin{bmatrix}
0\\
\cos2X\cos2Y\\
-\dfrac1r\sin2X\sin2Y
\end{bmatrix}.
}
\]

这些 basis 直接作用于 UHPC 和上下钢壳的共同面内位移场。

---

# 5. M3 frequency-generated enrichment 在 M6 中如何进入

M6 不一次性建立巨大 Fourier basis。

对当前 state，M3 candidate ledger 中只有 omitted residual 显著的 frequency 才实例化为 inner variables。

## 5.1 C-family，\(k>0,l>0\)

对每一个被激活的 \((k,l)\)：

\[
\boxed{
\mathbf B_{C_x^{kl}}
=
\begin{bmatrix}
\cos kX\cos lY\\
0\\
-\dfrac{lr}{k}\sin kX\sin lY
\end{bmatrix}
}
\]

\[
\boxed{
\mathbf B_{C_y^{kl}}
=
\begin{bmatrix}
0\\
\cos kX\cos lY\\
-\dfrac{k}{lr}\sin kX\sin lY
\end{bmatrix}.
}
\]

对应 residual：

\[
\boxed{
G_{C_x^{kl}}
=
\int_\Omega
\left[
N_x\cos kX\cos lY
-
\frac{lr}{k}N_{xy}\sin kX\sin lY
\right]dA
=0
}
\]

\[
\boxed{
G_{C_y^{kl}}
=
\int_\Omega
\left[
N_y\cos kX\cos lY
-
\frac{k}{lr}N_{xy}\sin kX\sin lY
\right]dA
=0.
}
\]

## 5.2 S-family，\(k>0,l>0\)

对 qA channel：

\[
\boxed{
\mathbf B_{S_x^{kl}}
=
\begin{bmatrix}
\sin kX\sin lY\\
0\\
-\dfrac{lr}{k}\cos kX\cos lY
\end{bmatrix}
}
\]

\[
\boxed{
\mathbf B_{S_y^{kl}}
=
\begin{bmatrix}
0\\
\sin kX\sin lY\\
-\dfrac{k}{lr}\cos kX\cos lY
\end{bmatrix}.
}
\]

对应：

\[
\boxed{
G_{S_x^{kl}}
=
\int_\Omega
\left[
N_x\sin kX\sin lY
-
\frac{lr}{k}N_{xy}\cos kX\cos lY
\right]dA
=0
}
\]

\[
\boxed{
G_{S_y^{kl}}
=
\int_\Omega
\left[
N_y\sin kX\sin lY
-
\frac{k}{lr}N_{xy}\cos kX\cos lY
\right]dA
=0.
}
\]

## 5.3 1-D B-family

A² channel 产生的 1-D companion：

\[
\boxed{
\mathbf B_{B_x^k}
=
\begin{bmatrix}
\cos kX\\0\\0
\end{bmatrix}
}
\]

\[
\boxed{
G_{B_x^k}
=
\int_\Omega N_x\cos kX\,dA
=0.
}
\]

以及：

\[
\boxed{
\mathbf B_{B_y^l}
=
\begin{bmatrix}
0\\\cos lY\\0
\end{bmatrix}
}
\]

\[
\boxed{
G_{B_y^l}
=
\int_\Omega N_y\cos lY\,dA
=0.
}
\]

常数项继续由 \(E_x,E_y\) 吸收。

因此 M6 的 inner state 是：

\[
\boxed{
\boldsymbol\xi
=
[
E_x,E_y,B_x,B_y,H_x,H_y,
\text{当前被激活的有限 C/S/B variables}
]^T.
}
\]

这些变量全部属于 inner condensation；结构层仍然只有：

\[
q,\qquad A^+,\qquad A^-.
\]

---

# 6. steel-local whole-face geometry 的 M6 完整运动学

定义某一钢面：

\[
s_+=+1,
\qquad
s_-=-1.
\]

局部形函数：

\[
\boxed{
\psi_\ell
=
[1-\cos(2NX)]
[1-\cos(2mY)].
}
\]

这里 \(N,m\) 保持符号；TOP/BOTTOM 分别使用 \(N^\pm,m^\pm\)。

当前钢面：

\[
W_s^\pm
=
W_g+s_\pm(A_0^\pm+A^\pm)\psi_\ell^\pm.
\]

stress-free initial steel geometry：

\[
W_{s0}^\pm
=
W_0+s_\pm A_0^\pm\psi_\ell^\pm.
\]

共同 membrane field \(\boldsymbol\varepsilon^0\) 已经包含 global-only Kármán contribution，所以钢壳相对于 global-only field 的额外中面几何应变必须只取：

\[
\frac12
\left[
(W_s^\pm)_{,x}^2-(W_{s0}^\pm)_{,x}^2
-
(W_g)_{,x}^2+(W_0)_{,x}^2
\right]
\]

等差额。

将它显式展开，TOP/BOTTOM 的 local extra normal \(x\) strain：

\[
\boxed{
\begin{aligned}
\Delta\varepsilon_x^{\ell,\pm}
={}&
s_\pm\pi
\left(
q_0A^\pm+qA_0^\pm+qA^\pm
\right)
\cos X\sin Y\,
\psi_{\ell,x}^\pm
\\
&+
\frac12
\left[
(A^\pm)^2+2A_0^\pm A^\pm
\right]
(\psi_{\ell,x}^\pm)^2.
\end{aligned}
}
\]

轴向：

\[
\boxed{
\begin{aligned}
\Delta\varepsilon_y^{\ell,\pm}
={}&
s_\pm\pi r
\left(
q_0A^\pm+qA_0^\pm+qA^\pm
\right)
\sin X\cos Y\,
\psi_{\ell,y}^\pm
\\
&+
\frac12
\left[
(A^\pm)^2+2A_0^\pm A^\pm
\right]
(\psi_{\ell,y}^\pm)^2.
\end{aligned}
}
\]

工程剪应变：

\[
\boxed{
\begin{aligned}
\Delta\gamma_{xy}^{\ell,\pm}
={}&
s_\pm\pi
\left(
q_0A^\pm+qA_0^\pm+qA^\pm
\right)
\left[
\cos X\sin Y\,\psi_{\ell,y}^\pm
+
r\sin X\cos Y\,\psi_{\ell,x}^\pm
\right]
\\
&+
\left[
(A^\pm)^2+2A_0^\pm A^\pm
\right]
\psi_{\ell,x}^\pm
\psi_{\ell,y}^\pm.
\end{aligned}
}
\]

因此 M3 锁定的三个物理 channel 在 M6 中全部保留：

\[
\boxed{
q^2+2q_0q
}
\]

\[
\boxed{
q_0A^\pm+qA_0^\pm+qA^\pm
}
\]

\[
\boxed{
(A^\pm)^2+2A_0^\pm A^\pm.
}
\]

---

# 7. steel-local curvature

因为 \(A_0^\pm\) 是 stress-free initial geometry，local bending strain 只由加载新增 \(A^\pm\) 产生。

定义：

\[
\boldsymbol\kappa^{\ell,\pm}
=
\begin{bmatrix}
\kappa_x^{\ell,\pm}\\
\kappa_y^{\ell,\pm}\\
\kappa_{xy}^{\ell,\pm}
\end{bmatrix}.
\]

则：

\[
\boxed{
\kappa_x^{\ell,\pm}
=
-s_\pm A^\pm\psi_{\ell,xx}^\pm
}
\]

\[
\boxed{
\kappa_y^{\ell,\pm}
=
-s_\pm A^\pm\psi_{\ell,yy}^\pm
}
\]

\[
\boxed{
\kappa_{xy}^{\ell,\pm}
=
-2s_\pm A^\pm\psi_{\ell,xy}^\pm.
}
\]

---

# 8. UHPC 与 steel 的完整 thickness strain input

## 8.1 UHPC

\[
-\frac{t_c}{2}\le z\le\frac{t_c}{2}.
\]

UHPC：

\[
\boxed{
\boldsymbol\varepsilon^U(z)
=
\boldsymbol\varepsilon^0
+
z\boldsymbol\kappa^g.
}
\]

这一输入直接送入 M4 directional tensile/compressive analytic active-set。

## 8.2 TOP/BOTTOM steel

令上下钢壳自身中面相对于 UHPC 中面的位置为：

\[
z_s^\pm.
\]

自身厚度坐标：

\[
-\frac{t_s^\pm}{2}
\le\zeta\le
\frac{t_s^\pm}{2}.
\]

则：

\[
\boxed{
\boldsymbol\varepsilon^{s,\pm}(\zeta)
=
\boldsymbol\varepsilon^0
+
\Delta\boldsymbol\varepsilon^{\ell,\pm}
+
(z_s^\pm+\zeta)\boldsymbol\kappa^g
+
\zeta\boldsymbol\kappa^{\ell,\pm}.
}
\]

所以 M5 中：

\[
\varepsilon_x=a_x+b_x\zeta,
\qquad
\varepsilon_y=a_y+b_y\zeta,
\qquad
\gamma_{xy}=a_\gamma+b_\gamma\zeta
\]

并没有新增运动学假定，而是这里的直接结果：

\[
\boxed{
\mathbf a^\pm
=
\boldsymbol\varepsilon^0
+
\Delta\boldsymbol\varepsilon^{\ell,\pm}
+
z_s^\pm\boldsymbol\kappa^g
}
\]

\[
\boxed{
\mathbf b^\pm
=
\boldsymbol\kappa^g
+
\boldsymbol\kappa^{\ell,\pm}.
}
\]

---

# 9. inner generalized residual 的统一 current virtual-work 形式

对任一 inner variable \(\xi_j\)，其虚拟应变 basis：

\[
\mathbf B_j
=
\frac{\partial\boldsymbol\varepsilon^0}
{\partial\xi_j}.
\]

因为 inner basis 不改变 \(W_g\) 和 \(W_s^\pm\)，其厚度方向都是相同的纯 membrane virtual strain。

定义 UHPC current stress：

\[
\boldsymbol\sigma^U
=
\begin{bmatrix}
\sigma_x^U\\
\sigma_y^U\\
\tau_{xy}^U
\end{bmatrix},
\]

上下钢：

\[
\boldsymbol\sigma^{s,+},
\qquad
\boldsymbol\sigma^{s,-}.
\]

则除 \(E_y\) 外：

\[
\boxed{
G_{\xi_j}
=
\int_\Omega
\int_{-t_c/2}^{t_c/2}
(\mathbf B_j)^T
\boldsymbol\sigma^U\,dz\,dA
+
\int_\Omega
\int_{-t_s^+/2}^{t_s^+/2}
(\mathbf B_j)^T
\boldsymbol\sigma^{s,+}\,d\zeta\,dA
+
\int_\Omega
\int_{-t_s^-/2}^{t_s^-/2}
(\mathbf B_j)^T
\boldsymbol\sigma^{s,-}\,d\zeta\,dA
=0.
}
\]

对于 \(E_y\)，有真实轴向边界 traction 的外功：

\[
\boxed{
G_{E_y}
=
\int_\Omega N_y\,dA
+
Pa_h
=0.
}
\]

因此 baseline 六式严格恢复：

\[
G_{E_x}=0,
\quad
G_{E_y}=0,
\quad
G_{B_x}=0,
\quad
G_{B_y}=0,
\quad
G_{H_x}=0,
\quad
G_{H_y}=0.
\]

新增 C/S/B residual 也只是同一个 current virtual-work relation 在对应 compatible basis 上的投影，不是另一套物理方程。

---

# 10. 外层 \(q\) 虚功方向

固定 inner variables、固定 \(P,A^+,A^-\) 后：

\[
\boxed{
\mathbf B_q^U(z)
=
\boldsymbol\varepsilon^0_{,q}
+
z\boldsymbol\kappa^g_{,q}.
}
\]

对钢壳：

\[
\boxed{
\mathbf B_q^{s,\pm}(\zeta)
=
\boldsymbol\varepsilon^0_{,q}
+
\Delta\boldsymbol\varepsilon^{\ell,\pm}_{,q}
+
(z_s^\pm+\zeta)
\boldsymbol\kappa^g_{,q}.
}
\]

其中：

\[
\boxed{
\Delta\varepsilon_{x,q}^{\ell,\pm}
=
s_\pm\pi(A_0^\pm+A^\pm)
\cos X\sin Y\,
\psi_{\ell,x}^\pm
}
\]

\[
\boxed{
\Delta\varepsilon_{y,q}^{\ell,\pm}
=
s_\pm\pi r(A_0^\pm+A^\pm)
\sin X\cos Y\,
\psi_{\ell,y}^\pm
}
\]

\[
\boxed{
\begin{aligned}
\Delta\gamma_{xy,q}^{\ell,\pm}
={}&
s_\pm\pi(A_0^\pm+A^\pm)
\left[
\cos X\sin Y\,
\psi_{\ell,y}^\pm
+
r\sin X\cos Y\,
\psi_{\ell,x}^\pm
\right].
\end{aligned}
}
\]

因此：

\[
\boxed{
\begin{aligned}
R_q
={}&
\int_\Omega
\int_{-t_c/2}^{t_c/2}
(\mathbf B_q^U)^T
\boldsymbol\sigma^U
\,dz\,dA
\\
&+
\int_\Omega
\int_{-t_s^+/2}^{t_s^+/2}
(\mathbf B_q^{s,+})^T
\boldsymbol\sigma^{s,+}
\,d\zeta\,dA
\\
&+
\int_\Omega
\int_{-t_s^-/2}^{t_s^-/2}
(\mathbf B_q^{s,-})^T
\boldsymbol\sigma^{s,-}
\,d\zeta\,dA
\\
&-
Pa_hr^2C_q'
=0.
\end{aligned}
}
\]

最后一项严格继承 M2 已修正并通过线弹性极限核验的 q 外载虚功。

---

# 11. 上、下钢壳 \(A^\pm\) 局部平衡

对某一侧：

\[
\boxed{
\mathbf B_A^{s,\pm}(\zeta)
=
\Delta\boldsymbol\varepsilon_{,A^\pm}^{\ell,\pm}
+
\zeta
\boldsymbol\kappa_{,A^\pm}^{\ell,\pm}.
}
\]

中面部分：

\[
\boxed{
\Delta\varepsilon_{x,A}^{\ell,\pm}
=
s_\pm\pi(q_0+q)
\cos X\sin Y\,
\psi_{\ell,x}^\pm
+
(A_0^\pm+A^\pm)
(\psi_{\ell,x}^\pm)^2
}
\]

\[
\boxed{
\Delta\varepsilon_{y,A}^{\ell,\pm}
=
s_\pm\pi r(q_0+q)
\sin X\cos Y\,
\psi_{\ell,y}^\pm
+
(A_0^\pm+A^\pm)
(\psi_{\ell,y}^\pm)^2
}
\]

\[
\boxed{
\begin{aligned}
\Delta\gamma_{xy,A}^{\ell,\pm}
={}&
s_\pm\pi(q_0+q)
\left[
\cos X\sin Y\,
\psi_{\ell,y}^\pm
+
r\sin X\cos Y\,
\psi_{\ell,x}^\pm
\right]
\\
&+
2(A_0^\pm+A^\pm)
\psi_{\ell,x}^\pm
\psi_{\ell,y}^\pm.
\end{aligned}
}
\]

local curvature derivative：

\[
\boxed{
\boldsymbol\kappa_{,A^\pm}^{\ell,\pm}
=
\begin{bmatrix}
-s_\pm\psi_{\ell,xx}^\pm\\
-s_\pm\psi_{\ell,yy}^\pm\\
-2s_\pm\psi_{\ell,xy}^\pm
\end{bmatrix}.
}
\]

局部 amplitude 不直接承受外加 generalized force，因此：

\[
\boxed{
R_{A^+}
=
\int_\Omega
\int_{-t_s^+/2}^{t_s^+/2}
(\mathbf B_A^{s,+})^T
\boldsymbol\sigma^{s,+}
\,d\zeta\,dA
=0
}
\]

\[
\boxed{
R_{A^-}
=
\int_\Omega
\int_{-t_s^-/2}^{t_s^-/2}
(\mathbf B_A^{s,-})^T
\boldsymbol\sigma^{s,-}
\,d\zeta\,dA
=0.
}
\]

因此：

\[
\boxed{
A^\pm
}
\]

仍然是由局部平衡自然求得的从属响应，不是 prescribed \(A(q)\)。

---

# 12. outer second-kinematic terms：Jacobian 中不能漏

M6 必须区分：

\[
\mathbf B_a^T\mathbf C_t\mathbf B_b
\]

材料切线项，和：

\[
\boldsymbol\sigma^T
\boldsymbol\varepsilon_{,ab}
\]

current-stress geometric term。

## 12.1 \(qA^\pm\) 二阶导

\[
\boxed{
\Delta\varepsilon_{x,qA}^{\ell,\pm}
=
s_\pm\pi
\cos X\sin Y\,
\psi_{\ell,x}^\pm
}
\]

\[
\boxed{
\Delta\varepsilon_{y,qA}^{\ell,\pm}
=
s_\pm\pi r
\sin X\cos Y\,
\psi_{\ell,y}^\pm
}
\]

\[
\boxed{
\begin{aligned}
\Delta\gamma_{xy,qA}^{\ell,\pm}
=
s_\pm\pi
\left[
\cos X\sin Y\,\psi_{\ell,y}^\pm
+
r\sin X\cos Y\,\psi_{\ell,x}^\pm
\right].
\end{aligned}
}
\]

## 12.2 \(A^\pm A^\pm\) 二阶导

\[
\boxed{
\Delta\varepsilon_{x,AA}^{\ell,\pm}
=
(\psi_{\ell,x}^\pm)^2
}
\]

\[
\boxed{
\Delta\varepsilon_{y,AA}^{\ell,\pm}
=
(\psi_{\ell,y}^\pm)^2
}
\]

\[
\boxed{
\Delta\gamma_{xy,AA}^{\ell,\pm}
=
2\psi_{\ell,x}^\pm\psi_{\ell,y}^\pm.
}
\]

这些项正是：

\[
qA
\]

与：

\[
A^2
\]

在 consistent Jacobian 中留下的几何刚度来源。

## 12.3 \(qq\) 二阶导

局部 extra 对 q 只有一次项：

\[
\Delta\boldsymbol\varepsilon_{,qq}^{\ell,\pm}=\mathbf0.
\]

但共同 C1 particular membrane field 有：

\[
\boxed{
\boldsymbol\varepsilon_{,qq}^0
=
\begin{bmatrix}
-\pi^2\cos2Y/4\\
-\pi^2r^2\cos2X/4\\
0
\end{bmatrix}.
}
\]

---

# 13. material tangent 接口

M6 不把 UHPC 和 steel 强行写成同一种 constitutive potential。

只要求每个材料 operator 返回：

\[
\boxed{
\boldsymbol\sigma
}
\]

以及 current derivative：

\[
\boxed{
\mathbf C_t
=
\frac{\partial\boldsymbol\sigma}
{\partial\boldsymbol\varepsilon}.
}
\]

UHPC：

- finite stress 来自 M4 directional piecewise polynomial active-set；
- tangent 可以非对称；
- cracking/softening 下仍用 current/incremental virtual work。

Steel：

- finite stress 使用 M5 \(E_{sec}\)；
- tangent 使用 M5 consistent \(E_{tan}\) relation；
- 两者不得混用。

因此后续 Jacobian 不要求全局对称。

---

# 14. moving active-boundary 对 Jacobian 的处理

M4/M5 的 active boundaries 都随 state 移动。

但只要材料应力在 branch interface 连续，分区积分的一阶导数不需要额外保留一项“边界运动力”。

设：

\[
I(\alpha)
=
\int_a^{s(\alpha)}
f_1(x,\alpha)\,dx
+
\int_{s(\alpha)}^b
f_2(x,\alpha)\,dx.
\]

则：

\[
\frac{dI}{d\alpha}
=
\int_a^{s}
\frac{\partial f_1}{\partial\alpha}dx
+
\int_s^b
\frac{\partial f_2}{\partial\alpha}dx
+
[f_1(s)-f_2(s)]
\frac{ds}{d\alpha}.
\]

如果：

\[
\boxed{
f_1(s)=f_2(s)
}
\]

则：

\[
\boxed{
[f_1-f_2]s_{,\alpha}=0.
}
\]

因此 M4 连续 polynomial branch 和 M5 已修正为连续 finite stress 的 yield interface 都可以直接使用当前 tangent 分区积分形成 Jacobian。

在 branch topology 切换的瞬间，Jacobian 允许 piecewise / semismooth；这属于 event localization 问题，不需要重新改成高斯材料点。

---

# 15. full residual system

给定 q，定义：

\[
\boxed{
\mathbf z
=
\begin{bmatrix}
P\\A^+\\A^-
\end{bmatrix}.
}
\]

inner vector：

\[
\boxed{
\boldsymbol\xi
=
[
E_x,E_y,B_x,B_y,H_x,H_y,
\text{active compatible enrichments}
]^T.
}
\]

完整 residual：

\[
\boxed{
\mathbf F
=
\begin{bmatrix}
\mathbf G(\boldsymbol\xi,\mathbf z;q)\\
R_q(\boldsymbol\xi,\mathbf z;q)\\
R_{A^+}(\boldsymbol\xi,\mathbf z;q)\\
R_{A^-}(\boldsymbol\xi,\mathbf z;q)
\end{bmatrix}
=
\mathbf0.
}
\]

这就是 M6 的完整方程组。

它不是：

\[
6+3
\]

个新的结构自由度。

真正结构层仍然只有：

\[
\boxed{
q\rightarrow(P,A^+,A^-).
}
\]

\(\boldsymbol\xi\) 每个 q-state 都被内部消元。

---

# 16. full Jacobian block structure

固定当前 active-set topology：

\[
\boxed{
\mathbf J_{\rm full}
=
\begin{bmatrix}
\mathbf G_{\xi} & \mathbf G_z\\
\mathbf R_{\xi} & \mathbf R_z
\end{bmatrix}.
}
\]

其中：

\[
\mathbf G_\xi
=
\frac{\partial\mathbf G}{\partial\boldsymbol\xi},
\]

\[
\mathbf G_z
=
\frac{\partial\mathbf G}{\partial\mathbf z},
\]

\[
\mathbf R_\xi
=
\frac{\partial\mathbf R}{\partial\boldsymbol\xi},
\]

\[
\mathbf R_z
=
\frac{\partial\mathbf R}{\partial\mathbf z}.
\]

---

# 17. \(\mathbf G_\xi\) 的明确形式

因为所有 inner variables 都在线性 compatible membrane basis 中进入，所以：

\[
\boxed{
\begin{aligned}
(\mathbf G_\xi)_{ij}
={}&
\int_{\Omega}
\int_{-t_c/2}^{t_c/2}
\mathbf B_i^T
\mathbf C_t^U
\mathbf B_j
\,dz\,dA
\\
&+
\int_{\Omega}
\int_{-t_s^+/2}^{t_s^+/2}
\mathbf B_i^T
\mathbf C_t^{s,+}
\mathbf B_j
\,d\zeta\,dA
\\
&+
\int_{\Omega}
\int_{-t_s^-/2}^{t_s^-/2}
\mathbf B_i^T
\mathbf C_t^{s,-}
\mathbf B_j
\,d\zeta\,dA.
\end{aligned}
}
\]

inner variables 之间没有第二运动学导数，因此不存在：

\[
\sigma:\varepsilon_{,\xi_i\xi_j}
\]

项。

若 UHPC tangent 非对称：

\[
\boxed{
\mathbf G_\xi
}
\]

也允许非对称，不强制做对称化。

---

# 18. \(\mathbf G_z\)

P 不进入材料 current strain，只进入 \(G_{E_y}\) 的外载项，因此：

\[
\boxed{
\frac{\partial G_{E_y}}{\partial P}
=a_h
}
\]

而其它 inner residual：

\[
\boxed{
\frac{\partial G_{\xi_j}}{\partial P}=0
\qquad
(\xi_j\ne E_y).
}
\]

对于 \(A^+\)：

\[
\boxed{
\frac{\partial G_{\xi_j}}{\partial A^+}
=
\int_{\Omega}
\int_{-t_s^+/2}^{t_s^+/2}
\mathbf B_j^T
\mathbf C_t^{s,+}
\mathbf B_A^{s,+}
\,d\zeta\,dA.
}
\]

对于 \(A^-\)：

\[
\boxed{
\frac{\partial G_{\xi_j}}{\partial A^-}
=
\int_{\Omega}
\int_{-t_s^-/2}^{t_s^-/2}
\mathbf B_j^T
\mathbf C_t^{s,-}
\mathbf B_A^{s,-}
\,d\zeta\,dA.
}
\]

这两列就是 local steel deformation 通过 nonlinear membrane condensation 反馈整体面内状态的代数入口。

---

# 19. \(\mathbf R_\xi\)

由于 \(\mathbf B_q,\mathbf B_A\) 都不依赖 inner amplitudes：

\[
\boxed{
\frac{\partial R_q}{\partial\xi_j}
=
\int_U
(\mathbf B_q^U)^T
\mathbf C_t^U
\mathbf B_j\,dV
+
\int_{s+}
(\mathbf B_q^{s,+})^T
\mathbf C_t^{s,+}
\mathbf B_j\,dV
+
\int_{s-}
(\mathbf B_q^{s,-})^T
\mathbf C_t^{s,-}
\mathbf B_j\,dV.
}
\]

\[
\boxed{
\frac{\partial R_{A^+}}{\partial\xi_j}
=
\int_{s+}
(\mathbf B_A^{s,+})^T
\mathbf C_t^{s,+}
\mathbf B_j\,dV.
}
\]

\[
\boxed{
\frac{\partial R_{A^-}}{\partial\xi_j}
=
\int_{s-}
(\mathbf B_A^{s,-})^T
\mathbf C_t^{s,-}
\mathbf B_j\,dV.
}
\]

若 tangent 非对称，不要求：

\[
\mathbf R_\xi=\mathbf G_z^T.
\]

这是 current directional UHPC operator 下的正常结果。

---

# 20. \(\mathbf R_z\)

列变量顺序为：

\[
P,\qquad A^+,\qquad A^-.
\]

## 20.1 P 列

\[
\boxed{
\frac{\partial R_q}{\partial P}
=
-a_hr^2C_q'
}
\]

\[
\boxed{
\frac{\partial R_{A^+}}{\partial P}=0,
\qquad
\frac{\partial R_{A^-}}{\partial P}=0.
}
\]

## 20.2 \(A^+\) 列

\[
\boxed{
\begin{aligned}
\frac{\partial R_q}{\partial A^+}
={}&
\int_{s+}
(\mathbf B_q^{s,+})^T
\mathbf C_t^{s,+}
\mathbf B_A^{s,+}
\,dV
\\
&+
\int_{s+}
(\boldsymbol\sigma^{s,+})^T
\Delta\boldsymbol\varepsilon_{,qA}^{\ell,+}
\,dV.
\end{aligned}
}
\]

\[
\boxed{
\frac{\partial R_{A^+}}{\partial A^+}
=
\int_{s+}
(\mathbf B_A^{s,+})^T
\mathbf C_t^{s,+}
\mathbf B_A^{s,+}
\,dV
+
\int_{s+}
(\boldsymbol\sigma^{s,+})^T
\Delta\boldsymbol\varepsilon_{,AA}^{\ell,+}
\,dV.
}
\]

直接 partial：

\[
\boxed{
\frac{\partial R_{A^-}}{\partial A^+}=0.
}
\]

## 20.3 \(A^-\) 列

\[
\boxed{
\begin{aligned}
\frac{\partial R_q}{\partial A^-}
={}&
\int_{s-}
(\mathbf B_q^{s,-})^T
\mathbf C_t^{s,-}
\mathbf B_A^{s,-}
\,dV
\\
&+
\int_{s-}
(\boldsymbol\sigma^{s,-})^T
\Delta\boldsymbol\varepsilon_{,qA}^{\ell,-}
\,dV.
\end{aligned}
}
\]

\[
\boxed{
\frac{\partial R_{A^-}}{\partial A^-}
=
\int_{s-}
(\mathbf B_A^{s,-})^T
\mathbf C_t^{s,-}
\mathbf B_A^{s,-}
\,dV
+
\int_{s-}
(\boldsymbol\sigma^{s,-})^T
\Delta\boldsymbol\varepsilon_{,AA}^{\ell,-}
\,dV.
}
\]

直接 partial：

\[
\boxed{
\frac{\partial R_{A^+}}{\partial A^-}=0.
}
\]

需要强调：

\[
\boxed{
\text{direct }R_{A^+A^-}=0
}
\]

不意味着凝聚以后 top/bottom uncoupled。

两侧通过：

\[
\boldsymbol\xi
\]

发生间接耦合，因此 condensed matrix 的：

\[
(K_{\rm cond})_{A^+A^-}
\]

通常不为零。

这正是 nonlinear membrane condensation 的物理意义之一。

---

# 21. exact Schur condensation

完整 Newton 增量：

\[
\begin{bmatrix}
\mathbf G_\xi & \mathbf G_z\\
\mathbf R_\xi & \mathbf R_z
\end{bmatrix}
\begin{bmatrix}
\Delta\boldsymbol\xi\\
\Delta\mathbf z
\end{bmatrix}
=
-
\begin{bmatrix}
\mathbf G\\
\mathbf R
\end{bmatrix}.
\]

第一行：

\[
\Delta\boldsymbol\xi
=
-\mathbf G_\xi^{-1}
\left(
\mathbf G+\mathbf G_z\Delta\mathbf z
\right).
\]

代回：

\[
\boxed{
\mathbf K_{\rm cond}
=
\mathbf R_z
-
\mathbf R_\xi
\mathbf G_\xi^{-1}
\mathbf G_z.
}
\]

若 inner solve 尚未完全满足 \(\mathbf G=0\)，凝聚右端必须是：

\[
\boxed{
\mathbf K_{\rm cond}\Delta\mathbf z
=
-\mathbf R
+
\mathbf R_\xi
\mathbf G_\xi^{-1}\mathbf G.
}
\]

不能只写：

\[
\mathbf K_{\rm cond}\Delta\mathbf z=-\mathbf R
\]

然后在 \(\mathbf G\ne0\) 时仍声称与 full Newton 等价。

当每个 outer iteration 已把 inner equilibrium 收敛到：

\[
\mathbf G=\mathbf0,
\]

才有：

\[
\boxed{
\mathbf K_{\rm cond}\Delta\mathbf z
=
-\mathbf R.
}
\]

数值实现中禁止显式形成：

\[
\mathbf G_\xi^{-1}.
\]

实际使用一次 factorization / linear solve：

\[
\mathbf G_\xi\mathbf X=\mathbf G_z,
\]

\[
\mathbf G_\xi\mathbf y=\mathbf G.
\]

然后：

\[
\mathbf K_{\rm cond}
=
\mathbf R_z-\mathbf R_\xi\mathbf X.
\]

---

# 22. q-continuation 的一致一阶灵敏度

给定 physical connected branch：

\[
\mathbf G(\boldsymbol\xi(q),\mathbf z(q);q)=0,
\]

\[
\mathbf R(\boldsymbol\xi(q),\mathbf z(q);q)=0.
\]

对 q 求导：

\[
\mathbf G_\xi
\frac{d\boldsymbol\xi}{dq}
+
\mathbf G_z
\frac{d\mathbf z}{dq}
+
\mathbf G_q
=
0.
\]

\[
\mathbf R_\xi
\frac{d\boldsymbol\xi}{dq}
+
\mathbf R_z
\frac{d\mathbf z}{dq}
+
\mathbf R_q^{\partial}
=
0.
\]

消去 inner sensitivity：

\[
\boxed{
\overline{\mathbf R}_q
=
\mathbf R_q^{\partial}
-
\mathbf R_\xi
\mathbf G_\xi^{-1}
\mathbf G_q.
}
\]

所以：

\[
\boxed{
\mathbf K_{\rm cond}
\frac{d\mathbf z}{dq}
=
-
\overline{\mathbf R}_q.
}
\]

即：

\[
\boxed{
\frac{d\mathbf z}{dq}
=
-
\mathbf K_{\rm cond}^{-1}
\overline{\mathbf R}_q.
}
\]

第一分量直接给：

\[
\boxed{
\frac{dP}{dq}.
}
\]

因此只要 q 仍是 regular path coordinate，峰值条件：

\[
\boxed{
\frac{dP}{dq}=0
}
\]

可以由一致灵敏度直接获得，而不需要对离散 \(P(q)\) 点做差分寻找峰值。

---

# 23. \(\mathbf G_q\) 与 \(\mathbf R_q^\partial\)

任一 inner equation：

\[
\boxed{
(G_q)_j
=
\int_U
\mathbf B_j^T\mathbf C_t^U\mathbf B_q^U\,dV
+
\int_{s+}
\mathbf B_j^T\mathbf C_t^{s,+}\mathbf B_q^{s,+}\,dV
+
\int_{s-}
\mathbf B_j^T\mathbf C_t^{s,-}\mathbf B_q^{s,-}\,dV.
}
\]

outer partial q derivative的第一行：

\[
\boxed{
\begin{aligned}
\frac{\partial R_q}{\partial q}
={}&
\int_U
(\mathbf B_q^U)^T
\mathbf C_t^U
\mathbf B_q^U\,dV
+
\int_U
(\boldsymbol\sigma^U)^T
\boldsymbol\varepsilon_{,qq}^0\,dV
\\
&+
\int_{s+}
(\mathbf B_q^{s,+})^T
\mathbf C_t^{s,+}
\mathbf B_q^{s,+}\,dV
+
\int_{s+}
(\boldsymbol\sigma^{s,+})^T
\boldsymbol\varepsilon_{,qq}^0\,dV
\\
&+
\int_{s-}
(\mathbf B_q^{s,-})^T
\mathbf C_t^{s,-}
\mathbf B_q^{s,-}\,dV
+
\int_{s-}
(\boldsymbol\sigma^{s,-})^T
\boldsymbol\varepsilon_{,qq}^0\,dV
\\
&-
Pa_hr^2C_q''.
\end{aligned}
}
\]

第二行：

\[
\boxed{
\frac{\partial R_{A^+}}{\partial q}
=
\int_{s+}
(\mathbf B_A^{s,+})^T
\mathbf C_t^{s,+}
\mathbf B_q^{s,+}\,dV
+
\int_{s+}
(\boldsymbol\sigma^{s,+})^T
\Delta\boldsymbol\varepsilon_{,qA}^{\ell,+}
\,dV.
}
\]

第三行：

\[
\boxed{
\frac{\partial R_{A^-}}{\partial q}
=
\int_{s-}
(\mathbf B_A^{s,-})^T
\mathbf C_t^{s,-}
\mathbf B_q^{s,-}\,dV
+
\int_{s-}
(\boldsymbol\sigma^{s,-})^T
\Delta\boldsymbol\varepsilon_{,qA}^{\ell,-}
\,dV.
}
\]

这样 \(dP/dq\)、\(dA^+/dq\)、\(dA^-/dq\) 都来自同一 residual/Jacobian，不需要额外经验演化 law。

---

# 24. 材料积分怎样进入 M6，而不退回 Gauss-point theory

## 24.1 UHPC

M4 已经得到：

\[
\boxed{
\text{analytic }z
+
\text{analytic }Y
+
\text{one deterministic }X\text{ integral}.
}
\]

M6 的：

\[
\mathbf G,\quad
\mathbf R,\quad
\mathbf G_\xi,\quad
\mathbf G_z,\quad
\mathbf R_\xi,\quad
\mathbf R_z
\]

对 UHPC 都调用同一套 active boundary。

对于 Jacobian，只把 stress polynomial：

\[
P(e)
\]

换成相应 branch tangent polynomial：

\[
P'(e)
\]

及 directional coupling，仍可使用 M4 的解析 \(z/Y\) machinery。

## 24.2 Steel

M5 已经得到：

\[
\bar\varepsilon_i^2
=
C_2\zeta^2+C_1\zeta+C_0.
\]

yield roots 全部解析。

finite residual 使用：

\[
E_{sec}.
\]

Jacobian 使用：

\[
\mathbf C_t(E_{sec},E_{tan}).
\]

厚度仍按解析 elastic/plastic intervals 积分。

因此：

\[
\boxed{
\text{M6 组装并没有重新引入 thickness Gauss points}.
}
\]

二维数值积分仍只允许作为独立 benchmark。

---

# 25. PBL/web correction 在 M6 的位置

当前合同把：

\[
\chi_w
=
1+\frac{A_w}{A_c}
\left(
\frac{E_s}{E_c}-1
\right)
\]

定义为 engineering reaction correction，而不是 current homogenized material layer。

因此 M6 不允许让：

\[
\chi_w
\]

进入：

\[
\mathbf G,\quad
R_q,\quad
R_{A^\pm}
\]

去改变 membrane state 或 \(A^\pm\)。

收敛后的原始 UHPC axial contribution：

\[
P_c
=
-\frac1{a_h}\int_\Omega N_y^U\,dA.
\]

报告量：

\[
\boxed{
P_c^*=\chi_wP_c.
}
\]

上下钢壳：

\[
P_s^\pm
=
-\frac1{a_h}\int_\Omega N_y^{s,\pm}\,dA.
\]

最终报告：

\[
\boxed{
P_{\rm report}
=
\chi_wP_c+P_s^++P_s^-.
}
\]

因此需要明确两个量：

\[
\boxed{
P=\text{进入 reduced equilibrium residual 的 generalized axial load}
}
\]

\[
\boxed{
P_{\rm report}=\text{按当前 PBL/web contract 修正后的最终报告反力}.
}
\]

这是符号区分，不增加自由度。

进入 M8 后，如果论文/图中只保留一个 \(P\) 符号，则应明确把最终绘图的 \(P\) 定义成：

\[
P_{\rm report}
\]

而不能在同一张表中混用未修正 generalized \(P\) 与修正 reaction。

---

# 26. C0 在 M6 中的严格位置

C0 不需要重新建立另一套 assembler。

只删除：

\[
H_x,\qquad H_y
\]

以及所有当前没有被激活的 shear-compatible enrichments。

求：

\[
G_{E_x}=G_{E_y}=G_{B_x}=G_{B_y}=0.
\]

同时计算：

\[
\widehat G_{H_x},
\qquad
\widehat G_{H_y}
\]

以及 M3 candidate omitted residual ledger。

C1/M6 则保留 \(H_x,H_y\)。

所以：

\[
\boxed{
\text{C0 与 C1 使用完全相同的 M4/M5 materials 和 outer }R.
}
\]

差异只在 inner compatible space。

---

# 27. dynamic enrichment 不是 branch switching

M3 candidate frequency 在某 state 被激活时，结构 branch identity 仍由：

\[
q,\quad P,\quad A^+,\quad A^-
\]

与连续 current geometry 定义。

新增 inner pair 只是在：

\[
\boldsymbol\xi
\]

中扩充当前 membrane condensation 的可容空间。

正确操作是：

1. 先在当前 active inner space 收敛；
2. 计算全部 exact candidate omitted residual；
3. 若某 omitted residual 大于当前内层数值平衡容限，则加入对应 compatible pair；
4. 从同一 state 重新做 inner Newton；
5. 直到 candidate residual 也满足同一 residual accuracy。

不得因为新增一个 inner pair：

- 重置 \(q\)；
- 重置 \(A^\pm\)；
- 跳到另一条 load branch；
- 重新拟合材料。

---

# 28. M6 Newton 的明确计算顺序

给定：

\[
q_n
\]

以及上一状态 predictor：

\[
P^{(0)},A^{+(0)},A^{-(0)},\boldsymbol\xi^{(0)}.
\]

每次 outer/current iteration：

第一步，按当前：

\[
q,P,A^+,A^-,\boldsymbol\xi
\]

生成：

\[
\boldsymbol\varepsilon^0,
\quad
\boldsymbol\kappa^g,
\quad
\Delta\boldsymbol\varepsilon^{\ell,+},
\quad
\Delta\boldsymbol\varepsilon^{\ell,-},
\quad
\boldsymbol\kappa^{\ell,+},
\quad
\boldsymbol\kappa^{\ell,-}.
\]

第二步，M4 返回 UHPC：

\[
\boldsymbol\sigma^U,
\quad
\mathbf C_t^U,
\]

及 analytic resultants / moments。

第三步，M5 对上下钢壳分别：

\[
\text{analytic yield roots}
\rightarrow
\text{elastic/plastic intervals}
\rightarrow
\boldsymbol\sigma^{s,\pm},
\mathbf C_t^{s,\pm}
\rightarrow
\text{analytic resultants}.
\]

第四步，组装：

\[
\mathbf G,\qquad
\mathbf R.
\]

第五步，组装：

\[
\mathbf G_\xi,\quad
\mathbf G_z,\quad
\mathbf R_\xi,\quad
\mathbf R_z.
\]

第六步，先 factorize：

\[
\mathbf G_\xi.
\]

第七步，exact Schur condensation：

\[
\mathbf K_{\rm cond}
=
\mathbf R_z
-
\mathbf R_\xi
\mathbf G_\xi^{-1}
\mathbf G_z.
\]

第八步，求：

\[
\Delta P,
\qquad
\Delta A^+,
\qquad
\Delta A^-.
\]

第九步，回代：

\[
\Delta\boldsymbol\xi.
\]

第十步，采用 Newton / damping / line-search 更新，但所有更新必须保存：

- iteration；
- residual norm；
- inner residual norm；
- outer residual norm；
- update norm；
- \(q,P,A^+,A^-\)；
- active UHPC regions；
- steel plastic intervals；
- active compatible frequencies；
- \(\kappa(\mathbf G_\xi)\)；
- \(\kappa(\mathbf K_{\rm cond})\)；
- branch identifier。

---

# 29. Schur condensation 的独立数值等价性检查

本轮专门对：

\[
n_\xi=14,
\qquad
n_z=3
\]

的非对称 block system 做确定性 benchmark。

直接解 full Newton：

\[
\begin{bmatrix}
G_\xi&G_z\\
R_\xi&R_z
\end{bmatrix}
\begin{bmatrix}
\Delta\xi\\
\Delta z
\end{bmatrix}
=
-
\begin{bmatrix}
G\\R
\end{bmatrix}
\]

与 exact Schur elimination 比较。

得到：

\[
\boxed{
\max|\Delta z_{\rm Schur}-\Delta z_{\rm full}|
=
1.110e-16
}
\]

\[
\boxed{
\max|\Delta\xi_{\rm Schur}-\Delta\xi_{\rm full}|
=
1.110e-16
}
\]

q-sensitivity：

\[
\boxed{
\max|
(dz/dq)_{\rm Schur}
-
(dz/dq)_{\rm full}
|
=
1.665e-16
}
\]

\[
\boxed{
\max|
(d\xi/dq)_{\rm Schur}
-
(d\xi/dq)_{\rm full}
|
=
4.163e-17
}
\]

全部达到 machine precision。

benchmark 中：

\[
\kappa(G_\xi)=20.082456,
\qquad
\kappa(K_{\rm cond})=1.842897.
\]

这证明 M6 的 Schur 操作只是同一完整方程组的精确代数消元，不改变 residual root。

---

# 30. steel-local 运动学导数独立检查

M6 同时对：

\[
\Delta\boldsymbol\varepsilon^{\ell,\pm}
\]

的：

\[
q,
\quad
A,
\quad
qA,
\quad
AA
\]

解析导数逐项与中心有限差分比较。

包含 TOP/BOTTOM，三分量：

\[
\varepsilon_x,\qquad
\varepsilon_y,\qquad
\gamma_{xy}.
\]

最大相对差：

\[
\boxed{
1.390e-10
}.
\]

因此 M6 outer Jacobian 中最容易漏掉的：

\[
qA
\]

和：

\[
A^2
\]

second-kinematic terms 已独立核验。

---

# 31. M6 consistency verdict

本轮得到：

\[
\boxed{
\mathrm{M6\ residual\ assembly}=PASS
}
\]

\[
\boxed{
\mathrm{M6\ outer\ }R_q,R_{A^+},R_{A^-}=PASS
}
\]

\[
\boxed{
\mathrm{M6\ exact\ Schur\ condensation}=PASS
}
\]

\[
\boxed{
\mathrm{M6\ q\mbox{-}sensitivity\ condensation}=PASS.
}
\]

没有增加 global structural DOF。

没有把：

\[
A^\pm
\]

改成经验 \(A(q)\)。

没有把：

\[
P
\]

改成端缩控制。

没有重新引入：

- 31DOF；
- 41DOF；
- 57DOF；
- large \(u,v\) Ritz；
- 2D/3D material Gauss production definition；
- FEM target fitting。

---

# 32. 本轮发现的问题

M6 没有发现新的路线级矛盾。

只确认两个已经存在、目前不阻塞 M7 的 material-input / notation interface：

第一，UHPC production tensile：

\[
e_{tp},\quad e_{tu},
\quad
P_{t1},\quad P_{t2}
\]

具体数值尚未冻结。

第二，Q355：

\[
P_s(\bar\varepsilon_i)
\]

production polynomial 系数尚未冻结。

这两者都必须在 M8 九试件正式 numerical path 前由真实材料输入冻结；不能按 Pu 误差拟合。

另外，必须在后续输出中把：

\[
P
\]

和：

\[
P_{\rm report}
\]

区分清楚，避免 PBL/web correction 与 equilibrium generalized load 混用。该问题属于符号/接口规范，不改变方程。

---

# 33. 唯一 NEXT_ACTION

严格进入：

\[
\boxed{\mathrm{M7}}
\]

只做理论自检，不使用 FEM 拟合。

检查：

\[
\boxed{
\text{zero-load}
}
\]

\[
\boxed{
\text{linear elastic}
}
\]

\[
\boxed{
q\rightarrow0
}
\]

\[
\boxed{
A^\pm\rightarrow0
}
\]

\[
\boxed{
\text{TOP/BOTTOM symmetry}
}
\]

\[
\boxed{
\text{dimensional consistency}
}
\]

\[
\boxed{
\text{virtual-work / Jacobian consistency}
}
\]

\[
\boxed{
\text{branch continuity}.
}
\]

M7 不跑九试件正式全过程；只有 M7 通过以后才进入 M8。

---

# 34. M7 自检回写：S-family loading-edge work 的 exact basis correction

原始
\[
\mathbf B_{S_y^{kl}}^{raw}
=
[0,\sin kX\sin lY,-k/(lr)\cos kX\cos lY]^T
\]
对应
\[
v_{S_y}^{raw}
=
-\frac{a_h}{l\pi}S_{y,kl}\sin kX\cos lY.
\]
因此 loading-edge 平均轴向位移系数为
\[
\boxed{
c_{kl}
=
\frac{[1-(-1)^k][1-(-1)^l]}{kl\pi^2}.
}
\]
qA 的 S-family 为 odd-odd pair，故
\[
c_{kl}=4/(kl\pi^2)\neq0.
\]
raw residual 必须含
\[
+P_{eq}a_hc_{kl}.
\]

由于 \(E_y\) 已存在，production 采用精确 basis transform
\[
\boxed{
\widetilde{\mathbf B}_{S_y^{kl}}
=
\mathbf B_{S_y^{kl}}^{raw}
-c_{kl}\mathbf B_{E_y}.
}
\]
即
\[
\widetilde{\mathbf B}_{S_y^{kl}}
=
[0,\sin kX\sin lY-c_{kl},-k/(lr)\cos kX\cos lY]^T.
\]
它仍严格 compatible，且平均 loading-edge displacement 为零。对应
\[
G_{\widetilde S_y}
=
G_{S_y}^{raw}-c_{kl}G_{E_y}.
\]
因此 root set、M3 candidate spectrum、single-q 结构与 Schur 方程均不变，只修正 inner basis / external-work bookkeeping。

---

# 35. M7 自检回写：\(P_{eq}\) 与 \(P_{report}\) 分离

M6 outer unknown 统一改记
\[
\boxed{P_{eq}}
\]
表示 reduced equilibrium system 的 generalized axial load。

PBL/web 仍只作 report correction：
\[
P_{report}
=
\chi_wP_c+P_s^++P_s^-.
\]

从 M8 起最终输出记号锁定为
\[
\boxed{P(q)\equiv P_{report}(q)}.
\]
因此 M6 Schur sensitivity 第一分量是
\[
dP_{eq}/dq,
\]
而最终极限必须由
\[
\boxed{
\frac{dP_{report}}{dq}
=
\chi_w\frac{dP_c}{dq}
+\frac{dP_s^+}{dq}
+\frac{dP_s^-}{dq}
}
\]
确定。每个 constituent derivative 由同一
\[
\xi_{,q},\ z_{,q}
\]
链式求导，不增加自由度。

故
\[
\boxed{
P_u=\max_qP_{report}(q)
}
\]
；只有 \(\chi_w=1\) 时，\(dP_{eq}/dq=0\) 才可直接作为最终峰值条件。
