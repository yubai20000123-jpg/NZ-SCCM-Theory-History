# NZ-SCCM / UCFT 运动学函数效应分解与下一聊天交接
## 时间：2026-09-07 17:29 +08:00
## 身份：CURRENT_STATE + ANALYSIS_LEDGER + NEXT_CHAT_ENTRY
## 目的：完整保存本聊天中的方法修正、已执行结果、失败原因、当前未闭合问题，以及下一聊天唯一优先研究方向。

---

# 0. 用户本轮最终纠偏

用户指出：当前研究再次有“跑偏”迹象。与其继续在 current operator、平衡闭合或某个已组合运动学上逐层补丁，不如回到最基础的问题：

\[
\boxed{
\text{单个函数到底对 }q,\varepsilon,\kappa,\text{虚功和平衡各产生什么作用？}
}
\]

例如分别研究：

\[
\sin X,
\qquad
\cos Y,
\qquad
\sin X\cos Y,
\]

或者其他非三角函数，再研究这些函数组合后是否能够生成我们需要的极限状态。

这里的核心不是“穷举所有函数”，而是：

\[
\boxed{
\text{先建立单个基函数的力学作用图谱，再按目标状态所需的作用签名进行最小组合。}
}
\]

这是下一聊天的第一优先级。

---

# 1. 研究纪律

## 1.1 FEM 标准答案可以看，但不能决定公式系数

FEM 允许用于：
- 判断一个候选函数能改变哪些指标；
- 判断作用方向是否正确；
- 识别缺失机制；
- 决定下一种函数“类型”。

禁止：
- 根据 FEM 反求固定系数；
- 逐件参数；
- 用总 loss 拟合函数；
- 因某个组合经过 FEM 状态就直接锁定。

所有非输入常数必须是：
1. 数学必然常数；
2. 边界/归一化推导常数；
3. 广义未知量，由力学方程求。

---

# 2. 固定几何与坐标

理论坐标：

\[
x=\text{板面横向},\qquad
y=\text{轴压方向},\qquad
z=\text{厚度方向}.
\]

代表完整半波：

\[
0\le x\le b,\qquad
0\le y\le a_h,
\]

九个 BH 试件均：

\[
a=2b,\qquad m=2,\qquad a_h=b.
\]

因此：

\[
\alpha=\frac{\pi}{b},
\qquad
\beta=\frac{\pi}{a_h}=\frac{\pi}{b}.
\]

定义无量纲坐标：

\[
X=\alpha x\in[0,\pi],
\qquad
Y=\beta y\in[0,\pi].
\]

九件宽度：

| Case | b / mm |
|---|---:|
| BH005 | 250 |
| BH010 | 500 |
| BH020 | 1000 |
| BH032 | 1600 |
| BH050 | 2500 |
| BH060 | 3000 |
| BH070 | 3500 |
| BH085 | 4250 |
| BH100 | 5000 |

统一：

\[
t_s=4\ {\rm mm},
\qquad
t_c=42\ {\rm mm},
\qquad
A_w=1332\ {\rm mm^2},
\qquad
z_f=23\ {\rm mm}.
\]

初始缺陷：

\[
\boxed{
w_0=bq_0\sin X\sin Y
}
\]

\[
q_0=0.0025.
\]

初始缺陷为无应力参考几何。

---

# 3. 固定二阶几何

任意新增位移：

\[
u(x,y),\quad v(x,y),\quad w(x,y)
\]

总几何：

\[
W=w_0+w.
\]

中面应变：

\[
\boxed{
\varepsilon_x^0=
u_{,x}
+\frac12(W_{,x}^2-w_{0,x}^2)
}
\]

\[
\boxed{
\varepsilon_y^0=
v_{,y}
+\frac12(W_{,y}^2-w_{0,y}^2)
}
\]

\[
\boxed{
\gamma_{xy}^0=
u_{,y}+v_{,x}
+
W_{,x}W_{,y}
-
w_{0,x}w_{0,y}
}
\]

曲率严格由新增 \(w\) 得：

\[
\boxed{
\kappa_x=-w_{,xx},\qquad
\kappa_y=-w_{,yy},\qquad
\kappa_{xy}=-2w_{,xy}.
}
\]

---

# 4. FEM 标准答案

## 4.1 极限荷载

