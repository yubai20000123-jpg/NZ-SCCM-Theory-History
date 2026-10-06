# BH100 固定总挠度下 UHPC 的 W_E–W_P–damage 自洽求解 R01

日期：2026-10-06  
分支：diagnostic/20261006-bh100-uhpc-we-wp-d-self-consistency  
对象：BH100，固定新增总面外挠度 w = 82.2 mm  
状态：理论重定位与生产求解合同；钢壳暂停，不使用 FEM 作为理论输入。

---

## 0. 本轮结论

旧 UHPC 路线的核心错误不是某个数值，而是求解顺序：

\[
w\to \text{一次性 full-elastic trial field}
\to d,\varepsilon^p
\to w_P
\to P_U
\]

该顺序把给定总挠度全部先视为可恢复弹性构形，plastic/damage 只在末端作为修正量，不能表达固定总挠度内部 elastic part、plastic reference geometry 与 damage stiffness 的相互反馈。

本轮改为钢壳 recoverable/plastic amplitude 思想的 UHPC 对应物：

\[
\boxed{
w\ \text{固定},\qquad
w=w_E+w_P,
}
\]

并在同一 current state 内联立

\[
\boxed{
w_E,\quad w_P,\quad d(x,y,z)
}
\]

直到构形分解、材料状态与结构平衡同时自洽。

钢壳与 UHPC 的共同结构是：

\[
\text{fixed total geometry}
\to
\text{recoverable elastic part}
+
\text{permanent reference part}.
\]

区别只在材料闭合：钢材可由 Mises/yield return 形成有限代数根；UHPC 使用分段 CDP stress–inelastic/cracking strain–damage 表，因此局部材料状态为分段代数根，空间分区边界仍是 quartic roots，整体至多保留有限一维确定性积分。

---

## 1. BH100 固定输入

\[
b=5000\ {\rm mm},\qquad
a_h=10000\ {\rm mm},\qquad
t_c=42\ {\rm mm},
\]

\[
E_c=43400\ {\rm MPa},\qquad
\nu_c=0.30,
\]

\[
w_0=bq_0=12.5\ {\rm mm},\qquad
w=82.2\ {\rm mm}.
\]

定义

\[
\alpha=\frac{\pi}{b},\qquad
\beta=\frac{\pi}{a_h},
\]

\[
\phi(x,y)=\sin\alpha x\sin\beta y.
\]

当前总构形振幅

\[
A_T=w_0+w=94.7\ {\rm mm}.
\]

---

## 2. 总构形、塑性参考构形与弹性构形

第一版先保留与钢壳 recoverable-amplitude 完全同构的一阶整体模态：

\[
W_T=A_T\phi,
\]

\[
W_R=(w_0+w_P)\phi,
\]

\[
W_E=w_E\phi.
\]

满足

\[
\boxed{
w_E+w_P=w.
}
\]

所以

\[
W_T=W_R+W_E.
\]

这里 W_R 是 current permanent/reference geometry，而不是原始制造缺陷本身。

在这一层不再允许先令 w_E=w 再在末端扣除 w_P。

---

## 3. 当前弹性几何增量

真正可恢复的 von Kármán 二阶几何量必须从 current reference geometry 到 current total geometry：

\[
Q
=
A_T^2-(w_0+w_P)^2.
\]

利用 w_P=w-w_E：

\[
\boxed{
Q(w_E)
=
2A_Tw_E-w_E^2
=
w_E^2+2(w_0+w_P)w_E.
}
\]

该式代替旧的一次性

\[
Q_E=w^2+2w_0w.
\]

注意：旧式只在 w_P=0 时成立。

---

## 4. damage 后的当前广义刚度

\[
D_0=
\frac{E_ct_c^3}{12(1-\nu_c^2)}.
\]

定义全板当前膜、弯保留系数：

\[
\rho_A,\qquad \rho_D.
\]

则

\[
A_c^{\rm eff}=\rho_AE_ct_c,
\]

