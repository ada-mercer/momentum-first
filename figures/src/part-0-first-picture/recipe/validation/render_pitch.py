"""Bosic-only constant-radius pitch comparison; shared geometry3d backend.

Small torus glyphs orient the centre positions. Their internal minor phase
never enters the helix. Its radius matches the outer torus radius.
"""
from torus_mesh import parameter_lines,mesh_record
from pathlib import Path
import json
import numpy as np
from PIL import Image
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mode_geometry import (ROOT, RB, RF, xyz, U, V, curve_object, SceneSpec, SceneObject,
    FigureLayout, CameraPreset, CAMERA_PRESETS, render_scene_with_backend)

PITCHES=(3.0,5.0)
GLYPH_SCALE=.30
RADIUS=GLYPH_SCALE*(RB+RF)
CAMERA='candidate-pitch'
CAMERA_PRESETS[CAMERA]=CameraPreset(CAMERA,25,12,
    projection_mode='orthographic',orthographic_scale=2.5)


def history(phi,pitch):
    """Fixed outer torus radius; no minor-phase dependence."""
    phi=np.asarray(phi)
    return np.stack([RADIUS*np.cos(phi),pitch*phi/(2*np.pi),-RADIUS*np.sin(phi)],axis=-1)


def glyph(q,j):
    g=GLYPH_SCALE*xyz(U,V);g[...,1]+=q
    objects=[SceneObject(f'torus-{j}','sampled_surface',dict(
        x=g[...,0],y=g[...,1],z=g[...,2],color='#ae96c8',alpha=.14,shade=True,ambient=.7))]
    # Restrained, smooth coordinate guides: never a foreground wire cage.
    for axis,i,u,v in parameter_lines():
        p=GLYPH_SCALE*xyz(u,v,lift=.009);p[:,1]+=q
        objects.append(curve_object(f'grid-{j}-{axis}-{i}',p,'#9a83b4',.005,.14))
    return objects


def scene(pitch):
    objects=[]
    for j in range(3):objects.extend(glyph(j*pitch,j))
    phi=np.linspace(0,4*np.pi,2001)
    objects.append(curve_object('bosic-helix',history(phi,pitch),'#276b9e',.035))
    points=history(np.array([0.,2*np.pi,4*np.pi]),pitch)
    objects.append(SceneObject('phase-points','point_markers',dict(
        x=points[:,0],y=points[:,1],z=points[:,2],color='#d99427',size=150)))
    objects.append(curve_object('axis',np.array([[0.,-.6,0.],[0.,11.8,0.]]),'#418d99',.009))
    a,t=np.meshgrid(np.linspace(0,2*np.pi,33),np.linspace(0,1,9))
    objects.append(SceneObject('axis-head','sampled_surface',dict(
        x=.065*(1-t)*np.cos(a),y=11.55+.25*t,z=.065*(1-t)*np.sin(a),color='#418d99')))
    return SceneSpec('torus-cycle','bosic-pitch',CAMERA,'light-manuscript',
        layout=FigureLayout(figsize=(13.5,3.7),dpi=180,xlim=(-2.,2.),
            ylim=(-1.,12.),zlim=(-2.,2.),show_axes=False),objects=objects,
        metadata={'pitch':pitch,'helix_radius':RADIUS,'bosic_phase_only':True,
            'glyph_scale':GLYPH_SCALE,'torus_opacity':.14,'same_cycle_duration':True})