| Case | Pu_FEM / MN |
|---|---:|
| BH005 | 2.297254 |
| BH010 | 4.330169 |
| BH020 | 7.908734 |
| BH032 | 10.884984 |
| BH050 | 12.572657 |
| BH060 | 13.090110 |
| BH070 | 13.194333 |
| BH085 | 14.163914 |
| BH100 | 15.454080 |

## 4.2 主整体幅值 q

| Case | q_FEM |
|---|---:|
| BH005 | 0.000129291 |
| BH010 | 0.000296389 |
| BH020 | 0.001301677 |
| BH032 | 0.00313099* |
| BH050 | 0.00516361 |
| BH060 | 0.005948088 |
| BH070 | 0.008800497 |
| BH085 | 0.012476594 |
| BH100 | 0.016590569 |

BH032 的 q 是 curvature proxy，弱于 direct U2 projection。

## 4.3 轴向中面宽向系数

以 FEM 居中宽向坐标：

\[
x_c\in[-B/2,B/2]
\]

定义：

\[
\varepsilon_y^0(x_c)
\simeq
c_{0y}
+
c_{1y}\cos\frac{2\pi x_c}{B}
+\cdots
\]

| Case | c0y | c1y |
|---|---:|---:|
| BH005 | -0.004121839 | -0.000533485 |
| BH010 | -0.004199984 | -0.000174585 |
| BH020 | -0.003873082 | +0.000038197 |
| BH032 | -0.002401505 | +0.000222541 |
| BH050 | -0.001585596 | +0.000248830 |
| BH060 | -0.001380880 | +0.000246876 |
| BH070 | -0.001196020 | +0.000335384 |
| BH085 | -0.001089734 | +0.000477785 |
| BH100 | -0.001019018 | +0.000595731 |

## 4.4 横向中面宽向系数

\[
\varepsilon_x^0(x_c)
\simeq
c_{0x}
+
c_{1x}\cos\frac{2\pi x_c}{B}
+\cdots
\]

| Case | c0x | c1x |
|---|---:|---:|
| BH005 | +0.001869891 | +0.000606729 |
| BH010 | +0.001809173 | +0.000318964 |
| BH020 | +0.001657621 | +0.000229721 |
| BH032 | +0.000707902 | -0.000055645 |
| BH050 | +0.000388887 | -0.000072937 |
| BH060 | +0.000316300 | -0.000085378 |
| BH070 | +0.000255925 | -0.000096744 |
| BH085 | +0.000178798 | -0.000140317 |
| BH100 | +0.000108470 | -0.000187101 |

## 4.5 峰值法向曲率

| Case | kappa_peak_FEM / mm^-1 |
|---|---:|
| BH050 | 1.8397435e-5 |
| BH060 | 1.5103622e-5 |
| BH070 | 1.7579194e-5 |
| BH085 | 2.4709157e-5 |
| BH100 | 3.1254821e-5 |

BH060–BH100 provenance 更一致。

## 4.6 峰值受力分担

| Case | UHPC | steel | web |
|---|---:|---:|---:|
| BH005 | 47.99% | 29.68% | 22.33% |
| BH010 | 56.59% | 31.57% | 11.85% |
| BH020 | 60.47% | 33.20% | 6.33% |
| BH032 | 65.52% | 29.95% | 4.53% |
| BH050 | 62.14% | 34.38% | 3.48% |
| BH060 | 61.74% | 35.26% | 3.00% |
| BH070 | 62.70% | 34.63% | 2.66% |
| BH085 | 64.48% | 33.28% | 2.24% |
| BH100 | 66.89% | 31.26% | 1.85% |

---

# 5. 一个重要的坐标纠错

程序常用：

\[
x\in[0,B].
\]

FEM 表使用：

\[
x_c=x-B/2.
\]

因此：

\[
\boxed{
\cos\frac{2\pi x_c}{B}
=
-\cos\frac{2\pi x}{B}
}
\]

即程序若拟合：

\[
\hat c_1\cos2\alpha x,
\]

与 FEM 表比较必须用：

\[
\boxed{
c_1^{FEM\ coordinate}=-\hat c_1.
}
\]

R04 第一、二轮曾遗漏这个相位转换，造成若干错误的“反号”诊断；第三轮已纠正。

---

# 6. 已执行运动学轮次及真实结论

## 6.1 C1：单正弦面外 + 平均面内

