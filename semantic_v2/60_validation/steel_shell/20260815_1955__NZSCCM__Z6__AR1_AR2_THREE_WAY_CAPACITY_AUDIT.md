# Z6 长宽比 a/b=1 与 2：NZ-SCCM / 周思铭经验式 / Winter 三向对比

**Timestamp:** 2026-08-15 19:55 +08:00

## 固定参数

保持 Z6 截面与材料：b=12000 mm, h=130 mm, ns=60, ls=200 mm, ts=4 mm, fy=355 MPa, fcu=40 MPa, f'c=30.4 MPa, Es=206000 MPa, Ec=32500 MPa, nu_s=0.30, nu_c(Zhou)=0.20。

Ac=1,434,720 mm^2; As=125,280 mm^2; Pyth=88.089888 MN。

比较两种几何：
- a/b=1: a=12000 mm, m=1, complete halfwave ell=a/m=12000 mm;
- a/b=2: a=24000 mm, classical/Zhou controlling m=2, complete representative halfwave ell=a/m=12000 mm.

因此二者的弹性代表半波几何完全一致。Zhou 正交异性弹性式对两者给出相同 Pcr：39.288014715 MN；lambda_n=sqrt(Pyth/Pcr)=1.49738330617。

## Zhou Eq.(5-87)-(5-88)

两者使用相同 lambda_n，因此均得到：phi_Zhou=0.561775793743，Pu_Zhou=49.4867667519 MN。

## Winter Eq.(5-86)

phi_W=(1/lambda_n)(1-0.22/lambda_n)=0.569711862155，故两者均得到 Pu_W=50.1858541295 MN。

## NZ-SCCM current continuum audit

当前正式 N48 单区间编译器在这两个修改算例的高幅值支路上会离开冻结覆盖域。把 N48 直接扩到约 [-2.1,0.55] 会产生不可接受的 T 函数全局误差（约 0.42），因此本轮没有把宽区间 N48 结果冒充正式理论值。

为了只回答“同一冻结物理 current operator 对 a/b=1 与 2 是否给出一致能量响应”，采用冻结 R10 current map 的直接点值矩阵函数评价，并用高阶 Gauss 作为 **audit-only continuum evaluator** 搜索同一 Rq=0 平衡支和峰值。该积分后端不是正式 NZ-SCCM 零积分生产算子，因此结果身份为 `R10_DIRECT_CONTINUUM_AUDIT_ONLY`，不改变 N_formal_spatial_quadrature=0 的项目治理。

32x32x10 audit：
- a/b=1, m=1, q0=a/(500b)=0.002: peak near D=1.625, q=0.02231796882, Pu=44.58066266 MN;
- a/b=2, m=2, q0=a/(500b)=0.004: peak near D=1.625, q=0.02077537762, Pu=44.55291911 MN.

两者差值仅 0.027744 MN，即约 0.0622%。因此在正确采用 m=2 和 ell=a/m=b 后，冻结 R10 连续理论也恢复了 a/b=1 与 2 几乎相同的极限承载力响应。

## 关键结论

1. 对 a/b=2 必须采用 m=2；若仍机械使用 m=1/ell=a，会把两个相同最优半波几何错误地区分开。
2. Zhou 经验式：49.4868 MN vs 49.4868 MN，完全相同。
3. Winter：50.1859 MN vs 50.1859 MN，完全相同。
4. NZ-SCCM R10 continuum audit：44.5807 MN vs 44.5529 MN，差约 0.06%，工程上可视为相同。
5. 因而用户关于 a/b=1 与 2 应具有相同/近似相同稳定能量身份的判断在本组 Z6 参数下得到支持。
6. 正式零积分 N48/D15 生产值仍需通过多尺度/局部材料编译把这两个高幅值支路重新投回可认证解析域后才能 release；本轮没有用失真的宽区间 N48 值代替它。
