# NZ-SCCM — Airy 锁定下耦合 Nx–Mx / Ny–My 最小方程组审计 R01

**Time:** 2026-08-23 17:24 +08:00  
**Status:** `DERIVATION_PASS / DIAGNOSTIC_ONLY / AIRY_LOCKED / NO_SWARTZ_Pu_EXECUTION / NO_CURRENT_STATE_CHANGE`

## 0. 本轮边界

本轮只解决一个问题：在**不改变 Airy 形函数、不改变 Airy 显式膜应力解、不重新建立全局路径求解器**的前提下，把原先单向 `Ny-My` 截面极限层升级为

\[
(N_x,M_x)\quad\text{与}\quad(N_y,M_y)
\]

两个相互耦合的方向容量，并证明表面上的四个分量条件能否降成低维问题。

本轮明确撤回“修改 Airy 全局残量/形函数”的路线。二维耦合只允许发生在原 `N-M` 终端/截面层。

---

# 1. 结构需求端：Airy 与 Zhou 完全锁定

取当前代表波形

\[
w=bq\sin(\alpha x)\Phi(y),
\qquad \alpha=\pi/b.
\]

初始缺陷与 Airy 兼容关系仍按现有 V1，不在本轮改动。对单正弦代表半波，

\[
\Phi(y)=\sin(\beta y),\qquad \beta=\pi/\ell.
\]

## 1.1 Airy 膜力

单正弦 V1 的显式膜力仍为

\[
N_x^d=-K_xQ\cos(2\beta y),
\]

\[
N_y^d=-\frac{P_{pb}(q)}{b}-K_yQ\cos(2\alpha x),
\]

\[
N_{xy}^d=0,
\]

其中

\[
Q=q(q+2q_0),
\]

\[
K_x=\frac{\alpha^2b^2\Delta_A}{8A_{22}},
\qquad
K_y=\frac{\beta^2b^2\Delta_A}{8A_{11}},
\]

\[
\Delta_A=A_{11}A_{22}-A_{12}^2.
\]

`P_pb(q)` 仍为现有 Marguerre–Airy 显式后屈曲式，不在本轮改写。

## 1.2 Airy 实际变形给出两向曲率方向

定义单位 `q` 的几何曲率向量

\[
\widehat{\boldsymbol\kappa}(x,y)=
\begin{bmatrix}
\widehat\kappa_x\\
\widehat\kappa_y
\end{bmatrix}
=
\begin{bmatrix}
b\alpha^2\sin(\alpha x)\Phi(y)\\
-b\sin(\alpha x)\Phi''(y)
\end{bmatrix}.
\]

于是实际曲率为

\[
\boxed{\boldsymbol\kappa^d=q\widehat{\boldsymbol\kappa}}.
\]

在单正弦半波中

\[
\widehat\kappa_x=b\alpha^2\sin\alpha x\sin\beta y,
\]

\[
\widehat\kappa_y=b\beta^2\sin\alpha x\sin\beta y,
\]

因此

\[
\boxed{\rho_\kappa=\frac{\widehat\kappa_x}{\widehat\kappa_y}=\frac{\alpha^2}{\beta^2}}.
\]

这个曲率比由 Airy/Navier 实际波形唯一给定，不是新增自由参数。

## 1.3 Zhou 正交刚度给出两向弯矩耦合

在当前正交轴、`D16=D26=0` 的结构骨架中

\[
\begin{bmatrix}M_x^d\\M_y^d\end{bmatrix}
=
\begin{bmatrix}D_x&D_\mu\\D_\mu&D_y\end{bmatrix}
\begin{bmatrix}\kappa_x^d\\\kappa_y^d\end{bmatrix}.
\]

因此

\[
\boxed{M_x^d=q(D_x\widehat\kappa_x+D_\mu\widehat\kappa_y)},
\]

\[
\boxed{M_y^d=q(D_\mu\widehat\kappa_x+D_y\widehat\kappa_y)}.
\]

单正弦下令

\[
r=\rho_\kappa=\alpha^2/\beta^2,
\qquad
\kappa_0=q\widehat\kappa_y,
\]

则

\[
\boxed{M_x^d=\kappa_0(D_xr+D_\mu)},
\]

\[
\boxed{M_y^d=\kappa_0(D_\mu r+D_y)}.
\]

故 `(Mx,My)` 同样不是两个独立 demand。

---

# 2. 截面端：把旧 two-slope 四变量改成 Airy 锁定三变量

历史 two-slope full-2D 接口使用

\[
\varepsilon_x(z)=a_x+b_xz,
\qquad
\varepsilon_y(z)=a_y+b_yz,
\]

