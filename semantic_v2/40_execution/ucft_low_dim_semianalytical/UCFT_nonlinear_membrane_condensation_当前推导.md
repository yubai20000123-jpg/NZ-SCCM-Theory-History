# UCFT nonlinear membrane condensation 当前推导

更新时间：2026-09-30 13:31 +08:00  
状态：M0 完成；M1（线弹性 Chen–Ji/Airy 退化）解析证明完成，通过。  
路线合同：指示词.md（本轮上传版本）。

## 1. 变量与整体几何

取
\[
0\le x\le b,\qquad 0\le y\le a_h,
\]
并定义
\[
X=\frac{\pi x}{b},\qquad Y=\frac{\pi y}{a_h},
\]
\[
Q(q)=q^2+2q_0q,\qquad C_q=\frac{\pi^2Q(q)}8.
\]

整体初始/当前构形：
\[
W_0=bq_0\sin X\sin Y,
\qquad
W=b(q_0+q)\sin X\sin Y.
\]

由 stress-free initial geometry 的 Marguerre/Kármán 增量几何：
\[
\frac12(W_{,x}^2-W_{0,x}^2)
=
C_q[1+\cos2X-\cos2Y-\cos2X\cos2Y],
\]
\[
\frac12(W_{,y}^2-W_{0,y}^2)
=
C_q\frac{b^2}{a_h^2}
[1-\cos2X+\cos2Y-\cos2X\cos2Y],
\]
\[
W_{,x}W_{,y}-W_{0,x}W_{0,y}
=
2C_q\frac{b}{a_h}\sin2X\sin2Y.
\]

因此必须满足
\[
\varepsilon_{x,yy}^0+\varepsilon_{y,xx}^0-\gamma_{xy,xy}^0
=
\frac{\pi^4Q(q)}{2a_h^2}
(\cos2X+\cos2Y).
\]

## 2. C1 最小 compatible displacement basis

不直接猜应变，而由面内位移生成：
\[
\begin{aligned}
u={}&(E_x-C_q)x
+\frac{b}{2\pi}(B_x-C_q)\sin2X\\
&+\frac{b}{2\pi}(H_x+C_q)\sin2X\cos2Y ,
\end{aligned}
\]
\[
\begin{aligned}
v={}&\left(E_y-C_q\frac{b^2}{a_h^2}\right)y
+\frac{a_h}{2\pi}
\left(B_y-C_q\frac{b^2}{a_h^2}\right)\sin2Y\\
&+\frac{a_h}{2\pi}
\left(H_y+C_q\frac{b^2}{a_h^2}\right)
\cos2X\sin2Y .
\end{aligned}
\]

这里
\[
E_x,E_y,B_x,B_y,H_x,H_y
\]
均为 inner membrane variables，不是结构级路径自由度。

与 Kármán 几何项相加后，严格得到：
\[
\boxed{
\varepsilon_x^0
=
E_x+B_x\cos2X-C_q\cos2Y+H_x\cos2X\cos2Y
}
\]
\[
\boxed{
\varepsilon_y^0
=
E_y-C_q\frac{b^2}{a_h^2}\cos2X
+B_y\cos2Y+H_y\cos2X\cos2Y
}
\]
\[
\boxed{
\gamma_{xy}^0
=
-\left(
\frac b{a_h}H_x+\frac{a_h}bH_y
\right)\sin2X\sin2Y
}
\]

## 3. compatibility 恒等验证

对上式直接微分：
\[
\varepsilon_{x,yy}^{H}
=
-\frac{4\pi^2}{a_h^2}H_x\cos2X\cos2Y,
\]
\[
\varepsilon_{y,xx}^{H}
=
-\frac{4\pi^2}{b^2}H_y\cos2X\cos2Y,
\]
\[
-\gamma_{xy,xy}^{H}
=
4\pi^2
\left(
\frac{H_x}{a_h^2}+\frac{H_y}{b^2}
\right)
\cos2X\cos2Y.
\]
三项严格相消。

