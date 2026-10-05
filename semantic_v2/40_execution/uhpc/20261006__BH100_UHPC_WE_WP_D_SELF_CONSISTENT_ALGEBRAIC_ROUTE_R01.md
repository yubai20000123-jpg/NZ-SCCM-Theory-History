# 2026-10-06 BH100 UHPC (W_E-W_P-d) 自洽低维代数路线 R01

## 0. 状态与边界

本文件只处理 **BH100 的 UHPC 子问题**，固定当前新增总面外挠度

[
w=82.2 {m mm}.
]

暂不接入 TOP/BOTTOM multiwave 钢壳，不用 FEM 荷载反标，不把旧 BH050/BH100 UHPC 回归点当正确性基准。

BH100 输入：

[
b=5000 {m mm},qquad a_h=10000 {m mm},qquad t_c=42 {m mm},
]

[
E_c=43400 {m MPa},qquad 
u_c=0.30,
qquad w_0=bq_0=12.5 {m mm}.
]

当前目标不是“总 (w) 先全部作为弹性 trial，再事后扣 (w_P)”，而是：

[
oxed{
W_T=W_0+W_P+W_E
}
]

并在固定 (W_T) 最大新增挠度 (w=82.2) mm 下，对

[
W_E,qquad W_P,qquad d
]

做同一 current state 内的自洽闭合。

---

## 1. 本轮最关键修正：材料总应变、弹性应变、塑性应变必须拆开

最终 UC141 Abaqus 表给出的 tension stiffening 横坐标是 cracking strain，compression hardening 横坐标是 inelastic strain。

因此节点总应变为

[
arepsilon_t^{tot}
=
arepsilon_t^{ck}+rac{sigma_t}{E_c},
]

[
arepsilon_c^{tot}
=
arepsilon_c^{in}+rac{sigma_c}{E_c}.
]

在损伤塑性解释下，可恢复弹性应变不是简单的 (sigma/E_c)，而是

[
oxed{
arepsilon^E
=
rac{sigma}{(1-d)E_c}
}
]

而塑性应变为

[
oxed{
arepsilon^p
=
arepsilon^{tot}
-
rac{sigma}{(1-d)E_c}.
}
]

这等价于 Abaqus 表变量形式：

### tension

[
oxed{
arepsilon_t^p
=
arepsilon_t^{ck}
-
rac{d_t}{1-d_t}rac{sigma_t}{E_c}
}
]

### compression

[
oxed{
arepsilon_c^p
=
arepsilon_c^{in}
-
rac{d_c}{1-d_c}rac{sigma_c}{E_c}.
}
]

因此：

### tensile peak (f_t=7.3) MPa

[
arepsilon_t^{tot}
=
0.000804+rac{7.3}{43400}
=
0.000972202765,
]

原始 damage：

[
d_t=0.584009,
]

当前可恢复弹性应变：

[
arepsilon_t^E
=
rac{7.3}{(1-0.584009)43400}
approx 4.0434	imes 10^{-4},
]

塑性应变：

[
oxed{
arepsilon_t^p
approx 5.6786	imes10^{-4}.
}
]

### compressive peak (f_c=141.1) MPa

[
arepsilon_c^{tot}
=
0.000248848+rac{141.1}{43400}
approx0.003500000074,
]

原始 damage：

[
d_c=0.0362051,
]

当前可恢复弹性应变：

[
arepsilon_c^E
=
rac{141.1}{(1-0.0362051)43400}
approx 3.3733	imes10^{-3},
]

塑性应变：

[
oxed{
arepsilon_c^p
approx1.2672	imes10^{-4}.
}
]

所以过去把 (0.0009722) 和 (0.0035) 整体称为“弹性 (f_t/f_c) 阈值”是不正确的；它们是总材料状态。

---

## 2. 与钢壳路线的对应关系

钢壳固定总挠度时有：

[
W=W_E+W_P,
]

钢材通过 Mises / EPP 判据决定 recoverable elastic part 与 plastic remainder。

UHPC 的结构完全同型，只是局部 constitutive corrector 从单一 Mises 截断变成：

[
oxed{
arepsilon^E
ightarrow
	ext{UC141 分段材料表反解}
ightarrow
{arepsilon^{tot},d,arepsilon^p,sigma}.
}
]

因此 UHPC 不需要新增大规模自由度。

第一版最小自洽未知量取：

[
oxed{
mathbf z=
egin{bmatrix}
w_P\
ho_A\
ho_D
end{bmatrix}.
}
]

