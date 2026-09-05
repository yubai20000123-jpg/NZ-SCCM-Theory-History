这次我确实把 **BH050 的新兼容 Airy 主链跑起来了，并直接和 FEM 对比**。结果已经足够把问题进一步缩小，而且出现了一个很重要的结论：

```math
\boxed{\text{现在最主要的问题已经不是 Airy，也不是 global 形函数阶数。}}
```

真正没有闭合的是：

```math
\boxed{ \text{compatible global Airy field} \;\longleftrightarrow\; \text{Multiwave local steel generalized work} }
```

之间的耦合。

先把结果直接给出来。

---

# 1. 这次实际跑的模型

BH050 使用统一原始输入：

```math
b=2500,\quad a=5000,\quad t_c=42,\quad t_s=4{\rm mm},
```

```math
A_w=1332{\rm mm^2}, \quad E_s=206000,\quad f_y=355{\rm MPa},
```

```math
E_c=43400,\quad f_c=141.1{\rm MPa}, \quad\varepsilon_{c0}=0.0035.
```

Multiwave 仍使用当前冻结的条带：

```math
{\rm TOP}:\quad n=(3,4,5,6),
```

```math
\omega=(0.225,0.225,0.225,0.325),
```

```math
{\rm BOTTOM}:\quad n=(3,4,5,20),
```

```math
\omega=(0.225,0.45,0.225,0.10).
```

这与当前 BH050 smoke-test 输入一致。

但全局前端已经**彻底删除 R4 独立曲率**：

```math
\boxed{ \kappa_x=-w_{,xx}, \qquad \kappa_y=-w_{,yy}, \qquad \kappa_{xy}=-2w_{,xy}. }
```

因此不存在：

```math
\kappa_y^{R4}.
```

这一点正针对最新审计发现的问题：BH050 的 R4 曲率是 `6.561\times10^{-5}/{\rm mm}`，而相同 `q` 的几何曲率只有 `1.947\times10^{-5}/{\rm mm}`，后者反而接近 FEM `2.039\times10^{-5}/{\rm mm}`。

---

# 2. UHPC 也按刚才讨论的 V0 思路换掉了

本轮诊断采用：

```math
\boxed{ 6\text{ 段压缩 PWL} + 17\text{ 段拉伸 PWL} + \text{Poisson closure} + K_{TC}=1.54{\rm GPa}. }
```

实际一维材料逼近误差为：

```math
\boxed{ \max|\Delta\sigma_c|/f_c=1.84\% }
```

拉伸：

```math
\boxed{ \max|\Delta\sigma_t|/f_{t,\max}=3.38\%. }
```

并专门在原点附近增加了一个极短弹性段，使：

```math
E_0\approx E_c
```

严格保住。数值检查给：

```math
\sigma_x(10^{-7},0)=0.004516{\rm MPa},
```

初始 plane-stress 理论应为：

```math
0.004521{\rm MPa}.
```

也就是说初始刚度误差只有约：

```math
0.1\%.
```

所以这一轮没有因为 PWL 把初始 Airy 刚度破坏掉。

---

# 3. 最关键的比较：取 FEM 实际全局曲率对应的 `q`

最新 FEM-U2 给 BH050：

```math
\kappa_{y,FEM} = 2.03851\times10^{-5}/{\rm mm}.
```

而当前全局模态：

```math
\kappa_y^g=\frac{\pi^2q}{b}.
```

因此完全独立地反算：

```math
\boxed{ q_{FEM} = \frac{\kappa_{y,FEM}b}{\pi^2} = 0.00516361. }
```

这个 `q` **只用于同状态后验比较，不用于理论选根**。

然后我分别跑两套：

### A. compatible Airy + AC-UHPC + R04 steel

也就是暂时不让钢壳发生局部后屈曲折减。

### B. compatible Airy + AC-UHPC + 当前 Multiwave R02/R06

也就是把当前 qU-off Multiwave 钢壳直接接进新的 compatible global field。

结果如下。

