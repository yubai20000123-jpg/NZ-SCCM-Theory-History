# NZ-SCCM Z0–Z5 钢壳局部屈服先后顺序、鼓波中心—侧部切线差异与重新计算审计

**Date:** 2026-08-17 23:42 +08:00  
**Object:** Z0–Z5 modified AR2/SSSS, one continuous representative halfwave  
**Trigger:** 审计“鼓波中间先进入屈服/低切线区，而鼓波两侧仍保持较高弹性切线”的空间先后顺序，以及这一点是否被当前钢壳求解正确体现。  
**Status:** `LOCAL_YIELD_FRONT + LOCAL_TANGENT + CURRENT-PATH RECALCULATION AUDIT`  
**Calibration:** NO  
**Comparator used in solve:** NO

## 0. 结论

本轮确认用户指出的力学现象：压缩侧钢面板不是整体同时降模，而是鼓波中心/中心附近先进入屈服和低切线区，然后屈服前沿向两侧扩展。Z0、Z1、Z3 在 current peak 前已经推进到 `x/b=0.125`；Z2 在 peak 前推进到 `x/b=0.25`，`x/b=0.125` 的 yield event 略晚于 current peak；Z4 在 peak 前推进到 `x/b=0.125`，edge 在 peak 后才屈服；Z5 最接近整体压缩主导，edge 在 current peak 前刚刚屈服。

因此整张钢面板不能在某一 `max VM/fy>1` 事件后统一设 `E_t=0`，也不能继续统一采用 `E_s`。正确对象必须是连续位置相关的 `C_t^s(X,Y,z)`。

此前 direct-current audit 没有把这一空间图显式输出，但其 finite-difference face Jacobian 实际上已经隐式包含当前 radial-cap current map 的局部切线差异。把 radial-cap 的解析局部导数重新积分后，与此前 FD face Jacobian 的最大相对差在六板中不超过约 `2.2e-3`。所以此前并不存在“整张钢板统一 Et=0”这一实现错误。

真正的新问题是：当前 radial-cap current map 的一致导数本身不等于一个物理可接受的 ideal-J2 flow tangent。在 Z0/Z1/Z2/Z3 的鼓波中心，radial derivative 甚至给出负的 `C_yyyy/C_yyyy^e`。例如 Z1 current peak 中心约为 `-0.01095`。这说明 current radial stress cap 可用于 stress-redistribution 诊断，但不能自动提升为 production full directional tangent。

用 associative ideal-J2 continued-plastic tangent 做独立审计后，鼓波中心确实远软于两侧；Z1 current peak 中心 `C_yyyy/C_yyyy^e≈0.01355`，边缘仍为 `1.0`。沿实际连接支路的局部 strain increment 计算，Z1 中心轴向 stress-increment retention 约 `0.06662`，边缘仍为 `1.0`。

把这个 positive-semidefinite J2 tangent 只替换进 current peak 的 tangent/Jacobian 做 sensitivity audit，六板在旧 radial-cap peak 的 `dP/dD` 全部变为正值。例如 Z1 从约 `0` 变为 `+0.704 MN/D`，Z4 从约 `0` 变为 `+2.169 MN/D`。因此旧 Z0–Z5 Pu 不能再称为已经通过 steel full-consistent-tangent 认证的 production Pu。

但本轮不把 tangent-only sensitivity 擅自改名为“新 Pu”。原因是 J2 flow tangent 不是当前 radial-cap state function 的导数；要得到新的 production Pu，必须先冻结一个同源 `sigma_s(epsilon)` + `C_t^s(epsilon)` plane-stress steel current operator，再用同一 operator 重跑 `P,Rq,RA,KZ,L`。

## 1. 运动学与检查位置

继续使用

`X=pi*x/b`, `Y=pi*y/ell`, `ell=b`, `w0=A0 sinX sinY`, `w=qb sinX sinY`，

`M=pi^2/eps0*(q0*q+q^2/2)`, `alpha=lambda_A*M`。

