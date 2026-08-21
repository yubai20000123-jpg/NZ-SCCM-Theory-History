# NZ-SCCM — web/rebar phase-volume conservation execution report

时间：2026-08-21 15:15 +08:00  
状态：`EXECUTED / NON-CALIBRATING / PRE-MEMBRANE BACKBONE`

## 0. 目的

本轮只检查一个物理问题：历史 pre-membrane 模型是否把钢腹板/钢筋所占据的材料体积仍按 100% 混凝土重复计算。

冻结：

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
NGUYEN_SECOND_ORDER
R10
N48-C1/MM / source-consistent case interval
CAYLEY-HAMILTON
GENERAL-D15
NO NEW MEMBRANE REDISTRIBUTION
NO RITZ H2/H4/...
NO TEST/COMPARATOR LOAD IN ROOT OR PARAMETER SELECTION
```

---

## 1. Z0-Z5 原截面参数与腹板材料账本

周思铭原始 MCFSTW 参数按 `[ns,ls,h,ts,fy,fcu,a,b]`：

|case|ns|ls mm|h mm|ts mm|fy MPa|fcu MPa|a mm|b mm|tc=h-2ts mm|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|Z0|30|200|130|4|355|40|6000|6000|122|
|Z1|30|200|100|4|235|40|6000|6000|92|
|Z2|30|200|130|4|460|40|6000|6000|122|
|Z3|30|200|130|4|355|60|6000|6000|122|
|Z4|40|200|200|4|355|40|6000|8000|192|
|Z5|10|200|130|4|355|40|3000|2000|122|

由 `b=ns*ls`，内部纵向钢腹板连续等效体积分数严格为

\[
\rho_w=\frac{t_s}{l_s}=0.02.
\]

等效腹板钢面积

\[
A_w=\rho_wbt_c=n_st_st_c.
\]

外面板面积

\[
A_{sh}=2bt_s.
\]

逐项：

|case|Aw mm2|Aconcrete remaining mm2|Aouter mm2|Aw+Aouter mm2|Zhou As mm2|
|---|---:|---:|---:|---:|---:|
|Z0|14640|717360|48000|62640|62640|
|Z1|11040|540960|48000|59040|59040|
|Z2|14640|717360|48000|62640|62640|
|Z3|14640|717360|48000|62640|62640|
|Z4|30720|1505280|64000|94720|94720|
|Z5|4880|239120|16000|20880|20880|

因此钢腹板补回是严格几何恒等式，不是经验加项。

---

## 2. 腹板相位公式

历史 H0 合同已给出且本轮原样采用：

\[
P=(1-\rho_w)P_{c,full}+P_w+P_{sh},
\]

\[
R_q=(1-\rho_w)R_{q,c,full}+R_{q,w}+R_{q,sh}.
\]

腹板沿加载方向采用连续理想弹塑性当前映射：

\[
u=E_s\varepsilon_y/f_y,
\qquad r=u^2,
\]

\[
\alpha(r)=\begin{cases}1,&r\le1,\\r^{-1/2},&r>1,\end{cases}
\]

\[
\sigma_y^w=f_yu\alpha(r).
\]

这意味着 `100% concrete + extra web steel` 明确禁止；腹板钢必须替换同体积混凝土。

---

## 3. 本轮重新建立并回归计算器

在加入腹板前，先用 high-order direct-current audit evaluator 复现原 A500/local-progressive D15 的 Z0-Z5 峰值：`Pc`、外钢板 `Psh` 与 `Rq` 均与历史 D15 台账一致至约 1e-3% 或更好；Z2 使用其历史 source-consistent compiler interval `[-1.35,0.15]`。

随后激活腹板相位。旧 H0 固定状态 `Pc_eff,Pw,Psh,Rq` 被逐项复现，证明本轮 evaluator 与 2026-08-15 H0 是同一个物理对象。

本轮与旧 H0 的区别只有一点：**Z6 不再阻断 Z0-Z5**。对 Z0-Z5 各自继续其 connected `Rq=0` branch，求第一局部荷载极限点。

---

## 4. Z0-Z5 完整新 Pu

|case|D_u|q_u|Pc,eff MN|Pw MN|Psh MN|Pu MN|Zhou original MN|error|
|---|---:|---:|---:|---:|---:|---:|---:|---:|
|Z0|0.970955|0.001165|16.771649|5.379866|18.388948|40.540463|36.945541|+9.730%|
|Z1|0.622414|0.001753|10.272964|2.605967|11.709886|24.588816|23.721432|+3.657%|
|Z2|1.207021|0.001659|14.834837|6.758155|23.003972|44.596964|41.213379|+8.210%|
|Z3|0.725662|0.001341|24.851640|5.405368|18.483294|48.740303|44.320271|+9.973%|
|Z4|0.994273|0.000536|40.225731|11.405124|24.916565|76.547420|70.187272|+9.062%|
|Z5|1.005412|0.000159|6.700713|1.816691|6.275136|14.792539|14.681648|+0.755%|

全部峰值均处于各自历史 material compiler interval 内。高分辨 direct-current audit 对上述 Pu 的变化远低于 0.01%，故空间 localizer 不是结果来源。

### 4.1 误差结构改变

不计腹板的旧结果：

```text
mean signed = -3.154 %
MAE         =  3.682 %
RMSE        =  4.853 %
sample std  =  4.041 pp
max |error| = 10.245 %
```

计入腹板材料相位：

```text
mean signed = +6.898 %
MAE         =  6.898 %
RMSE        =  7.720 %
sample std  =  3.798 pp
max |error| =  9.973 %
all six signed errors > 0
```

所以不能说“计入腹板后 MAE 更好”；事实上 MAE 变大。但误差由正负抵消转为完全同号、幅值较集中的系统性偏高。

机械解释是：旧模型的低误差中包含了“遗漏真实腹板材料”与其他保守机制的相互抵消。补回真实材料以后，剩余偏差更可能暴露当前仍明确遗漏的离散腹板支承/局部腹板屈曲/拓扑稳定作用。该解释是当前机制假设，不作为经验修正系数。

---

## 5. 局部钢材解析编译敏感性

在 degree-24 峰值 D 处重新闭合 q，使用同一精确 ideal-EP radial-cap 材料函数但改变材料坐标 Chebyshev 编译阶数：

|case|Pu deg16 MN|Pu deg24 MN|Pu deg32 MN|16-32 spread / deg24|
|---|---:|---:|---:|---:|
|Z0|40.727780|40.540463|40.293969|1.070%|
|Z1|24.706325|24.588816|24.432326|1.114%|
|Z2|44.651205|44.596964|44.516793|0.301%|
|Z3|49.055709|48.740303|48.353572|1.441%|
|Z4|77.015769|76.547420|75.995679|1.333%|
|Z5|14.903836|14.792539|14.662401|1.632%|

因此本轮可以锁定**理论材料函数**，但不能把 `degree=24` 本身提升为最终 production 常数。材料坐标编译阶次属于解析实现层，后续按非试验数据的材料函数收敛门槛冻结。

---

## 6. Swartz24 的严格同源等效：钢筋体积替换

历史 RC 闭式为 full-gross concrete + explicit rebar：

\[
P=P_c+P_s,
\qquad R_q=R_{q,c}+R_{q,s}.
\]

因此钢筋所占体积在旧 `Pc` 中仍被视为混凝土。与钢腹板完全同源的体积守恒式为

\[
\rho_{s,tot}=\rho_{s,x}+\rho_{s,y},
\]

\[
\boxed{P=(1-\rho_{s,tot})P_c+P_s},
\]

\[
\boxed{R_q=(1-\rho_{s,tot})R_{q,c}+R_{q,s}}.
\]

Swartz24 的 `rho_s,tot=0.2%-1.0%`，故这是小扰动。

### 6.1 24 块盲算冻结点的一阶约束极值重算

在原极限点

\[
\nabla P=\mu\nabla R_q,
\]

故对 `r=rho_s,tot`，不需要保持旧 D/q 不动，极限载荷的一阶同源变化严格满足 envelope/KKT：

\[
\boxed{
\frac{dP_u}{dr}=-P_c+\mu R_{q,c}
},
\]

\[
\mu=\frac{P_{,q}}{R_{q,q}}=\frac{P_{,D}}{R_{q,D}}.
\]

据盲算冻结的同源 `Pc,Rc,Jacobian` 逐板计算：

```text
old blind mean signed = -3.624 %
old blind MAE         = 12.056 %
old blind RMSE        = 13.518 %
old blind std         = 13.303 pp
old max |error|       = 22.302 %