固定 (w) 后：

[
oxed{
w_E=w-w_P.
}
]

---

## 3. 当前参考构形与几何量

定义

[
phi(x,y)
=
sinrac{pi x}{b}
sinrac{pi y}{a_h},
]

[
W_0=w_0phi,
qquad
W_P=w_Pphi,
qquad
W_E=w_Ephi.
]

当前总构形：

[
W_T=(w_0+w)phi.
]

当前无应力参考构形：

[
W_R=(w_0+w_P)phi.
]

因此弹性几何增量：

[
oxed{
Q_E^star
=
(w_0+w)^2-(w_0+w_P)^2
}
]

即

[
oxed{
Q_E^star
=
w_E^2+2(w_0+w_P)w_E
=
w^2+2w_0w-w_P^2-2w_0w_P.
}
]

这说明旧 (Q_P) 的代数形式本身没有错，错误在于过去先用总 (w) 生成全弹性 trial，再事后才扣 (w_P)。

---

## 4. 损伤后的当前广义反力

令

[
alpha=rac{pi}{b},qquad
eta=rac{pi}{a_h},
]

[
D_0=rac{E_ct_c^3}{12(1-
u_c^2)}.
]

当前一模态广义反力仍写为

[
oxed{
egin{aligned}
ar N_y
={}&
ho_DD_0
rac{(alpha^2+eta^2)^2}{eta^2}
rac{w_E}{w_0+w}
\
&+
ho_A
rac{E_ct_c}{16}
rac{alpha^4+eta^4}{eta^2}
Q_E^star.
end{aligned}
}
]

这里 (ho_A,ho_D) 不能作为一次性后处理量，而是和 (w_P) 一起进入当前状态方程。

---

## 5. 当前 recoverable elastic field

在第一版低维闭合中，用 (ho_A) 表示当前全板 membrane secant retention。

中面 recoverable elastic strain 写成

[
oxed{
egin{aligned}
arepsilon_{x,E}^0
={}&
rac{
u_car N_y}{ho_AE_ct_c}
-rac{alpha^2Q_E^star}{8}cos2eta y
+rac{
u_ceta^2Q_E^star}{8}cos2alpha x,
\
arepsilon_{y,E}^0
={}&
-rac{ar N_y}{ho_AE_ct_c}
-rac{eta^2Q_E^star}{8}cos2alpha x
+rac{
u_calpha^2Q_E^star}{8}cos2eta y.
end{aligned}
}
]

整个厚度：

[
oxed{
arepsilon_{x,E}
=
arepsilon_{x,E}^0
+
zalpha^2w_E
sinalpha xsineta y
}
]

[
oxed{
arepsilon_{y,E}
=
arepsilon_{y,E}^0
+
zeta^2w_E
sinalpha xsineta y
}
]

[
oxed{
gamma_{xy,E}
=
2zalphaeta w_E
cosalpha xcoseta y.
}
]

求 recoverable principal strains

[
arepsilon_{1,E},arepsilon_{2,E}.
]

---

## 6. 每个主方向的 UC141 algebraic material corrector

对每一个主方向，不再把 (arepsilon_E) 当作总应变。

### elastic range

若材料尚未进入 Abaqus inelastic/cracking 表，则

[
arepsilon^{tot}=arepsilon^E,qquad
d=0,qquad
arepsilon^p=0.
]

### nonlinear range

把 UC141 每一个材料表节点 (i) 预先转成

[
arepsilon_i^{tot},
qquad
arepsilon_i^{E}
=
rac{sigma_i}{(1-d_i)E_c},
qquad
arepsilon_i^p
=
arepsilon_i^{tot}-arepsilon_i^E.
]

给定结构产生的 recoverable (arepsilon_E)，在有限个相邻节点中找到

[
arepsilon_i^E
le
arepsilon_E
le
arepsilon_{i+1}^E,
]

在该段内只需要解一个一次代数根；若严格继承分段线性 (sigma-d-arepsilon^{tot}) 插值，则也最多是低阶代数根。

得到

[
oxed{
arepsilon^{tot}(arepsilon_E),quad
d(arepsilon_E),quad
arepsilon^p(arepsilon_E),quad
sigma(arepsilon_E).
}
]

这就是 UHPC 对应钢材 radial/Mises corrector 的材料级翻版。

---

## 7. 主方向塑性应变映射与 (w_P)

令 elastic/current principal angle 为

[
	an2	heta
=
rac{gamma_{xy,E}}
{arepsilon_{x,E}-arepsilon_{y,E}}.
]

