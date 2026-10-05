# 20261006 UCFT / BH100 固定总挠度 UHPC (W_E-W_P-d) 自洽路线 R01

## 0. 本文件身份

本文件记录 2026-10-06 当前聊天中对 UHPC 解析路线的关键纠正，并作为后续 BH100 (w=82.2,mathrm{mm}) 单点自洽求解的唯一恢复入口之一。

本文件不是 production 锁定稿；当前身份为 diagnostic / theory-reconstruction。

分支：

`diagnostic/20261006-bh100-uhpc-we-wp-d-self-consistency`

其起点为：

`diagnostic/20261004-analytic-ninecurve-attempt`

---

## 1. 当前被撤销的旧顺序

旧顺序是：

[
w ightarrow 	ext{complete elastic trial field}
ightarrow d,arepsilon^p
ightarrow w_P
ightarrow P_U .
]

这个顺序把给定总新增挠度 (w) 全部先当作可恢复弹性挠度，再在末端用 damage / plasticity 做凝聚修正。

现在明确：这不是当前要的物理闭合。

尤其不能再把：

[
arepsilon_{tp}=0.000972202765,qquad
arepsilon_{cp}=0.0035
]

直接称为“弹性 (f_t/f_c) 阈值”。它们是材料总应变状态。

---

## 2. 当前新的核心分解

固定当前总构形 (W_T)，引入：

[
W_R=W_0+W_P,
]

其中 (W_0) 为制造初始缺陷，(W_P) 为不可恢复塑性参考构形。

当前可恢复弹性部分：

[
W_E=W_T-W_R.
]

因此：

[
oxed{W_T=W_0+W_P+W_E.}
]

如果先采用一阶同形投影，则：

[
W_0=w_0phi,qquad
W_P=w_Pphi,qquad
W_E=w_Ephi,
]

并且在给定新增总挠度 (w) 下：

[
oxed{w=w_E+w_P.}
]

这与钢壳“fixed total amplitude + recoverable elastic amplitude + permanent plastic amplitude”的结构完全同构；不同点在于 UHPC 的材料映射含拉压不同、损伤、塑性/开裂应变、主方向旋转和空间分区。

---

## 3. 几何非线性必须以 current plastic reference configuration 为基准

不再使用：

[
Q_E=(w_0+w)^2-w_0^2
]

作为损伤后的 current elastic 几何量。

正确 current recoverable geometric source 为：

[
rac12left[

abla W_Totimes
abla W_T
-

abla W_Rotimes
abla W_R
ight].
]

若仍在第一正弦投影层级，则：

[
Q=
(w_0+w)^2-(w_0+w_P)^2.
]

利用 (w_E=w-w_P)：

[
oxed{
Q=w_E^2+2(w_0+w_P)w_E
}
]

等价地：

[
oxed{
Q=w^2+2w_0w-w_P^2-2w_0w_P.
}
]

旧稿中的 (Q_P) 代数形式本身可以保留；必须改变的是它进入 trial/current state 的时机：它要从迭代第一层就进入，而不是最后才修正反力。

---

## 4. 材料点的弹性—损伤—塑性分解

第一层未损伤 predictor 可用：

[
arepsilon_E^{(0)}=sigma/E_c.
]

例如：

[
f_t/E_c=7.3/43400=168.20,muarepsilon,
]

[
f_c/E_c=141.1/43400=3251.15,muarepsilon.
]

而材料输入中的峰值总应变为：

[
arepsilon_{tp}=972.20,muarepsilon,
qquad
arepsilon_{cp}approx3500,muarepsilon.
]

所以在未计 damage 的 decomposition 中，峰值处原始 inelastic 部分约为：

[
804,muarepsilon quad (	ext{tension}),
]

[
249sim251,muarepsilon quad (	ext{compression}).
]

若采用 damaged-elastic / plastic decomposition：

[
oxed{
sigma=(1-d)E_c(arepsilon^{tot}-arepsilon^p)
}
]

则：

[
oxed{
arepsilon^E=rac{sigma}{(1-d)E_c},
qquad
arepsilon^p=
arepsilon^{tot}
-
rac{sigma}{(1-d)E_c}.
}
]

