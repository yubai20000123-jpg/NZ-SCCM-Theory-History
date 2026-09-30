# UCFT 低维全过程半解析理论 — 执行日志

## 2026-09-30 21:15+08:00 — M8 rational-Y production operator

1. 按 `指示词(9).md` 恢复项目，不重开路线。
2. 读取最新 `UCFT_M8_input_closure_and_solver_interface_audit.md`；确认 NEXT_ACTION 为 finite-trigonometric/rational active-Y operator。
3. 恢复 M4 baseline analytic-Y 公式与 M6 Schur interface。
4. 实现 generalized finite Fourier/Laurent active-set；材料边界通过 t=tan(Y/2) 的代数多项式求根定位。
5. 对 active interval 实现 1/sin(Y)、1/sin^2(Y) 的 exact finite-harmonic recurrence primitive；其与半角 rational integral 等价，但避免高次多项式条件恶化。
6. Baseline M4 regression：1.125e-16 / 2.706e-15 relative diff，PASS。
7. 高频 k=7,9,16 boundary locator：最大原方程 residual 2.277e-18，PASS。
8. 独立 active-set benchmark：最大 relative diff 6.585e-07，1e-6 gate PASS。Gauss/quad 仅 benchmark，不进入 production。
9. 裁决：M8_RATIONAL_Y_OPERATOR=PASS；M8_PATH_SOLVER 仍 PARTIAL。
10. 检查现有 M6 source：它明确不是 nine-specimen executable solver；因此本轮未伪造 BH005 mode/path 数值。

NEXT_ACTION：集成 production evaluator 后立即 BH005 perfect-local N,m -> restore A0 -> imperfect connected q-path。
