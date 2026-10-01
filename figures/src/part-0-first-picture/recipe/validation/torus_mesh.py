"""One visible parameter grid for every torus in this chapter candidate.

48 major-angle stations and 24 minor-angle stations halve the angular cell
widths of the preceding 24-by-12 mode grid. Smooth curve sampling is separate
from visible cell spacing. Geometry, orientation and display scale stay local.
"""
import numpy as np
MAJOR_DIVISIONS=48
MINOR_DIVISIONS=24
MAJOR_SAMPLES=321
MINOR_SAMPLES=161

def parameter_lines():
    for j,u in enumerate(np.linspace(0,2*np.pi,MAJOR_DIVISIONS,endpoint=False)):
        v=np.linspace(0,2*np.pi,MINOR_SAMPLES)
        yield 'u',j,np.full_like(v,u),v
    for j,v in enumerate(np.linspace(0,2*np.pi,MINOR_DIVISIONS,endpoint=False)):
        u=np.linspace(0,2*np.pi,MAJOR_SAMPLES)
        yield 'v',j,u,np.full_like(u,v)

def mesh_record(asset,tori):
    return dict(asset=asset,torus_count=tori,major_divisions=MAJOR_DIVISIONS,
                minor_divisions=MINOR_DIVISIONS)
