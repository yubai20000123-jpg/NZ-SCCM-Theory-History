# NZ-SCCM v0.5.1 D19R-M1 回退执行报告

## 1. 执行目的

本轮只执行回退和证据固化，不修补承载力结果，不增加材料信息，不运行24板生产。

冻结基线为：

\[
\boxed{
\text{D19精确状态前沿}
+\text{D19R在v0.6.3修改前的原始材料边界}
+m=1
}
\]

## 2. 实际执行内容

### 2.1 原D19R代码身份核验

将回退包的 `src/` 和 `tests/` 与原始D19R v0.5逐文件计算SHA-256。共核验9个文件，9/9完全相同。回退没有重写普通混凝土或UHPC材料代码。

### 2.2 排除后续临时修改

活动代码中未发现：

- Chebyshev板级代理；
- pseudo-arclength/arc-length；
- v0.6.3 Source-U、Darwin–Pecknold、双割线迭代等普通混凝土专有新增实现。

### 2.3 回归测试

```text
D19 tests: PASS
178 topology intervals
45 analytic root derivatives
80 Liu tangent checks
1 full front-moment derivative

D19R tests: PASS
12 material tangents
2 full matrix Jacobians
6 UHPC path states
```

这些测试只说明原D19与D19R代码恢复一致，并不等同于材料理论最终获准。

### 2.4 m=1纯几何手算

采用

\[
\phi=\sin\frac{\pi x}{b}\sin\frac{\pi y}{\ell}
\]

逐项手算面积矩和厚度矩，再用12点Gauss作独立核验。最大非零相对差为：

\[
2.894\times10^{-12}.
\]

该核验没有调用或改变普通混凝土/UHPC材料关系。

## 3. 本轮没有执行的内容

- 没有计算Pcr或Pu；
- 没有计算24块板；
- 没有使用Case 21作材料反标定；
- 没有增加普通混凝土或UHPC专有机制；
- 没有启用Chebyshev、伪弧长或其他新求解器；
- 没有恢复m>1。

## 4. 历史恢复结论

最近的演化并不是从D19直接跳到D19C，而是：

\[
\text{DRS直接扫描}
\rightarrow
\text{D11有限解析能量矩}
\rightarrow
\text{D12材料候选否决}
\rightarrow
\text{D13连续势}
\rightarrow
\text{D14离线凝结}
\rightarrow
\text{D15精确矩}
\rightarrow
\text{D16可积性审计}
\rightarrow
\text{D17厚度前沿}
\rightarrow
\text{D18面内代数前沿}
\rightarrow
\text{D19精确拓扑事件}.
\]

用户反对“离散化”之后，真正形成的解析矩思想是：保留连续完整半波运动学，用理论三角矩、厚度矩和解析状态前沿替代空间材料点离散；不是用板级拟合面替代原方程。D19C Chebyshev路线因此不应被视为D19解析矩的自然完成。

完整版本历史见 `history/MODEL_CHANGE_HISTORY_RECOVERED_20260805.md`。

## 5. 当前裁决

```text
ROLLBACK_BASELINE                         = FROZEN
D19_EXACT_STATE_FRONT                     = RETAINED_PASS
D19R_PRE_V063_SOURCE_IDENTITY             = PASS_9_OF_9
FIXED_M1                                  = PASS
PURE_GEOMETRIC_HAND_CALC                  = PASS
CHEBYSHEV_FORMAL_IDENTITY                 = WITHDRAWN
V063_CONCRETE_SOURCE_U_FORMAL_IDENTITY    = WITHDRAWN
PSEUDO_ARCLENGTH                          = DISABLED
SWARTZ24                                  = PAUSED
NEW_PCR_PU                                = NOT_CALCULATED
```

下一轮应在这个未增项基线上共同判断问题，不再先改模型后看结果。