将两个主方向的 signed plastic strain 记为

[
p_1,qquad p_2.
]

则

[
arepsilon_{x,p}
=
p_1cos^2	heta+p_2sin^2	heta,
]

[
arepsilon_{y,p}
=
p_1sin^2	heta+p_2cos^2	heta,
]

[
gamma_{xy,p}
=
2(p_1-p_2)sin	hetacos	heta.
]

上下表面：

[
kappa_{x,p}
=
rac{arepsilon_{x,p}^+-arepsilon_{x,p}^-}{t_c},
]

[
kappa_{y,p}
=
rac{arepsilon_{y,p}^+-arepsilon_{y,p}^-}{t_c}.
]

第一正弦模态的永久参考挠度投影：

[
oxed{
w_P^{map}
=
rac{
4int_A
phi
[
(alpha^2+
u_ceta^2)kappa_{x,p}
+
(eta^2+
u_calpha^2)kappa_{y,p}
]dA
}{
ba_h(
alpha^4+eta^4+2
u_calpha^2eta^2
)
}.
}
]

---

## 8. raw damage，不再 peak-rebase

本轮明确撤销“到 (f_t/f_c) 才令 damage 从零开始”的 peak-rebase 规则。

因为用户当前要求正是：

[
oxed{
	ext{材料达到 }f_t/f_c	ext{ 之前已经允许存在 plastic strain 和 damage。}
}
]

所以直接使用最终 UC141 原始 damage 表，经材料 corrector 得到

[
d^+(x,y),qquad d^-(x,y).
]

定义

[
d_0=rac{d^++d^-}{2},
qquad
d_1=rac{d^+-d^-}{2}.
]

局部 membrane retention：

[
oxed{
ho_A^{loc}=1-d_0.
}
]

局部 bending retention（中性轴移动凝聚）：

[
oxed{
ho_D^{loc}
=
(1-d_0)
-
rac{d_1^2}{3(1-d_0)}.
}
]

全板采用原已建立的真实能量权：

[
Psi_A=
alpha^4cos^22eta y
+eta^4cos^22alpha x
-2
u_calpha^2eta^2
cos2alpha xcos2eta y,
]

[
Psi_D=
(alpha^4+eta^4+2
u_calpha^2eta^2)
sin^2alpha xsin^2eta y
+
2(1-
u_c)alpha^2eta^2
cos^2alpha xcos^2eta y.
]

于是

[
oxed{
ho_A^{map}
=
rac{
int_Aho_A^{loc}Psi_A,dA
}{
rac{ba_h}{2}(alpha^4+eta^4)
}.
}
]

[
oxed{
ho_D^{map}
=
rac{
int_Aho_D^{loc}Psi_D,dA
}{
rac{ba_h}{4}(alpha^2+eta^2)^2
}.
}
]

---

## 9. 最终只解三个结构级 root

固定 (w=82.2) mm，正式残量是

[
oxed{
R_P
=
w_P-w_P^{map}(w_P,ho_A,ho_D)=0,
}
]

[
oxed{
R_A
=
ho_A-ho_A^{map}(w_P,ho_A,ho_D)=0,
}
]

[
oxed{
R_D
=
ho_D-ho_D^{map}(w_P,ho_A,ho_D)=0.
}
]

即

[
oxed{
mathbf R(w_P,ho_A,ho_D)=mathbf 0.
}
]

不需要 41DOF/57DOF，不需要 FEM material points，不需要把全板离散成生产积分网格。

---

## 10. 正式解析后端

将

[
u=sinalpha x,qquad v=sineta y
]

后，上下表面 elastic strain 分量仍为 (u,v) 的低阶代数式。

任意材料表节点的边界均由主值特征方程

[
(arepsilon_x-lambda)
(arepsilon_y-lambda)
-rac14gamma_{xy}^2=0
]

给出。

对固定 (u)，仍归结为

[
oxed{
C_4v^4+C_3v^3+C_2v^2+C_1v+C_0=0.
}
]

因此正式 production 路线为：

[
oxed{
	ext{有限材料节点}
ightarrow
	ext{有限 quartic roots}
ightarrow
	ext{有限一维显式定积分}
ightarrow
mathbf R=0.
}
]

也就是：

[
oxed{
	ext{空间二维问题并没有变成二维数值积分问题。}
}
]

本轮数值网格/高阶求积仅允许作为独立诊断核验，不作为 production theory 身份。

---

