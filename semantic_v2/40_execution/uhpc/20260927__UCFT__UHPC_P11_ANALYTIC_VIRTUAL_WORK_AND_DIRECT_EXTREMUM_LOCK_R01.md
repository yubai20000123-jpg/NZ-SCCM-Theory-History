# UCFT / UHPC P11 解析虚功与直接极值体系锁定稿 R01
日期：2026-09-27

## 1. 理论状态
当前结构状态仍锁定为 10 个量：
[
mathbf z=[ararepsilon_x,U_{10},U_{11},ararepsilon_y,V_{01},V_{11},q,A^+,A^-,P]^T.
]
给定路径参数 (lambda) 时，平衡系统为 10 元：
[
mathbf F(mathbf z,lambda)=0.
]
此前出现的 21 元形式仅是引入路径灵敏度 (mathbf s=dmathbf z/dlambda) 的 bordered 数值实现，不是增加结构自由度。直接极值最简形式为 11 个未知量 ((mathbf z,lambda))：
[
mathbf F(mathbf z,lambda)=0,
]
[
g(mathbf z,lambda)=mathbf e_P^Tmathbf J^{-1}mathbf F_{,lambda}=0,
quad
mathbf J=partialmathbf F/partialmathbf z.
]

## 2. UHPC P11 单一 epsilon-only 本构
定义 (x=arepsilon/0.0035)，采用
[
rac{sigma_U}{141.1}
=
0.4486639433x
+1.1994315643x^2
+0.6665051179x^3
-1.2484183266x^4
-1.1317439450x^5
+0.7948135172x^6
+0.6534300091x^7
-0.4050081603x^8
-0.1276279131x^9
+0.1189092524x^{10}
-0.02031542207x^{11}.
]
当前结构计算定义域：(-0.0035learepsilonle0.0070)。
导数严格因式化，整个定义域仅有两个驻点，保持“拉伸软化—拉峰—原点—压峰—压缩软化”的单调拓扑。
当前峰值约：拉伸 -7.291 MPa at -0.000995；压缩 134.13 MPa at 0.003623（相对 UC141 的 141.1 MPa 保守约 4.9%）。原点切线约 18.09 GPa，低于 UC141 的 43.4 GPa，必须作为峰前刚度审计项。

## 3. 一阶 U2 几何场
[
X=pi x/b,quad Y=pi y/a_h,quad Q=q^2+2q_0q.
]
[
W=b(q_0+q)sin Xsin Y,qquad W_0=bq_0sin Xsin Y.
]
[
u=left(ararepsilon_x-rac{pi^2Q}{8}ight)x+rac{b}{2pi}U_{10}sin2X+rac{b}{2pi}U_{11}sin2Xcos2Y,
]
[
v=left(ararepsilon_y-rac{pi^2b^2Q}{8a_h^2}ight)y+rac{a_h}{2pi}V_{01}sin2Y+rac{a_h}{2pi}V_{11}cos2Xsin2Y.
]
中面应变、剪应变与曲率均为有限 Fourier 多项式；厚度应变对 z 仅一次。

## 4. UHPC 厚度解析积分
令任一法向有效应变
[
eta(z)=e+chi z,
quad
sigma_U(eta)=sum_{n=1}^{11}a_neta^n,
quad
a_n=f_cc_n/arepsilon_{cp}^n.
]
则
[
N(e,chi)=int_{-t/2}^{t/2}sigma_U(e+chi z),dz,
quad
M(e,chi)=int_{-t/2}^{t/2}zsigma_U(e+chi z),dz
]
均通过二项式展开和
[
int_{-t/2}^{t/2}z^{2r+1}dz=0,qquad
int_{-t/2}^{t/2}z^{2r}dz=rac{t^{2r+1}}{2^{2r}(2r+1)}
]
完全化成有限多项式，无厚度 Gauss 点。

## 5. 非线性剪切解析化
当前 secant shear 定义：
[
G_U=rac{1}{4(1+
u_c)}
left[rac{sigma_U(eta_x)}{eta_x}+rac{sigma_U(eta_y)}{eta_y}ight].
]
因 P11 无常数项，
[
rac{sigma_U(eta)}{eta}
=
sum_{n=1}^{11}a_neta^{n-1},
]
所以 (G_U) 是 P10 多项式，剪切虚功的厚度积分同样解析。

## 6. 七个 UHPC 虚功残量
保留：
[
R_{ararepsilon_x}^U, R_{U10}^U, R_{U11}^U, R_{ararepsilon_y}^U, R_{V01}^U, R_{V11}^U, R_q^U.
]
其二维 integrand 均只含有限 Fourier 乘积。利用
[
int_0^pisin^{2m}Xcos^{2n}X,dX
=
rac{Gamma(m+1/2)Gamma(n+1/2)}{Gamma(m+n+1)}
]
及奇对称项为零，可将 x-y 面积积分完全解析。A+、A- 不进入 UHPC 位移场，UHPC 对这两个局部残量贡献为 0。

## 7. Jacobian 不使用数值差分
P11 导数：
[
sigma'_U(eta)=
f_cleft[
rac{c_1}{arepsilon_p}
+rac{2c_2}{arepsilon_p^2}eta+cdots+
rac{11c_{11}}{arepsilon_p^{11}}eta^{10}
ight].
]
二阶导数：
[
sigma''_U(eta)=
f_cleft[
rac{2c_2}{arepsilon_p^2}
+rac{6c_3}{arepsilon_p^3}eta+cdots+
rac{110c_{11}}{arepsilon_p^{11}}eta^9
ight].
]
因此所有 (K_{ij}^U=partial R_i^U/partial r_j) 仍按相同的 z 幂矩 + x-y Fourier 解析积分生成，不需要有限差分或 Gauss 采样。

## 8. 已完成数值独立校核
P31 阶段已对 7 个 UHPC 残量使用“解析 Fourier-多项式后端”与独立三维 Gauss 积分做双后端核验，相对差均约 1e-13；P11 保持同一代数结构且阶数更低。代表性 P11 截面状态 e=0.002, kappa=2e-5 /mm, t=42 mm：
N_exact=3575.789725139095 N/mm，与数值积分差 9.1e-13；
M_exact=6468.357078306244 N，与数值积分差 3.6e-12。

## 9. 当前边界
UHPC 模块已视为 current-state 解析模块，可进入整板直接极值系统。后续主要未锁定项是 steel-local current-state 塑性闭合及其验证；在钢壳闭合之前，不重新调整 UHPC P11 以追逐整板误差。
