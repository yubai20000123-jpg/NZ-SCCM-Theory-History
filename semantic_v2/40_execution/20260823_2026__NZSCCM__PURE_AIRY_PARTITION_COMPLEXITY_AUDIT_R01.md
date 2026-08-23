# NZ-SCCM — 纯 Airy 分区复杂度审计 R01

**Time:** 2026-08-23 20:26 +08:00  
**Status:** `AIRY_FORCE_PARTITION = PASS_STRONG / FACE_COMPONENT_STRAIN_FRONTS = PASS_EXPLICIT_CONIC / TRUE_MATERIAL_PARTITION = OPEN-HARD / REGIONWISE_INDEPENDENT_EQUILIBRIUM = REJECT / NO_Pu`

## 0. 本轮目的与边界

只审计一个问题：在当前锁定的单正弦 Marguerre–Airy 代表半波中，`Nx, Ny, Mx, My` 以及上下表面应变零线是否能被显式求出，并据此判断受力分区是否有限、规则、可积。

本轮：

- 不计算 `Pu`；
- 不修改 Airy / Zhou；
- 不调用 full-domain current material；
- 不做 CC/TC/TT 材料求解；
- 不以数值积分代替理论结论。

定义

\[
X=\alpha x\in[0,\pi],\qquad Y=\beta y\in[0,\pi],
\]

\[
Q=q(q+2q_0)>0.
\]

当前单正弦 Airy 场：

\[
N_x=-G_xQ\cos 2Y,
\qquad
G_x=\frac{\alpha^2b^2\Delta_A}{8A_{22}},
\]

\[
N_y=-\frac{P(q)}b-G_yQ\cos 2X,
\qquad
G_y=\frac{\beta^2b^2\Delta_A}{8A_{11}},
\]

\[
N_{xy}=0.
\]

弯矩：

\[
M_x=J_x q\sin X\sin Y,
\qquad
J_x=b(D_x\alpha^2+D_\mu\beta^2),
\]

\[
M_y=J_y q\sin X\sin Y,
\qquad
J_y=b(D_\mu\alpha^2+D_y\beta^2).
\]

当前 RC 域内 `Jx>0, Jy>0`。

---

## 1. `Nx=0`：固定、规则、与 q 无关

\[
N_x=0\iff \cos 2Y=0.
\]

故内部零线恒为

\[
\boxed{Y=\frac\pi4,\ \frac{3\pi}4}
\]

即

\[
\boxed{y=\frac\ell4,\ \frac{3\ell}4}.
\]

因此 `Nx` 将完整半波固定分成三条横向带。这个分区不随 `q` 移动。

---

## 2. `Ny=0`：最多两条对称竖线，且拓扑只有一次可能变化

写

\[
\eta(q)=\frac{P(q)}{bG_yQ}>0.
\]

则

\[
N_y=0\iff \cos2X=-\eta(q).
\]

因此：

- `eta>1`：无内部 `Ny=0` 线，`Ny<0` 全域；
- `eta=1`：只在 `X=pi/2` 相切；
- `0<eta<1`：有两条对称零线

\[
\boxed{
X_1=\frac12\arccos[-\eta(q)],
\qquad
X_2=\pi-X_1
}
\]

即

\[
\boxed{
x_1=\frac{b}{2\pi}\arccos[-\eta(q)],\qquad x_2=b-x_1.}
\]

代入当前显式后屈曲

\[
P(q)=P_{cr}\frac{q}{q+q_0}+CQ
\]

可得

\[
\boxed{
\eta(q)=
\frac{P_{cr}}{bG_y(q+q_0)(q+2q_0)}
+\frac{C}{bG_y}.
}
\]

故 `eta(q)` 单调下降，并趋于 `C/(bGy)`。于是 `Ny` 分区拓扑至多只发生一次变化：从“全域压缩”变为“中部一条 Ny 拉力带 + 两侧压缩带”。若 `C/(bGy)>=1`，则这种变化永不发生。

若 `C/(bGy)<1`，临界 `q_N` 满足

\[
(q_N+q_0)(q_N+2q_0)
=\frac{P_{cr}}{bG_y-C},
\]

即

\[
\boxed{
q_N=\frac{-3q_0+\sqrt{q_0^2+4P_{cr}/(bG_y-C)}}{2}
}
\]

（仅在右端为正且物理可达时有效）。

---