| BH050 @ `q=0.00516361`FEMcompatible + R04compatible + Multiwave |             |             |               |
| --------------------------------------------------------------- | ----------- | ----------- | ------------- |
| `P` / MN                                                        | **12.5727** | **13.0994** | **10.1626**   |
| Pu同状态误差                                                         | —           | **+4.19%**  | **−19.17%**   |
| upper steel / MN                                                | 2.174       | 3.031       | **2.016**     |
| lower steel / MN                                                | 2.113       | 3.031       | **2.134**     |
| steel total / MN                                                | **4.289**   | 6.062       | **4.150**     |
| UHPC+web / MN                                                   | **8.284**   | 7.038       | **6.012**     |
| steel share                                                     | 34.11%      | 46.28%      | 40.84%        |
| `\bar\varepsilon_y`                                             | 约 FEM 端缩量级  | −0.001469   | **−0.001238** |

这里 FEM 分项按你前面给出的最新 ODB 力分配直接换算。

这个表非常有信息量。

---

# 4. 第一条非常强的结论：compatible Airy 的几何骨架没有崩

只把 R4 删除、让：

```math
q\rightarrow w\rightarrow\kappa
```

严格成立以后，在 FEM 实际几何状态：

```math
q=0.005164
```

上，即使使用最粗的 R04 steel：

```math
P=13.0994{\rm MN},
```

和 FEM：

```math
12.5727{\rm MN}
```

只差：

```math
\boxed{+4.19\%.}
```

而且：

```math
\boxed{ \kappa_y^g = 2.03851\times10^{-5}/{\rm mm} }
```

此时当然与 FEM-U2 完全一致，因为这个比较状态就是由 FEM 曲率换算而来。

更有意义的是此前旧 Airy/R4 在几乎同样的 `q` 上会得到约三倍大的独立 `\kappa_y^{R4}`。审计已经证明这不是 global displacement curvature。

所以：

```math
\boxed{ \text{删除 R4 curvature relaxation 是正确方向。} }
```

---

# 5. 但 R04 为什么总荷载这么准？其实内部还是错的

看分项立即暴露出来。

FEM：

```math
P_s^{FEM}\approx4.289{\rm MN}.
```

R04：

```math
P_s^{R04}=6.062{\rm MN}.
```

高了：

```math
\boxed{41.3\%.}
```

与此同时 FEM：

```math
P_{U+w}^{FEM}\approx8.284{\rm MN},
```

R04 只有：

```math
7.038{\rm MN}.
```

所以：

```math
\boxed{ 13.10{\rm MN}\approx12.57{\rm MN} }
```

不能解释成“R04 已经正确”。

实际上是：

```math
\boxed{ \text{steel 偏高} + \text{UHPC 偏低} \rightarrow \text{总荷载误差碰巧抵消}. }
```

这和我们此前一直强调的：

```math
P_{\rm total}\text{ 对} \not\Rightarrow \text{内部受力对}
```

完全一致。

---

# 6. 然后事情变得非常有意思：换成 Multiwave，钢力反而几乎对了

新的 compatible field + 当前 qU-off Multiwave 得：

```math
P_s^+=2.016{\rm MN},
```

```math
P_s^-=2.134{\rm MN}.
```

FEM：

```math
P_s^+\approx2.174{\rm MN},
```

```math
P_s^-\approx2.113{\rm MN}.
```

也就是说：

### upper steel

```math
\frac{2.016-2.174}{2.174} = -7.3\%.
```

### lower steel

```math
\frac{2.134-2.113}{2.113} = +1.0\%.
```

总钢力：

```math
P_s^{MW}=4.150{\rm MN}
```

对比：

```math
P_s^{FEM}=4.289{\rm MN},
```

只有：

```math
\boxed{-3.2\%.}
```

这个结果我认为很重要。

因为它说明：

```math
\boxed{ \textbf{Multiwave 对钢壳轴力衰减的量级其实非常合理。} }
```

至少 BH050 在真实 global-curvature 状态下是这样。

---

# 7. 真正出问题的是：一接 Multiwave，UHPC 的全局膜压缩跟着塌了

Multiwave 后：

```math
P_{U+w}=6.012{\rm MN}.
```

而 FEM 是：

```math
8.284{\rm MN}.
```

差：

```math
\boxed{-27.4\%.}
```

与此同时 mean longitudinal strain 从 R04 的：

```math
\bar\varepsilon_y=-0.001469
```

进一步松弛到：

```math
\boxed{ \bar\varepsilon_y=-0.001238. }
```

于是总荷载变成：

```math
10.163{\rm MN},
```

比 FEM 低：

```math
\boxed{-19.17\%.}
```

所以现在问题已经非常具体了：

```math
\boxed{ \text{不是 Multiwave 把 steel 算得太低。} }
```

