"""NZ-SCCM local radial-cap material tangent audit.

Identity: MATERIAL-LOCAL DERIVATIVE CHECK ONLY.
This file performs NO structural integration, NO Gauss/Simpson/adaptive
quadrature, NO spatial collocation, NO material-point production grid,
and NO root selection.

The production tangent is the analytic derivative below. The centered
finite-difference block is only an independent material-map derivative oracle.
"""

import numpy as np

ES = 206000.0
NU_S = 0.30
EPS0 = 0.0018712490394580678
NU_REF = 0.18

CE = ES / (1.0 - NU_S**2) * np.array(
    [
        [1.0, NU_S, 0.0],
        [NU_S, 1.0, 0.0],
        [0.0, 0.0, (1.0 - NU_S) / 2.0],
    ],
    dtype=float,
)

# s_vm^2 = s^T H s for s=[sx,sy,txy]^T under plane stress.
HVM = np.array(
    [
        [1.0, -0.5, 0.0],
        [-0.5, 1.0, 0.0],
        [0.0, 0.0, 3.0],
    ],
    dtype=float,
)


def vm(stress):
    return float(np.sqrt(stress @ HVM @ stress))


def radial_cap_map(strain, fy):
    trial = CE @ strain
    r = vm(trial)
    lam = 1.0 if r <= fy else fy / r
    return lam * trial


def radial_cap_tangent(strain, fy):
    """Exact d(returned stress)/d(engineering strain) for stated radial cap."""
    trial = CE @ strain
    r = vm(trial)
    if r <= fy:
        return CE.copy()
    lam = fy / r
    return lam * (np.eye(3) - np.outer(trial, HVM @ trial) / r**2) @ CE


def halfwave_center_strain(D, q, alpha, b, tc, ts, compressed_face=True):
    """Closed-form X=Y=pi/2 face-centroid strain; not a spatial integration."""
    zc = tc / 2.0 + ts / 2.0
    z = -zc if compressed_face else zc
    bax = (1.0 - 2.0 * NU_REF) / 4.0
    bay = (2.0 - NU_REF) / 4.0
    bend = z * np.pi**2 * q / b
    ex = EPS0 * (NU_REF * D + alpha * bax) + bend
    ey = EPS0 * (-D + alpha * bay) + bend
    return z, np.array([ex, ey, 0.0], dtype=float)


STATES = {
    "Z1_OFF": dict(D=0.5939452076, q=0.003204740061, alpha=0.0,
                   b=6000.0, tc=92.0, ts=4.0, fy=235.0),
    "Z1_ON": dict(D=0.5820414604, q=0.004873166767, alpha=0.1317481353,
                  b=6000.0, tc=92.0, ts=4.0, fy=235.0),
    "Z4_OFF": dict(D=0.9065170837, q=0.001300622089, alpha=0.0,
                   b=8000.0, tc=192.0, ts=4.0, fy=355.0),
    "Z4_ON": dict(D=0.9177226716, q=0.001403182997, alpha=0.004739862166,
                  b=8000.0, tc=192.0, ts=4.0, fy=355.0),
}


def centered_fd_tangent(strain, fy, h=1.0e-8):
    eye = np.eye(3)
    cols = []
    for j in range(3):
        sp = radial_cap_map(strain + h * eye[j], fy)
        sm = radial_cap_map(strain - h * eye[j], fy)
        cols.append((sp - sm) / (2.0 * h))
    return np.column_stack(cols)


def audit_state(name, p):
    z, strain = halfwave_center_strain(
        p["D"], p["q"], p["alpha"], p["b"], p["tc"], p["ts"], True
    )
    trial = CE @ strain
    r = vm(trial)
    returned = radial_cap_map(strain, p["fy"])
    ct = radial_cap_tangent(strain, p["fy"])
    ct_fd = centered_fd_tangent(strain, p["fy"])
    rel_fd = np.linalg.norm(ct - ct_fd) / np.linalg.norm(ct)
    svals = np.linalg.svd(ct, compute_uv=False)
    return {
        "name": name,
        "z": z,
        "strain": strain,
        "trial": trial,
        "vm": r,
        "vm_over_fy": r / p["fy"],
        "returned": returned,
        "singular_values": svals,
        "rank_tol_1e-7": int(np.linalg.matrix_rank(ct, tol=1.0e-7)),
        "relative_fd_error": rel_fd,
    }


if __name__ == "__main__":
    print("FORMAL_SPATIAL_QUADRATURE = 0")
    print("THIS_SCRIPT_STRUCTURAL_INTEGRATION = NONE")
    for key, pars in STATES.items():
        out = audit_state(key, pars)
        print("\n", key)
        for field, value in out.items():
            if field != "name":
                print(f"{field} = {value}")
        if out["vm_over_fy"] > 1.0:
            assert out["rank_tol_1e-7"] == 2
            assert out["relative_fd_error"] < 1.0e-8
