# 紫线＋钢壳双模态＋横向平均膜力零：解析模型研究包

运行（需要 numpy, scipy）：

```
python check_geometry_energy.py
python rebuild_lateral.py
python roots_check.py
```

所有板面积分基于闭式Fourier卷积，无Gauss、Simpson或板面离散。

- `理论重建与验收.md`：完整公式合同、物理假定、非线性释放和已知未闭合环节。
- `purple_projection_kernel.py`：前次双模态紫线7节点及顶点双弦材料算法的**本地固定副本**。注意该文件存在早期未锁定的双模态容量函数；真正本轮修订的调用入口是`rebuild_lateral.py`。
- `rebuild_lateral.py`：加入横向独立变量、重算七节点投影及Ritz临界阈值；两模态正向膜容量是明确的新结构代理。
- `fourier_exact.py`：三角函数Fourier精确积分，无空间数值求积。
- `check_geometry_energy.py`：弹性投影内能的梯度检查。
- `roots_check.py`：候选根试算，不是经验证的稳定路径。
- `roots_2size.csv`：当前全部找到的单侧合格候选根，仅用于审计。A=0的边界条件与内部根区分。

不要直接用这版新候选根报告钢壳或UCFT极限承载力。横向平均膜力零本身已经闭合；新紫线两模态膜容量并未通过全过程数值验证。