## 3. `Mx=0` 与 `My=0`：当前单正弦半波内没有内部符号分区

因为

\[
\sin X>0,\qquad \sin Y>0
\]

在开域 `(0,pi)x(0,pi)` 内均成立，而当前 `Jx,Jy>0`，故

\[
\boxed{M_x>0,\qquad M_y>0}
\]

遍及完整代表半波内部。

`Mx=0`、`My=0` 只出现在物理边界 `x=0,b` 或 `y=0,ell`。

因此，若只用 `Nx,Ny,Mx,My` 符号做“受力分区”，真正产生内部边界的只有 `Nx` 与 `Ny`。

### 纯 resultant 分区上限

- `Nx`：3 横带；
- `Ny`：1 或 3 竖带；

因此当前单正弦半波最多得到

\[
\boxed{3\times 3=9}
\]

个矩形小区，且所有边界都与坐标轴平行。

这部分对零数值积分非常友好：任何有限三角多项式在这些区域上的积分都仍是普通有限三角矩。

---

## 4. 补充：`Mxy` 若纳入，也仍是规则直线分区

当前

\[
M_{xy}=-2D_{66}bq\alpha\beta\cos X\cos Y.
\]

内部零线为

\[
\boxed{X=\frac\pi2\quad\text{或}\quad Y=\frac\pi2}.
\]

仍然只是中线，不破坏矩形/正交分区性质。

---

## 5. 上下表面法向应变零线：不是任意隐式曲线，而是显式二次曲线

由膜柔度

\[
\varepsilon_x^0=\frac{A_{22}N_x-A_{12}N_y}{\Delta_A},
\qquad
\varepsilon_y^0=\frac{-A_{12}N_x+A_{11}N_y}{\Delta_A},
\]

得到

\[
\varepsilon_x^0=
\frac{A_{12}P}{b\Delta_A}
+\frac{A_{12}\beta^2b^2Q}{8A_{11}}\cos2X
-\frac{\alpha^2b^2Q}{8}\cos2Y,
\]

\[
\varepsilon_y^0=
-\frac{A_{11}P}{b\Delta_A}
-\frac{\beta^2b^2Q}{8}\cos2X
+\frac{A_{12}\alpha^2b^2Q}{8A_{22}}\cos2Y.
\]

曲率

\[
\kappa_x=bq\alpha^2\sin X\sin Y,
\qquad
\kappa_y=bq\beta^2\sin X\sin Y.
\]

对上下表面 `z=zeta=±h`：

\[
\varepsilon_x^\zeta=\varepsilon_x^0+\zeta\kappa_x,
\qquad
\varepsilon_y^\zeta=\varepsilon_y^0+\zeta\kappa_y.
\]

令

\[
u=\sin X\in[0,1],\qquad v=\sin Y\in[0,1],\]

利用 `cos2X=1-2u^2`, `cos2Y=1-2v^2`，四条法向表面零线统一变成

\[
\boxed{C+A u^2+B v^2+\zeta Luv=0.}
\]

因此它们都是 `(u,v)` 第一象限单位方形中的二次曲线（conic），而不是未知复杂前沿。

例如 `eps_x^zeta=0`：

\[
A_x=-\frac{A_{12}\beta^2b^2Q}{4A_{11}},
\qquad
B_x=\frac{\alpha^2b^2Q}{4},
\qquad
L_x=bq\alpha^2,
\]

\[
C_x=
\frac{A_{12}P}{b\Delta_A}
+Q\left(
\frac{A_{12}\beta^2b^2}{8A_{11}}
-\frac{\alpha^2b^2}{8}
\right).
\]

故若 `Bx!=0`，边界可以显式写成

\[
\boxed{
v(u)=
\frac{-\zeta L_xu\pm
\sqrt{(L_x^2-4A_xB_x)u^2-4B_xC_x}}
{2B_x}.}
\]

`eps_y^zeta=0` 完全同型。

结论：**上下表面分量应变零线是有限、对称、显式可定位的代数曲线。**

---

## 6. 但这里出现第一处真正的“不可直接宣布成功”

虽然表面分量应变零线是 conic，但把它作为积分边界后，`x,y -> u,v` 的面积元为

\[
\boxed{
dxdy=\frac{dudv}{\alpha\beta\sqrt{1-u^2}\sqrt{1-v^2}}.}
\]

