# NZ-SCCM — NC-M6 半角有理化与厚度精确积分 V0

时间：2026-08-20 23:01 +08:00

状态：`NC_M6_MATERIAL_FROZEN / NO_CASE21 / NO_T5_REFIT / NO_ROOT_CANCELLATION_PROJECT / HALF_ANGLE_LIFT_PASS / EXACT_THICKNESS_INTEGRATION_PASS / IN_PLANE_CONTINUOUS_FIELD_UNRESOLVED`

## 0. 治理边界

本节点严格复制旧 NC-M4 已验证的解析积分路线，不另开 CC/TT “消根工程”。

固定：
- NC-M6 current material operator 不改；
- 不做 Case21；
- 不重新拟合 T5；
- 不引入 alpha、epsilon_m、Ritz 系数或其他新的结构未知量；
- 连续面内位移仍为 `u(x,y), v(x,y)`；
- 正式空间数值积分、材料点网格继续为 0。

目标：从已展开的 `P, R_A, R_u, R_v` 实际积分出发，执行

`theta 恒等消元 -> X/Y 半角有理化 -> 唯一二次根式 Q -> z 向 Euler 精确积分`。

---

## 1. 连续结构运动学

令

\[
X=\pi x/b,\qquad Y=\pi y/\ell,
\]

\[
S=A_0A+A^2/2.
\]

保持连续面内场：

\[
\varepsilon_x=u_{,x}+S\frac{\pi^2}{b^2}\cos^2X\sin^2Y
+zA\frac{\pi^2}{b^2}\sin X\sin Y,
\]

\[
\varepsilon_y=-\frac{\Delta}{\ell}+v_{,y}
+S\frac{\pi^2}{\ell^2}\sin^2X\cos^2Y
+zA\frac{\pi^2}{\ell^2}\sin X\sin Y,
\]

\[
\gamma_{xy}=u_{,y}+v_{,x}
+2S\frac{\pi^2}{b\ell}\cos X\sin X\sin Y\cos Y
-2zA\frac{\pi^2}{b\ell}\cos X\cos Y.
\]

---

## 2. 半角变量：避免与位移 u,v 混淆

取积分变量

\[
\xi=\tan(X/2),\qquad \eta=\tan(Y/2),
\]

\[
U=1+\xi^2,\qquad V=1+\eta^2,
\qquad D_0=U^2V^2.
\]

则

\[
\sin X=\frac{2\xi}{U},\quad \cos X=\frac{1-\xi^2}{U},
\]

\[
\sin Y=\frac{2\eta}{V},\quad \cos Y=\frac{1-\eta^2}{V},
\]

并且

\[
\partial_x=\frac{\pi U}{2b}\partial_\xi,
\qquad
\partial_y=\frac{\pi V}{2\ell}\partial_\eta,
\]

\[
dx\,dy=\frac{4b\ell}{\pi^2UV}\,d\xi\,d\eta.
\]

注意：`u(\xi,\eta),v(\xi,\eta)` 仍为未知连续函数；半角变换只把几何三角项有理化，并不把面内连续场提前降阶。

---

## 3. 三个应变分量统一为共同分母 D0

写成

\[
\varepsilon_x=E_x/D_0,\qquad
\varepsilon_y=E_y/D_0,\qquad
\gamma_{xy}=G/D_0.
\]

其中

\[
\begin{aligned}
E_x={}&D_0\frac{\pi U}{2b}u_{,\xi}
+4S\frac{\pi^2}{b^2}\eta^2(1-\xi^2)^2
+4zA\frac{\pi^2}{b^2}\xi\eta UV,
\end{aligned}
\]

\[
\begin{aligned}
E_y={}&D_0\left(-\frac{\Delta}{\ell}+\frac{\pi V}{2\ell}v_{,\eta}\right)
+4S\frac{\pi^2}{\ell^2}\xi^2(1-\eta^2)^2
+4zA\frac{\pi^2}{\ell^2}\xi\eta UV,
\end{aligned}
\]

\[
\begin{aligned}
G={}&D_0\left(\frac{\pi V}{2\ell}u_{,\eta}+\frac{\pi U}{2b}v_{,\xi}\right)
+8S\frac{\pi^2}{b\ell}\xi\eta(1-\xi^2)(1-\eta^2)
\\
&-2zA\frac{\pi^2}{b\ell}(1-\xi^2)(1-\eta^2)UV.
\end{aligned}
\]

因此 `E_x,E_y,G` 对厚度坐标 z 严格为一次式。

可仅为代数整理写

\[
E_x=E_{x0}+zE_{x1},\quad
E_y=E_{y0}+zE_{y1},\quad
G=G_0+zG_1,
\]

