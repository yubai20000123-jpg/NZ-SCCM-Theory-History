# NZ-SCCM — NC-M4 直接代入 Nguyen 二阶运动学后的多重积分完整展开

时间：2026-08-20 16:28 +08:00

状态：`ACTIVE_DERIVATION / DIRECT_SUBSTITUTION / ZERO_SPATIAL_QUADRATURE`

## 0. 本节点边界

本节点严格沿当前主线：

`(Delta,A,epsilon_m) -> Nguyen 二阶运动学 -> theta 与主应变 -> NC-M4 唯一九宫格 current operator -> 主应力 -> 板坐标应力 -> 膜力 N / 弯矩 M -> R_m, P, R_A`。

不引入 I1/I2 作为正式理论变量，不建立 spatial cells，不做 Gauss/Simpson/material-point grid，不把 CC/TC/TT 全域叠加。

---

## 1. 一般矩形完整代表半波

令

\[
k_x=\frac{\pi}{b},\qquad k_y=\frac{\pi}{\ell},
\]

并记

\[
s_x=\sin(k_xx),\quad c_x=\cos(k_xx),\quad s_y=\sin(k_yy),\quad c_y=\cos(k_yy).
\]

则

\[
\phi=s_xs_y,
\]

\[
\phi_{,x}=k_xc_xs_y,\qquad \phi_{,y}=k_ys_xc_y,
\]

\[
\phi_{,xx}=-k_x^2s_xs_y,\qquad \phi_{,yy}=-k_y^2s_xs_y,
\]

\[
\phi_{,xy}=k_xk_yc_xc_y.
\]

初始缺陷与新增挠度：

\[
w_0=A_0\phi,\qquad w=A\phi.
\]

定义

\[
S=A_0A+\frac12A^2,\qquad H=\frac{\partial S}{\partial A}=A_0+A.
\]

---

## 2. 中面膜应变、曲率与穿厚应变

中面膜应变：

\[
\varepsilon_x^0=\varepsilon_m+Sk_x^2c_x^2s_y^2,
\]

\[
\varepsilon_y^0=-\frac{\Delta}{\ell}+Sk_y^2s_x^2c_y^2,
\]

\[
\gamma_{xy}^0=2Sk_xk_yc_xs_xs_yc_y.
\]

曲率向量采用工程剪切约定：

\[
\kappa_x=-A\phi_{,xx}=Ak_x^2s_xs_y,
\]

\[
\kappa_y=-A\phi_{,yy}=Ak_y^2s_xs_y,
\]

\[
\kappa_{xy}=-2A\phi_{,xy}=-2Ak_xk_yc_xc_y.
\]

所以当前厚度点应变为

\[
\varepsilon_x=\varepsilon_m+Sk_x^2c_x^2s_y^2+zAk_x^2s_xs_y,
\]

\[
\varepsilon_y=-\frac{\Delta}{\ell}+Sk_y^2s_x^2c_y^2+zAk_y^2s_xs_y,
\]

\[
\gamma_{xy}=2Sk_xk_yc_xs_xs_yc_y-2zAk_xk_yc_xc_y.
\]

---

## 3. theta 与主应变：保持方向标签，不按大小排序

theta 是当前局部派生方向，不是新的结构未知量。方向 1/2 的标签按连续方向约定保持，不强制 epsilon1>=epsilon2；因此九宫格 TC 与 CT 都保留。

主方向满足

\[
\tan 2\theta=\frac{\gamma_{xy}}{\varepsilon_x-\varepsilon_y},
\]

其中 theta 的分支按方向连续性固定，而不是按主值大小排序。

记

\[
p=\cos\theta,\qquad q=\sin\theta.
\]

则

\[
\varepsilon_1=p^2\varepsilon_x+q^2\varepsilon_y+pq\gamma_{xy},
\]

\[
\varepsilon_2=q^2\varepsilon_x+p^2\varepsilon_y-pq\gamma_{xy}.
\]

