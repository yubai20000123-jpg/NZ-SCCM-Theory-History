# ERRATA — NC-R1 FORMAL CLOSURE CANONICAL

**Applies to:** `current/theory/NZ_SCCM_NC_R1_FORMAL_CLOSURE_ZHOU_STYLE_CANONICAL_20260812.md`

This errata contains editorial-symbol corrections only; no equation, physics, compiler identity, D15 identity, root rule, or stability interpretation is changed.

## Equation (29)

Where the canonical file renders the three branch symbols as `\nu_1`, `\nu_2`, `\nu_r`, read them as the intended Roman stress-utilization symbols

\[
\boxed{
u_{sm}(t)=
\begin{cases}
u_1(t/x_{cr}),&0\le t\le x_{cr},\\
u_2[(t-x_{cr})/(9x_{cr})],&x_{cr}<t\le10x_{cr},\\
u_r,&t>10x_{cr}.
\end{cases}}
\]

with

```text
u_sm -> u_sm
u_1  -> u_1
u_2  -> u_2
u_r  -> u_r
```

That is, the normative equation is

\[
\boxed{u_{sm}(t)=
\begin{cases}u_1(t/x_{cr}),&0\le t\le x_{cr},\\u_2[(t-x_{cr})/(9x_{cr})],&x_{cr}<t\le10x_{cr},\\u_r,&t>10x_{cr}.
\end{cases}}
\]

The definitions of `u_1`, `u_2`, and `u_r` are Equations (24), (27), and (26), respectively.

```text
ERRATA_IDENTITY = EDITORIAL_ONLY
THEORY_CHANGE = NO
```