即四个独立截面变量 `(a_x,a_y,b_x,b_y)`。本轮只修改这里的自由度：**两向斜率方向必须服从 Airy 实际曲率方向**。

定义归一化或任意固定尺度的曲率方向

\[
\mathbf d=
\begin{bmatrix}d_x\\d_y\end{bmatrix}
\parallel
\widehat{\boldsymbol\kappa},
\qquad \mathbf d\neq0.
\]

截面 affine 状态改写为

\[
\boxed{
\boldsymbol\varepsilon(z)
=
\begin{bmatrix}a_x\\a_y\end{bmatrix}
+\lambda z\mathbf d
}
\]

即

\[
\varepsilon_x(z)=a_x+\lambda d_xz,
\qquad
\varepsilon_y(z)=a_y+\lambda d_yz.
\]

因此

\[
\boxed{b_x:b_y=d_x:d_y=\widehat\kappa_x:\widehat\kappa_y}.
\]

截面变量从 4 个严格降为

\[
\boxed{\boldsymbol\eta=(a_x,a_y,\lambda)}.
\]

这里 `lambda` 是截面 N-M 容量参数化所需的共同弯曲斜率尺度；它不改变 Airy 的实际波形方向。

---

# 3. 同一个二维材料状态同时生成四个 capacity resultants

在 transverse-centre 控制线 `x=b/2` 上，现有单模态/source-wave 结构均有 `Nxy=Mxy=0`，故本轮先处理 normal-bending 四分量。

混凝土使用同一个 frozen 2D plane-stress operator

\[
\begin{bmatrix}\sigma_x^c(z)\\\sigma_y^c(z)\end{bmatrix}
=
\mathcal M_{2D}
\left[
\varepsilon_x(z),\varepsilon_y(z),\gamma_{xy}=0
\right].
\]

第 `l` 层钢筋共享相同物理应变

\[
\varepsilon_{sx,l}=a_x+\lambda d_xz_l,
\qquad
\varepsilon_{sy,l}=a_y+\lambda d_yz_l.
\]

令 `a_l=a_xl+a_yl` 为该层两方向钢筋占据的混凝土厚度面积，则相体积守恒的四个截面合力为

\[
\boxed{
N_x^c
=\int_{-h}^{h}\sigma_x^c(z)\,dz
-\sum_l a_l\sigma_x^c(z_l)
+\sum_l a_{xl}\sigma_{sx,l}
}
\]

\[
\boxed{
N_y^c
=\int_{-h}^{h}\sigma_y^c(z)\,dz
-\sum_l a_l\sigma_y^c(z_l)
+\sum_l a_{yl}\sigma_{sy,l}
}
\]

\[
\boxed{
M_x^c
=\int_{-h}^{h}z\sigma_x^c(z)\,dz
-\sum_l a_lz_l\sigma_x^c(z_l)
+\sum_l a_{xl}z_l\sigma_{sx,l}
}
\]

\[
\boxed{
M_y^c
=\int_{-h}^{h}z\sigma_y^c(z)\,dz
-\sum_l a_lz_l\sigma_y^c(z_l)
+\sum_l a_{yl}z_l\sigma_{sy,l}
}
\]

四个合力来自**同一个** `(a_x,a_y,lambda)` 和同一个二维材料映射，因此 `Nx-Mx` 与 `Ny-My` 不再是两个独立的一维截面。

只要 frozen material law 的 branch fronts 可有限定位，上述厚度积分仍可按历史 exact-section primitive 路线做零 formal quadrature。

---

# 4. 关键降阶：四个分量条件可转成“3 个内层方程 + 1 个标量二维耦合残量”

表面上需要

\[
N_x^c=N_x^d,
\quad
N_y^c=N_y^d,
\quad
M_x^c=M_x^d,
\quad
M_y^c=M_y^d.
\]

固定 `(q,u)` 后，截面只有三个未知量 `(a_x,a_y,lambda)`，所以直接把四个方程都当独立条件会显得过定。

Airy 曲率方向允许对此作精确坐标变换。

定义与曲率方向平行和正交的弯矩组合。可取未归一化

\[
\boxed{M_{\parallel}=d_xM_x+d_yM_y},
\]

\[
\boxed{M_{\perp}=d_yM_x-d_xM_y}.
\]

只要 `d_x^2+d_y^2>0`，从 `(Mx,My)` 到 `(M_parallel,M_perp)` 的变换可逆，因此

\[
(M_x^c,M_y^c)=(M_x^d,M_y^d)
\]

严格等价于

\[
M_\parallel^c=M_\parallel^d,
\qquad
M_\perp^c=M_\perp^d.
\]

