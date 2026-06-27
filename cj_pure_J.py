"""
cj_pure_J — 10 two-loop pure-gluon Wilson line integrals (J only, no constants).

Usage:
    import cj_pure_J

    # List all IDs
    print(cj_pure_J.IDS)
    # → ['2g1', '2g2', ...]

    # Access one integral
    J = cj_pure_J.INTEGRALS['2g2']
    print(J['J_plain'])
    # → 'x2*z * (-x2*(1 - x1) + i0)**(-1 + eps) * ...'

    # Iterate
    for rec in cj_pure_J.ALL:
        print(f"{rec['id']}: {rec['label']}")

    # Export to JSON string
    print(cj_pure_J.to_json())

Source: workspaces/cj_batch/CJ_summary.md (generated 2026-06-27)
"""

import json
from pathlib import Path

# ---------------------------------------------------------------------------
# Conventions (shared — C and C1 are provided in CJ_summary.md, not here)
# ---------------------------------------------------------------------------

META = {
    "title": "10 Two-Loop Pure-Gluon Wilson Line Integrals — J only",
    "date": "2026-06-27",
    "source": "workspaces/cj_batch/CJ_summary.md",
    "generator": "legacy/preprocess.py",
    "conventions": {
        "D": "4 - 2*eps",
        "kinematics": {
            "v14": 1,
            "z": "v12 = v34",
            "v13": "-(1+z)",
            "v24": "-(1+z)",
            "v23": 1,
        },
        "i0": "+i0 Minkowski causal prescription",
        "x_domain": "[0,1]",
        "alpha_domain": "simplex: alpha_i >= 0, sum(alpha_i) = 1",
        "eps": "dimensional regulator epsilon = (4-D)/2",
    },
}

# ---------------------------------------------------------------------------
# Integral data — J only (C and C1 in CJ_summary.md)
# ---------------------------------------------------------------------------

