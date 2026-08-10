# 原始共享对话 TURN 0001—0148：恢复定位器

## 1. 原件身份

```text
filename = chat_export_2026-08-05T20-29-31-447Z_part_01_turn_1-148.txt
ChatGPT File Library ID = file_00000000b7788209a161cd5ec2db852a
kind = original user-visible dialogue export
project-history authority = LEVEL 1
GitHub text copy = PENDING
```

配套 manifest：

```text
filename = chat_export_2026-08-05T20-29-31-447Z_manifest.txt
ChatGPT File Library ID = file_00000000d7b08209a6a93987565bd8c2
```

## 2. 为什么这个文件必须单独保留

它是 NZ-SCCM-U v0.2 一段关键历史中，用户可见共享页面 TURN 0001—0148 的连续正文基线。后期 R04/R05、D19R/D20 工件和 Conversation JSON 都不能代替它来证明“共享页面上到底交付了什么”。

## 3. 历史真值锁

已锁定：

```text
TURN 0001—0148 = 连续共享正文基线
TURN 0147 = 用户：“那就执行吧”
TURN 0148 = 任务启动/思考 + 连接中断
D20 formal assistant final = NOT DELIVERED ON SHARED PAGE
G31 final visible delivery = historically unresolved/absent in the recovered branch at its interruption point
```

因此，后续发现的：

```text
D20
D19R
D19C
v0.6.1
v0.6.3
G-series execution artifacts
```

只能证明相应后台/分支工件存在；在不能与原始消息树对应时，不得据此补写一个从未出现在共享页面的 assistant turn，也不得推定用户已经验收。

## 4. 恢复方式

新对话若需要恢复该阶段，应按以下顺序：

1. 在 ChatGPT File Library 搜精确文件名；
2. 打开 TURN 0001—0148 原始导出；
3. 再读取 `00_完整性复核与末24小时裁决_R04.md`；
4. 再读取 `NZ_SCCM_148回合思想演化与当前正式主线恢复_R05.md`；
5. 若需调查后台/分支，再读取 Conversation JSON active-main-branch audit；
6. 最后才使用 handoff/decision ledger 做索引。

## 5. GitHub 二进制/文本迁移说明

当前 GitHub connector 的文本写接口没有把 ChatGPT File Library 文件直接作为 file parameter 上传到仓库的动作。因此先保存精确 File Library locator 和证据身份。获得原始文本二进制/挂载副本后，应原样放入：

`history/raw/chat_export_2026-08-05T20-29-31-447Z_part_01_turn_1-148.txt`

不得用摘要重建该文件。
