# NZ-SCCM — Airy锁定下耦合 Nx–Mx / Ny–My：原一维终端 T 嵌入与 1D 严格退化门 R01

**Time:** 2026-08-23 17:35 +08:00  
**Status:** `DERIVATION_PASS / 1D_DEGENERATION_PASS / AIRY_LOCKED / NO_SWARTZ_Pu_EXECUTION / NO_CURRENT_STATE_CHANGE`

## 0. 本轮唯一任务

继承 `20260823_1724__NZSCCM__COUPLED_NM_MINIMAL_REDUCTION_AUDIT_R01.md`，本轮不改 Airy 形函数、不改 Airy 显式膜力、不改 Marguerre 后屈曲式，也不引入新的二维终端材料参数。

只做两件事：

1. 从当前正式 V1 的 RC 一维 `Ny-My` 容量中识别其**原样终端条件 T**，嵌入耦合 `(Nx,Mx) <-> (Ny,My)` 架构；
2. 证明取消横向耦合后，新方程组严格退化回 V1 的
   `F_N=0, F_M=0`，并在 interior controller 情况下严格恢复 `F_S=0`。

---

# 1. 当前正式一维 RC N-M 终端 T 到底是什么

V1 并未额外命名一个 `T(c)=0`。终端条件已经编码在其容量参数化本身：

从受压面向内量深度 `y`，

\[
\varepsilon_c(y)=\varepsilon_0\left(1-\frac{y}{c}\right).
\]

因此在受压面 `y=0`：

\[
\boxed{\varepsilon_c(0)=\varepsilon_0}.
\]

这就是当前正式一维 `N-M` 容量的终端约束：**受压面达到压缩上升支峰值应变 `eps0`**。`c` 只是该终端应变场的中性轴参数。

令板中面坐标 `z in [-h,h]`, `h=t/2`，并取 `z=+h` 为当前受压面，则 `y=h-z`，故

\[
\varepsilon_y(z)
=\varepsilon_0\left[1-\frac{h-z}{c}\right]
=\varepsilon_0\left(1-\frac{h}{c}\right)+\frac{\varepsilon_0}{c}z.
\]

若写成 affine 形式

\[
\varepsilon_y(z)=a_y+b_yz,
\]

则

\[
\boxed{a_y=\varepsilon_0\left(1-\frac{h}{c}\right)},
\qquad
\boxed{b_y=\frac{\varepsilon_0}{c}}.
\]

等价地，原一维终端可写为

\[
\boxed{T_y(a_y,b_y)=a_y+h b_y-\varepsilon_0=0.}
\]

本轮把这个 `T_y=0` **原样保留**。不把 first crack、first yield、postpeak residual 或任何新二维强度面替换成 T。

---

# 2. Airy 锁定的二维弯曲方向

取当前 Airy/Navier 实际波形

\[
w=bq\sin(\alpha x)\Phi(y).
\]

在给定控制位置 `xi`，两向曲率方向由实际波形唯一确定：

\[
\widehat\kappa_x=b\alpha^2\sin(\alpha x)\Phi(y),
\]

\[
\widehat\kappa_y=-b\sin(\alpha x)\Phi''(y).
\]

只要 `widehat{kappa}_y != 0`，取方便的未归一化方向

\[
\boxed{\mathbf d=(r,1)^T},
\qquad
\boxed{r=\frac{\widehat\kappa_x}{\widehat\kappa_y}}.
\]

单正弦代表半波中

\[
\boxed{r=\frac{\alpha^2}{\beta^2}}.
\]

因此 terminal-section affine strain 不允许再有独立 `b_x,b_y`，而必须写成

\[
\boxed{\varepsilon_x(z)=a_x+r\lambda z},
\]

\[
\boxed{\varepsilon_y(z)=a_y+\lambda z}.
\]

这只锁定两向斜率的**方向比**；`lambda` 仍是原 N-M 容量参数化中对应中性轴/弯曲强度状态的共同尺度，不把它强制等同于 Airy 当前弹性曲率幅值。

---

# 3. 原样 T 立即消掉 lambda

把 V1 原终端

\[
T_y=a_y+h\lambda-\varepsilon_0=0
\]

直接代入，得到

\[
\boxed{\lambda=\frac{\varepsilon_0-a_y}{h}}.
\]

所以二维 terminal strain field 变成只有两个截面未知量：

\[
\boxed{
\varepsilon_y(z)
=a_y+(\varepsilon_0-a_y)\frac{z}{h}
}
\]

和

\[
\boxed{
\varepsilon_x(z)
=a_x+r(\varepsilon_0-a_y)\frac{z}{h}.
}
\]

纵向中性轴参数仍可显式恢复：

\[
\lambda=\frac{\varepsilon_0}{c}
\]

故

\[
\boxed{c=\frac{h\varepsilon_0}{\varepsilon_0-a_y}},
\qquad
\boxed{a_y=\varepsilon_0\left(1-\frac{h}{c}\right)}.
\]

因此新二维 terminal parameterization 与旧 `c` 参数化之间存在一一对应；没有更改原一维终端定义。

---