本轮重点检查压缩侧外表面 `z=-(tc/2+ts)`、`Y=pi/2` 上的 `x/b=0,0.125,0.25,0.375,0.5`。当前六板 trial VM 最大值均位于或极接近 `X=Y=pi/2`、压缩侧外表面，因此该线能直接显示中心软化和 yield-front 扩展顺序。

## 2. 当前 radial-cap stress map 与解析 tangent

当前 face stress map：

`sig_tr=Ce*eps`

`VM_tr=sqrt(sx^2-sx*sy+sy^2+3*tau^2)`

`a=min(1,fy/VM_tr)`

`sig=a*sig_tr`。

在 `VM_tr>fy` 区域，解析 derivative 为

`Ct_rad = a*Ce - (a/VM_tr) * sig_tr outer (n^T Ce)`，

其中

`n=[(2sx-sy)/(2VM),(2sy-sx)/(2VM),3tau/VM]^T`。

把这个局部 `Ct_rad(X,Y,z)` 重新积分回 face Jacobian 后，与上一轮 FD face Jacobian 的最大相对差：

|Case|max relative difference|
|---|---:|
|Z0|1.74e-10|
|Z1|3.57e-4|
|Z2|2.20e-3|
|Z3|1.22e-3|
|Z4|1.03e-10|
|Z5|2.11e-4|

因此：

`PREVIOUS FD JACOBIAN USED ONE GLOBAL STEEL Et = NO`

`PREVIOUS FD JACOBIAN IMPLICITLY SAW LOCAL RADIAL-CAP TANGENT = YES`

## 3. ideal-J2 flow tangent audit

审计 tangent 使用 associative ideal-J2 continued-plastic tangent

`Cep = Ce - (Ce*n)(Ce*n)^T/(n^T Ce n)`。

弹性点仍用 `Ce`。yield-surface 点用 actual connected-branch strain increment

`epsdot = eps_D + q_D eps_q + alpha_D eps_alpha`

检查 `n^T Ce epsdot>0`；当前六板 peak 的已屈服 face 区域均为 continued plastic loading，没有出现把全部屈服区重置为 elastic unloading 的情况。

该 J2 tangent 仅是 `AUDIT/TANGENT-SENSITIVITY`，不是未经 source-freeze 的 production replacement。

## 4. Z1 逐阶段计算

### Stage A — D=0.400，全弹性

`D=0.400000`

`q=0.00217778`

`alpha=0.0418927`

`M=0.0584529`

`P=16.962121 MN`

`center VM/fy=0.76606`

`edge VM/fy=0.65233`

### Stage B — center first yield

`D=0.508850274`

`q=0.003320445`

`alpha=0.076845612`

`M=0.099128347`

`P=19.871434 MN`

`center VM/fy≈1.00000`

`quarter VM/fy=0.95396`

`edge VM/fy=0.83355`

在这个 first-yield state，center 的 ideal-J2 partial axial tangent retention 已约为 `C_yyyy^ep/C_yyyy^e=0.02843`。

### Stage C — yield front 到 x/b=0.25

`D=0.529928234`

`q=0.003630667`

`alpha=0.087125669`

`M=0.111359989`

`P=20.321044 MN`

`center VM/fy=1.04986`

`quarter VM/fy≈1.00000`

`edge VM/fy=0.86942`

### Stage D — yield front 到 x/b=0.125

`D=0.557246634`

`q=0.004180674`

`alpha=0.105355906`

`M=0.134293734`

`P=20.686732 MN`

`center VM/fy=1.12287`

`quarter VM/fy=1.06569`

`1/8 VM/fy≈1.00000`

`edge VM/fy=0.91738`

### Stage E — current ON peak

`D_u=0.582466694`

`q_u=0.004879405`

`M_u=0.165729871`

`alpha_u=0.131555694`

`P_u=20.812048 MN`  `[current radial-stress equilibrium path]`

压缩侧外表面中线：

