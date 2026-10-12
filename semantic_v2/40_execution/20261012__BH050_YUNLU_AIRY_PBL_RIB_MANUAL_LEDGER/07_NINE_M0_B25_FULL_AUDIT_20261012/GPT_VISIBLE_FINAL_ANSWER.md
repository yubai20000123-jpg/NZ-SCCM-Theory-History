# 九试件 M0 三层 Airy–Galerkin 计算与 GS_DIRECT 对比

已按统一模型完成九试件的 **\(0\le W\le B/25\)** 代数求根采样，并将各件已记录的 GS_DIRECT 整体荷载—新增整体面外挠度数据放在同一坐标中对比。理论采用上钢壳五等效子板、下钢壳六等效子板，固定轴向波数 \(m=4\)，UHPC 与钢材均为拉压同性线弹性，采用解析傅里叶积分而非板面离散求积。

**最重要的结论：九件都算到了规定的截止挠度，但其中不少大挠度数学根已不满足“钢壳只能向外鼓曲”的假定；BH005、BH010 还存在固定 \(W\) 求根中断，不能把跨越中断的代数根画成一条可靠的连续物理分支。** 因此下面区分数学结果、原点连通候选解和真实 FEM，绝不将 \(W=B/25\) 的荷载称为极限承载力。

## 1. 九试件计算与 FEM 峰值对比

| 试件 | 截止 \(B/25\) (mm) | FEM 峰值 (MN) | FEM 峰值对应 \(W\) (mm) | 同一 \(W\) 理论荷载 (MN) | 相对误差 | 理论在 \(B/25\) 的代数荷载 (MN) |
|---|---:|---:|---:|---:|---:|---:|
| BH005 | 10 | 2.324 | 0.043 | 7.089 | +205.10% | 94.700 |
| BH010 | 20 | 4.315 | 0.168 | 6.566 | +52.17% | 48.186 |
| BH020 | 40 | 7.850 | 1.293 | 9.972 | +27.03% | 29.432 |
| BH032 | 64 | 10.480 | 4.911 | 9.403 | −10.27% | 25.676 |
| BH050 | 100 | 11.630 | 15.240 | 7.528 | −35.28% | 27.614 |
| BH060 | 120 | 11.805 | 22.101 | 7.008 | −40.64% | 30.001 |
| BH070 | 140 | 11.858 | 39.794 | 8.146 | −31.30% | 32.840 |
| BH085 | 170 | 12.527 | 67.666 | 10.611 | −15.29% | 37.608 |
| BH100 | 200 | 13.486 | 87.323 | 12.257 | −9.11% | 42.704 |

相对误差按 \([P_{M0}(W_{FE\,peak})-P_{FE\,peak}]/P_{FE\,peak}\) 计算。最后一列**仅为代数根读数**，不是已验证的物理承载力，也不是极限荷载。

## 2. 九条理论—FEM 曲线

![九试件在 FEM 实际挠度范围内的理论—FEM 对比](sandbox:/mnt/data/UCFT_M0_NINE_B25_20261012/OVERVIEW_NINE_M0_vs_FEM_FEMrange.png)

![九试件延伸至规定 B/25 截止挠度的理论—FEM 对比](sandbox:/mnt/data/UCFT_M0_NINE_B25_20261012/OVERVIEW_NINE_M0_vs_FEM_B25.png)

每件另外提供两张独立高清图：一张限定在 FEM 实际记录的 \(W\) 范围，另一张显示完整 \(0\le W\le B/25\) 理论区间。**未对 FEM 曲线进行任何大挠度外推。** 数据源为原始 GS_DIRECT 九件按帧导出，采用加载端反力 `P_load_MN`，以及帧 0 修正、扣除端部弦线后的第二半波中线新增整体面外位移 `w_added_centerline_n2_mm`；并非轴向端缩。

曲线揭示两类不同偏差：窄板试件在 FEM 峰值所在小挠度区理论明显偏高；中等宽板在 FEM 峰值处反而偏低。随着 \(W\) 继续增大，线弹性 M0 又持续抬升，不能描述 FEM 的峰后下降。这不是通过调整 \(m\) 就可以直接宣布解决的材料非线性问题。

## 3. 数值分支与物理适用性

- **BH005：**有 23 个求根未通过残量门槛的采样点，首次在 \(W\approx0.417\) mm；BH010 有 4 个，首次在 \(W\approx0.833\) mm。这些位置在曲线中留空；其后的其他代数根**没有被证明与原始零荷载分支连续**。
- **BH032、BH050、BH060、BH070、BH085、BH100：**上钢壳的 \(A_{0+}+A_+\) 会在大挠度区变为负值。首次检测位置分别约为 45.87、50.83、54.00、56.00、60.92、65.00 mm。超出后只能看作忽略单侧接触约束的数学延拓。
- **BH020：**在本次采样区间内取得了残量合格、且总局部幅值方向仍为向外的候选根，但仍未完成实际肋线、局部接触和多根稳定性验证。

## 4. BH050、\(W=5\) mm：完整人工计算账本

