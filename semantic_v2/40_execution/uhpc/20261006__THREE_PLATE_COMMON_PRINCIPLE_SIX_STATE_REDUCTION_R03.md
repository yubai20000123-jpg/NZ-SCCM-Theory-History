# UCFT 三子板共用计算原则：六状态凝聚 R03

日期：2026-10-06  
分支：diagnostic/20261006-bh100-uhpc-we-wp-d-self-consistency

## 0. 对 R02 的物理裁决

R02 得到 BH100 @ w=82.2 mm 的 UHPC first-mode result:
w_E≈26.18 mm, w_P≈56.02 mm, P_U≈3.75 MN。

该结果不再作为继续升阶的依据。

核心问题不是“缺少 phi_13”，而是 R02 把局部 tensile CDP plastic/cracking state 过强地映射成全板永久参考曲率，同时又用同一 damaged field 降低刚度，相当于把拉裂非线性同时作为：

1. stiffness loss；
2. global permanent geometric imperfection；

两次强烈作用于承载力。

材料点的 plastic/cracking strain 只有其**厚度一阶矩 / 不对称残余曲率部分**能够形成板的 plastic reference imperfection；其厚度零阶矩主要表现为塑性膜应变/轴向缩短，damage 则主要表现为 recoverable stiffness loss。

因此 R02 的 w_P≈56 mm 没有足够物理依据。

---

## 1. 三个承载子板

总轴力只保留三部分：

\[
P=P_c+P_s^++P_s^-.
\]

三个结构子板：

- UHPC core；
- top steel shell；
- bottom steel shell。

PBL 不单独作为第四轴向承载项。

三个子板采用同一个结构级计算骨架，只允许材料闭合不同。

---

## 2. 每个子板只有两个 current state parameters

对

\[
j\in\{c,+,-\}
\]

定义：

\[
\boxed{
D_j^*
}
\]

current effective flexural rigidity，以及

\[
\boxed{
p_j
}
\]

plastic/permanent reference imperfection amplitude。

所以整个截面只有六个 current state variables：

\[
\boxed{
(D_c^*,p_c,\ D_+^*,p_+,\ D_-^*,p_-).
}
\]

材料常数 E, nu, t, f_y/f_c 与几何参数不属于 current unknowns。

---

## 3. 共用的几何原则

给定当前总新增挠度 amplitude w 和原始缺陷 w0。

总幅值：

\[
R=w_0+w.
\]

第 j 个子板的 stress-free/current reference amplitude：

\[
R_{r,j}=w_0+p_j.
\]

recoverable elastic amplitude：

\[
\boxed{
e_j=w-p_j.
}
\]

因此：

\[
R=R_{r,j}+e_j.
\]

von Karman geometric increment：

\[
\boxed{
Q_j
=
R^2-R_{r,j}^2
=
2Re_j-e_j^2
=
w^2+2w_0w-p_j^2-2w_0p_j.
}
\]

这一个式子对 UHPC 与两侧钢壳完全相同。

---

## 4. 云露型共用结构算子

对固定整体 mode family，定义纯几何常数：

\[
K_D
=
\frac{(\alpha^2+\beta^2)^2}{\beta^2},
\]

\[
K_A
=
\frac{1}{16}
\frac{\alpha^4+\beta^4}{\beta^2}.
\]

第 j 个子板的 current elastic/postbuckling trial resultant：

\[
\boxed{
N_j^{trial}
=
D_j^*K_D\frac{e_j}{R}
+
A_j^*K_AQ_j.
}
\]

若采用一个 scalar retention \(\rho_j\) 同时代表当前 recoverable membrane/bending stiffness：

\[
D_j^*=\rho_jD_{j0},
\]

\[
A_j^*=\rho_jA_{j0}.
\]

因为

\[
D_{j0}
=
\frac{E_jt_j^3}{12(1-\nu_j^2)},
\qquad
A_{j0}=E_jt_j,
\]

有：

\[
\boxed{
A_j^*
=
\frac{12(1-\nu_j^2)}{t_j^2}D_j^*.
}
\]

于是结构公式只需要 \(D_j^*,p_j\)：

\[
\boxed{
N_j^{trial}
=
D_j^*
\left[
K_D\frac{w-p_j}{w_0+w}
+
\frac{12(1-\nu_j^2)}{t_j^2}
K_A
\left(
(w_0+w)^2-(w_0+p_j)^2
\right)
\right].
}
\]

这就是“每个子板两个参数”的核心来源。

---

## 5. 四种材料信息各自只承担一个物理角色

### 5.1 pristine linear elasticity

纯线弹性负责提供结构骨架：

\[
D_{j0},\quad A_{j0},
\]

以及云露型大挠度几何关系。

### 5.2 plastic strain

塑性应变不直接作为 stiffness-loss coefficient。

它只负责生成 stress-free eigenstrain/eigencurvature，进而形成：

\[
\boxed{
p_j.
}
\]

只有 plastic strain 对厚度的**一阶矩**能够产生 plastic reference curvature。

对轴向塑性应变 \(\varepsilon_{y,j}^p(z)\)，最简 section relation 为：

\[
\boxed{
\kappa_{P,j}
=
\frac{
\int E_j^{r}(z)\,z\,\varepsilon_{y,j}^p(z)\,dz
}{
\int E_j^{r}(z)\,z^2\,dz
}.
}
\]