|x/b|VM/fy|radial Cyyyy/Ce|J2 Cyyyy/Ce|actual-path axial increment retention|
|---:|---:|---:|---:|---:|
|0|0.963513|1.000000|1.000000|1.000000|
|0.125|1.057843|0.042092|0.122621|—|
|0.25|1.133270|-0.000777|0.053373|0.104698|
|0.375|1.182131|-0.010599|0.021582|—|
|0.5|1.199165|-0.010954|0.013547|0.066618|

face-volume audit at current peak：

`both faces yielded fraction≈38.14%`

`compression-side skin yielded≈72.32%`

`opposite skin yielded≈3.97%`

`J2 z^2-weighted face Cyyyy retention≈0.6719`

`radial-cap z^2-weighted face Cyyyy retention≈0.6462`。

## 5. 六板 yield-front 顺序

|Case|center first yield D / P(MN)|quarter yield D / P|1/8 yield D / P|edge yield D / P|current peak D / P|
|---|---|---|---|---|---|
|Z0|0.820511 / 33.4963|0.846385 / 33.9524|0.877378 / 34.2215|peak 前未到|0.895406 / 34.2648|
|Z1|0.508850 / 19.8714|0.529928 / 20.3210|0.557247 / 20.6867|peak 前未到|0.582467 / 20.8120|
|Z2|1.009475 / 37.1886|1.041258 / 37.6619|1.081326 / 37.8061，略晚于 peak|peak 前未到|1.077007 / 37.8097|
|Z3|0.605026 / 39.3431|0.625207 / 39.9319|0.648873 / 40.2937|peak 前未到|0.664451 / 40.3617|
|Z4|0.865887 / 62.9614|0.885424 / 63.4474|0.906966 / 63.6988|0.934978 / 63.6452，晚于 peak|0.918014 / 63.7293|
|Z5|0.912752 / 13.9901|0.920900 / 14.0406|0.929316 / 14.0664|0.938698 / 14.0783|0.939442 / 14.0786|

所以更准确的顺序是：所有六板 center first；随后 yield front 向侧边推进，但其在 current peak 前推进到什么位置因板而异。不能把它概括成“所有板都在 peak 前扩展到同一个固定位置”。

## 6. current peak 的空间软化程度

|Case|center VM/fy|edge VM/fy|center J2 Cyyyy retention|edge retention|both-face yielded|compression-skin yielded|J2 z2-weighted face retention|
|---|---:|---:|---:|---:|---:|---:|---:|
|Z0|1.12650|0.96413|0.04599|1.000|27.69%|55.38%|0.7509|
|Z1|1.19916|0.96351|0.01355|1.000|38.14%|72.32%|0.6719|
|Z2|1.12987|0.90512|0.01623|1.000|17.30%|34.60%|0.8366|
|Z3|1.12812|0.96888|0.04814|1.000|28.72%|57.45%|0.7427|
|Z4|1.06701|0.98161|0.09170|1.000|26.72%|53.44%|0.7657|
|Z5|1.03029|1.00079|0.13394|0.16390|49.11%|91.71%|0.5832|

其中

`eta_s,I = integral(C_yyyy^t z^2 dVs) / integral(C_yyyy^e z^2 dVs)`

只是 bending-material tangent 的审计量，不替代 full KZ；full KZ 仍要保留全部 directional tangent 和 current-stress geometric terms。

## 7. current peak 的 yielded-band 宽度

在 `Y=pi/2`、压缩侧外表面上，令从侧边起第一个 `VM/fy=1` 位置为 `x_f/b`，则中心 yielded band 宽度为 `1-2x_f/b`：

|Case|x_f/b|center yielded band / b|
|---|---:|---:|
|Z0|0.07046|0.8591|
|Z1|0.04633|0.9073|
|Z2|0.13591|0.7282|
|Z3|0.06284|0.8743|
|Z4|0.07185|0.8563|
|Z5|0|1.0000|

这说明 whole-face volume yield fraction 并不能代替鼓波中线上的局部软化前沿。

## 8. 对当前 Pu 的影响