\[
D_c^{\rm eff}=\rho_DD_0.
\]

固定 w、给定 w_E,\rho_A,\rho_D 后，第一模态 current equilibrium 写成

\[
\boxed{
\bar N_y
=
\rho_DD_0
\frac{(\alpha^2+\beta^2)^2}{\beta^2}
\frac{w_E}{w_0+w}
+
\rho_A\frac{E_ct_c}{16}
\frac{\alpha^4+\beta^4}{\beta^2}
Q(w_E).
}
\]

最终 UHPC 反力：

\[
\boxed{
P_U=b\bar N_y.
}
\]

这里 bending numerator 必须使用 recoverable amplitude w_E，geometric denominator 使用 current total amplitude w_0+w。

---

## 5. current recoverable elastic strain field

为保持原 Airy 一阶母场的解析结构，同时使 damage 进入 current stiffness，膜力谐波按 \rho_AE_ct_c 缩放：

\[
N_x^E
=
-\rho_A\frac{E_ct_c\alpha^2Q}{8}\cos(2\beta y),
\]

\[
N_y^E
=
-\bar N_y
-\rho_A\frac{E_ct_c\beta^2Q}{8}\cos(2\alpha x).
\]

于是 current recoverable 中面应变为

\[
\boxed{
\varepsilon_x^{E0}
=
\frac{\nu_c\bar N_y}{\rho_AE_ct_c}
-\frac{\alpha^2Q}{8}\cos(2\beta y)
+\frac{\nu_c\beta^2Q}{8}\cos(2\alpha x)
}
\]

\[
\boxed{
\varepsilon_y^{E0}
=
-\frac{\bar N_y}{\rho_AE_ct_c}
-\frac{\beta^2Q}{8}\cos(2\alpha x)
+\frac{\nu_c\alpha^2Q}{8}\cos(2\beta y).
}
\]

厚度方向只对 recoverable curvature 使用 w_E：

\[
\boxed{
\varepsilon_x^E
=
\varepsilon_x^{E0}
+
z\alpha^2w_E\phi
}
\]

\[
\boxed{
\varepsilon_y^E
=
\varepsilon_y^{E0}
+
z\beta^2w_E\phi
}
\]

\[
\boxed{
\gamma_{xy}^E
=
2z\alpha\beta w_E
\cos\alpha x\cos\beta y.
}
\]

主 recoverable elastic strains：

\[
\varepsilon_{1,2}^E
=
\frac{\varepsilon_x^E+\varepsilon_y^E}{2}
\pm
\frac12
\sqrt{
(\varepsilon_x^E-\varepsilon_y^E)^2
+(\gamma_{xy}^E)^2
}.
\]

---

## 6. 必须区分：Abaqus inelastic/cracking strain 与 true plastic strain

UC141 原始输入表不是“总应变表”。

压缩 hardening 第二列是 compressive inelastic strain；
拉伸 stiffening 第二列是 cracking strain。

因此在压缩峰值：

\[
\sigma_c=141.1\ {\rm MPa},\qquad
\xi_c^{in}=0.000248848,
\qquad
d_c=0.036205109.
\]

由 Abaqus 输入定义：

\[
\varepsilon_c^{tot}
=
\xi_c^{in}
+
\frac{\sigma_c}{E_c}
=
0.003500000074.
\]

所以用户所称“约 251 微应变塑性量”严格说是 inelastic strain：

\[
\xi_c^{in}=248.848\ \mu\varepsilon.
\]

若严格按 damage-plasticity 的 damaged elastic strain 分解，则 true plastic strain 为

\[
\boxed{
\varepsilon_c^p
=
\xi_c^{in}
-
\frac{d_c}{1-d_c}
\frac{\sigma_c}{E_c}
=
0.000126717953.
}
\]

拉伸峰值的原始表节点为

\[
\sigma_t=7.3\ {\rm MPa},
\qquad
\xi_t^{ck}=0.000802233,
\qquad
d_t=0.58207912,
\]

