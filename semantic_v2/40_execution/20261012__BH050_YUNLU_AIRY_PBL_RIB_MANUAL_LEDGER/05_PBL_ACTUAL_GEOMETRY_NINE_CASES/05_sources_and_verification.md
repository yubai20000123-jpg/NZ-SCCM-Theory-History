# 来源、版本与逐项核验

研究仓库 yubai20000123-jpg/NZ-SCCM-Theory-History，目标分支 research/20261012-bh050-rib-airy-manual-ledger；四份前置账本完整阅读，基准提交 d2cf149e7a45b656cde75eab2ef2ab4e9bf03255。本次仅添加 05_PBL_ACTUAL_GEOMETRY_NINE_CASES，不覆盖原 00..03。时间 2026-10-12（中国标准时间）。

## 正式来源决策

正式文件目录命名 R01 不代表其仍是历史前接触版本。每件 INP SHA256 与 2026-10-10 正式截面提取 EXTRACTION_PROVENANCE.json 的 source_before.inp.sha256 完全一致；BH032 使用 2026-09-26 接触恢复后正式文件。ODB 钢结构全节点又与相同 INP 比对，九件均 MATCH。没有把 RP/BASE、U_GROOVE、PBL_CROSS R03 或其近期改肋模型纳入正式提取。

原 CAE：`C:\03SCI\abaqus-UCFT test\UCFT_GS_DIRECT_R01_11MODELS\UCFT_GS_DIRECT_R01_11MODELS.cae`。本次无需打开/保存 CAE：对应可读 INP 的节点/单元/截面/集合为几何主证据，ODB 网格作独立核验。没有 CAE 读取失败，也没有用 CAE 目测代替坐标提取。

原始来源完整路径逐项如下；行号为一基 INP 行号。每根全部元素/节点 ID、逐层初始剖面、装配和关键字记录保存在 06；CSV 保留行号区间，区间内可能夹有非该肋节点，应按 JSON ID 筛选，不把整个行区间都认作该肋。

## BH005 / FORMAL_GS_DIRECT_R02_CONTACT_RESTORED / AR=2

INP：`C:\03SCI\abaqus-UCFT test\UCFT_GS_DIRECT_R01_11MODELS\JOB_BH005_GS_DIRECT_R01.inp`

SHA256：`2da83f9b47362bed7debccf151571af8d7d5270b29647d2cd0cecdad40b9e176`；大小 1183091 bytes；mtime Unix=1790375451。

ODB：`C:\03SCI\abaqus-UCFT test\UCFT_GS_DIRECT_R01_11MODELS\JOB_BH005_GS_DIRECT_R01.odb`；只读网格，不读场/历史；5610 / 5610 钢壳节点；最大差 4.982910085e-08 mm；PBL 集合 2700 单元与 INP 相符。对应历史审计：`C:\03SCI\abaqus-UCFT test\outputs\DIRECT_END_CREST_FORCE_AUDIT_20261010\BH005_EXTRACTION_PROVENANCE.json`。

| 肋 | 节点行区间 | 单元行区间 | PBL 截面行 | 实例行 | 根部共节点 | LOAD / FIX Tie 节点覆盖 |
| --- | --- | --- | --- | --- | --- | --- |
| TOP_04 | 12665, 17674 | 18414, 20863 | 24683 | 24698 | 51 | 7/7 ; 7/7 |
| TOP_01 | 12653, 17233 | 18264, 20713 | 24683 | 24698 | 51 | 7/7 ; 7/7 |
| TOP_03 | 12661, 16890 | 18364, 20813 | 24683 | 24698 | 51 | 7/7 ; 7/7 |
| TOP_02 | 12657, 16547 | 18314, 20763 | 24683 | 24698 | 51 | 7/7 ; 7/7 |
| BOTTOM_05 | 12677, 18066 | 18664, 20563 | 24683 | 24698 | 51 | 7/7 ; 7/7 |
| BOTTOM_09 | 12701, 18262 | 19064, 20963 | 24683 | 24698 | 51 | 7/7 ; 7/7 |
| BOTTOM_06 | 12681, 18115 | 18714, 20613 | 24683 | 24698 | 51 | 7/7 ; 7/7 |
| BOTTOM_08 | 12697, 18213 | 19014, 20913 | 24683 | 24698 | 51 | 7/7 ; 7/7 |
| BOTTOM_07 | 12685, 18164 | 18764, 20663 | 24683 | 24698 | 51 | 7/7 ; 7/7 |

装配原始数据（先平移、随后旋转，仅 GS_FIX 有变换；肋/核心无变换）：

| Instance | Part | 定义行 | 原始变换记录 |
| --- | --- | --- | --- |
| C-C-1 | c-c | 24695 | [] |
| C-S-SHELL-1 | c-s-shell | 24698 | [] |
| GS_LOAD-1 | GS_SHELL_PART | 24701 | [] |
| GS_FIX-1 | GS_SHELL_PART | 24704 | [[0.0, 0.0, 500.0], [0.0, 0.0, 500.0, 1.0, 0.0, 500.0, 180.0]] |

连接和边界原始关键字证据：

| 行 | 关键字 | 数据行与内容 |
| --- | --- | --- |
| 24808 | *Embedded Element, host elset=C-C-1.UHPC_ALL_CELLS | L24809: C-S-SHELL-1.UCFT_PBL_EMBEDDED_INTERIOR_ELEMENTS |
| 24811 | *Tie, name=TIE_FIX_GS_TO_STEEL_END, adjust=no, type=NODE TO SURFACE, no thickness | L24812: STEEL_END_ALL_NODES_TIED_FIX_CNS_, GS_FIX-1.GS_COMPLETE_FACE |
| 24814 | *Tie, name=TIE_GS_FIX_TO_UHPC_END, adjust=no, no thickness | L24815: C-C-1.UHPC_END_FIX_ALL, GS_FIX-1.GS_COMPLETE_FACE |
| 24817 | *Tie, name=TIE_GS_LOAD_TO_UHPC_END, adjust=no, no thickness | L24818: C-C-1.UHPC_END_LOAD_ALL, GS_LOAD-1.GS_COMPLETE_FACE |
| 24820 | *Tie, name=TIE_LOAD_GS_TO_STEEL_END, adjust=no, type=NODE TO SURFACE, no thickness | L24821: STEEL_END_ALL_NODES_TIED_LOAD_CNS_, GS_LOAD-1.GS_COMPLETE_FACE |
| 24959 | *Friction | L24960: 0.4, |
| 24961 | *Surface Behavior, pressure-overclosure=HARD |  |
| 24966 | *Boundary | L24967: SET_GS_FIX_MIDLINE_DIRECT, 1, 1 ; L24968: SET_GS_FIX_MIDLINE_DIRECT, 2, 2 ; L24969: SET_GS_FIX_MIDLINE_DIRECT, 3, 3 ; L24970: SET_GS_FIX_MIDLINE_DIRECT, 6, 6 |
| 24972 | *Boundary | L24973: SET_GS_LOAD_MIDLINE_DIRECT, 1, 1 ; L24974: SET_GS_LOAD_MIDLINE_DIRECT, 2, 2 ; L24975: SET_GS_LOAD_MIDLINE_DIRECT, 6, 6 |
| 24977 | *Boundary | L24978: SET_NONLOADED_SIDE_PLATE_XMAX_ACTIVE, 2, 2 |
| 24980 | *Boundary | L24981: SET_NONLOADED_SIDE_PLATE_XMIN_ACTIVE, 2, 2 |
| 24987 | *Contact Inclusions | L24988: C-S-SHELL-1.SHELL_INTERFACE_X_NEG, C-C-1.UHPC_INTERFACE_X_NEG ; L24989: C-S-SHELL-1.SHELL_INTERFACE_X_POS, C-C-1.UHPC_INTERFACE_X_POS ; L24990: C-S-SHELL-1.SHELL_INTERFACE_Y_NEG, C-C-1.UHPC_INTERFACE_Y_NEG ; L24991: C-S-SHELL-1.SHELL_INTERFACE_Y_POS, C-C-1.UHPC_INTERFACE_Y_POS |
| 24992 | *Contact Property Assignment | L24993: , , PROP_STEEL_UHPC_FRICTION |
| 25006 | *Boundary, amplitude=AMP_RP_LOAD_U3 | L25007: SET_GS_LOAD_MIDLINE_DIRECT, 3, 3, 2.5 |

PBL / 外壳截面、集合、单元类型定义行：

| 行 | 关键字 | 数据 |
| --- | --- | --- |
| 119 | *Element, type=S4R |  |
| 18263 | *Element, type=S4R |  |
| 23945 | *Elset, elset=UCFT_OUTER_SHELL_FACES, generate |  |
| 24149 | *Elset, elset=UCFT_PBL_WEB_FACES |  |
| 24319 | *Elset, elset=UCFT_PBL_EMBEDDED_INTERIOR_ELEMENTS |  |
| 24455 | *Elset, elset=UCFT_PBL_NONEMBEDDED_CONSTRAINT_EXCLUSION_ELEMENTS |  |
| 24683 | *Shell Section, elset=UCFT_PBL_WEB_FACES, material=STEEL_Q355 | L24684: 4., 5 |
| 24686 | *Shell Section, elset=UCFT_OUTER_SHELL_FACES, material=STEEL_Q355, offset=SNEG | L24687: 4., 5 |

## BH010 / FORMAL_GS_DIRECT_R02_CONTACT_RESTORED / AR=2

INP：`C:\03SCI\abaqus-UCFT test\UCFT_GS_DIRECT_R01_11MODELS\JOB_BH010_GS_DIRECT_R01.inp`

SHA256：`66ec75df0ba33f56804e29facc43aa32fa23f1edc1ede449592b6fb94c5d5975`；大小 1182984 bytes；mtime Unix=1790367642。

ODB：`C:\03SCI\abaqus-UCFT test\UCFT_GS_DIRECT_R01_11MODELS\JOB_BH010_GS_DIRECT_R01.odb`；只读网格，不读场/历史；5610 / 5610 钢壳节点；最大差 5.000000058e-08 mm；PBL 集合 2700 单元与 INP 相符。对应历史审计：`C:\03SCI\abaqus-UCFT test\outputs\DIRECT_END_CREST_FORCE_AUDIT_20261010\BH010_EXTRACTION_PROVENANCE.json`。

| 肋 | 节点行区间 | 单元行区间 | PBL 截面行 | 实例行 | 根部共节点 | LOAD / FIX Tie 节点覆盖 |
| --- | --- | --- | --- | --- | --- | --- |
| TOP_04 | 12665, 17674 | 18414, 20863 | 24683 | 24698 | 51 | 7/7 ; 7/7 |
| TOP_01 | 12653, 17233 | 18264, 20713 | 24683 | 24698 | 51 | 7/7 ; 7/7 |
| TOP_03 | 12661, 16890 | 18364, 20813 | 24683 | 24698 | 51 | 7/7 ; 7/7 |
| TOP_02 | 12657, 16547 | 18314, 20763 | 24683 | 24698 | 51 | 7/7 ; 7/7 |
| BOTTOM_05 | 12677, 18066 | 18664, 20563 | 24683 | 24698 | 51 | 7/7 ; 7/7 |
| BOTTOM_09 | 12701, 18262 | 19064, 20963 | 24683 | 24698 | 51 | 7/7 ; 7/7 |
| BOTTOM_06 | 12681, 18115 | 18714, 20613 | 24683 | 24698 | 51 | 7/7 ; 7/7 |
| BOTTOM_08 | 12697, 18213 | 19014, 20913 | 24683 | 24698 | 51 | 7/7 ; 7/7 |
| BOTTOM_07 | 12685, 18164 | 18764, 20663 | 24683 | 24698 | 51 | 7/7 ; 7/7 |

装配原始数据（先平移、随后旋转，仅 GS_FIX 有变换；肋/核心无变换）：

| Instance | Part | 定义行 | 原始变换记录 |
| --- | --- | --- | --- |
| C-C-1 | c-c | 24695 | [] |
| C-S-SHELL-1 | c-s-shell | 24698 | [] |
| GS_LOAD-1 | GS_SHELL_PART | 24701 | [] |
| GS_FIX-1 | GS_SHELL_PART | 24704 | [[0.0, 0.0, 1000.0], [0.0, 0.0, 1000.0, 1.0, 0.0, 1000.0, 180.0]] |

连接和边界原始关键字证据：

| 行 | 关键字 | 数据行与内容 |
| --- | --- | --- |
| 24808 | *Embedded Element, host elset=C-C-1.UHPC_ALL_CELLS | L24809: C-S-SHELL-1.UCFT_PBL_EMBEDDED_INTERIOR_ELEMENTS |
| 24811 | *Tie, name=TIE_FIX_GS_TO_STEEL_END, adjust=no, type=NODE TO SURFACE, no thickness | L24812: STEEL_END_ALL_NODES_TIED_FIX_CNS_, GS_FIX-1.GS_COMPLETE_FACE |
| 24814 | *Tie, name=TIE_GS_FIX_TO_UHPC_END, adjust=no, no thickness | L24815: C-C-1.UHPC_END_FIX_ALL, GS_FIX-1.GS_COMPLETE_FACE |
| 24817 | *Tie, name=TIE_GS_LOAD_TO_UHPC_END, adjust=no, no thickness | L24818: C-C-1.UHPC_END_LOAD_ALL, GS_LOAD-1.GS_COMPLETE_FACE |
| 24820 | *Tie, name=TIE_LOAD_GS_TO_STEEL_END, adjust=no, type=NODE TO SURFACE, no thickness | L24821: STEEL_END_ALL_NODES_TIED_LOAD_CNS_, GS_LOAD-1.GS_COMPLETE_FACE |
| 24959 | *Friction | L24960: 0.4, |
| 24961 | *Surface Behavior, pressure-overclosure=HARD |  |
| 24966 | *Boundary | L24967: SET_GS_FIX_MIDLINE_DIRECT, 1, 1 ; L24968: SET_GS_FIX_MIDLINE_DIRECT, 2, 2 ; L24969: SET_GS_FIX_MIDLINE_DIRECT, 3, 3 ; L24970: SET_GS_FIX_MIDLINE_DIRECT, 6, 6 |
| 24972 | *Boundary | L24973: SET_GS_LOAD_MIDLINE_DIRECT, 1, 1 ; L24974: SET_GS_LOAD_MIDLINE_DIRECT, 2, 2 ; L24975: SET_GS_LOAD_MIDLINE_DIRECT, 6, 6 |
| 24977 | *Boundary | L24978: SET_NONLOADED_SIDE_PLATE_XMAX_ACTIVE, 2, 2 |
| 24980 | *Boundary | L24981: SET_NONLOADED_SIDE_PLATE_XMIN_ACTIVE, 2, 2 |
| 24987 | *Contact Inclusions | L24988: C-S-SHELL-1.SHELL_INTERFACE_X_NEG, C-C-1.UHPC_INTERFACE_X_NEG ; L24989: C-S-SHELL-1.SHELL_INTERFACE_X_POS, C-C-1.UHPC_INTERFACE_X_POS ; L24990: C-S-SHELL-1.SHELL_INTERFACE_Y_NEG, C-C-1.UHPC_INTERFACE_Y_NEG ; L24991: C-S-SHELL-1.SHELL_INTERFACE_Y_POS, C-C-1.UHPC_INTERFACE_Y_POS |
| 24992 | *Contact Property Assignment | L24993: , , PROP_STEEL_UHPC_FRICTION |
| 25006 | *Boundary, amplitude=AMP_RP_LOAD_U3 | L25007: SET_GS_LOAD_MIDLINE_DIRECT, 3, 3, 5. |

PBL / 外壳截面、集合、单元类型定义行：

| 行 | 关键字 | 数据 |
| --- | --- | --- |
| 119 | *Element, type=S4R |  |
| 18263 | *Element, type=S4R |  |
| 23945 | *Elset, elset=UCFT_OUTER_SHELL_FACES, generate |  |
| 24149 | *Elset, elset=UCFT_PBL_WEB_FACES |  |
| 24319 | *Elset, elset=UCFT_PBL_EMBEDDED_INTERIOR_ELEMENTS |  |
| 24455 | *Elset, elset=UCFT_PBL_NONEMBEDDED_CONSTRAINT_EXCLUSION_ELEMENTS |  |
| 24683 | *Shell Section, elset=UCFT_PBL_WEB_FACES, material=STEEL_Q355 | L24684: 4., 5 |
| 24686 | *Shell Section, elset=UCFT_OUTER_SHELL_FACES, material=STEEL_Q355, offset=SNEG | L24687: 4., 5 |

## BH020 / FORMAL_GS_DIRECT_R02_CONTACT_RESTORED / AR=2

INP：`C:\03SCI\abaqus-UCFT test\UCFT_GS_DIRECT_R01_11MODELS\JOB_BH020_GS_DIRECT_R01.inp`

SHA256：`447ab9a8c915d7800ac3c197fe879b4abb325a695476d0338d53e3220c37d5b0`；大小 1182957 bytes；mtime Unix=1790359824。

ODB：`C:\03SCI\abaqus-UCFT test\UCFT_GS_DIRECT_R01_11MODELS\JOB_BH020_GS_DIRECT_R01.odb`；只读网格，不读场/历史；5610 / 5610 钢壳节点；最大差 4.990234359e-08 mm；PBL 集合 2700 单元与 INP 相符。对应历史审计：`C:\03SCI\abaqus-UCFT test\outputs\DIRECT_END_CREST_FORCE_AUDIT_20261010\BH020_EXTRACTION_PROVENANCE.json`。

