# BH100 λ-w 六状态执行 R05

日期：2026-10-06
分支：diagnostic/20261006-bh100-uhpc-we-wp-d-self-consistency

## 1. 本轮不是继续改形函数

保留：
- 单一整体几何族；
- 六个内部状态 \(D_c^*,p_c,D_+^*,p_+,D_-^*,p_-\)；
- 外部路径坐标 \(\lambda,w\)；
- UC141 连续单调材料多项式；
- Yun 局部大挠度平均应力、应变-幅值兼容、理想塑性强度上限。

不引入 \(\phi_{13}\)、高阶 Ritz 或 FEM 受力占比标定。

BH100 当前几何材料：
\[
b=5000\ {\rm mm},\qquad a_h=b=5000\ {\rm mm},\qquad L=2a_h=10000\ {\rm mm},
\]
\[
t_c=42\ {\rm mm},\quad t_s=4\ {\rm mm},\quad
w_0=12.5\ {\rm mm},
\]
\[
E_c=43400\ {\rm MPa},\quad E_s=206000\ {\rm MPa},\quad
\nu_c=\nu_s=0.30,\quad f_y=355\ {\rm MPa}.
\]

Project geometry source also gives:
\[
A_w=1332\ {\rm mm^2},
\]
hence BH100
\[
\rho_w=\frac{1332}{5000\times42}=0.006342857143,
\qquad
1-\rho_w=0.993657142857.
\]

Thus PBL/web occupied-area correction is only \(0.6343\%\) of the nominal UHPC core area. It cannot explain a 20–35% force discrepancy.

## 2. λ-w reduced equilibrium execution

For each prescribed \(w\), solve common axial compression \(\lambda\) from the reduced transverse/overall virtual-work equilibrium and solve transverse mean strain from \(R_x=0\).

UHPC:
- UC141 monotone polynomial material law;
- plastic-reference amplitude \(p_c\) updated with independent \(\lambda\);
- damage supplies current recoverable flexural retention.

Steel:
- Yun exact strain-amplitude compatibility
\[
\varepsilon_s=\frac{\sigma_Y}{E_s}
+C_\varepsilon(2A_0A+A^2)
\]
is used;
- Yun average stress retained below \(f_y\);
- steel top/bottom symmetric in this BH100 diagnostic.

Computed window:

| w / mm | λ | Δ=λL / mm | p_c / mm | ρ_D,c | raw P_c / MN | raw P_s+ / MN | raw P_s- / MN | raw P / MN | Yun A / mm | Yun σ / MPa |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|80.000|0.00151763|15.1763|10.5589|0.874785|10.2494|3.3554|3.3554|16.9601|5.0345|167.77|
|82.500|0.00158197|15.8197|11.1934|0.867395|10.6426|3.4793|3.4793|17.6011|5.1492|173.96|
|85.000|0.00164777|16.4777|11.8361|0.860179|11.0438|3.6058|3.6058|18.2554|5.2641|180.29|
|87.323|0.00171053|17.1053|12.4333|0.855351|11.4269|3.7266|3.7266|18.8800|5.3717|186.33|
|90.000|0.00178505|17.8505|13.0676|0.849447|11.8818|3.8699|3.8699|19.6215|5.4972|193.49|
|92.500|0.00185406|18.5406|13.7090|0.842329|12.2988|≈3.998|≈3.999|20.2953|5.6095|≈200.03|
|95.000|0.00191968|19.1968|14.4049|0.834018|12.6843|≈4.105|≈4.110|20.8995|5.7105|206.01|

At the DIRECT peak geometry \(w=87.323\) mm:
\[
\Delta_{\rm theory}=17.1053\ {\rm mm}
\]
while DIRECT gives
\[
\Delta_{\rm DIRECT}=17.478\ {\rm mm}.
\]
Relative difference:
\[
-2.13\%.
\]

