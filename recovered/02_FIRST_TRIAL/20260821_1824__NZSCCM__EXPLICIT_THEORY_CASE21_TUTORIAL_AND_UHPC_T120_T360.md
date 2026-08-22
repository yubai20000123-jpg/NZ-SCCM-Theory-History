# NZ-SCCM — 显式理论 Case21 教学算例 + UHPC T120/T360 直接极限承载力

时间：2026-08-21 18:24 +08:00  
理论基线：`MARGUERRE_AIRY_EXPLICIT_LIMIT_THEORY_V1`  
状态：`EXECUTED / NO LOAD-PATH TRACKING / NO RITZ ORDER / NO FORMAL SPATIAL QUADRATURE`

## A. Swartz Case21 教学算例

原始输入：

- `a_phys=2440 mm, b=1220 mm, t=19.30 mm`;
- `fc=21.23 MPa, E0=20321 MPa, eps0=0.00209, nu=0.18`;
- nominal total reinforcement ratio `rho_tot=0.0075`, one mid-plane layer;
- `rho_x=rho_y=0.00375`, `Es=200000 MPa`, `fy=530 MPa`;
- `q0=1/400=0.0025`.

单位板宽每方向钢筋面积：

`ax=ay=0.00375*19.30=0.072375 mm`; `ax+ay=0.14475 mm`.

相体积守恒后：

`teff=19.30-0.14475=19.15525 mm`.

面内刚度：

- `A11=A22=416762.9653265813 N/mm`;
- `A12=72411.83375878463 N/mm`;
- `A66=164938.06578389835 N/mm`;
- `DeltaA=1.6844789559949536e11 (N/mm)^2`.

弯曲刚度（中面钢筋 z=0）：

- `Dx=Dy=12581716.557892382 N mm`;
- `Dmu=2264708.9804206286 N mm`;
- `D66=5158503.788735877 N mm`;
- `H=Dmu+2D66=12581716.557892382 N mm`.

整数半波候选：

|j|ell=a/j mm|Pcr kN|
|---:|---:|---:|
|1|2440.000|636.150436|
|2|1220.000|407.136279|
|3|813.333|477.819661|
|4|610.000|636.150436|
|5|488.000|856.004027|
|6|406.667|1130.934108|

所以：`m*=2`, `ell=1220 mm`, `alpha=beta=pi/1220`.

后屈曲系数：

- `Pcr=407.1362790591262 kN`;
- `C=608339.560102679 kN`;
- `G=498638.9836907205 N/mm`;
- `J=120105.20232244223 N`.

显式后屈曲关系：

\[
P_{pb}(q)=407.136279\frac{q}{q+0.0025}+608339.5601q(q+0.005)\quad kN.
\]

有限截面候选审计得到控制位置 `s*=1`。在 `0<c<t` 分支联立：

\[
n(1;q)=n_u(c),\qquad Jq=m_u(c).
\]

最终：

- `qu=0.006744947636006702`;
- `cu=16.46074830794686 mm`;
- `Pu=345.231397911789 kN`.

Pu 分项：

- linear-imperfection/buckling term `=297.0393117508868 kN`;
- postbuckling membrane-hardening term `=48.19208616090219 kN`.

控制截面 demand：

- `P/b=282.9765556654008 N/mm`;
- Airy redistribution `=-39.50170996795262 N/mm`;
- `nd=243.47484569744816 N/mm`;
- `md=Jq=810.1033004768634 N`.

截面 capacity：

- gross concrete `Nc=232.97445771847455 N/mm`;
- gross concrete `Mc=810.103300476698 N`;
- centered rebar depth from compressed face `ys=9.65 mm`;
- concrete stress replaced by rebar at ys `=13.9336531340968 MPa`;
- steel strain `=0.0008647519357754`;
- steel stress `=172.950387155 MPa < fy`;
- volume-conserving `nu=232.9744577-0.14475*13.9336531+0.072375*172.9503872=243.4748457 N/mm`;
- `mu=810.1033005 N` because z_s=0.