| 肋 | 节点行区间 | 单元行区间 | PBL 截面行 | 实例行 | 根部共节点 | LOAD / FIX Tie 节点覆盖 |
| --- | --- | --- | --- | --- | --- | --- |
| TOP_04 | 12665, 17674 | 18414, 20863 | 24683 | 24698 | 51 | 7/7 ; 7/7 |
| TOP_01 | 12653, 17233 | 18264, 20713 | 24683 | 24698 | 51 | 7/7 ; 7/7 |
| TOP_03 | 12661, 16890 | 18364, 20813 | 24683 | 24698 | 51 | 7/7 ; 7/7 |
| TOP_02 | 12657, 16547 | 18314, 20763 | 24683 | 24698 | 51 | 7/7 ; 7/7 |
| BOTTOM_05 | 12677, 18066 | 18664, 20563 | 24683 | 24698 | 51 | 7/7 ; 7/7 |
| BOTTOM_09 | 12701, 18262 | 19064, 20963 | 24683 | 24698 | 51 | 7/7 ; 7/7 |
| BOTTOM_06 | 12681, 18115 | 18714, 20613 | 24683 | 24698 | 51 | 7/7 ; 7/7 |
| BOTTOM_08 | 12697, 18213 | 19014, 20913 | 24683 | 24698 | 51 | 7/7 ; 7/7 |
| BOTTOM_07 | 12685, 18164 | 18764, 20663 | 24683 | 24698 | 51 | 7/7 ; 7/7 |

装配原始数据（先平移、随后旋转，仅 GS_FIX 有变换；肋/核心无变换）：

| Instance | Part | 定义行 | 原始变换记录 |
| --- | --- | --- | --- |
| C-C-1 | c-c | 24695 | [] |
| C-S-SHELL-1 | c-s-shell | 24698 | [] |
| GS_LOAD-1 | GS_SHELL_PART | 24701 | [] |
| GS_FIX-1 | GS_SHELL_PART | 24704 | [[0.0, 0.0, 2000.0], [0.0, 0.0, 2000.0, 1.0, 0.0, 2000.0, 180.0]] |

连接和边界原始关键字证据：

| 行 | 关键字 | 数据行与内容 |
| --- | --- | --- |
| 24808 | *Embedded Element, host elset=C-C-1.UHPC_ALL_CELLS | L24809: C-S-SHELL-1.UCFT_PBL_EMBEDDED_INTERIOR_ELEMENTS |
| 24811 | *Tie, name=TIE_FIX_GS_TO_STEEL_END, adjust=no, type=NODE TO SURFACE, no thickness | L24812: STEEL_END_ALL_NODES_TIED_FIX_CNS_, GS_FIX-1.GS_COMPLETE_FACE |
| 24814 | *Tie, name=TIE_GS_FIX_TO_UHPC_END, adjust=no, no thickness | L24815: C-C-1.UHPC_END_FIX_ALL, GS_FIX-1.GS_COMPLETE_FACE |
| 24817 | *Tie, name=TIE_GS_LOAD_TO_UHPC_END, adjust=no, no thickness | L24818: C-C-1.UHPC_END_LOAD_ALL, GS_LOAD-1.GS_COMPLETE_FACE |
| 24820 | *Tie, name=TIE_LOAD_GS_TO_STEEL_END, adjust=no, type=NODE TO SURFACE, no thickness | L24821: STEEL_END_ALL_NODES_TIED_LOAD_CNS_, GS_LOAD-1.GS_COMPLETE_FACE |
| 24959 | *Friction | L24960: 0.4, |
| 24961 | *Surface Behavior, pressure-overclosure=HARD |  |
| 24966 | *Boundary | L24967: SET_GS_FIX_MIDLINE_DIRECT, 1, 1 ; L24968: SET_GS_FIX_MIDLINE_DIRECT, 2, 2 ; L24969: SET_GS_FIX_MIDLINE_DIRECT, 3, 3 ; L24970: SET_GS_FIX_MIDLINE_DIRECT, 6, 6 |
| 24972 | *Boundary | L24973: SET_GS_LOAD_MIDLINE_DIRECT, 1, 1 ; L24974: SET_GS_LOAD_MIDLINE_DIRECT, 2, 2 ; L24975: SET_GS_LOAD_MIDLINE_DIRECT, 6, 6 |
| 24977 | *Boundary | L24978: SET_NONLOADED_SIDE_PLATE_XMAX_ACTIVE, 2, 2 |
| 24980 | *Boundary | L24981: SET_NONLOADED_SIDE_PLATE_XMIN_ACTIVE, 2, 2 |
| 24987 | *Contact Inclusions | L24988: C-S-SHELL-1.SHELL_INTERFACE_X_NEG, C-C-1.UHPC_INTERFACE_X_NEG ; L24989: C-S-SHELL-1.SHELL_INTERFACE_X_POS, C-C-1.UHPC_INTERFACE_X_POS ; L24990: C-S-SHELL-1.SHELL_INTERFACE_Y_NEG, C-C-1.UHPC_INTERFACE_Y_NEG ; L24991: C-S-SHELL-1.SHELL_INTERFACE_Y_POS, C-C-1.UHPC_INTERFACE_Y_POS |
| 24992 | *Contact Property Assignment | L24993: , , PROP_STEEL_UHPC_FRICTION |
| 25006 | *Boundary, amplitude=AMP_RP_LOAD_U3 | L25007: SET_GS_LOAD_MIDLINE_DIRECT, 3, 3, 10. |

PBL / 外壳截面、集合、单元类型定义行：

| 行 | 关键字 | 数据 |
| --- | --- | --- |
| 119 | *Element, type=S4R |  |
| 18263 | *Element, type=S4R |  |
| 23945 | *Elset, elset=UCFT_OUTER_SHELL_FACES, generate |  |
| 24149 | *Elset, elset=UCFT_PBL_WEB_FACES |  |
| 24319 | *Elset, elset=UCFT_PBL_EMBEDDED_INTERIOR_ELEMENTS |  |
| 24455 | *Elset, elset=UCFT_PBL_NONEMBEDDED_CONSTRAINT_EXCLUSION_ELEMENTS |  |
| 24683 | *Shell Section, elset=UCFT_PBL_WEB_FACES, material=STEEL_Q355 | L24684: 4., 5 |
| 24686 | *Shell Section, elset=UCFT_OUTER_SHELL_FACES, material=STEEL_Q355, offset=SNEG | L24687: 4., 5 |

## BH032 / FORMAL_GS_DIRECT_R02_CONTACT_RESTORED / AR=2

INP：`C:\03SCI\abaqus-UCFT test\UCFT_GS_DIRECT_R01_11MODELS\JOB_BH032_GS_DIRECT_R01.inp`

SHA256：`4c79aa6d2649c014d35ce0b123e9239f8eded86707e874c0082fd3c9a7fc2ffe`；大小 1182209 bytes；mtime Unix=1790429078。

ODB：`C:\03SCI\abaqus-UCFT test\UCFT_GS_DIRECT_R01_11MODELS\JOB_BH032_GS_DIRECT_R01.odb`；只读网格，不读场/历史；5610 / 5610 钢壳节点；最大差 4.978027413e-08 mm；PBL 集合 2700 单元与 INP 相符。对应历史审计：`C:\03SCI\abaqus-UCFT test\outputs\DIRECT_END_CREST_FORCE_AUDIT_20261010\BH032_EXTRACTION_PROVENANCE.json`。

| 肋 | 节点行区间 | 单元行区间 | PBL 截面行 | 实例行 | 根部共节点 | LOAD / FIX Tie 节点覆盖 |
| --- | --- | --- | --- | --- | --- | --- |
| TOP_04 | 12665, 17674 | 18414, 20863 | 24683 | 24698 | 51 | 7/7 ; 7/7 |
| TOP_01 | 12653, 17233 | 18264, 20713 | 24683 | 24698 | 51 | 7/7 ; 7/7 |
| TOP_03 | 12661, 16890 | 18364, 20813 | 24683 | 24698 | 51 | 7/7 ; 7/7 |
| TOP_02 | 12657, 16547 | 18314, 20763 | 24683 | 24698 | 51 | 7/7 ; 7/7 |
| BOTTOM_05 | 12677, 18066 | 18664, 20563 | 24683 | 24698 | 51 | 7/7 ; 7/7 |
| BOTTOM_09 | 12701, 18262 | 19064, 20963 | 24683 | 24698 | 51 | 7/7 ; 7/7 |
| BOTTOM_06 | 12681, 18115 | 18714, 20613 | 24683 | 24698 | 51 | 7/7 ; 7/7 |
| BOTTOM_08 | 12697, 18213 | 19014, 20913 | 24683 | 24698 | 51 | 7/7 ; 7/7 |
| BOTTOM_07 | 12685, 18164 | 18764, 20663 | 24683 | 24698 | 51 | 7/7 ; 7/7 |

装配原始数据（先平移、随后旋转，仅 GS_FIX 有变换；肋/核心无变换）：

| Instance | Part | 定义行 | 原始变换记录 |
| --- | --- | --- | --- |
| C-C-1 | c-c | 24695 | [] |
| C-S-SHELL-1 | c-s-shell | 24698 | [] |
| GS_LOAD-1 | GS_SHELL_PART | 24701 | [] |
| GS_FIX-1 | GS_SHELL_PART | 24704 | [[0.0, 0.0, 3200.0], [0.0, 0.0, 3200.0, 1.0, 0.0, 3200.0, 180.0]] |

连接和边界原始关键字证据：

| 行 | 关键字 | 数据行与内容 |
| --- | --- | --- |
| 24808 | *Embedded Element, host elset=C-C-1.UHPC_ALL_CELLS | L24809: C-S-SHELL-1.UCFT_PBL_EMBEDDED_INTERIOR_ELEMENTS |
| 24811 | *Tie, name=TIE_FIX_GS_TO_STEEL_END, adjust=no, type=NODE TO SURFACE, no thickness | L24812: STEEL_END_ALL_NODES_TIED_FIX_CNS_, GS_FIX-1.GS_COMPLETE_FACE |
| 24814 | *Tie, name=TIE_GS_FIX_TO_UHPC_END, adjust=no, no thickness | L24815: C-C-1.UHPC_END_FIX_ALL, GS_FIX-1.GS_COMPLETE_FACE |
| 24817 | *Tie, name=TIE_GS_LOAD_TO_UHPC_END, adjust=no, no thickness | L24818: C-C-1.UHPC_END_LOAD_ALL, GS_LOAD-1.GS_COMPLETE_FACE |
| 24820 | *Tie, name=TIE_LOAD_GS_TO_STEEL_END, adjust=no, type=NODE TO SURFACE, no thickness | L24821: STEEL_END_ALL_NODES_TIED_LOAD_CNS_, GS_LOAD-1.GS_COMPLETE_FACE |
| 24959 | *Friction | L24960: 0.4, |
| 24961 | *Surface Behavior, pressure-overclosure=HARD |  |
| 24966 | *Boundary | L24967: SET_GS_FIX_MIDLINE_DIRECT, 1, 1 ; L24968: SET_GS_FIX_MIDLINE_DIRECT, 2, 2 ; L24969: SET_GS_FIX_MIDLINE_DIRECT, 3, 3 ; L24970: SET_GS_FIX_MIDLINE_DIRECT, 6, 6 |
| 24972 | *Boundary | L24973: SET_GS_LOAD_MIDLINE_DIRECT, 1, 1 ; L24974: SET_GS_LOAD_MIDLINE_DIRECT, 2, 2 ; L24975: SET_GS_LOAD_MIDLINE_DIRECT, 6, 6 |
| 24977 | *Boundary | L24978: SET_NONLOADED_SIDE_PLATE_XMAX_ACTIVE, 2, 2 |
| 24980 | *Boundary | L24981: SET_NONLOADED_SIDE_PLATE_XMIN_ACTIVE, 2, 2 |
| 24987 | *Contact Inclusions | L24988: C-S-SHELL-1.SHELL_INTERFACE_X_NEG, C-C-1.UHPC_INTERFACE_X_NEG ; L24989: C-S-SHELL-1.SHELL_INTERFACE_X_POS, C-C-1.UHPC_INTERFACE_X_POS ; L24990: C-S-SHELL-1.SHELL_INTERFACE_Y_NEG, C-C-1.UHPC_INTERFACE_Y_NEG ; L24991: C-S-SHELL-1.SHELL_INTERFACE_Y_POS, C-C-1.UHPC_INTERFACE_Y_POS |
| 24992 | *Contact Property Assignment | L24993: , , PROP_STEEL_UHPC_FRICTION |
| 25006 | *Boundary, amplitude=AMP_RP_LOAD_U3 | L25007: SET_GS_LOAD_MIDLINE_DIRECT, 3, 3, 16. |

PBL / 外壳截面、集合、单元类型定义行：

| 行 | 关键字 | 数据 |
| --- | --- | --- |
| 119 | *Element, type=S4R |  |
| 18263 | *Element, type=S4R |  |
| 23945 | *Elset, elset=UCFT_OUTER_SHELL_FACES, generate |  |
| 24149 | *Elset, elset=UCFT_PBL_WEB_FACES |  |
| 24319 | *Elset, elset=UCFT_PBL_EMBEDDED_INTERIOR_ELEMENTS |  |
| 24455 | *Elset, elset=UCFT_PBL_NONEMBEDDED_CONSTRAINT_EXCLUSION_ELEMENTS |  |
| 24683 | *Shell Section, elset=UCFT_PBL_WEB_FACES, material=STEEL_Q355 | L24684: 4., 5 |
| 24686 | *Shell Section, elset=UCFT_OUTER_SHELL_FACES, material=STEEL_Q355, offset=SNEG | L24687: 4., 5 |

## BH050 / FORMAL_GS_DIRECT_R02_CONTACT_RESTORED / AR=2

INP：`C:\03SCI\abaqus-UCFT test\UCFT_GS_DIRECT_R01_11MODELS\JOB_BH050_GS_DIRECT_R01.inp`

SHA256：`8b8050de30a188025d9326f88413c56de74963535848f75e1c752263dc84a96e`；大小 1743386 bytes；mtime Unix=1790322758。

ODB：`C:\03SCI\abaqus-UCFT test\UCFT_GS_DIRECT_R01_11MODELS\JOB_BH050_GS_DIRECT_R01.odb`；只读网格，不读场/历史；11110 / 11110 钢壳节点；最大差 4.996337921e-08 mm；PBL 集合 5400 单元与 INP 相符。对应历史审计：`C:\03SCI\abaqus-UCFT test\outputs\DIRECT_END_CREST_FORCE_AUDIT_20261010\BH050_EXTRACTION_PROVENANCE.json`。

| 肋 | 节点行区间 | 单元行区间 | PBL 截面行 | 实例行 | 根部共节点 | LOAD / FIX Tie 节点覆盖 |
| --- | --- | --- | --- | --- | --- | --- |
| TOP_04 | 12676, 22585 | 24075, 28974 | 36579 | 36594 | 101 | 7/7 ; 7/7 |
| TOP_01 | 12664, 21694 | 23775, 28674 | 36579 | 36594 | 101 | 7/7 ; 7/7 |
| TOP_03 | 12672, 21001 | 23975, 28874 | 36579 | 36594 | 101 | 7/7 ; 7/7 |
| TOP_02 | 12668, 20308 | 23875, 28774 | 36579 | 36594 | 101 | 7/7 ; 7/7 |
| BOTTOM_05 | 12688, 23377 | 24575, 28374 | 36579 | 36594 | 101 | 7/7 ; 7/7 |
| BOTTOM_09 | 12712, 23773 | 25375, 29174 | 36579 | 36594 | 101 | 7/7 ; 7/7 |
| BOTTOM_06 | 12692, 23476 | 24675, 28474 | 36579 | 36594 | 101 | 7/7 ; 7/7 |
| BOTTOM_08 | 12708, 23674 | 25275, 29074 | 36579 | 36594 | 101 | 7/7 ; 7/7 |
| BOTTOM_07 | 12696, 23575 | 24775, 28574 | 36579 | 36594 | 101 | 7/7 ; 7/7 |

装配原始数据（先平移、随后旋转，仅 GS_FIX 有变换；肋/核心无变换）：

| Instance | Part | 定义行 | 原始变换记录 |
| --- | --- | --- | --- |
| C-C-1 | c-c | 36591 | [] |
| C-S-SHELL-1 | c-s-shell | 36594 | [] |
| GS_LOAD-1 | GS_SHELL_PART | 36597 | [] |
| GS_FIX-1 | GS_SHELL_PART | 36600 | [[0.0, 0.0, 5000.0], [0.0, 0.0, 5000.0, 1.0, 0.0, 5000.0, 180.0]] |

连接和边界原始关键字证据：

| 行 | 关键字 | 数据行与内容 |
| --- | --- | --- |
| 36760 | *Embedded Element, host elset=C-C-1.UHPC_ALL_CELLS | L36761: C-S-SHELL-1.UCFT_PBL_EMBEDDED_INTERIOR_ELEMENTS |
| 36763 | *Tie, name=TIE_FIX_GS_TO_STEEL_END, adjust=no, type=NODE TO SURFACE, no thickness | L36764: STEEL_END_ALL_NODES_TIED_FIX_CNS_, GS_FIX-1.GS_COMPLETE_FACE |
| 36766 | *Tie, name=TIE_GS_FIX_TO_UHPC_END, adjust=no, no thickness | L36767: C-C-1.UHPC_END_FIX_ALL, GS_FIX-1.GS_COMPLETE_FACE |
| 36769 | *Tie, name=TIE_GS_LOAD_TO_UHPC_END, adjust=no, no thickness | L36770: C-C-1.UHPC_END_LOAD_ALL, GS_LOAD-1.GS_COMPLETE_FACE |
| 36772 | *Tie, name=TIE_LOAD_GS_TO_STEEL_END, adjust=no, type=NODE TO SURFACE, no thickness | L36773: STEEL_END_ALL_NODES_TIED_LOAD_CNS_, GS_LOAD-1.GS_COMPLETE_FACE |
| 36911 | *Friction | L36912: 0.4, |
| 36913 | *Surface Behavior, pressure-overclosure=HARD |  |
| 36918 | *Boundary | L36919: SET_GS_FIX_MIDLINE_DIRECT, 1, 1 ; L36920: SET_GS_FIX_MIDLINE_DIRECT, 2, 2 ; L36921: SET_GS_FIX_MIDLINE_DIRECT, 3, 3 ; L36922: SET_GS_FIX_MIDLINE_DIRECT, 6, 6 |
| 36924 | *Boundary | L36925: SET_GS_LOAD_MIDLINE_DIRECT, 1, 1 ; L36926: SET_GS_LOAD_MIDLINE_DIRECT, 2, 2 ; L36927: SET_GS_LOAD_MIDLINE_DIRECT, 6, 6 |
| 36929 | *Boundary | L36930: SET_NONLOADED_SIDE_PLATE_XMAX_ACTIVE, 2, 2 |
| 36932 | *Boundary | L36933: SET_NONLOADED_SIDE_PLATE_XMIN_ACTIVE, 2, 2 |
| 36939 | *Contact Inclusions | L36940: C-S-SHELL-1.SHELL_INTERFACE_X_NEG, C-C-1.UHPC_INTERFACE_X_NEG ; L36941: C-S-SHELL-1.SHELL_INTERFACE_X_POS, C-C-1.UHPC_INTERFACE_X_POS ; L36942: C-S-SHELL-1.SHELL_INTERFACE_Y_NEG, C-C-1.UHPC_INTERFACE_Y_NEG ; L36943: C-S-SHELL-1.SHELL_INTERFACE_Y_POS, C-C-1.UHPC_INTERFACE_Y_POS |
| 36944 | *Contact Property Assignment | L36945: , , PROP_STEEL_UHPC_FRICTION |
| 36961 | *Boundary, amplitude=AMP_RP_LOAD_U3 | L36962: SET_GS_LOAD_MIDLINE_DIRECT, 3, 3, 25. |

