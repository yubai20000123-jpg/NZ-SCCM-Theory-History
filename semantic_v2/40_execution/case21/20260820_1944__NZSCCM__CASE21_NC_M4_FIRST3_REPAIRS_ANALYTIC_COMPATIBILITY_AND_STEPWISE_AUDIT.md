# NZ-SCCM — Case21 NC-M4 前三项修复：尺度、TC压缩软化、泊松耦合；解析框架兼容性与逐步审计

时间：2026-08-20 19:44 +08:00

状态：`FIRST3_REPAIRS_EXECUTED / STRUCTURAL_REDUCTION_UNTOUCHED / ANALYTIC_FRAMEWORK_PRESERVED`

本节点严格只处理此前根因审计中的前三项：

1. TC 压缩削弱的拉应变尺度错误；
2. 当前 `1/(1+0.15 t^2)` 对 Case21 过度削弱压缩；
3. NC-M4 丢失 `nu` / 双轴泊松耦合。

不修改第4项结构运动学降阶：仍保持当前 `(Delta,A,epsilon_m)` 三变量、一个连续完整半波、Nguyen二阶形函数。钢筋保持 Case21 `hr=0` 解析项。

## A. 固定输入

Case21:

- `b=ell=1220 mm`
- `h=19.30 mm`
- `fc=21.23 MPa`
- `E0=20321 MPa`
- `eps_c0=0.00209`
- `nu=0.18`
- `A0=3.05 mm`
- `ft=0.1 fc=2.123 MPa` (project rule when tensile strength absent)
- `eps_t0=0.0967635 ft/E0=1.01091929777e-5`
- rebar: `p=0.75%`, `rho_x=rho_y=0.00375`, `hr=0`, `Es=200000 MPa`.

Original NC-M4 tension and compression backbones remain unchanged:

\[
C(c)=\frac{2c}{1+c^2},
\]

\[
T_4(t_T)=1.07515\frac{t_T(t_T+0.09)}{1-0.83t_T+1.04t_T^2+0.14t_T^3},
\qquad t_T=\varepsilon_t/\varepsilon_{t0}.
\]

## B. Repair 1 — separate the compression-softening coordinate from the T4 coordinate

The old NC-M4 incorrectly reused `t_T=eps_t/eps_t0` inside the TC compression-softening factor.

First diagnostic correction only:

\[
\varepsilon_{cr}=\frac{f_t}{E_0},
\qquad
r_t=\frac{\varepsilon_t}{\varepsilon_{cr}},
\]

\[
\beta_{scale}(r_t)=\frac{1}{1+0.15r_t^2}.
\]

For Case21:

\[
\varepsilon_{cr}=1.04473205\times10^{-4},
\qquad
\varepsilon_{cr}/\varepsilon_{t0}\approx10.3345.
\]

### Analytic compatibility

This repair replaces one rational argument by another linear rescaling of the same principal strain. Under the half-angle + one-radical field used by the existing exact integration compiler, no new algebraic generator or spatial subdivision is introduced. `ANALYTIC_GATE_R1=PASS`.

### Direct-continuous audit (nonproduction)

Origin-connected equilibrium branch with rebar retained, converged audit around `32x32x20`:

\[
\Delta_u\approx0.76247\ \mathrm{mm},\quad
A_u\approx5.0645\ \mathrm{mm},\quad
\varepsilon_{m,u}\approx-2.3274\times10^{-5},
\]

\[
P_u\approx245.10\ \mathrm{kN}.
\]

Orders 24/16, 28/18, 32/20, 36/24 give approximately 245.45, 245.24, 245.10, 245.14 kN. Therefore scale repair alone does not recover Case21; the functional form remains too destructive after full equilibrium re-solution.

## C. Repair 2 — replace the ad-hoc beta with Nguyen Eq. (3.43) source compression-softening factor

Nguyen cracked TC compression uses the coexisting tensile strain to reduce the compressive peak. In positive-magnitude `eps_c0` notation the source form is

\[
\gamma_c(\chi)=\min\left(1,\frac{1}{0.8+0.34\chi}\right),
\qquad
\chi=\frac{\varepsilon_t}{\varepsilon_{c0}}.
\]

Equivalently,

