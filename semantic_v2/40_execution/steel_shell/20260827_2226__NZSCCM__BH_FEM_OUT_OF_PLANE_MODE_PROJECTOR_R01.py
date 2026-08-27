# -*- coding: utf-8 -*-
from __future__ import print_function

import argparse
import csv
import json
import math
import os
from collections import defaultdict
from odbAccess import openOdb


def vsub(a, b):
    return (a[0]-b[0], a[1]-b[1], a[2]-b[2])


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])


def norm(a):
    return math.sqrt(a[0]*a[0] + a[1]*a[1] + a[2]*a[2])


def polygon_area_xz(points):
    s = 0.0
    n = len(points)
    for i in range(n):
        x1, z1 = points[i][0], points[i][2]
        x2, z2 = points[(i+1) % n][0], points[(i+1) % n][2]
        s += x1*z2 - x2*z1
    return 0.5*abs(s)


def solve_linear(A, b):
    n = len(b)
    M = [list(A[i]) + [float(b[i])] for i in range(n)]
    for k in range(n):
        p = max(range(k, n), key=lambda i: abs(M[i][k]))
        if abs(M[p][k]) < 1.0e-20:
            raise RuntimeError('singular normal equation')
        if p != k:
            M[k], M[p] = M[p], M[k]
        piv = M[k][k]
        for j in range(k, n+1):
            M[k][j] /= piv
        for i in range(n):
            if i == k:
                continue
            f = M[i][k]
            if f == 0.0:
                continue
            for j in range(k, n+1):
                M[i][j] -= f*M[k][j]
    return [M[i][n] for i in range(n)]


def weighted_fit(rows, yvals, mode_sign, include_mode):
    ncol = 4 if include_mode else 3
    ATA = [[0.0]*ncol for _ in range(ncol)]
    ATb = [0.0]*ncol
    for r, y in zip(rows, yvals):
        cols = [1.0, r['xn'], r['zn']]
        if include_mode:
            cols.append(mode_sign*r['phi0'])
        w = r['weight']
        for i in range(ncol):
            ATb[i] += w*cols[i]*y
            for j in range(ncol):
                ATA[i][j] += w*cols[i]*cols[j]
    coef = solve_linear(ATA, ATb)
    sse = 0.0
    sw = 0.0
    for r, y in zip(rows, yvals):
        cols = [1.0, r['xn'], r['zn']]
        if include_mode:
            cols.append(mode_sign*r['phi0'])
        yp = sum(coef[i]*cols[i] for i in range(ncol))
        w = r['weight']
        sse += w*(y-yp)*(y-yp)
        sw += w
    return coef, sse, sw


def fit_field(rows, yvals, mode_sign):
    plane, sse_plane, sw = weighted_fit(rows, yvals, mode_sign, False)
    full, sse_full, sw2 = weighted_fit(rows, yvals, mode_sign, True)
    W = full[3]
    if sse_plane > 1.0e-30:
        modal_r2 = 1.0 - sse_full/sse_plane
    else:
        modal_r2 = 1.0 if sse_full <= 1.0e-30 else 0.0
    rms = math.sqrt(max(sse_full, 0.0)/max(sw2, 1.0e-30))
    return {
        'plane_c0': full[0], 'plane_cx': full[1], 'plane_cz': full[2],
        'W': W, 'sse_plane': sse_plane, 'sse_full': sse_full,
        'modal_R2_after_plane': modal_r2,
        'rms_residual': rms,
        'nrms_residual_over_absW': rms/max(abs(W), 1.0e-30)
    }


