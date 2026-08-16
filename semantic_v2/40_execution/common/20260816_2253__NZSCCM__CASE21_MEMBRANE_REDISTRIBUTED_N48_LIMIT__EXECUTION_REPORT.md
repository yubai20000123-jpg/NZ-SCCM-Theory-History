# NZ-SCCM Case21 五膜力重分布 N48 极限承载力计算

**时间：2026-08-16 22:53 +08:00**  
**门禁：`CASE21_N48_MEMBRANE_DIRECT_LIMIT_AND_KZ_GATE`**

## 1. 本轮目标

本轮不再发展新的材料积分后端，也不再沿 `q=1e-4,2e-4,...` 做密集加载步追踪。目标只有一个：在已经建立的五项膜内重分布理论下，直接求 Case21 的真实平衡极限状态，并在同一状态执行 `KZ` 审计。

外部变量仍为

\[
g=(D,q),\qquad A=bq.
\]

内部膜变量为

\[
r=(r_0,r_{20},r_{22},s_{02},s_{22}).
\]

内部平衡：

\[
R_m(D,q,r)=0.
\]

鼓曲广义平衡：

\[
R_q(D,q,r)=0.
\]

极限点为连接平衡支上首个荷载驻值。

## 2. 生产实现身份

本轮 Case21 使用已经实际闭合过的 2026-08-12 Case21-local N48-C1/MM + Cayley-Hamilton + General-D15 evaluator：

```text
compiler interval = [-1.15,+0.12]
U = N48-C1
C = N48-C1
T = N48-C1 constrained-minimax
T7 = N48-C1
structural coefficient corrector cap = 28
formal spatial sampling = 0
formal spatial quadrature = 0
formal spatial subdomains = 1
formal thickness quadrature = 0
```

先回归旧 `r=0` Case21 指纹：

```text
frozen P = 365.58042756532977 kN
reproduced P = 365.58042692483133 kN
Delta P = -6.4049844e-7 kN
```

因此本轮 evaluator 与 18:02 Case21 生产实现同族。

## 3. 为什么没有继续密集 continuation

前两个小 q 点只用于确认加入五个膜变量后存在从原点长出的 connected branch。随后本轮直接采用稀疏广义坐标求解：

1. N12 coefficient-space evaluator 用作低成本 predictor/corrector；
2. 仅在接近极限区使用 pseudo-arclength 穿越 `D`/`q` 参数折返点；
3. 极限附近全部回到 N28 正式 corrector；
4. N28 平衡状态用稀疏三点荷载括峰，而不是建立加载步历史；
5. 最终状态执行 N28 compiler-domain、reinforcement branch 和 same-state KZ。

这里的 corrector 只是 7 个有限广义变量的代数求根后端，不是材料点 Newton、空间积分点历史或正式加载步理论。

## 4. N12 极限区定位

N12 在 connected branch 上给出极限邻域，代表状态包括：

```text
D=0.45722216, q=0.00184546, P=320.8360216321 kN
D=0.46073179, q=0.00183633, P=321.1199872834 kN
D=0.46222350, q=0.00183026, P=321.1320342649 kN
```

沿同一平衡支的单位切向荷载导数由正变负：

```text
+11.9978 -> -8.0475
```

因此首个荷载极大值已经被括住。

## 5. N28 正式极限括峰

N28 corrector 在同一 connected branch 上得到以下三个极限邻域平衡状态。`s` 只是局部 pseudo-arclength 坐标，不是加载步参数：

| local s | P (kN) | status |
|---:|---:|---|
| -0.001 | 320.7448725628 | equilibrium |
| -0.002 | 320.7488729415 | equilibrium |
| -0.004 | 320.7455659492 | equilibrium |

三点二次驻值定位：

```text
s_peak_fit = -0.0025613195752152216
P_peak_fit = 320.7494667485 kN
```

在该位置重新执行 N28 equilibrium corrector 后，最终冻结状态为

\[
\boxed{D_u=0.4597278541813354}
\]

\[
\boxed{q_u=0.0018330938013757293}
\]

\[
\boxed{A_u=bq_u=2.2363744376783896\ \mathrm{mm}}
\]

五个膜内响应坐标：

\[
\boxed{
 r_u=
[-0.0124758024832,
 -0.00714186410334,
 +0.0469948841427,
 +0.0419461180672,
 -0.0998362974763]
}
\]

同一状态：

