# Zhou Table 5.1 screen and formula-comparison validation

Date: 2026-08-14 14:05 Asia/Tokyo

## 1. Scope

This validation executes the requested source-only screen of Zhou Siming, Table 5.1, for a four-edge simply-supported axial-compression source point satisfying

\[
 b_s/t_s \gtrsim 56,
\]

before activating the already-compiled `R10 + N48-C1/MM + Cayley-Hamilton + general-D15 + double outer steel shell + Yun-Lu local postbuckling` branch.

No synthetic plate thickness, panel width, yield stress, or experimental load is introduced.

## 2. Zhou Table 5.1 source audit

Source: Zhou Siming, *Stability performance of multi-celled concrete-filled steel tubular walls under complex boundary conditions*, Chapter 5, Table 5.1, p.149.

Table 5.1 gives the following four parameter groups for four-edge simply-supported walls under axial compression:

| group | ns | ls (mm) | h (mm) | ts (mm) | fy (MPa) | fcu (MPa) | a (mm) | b (mm) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 30 | 200 | 100-130 | 4 | 235-460 | 40 | 6000 | 6000 |
| 2 | 30 | 200 | 100-130 | 4 | 355 | 40-60 | 6000 | 6000 |
| 3 | 40 | 200 | 100-200 | 4 | 355 | 40 | 6000 | 8000 |
| 4 | 10-60 | 200 | 100-130 | 4 | 355 | 40 | 3000-9000 | 2000-12000 |

For the local steel-wall subpanel in this source family,

\[
 b_s=l_s=200\;\mathrm{mm},\qquad t_s=4\;\mathrm{mm},
\]

hence every Table 5.1 point has

\[
\boxed{b_s/t_s=200/4=50.}
\]

Therefore

```text
ZHOU_TABLE5_1_BS_TS_GE56_SCREEN = EMPTY
ZHOU_TABLE5_1_MAX_BS_TS = 50
MATCH_COUNT = 0
```

The requested clean Yun-Lu source benchmark cannot be generated from Table 5.1 without inventing a non-source thickness or local panel width. Such invention is prohibited.

This is a source-parameter-space gate, not a solver failure.

## 3. Consequence for the requested Yun-Lu event sequence

Because the source screen is empty, no new Table-5.1 calculation is permitted for

\[
B_s\rightarrow S1_{\rm Yun}\rightarrow Y_s\rightarrow K_Z/L.
\]

Status:

```text
R10_D15_DOUBLE_SHELL_NEW_RUN_FROM_TABLE5_1 = NOT_STARTED_SOURCE_SET_EMPTY
CLEAN_YUN_POSTBUCKLING_RESERVE_FROM_TABLE5_1 = NOT_IDENTIFIABLE
SYNTHETIC_ts_3mm_OR_bs_GT_200 = PROHIBITED
```

The previously executed real Table-5.1 reference point (`a=b=6000 mm, h=130 mm, ts=4 mm, fy=355 MPa, fcu=40 MPa`) remains useful as a negative mechanism benchmark: the reduced double-shell nonlinear branch reached a first-load-maximum neighbourhood before the local-shell buckling event.

## 4. Missing comparison repaired: Zhou formula replay

### 4.1 Same-object reduced-section strength comparator

Zhou gives the axial cross-section strength formula

\[
P_{yth}=f_yA_s+f'_cA_c,
\]

with

\[
f'_c=0.76 f_{cu}.
\]

To make the comparison physically consistent with the project reduction already used in the previous run, the internal web steel remains removed from steel-bearing identity and is absorbed into the continuous concrete core. Thus for the reduced two-outer-shell object:

\[
A_s^{red}=2bt_s=2\times6000\times4=48000\;\mathrm{mm^2},
\]

\[
A_c^{red}=b(h-2t_s)=6000\times122=732000\;\mathrm{mm^2},
\]

\[
f'_c=0.76\times40=30.4\;\mathrm{MPa}.
\]

Hence

\[
P_{s,yth}^{red}=355\times48000=17.0400\;\mathrm{MN},
\]

