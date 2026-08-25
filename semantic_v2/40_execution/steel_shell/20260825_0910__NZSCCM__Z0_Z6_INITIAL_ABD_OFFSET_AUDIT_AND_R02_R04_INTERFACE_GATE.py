from __future__ import annotations
from dataclasses import dataclass
from typing import Dict

# NZ-SCCM: Z0-Z6 initial-ABD offset-stiffness audit + R02/R04 interface gate.
# Formal calculation: algebra only. No spatial quadrature, material points, loading steps,
# experimental values, Zhou/Winter comparators, or effective-width production law.

FORMAL_SPATIAL_QUADRATURE = 0
MATERIAL_POINTS = 0
LOAD_PATH_TRACKING = 0
EFFECTIVE_WIDTH_PRODUCTION = False
CURRENT_TANGENT_INTO_AIRY = False

ES = 206000.0
NU_S = 0.30
NU_C_AIRY = 0.18
RHO_W = 0.02

@dataclass(frozen=True)
class ZCase:
    name: str
    h: float
    ts: float
    tc: float
    Ec: float
    D_EI_archived: float

CASES: Dict[str, ZCase] = {
    "Z0": ZCase("Z0", 130.0, 4.0, 122.0, 32500.0, 11461031000.0),
    "Z1": ZCase("Z1", 100.0, 4.0,  92.0, 32500.0,  5908136000.0),
    "Z2": ZCase("Z2", 130.0, 4.0, 122.0, 32500.0, 11461031000.0),
    "Z3": ZCase("Z3", 130.0, 4.0, 122.0, 35992.80143971206, 11989564042.391521),
    "Z4": ZCase("Z4", 200.0, 4.0, 192.0, 32500.0, 34998869333.333336),
    "Z5": ZCase("Z5", 130.0, 4.0, 122.0, 32500.0, 11461031000.0),
    "Z6": ZCase("Z6", 130.0, 4.0, 122.0, 32500.0, 11461031000.0),
}

Z6_A_SOURCE = {
    "A11": 5.826801330128901e6,
    "A22": 6.329441330128901e6,
    "A12": 1.266142920741884e6,
    "A66": 2.280329204693509e6,
}

def initial_A(c: ZCase):
    Qc = c.Ec/(1.0-NU_C_AIRY**2)
    Qs = ES/(1.0-NU_S**2)
    Gc = c.Ec/(2.0*(1.0+NU_C_AIRY))
    Gs = ES/(2.0*(1.0+NU_S))
    A11 = Qc*(1.0-RHO_W)*c.tc + 2.0*Qs*c.ts
    A22 = A11 + ES*RHO_W*c.tc
    A12 = Qc*NU_C_AIRY*(1.0-RHO_W)*c.tc + 2.0*Qs*NU_S*c.ts
    A66 = Gc*(1.0-RHO_W)*c.tc + 2.0*Gs*c.ts
    return dict(A11=A11, A22=A22, A12=A12, A66=A66)

def initial_D_EI(c: ZCase):
    zf = c.tc/2.0 + c.ts/2.0
    Ic = c.tc**3/12.0
    Is_offset = 2.0*c.ts*zf**2
    Is_skin = 2.0*c.ts**3/12.0
    Dc = c.Ec*Ic
    Ds_offset = ES*Is_offset
    Ds_skin = ES*Is_skin
    D = Dc + Ds_offset + Ds_skin
    return dict(
        zf=zf, Ic=Ic, Is_offset=Is_offset, Is_skin=Is_skin,
        Dc=Dc, Ds_offset=Ds_offset, Ds_skin=Ds_skin, D=D,
        offset_fraction_of_steel_D=Ds_offset/(Ds_offset+Ds_skin),
        steel_fraction_of_total_D=(Ds_offset+Ds_skin)/D,
    )

def run():
    print("Z0_Z6_INITIAL_ABD_OFFSET_AUDIT")
    max_abs_D = 0.0
    for name, c in CASES.items():
        d = initial_D_EI(c)
        a = initial_A(c)
        err = d["D"] - c.D_EI_archived
        max_abs_D = max(max_abs_D, abs(err))
        print(
            f"{name}: zf={d['zf']:.6f} mm, "
            f"Dcalc={d['D']:.12e}, Darch={c.D_EI_archived:.12e}, "
            f"err={err:.6e}, offset_share_steel={d['offset_fraction_of_steel_D']:.12f}, "
            f"steel_share_total={d['steel_fraction_of_total_D']:.12f}, "
            f"A11={a['A11']:.12e}, A22={a['A22']:.12e}, "
            f"A12={a['A12']:.12e}, A66={a['A66']:.12e}"
        )

    z6a = initial_A(CASES["Z6"])
    z6_A_abs = max(abs(z6a[k]-Z6_A_SOURCE[k]) for k in Z6_A_SOURCE)
    assert max_abs_D < 1e-3
    assert z6_A_abs < 1e-6

    print(f"max_D_archived_abs_error_Nmm={max_abs_D:.12e}")
    print(f"Z6_A_source_max_abs_error_N_per_mm={z6_A_abs:.12e}")
    print("INITIAL_OFFSET_STIFFNESS_ALREADY_IN_R07_FRONT = PASS")
    print("ADD_OFFSET_AGAIN = PROHIBITED_DOUBLE_COUNTING")

    # Interface audit:
    # R02's active API requires mean face strains (ex, ey, gamma) to solve its
    # amplitude and return trial resultants. The accepted reduced Airy production
    # interface supplies q/control coordinate and total structural demand resultants.
    # No currently frozen production identity maps those total resultants uniquely
    # to the steel-face mean strain triple while also satisfying the concrete/core
    # terminal and avoiding reintroduction of the superseded global material
    # residual route or the prohibited effective-width route.
    r02_required = {"ex", "ey", "gamma"}
    current_reduced_airy_terminal = {"q", "s", "Nx_d", "Ny_d", "Nxy_d", "Mx_d", "My_d", "Mxy_d"}
    production_face_strain_bridge = False

    print(f"R02_REQUIRED_FACE_STATE={sorted(r02_required)}")
    print(f"CURRENT_REDUCED_AIRY_TERMINAL_STATE={sorted(current_reduced_airy_terminal)}")
    print(f"PRODUCTION_FACE_STRAIN_BRIDGE={production_face_strain_bridge}")
    print("R02_R04_Z0_Z6_NEW_PU = BLOCKED_EXACT_INTERFACE")
    print("MISSING_IDENTITY = Airy total demand/resultants -> steel-face (ex,ey,gamma) consistent with common terminal section")
    print("NEW_PU_CALCULATED = False")

if __name__ == "__main__":
    run()
