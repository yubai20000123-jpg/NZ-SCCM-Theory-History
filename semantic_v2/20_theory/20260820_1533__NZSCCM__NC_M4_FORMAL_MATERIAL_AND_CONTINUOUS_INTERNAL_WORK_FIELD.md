# NZ-SCCM — NC-M4 正式候选公式与连续多重积分内功场

时间：2026-08-20 15:33 +08:00

状态：`ACTIVE_MATERIAL_CANDIDATE / NOT_YET_PRODUCTION_LOCK`

## 1. NC-M4 正式候选公式

压缩骨架：

\[
C(c)=\frac{2c}{1+c^2},\qquad c=-\varepsilon_c/\varepsilon_{c0}\ge0.
\]

拉伸骨架：

\[
T_4(t)=1.07515\frac{t(t+0.09)}{1-0.83t+1.04t^2+0.14t^3},
\qquad t=\varepsilon_t/\varepsilon_{t0}\ge0.
\]

其峰值约位于 `t_p≈1.5716`，不再强迫 `t=1` 达峰。

TC/CT 压缩削弱：

\[
\beta(t)=\frac{1}{1+0.15t^2}.
\]

CC 双压增强：

\[
\eta(c_1,c_2)=1+0.16C(c_1)C(c_2).
\]

九宫格四实体区：

CC:
\[
\sigma_i=-f_c\eta(c_1,c_2)C(c_i),\qquad i=1,2.
\]

TC:
\[
\sigma_1=f_tT_4(t_1),\qquad
\sigma_2=-f_c\beta(t_1)C(c_2).
\]

CT:
\[
\sigma_1=-f_c\beta(t_2)C(c_1),\qquad
\sigma_2=f_tT_4(t_2).
\]

TT:
\[
\sigma_i=f_tT_4(t_i),\qquad i=1,2.
\]

边界 `ε1=0` 或 `ε2=0` 由相邻实体区自然退化，不新增材料子模型。

## 2. 一般矩形板连续半波运动学

保持 `b` 与 `ell` 独立：

\[
\phi(x,y)=\sin\frac{\pi x}{b}\sin\frac{\pi y}{\ell},
\]

\[
w_0=A_0\phi,\qquad w_m=A\phi,
\]

\[
S(A)=A_0A+\frac12A^2.
\]

当前三结构变量为：

\[
\mathbf q=(\Delta,A,\varepsilon_m).
\]

其中 `Delta` 为轴向缩短，`epsilon_m` 为横向均匀膜应变。连续二阶应变场写为：

\[
\varepsilon_x=\varepsilon_m+S\phi_{,x}^2-zA\phi_{,xx},
\]

\[
\varepsilon_y=-\frac{\Delta}{\ell}+S\phi_{,y}^2-zA\phi_{,yy},
\]

\[
\gamma_{xy}=2S\phi_{,x}\phi_{,y}-2zA\phi_{,xy}.
\]

## 3. 由主应力回到板坐标

若局部主方向 1 与 x 轴夹角为 `theta`，则：

\[
\sigma_x=\sigma_1\cos^2\theta+\sigma_2\sin^2\theta,
\]

\[
\sigma_y=\sigma_1\sin^2\theta+\sigma_2\cos^2\theta,
\]

\[
\tau_{xy}=(\sigma_1-\sigma_2)\sin\theta\cos\theta.
\]

每个空间点只调用一个九宫格实体关系；禁止 `CC_full+TC_full+TT_full` 全域叠加。

## 4. 三个广义方向的连续内虚功密度

定义：

\[
g_{xA}=(A_0+A)\phi_{,x}^2-z\phi_{,xx},
\]

\[
g_{yA}=(A_0+A)\phi_{,y}^2-z\phi_{,yy},
\]

\[
g_{\gamma A}=2(A_0+A)\phi_{,x}\phi_{,y}-2z\phi_{,xy}.
\]

则面外幅值方向：