_ALL_DATA = [
    {
        "id": "2g1",
        "diagram": "diagrams/2g1_double_adjacent.png",
        "label": "2-gluon, edges (3,3)-(4,4) (double adjacent pair)",
        "n_gluons": 2,
        "n_x": 4,
        "n_alpha": 0,
        "edges": [3, 3, 4, 4],
        "topology": "double_adjacent",
        "J_latex": (
            r"x_1 x_2\,z^2 \cdot \bigl(-x_2(1 - x_1 x_3)\,x_4\,z + i0\bigr)"
            r"^{-1+\varepsilon} \cdot \bigl(-(1 - x_1)\,x_2\,z + i0\bigr)"
            r"^{-1+\varepsilon}"
        ),
        "J_plain": (
            "x1*x2*z**2 * (-x2*(1 - x1*x3)*x4*z + i0)**(-1 + eps)"
            " * (-(1 - x1)*x2*z + i0)**(-1 + eps)"
        ),
        "integration_vars": ["x1", "x2", "x3", "x4"],
        "integration_domain": "[0,1]^4",
        "kinematic_var": "z",
        "i0_prescription": "+i0",
    },
    {
        "id": "2g2",
        "diagram": "diagrams/2g2_adjacent_chain.png",
        "label": "2-gluon, edges 2,3-3,4 (adjacent chain)",
        "n_gluons": 2,
        "n_x": 4,
        "n_alpha": 0,
        "edges": [2, 3, 3, 4],
        "topology": "adjacent_chain",
        "J_latex": (
            r"x_2\,z \cdot \bigl(-x_2(1 - x_1) + i0\bigr)^{-1+\varepsilon}"
            r" \cdot \bigl(-x_3(1 - x_2 x_4)\,z + i0\bigr)^{-1+\varepsilon}"
        ),
        "J_plain": (
            "x2*z * (-x2*(1 - x1) + i0)**(-1 + eps)"
            " * (-x3*(1 - x2*x4)*z + i0)**(-1 + eps)"
        ),
        "integration_vars": ["x1", "x2", "x3", "x4"],
        "integration_domain": "[0,1]^4",
        "kinematic_var": "z",
        "i0_prescription": "+i0",
    },
    {
        "id": "2g3",
        "diagram": "diagrams/2g3_mixed_2344.png",
        "label": "2-gluon, edges 2,3-4,4 (mixed)",
        "n_gluons": 2,
        "n_x": 4,
        "n_alpha": 0,
        "edges": [2, 3, 4, 4],
        "topology": "mixed",
        "J_latex": (
            r"-x_3\,z(1+z) \cdot \bigl(-\!\bigl[1 - x_3 x_4 + x_1(-1 + "
            r"x_3 x_4(1+z))\bigr] + i0\bigr)^{-1+\varepsilon} \cdot "
            r"\bigl(-(1 - x_2)\,x_3\,z + i0\bigr)^{-1+\varepsilon}"
        ),
        "J_plain": (
            "-x3*z*(1 + z) * (-(1 - x3*x4 + x1*(-1 + x3*x4*(1 + z))) + i0)"
            "**(-1 + eps) * (-(1 - x2)*x3*z + i0)**(-1 + eps)"
        ),
        "integration_vars": ["x1", "x2", "x3", "x4"],
        "integration_domain": "[0,1]^4",
        "kinematic_var": "z",
        "i0_prescription": "+i0",
    },
    {
        "id": "2g4",
        "diagram": "diagrams/2g4_double_opposite.png",
        "label": "2-gluon, edges 1,1-3,3 (double opposite)",
        "n_gluons": 2,
        "n_x": 4,
        "n_alpha": 0,
        "edges": [1, 1, 3, 3],
        "topology": "double_opposite",
        "J_latex": (
            r"x_1 x_2\,(1+z)^2 \cdot \bigl(-\!\bigl[z - x_2 x_4 z + "
            r"x_1 x_3(-z + x_2 x_4(1+z))\bigr] + i0\bigr)^{-1+\varepsilon}"
            r" \cdot \bigl(-\!\bigl[z - x_2 z + x_1(x_2 - z + x_2 z)\bigr]"
            r" + i0\bigr)^{-1+\varepsilon}"
        ),
        "J_plain": (
            "x1*x2*(1 + z)**2 * (-(z - x2*x4*z + x1*x3*(-z + x2*x4*(1 + z)))"
            " + i0)**(-1 + eps) * (-(z - x2*z + x1*(x2 - z + x2*z)) + i0)"
            "**(-1 + eps)"
        ),
        "integration_vars": ["x1", "x2", "x3", "x4"],
        "integration_domain": "[0,1]^4",
        "kinematic_var": "z",
        "i0_prescription": "+i0",
    },
    {
        "id": "2g5",
        "diagram": "diagrams/2g5_mixed_1334.png",
        "label": "2-gluon, edges 1,3-3,4 (mixed)",
        "n_gluons": 2,
        "n_x": 4,
        "n_alpha": 0,
        "edges": [1, 3, 3, 4],
        "topology": "mixed",
        "J_latex": (
            r"-x_2\,z(1+z) \cdot \bigl(-\!\bigl[z - x_2 z + x_1(x_2 - z + "
            r"x_2 z)\bigr] + i0\bigr)^{-1+\varepsilon} \cdot \bigl(-x_3"
            r"(1 - x_2 x_4)\,z + i0\bigr)^{-1+\varepsilon}"
        ),
        "J_plain": (
            "-x2*z*(1 + z) * (-(z - x2*z + x1*(x2 - z + x2*z)) + i0)"
            "**(-1 + eps) * (-x3*(1 - x2*x4)*z + i0)**(-1 + eps)"
        ),
        "integration_vars": ["x1", "x2", "x3", "x4"],
        "integration_domain": "[0,1]^4",
        "kinematic_var": "z",
        "i0_prescription": "+i0",
    },
    {
        "id": "2g6",
        "diagram": "diagrams/2g6_one_per_edge.png",
        "label": "2-gluon, edges 1,2-3,4 (one per edge)",
        "n_gluons": 2,
        "n_x": 4,
        "n_alpha": 0,
        "edges": [1, 2, 3, 4],
        "topology": "one_per_edge",
        "J_latex": (
            r"(1+z)^2 \cdot \bigl(-\!\bigl[z - x_3 z + x_1(x_3 - z + "
            r"x_3 z)\bigr] + i0\bigr)^{-1+\varepsilon} \cdot \bigl(-\!\bigl"
            r"[1 - x_4 + x_2(-1 + x_4 + x_4 z)\bigr] + i0\bigr)^{-1+\varepsilon}"
        ),
        "J_plain": (
            "(1 + z)**2 * (-(z - x3*z + x1*(x3 - z + x3*z)) + i0)"
            "**(-1 + eps) * (-(1 - x4 + x2*(-1 + x4 + x4*z)) + i0)"
            "**(-1 + eps)"
        ),
        "integration_vars": ["x1", "x2", "x3", "x4"],
        "integration_domain": "[0,1]^4",
        "kinematic_var": "z",
        "i0_prescription": "+i0",
    },
    # ---- 3-gluon TGV integrals (α-simplex + x-hypercube) ----
    {
        "id": "3v1",
        "diagram": "diagrams/3v1_tgv_nondeg.png",
        "label": "3-gluon TGV, edges 1,3,4 (non-degenerate)",
        "n_gluons": 3,
        "n_x": 3,
        "n_alpha": 3,
        "edges": [1, 3, 4],
        "topology": "tgv_nondeg",
        "J_latex": (
            r"\frac{ \alpha_2\alpha_3\,z(-1+x_2+x_3-z+x_2z)"
            r" - \alpha_1\alpha_3\bigl((x_3-1)z + x_1(1+z)\bigr)"
            r" + \alpha_1\alpha_2\bigl(x_1(1+z) + z(3+z-x_2(1+z))\bigr) }"
            r"{ (\alpha_1\alpha_2\alpha_3)^{\varepsilon}\;"
            r"\bigl[-\alpha_1\alpha_3\,x_1(x_3-1)"
            r" - \alpha_2\alpha_3\,x_3(x_2-1)z"
            r" + \alpha_1\alpha_2\bigl(z - x_2z + x_1(x_2 - z + x_2z)\bigr)"
            r"\bigr]^{2-2\varepsilon} }"
        ),
        "J_plain": (
            "(a2*a3*z*(-1 + x2 + x3 - z + x2*z)"
            " - a1*a3*((x3-1)*z + x1*(1+z))"
            " + a1*a2*(x1*(1+z) + z*(3+z-x2*(1+z))))"
            " / ((a1*a2*a3)**eps"
            " * (-a1*a3*x1*(x3-1) - a2*a3*x3*(x2-1)*z"
            " + a1*a2*(z - x2*z + x1*(x2 - z + x2*z)))**(2 - 2*eps))"
        ),
        "integration_vars": ["x1", "x2", "x3", "a1", "a2", "a3"],
        "integration_domain": "[0,1]^3 × simplex(a1,a2,a3)",
        "kinematic_var": "z",
        "i0_prescription": "+i0",
        "alpha_constraint": "a1 + a2 + a3 = 1",
    },
    {
        "id": "3v2",
        "diagram": "diagrams/3v2_tgv_degen23.png",
        "label": "3-gluon TGV, edges 1,3,3 (degenerate Δ23=0)",
        "n_gluons": 3,
        "n_x": 3,
        "n_alpha": 3,
        "edges": [1, 3, 3],
        "topology": "tgv_degen23",
        "J_latex": (
            r"\frac{ -\alpha_1(\alpha_2-\alpha_3)\,x_1(1+z)"
            r"\,(x_2 - z + x_2z) }"
            r"{ (\alpha_1\alpha_2\alpha_3)^{\varepsilon}\;"
            r"\Bigl[\alpha_1\Bigl(\alpha_3\bigl(z - x_2z + x_1(x_2-z+x_2z)\bigr)"
            r" + \alpha_2\bigl(z - x_2z + x_1x_3(x_2-z+x_2z)\bigr)\Bigr)"
            r"\Bigr]^{2-2\varepsilon} }"
        ),
        "J_plain": (
            "(-a1*(a2 - a3)*x1*(1 + z)*(x2 - z + x2*z))"
            " / ((a1*a2*a3)**eps"
            " * (a1*(a3*(z - x2*z + x1*(x2 - z + x2*z))"
            " + a2*(z - x2*z + x1*x3*(x2 - z + x2*z))))**(2 - 2*eps))"
        ),
        "integration_vars": ["x1", "x2", "x3", "a1", "a2", "a3"],
        "integration_domain": "[0,1]^3 × simplex(a1,a2,a3)",
        "kinematic_var": "z",
        "i0_prescription": "+i0",
        "alpha_constraint": "a1 + a2 + a3 = 1",
    },
    {
        "id": "3v3",
        "diagram": "diagrams/3v3_tgv_degen23.png",
        "label": "3-gluon TGV, edges 3,4,4 (degenerate Δ23=0)",
        "n_gluons": 3,
        "n_x": 3,
        "n_alpha": 3,
        "edges": [3, 4, 4],
        "topology": "tgv_degen23",
        "J_latex": (
            r"\frac{ -\alpha_1(\alpha_2-\alpha_3)\,x_1(1-x_2)\,z^2 }"
            r"{ (\alpha_1\alpha_2\alpha_3)^{\varepsilon}\;"
            r"\bigl[-\alpha_1\,x_1(1-x_2)(\alpha_3 + \alpha_2 x_3)\,z"
            r"\bigr]^{2-2\varepsilon} }"
        ),
        "J_plain": (
            "(-a1*(a2 - a3)*x1*(1 - x2)*z**2)"
            " / ((a1*a2*a3)**eps"
            " * (-a1*x1*(1 - x2)*(a3 + a2*x3)*z)**(2 - 2*eps))"
        ),
        "integration_vars": ["x1", "x2", "x3", "a1", "a2", "a3"],
        "integration_domain": "[0,1]^3 × simplex(a1,a2,a3)",
        "kinematic_var": "z",
        "i0_prescription": "+i0",
        "alpha_constraint": "a1 + a2 + a3 = 1",
    },
    {
        "id": "3v4",
        "diagram": "diagrams/3v4_tgv_degen12.png",
        "label": "3-gluon TGV, edges 3,3,4 (degenerate Δ12=0)",
        "n_gluons": 3,
        "n_x": 3,
        "n_alpha": 3,
        "edges": [3, 3, 4],
        "topology": "tgv_degen12",
        "J_latex": (
            r"\frac{ (\alpha_2-\alpha_1)\,\alpha_3\,x_1 x_2\,z^2 }"
            r"{ (\alpha_1\alpha_2\alpha_3)^{\varepsilon}\;"
            r"\bigl[-\alpha_3\,x_2\bigl(\alpha_2(x_1-1)"
            r" + \alpha_1(x_1 x_3-1)\bigr)\,z\bigr]^{2-2\varepsilon} }"
        ),
        "J_plain": (
            "((a2 - a1)*a3*x1*x2*z**2)"
            " / ((a1*a2*a3)**eps"
            " * (-a3*x2*(a2*(x1 - 1) + a1*(x1*x3 - 1))*z)**(2 - 2*eps))"
        ),
        "integration_vars": ["x1", "x2", "x3", "a1", "a2", "a3"],
        "integration_domain": "[0,1]^3 × simplex(a1,a2,a3)",
        "kinematic_var": "z",
        "i0_prescription": "+i0",
        "alpha_constraint": "a1 + a2 + a3 = 1",
    },
]

# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

IDS = [d["id"] for d in _ALL_DATA]
INTEGRALS = {d["id"]: d for d in _ALL_DATA}
ALL = _ALL_DATA

BY_TOPOLOGY: dict[str, list[dict]] = {}
for d in _ALL_DATA:
    BY_TOPOLOGY.setdefault(d["topology"], []).append(d)

BY_N_GLUONS: dict[int, list[dict]] = {}
for d in _ALL_DATA:
    BY_N_GLUONS.setdefault(d["n_gluons"], []).append(d)


def to_json(indent: int = 2) -> str:
    """Export the full dataset as a JSON string (matching cj_pure_J.json)."""
    payload = {
        "meta": META,
        "integrals": _ALL_DATA,
    }
    return json.dumps(payload, indent=indent, ensure_ascii=False)


def dump_json(path: str | Path = "cj_pure_J.json") -> None:
    """Write cj_pure_J.json to disk."""
    Path(path).write_text(to_json(), encoding="utf-8")


if __name__ == "__main__":
    print(f"Loaded {len(IDS)} integrals (J only).")
    for tid in IDS:
        J = INTEGRALS[tid]
        print(f"  {tid:10s}  {J['n_gluons']}-gluon  {J['topology']:20s}  "
              f"x-dim={J['n_x']}  α-dim={J['n_alpha']}")