\[
\gamma_c(\chi)=
\begin{cases}
1,&0\le\chi\le10/17,\\
(0.8+0.34\chi)^{-1},&\chi>10/17.
\end{cases}
\]

This supersedes `beta_scale` for TC/CT compression. T4 still uses its own `eps_t0`; the compression softening now has its own physically distinct coordinate `eps_t/eps_c0`. The notation `gamma_c` is used to avoid confusion with Nguyen's separate shear-retention beta parameters.

TC/CT repaired scalar compression is therefore

\[
\bar\sigma_c=-f_c\gamma_c(\varepsilon_t/\varepsilon_{c0})C(c).
\]

### Analytic compatibility

Each branch of `gamma_c` is rational. The only added front is

\[
\varepsilon_t=\frac{10}{17}\varepsilon_{c0},
\]

which is an algebraic level set of the same principal-strain field. After the same residue lift it is an additional relative boundary, not a numerical spatial cell. The existing relative/incomplete GKZ architecture remains valid. `ANALYTIC_GATE_R2=PASS`.

### Same-point diagnostic at the previously successful Case21 center state

Using the old successful physical center strains

\[
\varepsilon_1=2.9758204\times10^{-4},\qquad
\varepsilon_2=-1.6461923\times10^{-3},
\]

we have

\[
\chi=\varepsilon_1/\varepsilon_{c0}=0.14238<10/17,
\]

so

\[
\gamma_c=1.
\]

The retained compression backbone gives

\[
-f_c C(-\varepsilon_2/\varepsilon_{c0})\approx-20.639\ \mathrm{MPa},
\]

compared with the old successful R10 value about `-20.600 MPa`. This confirms that the main prior loss was the TC reduction, not the compression backbone.

### Direct-continuous audit after Repairs 1+2, before Poisson repair

Origin-connected branch, rebar retained:

32/20 checkpoint:

\[
\Delta_u\approx2.09005\ \mathrm{mm},\quad
A_u\approx25.3558\ \mathrm{mm},\quad
\varepsilon_{m,u}\approx6.1157\times10^{-4},
\]

\[
P_u\approx331.946\ \mathrm{kN}.
\]

Convergence: 24/16 `331.789`, 28/18 `332.039`, 32/20 `331.946`, 36/24 `331.943 kN`.

Thus replacing the over-strong beta by source Eq. (3.43) recovers roughly 46 kN relative to the original 286.12 kN model, but the result remains below the 368.313 kN experiment.

## D. Repair 3 — restore Poisson/biaxial coupling without reopening the structural kinematics

Nguyen Eq. (3.21) expresses physical principal strains through equivalent-uniaxial strains. To preserve a closed analytic current operator while restoring the exact isotropic small-strain limit, use the constant-`nu` closed form of Eq. (3.21):

\[
\varepsilon_1=\widehat\varepsilon_1-\nu\widehat\varepsilon_2,
\qquad
\varepsilon_2=\widehat\varepsilon_2-\nu\widehat\varepsilon_1.
\]

Hence

\[
\boxed{\widehat\varepsilon_1=\frac{\varepsilon_1+\nu\varepsilon_2}{1-\nu^2}},
\qquad
\boxed{\widehat\varepsilon_2=\frac{\varepsilon_2+\nu\varepsilon_1}{1-\nu^2}}.
\]

Tensor form:

\[
\boxed{
\widehat{\mathbf E}
=\frac{(1-\nu)\mathbf E+\nu\,\operatorname{tr}(\mathbf E)\mathbf I}{1-\nu^2}.
}
\]

Because `Ehat = a E + b tr(E) I`, it commutes with `E` and has exactly the same principal directions. The scalar NC-M4 backbones are evaluated using `epshat_i`, while the Nguyen Eq. (3.43) compression-softening argument remains the coexisting physical tensile principal strain `eps_t/eps_c0`.

This is a minimal closed-form Poisson restoration, not the full nonlinear secant-dependent Darwin-Pecknold dilation iteration. The latter is intentionally not activated in this first-three-issue repair because it would introduce additional implicit algebraic material equations; the present form exactly restores the isotropic plane-stress small-strain limit and keeps the existing direct analytic compiler structure.

### Linear-limit proof