PBL / 外壳截面、集合、单元类型定义行：

| 行 | 关键字 | 数据 |
| --- | --- | --- |
| 130 | *Element, type=S4R |  |
| 23774 | *Element, type=S4R |  |
| 35131 | *Elset, elset=UCFT_OUTER_SHELL_FACES, generate |  |
| 35532 | *Elset, elset=UCFT_PBL_WEB_FACES |  |
| 35871 | *Elset, elset=UCFT_PBL_EMBEDDED_INTERIOR_ELEMENTS |  |
| 36120 | *Elset, elset=UCFT_PBL_NONEMBEDDED_CONSTRAINT_EXCLUSION_ELEMENTS |  |
| 36579 | *Shell Section, elset=UCFT_PBL_WEB_FACES, material=STEEL_Q355 | L36580: 4., 5 |
| 36582 | *Shell Section, elset=UCFT_OUTER_SHELL_FACES, material=STEEL_Q355, offset=SNEG | L36583: 4., 5 |

## BH060 / FORMAL_GS_DIRECT_R02_CONTACT_RESTORED / AR=2

INP：`C:\03SCI\abaqus-UCFT test\UCFT_GS_DIRECT_R01_11MODELS\JOB_BH060_GS_DIRECT_R01.inp`

SHA256：`898de0305bd18fabd8e576a0e12735f7f612665c43e8b64f05ad8c7cd030e9f8`；大小 1854622 bytes；mtime Unix=1790285846。

ODB：`C:\03SCI\abaqus-UCFT test\UCFT_GS_DIRECT_R01_11MODELS\JOB_BH060_GS_DIRECT_R01.odb`；只读网格，不读场/历史；11110 / 11110 钢壳节点；最大差 4.997558634e-08 mm；PBL 集合 5400 单元与 INP 相符。对应历史审计：`C:\03SCI\abaqus-UCFT test\outputs\DIRECT_END_CREST_FORCE_AUDIT_20261010\BH060_EXTRACTION_PROVENANCE.json`。

| 肋 | 节点行区间 | 单元行区间 | PBL 截面行 | 实例行 | 根部共节点 | LOAD / FIX Tie 节点覆盖 |
| --- | --- | --- | --- | --- | --- | --- |
| TOP_04 | 12831, 21643 | 29823, 34522 | 37545 | 37557 | 101 | 7/7 ; 7/7 |
| TOP_01 | 12819, 21346 | 29523, 34222 | 37545 | 37557 | 101 | 7/7 ; 7/7 |
| TOP_03 | 12827, 21544 | 29723, 34422 | 37545 | 37557 | 101 | 7/7 ; 7/7 |
| TOP_02 | 12823, 21445 | 29623, 34322 | 37545 | 37557 | 101 | 7/7 ; 7/7 |
| BOTTOM_05 | 12851, 23524 | 30723, 33722 | 37545 | 37557 | 101 | 7/7 ; 7/7 |
| BOTTOM_09 | 12875, 23920 | 32323, 34922 | 37545 | 37557 | 101 | 7/7 ; 7/7 |
| BOTTOM_06 | 12855, 23623 | 30923, 33922 | 37545 | 37557 | 101 | 7/7 ; 7/7 |
| BOTTOM_08 | 12871, 23821 | 32123, 34722 | 37545 | 37557 | 101 | 7/7 ; 7/7 |
| BOTTOM_07 | 12859, 23722 | 31123, 34122 | 37545 | 37557 | 101 | 7/7 ; 7/7 |

装配原始数据（先平移、随后旋转，仅 GS_FIX 有变换；肋/核心无变换）：

| Instance | Part | 定义行 | 原始变换记录 |
| --- | --- | --- | --- |
| C-C-1 | c-c | 37554 | [] |
| C-S-SHELL-1 | c-s-shell | 37557 | [] |
| GS_LOAD-1 | GS_SHELL_PART | 37560 | [] |
| GS_FIX-1 | GS_SHELL_PART | 37563 | [[0.0, 0.0, 6000.0], [0.0, 0.0, 6000.0, 1.0, 0.0, 6000.0, 180.0]] |

连接和边界原始关键字证据：

| 行 | 关键字 | 数据行与内容 |
| --- | --- | --- |
| 37895 | *Embedded Element, host elset=C-C-1.UHPC_ALL_CELLS | L37896: C-S-SHELL-1.UCFT_PBL_EMBEDDED_INTERIOR_ELEMENTS |
| 37898 | *Tie, name=TIE_FIX_GS_NEGY_TO_UHPC_END, adjust=no | L37899: GS_FIX-1.GS_TIE_BAND_NEGY, C-C-1.UHPC_END_FIX_ALL |
| 37901 | *Tie, name=TIE_FIX_GS_POSY_TO_UHPC_END, adjust=no | L37902: GS_FIX-1.GS_TIE_BAND_POSY, C-C-1.UHPC_END_FIX_ALL |
| 37904 | *Tie, name=TIE_FIX_GS_TO_STEEL_END_TIEDNSET, adjust=no, type=NODE TO SURFACE, no thickness | L37905: STEEL_FIX_END_ALL_NODES_TIED_CNS_, GS_FIX-1.GS_COMPLETE_FACE |
| 37907 | *Tie, name=TIE_LOAD_GS_NEGY_TO_UHPC_END, adjust=no | L37908: GS_LOAD-1.GS_TIE_BAND_NEGY, C-C-1.UHPC_END_LOAD_ALL |
| 37910 | *Tie, name=TIE_LOAD_GS_POSY_TO_UHPC_END, adjust=no | L37911: GS_LOAD-1.GS_TIE_BAND_POSY, C-C-1.UHPC_END_LOAD_ALL |
| 37913 | *Tie, name=TIE_LOAD_GS_TO_STEEL_END_TIEDNSET, adjust=no, type=NODE TO SURFACE, no thickness | L37914: STEEL_LOAD_END_ALL_NODES_TIED_CNS_, GS_LOAD-1.GS_COMPLETE_FACE |
| 38052 | *Friction | L38053: 0.4, |
| 38054 | *Surface Behavior, pressure-overclosure=HARD |  |
| 38056 | *Friction | L38057: 0.4, |
| 38058 | *Surface Behavior, pressure-overclosure=HARD |  |
| 38063 | *Boundary | L38064: SET_GS_FIX_MIDLINE_DIRECT, 1, 1 ; L38065: SET_GS_FIX_MIDLINE_DIRECT, 2, 2 ; L38066: SET_GS_FIX_MIDLINE_DIRECT, 3, 3 ; L38067: SET_GS_FIX_MIDLINE_DIRECT, 6, 6 |
| 38069 | *Boundary | L38070: SET_GS_LOAD_MIDLINE_DIRECT, 1, 1 ; L38071: SET_GS_LOAD_MIDLINE_DIRECT, 2, 2 ; L38072: SET_GS_LOAD_MIDLINE_DIRECT, 6, 6 |
| 38074 | *Boundary | L38075: SET_NONLOADED_SIDE_PLATE_XMAX_ACTIVE, 2, 2 |
| 38077 | *Boundary | L38078: SET_NONLOADED_SIDE_PLATE_XMIN_ACTIVE, 2, 2 |
| 38084 | *Contact Inclusions | L38085: C-S-SHELL-1.SHELL_INTERFACE_X_NEG, C-C-1.UHPC_INTERFACE_X_NEG ; L38086: C-S-SHELL-1.SHELL_INTERFACE_X_POS, C-C-1.UHPC_INTERFACE_X_POS ; L38087: C-S-SHELL-1.SHELL_INTERFACE_Y_NEG, C-C-1.UHPC_INTERFACE_Y_NEG ; L38088: C-S-SHELL-1.SHELL_INTERFACE_Y_POS, C-C-1.UHPC_INTERFACE_Y_POS |
| 38089 | *Contact Property Assignment | L38090: , , PROP_STEEL_UHPC_FRICTION |
| 38106 | *Boundary, amplitude=AMP_RP_LOAD_U3 | L38107: SET_GS_LOAD_MIDLINE_DIRECT, 3, 3, 30. |

PBL / 外壳截面、集合、单元类型定义行：

| 行 | 关键字 | 数据 |
| --- | --- | --- |
| 127 | *Element, type=S4R |  |
| 29522 | *Element, type=S4R |  |
| 35278 | *Elset, elset=UCFT_OUTER_SHELL_FACES |  |
| 36028 | *Elset, elset=UCFT_PBL_WEB_FACES |  |
| 36485 | *Elset, elset=UCFT_PBL_EMBEDDED_INTERIOR_ELEMENTS |  |
| 36740 | *Elset, elset=UCFT_PBL_NONEMBEDDED_CONSTRAINT_EXCLUSION_ELEMENTS |  |
| 37542 | *Shell Section, elset=UCFT_OUTER_SHELL_FACES, material=STEEL_Q355, offset=SNEG | L37543: 4., 5 |
| 37545 | *Shell Section, elset=UCFT_PBL_WEB_FACES, material=STEEL_Q355 | L37546: 4., 5 |

## BH070 / FORMAL_GS_DIRECT_R02_CONTACT_RESTORED / AR=2

INP：`C:\03SCI\abaqus-UCFT test\UCFT_GS_DIRECT_R01_11MODELS\JOB_BH070_GS_DIRECT_R01.inp`

SHA256：`f4c6f2b342a99a5d93b8df2ae073b0d38379f130d825e5651d5851d339b4118d`；大小 2512832 bytes；mtime Unix=1790272686。

ODB：`C:\03SCI\abaqus-UCFT test\UCFT_GS_DIRECT_R01_11MODELS\JOB_BH070_GS_DIRECT_R01.odb`；只读网格，不读场/历史；16610 / 16610 钢壳节点；最大差 4.023437441e-06 mm；PBL 集合 8100 单元与 INP 相符。对应历史审计：`C:\03SCI\abaqus-UCFT test\outputs\DIRECT_END_CREST_FORCE_AUDIT_20261010\BH070_EXTRACTION_PROVENANCE.json`。

| 肋 | 节点行区间 | 单元行区间 | PBL 截面行 | 实例行 | 根部共节点 | LOAD / FIX Tie 节点覆盖 |
| --- | --- | --- | --- | --- | --- | --- |
| TOP_04 | 12831, 25993 | 38273, 45322 | 49836 | 49848 | 151 | 7/7 ; 7/7 |
| TOP_01 | 12819, 25546 | 37823, 44872 | 49836 | 49848 | 151 | 7/7 ; 7/7 |
| TOP_03 | 12827, 25844 | 38123, 45172 | 49836 | 49848 | 151 | 7/7 ; 7/7 |
| TOP_02 | 12823, 25695 | 37973, 45022 | 49836 | 49848 | 151 | 7/7 ; 7/7 |
| BOTTOM_05 | 12851, 28824 | 39623, 44122 | 49836 | 49848 | 151 | 7/7 ; 7/7 |
| BOTTOM_09 | 12875, 29420 | 42023, 45922 | 49836 | 49848 | 151 | 7/7 ; 7/7 |
| BOTTOM_06 | 12855, 28973 | 39923, 44422 | 49836 | 49848 | 151 | 7/7 ; 7/7 |
| BOTTOM_08 | 12871, 29271 | 41723, 45622 | 49836 | 49848 | 151 | 7/7 ; 7/7 |
| BOTTOM_07 | 12859, 29122 | 40223, 44722 | 49836 | 49848 | 151 | 7/7 ; 7/7 |

装配原始数据（先平移、随后旋转，仅 GS_FIX 有变换；肋/核心无变换）：

| Instance | Part | 定义行 | 原始变换记录 |
| --- | --- | --- | --- |
| C-C-1 | c-c | 49845 | [] |
| C-S-SHELL-1 | c-s-shell | 49848 | [] |
| GS_LOAD-1 | GS_SHELL_PART | 49851 | [] |
| GS_FIX-1 | GS_SHELL_PART | 49854 | [[0.0, 0.0, 7000.0], [0.0, 0.0, 7000.0, 1.0, 0.0, 7000.0, 180.0]] |

连接和边界原始关键字证据：

| 行 | 关键字 | 数据行与内容 |
| --- | --- | --- |
| 50298 | *Embedded Element, host elset=C-C-1.UHPC_ALL_CELLS | L50299: C-S-SHELL-1.UCFT_PBL_EMBEDDED_INTERIOR_ELEMENTS |
| 50301 | *Tie, name=TIE_FIX_GS_NEGY_TO_UHPC_END, adjust=no | L50302: GS_FIX-1.GS_TIE_BAND_NEGY, C-C-1.UHPC_END_FIX_ALL |
| 50304 | *Tie, name=TIE_FIX_GS_POSY_TO_UHPC_END, adjust=no | L50305: GS_FIX-1.GS_TIE_BAND_POSY, C-C-1.UHPC_END_FIX_ALL |
| 50307 | *Tie, name=TIE_FIX_GS_TO_STEEL_END_TIEDNSET, adjust=no, type=NODE TO SURFACE, no thickness | L50308: STEEL_FIX_END_ALL_NODES_TIED_CNS_, GS_FIX-1.GS_COMPLETE_FACE |
| 50310 | *Tie, name=TIE_LOAD_GS_NEGY_TO_UHPC_END, adjust=no | L50311: GS_LOAD-1.GS_TIE_BAND_NEGY, C-C-1.UHPC_END_LOAD_ALL |
| 50313 | *Tie, name=TIE_LOAD_GS_POSY_TO_UHPC_END, adjust=no | L50314: GS_LOAD-1.GS_TIE_BAND_POSY, C-C-1.UHPC_END_LOAD_ALL |
| 50316 | *Tie, name=TIE_LOAD_GS_TO_STEEL_END_TIEDNSET, adjust=no, type=NODE TO SURFACE, no thickness | L50317: STEEL_LOAD_END_ALL_NODES_TIED_CNS_, GS_LOAD-1.GS_COMPLETE_FACE |
| 50455 | *Friction | L50456: 0.4, |
| 50457 | *Surface Behavior, pressure-overclosure=HARD |  |
| 50459 | *Friction | L50460: 0.4, |
| 50461 | *Surface Behavior, pressure-overclosure=HARD |  |
| 50466 | *Boundary | L50467: SET_GS_FIX_MIDLINE_DIRECT, 1, 1 ; L50468: SET_GS_FIX_MIDLINE_DIRECT, 2, 2 ; L50469: SET_GS_FIX_MIDLINE_DIRECT, 3, 3 ; L50470: SET_GS_FIX_MIDLINE_DIRECT, 6, 6 |
| 50472 | *Boundary | L50473: SET_GS_LOAD_MIDLINE_DIRECT, 1, 1 ; L50474: SET_GS_LOAD_MIDLINE_DIRECT, 2, 2 ; L50475: SET_GS_LOAD_MIDLINE_DIRECT, 6, 6 |
| 50477 | *Boundary | L50478: SET_NONLOADED_SIDE_PLATE_XMAX_ACTIVE, 2, 2 |
| 50480 | *Boundary | L50481: SET_NONLOADED_SIDE_PLATE_XMIN_ACTIVE, 2, 2 |
| 50487 | *Contact Inclusions | L50488: C-S-SHELL-1.SHELL_INTERFACE_X_NEG, C-C-1.UHPC_INTERFACE_X_NEG ; L50489: C-S-SHELL-1.SHELL_INTERFACE_X_POS, C-C-1.UHPC_INTERFACE_X_POS ; L50490: C-S-SHELL-1.SHELL_INTERFACE_Y_NEG, C-C-1.UHPC_INTERFACE_Y_NEG ; L50491: C-S-SHELL-1.SHELL_INTERFACE_Y_POS, C-C-1.UHPC_INTERFACE_Y_POS |
| 50492 | *Contact Property Assignment | L50493: , , PROP_STEEL_UHPC_FRICTION |
| 50509 | *Boundary, amplitude=AMP_RP_LOAD_U3 | L50510: SET_GS_LOAD_MIDLINE_DIRECT, 3, 3, 35. |

PBL / 外壳截面、集合、单元类型定义行：

| 行 | 关键字 | 数据 |
| --- | --- | --- |
| 127 | *Element, type=S4R |  |
| 37822 | *Element, type=S4R |  |
| 46453 | *Elset, elset=UCFT_OUTER_SHELL_FACES |  |
| 47575 | *Elset, elset=UCFT_PBL_WEB_FACES |  |
| 48257 | *Elset, elset=UCFT_PBL_EMBEDDED_INTERIOR_ELEMENTS |  |
| 48638 | *Elset, elset=UCFT_PBL_NONEMBEDDED_CONSTRAINT_EXCLUSION_ELEMENTS |  |
| 49833 | *Shell Section, elset=UCFT_OUTER_SHELL_FACES, material=STEEL_Q355, offset=SNEG | L49834: 4., 5 |
| 49836 | *Shell Section, elset=UCFT_PBL_WEB_FACES, material=STEEL_Q355 | L49837: 4., 5 |

