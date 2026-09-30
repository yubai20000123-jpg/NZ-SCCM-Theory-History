# UCFT nonlinear membrane condensation 当前推导

**状态时间：2026-09-30 13:31 +08:00**  
**路线合同：用户上传《指示词.md》为最高优先级。**  
**当前任务：M0、M1 已完成；M2 已完成解析激活判据和独立数值核验，正式 Gate 2 仍待半解析 active-set 面积分替换核验积分。**

---

## 1. 锁定对象

\[
0\le x\le b,\qquad 0\le y\le a_h,
\]

\[
X=\frac{\pi x}{b},\qquad Y=\frac{\pi y}{a_h}.
\]

整体 stress-free 初始构形：

\[
W_0=bq_0\sin X\sin Y,
\]

当前整体构形：

\[
W=b(q_0+q)\sin X\sin Y.
\]

定义仅用于书写的显式量：

\[
Q(q)=q^2+2q_0q,
\qquad
C_q=\frac{\pi^2Q(q)}8.
\]

其中 \(q\) 是整体路径参数，\(q_0\) 是无应力初始几何缺陷。

---

## 2. 整体 Kármán 几何增量

\[
\frac12\left(W_{,x}^2-W_{0,x}^2\right)
=
C_q
\left[
1+\cos2X-\cos2Y-\cos2X\cos2Y
\right],
\]

\[
\frac12\left(W_{,y}^2-W_{0,y}^2\right)
=
C_q\frac{b^2}{a_h^2}
\left[
1-\cos2X+\cos2Y-\cos2X\cos2Y
\right],
\]

\[
W_{,x}W_{,y}-W_{0,x}W_{0,y}
=
2C_q\frac b{a_h}\sin2X\sin2Y.
\]

因此：

\[
\boxed{
\varepsilon_{x,yy}^0+
\varepsilon_{y,xx}^0-
\gamma_{xy,xy}^0
=
\frac{\pi^4Q(q)}{2a_h^2}
\left(\cos2X+\cos2Y\right)
}
\]

该式不预设 \(N_{xy}=0\)。

---

## 3. C1 最小 compatible displacement basis

定义：

\[
\boxed{
\begin{aligned}
u(x,y)
={}&
(E_x-C_q)x
+\frac{b}{2\pi}(B_x-C_q)\sin2X\\
&+\frac{b}{2\pi}(C_q+H_x)\sin2X\cos2Y ,
\end{aligned}}
\]

\[
\boxed{
\begin{aligned}
v(x,y)
={}&
\left(E_y-C_q\frac{b^2}{a_h^2}\right)y
+\frac{a_h}{2\pi}
\left(B_y-C_q\frac{b^2}{a_h^2}\right)\sin2Y\\
&+\frac{a_h}{2\pi}
\left(C_q\frac{b^2}{a_h^2}+H_y\right)
\cos2X\sin2Y .
\end{aligned}}
\]

\(E_x,E_y,B_x,B_y,H_x,H_y\) 都是 inner membrane coefficients，不是结构路径自由度。

代入 Kármán 应变后严格得到：

\[
\boxed{
\varepsilon_x^0
=
E_x+B_x\cos2X-C_q\cos2Y
+H_x\cos2X\cos2Y
}
\]

\[
\boxed{
\varepsilon_y^0
=
E_y-C_q\frac{b^2}{a_h^2}\cos2X
+B_y\cos2Y
+H_y\cos2X\cos2Y
}
\]

\[
\boxed{
\gamma_{xy}^0
=
-\left(
\frac b{a_h}H_x+\frac{a_h}bH_y
\right)
\sin2X\sin2Y
}
\]

---

## 4. compatibility identity

\(E_x,E_y\) 对兼容源无贡献；\(B_x\cos2X\) 对 \(y\) 二阶导数为零；\(B_y\cos2Y\) 对 \(x\) 二阶导数为零。

特解部分：

\[
\frac{\partial^2}{\partial y^2}(-C_q\cos2Y)
=
\frac{\pi^4Q}{2a_h^2}\cos2Y,
\]

