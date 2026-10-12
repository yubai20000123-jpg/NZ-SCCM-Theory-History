"""Build the geometry-only research deliverables from independently extracted INPs.
No FEM source is written. Python 3 + standard library; extractor additionally uses numpy.
"""
import csv, json, math, hashlib, shutil, copy
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
WORK = SCRIPT_DIR.parent if SCRIPT_DIR.name=='scripts' else SCRIPT_DIR
REL = Path('semantic_v2/40_execution/20261012__BH050_YUNLU_AIRY_PBL_RIB_MANUAL_LEDGER/05_PBL_ACTUAL_GEOMETRY_NINE_CASES')
DEST = WORK if (WORK/'06_GEOMETRY_EVIDENCE.json').exists() else WORK / REL
DEST.mkdir(parents=True, exist_ok=True)
if (WORK/'geometry_raw.json').exists():
    formal = json.loads((WORK/'geometry_raw.json').read_text(encoding='utf-8'))
    variants = json.loads((WORK/'AR1_AR3_VARIANTS.json').read_text(encoding='utf-8'))
else:
    archived=json.loads((WORK/'06_GEOMETRY_EVIDENCE.json').read_text(encoding='utf-8'))
    formal=archived['formal'];variants=archived['historical_AR3']
    for rec in formal+variants:
        for rib in rec['ribs']:
            if 'initial_profile_arrays' in rib:
                rib['initial_profile']=[dict(zip(archived['initial_profile_columns'],row)) for row in rib.pop('initial_profile_arrays')]
            for field in ['element_ids','node_ids']:
                if field+'_exact_runs' in rib:
                    rib[field]=[n for run in rib.pop(field+'_exact_runs') for n in (range(run[0],run[1]+1,run[2]) if isinstance(run,list) else [run])]
odb = json.loads((WORK/'ODB_GEOMETRY_VERIFICATION.json').read_text(encoding='utf-8'))
inventory = json.loads((WORK/'VERSION_INVENTORY.json').read_text(encoding='utf-8'))
records = formal + variants
CASES = ['BH005','BH010','BH020','BH032','BH050','BH060','BH070','BH085','BH100']
BASE = 'd2cf149e7a45b656cde75eab2ef2ab4e9bf03255'
def num(v):
    if isinstance(v,(int,float)): return format(v,'.10g')
    return str(v)
def series(v): return ', '.join(num(x) for x in v)
def table(headers, rows):
    return '\n'.join(['| '+' | '.join(headers)+' |', '| '+' | '.join(['---']*len(headers))+' |'] + ['| '+' | '.join(num(x).replace('|','\\|').replace('\n',' ') for x in row)+' |' for row in rows])+'\n'
def emit(name, text): (DEST/name).write_text(text.rstrip()+'\n',encoding='utf-8')
def groups(r): return [(s,sorted([q for q in r['ribs'] if q['side']==s],key=lambda q:q['reference_x_mm'])) for s in ['TOP','BOTTOM']]
def title(r): return r['case']+' / '+r['version']+' / AR='+num(r['AR'])
def xyz(v, r): return (v[0]-r['xmin_mm'],v[2]-r['Z_start_mm'],v[1])
def arc(q):
    pts=q['initial_profile']
    return sum(math.hypot(b['original_Z_mm']-a['original_Z_mm'],b['midplane_Y_min_mm']-a['midplane_Y_min_mm']) for a,b in zip(pts,pts[1:]))