---

## 4. NC-M4 基础函数

压缩：

\[
C(c)=\frac{2c}{1+c^2}.
\]

拉伸：

\[
T_4(t)=1.07515\frac{t(t+0.09)}{1-0.83t+1.04t^2+0.14t^3}.
\]

TC/CT 压缩削弱：

\[
\beta(t)=\frac1{1+0.15t^2}.
\]

CC 双压增强：

\[
\eta(c_1,c_2)=1+0.16C(c_1)C(c_2).
\]

---

## 5. 四实体区主应力

### CC

\[
c_i=-\frac{\varepsilon_i}{\varepsilon_{c0}},\qquad i=1,2,
\]

\[
\sigma_1=-f_c\eta C(c_1),\qquad \sigma_2=-f_c\eta C(c_2).
\]

### TC

\[
t_1=\frac{\varepsilon_1}{\varepsilon_{t0}},\qquad c_2=-\frac{\varepsilon_2}{\varepsilon_{c0}},
\]

\[
\sigma_1=f_tT_4(t_1),\qquad \sigma_2=-f_c\beta(t_1)C(c_2).
\]

### CT

\[
c_1=-\frac{\varepsilon_1}{\varepsilon_{c0}},\qquad t_2=\frac{\varepsilon_2}{\varepsilon_{t0}},
\]

\[
\sigma_1=-f_c\beta(t_2)C(c_1),\qquad \sigma_2=f_tT_4(t_2).
\]

### TT

\[
t_i=\frac{\varepsilon_i}{\varepsilon_{t0}},\qquad i=1,2,
\]

\[
\sigma_1=f_tT_4(t_1),\qquad \sigma_2=f_tT_4(t_2).
\]

边界 epsilon1=0 或 epsilon2=0 由相邻实体区自然退化。

---

## 6. 主应力旋回板坐标

统一写成

\[
\sigma_x=p^2\sigma_1+q^2\sigma_2,
\]

\[
\sigma_y=q^2\sigma_1+p^2\sigma_2,
\]

\[
\tau_{xy}=pq(\sigma_1-\sigma_2).
\]

因此各实体区的板坐标应力是：

### CC

\[
\sigma_x^{CC}=-f_c\eta\left[p^2C(c_1)+q^2C(c_2)\right],
\]

\[
\sigma_y^{CC}=-f_c\eta\left[q^2C(c_1)+p^2C(c_2)\right],
\]

\[
\tau_{xy}^{CC}=-f_c\eta\,pq\left[C(c_1)-C(c_2)\right].
\]

### TC

\[
\sigma_x^{TC}=f_tT_4(t_1)p^2-f_c\beta(t_1)C(c_2)q^2,
\]

\[
\sigma_y^{TC}=f_tT_4(t_1)q^2-f_c\beta(t_1)C(c_2)p^2,
\]

\[
\tau_{xy}^{TC}=pq\left[f_tT_4(t_1)+f_c\beta(t_1)C(c_2)\right].
\]

### CT

\[
\sigma_x^{CT}=-f_c\beta(t_2)C(c_1)p^2+f_tT_4(t_2)q^2,
\]

\[
\sigma_y^{CT}=-f_c\beta(t_2)C(c_1)q^2+f_tT_4(t_2)p^2,
\]

\[
\tau_{xy}^{CT}=-pq\left[f_c\beta(t_2)C(c_1)+f_tT_4(t_2)\right].
\]

### TT

\[
\sigma_x^{TT}=f_t\left[p^2T_4(t_1)+q^2T_4(t_2)\right],
\]

\[
\sigma_y^{TT}=f_t\left[q^2T_4(t_1)+p^2T_4(t_2)\right],
\]

\[
\tau_{xy}^{TT}=f_t\,pq\left[T_4(t_1)-T_4(t_2)\right].
\]

每个空间点只调用以上四者中的唯一一个。

---