\[
r_A=\sigma_xg_{xA}+\sigma_yg_{yA}+\tau_{xy}g_{\gamma A}.
\]

横向膜应变方向：

\[
r_m=\sigma_x.
\]

轴向缩短方向：

\[
r_\Delta=-\frac{\sigma_y}{\ell}.
\]

## 5. 一个连续完整半波上的三重积分

积分域：

\[
V=[0,b]\times[0,\ell]\times[-h/2,h/2].
\]

正式连续积分：

\[
R_A(\Delta,A,\varepsilon_m)
=\int_0^b\int_0^{\ell}\int_{-h/2}^{h/2}r_A\,dz\,dy\,dx=0,
\]

\[
R_m(\Delta,A,\varepsilon_m)
=\int_0^b\int_0^{\ell}\int_{-h/2}^{h/2}\sigma_x\,dz\,dy\,dx=0,
\]

\[
P(\Delta,A,\varepsilon_m)
=-\frac1\ell
\int_0^b\int_0^{\ell}\int_{-h/2}^{h/2}\sigma_y\,dz\,dy\,dx.
\]

这三个积分由同一个局部应力场产生，不建立第二套 Pu 求解器。

## 6. 材料状态支持域的正确组织

可写为：

\[
V=V_{CC}\cup V_{TC}\cup V_{CT}\cup V_{TT}\cup\text{measure-zero boundaries},
\]

并有：

\[
R_p=\sum_{s\in\{CC,TC,CT,TT\}}\iiint_{V_s}r_p^{(s)}dV.
\]

这只是材料响应支持域的数学表达，不是空间 cell/subdomain 离散；正式结构域仍是一个连续完整半波。

## 7. “能量场”必须严格改称内功/虚功场

当前 NC-M4 的 TC 耦合满足：

\[
\sigma_t=f_tT_4(t),\qquad
\sigma_c=-f_c\beta(t)C(c).
\]

因此：

\[
\frac{\partial\sigma_t}{\partial\varepsilon_c}=0,
\qquad
\frac{\partial\sigma_c}{\partial\varepsilon_t}
=-\frac{f_c}{\varepsilon_{t0}}\beta'(t)C(c)\ne0.
\]

故一般不存在路径无关的标量势能密度 `Psi(ε1,ε2)` 满足 `sigma_i=∂Psi/∂ε_i`。

CC 的当前 `eta=1+0.16 C1 C2` 也一般不满足交叉偏导对称性。

因此 NC-M4 当前能够严格形成的是：

\[
\boxed{\text{连续内虚功场 / 广义内力场}}
\]

而不是未经证明的超弹性标量势能场。

沿任一实际加载路径 `Gamma` 可定义累积内功：

\[
W_{int}[\Gamma]
=\int_{\Gamma}\left(P\,d\Delta+R_A\,dA+R_m\,d\varepsilon_m\right),
\]

但该量一般依赖路径。

## 8. 极限条件接口

在 `R_A=0, R_m=0` 上，若以 `Delta` 为路径变量，极限点满足：

\[
L=P_{,\Delta}-[P_{,A}\ P_{,m}]
\begin{bmatrix}
R_{A,A}&R_{A,m}\\
R_{m,A}&R_{m,m}
\end{bmatrix}^{-1}
\begin{bmatrix}
R_{A,\Delta}\\R_{m,\Delta}
\end{bmatrix}=0.
\]

等价地，可用相应 3×3 bordered determinant 的零值形式。

## 9. 当前治理结论

- `NC-M4 = ACTIVE_MATERIAL_CANDIDATE / NOT_YET_PRODUCTION_LOCK`。
- 当前已从材料公式推进到连续三重积分内功场。
- 尚未执行 Case21 Pu。
- 尚未使用空间 Gauss/Simpson/Chebyshev collocation/material-point grid。
- 下一步应检查上述三个连续积分能否在 NC-M4 下直接解析闭合，优先从 `R_m`、`P` 两个最简单核开始，再处理 `R_A`。