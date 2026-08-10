# NZ-SCCM Case21 nested moment-first D15 可复现性闭合 R1 报告

**日期：2026-08-09**  
**性质：执行/证据链修复，不改变 NC 物理、本构目标、钢筋物理、Nguyen 二阶运动学、D15 精确矩或零空间数值积分原则。**

## 1. 为什么建立 R1

原 `NZ_SCCM_NESTED_D15_CASE21_REGRESSION_20260809` 包报告 `Pu=342.10774 kN`，但其冻结 `final_case21_out.txt` 无法由包内同时交付的源码、材料系数和 fixed mask 在 README 声明的状态下复现。旧包还存在：

- 运行路径硬编码；
- formal 默认参数并非 N=60 fixed；
- N=40 可静默使用 N=60 mask；
- 没有完整 `D,q -> concrete -> reinforcement -> total Rq -> limit` driver。

R1 只修这些执行/可复现性问题。

## 2. 保留不变的理论对象

- 一个连续完整代表半波；
- active mode `m=1`；
- Nguyen 二阶运动学；
- NC current operator 的现有系数文件 `ug/Cg/Tg`；
- nested moment-first D15；
- formal spatial quadrature = 0；
- Case21 fixed support mask 本身未重建；
- 钢筋不是峰后标量追加，而是同时进入 `P` 和 `Rq`，重新求总平衡极限状态。

## 3. Case21 输入与钢筋解析项

Case21：

- `b=ell=1220 mm`；
- `t=19.30 mm`；
- `A0=b/400=3.05 mm`；
- `fc=21.23 MPa`；
- `E0=20321 MPa`；
- `eps0=0.00209`；
- `nu=0.18`；
- 总配筋率 `p=0.75%`，单层，两个正交方向平分，所以 `rho_x=rho_y=0.00375`；
- `Es=200000 MPa, fy=530 MPa`。当前极限附近钢筋保持弹性。

令

`S=q0*q+q^2/2`, `Cm=pi^2*S/eps0`, `q0=1/400`。

加载方向钢筋轴力解析贡献：

`Ps = rho_y*t*b*Es*eps0*(D-Cm/4)/1000`  [kN]。

钢筋幅值残量物理贡献：

`Rq_s_phys = rho_y*t*Es*pi^2*(q0+q)*b*ell*(eps0*D*(nu-1)/4 + 9*pi^2*S/32)`。

与 concrete evaluator 使用相同无量纲残量口径：

`Rs = Rq_s_phys / [fc*eps0*b*ell*t/(2*pi^2)]`。

总体系：

`P=Pc+Ps`, `R=Rc+Rs=0`。

## 4. R1 修复内容

### 4.1 portable state generator

`core/gen_state_portable.py` 仅使用包内相对路径输出当前 D,q 的 D15 状态场文件。

### 4.2 strict evaluator

`core/eval_stepmask_strict.cpp`：

- formal 默认 `N=60, TOL=1e-6, fixed`；
- fixed mask 运行后必须 `PRUNE_CALL == SMASK.size()`；
- 不满足时返回非零退出码 92。

负向测试：把 N=60 mask 强行用于 N=40，得到：

`fixed_calls=1351/2021`

`MASK_CALL_COUNT_MISMATCH`

return code = 92。

因此旧包“错误 N 也静默成功”的漏洞已封闭。

### 4.3 mask identity metadata

`core/mask_metadata.json` 固定：

- N=60；
- TOL=1e-6；
- reference D=0.71；
- reference q=0.00220821；
- expected mask calls=2021；
- mask 与 ug/Cg/Tg 的 SHA-256。

`run_case21_regression.py` 在计算前先校验这些身份。

### 4.4 end-to-end driver

唯一入口：

```bash
python run_case21_regression.py
```

执行链：

`D,q -> gen_state -> nested D15 concrete Pc,Rc -> analytic steel Ps,Rs -> total R=0 -> P(D) -> smooth local maximum`。

## 5. 重新生成的总平衡分支

R1 不使用旧 peak CSV 的 q 作为最终平衡点，而是在每一个 D 上重新求 `Rc+Rs=0`。