## BH085 / FORMAL_GS_DIRECT_R02_CONTACT_RESTORED / AR=2

INP：`C:\03SCI\abaqus-UCFT test\UCFT_GS_DIRECT_R01_11MODELS\JOB_BH085_GS_DIRECT_R01.inp`

SHA256：`1f4c21ee2d3531d4b4b3eb64aa7fff648ea21a50ae95bff8d118947ee0bba18b`；大小 2512849 bytes；mtime Unix=1790259799。

ODB：`C:\03SCI\abaqus-UCFT test\UCFT_GS_DIRECT_R01_11MODELS\JOB_BH085_GS_DIRECT_R01.odb`；只读网格，不读场/历史；16610 / 16610 钢壳节点；最大差 4.023437441e-06 mm；PBL 集合 8100 单元与 INP 相符。对应历史审计：`C:\03SCI\abaqus-UCFT test\outputs\DIRECT_END_CREST_FORCE_AUDIT_20261010\BH085_EXTRACTION_PROVENANCE.json`。

| 肋 | 节点行区间 | 单元行区间 | PBL 截面行 | 实例行 | 根部共节点 | LOAD / FIX Tie 节点覆盖 |
| --- | --- | --- | --- | --- | --- | --- |
| TOP_04 | 12831, 25993 | 38273, 45322 | 49836 | 49848 | 151 | 7/7 ; 7/7 |
| TOP_01 | 12819, 25546 | 37823, 44872 | 49836 | 49848 | 151 | 7/7 ; 7/7 |
| TOP_03 | 12827, 25844 | 38123, 45172 | 49836 | 49848 | 151 | 7/7 ; 7/7 |
| TOP_02 | 12823, 25695 | 37973, 45022 | 49836 | 49848 | 151 | 7/7 ; 7/7 |
| BOTTOM_05 | 12851, 28824 | 39623, 44122 | 49836 | 49848 | 151 | 7/7 ; 7/7 |
| BOTTOM_09 | 12875, 29420 | 42023, 45922 | 49836 | 49848 | 151 | 7/7 ; 7/7 |
| BOTTOM_06 | 12855, 28973 | 39923, 44422 | 49836 | 49848 | 151 | 7/7 ; 7/7 |
| BOTTOM_08 | 12871, 29271 | 41723, 45622 | 49836 | 49848 | 151 | 7/7 ; 7/7 |
| BOTTOM_07 | 12859, 29122 | 40223, 44722 | 49836 | 49848 | 151 | 7/7 ; 7/7 |

装配原始数据（先平移、随后旋转，仅 GS_FIX 有变换；肋/核心无变换）：

| Instance | Part | 定义行 | 原始变换记录 |
| --- | --- | --- | --- |
| C-C-1 | c-c | 49845 | [] |
| C-S-SHELL-1 | c-s-shell | 49848 | [] |
| GS_LOAD-1 | GS_SHELL_PART | 49851 | [] |
| GS_FIX-1 | GS_SHELL_PART | 49854 | [[0.0, 0.0, 8500.0], [0.0, 0.0, 8500.0, 1.0, 0.0, 8500.0, 180.0]] |

连接和边界原始关键字证据：

| 行 | 关键字 | 数据行与内容 |
| --- | --- | --- |
| 50298 | *Embedded Element, host elset=C-C-1.UHPC_ALL_CELLS | L50299: C-S-SHELL-1.UCFT_PBL_EMBEDDED_INTERIOR_ELEMENTS |
| 50301 | *Tie, name=TIE_FIX_GS_NEGY_TO_UHPC_END, adjust=no | L50302: GS_FIX-1.GS_TIE_BAND_NEGY, C-C-1.UHPC_END_FIX_ALL |
| 50304 | *Tie, name=TIE_FIX_GS_POSY_TO_UHPC_END, adjust=no | L50305: GS_FIX-1.GS_TIE_BAND_POSY, C-C-1.UHPC_END_FIX_ALL |
| 50307 | *Tie, name=TIE_FIX_GS_TO_STEEL_END_TIEDNSET, adjust=no, type=NODE TO SURFACE, no thickness | L50308: STEEL_FIX_END_ALL_NODES_TIED_CNS_, GS_FIX-1.GS_COMPLETE_FACE |
| 50310 | *Tie, name=TIE_LOAD_GS_NEGY_TO_UHPC_END, adjust=no | L50311: GS_LOAD-1.GS_TIE_BAND_NEGY, C-C-1.UHPC_END_LOAD_ALL |
| 50313 | *Tie, name=TIE_LOAD_GS_POSY_TO_UHPC_END, adjust=no | L50314: GS_LOAD-1.GS_TIE_BAND_POSY, C-C-1.UHPC_END_LOAD_ALL |
| 50316 | *Tie, name=TIE_LOAD_GS_TO_STEEL_END_TIEDNSET, adjust=no, type=NODE TO SURFACE, no thickness | L50317: STEEL_LOAD_END_ALL_NODES_TIED_CNS_, GS_LOAD-1.GS_COMPLETE_FACE |
| 50455 | *Friction | L50456: 0.4, |
| 50457 | *Surface Behavior, pressure-overclosure=HARD |  |
| 50459 | *Friction | L50460: 0.4, |
| 50461 | *Surface Behavior, pressure-overclosure=HARD |  |
| 50466 | *Boundary | L50467: SET_GS_FIX_MIDLINE_DIRECT, 1, 1 ; L50468: SET_GS_FIX_MIDLINE_DIRECT, 2, 2 ; L50469: SET_GS_FIX_MIDLINE_DIRECT, 3, 3 ; L50470: SET_GS_FIX_MIDLINE_DIRECT, 6, 6 |
| 50472 | *Boundary | L50473: SET_GS_LOAD_MIDLINE_DIRECT, 1, 1 ; L50474: SET_GS_LOAD_MIDLINE_DIRECT, 2, 2 ; L50475: SET_GS_LOAD_MIDLINE_DIRECT, 6, 6 |
| 50477 | *Boundary | L50478: SET_NONLOADED_SIDE_PLATE_XMAX_ACTIVE, 2, 2 |
| 50480 | *Boundary | L50481: SET_NONLOADED_SIDE_PLATE_XMIN_ACTIVE, 2, 2 |
| 50487 | *Contact Inclusions | L50488: C-S-SHELL-1.SHELL_INTERFACE_X_NEG, C-C-1.UHPC_INTERFACE_X_NEG ; L50489: C-S-SHELL-1.SHELL_INTERFACE_X_POS, C-C-1.UHPC_INTERFACE_X_POS ; L50490: C-S-SHELL-1.SHELL_INTERFACE_Y_NEG, C-C-1.UHPC_INTERFACE_Y_NEG ; L50491: C-S-SHELL-1.SHELL_INTERFACE_Y_POS, C-C-1.UHPC_INTERFACE_Y_POS |
| 50492 | *Contact Property Assignment | L50493: , , PROP_STEEL_UHPC_FRICTION |
| 50509 | *Boundary, amplitude=AMP_RP_LOAD_U3 | L50510: SET_GS_LOAD_MIDLINE_DIRECT, 3, 3, 42.5 |

PBL / 外壳截面、集合、单元类型定义行：

| 行 | 关键字 | 数据 |
| --- | --- | --- |
| 127 | *Element, type=S4R |  |
| 37822 | *Element, type=S4R |  |
| 46453 | *Elset, elset=UCFT_OUTER_SHELL_FACES |  |
| 47575 | *Elset, elset=UCFT_PBL_WEB_FACES |  |
| 48257 | *Elset, elset=UCFT_PBL_EMBEDDED_INTERIOR_ELEMENTS |  |
| 48638 | *Elset, elset=UCFT_PBL_NONEMBEDDED_CONSTRAINT_EXCLUSION_ELEMENTS |  |
| 49833 | *Shell Section, elset=UCFT_OUTER_SHELL_FACES, material=STEEL_Q355, offset=SNEG | L49834: 4., 5 |
| 49836 | *Shell Section, elset=UCFT_PBL_WEB_FACES, material=STEEL_Q355 | L49837: 4., 5 |

## BH100 / FORMAL_GS_DIRECT_R02_CONTACT_RESTORED / AR=2

INP：`C:\03SCI\abaqus-UCFT test\UCFT_GS_DIRECT_R01_11MODELS\JOB_BH100_GS_DIRECT_R01.inp`

SHA256：`06c154f86807f0573ff500a1bad347c5d405027195edc6e440a91fe87f42f228`；大小 3133782 bytes；mtime Unix=1790243653。

ODB：`C:\03SCI\abaqus-UCFT test\UCFT_GS_DIRECT_R01_11MODELS\JOB_BH100_GS_DIRECT_R01.odb`；只读网格，不读场/历史；22110 / 22110 钢壳节点；最大差 4.997558634e-08 mm；PBL 集合 10800 单元与 INP 相符。对应历史审计：`C:\03SCI\abaqus-UCFT test\outputs\DIRECT_END_CREST_FORCE_AUDIT_20261010\BH100_EXTRACTION_PROVENANCE.json`。

| 肋 | 节点行区间 | 单元行区间 | PBL 截面行 | 实例行 | 根部共节点 | LOAD / FIX Tie 节点覆盖 |
| --- | --- | --- | --- | --- | --- | --- |
| TOP_04 | 12831, 30343 | 46723, 56122 | 62127 | 62139 | 201 | 7/7 ; 7/7 |
| TOP_01 | 12819, 29746 | 46123, 55522 | 62127 | 62139 | 201 | 7/7 ; 7/7 |
| TOP_03 | 12827, 30144 | 46523, 55922 | 62127 | 62139 | 201 | 7/7 ; 7/7 |
| TOP_02 | 12823, 29945 | 46323, 55722 | 62127 | 62139 | 201 | 7/7 ; 7/7 |
| BOTTOM_05 | 12851, 34124 | 48523, 54522 | 62127 | 62139 | 201 | 7/7 ; 7/7 |
| BOTTOM_09 | 12875, 34920 | 51723, 56922 | 62127 | 62139 | 201 | 7/7 ; 7/7 |
| BOTTOM_06 | 12855, 34323 | 48923, 54922 | 62127 | 62139 | 201 | 7/7 ; 7/7 |
| BOTTOM_08 | 12871, 34721 | 51323, 56522 | 62127 | 62139 | 201 | 7/7 ; 7/7 |
| BOTTOM_07 | 12859, 34522 | 49323, 55322 | 62127 | 62139 | 201 | 7/7 ; 7/7 |

装配原始数据（先平移、随后旋转，仅 GS_FIX 有变换；肋/核心无变换）：

| Instance | Part | 定义行 | 原始变换记录 |
| --- | --- | --- | --- |
| C-C-1 | c-c | 62136 | [] |
| C-S-SHELL-1 | c-s-shell | 62139 | [] |
| GS_LOAD-1 | GS_SHELL_PART | 62142 | [] |
| GS_FIX-1 | GS_SHELL_PART | 62145 | [[0.0, 0.0, 10000.0], [0.0, 0.0, 10000.0, 1.0, 0.0, 10000.0, 180.0]] |

连接和边界原始关键字证据：

| 行 | 关键字 | 数据行与内容 |
| --- | --- | --- |
| 62703 | *Embedded Element, host elset=C-C-1.UHPC_ALL_CELLS | L62704: C-S-SHELL-1.UCFT_PBL_EMBEDDED_INTERIOR_ELEMENTS |
| 62706 | *Tie, name=TIE_FIX_GS_NEGY_TO_UHPC_END, adjust=no | L62707: GS_FIX-1.GS_TIE_BAND_NEGY, C-C-1.UHPC_END_FIX_ALL |
| 62709 | *Tie, name=TIE_FIX_GS_POSY_TO_UHPC_END, adjust=no | L62710: GS_FIX-1.GS_TIE_BAND_POSY, C-C-1.UHPC_END_FIX_ALL |
| 62712 | *Tie, name=TIE_FIX_GS_TO_STEEL_END_TIEDNSET, adjust=no, type=NODE TO SURFACE, no thickness | L62713: STEEL_FIX_END_ALL_NODES_TIED_CNS_, GS_FIX-1.GS_COMPLETE_FACE |
| 62715 | *Tie, name=TIE_LOAD_GS_NEGY_TO_UHPC_END, adjust=no | L62716: GS_LOAD-1.GS_TIE_BAND_NEGY, C-C-1.UHPC_END_LOAD_ALL |
| 62718 | *Tie, name=TIE_LOAD_GS_POSY_TO_UHPC_END, adjust=no | L62719: GS_LOAD-1.GS_TIE_BAND_POSY, C-C-1.UHPC_END_LOAD_ALL |
| 62721 | *Tie, name=TIE_LOAD_GS_TO_STEEL_END_TIEDNSET, adjust=no, type=NODE TO SURFACE, no thickness | L62722: STEEL_LOAD_END_ALL_NODES_TIED_CNS_, GS_LOAD-1.GS_COMPLETE_FACE |
| 62860 | *Friction | L62861: 0.4, |
| 62862 | *Surface Behavior, pressure-overclosure=HARD |  |
| 62864 | *Friction | L62865: 0.4, |
| 62866 | *Surface Behavior, pressure-overclosure=HARD |  |
| 62871 | *Boundary | L62872: SET_GS_FIX_MIDLINE_DIRECT, 1, 1 ; L62873: SET_GS_FIX_MIDLINE_DIRECT, 2, 2 ; L62874: SET_GS_FIX_MIDLINE_DIRECT, 3, 3 ; L62875: SET_GS_FIX_MIDLINE_DIRECT, 6, 6 |
| 62877 | *Boundary | L62878: SET_GS_LOAD_MIDLINE_DIRECT, 1, 1 ; L62879: SET_GS_LOAD_MIDLINE_DIRECT, 2, 2 ; L62880: SET_GS_LOAD_MIDLINE_DIRECT, 6, 6 |
| 62882 | *Boundary | L62883: SET_NONLOADED_SIDE_PLATE_XMAX_ACTIVE, 2, 2 |
| 62885 | *Boundary | L62886: SET_NONLOADED_SIDE_PLATE_XMIN_ACTIVE, 2, 2 |
| 62892 | *Contact Inclusions | L62893: C-S-SHELL-1.SHELL_INTERFACE_X_NEG, C-C-1.UHPC_INTERFACE_X_NEG ; L62894: C-S-SHELL-1.SHELL_INTERFACE_X_POS, C-C-1.UHPC_INTERFACE_X_POS ; L62895: C-S-SHELL-1.SHELL_INTERFACE_Y_NEG, C-C-1.UHPC_INTERFACE_Y_NEG ; L62896: C-S-SHELL-1.SHELL_INTERFACE_Y_POS, C-C-1.UHPC_INTERFACE_Y_POS |
| 62897 | *Contact Property Assignment | L62898: , , PROP_STEEL_UHPC_FRICTION |
| 62914 | *Boundary, amplitude=AMP_RP_LOAD_U3 | L62915: SET_GS_LOAD_MIDLINE_DIRECT, 3, 3, 50. |

PBL / 外壳截面、集合、单元类型定义行：

| 行 | 关键字 | 数据 |
| --- | --- | --- |
| 127 | *Element, type=S4R |  |
| 46122 | *Element, type=S4R |  |
| 57628 | *Elset, elset=UCFT_OUTER_SHELL_FACES |  |
| 59122 | *Elset, elset=UCFT_PBL_WEB_FACES |  |
| 60030 | *Elset, elset=UCFT_PBL_EMBEDDED_INTERIOR_ELEMENTS |  |
| 60538 | *Elset, elset=UCFT_PBL_NONEMBEDDED_CONSTRAINT_EXCLUSION_ELEMENTS |  |
| 62124 | *Shell Section, elset=UCFT_OUTER_SHELL_FACES, material=STEEL_Q355, offset=SNEG | L62125: 4., 5 |
| 62127 | *Shell Section, elset=UCFT_PBL_WEB_FACES, material=STEEL_Q355 | L62128: 4., 5 |

## BH005 / HISTORICAL_LB3_RP_R01 / AR=3

INP：`C:\03SCI\abaqus-UCFT test\_codex_lb3_git_worktree\semantic_v2\40_execution\model_governance\20260921_ucft_lb3_cleanup\BH005_LB3_EXPLICIT_R01.inp`

SHA256：`7ca51b6319366f81044ffd583dd66aa28624d1aca3ba572bc23b49b6a07b62ce`；大小 1894660 bytes；mtime Unix=1789926394。

此版只用 INP 作为主证据，未读取历史 ODB；不是正式 DIRECT。完全相同 SHA 的重复来源（不是另一套模型）：

- `C:\03SCI\abaqus-UCFT test\_codex_lb3_git_worktree\semantic_v2\40_execution\model_governance\20260921_ucft_lb3_cleanup\COMPUTATION_FILES\BH005_LB3_EXPLICIT_R01.inp`

| 肋 | 节点行区间 | 单元行区间 | PBL 截面行 | 实例行 | 根部共节点 | LOAD / FIX Tie 节点覆盖 |
| --- | --- | --- | --- | --- | --- | --- |
| TOP_04 | 20212, 27977 | 31467, 36709 | 41454 | 41469 | 76 | 7/7 ; 7/7 |
| TOP_01 | 20206, 27536 | 31317, 36706 | 41454 | 41469 | 76 | 7/7 ; 7/7 |
| TOP_03 | 20210, 27193 | 31417, 36708 | 41454 | 41469 | 76 | 7/7 ; 7/7 |
| TOP_02 | 20208, 26850 | 31367, 36707 | 41454 | 41469 | 76 | 7/7 ; 7/7 |
| BOTTOM_05 | 20218, 28369 | 31717, 36703 | 41454 | 41469 | 76 | 7/7 ; 7/7 |
| BOTTOM_09 | 20230, 28565 | 32117, 36711 | 41454 | 41469 | 76 | 7/7 ; 7/7 |
| BOTTOM_06 | 20220, 28418 | 31767, 36704 | 41454 | 41469 | 76 | 7/7 ; 7/7 |
| BOTTOM_08 | 20228, 28516 | 32067, 36710 | 41454 | 41469 | 76 | 7/7 ; 7/7 |
| BOTTOM_07 | 20222, 28467 | 31817, 36705 | 41454 | 41469 | 76 | 7/7 ; 7/7 |