剩余 particular terms 给出：
\[
\boxed{
\varepsilon_{x,yy}^0+\varepsilon_{y,xx}^0-\gamma_{xy,xy}^0
=
\frac{\pi^4Q(q)}{2a_h^2}
(\cos2X+\cos2Y)
}
\]
故 C1 对任意六个 inner variables 均严格 compatible。

符号代数独立核验亦得到：
\[
4\pi^2C_q/a_h^2\,(\cos2X+\cos2Y)
=
\pi^4Q/(2a_h^2)(\cos2X+\cos2Y).
\]

## 4. C0：Chen–Ji zero-shear 退化

取
\[
H_x=H_y=0.
\]
则
\[
\gamma_{xy}^0=0.
\]
在当前剪应力 law 满足 \(\tau_{xy}=0\) when \(\gamma_{xy}=0\) 的条件下：
\[
N_{xy}=0.
\]

C0：
\[
\varepsilon_x^0=E_x+B_x\cos2X-C_q\cos2Y,
\]
\[
\varepsilon_y^0=E_y-C_q\frac{b^2}{a_h^2}\cos2X+B_y\cos2Y.
\]

inner unknowns 仅为
\[
(E_x,E_y,B_x,B_y).
\]

## 5. C1 inner generalized residuals

设 current composite thickness integration 返回
\[
N_x(x,y),\quad N_y(x,y),\quad N_{xy}(x,y),
\]
统一采用膜力拉正；外部总轴压力 \(P>0\)。

面积域 \(\Omega=[0,b]\times[0,a_h]\)。

自由横向平均膜力：
\[
\boxed{G_{E_x}=\int_\Omega N_x\,dA=0}
\]

轴向外载功共轭：
\[
\boxed{G_{E_y}=\int_\Omega N_y\,dA+Pa_h=0}
\]

一阶 normal harmonic：
\[
\boxed{G_{B_x}=\int_\Omega N_x\cos2X\,dA=0}
\]
\[
\boxed{G_{B_y}=\int_\Omega N_y\cos2Y\,dA=0}
\]

最小 mixed/shear-compatible pair：
\[
\boxed{
G_{H_x}
=
\int_\Omega
\left[
N_x\cos2X\cos2Y
-\frac b{a_h}N_{xy}\sin2X\sin2Y
\right]dA=0
}
\]
\[
\boxed{
G_{H_y}
=
\int_\Omega
\left[
N_y\cos2X\cos2Y
-\frac{a_h}bN_{xy}\sin2X\sin2Y
\right]dA=0
}
\]

因此
\[
\boxed{
\mathbf G_m=
[G_{E_x},G_{E_y},G_{B_x},G_{B_y},G_{H_x},G_{H_y}]^T=\mathbf0.
}
\]

C0 则只求前四式，并在求解后审计：
\[
\widehat G_{H_x}
=
\int_\Omega N_x\cos2X\cos2Y\,dA,
\]
\[
\widehat G_{H_y}
=
\int_\Omega N_y\cos2X\cos2Y\,dA.
\]

## 6. M1 / Gate 1：线弹性 Chen–Ji/Airy 退化证明

Gate 1 benchmark：
- \(A^+=A^-=0\)；
- UHPC/上下钢壳全部退回线弹性；
- 上下截面对称，使纯整体曲率不产生净 membrane-bending coupling；
- 组合截面的线弹性 extensional matrix 为
\[
\mathbf A=
\begin{bmatrix}
A_{11}&A_{12}&0\\
A_{12}&A_{22}&0\\
0&0&A_{66}
\end{bmatrix}.
\]

定义
\[
\Delta_A=A_{11}A_{22}-A_{12}^2>0,
\qquad
r=b/a_h.
\]

### 6.1 C0 的四个闭式内部变量

由平均横向无外力：
\[
A_{11}E_x+A_{12}E_y=0.
\]

由平均轴向总力：
\[
b(A_{12}E_x+A_{22}E_y)+P=0.
\]

故
\[
\boxed{
E_x=\frac{PA_{12}}{b\Delta_A}
}
\]
\[
\boxed{
E_y=-\frac{PA_{11}}{b\Delta_A}
}
\]