\[
w=bq\sin X\sin Y,
\]

\[
u=\bar\varepsilon_xx,
\qquad
v=-Dy.
\]

重要事实：
- BH100 在 FEM q 下标准正弦峰曲率仅约 +4.8%；
- BH060 标准正弦峰曲率约 +29.6%；
- 所以至少 BH100 的主要缺口不是面外主函数本身；
- corrected centered coordinate 后，C1 的 \(c_{1y}\) 对 BH060/BH100 是正确正号，不是之前误判的反号；
- 但 P(q) 在 FEM q 后继续增长，没有自然极限点。

## 6.2 C2：加入第三谐波 q3

\[
w=b\sin X[q_1\sin Y+q_3\sin3Y].
\]

\(q_3\) 由广义虚功求。

结果：
- current mechanics 自行选择的 q3 往往使峰值曲率更尖，而不是压平；
- BH060/BH100 的峰曲率显著恶化；
- 说明“第三谐波”作为单独形状补充不自动解决目标。

## 6.3 C3/C4：cross in-plane harmonic

核心对子：

\[
u_c\sim\sin2X\cos2Y,
\]

\[
v_c\sim\cos2X\sin2Y.
\]

在 corrected centered coordinate 下：
- BH060 的 C4 \(c_{1x}\) 已很接近 FEM；
- \(c_{1y}\) 方向正确但幅值不足；
- 说明这个 cross harmonic 不是错误方向，反而是有用成分；
- 但荷载仍偏低，极限点不在 FEM q。

## 6.4 C5：强制 shear-free

强制：

\[
A_u=-A_v
\]

以消除线性 shear。

结果：
- 连续物理解很快丢失；
- 会跳到巨大非物理解；
- 约束过强，否决。

## 6.5 C6：多项式轴向相位

测试：

\[
v_c
=
A_v a_h\eta(1-\eta)(2\eta-1)\cos2X.
\]

结果对面积积分阶数高度敏感，连 \(c_{1y}\) 符号都会变，否决。

## 6.6 C7：所谓“最低阶 Fourier closure”

\[
u=
\bar\varepsilon_xx+
\frac{U_{20}}{2\alpha}\sin2X+
\frac{U_{22}}{2\alpha}\sin2X\cos2Y,
\]

\[
v=
-Dy+
\frac{V_{02}}{2\beta}\sin2Y+
\frac{V_{22}}{2\beta}\cos2X\sin2Y.
\]

结果：
- 高阶积分稳定；
- BH100 的 \(c_{1y}\) 与曲率已经比较接近；
- 但 \(c_{0x}\) 错、\(c_{1x}\) 不足、steel 分担偏高；
- P(q) 仍持续增长。
- 后来发现 C7 并不真正“完整”，因为没有给几何 forcing 中 pure \(\cos2Y\) 横向应变一个独立出口。

## 6.7 C8：C7 + U02

新增：

\[
u_{02}
=
U_{02}(x-b/2)\cos2Y.
\]

结果：
- BH060 的 \(c_{0x}\) 从负推到略正，证明 U02 方向有作用；
- BH100 的 \(c_{1x}\) 明显改善；
- 但平均横向应变仍不够、c1y 仍不足、steel 分担仍高；
- P(q) 仍不在 FEM q 附近形成峰值；
- 因此继续堆更多面内 Fourier 坐标没有充分依据。

---

# 7. 第五轮 current normal coupling 审计

当前 UHPC normal current resultant 是方向分离的一维 operator：

\[
N_x^U=N_x^U(\varepsilon_x,\kappa_x),
\]

\[
N_y^U=N_y^U(\varepsilon_y,\kappa_y).
\]

因此 current nonlinear 层没有显式：

\[
\partial N_x^U/\partial\varepsilon_y.
\]

但输入材料有：

\[
\nu_c=0.20.
\]

为诊断这一点，测试了无 FEM 拟合的 Nguyen / Darwin–Pecknold 型最低阶 equivalent-strain coupling：

固定轴版本：

\[
\tilde\varepsilon_x
=
\frac{\varepsilon_x+\nu_c\varepsilon_y}{1-\nu_c^2},
\]

\[
\tilde\varepsilon_y
=
\frac{\varepsilon_y+\nu_c\varepsilon_x}{1-\nu_c^2}.
\]