其中这些只是由上式读出的系数，不是新的结构未知量。

---

## 4. theta 恒等消元与唯一二次根式

定义

\[
Q=(E_x-E_y)^2+G^2.
\]

则

\[
Q=q_2z^2+q_1z+q_0,
\]

其中

\[
q_2=(E_{x1}-E_{y1})^2+G_1^2,
\]

\[
q_1=2[(E_{x0}-E_{y0})(E_{x1}-E_{y1})+G_0G_1],
\]

\[
q_0=(E_{x0}-E_{y0})^2+G_0^2.
\]

并且

\[
d_\varepsilon=\frac{\sqrt Q}{D_0}.
\]

NC-M6 两个材料驱动主值直接为

\[
\lambda_1=\frac{E_x+E_y}{2(1-\nu)\varepsilon_{c0}D_0}
+\frac{\sqrt Q}{2(1+\nu)\varepsilon_{c0}D_0},
\]

\[
\lambda_2=\frac{E_x+E_y}{2(1-\nu)\varepsilon_{c0}D_0}
-\frac{\sqrt Q}{2(1+\nu)\varepsilon_{c0}D_0}.
\]

物理应力无需显式 theta：

\[
\sigma_x=\frac{f_c}{2}\left[(s_1+s_2)+(s_1-s_2)\frac{E_x-E_y}{\sqrt Q}\right],
\]

\[
\sigma_y=\frac{f_c}{2}\left[(s_1+s_2)-(s_1-s_2)\frac{E_x-E_y}{\sqrt Q}\right],
\]

\[
\tau_{xy}=\frac{f_c}{2}(s_1-s_2)\frac{G}{\sqrt Q}.
\]

这与 NC-M4 的处理原则相同：接受一个二次代数根式，不先要求消根。

---

## 5. NC-M6 每一材料解析 branch 仍属于同一个二次扩张

固定任一材料 branch 后：

- `C(c)` 为有理函数；
- `T_NC` 的每一支为有限多项式/线性/常数；
- CC/TC/TT 的有限乘积与八次项仍封闭在二次扩张内。

因此任一局部主应力、物理应力及 `P, R_A, R_u, R_v` 的厚度积分核均可整理成

\[
\boxed{
K(\xi,\eta,z)=\frac{A(\xi,\eta,z)+B(\xi,\eta,z)\sqrt Q}
{C(\xi,\eta,z)}
}
\]

其中 A、B、C 对 z 为有限有理/多项式表达，其系数可依赖

\[
u,\ v,\ u_{,\xi},u_{,\eta},v_{,\xi},v_{,\eta},\Delta,A,\xi,\eta.
\]

分母若出现 `a+b sqrt(Q)`，用代数共轭有理化；任意高次 `sqrt(Q)` 用 `Q` 归约。不会产生第二个独立根式。

---

## 6. 材料 branch/front 在厚度方向仍是精确二次代数根

NC-M6 材料坐标张量在半角公共分母下满足：若某一主材料坐标达到常数 `lambda_b`，则

\[
\det(\mathbf X-\lambda_b\mathbf I)=0
\]

等价于

\[
\boxed{
[(E_x+\nu E_y)-L_b][(\nu E_x+E_y)-L_b]
-\frac{(1-\nu)^2}{4}G^2=0
}
\]

其中

\[
L_b=(1-\nu^2)\varepsilon_{c0}D_0\lambda_b.
\]

因为 `E_x,E_y,G` 对 z 一次，上式对 z 至多二次。

用于 NC-M6 的全部材料阈值为

\[
\lambda_b\in\{0,\ 0.7x_{cr},\ 1.5x_{cr},\ 9x_{cr},\ 11x_{cr}\}.
\]

因此 sector front 与 `T_NC` branch front 都由有限个精确二次根给出。它们是连续材料状态前沿，不是数值空间 cell，也不改变 `N_formal_spatial_quadrature=0`。

---

## 7. z 向 Euler 精确积分

固定 `(\xi,\eta)` 和一个材料解析 branch，有

\[
Q=q_2z^2+q_1z+q_0.
\]

### 7.1 q2 > 0

取 Euler 变量

\[
w=\sqrt Q+\sqrt{q_2}\,z.
\]

则

\[
\boxed{
z=\frac{w^2-q_0}{2\sqrt{q_2}w+q_1}
}
\]

且 `sqrt(Q)`、`dz/dw` 均为 w 的有理函数。因此

\[
\int K(z,\sqrt Q)\,dz
=\int R(w)\,dw,
\]

右侧为普通有理函数积分。