要求 \(N_x\) 中不出现 \(\cos2X\)：
\[
A_{11}B_x-A_{12}C_qr^2=0,
\]
故
\[
\boxed{
B_x=\frac{A_{12}}{A_{11}}C_qr^2
}
\]

要求 \(N_y\) 中不出现 \(\cos2Y\)：
\[
-A_{12}C_q+A_{22}B_y=0,
\]
故
\[
\boxed{
B_y=\frac{A_{12}}{A_{22}}C_q
}
\]

### 6.2 结果膜力严格变量分离

代回可得：
\[
\boxed{
N_x
=
-\frac{\Delta_A}{A_{22}}C_q\cos2Y
}
\]
\[
\boxed{
N_y
=
-\frac Pb
-\frac{\Delta_A}{A_{11}}C_qr^2\cos2X
}
\]
\[
\boxed{N_{xy}=0}
\]

于是强式平衡逐点满足：
\[
N_{x,x}=0,\qquad N_{y,y}=0.
\]

对于均质各向同性单层：
\[
A_{11}=A_{22}=\frac{Et}{1-\nu^2},
\qquad
A_{12}=\nu A_{11},
\]
故
\[
B_x=\nu C_qr^2,\qquad B_y=\nu C_q,
\]
\[
N_x=-EtC_q\cos2Y,
\]
\[
N_y=-P/b-EtC_qr^2\cos2X,
\]
即严格恢复 Chen–Ji/Airy zero-shear 分离结构。

### 6.3 C1 中 Hx=Hy=0 是唯一弹性解

在线弹性 Gate 1 状态中，C0 解对 H-residual 的 forcing 由谐波正交性严格为零。

Hx/Hy 的弹性 generalized stiffness 为：
\[
\begin{bmatrix}
G_{H_x}\\G_{H_y}
\end{bmatrix}
=
\frac{ba_h}{4}
\begin{bmatrix}
A_{11}+A_{66}r^2 & A_{12}+A_{66}\\
A_{12}+A_{66} & A_{22}+A_{66}/r^2
\end{bmatrix}
\begin{bmatrix}
H_x\\H_y
\end{bmatrix}.
\]

对稳定线弹性 extensional law，该矩阵正定，因此：
\[
\boxed{H_x=H_y=0}
\]
为唯一解。

故 C1 自动退化为 C0，并严格恢复 Chen–Ji/Airy zero-shear 解。

## 7. Gate 状态

- M0 compatible displacement basis：PASS
- M0 compatibility identity：PASS
- M0 六个 inner residual：PASS
- M1 Gate 1：PASS（解析证明）
- M2：NOT STARTED

## 8. 发现的问题

无致命理论矛盾。

需要记录的适用边界：
Gate 1 的“严格 Chen–Ji 退化”针对线弹性、上下对称的 UCFT benchmark；若人为设置上下钢壳不同材料/厚度导致 extensional-bending coupling，则不应要求退化为对称单层 Chen–Ji 解。

## 9. NEXT_ACTION

唯一下一步：M2。

关闭 steel-local：
\[
A^+=A^-=0
\]
打开 UHPC 拉/压多项式 nonlinear active-set，分别构造 C0 和 C1 的 current composite membrane residual；先保持材料参数符号化，完成解析 active-set kernel 与 C0/C1 路径求解器接口，然后再进入具体试件参数计算。


# M2：A+=A−=0 下 UHPC nonlinear active-set 与 C0/C1 诊断

更新时间：2026-09-30 14:17 +08:00

## 10. M2 的隔离边界

本阶段严格关闭 steel-local：

[
A^+=A^-=0.
]

目标仅判断：在整体 single-q 几何 + UHPC 法向材料非线性下，C0 的 (N_{xy}=0) 是否已经产生不可忽略的 omitted mixed/shear residual。

为隔离 UHPC 非线性，本阶段上下钢壳保持对称线弹性。钢壳塑性与 (A^pm) 在 M3/M5 再打开。

UHPC 法向 current stress 使用方向性输入：