def choose_instance(odb, requested, normal_cut):
    if requested:
        if requested not in odb.rootAssembly.instances:
            raise RuntimeError('instance not found: %s' % requested)
        return odb.rootAssembly.instances[requested]
    scored = []
    for name, inst in odb.rootAssembly.instances.items():
        nodes = dict((n.label, tuple(float(x) for x in n.coordinates)) for n in inst.nodes)
        count = 0
        xvals, zvals = [], []
        for e in inst.elements:
            if not str(getattr(e, 'type', '')).upper().startswith('S') or len(e.connectivity) < 3:
                continue
            p0, p1, p2 = [nodes[e.connectivity[i]] for i in range(3)]
            nn = cross(vsub(p1, p0), vsub(p2, p0))
            nnorm = norm(nn)
            if nnorm <= 1.0e-20 or abs(nn[1]/nnorm) < normal_cut:
                continue
            count += 1
            for lab in e.connectivity:
                p = nodes[lab]
                xvals.append(p[0]); zvals.append(p[2])
        if count and xvals and zvals:
            span = (max(xvals)-min(xvals))*(max(zvals)-min(zvals))
            scored.append((count*max(span, 1.0), name, inst))
    if not scored:
        raise RuntimeError('no instance with horizontal shell faces was found')
    scored.sort(key=lambda t: t[0], reverse=True)
    return scored[0][2]


def build_mid_pairs(inst, normal_cut, pair_tol):
    nodes = dict((n.label, tuple(float(x) for x in n.coordinates)) for n in inst.nodes)
    node_weight = defaultdict(float)
    horizontal_labels = set()
    xall, zall = [], []
    for e in inst.elements:
        if not str(getattr(e, 'type', '')).upper().startswith('S') or len(e.connectivity) < 3:
            continue
        pts = [nodes[lab] for lab in e.connectivity]
        nn = cross(vsub(pts[1], pts[0]), vsub(pts[2], pts[0]))
        nnorm = norm(nn)
        if nnorm <= 1.0e-20 or abs(nn[1]/nnorm) < normal_cut:
            continue
        area = polygon_area_xz(pts)
        if area <= 0.0:
            continue
        share = area/float(len(e.connectivity))
        for lab in e.connectivity:
            horizontal_labels.add(lab)
            node_weight[lab] += share
            p = nodes[lab]
            xall.append(p[0]); zall.append(p[2])
    if not horizontal_labels:
        raise RuntimeError('no horizontal shell nodes found')
    lx0 = max(xall)-min(xall); lz0 = max(zall)-min(zall)
    if pair_tol is None:
        pair_tol = max(1.0e-5, 1.0e-6*max(lx0, lz0, 1.0))
    buckets = defaultdict(list)
    for lab in horizontal_labels:
        x, y, z = nodes[lab]
        buckets[(int(round(x/pair_tol)), int(round(z/pair_tol)))].append(lab)
    raw = []
    for labs in buckets.values():
        if len(labs) < 2:
            continue
        labs = sorted(labs, key=lambda lab: nodes[lab][1])
        bot, top = labs[0], labs[-1]
        xt, yt, zt = nodes[top]; xb, yb, zb = nodes[bot]
        if abs(yt-yb) < 1.0:
            continue
        w = 0.5*(node_weight[top]+node_weight[bot])
        if w <= 0.0:
            continue
        raw.append((0.5*(xt+xb), 0.5*(zt+zb), top, bot, 0.5*(yt+yb), w))
    if len(raw) < 20:
        raise RuntimeError('too few paired top/bottom face coordinates: %d' % len(raw))
    xmin = min(r[0] for r in raw); xmax = max(r[0] for r in raw)
    zmin = min(r[1] for r in raw); zmax = max(r[1] for r in raw)
    lx = xmax-xmin; lz = zmax-zmin
    rows = []
    for x, z, top, bot, ymid0, w in raw:
        rows.append({'x': x, 'z': z,
                     'xn': (x-0.5*(xmin+xmax))/lx,
                     'zn': (z-0.5*(zmin+zmax))/lz,
                     'top': top, 'bottom': bot,
                     'ymid0': ymid0, 'weight': w})
    return rows, pair_tol, (xmin, xmax, zmin, zmax)


def attach_mode(rows, bounds, mstar):
    xmin, xmax, zmin, zmax = bounds
    lx = xmax-xmin; lz = zmax-zmin
    for r in rows:
        xi = (r['x']-xmin)/lx
        eta = (r['z']-zmin)/lz
        r['phi0'] = math.sin(math.pi*xi)*math.sin(float(mstar)*math.pi*eta)


