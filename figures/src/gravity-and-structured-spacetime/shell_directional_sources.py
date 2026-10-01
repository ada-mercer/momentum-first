#!/usr/bin/env python3
"""Render the approved shell-to-source figure through the 2D registry pipeline.

The contour is a reading graph; dp_Omega is the auxiliary measure defined in
shell-directional-sources.caption.md, not a microscopic constituent claim.
Default output: canonical PNG only. Request SVG/PDF companions explicitly.
"""
from __future__ import annotations

import argparse
import importlib.util
import math
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyArrow, Rectangle, Circle
import numpy as np
import yaml

SOURCE_DIR = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    'original_shell', SOURCE_DIR.parent / 'foundations/directional_momentum_readings.py')
original = importlib.util.module_from_spec(spec)
spec.loader.exec_module(original)
RED, BLUE, INK = '#be4045', '#246bb3', '#202d40'


def render(output_dir: Path, layout_path: Path, formats: list[str]) -> list[Path]:
    layout = yaml.safe_load(layout_path.read_text(encoding='utf-8'))
    output_dir.mkdir(parents=True, exist_ok=True)
    M=math.sqrt(2); p=1.; beta=math.pi/6
    R=lambda t: 1+p/(2*M)*np.cos(t-beta)
    plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'stix','svg.fonttype':'none','pdf.fonttype':42})
    fig=plt.figure(figsize=layout['figure_size'],facecolor='white')
    fig.text(*layout['title_position'],'From momentum shells to directional sources',ha='center',fontsize=23,weight='bold',color=INK)
    for plus,box in [(False,layout['panels']['minus']),(True,layout['panels']['plus'])]:
     ax=fig.add_axes(box); ax.set(xlim=(0,1),ylim=(0,1)); ax.axis('off')
     col=BLUE if plus else RED; s='+' if plus else '-'
     ax.add_patch(Rectangle((0,0),1,1,fc='#eef5fc' if plus else '#fceeee',ec='none'))
     ax.text(.5,.91,r'Source in $'+s+r'\hat{k}$',ha='center',fontsize=18,color=col,weight='bold')
     length=.55*float(R(0 if plus else math.pi))
     ax.add_patch(FancyArrow(.5-length/2 if plus else .5+length/2,.67,length if plus else -length,0,width=.065,head_width=.17,head_length=.10,length_includes_head=True,color=col))
     ax.text(.5,.25,r'$\mathcal{J}_k^'+s+r'=\left\langle\sum_a p_{k,a}^'+s+r'\right\rangle$',ha='center',fontsize=24,color=INK)
    ax=fig.add_axes(layout['panels']['shell']); ax.set_aspect('equal'); ax.set(xlim=layout['shell_limits']['x'],ylim=layout['shell_limits']['y']); ax.axis('off')
    # The contour remains the original directional-reading graph, normalized by M.
    for lo,hi,col in [(-math.pi/2,math.pi/2,'#e4effa'),(math.pi/2,3*math.pi/2,'#fae7e7')]:
     t=np.linspace(lo,hi,600); pts=np.column_stack((R(t)*np.cos(t),R(t)*np.sin(t)))
     ax.add_patch(Polygon(np.vstack(([0,0],pts,[0,0])),fc=col,ec='none'))
    t=np.linspace(0,2*math.pi,1200); ax.plot(R(t)*np.cos(t),R(t)*np.sin(t),color=original.SHELL_EDGE,lw=layout['lines']['contour'])
    ax.plot([0,0],[-.94,1.28],ls=(0,(3,3)),color=original.GRID,lw=layout['lines']['axis'])
    ax.annotate('',xy=(1.6,0),xytext=(-1.,0),arrowprops=dict(arrowstyle='->',color=original.GRID,lw=layout['lines']['axis']))
    ax.text(*layout['labels']['axis_plus'],r'$+\hat k$',color=BLUE,fontsize=17)
    ax.text(*layout['labels']['axis_minus'],r'$-\hat k$',color=RED,fontsize=17)
    ax.add_patch(Circle((0,0),.062,fc=original.INK,ec='white',lw=1.,zorder=9))
    # Original scalar-spoke drawing helpers: capped readings, no emitted arrows.
    for angle,color in [(30,BLUE),(210,RED),(0,BLUE),(180,RED)]:
     original.scalar_spoke(ax,angle,float(R(math.radians(angle))),color,width=layout['lines']['principal'] if angle in (30,210) else layout['lines']['directional'])
    ax.text(*layout['labels']['p_plus'],r'$p^+$',fontsize=24,color=BLUE)
    ax.text(*layout['labels']['p_minus'],r'$p^-$',fontsize=24,color=RED)
    ax.text(*layout['labels']['pk_plus'],r'$p_k^+$',fontsize=21,color=BLUE)
    ax.text(*layout['labels']['pk_minus'],r'$p_k^-$',fontsize=21,color=RED)
    # Solid-angle element shown schematically in a meridional section, quadrant IV.
    a=math.radians(-48); da=math.radians(9); ts=np.linspace(a-da/2,a+da/2,60)
    pts=np.column_stack((R(ts)*np.cos(ts),R(ts)*np.sin(ts)))
    ax.add_patch(Polygon(np.vstack(([0,0],pts,[0,0])),fc=BLUE,alpha=.22,ec='none'))
    ax.plot(pts[:,0],pts[:,1],color=BLUE,lw=3)
    for ang in [a-da/2,a+da/2]:
     ax.plot([0,R(ang)*math.cos(ang)],[0,R(ang)*math.sin(ang)],color=BLUE,lw=.7)
    ax.text(*layout['labels']['solid_angle'],r'$d\Omega$',fontsize=21,color=BLUE)
    ax.text(*layout['labels']['direction'],r'$\hat l$',fontsize=18,color=BLUE)
    fig.text(*layout['integral_position'],r'$p_k^+=\int_{\hat l\cdot\hat k>0}(\hat l\cdot\hat k)\,dp_\Omega$',ha='center',fontsize=27,color=BLUE)
    # Independent quadrature around k, including all azimuths, for the displayed oblique p.
    u,w=np.polynomial.legendre.leggauss(120); u=(u+1)/2; w=w/2
    ph=np.linspace(0,2*math.pi,240,endpoint=False)
    values=[]
    for s in [1,-1]:
     dot=p*(math.cos(beta)*s*u[:,None]+math.sin(beta)*np.sqrt(1-u[:,None]**2)*np.cos(ph)[None,:])
     val=float(np.sum(w[:,None]*u[:,None]*(M+.75*dot)/math.pi)*(2*math.pi/len(ph)))
     target=M+s*.5*p*math.cos(beta)
     assert abs(val-target)<1e-12
     values.append({'sign':s,'integral':val,'reading':target})
    paths = []
    for ext in formats:
        path = output_dir / f'shell-directional-sources.{ext}'
        # SVG IDs and PDF timestamps must not introduce incidental build drift.
        metadata = {'CreationDate': None, 'ModDate': None} if ext == 'pdf' else (
            {'Date': None} if ext == 'svg' else None)
        with matplotlib.rc_context({'svg.hashsalt': 'shell-directional-sources'}):
            fig.savefig(path, dpi=layout['dpi'], facecolor='white', metadata=metadata)
        paths.append(path)
    plt.close(fig)
    return paths


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path,
                        default=SOURCE_DIR.parents[1] / 'build/gravity-and-structured-spacetime')
    parser.add_argument('--layout', type=Path,
                        default=SOURCE_DIR / 'shell_directional_sources.layout.yaml')
    parser.add_argument('--formats', nargs='+', choices=['png', 'svg', 'pdf'], default=['png'])
    args = parser.parse_args()
    for path in render(args.output_dir.resolve(), args.layout.resolve(), args.formats):
        print(path)


if __name__ == '__main__':
    main()