由当前历史材料表峰值 damage：

[
d_tapprox0.584009,qquad
d_capprox0.0362051,
]

可恢复旧账本附近的：

[
arepsilon_{t,p}approx5.68	imes10^{-4},
qquad
arepsilon_{c,p}approx1.27	imes10^{-4}.
]

这说明两组“804/249”和“568/127”并不互相矛盾：前者是未损伤 (E_c) decomposition，后者是 damaged-elastic + plastic decomposition。

---

## 5. 当前固定 (w) 的正确闭环

对给定 (w^ast)，内部状态不能单向读取，而必须自洽：

[
W_P^{(k)}
ightarrow
W_E^{(k)}
ightarrow
arepsilon_E^{(k)},sigma^{(k)}
ightarrow
d^{(k)},arepsilon_p^{(k)}
ightarrow
W_P^{(k+1)}.
]

其中：

[
W_E^{(k)}=W_T-W_0-W_P^{(k)}.
]

damage 还会改变 current elastic stiffness，因此需要同时更新：

[
D(x,y;d),qquad A(x,y;d).
]

收敛条件至少为：

[
|W_P^{(k+1)}-W_P^{(k)}|ightarrow0,
]

[
|d^{(k+1)}-d^{(k)}|ightarrow0,
]

[
|W_E^{(k+1)}-W_E^{(k)}|ightarrow0.
]

---

## 6. 解析求解约束

当前路线不允许退回二维/三维高斯网格作为 production 主解。

目标是尽量保持与 steel-local 相同的“有限代数根 + 最多一维确定性解析积分”身份。

已知 current first-mode UHPC 上下表面主应变阈值满足：

[
(arepsilon_x-lambda)(arepsilon_y-lambda)-rac14gamma_{xy}^2=0,
]

在 (u=sinalpha x, v=sineta y) 变量下，对固定 (u) 可化为 quartic：

[
C_4v^4+C_3v^3+C_2v^2+C_1v+C_0=0.
]

因此 (f_t/f_c)、damage 表节点、plastic/inelastic strain 表节点的空间边界均可由有限代数根确定；区域内部积分允许化成一维确定性定积分。

---

## 7. BH100 单点任务

唯一试算对象：

[
b=5000,mathrm{mm},qquad
a_h=10000,mathrm{mm},qquad
t_c=42,mathrm{mm},
]

[
E_c=43400,mathrm{MPa},quad

u_c=0.30,quad
f_c=141.1,mathrm{MPa},quad
f_t=7.3,mathrm{MPa},
]

[
q_0=0.0025,qquad
w_0=12.5,mathrm{mm},
]

固定新增总面外挠度：

[
oxed{w^ast=82.2,mathrm{mm}.}
]

本轮应输出：

1. current recoverable (w_E)；
2. current plastic reference amplitude / field (w_P)；
3. damage field 的解析分区、面积/能量权重及关键极值；
4. current (ho_A,ho_D) 或更严格的损伤刚度投影；
5. current UHPC reaction (P_U(82.2))；
6. 每个内部根和一维积分的求解日志；
7. 与旧单向结果 (ho_A=0.97921043,ho_D=0.96641992,w_P=10.330668,mathrm{mm},P_U=10.569428,mathrm{MN}) 的差异。旧值只能作为历史对照，不能作为新路线回归门。

---

## 8. 当前待完成事项

在正式数值求解前必须从项目源文件恢复完整 UC141 tension/compression：
- stress vs cracking/inelastic strain；
- DAMAGE TENSION / COMPRESSION；
- 若需 CDP plastic strain conversion，则恢复完整转换规则；
- terminal extrapolation convention。

禁止只用峰值点临时拟合材料表。

---

## 9. 下一阶段

先只做 BH100 (w=82.2)；不接 steel shell；不跑九试件。

单点自洽闭合确认后，才允许：
- 批量九件；
- 再接 TOP/BOTTOM steel-local；
- 再求组合 (P(w)) 与 (P_u)。
