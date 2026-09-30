# UCFT M8 — BH005 人工可复现 fixed-q 弹性起点审计

更新时间：2026-09-30 23:29 +08:00

## 边界
不进入 M9，不使用 FEM/试验 Pu，不默认实例化任何 M3 candidate harmonic。
BH005 perfect-local auxiliary state 先令 A0+=A0-=0，并取第一个非零 continuation seed q=1.0e-5。
该 q 仅是数值 continuation seed，不是拟合参数。

BH005:
b=250 mm, a_h=500 mm, r=0.5, tc=42 mm, ts=4 mm, q0=0.0025.
final-INP/M5:
Ec=43400 MPa, nuc=0.30; Es=206000 MPa, nus=0.30, fy=355 MPa.

## fixed-q C1 base state
局部模态未识别以前先求 constrained global base state A+=A-=0；A 变量没有删除，随后必须审计 RA 与局部 tangent。
本点 active unknowns:
[Ex,Ey,Bx,By,Hx,Hy,P]^T.

Q=q^2+2q0q,
Cq=pi^2 Q/8,
Cq'=pi^2(q+q0)/4.

组合弹性刚度:
S=Ec tc+2 Es ts=3470800 N/mm,
A11=S/(1-nu^2)=3814065.934066 N/mm,
zs=tc/2+ts/2=23 mm,
D11=[Ec tc^3/12+2Es(ts^3/12+ts zs^2)]/(1-nu^2)
=1.254880146520e9 N mm.

弹性三角正交积分后:
G_Ex=bah A11(Ex+nu Ey)
G_Ey=bah A11(Ey+nu Ex)+P ah
G_Bx=bah A11/2 (Bx-nu Cq r^2)
G_By=bah A11/2 (By-nu Cq)
G_Hx=bah/4[(A11+A66 r^2)Hx+(nu A11+A66)Hy]
G_Hy=bah/4[(nu A11+A66)Hx+(A11+A66/r^2)Hy]

Rq=
bah A11 Cq'/2 [Cq(1+r^4)-nu(By+r^2 Bx)]
+q bah pi^4 D11/(4b^2)(1+r^2)^2
-P ah r^2 Cq'.

这些 residual 全部是有限三角函数解析积分，不用二维 Gauss。

## Newton ledger
iteration 0 predictor:
Ex=Ey=Bx=By=Hx=Hy=P=0.

R^(0)=
[0,
 0,
 -1.105037361e3,
 -4.420149442e3,
 0,
 0,
 9.550714400e5]^T.

固定 q 且全材料弹性时 residual 对未知量是 affine，所以 Newton 一次线性求解即可精确到根。

iteration 1:
Ex= 4.26540289e-4
Ey=-1.421800965e-3
Bx= 4.63562982e-9
By= 1.85425193e-8
Hx=0
Hy=0
P=1.233696696957e6 N = 1233.696696957 kN

回代 residual:
[0,0,0,0,0,0,1.16e-10]^T.

## material active-set proof
final-INP tension first nonlinear total strain:
e_t1=5.571309/43400=1.283711751e-4.

compression first inelastic total strain magnitude:
|e_c1|=119.49/43400=2.753225806e-3.

本点 C1 解可化简:
e_x=-Cq cos2Y + z(pi^2 q/b)(1+nu r^2)/(1-nu^2) sinX sinY,
e_y=Ey-Cq r^2 cos2X + z(pi^2 q/b)(r^2+nu)/(1-nu^2) sinX sinY.

UHPC |z|<=21 mm 给出解析上界:
|e_x|<=9.855492765e-6 < e_t1,
-1.426827139e-3 <= e_y <= -1.416774790e-3,
且 |e_y|<|e_c1|.
=> UHPC 全域 elastic branch.

M5 steel yield strain:
fy/Es=1.723300971e-3.
用 H_nu metric 和 |z|<=25 mm 建立保守解析上界:
ebar_i<=1.436171823e-3 < 1.723300971e-3.
=> 上下钢壳全域 elastic branch.

因此本点闭式 residual 与 final-INP/M5 production operator 严格一致。

## force shares / derived Delta
Pc=647.914699554 kN
Ps+=Ps-=292.890998701 kN
Pc+Ps++Ps-=1233.696696957 kN=P.

BH005 chi_w=1.475275839368.
P_report=chi_w Pc+Ps++Ps-=1541.634899626 kN.
chi_w 只用于 report，不反馈平衡。

由 v_,y=eps_y^0-1/2[(W_,y)^2-(W0_,y)^2] 沿 y 积分，本弹性 C1 基点中 x 相关项严格抵消:
Delta=-a_h(Ey-Cq r^2)=0.710908208334 mm.
这是派生量，不是预设 uniform Delta.

## 进入 local mode identification 前发现的实现问题
旧 M8 mode-identification rule 在 A0+=A0-=0 后，把 A+=A-=0 当作 perfect-local base state，再直接评 K_l,cond 并跟踪 lambda_min=0。

本轮按 M6 已锁定 RA 公式，对上面的 BH005 q=1e-5 弹性 C1 平衡点做有限三角多项式的解析 X,Y 积分，得到:

candidate N=m=1:
RA+ = -2561.158110982 N
RA- = +2644.857566627 N

candidate N=m=2:
RA+ = -1666.066308563 N
RA- = +1666.066308563 N

所以至少对多个正式候选:
RA±(A±=0,A0±=0;q>0) != 0.

因此 A=0 不能普遍视为 unconstrained local equilibrium branch；在 RA!=0 的点把 K_l,cond 过零称作严格 bifurcation critical point 不成立。

这是 mode-identification auxiliary algorithm 的实现问题，不是 single-q、C1、M4、M5、M6 residual 路线失败。

## 最小修正
不改结构方程、不加经验参数、不改 whole-face local basis。

对每个候选整数 pair (N,m)，仍令 A0+=A0-=0，但从 q=0,A+=A-=0 出发，随着 q continuation 实际联立:
RA+=0, RA-=0,
得到该 candidate 的 perfect-geometry forced local response:
A+(q;N,m), A-(q;N,m).

只在这些真实平衡点上评:
K_l,cond=R_AA-R_Axi G_xi^{-1} G_xiA.

若最小特征值在某状态过零，再记录该 candidate 的 local tangent loss；候选之间按最早事件识别模式。

这只把旧的“非平衡点 tangent scan”修正为“平衡支路 tangent scan”，保持原 M6 方程与同一物理根。

## 状态
- 新增指示词 29.1 人工可复现锁定：完成。
- BH005 第一个真实 fixed-q C1 base point：完成。
- residual/Jacobian/Newton/active-set/force-share/Delta：可人工逐项复算。
- 未加入任何 M3 high-frequency unknown。
- M8_PATH_SOLVER 仍 PARTIAL。
- mode-identification 旧辅助算法：需要最小修正，非路线致命。

## 唯一 NEXT_ACTION
建立 BH005 A0±=0 的 candidate-wise perfect-geometry forced-response evaluator。
对 (N,m)=1..12 的每个 candidate，从 q=0 连续联立求解当前 C1:
Ex,Ey,Bx,By,Hx,Hy,P,A+,A-.
每一步保存完整 Newton ledger，并只在真实 RA=0 平衡点上评 K_l,cond。
M3 candidate harmonics 不默认实例化；只有真实路径 omitted residual 显著时按 Gate 3 增加。
