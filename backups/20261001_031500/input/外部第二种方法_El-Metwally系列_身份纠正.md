# 外部“第二种”方法身份纠正

时间：2026-10-01 02:48 +08:00

## 纠正
用户所称“第二种”不是当前 UCFT/M8 理论的第二个变体，也不是 current single-q/C1/steel-local 体系。

这里的“第二种”是已有学者提出的外部 nonlinear equilibrium-path method：
- Salah E. El-Metwally, A.M. El-Shahhat, W.F. Chen, "3-D nonlinear analysis of R/C slender columns", Computers & Structures 37(5), 1990, 863-872.
- Salah E. El-Metwally, F. Ashour, W.F. Chen, "Instability Analysis of Eccentrically Loaded Concrete Walls", Journal of Structural Engineering, ASCE 116(10), 1990, 2862-2880.

其共同特征：
1. 同时考虑材料非线性和几何非线性；
2. 以指定挠度/增量挠度作为路径控制量，反求对应荷载；
3. 逐步迭代得到完整 load-deflection equilibrium path；
4. 可以越过最大荷载点继续得到 post-peak / descending branch；
5. wall paper 明确采用 Newmark method + equivalent-column concept，并明确声称可得到 ascending and descending branches；
6. column paper 明确称 incremental deflection approach 可跟踪 complete load-deflection curve including post-peak softening branch。

这套方法是外部既有理论，与当前 UCFT 理论无关。后续若用户要求“完整输出第二种公式体系”，必须以这套 El-Metwally 系列方法及其原始/后续复现文献为对象，不得再把 UCFT 的 q,A+,A-,C1,M4,M5,M6 方程混入。

## 当前文献证据
- ASCE 1990 wall paper abstract: wall treated as beam-column; material models with tension/compression difference can be implemented; ascending and descending load-deflection branches predicted; method based on Newmark method combined with equivalent-column concept.
- Computers & Structures 1990 column paper abstract: both material and geometric nonlinearities included; incremental deflection approach calculates the load corresponding to a specified deflection; complete load-deflection curve including post-peak softening branch can be traced.
- 2013 Engineering Structures follow-up uses finite difference method to calculate load corresponding to a specified deflection while considering material and geometric nonlinearities, and computes complete load-deflection curves.

## NEXT_ACTION
暂停 UCFT 计算。若继续，只对 El-Metwally 外部既有方法做文献级公式恢复：优先恢复原始 1990 两篇论文的 governing equations / section M-N-phi relation / Newmark or finite-difference recursion / specified-deflection load solve / peak-crossing and descending-branch continuation，不嫁接当前 UCFT 公式。
