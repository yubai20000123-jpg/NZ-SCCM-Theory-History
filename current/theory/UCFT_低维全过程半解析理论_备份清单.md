# UCFT 低维全过程半解析理论 — 备份清单

## 2026-09-30 13:31 +08:00 — 输入原件

- original filename: 指示词.md
- source: conversation upload
- source file id: file_00000000d820820791b2147579ba0920
- SHA256: 224e46926dceb3d308581b8e34290df90949688fbfd6f5d20afadd82c889d524
- persistent backup: Library
- backup path: /UCFT_lowdim/backups/20260930_133100/input/指示词.md
- backup library file id: libfile_0d60eed2a63c8191a14b53e717ced036
- description: 最高层路线合同原始上传文件，保持原始文件名不变。

## 2026-09-30 13:31 +08:00 — 首次生成 stable files

1. UCFT_nonlinear_membrane_condensation_当前推导.md
   - stable path: current/theory/UCFT_nonlinear_membrane_condensation_当前推导.md
   - first commit: 4067bc45a4356e84912b9004cf2c6d5a9e4d8cad

2. UCFT_低维全过程半解析理论_当前状态.md
   - stable path: current/theory/UCFT_低维全过程半解析理论_当前状态.md
   - first commit: 622a96e9941128d5fc9a1b9a74efb7277387a438

3. UCFT_低维全过程半解析理论_执行日志.md
   - stable path: current/theory/UCFT_低维全过程半解析理论_执行日志.md
   - first commit: 9aca781689528c5baeb8f67ad03001c6658938a6

4. UCFT_低维全过程半解析理论_备份清单.md
   - stable path: current/theory/UCFT_低维全过程半解析理论_备份清单.md
   - first commit: b0d088fce7cf40627f3232444673e268a8f44c67

首次 timestamp output backups：

- history/UCFT/backups/20260930_133100/output/UCFT_nonlinear_membrane_condensation_当前推导.md
  - commit: 7627d8ffb23ffd59a83742af546dd932ce66457f

- history/UCFT/backups/20260930_133100/output/UCFT_低维全过程半解析理论_当前状态.md
  - commit: 0edd4a89b252726966420ad72bed27f2942da55c

- history/UCFT/backups/20260930_133100/output/UCFT_低维全过程半解析理论_执行日志.md
  - commit: 4b7c7ca5cf5fd25f49295f34d76fd85d58ad241a

- history/UCFT/backups/20260930_133100/output/UCFT_低维全过程半解析理论_备份清单.md
  - commit: 21d37f755786b8cbc6babfbc375625df557dde7e

## 2026-09-30 14:06 +08:00 — LaTeX repair + M2 progress

首次 JavaScript template string 写入导致部分 LaTeX 反斜杠被解释为 control escape。首次文件和 timestamp backup 保留作为历史证据，不覆盖。

stable files 已使用 raw string 修复：

- UCFT_nonlinear_membrane_condensation_当前推导.md
  - repair + M2 commit: 65435280fa12ef03230d65ce3558fa525c450a7a

- UCFT_低维全过程半解析理论_当前状态.md
  - repair + M2 state commit: 6b6a66df84f3b87a39814a07b1449c453fd92f5b

- UCFT_低维全过程半解析理论_执行日志.md
  - repair + M2 log commit: f8ba59c327d08682fedbdb26d77e5238f0f24748

M2 当前新增内容：

- 解析证明 nonlinear UHPC 一般会产生 C1 mixed harmonic；
- BH060、BH100 做 independent numerical verification；
- 正式 Gate 2 保持 PENDING，等待 semi-analytic active-set area kernel 替换临时面内 Gauss verification。

## 备份策略

- 用户上传原件优先 exact-byte persistent Library backup；
- 生成理论文本优先写 private GitHub repo：
  yubai20000123-jpg/NZ-SCCM-Theory-History；
- stable filename 不随版本改变；
- 版本由 Git commit + timestamp backup directory 区分；
- 不覆盖唯一原件；
- 第三方未授权论文不上传公开仓库；
- 后续含 LaTeX 的 GitHub text write 必须使用 raw string，避免反斜杠 escape。


## 2026-09-30 14:16:59 +08:00 — M2 formal semi-analytic kernel post-backup

Stable updates before backup:

- UCFT_nonlinear_membrane_condensation_当前推导.md
  - semi-analytic M2 commit: e592e710ce71fa34020285fbe56c73d752552a25

- UCFT_低维全过程半解析理论_当前状态.md
  - state commit: 0b6b5960e6284c540a1f58e067851edf203e56b2

- UCFT_低维全过程半解析理论_执行日志.md
  - log commit: 2157fc82fd210aeb9443eccb950d86e6fb341451

- UCFT_nonlinear_membrane_condensation_solver.py
  - first code commit: 427d6e88779d0bfa3925c2ed2ced98546b63bd65

Timestamp output backups:

- history/UCFT/backups/20260930_141659/output/UCFT_nonlinear_membrane_condensation_当前推导.md
  - commit: 1b7374c326b93192d471a1fc77de14680df91820

- history/UCFT/backups/20260930_141659/output/UCFT_低维全过程半解析理论_当前状态.md
  - commit: 8922918071c55c864036ab91ebec7f221ae400e5

- history/UCFT/backups/20260930_141659/output/UCFT_低维全过程半解析理论_执行日志.md
  - commit: 728b71b94a00d01887dd67bb6689ea099fccf375

- history/UCFT/backups/20260930_141659/output/UCFT_nonlinear_membrane_condensation_solver.py
  - commit: 5dc99249dd107055eab8ec2fc38c32d00cf0f41d

本次备份对应状态：

- M0 PASS；
- Gate 1 PASS；
- M2 semi-analytic active-set single-state kernel cross-check PASS；
- Gate 2 full path PENDING；
- NEXT：向量化唯一剩余的一维 X integration，并跑 BH060/BH100 continuous q-path。