\[
\frac{\partial^2}{\partial x^2}
\left(-C_q\frac{b^2}{a_h^2}\cos2X\right)
=
\frac{\pi^4Q}{2a_h^2}\cos2X.
\]

对 \(H_x,H_y\)：

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
\frac{H_x}{a_h^2}+
\frac{H_y}{b^2}
\right)\cos2X\cos2Y.
\]

三者严格相消。

因此上述 C1 场对任意六个 inner coefficients 都严格满足当前 \(q\) 的 Kármán/Marguerre compatibility。

---

## 5. C0：Chen–Ji zero-shear 退化

令：

\[
H_x=H_y=0,
\]

则：

\[
\gamma_{xy}^0=0.
\]

C0 中面应变：

\[
\boxed{
\varepsilon_x^0
=
E_x+B_x\cos2X-C_q\cos2Y
}
\]

\[
\boxed{
\varepsilon_y^0
=
E_y-C_q\frac{b^2}{a_h^2}\cos2X+B_y\cos2Y
}
\]

并在 C0 中明确设：

\[
N_{xy}=0.
\]

inner variables 为：

\[
(E_x,E_y,B_x,B_y).
\]

---

## 6. C0/C1 inner generalized residual

设：

\[
\Omega=[0,b]\times[0,a_h].
\]

横向无外加总膜力：

\[
\boxed{
G_{E_x}
=
\int_\Omega N_x\,dA=0
}
\]

轴向压力 \(P>0\)、膜力拉正：

\[
\boxed{
G_{E_y}
=
\int_\Omega N_y\,dA+Pa_h=0
}
\]

\[
\boxed{
G_{B_x}
=
\int_\Omega N_x\cos2X\,dA=0
}
\]

\[
\boxed{
G_{B_y}
=
\int_\Omega N_y\cos2Y\,dA=0
}
\]

C1 再增加：

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
-\frac{a_h}{b}N_{xy}\sin2X\sin2Y
\right]dA=0
}
\]

因此：

\[
\mathbf G_{C0}
=
(G_{E_x},G_{E_y},G_{B_x},G_{B_y})^T=\mathbf0
\]

和

\[
\mathbf G_{C1}
=
(G_{E_x},G_{E_y},G_{B_x},G_{B_y},G_{H_x},G_{H_y})^T
=\mathbf0.
\]

C0 求根后仍必须计算：

\[
\widehat G_{H_x}
=
\int_\Omega N_x\cos2X\cos2Y\,dA,
\]

\[
\widehat G_{H_y}
=
\int_\Omega N_y\cos2X\cos2Y\,dA,
\]

作为 omitted shear-channel residual。

---

## 7. Gate 1：一般线弹性组合截面退化

令：

\[
A^+=A^-=0
\]

且所有材料退回线弹性。

对上下对称、各相平面内各向同性的组合截面：

\[
\begin{bmatrix}
N_x\\N_y\\N_{xy}
\end{bmatrix}
=
\begin{bmatrix}
A_{11}&A_{12}&0\\
A_{12}&A_{11}&0\\
0&0&A_{66}
\end{bmatrix}
\begin{bmatrix}
\varepsilon_x^0\\
\varepsilon_y^0\\
\gamma_{xy}^0
\end{bmatrix},
\]

且：

\[
A_{66}=\frac{A_{11}-A_{12}}2.
\]

定义：

\[
\bar\nu=\frac{A_{12}}{A_{11}},
\qquad
\bar K=A_{11}(1-\bar\nu^2).
\]

C0 中由 \(G_{B_x}=G_{B_y}=0\)：

\[
\boxed{
B_x=\bar\nu C_q\frac{b^2}{a_h^2}
}
\]

\[
\boxed{
B_y=\bar\nu C_q
}
\]

由横向总合力和轴向总合力：

\[
\boxed{
E_y
=
-\frac{P/b}{A_{11}(1-\bar\nu^2)}
}
\]

\[
\boxed{
E_x
=
\frac{\bar\nu\,P/b}{A_{11}(1-\bar\nu^2)}
}
\]

因此：

\[
\boxed{
N_x(y)=-\bar K C_q\cos2Y
}
\]