装配原始数据（先平移、随后旋转，仅 GS_FIX 有变换；肋/核心无变换）：

| Instance | Part | 定义行 | 原始变换记录 |
| --- | --- | --- | --- |
| C-C-1 | c-c | 41466 | [] |
| C-S-SHELL-1 | c-s-shell | 41469 | [] |
| GS_LOAD-1 | GS_SHELL_PART | 41472 | [] |
| GS_FIX-1 | GS_SHELL_PART | 41475 | [[0.0, 0.0, 750.0], [0.0, 0.0, 750.0, 1.0, 0.0, 750.0, 180.0]] |

连接和边界原始关键字证据：

| 行 | 关键字 | 数据行与内容 |
| --- | --- | --- |
| 41595 | *Coupling, constraint name=COUP_RP_FIX_TO_GS_MIDLINE, ref node=RP_FIX_GS, surface=GS_FIX-1.GS_MIDLINE |  |
| 41598 | *Coupling, constraint name=COUP_RP_LOAD_TO_GS_MIDLINE, ref node=RP_LOAD_GS, surface=GS_LOAD-1.GS_MIDLINE |  |
| 41601 | *Embedded Element, host elset=C-C-1.UHPC_ALL_CELLS | L41602: C-S-SHELL-1.UCFT_PBL_EMBEDDED_INTERIOR_ELEMENTS |
| 41604 | *Tie, name=TIE_FIX_GS_TO_STEEL_END, adjust=no, type=NODE TO SURFACE, no thickness | L41605: STEEL_END_ALL_NODES_TIED_FIX_CNS_, GS_FIX-1.GS_COMPLETE_FACE |
| 41607 | *Tie, name=TIE_GS_FIX_TO_UHPC_END, adjust=no, no thickness | L41608: C-C-1.UHPC_END_FIX_ALL, GS_FIX-1.GS_COMPLETE_FACE |
| 41610 | *Tie, name=TIE_GS_LOAD_TO_UHPC_END, adjust=no, no thickness | L41611: C-C-1.UHPC_END_LOAD_ALL, GS_LOAD-1.GS_COMPLETE_FACE |
| 41613 | *Tie, name=TIE_LOAD_GS_TO_STEEL_END, adjust=no, type=NODE TO SURFACE, no thickness | L41614: STEEL_END_ALL_NODES_TIED_LOAD_CNS_, GS_LOAD-1.GS_COMPLETE_FACE |
| 41752 | *Friction | L41753: 0.4, |
| 41754 | *Surface Behavior, pressure-overclosure=HARD |  |
| 41759 | *Boundary | L41760: SET_NONLOADED_SIDE_PLATE_XMAX_ACTIVE, 2, 2 |
| 41762 | *Boundary | L41763: SET_NONLOADED_SIDE_PLATE_XMIN_ACTIVE, 2, 2 |
| 41765 | *Boundary | L41766: RP_FIX_GS, 1, 1 ; L41767: RP_FIX_GS, 2, 2 ; L41768: RP_FIX_GS, 3, 3 ; L41769: RP_FIX_GS, 6, 6 |
| 41771 | *Boundary | L41772: RP_LOAD_GS, 1, 1 ; L41773: RP_LOAD_GS, 2, 2 ; L41774: RP_LOAD_GS, 6, 6 |
| 41780 | *Contact Inclusions | L41781: C-S-SHELL-1.SHELL_INTERFACE_X_NEG, C-C-1.UHPC_INTERFACE_X_NEG ; L41782: C-S-SHELL-1.SHELL_INTERFACE_X_POS, C-C-1.UHPC_INTERFACE_X_POS ; L41783: C-S-SHELL-1.SHELL_INTERFACE_Y_NEG, C-C-1.UHPC_INTERFACE_Y_NEG ; L41784: C-S-SHELL-1.SHELL_INTERFACE_Y_POS, C-C-1.UHPC_INTERFACE_Y_POS |
| 41785 | *Contact Property Assignment | L41786: , , PROP_STEEL_UHPC_FRICTION |
| 41799 | *Boundary, amplitude=AMP_RP_LOAD_U3 | L41800: RP_LOAD_GS, 3, 3,3.75 |

PBL / 外壳截面、集合、单元类型定义行：

| 行 | 关键字 | 数据 |
| --- | --- | --- |
| 120 | *Element, type=S4R |  |
| 28566 | *Element, type=S4R |  |
| 39835 | *Elset, elset=UCFT_OUTER_SHELL_FACES |  |
| 40400 | *Elset, elset=UCFT_PBL_WEB_FACES |  |
| 40655 | *Elset, elset=UCFT_PBL_EMBEDDED_INTERIOR_ELEMENTS |  |
| 40859 | *Elset, elset=UCFT_PBL_NONEMBEDDED_CONSTRAINT_EXCLUSION_ELEMENTS |  |
| 41454 | *Shell Section, elset=UCFT_PBL_WEB_FACES, material=STEEL_Q355 | L41455: 4., 5 |
| 41457 | *Shell Section, elset=UCFT_OUTER_SHELL_FACES, material=STEEL_Q355, offset=SNEG | L41458: 4., 5 |

## BH010 / HISTORICAL_LB3_RP_R01 / AR=3

INP：`C:\03SCI\abaqus-UCFT test\_codex_lb3_git_worktree\semantic_v2\40_execution\model_governance\20260921_ucft_lb3_cleanup\BH010_LB3_EXPLICIT_R01.inp`

SHA256：`4342b238a60544afb2610f52a200535cc80e9cd97cffd9f1568008305c3a5696`；大小 1897384 bytes；mtime Unix=1789926395。

此版只用 INP 作为主证据，未读取历史 ODB；不是正式 DIRECT。完全相同 SHA 的重复来源（不是另一套模型）：

- `C:\03SCI\abaqus-UCFT test\_codex_lb3_git_worktree\semantic_v2\40_execution\model_governance\20260921_ucft_lb3_cleanup\COMPUTATION_FILES\BH010_LB3_EXPLICIT_R01.inp`

| 肋 | 节点行区间 | 单元行区间 | PBL 截面行 | 实例行 | 根部共节点 | LOAD / FIX Tie 节点覆盖 |
| --- | --- | --- | --- | --- | --- | --- |
| TOP_04 | 20212, 27977 | 31467, 36709 | 41454 | 41469 | 76 | 7/7 ; 7/7 |
| TOP_01 | 20206, 27536 | 31317, 36706 | 41454 | 41469 | 76 | 7/7 ; 7/7 |
| TOP_03 | 20210, 27193 | 31417, 36708 | 41454 | 41469 | 76 | 7/7 ; 7/7 |
| TOP_02 | 20208, 26850 | 31367, 36707 | 41454 | 41469 | 76 | 7/7 ; 7/7 |
| BOTTOM_05 | 20218, 28369 | 31717, 36703 | 41454 | 41469 | 76 | 7/7 ; 7/7 |
| BOTTOM_09 | 20230, 28565 | 32117, 36711 | 41454 | 41469 | 76 | 7/7 ; 7/7 |
| BOTTOM_06 | 20220, 28418 | 31767, 36704 | 41454 | 41469 | 76 | 7/7 ; 7/7 |
| BOTTOM_08 | 20228, 28516 | 32067, 36710 | 41454 | 41469 | 76 | 7/7 ; 7/7 |
| BOTTOM_07 | 20222, 28467 | 31817, 36705 | 41454 | 41469 | 76 | 7/7 ; 7/7 |

装配原始数据（先平移、随后旋转，仅 GS_FIX 有变换；肋/核心无变换）：

| Instance | Part | 定义行 | 原始变换记录 |
| --- | --- | --- | --- |
| C-C-1 | c-c | 41466 | [] |
| C-S-SHELL-1 | c-s-shell | 41469 | [] |
| GS_LOAD-1 | GS_SHELL_PART | 41472 | [] |
| GS_FIX-1 | GS_SHELL_PART | 41475 | [[0.0, 0.0, 1500.0], [0.0, 0.0, 1500.0, 1.0, 0.0, 1500.0, 180.0]] |

连接和边界原始关键字证据：

| 行 | 关键字 | 数据行与内容 |
| --- | --- | --- |
| 41595 | *Coupling, constraint name=COUP_RP_FIX_TO_GS_MIDLINE, ref node=RP_FIX_GS, surface=GS_FIX-1.GS_MIDLINE |  |
| 41598 | *Coupling, constraint name=COUP_RP_LOAD_TO_GS_MIDLINE, ref node=RP_LOAD_GS, surface=GS_LOAD-1.GS_MIDLINE |  |
| 41601 | *Embedded Element, host elset=C-C-1.UHPC_ALL_CELLS | L41602: C-S-SHELL-1.UCFT_PBL_EMBEDDED_INTERIOR_ELEMENTS |
| 41604 | *Tie, name=TIE_FIX_GS_TO_STEEL_END, adjust=no, type=NODE TO SURFACE, no thickness | L41605: STEEL_END_ALL_NODES_TIED_FIX_CNS_, GS_FIX-1.GS_COMPLETE_FACE |
| 41607 | *Tie, name=TIE_GS_FIX_TO_UHPC_END, adjust=no, no thickness | L41608: C-C-1.UHPC_END_FIX_ALL, GS_FIX-1.GS_COMPLETE_FACE |
| 41610 | *Tie, name=TIE_GS_LOAD_TO_UHPC_END, adjust=no, no thickness | L41611: C-C-1.UHPC_END_LOAD_ALL, GS_LOAD-1.GS_COMPLETE_FACE |
| 41613 | *Tie, name=TIE_LOAD_GS_TO_STEEL_END, adjust=no, type=NODE TO SURFACE, no thickness | L41614: STEEL_END_ALL_NODES_TIED_LOAD_CNS_, GS_LOAD-1.GS_COMPLETE_FACE |
| 41752 | *Friction | L41753: 0.4, |
| 41754 | *Surface Behavior, pressure-overclosure=HARD |  |
| 41759 | *Boundary | L41760: SET_NONLOADED_SIDE_PLATE_XMAX_ACTIVE, 2, 2 |
| 41762 | *Boundary | L41763: SET_NONLOADED_SIDE_PLATE_XMIN_ACTIVE, 2, 2 |
| 41765 | *Boundary | L41766: RP_FIX_GS, 1, 1 ; L41767: RP_FIX_GS, 2, 2 ; L41768: RP_FIX_GS, 3, 3 ; L41769: RP_FIX_GS, 6, 6 |
| 41771 | *Boundary | L41772: RP_LOAD_GS, 1, 1 ; L41773: RP_LOAD_GS, 2, 2 ; L41774: RP_LOAD_GS, 6, 6 |
| 41780 | *Contact Inclusions | L41781: C-S-SHELL-1.SHELL_INTERFACE_X_NEG, C-C-1.UHPC_INTERFACE_X_NEG ; L41782: C-S-SHELL-1.SHELL_INTERFACE_X_POS, C-C-1.UHPC_INTERFACE_X_POS ; L41783: C-S-SHELL-1.SHELL_INTERFACE_Y_NEG, C-C-1.UHPC_INTERFACE_Y_NEG ; L41784: C-S-SHELL-1.SHELL_INTERFACE_Y_POS, C-C-1.UHPC_INTERFACE_Y_POS |
| 41785 | *Contact Property Assignment | L41786: , , PROP_STEEL_UHPC_FRICTION |
| 41799 | *Boundary, amplitude=AMP_RP_LOAD_U3 | L41800: RP_LOAD_GS, 3, 3,7.5 |

PBL / 外壳截面、集合、单元类型定义行：

| 行 | 关键字 | 数据 |
| --- | --- | --- |
| 120 | *Element, type=S4R |  |
| 28566 | *Element, type=S4R |  |
| 39835 | *Elset, elset=UCFT_OUTER_SHELL_FACES |  |
| 40400 | *Elset, elset=UCFT_PBL_WEB_FACES |  |
| 40655 | *Elset, elset=UCFT_PBL_EMBEDDED_INTERIOR_ELEMENTS |  |
| 40859 | *Elset, elset=UCFT_PBL_NONEMBEDDED_CONSTRAINT_EXCLUSION_ELEMENTS |  |
| 41454 | *Shell Section, elset=UCFT_PBL_WEB_FACES, material=STEEL_Q355 | L41455: 4., 5 |
| 41457 | *Shell Section, elset=UCFT_OUTER_SHELL_FACES, material=STEEL_Q355, offset=SNEG | L41458: 4., 5 |

## BH020 / HISTORICAL_LB3_RP_R01 / AR=3

INP：`C:\03SCI\abaqus-UCFT test\_codex_lb3_git_worktree\semantic_v2\40_execution\model_governance\20260921_ucft_lb3_cleanup\BH020_LB3_EXPLICIT_R01.inp`

SHA256：`abcdeb2a5f042b3a123c52b808ae123fc55391c6bfb0a65bfb3546c679c06d7f`；大小 1893371 bytes；mtime Unix=1789926395。

此版只用 INP 作为主证据，未读取历史 ODB；不是正式 DIRECT。完全相同 SHA 的重复来源（不是另一套模型）：

- `C:\03SCI\abaqus-UCFT test\_codex_lb3_git_worktree\semantic_v2\40_execution\model_governance\20260921_ucft_lb3_cleanup\COMPUTATION_FILES\BH020_LB3_EXPLICIT_R01.inp`

| 肋 | 节点行区间 | 单元行区间 | PBL 截面行 | 实例行 | 根部共节点 | LOAD / FIX Tie 节点覆盖 |
| --- | --- | --- | --- | --- | --- | --- |
| TOP_04 | 20212, 27977 | 31467, 36709 | 41454 | 41469 | 76 | 7/7 ; 7/7 |
| TOP_01 | 20206, 27536 | 31317, 36706 | 41454 | 41469 | 76 | 7/7 ; 7/7 |
| TOP_03 | 20210, 27193 | 31417, 36708 | 41454 | 41469 | 76 | 7/7 ; 7/7 |
| TOP_02 | 20208, 26850 | 31367, 36707 | 41454 | 41469 | 76 | 7/7 ; 7/7 |
| BOTTOM_05 | 20218, 28369 | 31717, 36703 | 41454 | 41469 | 76 | 7/7 ; 7/7 |
| BOTTOM_09 | 20230, 28565 | 32117, 36711 | 41454 | 41469 | 76 | 7/7 ; 7/7 |
| BOTTOM_06 | 20220, 28418 | 31767, 36704 | 41454 | 41469 | 76 | 7/7 ; 7/7 |
| BOTTOM_08 | 20228, 28516 | 32067, 36710 | 41454 | 41469 | 76 | 7/7 ; 7/7 |
| BOTTOM_07 | 20222, 28467 | 31817, 36705 | 41454 | 41469 | 76 | 7/7 ; 7/7 |

装配原始数据（先平移、随后旋转，仅 GS_FIX 有变换；肋/核心无变换）：

| Instance | Part | 定义行 | 原始变换记录 |
| --- | --- | --- | --- |
| C-C-1 | c-c | 41466 | [] |
| C-S-SHELL-1 | c-s-shell | 41469 | [] |
| GS_LOAD-1 | GS_SHELL_PART | 41472 | [] |
| GS_FIX-1 | GS_SHELL_PART | 41475 | [[0.0, 0.0, 3000.0], [0.0, 0.0, 3000.0, 1.0, 0.0, 3000.0, 180.0]] |

连接和边界原始关键字证据：

| 行 | 关键字 | 数据行与内容 |
| --- | --- | --- |
| 41595 | *Coupling, constraint name=COUP_RP_FIX_TO_GS_MIDLINE, ref node=RP_FIX_GS, surface=GS_FIX-1.GS_MIDLINE |  |
| 41598 | *Coupling, constraint name=COUP_RP_LOAD_TO_GS_MIDLINE, ref node=RP_LOAD_GS, surface=GS_LOAD-1.GS_MIDLINE |  |
| 41601 | *Embedded Element, host elset=C-C-1.UHPC_ALL_CELLS | L41602: C-S-SHELL-1.UCFT_PBL_EMBEDDED_INTERIOR_ELEMENTS |
| 41604 | *Tie, name=TIE_FIX_GS_TO_STEEL_END, adjust=no, type=NODE TO SURFACE, no thickness | L41605: STEEL_END_ALL_NODES_TIED_FIX_CNS_, GS_FIX-1.GS_COMPLETE_FACE |
| 41607 | *Tie, name=TIE_GS_FIX_TO_UHPC_END, adjust=no, no thickness | L41608: C-C-1.UHPC_END_FIX_ALL, GS_FIX-1.GS_COMPLETE_FACE |
| 41610 | *Tie, name=TIE_GS_LOAD_TO_UHPC_END, adjust=no, no thickness | L41611: C-C-1.UHPC_END_LOAD_ALL, GS_LOAD-1.GS_COMPLETE_FACE |
| 41613 | *Tie, name=TIE_LOAD_GS_TO_STEEL_END, adjust=no, type=NODE TO SURFACE, no thickness | L41614: STEEL_END_ALL_NODES_TIED_LOAD_CNS_, GS_LOAD-1.GS_COMPLETE_FACE |
| 41752 | *Friction | L41753: 0.4, |
| 41754 | *Surface Behavior, pressure-overclosure=HARD |  |
| 41759 | *Boundary | L41760: SET_NONLOADED_SIDE_PLATE_XMAX_ACTIVE, 2, 2 |
| 41762 | *Boundary | L41763: SET_NONLOADED_SIDE_PLATE_XMIN_ACTIVE, 2, 2 |
| 41765 | *Boundary | L41766: RP_FIX_GS, 1, 1 ; L41767: RP_FIX_GS, 2, 2 ; L41768: RP_FIX_GS, 3, 3 ; L41769: RP_FIX_GS, 6, 6 |
| 41771 | *Boundary | L41772: RP_LOAD_GS, 1, 1 ; L41773: RP_LOAD_GS, 2, 2 ; L41774: RP_LOAD_GS, 6, 6 |
| 41780 | *Contact Inclusions | L41781: C-S-SHELL-1.SHELL_INTERFACE_X_NEG, C-C-1.UHPC_INTERFACE_X_NEG ; L41782: C-S-SHELL-1.SHELL_INTERFACE_X_POS, C-C-1.UHPC_INTERFACE_X_POS ; L41783: C-S-SHELL-1.SHELL_INTERFACE_Y_NEG, C-C-1.UHPC_INTERFACE_Y_NEG ; L41784: C-S-SHELL-1.SHELL_INTERFACE_Y_POS, C-C-1.UHPC_INTERFACE_Y_POS |
| 41785 | *Contact Property Assignment | L41786: , , PROP_STEEL_UHPC_FRICTION |
| 41799 | *Boundary, amplitude=AMP_RP_LOAD_U3 | L41800: RP_LOAD_GS, 3, 3,15 |