## 4.1 内层 3×3 截面闭合

对固定 `(q,u)`，先解

\[
\boxed{
R_{Nx}=N_x^c-N_x^d=0,
}
\]

\[
\boxed{
R_{Ny}=N_y^c-N_y^d=0,
}
\]

\[
\boxed{
R_{M\parallel}=M_\parallel^c-M_\parallel^d=0
}
\]

得到

\[
\boxed{\boldsymbol\eta^*(q,u)=(a_x^*,a_y^*,\lambda^*)}.
\]

随后只剩一个真正的二维方向一致性残量

\[
\boxed{
F_{2D}(q,u)
=M_\perp^c[\boldsymbol\eta^*(q,u),u]
-M_\perp^d(q,u).
}
\]

于是四个 resultant 条件已经严格降成：

- 一个 3×3 局部截面求解；
- 一个外层标量 `F_2D=0`。

这不是近似删方程，而是可逆坐标变换加隐函数消元。

---

# 5. Zhou 耦合在平行/正交坐标中的显式形式

对单正弦，取

\[
\mathbf d=(r,1)^T,
\qquad r=\alpha^2/\beta^2.
\]

采用

\[
M_\parallel=rM_x+M_y,
\qquad
M_\perp=M_x-rM_y.
\]

由 Zhou 刚度关系直接得

\[
\boxed{
M_\parallel^d
=\kappa_0
\left(D_xr^2+2D_\mu r+D_y\right)
}
\]

以及

\[
\boxed{
M_\perp^d
=\kappa_0
\left[(D_x-D_y)r+D_\mu(1-r^2)\right].
}
\]

第一式是沿 Airy 实际曲率方向的广义弯曲需求；第二式正是由于正交各向刚度和 Poisson/cross-bending 产生的**两方向耦合需求**。

因此 `M_perp` 不是新增经验相互作用项，而是 Zhou 刚度矩阵作用在 Airy 曲率方向后自然出现的结果。

---

# 6. 内层 Jacobian 与“塑性刚度”位置

令当前二维材料一致切线为

\[
\mathbf C_t(z)=\frac{\partial(\sigma_x,\sigma_y)}{\partial(\varepsilon_x,\varepsilon_y)}.
\]

定义截面切线矩

\[
\mathbf A_t=\int\mathbf C_t\,dz+\text{steel/phase corrections},
\]

\[
\mathbf B_t=\int z\mathbf C_t\,dz+\text{steel/phase corrections},
\]

\[
\mathbf D_t=\int z^2\mathbf C_t\,dz+\text{steel/phase corrections}.
\]

则内层三方程对 `(a_x,a_y,lambda)` 的一致 Jacobian 为

\[
\boxed{
\mathbf J_{\parallel}
=
\begin{bmatrix}
\mathbf A_t & \mathbf B_t\mathbf d\\
\mathbf d^T\mathbf B_t & \mathbf d^T\mathbf D_t\mathbf d
\end{bmatrix}
}
\]

这里上左块为 `2×2`，右列/下行为 `2×1/1×2`，整体为 `3×3`。

这就是本轮允许出现的“材料非线性/塑性刚度”：它只用于原 `N-M` 截面层的二维耦合求解，不反馈修改 Airy 形函数或其显式膜应力公式。

当材料为线弹性、截面对称时

\[
\mathbf B_t=0,
\]

且 `A_t,D_t` 退化为现有初始刚度，严格回到 Zhou/RC elastic stiffness degeneration。

---

# 7. 是否已经得到唯一 Pu？需要区分“二维耦合闭合”和“终端容量定义”

上述 `F_2D=0` 证明的是：**两个方向的 N-M 可以在 Airy 锁定形变下用低维方式精确耦合**。

但若 `M_2D` 使用的是完整 current constitutive response，线弹性阶段 `F_2D` 会因同源刚度而恒等或近似恒等，不能单独定义 ultimate load。这与历史 four-variable current-map branch 的问题相同。

如果要严格保留旧 `N-M capacity` 的“终端截面”身份，需要把旧一维容量中已经存在的终端材料条件抽象为

\[
\boxed{T(a_x,a_y,\lambda;u)=0}.
\]

本轮不修改 `T` 的物理定义，也不新增经验终端。

若 `T_{,\lambda}\neq0`，可先由

\[
T=0
\]

消去

\[
\lambda=\Lambda(a_x,a_y;u).
\]

此时终端截面只剩两个自由参数 `(a_x,a_y)`。

对给定 `(q,u)`，先由

\[
N_x^c=N_x^d,
\qquad
N_y^c=N_y^d
\]