This is an independent validation of the repaired kinematic/path decomposition. The measured axial shortening was not used to generate the theoretical \(\lambda\).

Also:
\[
p_c=12.433\ {\rm mm},
\]
instead of the old \(w\)-only R03 result \(p_c\approx60.25\) mm at the same geometry.

Therefore the runaway permanent-reference mapping in R03 was primarily caused by eliminating the independent axial membrane coordinate.

## 3. Actual \(A_w\) does not repair the raw force

At \(w=87.323\):
\[
1-\rho_w=0.993657.
\]
If the raw UHPC force above had not already been area-corrected, the maximum area-only correction would be:
\[
11.4269\times0.993657=11.3544\ {\rm MN}.
\]
It remains far above the desired component scale.

Thus PBL/web occupied area is not the missing mechanism.

## 4. Steel tangent cannot be multiplied into finite force

At \(w=87.323\), the Yun compatibility state gives approximately:
\[
A=5.3717\ {\rm mm},\qquad
\sigma_Y=186.33\ {\rm MPa}<f_y.
\]
The corresponding Yun effective tangent is approximately:
\[
E_Y^{tan}\approx145.15\ {\rm GPa},
\qquad
E_Y^{tan}/E_s\approx0.7046.
\]

It is tempting to multiply the raw finite steel force by 0.7046, which would numerically give about 2.63 MN per shell. This operation is REJECTED as a production formula.

Reason:
- \(E_Y^{tan}\) is \(d\sigma/d\varepsilon\), a tangent stiffness;
- \(\sigma_Y\) is the finite stress itself;
- tangent stiffness is allowed in equilibrium/stability linearization but cannot reconstruct finite stress by a simple multiplicative factor.
This matches the existing project rule for ideal elastoplastic steel: finite stress and tangent stiffness must not be conflated.

## 5. Physical status after R05

Two facts are now separated:

### PASS — path kinematics
The pair \((\lambda,w)\) with independent axial membrane compression repairs the gross kinematic inconsistency:
- peak geometry \(w=87.323\) predicts \(\Delta\) within ~2.1%;
- UHPC permanent reference amplitude falls from ~60 mm to ~12.4 mm.

### FAIL — finite force condensation
The raw finite-force recovery still gives:
\[
P_c\approx11.43\ {\rm MN},
\quad
P_s^+\approx3.73\ {\rm MN},
\quad
P_s^-\approx3.73\ {\rm MN},
\]
\[
P\approx18.88\ {\rm MN}.
\]

This is not a failure of the repaired \((\lambda,w)\) geometry. It means the proposed six-state statement
\[
(D_j^*,p_j)\rightarrow P_j
\]
has not yet been derived consistently from virtual work.

In particular, \(D_j^*\) is a tangent/energy quantity. A finite axial force cannot be obtained by multiplying raw material force by an arbitrary stiffness-retention factor.

## 6. Correct R06 target

The next derivation must start from one common reduced free/real-work functional for each plate \(j\):
\[
\mathcal W_j(\lambda,w,p_j)
=
\int_{V_j}
\int_0^{\varepsilon_j^e}
\sigma_j(\eta)\,d\eta\,dV
+
\text{plastic-reference constraint terms},
\]
with steel Yun local geometry condensed internally.

Then define:
\[
P_j=\frac{\partial\mathcal W_j}{\partial\Delta},
\qquad
R_{p,j}=\frac{\partial\mathcal W_j}{\partial p_j}=0,
\qquad
D_j^*=\frac{\partial^2\mathcal W_j}{\partial\kappa_j^2}.
\]

This forces finite force, permanent geometry and current rigidity to be derivatives of ONE scalar work object. It prevents:
- using damage twice;
- using plastic strain twice;
- multiplying finite stress by a tangent-retention factor;
- inventing empirical \(\rho_D^2\) or \(\rho_E\) force corrections.

R06 should therefore derive this common work object first and then rerun the same \(w=80\)–95 mm window.
