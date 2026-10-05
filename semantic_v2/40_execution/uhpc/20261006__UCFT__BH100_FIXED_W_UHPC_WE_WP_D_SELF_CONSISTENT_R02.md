# 20261006 UCFT / BH100 固定 w=82.2 mm — UHPC (W_E-W_P-d) 三元自洽闭合 R02

> 分支：`diagnostic/20261006-bh100-uhpc-we-wp-d-self-consistency`  
> 身份：diagnostic theory + numerical cross-check；不是 production 锁定稿。  
> R01 commit: `367bab01824f92d96029868db0d3c266a43ffb3d`

## 1. R01 后的关键再修正

R01 已经把
[
W_T=W_0+W_P+W_E
]
锁定，但仍需进一步区分：

1. Abaqus 输入的 **inelastic/cracking strain**；
2. CDP 损伤存在时真正的 **plastic strain**；
3. damage 对 current recoverable stiffness 的反馈。

用户所说“(f_c) 处约 (251,muarepsilon) 塑性应变”数值上对应原始 compression **inelastic strain**
[
0.000248848.
]
若 damage 同时独立进入 stiffness，则不可直接把这 (248.848,muarepsilon) 再全部当作 permanent plastic strain，否则会把 damage-induced elastic degradation 与 inelastic strain 重复计入。

因此本轮把第一次 (E_c) 分解解释为 predictor，而 self-consistent corrector 使用 CDP-compatible plastic strain：

[
oxed{
arepsilon^{pl}
=
arepsilon^{in/cr}
-
rac{d}{1-d}rac{sigma}{E_c}
}
]

在峰值节点：

[
arepsilon_{t,p}^{pl}
=
0.000804
-
rac{0.584009}{1-0.584009}rac{7.3}{43400}
=
5.6786045	imes10^{-4},
]

[
arepsilon_{c,p}^{pl}
=
0.000248848
-
rac{0.0362051}{1-0.0362051}rac{141.1}{43400}
=
1.26717985	imes10^{-4}.
]

这正好把“初始 (E_c) predictor 得到 804/249 με”与“damage 更新后 568/127 με”统一到同一 fixed-point 中。

## 2. BH100 输入

[
b=5000 mathrm{mm},quad
a_h=10000 mathrm{mm},quad
t_c=42 mathrm{mm},
]

[
E_c=43400 mathrm{MPa},quad

u_c=0.30,quad
f_t=7.3 mathrm{MPa},quad
f_c=141.1 mathrm{MPa},
]

[
q_0=0.0025,quad
w_0=12.5 mathrm{mm},
]

固定新增总最大挠度：

[
oxed{w=82.2 mathrm{mm}}.
]

总当前一阶模态幅值：

[
A_T=w_0+w=94.7 mathrm{mm}.
]

## 3. 三个 current scalar unknowns

第一层仍采用一阶整体形函数：

[
phi=sinalpha xsineta y,qquad
alpha=pi/b,quadeta=pi/a_h.
]

未知量定义为：

[
oxed{
e=w_E,qquad
ho_A,qquad
ho_D.
}
]

塑性参考幅值不是独立第四未知，而由 fixed total amplitude 给出：

[
oxed{
w_P=w-e.
}
]

当前参考构形幅值：

[
A_R=w_0+w_P=A_T-e.
]

current recoverable von Kármán source：

[
oxed{
Q=A_T^2-A_R^2
=2A_Te-e^2.
}
]

## 4. damage-feedback 后的 current reduced equilibrium

[
D_0=rac{E_ct_c^3}{12(1-
u_c^2)}.
]

定义：

[
oxed{
ar N_y(e,ho_A,ho_D)
=
ho_DD_0
rac{(alpha^2+eta^2)^2}{eta^2}
rac{e}{A_T}
+
ho_Arac{E_ct_c}{16}
rac{alpha^4+eta^4}{eta^2}Q.
}
]

这里 (ho_A,ho_D) 已经进入 current equilibrium，不再等最后反力时才乘。

在一阶 uniform-condensed damage 层级，用 current extensional stiffness (ho_AE_ct_c) 反演平均膜应变；几何谐波部分因 membrane stiffness 同比例缩放而保持原 compatibility 形式：

[
arepsilon_x^0
=
rac{
u_car N_y}{ho_AE_ct_c}
-rac{alpha^2Q}{8}cos2eta y
+rac{
u_ceta^2Q}{8}cos2alpha x,
]

[
arepsilon_y^0
=
-rac{ar N_y}{ho_AE_ct_c}
-rac{eta^2Q}{8}cos2alpha x
+rac{
u_calpha^2Q}{8}cos2eta y.
]

recoverable bending part 必须只使用 (e)：