def u2_map(frame, inst_name):
    if 'U' not in frame.fieldOutputs:
        raise RuntimeError('frame has no U field output')
    out = {}
    for v in frame.fieldOutputs['U'].values:
        try:
            if v.instance.name != inst_name:
                continue
        except Exception:
            pass
        if len(v.data) >= 2:
            out[v.nodeLabel] = float(v.data[1])
    return out


def main():
    ap = argparse.ArgumentParser(description='Read-only BH global out-of-plane mode projection from Abaqus ODB.')
    ap.add_argument('odb_path')
    ap.add_argument('outdir')
    ap.add_argument('b_theory', type=float)
    ap.add_argument('a_theory', type=float)
    ap.add_argument('mstar', type=int)
    ap.add_argument('q0_theory', type=float)
    ap.add_argument('--step', default='EXPLICIT_LOADING')
    ap.add_argument('--instance', default=None)
    ap.add_argument('--target-frame', type=int, default=None)
    ap.add_argument('--target-time', type=float, default=None)
    ap.add_argument('--normal-cut', type=float, default=0.90)
    ap.add_argument('--pair-tol', type=float, default=None)
    args = ap.parse_args()
    if not os.path.isdir(args.outdir):
        os.makedirs(args.outdir)
    odb = openOdb(args.odb_path, readOnly=True)
    try:
        if args.step not in odb.steps:
            raise RuntimeError('step not found: %s' % args.step)
        step = odb.steps[args.step]
        inst = choose_instance(odb, args.instance, args.normal_cut)
        rows, pair_tol, bounds = build_mid_pairs(inst, args.normal_cut, args.pair_tol)
        attach_mode(rows, bounds, args.mstar)
        y0 = [r['ymid0'] for r in rows]
        pre = fit_field(rows, y0, 1.0)
        mode_sign = 1.0 if pre['W'] >= 0.0 else -1.0
        initial = fit_field(rows, y0, mode_sign)
        xmin, xmax, zmin, zmax = bounds
        lx_fe = xmax-xmin; lz_fe = zmax-zmin
        initial['q0_FE'] = initial['W']/args.b_theory
        initial['q0_theory'] = args.q0_theory
        initial['q0_ratio_FE_over_theory'] = initial['q0_FE']/args.q0_theory if args.q0_theory != 0.0 else None
        initial['kappa_x_FE_geom_per_mm'] = initial['W']*(math.pi/lx_fe)**2
        initial['kappa_y_FE_geom_per_mm'] = initial['W']*(args.mstar*math.pi/lz_fe)**2
        path = []
        for iframe, frame in enumerate(step.frames):
            umap = u2_map(frame, inst.name)
            vals, valid = [], []
            for r in rows:
                if r['top'] in umap and r['bottom'] in umap:
                    vals.append(0.5*(umap[r['top']]+umap[r['bottom']]))
                    valid.append(r)
            if len(valid) < max(20, int(0.8*len(rows))):
                raise RuntimeError('insufficient paired U2 data at frame %d: %d/%d' % (iframe, len(valid), len(rows)))
            fit = fit_field(valid, vals, mode_sign)
            Wd = fit['W']
            path.append({'frame': iframe, 'time': float(frame.frameValue), 'n_pairs': len(valid),
                         'Wd_FE_mm': Wd, 'q_FE': Wd/args.b_theory,
                         'kappa_x_FE_geom_per_mm': Wd*(math.pi/lx_fe)**2,
                         'kappa_y_FE_geom_per_mm': Wd*(args.mstar*math.pi/lz_fe)**2,
                         'modal_R2_after_plane': fit['modal_R2_after_plane'],
                         'rms_residual_mm': fit['rms_residual'],
                         'nrms_residual_over_absW': fit['nrms_residual_over_absW'],
                         'rigid_c0_mm': fit['plane_c0'],
                         'tilt_x_coeff_mm': fit['plane_cx'],
                         'tilt_z_coeff_mm': fit['plane_cz']})
        selected = None; selection = 'NONE'
        if args.target_frame is not None:
            for r in path:
                if r['frame'] == args.target_frame:
                    selected = r; break
            if selected is None:
                raise RuntimeError('target frame %d not found' % args.target_frame)
            selection = 'TARGET_FRAME'
        elif args.target_time is not None:
            selected = min(path, key=lambda r: abs(r['time']-args.target_time))
            selection = 'NEAREST_TARGET_TIME'
        elif path:
            selected = path[-1]
            selection = 'LAST_FRAME_ONLY_NOT_ASSUMED_PEAK'
        fields = ['frame','time','n_pairs','Wd_FE_mm','q_FE','kappa_x_FE_geom_per_mm','kappa_y_FE_geom_per_mm','modal_R2_after_plane','rms_residual_mm','nrms_residual_over_absW','rigid_c0_mm','tilt_x_coeff_mm','tilt_z_coeff_mm']
        csv_path = os.path.join(args.outdir, 'FEM_GLOBAL_OUT_OF_PLANE_MODE_PATH.csv')
        with open(csv_path, 'wb') as f:
            wr = csv.DictWriter(f, fieldnames=fields); wr.writeheader()
            for r in path: wr.writerow(r)
        pair_path = os.path.join(args.outdir, 'FEM_GLOBAL_MODE_PAIRED_NODES.csv')
        with open(pair_path, 'wb') as f:
            wr = csv.writer(f); wr.writerow(['x','z','top_node','bottom_node','ymid0','area_weight','phi_aligned'])
            for r in rows:
                wr.writerow([r['x'],r['z'],r['top'],r['bottom'],r['ymid0'],r['weight'],mode_sign*r['phi0']])
        summary = {
            'status': 'FEM_DISPLACEMENT_MODE_PROJECTION_EXECUTED',
            'diagnostic_only': True, 'theory_modified': False,
            'formal_structural_spatial_quadrature': 0, 'material_points': 0,
            'odb': os.path.abspath(args.odb_path), 'step': args.step, 'instance': inst.name,
            'mode_contract': {'FE_loading_axis':'global Z','FE_out_of_plane_axis':'global Y','theory_x_from_FE':'X','theory_y_from_FE':'Z','incremental_w_from_FE':'U2','phi':'sin(pi*(X-Xmin)/Lx_FE)*sin(m*pi*(Z-Zmin)/Lz_FE)','mode_sign_source':'initial_imperfection_projection','rigid_terms_removed':['constant','linear_X','linear_Z']},
            'theory': {'b_mm':args.b_theory,'a_mm':args.a_theory,'mstar':args.mstar,'q0':args.q0_theory},
            'mesh': {'pair_tolerance_mm':pair_tol,'n_mid_pairs':len(rows),'xmin':xmin,'xmax':xmax,'Lx_FE':lx_fe,'zmin':zmin,'zmax':zmax,'Lz_FE':lz_fe,'Lx_FE_over_b_theory':lx_fe/args.b_theory,'Lz_FE_over_a_theory':lz_fe/args.a_theory},
            'initial_imperfection_projection': initial,
            'selection_policy': selection, 'selected_frame': selected, 'n_frames': len(path),
            'outputs': {'path_csv':os.path.basename(csv_path),'paired_nodes_csv':os.path.basename(pair_path)}
        }
        json_path = os.path.join(args.outdir, 'FEM_GLOBAL_OUT_OF_PLANE_MODE_SUMMARY.json')
        with open(json_path, 'w') as f: json.dump(summary, f, indent=2, sort_keys=True)
        print('PASS instance=%s pairs=%d frames=%d' % (inst.name, len(rows), len(path)))
        print('initial W0_FE=%.12g mm q0_FE=%.12g modal_R2=%.6f' % (initial['W'], initial['q0_FE'], initial['modal_R2_after_plane']))
        if selected is not None:
            print('selected policy=%s frame=%d time=%.12g Wd=%.12g mm q_FE=%.12g modal_R2=%.6f' % (selection, selected['frame'], selected['time'], selected['Wd_FE_mm'], selected['q_FE'], selected['modal_R2_after_plane']))
        print('summary=%s' % json_path)
    finally:
        odb.close()


if __name__ == '__main__':
    main()
