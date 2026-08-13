# NZ-SCCM NC-R1：极限根生产合同 V1
## Primary equilibrium branch → first admissible maximum → unique production \(P_u\)

**日期：2026-08-12**  
**身份：CURRENT GOVERNING LIMIT-ROOT PRODUCTION CONTRACT — NC + REBAR**  

---

# 0. 本合同只补最后一层，不修改任何上游理论

本合同不修改：

```text
R10_MATERIAL_TARGET = FROZEN
N48_ORDER = 48
U/C/T7 = N48-C1
T = N48-C1-CONSTRAINED-MINIMAX
CAYLEY_HAMILTON = GOVERNING
KINEMATICS = NGUYEN_SECOND_ORDER
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
D15 = GOVERNING
FORMAL_SPATIAL_QUADRATURE = 0
ZHOU_Dx_Dy_H = TANGENT-STABILITY ACCEPTANCE
```

它只回答一个过去尚未唯一规定的问题：

\[
\boxed{
\text{当 }R_q(D,q)=0,\;L(D,q)=0
\text{ 有多个数学实根时，哪一个才是生产意义上的 }P_u?
}
\]

不得使用试验荷载、历史 Case21 根、历史 Pu 或“最大数学根”回答这个问题。

---

# 1. 基本对象

定义总轴力

\[
\boxed{
P(D,q)=P_c(D,q)+P_s(D,q)
}
\tag{1}
\]

定义局部幅值广义残量

\[
\boxed{
R(D,q)\equiv R_q(D,q)
=R_{q,c}(D,q)+R_{q,s}(D,q)
}
\tag{2}
\]

其中，\(D\) 为无量纲平均轴向压缩广义变量；\(q=A/b\) 为相对于初始缺陷形状的附加无量纲挠曲幅值。

平衡集合为

\[
\boxed{
\mathcal E=
\{(D,q):R(D,q)=0\}.
}
\tag{3}
\]

同源导数记为

\[
P_D=\frac{\partial P}{\partial D},
\qquad
P_q=\frac{\partial P}{\partial q},
\tag{4}
\]

\[
R_D=\frac{\partial R}{\partial D}
=R_{q,D},
\qquad
R_q^\star=\frac{\partial R}{\partial q}
=R_{q,q}.
\tag{5}
\]

这里用 \(R_q^\star\) 暂时区分“总残量 \(R_q\)”和“总残量对 \(q\) 的导数 \(R_{q,q}\)”。

极限函数保持原定义：

\[
\boxed{
L(D,q)
=
P_D R_q^\star
-
P_q R_D.
}
\tag{6}
\]

---

# 2. \(L\) 的几何意义：不是额外经验式

在正则平衡点

\[
\nabla R=(R_D,R_q^\star)\neq\mathbf0
\]

处，平衡曲线 \(R=0\) 的一个切向量为

\[
\mathbf t_0=
\begin{bmatrix}
R_q^\star\\
-R_D
\end{bmatrix}.
\tag{7}
\]

因为

\[
\nabla R\cdot\mathbf t_0
=
R_D R_q^\star
-
R_q^\star R_D
=0.
\]

沿平衡支的轴力方向导数为

\[
\nabla P\cdot\mathbf t_0
=
P_D R_q^\star
-
P_qR_D
=
\boxed{L}.
\tag{8}
\]

因此：

\[
\boxed{
L=0
\iff
P\text{ 沿正则平衡支的切向导数为零}.
}
\tag{9}
\]

这个定义比单独写

\[
dP/dD=L/R_{q,q}
\]

更一般：即使局部 \(R_{q,q}=0\)、无法把平衡支写成单值 \(q(D)\)，只要 \(\nabla R\neq0\)，式（7）—（9）仍然有效。

所以 \(L\) 的正式身份是：

```text
LIMIT FUNCTION = TANGENTIAL STATIONARITY OF P ON R=0
```

不是第二套材料理论，也不是经验稳定折减。

---

# 3. admissible \((D,q)\) 域

当前 NC + Rebar 的生产可接受域定义为

