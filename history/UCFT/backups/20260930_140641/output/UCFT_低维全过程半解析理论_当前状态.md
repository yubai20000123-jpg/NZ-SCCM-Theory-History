# UCFT 低维全过程半解析理论 — 当前状态

**更新时间：2026-09-30 13:31 +08:00**  
**最高层路线合同：用户上传《指示词.md》**  
**当前主攻方向：nonlinear membrane condensation**

## 1. 当前结构级变量

路径参数：

\[
q.
\]

每个给定 \(q\) 的外层未知量：

\[
P,\qquad A^+,\qquad A^-.
\]

统一端缩 \(\Delta\) 不再是路径控制量。端部位移、平均端缩和 RP 位移均在平衡后恢复。

## 2. 当前整体几何

\[
W_0=bq_0\sin\frac{\pi x}{b}\sin\frac{\pi y}{a_h},
\]

\[
W=b(q_0+q)\sin\frac{\pi x}{b}\sin\frac{\pi y}{a_h},
\]

\[
Q(q)=q^2+2q_0q.
\]

## 3. steel-local

\[
W_s^+=W+(A_0^++A^+)\psi_\ell^+,
\]

\[
W_s^-=W-(A_0^-+A^-)\psi_\ell^-.
\]

后续必须保留 \(qA\)、\(A^2\) 及初始缺陷交叉项。

## 4. PBL / 加劲肋

不作为独立轴向力、弹簧、自由度或材料模块。

\[
\chi_w
=
1+\frac{A_w}{bt_c}
\left(\frac{E_s}{E_c}-1\right),
\]

\[
P_{\rm report}
=
\chi_wP_c+P_s^++P_s^-.
\]

该项是 engineering reaction correction，不反向定义 \(q,A^\pm\)。

## 5. C0 / C1 membrane condensation

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

inner variables：

\[
E_x,E_y,B_x,B_y.
\]

### C1

增加：

\[
H_x,H_y,
\]

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

inner residual：

\[
G_{E_x},G_{E_y},G_{B_x},G_{B_y},G_{H_x},G_{H_y}=0.
\]

## 6. Gate 状态

### M0 — PASS

- C0/C1 compatible displacement basis 已建立；
- compatibility identity 已解析验证；
- 六个 inner residual 已建立。

### Gate 1 / M1 — PASS

在线弹性、\(A^+=A^-=0\) 下解析证明：

\[
H_x=H_y=0
\]

为 C1 shear 子系统唯一解，并严格恢复 Chen–Ji/Airy \(N_{xy}=0\) 分离解。

### Gate 2 / M2 — 未正式通过，但已取得明确中间结论

解析证明：

只要 UHPC normal law 非线性且 \(q\neq0\)，厚度 nonlinear bending-membrane coupling 一般会产生：

\[
\cos2X\cos2Y
\]

mixed resultant，因此：

\[
\widehat G_{H_x},\widehat G_{H_y}
\]

一般不再严格为零。

也就是说：

\[
\boxed{\text{material nonlinearity generically activates the C1 channel.}}
\]

但独立数值核验（exact thickness active-set + 临时 18×18 面内 Gauss，只用于验证、不是正式 residual）显示，在 pre-tensile-peak 参考区间 C1 correction 很小。

BH060：
- \(q=0.001\)：C0/C1 \(P\) 相对差 \(3.46\times10^{-5}\%\)；
- 接近 tensile peak：相对差 \(-0.002406\%\)；
- \(|H|\) 约 \(10^{-7}\sim10^{-6}\)。

BH100：
- \(q=0.001\)：相对差 \(-2.08\times10^{-4}\%\)；
- 接近 tensile peak：相对差 \(-0.002157\%\)；
- \(|H|\) 约 \(10^{-7}\sim10^{-6}\)。

因此当前证据：

\[
\boxed{
\text{C1 被激活，但 pre-peak 很弱；C0 很可能是有效降阶。}
}
\]

正式 Gate 2 仍为：

\[
\boxed{\text{PENDING}}
\]

唯一原因是正式 residual 必须将临时二维 Gauss 面积分替换成合同要求的 semi-analytic active-set area integration。

### Gate 3 / M3 — 未执行

必须等正式 Gate 2 闭合后，再打开 \(A^\pm\) 做 mixed-harmonic omitted residual spectrum。

## 7. M2 reference UHPC law

压缩：

\[
E_c=43.4\ {\rm GPa},
\quad
f_c=141.1\ {\rm MPa},
\quad
\varepsilon_{c0}=0.0035,
\]

采用当前六次多项式。

独立 Gate 2 前峰值核验的拉伸 reference：

\[
f_t=7.2\ {\rm MPa},
\qquad
\varepsilon_{tp}=0.000200.
\]

采用满足原点斜率 \(E_c\)、峰值应力和峰值零切线的 cubic Hermite polynomial，并在任一点达到 \(\varepsilon_{tp}\) 时停止；因此没有在 M2 中人为发明峰后软化。

该 reference 仅用于 Gate 2，不等于最终 M8 材料定稿。

## 8. steel 当前材料合同

正式主线仍是：

Chen–Ji-style Mises deformation theory  
+ equivalent uniaxial polynomial  
+ \(E_{\rm sec}/E_{\rm tan}\).

M2 为隔离 UHPC material nonlinearity，关闭 steel-local 并保持两层钢壳线弹性。

## 9. 已记录但不阻塞的边界审计

当前最低阶 C0/C1 displacement basis 与 Chen–Ji straight-edge 退化一致。

由于最终理论不允许统一端缩作为外部控制，后续 nonlinear Gate 2/3 应监测 end-warping omitted residual；只有显著时才增加 compatible enrichment。

## 10. 当前唯一 NEXT_ACTION

不进入 M3。

先完成正式 Gate 2 所依赖的最小 semi-analytic active-set kernel：

\[
\boxed{
\text{显式材料分区}
+
\text{exact thickness integration}
+
\text{最多一维确定积分}
}
\]

并用它替换临时 18×18 面内 Gauss verification，再重新计算 C0/C1 \(P(q)\)、\(H_x,H_y\) 和 omitted residual。

完成后才正式裁决 Gate 2。