又测试了 principal-strain 版本。

结论：
- normal coupling 确实改善部分 \(c_{0x}\)、\(c_{1x}\)；
- principal rotation 不是主要误差源；
- 但不同试件荷载改善不一致；
- P(q) 依然在 FEM q 后继续增长；
- 因此 Poisson normal coupling 是真实材料缺口，但不是“极限点不出现”的单一根因。

---

# 8. 当前极限路径的重要事实

即使使用不同低维运动学和最低阶 normal coupling：

BH060、BH100 的：

\[
P(q)
\]

通常在：

\[
q=q_{FEM}
\]

之后仍然继续增加。

例如某轮 BH100：

\[
q/q_F=1.0 \Rightarrow P\approx12.25,
\]

\[
1.30 \Rightarrow P\approx15.07,
\]

\[
1.50 \Rightarrow P\approx16.67,
\]

继续增大。

这意味着理论可能“经过”正确荷载值，但并未把那里识别为极限点。

因此用户明确提醒：

\[
\boxed{
\text{不能因为路过正确荷载，就说找到了正确极限点。}
}
\]

---

# 9. q-work 分解的已有诊断

在固定 FEM 的 \(P,q\) 附近，对 C4 的非-q 内部变量求平衡后检查 \(R_q\)。

BH060 的 q-work 约分解为：

\[
R_q^{N_x}=+4.11,
\]

\[
R_q^{N_y}=-86.63,
\]

\[
R_q^{N_{xy}}=+0.18,
\]

\[
R_q^{M_x}=+14.06,
\]

\[
R_q^{M_y}=+11.75,
\]

\[
R_q^{M_{xy}}=+28.75.
\]

总：

\[
R_q\approx-27.79.
\]

BH100：

\[
+43.20-92.50+1.91+15.29+15.19+28.90
\approx+11.99.
\]

这说明正确 FEM 极限附近的广义功确实是：

\[
\boxed{
N_y\text{ 二阶几何功}
\leftrightarrow
M_x+M_y+M_{xy}\text{ 抗力功}
}
\]

的大量抵消。

但用户认为当前研究再次容易被“平衡模型”吸走注意力；下一聊天优先回到更基础的“函数作用”分解。

---

# 10. 下一聊天新的唯一优先方向：FUNCTION EFFECT ATLAS

不要先假设完整的 \(u,v,w\) 组合。

先把候选函数拆成“单个基函数”，逐个研究它经过微分、二阶几何和虚功后会产生什么。

建议无量纲坐标：

\[
X=\alpha x,\qquad Y=\beta y.
\]

对每一个基函数 \(\phi(X,Y)\)，建立完整 `FUNCTION CARD`。

---

# 11. 每个 FUNCTION CARD 必须回答

## A. 数学身份

例如：

\[
\phi=\sin X,
\quad
\phi=\cos Y,
\quad
\phi=\sin X\cos Y,
\]

或非三角函数：

\[
\phi=X(\pi-X),
\]

\[
\phi=Y(\pi-Y),
\]

\[
\phi=X(\pi-X)Y(\pi-Y),
\]

\[
\phi=\sin^p X,
\]

\[
\phi=\exp[-a(X-\pi/2)^2],
\]

等等。

若函数有形状参数 \(p,a\)，参数必须作为广义未知或由数学归一化决定，不能 FEM 拟合。

## B. 可放在哪个场

分别检查：

\[
u\leftarrow A\phi,
\qquad
v\leftarrow A\phi,
\qquad
w\leftarrow bq\phi.
\]

不是所有函数都适合三个场。

## C. 边界相容性

检查：
- \(w=0\) 边界；
- 轴向端缩修正是否为零；
- 横向自由边是否合理；
- 刚体模态；
- 中心对称/反对称。

## D. 一阶导数签名

若放入 \(u\)：

\[
u_{,x},u_{,y}
\]

分别影响：

\[
\varepsilon_x,\gamma_{xy}.
\]

若放入 \(v\)：

\[
v_{,y},v_{,x}
\]

分别影响：

\[
\varepsilon_y,\gamma_{xy}.
\]

若放入 \(w\)：

\[
w_{,x},w_{,y}
\]

通过二次项产生：

\[
\varepsilon_x^g,\varepsilon_y^g,\gamma_{xy}^g.
\]

## E. 二阶导数签名

