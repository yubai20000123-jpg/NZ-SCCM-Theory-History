# SOURCE REGISTRY — 原始资料登记表

本文件只登记“原件在哪里、是什么、扮演什么角色”。不把项目解释冒充原文。

## A. 当前运行环境中已有本地原件（可校验 SHA-256）

| source_id | 原始文件名 | 类别 | bytes | SHA-256 | 当前角色 | GitHub PDF binary |
|---|---|---:|---:|---|---|---|
| NC_NGUYEN_THESIS | `Nguyen-011325526.pdf` | NC/RC | 34860966 | `de4369d427540716e965bd9188ef0aaac77146eab3f054a433703f772e20111e` | 普通混凝土二维材料、钢筋、第4/6章稳定与路径来源 | PENDING |
| UHPC_ZHOU_TRIAXIAL | `UHPC三轴受压力学性能研究_周俊.pdf` | UHPC | 2076983 | `37531c8f73765fea9192bef094a88edd7d7eacc5756b51640a7353b65ed72e59` | 三轴受压、八面体/DP 强度约束 | PENDING |
| UHPC_WANG_TRIAXIAL | `超高性能混凝土三轴受压力学性能及破坏准则_王淑楠.pdf` | UHPC | 5145596 | `e6e24cf47b21b1faa09f13ceb97a599321283c154578da92ef844b5d8e5c27dd` | 三轴全过程、W-W 五参数破坏面 | PENDING |
| UHPC_HU_INTERFACE | `钢-预制UHPC开孔板组合桥面板界面抗剪性能研究_胡文旭.pdf` | UHPC/interface | 12741610 | `a554649f440bdb5d6523dc174aab68e1128aa6e4f9d19ebb9b67a9e19b544909` | UHPC 单轴压/拉本构早期来源、界面研究 | PENDING |
| SHELL_YUN | `考虑薄膜效应的钢箱混凝土壁板局部屈曲行为研究_云露.pdf` | shell/Y | 6109981 | `1fce0f9ce9058f00b2a6ddd0f6dd11faa41366816e2145348812c1a93884e897` | 大挠度、薄膜效应、局部屈后 | PENDING |
| PBL_ZHANG | `PBL加劲型矩形钢管混凝土轴压柱局部屈曲性能分析_张宁.pdf` | PBL/shell | 535182 | `7ae43da9f08d777e8b6a47acfff450ff22929dc7fcdad15fe95d29a5370572c5` | PBL 加劲局部稳定/能量法参考 | PENDING |
| PBL_SUN | `PBL加劲型薄壁钢管混凝土...塔的计算理论与设计方法研究_孙立鹏.pdf` | PBL/shell | 19805746 | `e441312bd0585536bbb7244e6cc2aaa37235fbe7a75f2c1e934f1a4e78981a6e` | R-O/Bleich、PBL加劲薄壁钢管理论历史来源 | PENDING |

> `PENDING` 只表示当前 GitHub 连接器尚未把 PDF 二进制原件复制进仓库；不表示原件缺失。文本检索镜像会放在 `sources_text/`。

## B. File Library 中已重新确认存在的 UHPC 原始 PDF

这些文件是用户先前实际上传过的原件，不得从历史中省略。

| source_id | 文件名 | ChatGPT File Library ID | 已核验内容/身份 | GitHub binary |
|---|---|---|---|---|
| UHPC_HIEW_2024_TENSION | `Hiew_2024_UHPC_unified_tension_2pct.pdf` | `file_0000000087e882079606fbbb13dd1e2d` | Cement and Concrete Composites 150 (2024) 105553；统一直接拉伸本构，elastic→hardening→peak→localization→fiber-pullout softening | PENDING / FILE_LIBRARY_ONLY |
| UHPC_LIU_2024_BIAXIAL | `Liu_2024_UHPC_biaxial_full.pdf` | `file_0000000012988211ab7b3fbcacf060ab` | UHPC 双轴强度/TC 等；文内引用 Liu 2023 softened TC law、Lee 2017 UHPFRC 等 | PENDING / FILE_LIBRARY_ONLY |
| UHPC_HU_INTERFACE_FL | `钢-预制UHPC开孔板组合桥面板界面抗剪性能研究_胡文旭.pdf` | `file_000000003824720ba4ffbb7e840dec6b` | 与本地原件同名；UHPC 本构/界面试验 | LOCAL_COPY_AVAILABLE |
| UHPC_ZHOU_FL | `UHPC三轴受压力学性能研究_周俊.pdf` | 项目已上传原件 | 三轴 DP/八面体关系 | LOCAL_COPY_AVAILABLE |
| UHPC_WANG_FL | `超高性能混凝土三轴受压力学性能及破坏准则_王淑楠.pdf` | 项目已上传原件 | 三轴全过程/W-W | LOCAL_COPY_AVAILABLE |

## C. UHPC 关键“原始研究工件/响应文件”也属于证据源

| artifact_id | 文件名 | File Library ID | 作用 |
|---|---|---|---|
| UHPC_G16R | `NZ_SCCM_G16R_signed_excess坐标_材料参数重审_U候选_D可识别性门禁.md` | `file_00000000d08481fb94ae56066ec12649` | 记录用户只强制 `fc=141.1 MPa`；Ec/eps0/ft/nu 重审；Hiew 2% 参数替换旧 ft=7.3；D 可识别性失败 |
| UHPC_STATE_LEDGER | `UHPC_STATE_EQUATION_LEDGER.csv` | `file_000000003ac081fab7f7d4ff33981d05` | 记录 U/TC/TT/CC/TCX/C3 各状态来源、缺口与当前保留用途 |
| UHPC_D19_LIU_TC | `D19_LIU_TC_CLOSURE_MATRIX.csv` | `file_000000004ba482079c419a867f98540d` | Liu 2023 TC 软化压缩支路的闭合/未闭合矩阵；明确 tensile/shear/history 尚缺 |
| D15_UHPC_REPORT | `NZ_SCCM_DAEM_v0.5_D15_精确矩生成与UHPC解析矩公式报告.md` | `file_00000000e17081f898276bf421de6f6a` | D15 精确矩与 UHPC L0/L1 历史阶段；生产未授权 |
| LOW_PARAM_LEDGER | `04_low_parameter_physical_target_ledger.csv` | `file_00000000c28c82099d640f2785e9fa41` | NC/UHPC 低参数物理目标；UHPC TC 明确要求独立识别 |

## D. 公开来源/二次获取的处理规则

如果某篇论文最初通过公开网络获取、而 File Library 中仍有原始 PDF：

1. 优先保存用户实际上传的 PDF SHA；
2. 同时在 evidence note 中登记 DOI/出版社/公开下载 URL（重新核验后填写）；
3. 不因找到新的网页副本而覆盖用户原始 PDF；
4. 若 PDF 二进制无法直接由当前 GitHub connector 复制，至少保留 File Library ID + 公开 URL + bibliographic metadata。

## E. 强制恢复关键词

新对话涉及 UHPC 时，至少搜索：

`Hiew 2024`, `Liu 2023`, `Liu 2024`, `Lee 2017`, `周俊`, `王淑楠`, `胡文旭`, `G16R`, `D19_LIU_TC`, `UHPC_STATE_EQUATION_LEDGER`, `Zhang 2023`, `Fehling`。

任何声称“完整恢复 UHPC 材性研究”的对话，若没有检查上述原件/工件，应判恢复不完整。