保持 current radial stress map 不变，只显式计算其自身解析 local tangent，结果与上一轮 FD Jacobian 匹配，因此 current radial-stress equilibrium peak 数值不会因“把局部 radial tangent 展开写出来”而改变。

但把 positive-semidefinite J2 tangent 仅代入 tangent sensitivity 时：

|Case|current radial-map dP/dD at peak (MN/D)|J2 tangent-only sensitivity dP/dD (MN/D)|
|---|---:|---:|
|Z0|~0|+1.5158|
|Z1|+0.00076|+0.7042|
|Z2|+0.00979|+2.2250|
|Z3|+0.02823|+2.6364|
|Z4|-0.00427|+2.1688|
|Z5|-0.31747|+0.2640|

所以旧 peak 在 physically admissible J2 tangent 下不再是 tangent-neutral point。current radial cap 的过软/局部负 tangent 很可能把 current limit 提前了。

但是 `J2 tangent-only sensitivity != new production Pu`。新的 production Pu 必须在 same-source steel stress+tangent operator freeze 后重新求解。

## 9. 更新后的治理状态

`STEEL FACE NONUNIFORM YIELD ORDER = CONFIRMED`

`CENTER-FIRST YIELD FRONT = CONFIRMED`

`WHOLE-STEEL GLOBAL Et=0 MODEL = REJECTED`

`WHOLE-STEEL GLOBAL Es AFTER CENTER YIELD = REJECTED`

`CURRENT RADIAL-CAP LOCALITY = CONFIRMED`

`CURRENT RADIAL ANALYTIC TANGENT vs PRIOR FD JACOBIAN = MATCH`

`CURRENT RADIAL-CAP TANGENT PHYSICAL ACCEPTANCE = FAIL / NOT PRODUCTION-FROZEN`

`OLD Z0-Z5 Pu FULL-STEEL-TANGENT PRODUCTION CERTIFICATE = NOT PASSED`

下一步应先 freeze 一个 source-consistent plane-stress steel current operator，同时返回 `sigma_s(epsilon)` 和 `Ct_s(epsilon)`；再把 `Ct_s(X,Y,z)` 解析编译进 `KZ_s^mat + KZ_s^geo`，优先重跑 Z1/Z4 后再做 Z0–Z5 batch。

## 10. formal/audit boundary

Formal counters 保持：

`N_formal_spatial_sampling=0`

`N_formal_spatial_quadrature=0`

`N_formal_spatial_subdomains=1`

`N_formal_thickness_quadrature=0`

本轮 dense VM/tangent profile、yield-front localization、face-volume yield fraction 都是 direct-continuum audit oracle，不获得正式理论身份，不用于拟合、选根或 comparator calibration。

## 11. 同批数据文件

- `semantic_v2/60_validation/steel_shell/20260817_2342__NZSCCM__Z0_Z5__STEEL_YIELD_FRONT_SEQUENCE.csv`
- `semantic_v2/60_validation/steel_shell/20260817_2342__NZSCCM__Z0_Z5__STEEL_LOCAL_TANGENT_PEAK_PROFILE.csv`
- `semantic_v2/60_validation/steel_shell/20260817_2342__NZSCCM__Z0_Z5__STEEL_TANGENT_SEQUENCE_SUMMARY.csv`

Theory/source anchors:

- `20260814_TUNK__NZSCCM__STEEL_SHELL__YUN_SSSS_IDEAL_EP_POSTBUCKLING_TANGENT__THEORY_DERIVATION.md`
- `20260813_1834__NZSCCM__STEEL_SHELL__J2_DEFORMATION_THEORY_SOURCE_CURVE_PLANE_STRESS__MATERIAL_OPERATOR_DERIVATION.md`
- `20260816_1217__NZSCCM__NC_STEEL_SHELL_PANEL__UNIFIED_WORKFLOW_V1_ADAPTER_BRIDGE__GOVERNANCE.md`
- `20260817_1407__NZSCCM__Z6_N48_FAMILY_SOURCE_COMPILER_AND_AIRY_MEMBRANE_REDIStribution__THEORY.md`