rows=[]
for r in records:
    for side,qs in groups(r):
        for i,q in enumerate(qs):
            b=r['width_mm'];lo,hi=q['finite_thickness_bbox_original'];p0=xyz(q['root_start_original'],r);p1=xyz(q['root_end_original'],r)
            nodes=[j*b/4 for j in range(5)];near=min(nodes,key=lambda x:abs(x-q['reference_x_mm']))
            row=dict(case=r['case'],version=r['version'],AR=r['AR'],rib_id=q['rib_id'],part=q['part'],instance=q['instance'],rib_type=q['rib_type'],side=side,
              B_nominal_mm=b,B_UHPC_mm=r['core_width_mm'],L_projected_mm=r['length_mm'],a_h_geometry_mm=r['half_wave_length_mm'],
              original_X_mm=q['original_X_mm'],theory_x_mm=q['reference_x_mm'],core_origin_x_mm=q['core_origin_x_mm'],theory_y_start_mm=q['reference_y_start_mm'],theory_y_end_mm=q['reference_y_end_mm'],
              reference_flat_centerline_z_mm=q['reference_centerline_z_mm'],centerline_start_x_mm=q['reference_x_mm'],centerline_start_y_mm=q['reference_y_start_mm'],centerline_start_z_mm=q['reference_centerline_z_mm'],centerline_end_x_mm=q['reference_x_mm'],centerline_end_y_mm=q['reference_y_end_mm'],centerline_end_z_mm=q['reference_centerline_z_mm'],
              root_start_x_mm=p0[0],root_start_y_mm=p0[1],root_start_z_mm=p0[2],root_end_x_mm=p1[0],root_end_y_mm=p1[1],root_end_z_mm=p1[2],
              finite_theory_x_min_mm=lo[0]-r['xmin_mm'],finite_theory_x_max_mm=hi[0]-r['xmin_mm'],finite_theory_y_min_mm=lo[2]-r['Z_start_mm'],finite_theory_y_max_mm=hi[2]-r['Z_start_mm'],finite_theory_z_min_mm=lo[1],finite_theory_z_max_mm=hi[1],
              flat_z_min_mm=q['flat_reference_z_min_mm'],flat_z_max_mm=q['flat_reference_z_max_mm'],thickness_mm=q['thickness_mm'],height_min_mm=q['height_min_mm'],height_max_mm=q['height_max_mm'],projected_length_mm=q['axial_length_mm'],initial_centerline_polyline_arclength_mm=arc(q),
              same_side_previous_pitch_mm=q['reference_x_mm']-qs[i-1]['reference_x_mm'] if i else 'N/A_EDGE',same_side_next_pitch_mm=qs[i+1]['reference_x_mm']-q['reference_x_mm'] if i+1<len(qs) else 'N/A_EDGE',
              shared_shell_root_nodes=q['shared_root_node_count'],embedded_elements=q['embedded_element_count'],rib_elements=q['element_count'],rib_unique_nodes=q['node_count'],
              load_tie_set=q['end_load_tie_set'],fix_tie_set=q['end_fix_tie_set'],load_end_nodes=q['end_load_node_count'],load_tied_nodes=q['end_load_tied_node_count'],fix_end_nodes=q['end_fix_node_count'],fix_tied_nodes=q['end_fix_tied_node_count'],end_coverage=q['direct_named_end_set_coverage'],
              connection=q['connection'],independent_rib_rotation_constraint='NOT_FOUND',model_hole_count=q['hole_boundary_loop_count'],hole_centres_diameters_pitch='N/A_NO_MODELLED_HOLES',nearest_N4_node_x_mm=near,signed_distance_to_N4_node_mm=q['reference_x_mm']-near,N4_longitudinal_line_match=abs(q['reference_x_mm']-near)<1e-7,
              source_INP=r['source'],source_SHA256=r['sha256'],node_evidence_first_line=q['node_line_range'][0],node_evidence_last_line=q['node_line_range'][1],element_evidence_first_line=q['element_line_range'][0],element_evidence_last_line=q['element_line_range'][1],PBL_section_line=q['section_line'],assembly_instance_line=q['assembly_line'],PBL_elset='UCFT_PBL_WEB_FACES',profile_evidence_file='06_GEOMETRY_EVIDENCE.json')
            rows.append(row)