因此即使边界 `v=v(u)` 只有一个平方根，区域积分也一般会出现

- `arcsin`；
- 根式嵌套；
- 椭圆型积分；

而不再自动属于现有 D15 的矩形有限三角矩族。

所以：

\[
\boxed{
\text{face-strain front 显式}
\not\Rightarrow
\text{区域积分仍是简单 D15 exact moment}.
}
\]

---

## 7. 更关键：真正 CC/TC/TT 的边界不是 `eps_x=0` 或 `eps_y=0`

若存在表面剪切，则

\[
\gamma_{xy}^{\zeta}
=\zeta\kappa_{xy},
\qquad
\kappa_{xy}=-2bq\alpha\beta\cos X\cos Y.
\]

二维主应变状态的零边界满足

\[
\det\mathbf E^\zeta
=
\varepsilon_x^\zeta\varepsilon_y^\zeta
-\left(\frac{\gamma_{xy}^\zeta}{2}\right)^2
=0.
\]

因为 `eps_x^zeta, eps_y^zeta` 各为 `(u,v)` 二次式，而

\[
(\gamma_{xy}^\zeta/2)^2
\propto(1-u^2)(1-v^2),
\]

故真实主应变符号前沿为

\[
\boxed{F_4(u,v;q)=0}
\]

的四次代数曲线。

它仍然是“有限、代数、由 Airy 状态确定”的，但已经不再是简单的矩形边界或单个 conic。

因此：

```text
AIRY KNOWS TRUE MATERIAL-STATE FRONT = YES, IN PRINCIPLE
TRUE MATERIAL-STATE FRONT = ALGEBRAIC QUARTIC, GENERICALLY
SIMPLE RECTANGULAR PARTITION = NO
D15-READY BY INSPECTION = NO
```

---

## 8. “按每个分区各自建立独立平衡方程”在力学上不成立

Airy 已经逐点满足膜平衡：

\[
N_{x,x}+N_{xy,y}=0,
\qquad
N_{xy,x}+N_{y,y}=0.
\]

把区域切成 `Omega_r` 后，任一区域只会得到同一恒等式的积分形式

\[
\int_{\partial\Omega_r}\mathbf N\mathbf n\,ds=0.
\]

这不会产生新的独立结构自由度。

所以若对每个分区再人为建立一个独立 `R_r=0`，有很高风险只是重复平衡或人为过约束。

**可接受的力学形式**是：区域只负责选择不同的 constitutive/capacity expression，最后所有区域贡献回到同一个全局/同一模态虚功平衡：

\[
\boxed{R_q=\sum_r R_q^{(r)}=0.}
\]

而不是

\[
R_q^{(1)}=R_q^{(2)}=\cdots=0.
\]

---

## 9. 本轮最终裁决

### A. 纯 Airy resultant 受力分区

\[
\boxed{PASS\_STRONG}
\]

原因：

- `Nx=0` 为两条固定横线；
- `Ny=0` 为 0/1-touch/2 条对称竖线；
- `Mx,My` 无内部零线；
- 若纳入 `Mxy`，也只增加两条中线；
- 纯 resultant 分区最多 9 个坐标矩形（不计 Mxy 再细分）；
- 对有限三角项保持直接 exact integrability。

### B. 上下表面分量应变零线

\[
\boxed{PASS\_EXPLICIT\_CONIC}
\]

它们确实可显式求出，且是有限二次曲线。

### C. 真实 CC/TC/TT 主应变分区

\[
\boxed{OPEN\_HARD}
\]

Airy 确实能确定其边界，但一般为四次代数曲线；这并没有自动解决零空间积分问题。

### D. 每个受力区建立一个独立平衡方程

\[
\boxed{REJECT}
\]

Airy 已经满足局部膜平衡；独立区域平衡不会自然产生新的合法结构方程。

### E. 当前值得继续的唯一版本

\[
\boxed{
\text{Airy explicit region fronts}
\rightarrow
\text{fixed branch expression per region}
\rightarrow
\text{regional analytic contribution}
\rightarrow
\sum_rR_q^{(r)}=0.
}
\]

但在进入材料之前，下一门禁必须只回答：**对 conic / quartic Airy-defined boundaries，所需区域积分能否被压缩成有限可审计解析对象；若不能，则该猜想不能解决原 full-domain current-material 死胡同。**

本轮不计算 Pu，不修改当前 production state。
