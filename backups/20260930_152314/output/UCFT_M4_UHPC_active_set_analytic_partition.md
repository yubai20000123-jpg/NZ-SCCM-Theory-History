# UCFT M4 — UHPC 拉压 polynomial active-set 的 production 面内解析分区

更新时间：2026-09-30 15:23 +08:00

状态：M0/M1/M2/M3 已完成；本文件完成 M4。

---

## 1. M4 的任务边界

M4 不改变结构级变量：

\[
q=\text{continuation parameter},\qquad
(P,A^+,A^-)=\text{给定 }q\text{ 后的外层未知}.
\]

M4 只关闭 UHPC current directional normal law 的解析积分接口：

\[
e_x=
\frac{\varepsilon_x^U+\nu_c\varepsilon_y^U}{1-\nu_c^2},
\qquad
e_y=
\frac{\varepsilon_y^U+\nu_c\varepsilon_x^U}{1-\nu_c^2}.
\]

厚度 active-set 在 M2 已闭式；本轮完成：

\[
\boxed{
\text{显式面内 active boundaries}
\rightarrow
\text{解析 }Y\text{ 积分}
\rightarrow
\text{仅保留一个 }X\text{ 向确定积分}
}
\]

二维/三维 Gauss 不进入 production residual。

本轮没有冻结一条并不存在于最新合同中的任意 UHPC tensile peak strain / softening endpoint。当前材料合同只锁定 tensile peak 约 7 MPa 量级；因此 production kernel 接受“已锁定的有限阶分段 polynomial coefficients + thresholds”作为材料输入。数值一致性核验临时调用 M2 central diagnostic family，只验证积分算法，不把该 family 升级为生产材料参数。

---

## 2. C1 下 UHPC directional strain 的固定-\(X\) 形式

令

\[
X=\frac{\pi x}b,\qquad
Y=\frac{\pi y}{a_h},\qquad
r=\frac b{a_h},\qquad
D_\nu=1-\nu_c^2,
\]

\[
C_q=\frac{\pi^2}{8}(q^2+2q_0q).
\]

C1：

\[
\varepsilon_x^0
=
E_x+B_x\cos2X-C_q\cos2Y+H_x\cos2X\cos2Y,
\]

\[
\varepsilon_y^0
=
E_y-C_qr^2\cos2X+B_y\cos2Y+H_y\cos2X\cos2Y.
\]

整体曲率：

\[
\kappa_x
=
\frac{\pi^2q}b\sin X\sin Y,
\]

\[
\kappa_y
=
\frac{\pi^2q}b r^2\sin X\sin Y.
\]

于是 \(x\) 向 directional material input 的中面部分是

\[
\boxed{
e_{xm}
=
\frac{
E_x+\nu_cE_y
+
(B_x-\nu_cC_qr^2)\cos2X
+
[-C_q+\nu_cB_y+(H_x+\nu_cH_y)\cos2X]\cos2Y
}{D_\nu}
}
\]

且厚度斜率

\[
\boxed{
\chi_x
=
\frac{\pi^2q}b
\frac{1+\nu_cr^2}{D_\nu}
\sin X\sin Y.
}
\]

\(y\) 向为

\[
\boxed{
e_{ym}
=
\frac{
E_y+\nu_cE_x
+
(-C_qr^2+\nu_cB_x)\cos2X
+
[B_y-\nu_cC_q+(H_y+\nu_cH_x)\cos2X]\cos2Y
}{D_\nu}
}
\]

\[
\boxed{
\chi_y
=
\frac{\pi^2q}b
\frac{r^2+\nu_c}{D_\nu}
\sin X\sin Y.
}
\]

UHPC 顶、底面：

\[
e_x^\pm=e_{xm}\pm\frac{t_c}2\chi_x,
\qquad
e_y^\pm=e_{ym}\pm\frac{t_c}2\chi_y.
\]

---

## 3. 为什么面内材料边界必然是二次方程

在固定 \(X\) 后令

\[
s=\sin Y,\qquad 0\le s\le1,
\]

且

\[
\cos2Y=1-2s^2.
\]

因此任一方向、任一厚度表面的材料输入严格具有：

\[
\boxed{
e^\pm(X,s)
=
A(X)+B(X)+C^\pm(X)s-2B(X)s^2.
}
\]

这里 \(A,B,C^\pm\) 只是上一节显式公式按 \(X\) 收集后的代数系数，不是新结构变量。

对任一材料阈值 \(e_j\)：

\[
e^\pm=e_j
\]