```text
Cm = 0.029575053233322175
Cb = 0.06847083605353030
Pc = 304.05427812103903 kN
Ps =  16.69490720454312 kN
P  = 320.74918532558220 kN
Rq = +2.3335610177355193e-4 kN mm
||Rm||2 = 3.489005279868966e-6
```

故本轮 Case21 膜力重分布极限承载力冻结为

\[
\boxed{P_u=320.75\ \mathrm{kN}}
\]

按当前计算精度保留到 `0.01 kN` 已足够；更多小数仅作为复现记录。

## 6. 连续 compiler-domain 证书

最终状态的低阶连续运动学可写成 `u=sinX,v=sinY,w=(zeta+1)/2` 上的有限多项式。对

```text
0.12 - X11
det(0.12 I - X)
X11 + 1.15
det(X + 1.15 I)
```

执行 tensor-product Bernstein coefficient enclosure，所有 Bernstein coefficient 均为正，最小值分别为

```text
0.019818419276368335
0.012584829997801125
1.0807409482494919
0.5069185061516994
```

因此整个连续完整半波严格满足

\[
\boxed{-1.15<\lambda_-\le\lambda_+<0.12}.
\]

这不是空间点扫描。

## 7. 钢筋 branch 证书

中面单层钢筋的连续应变 Bernstein enclosure：

```text
x-direction epsilon_s in [+6.35824e-5,+2.60021e-4]
y-direction epsilon_s in [-1.25716e-3,-6.0269e-4]
max |epsilon_s| ~= 0.00125716 < epsilon_y=0.00265
```

所以全钢筋场保持弹性，钢筋 branch 不需要空间分区。

## 8. same-state KZ

为验证 N28 current-tangent implementation，先在 18:02 旧 Case21 `r=0` 极限状态回归：

```text
computed:
KZc_mat = +765.4632623203 N/mm
KZc_geo = -719.5765266712 N/mm
KZs_mat =    0
KZs_geo =  -45.5059868447 N/mm
KZ_total=   +0.3807488044 N/mm

frozen 18:02 total ~= +0.3795268508 N/mm
```

误差约 `1.22e-3 N/mm`，说明当前有限差分只用于解析 N48 current-map 的一致切线作用校核，并未改变结构空间积分身份。

在新的膜力重分布极限状态：

```text
KZc_mat = +871.8683854054 N/mm
KZc_geo = -587.3952216885 N/mm
KZs_mat =    0
KZs_geo =  -24.3022580441 N/mm
--------------------------------
KZ_total= +260.1709056728 N/mm
```

所以

\[
\boxed{K_Z(P_u)=+260.17\ \mathrm{N/mm}>0}.
\]

当前控制不是 tangent loss，而是 connected branch 上的第一个荷载极大值。

## 9. 与旧 Case21 无膜重分布结果的关系

旧 18:02 `r=0`：

```text
P_u(old)=365.5804275653 kN
```

新五膜重分布：

```text
P_u(new)=320.7491853256 kN
Delta=-44.8312422397 kN
relative change=-12.2630312947 %
```

这说明膜力重分布不是微小数值修正，而是显著改变 Case21 的 current stress redistribution 和极限点位置。

## 10. 试验值只在理论结果冻结后比较

当前 Case21 experiment-only source 文件给出

```text
P_exp=336 kN
```

因此

```text
P_u/P_exp = 0.9546106706
error = -4.5389329388 %
```

相较旧 `r=0` 结果的 `+8.80%` 高估，新膜力重分布结果变为约 `-4.54%` 低估，绝对误差明显减小。

## 11. 门禁结论

```text
CASE21_N48_1802_FINGERPRINT = PASS
FIVE_MEMBRANE_EQUILIBRIUM = PASS
TOTAL_Rq_EQUILIBRIUM = PASS
CONNECTED_FIRST_LOAD_MAXIMUM = PASS
CONTINUOUS_COMPILER_DOMAIN = PASS_BERNSTEIN
REBAR_SUPPORTED_BRANCH = PASS_ELASTIC
SAME_STATE_KZ = PASS_POSITIVE
CONTROL = FIRST_CONNECTED_LOAD_MAXIMUM
CASE21_MEMBRANE_REDISTRIBUTED_Pu = 320.75 kN
FORMAL_SPATIAL_SAMPLING = 0
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_SPATIAL_SUBDOMAINS = 1
FORMAL_THICKNESS_QUADRATURE = 0
```