def overlay(path,pitch,title):
    image=Image.open(path).convert('RGB');w,h=image.size;top=0;bottom=0
    plate=Image.new('RGB',(w,h+top+bottom),'white');plate.paste(image,(0,top))
    fig=plt.figure(figsize=(w/180,(h+top+bottom)/180),dpi=180)
    ax=fig.add_axes([0,0,1,1]);ax.imshow(plate);ax.axis('off')
    cam=CAMERA_PRESETS[CAMERA];az,el=np.deg2rad([cam.azimuth_deg,cam.elevation_deg])
    right=np.array([-np.sin(az),np.cos(az),0.])
    up=np.array([-np.cos(az)*np.sin(el),-np.sin(az)*np.sin(el),np.cos(el)])
    scale=h/(2*cam.orthographic_scale)
    def project(p):
        d=np.asarray(p)-np.array([0.,5.5,0.])
        return np.stack([w/2+(d@right)*scale,h/2-(d@up)*scale+top],axis=-1)
    for j,text in enumerate([r'$0$',r'$2\pi$',r'$4\pi$']):
        p=project([0.,j*pitch,RADIUS+.32])
        ax.text(*p,text,fontsize=19,ha='center',va='bottom',color='#48566a')
    k=project([0.,12.,0.]);ax.text(*k,r'$\hat{k}$',fontsize=22,color='#347d89',va='center')
    stations=project([[0.,j*pitch,-RADIUS-.40] for j in range(3)])
    d=stations[2]-stations[0];d/=np.linalg.norm(d);normal=np.array([-d[1],d[0]])
    ax.plot(stations[:,0],stations[:,1],color='#a36624',lw=1.6)
    for p in stations:
        ends=np.array([p-12*normal,p+12*normal]);ax.plot(ends[:,0],ends[:,1],color='#a36624',lw=1.6)
    for j in range(2):
        p=(stations[j]+stations[j+1])/2+48*normal
        text=title if j==0 else 'Per turn'
        ax.text(*p,text,ha='center',va='center',fontsize=20,color='#a36624',
            rotation=float(np.degrees(np.arctan2(-d[1],d[0]))),rotation_mode='anchor',
            bbox=dict(facecolor='white',edgecolor='none',pad=2))
    # Intrinsic pitch arc in the local tangent plane, then camera projection.
    phase=7*np.pi/4
    q=history(phase,pitch)
    circum=-np.array([-np.sin(phase),0.,-np.cos(phase)])
    axial=np.array([0.,-1.,0.])
    alpha=np.arctan2(pitch,2*np.pi*RADIUS)
    tangent=circum*np.cos(alpha)+axial*np.sin(alpha)
    for direction in (circum,tangent):
        ray=project(np.stack([q,q+.82*direction]))
        ax.plot(ray[:,0],ray[:,1],color='#374151',lw=1.7)
    angles=np.linspace(0,alpha,60)
    arc=project(q+.44*(np.cos(angles)[:,None]*circum+np.sin(angles)[:,None]*axial))
    ax.plot(arc[:,0],arc[:,1],color='#a36624',lw=2)
    label=project(q+.69*(np.cos(alpha/2)*circum+np.sin(alpha/2)*axial))
    ax.text(*label,r'$\alpha$',fontsize=23,color='#a36624',ha='center',va='center')
    assert np.isclose(np.dot(tangent,circum),np.cos(alpha))
    fig.savefig(path,dpi=180,facecolor='white');plt.close(fig)


def main():
    reports=[];frames=[]
    phi=np.linspace(0,4*np.pi,2001)
    for j,(pitch,title) in enumerate(zip(PITCHES,['Less advance','More advance'])):
        points=history(phi,pitch)
        radius=np.linalg.norm(points[:,[0,2]],axis=1)
        assert np.allclose(radius,RADIUS)
        outer=GLYPH_SCALE*xyz(phi,np.zeros_like(phi))
        outer[:,1]+=points[:,1]
        assert np.allclose(points,outer)
        assert np.isclose(RADIUS,GLYPH_SCALE*RB+GLYPH_SCALE*RF)
        assert np.allclose(points[:,1],pitch*phi/(2*np.pi))
        assert np.allclose(history(phi+2*np.pi,pitch)-points,[0.,pitch,0.])
        assert np.allclose(history(phi+4*np.pi,pitch)-points,[0.,2*pitch,0.])
        output=ROOT/f'validation/pitch-panel-{j}.png'
        render_scene_with_backend('pyvista3d',scene=scene(pitch),output_path=output,
                                  camera_name=CAMERA,style_name='light-manuscript')
        overlay(output,pitch,title);frames.append(Image.open(output).convert('RGB'))
        reports.append({'pitch':pitch,'radius_min':float(radius.min()),'radius_max':float(radius.max()),
                        'one_turn_advance_verified':True,'pitch_angle_degrees':float(np.degrees(np.arctan2(pitch,2*np.pi*RADIUS))),'arc_projected_from_local_tangent_plane':True})
    assert frames[0].size==frames[1].size
    w,h=frames[0].size
    plate=Image.new('RGB',(w,2*h),'white')
    for j,frame in enumerate(frames):plate.paste(frame,(0,j*h))
    plate.save(ROOT/'assets/translation-pitch.png')
    (ROOT/'validation/mesh-pitch.json').write_text(json.dumps([mesh_record('assets/translation-pitch.png',3*len(frames))],indent=2)+'\n')
    checks={'panels':reports,'same_camera_and_axial_scale':True,'same_radius':True,
        'radius_matches_torus_outer_rim':True,
        'no_fermic_phase_input':True,'glyph_scale':GLYPH_SCALE,'torus_opacity':.14,
        'backend':'existing geometry3d/pyvista3d','new_dependencies':[]}
    (ROOT/'validation/pitch-checks.json').write_text(json.dumps(checks,indent=2)+'\n')
    print(json.dumps(checks,indent=2))

if __name__=='__main__':main()