# 4. 同一二维材料状态生成四个 capacity resultants

在 terminal layer 中使用同一个冻结二维 plane-stress material operator

\[
(\sigma_x^c,\sigma_y^c)^T
=\mathcal M_{2D}(\varepsilon_x,\varepsilon_y,\gamma_{xy}=0),
\]

以及共享相容应变的两向钢筋。

相体积守恒后定义

\[
N_x^c(a_x,a_y;r),\quad N_y^c(a_x,a_y;r),
\]

\[
M_x^c(a_x,a_y;r),\quad M_y^c(a_x,a_y;r).
\]

这四个量全部来自同一个 `(a_x,a_y)`、同一个 `r`、同一个二维材料映射；不允许分别建立 x/y 两套一维截面。

只要 frozen material branches 仍有有限解析 primitive，本层保持

```text
FORMAL_THICKNESS_QUADRATURE = 0
FORMAL_MATERIAL_POINTS = 0
```

---

# 5. 结构 demand 仍由 Airy + Zhou 给定

Airy 显式解给

\[
N_x^d(q,\xi),\qquad N_y^d(q,\xi).
\]

Zhou 正交刚度作用在同一 Airy 曲率方向上给

\[
M_x^d(q,\xi),\qquad M_y^d(q,\xi).
\]

单正弦时取 `d=(r,1)`，可写

\[
M_x^d=\kappa_0(D_xr+D_\mu),
\]

\[
M_y^d=\kappa_0(D_\mu r+D_y),
\]

其中 `kappa0` 是同一实际变形的公共曲率尺度。

定义可逆弯矩坐标

\[
\boxed{M_\parallel=rM_x+M_y},
\]

\[
\boxed{M_\perp=M_x-rM_y}.
\]

故 demand 显式为

\[
\boxed{
M_\parallel^d
=\kappa_0(D_xr^2+2D_\mu r+D_y)
}
\]

和

\[
\boxed{
M_\perp^d
=\kappa_0[(D_x-D_y)r+D_\mu(1-r^2)].
}
\]

`M_perp` 是 Airy 实际变形经过 Zhou 刚度矩阵以后自然产生的正交耦合需求，不是经验 interaction coefficient。

---

# 6. 固定 (q,xi) 时的内层 2x2 膜力闭合

由于 T 已消去 `lambda`，固定 `(q,xi)` 后只剩 `(a_x,a_y)` 两个截面未知量。

先解

\[
\boxed{R_{Nx}(a_x,a_y;q,\xi)=N_x^c-N_x^d=0},
\]

\[
\boxed{R_{Ny}(a_x,a_y;q,\xi)=N_y^c-N_y^d=0}.
\]

得到

\[
\boxed{(a_x^*,a_y^*)=(a_x^*,a_y^*)(q,\xi)}.
\]

这一步不是把 `Nx` 当终端；它只是利用同一个二维 terminal strain state 使两向膜力与 Airy demand 同时一致。

---

# 7. 完整写出 F_parallel 与 F_perp

在上述内层解上，定义

\[
\boxed{
F_\parallel(q,\xi)
=
[rM_x^c+M_y^c]_{(a_x^*,a_y^*)}
-[rM_x^d+M_y^d]
}
\]

即

\[
\boxed{
F_\parallel(q,\xi)
=M_\parallel^c(q,\xi)-M_\parallel^d(q,\xi)
}.
\]

第二个独立耦合残量为

\[
\boxed{
F_\perp(q,\xi)
=
[M_x^c-rM_y^c]_{(a_x^*,a_y^*)}
-[M_x^d-rM_y^d]
}
\]

即

\[
\boxed{
F_\perp(q,\xi)
=M_\perp^c(q,\xi)-M_\perp^d(q,\xi)
}.
\]

由于 `(Mx,My) -> (M_parallel,M_perp)` 变换行列式为 `-(1+r^2) != 0`，故

\[
\boxed{F_\parallel=0,\ F_\perp=0}
\]

与

\[
\boxed{M_x^c=M_x^d,\ M_y^c=M_y^d}
\]

严格等价。

因此在已有 terminal T 下，generic coupled-NM 外层最小系统为

\[
\boxed{F_\parallel(q,\xi)=0},
\qquad
\boxed{F_\perp(q,\xi)=0}.
\]

对已由结构对称/来源证据压缩为一个控制位置坐标的场景，外层未知量正好是 `(q,xi)`。

- 原单正弦 V1 在纵向半波中心可取 `xi=s=sin(alpha x)`；
- 冻结 source-wave 且 transverse-centre 已由结构审计锁定时可取 `xi=u=y/a`。

不允许因为方便而把一个本来独立的空间位置自由度静默删掉。

---

# 8. 1D 严格退化门：定义取消横向耦合的数学退化

这里的“取消横向耦合”是一个**退化检查**，不是声称真实有限板有 `r=0`。

定义 1D degeneration operator `D_1D`：