Thus demand=capacity simultaneously.

---

## B. UHPC replacement layer

For UHPC use the locked Hu-source uniaxial compression curve:

\[
\sigma_c=f_c\frac{n\xi-\xi^2}{1+(n-2)\xi},\quad
\xi=\varepsilon/\varepsilon_{c0},\quad
n=E_c\varepsilon_{c0}/f_c,
\quad 0\le\xi\le1.
\]

Current UCFT UHPC values:

`fc=141.1 MPa, Ec=43400 MPa, epsc0=0.0035, nuc=0.20`.

Steel:

`Es=206000 MPa, nus=0.30, fy=355 MPa`.

Define `a=n-2` and antiderivatives:

\[
F_0(\xi)=-\frac{\xi^2}{2a}+\frac{(n-1)^2}{a^2}\xi-\frac{(n-1)^2}{a^3}\ln(1+a\xi),
\]

\[
F_1(\xi)=-\frac{\xi^3}{3a}+\frac{(n-1)^2}{2a^2}\xi^2-\frac{(n-1)^2}{a^3}\xi+\frac{(n-1)^2}{a^4}\ln(1+a\xi).
\]

For neutral-axis depth `c` from the compressed UHPC face:

\[
\xi_b=\max(0,1-t_c/c),
\]

\[
N_c=f_cc[F_0(1)-F_0(\xi_b)],
\]

\[
M_c=f_cc\{(t_c/2-c)[F_0(1)-F_0(\xi_b)]+c[F_1(1)-F_1(\xi_b)]\}.
\]

No thickness quadrature is required.

---

## C. T120/T360 common whole-panel explicit front end

Current analytical wall-panel domain follows the project source idealization:

`b=a_phys=1600 mm`, `tc=42 mm`, two steel faces `ts=4 mm`, `q0=4/1600=0.0025`.

The physical CAE model is 1600 x 50 x 3000 externally with a 1592 x 42 x 3000 UHPC core; the present analytical calculation intentionally follows the historical 1600 x 1600 theoretical panel rather than the 3000-mm CAE member length.

Symmetric laminate extensional terms:

- `A11=A22=3709739.0109890113 N/mm`;
- `A12=923046.7032967033 N/mm`;
- `A66=1393346.153846154 N/mm`;
- `DeltaA=1.2910148313186814e13 (N/mm)^2`.

Bending terms:

- `Dx=Dy=1.239544088827839e9 N mm`;
- `Dmu=D12=3.4395160164835167e8 N mm`;
- `D66=4.477962435897436e8 N mm`;
- `H=1.239544088827839e9 N mm`.

Mode candidates for the 1600 x 1600 analytical panel:

|j|Pcr MN|
|---:|---:|
|1|30.5845245|
|2|47.7883195|
|3|84.9570125|
|4|138.1082434|
|5|206.7513855|

Thus `m*=1`, `ell=1600 mm`, `alpha=beta=pi/1600`.

Common explicit coefficients:

- `Pcr=30.5845244861 MN`;
- `C=6869.381173883467 MN`;
- `G=4.293363233677167e6 N/mm`;
- `J=9.767797522393651e6 N`.

\[
P_{pb}(q)=30.5845244861\frac{q}{q+0.0025}+6869.38117388q(q+0.005)\quad MN.
\]

---

## D. T120

T120 source analytical panel uses 120-mm PBL-bounded local steel strips. Source audit establishes their local buckling stress is above yielding, so the section calculation uses the project Ramberg-Osgood steel law before the `fy` plateau rather than a pre-yield local-buckling reduction:

\[
\varepsilon_s=\sigma_s/E_s+0.0005(\sigma_s/f_y)^{10},\qquad |\sigma_s|<f_y,
\]
then `|sigma|=fy` plateau.

At `s=1`, solve the explicit postbuckling demand with UHPC+two steel faces section capacity.

