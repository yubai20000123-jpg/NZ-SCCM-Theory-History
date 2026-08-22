# NZ-SCCM — Panel 1 / 14 / 21 来源波形 → 当前显式结构 → 二维材料约束诊断

**Time:** 2026-08-22 17:51 +08:00  
**Status:** `EXECUTED / SOURCE_WAVEFORM_EXOGENOUS / GENERALIZED_EXPLICIT_STRUCTURE_PASS / CURRENT_1D_CAPACITY_RERUN_PASS / FULL_2D_PU_NOT_PROMOTED / MATERIAL-SECTION-KINEMATIC_OMISSION_IDENTIFIED`

## 0. 本轮目的与边界

本轮按用户最新目标执行：

> 不预测这些非常规鼓包；把来源中已经出现的波形作为外部给定几何输入，送入当前显式计算路径，观察结构需求和二维材料状态，从而反向检查当前材料约束选择遗漏了什么。

因此：

```text
SELF_GROWN_WAVEFORM = OFF
TANGENT_MODE_GATE_AS_CURRENT_PRIORITY = OFF
FIT_WAVEFORM_TO_Pf = PROHIBITED
MATERIAL_RETUNING = OFF
CURRENT_EXPLICIT_METHOD = RETAINED
```

试验 `Pf` 只在理论根和材料状态冻结之后用于比较。

本轮采用 Nguyen Fig.5.7a / 5.8a / 5.6a 的 Panel 1 / 14 / 21 FE buckled-shape surfaces 作为三种代表性**来源波形代理**。必须强调：扫描图没有面外位移数值轴，因此只能恢复**归一化形状**，不能恢复真实初始缺陷幅值。初始缺陷幅值仍保持当前统一 `q0=b/400`，本轮只改变“形状”，不同时反标幅值。

---

# 1. 三条来源波形的有限解析恢复

沿加载方向定义

\[
u=y/a,\qquad 0\le u\le1,
\]

并固定横向形状仍为 `sin(pi x/b)`。扫描图的 9 个纵向网格站 `u=0,1/8,...,1` 被人工数字化并归一化。数字化点只用于恢复几何形状，不是正式结构积分点。

有限正弦拟合后：

### Panel 1

\[
\boxed{
\Phi_1(u)=
1.04276809\sin\pi u
-0.09582984\sin2\pi u
+0.08299371\sin3\pi u
}
\]

9点归一化 RMSE ≈ `0.0111`。

### Panel 14

\[
\boxed{
\Phi_{14}(u)=
1.05654776\sin\pi u
-0.03901107\sin2\pi u
+0.06242867\sin3\pi u
}
\]

RMSE ≈ `0.0149`。

### Panel 21

\[
\boxed{
\Phi_{21}(u)=
-0.12203066\sin\pi u
-0.76471804\sin2\pi u
+0.18158893\sin3\pi u
+0.25675995\sin4\pi u
}
\]

RMSE ≈ `0.0218`。该有限式保留了可见的两个不等幅反向鼓包：第一主瓣归一化约 `-1`，第二主瓣约 `+0.84`。

三条函数均严格满足

\[
\Phi(0)=\Phi(1)=0,
\]

所以不会像直接写任意非整数 `sin(pi y/ell)` 那样破坏端部简支条件。

---

# 2. 当前显式方法推广到“给定有限波形”后仍保持同一低维形式

定义

\[
\psi(x,y)=\sin\frac{\pi x}{b}\,\Phi(y),
\]

\[
w_i=bq_0\psi,\qquad w=bq\psi.
\]

注意：`Phi` 的系数在计算前已经由来源波形固定，不是新的结构未知量。

定义三个精确波形矩：

