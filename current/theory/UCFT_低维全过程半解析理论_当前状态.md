# UCFT 低维全过程半解析理论 — 当前状态

**更新时间：2026-09-30 14:06 +08:00**  
**最高层路线合同：用户上传《指示词.md》**  
**当前主攻方向：M2 nonlinear membrane condensation / formal semi-analytic active-set path**

## 1. 结构级变量

路径参数：

\[
q.
\]

给定 \(q\) 后外层未知：

\[
P,\qquad A^+,\qquad A^-.
\]

统一端缩 \(\Delta\) 不作为路径控制量；端部位移在平衡后恢复。

## 2. 整体几何

\[
W_0=bq_0\sin\frac{\pi x}{b}\sin\frac{\pi y}{a_h},
\]

\[
W=b(q_0+q)\sin\frac{\pi x}{b}\sin\frac{\pi y}{a_h},
\]

\[
Q(q)=q^2+2q_0q.
\]

## 3. C0 / C1

### C0

\[
\varepsilon_x^0
=
E_x+B_x\cos2X-C_q\cos2Y,
\]

\[
\varepsilon_y^0
=
E_y-C_q\frac{b^2}{a_h^2}\cos2X+B_y\cos2Y,
\]

\[
\gamma_{xy}^0=0,\qquad N_{xy}=0.
\]

### C1

\[
\varepsilon_x^0
=
E_x+B_x\cos2X-C_q\cos2Y+H_x\cos2X\cos2Y,
\]

\[
\varepsilon_y^0
=
E_y-C_q\frac{b^2}{a_h^2}\cos2X+B_y\cos2Y+H_y\cos2X\cos2Y,
\]

\[
\gamma_{xy}^0
=
-\left(
\frac b{a_h}H_x+\frac{a_h}bH_y
\right)\sin2X\sin2Y.
\]

## 4. Gate 状态

### M0 — PASS

- compatible displacement basis：完成；
- strain basis：完成；
- compatibility identity：解析 PASS；
- C0/C1 generalized residual：完成。

### Gate 1 / M1 — PASS

在线弹性且 \(A^+=A^-=0\) 下：

\[
H_x=H_y=0
\]

为 C1 shear 子系统唯一解，并严格恢复 Chen–Ji/Airy \(N_{xy}=0\) 分离解。

### M2 — 正式实现中

已解析证明：

\[
q\neq0,\quad f''(e)\neq0
\]

时，UHPC nonlinear thickness integration 一般会产生：

\[
\cos2X\cos2Y
\]

mixed resultant，因此 C1 channel 一般被激活。

但预峰值独立核验表明其量级很小。

## 5. M2 semi-analytic active-set kernel

已经正式构造：

\[
\boxed{
\text{analytic material-boundary roots}
+
\text{exact thickness integration}
+
\text{exact }Y\text{ integration}
+
\text{one-dimensional }X\text{ integral}
}
\]

对固定 \(X\)：

\[
e_{\alpha m}
=
\mathcal A_\alpha+\mathcal B_\alpha\cos2Y,
\]

\[
\chi_\alpha
=
\mathcal D_\alpha\sin Y.
\]

令 \(s=\sin Y\)，任意表面材料阈值：

\[
e_{\alpha,\pm}=e_j
\]

严格变成二次方程：

\[
2\mathcal B_\alpha s^2
\mp\frac{t_c}{2}\mathcal D_\alpha s
-
(\mathcal A_\alpha+\mathcal B_\alpha-e_j)=0.
\]

因此 active-set boundary 为显式根。

厚度积分：

\[
N_j
=
\frac{F_j(e_b)-F_j(e_a)}{\chi},
\]

\[
M_j
=
\frac{
J_j(e_b)-J_j(e_a)
-e_m[F_j(e_b)-F_j(e_a)]
}{\chi^2}.
\]

固定 \(X\) 后，\(Y\) 积分退化为有限 Laurent polynomial 的：

\[
I_p=\int\sin^pY\,dY,
\]

