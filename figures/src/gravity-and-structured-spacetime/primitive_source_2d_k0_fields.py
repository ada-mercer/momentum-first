#!/usr/bin/env python3
"""Primitive channel contributions from a finite normalized axial profile.

The historical file/asset ID stays in place. This is a linear source-basis
illustration, not a replacement light-beam model. The actual axial Newton
convolution is evaluated; no K0 identity, core clipping or cylinder boundary.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import xml.etree.ElementTree as ET
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.patches import Circle
import numpy as np
from numpy.polynomial.legendre import leggauss

ROOT=Path(__file__).resolve().parents[3]
SLUG="primitive-source-2d-k0-fields"
TITLE="Primitive single-channel and balanced-pair response"
DESCRIPTION=("Whole-profile channel pairs J1plus/zero and J1plus/2,J1minus/2 "
             "label the axial source graphs. Positive amounts Qplus and Qminus "
             "are the integrals of matched full-strength opposite profiles. "
             "Temporal channel maps agree and directional maps cancel in the pair. "
             "Both directional panels use upper 1, lower 0: theta10=-theta01, "
             "and phi10=4 theta10 at first order. Transport is separate.")


def axial_profile(z, r0=1.0):
    return np.exp(-np.abs(np.asarray(z,dtype=float))/r0)/(2*r0)


def axial_kernel(radius, r0=1.0, order=96):
    """Integral f(z)/sqrt(r^2+z^2) dz, evaluated off the source axis.

    Substitute z=r*sinh(t); the integral becomes
    (1/r0) integral exp[-(r/r0)*sinh(t)] dt. A tail exponent of 48
    controls quadrature truncation; it is not a cutoff of the source profile.
    """
    radii=np.asarray(radius,dtype=float)
    flat=radii.ravel()
    result=np.full(flat.shape,np.nan)
    nodes,weights=leggauss(order)
    positive=np.flatnonzero(flat>0)
    for start in range(0,len(positive),2048):
        where=positive[start:start+2048]
        ratio=flat[where]/r0
        stop=np.arcsinh(48/ratio)
        t=(nodes[None,:]+1)*stop[:,None]/2
        result[where]=np.sum(np.exp(-ratio[:,None]*np.sinh(t))*weights[None,:],axis=1)*stop/(2*r0)
    return result.reshape(radii.shape)


def compute_fields(n=401, r0=1.0, qplus=1.0, coupling=0.001, extent=4.0):
    x=np.linspace(-extent*r0,extent*r0,n)
    X,Y=np.meshgrid(x,x)
    r=np.hypot(X,Y)
    shown=(r>0)&(r<=extent*r0)
    kernel=np.full(r.shape,np.nan)
    kernel[shown]=axial_kernel(r[shown],r0)
    # Only the mean/difference channel terms of the linear source map.
    # The resolved C contribution is separate, not inferred or set to zero
    # as a property of a material population.
    theta00=coupling*qplus*kernel/2
    theta01=coupling*qplus*kernel
    z=np.linspace(-5*r0,5*r0,1001)
    profile=qplus*axial_profile(z,r0)
    return {
        "x":x,"r":r,"kernel":kernel,"theta00":theta00,
        "theta01_single":theta01,"theta01_pair":0*theta01,
        "theta10_single":-theta01,"theta10_pair":0*theta01,
        "phi00_single":1-theta00,"phi00_pair":1-theta00,
        "phi10_single":-4*theta01,"phi10_pair":0*theta01,
        "source_z":z,"source_plus_single":profile,"source_minus_single":0*profile,
        "source_plus_pair":profile/2,"source_minus_pair":profile/2,
        # Equal positive integrals of the two full-strength reference profiles.
        "r0":np.array(r0),"qplus":np.array(qplus),"qminus":np.array(qplus),
        "coupling":np.array(coupling),
        "extent":np.array(extent),
    }


def draw_profile(ax, fields, paired):
    z=fields["source_z"]
    suffix="pair" if paired else "single"
    plus=fields["source_plus_"+suffix];minus=fields["source_minus_"+suffix]
    ax.fill_between(z,plus,color="#6d9cba",alpha=.13,lw=0)
    ax.plot(z,plus,color="#2a658e",lw=2.4,zorder=3)
    ax.plot(z,minus,color="#b5663d",lw=1.8,ls=(0,(4,3)),zorder=4)
    ax.set(xlim=(-5,5),ylim=(-.045,.61))
    for side in ("left","right","top"):ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_position(("data",0));ax.spines["bottom"].set_color("#aab1b7")
    ax.spines["bottom"].set_linewidth(.8)
    ax.set_xticks([0]);ax.set_xticklabels(["0"],fontsize=14)
    ax.set_yticks([]);ax.tick_params(axis="x",length=2,color="#aab1b7",pad=3)
    ax.text(5.12,-.012,r"$z$",fontsize=19,ha="left",va="center",clip_on=False)
    # Pair labels above the axes name whole distributions, not point values.
    # The quiet right-hand wing holds their integrated amounts.
    amounts=(r"$\left(\frac{Q^+}{2},\ \frac{Q^-}{2}\right)$" if paired
             else r"$\left(Q^+,\ 0\right)$")
    ax.text(.98,.90,"Amounts",transform=ax.transAxes,fontsize=14,
            color="#596773",ha="right",va="center")
    ax.text(.98,.61,amounts,transform=ax.transAxes,fontsize=21,
            color="#263b4a",ha="right",va="center")


def draw_map(ax, fields, key, title, cmap, limits):
    R=float(fields["extent"]*fields["r0"])
    Z=fields[key]
    ax.imshow(Z,origin="lower",extent=(-R,R,-R,R),cmap=cmap,
              norm=Normalize(*limits),interpolation="bilinear")
    if np.nanmax(Z)>np.nanmin(Z):
        lo,hi=np.nanmin(Z),np.nanmax(Z)
        # Contours trace the profile without becoming repeated calibrations.
        levels=lo+(hi-lo)*np.array([.10,.20,.34,.52,.73])
        ax.contour(fields["x"],fields["x"],Z,levels=levels,
                   colors="#455666",linewidths=.42,alpha=.22)
    ax.add_patch(Circle((0,0),R,fill=False,lw=.7,ec="#bdc6cd"))
    ax.plot(0,0,"o",ms=3.0,color="#526270",zorder=6)
    ax.set(xlim=(-R*1.04,R*1.04),ylim=(-R*1.04,R*1.04),aspect="equal")
    ax.set_axis_off()
    ax.set_title(title,fontsize=23,pad=9)


def render(output_dir,layout_report=None):
    plt.rcParams.update({"font.family":"DejaVu Sans","mathtext.fontset":"dejavusans",
                         "font.size":15,"svg.fonttype":"none","pdf.fonttype":42,
                         "svg.hashsalt":SLUG})
    fields=compute_fields()
    fig=plt.figure(figsize=(14,10),facecolor="white")
    gs=fig.add_gridspec(3,5,width_ratios=[1,1,.28,1,1],height_ratios=[.68,1,1],
                       left=.055,right=.945,bottom=.035,top=.835,hspace=.37,wspace=.22)
    groups=[(0,False),(3,True)]
    for col,paired in groups:
        box=gs[0,col:col+2].get_position(fig)
        center=(box.x0+box.x1)/2
        heading="Balanced pair" if paired else "Single channel"
        profiles=(r"$\left(\frac{\mathcal{J}_1^+}{2},\ \frac{\mathcal{J}_1^-}{2}\right)$"
                  if paired else r"$\left(\mathcal{J}_1^+,\ 0\right)$")
        fig.text(center,.953,heading,ha="center",va="center",fontsize=25)
        fig.text(center,.900,profiles,ha="center",va="center",fontsize=24)
        # Preserve the approved curve rendering; only its labels change.
        ax=fig.add_subplot(gs[0,col:col+2])
        draw_profile(ax,fields,paired)
    blue=matplotlib.colormaps["Blues"].copy();signed=matplotlib.colormaps["RdBu_r"].copy()
    for cmap in (blue,signed):cmap.set_bad("white")
    tmax=float(np.nanmax(fields["theta00"]))
    dmax=float(np.nanmax(fields["theta01_single"]))
    for col,paired in groups:
        suffix="pair" if paired else "single"
        zero="=0" if paired else ""
        panels=[(1,col,"theta00",r"$\theta^0{}_0$",blue,(0,tmax)),
                (1,col+1,"theta10_"+suffix,r"$\theta^1{}_0"+zero+"$",signed,(-dmax,dmax)),
                (2,col,"phi00_"+suffix,r"$\phi^0{}_0$",blue,(1-tmax,1)),
                (2,col+1,"phi10_"+suffix,r"$\phi^1{}_0"+zero+"$",signed,(-4*dmax,4*dmax))]
        for row,column,key,title,cmap,limits in panels:
            draw_map(fig.add_subplot(gs[row,column]),fields,key,title,cmap,limits)
    fig.add_artist(plt.Line2D([.5,.5],[.05,.975],transform=fig.transFigure,color="#dde2e7",lw=.8))
    layout=validate_text_layout(fig)
    if layout_report:
        layout_report.parent.mkdir(parents=True,exist_ok=True)
        layout_report.write_text(json.dumps(layout,indent=2)+"\n")
    print(f"Text layout: {layout['labels_checked']} labels; no collisions or clipping")
    output_dir.mkdir(parents=True,exist_ok=True)
    for ext in ("png","pdf","svg"):
        path=output_dir/f"{SLUG}.{ext}"
        metadata={"Title":TITLE,"Description":DESCRIPTION} if ext=="png" else (
            {"Title":TITLE,"Subject":DESCRIPTION,"Author":"Momentum First","CreationDate":None}
            if ext=="pdf" else {"Title":TITLE,"Description":DESCRIPTION,"Creator":"Momentum First","Date":None})
        fig.savefig(path,dpi=180,metadata=metadata)
        if ext=="svg":add_svg_accessibility(path)
        print(path)
    plt.close(fig)
    return fields


def validate_text_layout(fig):
    """Check actual Agg text extents; image review still checks non-text marks."""
    from matplotlib.text import Text
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    candidates = list(fig.texts)
    for ax in fig.axes:
        candidates.extend([ax.title, *ax.texts])
        if ax.axison:
            candidates.extend(ax.get_xticklabels())
            candidates.extend(ax.get_yticklabels())
    labels = []
    seen = set()
    for text in candidates:
        if id(text) in seen or not text.get_visible() or not text.get_text().strip():
            continue
        seen.add(id(text))
        # For annotations, measure the text rather than its leader arrow.
        box = Text.get_window_extent(text, renderer)
        labels.append({"text": text.get_text(), "bounds": list(box.extents)})
    collisions = []
    for i, first in enumerate(labels):
        a = first["bounds"]
        for second in labels[i+1:]:
            b = second["bounds"]
            if min(a[2], b[2]) > max(a[0], b[0])+1 and min(a[3], b[3]) > max(a[1], b[1])+1:
                collisions.append([first["text"], second["text"]])
    width, height = fig.canvas.get_width_height()
    clipped = [item["text"] for item in labels if item["bounds"][0] < 0 or item["bounds"][1] < 0 or item["bounds"][2] > width or item["bounds"][3] > height]
    report = {"labels_checked": len(labels), "collisions": collisions, "clipped": clipped, "labels": labels}
    if collisions or clipped:
        raise ValueError("Text layout needs repair: "+json.dumps({"collisions": collisions, "clipped": clipped}))
    return report

def add_svg_accessibility(path):
    # Preserve namespace prefixes while adding explicit accessible labels.
    namespaces = {}
    for _, (prefix, uri) in ET.iterparse(path, events=["start-ns"]):
        namespaces[prefix] = uri
    for prefix, uri in namespaces.items():
        ET.register_namespace(prefix, uri)
    tree = ET.parse(path)
    root = tree.getroot()
    ns = "{http://www.w3.org/2000/svg}"
    # Identical raster panels can receive duplicate content-hashed image IDs.
    # These image elements are not reusable definitions; rename only when
    # no fragment reference depends on the generated ID.
    references = [value for element in root.iter() for value in element.attrib.values()]
    for number, image in enumerate(root.iter(ns+"image"), 1):
        old_id = image.get("id")
        if old_id and any(value == "#"+old_id or "url(#"+old_id+")" in value for value in references):
            raise ValueError("Cannot rename a referenced raster ID: "+old_id)
        image.set("id", f"primitive-phi-raster-{number}")
    title = root.find(ns+"title")
    if title is None:
        title = ET.Element(ns+"title")
        root.insert(0, title)
    title.set("id", "primitive-phi-title")
    title.text = TITLE
    desc = ET.Element(ns+"desc", {"id": "primitive-phi-description"})
    desc.text = DESCRIPTION
    root.insert(1, desc)
    root.set("role", "img")
    root.set("aria-labelledby", "primitive-phi-title primitive-phi-description")
    tree.write(path, encoding="utf-8", xml_declaration=True)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir",type=Path,default=ROOT/"figures/build/gravity-and-structured-spacetime")
    parser.add_argument("--data",type=Path)
    parser.add_argument("--layout-report",type=Path)
    args=parser.parse_args()
    fields=render(args.output_dir,args.layout_report)
    if args.data:
        args.data.parent.mkdir(parents=True,exist_ok=True)
        np.savez_compressed(args.data,**fields)
        print(args.data)


if __name__=="__main__":main()
