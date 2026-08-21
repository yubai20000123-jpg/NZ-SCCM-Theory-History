# NZ-SCCM — FULL AR2 TWO-HALFWAVE ↔ ONE REPRESENTATIVE HALFWAVE 等价性审计

时间：2026-08-21 13:18 +08:00
状态：`STEP1_COMPLETED_WITH_CONDITIONAL_PASS`
材料：`NC-M6 FROZEN`

## 0. 本审计回答的问题

对全板 `a=2b`、四边简支、理想两个完整半波，当前正式 H_{2N} 体系把 `ell=b` 的一个完整半波作为代表域。本审计逐项检查：

`u,v,w -> strain -> current material map -> P,R,J`

是否能从全板严格约化到一个代表半波。

结论必须区分两件事：

1. **重复两半波子空间内的严格等价**；
2. **对全板全部允许扰动的全局 production 等价**。

二者不能混写。

---

## 1. 几何与坐标

全板：

\[
\Omega_F=\{0\le x\le b,\ 0\le y\le a=2\ell\},\qquad \ell=b.
\]

代表半波：

\[
\Omega_H=\{0\le x\le b,\ 0\le s\le\ell\}.
\]

写

\[
y=r\ell+s,\qquad r\in\{0,1\},\qquad 0\le s\le\ell,
\]

并定义

\[
X=\pi x/b,\qquad Y=\pi s/\ell,\qquad \chi_r=(-1)^r.
\]

全板理想两半波横向场：

\[
w_F=b(q_0+q)\sin X\sin\frac{2\pi y}{a}
=b(q_0+q)\sin X\sin\frac{\pi y}{\ell}.
\]

故

\[
\boxed{w_F(x,r\ell+s)=\chi_r w_H(x,s)}.
\]

`w0` 与 `Delta w` 分别满足同一关系。

---

## 2. 内部节点 y=ell 的兼容

第一半波末端 `s=ell` 与第二半波起点 `s=0`：

\[
w_H(x,\ell)=0,\qquad -w_H(x,0)=0.
\]

又因为

\[
\partial_s w_H\propto \cos(\pi s/\ell),
\]

有

\[
\partial_y w_F(x,\ell^-)
=\partial_y w_F(x,\ell^+).
\]

`w_x` 在内部节点两侧均为零；由同一全局正弦函数直接求导可知所有需要的曲率分量均为单值连续场。内部 `y=ell` 只是理想两半波的 nodal line，不是额外支承。

因此：

`W_CONTINUITY_GATE = PASS`。

---

## 3. H_{2N} 面内位移的全板延拓

代表半波 H_{2N}：

\[
u_H=\varepsilon_0\left[\eta x+\sum_{m=1}^N\sum_{n=0}^N
\frac{b}{2m\pi}a_{2m,2n}\sin 2mX\cos 2nY\right],
\]

\[
v_H=\varepsilon_0\left[-Ds+\sum_{m=0}^N\sum_{n=1}^N
\frac{\ell}{2n\pi}b_{2m,2n}\cos2mX\sin2nY\right].
\]

利用

\[
\cos[2n(Y+\pi)]=\cos2nY,\qquad
\sin[2n(Y+\pi)]=\sin2nY,
\]

全板重复延拓为

\[
\boxed{u_F(x,r\ell+s)=u_H(x,s)},
\]

\[
\boxed{v_F(x,r\ell+s)=v_H(x,s)-r\varepsilon_0D\ell}.
\]

常数平移不改变 strain。

在 `y=ell`：

\[
v_H(x,\ell)=-\varepsilon_0D\ell,
\]

而第二半波起点

\[
v_H(x,0)-\varepsilon_0D\ell=-\varepsilon_0D\ell.
\]

故 `u,v` 均连续；全板端点为 `v(x,0)=0`、`v(x,2ell)=-2 eps0 D ell`。Swartz 的 `eta=0` 继续保证两条 x 侧边逐点 `u=0`；Z 的自由 `eta` 仍由 `R_eta=0` 决定。

因此：

`UV_REPEAT_EXTENSION_GATE = PASS`。

---

## 4. von Karman 膜应变严格重复

当前二阶几何增量采用

\[
\varepsilon^G_{ij}
=\frac12\left[(w_0+\Delta w)_{,i}(w_0+\Delta w)_{,j}
-w_{0,i}w_{0,j}\right].
\]

两个半波间所有一阶 `w` 导数同时乘 `chi_r`，故二次积中的符号严格抵消：

\[
\boxed{\varepsilon^{G,(2)}(x,s)=\varepsilon^{G,(1)}(x,s)}.
\]

H_{2N} 线性膜 strain 由上一节的周期延拓同样逐点重复。因此完整中面膜应变满足

\[
\boxed{\varepsilon_m^{(2)}(x,s)=\varepsilon_m^{(1)}(x,s)}.
\]

`VON_KARMAN_REPEAT_GATE = PASS`。

---

## 5. 弯曲应变与 z-reflection