最低只需要 \(p=-2\)，可完全解析。

最终正式 residual：

\[
G_i
=
\frac{4ba_h}{\pi^2}
\int_0^{\pi/2}\mathcal G_i(X)\,dX.
\]

因此正式理论已经不需要二维或三维 Gauss points。

## 6. semi-analytic 单状态交叉核验

BH060：

\[
b=a_h=3000\ {\rm mm},
\qquad q=0.001.
\]

semi-analytic：

\[
P_{C0}=4.762006709\ {\rm MN},
\]

\[
P_{C1}=4.762008362\ {\rm MN},
\]

\[
H_x=-1.35053\times10^{-7},
\qquad
H_y=6.18794\times10^{-8}.
\]

对应 C0 omitted residual：

\[
\widehat G_{H_x}=1.26319\times10^6\ {\rm N\,mm},
\]

\[
\widehat G_{H_y}=-6.71489\times10^3\ {\rm N\,mm}.
\]

与之前仅用于独立验证的 18×18 面内 Gauss 结果在 \(P\)、\(H_x\)、\(H_y\) 上一致到远小于工程相关量级。

结论：

\[
\boxed{
\text{semi-analytic active-set kernel 的单状态实现已交叉验证通过。}
}
\]

## 7. Gate 2 当前状态

还不能正式 PASS。

原因只剩：

\[
\boxed{
\text{必须用同一 formal semi-analytic kernel 跑完连续 }q\text{-path。}
}
\]

目前已经不是理论积分缺口，而是执行性能问题。

当前 prototype 的瓶颈：

1. 每个 residual component 重复执行同一个一维 \(X\) adaptive integral；
2. finite-difference Jacobian 重复这些积分；
3. 4×4 / 6×6 小矩阵求解本身不是瓶颈。

## 8. 当前代码

已创建：

current/code/UCFT_nonlinear_membrane_condensation_solver.py

功能：

- M2 pre-peak UHPC polynomial reference；
- active-set threshold roots；
- exact thickness primitives；
- exact \(Y\) Laurent integration；
- one-dimensional \(X\) residual；
- C0/C1 residual framework。

commit：

427d6e88779d0bfa3925c2ed2ced98546b63bd65

## 9. 当前 UHPC reference

M2 前峰值核验：

\[
f_t=7.2\ {\rm MPa},
\qquad
\varepsilon_{tp}=0.000200,
\]

使用满足：

\[
\sigma_t(0)=0,\quad
\sigma_t'(0)=E_c,\quad
\sigma_t(\varepsilon_{tp})=f_t,\quad
\sigma_t'(\varepsilon_{tp})=0
\]

的 cubic Hermite polynomial。

任何材料点达到 \(\varepsilon_{tp}\) 即停止 M2 pre-peak reference path，因此 M2 没有人工发明 tensile softening。

## 10. 计算算法检索结论

已按最高层合同检查 active-set / nonsmooth Newton 相关方法。

semismooth Newton / active-set 方法确实适合分段材料状态切换，但当前 profile 显示：

\[
\boxed{
\text{当前首要瓶颈不是 nonsmooth root，而是重复的一维外积分和 finite-difference Jacobian。}
}
\]

所以暂不为了“算法先进”引入 semismooth framework。

优化优先级保持：

\[
\boxed{
\text{vector-valued outer integration}
\rightarrow
\text{common-expression reuse}
\rightarrow
\text{consistent Jacobian}
}
\]

只有 active-set 切换真正导致 Newton 抖动时，再启用 semismooth Newton。

## 11. 唯一 NEXT_ACTION

保持 M2，不进入 M3。

将当前 solver 改为：

\[
\boxed{
\text{一次 }X\text{ sweep 同时返回全部 residual components}
}
\]

并减少 finite-difference Jacobian 对外层积分的重复调用。

然后用 formal semi-analytic kernel 完整计算 BH060、BH100 的 pre-tensile-peak C0/C1 连续 \(q\)-path，正式裁决 Gate 2。
