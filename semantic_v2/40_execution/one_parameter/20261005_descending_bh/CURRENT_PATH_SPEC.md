# 2026-10-05 当前数值路径冻结摘要

本文件只用于防止本轮按 BH 宽厚比由大到小逐件计算时发生公式/材料口径漂移。

## 0. 重要执行口径：本轮保持 BH100 已得到 13.40 MN 曲线的同一数值路径

正式锁定稿曾写“峰值重基准 damage/plastic”。重新复核 BH100 已执行数值链后确认：产生当前 BH100 曲线（(w=82) mm 时 (P=13.3959) MN、峰值约 13.40 MN）的实际后端采用的是 **UC141 原始/absolute damage 与 plastic strain**，而不是峰值重基准后的增量 damage/plastic。

因此，为保证“按照现在这个路径”向 BH085→...→BH005 外推时不在试件之间偷换模型，本轮系列计算统一锁定为：

[
oxed{	ext{ABS/raw UC141 damage + ABS/raw plastic strain}}
]

这个执行口径与“formal peak-rebased lock”之间的差异作为 OPEN 理论治理问题保留；本轮不在中途修改。

## 1. 几何
[
a_h=2b,qquad q_0=0.0025,qquad w_0=bq_0,
qquad alpha=pi/b,qquadeta=pi/a_h.
]

BH 族：
[
t_c=42 {m mm},qquad t_s=4 {m mm},
]
[
N_+=N_-=4,qquad m_+=m_-=4,
qquad A_0^pm=rac{0.225b}{1600}.
]

## 2. UHPC current state
固定
[
E_c=43400 {m MPa},quad
u_c=0.30,quad f_c=141.1 {m MPa},quad f_t=7.3 {m MPa}.
]

给定每个独立的 overall deflection (w)，由完全弹性 overall trial field 得到上下表面主应变。UC141 Abaqus 表按：
- tension total strain = cracking strain + stress/(E_c)
- compression total strain = inelastic strain + stress/(E_c)
- tension plastic strain = cracking strain - (d_t/(1-d_t)) stress/(E_c)
- compression plastic strain = inelastic strain - (d_c/(1-d_c)) stress/(E_c)

得到 current raw damage/plastic fields；每个表面采用
[
d=max(d_t,d_c).
]

上下表面凝聚后得到
[
ho_A(w),qquadho_D(w),qquad w_P(w).
]

最终
[
Q_P=w^2+2w_0w-w_P^2-2w_0w_P
]
并用当前单参数 UHPC 反力式得到 (P_U(w))。

## 3. 钢壳 current state
固定
[
E_s=206000 {m MPa},quad
u_s=0.30,quad f_y=355 {m MPa}.
]

UHPC/overall 给钢壳的轴向广义压缩量采用同源闭式
[
e_U^pm(w)=
rac{ar N_y^E(w)}{E_ct_c}
mprac{2t_cw}{a_h^2}.
]

塑性参考后的 global-local cross 几何幅
[
G(A)=(w_0+w_P)A+(w-w_P)A_0+(w-w_P)A.
]

对 TOP/BOTTOM 每侧：
1. 先求 elastic predictor 总几何幅值 (A^pm>0) 的正实根；
2. 固定 (A^pm)，检查 whole-face 连续 global+local Mises 最大值；
3. 若超 (f_y)，反求最大可恢复 local 幅值 (e^pmin[0,A^pm])，使
[
maxsigma_{m VM}(A^pm,e^pm)=f_y;
]
4. 输出
[
A_P^pm=A^pm-e^pm.
]

corrector 不在屈服后重新移动总几何幅 (A^pm)。

## 4. 总反力与峰值
[
P(w)=P_U(w)+P_s^+(w)+P_s^-(w),
qquad
P_u=max_wP(w).
]

每个 (w) 是独立 current state，不读取上一 (w) 的材料历史；相邻 (w) 只用于数值上扫描/定位曲线极大值。

FEM/试验峰值只允许在理论曲线冻结后比较，不进入任何求根。