相反：

```math
\boxed{ \text{Multiwave steel 的绝对轴力已经相当接近 FEM。} }
```

真正的问题是：

> **current qU-off R02/R06 作为“平均钢应力算子”塞进 compatible global equilibrium 后，降低了钢力，却没有把相应 local/global generalized work 正确反馈到整体平衡，于是全局方程通过降低** **`\bar\varepsilon_y`** **来重新平衡。**

结果 UHPC 也被一起卸载。

我现在会把这个写成：

```math
\boxed{ \text{STEEL FORCE REDUCTION = approximately right} }
```

但：

```math
\boxed{ \text{LOCAL}\rightarrow\text{GLOBAL WORK TRANSFER = wrong/incomplete}. }
```

---

# 8. “是不是因为你的 global 形函数还太少？”——我也直接跑了

这次没有停在 `N=1`。

compatible `u,v` 谐波分别继续扩到：

```math
N=1,\quad2,\quad3.
```

仍在同一个：

```math
q_{FEM}=0.00516361
```

比较。

### compatible + R04

```math
\begin{array}{c|c} N&P/{\rm MN}\\\hline 1&13.09945\\ 2&13.09745\\ 3&13.07900 \end{array}
```

从 `N=1\to3` 只变化：

```math
\boxed{0.16\%.}
```

### compatible + Multiwave

```math
\begin{array}{c|c} N&P/{\rm MN}\\\hline 1&10.16257\\ 2&10.16230\\ 3&10.15556 \end{array}
```

变化：

```math
\boxed{0.07\%.}
```

所以至少对于 BH050：

```math
\boxed{ \textbf{“global basis 不够多”基本可以从第一嫌疑名单删除。} }
```

这也回答了我们前面反复争论的那个问题。

这里不是：

> 3 个不够，要不要 11 个？

目前：

```math
1\rightarrow2\rightarrow3
```

已经几乎完全不动。

真正缺的不是更多 global basis。

---

# 9. 我没有停在那里，还把之前那个 qU 黑箱真正编出来了

这一点也做成功了。

历史 exact GL 运动学明确给：

```math
d=U^2-A_0^2,
```

以及：

```math
\boxed{ \Delta = s_f b \left[ (q_0+q)U-q_0A_0 \right]. }
```

并进入：

```math
m_x,\quad m_y,\quad m_\gamma
```

以及：

```math
K_{d\Delta},\quad K_{\Delta\Delta}.
```

这些式子的源头在此前完整 qU 推导中已经存在。

完整 augmented local energy 则包含：

```math
t_sE_sK_Ad^2 + 2t_sE_sK_{d\Delta}d\Delta + t_sE_sK_{\Delta\Delta}\Delta^2.
```

这次我真正写了一个 combined-frequency harmonic compiler：

```math
\text{LL source} \rightarrow F_{LL},
```

```math
\text{GL source} \rightarrow F_{GL},
```

每一个 Fourier harmonic 直接除以：

```math
(\lambda^2+\mu^2)^2
```

得到 Airy coefficient，再用 exact sinc/end-point moment 做全部 harmonic energy contraction。

没有对 `K_A` 做拟合。

---

# 10. qU compiler 有一个非常强的独立验证：它把已有 `K_A` 精确恢复出来了

对 BH050 不同 local `n`：

| `n`新 compiler `K_A`当前冻结 `K_A` |                                  |                                  |
| ----------------------------- | -------------------------------- | -------------------------------- |
| 3                             | `1.456838643840914\times10^{-9}` | `1.456838643841271\times10^{-9}` |
| 4                             | `2.133353943849692\times10^{-9}` | `2.133353943849617\times10^{-9}` |
| 5                             | `3.346324890739237\times10^{-9}` | `3.346324890739380\times10^{-9}` |

误差已经在：

```math
\boxed{10^{-22}\sim10^{-21}}
```

量级。

所以：

```math
\boxed{ \textbf{GL/qU finite-harmonic compiler 本身已经跑通。} }
```

而当前 R02 的 `K_A`、cubic、七谐波 R06 本来就具有明确的 frozen 解析结构。

这意味着现在已经没有“qU 数学上到底能不能显式计算”的问题。

答案是：

```math
\boxed{\textbf{能。}}
```

---

# 11. 但是这里发现了最后一个不能伪造的数据缺口

GL 项依赖：

