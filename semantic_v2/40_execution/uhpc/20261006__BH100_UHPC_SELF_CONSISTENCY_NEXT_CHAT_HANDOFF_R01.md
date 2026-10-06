# BH100 UHPC W_E–W_P–damage 自洽求解 NEXT CHAT HANDOFF R01

日期：2026-10-06  
工作分支：diagnostic/20261006-bh100-uhpc-we-wp-d-self-consistency

## 已锁定的两个上游文件

1. 20261006__BH100_FIXED_W_WE_WP_DAMAGE_SELF_CONSISTENCY_R01.md
   - 理论合同：fixed total w = recoverable elastic part + permanent plastic reference part
   - 三个全局未知量：w_E, rho_A, rho_D
   - 三个残量：F_E, F_A, F_D
   - local UHPC 采用分段 CDP algebraic return
   - 空间边界 quartic roots
   - 正式积分只允许有限一维确定性积分；禁止 2D production grid/search

2. 20261006__UC141_MATERIAL_TABLE_SOURCE_LOCK_R01.csv
   - UC141 精确 30 行 compression hardening/damage
   - UC141 精确 23 行 tension stiffening/damage
   - 来源为已审计 Abaqus 模型材料仓库，不再使用早期手抄近似峰值

## 必须继承的修正

Abaqus 表第二列：
- compression = inelastic strain
- tension = cracking strain

它们不等于 CDP true plastic strain。

压缩峰值源数据：
sigma = 141.1 MPa
xi_in = 0.000248848
d = 0.036205109
total strain = xi_in + sigma/Ec = 0.003500000074
true plastic strain = xi_in - d/(1-d)*sigma/Ec = 0.000126717953

拉伸峰值源数据：
sigma = 7.3 MPa
xi_ck = 0.000802233
d = 0.58207912
total strain = xi_ck + sigma/Ec = 0.000970435765
true plastic strain = xi_ck - d/(1-d)*sigma/Ec = 0.000567960624

因此旧手抄近似：
epsilon_tp = 0.000972202765
d_tp ~ 0.584009
以后不得作为源表精确值继续传播。

## BH100 固定点

b = 5000 mm
a_h = 10000 mm
t_c = 42 mm
Ec = 43400 MPa
nu = 0.30
w0 = 12.5 mm
fixed w = 82.2 mm
current total amplitude = 94.7 mm

旧 one-way UHPC 值
rho_A ~ 0.9792
rho_D ~ 0.9664
w_P ~ 10.33 mm
P_U ~ 10.57 MN
全部降级为历史诊断值，不再作为 regression truth。

## 下一执行任务

只算 BH100 @ w = 82.2 mm。

生产算法：

1. 用 exact UC141 table 预生成每段 a_sigma,b_sigma,a_d,b_d。
2. fixed total w 下未知 x=(w_E,rho_A,rho_D).
3. w_P = w - w_E.
4. Q = 2(w0+w)w_E - w_E^2.
5. 由 current rho_A,rho_D,w_E 得 recoverable Airy strain field。
6. local material return:
   - 每段用显式代数式；
   - softening branch 采用 connected active-set；
   - 不允许材料点 Newton 或黑箱全局搜索。
7. 用 quartic level sets 划分各材料表区。
8. rho_A,rho_D,w_P_calc 只做解析分区 + 有限一维确定性积分。
9. 解 F_E=F_A=F_D=0。
10. 输出 w_E,w_P,rho_A,rho_D,max damage,damage region,active material segments,P_U。
11. 求 plastic-curvature residual R_p=kappa_p-Pi_11(kappa_p)；只有高阶 residual 显著才增加形函数。
12. 单点闭合之前不接 steel shell、不跑九试件。

## 理论身份

这一步是“钢壳 recoverable/plastic amplitude”在 UHPC 上的同构版本：

fixed total geometry
→ recoverable elastic geometry + permanent reference geometry
→ material return/damage
→ updated stiffness
→ self-consistent root.

钢壳主要是 Mises/yield algebraic return；
UHPC 主要是 piecewise CDP table + damage + softening active set。

禁止退回 full-w elastic trial → one-shot damage/plastic correction。
