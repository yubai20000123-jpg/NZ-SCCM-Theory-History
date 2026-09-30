# UCFT 低维全过程半解析理论 — 执行日志

## 2026-09-30 13:31–14:06 +08:00

### A. 状态恢复

已读取：

- 用户上传最高层路线合同：指示词.md；
- Project / Library 中的解析化与极值迭代、陈骥/H1、UCFT 层0与材料文件；
- private GitHub：yubai20000123-jpg/NZ-SCCM-Theory-History；
- GitHub 原 current/CURRENT_STATE.md。

发现：

旧 current/CURRENT_STATE.md 仍停留在 2026-08-25 旧 NZ-SCCM 状态，已被当前《指示词.md》与 2026-09 最新项目状态 supersede。

当前路线恢复为：

single-q  
+ \(A^+,A^-\) slave local response  
+ nonlinear membrane condensation  
+ UHPC analytic tension/compression active set  
+ steel Mises deformation theory  
+ q-continuation.

### B. 本轮主任务

执行 M0 / M1，并继续推进 M2：

1. 正式建立 C0/C1 compatible membrane basis；
2. 完成 linear elastic Gate 1；
3. 开始审计 UHPC material nonlinearity 是否单独激活 C1 shear channel。

### C. M0 完成内容

已建立：

\[
X=\frac{\pi x}{b},\qquad
Y=\frac{\pi y}{a_h},
\]

\[
Q=q^2+2q_0q,
\qquad
C_q=\frac{\pi^2Q}{8}.
\]

完成 C1 compatible displacement basis：

\[
u(E_x,B_x,H_x;q),
\qquad
v(E_y,B_y,H_y;q),
\]

并严格得到：

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

逐项验证：

\[
\varepsilon_{x,yy}^0+
\varepsilon_{y,xx}^0-
\gamma_{xy,xy}^0
=
\frac{\pi^4Q}{2a_h^2}(\cos2X+\cos2Y).
\]

建立六个 inner generalized residual：

\[
G_{E_x},
G_{E_y},
G_{B_x},
G_{B_y},
G_{H_x},
G_{H_y}.
\]

M0：

\[
\boxed{\text{PASS}}
\]

### D. M1 / Gate 1

在线弹性、\(A^+=A^-=0\) 下：

\[
\bar\nu=\frac{A_{12}}{A_{11}},
\qquad
\bar K=A_{11}(1-\bar\nu^2).
\]

解析得到：

\[
B_x=\bar\nu C_q\frac{b^2}{a_h^2},
\qquad
B_y=\bar\nu C_q,
\]

\[
E_y=-\frac{P/b}{A_{11}(1-\bar\nu^2)},
\]

\[
E_x=\frac{\bar\nu P/b}{A_{11}(1-\bar\nu^2)}.
\]

膜力：

\[
N_x=-\bar K C_q\cos2Y,
\]

\[
N_y=-\frac Pb-\bar K C_q\frac{b^2}{a_h^2}\cos2X,
\]

\[
N_{xy}=0.
\]

C1 shear 子系统行列式：

\[
A_{11}^2(1-\bar\nu)
\left[1+\frac12(r^2+r^{-2})\right]>0,
\]

因此：

\[
H_x=H_y=0
\]

为唯一解。

结论：

\[
\boxed{\text{Gate 1 / M1 = PASS}}
\]

### E. M2 解析进展

对多项式材料分支：

\[
\sigma=f(e),
\qquad
e=e_m+z\chi,
\]

精确厚度展开：

\[
N
=
tf(e_m)
+
\frac{t^3\chi^2}{24}f''(e_m)
+
\frac{t^5\chi^4}{1920}f^{(4)}(e_m)
+
\frac{t^7\chi^6}{322560}f^{(6)}(e_m).
\]

由于：

\[
\chi=\chi_0\sin X\sin Y,
\]

且：