PBL / 外壳截面、集合、单元类型定义行：

| 行 | 关键字 | 数据 |
| --- | --- | --- |
| 120 | *Element, type=S4R |  |
| 28566 | *Element, type=S4R |  |
| 39835 | *Elset, elset=UCFT_OUTER_SHELL_FACES |  |
| 40400 | *Elset, elset=UCFT_PBL_WEB_FACES |  |
| 40655 | *Elset, elset=UCFT_PBL_EMBEDDED_INTERIOR_ELEMENTS |  |
| 40859 | *Elset, elset=UCFT_PBL_NONEMBEDDED_CONSTRAINT_EXCLUSION_ELEMENTS |  |
| 41454 | *Shell Section, elset=UCFT_PBL_WEB_FACES, material=STEEL_Q355 | L41455: 4., 5 |
| 41457 | *Shell Section, elset=UCFT_OUTER_SHELL_FACES, material=STEEL_Q355, offset=SNEG | L41458: 4., 5 |

## BH032 / HISTORICAL_LB3_RP_R01 / AR=3

INP：`C:\03SCI\abaqus-UCFT test\_codex_lb3_git_worktree\semantic_v2\40_execution\model_governance\20260921_ucft_lb3_cleanup\BH032_LB3_EXPLICIT_R01.inp`

SHA256：`22b7382b07bf8ce3c3ebbc345664711d731202916ae98a096d5dbf36e39a84dc`；大小 1884973 bytes；mtime Unix=1789926395。

此版只用 INP 作为主证据，未读取历史 ODB；不是正式 DIRECT。完全相同 SHA 的重复来源（不是另一套模型）：

- `C:\03SCI\abaqus-UCFT test\_codex_lb3_git_worktree\semantic_v2\40_execution\model_governance\20260921_ucft_lb3_cleanup\COMPUTATION_FILES\BH032_LB3_EXPLICIT_R01.inp`

| 肋 | 节点行区间 | 单元行区间 | PBL 截面行 | 实例行 | 根部共节点 | LOAD / FIX Tie 节点覆盖 |
| --- | --- | --- | --- | --- | --- | --- |
| TOP_04 | 20212, 27977 | 31467, 36709 | 41454 | 41469 | 76 | 7/7 ; 7/7 |
| TOP_01 | 20206, 27536 | 31317, 36706 | 41454 | 41469 | 76 | 7/7 ; 7/7 |
| TOP_03 | 20210, 27193 | 31417, 36708 | 41454 | 41469 | 76 | 7/7 ; 7/7 |
| TOP_02 | 20208, 26850 | 31367, 36707 | 41454 | 41469 | 76 | 7/7 ; 7/7 |
| BOTTOM_05 | 20218, 28369 | 31717, 36703 | 41454 | 41469 | 76 | 7/7 ; 7/7 |
| BOTTOM_09 | 20230, 28565 | 32117, 36711 | 41454 | 41469 | 76 | 7/7 ; 7/7 |
| BOTTOM_06 | 20220, 28418 | 31767, 36704 | 41454 | 41469 | 76 | 7/7 ; 7/7 |
| BOTTOM_08 | 20228, 28516 | 32067, 36710 | 41454 | 41469 | 76 | 7/7 ; 7/7 |
| BOTTOM_07 | 20222, 28467 | 31817, 36705 | 41454 | 41469 | 76 | 7/7 ; 7/7 |

装配原始数据（先平移、随后旋转，仅 GS_FIX 有变换；肋/核心无变换）：

| Instance | Part | 定义行 | 原始变换记录 |
| --- | --- | --- | --- |
| C-C-1 | c-c | 41466 | [] |
| C-S-SHELL-1 | c-s-shell | 41469 | [] |
| GS_LOAD-1 | GS_SHELL_PART | 41472 | [] |
| GS_FIX-1 | GS_SHELL_PART | 41475 | [[0.0, 0.0, 4800.0], [0.0, 0.0, 4800.0, 1.0, 0.0, 4800.0, 180.0]] |

连接和边界原始关键字证据：

| 行 | 关键字 | 数据行与内容 |
| --- | --- | --- |
| 41595 | *Coupling, constraint name=COUP_RP_FIX_TO_GS_MIDLINE, ref node=RP_FIX_GS, surface=GS_FIX-1.GS_MIDLINE |  |
| 41598 | *Coupling, constraint name=COUP_RP_LOAD_TO_GS_MIDLINE, ref node=RP_LOAD_GS, surface=GS_LOAD-1.GS_MIDLINE |  |
| 41601 | *Embedded Element, host elset=C-C-1.UHPC_ALL_CELLS | L41602: C-S-SHELL-1.UCFT_PBL_EMBEDDED_INTERIOR_ELEMENTS |
| 41604 | *Tie, name=TIE_FIX_GS_TO_STEEL_END, adjust=no, type=NODE TO SURFACE, no thickness | L41605: STEEL_END_ALL_NODES_TIED_FIX_CNS_, GS_FIX-1.GS_COMPLETE_FACE |
| 41607 | *Tie, name=TIE_GS_FIX_TO_UHPC_END, adjust=no, no thickness | L41608: C-C-1.UHPC_END_FIX_ALL, GS_FIX-1.GS_COMPLETE_FACE |
| 41610 | *Tie, name=TIE_GS_LOAD_TO_UHPC_END, adjust=no, no thickness | L41611: C-C-1.UHPC_END_LOAD_ALL, GS_LOAD-1.GS_COMPLETE_FACE |
| 41613 | *Tie, name=TIE_LOAD_GS_TO_STEEL_END, adjust=no, type=NODE TO SURFACE, no thickness | L41614: STEEL_END_ALL_NODES_TIED_LOAD_CNS_, GS_LOAD-1.GS_COMPLETE_FACE |
| 41752 | *Friction | L41753: 0.4, |
| 41754 | *Surface Behavior, pressure-overclosure=HARD |  |
| 41759 | *Boundary | L41760: SET_NONLOADED_SIDE_PLATE_XMAX_ACTIVE, 2, 2 |
| 41762 | *Boundary | L41763: SET_NONLOADED_SIDE_PLATE_XMIN_ACTIVE, 2, 2 |
| 41765 | *Boundary | L41766: RP_FIX_GS, 1, 1 ; L41767: RP_FIX_GS, 2, 2 ; L41768: RP_FIX_GS, 3, 3 ; L41769: RP_FIX_GS, 6, 6 |
| 41771 | *Boundary | L41772: RP_LOAD_GS, 1, 1 ; L41773: RP_LOAD_GS, 2, 2 ; L41774: RP_LOAD_GS, 6, 6 |
| 41780 | *Contact Inclusions | L41781: C-S-SHELL-1.SHELL_INTERFACE_X_NEG, C-C-1.UHPC_INTERFACE_X_NEG ; L41782: C-S-SHELL-1.SHELL_INTERFACE_X_POS, C-C-1.UHPC_INTERFACE_X_POS ; L41783: C-S-SHELL-1.SHELL_INTERFACE_Y_NEG, C-C-1.UHPC_INTERFACE_Y_NEG ; L41784: C-S-SHELL-1.SHELL_INTERFACE_Y_POS, C-C-1.UHPC_INTERFACE_Y_POS |
| 41785 | *Contact Property Assignment | L41786: , , PROP_STEEL_UHPC_FRICTION |
| 41799 | *Boundary, amplitude=AMP_RP_LOAD_U3 | L41800: RP_LOAD_GS, 3, 3,24 |

PBL / 外壳截面、集合、单元类型定义行：

| 行 | 关键字 | 数据 |
| --- | --- | --- |
| 120 | *Element, type=S4R |  |
| 28566 | *Element, type=S4R |  |
| 39835 | *Elset, elset=UCFT_OUTER_SHELL_FACES |  |
| 40400 | *Elset, elset=UCFT_PBL_WEB_FACES |  |
| 40655 | *Elset, elset=UCFT_PBL_EMBEDDED_INTERIOR_ELEMENTS |  |
| 40859 | *Elset, elset=UCFT_PBL_NONEMBEDDED_CONSTRAINT_EXCLUSION_ELEMENTS |  |
| 41454 | *Shell Section, elset=UCFT_PBL_WEB_FACES, material=STEEL_Q355 | L41455: 4., 5 |
| 41457 | *Shell Section, elset=UCFT_OUTER_SHELL_FACES, material=STEEL_Q355, offset=SNEG | L41458: 4., 5 |

## BH050 / HISTORICAL_LB3_RP_R01 / AR=3

INP：`C:\03SCI\abaqus-UCFT test\_codex_lb3_git_worktree\semantic_v2\40_execution\model_governance\20260921_ucft_lb3_cleanup\BH050_LB3_EXPLICIT_R01.inp`

SHA256：`af178cab4fe82659af31f2ec806aa8eb2758b5a1e8af98790f004d4e755e8734`；大小 2851446 bytes；mtime Unix=1789926396。

此版只用 INP 作为主证据，未读取历史 ODB；不是正式 DIRECT。完全相同 SHA 的重复来源（不是另一套模型）：

- `C:\03SCI\abaqus-UCFT test\_codex_lb3_git_worktree\semantic_v2\40_execution\model_governance\20260921_ucft_lb3_cleanup\COMPUTATION_FILES\BH050_LB3_EXPLICIT_R01.inp`

| 肋 | 节点行区间 | 单元行区间 | PBL 截面行 | 实例行 | 根部共节点 | LOAD / FIX Tie 节点覆盖 |
| --- | --- | --- | --- | --- | --- | --- |
| TOP_04 | 20211, 35626 | 42616, 53158 | 62554 | 62569 | 151 | 7/7 ; 7/7 |
| TOP_01 | 20205, 34735 | 42316, 53155 | 62554 | 62569 | 151 | 7/7 ; 7/7 |
| TOP_03 | 20209, 34042 | 42516, 53157 | 62554 | 62569 | 151 | 7/7 ; 7/7 |
| TOP_02 | 20207, 33349 | 42416, 53156 | 62554 | 62569 | 151 | 7/7 ; 7/7 |
| BOTTOM_05 | 20217, 36418 | 43116, 53152 | 62554 | 62569 | 151 | 7/7 ; 7/7 |
| BOTTOM_09 | 20229, 36814 | 43916, 53160 | 62554 | 62569 | 151 | 7/7 ; 7/7 |
| BOTTOM_06 | 20219, 36517 | 43216, 53153 | 62554 | 62569 | 151 | 7/7 ; 7/7 |
| BOTTOM_08 | 20227, 36715 | 43816, 53159 | 62554 | 62569 | 151 | 7/7 ; 7/7 |
| BOTTOM_07 | 20221, 36616 | 43316, 53154 | 62554 | 62569 | 151 | 7/7 ; 7/7 |

装配原始数据（先平移、随后旋转，仅 GS_FIX 有变换；肋/核心无变换）：

| Instance | Part | 定义行 | 原始变换记录 |
| --- | --- | --- | --- |
| C-C-1 | c-c | 62566 | [] |
| C-S-SHELL-1 | c-s-shell | 62569 | [] |
| GS_LOAD-1 | GS_SHELL_PART | 62572 | [] |
| GS_FIX-1 | GS_SHELL_PART | 62575 | [[0.0, 0.0, 7500.0], [0.0, 0.0, 7500.0, 1.0, 0.0, 7500.0, 180.0]] |

连接和边界原始关键字证据：

| 行 | 关键字 | 数据行与内容 |
| --- | --- | --- |
| 62779 | *Coupling, constraint name=COUP_RP_FIX_TO_GS_MIDLINE, ref node=RP_FIX_GS, surface=GS_FIX-1.GS_MIDLINE |  |
| 62782 | *Coupling, constraint name=COUP_RP_LOAD_TO_GS_MIDLINE, ref node=RP_LOAD_GS, surface=GS_LOAD-1.GS_MIDLINE |  |
| 62785 | *Embedded Element, host elset=C-C-1.UHPC_ALL_CELLS | L62786: C-S-SHELL-1.UCFT_PBL_EMBEDDED_INTERIOR_ELEMENTS |
| 62788 | *Tie, name=TIE_FIX_GS_TO_STEEL_END, adjust=no, type=NODE TO SURFACE, no thickness | L62789: STEEL_END_ALL_NODES_TIED_FIX_CNS_, GS_FIX-1.GS_COMPLETE_FACE |
| 62791 | *Tie, name=TIE_GS_FIX_TO_UHPC_END, adjust=no, no thickness | L62792: C-C-1.UHPC_END_FIX_ALL, GS_FIX-1.GS_COMPLETE_FACE |
| 62794 | *Tie, name=TIE_GS_LOAD_TO_UHPC_END, adjust=no, no thickness | L62795: C-C-1.UHPC_END_LOAD_ALL, GS_LOAD-1.GS_COMPLETE_FACE |
| 62797 | *Tie, name=TIE_LOAD_GS_TO_STEEL_END, adjust=no, type=NODE TO SURFACE, no thickness | L62798: STEEL_END_ALL_NODES_TIED_LOAD_CNS_, GS_LOAD-1.GS_COMPLETE_FACE |
| 62936 | *Friction | L62937: 0.4, |
| 62938 | *Surface Behavior, pressure-overclosure=HARD |  |
| 62943 | *Boundary | L62944: SET_NONLOADED_SIDE_PLATE_XMAX_ACTIVE, 2, 2 |
| 62946 | *Boundary | L62947: SET_NONLOADED_SIDE_PLATE_XMIN_ACTIVE, 2, 2 |
| 62949 | *Boundary | L62950: RP_FIX_GS, 1, 1 ; L62951: RP_FIX_GS, 2, 2 ; L62952: RP_FIX_GS, 3, 3 ; L62953: RP_FIX_GS, 6, 6 |
| 62955 | *Boundary | L62956: RP_LOAD_GS, 1, 1 ; L62957: RP_LOAD_GS, 2, 2 ; L62958: RP_LOAD_GS, 6, 6 |
| 62964 | *Contact Inclusions | L62965: C-S-SHELL-1.SHELL_INTERFACE_X_NEG, C-C-1.UHPC_INTERFACE_X_NEG ; L62966: C-S-SHELL-1.SHELL_INTERFACE_X_POS, C-C-1.UHPC_INTERFACE_X_POS ; L62967: C-S-SHELL-1.SHELL_INTERFACE_Y_NEG, C-C-1.UHPC_INTERFACE_Y_NEG ; L62968: C-S-SHELL-1.SHELL_INTERFACE_Y_POS, C-C-1.UHPC_INTERFACE_Y_POS |
| 62969 | *Contact Property Assignment | L62970: , , PROP_STEEL_UHPC_FRICTION |
| 62986 | *Boundary, amplitude=AMP_RP_LOAD_U3 | L62987: RP_LOAD_GS, 3, 3,37.5 |

PBL / 外壳截面、集合、单元类型定义行：

| 行 | 关键字 | 数据 |
| --- | --- | --- |
| 119 | *Element, type=S4R |  |
| 36815 | *Element, type=S4R |  |
| 59347 | *Elset, elset=UCFT_OUTER_SHELL_FACES |  |
| 60469 | *Elset, elset=UCFT_PBL_WEB_FACES |  |
| 60977 | *Elset, elset=UCFT_PBL_EMBEDDED_INTERIOR_ELEMENTS |  |
| 61348 | *Elset, elset=UCFT_PBL_NONEMBEDDED_CONSTRAINT_EXCLUSION_ELEMENTS |  |
| 62554 | *Shell Section, elset=UCFT_PBL_WEB_FACES, material=STEEL_Q355 | L62555: 4., 5 |
| 62557 | *Shell Section, elset=UCFT_OUTER_SHELL_FACES, material=STEEL_Q355, offset=SNEG | L62558: 4., 5 |

## BH060 / HISTORICAL_LB3_RP_R01 / AR=3

INP：`C:\03SCI\abaqus-UCFT test\_codex_lb3_git_worktree\semantic_v2\40_execution\model_governance\20260921_ucft_lb3_cleanup\BH060_LB3_EXPLICIT_R01.inp`

SHA256：`b072f0f4812ffb58b7ec1c834e667a2008fb1ec77abf0670043e3d68fcd4587d`；大小 3152927 bytes；mtime Unix=1789926396。

此版只用 INP 作为主证据，未读取历史 ODB；不是正式 DIRECT。完全相同 SHA 的重复来源（不是另一套模型）：

- `C:\03SCI\abaqus-UCFT test\_codex_lb3_git_worktree\semantic_v2\40_execution\model_governance\20260921_ucft_lb3_cleanup\COMPUTATION_FILES\BH060_LB3_EXPLICIT_R01.inp`