解出

\[
(a_x^*,a_y^*).
\]

再定义两个外层弯矩残量

\[
\boxed{
F_\parallel(q,u)=M_\parallel^c-M_\parallel^d,
}
\]

\[
\boxed{
F_\perp(q,u)=M_\perp^c-M_\perp^d.
}
\]

最终 generic coupled-terminal 闭合成为

\[
\boxed{
F_\parallel(q,u)=0,
\qquad
F_\perp(q,u)=0.
}
\]

即外层仅有两个未知量

\[
\boxed{(q,u)}
\]

和两个方程。

因此，**保留旧 N-M 终端语义时，最小一般形式是一个 2×2 外层系统，而不是 4D 容量面。**

---

# 8. 什么时候还能进一步降成单标量？

只有在下列特殊情形之一被证明时，`F_parallel` 与 `F_perp` 才能依赖/合并：

1. 控制位置 `u` 由严格对称性/source geometry 预先固定；且
2. terminal section 的二维材料响应使 `M_perp` 关系自动与 Zhou demand 同源；或
3. `F_perp` 在该材料/几何退化下恒等为零。

线弹性同源刚度是这种退化的典型例子，但一般 cracked/TC/CC 非线性状态下不能预先假设成立。

因此当前不能宣称 generic theory 已经降到单一 `q` 方程。

最小诚实结论是

\[
\boxed{\text{generic: }(q,u)\text{ two unknowns, two outer equations}.}
\]

对于有限已知控制位置候选，可逐个固定 `u` 检查是否存在一维退化；不得人为删除 `F_perp`。

---

# 9. 与历史 two-slope full-2D 失败路线的区别

历史 20260822_1927 two-slope 接口使用

\[
(a_x,a_y,b_x,b_y)
\]

四个完全独立的 section variables，并直接让四个 resultants 平衡。它能够表达任意二维截面弯曲方向，但没有把该方向锁定到 Airy 实际变形，因此 section freedom 大于当前显式结构运动学自由度。

本轮修正为

\[
\boxed{(a_x,a_y,\lambda),\quad (b_x,b_y)=\lambda(d_x,d_y)}.
\]

这一步正是用户要求的：

\[
\boxed{\text{Nx-Mx 与 Ny-My 的二维关系由 Airy 变形方向 + Zhou 刚度建立。}}
\]

而不是通过两个独立 N-M、经验 4D surface 或新形函数建立。

---

# 10. 本轮 gate

```text
AIRY_SHAPE_FUNCTION = LOCKED
AIRY_MEMBRANE_EXPLICIT_SOLUTION = LOCKED
MARGUERRE_Ppb = LOCKED

OLD_TWO_INDEPENDENT_SLOPES_bx_by = REDUCED
SECTION_SLOPE_DIRECTION = AIRY_CURVATURE_DIRECTION
SECTION_UNKNOWN_COUNT = 3  # ax, ay, lambda

DIRECTIONAL_RESULTANTS = Nx, Ny, Mx, My
DIRECTIONAL_NM_PAIRS = (Nx,Mx) + (Ny,My)
X_Y_INDEPENDENT_CAPACITY = PROHIBITED

INNER_SECTION_SYSTEM = Nx + Ny + M_parallel  # 3x3
OUTER_2D_COUPLING_RESIDUAL = M_perp

IF_CURRENT_CONSTITUTIVE_ONLY:
    F2D = COUPLING_CLOSURE_NOT_ULTIMATE_TERMINAL

IF_OLD_NM_TERMINAL_T_IS_RETAINED:
    TERMINAL_SECTION_DOF_AFTER_T = 2
    OUTER_UNKNOWN = (q,u)
    OUTER_SYSTEM = F_parallel = 0 + F_perp = 0

GENERIC_ONE_SCALAR_q_REDUCTION = NOT_PROVEN
GENERIC_MINIMAL_TERMINAL_SYSTEM = 2x2_IN_(q,u)

ARBITRARY_4D_CAPACITY_SURFACE = NOT_REQUIRED
GLOBAL_AIRY_REDERIVATION = PROHIBITED
SWARTZ_Pu_EXECUTION = NOT_STARTED
```

## 11. 下一步

本轮已经完成“能否降阶”的结构证明。下一步若继续，应只做两件事：

1. 把当前正式一维 `N-M` 的终端条件 `T` 原样嵌入上述二维参数化，不能重新发明 terminal；
2. 选 accepted Swartz analysis set 的共同波形/位置规则，先检查 `F_parallel,F_perp` 的根结构与退化性质，再决定是否已经有资格计算 8 板 `Pu`。