phase-volume mean     = -4.179 %
phase-volume MAE      = 12.101 %
phase-volume RMSE     = 13.590 %
phase-volume std      = 13.209 pp
phase max |error|     = 22.061 %
```

结论：体积守恒对 Swartz24 每块板仅改变约 0.7%-1.0% 以内，不能解释原 ±20% 的试件散差，也没有显著改善总体 MAE。它只是修正了一个小的材料账本重复计数。

### 6.2 Case21 完整重闭合验证

为验证一阶公式没有偷换极限点，Case21 用同一 R10→N48→CH current map 和钢筋闭式重新求解：

旧：

\[
D_u=0.8359179022,\quad q_u=0.00178978936,\quad P_u=368.1893375\;kN.
\]

体积守恒后：

\[
\boxed{D_u=0.8353000184},
\]

\[
\boxed{q_u=0.00179132513},
\]

\[
\boxed{P_u=365.4735386\;kN}.
\]

一阶公式给 `365.4737394 kN`，与完整重闭合差 `0.0002009 kN`，相对约 `5.5e-5 %`。因此对 0.2%-1.0% 的 Swartz 钢筋体积分数，一阶批量审计足以判断该机制量级。

---

## 7. 总结裁决

```text
STEEL_WEB_MATERIAL_VOLUME = MUST_INCLUDE
REBAR_REPLACED_CONCRETE_VOLUME = SHOULD_INCLUDE
EMPIRICAL_CORRECTION_FACTOR = NO
NEW_MEMBRANE_REDISTRIBUTION = NO
RITZ_EXPANSION = NO
```

Z0-Z5 补回腹板以后得到统一正偏约 `+0.8% ~ +10.0%`，符合“宁可保留可解释的系统偏差，也不靠机制遗漏获得偶然零误差”的治理原则。

Swartz24 的相位体积守恒只产生小修正，无法消除试件间大散差；因此不应再为追逐单块 Swartz 误差扩张膜场或引入经验项。

正式相位体积守恒理论另见同时间戳 `PRE_MEMBRANE_MULTIPHASE_VOLUME_CONSERVING_THEORY_V1`。