| 肋 | 节点行区间 | 单元行区间 | PBL 截面行 | 实例行 | 根部共节点 | LOAD / FIX Tie 节点覆盖 |
| --- | --- | --- | --- | --- | --- | --- |
| TOP_04 | 20278, 34600 | 48039, 58479 | 63832 | 63844 | 151 | 7/7 ; 7/7 |
| TOP_01 | 20272, 34303 | 48036, 58179 | 63832 | 63844 | 151 | 7/7 ; 7/7 |
| TOP_03 | 20276, 34501 | 48038, 58379 | 63832 | 63844 | 151 | 7/7 ; 7/7 |
| TOP_02 | 20274, 34402 | 48037, 58279 | 63832 | 63844 | 151 | 7/7 ; 7/7 |
| BOTTOM_05 | 20288, 36481 | 48048, 57679 | 63832 | 63844 | 151 | 7/7 ; 7/7 |
| BOTTOM_09 | 20300, 36877 | 48064, 58879 | 63832 | 63844 | 151 | 7/7 ; 7/7 |
| BOTTOM_06 | 20290, 36580 | 48050, 57879 | 63832 | 63844 | 151 | 7/7 ; 7/7 |
| BOTTOM_08 | 20298, 36778 | 48062, 58679 | 63832 | 63844 | 151 | 7/7 ; 7/7 |
| BOTTOM_07 | 20292, 36679 | 48052, 58079 | 63832 | 63844 | 151 | 7/7 ; 7/7 |

装配原始数据（先平移、随后旋转，仅 GS_FIX 有变换；肋/核心无变换）：

| Instance | Part | 定义行 | 原始变换记录 |
| --- | --- | --- | --- |
| C-C-1 | c-c | 63841 | [] |
| C-S-SHELL-1 | c-s-shell | 63844 | [] |
| GS_LOAD-1 | GS_SHELL_PART | 63847 | [] |
| GS_FIX-1 | GS_SHELL_PART | 63850 | [[0.0, 0.0, 9000.0], [0.0, 0.0, 9000.0, 1.0, 0.0, 9000.0, 180.0]] |

连接和边界原始关键字证据：

| 行 | 关键字 | 数据行与内容 |
| --- | --- | --- |
| 65841 | *Coupling, constraint name=COUP_RP_FIX_TO_GS_MIDLINE, ref node=RP_FIX_GS, surface=GS_FIX-1.GS_MIDLINE |  |
| 65844 | *Coupling, constraint name=COUP_RP_LOAD_TO_GS_MIDLINE, ref node=RP_LOAD_GS, surface=GS_LOAD-1.GS_MIDLINE |  |
| 65847 | *Embedded Element, host elset=C-C-1.UHPC_ALL_CELLS | L65848: C-S-SHELL-1.UCFT_PBL_EMBEDDED_INTERIOR_ELEMENTS |
| 65850 | *Tie, name=TIE_FIX_GS_NEGY_TO_UHPC_END, adjust=no | L65851: GS_FIX-1.GS_TIE_BAND_NEGY, C-C-1.UHPC_END_FIX_ALL |
| 65853 | *Tie, name=TIE_FIX_GS_POSY_TO_UHPC_END, adjust=no | L65854: GS_FIX-1.GS_TIE_BAND_POSY, C-C-1.UHPC_END_FIX_ALL |
| 65856 | *Tie, name=TIE_FIX_GS_TO_STEEL_END_TIEDNSET, adjust=no, type=NODE TO SURFACE, no thickness | L65857: STEEL_FIX_END_ALL_NODES_TIED_CNS_, GS_FIX-1.GS_COMPLETE_FACE |
| 65859 | *Tie, name=TIE_LOAD_GS_NEGY_TO_UHPC_END, adjust=no | L65860: GS_LOAD-1.GS_TIE_BAND_NEGY, C-C-1.UHPC_END_LOAD_ALL |
| 65862 | *Tie, name=TIE_LOAD_GS_POSY_TO_UHPC_END, adjust=no | L65863: GS_LOAD-1.GS_TIE_BAND_POSY, C-C-1.UHPC_END_LOAD_ALL |
| 65865 | *Tie, name=TIE_LOAD_GS_TO_STEEL_END_TIEDNSET, adjust=no, type=NODE TO SURFACE, no thickness | L65866: STEEL_LOAD_END_ALL_NODES_TIED_CNS_, GS_LOAD-1.GS_COMPLETE_FACE |
| 66004 | *Friction | L66005: 0.4, |
| 66006 | *Surface Behavior, pressure-overclosure=HARD |  |
| 66008 | *Friction | L66009: 0.4, |
| 66010 | *Surface Behavior, pressure-overclosure=HARD |  |
| 66015 | *Boundary | L66016: SET_NONLOADED_SIDE_PLATE_XMAX_ACTIVE, 2, 2 |
| 66018 | *Boundary | L66019: SET_NONLOADED_SIDE_PLATE_XMIN_ACTIVE, 2, 2 |
| 66021 | *Boundary | L66022: RP_FIX_GS, 1, 1 ; L66023: RP_FIX_GS, 2, 2 ; L66024: RP_FIX_GS, 3, 3 ; L66025: RP_FIX_GS, 6, 6 |
| 66027 | *Boundary | L66028: RP_LOAD_GS, 1, 1 ; L66029: RP_LOAD_GS, 2, 2 ; L66030: RP_LOAD_GS, 6, 6 |
| 66036 | *Contact Inclusions | L66037: C-S-SHELL-1.SHELL_INTERFACE_X_NEG, C-C-1.UHPC_INTERFACE_X_NEG ; L66038: C-S-SHELL-1.SHELL_INTERFACE_X_POS, C-C-1.UHPC_INTERFACE_X_POS ; L66039: C-S-SHELL-1.SHELL_INTERFACE_Y_NEG, C-C-1.UHPC_INTERFACE_Y_NEG ; L66040: C-S-SHELL-1.SHELL_INTERFACE_Y_POS, C-C-1.UHPC_INTERFACE_Y_POS |
| 66041 | *Contact Property Assignment | L66042: , , PROP_STEEL_UHPC_FRICTION |
| 66058 | *Boundary, amplitude=AMP_RP_LOAD_U3 | L66059: RP_LOAD_GS, 3, 3,45 |

PBL / 外壳截面、集合、单元类型定义行：

| 行 | 关键字 | 数据 |
| --- | --- | --- |
| 119 | *Element, type=S4R |  |
| 47979 | *Element, type=S4R |  |
| 59410 | *Elset, elset=UCFT_OUTER_SHELL_FACES |  |
| 60532 | *Elset, elset=UCFT_PBL_WEB_FACES |  |
| 62252 | *Elset, elset=UCFT_PBL_EMBEDDED_INTERIOR_ELEMENTS |  |
| 62632 | *Elset, elset=UCFT_PBL_NONEMBEDDED_CONSTRAINT_EXCLUSION_ELEMENTS |  |
| 63829 | *Shell Section, elset=UCFT_OUTER_SHELL_FACES, material=STEEL_Q355, offset=SNEG | L63830: 4., 5 |
| 63832 | *Shell Section, elset=UCFT_PBL_WEB_FACES, material=STEEL_Q355 | L63833: 4., 5 |

## BH070 / HISTORICAL_LB3_RP_R01 / AR=3

INP：`C:\03SCI\abaqus-UCFT test\_codex_lb3_git_worktree\semantic_v2\40_execution\model_governance\20260921_ucft_lb3_cleanup\BH070_LB3_EXPLICIT_R01.inp`

SHA256：`7e3706c82f22f5af154a6d9fd9d72380f8752d288470957c3ebff7f8d2ef9216`；大小 4288590 bytes；mtime Unix=1789926397。

此版只用 INP 作为主证据，未读取历史 ODB；不是正式 DIRECT。完全相同 SHA 的重复来源（不是另一套模型）：

- `C:\03SCI\abaqus-UCFT test\_codex_lb3_git_worktree\semantic_v2\40_execution\model_governance\20260921_ucft_lb3_cleanup\COMPUTATION_FILES\BH070_LB3_EXPLICIT_R01.inp`

| 肋 | 节点行区间 | 单元行区间 | PBL 截面行 | 实例行 | 根部共节点 | LOAD / FIX Tie 节点覆盖 |
| --- | --- | --- | --- | --- | --- | --- |
| TOP_04 | 20278, 41700 | 61839, 77529 | 85536 | 85548 | 226 | 7/7 ; 7/7 |
| TOP_01 | 20272, 41253 | 61836, 77079 | 85536 | 85548 | 226 | 7/7 ; 7/7 |
| TOP_03 | 20276, 41551 | 61838, 77379 | 85536 | 85548 | 226 | 7/7 ; 7/7 |
| TOP_02 | 20274, 41402 | 61837, 77229 | 85536 | 85548 | 226 | 7/7 ; 7/7 |
| BOTTOM_05 | 20288, 44531 | 61848, 76329 | 85536 | 85548 | 226 | 7/7 ; 7/7 |
| BOTTOM_09 | 20300, 45127 | 61864, 78129 | 85536 | 85548 | 226 | 7/7 ; 7/7 |
| BOTTOM_06 | 20290, 44680 | 61850, 76629 | 85536 | 85548 | 226 | 7/7 ; 7/7 |
| BOTTOM_08 | 20298, 44978 | 61862, 77829 | 85536 | 85548 | 226 | 7/7 ; 7/7 |
| BOTTOM_07 | 20292, 44829 | 61852, 76929 | 85536 | 85548 | 226 | 7/7 ; 7/7 |

装配原始数据（先平移、随后旋转，仅 GS_FIX 有变换；肋/核心无变换）：

| Instance | Part | 定义行 | 原始变换记录 |
| --- | --- | --- | --- |
| C-C-1 | c-c | 85545 | [] |
| C-S-SHELL-1 | c-s-shell | 85548 | [] |
| GS_LOAD-1 | GS_SHELL_PART | 85551 | [] |
| GS_FIX-1 | GS_SHELL_PART | 85554 | [[0.0, 0.0, 10500.0], [0.0, 0.0, 10500.0, 1.0, 0.0, 10500.0, 180.0]] |

连接和边界原始关键字证据：

| 行 | 关键字 | 数据行与内容 |
| --- | --- | --- |
| 88230 | *Coupling, constraint name=COUP_RP_FIX_TO_GS_MIDLINE, ref node=RP_FIX_GS, surface=GS_FIX-1.GS_MIDLINE |  |
| 88233 | *Coupling, constraint name=COUP_RP_LOAD_TO_GS_MIDLINE, ref node=RP_LOAD_GS, surface=GS_LOAD-1.GS_MIDLINE |  |
| 88236 | *Embedded Element, host elset=C-C-1.UHPC_ALL_CELLS | L88237: C-S-SHELL-1.UCFT_PBL_EMBEDDED_INTERIOR_ELEMENTS |
| 88239 | *Tie, name=TIE_FIX_GS_NEGY_TO_UHPC_END, adjust=no | L88240: GS_FIX-1.GS_TIE_BAND_NEGY, C-C-1.UHPC_END_FIX_ALL |
| 88242 | *Tie, name=TIE_FIX_GS_POSY_TO_UHPC_END, adjust=no | L88243: GS_FIX-1.GS_TIE_BAND_POSY, C-C-1.UHPC_END_FIX_ALL |
| 88245 | *Tie, name=TIE_FIX_GS_TO_STEEL_END_TIEDNSET, adjust=no, type=NODE TO SURFACE, no thickness | L88246: STEEL_FIX_END_ALL_NODES_TIED_CNS_, GS_FIX-1.GS_COMPLETE_FACE |
| 88248 | *Tie, name=TIE_LOAD_GS_NEGY_TO_UHPC_END, adjust=no | L88249: GS_LOAD-1.GS_TIE_BAND_NEGY, C-C-1.UHPC_END_LOAD_ALL |
| 88251 | *Tie, name=TIE_LOAD_GS_POSY_TO_UHPC_END, adjust=no | L88252: GS_LOAD-1.GS_TIE_BAND_POSY, C-C-1.UHPC_END_LOAD_ALL |
| 88254 | *Tie, name=TIE_LOAD_GS_TO_STEEL_END_TIEDNSET, adjust=no, type=NODE TO SURFACE, no thickness | L88255: STEEL_LOAD_END_ALL_NODES_TIED_CNS_, GS_LOAD-1.GS_COMPLETE_FACE |
| 88393 | *Friction | L88394: 0.4, |
| 88395 | *Surface Behavior, pressure-overclosure=HARD |  |
| 88397 | *Friction | L88398: 0.4, |
| 88399 | *Surface Behavior, pressure-overclosure=HARD |  |
| 88404 | *Boundary | L88405: SET_NONLOADED_SIDE_PLATE_XMAX_ACTIVE, 2, 2 |
| 88407 | *Boundary | L88408: SET_NONLOADED_SIDE_PLATE_XMIN_ACTIVE, 2, 2 |
| 88410 | *Boundary | L88411: RP_FIX_GS, 1, 1 ; L88412: RP_FIX_GS, 2, 2 ; L88413: RP_FIX_GS, 3, 3 ; L88414: RP_FIX_GS, 6, 6 |
| 88416 | *Boundary | L88417: RP_LOAD_GS, 1, 1 ; L88418: RP_LOAD_GS, 2, 2 ; L88419: RP_LOAD_GS, 6, 6 |
| 88425 | *Contact Inclusions | L88426: C-S-SHELL-1.SHELL_INTERFACE_X_NEG, C-C-1.UHPC_INTERFACE_X_NEG ; L88427: C-S-SHELL-1.SHELL_INTERFACE_X_POS, C-C-1.UHPC_INTERFACE_X_POS ; L88428: C-S-SHELL-1.SHELL_INTERFACE_Y_NEG, C-C-1.UHPC_INTERFACE_Y_NEG ; L88429: C-S-SHELL-1.SHELL_INTERFACE_Y_POS, C-C-1.UHPC_INTERFACE_Y_POS |
| 88430 | *Contact Property Assignment | L88431: , , PROP_STEEL_UHPC_FRICTION |
| 88447 | *Boundary, amplitude=AMP_RP_LOAD_U3 | L88448: RP_LOAD_GS, 3, 3,52.5 |

PBL / 外壳截面、集合、单元类型定义行：

| 行 | 关键字 | 数据 |
| --- | --- | --- |
| 119 | *Element, type=S4R |  |
| 61779 | *Element, type=S4R |  |
| 78922 | *Elset, elset=UCFT_OUTER_SHELL_FACES |  |
| 80602 | *Elset, elset=UCFT_PBL_WEB_FACES |  |
| 83176 | *Elset, elset=UCFT_PBL_EMBEDDED_INTERIOR_ELEMENTS |  |
| 83745 | *Elset, elset=UCFT_PBL_NONEMBEDDED_CONSTRAINT_EXCLUSION_ELEMENTS |  |
| 85533 | *Shell Section, elset=UCFT_OUTER_SHELL_FACES, material=STEEL_Q355, offset=SNEG | L85534: 4., 5 |
| 85536 | *Shell Section, elset=UCFT_PBL_WEB_FACES, material=STEEL_Q355 | L85537: 4., 5 |

## BH085 / HISTORICAL_LB3_RP_R01 / AR=3

INP：`C:\03SCI\abaqus-UCFT test\_codex_lb3_git_worktree\semantic_v2\40_execution\model_governance\20260921_ucft_lb3_cleanup\BH085_LB3_EXPLICIT_R01.inp`

SHA256：`f0ccf11f68ad017d00d8758703b8403ea23f3d8e59686a270e58c925eca88024`；大小 4305290 bytes；mtime Unix=1789926398。

此版只用 INP 作为主证据，未读取历史 ODB；不是正式 DIRECT。完全相同 SHA 的重复来源（不是另一套模型）：

- `C:\03SCI\abaqus-UCFT test\_codex_lb3_git_worktree\semantic_v2\40_execution\model_governance\20260921_ucft_lb3_cleanup\COMPUTATION_FILES\BH085_LB3_EXPLICIT_R01.inp`

| 肋 | 节点行区间 | 单元行区间 | PBL 截面行 | 实例行 | 根部共节点 | LOAD / FIX Tie 节点覆盖 |
| --- | --- | --- | --- | --- | --- | --- |
| TOP_04 | 20278, 41700 | 61839, 77529 | 85536 | 85548 | 226 | 7/7 ; 7/7 |
| TOP_01 | 20272, 41253 | 61836, 77079 | 85536 | 85548 | 226 | 7/7 ; 7/7 |
| TOP_03 | 20276, 41551 | 61838, 77379 | 85536 | 85548 | 226 | 7/7 ; 7/7 |
| TOP_02 | 20274, 41402 | 61837, 77229 | 85536 | 85548 | 226 | 7/7 ; 7/7 |
| BOTTOM_05 | 20288, 44531 | 61848, 76329 | 85536 | 85548 | 226 | 7/7 ; 7/7 |
| BOTTOM_09 | 20300, 45127 | 61864, 78129 | 85536 | 85548 | 226 | 7/7 ; 7/7 |
| BOTTOM_06 | 20290, 44680 | 61850, 76629 | 85536 | 85548 | 226 | 7/7 ; 7/7 |
| BOTTOM_08 | 20298, 44978 | 61862, 77829 | 85536 | 85548 | 226 | 7/7 ; 7/7 |
| BOTTOM_07 | 20292, 44829 | 61852, 76929 | 85536 | 85548 | 226 | 7/7 ; 7/7 |

装配原始数据（先平移、随后旋转，仅 GS_FIX 有变换；肋/核心无变换）：

| Instance | Part | 定义行 | 原始变换记录 |
| --- | --- | --- | --- |
| C-C-1 | c-c | 85545 | [] |
| C-S-SHELL-1 | c-s-shell | 85548 | [] |
| GS_LOAD-1 | GS_SHELL_PART | 85551 | [] |
| GS_FIX-1 | GS_SHELL_PART | 85554 | [[0.0, 0.0, 12750.0], [0.0, 0.0, 12750.0, 1.0, 0.0, 12750.0, 180.0]] |