```math
\boxed{ x_0,\quad y_0,\quad s_f }
```

也就是**每个真实 local cell 相对于 global sine wave 的 registration/phase**。

因为：

```math
\psi(x_0+\xi,y_0+\eta)
```

进入 GL source。

而当前 Multiwave 输入合同只有：

```math
n_i,\quad\omega_i,\quad L_{x,i},\quad A_{0i}.
```

没有：

```math
\boxed{x_{0i},y_{0i},s_{fi}.}
```

当前历史资料自己也已经指出：`h_x,h_y,h_\gamma,K_{d\Delta},K_{\Delta\Delta}` 会随 cell registration 改变，不能假定一个有利相位。

我实际扫描后也确认：

```math
K_{d\Delta}
```

会随 registration 改变正负号。

所以这一项不能为了“把 BH050 跑准”随便取一个 `x_0,y_0`。

那会重新变成：

```math
\boxed{\text{case-specific fitting}.}
```

---

# 12. 我还是用临时规则做了 qU 敏感性跑，但不把它冒充正式结果

用一个简单的连续条带 registration 做诊断，加入：

```math
qU
```

mean GL 后，BH050 在 `q\approx0.005`：

```math
P\approx10.90{\rm MN}.
```

继续把：

```math
K_{d\Delta},K_{\Delta\Delta}
```

也全部加入，由于相位改变，结果又可以回到约：

```math
10.1{\rm MN}.
```

这说明：

```math
\boxed{ qU\text{ 的量级确实不可忽略，} }
```

但也证明：

```math
\boxed{ \text{没有真实 registration 时，其符号和合量不能唯一确定。} }
```

所以我不会拿其中某一个漂亮数字称作“新理论结果”。

---

# 13. 我也把完整 connected branch 往前跑了，而不是只算 FEM 那一个点

采用：

```math
\text{compatible Airy} + \text{AC-UHPC V0} + \text{qU-off Multiwave}
```

最低谱阶，得到：

| `qP` / MN最小 UHPC 等效压应变 |        |               |
| ---------------------- | ------ | ------------- |
| 0.00287                | 8.122  | −0.001228     |
| 0.00500                | 10.070 | −0.001677     |
| 0.01000                | 12.059 | −0.002467     |
| 0.01200                | 12.692 | −0.002755     |
| 0.01400                | 13.303 | −0.003032     |
| 0.01600                | 13.805 | −0.003293     |
| 0.01700                | 14.001 | −0.003413     |
| 0.01800                | 14.191 | **−0.003527** |

因此当前 source-locked 压缩域：

```math
\varepsilon^*\ge-0.0035
```

在大约：

```math
\boxed{q\approx0.0178}
```

附近先结束。

对应荷载约：

```math
\boxed{P\approx14.15{\rm MN}}
```

量级。

但是这**不能叫新** **`P_u`**，因为目前还没有峰后压缩本构，而我们也不能重新把材料边界偷偷定义成极限。

当前母式同样明确要求：材料定义域提前结束时，不能用该荷载冒充正式 structural Pu。

所以我没有伪造一个“新理论 Pu=14.15 MN”。

---

# 14. 但这一轮其实已经把真正的问题定位得相当窄

现在四个候选原因可以重新排序：

### 第一：R4 force-fitting curvature

```math
\boxed{\text{已确认错误，应删除。}}
```

审计直接证明 R4 曲率不是 `q` 的几何曲率。

### 第二：global Airy / global shape basis

目前：

```math
\boxed{\text{基本 PASS。}}
```

原因是：

- `q\rightarrow\kappa` 与 FEM BH050/BH100 很接近；
- 线弹性 limit 严格恢复旧 `K_x,G,C_A`；
- `N=1\rightarrow3` 对 BH050 结果影响不到约 0.2%。

### 第三：UHPC 非线性导致二维分区无法显式

目前：

```math
\boxed{\text{不是主要 blocker。}}
```

PWL/branch V0 可以正常跑，而且材料逼近误差只有几个百分点。

### 第四：Multiwave local steel

这里出现了一个非常微妙的结论：

```math
\boxed{ \textbf{steel force 本身反而已经基本正确。} }
```

BH050：

```math
4.150{\rm MN}
```

vs FEM：

```math
4.289{\rm MN}.
```

真正缺的是：

```math
\boxed{ \textbf{local steel postbuckling 的 generalized work 如何反馈完整 global Airy equilibrium。} }
```