对应

\[
\varepsilon_t^{tot}
=
\xi_t^{ck}
+
\frac{\sigma_t}{E_c}
=
0.000970435765,
\]

以及 true plastic strain

\[
\boxed{
\varepsilon_t^p
=
\xi_t^{ck}
-
\frac{d_t}{1-d_t}
\frac{\sigma_t}{E_c}
=
0.000567960624.
}
\]

因此本轮必须把两个概念分开：

1. inelastic/cracking strain：Abaqus 输入表第二列；
2. true plastic strain：扣除 damage-induced elastic strain 后的永久塑性量。

生产主线优先使用 true plastic strain 生成 plastic reference geometry；
若后续专门验证“把 raw inelastic/cracking strain 全部视为 permanent geometry source”的结构级近似，则必须另标记为 reduced diagnostic，不能与 CDP true plastic 混名。

---

## 7. 每一材料表区间均可显式代数反求，不需要材料点 Newton

对任一 tension/compression 表区间，以材料内部变量 \xi 表示 cracking/inelastic strain。

该区间内

\[
\sigma(\xi)=a_\sigma+b_\sigma\xi,
\]

\[
d(\xi)=a_d+b_d\xi.
\]

若 current recoverable principal elastic strain 为 \eta_E，damaged-elastic relation 为

\[
\boxed{
\eta_E
=
\frac{\sigma(\xi)}
{[1-d(\xi)]E_c}.
}
\]

于是 \xi 不是数值迭代量，而是直接：

\[
\boxed{
\xi
=
\frac{
E_c\eta_E(1-a_d)-a_\sigma
}{
b_\sigma+E_c\eta_Eb_d
}.
}
\]

得到 \xi 后：

\[
\sigma=a_\sigma+b_\sigma\xi,
\]

\[
d=a_d+b_d\xi,
\]

\[
\boxed{
\varepsilon^p
=
\xi
-
\frac{d}{1-d}
\frac{\sigma}{E_c}.
}
\]

因此 UHPC local return 的核心仍然是有限代数根/显式有理式，不是积分点 Newton。

---

## 8. 软化分支的 branch identity 不能靠“任选一个根”

由于 post-peak 表中 \sigma(\xi) 下降，同一个 recoverable elastic strain可能对应多个 \xi。

所以生产求解必须采用 connected active-set：

1. 先用 virgin/full-elastic predictor 在固定 w=82.2 mm 下识别每一点第一次落入的材料表区间；
2. 进入 plastic/damage active set 后，该点不得因为 current elastic stress 回落而自动“反塑化”；
3. 后续只允许在相邻表区间之间按 monotonic internal variable \xi 更新；
4. 每个区间内 \xi 仍用上一节显式有理式；
5. branch switch 只发生在材料表节点，不需要黑箱连续优化。

这一规则是 UHPC 对应于钢材 return mapping / active-set 的必要版本。

---

## 9. plastic reference geometry

在两个主方向得到 signed true plastic strains p_1,p_2 后，按 principal direction \theta 回转：

\[
\varepsilon_{x,p}
=
p_1\cos^2\theta+p_2\sin^2\theta,
\]

\[
\varepsilon_{y,p}
=
p_1\sin^2\theta+p_2\cos^2\theta,
\]

\[
\gamma_{xy,p}
=
2(p_1-p_2)\sin\theta\cos\theta.
\]

上下表面：

\[
\kappa_{x,p}
=
\frac{\varepsilon_{x,p}^{+}-\varepsilon_{x,p}^{-}}{t_c},
\]

\[
\kappa_{y,p}
=
\frac{\varepsilon_{y,p}^{+}-\varepsilon_{y,p}^{-}}{t_c}.
\]

第一模态 plastic reference amplitude 为