连接和边界原始关键字证据：

| 行 | 关键字 | 数据行与内容 |
| --- | --- | --- |
| 88230 | *Coupling, constraint name=COUP_RP_FIX_TO_GS_MIDLINE, ref node=RP_FIX_GS, surface=GS_FIX-1.GS_MIDLINE |  |
| 88233 | *Coupling, constraint name=COUP_RP_LOAD_TO_GS_MIDLINE, ref node=RP_LOAD_GS, surface=GS_LOAD-1.GS_MIDLINE |  |
| 88236 | *Embedded Element, host elset=C-C-1.UHPC_ALL_CELLS | L88237: C-S-SHELL-1.UCFT_PBL_EMBEDDED_INTERIOR_ELEMENTS |
| 88239 | *Tie, name=TIE_FIX_GS_NEGY_TO_UHPC_END, adjust=no | L88240: GS_FIX-1.GS_TIE_BAND_NEGY, C-C-1.UHPC_END_FIX_ALL |
| 88242 | *Tie, name=TIE_FIX_GS_POSY_TO_UHPC_END, adjust=no | L88243: GS_FIX-1.GS_TIE_BAND_POSY, C-C-1.UHPC_END_FIX_ALL |
| 88245 | *Tie, name=TIE_FIX_GS_TO_STEEL_END_TIEDNSET, adjust=no, type=NODE TO SURFACE, no thickness | L88246: STEEL_FIX_END_ALL_NODES_TIED_CNS_, GS_FIX-1.GS_COMPLETE_FACE |
| 88248 | *Tie, name=TIE_LOAD_GS_NEGY_TO_UHPC_END, adjust=no | L88249: GS_LOAD-1.GS_TIE_BAND_NEGY, C-C-1.UHPC_END_LOAD_ALL |
| 88251 | *Tie, name=TIE_LOAD_GS_POSY_TO_UHPC_END, adjust=no | L88252: GS_LOAD-1.GS_TIE_BAND_POSY, C-C-1.UHPC_END_LOAD_ALL |
| 88254 | *Tie, name=TIE_LOAD_GS_TO_STEEL_END_TIEDNSET, adjust=no, type=NODE TO SURFACE, no thickness | L88255: STEEL_LOAD_END_ALL_NODES_TIED_CNS_, GS_LOAD-1.GS_COMPLETE_FACE |
| 88393 | *Friction | L88394: 0.4, |
| 88395 | *Surface Behavior, pressure-overclosure=HARD |  |
| 88397 | *Friction | L88398: 0.4, |
| 88399 | *Surface Behavior, pressure-overclosure=HARD |  |
| 88404 | *Boundary | L88405: SET_NONLOADED_SIDE_PLATE_XMAX_ACTIVE, 2, 2 |
| 88407 | *Boundary | L88408: SET_NONLOADED_SIDE_PLATE_XMIN_ACTIVE, 2, 2 |
| 88410 | *Boundary | L88411: RP_FIX_GS, 1, 1 ; L88412: RP_FIX_GS, 2, 2 ; L88413: RP_FIX_GS, 3, 3 ; L88414: RP_FIX_GS, 6, 6 |
| 88416 | *Boundary | L88417: RP_LOAD_GS, 1, 1 ; L88418: RP_LOAD_GS, 2, 2 ; L88419: RP_LOAD_GS, 6, 6 |
| 88425 | *Contact Inclusions | L88426: C-S-SHELL-1.SHELL_INTERFACE_X_NEG, C-C-1.UHPC_INTERFACE_X_NEG ; L88427: C-S-SHELL-1.SHELL_INTERFACE_X_POS, C-C-1.UHPC_INTERFACE_X_POS ; L88428: C-S-SHELL-1.SHELL_INTERFACE_Y_NEG, C-C-1.UHPC_INTERFACE_Y_NEG ; L88429: C-S-SHELL-1.SHELL_INTERFACE_Y_POS, C-C-1.UHPC_INTERFACE_Y_POS |
| 88430 | *Contact Property Assignment | L88431: , , PROP_STEEL_UHPC_FRICTION |
| 88447 | *Boundary, amplitude=AMP_RP_LOAD_U3 | L88448: RP_LOAD_GS, 3, 3,63.75 |

PBL / 外壳截面、集合、单元类型定义行：

| 行 | 关键字 | 数据 |
| --- | --- | --- |
| 119 | *Element, type=S4R |  |
| 61779 | *Element, type=S4R |  |
| 78922 | *Elset, elset=UCFT_OUTER_SHELL_FACES |  |
| 80602 | *Elset, elset=UCFT_PBL_WEB_FACES |  |
| 83176 | *Elset, elset=UCFT_PBL_EMBEDDED_INTERIOR_ELEMENTS |  |
| 83745 | *Elset, elset=UCFT_PBL_NONEMBEDDED_CONSTRAINT_EXCLUSION_ELEMENTS |  |
| 85533 | *Shell Section, elset=UCFT_OUTER_SHELL_FACES, material=STEEL_Q355, offset=SNEG | L85534: 4., 5 |
| 85536 | *Shell Section, elset=UCFT_PBL_WEB_FACES, material=STEEL_Q355 | L85537: 4., 5 |

## BH100 / HISTORICAL_LB3_RP_R01 / AR=3

INP：`C:\03SCI\abaqus-UCFT test\_codex_lb3_git_worktree\semantic_v2\40_execution\model_governance\20260921_ucft_lb3_cleanup\BH100_LB3_EXPLICIT_R01.inp`

SHA256：`984c9fa1bff5dcc4709ce6e220fe875bea31f180b29e09f1592e6c29d3e32793`；大小 5348044 bytes；mtime Unix=1789926399。

此版只用 INP 作为主证据，未读取历史 ODB；不是正式 DIRECT。完全相同 SHA 的重复来源（不是另一套模型）：

- `C:\03SCI\abaqus-UCFT test\_codex_lb3_git_worktree\semantic_v2\40_execution\model_governance\20260921_ucft_lb3_cleanup\COMPUTATION_FILES\BH100_LB3_EXPLICIT_R01.inp`

| 肋 | 节点行区间 | 单元行区间 | PBL 截面行 | 实例行 | 根部共节点 | LOAD / FIX Tie 节点覆盖 |
| --- | --- | --- | --- | --- | --- | --- |
| TOP_04 | 20278, 48800 | 75639, 96579 | 107235 | 107247 | 301 | 7/7 ; 7/7 |
| TOP_01 | 20272, 48203 | 75636, 95979 | 107235 | 107247 | 301 | 7/7 ; 7/7 |
| TOP_03 | 20276, 48601 | 75638, 96379 | 107235 | 107247 | 301 | 7/7 ; 7/7 |
| TOP_02 | 20274, 48402 | 75637, 96179 | 107235 | 107247 | 301 | 7/7 ; 7/7 |
| BOTTOM_05 | 20288, 52581 | 75648, 94979 | 107235 | 107247 | 301 | 7/7 ; 7/7 |
| BOTTOM_09 | 20300, 53377 | 75664, 97379 | 107235 | 107247 | 301 | 7/7 ; 7/7 |
| BOTTOM_06 | 20290, 52780 | 75650, 95379 | 107235 | 107247 | 301 | 7/7 ; 7/7 |
| BOTTOM_08 | 20298, 53178 | 75662, 96979 | 107235 | 107247 | 301 | 7/7 ; 7/7 |
| BOTTOM_07 | 20292, 52979 | 75652, 95779 | 107235 | 107247 | 301 | 7/7 ; 7/7 |

装配原始数据（先平移、随后旋转，仅 GS_FIX 有变换；肋/核心无变换）：

| Instance | Part | 定义行 | 原始变换记录 |
| --- | --- | --- | --- |
| C-C-1 | c-c | 107244 | [] |
| C-S-SHELL-1 | c-s-shell | 107247 | [] |
| GS_LOAD-1 | GS_SHELL_PART | 107250 | [] |
| GS_FIX-1 | GS_SHELL_PART | 107253 | [[0.0, 0.0, 15000.0], [0.0, 0.0, 15000.0, 1.0, 0.0, 15000.0, 180.0]] |

连接和边界原始关键字证据：

| 行 | 关键字 | 数据行与内容 |
| --- | --- | --- |
| 110615 | *Coupling, constraint name=COUP_RP_FIX_TO_GS_MIDLINE, ref node=RP_FIX_GS, surface=GS_FIX-1.GS_MIDLINE |  |
| 110618 | *Coupling, constraint name=COUP_RP_LOAD_TO_GS_MIDLINE, ref node=RP_LOAD_GS, surface=GS_LOAD-1.GS_MIDLINE |  |
| 110621 | *Embedded Element, host elset=C-C-1.UHPC_ALL_CELLS | L110622: C-S-SHELL-1.UCFT_PBL_EMBEDDED_INTERIOR_ELEMENTS |
| 110624 | *Tie, name=TIE_FIX_GS_NEGY_TO_UHPC_END, adjust=no | L110625: GS_FIX-1.GS_TIE_BAND_NEGY, C-C-1.UHPC_END_FIX_ALL |
| 110627 | *Tie, name=TIE_FIX_GS_POSY_TO_UHPC_END, adjust=no | L110628: GS_FIX-1.GS_TIE_BAND_POSY, C-C-1.UHPC_END_FIX_ALL |
| 110630 | *Tie, name=TIE_FIX_GS_TO_STEEL_END_TIEDNSET, adjust=no, type=NODE TO SURFACE, no thickness | L110631: STEEL_FIX_END_ALL_NODES_TIED_CNS_, GS_FIX-1.GS_COMPLETE_FACE |
| 110633 | *Tie, name=TIE_LOAD_GS_NEGY_TO_UHPC_END, adjust=no | L110634: GS_LOAD-1.GS_TIE_BAND_NEGY, C-C-1.UHPC_END_LOAD_ALL |
| 110636 | *Tie, name=TIE_LOAD_GS_POSY_TO_UHPC_END, adjust=no | L110637: GS_LOAD-1.GS_TIE_BAND_POSY, C-C-1.UHPC_END_LOAD_ALL |
| 110639 | *Tie, name=TIE_LOAD_GS_TO_STEEL_END_TIEDNSET, adjust=no, type=NODE TO SURFACE, no thickness | L110640: STEEL_LOAD_END_ALL_NODES_TIED_CNS_, GS_LOAD-1.GS_COMPLETE_FACE |
| 110778 | *Friction | L110779: 0.4, |
| 110780 | *Surface Behavior, pressure-overclosure=HARD |  |
| 110782 | *Friction | L110783: 0.4, |
| 110784 | *Surface Behavior, pressure-overclosure=HARD |  |
| 110789 | *Boundary | L110790: SET_NONLOADED_SIDE_PLATE_XMAX_ACTIVE, 2, 2 |
| 110792 | *Boundary | L110793: SET_NONLOADED_SIDE_PLATE_XMIN_ACTIVE, 2, 2 |
| 110795 | *Boundary | L110796: RP_FIX_GS, 1, 1 ; L110797: RP_FIX_GS, 2, 2 ; L110798: RP_FIX_GS, 3, 3 ; L110799: RP_FIX_GS, 6, 6 |
| 110801 | *Boundary | L110802: RP_LOAD_GS, 1, 1 ; L110803: RP_LOAD_GS, 2, 2 ; L110804: RP_LOAD_GS, 6, 6 |
| 110810 | *Contact Inclusions | L110811: C-S-SHELL-1.SHELL_INTERFACE_X_NEG, C-C-1.UHPC_INTERFACE_X_NEG ; L110812: C-S-SHELL-1.SHELL_INTERFACE_X_POS, C-C-1.UHPC_INTERFACE_X_POS ; L110813: C-S-SHELL-1.SHELL_INTERFACE_Y_NEG, C-C-1.UHPC_INTERFACE_Y_NEG ; L110814: C-S-SHELL-1.SHELL_INTERFACE_Y_POS, C-C-1.UHPC_INTERFACE_Y_POS |
| 110815 | *Contact Property Assignment | L110816: , , PROP_STEEL_UHPC_FRICTION |
| 110832 | *Boundary, amplitude=AMP_RP_LOAD_U3 | L110833: RP_LOAD_GS, 3, 3,75 |

PBL / 外壳截面、集合、单元类型定义行：

| 行 | 关键字 | 数据 |
| --- | --- | --- |
| 119 | *Element, type=S4R |  |
| 75579 | *Element, type=S4R |  |
| 98435 | *Elset, elset=UCFT_OUTER_SHELL_FACES |  |
| 100673 | *Elset, elset=UCFT_PBL_WEB_FACES |  |
| 104100 | *Elset, elset=UCFT_PBL_EMBEDDED_INTERIOR_ELEMENTS |  |
| 104858 | *Elset, elset=UCFT_PBL_NONEMBEDDED_CONSTRAINT_EXCLUSION_ELEMENTS |  |
| 107232 | *Shell Section, elset=UCFT_OUTER_SHELL_FACES, material=STEEL_Q355, offset=SNEG | L107233: 4., 5 |
| 107235 | *Shell Section, elset=UCFT_PBL_WEB_FACES, material=STEEL_Q355 | L107236: 4., 5 |

## 连接、几何与集合核验口径

- 实体集合 UCFT_PBL_WEB_FACES 与 UCFT_OUTER_SHELL_FACES 不相交；PBL 仅沿自己的元素图拆分九个连通分量，然后再检查其节点与 outer shell 的交集。
- 每件 PBL 分量元素数之和 = PBL 全集元素数，无重复计数；上四下五单独保留；所有肋 X 恒定、轴向贯穿、截面高 41、厚 4。没有横向 PBL 分量。
- 钢壳根部节点共享是位移/转角节点一致的直接证据，但 PBL 内部 Embedded 对 UHPC 只证明所声明的嵌入关系；不能推定整个 UHPC 肋线独立零转角。
- 嵌入集 UCFT_PBL_EMBEDDED_INTERIOR_ELEMENTS，宿主 C-C-1.UHPC_ALL_CELLS；排除集合 UCFT_PBL_NONEMBEDDED_CONSTRAINT_EXCLUSION_ELEMENTS 不当成额外钢构件。
- 正式端部有两种同义命名：STEEL_END_ALL_NODES_TIED_LOAD/FIX 或 STEEL_LOAD/FIX_END_ALL_NODES_TIED；逐根两端节点覆盖都完整。只认名称而不核对节点可能误报后四件漏绑。
- 接触四对 X_NEG/X_POS/Y_NEG/Y_POS，摩擦关键字 0.4；法向接触、端部 Tie 与 Embedded 分开保存。不存在把接触线或网格层当实体肋的步骤。
- 每根 PBL 自由边界图一个闭合连通环，内部孔环为 0；不提供虚构孔径。无孔 FEM 不证明实物 PBL 没有孔。
- INP 读取前后大小与 mtime 保持一致；ODB readOnly=True，读取前后大小与 mtime 保持一致。没有新 JOB 或 ODB 场提取。

## AR 版本检索及缺失项

全工作区检索到 137 个具有九试件名字的候选 INP，逐项记录在 VERSION_INVENTORY.json；目录内 PBL_CROSS/U 槽/诊断重复文件不替代正式源。九套 AR=3 LB3 历史 INP 各有一个 SHA 相同的 COMPUTATION_FILES 副本，合并后为九个版本。

历史来源目录：`C:\03SCI\abaqus-UCFT test\_codex_lb3_git_worktree\semantic_v2\40_execution\model_governance\20260921_ucft_lb3_cleanup`；对应 CAE 为 UCFT_LB3_9SPEC_MASTER.cae。build_lb3_from_current_inp_r01.py L101..129 的 make_periodic_copy：Lnew=1.5Lold，复制原第二半波节点 X/Y 不变；IMPERFECTION_AUDIT_LB3.csv 与 UCFT_LB3_9SPEC_BUILD_REPORT.md 为辅助来源。复制规则已用实际节点零点与长度核实，不能重释成全长单一三半波正弦。

AR=1：在本次可访问工作区 INP 及研究仓库中没有找到可验证九件 AR=1 实体建模文件。仓库存在 AR1 理论比较文件不构成 FEM 几何证据；标为 NOT_FOUND，不能断言其他不可访问位置不存在。AR3 未单独读 ODB，不宣称其 ODB 核验 PASS。

独立肋线零转角约束：NOT_FOUND；真实孔中心/直径/间距：N/A_NO_MODELLED_HOLES；未经读取的 CAE 内 Part 切分特征树和理论转角等效约束：不声称已识别。上述缺失不影响 INP 中实际肋坐标确认，但影响将其理想化为固支理论边界的判断。

## 可复算与验收

scripts/extract_geometry.py：主 INP 解析和逐根分量恢复；scripts/verify_odb_geometry.py：Abaqus Python 只读网格核验；scripts/inventory_versions.py + refresh_variants.py：候选版本检索、SHA 去重；scripts/build_ledgers.py：原始 JSON 转本账本。归档版 build_ledgers.py 可直接从相邻 06_GEOMETRY_EVIDENCE.json 复算；若原 INP 不可访问，源 SHA 复核记 NOT_FOUND，不冒充源核验通过。重新提取须在本地独立输出目录运行 extract → inventory → refresh → ODB 验证 → build，原 ROOT 需对应可访问工作区，禁止写原 INP/ODB。06 的逐层坐标按 initial_profile_columns 列序存数组；节点/单元 ID 以无损等差段 [start,end_inclusive,step] 或单值存储，build 自动还原，绝无坐标采样压缩或插值。

验收结果记录在 VERIFICATION_RESULTS.json。正式九件 81 根，历史 AR3 独立 81 根；CSV 总 162 行，版本字段明确。CSV 数值字段可直接计算，无坐标插值；逐层剖面可复现有限厚度实际包围盒与初始长度，不把理论坐标当实测。下一轮可以据此采用上/下分别的实际肋线和有限厚度边界；转角理想化仍须明确模型假设。