其中 \(E_j^r\) 是 current recoverable modulus。

厚度零阶矩

\[
\int E_j^r\varepsilon_{y,j}^p dz
\]

是 plastic membrane shortening，不得直接转成 p_j。

随后把 \(\kappa_{P,j}\) 投影到选定 Yun/modal geometry 得到 \(p_j\)。

### 5.3 damage / yielded-zone stiffness loss

damage 不直接制造 plastic imperfection。

它只决定 current recoverable rigidity：

UHPC：

\[
\boxed{
D_c^*
=
\int (1-d_c)E_cz^2dz
}
\]

或其 mode-energy equivalent。

钢材没有 continuum damage；其“loss”来自屈服区 tangent stiffness 消失：

\[
E_s^{tan}
=
\begin{cases}
E_s,& |\sigma_s|<f_y,\\
0,& \text{active ideal-plastic plateau}.
\end{cases}
\]

因此：

\[
\boxed{
D_s^*
=
\int E_s^{tan}(z)z^2dz
}
\]

或 Yun local multiwave operator 凝聚后的等效值。

### 5.4 yield plateau

yield plateau 不等于 stiffness loss，也不等于 plastic imperfection。

它只负责 stress/resultant cap：

\[
\boxed{
|\sigma_s|\le f_y.
}
\]

云露 elastic large-deflection path 只在未达到 \(f_y\) 时使用；达到 \(f_y\) 后强度截断，tangent 进入平台。

所以 steel contribution：

\[
\boxed{
N_s^\pm
=
\operatorname{cap}_{f_y}
\left[
\mathcal Y(D_\pm^*,p_\pm;w)
\right].
}
\]

材料常数 \(f_y\) 是已知常数，不增加 current state variable。

---

## 6. UHPC 与钢壳的真正统一点

三者的外层完全一致：

\[
\boxed{
\text{current total geometry}
-
\text{plastic reference geometry}
=
\text{recoverable geometry}
}
\]

\[
\boxed{
\text{recoverable geometry}
+
D_j^*
\longrightarrow
N_j
}
\]

区别仅在内部得到 \(D_j^*,p_j\) 的方法：

UHPC：
- polynomial damage law -> \(D_c^*\)
- residual plastic-strain first moment -> \(p_c\)

Steel:
- elastic/yielded-region tangent -> \(D_s^*\)
- accumulated steel plastic-strain first moment -> \(p_s\)
- \(f_y\) provides stress cap.

所以不是三套理论，而是一个结构算子 + 两种材料 state updater。

---

## 7. 六状态总式

\[
\boxed{
P(w)
=
P_c(D_c^*,p_c;w)
+
P_s^+(D_+^*,p_+;w)
+
P_s^-(D_-^*,p_-;w).
}
\]

如果三个 plate contribution 都用相同 Yun-derived geometry operator，则：

\[
\boxed{
P(w)
=
b\sum_{j=c,+,-}
D_j^*
\left[
K_D\frac{w-p_j}{w_0+w}
+
\frac{12(1-\nu_j^2)}{t_j^2}K_A
\left(
(w_0+w)^2-(w_0+p_j)^2
\right)
\right],
}
\]

其中 steel terms 在 local/average stress 达到 fy 时执行 ideal-plastic cap。

---

## 8. BH100 的新物理门

DIRECT 20261005 extraction at global Pu frame:

- total Pu = 13.486 MN
- total global deflection = 99.823 mm
- initial global imperfection = 12.5 mm
- increment = 87.323 mm

因此，如果目标是审计“极限点同一帧”的三部分受力，下一次固定 w 应使用：

\[
\boxed{
w=87.323\ {\rm mm}
}
\]

而不是旧的 82.2 mm。

已有物理分配认知：

\[
P_c\sim7\text{--}8\ {\rm MN},
\]

\[
P_s^+\sim2\text{--}3\ {\rm MN},
\qquad
P_s^-\sim2\text{--}3\ {\rm MN},
\]

\[
P\sim13\text{--}14\ {\rm MN}.
\]

这些值只作为 external sanity gate，不允许反标 \(D_j^*,p_j\)。

如果理论在不使用该分配作为输入时得到 UHPC≈3.75 MN，则先判定 state updater/condensation 物理映射错误，不允许通过增加模态自由度“救数值”。

---

## 9. 下一步计算原则

下一步不再增加形函数。

只做六状态闭合：

\[
(D_c^*,p_c,D_+^*,p_+,D_-^*,p_-).
\]

优先从当前材料 law 直接计算：

1. UHPC damage polynomial -> \(D_c^*\)
2. UHPC plastic eigenstrain first moment -> \(p_c\)
3. top steel elastic/yield tangent -> \(D_+^*\)
4. top steel plastic first moment -> \(p_+\)
5. bottom steel elastic/yield tangent -> \(D_-^*\)
6. bottom steel plastic first moment -> \(p_-\)

再代入三个 Yun-derived plate formulas，直接相加。

在这个六状态原则没有先恢复合理三部分受力比例前：
- 不增加 phi_13
- 不增加高阶 Ritz
- 不增加新的 coupling free DOF
- 不允许用 FEM force shares 反标 state variables

R02 first-mode modal-expansion proposal正式降级为错误方向。