严格化为

\[
\boxed{
-2B\,s^2+C^\pm s+A+B-e_j=0.
}
\]

若 \(B\neq0\)：

\[
\boxed{
s_{j,\pm}^{(1,2)}
=
\frac{
C^\pm
\pm
\sqrt{(C^\pm)^2+8B(A+B-e_j)}
}{4B}.
}
\]

若 \(B=0,\ C^\pm\neq0\)：

\[
\boxed{
s_j=\frac{e_j-A}{C^\pm}.
}
\]

只保留

\[
0<s_j<1.
\]

每个有效根自动对应关于 \(Y=\pi/2\) 对称的两条边界：

\[
\boxed{
Y_j^{L}=\arcsin s_j,
\qquad
Y_j^{R}=\pi-\arcsin s_j.
}
\]

因此 M4 不需要在 \(Y\) 方向逐点判定材料状态。

---

## 4. 厚度 active-set：显式排序与全局原函数严格等价

当前材料阈值按拉应变为正排列为

\[
e_z<0<e_{tp}<e_{tu}.
\]

其物理分区为：

\[
e\le e_z:\quad \sigma=0,
\]

\[
e_z<e<0:\quad \sigma=P_c(e),
\]

\[
0\le e<e_{tp}:\quad \sigma=P_{t1}(e),
\]

\[
e_{tp}\le e<e_{tu}:\quad \sigma=P_{t2}(e),
\]

\[
e\ge e_{tu}:\quad \sigma=0.
\]

传统显式 active-set 对每个阈值求：

\[
z_j=\frac{e_j-e_m}\chi,
\]

筛选

\[
-\frac{t_c}2<z_j<\frac{t_c}2,
\]

再与 \(-t_c/2,+t_c/2\) 一起排序。

M4 同时构造连续的全局累计原函数：

\[
\mathcal F'(e)=\sigma(e),
\qquad
\mathcal H'(e)=e\sigma(e).
\]

其中：

\[
\mathcal F(e)=0,\qquad \mathcal H(e)=0,
\quad e\le e_z,
\]

\[
\mathcal F(e)=F_c(e)-F_c(e_z),
\quad
\mathcal H(e)=H_c(e)-H_c(e_z),
\quad e_z<e<0,
\]

\[
\mathcal F(e)=F_c(0)-F_c(e_z)+F_{t1}(e)-F_{t1}(0),
\]

\[
\mathcal H(e)=H_c(0)-H_c(e_z)+H_{t1}(e)-H_{t1}(0),
\quad 0\le e<e_{tp},
\]

\[
\begin{aligned}
\mathcal F(e)={}&
F_c(0)-F_c(e_z)
+F_{t1}(e_{tp})-F_{t1}(0)\\
&+F_{t2}(e)-F_{t2}(e_{tp}),
\end{aligned}
\]

\[
\begin{aligned}
\mathcal H(e)={}&
H_c(0)-H_c(e_z)
+H_{t1}(e_{tp})-H_{t1}(0)\\
&+H_{t2}(e)-H_{t2}(e_{tp}),
\end{aligned}
\]

\[
e_{tp}\le e<e_{tu},
\]

而 \(e\ge e_{tu}\) 后 \(\mathcal F,\mathcal H\) 保持在 \(e_{tu}\) 的常值。

于是无需在 production evaluator 中反复把各厚度段重新相加：

\[
\boxed{
N^U
=
\frac{
\mathcal F(e^+)-\mathcal F(e^-)
}\chi
}
\]

\[
\boxed{
M^U
=
\frac{
\mathcal H(e^+)-\mathcal H(e^-)
-e_m[\mathcal F(e^+)-\mathcal F(e^-)]
}{\chi^2}.
}
\]

