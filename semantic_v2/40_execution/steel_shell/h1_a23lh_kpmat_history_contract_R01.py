# -*- coding: utf-8 -*-
"""
H1 A23-LH Kp^mat exact-thickness reduction / history-transport contracts R01

Production identity:
  Kh = Ke + Kg_trial - Kp_mat - Kp_hist_g

Kp_mat:
  - yield and loading-index boundaries are quadratic in z;
  - exact active thickness intervals are root-defined;
  - each entry reduces to elementary integral P4(z)/Q2(z);
  - remaining xi/psi integral is an algebraic-period object.

Kp_hist_g:
  - requires connected-path current finite stress;
  - current active mask alone is insufficient after unloading;
  - formal evaluator must transport the continuous algebraic history partition.

NO SPATIAL GAUSS FALLBACK.
"""

UNRESOLVED_PHASE_PERIOD = "UNRESOLVED_PHASE_ALGEBRAIC_PERIOD"
UNRESOLVED_HISTORY_PERIOD = "UNRESOLVED_HISTORY_PERIOD_TRANSPORT"

def Kp_mat_formal(exact_z_reduced_period):
    if exact_z_reduced_period is None:
        raise RuntimeError(UNRESOLVED_PHASE_PERIOD)
    return exact_z_reduced_period

def history_geometric_transport(Kg_at_first_yield, path_period_derivative, s0, s1, path_integrator=None):
    if path_integrator is None:
        raise RuntimeError(UNRESOLVED_HISTORY_PERIOD)
    return Kg_at_first_yield + path_integrator(path_period_derivative, s0, s1)

def local_hinge_matrix(Ke, Kg_trial, Kp_mat, Kp_hist_g):
    return Ke + Kg_trial - Kp_mat - Kp_hist_g