\[
\boxed{
\mathcal A=
\left\{
(D,q):
\begin{array}{l}
D\ge0,\\
q\ge0,\\
P(D,q)\ge0,\\
\text{continuous compiler-domain certificate = PASS},\\
\text{all frozen material/source-range gates = PASS},\\
\text{steel branch required by the active contract = PASS},\\
P,R\text{ and all first derivatives finite}
\end{array}
\right\}.
}
\tag{10}
\]

其中：

- \(D\ge0\)：只考虑单调轴压方向；
- \(q\ge0\)：当前初始缺陷 \(q_0>0\)，生产主支只接受与初始缺陷同向增长的附加挠曲；
- 负 \(q\) 数学根保留记录，但不属于当前缺陷板生产主支；
- compiler-domain gate 必须是完整连续半波的全域证书，不能用有限空间点扫描替代；
- 本合同不扩展任何材料支路。

特别地，在当前 Case21 V2 自包含合同中，如果钢筋在最终根以前进入尚未定义的材料支，则：

```text
BLOCKED_AT_STEEL_BRANCH
```

不得为了保住一个极限根临时补材料公式。

本合同**不人为指定 \(D_{\max}\) 或 \(q_{\max}\)**。可接受域的上边界由冻结材料来源、compiler certificate 和连续结构状态自身决定，而不是由 Case21 历史答案决定。

---

# 4. primary equilibrium branch 的唯一数学定义

初始无载状态为

\[
\boxed{
(D,q)=(0,0).
}
\tag{11}
\]

初始缺陷 \(q_0\) 已经包含在几何中，因此 \(q=0\) 表示“没有加载后附加挠曲”，不是“完美板”。

定义

\[
\boxed{
\Gamma_0
=
\operatorname{Conn}_{(0,0)}
\left(
\mathcal E\cap\mathcal A
\right),
}
\tag{12}
\]

即：

> **\(\Gamma_0\) 是可接受平衡集合中，与无载状态 \((0,0)\) 连通的那一个连通分支。**

这就是当前唯一的 `PRIMARY_EQUILIBRIUM_BRANCH`。

因此：

- 与 \((0,0)\) 不连通的高幅值正根：`REJECTED_DISCONNECTED_BRANCH`；
- 负 \(q\) 根：`REJECTED_WRONG_IMPERFECTION_DIRECTION`；
- 即使这些根具有更大的 \(P\)，也不得成为 \(P_u\)。

这继承了早期解析审计已经形成的“高幅值/负 \(q\) 断开根不属于 \(D\to0,q\to0^+\) 可达主支”的物理判定，但现在把它提升为正式数学合同。

---

# 5. 主支方向

在 \(\Gamma_0\) 的正则部分，定义单位切向量

\[
\widehat{\mathbf t}
=
\pm
\frac{
(R_q^\star,-R_D)
}{
\sqrt{(R_q^\star)^2+R_D^2}
}.
\tag{13}
\]

符号按以下唯一规则选择：

1. 在无载端选择使分支进入 \(D>0\) 的方向；
2. 之后连续选择符号，使当前切向量与上一个切向量点积为正。

由此得到从无载状态出发的唯一有向弧长参数 \(s\)：

\[
s=0\quad\text{at }(D,q)=(0,0),
\qquad
s>0\quad\text{along loading direction}.
\tag{14}
\]

如果在第一个极限点以前出现

\[
\boxed{
\nabla R=\mathbf0
}
\tag{15}
\]

导致平衡分支局部拓扑不再唯一，则停止：

```text
BLOCKED_AT_PRIMARY_BRANCH_SINGULARITY
```

不得在该点凭“更大承载力”自行选择某一分叉。

---

# 6. 极限根不是任意 \(L=0\) 根，而必须是主支上的局部最大值

沿主支定义

\[
\boxed{
g(s)
=
\frac{dP}{ds}
=
\nabla P\cdot\widehat{\mathbf t}.
}
\tag{16}
\]

在正则点：

\[
g(s)=0
\iff
L=0.
\tag{17}
\]

但 \(L=0\) 可能对应：

- 局部最大值；
- 局部最小值；
- 无符号改变的高阶驻点。

所以正式 `MAXIMUM_LIMIT_ROOT` 必须满足：

\[
\boxed{
g(s)>0\quad\text{在根的加载前侧},}
\tag{18}
\]

\[
\boxed{
g(s)<0\quad\text{在根的加载后侧}.}
\tag{19}
\]