\[
P_{c,yth}^{red}=30.4\times732000=22.2528\;\mathrm{MN},
\]

and

\[
\boxed{P_{yth}^{red}=39.2928\;\mathrm{MN}.}
\]

The previous reduced nonlinear NZ-SCCM branch diagnostic first-load-maximum neighbourhood was

\[
P_{NZ,diag}=26.1085\;\mathrm{MN}.
\]

Therefore

\[
\boxed{P_{NZ,diag}/P_{yth}^{red}=0.6644602},
\]

or

\[
\boxed{(P_{NZ,diag}-P_{yth}^{red})/P_{yth}^{red}=-33.5540\%}.
\]

This is the previously missing numerical comparison to a Zhou formula.

### 4.2 Identity boundary of this comparison

`P_yth^red` is **not** Zhou's original full multi-cell Table-5.1 wall strength, because the project reduction intentionally deletes the internal web steel as an independent steel-bearing term. It is Zhou Eq.(3-2)/(3-3) replayed on exactly the same reduced two-shell + concrete object used by NZ-SCCM.

Likewise, `P_NZ,diag=26.1085 MN` is still a diagnostic branch-peak neighbourhood from the preceding run, not yet the final production `Rq=0 + L=0` root. It must not be relabelled as a frozen production `Pu`.

## 5. Zhou elastic-stability formula comparison boundary

For four-edge simply-supported axial compression, Zhou Eq.(5-79) is

\[
N_{cr,m}=\pi^2\left[
\frac{D_xa^2}{m^2b^4}+\frac{2H}{b^2}+\frac{D_ym^2}{a^2}
\right].
\]

This formula is retained as the correct Zhou/Navier elastic-stability comparator. However, a literal numerical replay of the **original MCFSTW** Eq.(5-79) requires the original multi-cell `D_y`, `D_{xy}`, `D_mu`, and `H`, whose values include the internal cell/web topology. Those terms are intentionally absent from the reduced double-shell object.

Accordingly this validation does **not** create a false `Ncr_Zhou_original` number by mixing original MCFSTW torsional/web stiffness with the reduced NZ-SCCM section.

The project may use Eq.(5-79) in two valid ways only:

1. original Zhou MCFSTW section + original Zhou stiffness constants: a cross-model source benchmark;
2. reduced double-shell section + a consistently re-derived reduced `Dx,Dy,H`: a same-object elastic-degeneration benchmark.

Neither is allowed to be silently mixed with the other.

## 6. Source-level formula accuracy context

Zhou reports for the Table-5.1 four-edge axial-compression elastic-buckling validation that most theoretical-vs-FE points are within 5%, most remaining points are within 5%-10%, and the reported average error is 5.14%. This validates the source formula family but does not convert the source formula into the current nonlinear `Pu` solver.

## 7. Gate result

```text
TABLE5_1_SOURCE_SCREEN = PASS
TABLE5_1_GE56_MATCH = NONE
NO_SYNTHETIC_SOURCE_POINT_CREATED = PASS
ZHOU_EQ3_2_EQ3_3_REDUCED_REPLAY = PASS
Pyth_reduced = 39.2928 MN
previous_NZ_branch_peak_diagnostic = 26.1085 MN
NZ_over_Zhou_reduced_strength = 0.6644602
relative_difference = -33.5540 percent
ZHOU_EQ5_79_SYMBOLIC_COMPARATOR = REGISTERED
ZHOU_ORIGINAL_EQ5_79_NUMERIC_REPLAY_ON_REDUCED_OBJECT = REJECTED_AS_OBJECT_MIXING
CLEAN_YUN_POSTBUCKLING_BENCHMARK_FROM_TABLE5_1 = BLOCKED_BY_SOURCE_PARAMETER_SPACE
```

## 8. Next source-compliant action

The clean Yun-Lu postbuckling benchmark must now be selected from a different real-source parameter set containing a concrete-constrained steel subpanel with sufficiently large `b_s/t_s` (or otherwise directly satisfying `sigma_cr,el < fy`). The screen must be source-first; no geometry may be reverse-designed merely to force the desired mechanism.
