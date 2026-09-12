# H1 STEP-9：\(K_p^{mat}\) 精确厚度分区与 History Transport R02

## 0. 本步身份

本步推进 STEP-8 的两个 open blocks：

\[
K_h=K_e+K_g^{trial}-K_p^{mat}-K_p^{hist-g}.
\]

正式进展：

\[
\boxed{K_p^{mat}\text{ 的厚度 active-set partition 与 }z\text{ 积分已经闭合}}
\]

但 phase \((\xi,\psi)\) algebraic-period evaluator 仍未 production-close。

\[
\boxed{K_p^{hist-g}}
\]

已建立 continuous path-rate identity，但 history-period transport evaluator 仍 open。

没有修改 A20、finite force、Multiwave 权重，也没有 FEM 拟合系数。

## 1. Exact active thickness partition

through-thickness trial stress：

\[
\sigma^{tr}(z)=s_0+zs_1.
\]

yield excess：

\[
g_y(z)=\phi_{tr}^2-f_y^2
=a_yz^2+b_yz+c_y.
\]

未归一化 Mises normal：

\[
m=
[\sigma_x-\sigma_y/2,\ \sigma_y-\sigma_x/2,\ 3\tau]^T
=m_0+zm_1.
\]

local amplitude path direction：

\[
b_A(z)=b_{A0}+zk_\Psi.
\]

loading-index sign：

\[
g_\chi(z)=m^TC_eb_A
=a_\chi z^2+b_\chi z+c_\chi.
\]

所以：

\[
\boxed{
I_A(\xi,\psi)=
\{z\in[-t_s/2,t_s/2]:
g_y(z)\ge0,\ g_\chi(z)>0\}
}
\]

由两个二次方程实根精确分区。

不存在 thickness Gauss 点。

## 2. Material correction 的根号消去

因为：

\[
n=m/\phi,
\]

有恒等式：

\[
\boxed{
\frac{(B_a^TC_en)(B_b^TC_en)}
{n^TC_en}
=
\frac{(B_a^TC_em)(B_b^TC_em)}
{m^TC_em}.
}
\]

而：

\[
B_a=b_{a0}+zk_a,
\quad
m=m_0+zm_1.
\]

故：

\[
B_a^TC_em=u_{a0}+u_{a1}z+u_{a2}z^2,
\]

\[
m^TC_em=d_0+d_1z+d_2z^2.
\]

于是：

\[
\boxed{
K_{p,ab}^{mat}(\xi,\psi)
=
\sum_{I\subset I_A}
\int_I\frac{P_4(z)}{Q_2(z)}\,dz.
}
\]

这是 elementary primitive：
polynomial division 后只剩多项式、\(\ln\)、\(\arctan\)/logarithmic quadratic primitive。

本步随机正二次分母 primitive regression 的最大相对误差为：

\[
\boxed{1.64\times10^{-10}}
\]

（对超高密度一维 numerical reference）。

## 3. 剩余 phase operator

厚度消元后：

\[
\boxed{
K_{p,ab}^{mat}
=
\frac1{4\pi^2}
\int_0^{2\pi}\int_0^{2\pi}
\mathcal I_{ab}(\xi,\psi)\,d\xi d\psi.
}
\]

\(\mathcal I_{ab}\) 的 topology 由二次根排序、yield/loading inequalities 决定，
因此属于 H1 第55–56节的 algebraic-period 对象。

正式 identity：

\[
\boxed{
K_p^{mat}
=
\mathfrak P_{\Omega_A}[\mathcal I].
}
\]

## 4. Numerical regression 的纠正

本步最初尝试用低阶 tanh-sinh 直接评价具有 sharp active-topology switching 的 phase period。
虽然 active-volume measure 已接近，但 matrix entries 没有收敛，**该尝试正式撤回，不作为成功结果**。

随后改用同一 phase midpoint grid 只做 diagnostic regression：

- 一侧：每个 phase 点使用 exact quadratic active intervals + exact \(P_4/Q_2\) thickness primitive；
- 另一侧：完全相同 phase 点，厚度使用 121-point dense midpoint reference。

这样只检验 exact-\(z\) reduction，不把 phase grid 冒充 production period evaluator。

| Case | exact active fraction | dense-z active fraction | exact-z vs dense-z matrix | phase 24→40 change |
|---|---:|---:|---:|---:|
| BH050 | 0.3457 | 0.3457 | 0.030% | 0.378% |
| BH060 | 0.3452 | 0.3451 | 0.032% | 0.435% |
| BH100 | 0.3138 | 0.3138 | 0.013% | 0.461% |

其中 `exact-z vs dense-z` 是当前真正应该看的厚度闭合 regression；
`phase 24→40` 仍只是说明 phase algebraic-period evaluator 尚需进一步实现。

## 5. 为什么 \(K_p^{hist-g}\) 仍必须保留 history

perfect-plastic rate：

\[
\dot\sigma=C_e(\dot\varepsilon-\dot\lambda n)
\]

\[
\dot\lambda=
\begin{cases}
\dfrac{n^TC_e\dot\varepsilon}{n^TC_en},&f=0,\chi>0,\\
0,&elastic/unloading.
\end{cases}
\]

一旦某点经历塑性后卸载：

\[
C_{tan}=C_e
\]

但：

\[
\boxed{\sigma^{ep}\neq\sigma^{trial}}.
\]

所以 current active set 只能决定 material tangent correction，
不能恢复 geometric stiffness 所需的 current finite stress history。

## 6. History transport identity

connected path 参数 \(s\)：

\[
\boxed{
\frac{d\sigma^{ep}}{ds}
=
C_{ep}\frac{d\varepsilon}{ds}.
}
\]

并：

\[
\boxed{
\frac{dK_{g,ab}^{ep}}{ds}
=
\left\langle\int
[
\dot\sigma_xp_{x,a}p_{x,b}
+\dot\sigma_yp_{y,a}p_{y,b}
+\dot\tau(p_{x,a}p_{y,b}+p_{y,a}p_{x,b})
]dz
\right\rangle.
}
\]

从 first yield transport：

\[
\boxed{
K_g^{ep}(s)
=
K_g^{ep}(s_y)
+
\int_{s_y}^{s}\dot K_g^{ep}\,d\hat s.
}
\]

因此理论上不需要“把卸载折算成某个经验 \(r\)”；
真正需要的是 continuous history topology / period transport。

## 7. 状态更新

- \(K_e\)：CLOSED
- \(K_g^{trial}\)：CLOSED
- \(K_p^{mat}\)：**THICKNESS CLOSED / PHASE ALGEBRAIC-PERIOD OPEN**
- \(K_p^{hist-g}\)：**RATE IDENTITY CLOSED / HISTORY-PERIOD EVALUATOR OPEN**
- A17：LOCKED
- A20：不改
- A22：保留 finite-force 身份，但必须提供 history-consistent current stress
- A23-LH：第一优先
- A20-X、A07/A08、A26-A29：冻结

## 8. 下一步

现在只剩两个 numerical-analysis 实现问题，不能再通过新增物理假定解决：

1. phase algebraic-period 的 certified / validated evaluator；
2. connected path 的 history-period transport。

下一步先实现第1项，并在 BH050/BH060/BH100 的 frozen states 上把 \(K_p^{mat}\) phase period 收敛；
再把同一 evaluator 嵌入 history transport。