with (DEST/'01_nine_specimens_rib_coordinates.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

intro='''# 九试件真实 PBL 几何坐标账本（仅诊断）

单位均为 mm。只读取已有 INP / ODB 网格；不改 FEM、理论或求解。正式数据为 GS_DIRECT R02 接触恢复后集合，磁盘目录和 JOB 名仍保留 R01。历史 AR=3 RP 模型独立列出，不混用。AR=1 可验证 FEM 文件：NOT_FOUND。

## 坐标与实体口径

ABAQUS `(X,Y,Z)` = `(板宽,厚度/面外,轴向)`；理论 `(x,y,z)` = `(X+B/2,Z-Z_start,Y)`，本次 Z_start=0。板宽原点为 nominal 外轮廓左边；横向正向不变，轴向正向从加载端 Z=0 指向固定端 Z=L。加载端 U3 正向压缩。UHPC 实宽为 B-8，core-origin x = theory x - 4，不能偷偷以 UHPC 左边替换理论原点。

实体 PBL 指实际钢板构件，本模型用 S4R 壳离散，不是 3D 实体单元。PBL 的中心面 X=Xc，ShellSection 厚 4，默认中面偏置；实际材料横向范围 Xc±2。每根肋的平直参考高度 41：上肋 Y∈[-16,25]、下肋 Y∈[-25,16]；根部在外壳参考面 ±25，与外壳共节点。外壳内表面参考 ±21，因此肋尖距对侧内表面 5。参考中心线 z 为上 +4.5、下 -4.5，不是上/下壳 ±25 或壳材料形心 ±23。

表中端点是肋中心线 `(x,0,±4.5)` → `(x,L,±4.5)`；根部端点另存 CSV。中间高度随实际初始缺陷移动；CSV 包围范围及 JSON 逐层剖面保留该变化，不能把平直参考图当成实际无缺陷几何。各 INP 中 C-S-SHELL-1 与 C-C-1 均无装配变换。

连接：钢壳根部共节点；部分 PBL 网格 Embedded 到 UHPC；两端 PBL 节点均纳入对应 GS Tie。没有独立查到整条 PBL 线的零转角边界（NOT_FOUND），不能把 Embedded 平移协调称为 UHPC 固支转角。正式外钢壳/UHPC 四对界面是接触，不是全表面 Tie。

## 正式 DIRECT 九件总览
'''
intro+=table(['试件','B','UHPC 宽','L','a_h=L/2','上肋原始 X（4 根）','下肋原始 X（5 根）','同板中心距'],[(r['case'],r['width_mm'],r['core_width_mm'],r['length_mm'],r['half_wave_length_mm'],series([q['original_X_mm'] for s,qs in groups(r) if s=='TOP' for q in qs]),series([q['original_X_mm'] for s,qs in groups(r) if s=='BOTTOM' for q in qs]),groups(r)[0][1][1]['reference_x_mm']-groups(r)[0][1][0]['reference_x_mm']) for r in formal])
intro+='\n下面每行是一个独立物理肋板；编号按 PBL 子图连通分量保留，不表示 Part 数。用 PBL 专属单元连通性识别，再核对根部共享节点，避免所有肋在同一钢壳 Part 中被合并。\n'
for r in records:
    intro+='\n## '+title(r)+'\n\n'
    intro+=table(['肋 ID / 侧','原始 X','理论 x','有限厚度 x 范围','中心线起点 → 终点','平直 z 范围','长度 / 厚 / 高','单元 / 嵌入单元','根部共节点 / 端部 Tie'],[(q['rib_id']+' / '+s,q['original_X_mm'],q['reference_x_mm'],series([q['reference_x_mm']-2,q['reference_x_mm']+2]),f"({num(q['reference_x_mm'])},0,{num(q['reference_centerline_z_mm'])}) → ({num(q['reference_x_mm'])},{num(r['length_mm'])},{num(q['reference_centerline_z_mm'])})",series([q['flat_reference_z_min_mm'],q['flat_reference_z_max_mm']]),series([q['axial_length_mm'],q['thickness_mm'],q['height_min_mm']]),f"{q['element_count']} / {q['embedded_element_count']}",f"{q['shared_root_node_count']} / {q['direct_named_end_set_coverage']}") for s,qs in groups(r) for q in qs])
    intro+='\nPart `c-s-shell` / Instance `C-S-SHELL-1`；集合 `UCFT_PBL_WEB_FACES`；模型孔洞 0（每根外边界仅一个连通环），没有孔心、孔径、孔距可填写。该结论仅指 FEM 所建几何。完整原始坐标证据见 05 和 06。\n'
intro+='''
## 数量与版本

正式九件：81 根纵向 PBL = 36 根上肋 + 45 根下肋，横向实体 PBL 0。九件均 COMPLETE，坐标全部逐节点核实。历史 AR=3 又有 81 根同横截面肋，但属于另九个模型，不计入正式九件数量；重复路径 SHA 去重后只保留每件一份。

AR=3 长度分别 750、1500、3000、4800、7500、9000、10500、12750、15000；加载方式为历史 RP 耦合。a_h=B=L/3，初始形状采用第二半波复制，三个符号为 (+,-,-)，不是一个全长 sin(3πy/L)。本账本没有修复历史几何。
'''
emit('02_nine_specimens_rib_coordinates.md',intro)

cells='''# 肋距、真实子板与整体半波计算账本

所有坐标先按 x=X+B/2 转换，以下宽度逐项由实际提取的 x 相减，不由波数猜测。上、下钢板分别分区；交错两面的所有 X 站位不能混合成同一钢板的支持肋。

nominal 钢板范围 x=0..B；UHPC 横向范围 x=4..B-4。以下边缘钢板宽度按 nominal 外轮廓计算，实际侧壳连接中心面/内表面不同，应使用所需边界口径，不把 UHPC core 边界当作同一个几何边界。

中心线分区仅为理论参考分区，并非把有厚度肋消除；内部净宽 = 中心距 -2 -2；边缘净宽 = 边缘中心线宽 -2。core 边缘净宽再减 4。PBL 只从单侧伸入，不切透整个 UHPC 厚度，分区不等于互不连接的 UHPC 实体块。
'''
for r in records:
    b=r['width_mm'];L=r['length_mm'];ah=r['half_wave_length_mm']
    cells+='\n## '+title(r)+'\n\n'
    cells+=f"x=X+{num(b)}/2=X+{num(b/2)}；y=Z-{num(r['Z_start_mm'])}。L={num(L)}；实测初始缺陷零点 Z={series(r['centerline_initial_bow_zero_Z_mm'])}；a_h={num(ah)}；L/a_h={num(L/ah)}。\n\n"
    for side,qs in groups(r):
        xs=[q['reference_x_mm'] for q in qs];bounds=[0]+xs+[b]
        cells+='### '+side+'\n\n'
        cells+=table(['肋 ID','坐标转换减法/加法','理论 x','前肋中心距计算'],[(q['rib_id'],f"{num(q['original_X_mm'])}+{num(b/2)}={num(q['reference_x_mm'])}",q['reference_x_mm'],f"{num(q['reference_x_mm'])}-{num(qs[i-1]['reference_x_mm'])}={num(q['reference_x_mm']-qs[i-1]['reference_x_mm'])}" if i else 'N/A 第一根') for i,q in enumerate(qs)])
        rr=[]
        for i,(left,right) in enumerate(zip(bounds,bounds[1:])):
            width=right-left;deduct=2 if i==0 or i==len(bounds)-2 else 4
            core_left=4 if i==0 else left;core_right=b-4 if i==len(bounds)-2 else right
            rr.append((f'{side}_{i+1:02d}',left,right,f'{num(right)}-{num(left)}={num(width)}',f'{num(width)}-{deduct}={num(width-deduct)}',f'{num(core_right)}-{num(core_left)}-{deduct}={num(core_right-core_left-deduct)}',L,ah,f'{num(L)}/{num(ah)}={num(L/ah)}'))
        cells+=table(['子板','左中心线/边界 x','右中心线/边界 x','参考宽度计算','钢板净宽计算','core 对应横向净距','轴向总长','整体半波长','对应半波数'],rr)+'\n'
    cells+='各肋均贯穿 y=0..L；没有内部横向实体 PBL，所以不得将 y=j a_h/4 当成实体肋支持线而把长度自行截成四段。\n'
cells+='''
## 从提取值归纳（不是作为提取前提）

上肋 x/B=0.1625、0.3875、0.6125、0.8375；下肋 x/B=0.05、0.275、0.50、0.725、0.95。同面中心距 0.225B，上下相位差 0.1125B，完全不对齐。上面边缘参考宽度 0.1625B，下面 0.05B；中间宽度均 0.225B。中心线子板宽度之和每面严格等于 B。

正式初始几何经实际节点验证：w0=(B/400) sin(πx/B) sin(2πy/L)，两个整体半波，a_h=L/2=B。该式用于核验已有初始坐标，不修改模型。参考高度范围加 w0，即上 [-16+w0,25+w0]、下 [-25+w0,16+w0]。逐层实测剖面保留在 06，CSV 中实际包围盒包含 w0，不把包围盒高度误当肋高。

历史 AR=3 由原 AR=2 的第二半段 B..2B 原坐标复制至 2B..3B：y_new=2B+(y_old-B)，横向和厚度坐标不变。因此三段符号 (+,-,-)，不是新 sin(3πy/L)。在拼接零点可能存在斜率不连续，本次仅如实登记，不在 Airy 输入中掩盖。

平直参考全肋截面面积：9×4×41=1476 mm²；与 UHPC 厚度 [-21,21] 相交的几何条带每根高 37，9×4×37=1332 mm²；差 144 为根部超出 core 厚度范围的条带。1332 可以作为 core 内几何相交面积解释，不能未经受力审计视为全部肋的有效承载面积；本任务不计算内力。
'''
emit('03_rib_spacing_and_theoretical_cells.md',cells)

modes='''# 实体肋 A、约束 B、理论波节 C、网格分割 D 的区分

沿用已有账本的 N=m=4、b=B、a=a_h，而不修改公式。ψ=(1-cos(8πx/B))(1-cos(8πy/a_h))。纵向零线 x=jB/4 (j=0..4)；每个整体半波内横向零线 y_local=k a_h/4 (k=0..4)。它们是 C，不是实体数量清单。

A：UCFT_PBL_WEB_FACES 的独立连通钢板，共九根，均纵向且有限厚度 4 mm。
B：根部共享节点、部分 Embedded、两端 GS Tie；没有查到内部四条横向 PBL Tie 或整条肋线独立转角锁定。
C：上式数学零线。仅下肋中间一根在 x=B/2 与纵向 C 线重合。
D：UHPC/钢壳网格层或切分边，未有 PBL 单元证据的不能算 A。很多轴向网格线位于上述 C 线附近也不代表横肋。

下表距波节为实际 x 减最近 jB/4，保留符号。ψ 沿整条实体肋恒零需要横向因子 f_x=1-cos(8πx/B)=0，只有在个别 y 波节处 ψ=0 不算整条肋满足。
'''
for r in records:
    b=r['width_mm'];ah=r['half_wave_length_mm']
    modes+='\n## '+title(r)+'\n\n'
    modes+=f"理论 x 零线：{series([j*b/4 for j in range(5)])}；单个整体半波理论 y 零线：{series([j*ah/4 for j in range(5)])}。\n\n"
    rr=[]
    for s,qs in groups(r):
        for q in qs:
            x=q['reference_x_mm'];near=min([j*b/4 for j in range(5)],key=lambda v:abs(x-v));match=abs(x-near)<1e-7
            rr.append((q['rib_id'],x,near,x-near,1-math.cos(8*math.pi*x/b),'MATCH' if match else 'MISMATCH','仅根部节点/Embedded；无独立零转角证明'))
    modes+=table(['真实肋','实际 x','最近 C 线','差值','f_x','整条 ψ=0','连接/转角'],rr)
    modes+='真实横向实体肋：0。两端 Tie 位于 y=0、L；其余 y 波节没有对应横向实体肋。正好与数学零线重合的中间纵肋，形函数一阶导数也为零，但这只是形函数性质，不是模型转角固支证明。\n'
modes+='''
## 对下一轮三层 Airy 肋线协调的输入限制

真实上、下肋 x 坐标应独立输入，不能共同用 x=jB/4 替代。每件九根中仅一根匹配该 N=4 零线，其余八根不匹配；真实同面肋距 0.225B 比 B/4 小 10%。BH050 的真实间距 562.5 而不是 625。边缘条带也不等于中间板带。

ψ 在八条实体肋线一般不为零，因此当前局部场不能在未经说明的情况下直接声称满足真实肋线位移边界。也不能把无孔壳 PBL、Embedded、共同根节点自动升级为理想刚性固支。现有几何支持建立实际肋线协调条件，尚不支持直接使用等距 N=4、m=4 作为物理加劲网格。本账本只报告差异，不改波数、不重推、不求荷载。
'''
emit('04_real_ribs_vs_mode_nodes.md',modes)

sources=f'''# 来源、版本与逐项核验

研究仓库 yubai20000123-jpg/NZ-SCCM-Theory-History，目标分支 research/20261012-bh050-rib-airy-manual-ledger；四份前置账本完整阅读，基准提交 {BASE}。本次仅添加 05_PBL_ACTUAL_GEOMETRY_NINE_CASES，不覆盖原 00..03。时间 2026-10-12（中国标准时间）。

## 正式来源决策

正式文件目录命名 R01 不代表其仍是历史前接触版本。每件 INP SHA256 与 2026-10-10 正式截面提取 EXTRACTION_PROVENANCE.json 的 source_before.inp.sha256 完全一致；BH032 使用 2026-09-26 接触恢复后正式文件。ODB 钢结构全节点又与相同 INP 比对，九件均 MATCH。没有把 RP/BASE、U_GROOVE、PBL_CROSS R03 或其近期改肋模型纳入正式提取。

原 CAE：`C:\\03SCI\\abaqus-UCFT test\\UCFT_GS_DIRECT_R01_11MODELS\\UCFT_GS_DIRECT_R01_11MODELS.cae`。本次无需打开/保存 CAE：对应可读 INP 的节点/单元/截面/集合为几何主证据，ODB 网格作独立核验。没有 CAE 读取失败，也没有用 CAE 目测代替坐标提取。

原始来源完整路径逐项如下；行号为一基 INP 行号。每根全部元素/节点 ID、逐层初始剖面、装配和关键字记录保存在 06；CSV 保留行号区间，区间内可能夹有非该肋节点，应按 JSON ID 筛选，不把整个行区间都认作该肋。
'''
for r in records:
    sources+='\n## '+title(r)+'\n\n'+f"INP：`{r['source']}`\n\nSHA256：`{r['sha256']}`；大小 {r['bytes']} bytes；mtime Unix={num(r['mtime'])}。\n\n"
    if r in formal:
        o=next(q for q in odb if q['case']==r['case'])
        sources+=f"ODB：`{o['odb']}`；只读网格，不读场/历史；{o['INP_nodes']} / {o['ODB_nodes']} 钢壳节点；最大差 {num(o['max_coordinate_difference_mm'])} mm；PBL 集合 {o['PBL_elements']} 单元与 INP 相符。对应历史审计：`C:\\03SCI\\abaqus-UCFT test\\outputs\\DIRECT_END_CREST_FORCE_AUDIT_20261010\\{r['case']}_EXTRACTION_PROVENANCE.json`。\n\n"
    else:
        sources+='此版只用 INP 作为主证据，未读取历史 ODB；不是正式 DIRECT。完全相同 SHA 的重复来源（不是另一套模型）：\n\n'+ '\n'.join('- `'+p+'`' for p in r.get('duplicate_source_paths',[]))+'\n\n'
    sources+=table(['肋','节点行区间','单元行区间','PBL 截面行','实例行','根部共节点','LOAD / FIX Tie 节点覆盖'],[(q['rib_id'],series(q['node_line_range']),series(q['element_line_range']),q['section_line'],q['assembly_line'],q['shared_root_node_count'],f"{q['end_load_tied_node_count']}/{q['end_load_node_count']} ; {q['end_fix_tied_node_count']}/{q['end_fix_node_count']}") for s,qs in groups(r) for q in qs])
    sources+='\n装配原始数据（先平移、随后旋转，仅 GS_FIX 有变换；肋/核心无变换）：\n\n'
    sources+=table(['Instance','Part','定义行','原始变换记录'],[(k,v['part'],v['line'],json.dumps(v['transform'])) for k,v in r['instances'].items()])
    sources+='\n连接和边界原始关键字证据：\n\n'
    sources+=table(['行','关键字','数据行与内容'],[(c['line'],c['header'],' ; '.join(f"L{v[0]}: {v[1]}" for v in c['data'])) for c in r['connections']])
    sources+='\nPBL / 外壳截面、集合、单元类型定义行：\n\n'+table(['行','关键字','数据'],[(c['line'],c['header'],' ; '.join(f"L{v[0]}: {v[1]}" for v in c['data'])) for c in r.get('geometry_keyword_evidence',[])])
sources+='''
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

历史来源目录：`C:\\03SCI\\abaqus-UCFT test\\_codex_lb3_git_worktree\\semantic_v2\\40_execution\\model_governance\\20260921_ucft_lb3_cleanup`；对应 CAE 为 UCFT_LB3_9SPEC_MASTER.cae。build_lb3_from_current_inp_r01.py L101..129 的 make_periodic_copy：Lnew=1.5Lold，复制原第二半波节点 X/Y 不变；IMPERFECTION_AUDIT_LB3.csv 与 UCFT_LB3_9SPEC_BUILD_REPORT.md 为辅助来源。复制规则已用实际节点零点与长度核实，不能重释成全长单一三半波正弦。

AR=1：在本次可访问工作区 INP 及研究仓库中没有找到可验证九件 AR=1 实体建模文件。仓库存在 AR1 理论比较文件不构成 FEM 几何证据；标为 NOT_FOUND，不能断言其他不可访问位置不存在。AR3 未单独读 ODB，不宣称其 ODB 核验 PASS。

独立肋线零转角约束：NOT_FOUND；真实孔中心/直径/间距：N/A_NO_MODELLED_HOLES；未经读取的 CAE 内 Part 切分特征树和理论转角等效约束：不声称已识别。上述缺失不影响 INP 中实际肋坐标确认，但影响将其理想化为固支理论边界的判断。

## 可复算与验收

scripts/extract_geometry.py：主 INP 解析和逐根分量恢复；scripts/verify_odb_geometry.py：Abaqus Python 只读网格核验；scripts/inventory_versions.py + refresh_variants.py：候选版本检索、SHA 去重；scripts/build_ledgers.py：原始 JSON 转本账本。归档版 build_ledgers.py 可直接从相邻 06_GEOMETRY_EVIDENCE.json 复算；若原 INP 不可访问，源 SHA 复核记 NOT_FOUND，不冒充源核验通过。重新提取须在本地独立输出目录运行 extract → inventory → refresh → ODB 验证 → build，原 ROOT 需对应可访问工作区，禁止写原 INP/ODB。06 的逐层坐标按 initial_profile_columns 列序存数组；节点/单元 ID 以无损等差段 [start,end_inclusive,step] 或单值存储，build 自动还原，绝无坐标采样压缩或插值。

验收结果记录在 VERIFICATION_RESULTS.json。正式九件 81 根，历史 AR3 独立 81 根；CSV 总 162 行，版本字段明确。CSV 数值字段可直接计算，无坐标插值；逐层剖面可复现有限厚度实际包围盒与初始长度，不把理论坐标当实测。下一轮可以据此采用上/下分别的实际肋线和有限厚度边界；转角理想化仍须明确模型假设。
'''
emit('05_sources_and_verification.md',sources)

# Compact original evidence: all relevant IDs and profiles are preserved, no all-model nodes dump.
profile_columns=['original_Z_mm','midplane_Y_min_mm','midplane_Y_max_mm','root_Y_mm']
def exact_runs(ids):
    seq=sorted(ids);runs=[];i=0
    while i<len(seq):
        if i+1==len(seq):runs.append(seq[i]);break
        step=seq[i+1]-seq[i];j=i+1
        while j+1<len(seq) and seq[j+1]-seq[j]==step:j+=1
        if j==i+1:runs.extend(seq[i:j+1])
        else:runs.append([seq[i],seq[j],step])
        i=j+1
    expanded=[n for run in runs for n in (range(run[0],run[1]+1,run[2]) if isinstance(run,list) else [run])]
    assert expanded==seq
    return runs
packed=copy.deepcopy(records)
for rec in packed:
    for q in rec['ribs']:
        q['initial_profile_arrays']=[[p[k] for k in profile_columns] for p in q.pop('initial_profile')]
        for field in ['element_ids','node_ids']:q[field+'_exact_runs']=exact_runs(q.pop(field))
evidence=dict(base_commit=BASE,coordinate_map=dict(x='X+B/2',y='Z-Z_start',z='Y',units='mm'),initial_profile_columns=profile_columns,formal=packed[:len(formal)],historical_AR3=packed[len(formal):])
(DEST/'06_GEOMETRY_EVIDENCE.json').write_text(json.dumps(evidence,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8')
for name in ['ODB_GEOMETRY_VERIFICATION.json','VERSION_INVENTORY.json']:
    if (WORK/name).resolve()!=(DEST/name).resolve():shutil.copyfile(WORK/name,DEST/name)
(DEST/'scripts').mkdir(exist_ok=True)
for name in ['extract_geometry.py','verify_odb_geometry.py','inventory_versions.py','refresh_variants.py','build_ledgers.py']:
    src=SCRIPT_DIR/name
    if src.resolve()!=(DEST/'scripts'/name).resolve():shutil.copyfile(src,DEST/'scripts'/name)

checks=[]
for r in records:
    rs=r['ribs'];gs=groups(r);b=r['width_mm']
    assert len(rs)==9 and [len(qs) for s,qs in gs]==[4,5]
    assert sum(q['element_count'] for q in rs)==r['PBL_element_count']
    ids=[e for q in rs for e in q['element_ids']];assert len(ids)==len(set(ids))
    assert all(q['rib_type']=='LONGITUDINAL' and q['reference_flat_plane_span_mm']<1e-7 and q['thickness_mm']==4 for q in rs)
    assert all(abs(q['height_min_mm']-41)<1e-4 and abs(q['height_max_mm']-41)<1e-4 and abs(q['axial_length_mm']-r['length_mm'])<1e-5 for q in rs)
    assert all(q['direct_named_end_set_coverage']=='COMPLETE' and q['shared_root_node_count']>0 and q['hole_boundary_loop_count']==0 for q in rs)
    for s,qs in gs:
        xs=[q['reference_x_mm'] for q in qs];widths=[y-x for x,y in zip([0]+xs,xs+[b])];assert abs(sum(widths)-b)<1e-7
        assert all(abs(y-x-.225*b)<1e-6 for x,y in zip(xs,xs[1:]))
    assert r['half_wave_length_mm']==b
    source_status='NOT_FOUND_SOURCE_OFFLINE'
    if Path(r['source']).exists():
        assert hashlib.sha256(Path(r['source']).read_bytes()).hexdigest()==r['sha256'];source_status='SHA256_MATCH'
    checks.append(dict(case=r['case'],version=r['version'],status='PASS_GEOMETRY_ONLY',source_SHA_recheck=source_status,longitudinal_ribs=9,transverse_ribs=0,top=4,bottom=5,unique_PBL_elements=len(ids),end_tie_coverage='COMPLETE',holes=0,N4_whole_line_matches=1))
with (DEST/'01_nine_specimens_rib_coordinates.csv').open(encoding='utf-8-sig',newline='') as f:
    roundtrip=list(csv.DictReader(f));assert len(roundtrip)==162
assert set(r['case'] for r in formal)==set(CASES)==set(r['case'] for r in variants)
assert all(o['status']=='MATCH' for o in odb)
report=dict(status='PASS_GEOMETRY_ONLY_NOT_THEORY_BOUNDARY_PASS',CSV_rows=162,formal_cases=9,formal_longitudinal=81,formal_transverse=0,historical_AR3_cases=9,historical_AR3_longitudinal=81,AR1='NOT_FOUND',ODB_geometry_max_difference_mm=max(o['max_coordinate_difference_mm'] for o in odb),checks=checks)
(DEST/'VERIFICATION_RESULTS.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
manifest=[]
for p in sorted(DEST.rglob('*')):
    if p.is_file() and p.name!='FILE_MANIFEST.json':manifest.append(dict(path=str(p.relative_to(DEST)).replace('\\','/'),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
(DEST/'FILE_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(output=str(DEST),formal_ribs=81,historical_AR3_ribs=81,CSV_rows=162,files=len(manifest)+1,total_bytes=sum(q['bytes'] for q in manifest)),ensure_ascii=False))