For small strain, `sigmahat_i=E0 epshat_i`, hence

\[
\sigma_1=\frac{E_0}{1-\nu^2}(\varepsilon_1+\nu\varepsilon_2),
\]

\[
\sigma_2=\frac{E_0}{1-\nu^2}(\varepsilon_2+\nu\varepsilon_1),
\]

which is exactly isotropic plane stress. In free uniaxial compression, `sigma_1=0` yields `eps_1=-nu eps_2`, so Poisson expansion is no longer incorrectly interpreted as independent tensile material strain.

### Analytic compatibility proof

Since `Ehat` is linear in `E` and `tr(E)`, its eigenvalues are linear combinations of the same two principal strains. Therefore the only existing square-root generator `W=sqrt((ex-ey)^2+gamma^2)` remains the only principal-direction radical. `T4`, `C`, and each branch of `gamma_c` are rational functions of quantities in the same algebraic field. No new spatial quadrature, material point, or new transcendental generator is required. `ANALYTIC_GATE_R3=PASS`.

### Same-point check

At the old successful Case21 center state and `nu=0.18`:

\[
\widehat\varepsilon_1\approx1.30986\times10^{-6},
\qquad
\widehat\varepsilon_2\approx-1.64596\times10^{-3}.
\]

Thus the large physical transverse tensile strain is almost entirely recognized as Poisson dilation; the equivalent tensile material strain is nearly zero. Meanwhile `chi=eps1/eps_c0=0.14238<10/17`, so `gamma_c=1`, and the compressive scalar backbone remains about `-20.64 MPa`.

### Direct-continuous audit after Repairs 1+2+3

Current structural kinematics is deliberately left unchanged. Rebar remains exact `hr=0` terms.

Converged audit:

| concrete audit order | Delta_u mm | A_u mm | eps_m | Pu kN |
|---|---:|---:|---:|---:|
|24x24x16|2.44447|26.6786|7.0651e-4|325.734|
|28x28x18|2.45394|26.7838|6.9761e-4|325.812|
|32x32x20|2.40901|26.3745|6.9483e-4|325.871|
|36x36x24|2.44179|26.6656|7.0062e-4|325.805|

Use the 32/20 checkpoint for detailed comparison:

\[
\boxed{\Delta_u\approx2.40901\ \mathrm{mm}},
\]

\[
\boxed{A_u\approx26.3745\ \mathrm{mm}},
\]

\[
\boxed{\varepsilon_{m,u}\approx6.9483\times10^{-4}},
\]

\[
\boxed{P_u^{R123,audit}\approx325.871\ \mathrm{kN}}.
\]

Relative to the correct experiment `368.31275 kN`, the remaining deficit is approximately

\[
-42.44\ \mathrm{kN}\approx-11.52\%.
\]

## E. Stepwise interpretation

- Original NC-M4 + current 3-variable kinematics + hr=0 rebar audit: about `286.12 kN`.
- Repair 1 only (correct tensile scale but keep old beta form): about `245.1 kN`; this proves the old beta functional shape itself is unacceptable.
- Repairs 1+2 (Nguyen Eq. 3.43 compression softening): about `331.94 kN`; major recovery.
- Repairs 1+2+3 (plus constant-nu equivalent-uniaxial Poisson coupling): about `325.8 kN`; physically correct small-strain coupling is restored, but the remaining gap is still about 11.5%.

The nonmonotonic numerical changes between repair stages are not used as calibration targets; each stage re-solves the full equilibrium branch. No parameter is adjusted to match the experiment.

## F. Locked conclusion

1. The first three repairs can be made without destroying the previously established exact analytic integration architecture.
2. Repair 2 is the dominant correction: the prior TC beta was the main direct constitutive error.
3. Repair 3 restores the correct small-strain plane-stress/Poisson limit while preserving the same principal directions and same one-radical algebraic field.
4. Even after the first three repairs only, the current reduced structural kinematics still gives about `325.8 kN`, leaving ~`42.5 kN` below experiment.
5. Per user instruction, structural issue 4 is NOT modified in this node. The large resulting `A_u≈26 mm` is retained as a diagnostic signal, not repaired here.
6. Formal zero-spatial integration remains the target; Gauss values above are independent numerical audits only and have no production identity.