[
arepsilon_x^{E}
=
arepsilon_x^0+zalpha^2esinalpha xsineta y,
]

[
arepsilon_y^{E}
=
arepsilon_y^0+zeta^2esinalpha xsineta y,
]

[
gamma_{xy}^{E}
=
2zalphaeta ecosalpha xcoseta y.
]

## 5. UC141 material corrector

每个上下表面先求 principal strain：

[
arepsilon_{1,2}
=
rac{arepsilon_x+arepsilon_y}{2}
pm
rac12sqrt{(arepsilon_x-arepsilon_y)^2+gamma_{xy}^2}.
]

定义：

[
eta_t=max(arepsilon_1,0),qquad
eta_c=max(-arepsilon_2,0).
]

所有 UC141 stress/damage/plastic 节点先从 Abaqus inelastic/cracking strain 转为 total strain：

[
eta_t^{(k)}=arepsilon_{ck}^{(k)}+sigma_t^{(k)}/E_c,
]

[
eta_c^{(j)}=arepsilon_{in}^{(j)}+sigma_c^{(j)}/E_c.
]

然后各段均为 piecewise-linear analytic function：

[
d_t=d_t(eta_t),quad
d_c=d_c(eta_c),
]

[
p_t=p_t(eta_t),quad
p_c=p_c(eta_c).
]

其中 (p_t,p_c) 由 CDP-compatible plastic conversion 得到，而不是 peak-rebase。

当前 BH100 该点最终解中，compression channel 根本没有进入第一个 compression-inelastic 节点，因此实际只有 tension damage/plastic active。

## 6. principal plastic strain -> global plastic curvature

主方向投影后：

[
arepsilon_{x,p}
=p_tcos^2	heta-p_csin^2	heta,
]

[
arepsilon_{y,p}
=p_tsin^2	heta-p_ccos^2	heta.
]

上下表面：

[
kappa_{x,p}
=
rac{arepsilon_{x,p}^{+}-arepsilon_{x,p}^{-}}{t_c},
qquad
kappa_{y,p}
=
rac{arepsilon_{y,p}^{+}-arepsilon_{y,p}^{-}}{t_c}.
]

一阶 plastic reference projection：

[
oxed{
mathcal W_P(e,ho_A,ho_D)
=
rac{
4int_Aphi[
(alpha^2+
u_ceta^2)kappa_{x,p}
+
(eta^2+
u_calpha^2)kappa_{y,p}
],dA
}{
ba_h(alpha^4+eta^4+2
u_calpha^2eta^2)
}.
}
]

## 7. damage condensation

上下表面：

[
d^+(x,y),qquad d^-(x,y).
]

[
d_0=rac{d^++d^-}{2},qquad
d_1=rac{d^+-d^-}{2}.
]

[
ho_A^{loc}=1-d_0,
]

[
ho_D^{loc}
=(1-d_0)-rac{d_1^2}{3(1-d_0)}.
]

于是定义两个解析分区积分算子：

[
mathcal R_A(e,ho_A,ho_D),
qquad
mathcal R_D(e,ho_A,ho_D),
]

分别由既有 (Psi_A,Psi_D) energy weighting 积分得到。

## 8. 真正的 fixed-w 三元 root

因此 BH100 (w=82.2) 的一阶 current closure 不是逐点 Newton，而只有三个结构级标量根：

[
oxed{
R_P
=
w-e-mathcal W_P(e,ho_A,ho_D)
=0,
}
]

[
oxed{
R_A
=
ho_A-mathcal R_A(e,ho_A,ho_D)
=0,
}
]

[
oxed{
R_D
=
ho_D-mathcal R_D(e,ho_A,ho_D)
=0.
}
]

这就是 UHPC 对应 steel recoverable-(e) 账本的最小 damage-plastic 扩展。

## 9. production analytic identity

对任意材料节点 (lambda)，上下表面阈值仍满足：

[
(arepsilon_x-lambda)(arepsilon_y-lambda)-gamma_{xy}^2/4=0.
]

在
[
u=sinalpha x,qquad v=sineta y
]
后，对固定 (u) 为 quartic：

[
C_4v^4+C_3v^3+C_2v^2+C_1v+C_0=0.
]

因此 production 后端仍锁定为：

[
oxed{
	ext{finite quartic roots}
+
	ext{piecewise 1-D algebraic/Abelian definite integrals}
+
	ext{3-scalar root}.
}
]

二维网格/Gauss/Simpson 不得成为 production backend。

## 10. 本轮独立数值 cross-check

为了在继续写正式 1-D Abelian evaluator 前检查上述三元 closure 是否有稳定物理解，本轮另外做了 **DIAGNOSTIC ONLY** 的对称高阶 deterministic area quadrature。该数值积分不改变 production 身份，也不能以后作为正式求解器引用。