即：

\[
\boxed{+\rightarrow-}
\]

的轴力切线变号。

相反：

```text
- -> +  = MINIMUM_STATIONARY_ROOT
no sign change = DEGENERATE_STATIONARY_ROOT
```

均保留记录，但不作为极限承载力。

---

# 7. 最终 \(P_u\) 的唯一 root-selection rule

定义主支上所有通过可接受域和数值残量门的局部最大值集合

\[
\mathcal M
=
\left\{
s_i>0:
R=0,\;
L=0,\;
g:+\to-
\right\}.
\tag{20}
\]

最终生产极限点定义为

\[
\boxed{
s_u=\min\mathcal M.
}
\tag{21}
\]

即：

> **从无载状态沿 primary equilibrium branch 前进时遇到的第一个轴力局部最大值。**

于是

\[
\boxed{
(D_u,q_u)=\Gamma_0(s_u),
}
\tag{22}
\]

\[
\boxed{
P_u=P(D_u,q_u).
}
\tag{23}
\]

这一定义明确禁止：

```text
选全部数学根中的最大 P       = NO
选最小 D 的任意 L=0 根       = NO
选最接近试验值的根           = NO
选最接近历史 Case21 根        = NO
跳到断开的高幅值根            = NO
跳过第一个最大值去选后续最大值 = NO
```

如果在主支离开 \(\mathcal A\) 以前不存在 \(+\to-\) 最大值，则：

```text
NO_ADMISSIBLE_LIMIT_ROOT
```

不得借用其他断开分支替代。

---

# 8. \(R_q\) 的统一无量纲接受尺度

对 NC + Rebar 定义自然广义功尺度

\[
\boxed{
R_{\mathrm{mat}}
=
f_c\varepsilon_0J_\Omega.
}
\tag{24}
\]

其中

\[
J_\Omega=\frac{b\ell t_p}{2\pi^2}.
\]

定义

\[
\boxed{
R_{\mathrm{scale}}
=
\max
\left(
R_{\mathrm{mat}},
|R_{q,c}|+|R_{q,s}|
\right).
}
\tag{25}
\]

统一平衡残量为

\[
\boxed{
R_{\mathrm{norm}}
=
\frac{|R_q|}{R_{\mathrm{scale}}}.
}
\tag{26}
\]

生产接受门：

\[
\boxed{
R_{\mathrm{norm}}\le10^{-5}.
}
\tag{27}
\]

该容差在任何 Case21/Swartz 试验结果读取以前冻结；它是工程数值闭合门，不是材料参数。

---

# 9. \(L_{\rm norm}\) 的唯一正式定义

令

\[
A_L=P_D R_{q,q},
\qquad
B_L=P_q R_{q,D}.
\tag{28}
\]

则

\[
L=A_L-B_L.
\]

正式定义 signed normalized limit residual：

\[
\boxed{
L_{\mathrm{norm}}
=
\frac{
L
}{
|A_L|+|B_L|
}
=
\frac{
P_D R_{q,q}-P_qR_{q,D}
}{
|P_D R_{q,q}|+|P_qR_{q,D}|
}.
}
\tag{29}
\]

如果分母为零，则不得人为设为 0，而应检查：

- \(\nabla R=\mathbf0\)：branch singularity；
- \(\nabla P=\mathbf0\)：degenerate stationary state；
- 其他退化。

生产接受门：

\[
\boxed{
|L_{\mathrm{norm}}|\le10^{-5}.
}
\tag{30}
\]

这个定义具有三个优点：

1. 无量纲；
2. 直接衡量 \(L\) 中两个大项的相消程度；
3. 对 \(D,q\) 的独立线性重标度保持不变。

因此以后不得再并列使用多个不同的 \(L_{\rm norm}\) 定义。

---

# 10. root duplicate / repeatability contract

对于两个独立数学后端或两次独立求解得到的候选根 \(i,j\)，定义

\[
\boxed{
d_{ij}
=
\max
\left[
|D_i-D_j|,
\frac{|q_i-q_j|}{q_0},
\frac{|P_i-P_j|}{\max(|P_i|,|P_j|,1\ {\rm kN})}
\right].
}
\tag{31}
\]

若