\[
\sin^2X\sin^2Y
=
\frac14(1-\cos2X-\cos2Y+\cos2X\cos2Y),
\]

只要：

\[
q\neq0,\qquad f''\neq0,
\]

nonlinear UHPC current resultant 一般会出现 \(\cos2X\cos2Y\) mixed harmonic。

因此：

\[
\boxed{
\widehat G_{H_x},\widehat G_{H_y}
\text{ 一般不再严格为零。}
}
\]

说明 UHPC material nonlinearity 本身可以激活 C1 channel。

### F. M2 独立数值核验

只为验证量级，使用：

- UHPC 厚度方向：按 \(e=0\) 显式分区，分段多项式 exact integration；
- steel-local：关闭；
- 两层钢壳：线弹性；
- UHPC compression：当前六次多项式；
- Gate 2 reference tension：\(f_t=7.2\) MPa、\(\varepsilon_{tp}=0.0002\)，构造前峰值 cubic Hermite polynomial；
- 面内积分：临时 18×18 Gauss–Legendre。

因为最后一项违反正式理论“不得以二维 Gauss 定义 residual”的合同，所以这组结果只作为 independent numerical verification，不用于正式 PASS Gate 2。

BH060：

- \(q=0.001\)：
  - \(P_{C0}=4.762006642\) MN；
  - \(P_{C1}=4.762008289\) MN；
  - \(H_x=-1.35054\times10^{-7}\)；
  - \(H_y=6.18798\times10^{-8}\)；
  - relative \(P\) difference \(=3.46\times10^{-5}\%\).

- 接近 reference tensile peak，\(q\approx0.00180020\)：
  - \(P_{C0}=7.001686213\) MN；
  - \(P_{C1}=7.001517755\) MN；
  - \(H_x=5.12849\times10^{-7}\)；
  - \(H_y=-2.27504\times10^{-7}\)；
  - relative \(P\) difference \(=-0.002406\%\).

BH100：

- \(q=0.001\)：
  - \(P_{C0}=2.936723791\) MN；
  - \(P_{C1}=2.936717693\) MN；
  - relative difference \(=-2.08\times10^{-4}\%\).

- 接近 reference tensile peak，\(q\approx0.00305498\)：
  - \(P_{C0}=5.925417195\) MN；
  - \(P_{C1}=5.925289383\) MN；
  - \(H_x=4.39023\times10^{-7}\)；
  - \(H_y=-1.98558\times10^{-7}\)；
  - relative difference \(=-0.002157\%\).

当前证据：

\[
\boxed{
\text{C1 被激活，但 pre-peak correction 极小；C0 很可能是有效低阶模型。}
}
\]

正式状态：

\[
\boxed{\text{Gate 2 = PENDING}}
\]

唯一缺口是把临时面内 Gauss verification 换成最高层合同要求的 semi-analytic active-set area integration。

### G. 本轮发现的问题及处理

#### 1. GitHub LaTeX escape corruption

首次通过 JavaScript template string 写 GitHub 时，反斜杠序列被 JavaScript 当作 escape，导致部分 LaTeX 出现 control characters。

级别：

\[
\boxed{\text{需要修正，但不影响力学推导本身}}
\]

已经：

- 保留首次 timestamp backup，不覆盖历史；
- 使用 String.raw 重写 stable derivation/state 文件；
- 后续所有含 LaTeX 的 GitHub 写入必须使用 raw string。

#### 2. M2 / M4 实现依赖

M2 要正式给出 C0/C1 \(P(q)\) 路径，但正式 residual 不能由二维 Gauss 定义；因此必须实现 active-set semi-analytic area kernel。

这不是新增 Gate，也不是路线改变，只是 M2 正式闭合所需的 M4 最小实现依赖。

### H. Gate status

- M0: PASS
- Gate 1 / M1: PASS
- Gate 2 / M2: PENDING formal semi-analytic area integration
- Gate 3 / M3: NOT RUN

### I. NEXT_ACTION

继续 M2，不进入 M3：