Result:

- `qu=0.001535717246892525`;
- `cu=81.13530691320507 mm`;
- `Pu,T120=11.70732084978392 MN`.

Pu split:

- `11.638372776852666 MN` from the imperfection/buckling term;
- `0.0689480729312603 MN` from nonlinear membrane hardening.

At the controlling section:

- `Nc=4628.450634113023 N/mm`;
- `Mc=10527.819201888098 N`;
- compressed-face steel strain `0.00358627563346113`, hence `sigma_top=355 MPa` plateau;
- opposite-face strain `0.00160193606385513`, R-O inversion gives `sigma_bottom=306.383087854 MPa`;
- steel axial `Ns=2645.532351416559 N/mm`;
- steel moment `Ms=4472.755917419141 N`;
- total `n=7273.98298553 N/mm`, `m=15000.5751193 N`.

---

## E. T360

T360 analytical steel-face partition is `[80,360,360,360,360,80] mm`. The 360-mm panels use the source Yun local-postbuckling mean-stress relation with:

`B=360 mm, A0=0.225 mm, kcrx=10.84493827, kp=43.31003106`.

\[
\sigma_Y(A)=\left[k_{crx}\frac{A}{A+A_0}+k_p(1-\nu_s^2)\frac{2A_0A+A^2}{t_s^2}\right]\frac{\pi^2E_st_s^2}{12(1-\nu_s^2)B_s^2}.
\]

Verified source branch points:

- `sigma_cr=249.279401243 MPa`;
- `eps_cr=0.001224667229`;
- `Acr=0.7887844399 mm`;
- `Au=1.09111429 mm`;
- `sigma360,u=301.871332929 MPa`;
- `eps_u=0.001560432324`.

Because Yun stress is a panel-average stress, use exact panel averages rather than a center-point sample. For the inner 360-mm panel `[x0,x1]=[440,800] mm`:

\[
\bar s=\frac1{360}\int_{440}^{800}\sin(\pi x/1600)dx=0.918781041539,
\]

\[
\overline{s^2}=\frac1{360}\int_{440}^{800}\sin^2(\pi x/1600)dx=0.849323292533.
\]

Thus:

\[
\bar n=P_{pb}(q)/1600+Gq(q+2q_0)[1-2\overline{s^2}],
\]

\[
\bar m=Jq\bar s.
\]

Solve with the UHPC section integral and the two local 360-mm steel-face laws.

Result:

- `qu=0.001402606680567288`;
- `cu=75.9449850229306 mm`;
- `Pu,T360=11.0538445835073 MN`.

Pu split:

- `10.992155212505 MN` imperfection/buckling term;
- `0.061689370997 MN` membrane hardening.

Controlling inner-panel average demand:

- `n=6881.71594695 N/mm`;
- `m=12587.64762284 N`.

UHPC:

- `Nc=4521.15940256 N/mm`;
- `Mc=11336.12288509 N`.

Steel faces:

- compressed-face strain `0.003592171985 > eps_u`, hence `sigma_top=301.871332929 MPa` local-postbuckling plateau;
- opposite-face strain `0.001472216336`, Yun inversion gives `A=1.01515914809 mm`, `sigma_bottom=288.267803170 MPa`;
- `Ns=2360.55654440 N/mm`;
- `Ms=1251.52473776 N`.

Capacity/demand closure:

`4521.15940256+2360.55654440=6881.71594696 N/mm`,

`11336.12288509+1251.52473776=12587.64762285 N`.

Ratio:

\[
P_{u,T360}/P_{u,T120}=0.944182254,
\]

so T360 is `5.5818%` below T120 under this explicit source-consistent calculation.

---

## F. Status

These T120/T360 values are predictions of the current explicit Marguerre-Air y + section-capacity theory with the locked UHPC source curve and source local-steel laws. No FEM/test ultimate load is used to select `q,c`, coefficients, local branch, or stopping criterion.