\[
\boxed{
N_y(x)
=
-\frac Pb
-\bar K C_q\frac{b^2}{a_h^2}\cos2X
}
\]

\[
\boxed{N_{xy}=0}.
\]

对均质单层：

\[
\bar\nu=\nu,\qquad \bar K=Et,
\]

严格退化到 Chen–Ji/Kármán–Airy zero-shear 分离场。

一个显式 Airy 函数为：

\[
\boxed{
\Phi
=
-\frac{P}{2b}x^2
+
\frac{\bar K C_q b^4}{4\pi^2a_h^2}\cos2X
+
\frac{\bar K C_q a_h^2}{4\pi^2}\cos2Y
}
\]

并满足：

\[
\Phi_{,yy}=N_x,\qquad
\Phi_{,xx}=N_y,\qquad
-\Phi_{,xy}=0.
\]

---

## 8. C1 在线弹性极限下的 H 子系统

令：

\[
r=\frac b{a_h}.
\]

三角正交性给：

\[
\frac{ba_h}{4}
\begin{bmatrix}
A_{11}+A_{66}r^2 & A_{12}+A_{66}\\
A_{12}+A_{66} & A_{11}+A_{66}r^{-2}
\end{bmatrix}
\begin{bmatrix}
H_x\\H_y
\end{bmatrix}
=\mathbf0.
\]

该 \(2\times2\) 子矩阵行列式为：

\[
\boxed{
A_{11}^2(1-\bar\nu)
\left[
1+\frac12(r^2+r^{-2})
\right]>0
}
\]

对物理范围 \(\bar\nu<1\) 恒正。

因此：

\[
\boxed{H_x=H_y=0}
\]

是唯一解。

所以：

\[
\boxed{\text{M0 = PASS,\qquad Gate 1 / M1 = PASS}}
\]

且不存在额外 spurious shear branch。

---

# M2：UHPC 材料非线性本身是否激活 shear membrane channel

## 9. 一个不依赖具体拟合参数的解析结论

即使 \(A^+=A^-=0\)，只要 UHPC normal law 非线性，C0 的 \(N_{xy}=0\) 在一般 current state 中也不再保证点态二维平衡。

对任意一个多项式分支 \(\sigma=f(e)\)，若厚度应变为：

\[
e=e_m+z\chi,
\]

则在整个厚度属于同一材料分支时：

\[
\boxed{
N
=
t f(e_m)
+
\frac{t^3\chi^2}{24}f''(e_m)
+
\frac{t^5\chi^4}{1920}f^{(4)}(e_m)
+
\frac{t^7\chi^6}{322560}f^{(6)}(e_m)
}
\]

对于当前最高六次 UHPC 压缩多项式，该式已经终止，不存在无限级数。

整体曲率给：

\[
\chi=\chi_0\sin X\sin Y.
\]

因此二阶项含：

\[
\sin^2X\sin^2Y
=
\frac14
\left(
1-\cos2X-\cos2Y+\cos2X\cos2Y
\right).
\]

也就是说，只要：

\[
q\neq0,\qquad f''(e_m)\neq0,
\]

current normal resultant 中就会自然出现：

\[
\boxed{\cos2X\cos2Y}
\]

mixed harmonic。

它恰好被 C0 删除，而由 C1 的 \(H_x,H_y\) 接收。

若先在均匀基态附近线性化，则由厚度 nonlinear bending-membrane coupling 单独产生的 omitted residual 主项为：

\[
\boxed{
\widehat G_{H_x}^{(2)}
\approx
\frac{ba_h\,t_c^3}{384}
f_x''(\bar e_x)\,
\chi_{x0}^2
}
\]

其中：

\[
\chi_{x0}
=
\frac{\pi^2q}{1-\nu_c^2}
\left(
\frac1b+\nu_c\frac b{a_h^2}
\right).
\]

同理：

\[
\boxed{
\widehat G_{H_y}^{(2)}
\approx
\frac{ba_h\,t_c^3}{384}
f_y''(\bar e_y)\,
\chi_{y0}^2
}
\]

\[
\chi_{y0}
=
\frac{\pi^2q}{1-\nu_c^2}
\left(
\frac b{a_h^2}+\frac{\nu_c}{b}
\right).
\]

