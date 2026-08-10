# N模块分支C：来源Newton全局化与首个自然路径审计 R18

> Archive identity: complete text recovered from File Library `file_000000009a508207acadd05eca0beffa`. Historical N-module Branch-C audit; not a current zero-spatial production theory.

## 1. 本阶段边界

本阶段仅处理 **N–Y系统中N模块Nguyen完整分支C** 的数值求解组织：

- N模块：启用；
- Y模块：关闭；
- 分支P、分支A：仅保留既有退化回归测试；
- Nguyen第3章材料关系：未修改；
- Nguyen第4章Q4面内离散、四节点16自由度Kirchhoff板单元及离散钢筋梁：未修改；
- Nguyen第6章完整分层耦合残量：未修改；
- Swartz结构试件计算：未启动；
- 试验结果反标定：未进行。

R18只解决R17暴露的全局数值问题：Nguyen来源切线Newton在CC状态下可能出现“所有回溯步均不能降低残量”的情况。允许的处理范围仅为对原来源Newton迭代进行数值全局化，不改变任何物理方程。

## 2. 原方程与程序变量

完整分支C仍求解Nguyen式（6.36）对应的全局平衡方程：

\[
\mathbf R(\mathbf q,\lambda)=\mathbf 0,
\]

来源切线Newton修正保持为：

\[
\Delta\mathbf q_N=-\mathbf K_s^{-1}\mathbf R,
\]

其中：

- \(\mathbf R\)：第6章完整分层耦合残量；
- \(\mathbf K_s\)：由Nguyen第3章来源材料切线，经分层、单元和全局装配形成的来源结构切线；
- \(\mathbf q\)：Q4面内自由度与Nguyen 16自由度面外板自由度形成的全局向量；
- \(\lambda\)：荷载因子。

R18没有以中心差分、其他本构切线或试验拟合切线替换 \(\mathbf K_s\)。

## 3. R18数值全局化

### 3.1 问题定位

R17的CC固定荷载审计在第2次Newton校正后达到：

\[
\|\mathbf R_f\|=1.0225095075,
\]

但沿来源Newton方向从 \(\alpha=1\) 缩小到既定最小步长，残量均不能继续降低，因此原程序返回线搜索失败。

该失败不是材料点不收敛，也不是第3章公式缺失；材料状态始终为CC，失败位置是全局来源Newton方向的数值全局化。

### 3.2 允许范围内的处理

R18保留每一步来源Newton修正：

\[
\mathbf f_k=\Delta\mathbf q_{N,k}=-\mathbf K_{s,k}^{-1}\mathbf R_k.
\]

在已有来源Newton历史上构造有限深度多割线组合：

\[
\mathbf q_{A,k+1}
=
\mathbf q_k+\mathbf f_k
-
\left(\Delta\mathbf Q+\Delta\mathbf F\right)\boldsymbol\gamma,
\]

其中 \(\boldsymbol\gamma\) 仅由历次 \(\mathbf q_k\) 和来源Newton修正 \(\mathbf f_k\) 求得。该候选点仍以原始完整残量重新评价；只有残量降低时才接受。

因此该算法的身份是：

> **Nguyen来源Newton映射的数值全局化**，不是新Jacobian、不是新材料模型，也不是新理论分支。

程序实现：

- `n_branch_c.solver._source_newton_anderson_candidate`
- `n_branch_c.solver.solve_fixed_load`

所有候选点仍从同一个已提交材料状态计算；拒绝候选不会提交材料历史。

## 4. 材料来源未变证明

R17与R18的 `n_branch_c/materials.py` SHA-256完全一致：

```text
3a8dffd6eeff11f25945af7674fe36fc1432a43cc491d4c6a5ff6fe6f713f97f
```

R18唯一核心代码变化位于全局求解器 `solver.py`，详见：

- `audit/solver_R17_to_R18.diff`
- `audit/materials_hash_comparison_R18.txt`

## 5. CC来源Newton全局化审计

使用R17同一CC平衡问题、同一材料状态、同一来源切线和同一起点：

