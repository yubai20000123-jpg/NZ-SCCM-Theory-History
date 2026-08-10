# NZ-SCCM Case21 不变量与四族精确解析矩推导 V1

**日期：2026-08-10**  
**身份：CURRENT ANALYTIC DERIVATION / EXACT-MOMENT FOUNDATION**

## 0. 目的与边界

本文件执行 `NZ_SCCM_TARGET_FUNCTION_REBUILD_ANALYTIC_MOMENT_V1_20260810.md` 的第一步：在不改变 Case21 Nguyen 二阶运动学的条件下，将归一化应变张量的两个二维不变量 `I1=tr(X)`、`I2=det(X)` 完整展开，并建立 `P`、`Rq` 所需四族解析矩。

正式边界继续锁定：

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
FORMAL_INTEGRATION = ANALYTIC_EXACT_MOMENTS
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
ELEMENT_INTEGRATION = PROHIBITED
```

本文件只证明结构运动学—不变量—精确矩这一层的闭合；**不把低阶 generic polynomial material law 当作真实混凝土可行性证明。**真实混凝土的强非线性必须通过独立 `CONCRETE_NONLINEARITY_GATE`。

---

## 1. Case21 冻结归一化运动学

历史 moment-first 冻结稿给出：

\[
X=\pi x/b,\qquad Y=\pi y/\ell,\qquad \zeta=2z/t,
\]

\[
q=A/b,\qquad q_0=A_0/b,
\]

\[
C_m(q)=\frac{\pi^2}{\varepsilon_0}\left(q_0q+\frac12q^2\right),
\qquad
C_b(q)=\frac{\pi^2}{2\varepsilon_0}\frac tb q.
\]

物理应变为 `eps0*(e_x,e_y,g_xy)`，其中

\[
e_x=\nu D+C_m\cos^2X\sin^2Y+C_b\sin X\sin Y\,\zeta,
\]

\[
e_y=-D+C_m\sin^2X\cos^2Y+C_b\sin X\sin Y\,\zeta,
\]

\[
g_{xy}=2C_m\sin X\cos X\sin Y\cos Y-2C_b\cos X\cos Y\,\zeta.
\]

因此本文件直接采用归一化物理应变张量

\[
\mathbf X=\frac{\mathbf E}{\varepsilon_0}
=\begin{bmatrix}
e_x&g_{xy}/2\\
g_{xy}/2&e_y
\end{bmatrix}.
\]

为压缩记号，定义

\[
u=\sin X,\qquad v=\sin Y,\qquad z=\zeta,
\]

并写

\[
M=C_m(q),\qquad B=C_b(q).
\]

由于完整半波内 `sin X,sin Y >= 0`，这里不需要引入任何空间分支。

再定义三个有限多项式块：

\[
H=u^2+v^2-2u^2v^2,
\]

\[
K=\nu u^2-v^2+(1-\nu)u^2v^2,
\]

\[
W=uvz.
\]

---

## 2. 第一个不变量 I1：完整解析展开

由 `I1=tr(X)=e_x+e_y`：

\[
\boxed{
I_1=(\nu-1)D+MH+2BW
}
\]

即

\[
\boxed{
I_1=(\nu-1)D
+M(u^2+v^2-2u^2v^2)
+2Buvz
}.
\]

这是 `u,v,z` 的有限多项式。

---

## 3. 第二个不变量 I2：完整解析展开

二维行列式：

\[
I_2=\det\mathbf X=e_xe_y-(g_{xy}/2)^2.
\]

直接展开后，`M^2` 项来自

\[
M^2\cos^2X\sin^2X\cos^2Y\sin^2Y
\]

并在 `e_xe_y` 与 `(g_xy/2)^2` 之间**严格完全抵消**。

继续使用

\[
\cos^2X=1-u^2,\qquad \cos^2Y=1-v^2,
\]

得到

\[
\boxed{
\begin{aligned}
I_2={}&-\nu D^2
+DMK
+BD(\nu-1)W\\
&+BMW(2-u^2-v^2)
+B^2z^2(u^2+v^2-1).
\end{aligned}
}
\]

即

\[
\boxed{
\begin{aligned}
I_2={}&-\nu D^2
+DM[\nu u^2-v^2+(1-\nu)u^2v^2]\\
&+BD(\nu-1)uvz\\
&+BMuvz(2-u^2-v^2)\\
&+B^2z^2(u^2+v^2-1).
\end{aligned}
}
\]

### 3.1 关键结构结论

1. `I2` 中不存在 `M^2`；
2. `I1,I2` 均不再显式含 `cos X,cos Y`；
3. 两个不变量都属于有限多项式环

\[
\mathbb R[D,M,B,\nu][u,v,z].
\]

因此任何有限多项式材料基 `Phi(I1,I2)` 与它们复合后仍是 `u,v,z` 的有限多项式。

---

## 4. q 导数：解析闭合

定义

\[
\alpha=\frac{\pi^2}{\varepsilon_0},
\qquad
\beta=\frac{\pi^2}{2\varepsilon_0}\frac tb,
\]

则

\[
M=\alpha\left(q_0q+\frac12q^2\right),
\qquad
B=\beta q,
\]

\[
M_q=\alpha(q_0+q),\qquad M_{qq}=\alpha,
\]

\[
B_q=\beta,\qquad B_{qq}=0.
\]

因此

\[
\boxed{I_{1,q}=M_qH+2B_qW}
\]

\[
\boxed{I_{1,D}=\nu-1}
\]

以及

\[
\boxed{
\begin{aligned}
I_{2,q}={}&DM_qK+B_qD(\nu-1)W\\
&+(B_qM+BM_q)W(2-u^2-v^2)\\
&+2BB_qz^2(u^2+v^2-1).
\end{aligned}
}
\]

\[
\boxed{
I_{2,D}=-2\nu D+MK+B(\nu-1)W
}
\]

还可直接得到

\[
\boxed{I_{1,qq}=\alpha H}
\]

\[
\boxed{I_{1,Dq}=0}
\]

\[
\boxed{
\begin{aligned}
I_{2,qq}={}&D\alpha K
+(2B_qM_q+B\alpha)W(2-u^2-v^2)\\
&+2B_q^2z^2(u^2+v^2-1),
\end{aligned}
}
\]

\[
\boxed{I_{2,Dq}=M_qK+B_q(\nu-1)W}.
\]

所有导数仍属于同一个有限多项式环。

---

## 5. P 所需应变分量

轴向归一化应变分量可化为

\[
\boxed{
X_{yy}=e_y=-D+Mu^2(1-v^2)+BW
}.
\]

其 q 导数：

\[
\boxed{
X_{yy,q}=M_qu^2(1-v^2)+B_qW
}.
\]

---

## 6. Rq 中 X:X_q 的不变量恒等式

对二维对称张量：

\[
\operatorname{tr}(\mathbf X^2)=I_1^2-2I_2.
\]

对 q 求导：

\[
2\mathbf X:\mathbf X_{,q}
=2I_1I_{1,q}-2I_{2,q}.
\]

因此

\[
\boxed{
\mathbf X:\mathbf X_{,q}=I_1I_{1,q}-I_{2,q}
}.
\]

这使 `Rq` 不需要显式保留三个应变分量与剪应变乘积；只需 `I1,I2` 及其导数。

记

\[
G_q=I_1I_{1,q}-I_{2,q}.
\]

进一步：

\[
\boxed{
G_{q,q}=I_{1,q}^2+I_1I_{1,qq}-I_{2,qq}
}
\]

\[
\boxed{
G_{q,D}=(\nu-1)I_{1,q}-I_{2,Dq}
}
\]

因为 `I1,Dq=0`。

---

## 7. 四族材料—结构精确矩

若 V1 同轴材料写为

\[
\widehat{\boldsymbol\sigma}
=A(I_1,I_2)\mathbf I+B(I_1,I_2)\mathbf X,
\]

并采用有限材料基

\[
\Phi_{mn}=I_1^mI_2^n,
\]

则定义归一化完整半波积分泛函

\[
\mathscr M[F]
=\int_0^\pi\int_0^\pi\int_{-1}^{1}
F(u,v,z)\,dz\,dY\,dX.
\]

结构只需要四族矩：

### 7.1 轴力 A 矩

\[
\boxed{
J^A_{P,mn}=\mathscr M[I_1^mI_2^n]
}
\]

### 7.2 轴力 B 矩

\[
\boxed{
J^B_{P,mn}=\mathscr M[I_1^mI_2^nX_{yy}]
}
\]

### 7.3 幅值平衡 A 矩

\[
\boxed{
J^A_{q,mn}=\mathscr M[I_1^mI_2^nI_{1,q}]
}
\]

### 7.4 幅值平衡 B 矩

\[
\boxed{
J^B_{q,mn}=\mathscr M[I_1^mI_2^nG_q]
}
\]

其中

\[
G_q=I_1I_{1,q}-I_{2,q}.
\]

于是有限材料系数与结构矩只做线性 contraction：

\[
P_c=-f_rJ_\Omega
\sum_{mn}\left(a_{mn}J^A_{P,mn}+b_{mn}J^B_{P,mn}\right),
\]

\[
R_{q,c}=f_r\varepsilon_0J_\Omega
\sum_{mn}\left(a_{mn}J^A_{q,mn}+b_{mn}J^B_{q,mn}\right).
\]

这里 `J_Omega` 是从 `x,y,z` 到 `X,Y,zeta` 的物理 Jacobian；其具体符号保持与当前 Case21 定义一致。

---

## 8. 精确基础矩进一步简化：只需 sin-power × sin-power × z-power

由于 `I1,I2,Xyy,I1q,Gq` 已全部写为 `u=sin X`、`v=sin Y`、`z=zeta` 的多项式，正式基础矩甚至不再需要一般 `sin^p cos^r` 形式。

任意 integrand 唯一表示为有限和

\[
F=\sum_{a,b,h}c_{abh}(D,q)u^av^bz^h.
\]

因此

\[
\boxed{
\mathscr M[F]
=\sum_{a,b,h}c_{abh}(D,q)S_aS_bZ_h
}
\]

其中

\[
S_n=\int_0^\pi\sin^nX\,dX
=\sqrt\pi\frac{\Gamma((n+1)/2)}{\Gamma((n+2)/2)},
\]

\[
Z_h=\int_{-1}^{1}z^h\,dz
=\begin{cases}
0,&h\text{ odd},\\
2/(h+1),&h\text{ even}.
\end{cases}
\]

所有积分均是完整连续域上的解析闭式；不存在 element、cell、Gauss point 或 spatial sampling。

### 8.1 有限多项式乘法规则

若

\[
F=\sum c_{abh}u^av^bz^h,
\qquad
G=\sum d_{ijk}u^iv^jz^k,
\]

则

\[
FG=\sum_{p,r,s}
\left(\sum_{a+i=p\atop b+j=r,\ h+k=s}c_{abh}d_{ijk}\right)
u^pv^rz^s.
\]

这是有限 Cauchy convolution，仅发生在解析系数代数中；不是空间离散。

---

## 9. 低阶解析校验值

以下不是材料模型，而是四族矩引擎的人工校验点。

### 9.1 `(m,n)=(0,0)`

\[
\boxed{J^A_{P,00}=2\pi^2}
\]

\[
\boxed{
J^B_{P,00}=\pi^2\left(-2D+\frac M2\right)
}
\]

\[
\boxed{J^A_{q,00}=\pi^2M_q}
\]

\[
\boxed{
J^B_{q,00}=\pi^2\left[
M_q\left(\frac{(\nu-1)D}{2}+\frac{5M}{8}\right)
+\frac23BB_q
\right]
}
\]

### 9.2 另外两个不变量平均值

\[
\boxed{
\mathscr M[I_1]
=\pi^2[2(\nu-1)D+M]
}
\]

\[
\boxed{
\mathscr M[I_2]
=-\frac{\pi^2D}{2}[4\nu D+(1-\nu)M]
}
\]

这些式子已用独立 SymPy 直接从原 `e_x,e_y,g_xy` 展开并积分核对。

---

## 10. 导数与 L 的同一矩族闭合

对

\[
\Phi_{mn}=I_1^mI_2^n
\]

任意广义坐标 `a in {D,q}`：

\[
\boxed{
\Phi_{mn,a}
=mI_1^{m-1}I_2^nI_{1,a}
+nI_1^mI_2^{n-1}I_{2,a}
}
\]

因此 `P_,D,P_,q,Rq_,D,Rq_,q` 不需要新的空间积分概念，只是对同一有限多项式矩族增加解析因子并再次施加 `mathscr M`。

最终仍为

\[
R_q(D,q)=0,
\]

\[
L(D,q)=P_{,D}R_{q,q}-P_{,q}R_{q,D}=0.
\]

完成矩收缩后，`X,Y,zeta` 从正式求根器中完全消失。

---

## 11. 对材料强非线性的意义

本推导只证明：**任何有限阶、可化为 `I1,I2` 有限多项式/有限矩阵多项式的材料非线性，都可以保持精确解析积分。**

它并未证明“低阶多项式就足够描述混凝土”。

因此下一材料层必须遵守：

1. 混凝土非线性阶次由材料级单轴/双轴/三轴/拉伸/峰后证据决定；
2. 若需要高阶，增加的是有限解析材料阶次和精确矩项数，不是空间积分点；
3. 若单一低阶 `A/B` surface 无法同时描述压缩峰值/峰后、拉伸开裂后响应、CC 强度增强、TC 软化等，则该材料表示失败，不能通过结构 Pu 调参掩盖；
4. 必须立即使用当前 frozen NC operator 与原始材料数据作为强非线性 benchmark，而不能只用 generic low-order polynomial 做架构验收。

下一步见 `NZ_SCCM_CONCRETE_NONLINEARITY_GATE_V1_20260810.md`。