`Delta w` 的所有二阶曲率在相邻半波间乘 `chi_r`。Kirchhoff/Nguyen 当前板应变中的弯曲部分对厚度坐标 `z` 为线性，因此第二半波满足

\[
\varepsilon_b^{(2)}(x,s,z)=-\varepsilon_b^{(1)}(x,s,z)
=\varepsilon_b^{(1)}(x,s,-z).
\]

结合膜应变重复：

\[
\boxed{
\varepsilon_F(x,\ell+s,z)
=\varepsilon_H(x,s,-z)
}.
\]

该式可直接从当前 H2 显式式中的 `B zeta phi` 与 `-2k B zeta c` 检查：`phi`、`c` 在 `Y->Y+pi` 下同时反号，所有 bending 项等价于 `z->-z`；`M` 型 von-Karman 项保持不变。

`THICKNESS_REFLECTION_GATE = PASS`。

---

## 6. 多相截面对称性

上述 z-reflection 要进入材料和体积分，要求相集合关于中面成对：同一 `+z` 与 `-z` 位置具有相同材料律与几何权重。

### Z0–Z5 / Z family

当前 Z 组装满足：

- concrete core 关于 `z=0` 对称；
- upper/lower face steel 厚度相同、材料律相同；
- web/PBL 等效相在对称 core 体积中按同一 longitudinal current law 分布。

故 phase measure 在 `z->-z` 下不变。

### Swartz24

当前源数据为一层钢筋位于板中面，或两层钢筋按两侧相同 cover 布置；因此当前 RC 截面模型关于中面成对。单层 `z=0` 自身不变，两层在 `z->-z` 下互换。

因此对当前两类验证族：

`SECTION_PHASE_REFLECTION_GATE = PASS`。

若未来加入不对称单侧加劲、不同上下材料、偏置钢筋层等，该结论必须重新审计，不能自动继承。

---

## 7. M6 与其他 current maps 不需要额外对称假设

因为第二半波的物理 strain 并不是简单取负，而是第一半波在 `-z` 处的**同一个 strain tensor**：

\[
\varepsilon_2(x,s,z)=\varepsilon_1(x,s,-z).
\]

故对任意局部 current map `M_p`：

\[
\sigma_2(x,s,z)
=M_p(\varepsilon_2)
=M_p(\varepsilon_1(x,s,-z))
=\sigma_1(x,s,-z).
\]

同理 source-consistent tangent：

\[
\boxed{D_2(x,s,z)=D_1(x,s,-z)}.
\]

因此本证明**不要求** NC-M6 为奇函数、势函数或 major-symmetric tangent，也不要求修改 CC/TC/TT/T5。

`CURRENT_MAP_GATE = PASS`。

---

## 8. 广义 strain derivatives 的映射

对当前 generalized coordinates

\[
z_i\in\{D,q,\eta,c_\mu\},
\]

有

\[
\boxed{
\varepsilon^{(2)}_{,i}(x,s,z)
=\varepsilon^{(1)}_{,i}(x,s,-z)
}.
\]

唯一非零的二阶 strain derivative `epsilon_,qq` 为 von-Karman 膜项，因此在两半波间直接重复；也满足同一 z-reflection 映射。

---

## 9. Residual 的严格倍数关系

代表半波：

\[
R_i^H=\sum_p\int_{V_{p,H}}
\sigma_p:\varepsilon_{,i}\,dV.
\]

全板第二半波作变量替换 `z'=-z`。由截面对称和上两节映射，第二半波积分恰等于第一半波：

\[
\int_{V_{p,2}}\sigma:\varepsilon_{,i}\,dV
=\int_{V_{p,1}}\sigma:\varepsilon_{,i}\,dV.
\]

因此

\[
\boxed{R_i^F=2R_i^H}.
\]

故

\[
\boxed{R_i^H=0\iff R_i^F=0}
\]

**在重复两半波子空间内严格成立。**

---

## 10. 轴力 P 的严格等价

代表半波定义：

\[
P_H=-\frac1\ell\sum_p\int_{V_{p,H}}\sigma_y\,dV.
\]

全板对应定义必须使用全长 `2ell`：

\[
P_F=-\frac1{2\ell}\sum_p\int_{V_{p,F}}\sigma_y\,dV.
\]

全板积分为代表半波的两倍，因此

\[
\boxed{P_F=P_H}.
\]

同样

\[
\boxed{P_{F,j}=P_{H,j}}.
\]

---

## 11. source-consistent Jacobian 的严格倍数关系

当前 Jacobian：

\[
J_{ij}=\sum_p\int
\left[\varepsilon_{,i}^TD_p\varepsilon_{,j}
+\sigma_p:\varepsilon_{,ij}\right]dV.
\]

每一项均满足 z-reflection 映射，故

\[
\boxed{J_{ij}^F=2J_{ij}^H}.
\]

不需要强制 `J=J^T`，也不需要强制 NC-M6 tangent major symmetry。

于是代表子空间内的 equilibrium branch 与 load extremum/KKT 条件保持不变：residual 行乘常数 2 不改变零点或 rank-loss 位置；`P` 本身不变。

