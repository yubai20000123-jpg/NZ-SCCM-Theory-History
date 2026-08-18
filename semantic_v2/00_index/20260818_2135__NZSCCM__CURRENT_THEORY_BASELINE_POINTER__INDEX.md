# NZ-SCCM CURRENT THEORY BASELINE POINTER

**Timestamp:** 2026-08-18 21:35 +08:00  
**Status:** CURRENT SHARED BASELINE / CHAT-LENGTH HANDOFF / NO NEW THEORY BRANCH

## Canonical current handoff

`semantic_v2/20_theory/20260818_2135__NZSCCM__CURRENT_COMPLETE_THEORY_LEDGER_CASE21_Z6__LOCKED_HANDOFF.md`

Creation commit:

`ab5ec6299a1586dca8ee58dd20174440e489347a`

### Mandatory notation errata

`semantic_v2/20_theory/20260818_2135__NZSCCM__CURRENT_COMPLETE_THEORY_LEDGER_CASE21_Z6__ERRATA_R01.md`

Errata commit:

`0f4db991ada73001bae4d555672ea4d4d4222d53`

The errata is notation-only: in the first GitHub copy, displayed `\nu_R`, `\nu_R'`, and `\nu_w` are to be read as `u_R`, `u_R'`, and `u_w`. No theory, model, root, or numerical result changes.

## Position

The handoff plus mandatory R01 errata is the current consolidated entry point for the Case21 + Z6 theory state as of 2026-08-18 21:35 +08:00. It does **not** delete, overwrite, or replace the evidentiary identity of the 2026-08-17 execution/audit/REPRO artifacts; instead it consolidates them together with the formula expansions and corrections completed in the 2026-08-18 conversation.

The current formal Pu production chain is:

```text
raw specimen inputs
-> controlling complete representative halfwave
-> continuous Nguyen/von-Karman kinematics
-> current material operators
-> material-coordinate true-infinite analytic streams
-> 2x2 Cayley-Hamilton
-> exact General-D15 moments
-> P(D,q,alpha), Rq(D,q,alpha), Ralpha(D,q,alpha) and same-source first derivatives
-> direct solve Rq=0, Ralpha=0, det(J_lim)=0
-> (Du,qu,alphau)
-> Pu=P(Du,qu,alphau)
-> comparator only after solve
```

The earlier `D`-by-`D` continuation/Newton path is retained only as `ROOT IDENTITY / CONNECTED-BRANCH AUDIT`, not as the formal Pu production algorithm.

## Frozen released results recorded in the handoff

```text
Case21:
Du = 0.7887924801
qu = 0.0018083572562965242
alphau = 0.002506908330448254
lambda_A,u = 0.08623596353826937
Pu = 366.7678286852115 kN
error vs test = -0.419459 %

Z6(a=24000):
Du = 1.36180798
qu = 0.0264854039
alphau = 1.8954326279510263
lambda_A,u = 0.786915819
Pu = 48.4061215 MN
error vs Zhou = -2.183706 %
error vs Winter = -3.546283 %
```

## Remaining documentation frontier

- `GAP A`: raw section/material parameters -> `Dx,Dy,H` -> halfwave selection.
- `GAP B`: print the Z6 face/web same-source tangent as material-series nth-term -> D15 ledger.
- `GAP C`: freeze the multiple-root connected-branch identity audit protocol after direct three-variable limit solving.

## New-chat restore instruction

Read the canonical current handoff **and R01 errata** first. Do not reopen R10 calibration, the released Case21/Z6 roots, spatial quadrature, or load-stepping as a formal production route. Resume from `GAP A` unless the user explicitly changes priority.