### 7.2 q2 = 0, q1 != 0

取

\[
w=\sqrt{q_1z+q_0},
\]

\[
z=(w^2-q_0)/q_1,\qquad dz=2w/q_1\,dw,
\]

同样变成有理积分。

### 7.3 q2=q1=0

Q 与 z 无关，厚度核直接成为普通有理函数。

因此每个 branch 的厚度原函数严格属于有限组合

\[
\boxed{
F(z)=R_0(z,\sqrt Q)+\sum_i a_i\log L_i+\sum_j b_j\arctan M_j
}
\]

（或等价复对数形式）。

结论：

`NC_M6_EXACT_THICKNESS_INTEGRATION = PASS`。

---

## 8. P 与 R_A 的厚度积分已经可以完全消去积分号

板面半角 Jacobian 为

\[
dx\,dy=\frac{4b\ell}{\pi^2UV}d\xi d\eta.
\]

因此

\[
P=-\frac{4b}{\pi^2}
\int_0^\infty\int_0^\infty\frac1{UV}
\left[
\sum_k(F_{P,k}(z_{k+1})-F_{P,k}(z_k))
\right]d\eta d\xi,
\]

其中 `z_k` 仅为由上一节精确二次 front 方程给出的物理厚度端点。

同理

\[
R_A=\frac{4b\ell}{\pi^2}
\int_0^\infty\int_0^\infty\frac1{UV}
\left[
\sum_k(F_{A,k}(z_{k+1})-F_{A,k}(z_k))
\right]d\eta d\xi.
\]

这里已经没有 z 数值积分，也没有材料点。

---

## 9. R_u 与 R_v 经厚度精确凝聚后的真实二维连续方程

原弱式：

\[
R_u[\delta u]=\int_\Omega\int_{-h/2}^{h/2}
(\sigma_x\delta u_{,x}+\tau_{xy}\delta u_{,y})\,dz\,d\Omega=0,
\]

\[
R_v[\delta v]=\int_\Omega\int_{-h/2}^{h/2}
(\sigma_y\delta v_{,y}+\tau_{xy}\delta v_{,x})\,dz\,d\Omega=0.
\]

由于虚位移导数与 z 无关，z 积分可先完全精确完成。于是强式可以直接写为

\[
\boxed{
\partial_x\left\{\sum_k[F_{x,k}(z_{k+1})-F_{x,k}(z_k)]\right\}
+\partial_y\left\{\sum_k[F_{xy,k}(z_{k+1})-F_{xy,k}(z_k)]\right\}=0
}
\]

以及

\[
\boxed{
\partial_x\left\{\sum_k[F_{xy,k}(z_{k+1})-F_{xy,k}(z_k)]\right\}
+\partial_y\left\{\sum_k[F_{y,k}(z_{k+1})-F_{y,k}(z_k)]\right\}=0.
}
\]

这些 `F` 都是上一节 Euler 积分得到的显式 rational/algebraic/log/arctan endpoint functions；它们不是新的结构未知量。

---

## 10. 与 NC-M4 的关键区别现在被准确定位

旧 NC-M4 在进入半角有理化之前已经把面内运动学压成 `(Delta,A,epsilon_m)`，所以做完 z 凝聚后，板面剩余对象完全是有限代数函数，可继续识别为标准精确 period。

NC-M6 本轮故意不做该结构降阶，因此虽然 z 向仍严格初等解析闭合，但二维板面方程中仍保留

\[
u(\xi,\eta),\quad v(\xi,\eta),\quad\nabla u,\quad\nabla v.
\]

因此当前真正未闭合项不是 NC-M6 材料根式，而是连续面内平衡 PDE 本身。

本节点不提前决定该 PDE 应如何表示或降阶。

---

## 11. 当前锁定结论

1. 不需要 CC/TT 单独“消根工程”。
2. NC-M6 与 NC-M4 一样，全部局部厚度核只含一个二次代数根 `sqrt(Q)`。
3. `theta` 已可恒等消元。
4. `X,Y` 几何三角项已可半角有理化。
5. 所有 sector/T_NC branch 厚度前沿都是有限个二次代数根。
6. `P,R_A,R_u,R_v` 的 z 向积分全部可用 Euler substitution 精确初等闭合。
7. 做完 z 凝聚后，真正剩下的是含连续 `u,v` 的二维非线性平衡 PDE。
8. 当前仍不引入 alpha、epsilon_m、Ritz 系数、空间网格或 Case21。

下一步：只研究上述厚度凝聚后的二维 `R_u=0,R_v=0` 连续方程是否可直接解析闭合；在得到否定证据之前，不提前设计新的中间结构参数。