\[
\boxed{
d_{ij}\le10^{-4},
}
\tag{32}
\]

则视为同一物理根的重复数值表示。

若两个声称的生产根不满足式（32），则：

```text
ROOT_REPRODUCIBILITY = FAIL
```

不得取平均值。

---

# 11. 数值搜索后端与正式理论身份分离

生产根的**定义**是式（10）—（23），不依赖某一种求根器。

允许的低维数学后端包括：

- 连续主支 continuation；
- pseudo-arclength continuation；
- low-dimensional homotopy；
- direct \(R=L=0\) root solve；
- bracket + Newton / secant / bisection refinement；
- 全部低维实根枚举作为诊断。

但生产流程至少必须做两件事：

### Route A — branch topology
从 \((0,0)\) 建立 \(\Gamma_0\)，确认第一个 \(g:+\to-\) 区间。

### Route B — local joint-root refinement
在该区间内独立求解

\[
R=0,\qquad L=0.
\]

Route B 不能代替 Route A 的物理支路身份。

同样：

```text
continuation in (D,q)
≠ material load-step history
≠ spatial discretization
```

因为每一个 \((D,q)\) 状态的材料仍由同一个 current operator 直接评价，不保存空间材料点历史。

---

# 12. 必须记录而不能静默删除的数学根

所有发现的 \(R=L=0\) 根都记录为以下之一：

```text
PRIMARY_FIRST_MAXIMUM_LIMIT_ROOT
PRIMARY_LATER_MAXIMUM_ROOT
PRIMARY_MINIMUM_STATIONARY_ROOT
PRIMARY_DEGENERATE_STATIONARY_ROOT
REJECTED_DISCONNECTED_BRANCH
REJECTED_WRONG_IMPERFECTION_DIRECTION
REJECTED_OUTSIDE_COMPILER_DOMAIN
REJECTED_MATERIAL_SOURCE_EXHAUSTED
REJECTED_STEEL_BRANCH_UNSUPPORTED
REJECTED_DUPLICATE_ROOT
REJECTED_NUMERICAL_ARTIFACT
```

不得只输出最终根。

但是只有：

```text
PRIMARY_FIRST_MAXIMUM_LIMIT_ROOT
```

具有 \(P_u\) 生产身份。

---

# 13. Case21 / Swartz blind discipline

NC-R1 合同冻结以后，Case21 再验证必须：

1. 不读取历史 Case21 \(D,q,P_u\)；
2. 不读取 direct-N48 根；
3. 不读取实验破坏荷载；
4. 从 R10 → N48-C1/MM → CH → Nguyen → D15 重建 \(P,R\)；
5. 从 \((0,0)\) 建立 \(\Gamma_0\)；
6. 找到第一个 \(g:+\to-\) 极限根；
7. 检查 \(R_{\rm norm}\)、\(L_{\rm norm}\)、连续谱域、钢筋支路；
8. 用第二个低维 root backend 复核式（31）；
9. 理论 \(D_u,q_u,P_u\) 冻结；
10. 之后才允许读取实验值。

任何实验值不得参与：

- branch identification；
- root-selection；
- solver initial target；
- tolerance selection。

---

# 14. NC-R1 当前裁决

本合同补齐此前 V2 缺少的五项：

```text
ADMISSIBLE_DQ_DOMAIN = DEFINED
PRIMARY_EQUILIBRIUM_BRANCH = DEFINED
UNIQUE_ROOT_SELECTION = DEFINED
Rq_ACCEPTANCE_TOLERANCE = DEFINED
L_norm = DEFINED
```

最终生产定义压缩为：

\[
\boxed{
P_u
=
\text{从 }(0,0)\text{ 出发的可接受主平衡支上，
第一个 }P\text{ 的 }+\to-\text{ 局部最大值}.
}
\tag{33}
\]

所以：

```text
NC_R1_LIMIT_ROOT_PRODUCTION_CONTRACT = COMPLETE
CASE21_WITH_NC_R1_INDEPENDENT_REPRO = NOT_YET_EXECUTED
SWARTZ24_RECALCULATION = NOT_AUTHORIZED_YET
```

下一门禁是：

```text
NC-R2 = BLANK-CHAT CASE21 INDEPENDENT REPRODUCTION
```