[
e_x=rac{arepsilon_x^U+
u_carepsilon_y^U}{1-
u_c^2},
qquad
e_y=rac{arepsilon_y^U+
u_carepsilon_x^U}{1-
u_c^2}.
]

## 11. UHPC 厚度 active-set 的解析形式

整体 loading-induced curvatures：

[
kappa_x=rac{pi^2q}{b}sin Xsin Y,
]

[
kappa_y=rac{pi^2bq}{a_h^2}sin Xsin Y,
]

[
kappa_{xy}=-rac{2pi^2q}{a_h}cos Xcos Y.
]

UHPC 任意厚度：

[
arepsilon_x^U=arepsilon_x^0+zkappa_x,
qquad
arepsilon_y^U=arepsilon_y^0+zkappa_y.
]

故两个方向的材料输入都严格是厚度线性式：

[
e_x=e_{xm}+chi_x z,
qquad
e_y=e_{ym}+chi_y z,
]

其中

[
e_{xm}=rac{arepsilon_x^0+
u_carepsilon_y^0}{1-
u_c^2},
qquad
chi_x=rac{kappa_x+
u_ckappa_y}{1-
u_c^2},
]

[
e_{ym}=rac{arepsilon_y^0+
u_carepsilon_x^0}{1-
u_c^2},
qquad
chi_y=rac{kappa_y+
u_ckappa_x}{1-
u_c^2}.
]

任意材料阈值 (e=e_j) 的穿越位置显式为：

[
oxed{
z_j=rac{e_j-e_m}{chi}
}
]

只保留

[
-rac{t_c}{2}<z_j<rac{t_c}{2}.
]

因此厚度方向不是 Gauss-point 状态判断，而是：求有限个根 -> 排序 -> 对每个材料区间调用对应多项式。

对任意分段多项式

[
P_j(e)=a_0+a_1e+cdots+a_ne^n,
]

定义

[
F_j(e)=a_0e+rac{a_1}{2}e^2+cdots+rac{a_n}{n+1}e^{n+1},
]

[
H_j(e)=rac{a_0}{2}e^2+rac{a_1}{3}e^3+cdots+rac{a_n}{n+2}e^{n+2}.
]

在 (z_aightarrow z_b) 上有完全闭式：

[
oxed{
N_j=
rac{F_j(e_b)-F_j(e_a)}{chi}
}
]

[
oxed{
M_j=
rac{
H_j(e_b)-H_j(e_a)
-e_m[F_j(e_b)-F_j(e_a)]
}{chi^2}
}
]

当 (chi	o0) 时取连续极限：

[
N_j=(z_b-z_a)P_j(e_m),
]

[
M_j=rac{z_b^2-z_a^2}{2}P_j(e_m).
]

这使 UHPC 厚度积分在 M2 已经完全解析。

## 12. 本轮诊断用 UHPC 多项式族

当前最高层级合同只锁定“拉、压分别为多项式；拉伸峰值约 7 MPa”，并没有冻结唯一的生产版拉伸峰值应变和软化终点。因此本轮没有偷偷继承历史约 10 MPa PCHIP，也没有把任意一条新曲线冒充成最终材料定稿。

压缩侧采用当前项目已有的六次多项式（拉应变为正）：

[
x=-rac e{arepsilon_{c0}},
]

[
oxed{
P_c(e)=
-f_c(A_cx+B_cx^5+C_cx^6)
}
]

[
A_c=rac{E_carepsilon_{c0}}{f_c}=1.07654145996,
]

[
B_c=6-5A_c=0.61729270021,
]

[
C_c=4A_c-5=-0.69383416017.
]

第一峰后零应力根：

[
x_z=1.35286765,
qquad
e_z=-0.00473504.
]

当 (e<e_z) 时本轮取零应力区。

拉伸侧构造一个不用于拟合试件、只用于 M2 鲁棒性门槛的多项式族。固定：

[
f_t=7.0 {m MPa}.
]

令：

[
r_t=rac{E_carepsilon_{tp}}{f_t},
qquad
t=rac e{arepsilon_{tp}}.
]

峰前：