\[
I_0=\int_0^a\Phi^2dy,
\qquad
I_1=\int_0^a(\Phi')^2dy,
\qquad
I_2=\int_0^a(\Phi'')^2dy.
\]

由于 `Phi` 是有限正弦和，这些积分由正交性直接成为有限代数和，不使用空间数值积分。

新的弹性项为

\[
\boxed{
P_{cr,\Phi}=b\,
\frac{D_x\alpha^4I_0+2H\alpha^2I_1+D_yI_2}{I_1}
}
\]

其中 `alpha=pi/b`。

对任意该类 `Phi`，Marguerre 兼容源精确写成

\[
\boxed{
\mathcal G
=b^2q(q+2q_0)\frac{\alpha^2}{2}
\left[
(\Phi'^2+\Phi\Phi'')
+\cos(2\alpha x)(\Phi'^2-\Phi\Phi'')
\right]
}
\]

`Phi'^2 ± Phi Phi''` 仍是有限 cosine 和，因此 Airy 特解仍是有限解析和。精确 Fourier 正交求和后，面外平衡继续保持原来的函数结构：

\[
\boxed{
P_\Phi(q)=
P_{cr,\Phi}\frac{q}{q+q_0}
+C_\Phi q(q+2q_0)
}
\]

没有增加 Ritz 自由度，没有空间 Gauss/Simpson，没有材料点。

代码首先用纯 `m=1` 与纯 `m=2` 正弦回代，精确复现当前旧公式的 `Pcr,C`，作为 generalized-wave operator 的退化门禁。

---

# 3. 三块板的来源波形显式系数

|Panel|Pcr,Phi / kN|C,Phi / kN|
|---:|---:|---:|
|1|1513.15494|1,509,873.179|
|14|2795.78863|1,765,103.761|
|21|478.90611|657,684.459|

这些系数只由来源归一化波形、板几何和当前冻结刚度生成；`Pf` 未进入。

---

# 4. 先通过当前 1D 截面容量路径：三板都可以计算

保持当前 RC 显式 `N-M_y` 容量：Nguyen 型抛物线压缩上升支、相体积扣除、纵向钢筋 elastic-perfectly-plastic，零截面数值积分。

把旧单正弦的局部需求替换为来源 `Phi` 对应的精确 `N_y(x,y;q),M_y(x,y;q)` 后，三块板均得到有限正根。

|Panel|source-wave q_u|控制 s|控制 u=y/a|控制 y / mm|source-wave 1D Pu / kN|Pf / kN|误差|
|---:|---:|---:|---:|---:|---:|---:|---:|
|1|0.001913942|1|0.761718|1858.6|**676.103**|490.194|**+37.926%**|
|14|0.000882066|1|0.749850|1829.6|**738.319**|716.164|**+3.094%**|
|21|0.004265235|1|0.373485|911.3|**327.924**|368.313|**−10.966%**|

对照端点敏感性：

|Panel|旧 m=2 1D / kN|纯 m=1 / kN|来源有限波形 / kN|
|---:|---:|---:|---:|
|1|567.712|689.055|**676.103**|
|14|657.813|740.998|**738.319**|
|21|350.460|496.701|**327.924**|

读取：

- Panel14 在来源波形下，单纯结构+1D材料容量已经只高约 `3.1%`；
- Panel1 则变成显著高估 `37.9%`；
- Panel21 仍低估约 `11.0%`。

因此来源波形并不是统一“修正系数”，也不能据此调整一个全局材料参数。

---

# 5. 来源波形暴露的完整板内力：当前材料接口此前只消费了其中一部分

对于一般 `Phi(y)`，新增挠曲的弯矩结果量为

\[
\boxed{
M_x=bq\sin(\alpha x)
\left[D_x\alpha^2\Phi-D_\mu\Phi''\right]
}
\]

\[
\boxed{
M_y=bq\sin(\alpha x)
\left[D_\mu\alpha^2\Phi-D_y\Phi''\right]
}
\]

\[
\boxed{
M_{xy}=-2D_{66}bq\alpha\cos(\alpha x)\Phi'
}
\]

而一般有限 `Phi` 的 Airy 场还产生

\[
N_{xy}\neq0
\]

于非对称线位置。

三块板在当前 1D 控制点处：

|Panel|Nx / N/mm|Ny / N/mm|Nxy|Mx / N|My / N|Mxy|abs(Mx/My)|
|---:|---:|---:|---:|---:|---:|---:|---:|
|1|+3.939|−550.458|≈0|+448.947|+273.227|≈0|**1.643**|
|14|+1.069|−603.859|≈0|+366.730|+189.238|≈0|**1.938**|
|21|+27.971|−241.043|≈0|−563.289|−837.262|≈0|**0.673**|

`Nxy,Mxy≈0` 仅因为三块的当前最小根都落在横向中心 `s=1`。在整板上按同一解析 `Phi` 检查，峰值约为：

|Panel|max abs(Nxy) / N/mm|max abs(Mxy) / N|
|---:|---:|---:|
|1|0.762|288.8|
|14|0.210|195.7|
|21|6.829|467.1|

最重要的不是小量 `Nxy`，而是：

\[
\boxed{M_x\text{ 与 }M_y\text{ 同量级，Panel1/14 甚至 }|M_x|>|M_y|.}
\]

---

# 6. 这直接暴露当前 TC-R2 截面约束的一个维度缺失

当前 TC-R2 compact section reduction 使用

\[
\lambda_t(z)=\lambda_{t0}+\nu_c\chi z,
\qquad
\lambda_c(z)=\lambda_{c0}+\chi z.
\]

这组特殊化意味着物理横向应变通过厚度保持常数，只有一个独立弯曲斜率；它非常适合旧的

\[
N_x + N_y + M_y
\]

截面化处理。

但来源波形结构场明确给出独立的

\[
\kappa_x\neq0,\qquad\kappa_y\neq0,
\]

也就是同时存在 `Mx` 与 `My`。因此完整 bonded plane-stress 材料坐标通过厚度应当至少允许

\[
\boxed{
\lambda_t(z)=a_t+b_tz,
\qquad
\lambda_c(z)=a_c+b_cz
}
\]

其中 `b_t,b_c` 为两个独立斜率，而不能预先锁成

\[
b_t=\nu_c\chi,\qquad b_c=\chi.
\]

这不是修改 TC-R2 材料定律；它是释放当前**截面运动学/材料约束接口**中被省掉的横向弯曲维度。

所以本轮真正发现的是：

\[
\boxed{
\text{此前所谓 RC 2D 材料检查，本质上更接近“2D membrane + 1D bending”，}
}
\]

而不是一般波形下完整的 biaxial bending material state。

---

# 7. 用完整来源波形运动学直接看厚度材料状态：遗漏在 Panel21 最明显

为了不在发现接口缺口后继续造一个不一致的“最终 2D Pu”，本轮只做同源运动学状态诊断：

1. 用解析 Airy `N` 通过 `A^{-1}` 得到中面应变；
2. 用来源 `Phi` 的 `kappa_x,kappa_y` 得到厚度线性应变；
3. 转成当前 NC plane-stress material coordinates；
4. 不进行材料参数拟合，不把这个诊断冒充最终 phase-compatible 2D re-cut。

当前材料坐标：

\[
\lambda_t=
\frac{\varepsilon_x+\nu\varepsilon_y}
{\varepsilon_0(1-\nu^2)},
\qquad
\lambda_c=
\frac{\varepsilon_y+\nu\varepsilon_x}
{\varepsilon_0(1-\nu^2)}.
\]

三块板的当前 tensile cracking 坐标都约为

\[
x_{cr}=\frac{f_t}{E_0\varepsilon_0}\approx0.05.
\]

### Panel 1

厚度三点（两面+中面）的 `lambda_t,lambda_c` 约为：

\[
(-0.0897,-0.5238),
\quad
(+0.0018,-0.4682),
\quad
(+0.0933,-0.4125).
\]

所以厚度状态跨越：

\[
\boxed{CC\rightarrow TC}
\]

而拉侧 `lambda_t≈0.0933>xcr≈0.05`，已进入 tensile post-cracking/stiffening 侧；但尚远小于 `10/17`，当前 TC-R2 compression-softening 尚未启动。

### Panel 14

\[
(-0.0629,-0.5509),
\quad
(-0.0064,-0.5208),
\quad
(+0.0502,-0.4906).
\]

同样是：

\[
\boxed{CC\rightarrow TC}
\]

但拉侧恰好处于 `lambda_t≈xcr` 附近。这与其来源波形下 1D 结果只高约 3.1% 是一个很有价值的状态参照，但不据此拟合材料。

### Panel 21

\[
(-0.1849,-0.5949),
\quad
(+0.0287,-0.2774),
\quad
(+0.2424,+0.0402).
\]

厚度状态直接跨越：

\[
\boxed{CC\rightarrow TC\rightarrow TT}
\]

这意味着 Panel21 的来源波形把一个截面同时推入三种二维材料象限；旧的“TC 一条截面化修正”不可能完整表示这个状态拓扑。

---

# 8. 为什么本轮没有继续报一个“来源波形 2D Pu”

执行确实已经把三条来源波形送到了当前显式结构—材料接口；正是在这里发现现有材料截面化约束不够一般。

如果此时继续沿用旧 TC-R2 的单斜率厚度场求一个数字，就会主动丢掉刚刚由来源波形产生的 `Mx`，并对 Panel21 丢掉 `TT-CC` 共存。这样的数值不再是“当前来源波形真实进入二维材料路径”的结果。

所以正式停止点是：

```text
SOURCE_WAVEFORM_TO_GENERALIZED_EXPLICIT_STRUCTURE = PASS
SOURCE_WAVEFORM_TO_CURRENT_1D_CAPACITY = PASS
FULL_RESULTANT_RECOVERY_Mx_My_Mxy = PASS
CURRENT_TC_R2_ONE-SLOPE_SECTION_INTERFACE = FAIL_FOR_GENERAL_WAVEFORM
FINAL_SOURCE_WAVEFORM_FULL_2D_Pu = NOT_PROMOTED
```

这是理论接口门禁失败，不是求解器数值失败。

---

# 9. 对材料约束选择的第一轮反推结论

本轮没有证据要求重写 NC 单轴压缩 backbone，也没有证据要求调整 `alpha1,alpha2` 或 `gamma_c`。

首先暴露的是**材料约束空间选择本身**：

1. 不能只检查 `Nx + Ny + My`；
2. 一般来源波形必须允许 `Mx + My` 同时进入厚度状态；
3. Panel21 还要求完整 `TT/TC/CC` 象限共存，而非只建立 TC correction；
4. `Mxy/Nxy` 在控制中心为零，但整板可非零；它们应在下一层检查中保留，不能先验删除；
5. 因此下一步应先把当前 NC 二维 material current operator 接口扩成**两个独立 affine thickness slopes**，再用同一三条来源波形重新求 phase-compatible 2D 极限；材料函数本身先不改。

这正是来源波形诊断的目的：先把结构几何误差拿掉，再识别材料约束选择中被隐藏的自由度。

---

# 10. Decision

```text
PANEL1_14_21_SOURCE_WAVEFORM_DIGITIZATION = EXECUTED
WAVEFORM_COEFFICIENTS_FIT_TO_Pf = FALSE
WAVEFORM_AMPLITUDE_BACKFIT = FALSE
GENERALIZED_FINITE_WAVE_EXPLICIT_OPERATOR = PASS
PANEL1_SOURCE_WAVE_1D_Pu = 676.103 kN
PANEL14_SOURCE_WAVE_1D_Pu = 738.319 kN
PANEL21_SOURCE_WAVE_1D_Pu = 327.924 kN
PANEL1_ERROR_VS_Pf = +37.926%
PANEL14_ERROR_VS_Pf = +3.094%
PANEL21_ERROR_VS_Pf = -10.966%
FULL_BENDING_RESULTANTS_EXPOSED = Mx + My + Mxy
CURRENT_RC_2D_SECTION_IDENTITY = 2D_MEMBRANE_PLUS_1D_BENDING_APPROXIMATION
PRIMARY_OMITTED_DIMENSION = INDEPENDENT_TRANSVERSE_BENDING_CURVATURE
PANEL21_REQUIRED_STATE_FAMILY = TT + TC + CC
MATERIAL_LAW_RETUNING = NO
NEXT_RC_TASK = TWO-INDEPENDENT-AFFINE-SLOPE_PHASE-COMPATIBLE_2D_SECTION_RERUN_ON_PANELS_1_14_21
```

Reproduction script:

`semantic_v2/40_execution/rc/20260822_1751__NZSCCM__PANEL1_14_21_SOURCE_WAVEFORM_EXPLICIT_DIAGNOSTIC.py`
