# NZ-SCCM — 膜应力显式恢复与 TC/CT 用 θ 处理的修正

时间：2026-08-20 16:22 +08:00

## 1. 修正点

上一轮直接把 NC-M4 代入 Nguyen 二阶运动学时，虽然体积分 `sigma:epsilon_,p` 在数学上隐含包含膜应力贡献，但没有显式恢复 Nguyen 薄板虚功中的膜力合力 `N` 与弯矩合力 `M` 分解，导致“膜应力部分”在表达上被遗漏。正式表达应恢复为中面膜应变 + 曲率 + 厚度积分后的 `N/M`。

同时，上一轮把 TC/CT 的主方向识别问题误判成必须重构 TC/CT 材料函数。对当前 NC-M4 这种以当前主应变为输入的同轴 total-strain 候选，完全可以保留派生的主方向角 `theta(x,y,z)`，在主坐标中调用唯一 TC/CT 关系，再旋回板坐标。`theta` 不是新的结构未知量。

## 2. Nguyen 二阶中面膜应变与曲率

设

\[
w_0=A_0\phi,\qquad w=A\phi,\qquad S=A_0A+\frac12A^2.
\]

当前三变量约化下，面内线性膜应变取

\[
u_{,x}=\varepsilon_m,\qquad v_{,y}=-\frac{\Delta}{\ell},\qquad u_{,y}+v_{,x}=0.
\]

于是中面膜应变为

\[
\varepsilon_x^0=\varepsilon_m+S\phi_{,x}^2,
\]

\[
\varepsilon_y^0=-\frac{\Delta}{\ell}+S\phi_{,y}^2,
\]

\[
\gamma_{xy}^0=2S\phi_{,x}\phi_{,y}.
\]

新增曲率向量采用工程剪应变约定：

\[
\boldsymbol\kappa=
-\begin{bmatrix}
A\phi_{,xx}\\
A\phi_{,yy}\\
2A\phi_{,xy}
\end{bmatrix}.
\]

厚度任意点：

\[
\boldsymbol\varepsilon(z)=\boldsymbol\varepsilon^0+z\boldsymbol\kappa.
\]

## 3. 膜力与弯矩合力必须显式保留

材料 current operator 返回

\[
\boldsymbol\sigma=(\sigma_x,\sigma_y,\tau_{xy})^T.
\]

定义

\[
\mathbf N=\int_{-h/2}^{h/2}\boldsymbol\sigma\,dz,
\qquad
\mathbf M=\int_{-h/2}^{h/2}z\boldsymbol\sigma\,dz.
\]

即

\[
\mathbf N=(N_x,N_y,N_{xy})^T,
\qquad
\mathbf M=(M_x,M_y,M_{xy})^T.
\]

对幅值 `A`：

\[
\frac{\partial\boldsymbol\varepsilon^0}{\partial A}
=(A_0+A)
\begin{bmatrix}
\phi_{,x}^2\\
\phi_{,y}^2\\
2\phi_{,x}\phi_{,y}
\end{bmatrix},
\]

\[
\frac{\partial\boldsymbol\kappa}{\partial A}
=-
\begin{bmatrix}
\phi_{,xx}\\
\phi_{,yy}\\
2\phi_{,xy}
\end{bmatrix}.
\]

因此正式面外平衡残量应写为

\[
\boxed{
R_A=\int_A\left[
\left(\frac{\partial\boldsymbol\varepsilon^0}{\partial A}\right)^T\mathbf N
+
\left(\frac{\partial\boldsymbol\kappa}{\partial A}\right)^T\mathbf M
\right]dA=0
}
\]

即

\[
\begin{aligned}
R_A=\int_A\{&(A_0+A)[N_x\phi_{,x}^2+N_y\phi_{,y}^2+2N_{xy}\phi_{,x}\phi_{,y}]\\
&-M_x\phi_{,xx}-M_y\phi_{,yy}-2M_{xy}\phi_{,xy}\}\,dA.
\end{aligned}
\]

横向膜平衡：

\[
\boxed{R_m=\int_A N_x\,dA=0}
\]

轴向荷载：

\[
\boxed{P=-\frac1\ell\int_A N_y\,dA}
\]

所以膜应力并未应被删去；它通过 `N_x,N_y,N_xy` 显式进入 `R_m,P,R_A`，并在切线中形成当前膜力几何刚度。

## 4. TC/CT 可直接用 θ 处理

对当前厚度点的工程应变

\[
(\varepsilon_x,\varepsilon_y,\gamma_{xy}),
\]

定义派生主方向角

\[
\boxed{
\theta=\frac12\operatorname{atan2}(\gamma_{xy},\varepsilon_x-\varepsilon_y)
}
\]

则主应变无需先写成平方根形式，可直接旋转得到

\[
\varepsilon_1=\varepsilon_x\cos^2\theta+\varepsilon_y\sin^2\theta+\gamma_{xy}\sin\theta\cos\theta,
\]

\[
\varepsilon_2=\varepsilon_x\sin^2\theta+\varepsilon_y\cos^2\theta-\gamma_{xy}\sin\theta\cos\theta.
\]

在 TC 区若 `epsilon_1>0, epsilon_2<0`：

\[
\sigma_1=f_tT_4(\varepsilon_1/\varepsilon_{t0}),
\]

\[
\sigma_2=-f_c\beta(\varepsilon_1/\varepsilon_{t0})C(-\varepsilon_2/\varepsilon_{c0}).
\]

CT 区交换 1、2 方向。

旋回板坐标：

\[
\sigma_x=\sigma_1\cos^2\theta+\sigma_2\sin^2\theta,
\]

\[
\sigma_y=\sigma_1\sin^2\theta+\sigma_2\cos^2\theta,
\]

\[
\tau_{xy}=(\sigma_1-\sigma_2)\sin\theta\cos\theta.
\]

因此 TC/CT 不需要为了避免显式根号而重构材料函数。`theta` 只是由当前应变场派生的局部方向变量，不增加结构自由度。

## 5. 来源边界

Nguyen 第6章 Eq.6.3 明确保留中面面内位移 `u,v`、膜应变与穿厚曲率；项目 Branch-C 审计也以 `N/M` 合力形式写成 `R_m = integral(B_m^T N)`、`R_w = integral(B_g^T N + B_kappa^T M)`，并单独包含当前膜力几何刚度。

需要区分：Nguyen 源模型在开裂后程序中保存的是 principal stress angle；当前 NC-M4 若按 total-strain、同轴的极简候选执行，则上述 `theta` 取当前主应变方向。这是 NC-M4 的简化假设，不应冒充 Nguyen 完整历史开裂方向模型。

## 6. 当前主线

正式链条修正为：

`(Delta,A,epsilon_m)`
→ `Nguyen second-order membrane strain + curvature`
→ `epsilon(x,y,z)`
→ `theta + principal strains`
→ `single local CC/TC/CT/TT law`
→ `rotate back to sigma_x,sigma_y,tau_xy`
→ `thickness integrate to N,M`
→ `R_m, P, R_A`
→ `L=0`.

不再因 TC/CT 的方向识别问题单独重构材料函数；下一步应在这个完整 `N/M + theta` 链条上直接检查 NC-M4 的连续积分。