若放入 \(w\)：

\[
-w_{,xx}\rightarrow\kappa_x,
\]

\[
-w_{,yy}\rightarrow\kappa_y,
\]

\[
-2w_{,xy}\rightarrow\kappa_{xy}.
\]

必须明确：
- 是否改变中心峰值 q；
- 是否改变 \(\kappa_y/q\)；
- 是否同时恶化 \(\kappa_{xy}\)；
- 是否只改变节点/中心/边缘。

## F. Fourier / parity signature

把函数及其导数投影到：

\[
1,\cos2X,\cos2Y,\cos2X\cos2Y,\sin2X\sin2Y,\ldots
\]

看它能控制：

\[
c_{0x},c_{1x},c_{0y},c_{1y}
\]

中的哪一个。

## G. 广义功签名

定义：

\[
R_A
=
\int_\Omega
\mathbf s^T
\frac{\partial\mathbf e}{\partial A}
dA.
\]

拆成：

\[
R_A^{N_x},
R_A^{N_y},
R_A^{N_{xy}},
R_A^{M_x},
R_A^{M_y},
R_A^{M_{xy}}.
\]

看该基函数主要由哪个 current channel 驱动。

## H. 目标作用向量

为每个函数形成一个定性/半定量向量，例如：

```text
q_peak       : 0
c0x          : +
c1x          : --
c0y          : 0
c1y          : +
kappa_x      : 0
kappa_y      : 0
kappa_xy     : 0
shear_cost   : high
boundary     : admissible
```

这就是函数的“力学指纹”。

---

# 12. 第一批应优先研究的单函数，不要一上来组合

## 12.1 面外基本函数

### W-A

\[
\phi_{11}=\sin X\sin Y.
\]

这是基准。

### W-B

\[
\phi_{10}=\sin X.
\]

研究它：
- 能否代表沿 y 更均匀的鼓曲；
- 会造成什么端部边界问题；
- 对 \(\kappa_y\) 为零，对 \(\kappa_x\) 非零；
- 能否作为“降低 \(\kappa_y/q\)”的自然方向。

### W-C

\[
\phi_{01}=\sin Y.
\]

对应反方向作用。

### W-D

\[
\phi_{1c}=\sin X\cos Y.
\]

重点检查：
- 它在 y=0,\pi 不为零，不能直接作为简支 w；
- 但可能适合 slope/derivative correction 或乘 envelope 后使用。

### W-E

\[
\phi_{13}=\sin X\sin3Y.
\]

已有 q3 结果提示 current mechanics 会把它选向锐化方向，但仍要在函数图谱中保留其作用签名，不直接永久忘记。

## 12.2 面内 u 函数

研究最简单：
- \(x_c\)；
- \(\sin2X\)；
- \(x_c\cos2Y\)；
- \(\sin2X\cos2Y\)；
- 非三角 \(x_c\,Y(\pi-Y)\)。

逐个记录它对：
\[
\varepsilon_x,\gamma_{xy}
\]
的作用，而不是先组合。

## 12.3 面内 v 函数

研究：
- \(y\)（平均 D）；
- \(\sin2Y\)；
- \(\cos2X\sin2Y\)；
- \(Y(\pi-Y)\cos2X\)；
- \(Y(\pi-Y)(2Y-\pi)\cos2X\)。

逐个研究：
\[
\varepsilon_y,\gamma_{xy}
\]
签名。

---

# 13. 不限于三角函数：建议函数族

每一种都先单独研究作用，不直接大组合。

## 13.1 polynomial envelope

\[
X(\pi-X),
\qquad
Y(\pi-Y).
\]

## 13.2 symmetric bump

\[
X(\pi-X)[1+a(X-\pi/2)^2].
\]

\(a\) 若使用必须由力学求。

## 13.3 power-sine

\[
\sin^p X,
\qquad
\sin^p Y.
\]

\(p\) 为 shape DOF。

## 13.4 rational/beta-like shape

\[
[X(\pi-X)]^p.
\]

## 13.5 localized smooth bump

例如：

\[
e^{-a(X-\pi/2)^2}
\]

但必须乘满足边界的 envelope，如：

\[
X(\pi-X)e^{-a(X-\pi/2)^2}.
\]

## 13.6 orthogonal polynomial on [0,\pi]

例如 shifted Legendre/Chebyshev，再乘边界 envelope。

