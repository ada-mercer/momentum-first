#!/usr/bin/env python3
"""Render the canonical Foundations directional-momentum notation figure.

This is a deterministic schematic. Lengths are illustrative; the
displayed equations, not the drawn scale, carry the quantitative definition.
"""

from __future__ import annotations

import argparse
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import yaml
from matplotlib.patches import Arc, Circle, FancyArrowPatch, Polygon


INK = "#172033"
MUTED = "#657186"
GRID = "#AAB4C3"
TRANSLATION = "#275D9B"
READING_PLUS = "#2F67B2"
READING_MINUS = "#C4514A"
READING_K = "#147D86"
READING_K_MINUS = "#8E5A9F"
READING_PERP = "#657186"
SHELL_PLUS = "#DDE9F8"
SHELL_MINUS = "#F5DEDA"
SHELL_EDGE = "#435167"
PANEL = "#F6F8FB"


def polar(radius: float, degrees: float) -> tuple[float, float]:
    theta = math.radians(degrees)
    return radius * math.cos(theta), radius * math.sin(theta)


def line_relative_position(
    anchor: tuple[float, float], angle: float, position: dict
) -> tuple[float, float]:
    """Resolve along/normal offsets relative to an oriented geometry line."""
    along_x, along_y = polar(position["along"], angle)
    normal_x, normal_y = polar(position["normal"], angle + 90.0)
    return anchor[0] + along_x + normal_x, anchor[1] + along_y + normal_y


def scalar_spoke(ax, angle: float, radius: float, color: str, width: float = 2.1) -> None:
    """Draw a scalar radial dimension: line plus terminal cap, never an arrow."""
    x, y = polar(radius, angle)
    ax.plot([0, x], [0, y], color=color, lw=width, solid_capstyle="round", zorder=4)
    cap_half = 0.055
    dx, dy = polar(cap_half, angle + 90)
    ax.plot([x - dx, x + dx], [y - dy, y + dy], color=color, lw=width, zorder=5)


def reference_tick(ax, angle: float, radius: float = 1.0) -> None:
    """Mark the undeformed radius M locally without drawing a second shell."""
    x, y = polar(radius, angle)
    dx, dy = polar(0.045, angle + 90)
    ax.plot([x - dx, x + dx], [y - dy, y + dy], color=MUTED, lw=1.05, zorder=6)


def signed_offset(
    ax,
    angle: float,
    start: float,
    end: float,
    label: str,
    color: str,
    label_position: dict,
) -> None:
    """Dimension the signed shell displacement from M to a reading."""
    x0, y0 = polar(start, angle)
    x1, y1 = polar(end, angle)
    ax.add_patch(
        FancyArrowPatch(
            (x0, y0),
            (x1, y1),
            arrowstyle="<->",
            mutation_scale=7.5,
            lw=0.85,
            color=color,
            shrinkA=1,
            shrinkB=1,
            zorder=7,
        )
    )
    xm, ym = polar((start + end) / 2, angle)
    label_x, label_y = line_relative_position((xm, ym), angle, label_position)
    ax.text(
        label_x,
        label_y,
        label,
        ha=label_position["ha"],
        va=label_position["va"],
        fontsize=8.4,
        color=color,
        zorder=8,
    )


def load_layout(layout_path: Path) -> dict:
    """Load human-editable text positions from YAML."""
    with layout_path.open("r", encoding="utf-8") as stream:
        layout = yaml.safe_load(stream)
    if not isinstance(layout, dict):
        raise ValueError(f"Layout must be a YAML mapping: {layout_path}")
    return layout


