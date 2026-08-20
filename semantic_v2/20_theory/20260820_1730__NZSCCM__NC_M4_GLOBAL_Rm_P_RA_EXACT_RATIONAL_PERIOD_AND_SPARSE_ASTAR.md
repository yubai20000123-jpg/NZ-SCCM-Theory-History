# NZ-SCCM — NC-M4 全局 R_m、P、R_A 精确有理周期闭合与稀疏 A* 主族

时间：2026-08-20 17:30 +08:00

状态：`ACTIVE_EXACT_GLOBAL_INTEGRATION / GLOBAL_Rm_P_RA_CLOSED_AS_RELATIVE_GKZ / ZERO_SPATIAL_QUADRATURE`

## 0. 本节点只做全局积分

本节点不再重新打开 TC/CT。当前固定链条为：

`Nguyen 二阶运动学 -> theta/主应变 -> frozen NC-M4 -> sigma_x,sigma_y,tau_xy -> global exact R_m,P,R_A`。

目标是把三个三重积分整体提升成一个有限稀疏有理周期，并给出其完整材料/运动学多项式关系与有限主支撑 A*。这不是局部 TC 积分证明，而是三个全局量的共同解析后端。

---

## 1. 半角坐标下的显式运动学

令

\[
u=\tan\frac X2,\qquad v=\tan\frac Y2,
\]

\[
U=1+u^2,\qquad V=1+v^2,\qquad D=U^2V^2.
\]

于是

\[
\sin X=\frac{2u}{U},\quad \cos X=\frac{1-u^2}{U},
\qquad
\sin Y=\frac{2v}{V},\quad \cos Y=\frac{1-v^2}{V},
\]

\[
dX\,dY=\frac{4\,du\,dv}{UV}.
\]

定义

\[
S=A_0A+\frac12A^2,
\]

\[
a_x=\frac{\pi^2S}{b^2},\qquad
a_y=\frac{\pi^2S}{\ell^2},\qquad
a_g=\frac{2\pi^2S}{b\ell},
\]

\[
b_x=\frac{hA\pi^2}{2b^2},\qquad
b_y=\frac{hA\pi^2}{2\ell^2},\qquad
b_g=\frac{hA\pi^2}{b\ell}.
\]

取

\[
C_x=1-u^2,\qquad C_y=1-v^2.
\]

则三个板坐标应变写为

\[
\varepsilon_x=\frac{E_x}{D},\qquad
\varepsilon_y=\frac{E_y}{D},\qquad
\gamma_{xy}=\frac{E_\gamma}{D},
\]

其中

\[
\boxed{
E_x=\varepsilon_mD+4a_xv^2C_x^2+4b_x\zeta\,uvUV
}
\]

\[
\boxed{
E_y=-\frac{\Delta}{\ell}D+4a_yu^2C_y^2+4b_y\zeta\,uvUV
}
\]

\[
\boxed{
E_\gamma=4a_guvC_xC_y-b_g\zeta C_xC_yUV.
}
\]

再定义

\[
E_s=E_x+E_y,\qquad E_d=E_x-E_y.
\]

---

## 2. theta 的精确代数后端：只引入一个根生成元

理论层仍由 theta 识别主方向。积分后端仅为精确消元引入

\[
\boxed{
G_W=W^2-E_d^2-E_\gamma^2=0.
}
\]

取物理正根支 `W>0`。于是

\[
\lambda_+=\frac{E_s+W}{2D},\qquad
\lambda_-=\frac{E_s-W}{2D}.
\]

定义

\[
L_+=E_s+W,\qquad L_-=E_s-W.
\]

正式九宫格 TC/CT 标签不被删除；在无方向标签的张量后端中，一拉一压只需要一个 mixed relative chain，TC/CT 的区别由方向旋转自动恢复。

---

## 3. NC-M4 四个材料函数全部显式有理化

记

\[
e_t=\varepsilon_{t0},\qquad e_c=\varepsilon_{c0},\qquad \kappa_T=1.07515.
\]

### 3.1 拉伸主应力函数

定义

\[
\boxed{
\mathcal D_{t,\pm}
=8e_t^3D^3
-3.32e_t^2D^2L_\pm
+2.08e_tDL_\pm^2
+0.14L_\pm^3.
}
\]

则

\[
\boxed{
T_\pm^\sigma
=\frac{2\kappa_T f_t e_tD\,L_\pm(L_\pm+0.18e_tD)}{\mathcal D_{t,\pm}}.
}
\]

这与

\[
f_tT_4\!\left(\frac{\lambda_\pm}{e_t}\right)
\]

严格恒等。

### 3.2 压缩主应力函数

定义

\[
\boxed{
\mathcal D_{c,\pm}=4e_c^2D^2+L_\pm^2.
}
\]

则

\[
\boxed{
C_\pm^\sigma
=\frac{4f_ce_cD\,L_\pm}{\mathcal D_{c,\pm}}.
}
\]

当 `L_\pm<0` 时该式自动给出负压应力。

### 3.3 mixed 拉压削弱