## 7. 膜力与弯矩合力必须显式保留

定义

\[
N_x=\int_{-h/2}^{h/2}\sigma_x\,dz,\qquad
N_y=\int_{-h/2}^{h/2}\sigma_y\,dz,\qquad
N_{xy}=\int_{-h/2}^{h/2}\tau_{xy}\,dz,
\]

\[
M_x=\int_{-h/2}^{h/2}z\sigma_x\,dz,\qquad
M_y=\int_{-h/2}^{h/2}z\sigma_y\,dz,\qquad
M_{xy}=\int_{-h/2}^{h/2}z\tau_{xy}\,dz.
\]

这里的 sigma 是上述唯一 NC-M4 current operator，不是 CC/TC/TT 全厚度叠加。

---

## 8. R_m 与 P 完全展开

横向膜应变 epsilon_m 的导数只有 epsilon_x^0 对其为 1，因此

\[
R_m=\int_0^b\int_0^\ell N_x\,dy\,dx=0,
\]

即三重积分

\[
R_m=\int_0^b\int_0^\ell\int_{-h/2}^{h/2}\sigma_x(x,y,z)\,dz\,dy\,dx=0.
\]

其局部 integrand 对四状态分别为：

\[
r_m^{CC}=-f_c\eta[p^2C(c_1)+q^2C(c_2)],
\]

\[
r_m^{TC}=f_tT_4(t_1)p^2-f_c\beta(t_1)C(c_2)q^2,
\]

\[
r_m^{CT}=-f_c\beta(t_2)C(c_1)p^2+f_tT_4(t_2)q^2,
\]

\[
r_m^{TT}=f_t[p^2T_4(t_1)+q^2T_4(t_2)].
\]

轴向缩短 Delta 的内力共轭为

\[
P=-\frac1\ell\int_0^b\int_0^\ell N_y\,dy\,dx,
\]

即

\[
P=-\frac1\ell\int_0^b\int_0^\ell\int_{-h/2}^{h/2}\sigma_y(x,y,z)\,dz\,dy\,dx.
\]

四状态对应 sigma_y 已在第6节完整列出。

---

## 9. R_A 的膜力项与弯矩项

有

\[
\frac{\partial\varepsilon_x^0}{\partial A}=Hk_x^2c_x^2s_y^2,
\]

\[
\frac{\partial\varepsilon_y^0}{\partial A}=Hk_y^2s_x^2c_y^2,
\]

\[
\frac{\partial\gamma_{xy}^0}{\partial A}=2Hk_xk_yc_xs_xs_yc_y,
\]

以及

\[
\frac{\partial\kappa_x}{\partial A}=k_x^2s_xs_y,
\]

\[
\frac{\partial\kappa_y}{\partial A}=k_y^2s_xs_y,
\]

\[
\frac{\partial\kappa_{xy}}{\partial A}=-2k_xk_yc_xc_y.
\]

因此

\[
R_A=R_A^{N}+R_A^{M},
\]

其中膜力部分

\[
R_A^{N}=H\int_0^b\int_0^\ell
\left[
 k_x^2c_x^2s_y^2N_x
+k_y^2s_x^2c_y^2N_y
+2k_xk_yc_xs_xs_yc_yN_{xy}
\right]dy\,dx,
\]

弯矩部分

\[
R_A^{M}=\int_0^b\int_0^\ell
\left[
 k_x^2s_xs_yM_x
+k_y^2s_xs_yM_y
-2k_xk_yc_xc_yM_{xy}
\right]dy\,dx.
\]

合并为一次三重积分时，定义三个显式虚应变核：

\[
G_x=Hk_x^2c_x^2s_y^2+zk_x^2s_xs_y,
\]

\[
G_y=Hk_y^2s_x^2c_y^2+zk_y^2s_xs_y,
\]

\[
G_\gamma=2Hk_xk_yc_xs_xs_yc_y-2zk_xk_yc_xc_y.
\]

