# FINAL ATTEMPT / NEW OPERATOR 分岔 R2

## 现路线最后一次 hard gates

G1:
sampling=0, quadrature=0, spatial subdomains=1.

G2:
内部 global order convergence，不借历史 338/342 或 audit target 选阶。

G3:
audit 只在正式结果形成后使用。

G4:
engineering analytic error 显著小于当前材料/结构模型误差。
theorem-level tight interval certificate 不再是独立 hard gate。

G5:
同一 evaluator 完成 concrete + reinforcement 的 P/R/root，
钢筋必须进入 residual 后重新求极限。

G6:
不存在会实质改变 Pu 身份的 unresolved blocker：
- Rq/root 大幅随阶次漂移；
- 必须用 audit 选阶；
- 必须 spatial split；
- provenance 无法闭合；
- 必须用结构 Pu 反标材料。

若 G1—G6 PASS：
CURRENT_OPERATOR_SINGLE_DOMAIN_ROUTE = PASS

若任一关键 gate FAIL：
CURRENT_OPERATOR_SINGLE_DOMAIN_ROUTE = TERMINATED_FOR_PRODUCTION

立即进入：
NEW MATERIAL / NEW TARGET FUNCTION / NEW SOLUTION OPERATOR

禁止继续追加“再一个 tail / 再一个 R0x”无限修补。