\[
\boxed{
w_P^{\rm calc}
=
\frac{
\displaystyle
\int_A\phi
[
(\alpha^2+\nu_c\beta^2)\kappa_{x,p}
+
(\beta^2+\nu_c\alpha^2)\kappa_{y,p}
]dA
}{
\displaystyle
(\alpha^4+\beta^4+2\nu_c\alpha^2\beta^2)
\int_A\phi^2dA
}.
}
\]

且

\[
\int_A\phi^2dA=\frac{ba_h}{4}.
\]

自洽条件：

\[
\boxed{
F_E
=
w_E+w_P^{\rm calc}-w
=
0.
}
\]

---

## 10. damage condensation

上下表面 damage：

\[
d^+(x,y),\qquad d^-(x,y).
\]

定义

\[
d_0=\frac{d^++d^-}{2},
\qquad
d_1=\frac{d^+-d^-}{2}.
\]

局部膜、弯保留：

\[
\rho_A^{loc}=1-d_0,
\]

\[
\rho_D^{loc}
=
(1-d_0)
-
\frac{d_1^2}{3(1-d_0)}.
\]

膜权函数：

\[
\Psi_A
=
\alpha^4\cos^2(2\beta y)
+
\beta^4\cos^2(2\alpha x)
-
2\nu_c\alpha^2\beta^2
\cos(2\alpha x)\cos(2\beta y),
\]

\[
\int_A\Psi_A dA
=
\frac{ba_h}{2}(\alpha^4+\beta^4).
\]

弯曲权函数：

\[
\Psi_D
=
(\alpha^4+\beta^4+2\nu_c\alpha^2\beta^2)
\sin^2\alpha x\sin^2\beta y
+
2(1-\nu_c)\alpha^2\beta^2
\cos^2\alpha x\cos^2\beta y,
\]

\[
\int_A\Psi_DdA
=
\frac{ba_h}{4}(\alpha^2+\beta^2)^2.
\]

所以

\[
\boxed{
F_A
=
\rho_A
-
\frac{\int_A\rho_A^{loc}\Psi_A dA}
{\frac{ba_h}{2}(\alpha^4+\beta^4)}
=
0,
}
\]

\[
\boxed{
F_D
=
\rho_D
-
\frac{\int_A\rho_D^{loc}\Psi_D dA}
{\frac{ba_h}{4}(\alpha^2+\beta^2)^2}
=
0.
}
\]

---

## 11. 第一生产求解器只有三个全局未知量

固定 w=82.2 mm 后：

\[
\boxed{
\mathbf x=
(w_E,\rho_A,\rho_D)^T.
}
\]

联立：

\[
\boxed{
\begin{cases}
F_E(w_E,\rho_A,\rho_D)=0,\\
F_A(w_E,\rho_A,\rho_D)=0,\\
F_D(w_E,\rho_A,\rho_D)=0.
\end{cases}
}
\]

然后

\[
w_P=w-w_E
\]

和

\[
P_U=b\bar N_y
\]

直接恢复。

这就是 UHPC 版的 recoverable/plastic-amplitude return problem。

---

## 12. 不允许二维空间网格：quartic roots 仍然保留

令

\[
u=\sin\alpha x,\qquad
v=\sin\beta y.
\]

对上下表面 s=\pm1，current recoverable strain 仍具有

\[
\varepsilon_x^{(s)}
=
c_x+a_xu^2+b_xv^2+s r_xuv,
\]

\[
\varepsilon_y^{(s)}
=
c_y+a_yu^2+b_yv^2+s r_yuv,
\]

\[
\gamma_{xy}^{(s)}
=
s r_\gamma
\sqrt{1-u^2}\sqrt{1-v^2}.
\]

其中所有系数只需把旧全弹性 w,Q_E,N_y 换为 current w_E,Q,\bar N_y,\rho_A。

任意 principal elastic-strain threshold \lambda 的边界：

\[
(\varepsilon_x^{(s)}-\lambda)
(\varepsilon_y^{(s)}-\lambda)
-
\frac14(\gamma_{xy}^{(s)})^2
=0.
\]

固定 u 后严格化为