## 11. BH100, (w=82.2) mm 第一轮自洽数值诊断

为了先判断这条三根路线有没有实际根，在完全相同的公式下做了独立高阶确定性面积求积诊断；不同积分阶数都收敛到同一个根邻域。

代表性结果：

[
oxed{
w_Papprox 52.82 {m mm}
}
]

[
oxed{
w_E=w-w_P
approx29.38 {m mm}
}
]

[
oxed{
ho_Aapprox0.7443
}
]

[
oxed{
ho_Dapprox0.6677
}
]

相应纯 UHPC 当前反力约：

[
oxed{
P_U(82.2)approx4.10 {m MN}.
}
]

典型积分阶数核验：

| diagnostic order | (w_P) mm | (w_E) mm | (ho_A) | (ho_D) | (P_U) MN |
|---:|---:|---:|---:|---:|---:|
| 20 | 52.734 | 29.466 | 0.74316 | 0.66743 | 4.1016 |
| 30 | 52.862 | 29.338 | 0.74456 | 0.66850 | 4.0939 |
| 40 | 52.791 | 29.409 | 0.74404 | 0.66731 | 4.0987 |
| 50 | 52.826 | 29.374 | 0.74427 | 0.66784 | 4.0961 |
| 80 | 52.824 | 29.376 | 0.74425 | 0.66777 | 4.0962 |
| 100 | 52.820 | 29.380 | 0.74424 | 0.66771 | 4.0966 |
| 120 | 52.824 | 29.376 | 0.74427 | 0.66776 | 4.0963 |

所以这不是“没有根”的路线。相反，固定总 (w) 时 recoverable 与 permanent 部分发生了非常强的重新分配。

但此结果暂时标记为：

[
oxed{
	ext{R01 DIAGNOSTIC ROOT，尚未升格为 production locked value。}
}
]

原因：正式版本还要把面积求积分区完全替换为上面的 quartic-boundary + 1D exact/deterministic integral，并检查第一正弦 (W_P=w_Pphi) 投影后的高阶塑性曲率残差。

---

## 12. 与旧 BH100 单向算法的差异

旧算法在 (w=82.2) mm 曾给出大致：

[
w_Papprox10.33 {m mm},qquad
ho_Aapprox0.979,qquad
ho_Dapprox0.966,
]

[
P_Uapprox10.57 {m MN}.
]

R01 自洽 raw-damage 路线则给出约：

[
w_Papprox52.82 {m mm},
quad
ho_Aapprox0.744,
quad
ho_Dapprox0.668,
quad
P_Uapprox4.10 {m MN}.
]

差异来源不是参数调整，而是理论身份变化：

旧：

[
w
ightarrow
	ext{pristine elastic trial}
ightarrow
	ext{peak-rebased damage/plastic}
ightarrow
	ext{one-pass correction}.
]

新：

[
oxed{
w
ightarrow
{w_E,w_P,d}
	ext{ 同一 current state 三根自洽}
}
]

且 raw damage / plastic 从材料表真正开始非弹性的位置进入，而不是在 (f_t/f_c) 处重新置零。

---

## 13. 下一步唯一工作

1. 保持 BH100 (w=82.2) mm 不动。
2. 不接钢壳。
3. 将 (ho_A,ho_D,w_P) 的二维诊断积分改写成：
   - 材料表各 elastic-coordinate 节点；
   - quartic level-set roots；
   - finite 1D integrals。
4. 输出每一材料状态区的边界与面积/能量权。
5. 检查 plastic-curvature residual：
   [
   kappa_p-kappa_p^{(1,1)}
   ]
   是否足够小。
6. 若高阶 residual 小，则锁定三元一模态 root。
7. 若 residual 不小，不新增任意经验模态；只把 plastic curvature 的首个正交非零谐波加入 (W_P)，再次形成有限代数 root 系统。
8. 只有 UHPC 这一点闭合后，才恢复 TOP/BOTTOM multiwave steel。

## 14. 当前判决

[
oxed{
	ext{UHPC 与钢壳确实属于同一“固定总构形—recoverable/permanent 分配”母思想。}
}
]

区别只是：

[
oxed{
	ext{steel: Mises/EPP algebraic corrector}
}
]

而

[
oxed{
	ext{UHPC: piecewise UC141 damage-plastic algebraic corrector + energy projection}.
}
]

因此 UHPC 不需要退回大规模有限元式离散；目标应继续保持

[
oxed{
	ext{低维 root + quartic boundary + 至多一维显式/确定性积分}.
}
]