[
oxed{
P_{t1}(e)
=
f_t
left[
r_tt+(3-2r_t)t^2+(r_t-2)t^3
ight]
}
]

它严格满足：

[
P_{t1}(0)=0,quad P'_{t1}(0)=E_c,
]

[
P_{t1}(arepsilon_{tp})=f_t,quad
P'_{t1}(arepsilon_{tp})=0.
]

峰后令

[
s=rac{e-arepsilon_{tp}}{arepsilon_{tu}-arepsilon_{tp}},
]

[
oxed{
P_{t2}(e)=f_t(1-3s^2+2s^3)
}
]

并在 (egearepsilon_{tu}) 取零拉应力。

诊断采用三组故意拉开的参数，不作为试件拟合：

1. (r_t=1.5, arepsilon_{tu}/arepsilon_{tp}=2)
2. (r_t=2.0, arepsilon_{tu}/arepsilon_{tp}=5)
3. (r_t=3.0, arepsilon_{tu}/arepsilon_{tp}=10)

用它们判断 C0/C1 结论是否依赖某一条任意拉伸曲线。

## 13. M2 新发现并修正：q 方程必须包含外载虚功

M0 的 compatible displacement basis 在加载边 (y=a_h) 给出：

[
oxed{
v(x,a_h)=a_hleft(E_y-C_qrac{b^2}{a_h^2}ight)
}
]

因为 (sin 2Y=0) 于 (Y=pi)。

所以在固定 inner variables 时：

[
rac{partial v(x,a_h)}{partial q}
=
-a_hrac{b^2}{a_h^2}C_q',
]

[
oxed{
C_q'=rac{pi^2}{4}(q+q_0).
}
]

当前符号约定为膜力拉正、总轴压力 (P>0)。(G_{E_y}) 已经采用

[
G_{E_y}=int_Omega N_y,dA+Pa_h=0.
]

因此 q 虚位移对应的外力虚功为

[
delta W_{m ext}
=
P a_hrac{b^2}{a_h^2}C_q',delta q.
]

故正式 q 残量必须是：

[
oxed{
egin{aligned}
R_q={}&
int_Omega
Big[
N_xarepsilon^0_{x,q}
+N_yarepsilon^0_{y,q}
+N_{xy}gamma^0_{xy,q}
\
&qquad
+M_xkappa_{x,q}
+M_ykappa_{y,q}
+M_{xy}kappa_{xy,q}
Big],dA
\
&-
P a_hrac{b^2}{a_h^2}C_q'
=0.
end{aligned}
}
]

其中在固定 inner variables 下：

[
arepsilon^0_{x,q}=-C_q'cos2Y,
]

[
arepsilon^0_{y,q}=-C_q'rac{b^2}{a_h^2}cos2X,
]

[
gamma^0_{xy,q}=0,
]

[
kappa_{x,q}=rac{pi^2}{b}sin Xsin Y,
]

[
kappa_{y,q}=rac{pi^2b}{a_h^2}sin Xsin Y,
]

[
kappa_{xy,q}=-rac{2pi^2}{a_h}cos Xcos Y.
]

这一项不是新路线，而是同一 compatible coordinates 下不可删除的 external virtual work。

### 13.1 为什么这一修正是必要而不是可选

在线弹性 C0 中，均匀轴压力只出现在 (N_y) 的常数项。若错误删除外载 q 虚功，由于

[
int_0^bcos2X,dx=0,
]

均匀 (P) 对内部 q 虚功的贡献会消失，(R_q) 在线弹性极限甚至不能正确建立 (P-q) 稳定关系。

保留外载项后，线弹性 C0 可严格写成：

[
K_b q
+
rac{ba_h}{2}C_qC_q'
left(
K_x+K_yrac{b^4}{a_h^4}
ight)
-
P a_hrac{b^2}{a_h^2}C_q'
=0,
]

从而：

[
oxed{
P(q)
=
P_{cr}rac{q}{q+q_0}
+
C_Aleft(q^2+2q_0qight)
}
]

其中 (P_{cr}) 和 (C_A) 均由当前线弹性 (A/D) 刚度解析给出。