将解析积分后的残量展开为关于 \(a=A_+\)、\(b=A_-\)、\(e=\varepsilon_y^0\) 的有限多项式。三条 Galerkin 方程分别有 **13、10、10 个非零单项式**，轴力恢复式有 **6 个单项式**。由整体方程 \(R_W=F_0(a,b)+F_1(a,b)e=0\) 精确消去 \(e=-F_0/F_1\)，再解两条局部方程。

首次平衡点独立复算为：

\[
\boxed{W=5.000000\ \mathrm{mm},\quad A_+=0.316462248204096\ \mathrm{mm},\quad A_-=0.503447015296702\ \mathrm{mm}}
\]
\[
\boxed{\varepsilon_y^0=-0.000582834754985961,\quad P_{M0}=4.841459700673342\ \mathrm{MN}}
\]

三层轴力：UHPC 为 **2.569528797207 MN**，上钢壳为 **0.930399817581 MN**，下钢壳为 **1.341531085886 MN**，相加为 **4.841459700674 MN**（尾数受浮点舍入影响）。全部三个广义残量绝对值处于约 \(10^{-10}\) N 以下。

完整复算包中逐项列出了：**3,616 行傅里叶解析积分原函数乘积、430 行 Airy／应力谐波、13＋10＋10＋6 个多项式系数、九轮 Newton 的每一项四则运算、351 行逐单项式乘积、891 行导数单项式、各轮 2×2 雅可比及行列式、三层平均应力与全部残量**。每一行都有原始符号/指数、数值因子、乘积及累计和；另附解析积分计算程序源码，可通过改变输入重新独立复算。无限精度常数 \(\pi\) 仍保留解析表示，数值仅给所保存的有效精度。

## 5. 下载和可追溯备份

**[下载全部九试件计算、九件 FEM 曲线、18 张单件图、两张总览图以及 BH050 完整人工复算账本](sandbox:/mnt/data/UCFT_NINE_M0_B25_FULL_EXACT_AUDIT_AND_FEM_20261012.zip)**

**[GitHub 完整压缩包备份](https://github.com/yubai20000123-jpg/NZ-SCCM-Theory-History/blob/research/20261012-bh050-rib-airy-manual-ledger/semantic_v2/40_execution/20261012__BH050_YUNLU_AIRY_PBL_RIB_MANUAL_LEDGER/07_NINE_M0_B25_FULL_AUDIT_20261012/UCFT_NINE_M0_B25_FULL_EXACT_AUDIT_AND_FEM_20261012.zip)** ｜ **[GitHub 可直接阅读的九试件报告](https://github.com/yubai20000123-jpg/NZ-SCCM-Theory-History/blob/research/20261012-bh050-rib-airy-manual-ledger/semantic_v2/40_execution/20261012__BH050_YUNLU_AIRY_PBL_RIB_MANUAL_LEDGER/07_NINE_M0_B25_FULL_AUDIT_20261012/README_九试件结果与复算状态.md)** ｜ **[GitHub 可直接阅读的 BH050 账本](https://github.com/yubai20000123-jpg/NZ-SCCM-Theory-History/blob/research/20261012-bh050-rib-airy-manual-ledger/semantic_v2/40_execution/20261012__BH050_YUNLU_AIRY_PBL_RIB_MANUAL_LEDGER/07_NINE_M0_B25_FULL_AUDIT_20261012/BH050_W5_00_complete_human_reproduction_readme.md)**

主要可单独查看的文件：

- [全部九件至 \(B/25\) 的每个理论状态](sandbox:/mnt/data/UCFT_M0_NINE_B25_20261012/01_NINE_M0_all_formula_roots_to_B25.csv)
- [九件全部实际 FEM 帧](sandbox:/mnt/data/UCFT_M0_NINE_B25_20261012/02_NINE_GS_DIRECT_source_frames.csv)
- [理论在每一个 FEM 记录点的逐帧对比](sandbox:/mnt/data/UCFT_M0_NINE_B25_20261012/03_NINE_M0_at_all_FEM_frames.csv)
- [九件误差与分支状态总表](sandbox:/mnt/data/UCFT_M0_NINE_B25_20261012/04_NINE_summary_peak_and_B25.csv)
- [BH050 所有积分与九轮 Newton 复算说明](sandbox:/mnt/data/UCFT_M0_NINE_B25_20261012/BH050_W5_00_complete_human_reproduction_readme.md)
- [本轮理论及模型适用性报告](sandbox:/mnt/data/UCFT_M0_NINE_B25_20261012/README_九试件结果与复算状态.md)

GitHub 备份采用之前的独立研究分支 `research/20261012-bh050-rib-airy-manual-ledger`，不覆盖 `main` 或 production。归档中的 `GPT_VISIBLE_FINAL_ANSWER.md` 保存了本次可见完整答复原文，`MANIFEST_SHA256.csv` 则为其余计算文件提供字节级校验。此处“输出过程”指可核查的显式公式、积分和求根记录，不包含不可导出的内部推理。

**结论：九试件的公式计算、FEM 对比和 BH050 完整算术账本已经完成；严格满足真实 PBL 及单侧接触条件的九试件稳定分支尚未完成。M0 的大挠度代数值不能作为实际极限承载力。**