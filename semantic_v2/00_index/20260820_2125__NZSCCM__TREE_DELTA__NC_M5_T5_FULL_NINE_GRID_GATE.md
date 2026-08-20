# TREE DELTA — NC-M5 T5 single rational + full nine-grid gate

Time: 2026-08-20 21:25 +08:00

Current mainline:

`NC-基准本构 (frozen) -> NC-M5 fixed plane-stress material coordinates -> T_NC -> T5 [8/8] single rational -> frozen CC/TC/CT/TT interactions -> full nine-grid stress/tangent/boundedness gate`.

Locked this turn:

1. `T5(r)=P8(r)/Q8(r)` is a single [8/8] rational compilation of the actual G20/G21 C2-regularized NC tensile target, not of another external reference.
2. Structural identities: `T5(0)=0`, `T5'(0)=1`, `T5(infinity)=0.3`.
3. Material qualification on `r in [0,34]`: stress RMS `7.1390e-4`, max `1.4418e-3`; tangent RMS `1.80425e-3`, max `1.32626e-2`.
4. Full domain `r>=0`: no positive denominator roots; `0<=T5<1`; stress/tangent within sector bounded.
5. NC-M5 four sectors remain exactly the frozen NC benchmark: CC `c_i*=c_i(1+a_cc c1 c2)`, TC `c*=c(1-tau)`, TT `tau_i*=tau_i(1-a_t tau_j^8)`.
6. All four sectors share the same origin tangent `K_lambda(0)=kappa I`; after fixed NC plane-stress coordinate map they recover standard physical plane-stress tangent.
7. Stress is exactly continuous at finite zero-coordinate sector boundaries.
8. Finite-state tangent is not continuous across sector fronts before the already-registered G21 C1/C2 regularization. Example CC-TC: `K21^- = a_cc c^2 C'(c)` vs `K21^+ = c C'(c)/xcr`; TC-TT: `K22^- = kappa(1-tau)` vs `K22^+ = kappa(1-a_t tau^8)`.
9. Therefore the only next material task is the already-registered C1/C2 sector-front regularization. Do not reopen T5, the reference, CC/TC/TT physics, or Poisson architecture without a separate user-approved reference-change decision.

No Case21 structural solve was performed in this node.