\[
\boxed{
\mathcal D_\beta=4e_t^2D^2+0.15L_+^2
}
\]

\[
\boxed{
B_+=\frac{4e_t^2D^2}{\mathcal D_\beta}.
}
\]

### 3.4 CC 双压增强

\[
\boxed{
\eta
=1+
\frac{2.56e_c^2D^2L_+L_-}
{\mathcal D_{c,+}\mathcal D_{c,-}}.
}
\]

---

## 4. 三个谱状态的主应力对

TT：

\[
s_+^{TT}=T_+^\sigma,\qquad s_-^{TT}=T_-^\sigma.
\]

Mixed（张量上同时代表 TC/CT）：

\[
s_+^{M}=T_+^\sigma,\qquad s_-^{M}=B_+C_-^\sigma.
\]

CC：

\[
s_+^{CC}=\eta C_+^\sigma,\qquad s_-^{CC}=\eta C_-^\sigma.
\]

对应相对链：

\[
\Gamma_{TT}:L_->0,
\]

\[
\Gamma_M:L_+>0>L_-,
\]

\[
\Gamma_{CC}:L_+<0.
\]

这些是 exact relative-chain 数据，不是 spatial cells。

定义对每个状态 `s`：

\[
\Sigma_s=s_+^s+s_-^s,
\qquad
\Delta_s=s_+^s-s_-^s.
\]

---

## 5. 板坐标应力的显式谱重构

严格有

\[
\boxed{
\sigma_x^s
=\frac12\Sigma_s+\frac{E_d}{2W}\Delta_s
}
\]

\[
\boxed{
\sigma_y^s
=\frac12\Sigma_s-\frac{E_d}{2W}\Delta_s
}
\]

\[
\boxed{
\tau_{xy}^s
=\frac{E_\gamma}{2W}\Delta_s.
}
\]

也即

\[
2W\sigma_x^s=W\Sigma_s+E_d\Delta_s,
\]

\[
2W\sigma_y^s=W\Sigma_s-E_d\Delta_s,
\]

\[
2W\tau_{xy}^s=E_\gamma\Delta_s.
\]

---

## 6. R_A 权函数的显式半角形式

令

\[
H=A_0+A,
\]

\[
g_{x0}=\frac{\pi^2H}{b^2},\qquad
g_{x1}=\frac{h\pi^2}{2b^2},
\]

\[
g_{y0}=\frac{\pi^2H}{\ell^2},\qquad
g_{y1}=\frac{h\pi^2}{2\ell^2},
\]

\[
g_{\gamma0}=\frac{2\pi^2H}{b\ell},\qquad
g_{\gamma1}=\frac{h\pi^2}{b\ell}.
\]

则

\[
G_x=\frac{\mathcal G_x}{D},\qquad
G_y=\frac{\mathcal G_y}{D},\qquad
G_\gamma=\frac{\mathcal G_\gamma}{D},
\]

其中

\[
\boxed{
\mathcal G_x
=4g_{x0}v^2C_x^2+4g_{x1}\zeta uvUV
}
\]

\[
\boxed{
\mathcal G_y
=4g_{y0}u^2C_y^2+4g_{y1}\zeta uvUV
}
\]

\[
\boxed{
\mathcal G_\gamma
=4g_{\gamma0}uvC_xC_y-g_{\gamma1}\zeta C_xC_yUV.
}
\]

---

## 7. 正根支 residue lift

对任意物理正根支上的函数 `H(W_+)`：

\[
\boxed{
H(W_+)
=\frac1{2\pi i}
\oint_{\gamma_+}
H(W)\frac{2W}{G_W}\,dW.
}
\]

因此三个完整空间三重积分整体变成有限有理 relative periods。

记

\[
K_0=\frac{b\ell h}{2\pi^2}.
\]

---

## 8. 全局 R_m 的精确解析形式

\[
\boxed{
R_m
=\frac{4K_0}{2\pi i}
\sum_{s\in\{TT,M,CC\}}
\int_{\Gamma_s}
\oint_{\gamma_+}
\frac{W\Sigma_s+E_d\Delta_s}
{UV\,G_W}
\,dW\,d\zeta\,dv\,du.
}
\]

其中全部分子、分母和分支条件已经在第 1–6 节明确定义。

---

## 9. 全局 P 的精确解析形式

\[
\boxed{
P
=-\frac{4K_0}{\ell(2\pi i)}
\sum_{s\in\{TT,M,CC\}}
\int_{\Gamma_s}
\oint_{\gamma_+}
\frac{W\Sigma_s-E_d\Delta_s}
{UV\,G_W}
\,dW\,d\zeta\,dv\,du.
}
\]

---

## 10. 全局 R_A 的精确解析形式

由

\[
2Wr_A^s
=\frac1D\left\{
W\Sigma_s(\mathcal G_x+\mathcal G_y)
+\Delta_s\left[
E_d(\mathcal G_x-\mathcal G_y)
+E_\gamma\mathcal G_\gamma
\right]
\right\},
\]

得到