| 项目 | 关闭R18全局化 | 启用R18全局化 |
|---|---:|---:|
| 是否收敛 | 否 | 是 |
| 结束原因 | 线搜索与全局化均关闭/失败 | CONVERGED |
| 迭代记录数 | 3 | 7 |
| 最终自由残量 | 1.0225095075 | \(2.40615\times10^{-7}\) |
| 相对已知平衡解误差 | \(4.30473\times10^{-4}\) | \(3.70102\times10^{-11}\) |
| 材料状态 | CC | CC |

启用后的残量序列为：

\[
1800.0709
\rightarrow3.76921
\rightarrow1.02251
\rightarrow0.183141
\rightarrow0.00363392
\rightarrow2.94615\times10^{-5}
\rightarrow2.40615\times10^{-7}.
\]

结论：

\[
\boxed{\text{CC来源Newton全局化：PASS}}
\]

## 6. 首个自然全局状态路径审计

为避免再次用“预置状态附近Newton”冒充自然路径能力，R18另外建立了一个非Swartz、无试验标定的2×2混凝土板网格：

- 材料从零状态开始；
- Q4面内离散、ConcreteLayer、单元积分和全局装配均实际调用；
- 面外自由度仅在本膜状态审计中约束为零；
- 边界位移按比例加载；
- 材料状态由程序自然从U进入TT；
- 未直接预置TT状态。

名义八等分路径在 \(t=0.75\rightarrow0.875\) 之间需要一次确定性缩步，因此加入：

\[
t=0.8125.
\]

最终接受序列：

```text
0.125, 0.25, 0.375, 0.5,
0.625, 0.75, 0.8125, 0.875, 0.9375, 1.0
```

状态演化：

- \(t\le0.5\)：U；
- \(t\ge0.625\)：TT；
- 全部10个全局平衡点收敛；
- 最终自由残量：\(2.93880\times10^{-9}\)。

这证明了：

\[
\text{材料点}
\rightarrow\text{厚度层}
\rightarrow\text{单元}
\rightarrow\text{全局残量/来源切线}
\rightarrow\text{来源Newton全局化}
\]

能够在至少一条从零状态自然发生的 \(U\rightarrow TT\) 路径上闭合。

结论：

\[
\boxed{\text{自然全局 }U\rightarrow TT\text{ 路径：PASS}}
\]

该结果不能外推为其余状态路径或完整Swartz计算能力。

## 7. 自动测试与回归

```text
71 tests collected
71 passed
compileall PASS
```

完整回归继续覆盖：

- Nguyen分象限局部材料；
- 来源状态交接；
- Q4与Hermite16；
- 分层积分；
- 完整残量及结构切线；
- 离散钢筋；
- 全局装配；
- Newton事务；
- 恒弧长基础算法；
- 分支P/A退化；
- Swartz输入门禁。

R18新增测试：

- `test_source_newton_anderson_globalizes_cc_without_material_change`
- `test_natural_u_to_tt_global_path_converges_with_source_step_cutback`

## 8. 当前门禁

通过：

\[
\boxed{\text{Nguyen局部材料门禁：PASS}}
\]

\[
\boxed{\text{来源状态交接门禁：PASS\_SOURCE\_EXACT}}
\]

\[
\boxed{\text{CC来源Newton全局化：PASS}}
\]

\[
\boxed{\text{自然全局 }U\rightarrow TT\text{：PASS}}
\]

仍未完成：

- 自然全局 \(U\rightarrow TC\)；
- 自然全局 \(U\rightarrow CC\)；
- 自然全局 \(TC\rightarrow TCX\)；
- 真实Nguyen材料跨来源状态的恒弧长路径；
- 上述全部完成后的完整全局门禁复核。

因此当前只能判定：

\[
\boxed{\text{GLOBAL NESTED GATE：PARTIAL PASS}}
\]

\[
\boxed{\text{READY FOR SWARTZ 24-PANEL CALCULATION：NO}}
\]

本轮没有计算任何Swartz试件，也没有生成任何单板、部分板或承载力结果。

## 9. 下一唯一任务

保持R18材料文件、单元、残量和临时Swartz输入全部冻结，只继续完成：

\[
U\rightarrow TC
\rightarrow
U\rightarrow CC
\rightarrow
TC\rightarrow TCX
\rightarrow
\text{真实材料恒弧长嵌套审计}.
\]

只有这些自然全局路径、事务回滚、路径步接受/拒绝、极限点和峰后平衡点全部通过后，才允许重新判定完整求解器门禁。不得在此之前计算任何Swartz板。
