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