1. x 方向不参与 terminal capacity：`N_x^d=M_x^d=0`；
2. terminal curvature direction 退化为 `d=(0,1)`，即 `r=0`；
3. y 向混凝土应力退化为当前 V1 一维压缩上升支，拉区为零；
4. x 向钢筋仍按 V1 只作为被其占据混凝土体积的 phase-volume subtraction，不直接承担 `Ny,My`；
5. y 向钢筋保持当前 V1 `clip(Es*eps, -fy, +fy)`。

于是 terminal strain field 变成

\[
\varepsilon_y(z)=a_y+(\varepsilon_0-a_y)\frac{z}{h},
\]

而 `epsilon_x` 从 y 向容量中完全退出。

利用

\[
c=\frac{h\varepsilon_0}{\varepsilon_0-a_y}
\]

立即得到

\[
\boxed{N_y^c=n_u(c)},
\qquad
\boxed{M_y^c=m_u(c)},
\]

其中 `n_u(c),m_u(c)` 与 V1 第18节完全同式。

---

# 9. F_N 与 F_M 被逐项恢复

在 `D_1D` 下，x 向内层方程成为非活动/恒等分支；真正的膜力闭合只剩

\[
N_y^c=N_y^d.
\]

在原单正弦 V1 纵向半波中心，采用压缩为正的旧记号

\[
n_d(s,q)=n(s;q),
\]

故

\[
N_y^c=N_y^d
\]

逐项就是

\[
\boxed{F_N(q,s,c)=n_d(s,q)-n_u(c)=0}.
\]

另一方面 `r=0` 时

\[
M_\parallel=M_y,
\]

故

\[
F_\parallel=0
\]

逐项成为

\[
\boxed{F_M(q,s,c)=Jqs-m_u(c)=0}.
\]

同时

\[
M_\perp=M_x,
\]

而在 `D_1D` 定义下 x 方向 demand/capacity 均非活动，所以

\[
\boxed{F_\perp\equiv0}.
\]

因此 coupled-NM 系统严格因子化为

\[
\boxed{F_N=0,\qquad F_M=0},
\]

没有留下任何额外二维经验项。

---

# 10. interior controller 时 F_S 也被严格恢复

若控制位置 `s` 不是端点而在 `0<s<1`，旧 V1 还要求沿截面接触位置驻值。

从

\[
F_N=n_d(s,q)-n_u(c)=0
\]

有

\[
\frac{dc}{ds}=\frac{n_{d,s}}{n_u'(c)}.
\]

沿该隐式膜力平衡支，令

\[
m_u(c(s))-Jqs
\]

对 `s` 驻值：

\[
0=m_u'(c)\frac{dc}{ds}-Jq.
\]

乘 `n_u'(c)` 得

\[
0=n_{d,s}m_u'(c)-Jq n_u'(c).
\]

而

\[
n_{d,s}=-4Gq(q+2q_0)s,
\]

所以

\[
\boxed{
F_S(q,s,c)
=-4Gq(q+2q_0)s\,m_u'(c)-Jq\,n_u'(c)=0
}
\]

与 V1 第21节完全一致。

因此不仅 `F_N,F_M`，连 interior-controller 的第三个旧方程 `F_S` 也逐项恢复。

---

# 11. 退化门结论

```text
FROZEN_1D_TERMINAL_T_IDENTIFIED
    = compression-face eps_y = eps0

T_REEXPRESSED_AFFINE
    = a_y + h*b_y - eps0 = 0

AIRY_LOCKED_SLOPE_RATIO
    = b_x:b_y = kappa_x:kappa_y

T_ELIMINATES_COMMON_SLOPE_SCALE
    = PASS

INNER_TERMINAL_MEMBRANE_SYSTEM
    = 2x2 in (a_x,a_y)

OUTER_COUPLED_MOMENT_SYSTEM
    = F_parallel(q,xi)=0 + F_perp(q,xi)=0

ARBITRARY_4D_CAPACITY_SURFACE
    = NOT_USED

INDEPENDENT_X_Y_NM_CURVES
    = NOT_USED

ONE_DIMENSIONAL_DEGENERATION
    = EXACT_PASS

RECOVER_F_N
    = EXACT
RECOVER_F_M
    = EXACT
RECOVER_F_S_FOR_INTERIOR_CONTROL
    = EXACT

AIRY_GLOBAL_FORM
    = UNCHANGED
P_pb(q)
    = UNCHANGED
CURRENT_STATE_FILE
    = NOT_CHANGED
```

---

# 12. Remaining gate before Swartz8 calculation

The algebraic architecture is now closed at the level requested here. Before calculating the eight accepted Swartz panels, one implementation gate remains:

1. instantiate the **currently frozen 2D material operator** inside `Nx^c,Ny^c,Mx^c,My^c` without changing its material functions;
2. use the same exact affine-through-thickness primitives / finite branch-front localization already demonstrated by the historical two-slope full-2D section audit;
3. verify the inner `2x2` membrane solve has an origin-connected admissible terminal solution and that no hidden x/y-independent slope DOF is reintroduced;
4. only then solve the same outer `F_parallel=F_perp=0` rule for the full accepted Swartz set, with no experimental `Pf` in root selection.

This remaining step is implementation/branch-admissibility closure, not another theoretical change of Airy or of the one-dimensional terminal T.