`P_R_J_REPEAT_SUBSPACE_GATE = PASS`。

---

## 12. 关键发现：这还不是“全板无遗漏”的证明

当前代表 H_{2N} 的 longitudinal harmonics 是

\[
\cos(2nY),\ \sin(2nY),\qquad Y=\pi s/\ell.
\]

若改用全板坐标

\[
\bar Y=\pi y/a=\pi y/(2\ell),
\]

则这些项成为

\[
\cos(4n\bar Y),\ \sin(4n\bar Y).
\]

也就是说，代表半波延拓只覆盖全板 longitudinal Fourier family 中 `r=0 mod 4` 的重复子空间。

而全板 essential BC 本身还允许其他 longitudinal harmonics，例如 `r` 非 `4n` 的模式；这些模式能够描述两个理想半波之间的**膜内重分布差异/互补扰动**，但当前一个代表半波将其强制为零。

因此已经证明的是：

\[
\boxed{\mathcal V_{rep}\subset\mathcal V_{full}}
\]

且 `V_rep` 是当前全板方程的一个严格 invariant equilibrium subspace。

尚未证明：

\[
\boxed{\mathcal V_{rep}=\mathcal V_{full}}.
\]

后者一般不成立。

---

## 13. 为什么代表解仍然是全板的精确平衡解

在 representative state 上，厚度积分后的 current stress/tangent coefficients 沿 y 具有半波长度 `ell` 的重复性；因此它们的全板 Fourier 内容只含与该重复周期相容的 harmonics。

对任意不属于重复 family 的互补 full-panel test mode，Galerkin/virtual-work 投影在两个半波间抵消。因此其 residual 在 representative state 上为零。

所以嵌入关系不是近似：

\[
\boxed{
R_{full}(z_{rep},c_\perp=0)=0
}
\]

只要 `R_rep(z_rep)=0`。

但 tangent 还包含互补扰动块。

选择按重复/互补 sector 排列的全板坐标，可写为

\[
\boxed{
J_{full}=
\begin{bmatrix}
2J_{rep} & 0\\
0 & J_\perp
\end{bmatrix}
}
\]

其中零耦合来自代表状态的周期/对称正交性；`J_perp` 不存在于单代表半波模型中。

因此全板可能先发生：

\[
\det J_\perp=0,
\]

即两个半波之间的 secondary / symmetry-breaking / halfwave-difference instability，哪怕 `J_rep` 尚未到自己的 limit point。

---

## 14. STEP 1 最终裁决

逐项结果：

- w 两半波延拓与内部节点兼容：PASS
- H2N u,v 延拓与 essential BC：PASS
- von-Karman 膜 strain 重复：PASS
- bending strain ↔ z-reflection：PASS
- Swartz/Z 当前截面相对中面对称：PASS
- current material map：PASS，M6 无需修改
- representative P、R、J 与 full repeated-sector 的倍数/归一关系：PASS
- **“全板没有任何额外 generalized perturbation”**：FAIL / NOT TRUE
- **“单代表半波自动给出 unrestricted full-panel first instability/ultimate”**：NOT YET PROVED

故正式状态：

`REPEATED_TWO_HALFWAVE_SUBSPACE_EQUIVALENCE = EXACT_PASS`

`UNRESTRICTED_FULL_PANEL_EQUIVALENCE = CONDITIONAL_NOT_YET_PASS`

`ONE_CONTINUOUS_COMPLETE_HALFWAVE = RETAINED_AS_EXACT_REPRESENTATIVE_SUBSPACE, NOT YET GLOBAL_PRODUCTION_CERTIFIED`

NC-M6 保持冻结；M7 继续禁止。

---

## 15. 新的唯一下一门禁：互补模态稳定性

继续 H12 以前，应在 full `a=2b` 域构造最小必要的 complementary membrane Ritz sector `V_perp`，但**不需要先做第二套完整 nonlinear full-panel solve**。

在每个 representative equilibrium state 上只评估

\[
\boxed{J_\perp(D,q,\eta,c)}.
\]

判据：

1. 若沿 origin-connected representative branch 直到其第一可达极限点，`J_perp` 始终保持 full rank / 不出现零特征条件，则代表半波对当前理想两半波分支获得 global-mode gate PASS；
2. 若 `J_perp` 在更低荷载先失去 rank，则单代表半波 production identity FAIL，必须激活 full two-halfwave complementary coordinates，并以该较早 instability 为控制状态；
3. 该门禁只用当前理论自身，不使用 Z FE 或 Swartz 试验荷载。

因此下一任务锁定为：

`FULL_AR2_COMPLEMENTARY_HALFWAVE_DIFFERENCE_TANGENT_GATE`。

在此 gate 完成前：

- H8→H10 的 31+ -> 18.42 MN 仍保留为 representative-sector executed warning；
- H10→H12 初步结果不升级为 production convergence decision；
- 不继续机械增加 H14；
- 不修改 M6。