实现：

\[
\boxed{
\text{analytic active-set boundary}
+
\text{exact thickness integration}
+
\text{at most one-dimensional definite integral}
}
\]

替换临时二维 Gauss verification，然后重跑同一 C0/C1 \(q\)-path，并正式裁决 Gate 2。


---

## 2026-09-30 14:06 +08:00 — M2 formal semi-analytic kernel advance

### task

把 M2 临时二维面内 Gauss verification 替换为合同允许的 semi-analytic active-set residual。

### completed

对固定 \(X\) 证明：

\[
e_{\alpha m}
=
\mathcal A_\alpha+\mathcal B_\alpha\cos2Y,
\qquad
\chi_\alpha=\mathcal D_\alpha\sin Y.
\]

令 \(s=\sin Y\) 后，所有厚度表面材料阈值都变成二次方程，因此 active-set boundaries 可显式求根。

厚度方向采用 exact polynomial primitives：

\[
N_j
=
\frac{F_j(e_b)-F_j(e_a)}{\chi},
\]

\[
M_j
=
\frac{J_j(e_b)-J_j(e_a)-e_m[F_j(e_b)-F_j(e_a)]}{\chi^2}.
\]

在固定 active pattern 中，\(N,M\) 成为有限 \(\sin^pY\) Laurent polynomial，最低 \(p=-2\)。

使用：

\[
I_{-1}=\ln\tan(Y/2),
\qquad
I_{-2}=-\cot Y
\]

及正整数递推，\(Y\) 方向完全解析积分。

最终只保留：

\[
X\in[0,\pi/2]
\]

一个一维 adaptive definite integral。

因此正式 M2 residual 不再依赖二维/三维 Gauss points。

### single-state formal cross-check

BH060：

\[
b=a_h=3000\ {\rm mm},
\quad q=0.001.
\]

semi-analytic C0：

\[
P=4.762006709\ {\rm MN}.
\]

semi-analytic C1：

\[
P=4.762008362\ {\rm MN}.
\]

\[
H_x=-1.35053\times10^{-7},
\qquad
H_y=6.18794\times10^{-8}.
\]

与此前 18×18 面内 Gauss independent verification 基本完全一致。

所以：

\[
\boxed{
\text{formal semi-analytic kernel single-state cross-check = PASS}
}
\]

### code

created:

current/code/UCFT_nonlinear_membrane_condensation_solver.py

commit:

427d6e88779d0bfa3925c2ed2ced98546b63bd65

### performance finding

连续多点 semi-analytic trace 的首次执行出现运行时间过长。

profile 结论：

- 4×4 / 6×6 solve 不是瓶颈；
- 同一 residual evaluation 对不同分量重复执行 \(X\) adaptive integral 是主要成本；
- finite-difference Jacobian 进一步重复这些积分。

按路线合同，当前不引入大型矩阵算法。

最小等价加速：

1. vector-valued \(X\) quadrature；
2. residual component 共用 active-set / Laurent expansion；
3. consistent Jacobian 或至少复用 active-set 的差分 Jacobian。

### algorithm literature check

已检索 semismooth Newton / active-set literature。

结论：

semismooth Newton 对 piecewise / active-set nonlinear equations 有严谨基础，但当前根本瓶颈是 quadrature/Jacobian 重复计算，而不是 active-set nondifferentiability。

所以当前：

\[
\boxed{\text{不引入 semismooth Newton；只记录为后备。}}
\]

### Gate status

- M0 PASS
- Gate 1 PASS
- M2 single-state semi-analytic kernel PASS
- Gate 2 full path PENDING
- Gate 3 NOT RUN

### NEXT_ACTION

保持 M2：

把 outer \(X\) integration 向量化，使一次 X sweep 同时返回全部 residual components，并减少 Jacobian 的重复积分；随后跑完 BH060、BH100 pre-tensile-peak C0/C1 连续 q-path，正式判定 Gate 2。
