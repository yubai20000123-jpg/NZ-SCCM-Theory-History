# 2026-10-05 当前计算路径冻结摘要

本文件只用于防止本轮逐件计算中发生公式漂移。

## 几何
[
a_h=2b,quad q_0=0.0025,quad w_0=bq_0,quad
alpha=pi/b,quadeta=pi/a_h.
]

## UHPC
固定 (t_c=42) mm, (E_c=43400) MPa, (
u_c=0.30), (f_c=141.1) MPa, (f_t=7.3) MPa。
先由完全弹性 overall trial field 得到表面主应变，依据 UC141 原始 damage/plastic 表做峰值重基准，凝聚为
(ho_A(w),ho_D(w),w_P(w))，再用
[
Q_P=w^2+2w_0w-w_P^2-2w_0w_P
]
及当前锁定 UHPC 反力式得到 (P_U(w))。

## 钢壳
固定 (E_s=206000) MPa, (
u_s=0.30), (f_y=355) MPa, (t_s=4) mm。
BH 族 whole-face topology：
[
N_+=N_-=4,quad m_+=m_-=4,quad
A_0^pm=0.225b/1600.
]
塑性参考后的 GL 几何幅：
[
G(A)=(w_0+w_P)A+(w-w_P)A_0+(w-w_P)A.
]
每一侧先求 total geometric amplitude (A^pm) 的 predictor 正实根；随后固定该 (A^pm)，对 total(global+local) Mises 场求最大可恢复 (e^pmin[0,A^pm])。最终输出
[
A_P^pm=A^pm-e^pm.
]

## 总反力
[
P(w)=P_U(w)+P_s^+(w)+P_s^-(w),qquad P_u=max_wP(w).
]

FEM/试验数据只允许在理论结果冻结后比较，不进入求根。