收敛结果：

[
oxed{
w_E=e=54.05827 mathrm{mm}
}
]

[
oxed{
w_P=w-e=28.14173 mathrm{mm}
}
]

[
oxed{
ho_A=0.781741
}
]

[
oxed{
ho_D=0.721547
}
]

[
oxed{
P_U(82.2)=6.96255 mathrm{MN}.
}
]

current geometric source：

[
Q=7316.34 mathrm{mm^2}.
]

current mean axial membrane resultant：

[
ar N_y=1392.51 mathrm{N/mm}.
]

反力拆分：

[
N_{bend}=299.25 mathrm{N/mm},
]

[
N_{mem}=1093.26 mathrm{N/mm}.
]

同一 (e) 若错误地令 (ho_A=ho_D=1)，则约：

[
P_U=9.0661 mathrm{MN}.
]

所以本点 damage feedback 不是小修正。

## 11. material state audit

最终一阶 closure 的全场 extrema：

[
oxed{
eta_{t,max}=0.00107531
}
]

[
oxed{
eta_{c,max}=0.00119319.
}
]

对照：

[
arepsilon_{tp}=0.000972203,
]

第一 compression-inelastic total-strain 节点：

[
0.00275323.
]

因此：

- tension 局部已经越过 (f_t)；
- compression 仍远未进入 compression-inelastic/damage；
- 本点所有 degradation/permanent curvature 都是 tension channel 主导。

最大 raw tensile damage：

[
oxed{d_{t,max}=0.604961.}
]

几何面积审计：
- TOP 表面进入 tensile damage 非零区约 (78.1%)；
- BOTTOM 表面约 (44.2%)；
- TOP 表面超过 tensile peak 的区域约 (8.4%)；
- BOTTOM 表面没有超过 tensile peak；
- 两面均没有进入 compression inelastic 区。

## 12. 与旧单向结果比较

旧 one-way / peak-rebased：

[
w_P=10.330668 mathrm{mm},
quad
ho_A=0.979210,
quad
ho_D=0.966420,
quad
P_U=10.569428 mathrm{MN}.
]

新 fixed-(w) raw-damage + CDP-plastic self-consistent closure：

[
w_P=28.14173 mathrm{mm},
quad
ho_A=0.781741,
quad
ho_D=0.721547,
quad
P_U=6.96255 mathrm{MN}.
]

因此旧 BH100 checkpoint 不能继续作为 UHPC 正确性门。

## 13. “形函数改变”审计

把本轮得到的 plastic curvature field 投影到 odd sine family：

[
phi_{nm}=sin(nalpha x)sin(meta y).
]

主要 plastic-reference amplitudes：

[
w_{P,11}=28.1417 mathrm{mm},
]

[
w_{P,13}=-1.7965 mathrm{mm},
]

其余：
[
w_{P,15}approx-0.1500 mathrm{mm},
qquad
w_{P,31}approx0.1057 mathrm{mm}.
]

在 (n,mle7) odd family 中，除 ((1,1)) 外的 plastic bending-energy share 约：

[
oxed{2.7%}.
]

所以：
- plastic reference shape 确实不是严格单一 (phi_{11})；
- 最大首个 omitted amplitude 是 (phi_{13})，约为 (w_{P,11}) 的 (6.4%)；
- 但第一轮一阶 closure 仍占绝对主导；
- 下一次最小 enrichment 应只增加 ((1,3))，而不是回到 31/41/57DOF。

如果 total current shape 仍锁定 (phi_{11})，那么出现 (w_{P,13}) 时 recoverable elastic field 必须自动带有：

[
w_{E,13}=-w_{P,13},
]

这正是“塑性形函数改变时，弹性部分也必须同步改变”的明确数学表达。

## 14. 当前裁决

本轮已经证明 fixed-(w) UHPC 可以保持与 steel recoverable-(e) 路线同一计算哲学：

[
oxed{
	ext{fixed total amplitude}
ightarrow
	ext{recoverable elastic amplitude}
+
	ext{permanent reference amplitude}
+
	ext{damage stiffness}
}
]

区别只是 steel 的屈服面可直接给 finite algebraic roots，而 UHPC 因 piecewise damage/plastic field 需要 quartic level sets + finite 1-D algebraic integrals。

下一步只做两件事：
1. 用正式 quartic + 1-D evaluator 重现本文件的 (54.058/28.142/0.78174/0.72155/6.96255) 数值；
2. 然后只加 ((1,3)) 最小 plastic/recoverable pair，检查 BH100 单点变化。

未完成上述两步之前，不进入九试件，也不接 steel shell。
