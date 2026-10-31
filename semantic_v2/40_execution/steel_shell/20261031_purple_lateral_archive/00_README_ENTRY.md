# 2026-10-31 UCFT Purple Shell Archive — Entry Point

Status: FROZEN DIAGNOSTIC SNAPSHOT. Not a verified steel-shell or UCFT ultimate-load prediction.

## Source of truth
- [01_theory_locked.md](01_theory_locked.md): geometry -> membrane -> Lagrange 7 conditions -> projected Mises quadratic -> vertex two-chord -> bending-energy recovery -> two-modal capacity -> R_W,R_A,R_perp.
- [02_UHPC_seven_condition_audit.md](02_UHPC_seven_condition_audit.md): physical limits of signed Lagrange weighting and recommended positive-weight seven Bernstein conditional moments for UHPC C1.
- [source/geometry_projection_derivation.md](source/geometry_projection_derivation.md): original 2026-10-31 detailed derivation.
- [source/rebuild_lateral.py](source/rebuild_lateral.py): two-modal nonlinear transverse-release solver.
- [source/purple_projection_kernel.py](source/purple_projection_kernel.py): thickness-projected Mises material and vertex split.
- [source/fourier_exact.py](source/fourier_exact.py): exact Fourier integration.
- [source/check_geometry_energy.py](source/check_geometry_energy.py): elastic consistency checks.
- [source/roots_check.py](source/roots_check.py): candidate root diagnostics.
- [data/trial_fixed_20261031.csv](data/trial_fixed_20261031.csv): fixed d scan, separate A=0 boundaries.
- [data/phase_scan_20261031.csv](data/phase_scan_20261031.csv): sampled softening-range audit.
- [04_SHA256_文件清单.json](04_SHA256_文件清单.json): SHA256 for the original local complete backup ZIP extraction. GitHub normalized UTF-8 line endings may differ from these byte hashes.

## Governance
1. Keep original October 25 pure-steel purple unchanged.
2. New transverse average membrane-force condition R_perp = 0 is user-specified for the *independent* trial steel plate.
3. Current two-modal membrane capacity remains a proposed structural approximation; A>0 stable postbuckling and Pu have NOT been established.
4. Nonlinear algebraic unknowns are (W,A,e_perp) at prescribed axial d; six in-plane Fourier coordinates are elastically condensed by a constant linear system.
5. Do not substitute seven Bernstein conditions for seven signed Lagrange nodes without a new model identity. For UHPC C1 prefer positive seven Bernstein conditions while using the shared exact moment/integration and generalized-work architecture.
6. No FEM fitting, area Gauss or mesh integration was used in this recorded variant.
7. Independent trial b=a=2500/5000 mm, t=4 mm, N=5,m=4, E=206000 MPa, nu=0.3, fy=355 MPa, W0=b/400,A0=t/60; sampled loads are NOT ultimate loads.

Complete ZIP backup is preserved as a conversation artifact and in personal Library at /NZ-SCCM/20261031_紫线钢壳横向释放归档/完整源包.zip (Library is distinct from native Project attachment membership).