这两个式子与“求全部 \(z_j\rightarrow排序\rightarrow逐段原函数积分”严格代数等价。

当 \(\chi\to0\)：

\[
\boxed{
N^U\to t_c\sigma(e_m),
\qquad
M^U\to0.
}
\]

因此 \(q\to0\) 时不存在数值 \(0/0\) 的理论缺口。

---

## 5. 当前压缩六次 polynomial 的显式原函数

当前 compression branch：

\[
P_c(e)
=
E_ce
+
\frac{f_cB_c}{\varepsilon_{c0}^5}e^5
-
\frac{f_cC_c}{\varepsilon_{c0}^6}e^6,
\]

其中

\[
B_c
=
6-\frac{5E_c\varepsilon_{c0}}{f_c},
\qquad
C_c
=
\frac{4E_c\varepsilon_{c0}}{f_c}-5.
\]

因此：

\[
\boxed{
F_c(e)
=
\frac{E_c}2e^2
+
\frac{f_cB_c}{6\varepsilon_{c0}^5}e^6
-
\frac{f_cC_c}{7\varepsilon_{c0}^6}e^7
}
\]

\[
\boxed{
H_c(e)
=
\frac{E_c}3e^3
+
\frac{f_cB_c}{7\varepsilon_{c0}^5}e^7
-
\frac{f_cC_c}{8\varepsilon_{c0}^6}e^8.
}
\]

对于任一 cubic tensile branch

\[
P_t(e)
=
a_0+a_1e+a_2e^2+a_3e^3,
\]

其 production primitive 不需要数值积分：

\[
\boxed{
F_t(e)
=
a_0e+\frac{a_1}2e^2+\frac{a_2}3e^3+\frac{a_3}4e^4
}
\]

\[
\boxed{
H_t(e)
=
\frac{a_0}2e^2+\frac{a_1}3e^3+\frac{a_2}4e^4+\frac{a_3}5e^5.
}
\]

若最终 tensile branch 采用其他有限阶 polynomial，只改变有限个系数和最高次数，不改变本 M4 的 active boundary 与积分结构。

---

## 6. 固定 \(X\) 后，完整 \(Y\) 积分是初等闭式

在任一由材料边界切开的 \(s\)-区间内：

- \(e^+(s)\) 与 \(e^-(s)\) 已固定属于各自 polynomial branch；
- \(\mathcal F(e^\pm)\)、\(\mathcal H(e^\pm)\) 因而都是 \(s\) 的有限多项式；
- \(\chi=\chi_0(X)s\)。

当前最高阶来自 compression branch，因此：

\[
\boxed{
N^U(s)
=
n_{-1}s^{-1}
+n_0
+n_1s
+n_2s^2
+n_3s^3
+n_4s^4
+n_5s^5
+n_6s^6
+n_7s^7
+n_8s^8
+n_9s^9
+n_{10}s^{10}
+n_{11}s^{11}
+n_{12}s^{12}
+n_{13}s^{13}.
}
\]

\[
\boxed{
\begin{aligned}
M^U(s)
={}&
m_{-2}s^{-2}
+m_{-1}s^{-1}
+m_0
+m_1s
+m_2s^2
+m_3s^3
+m_4s^4\\
&+m_5s^5
+m_6s^6
+m_7s^7
+m_8s^8
+m_9s^9
+m_{10}s^{10}
+m_{11}s^{11}\\
&+m_{12}s^{12}
+m_{13}s^{13}
+m_{14}s^{14}.
\end{aligned}
}
\]

这里 \(n_i,m_i\) 是当前状态下由上节原函数直接展开得到的代数系数，不是新的物理自由度。

利用

\[
dY=\frac{ds}{\sqrt{1-s^2}}
\]

只需以下有限 primitive family：

\[
J_{-2}(s)
=
-\frac{\sqrt{1-s^2}}s,
\]

\[
J_{-1}(s)
=
\ln\left(
\frac{s}{1+\sqrt{1-s^2}}
\right),
\]

\[
J_0(s)=\arcsin s,
\]

\[
J_1(s)=-\sqrt{1-s^2},
\]

\[
\boxed{
J_n(s)
=
-\frac{s^{n-1}\sqrt{1-s^2}}n
+
\frac{n-1}nJ_{n-2}(s),
\qquad n\ge2.
}
\]

因此：

\[
\int N^U dY,\qquad
\int N^U\cos2Y\,dY,\qquad
\int M^U\sin Y\,dY
\]

在每个 active interval 都完全解析。

其中：

\[
\cos2Y=1-2s^2.
\]

所以 \(\cos2Y\) 权重只把 \(J_n\) 变为

\[
J_n-2J_{n+2},
\]

而 \(\sin Y\) 权重只变为

\[
J_{n+1}.
\]

这一步已经把原先二维 \(X-Y\) material-state integration 严格降到只剩 \(X\) 一个积分变量。

---

## 7. production residual 的一维形式

物理面积：

\[
dx\,dy
=
\frac{ba_h}{\pi^2}dX\,dY.
\]

对每个固定 \(X\)，先由上一节得到六个解析 \(Y\)-moment：

\[
\int_0^\pi N_x^U\,dY,
\quad
\int_0^\pi N_x^U\cos2Y\,dY,
\quad
\int_0^\pi M_x^U\sin Y\,dY,
\]

\[
\int_0^\pi N_y^U\,dY,
\quad
\int_0^\pi N_y^U\cos2Y\,dY,
\quad
\int_0^\pi M_y^U\sin Y\,dY.
\]

于是 UHPC normal 部分：

\[
\boxed{
G_{E_x}^U
=
\frac{ba_h}{\pi^2}
\int_0^\pi
\left[
\int_0^\pi N_x^U\,dY
\right]dX
}
\]

\[
\boxed{
G_{E_y}^U
=
\frac{ba_h}{\pi^2}
\int_0^\pi
\left[
\int_0^\pi N_y^U\,dY
\right]dX
}
\]

\[
\boxed{
G_{B_x}^U
=
\frac{ba_h}{\pi^2}
\int_0^\pi
\cos2X
\left[
\int_0^\pi N_x^U\,dY
\right]dX
}
\]

\[
\boxed{
G_{B_y}^U
=
\frac{ba_h}{\pi^2}
\int_0^\pi
\left[
\int_0^\pi N_y^U\cos2Y\,dY
\right]dX
}
\]

\[
\boxed{
G_{H_x,\mathrm{normal}}^U
=
\frac{ba_h}{\pi^2}
\int_0^\pi
\cos2X
\left[
\int_0^\pi N_x^U\cos2Y\,dY
\right]dX
}
\]

\[
\boxed{
G_{H_y,\mathrm{normal}}^U
=
\frac{ba_h}{\pi^2}
\int_0^\pi
\cos2X
\left[
\int_0^\pi N_y^U\cos2Y\,dY
\right]dX.
}
\]

UHPC normal 对 \(R_q\) 的贡献为：

\[
\boxed{
\begin{aligned}
R_{q,U}^{normal}
={}&
-\frac{ba_h}{\pi^2}C_q'
\int_0^\pi
\left[
\int_0^\pi N_x^U\cos2Y\,dY
\right]dX
\\
&-
\frac{ba_h}{\pi^2}C_q'r^2
\int_0^\pi
\cos2X
\left[
\int_0^\pi N_y^U\,dY
\right]dX
\\
&+
a_h
\int_0^\pi
\sin X
\left[
\int_0^\pi M_x^U\sin Y\,dY
+
r^2
\int_0^\pi M_y^U\sin Y\,dY
\right]dX.
\end{aligned}
}
\]

其中：

\[
C_q'=\frac{\pi^2}4(q+q_0).
\]

因此 production normal residual 已严格成为：

\[
\boxed{\text{analytic }z + \text{analytic }Y + \text{one deterministic }X\text{ integral}}.
\]

---

## 8. UHPC shear channel 不需要 active-set

当前方向性 UHPC operator 的 shear branch 保持：

\[
G_c=\frac{E_c}{2(1+\nu_c)},
\]

\[
\tau_{xy}^U
=
G_c(\gamma_{xy}^0+z\kappa_{xy}).
\]

所以：

\[
\boxed{
N_{xy}^U=G_ct_c\gamma_{xy}^0
}
\]

\[
\boxed{
M_{xy}^U
=
G_c\frac{t_c^3}{12}\kappa_{xy}.
}
\]

C1：

\[
\gamma_{xy}^0
=
-\left(
rH_x+\frac1rH_y
\right)\sin2X\sin2Y.
\]

因此 shear 部分的两个 \(H\)-residual 甚至不需要保留一维积分：

\[
\boxed{
G_{H_x,\mathrm{shear}}^U
=
\frac{ba_h}4G_ct_c
(r^2H_x+H_y)
}
\]

\[
\boxed{
G_{H_y,\mathrm{shear}}^U
=
\frac{ba_h}4G_ct_c
\left(H_x+\frac{H_y}{r^2}\right).
}
\]

同时：

\[
\kappa_{xy}
=
-\frac{2\pi^2q}{a_h}\cos X\cos Y,
\]

所以 \(q\) 虚功中的 UHPC twisting contribution 也是闭式：

\[
\boxed{
R_{q,U}^{twist}
=
G_c\frac{t_c^3\pi^4qb}{12a_h}.
}
\]

因此完整 UHPC C1 模块没有隐藏二维材料积分。

---

## 9. UHPC 轴向分项的恢复

UHPC 原始 axial contribution：

\[
\boxed{
P_c
=
-\frac1{a_h}
\int_\Omega N_y^U\,dA
=
-\frac b{\pi^2}
\int_0^\pi
\left[
\int_0^\pi N_y^U\,dY
\right]dX.
}
\]

PBL/web reaction correction 仍只作用于报告量：

\[
\boxed{
P_c^*=\chi_wP_c.
}
\]

它不反向进入 M4 active-set，不制造新的 \(q,A^\pm\) 或 membrane variable。

---

## 10. 独立一致性核验

### 10.1 厚度：全局累计原函数 vs 显式 \(z_j\) 排序

验证状态：

\[
q=0.005,\ 0.010,\ 0.015,\ 0.020,
\]

每个状态：

- \(x,y\) 两方向；
- 9 个确定 \(X\)；
- 11 个确定 \(Y\)；
- 总计 792 个方向-空间状态；
- 使用 M2 central tensile family 仅作为数值 benchmark。

最大相对差：

\[
\boxed{1.722e-08}.
\]

这证明 cumulative primitive 并没有改变 active-set physics；只是把已经显式定义的分段积分做了严格代数凝聚。

### 10.2 面内：解析 \(Y\)+一维 \(X\) vs 80×120 二维 Gauss diagnostic

同样取 C1 的：

\[
q=0.005,\ 0.010,\ 0.015,\ 0.020.
\]

比较八个面积积分：

\[
\int N_x\,dA,
\quad
\int N_y\,dA,
\quad
\int N_x\cos2X\,dA,
\quad
\int N_y\cos2Y\,dA,
\]

\[
\int N_x\cos2X\cos2Y\,dA,
\quad
\int N_y\cos2X\cos2Y\,dA,
\]

\[
\int M_x\sin X\sin Y\,dA,
\quad
\int M_y\sin X\sin Y\,dA.
\]

最大相对差：

\[
\boxed{2.720e-07}
\]

平均相对差：

\[
\boxed{2.269e-08}.
\]

80×120 Gauss 这里只是独立 benchmark；production 仍由解析 \(Y\) active partition + 单一 \(X\) integral 定义。

---

## 11. 一个可人工复算的材料边界例子

仅作 M4 算法核验，取 M2 central diagnostic family、BH050 representative half-wave 的 C1 状态：

\[
q=0.010.
\]

在：

\[
X=\frac\pi2
\]

时，\(x\) directional top face 得到：

零应力边界：

\[
s=0.0149328712,
\]

\[
Y_L=0.0149334262,\qquad
Y_R=3.1266592274.
\]

tension-peak 边界：

\[
s=0.2909096675,
\]

\[
Y_L=0.2951774891,\qquad
Y_R=2.8464151645.
\]

这些值直接来自第 3 节二次方程，没有空间 Gauss 点。

该状态的 \(y\) directional field 全部保持 compression branch，因此没有内部 \(Y\)-boundary。

---

## 12. M4 裁决

\[
\boxed{\mathrm{M4\ analytic\ active\mbox{-}set\ kernel}=\mathrm{PASS}}
\]

本轮完成了：

\[
\boxed{
z\text{ 向：闭式}
\quad+\quad
Y\text{ 向：显式 moving-boundary + 初等闭式}
\quad+\quad
X\text{ 向：唯一低维确定积分}.
}
\]

没有发现需要改变 single-\(q\) / \(A^+,A^-\) 路线的矛盾。

唯一仍未冻结的是 UHPC tensile polynomial 的具体材料数值输入：

\[
e_{tp},\quad e_{tu},\quad
P_{t1}\text{ coefficients},\quad
P_{t2}\text{ coefficients}.
\]

这不是 M4 数学缺口，因为 M4 kernel 对任意已锁定的有限阶 piecewise polynomial 原样工作；当前项目只明确锁定 tensile peak \(\sim7\) MPa，不能把 M2 的 diagnostic family 偷偷升级成正式材料参数。

该输入在进入 M8 九试件正式数值路径前必须冻结，但不阻塞 M5 steel material operator 的推导。

---

## 13. NEXT_ACTION

严格进入 M5：

\[
\boxed{
\text{steel Mises deformation theory}
+
\text{equivalent uniaxial polynomial}
+
E_{sec}/E_{tan}
+
\text{analytic elastic/plastic thickness active-set}
}
\]

要求保持：

\[
\varepsilon_i^2
=
C_2\zeta^2+C_1\zeta+C_0,
\]

使屈服边界

\[
\varepsilon_i=\varepsilon_y
\]

继续只由二次方程解析求根，并明确区分：

\[
\text{finite current stress}
\neq
\text{tangent used by Newton/Jacobian}.
\]