因此：

\[
\boxed{
\text{UHPC material nonlinearity generically activates the C1 mixed/shear channel.}
}
\]

但“被激活”不等于“对 \(P(q)\) 显著”。

在 C0 解附近：

\[
\boxed{
\begin{bmatrix}
H_x\\H_y
\end{bmatrix}
\approx
-
\left[
\frac{\partial(G_{H_x},G_{H_y})}
{\partial(H_x,H_y)}
\right]^{-1}_{C0}
\begin{bmatrix}
\widehat G_{H_x}\\
\widehat G_{H_y}
\end{bmatrix}
}
\]

因此 C0 能否最终保留，必须看 omitted residual 和 C1 correction 的实际量级，而不能仅依据“非零/为零”。

---

## 10. M2 参考 tensile polynomial：只用于 Gate 2 前峰值核验

为避免重新使用历史约 10 MPa PCHIP，本轮独立核验使用：

\[
f_t=7.2\ {\rm MPa},
\qquad
\varepsilon_{tp}=0.000200,
\qquad
E_c=43.4\ {\rm GPa}.
\]

定义：

\[
\xi_t=\frac{e}{\varepsilon_{tp}},
\qquad
r_t=\frac{E_c\varepsilon_{tp}}{f_t}
=1.2055555556.
\]

构造满足：

\[
\sigma_t(0)=0,\quad
\sigma_t'(0)=E_c,\quad
\sigma_t(\varepsilon_{tp})=f_t,\quad
\sigma_t'(\varepsilon_{tp})=0
\]

的最小 cubic Hermite polynomial：

\[
\boxed{
\sigma_t
=
7.2
\left(
1.2055555556\,\xi_t
+
0.5888888889\,\xi_t^2
-
0.7944444444\,\xi_t^3
\right)
}
\]

只在：

\[
0\le e\le0.000200
\]

使用。

本轮 Gate 2 数值核验在任何材料点达到该峰值时停止；因此没有人为定义峰后 tensile softening。

压缩继续使用当前锁定六次多项式：

\[
\sigma_c
=
-f_c
\left(
A_c\xi_c+B_c\xi_c^5+C_c\xi_c^6
\right),
\qquad
\xi_c=-\frac e{\varepsilon_{c0}},
\]

\[
A_c=1.07654145996,\quad
B_c=0.61729270021,\quad
C_c=-0.69383416017.
\]

---

## 11. M2 独立数值核验的身份

为检查上述解析判据的量级，做了一次**非生产数值核验**：

- UHPC 厚度积分：按拉/压根 \(e=0\) 显式分区，分段使用多项式原函数，厚度积分为 exact；
- steel-local：关闭，\(A^+=A^-=0\)；
- 两层钢壳：保持线弹性，以隔离 UHPC material nonlinearity；
- C0/C1 inner equations + 当前 q generalized virtual-work equation 同时求解；
- 面内面积积分临时使用 18×18 Gauss–Legendre，仅用于验证量级。

因此下面结果：

\[
\boxed{\text{不能作为正式 Gate 2 的 production result}}
\]

因为最高层合同明确禁止用面内 Gauss 点定义正式 residual。

它们只负责回答：

“analytic omitted-residual 预言的 C1 激活是否实际可见、量级大约多大？”

### BH060，\(b=a_h=3000\ {\rm mm}\)

在：

\[
q=0.001000
\]

时：

\[
P_{C0}=4.762006642\ {\rm MN},
\]

\[
P_{C1}=4.762008289\ {\rm MN},
\]

\[
H_x=-1.35054\times10^{-7},
\qquad
H_y=+6.18798\times10^{-8}.
\]

相对荷载差：

\[
\frac{P_{C1}-P_{C0}}{P_{C0}}
=
3.46\times10^{-5}\%.
\]

C0 omitted residual norm：

\[
\sqrt{\widehat G_{H_x}^2+\widehat G_{H_y}^2}
=
1.26322\times10^6\ {\rm N\,mm},
\]

归一到 \(Pa_h\)：

\[
8.84\times10^{-5}.
\]

接近 reference tensile peak、但尚未超过时：