也就是说，修正后的 q 方程严格恢复既有经典 imperfect-postbuckling 结构；这一结果反过来验证了外载虚功项的必要性。

M0 的 compatible basis、compatibility identity 和 Gate 1 membrane condensation 本身不受这一修正影响，因为此前 Gate 1 尚未使用 q 外平衡来求路径。

## 14. M2 数值诊断实现边界

正式理论 residual 仍然由上面的连续面积积分定义。

本轮为了在 M4 完成完整面内解析 moving-boundary 之前检查 C0/C1 是否需要 (N_{xy}) 通道，使用高阶 Gauss-Legendre X-Y 求积作为独立数值 evaluator；UHPC 厚度方向仍按第 11 节完全解析分区积分。

因此本轮面积求积只属于 M2 diagnostic verification，不构成生产理论定义。

代表对象采用 BH050 的一个整体代表半波：

[
b=a_h=2500 {m mm},
quad
q_0=0.0025,
]

[
t_c=42 {m mm},
quad
t_s=4 {m mm}.
]

为隔离 UHPC nonlinear membrane effect，steel-local 保持关闭、上下钢壳保持线弹性对称。

C0 给定 q 后求：

[
(E_x,E_y,B_x,B_y)
]

的四式：

[
G_{E_x}=G_{B_x}=G_{B_y}=R_q=0,
]

而

[
P=-rac1{a_h}int_Omega N_y,dA
]

由 (G_{E_y}=0) 直接消元。

C1 同理求：

[
(E_x,E_y,B_x,B_y,H_x,H_y)
]

的六式：

[
G_{E_x}=G_{B_x}=G_{B_y}=G_{H_x}=G_{H_y}=R_q=0.
]

## 15. 中央诊断材料族的 C0/C1 路径结果

中央诊断采用：

[
f_t=7.0 {m MPa},
quad
r_t=2,
quad
arepsilon_{tu}/arepsilon_{tp}=5.
]

此时

[
arepsilon_{tp}=0.00032258.
]

q 从 0 连续算至 0.02，41 个状态，全部得到 connected root。

代表状态：

| q | P_C0 / MN | P_C1 / MN | (C1-C0)/C0 | omitted (eta_H) | Hx | Hy |
|---:|---:|---:|---:|---:|---:|---:|
|0.002|8.710935|8.710136|-0.00917%|0.000635|2.361e-6|-1.046e-6|
|0.005|13.140127|13.135579|-0.03461%|0.002280|1.360e-5|-5.867e-6|
|0.010|16.365869|16.363093|-0.01696%|0.004400|3.498e-5|-1.501e-5|
|0.015|18.620862|18.626914|+0.03250%|0.004893|4.691e-5|-2.099e-5|
|0.020|20.747051|20.757001|+0.04796%|0.003904|4.362e-5|-2.088e-5|

这里

[
oxed{
eta_H=
rac{
sqrt{widehat G_{H_x}^2+widehat G_{H_y}^2}
}{
|P|a_h
}
}
]

只用于 C0 omitted-channel 审计。

中央材料族全过程：

[
max |P_{C1}/P_{C0}-1|
=
0.04821%.
]

[
max eta_H
=
0.004939
=
0.4939%.
]

因此 UHPC 法向材料非线性确实产生非零 mixed/shear-compatible generalized forcing，但它对当前 A=0 总轴力路径的影响非常小。

## 16. active-set 实际分区

中央材料族 C0 的 UHPC 体积分区显示：

q=0.005 时，x 方向有效材料输入：
- tension ascending: 70.13%
- compression: 20.48%
- tension softening: 9.39%

y 方向：
- compression: 100%

q=0.010 时，x 方向：
- compression: 33.91%
- tension ascending: 40.25%
- tension softening: 25.84%

y 方向：
- compression: 100%

q=0.020 时，x 方向：
- compression: 41.60%
- tension ascending: 14.74%
- tension softening: 36.59%
- zero-tension tail: 7.06%

y 方向：
- compression: 99.75%
- tension ascending: 0.25%

