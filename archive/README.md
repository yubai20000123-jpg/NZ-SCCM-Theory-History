# ARCHIVE — POINTER ONLY / DEFAULT DO NOT LOAD

为避免 GitHub 搜索把迁移期全文、旧 checkpoint 和 R2 快照混入正常理论检索，**大体积迁移资产已从当前 `main` 删除**。

它们没有丢失，仍存在于 Git 历史中。恢复入口见：

- `PRE_CLEAN_POINTER.md`

主要历史恢复基点：

- `5c83f82da95d42efa33cbf2192c95545ab009017` — 清理前、临时重构标记之前的完整迁移期工作树；
- `41fc94aea846f05ed98d7099703ec49c9356cf9e` — 原子重构前的 staging tree。

如确需找回旧全文镜像、迁移 checkpoint、R2 snapshot 或 migration metadata，应从上述 commit 定点读取/恢复，**不要把整套旧目录重新并回当前工作树**。

正常理论工作不读取 `archive/`。