def render(output_dir: Path, layout_path: Path) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    layout = load_layout(layout_path)
    shell_layout = layout["shell_panel"]
    vector_layout = layout["vector_panel"]

    # Canonical book geometry. The physical values obey M=sqrt(p_f^2+p^2);
    # only plotted lengths are normalized by M so the reference shell has
    # display radius 1. Alpha remains 30 degrees behind the scenes, but the
    # visible figure treats it as the general angle alpha.
    p_f = 1.0
    p = 1.0
    M = math.sqrt(p_f**2 + p**2)
    alpha_deg = 30.0
    alpha_rad = math.radians(alpha_deg)
    p_over_M = p / M
    M_display = 1.0
    aligned_high = 1.0 + p_over_M / 2
    aligned_low = 1.0 - p_over_M / 2
    perpendicular_angle = alpha_deg + 90.0
    k_plus = 1.0 + 0.5 * p_over_M * math.cos(alpha_rad)
    k_minus = 1.0 - 0.5 * p_over_M * math.cos(alpha_rad)

    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "mathtext.fontset": "stix",
            "font.size": 9.2,
            "axes.linewidth": 0.0,
            "pdf.fonttype": 42,
            "svg.fonttype": "none",
        }
    )

    fig = plt.figure(figsize=(7.2, 3.75), facecolor="white")
    gs = fig.add_gridspec(1, 2, width_ratios=[0.98, 1.02], wspace=0.08)
    geom = fig.add_subplot(gs[0, 0])
    shell = fig.add_subplot(gs[0, 1])

    for ax in (shell, geom):
        ax.set_facecolor(PANEL)
        for spine in ax.spines.values():
            spine.set_visible(False)
        ax.set_xticks([])
        ax.set_yticks([])

    # Exact normalized 2D cross-section of the canonical directional shell:
    # r(beta)/M = 1 + [p/(2M)] cos(beta-alpha).
    shell_angles = [alpha_deg - 90.0 + i * 360.0 / 360 for i in range(361)]
    shell_points = [
        polar(1.0 + 0.5 * p_over_M * math.cos(math.radians(angle - alpha_deg)), angle)
        for angle in shell_angles
    ]
    plus_boundary = shell_points[:181]
    minus_boundary = shell_points[180:]
    shell.add_patch(Polygon(plus_boundary, closed=True, fc=SHELL_PLUS, ec="none", zorder=0))
    shell.add_patch(Polygon(minus_boundary, closed=True, fc=SHELL_MINUS, ec="none", zorder=0))
    shell.add_patch(
        Circle(
            (0, 0),
            M_display,
            fill=False,
            ec=GRID,
            lw=1.05,
            ls=(0, (3, 3)),
            zorder=1,
        )
    )
    shell.add_patch(Polygon(shell_points, closed=True, fill=False, ec=SHELL_EDGE, lw=1.5, zorder=2))

    # Exact key-direction checks: extrema, perpendicular reading, and the two
    # independently chosen k-direction readings must all lie on the same shell.
    def shell_radius_display(beta_deg: float) -> float:
        return 1.0 + 0.5 * p_over_M * math.cos(math.radians(beta_deg - alpha_deg))

    assert math.isclose(shell_radius_display(alpha_deg), aligned_high, rel_tol=0.0, abs_tol=1e-12)
    assert math.isclose(shell_radius_display(alpha_deg + 180.0), aligned_low, rel_tol=0.0, abs_tol=1e-12)
    assert math.isclose(shell_radius_display(perpendicular_angle), M_display, rel_tol=0.0, abs_tol=1e-12)
    assert math.isclose(shell_radius_display(0.0), k_plus, rel_tol=0.0, abs_tol=1e-12)
    assert math.isclose(shell_radius_display(180.0), k_minus, rel_tol=0.0, abs_tol=1e-12)

    # Panel (b): all capped spokes are positive readings of one shell.
    xp, yp = polar(1.50, alpha_deg)
    shell.plot([-xp, xp], [-yp, yp], color=GRID, lw=0.9, ls=(0, (3, 3)), zorder=1)
    shell.plot([-1.48, 1.48], [0, 0], color=GRID, lw=0.9, ls=(0, (3, 3)), zorder=1)
    xperp, yperp = polar(1.16, perpendicular_angle)
    shell.plot([0, xperp], [0, yperp], color=GRID, lw=0.9, ls=(0, (3, 3)), zorder=1)

    scalar_spoke(shell, alpha_deg, aligned_high, READING_PLUS, width=2.15)
    scalar_spoke(shell, alpha_deg + 180, aligned_low, READING_MINUS, width=2.15)
    scalar_spoke(shell, perpendicular_angle, M_display, READING_PERP, width=1.85)
    scalar_spoke(shell, 0, k_plus, READING_K, width=1.95)
    scalar_spoke(shell, 180, k_minus, READING_K_MINUS, width=1.95)
    shell.add_patch(Circle((0, 0), 0.062, fc=INK, ec="white", lw=1.0, zorder=9))

    # The handwritten review asks the drawing itself to expose the shell law:
    # each reading is M plus or minus a signed half-momentum deformation. Local
    # M ticks do this without reinstating a misleading reference-M circle.
    for angle in (alpha_deg, alpha_deg + 180, perpendicular_angle, 0, 180):
        reference_tick(shell, angle, M_display)
    half_offset_layout = shell_layout["half_offset_labels"]
    signed_offset(
        shell,
        alpha_deg,
        M_display,
        aligned_high,
        r"$\frac{1}{2}p$",
        READING_PLUS,
        half_offset_layout["p_plus"],
    )
    signed_offset(
        shell,
        alpha_deg + 180,
        M_display,
        aligned_low,
        r"$-\frac{1}{2}p$",
        READING_MINUS,
        half_offset_layout["p_minus"],
    )
    signed_offset(
        shell,
        0,
        M_display,
        k_plus,
        r"$\frac{1}{2}p_k$",
        READING_K,
        half_offset_layout["pk_plus"],
    )
    signed_offset(
        shell,
        180,
        M_display,
        k_minus,
        r"$-\frac{1}{2}p_k$",
        READING_K_MINUS,
        half_offset_layout["pk_minus"],
    )

    reading_layout = shell_layout["reading_labels"]
    x, y = polar(aligned_high, alpha_deg)
    pos = reading_layout["p_plus"]
    label_x, label_y = line_relative_position((x, y), alpha_deg, pos)
    shell.text(label_x, label_y, r"$p^+$", ha=pos["ha"], va=pos["va"], fontsize=12.0, color=READING_PLUS)
    x, y = polar(aligned_low, alpha_deg + 180)
    pos = reading_layout["p_minus"]
    label_x, label_y = line_relative_position((x, y), alpha_deg + 180, pos)
    shell.text(label_x, label_y, r"$p^-$", ha=pos["ha"], va=pos["va"], fontsize=12.0, color=READING_MINUS)
    x, y = polar(M_display, perpendicular_angle)
    pos = reading_layout["p_perp"]
    label_x, label_y = line_relative_position((x, y), perpendicular_angle, pos)
    shell.text(label_x, label_y, r"$p^\perp=M$", ha=pos["ha"], va=pos["va"], fontsize=12.0, color=READING_PERP)
    x, y = polar(k_plus, 0)
    pos = reading_layout["pk_plus"]
    label_x, label_y = line_relative_position((x, y), 0, pos)
    shell.text(label_x, label_y, r"$p_k^{+}$", ha=pos["ha"], va=pos["va"], fontsize=11.0, color=READING_K)
    x, y = polar(k_minus, 180)
    pos = reading_layout["pk_minus"]
    label_x, label_y = line_relative_position((x, y), 180, pos)
    shell.text(label_x, label_y, r"$p_k^{-}$", ha=pos["ha"], va=pos["va"], fontsize=11.0, color=READING_K_MINUS)

    equation_layout = shell_layout["equations"]
    pos = equation_layout["p_pm"]
    shell.text(pos["x"], pos["y"], r"$p^{\pm}=M\pm\frac{1}{2}p$", transform=shell.transAxes, ha=pos["ha"], va=pos["va"], fontsize=9.2, color=INK)
    pos = equation_layout["pk_pm"]
    shell.text(pos["x"], pos["y"], r"$p_k^{\pm}=M\pm\frac{1}{2}p_k$", transform=shell.transAxes, ha=pos["ha"], va=pos["va"], fontsize=9.0, color=INK)
    pos = shell_layout["title"]
    shell.text(pos["x"], pos["y"], "(b)  Shell readings", transform=shell.transAxes, ha=pos["ha"], va=pos["va"], fontsize=10.0, weight="bold", color=INK)

    shell.set_aspect("equal")
    shell.set_xlim(-1.60, 1.60)
    shell.set_ylim(-1.35, 1.35)

    # Panel (a): conventional vector/component momentum triangle.
    geom.plot([-0.22, 1.46], [0, 0], color=GRID, lw=1.1, zorder=1)

    vector_length = 1.04
    p_tip = polar(vector_length, alpha_deg)
    geom.add_patch(
        FancyArrowPatch(
            (0, 0),
            p_tip,
            arrowstyle="-|>",
            mutation_scale=15,
            lw=2.6,
            color=TRANSLATION,
            shrinkA=3,
            shrinkB=0,
            zorder=7,
        )
    )

    projection_x = p_tip[0]
    geom.plot([0, projection_x], [0, 0], color=READING_K, lw=2.4, solid_capstyle="round", zorder=5)
    geom.plot([projection_x, projection_x], [0, p_tip[1]], color=READING_K_MINUS, lw=2.4, solid_capstyle="round", zorder=5)
    geom.plot([projection_x - 0.075, projection_x - 0.075, projection_x], [0, 0.075, 0.075], color=MUTED, lw=0.9, zorder=6)
    geom.add_patch(Arc((0, 0), 0.72, 0.72, theta1=0, theta2=alpha_deg, ec=MUTED, lw=1.0, zorder=3))
    geom.add_patch(Circle((0, 0), 0.055, fc=INK, ec="white", lw=1.0, zorder=9))

    pos = vector_layout["vector_label"]
    geom.text(p_tip[0] + pos["dx"], p_tip[1] + pos["dy"], r"$\vec p$", ha=pos["ha"], va=pos["va"], fontsize=12.5, color=TRANSLATION)
    pos = vector_layout["magnitude_label"]
    geom.text(pos["x"], pos["y"], r"$p=|\vec p|$", ha=pos["ha"], va=pos["va"], fontsize=10.2, color=TRANSLATION, rotation=alpha_deg)
    pos = vector_layout["alpha_label"]
    geom.text(pos["x"], pos["y"], r"$\alpha$", ha=pos["ha"], va=pos["va"], fontsize=9.4, color=MUTED)
    pos = vector_layout["projection_equation"]
    geom.text(projection_x * pos["x_fraction"], pos["y"], r"$p_k=\vec p\!\cdot\!\hat k=p\,\cos\alpha$", ha=pos["ha"], va=pos["va"], fontsize=9.7, color=READING_K)
    # Keep the perpendicular leg as triangle geometry, but omit its local label
    # and the two lower identities, as marked in the annotated reference. This
    # leaves panel (a) focused on p-vector, magnitude, angle, and projection.
    pos = vector_layout["title"]
    geom.text(pos["x"], pos["y"], "(a)  Vector decomposition", transform=geom.transAxes, ha=pos["ha"], va=pos["va"], fontsize=10.0, weight="bold", color=INK)

    geom.set_aspect("equal")
    geom.set_xlim(-0.30, 1.65)
    geom.set_ylim(-0.68, 1.05)

    fig.subplots_adjust(left=0.025, right=0.985, top=0.84, bottom=0.08)

    base = output_dir / "directional-momentum-readings"
    paths = [base.with_suffix(".png")]
    fig.savefig(paths[0], dpi=300, facecolor="white")
    plt.close(fig)
    return paths


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parents[2] / "build" / "foundations",
        help="Output directory (default: canonical Foundations build directory).",
    )
    parser.add_argument(
        "--layout",
        type=Path,
        default=Path(__file__).with_name("directional_momentum_readings.layout.yaml"),
        help="YAML file containing label and equation positions.",
    )
    args = parser.parse_args()
    for path in render(args.output_dir.resolve(), args.layout.resolve()):
        print(path)


if __name__ == "__main__":
    main()