这说明 M2 并非处在“全域同一材料分支”的伪简单状态；解析 active-set 实际跨越了拉、压、拉伸软化和零拉应力区，而 C0/C1 的 P 路径仍然几乎重合。

## 17. 拉伸多项式鲁棒性诊断

三组故意拉开的 7 MPa 多项式族结果：

| rt | eps_tu/eps_tp | max |dP_C1-C0| / P | max eta_H | P_C0(q=.02) / MN | P_C1(q=.02) / MN |
|---:|---:|---:|---:|---:|---:|
|1.5|2|0.10898%|0.004807|20.63841|20.64274|
|2.0|5|0.04785%|0.004938|20.74793|20.75785|
|3.0|10|0.03063%|0.004103|20.89586|20.90226|

因此结论不依赖某一条任意选定的 7 MPa 拉伸多项式：

[
oxed{
	ext{UHPC 材料非线性单独存在时，C1 shear-compatible 通道会被激活，
但对总 P(q) 的影响在本轮诊断中低于约 0.11%。}
}
]

注意：这不等价于现在就把 (N_{xy}) 永久删除。

在相关 q 区间，(H_x/C_q) 可达到约 0.22，说明 mixed compatible strain correction 在应变场层面并非严格为零；而 M3 打开 qA/A² steel-local mixed harmonics 后，可能显著放大该通道。

所以当前决策是：

[
oxed{
	ext{C0 可以作为 A=0 时的高精度低成本 reduced model，
但最终是否锁定 }N_{xy}=0	ext{ 必须等 M3。}
}
]

## 18. X-Y 数值 evaluator 的独立收敛检查

正式 residual 并不由 Gauss 点定义；本表只检查本轮 diagnostic evaluator。

8×8 与 12×12 对比：

- q=0.005：P_C0 差 -0.00011%，P_C1 差 +0.00011%
- q=0.010：P_C0 差 +0.00019%，P_C1 差 +0.00039%
- q=0.020：P_C0 差 -0.00287%，P_C1 差 -0.00265%

omitted residual 的相对变化在 q=0.02 约 1.04%，但其绝对量本身仅约 0.39% 的 (Pa_h)。

一次 16×16 全路径收敛复核尝试在当前执行环境 60 s 限时内被中止，没有把未完成结果作为证据，也没有改变任何理论结论。

## 19. 求解成本

当前未优化 Python diagnostic backend，12×12 X-Y evaluator、厚度解析 active-set：

- C0：平均约 0.39 s / q 点
- C1：平均约 0.54 s / q 点
- continuation 下每点通常 3 次 residual/Jacobian function-step level 收敛，最大 4 次 nonlinear solve evaluations 级别记录（SciPy nfev）。

中央 41 点路径总量仍是几十秒量级。

这进一步确认当前瓶颈是 repeated active-set / area evaluation，而不是 4×4 与 6×6 小矩阵求解。

## 20. M2 Gate 结论

- q->0：(B_x,B_y,H_x,H_y	o0)：PASS
- q->P connected branch：PASS（诊断多项式族均连续）
- C0 omitted mixed/shear residual：非零但 <0.5% (Pa_h) 量级
- C1 vs C0 P-path：三组拉伸多项式族最大差 <0.11%
- UHPC active-set：实际进入 tension/compression/tension-softening 多区，非假性单区结果
- production (N_{xy}=0) 决策：DEFER TO M3

因此：

[
oxed{
mathrm{M2}=mathrm{PASS at modelmbox{-}class/diagnostic level}.
}
]

生产版 UHPC 拉伸多项式的精确参数仍未在 M2 冒充冻结；M4 将完成正式材料分段与面内解析 moving-boundary 集成。

## 21. NEXT_ACTION

严格进入 M3：

[
A^+
eq0,qquad A^-
eq0.
]

先不增加任何额外 membrane modes。

必须从现有 whole-face multiwave steel-local 几何完整展开 qA 与 A² 的 mixed-harmonic 频谱，对 C0/C1 当前 basis 计算 omitted generalized residual spectrum；只有显著频率才允许激活对应 compatible ((H_{x,kl},H_{y,kl})) pair。