| D | q (重新求根) | Pc/kN | Ps/kN | P/kN | total R |
|---:|---:|---:|---:|---:|---:|
| 0.70750 | 0.00219648348 | 316.56997164 | 25.76828234 | 342.33825398 | -4.24e-9 |
| 0.70775 | 0.00219727625 | 316.56098687 | 25.77734718 | 342.33833405 | -3.48e-9 |
| 0.70800 | 0.00219806937 | 316.55194029 | 25.78641193 | 342.33835221 | -1.75e-9 |
| 0.70850 | 0.00219965664 | 316.53366195 | 25.80454112 | 342.33820307 | +4.49e-9 |

形成真实峰值夹逼。

## 6. R1 当前极限点

对上述总平衡分支作局部二次极值定位，并在得到的 D 上再次闭合总 `R=0`：

- `D_u = 0.7079484366`；
- `q_u = 0.002197905755`；
- `A_u = q_u*b = 2.681445 mm`；
- `A0+A_u = 5.731445 mm`；
- `eps_bar = D_u*eps0 = 0.00147961223`；
- `Pc = 316.55381122 kN`；
- `Ps = 25.78454230 kN`；
- `Pu = 342.33835352 kN`；
- `Rc = +4.35277469298`；
- `Rs = -4.35277469306`；
- `R_total = -7.88e-11`。

相对 Case21 试验 `Pf=368.31275 kN`：

`(Pu/Pf-1)*100 = -7.05227%`。

## 7. 对旧 342.10774 kN 的裁决

R1 重新计算值与旧冻结值差：

- `+0.230614 kN`；
- 相对旧值 `+0.06741%`。

旧 `342.10774 kN` 继续保留在 `legacy_snapshot/` 中作为历史证据，但**不再作为当前 shipped source/coefficient/mask 组合的可执行回归目标**。

这不是修改材料或调参得到的新值，而是把同一 shipped backend 与钢筋贡献真正放回总残量 `Rc+Rs=0` 上重新求根得到的 provenance correction。

## 8. 与独立空间数值积分 audit 的关系

原包 README 报告的独立高阶空间 quadrature audit 值约为 `342.32988 kN`。R1 formal nested-D15：

`342.33835352 - 342.32988 = +0.008474 kN`

相对 audit 约 `+0.00248%`。

这是一项很强的数值一致性信号，但 quadrature 仍仅用于 audit，不进入 formal operator。

## 9. R1 能宣布什么，不能宣布什么

### 已闭合

- Case21 shipped nested backend 的 portable 执行；
- fixed-mask call-count fail-fast；
- mask N/TOL/关键文件 hash 身份检查；
- concrete + reinforcement 总残量重新求根；
- Case21 局部 smooth limit 的端到端一键重算；
- 旧 342.10774 的 provenance 冲突已被显式隔离而非静默覆盖。

### 仍未闭合

R1 **不授权 Swartz24 production**，原因仍包括：

1. 当前 mask 仍是 Case21-local，并不是 24 板共同 state-independent support policy；
2. Case21 TT 目前仍依赖局部上界证书，不能直接推广到 24 板；
3. N 阶数对总 stress + consistent tangent + Rq/L 的正式收敛门禁尚未完成；
4. 当前 R1 只闭合 Case21 局部回归，不等于 NC-MSAC-v1 的 24 板共同 compiler domain 已冻结。

因此下一唯一任务仍应是：

**建立 Swartz24 共用、state-independent 的 support policy / compiler domain，并先用同一个共用 policy 回归 Case21，通过后再统一批算 24 板。**

## 10. 状态标签

```text
ARTIFACT_STAGE = CASE21_NESTED_D15_REPRODUCIBILITY_CLOSURE_R1
THEORY_ROUTE = RETAINED
NC_PHYSICS_CHANGED = NO
REINFORCEMENT_PHYSICS_CHANGED = NO
FORMAL_SPATIAL_QUADRATURE = 0
FIXED_MASK_IDENTITY_GATE = PASS_R1
N40_WITH_N60_MASK_NEGATIVE_TEST = PASS_REJECTED
TOTAL_RQ_ROOT = PASS
CASE21_REGENERATED_PU_KN = 342.33835352
LEGACY_342.10774 = DEPRECATED_AS_EXECUTABLE_TARGET / RETAINED_AS_HISTORY
SWARTZ24_PRODUCTION = NOT_AUTHORIZED
```