---

# 15. 因此我现在会把新的核心方程改成这个，而不是继续“平均钢应力替换”

钢壳不能只提供：

```math
N_s(\varepsilon).
```

它必须同时从同一个 condensed local energy：

```math
\Pi_s(U;q,\mathbf e)
```

给：

```math
\boxed{ N_{s,ij} = \frac{\partial\Pi_s} {\partial e_{ij}} }
```

以及：

```math
\boxed{ R_q^s = \frac{\partial\Pi_s}{\partial q}. }
```

这两者必须同源。

当前问题就在于我们实际上做了：

```math
\boxed{ \text{R02/R06} \rightarrow \bar\sigma_s }
```

然后把这个 reduced stress 塞回 global equilibrium，

但没有同时完整加入：

```math
\boxed{ \frac{\partial\Pi_s}{\partial q} }
```

中的：

```math
qU,\quad d\Delta,\quad\Delta^2
```

全部 generalized work。

这会自然造成刚才看到的现象：

> steel force 降对了，但 global equilibrium 不知道这些 local deformation 到底做了多少功，于是错误地降低 global membrane compression，连 UHPC 一起卸载。

这个解释和本轮数值结果是完全一致的。

---

# 16. 所以现在距离真正“跑通”其实只剩一个非常明确的工程选择

不是再研究一个新材料，也不是增加第 4、第 11 个 global shape function。

而是必须解决 Multiwave registration。

有两条理论上合法的办法：

```math
\boxed{\text{A. 保留真实 cell registration}}
```

即每个 strip 输入：

```math
(n_i,\omega_i,L_{xi},A_{0i},x_{0i},y_{0i},s_{fi}).
```

然后 exact qU compiler 已经可以直接算。

或者更漂亮：

```math
\boxed{\text{B. 推导 phase-averaged / homogenized GL operator}}
```

把：

```math
x_0,y_0
```

解析积分掉：

```math
\overline{\Pi}^{GL} = \frac1{L_G^2} \int \Pi^{GL}(x_0,y_0)\,dx_0dy_0.
```

那么最后 Multiwave 输入仍然只需要：

```math
n,\omega,L_x,A_0
```

而不需要 case-specific phase。

**我现在明显更倾向 B。**

因为这才符合你一直要求的：

```math
\boxed{ \text{没有 specimen-specific recipe} }
```

而且我们现在已经有 finite-harmonic compiler，所以 phase average 本身仍然有希望完全解析化。

---

## 这次执行后的最终裁决

```math
\boxed{ \textbf{COMPATIBLE AIRY GLOBAL BACKBONE = PASS} }
```

```math
\boxed{ \textbf{GLOBAL BASIS N=1\rightarrow3 SENSITIVITY = NEGLIGIBLE FOR BH050} }
```

```math
\boxed{ \textbf{AC-UHPC PWL V0 = RUNNABLE} }
```

```math
\boxed{ \textbf{MULTIWAVE STEEL FORCE MAGNITUDE = SURPRISINGLY GOOD} }
```

BH050 同几何状态：

```math
P_s^{MW}=4.150 \quad\text{vs}\quad P_s^{FEM}=4.289{\rm MN}.
```

但：

```math
\boxed{ \textbf{MULTIWAVE LOCAL}\rightarrow \textbf{GLOBAL GENERALIZED-WORK CLOSURE = FAIL/INCOMPLETE} }
```

这才造成：

```math
P^{MW}=10.16{\rm MN}
```

而不是 FEM：

```math
12.57{\rm MN}.
```

同时：

```math
\boxed{ \textbf{EXACT qU HARMONIC COMPILER = PASS} }
```

因为它已经把现有 `K_A` 回归到 `10^{-21}` 左右的误差。

所以这次没有再停在“Airy 到底行不行”“是不是需要更多形函数”“UHPC 能不能显式”这些模糊问题上。

**现在唯一最值得下刀的位置已经非常具体：**

```math
\boxed{ \textbf{把 Multiwave R02 从“mean-stress reduction operator” 升级成“same-energy local condensed operator”，} }
```

使：

```math
\boxed{ (N_s,M_s,R_q^s) = \text{同一个 }\Pi_s(U,q,\mathbf e) \text{ 的共轭导数}. }
```

我认为这是目前第一次把新理论真正跑起来以后，定位到的**最实质性缺口**。