这些函数的目的不是“更多”，而是提供与三角函数不同的：
- 峰顶平坦度；
- 边界斜率；
- 曲率分布；
- 局部化程度。

---

# 14. 下一聊天禁止直接做的事

不要一开始就：
- 再设计完整 C9/C10；
- 再修 UHPC；
- 再推新的极限效率系数；
- 再把所有虚功问题整体求一遍；
- 再用 FEM 反求函数系数。

第一阶段只做：

\[
\boxed{
\text{FUNCTION EFFECT DECOMPOSITION}
}
\]

先得到一个函数—作用矩阵。

---

# 15. 推荐输出：FUNCTION–EFFECT MATRIX

行 = 基函数。

列至少包括：

| function | field | BC | eps_x | eps_y | gamma_xy | kappa_x | kappa_y | kappa_xy | c0x | c1x | c0y | c1y | q_peak | shear_cost | dominant_work |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

然后结合 FEM 目标签名，做“最小覆盖”：

例如若目标需要：
- \(c_{1y}\uparrow\)
- \(c_{1x}<0\)
- \(\kappa_y/q\downarrow\)
- 不显著增加 \(\gamma_{xy}\)

就从 atlas 中选 2–3 个互补函数，而不是盲试几十种组合。

---

# 16. 下一聊天第一句话应直接执行

建议新聊天直接写：

> 读取 GitHub 最新 `20260907_1729__NZSCCM__KINEMATIC_FUNCTION_EFFECT_DECOMPOSITION_NEXT_CHAT_HANDOFF_R01.md`。不要继续第五轮的 current-operator / 极限平衡主线。先按 handoff 第 10–15 节执行 FUNCTION EFFECT ATLAS：以无量纲 \(X=\alpha x,Y=\beta y\) 为坐标，逐个分析最简单的 \(w,u,v\) 基函数对 \(\varepsilon_x,\varepsilon_y,\gamma_{xy},\kappa_x,\kappa_y,\kappa_{xy},c_0,c_1\) 和广义功通道的影响；先做单函数，不组合；完成 function-effect matrix 后再按目标作用向量选择最小组合。

---

# 17. 本聊天最新本地执行文件

以下文件属于当前聊天的计算证据：

- `20260907__NZSCCM__R04_FIRST_ROUND_STRONG_LOGIC_REPORT.md`
- `20260907__NZSCCM__R04_FIRST_ROUND_C1_C2_C3_RESULTS.csv`
- `20260907__NZSCCM__R04_SECOND_ROUND_STRONG_LOGIC_REPORT.md`
- `20260907__NZSCCM__R04_SECOND_ROUND_C4_C5_C6_RESULTS.csv`
- `20260907__NZSCCM__R04_THIRD_ROUND_C7_CENTERED_COORDINATE_REPORT.md`
- `20260907__NZSCCM__R04_THIRD_ROUND_C7_CENTERED_COORDINATE_AUDIT.csv`
- `20260907__NZSCCM__R04_FOURTH_ROUND_C8_U02_AND_C_DIAGNOSIS.md`
- `20260907__NZSCCM__R04_FOURTH_ROUND_C8_U02_RESULTS.csv`
- `20260907__NZSCCM__CURRENT_OPERATOR_POISSON_DIAGNOSTIC.csv`
- `20260907__NZSCCM__R04_FIFTH_ROUND_NGUYEN_EQUIVALENT_STRAIN_AUDIT.md`
- `20260907__NZSCCM__R04_FIFTH_ROUND_NGUYEN_EQUIVALENT_STRAIN_RESULTS.csv`

这些结果属于历史诊断，不应在新聊天中机械延续 C1→C8 编号搜索；新聊天应从函数作用图谱重新组织已有信息。

---

# 18. 当前最终研究状态

不是：
\[
\text{已经找到运动学}
\]

也不是：
\[
\text{已经证明材料或平衡是唯一问题}
\]

而是：

\[
\boxed{
\text{我们已经积累了足够多的失败/局部成功组合，现在应反向提炼“每个基本函数究竟做了什么”。}
}
\]

下一阶段的核心问题：

\[
\boxed{
\text{能否先从单函数的力学指纹出发，构造一个真正最小、物理互补的运动学组合？}
}
\]

这比继续在完整组合上逐个补丁更符合当前研究目标。