于是

\[
R_A=\int_0^b\int_0^\ell\int_{-h/2}^{h/2}
\left(\sigma_xG_x+\sigma_yG_y+\tau_{xy}G_\gamma\right)dz\,dy\,dx.
\]

---

## 10. R_A integrand 在主方向中的有限展开

利用旋回关系，局部虚功密度恒等于

\[
r_A=\sigma_1\left[p^2G_x+q^2G_y+pqG_\gamma\right]
+\sigma_2\left[q^2G_x+p^2G_y-pqG_\gamma\right].
\]

这里不需要 theta 对 A 的导数；在当前主坐标中应力张量对角化，方向变化项在一阶虚功中消失。

将 G_x,G_y,G_gamma 继续展开，得到

\[
\begin{aligned}
r_A={}&Hk_x^2c_x^2s_y^2\left(p^2\sigma_1+q^2\sigma_2\right)
+Hk_y^2s_x^2c_y^2\left(q^2\sigma_1+p^2\sigma_2\right)\\
&+2Hk_xk_yc_xs_xs_yc_y\,pq\left(\sigma_1-\sigma_2\right)\\
&+zk_x^2s_xs_y\left(p^2\sigma_1+q^2\sigma_2\right)
+zk_y^2s_xs_y\left(q^2\sigma_1+p^2\sigma_2\right)\\
&-2zk_xk_yc_xc_y\,pq\left(\sigma_1-\sigma_2\right).
\end{aligned}
\]

保持 H=A0+A 不再拆开时，这只是 6 个物理组；若连每个括号中的 sigma1/sigma2 都展开，则总共 12 个加法项，不存在高项数爆炸。

---

## 11. 四实体区的 R_A integrand 直接代入

### CC

\[
\begin{aligned}
r_A^{CC}=-f_c\eta\{&C(c_1)[p^2G_x+q^2G_y+pqG_\gamma]\\
&+C(c_2)[q^2G_x+p^2G_y-pqG_\gamma]\}.
\end{aligned}
\]

### TC

\[
\begin{aligned}
r_A^{TC}={}&f_tT_4(t_1)[p^2G_x+q^2G_y+pqG_\gamma]\\
&-f_c\beta(t_1)C(c_2)[q^2G_x+p^2G_y-pqG_\gamma].
\end{aligned}
\]

### CT

\[
\begin{aligned}
r_A^{CT}={}&-f_c\beta(t_2)C(c_1)[p^2G_x+q^2G_y+pqG_\gamma]\\
&+f_tT_4(t_2)[q^2G_x+p^2G_y-pqG_\gamma].
\end{aligned}
\]

### TT

\[
\begin{aligned}
r_A^{TT}=f_t\{&T_4(t_1)[p^2G_x+q^2G_y+pqG_\gamma]\\
&+T_4(t_2)[q^2G_x+p^2G_y-pqG_\gamma]\}.
\end{aligned}
\]

这些是正式三重积分中实际出现的四个局部表达式；每一点只取其中一个。

---

## 12. 当前结论

1. 膜应变、膜力 N、弯矩 M 均已显式恢复；R_A 中膜力项与弯矩项均保留。
2. theta 只负责当前局部主方向识别与应力旋回，不是新增结构未知量。
3. 不需要 I1/I2 作为正式中间理论层。
4. 三个正式连续积分已经完全展开为：
   - R_m：唯一 local sigma_x 的三重积分；
   - P：唯一 local sigma_y 的三重积分；
   - R_A：6 个物理组 / 12 个完全展开加法项乘以唯一 local principal stress pair。
5. NC-M4 当前真正需要 CAS 继续执行的对象已经是上述 explicit integrands 本身，而不是重新构造材料映射。
6. theta 解决的是 TC/CT 的方向识别与旋回；若 CAS 后端为了消元 theta 自动产生平方根，那只是内部代数表示，不应再升级为新的理论变量或理论层。