\[
\boxed{
C_4v^4+C_3v^3+C_2v^2+C_1v+C_0=0.
}
\]

因此：

- material table node；
- damage branch node；
- plastic branch node；
- active-set switch node；

全部由有限 quartic roots 给出。

正式生产不使用 101x101、401x401、二维 Gauss 网格或 differential evolution。

如果分区内的最终 integrand 因 principal square-root / rational damage 不能化成初等原函数，则允许保留有限个一维确定性代数型定积分；这是当前数学上真实的解析上限。

---

## 13. “形函数发生变化”如何进入，而不立即膨胀成高维模型

R01 先做 same-mode self-consistency：

\[
W_E=w_E\phi,\qquad
W_P=w_P\phi.
\]

但求解后必须计算完整 plastic-curvature residual：

\[
R_p(x,y)
=
\kappa_p(x,y)
-
\Pi_{11}\kappa_p(x,y).
\]

若高阶 residual energy 不可忽略，再只增加由 plastic curvature 投影实际产生的少量正交谐波；不得预设大规模高阶 Ritz。

也就是说：

\[
\boxed{
\text{先验证一阶钢壳式翻版是否已经闭合；
只有 residual 明确要求时才扩充形函数。}
}
\]

这保持计算成本与物理可审计性。

---

## 14. BH100 @ 82.2 mm 的当前已知诊断

旧 full-elastic mother field 在 w=82.2 mm 给出：

\[
P_U^E\approx11.57495\ {\rm MN}.
\]

其最大 trial strains 约为：

\[
\varepsilon_{t,max}^{trial}\approx1.465\times10^{-3},
\]

\[
\varepsilon_{c,max}^{trial}\approx1.543\times10^{-3}.
\]

因此该点的核心不是 compression crushing，而是 tensile inelastic/damage 已经明显激活。

旧单向算法得到的约

\[
P_U\approx10.57\ {\rm MN}
\]

不再作为 regression truth，因为它没有让 w_E-w_P-d 重新闭合。

---

## 15. 当前执行顺序

生产下一步严格按以下顺序：

1. 锁定 UC141 原始 23 行 tension stiffening/damage 与 30 行 compression hardening/damage 表；
2. 将每一表段转换为 a_sigma,b_sigma,a_d,b_d；
3. 建立 current w_E,rho_A,rho_D 三未知系统；
4. 用 virgin elastic predictor 只做 active-set 初始识别；
5. 每一材料段内部只做显式代数反求；
6. 空间边界只做 quartic roots；
7. rho_A,rho_D,w_P 用分区一维确定性积分；
8. 求 F_E=F_A=F_D=0；
9. 输出 w_E、w_P、rho_A、rho_D、damage 最大值与区域、active material segments、P_U(82.2)；
10. 再做 plastic-curvature high-mode residual 审计；只有 residual 显著时增加形函数；
11. 在 BH100 单点闭合以前，不重新接 steel shell，也不批量跑九件。

---

## 16. 禁止项

- 不再把 w=82.2 全部先作为 elastic amplitude；
- 不再把 epsilon_tp/epsilon_cp 称为“纯弹性强度应变”；
- 不再把 Abaqus inelastic/cracking strain 与 true plastic strain 混为一谈；
- 不再做 peak-rebased plastic strain 清零作为本轮主线；
- 不再用 old BH050 7.503 MN 或 old BH100 10.569 MN 作为当前回归门；
- 不使用 FEM stress/strain 作为本理论输入；
- 不使用二维空间离散积分作为生产算法；
- 不在 BH100 单点闭合前接入钢壳。

---

## 17. 当前理论身份

\[
\boxed{
\text{BH100 fixed-}w
+
\text{UHPC recoverable/plastic reference split}
+
\text{CDP algebraic local return}
+
\text{damage-weighted current stiffness}
+
\text{quartic level sets}
+
\text{finite 1D deterministic integrals}
}
\]

这是当前唯一允许继续实现的 UHPC 单点闭合路线。