\[
\boxed{
R_A
=\frac{4K_0}{2\pi i}
\sum_{s\in\{TT,M,CC\}}
\int_{\Gamma_s}
\oint_{\gamma_+}
\frac{
W\Sigma_s(\mathcal G_x+\mathcal G_y)
+\Delta_s\left[
E_d(\mathcal G_x-\mathcal G_y)+E_\gamma\mathcal G_\gamma
\right]
}
{UV\,D\,G_W}
\,dW\,d\zeta\,dv\,du.
}
\]

这三个式子是同一个 NC-M4 operator 的三个 numerator insertions，不是三套求解器。

---

## 11. NC-M4 的显式稀疏多项式电路

取变量顺序：

`u,v,zeta,Cx,Cy,U,V,D,Ex,Ey,Eg,Es,Ed,W,Lp,Lm,DtP,DtM,DcP,DcM,Db,ItP,ItM,IcP,IcM,Ib,Tp,Tm,Cp,Cm,Beta,Eta`。

共 32 个变量。

电路关系共 29 条：

1. `Cx-(1-u^2)=0`
2. `Cy-(1-v^2)=0`
3. `U-(1+u^2)=0`
4. `V-(1+v^2)=0`
5. `D-U^2 V^2=0`
6. `Ex-[eps_m D+4 a_x v^2 Cx^2+4 b_x zeta u v U V]=0`
7. `Ey-[-Delta/ell D+4 a_y u^2 Cy^2+4 b_y zeta u v U V]=0`
8. `Eg-[4 a_g u v Cx Cy-b_g zeta Cx Cy U V]=0`
9. `Es-Ex-Ey=0`
10. `Ed-Ex+Ey=0`
11. `W^2-Ed^2-Eg^2=0`
12. `Lp-Es-W=0`
13. `Lm-Es+W=0`
14. `DtP-[8 et^3 D^3-3.32 et^2 D^2 Lp+2.08 et D Lp^2+0.14 Lp^3]=0`
15. `DtM-[8 et^3 D^3-3.32 et^2 D^2 Lm+2.08 et D Lm^2+0.14 Lm^3]=0`
16. `DcP-[4 ec^2 D^2+Lp^2]=0`
17. `DcM-[4 ec^2 D^2+Lm^2]=0`
18. `Db-[4 et^2 D^2+0.15 Lp^2]=0`
19. `ItP DtP-1=0`
20. `ItM DtM-1=0`
21. `IcP DcP-1=0`
22. `IcM DcM-1=0`
23. `Ib Db-1=0`
24. `Tp-[2 kappa_T ft et D Lp(Lp+0.18 et D) ItP]=0`
25. `Tm-[2 kappa_T ft et D Lm(Lm+0.18 et D) ItM]=0`
26. `Cp-[4 fc ec D Lp IcP]=0`
27. `Cm-[4 fc ec D Lm IcM]=0`
28. `Beta-[4 et^2 D^2 Ib]=0`
29. `Eta-[1+2.56 ec^2 D^2 Lp Lm IcP IcM]=0`

对这 29 个辅助量的 residue Jacobian 为

\[
\boxed{
J_{\rm circ}=2W\,DtP\,DtM\,DcP\,DcM\,Db.
}
\]

所以整个 NC-M4 complete-halfwave integral 可以一次性 lifted 成纯有理多重 residue period。

---

## 12. 主支撑 A_*^{M4} 的实际规模

对上述 29 条关系做实际 monomial-support 审计，得到：

```text
physical+circuit variables = 32
circuit relations = 29
total Cayley monomial columns = 84
max monomials in any one relation = 5
Cayley A* size = 61 x 84
```

与旧 R10 pilot 的 `159 x 271` 相比，NC-M4 的全局 exact integration support 大幅缩小。

三个目标的 numerator support（合并同指数 monomial 后）：

```text
R_m numerator support per spectral branch = 4
P numerator support per spectral branch   = 4
R_A numerator support per spectral branch = 16
```

因此

\[
\boxed{
R_m,\;P,\;R_A,\;J_{\lim}
}
\]

全部属于同一个显式有限 relative/incomplete GKZ 主族

\[
\boxed{A_*^{M4}\in\mathbb Z^{61\times84}}
\]

的有限 numerator / contiguity / differential shifts。

---

## 13. 完成度定义

本节点已完成：

- NC-M4 的完整三重空间积分整体 exact rational-period lift；
- 三个目标 R_m、P、R_A 的明确全局 numerator；
- 全部材料分母、电路关系、branch relative-chain 数据；
- 一个实际审计过的 61x84 finite sparse master support；
- zero spatial quadrature / zero material-point grid。

严格来说，若要求最终纸面上完全没有任何积分符号，则 `relative/incomplete GKZ period` 应作为标准函数记号使用。当前 rational-period 公式给出的已是该标准函数的完整参数化定义，不存在匿名 `a_nu` 或 `mathfrak A_nu` 占位符。

没有证明一般参数下这三个 relative periods 会进一步塌缩成 elementary/Appell/Lauricella 的短公式；也不应伪造这样的降阶。