\[
q\approx0.00180020,
\]

C1 最大 directional tensile strain：

\[
e_{\max}\approx1.99998\times10^{-4}.
\]

此时：

\[
P_{C0}=7.001686213\ {\rm MN},
\]

\[
P_{C1}=7.001517755\ {\rm MN},
\]

\[
H_x=5.12849\times10^{-7},
\qquad
H_y=-2.27504\times10^{-7},
\]

相对差：

\[
\boxed{-0.002406\%}.
\]

C0 omitted residual norm 对 \(Pa_h\)：

\[
2.27\times10^{-4}.
\]

### BH100，\(b=a_h=5000\ {\rm mm}\)

在：

\[
q=0.001000
\]

时：

\[
P_{C0}=2.936723791\ {\rm MN},
\]

\[
P_{C1}=2.936717693\ {\rm MN},
\]

\[
H_x=-1.10163\times10^{-7},
\qquad
H_y=5.00168\times10^{-8}.
\]

相对荷载差：

\[
-2.08\times10^{-4}\%.
\]

接近 reference tensile peak：

\[
q\approx0.00305498,
\]

\[
P_{C0}=5.925417195\ {\rm MN},
\]

\[
P_{C1}=5.925289383\ {\rm MN},
\]

\[
H_x=4.39023\times10^{-7},
\qquad
H_y=-1.98558\times10^{-7},
\]

相对差：

\[
\boxed{-0.002157\%}.
\]

C0 omitted residual norm 对 \(Pa_h\)：

\[
3.77\times10^{-4}.
\]

---

## 12. M2 当前结论

解析上：

\[
\boxed{
\text{UHPC nonlinear law 使 }G_{H_x},G_{H_y}\text{ 一般不再严格为零。}
}
\]

所以“非线性以后 \(N_{xy}=0\) 仍是严格恒等式”这一说法不能成立。

但独立核验表明，在当前 pre-tensile-peak 参考区间：

\[
|H_x|,|H_y|\sim10^{-7}\text{--}10^{-6},
\]

而 C0/C1 的 \(P\) 差仅约：

\[
10^{-5}\%\text{ 到 }2.5\times10^{-3}\%.
\]

因此当前证据支持：

\[
\boxed{
\text{C1 channel 被激活，但 pre-peak 量级很小；C0 很可能是有效低阶退化。}
}
\]

不过正式 Gate 2 仍标记：

\[
\boxed{\text{Gate 2 = PENDING FORMAL SEMI-ANALYTIC AREA INTEGRATION}}
\]

原因不是新增理论门，而是 task contract 已规定：

正式 residual 不能由二维 Gauss 点定义。

---

## 13. M2 与 M4 的最小实现依赖

M2 要正式给出 \(P_{C0}(q)\)、\(P_{C1}(q)\)，必须将上述临时面内 quadrature 替换成合同要求的：

\[
\text{analytic active-set boundary}
+
\text{exact thickness integration}
+
\text{at most one-dimensional definite integral}.
\]

因此下一步不是改路线，而是把 M4 中**M2 所必需的最小 active-set kernel**提前实现：

对固定 \(X\)，材料点方向性输入在任意给定厚度坐标 \(z\) 都可写为：

\[
e(Y)
=
A(X,z)+B(X,z)\cos2Y+D(X,z)\sin Y.
\]

令：

\[
s=\sin Y,
\]

则任意材料阈值 \(e=e_j\) 化为：

\[
\boxed{
2B\,s^2-D\,s-\left(A+B-e_j\right)=0.
}
\]

所以所有 tension/compression/peak boundary 都可以显式求根。

这将用于生成可人工识别的 active intervals，再做多项式精确积分。

---

## 14. 当前唯一 NEXT_ACTION

继续 M2 的正式闭合，不转向 M3：

\[
\boxed{
\text{实现 M2 所需的 semi-analytic UHPC active-set area kernel，}
}
\]

用解析分区 + exact thickness integration + 最多一维确定积分，替换本轮 18×18 Gauss verification，然后重新计算同一 C0/C1 \(q\)-path。

只有这样才能正式判定 Gate 2。
