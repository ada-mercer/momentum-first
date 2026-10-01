"""A literal crop of the same opaque torus; momentum triangle is an overlay.
Shared geometry3d/PyVista backend, same 48x24 grid, no new dependencies.
The frequency relation is inherited from Foundations, not torus arclength.
"""
from pathlib import Path
import sys,json
import numpy as np
from PIL import Image
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.patches import Rectangle,ConnectionPatch
import render_geometry_momentum as old
from mode_geometry import curve_object
from torus_mesh import parameter_lines
from geometry3d.scene_spec import SceneSpec,SceneObject,FigureLayout
from geometry3d.cameras import CAMERA_PRESETS,CameraPreset
from geometry3d.backends import render_scene_with_backend

R=Path(__file__).resolve().parents[1]
RB,RF=old.RB,old.RF
AZ,EL,SCALE=135.,20.,2.25
W,H=2000,1500
U_START=np.deg2rad(AZ)
V_START=0.
ZOOM=1.5
N_B,N_F=1,5
# One illustrative momentum state, chosen to match the local tangent at Q.
P_DRAW=(RB+RF)*N_B
PF_DRAW=RF*N_F
M_DRAW=np.hypot(P_DRAW,PF_DRAW)
THETA=np.arctan2(P_DRAW,PF_DRAW)
BLUE,AMBER,INK,PHASE=old.BLUE,old.AMBER,old.INK,old.PHASE


def xyz(u,v,lift=0.):
    rr=RF+lift
    return np.stack([(RB+rr*np.cos(v))*np.cos(u),
                     (RB+rr*np.cos(v))*np.sin(u),rr*np.sin(v)],axis=-1)


def project(point):
    az,el=np.deg2rad([AZ,EL])
    right=np.array([-np.sin(az),np.cos(az),0.])
    up=np.array([-np.cos(az)*np.sin(el),-np.sin(az)*np.sin(el),np.cos(el)])
    return np.array([W/2+np.dot(point,right)*H/(2*SCALE),
                     H/2-np.dot(point,up)*H/(2*SCALE)])


def render_surface():
    u,v=np.meshgrid(np.linspace(0,2*np.pi,321),np.linspace(0,2*np.pi,161))
    mesh=xyz(u,v)
    objects=[SceneObject('opaque-torus','sampled_surface',dict(
        x=mesh[...,0],y=mesh[...,1],z=mesh[...,2],color='#c7b7d6',alpha=1.,shade=True,ambient=.48))]
    for axis,j,uu,vv in parameter_lines():
        objects.append(curve_object(f'grid-{axis}-{j}',xyz(uu,vv,.007),'#8c779d',.005,1.))
    s=np.linspace(0,1,6001)
    objects.append(curve_object('five-fermic-loop',xyz(U_START+2*np.pi*N_B*s,V_START+2*np.pi*N_F*s),INK,.018))
    s=np.linspace(0.,.021,201)
    objects.append(curve_object('selected-loop',xyz(U_START+2*np.pi*N_B*s,V_START+2*np.pi*N_F*s),AMBER,.024))
    CAMERA_PRESETS['candidate-opaque-closeup']=CameraPreset('candidate-opaque-closeup',AZ,EL,
        projection_mode='orthographic',orthographic_scale=SCALE)
    scene=SceneSpec('torus-cycle','opaque-closeup','candidate-opaque-closeup','light-manuscript',
        layout=FigureLayout(figsize=(8,6),dpi=250,xlim=(-3,3),ylim=(-3,3),zlim=(-3,3),show_axes=False),
        objects=objects,annotations=[],metadata={'opaque':True,'mesh':[48,24]})
    out=R/'validation/opaque-torus-full.png'
    render_scene_with_backend('pyvista3d',scene=scene,output_path=out,
        camera_name='candidate-opaque-closeup',style_name='light-manuscript')
    image=Image.open(out).convert('RGB')
    assert image.size==(W,H),image.size
    return image


def triangle(ax,q,length,labelsize,linewidth):
    # Components in the actual tangent plane, projected through the same camera.
    x,y=q;dx=length;foreshorten=np.cos(np.deg2rad(EL))
    dy=length*(PF_DRAW/P_DRAW)*foreshorten
    halo=[pe.Stroke(linewidth=linewidth+2.0,foreground='white',alpha=.9),pe.Normal()]
    for start,end,col in [((x,y),(x,y-dy),AMBER),((x,y-dy),(x+dx,y-dy),BLUE),((x,y),(x+dx,y-dy),INK)]:
        art=ax.annotate('',xy=end,xytext=start,arrowprops=dict(arrowstyle='-|>',lw=linewidth,color=col,
                       mutation_scale=labelsize+2,shrinkA=0,shrinkB=0))
        art.arrow_patch.set_path_effects(halo)
    # theta directly between p_f and M, at their shared origin Q.
    angle=np.linspace(0,THETA,65);radius=dx*.34
    ax.plot(x+radius*np.sin(angle),y-radius*np.cos(angle)*foreshorten,
            color=INK,lw=1.2,path_effects=[pe.Stroke(linewidth=3,foreground='white'),pe.Normal()])
    t=ax.text(x+radius*1.65*np.sin(THETA/2),
              y-radius*1.65*np.cos(THETA/2)*foreshorten,r'$\theta$',
              ha='center',va='center',fontsize=labelsize,color=INK,zorder=10)
    t.set_path_effects([pe.Stroke(linewidth=3,foreground='white'),pe.Normal()])
    d=dx*.11
    ax.plot([x,x+d,x+d],[y-dy+d*foreshorten,y-dy+d*foreshorten,y-dy],
            color=INK,lw=.8,path_effects=[pe.Stroke(linewidth=2,foreground='white'),pe.Normal()])
    ax.scatter(x,y,color=AMBER,s=18,zorder=9,edgecolor='white',linewidth=.5)
    for px,py,text,col in [(x-30,y+28,'Q',AMBER),(x+dx/2,y-dy-32,r'$p$',BLUE),
                           (x-35,y-dy/2,r'$p_f$',AMBER),(x+dx*.60+26,y-dy*.48,r'$M$',INK)]:
        t=ax.text(px,py,text,ha='center',va='center',fontsize=labelsize,color=col,zorder=10)
        t.set_path_effects([pe.Stroke(linewidth=3,foreground='white',alpha=.95),pe.Normal()])


def main():
    image=render_surface()
    q=project(xyz(U_START,V_START))
    assert np.isclose(q[0],W/2)
    assert np.isclose(np.hypot(*xyz(U_START,V_START)[:2]),RB+RF)
    assert np.allclose(xyz(U_START,V_START),xyz(U_START+2*np.pi*N_B,V_START+2*np.pi*N_F))
    e_b=np.array([-np.sin(U_START),np.cos(U_START),0.])
    e_f=np.array([0.,0.,1.])
    tangent=P_DRAW*e_b+PF_DRAW*e_f
    h=1.e-7
    numerical=(xyz(U_START+2*np.pi*N_B*h,2*np.pi*N_F*h)-
               xyz(U_START-2*np.pi*N_B*h,-2*np.pi*N_F*h))/(2*h)/(2*np.pi)
    assert np.allclose(tangent,numerical,rtol=1.e-7,atol=1.e-7)
    projected=project(xyz(U_START,V_START)+tangent)-project(xyz(U_START,V_START))
    assert np.isclose(-projected[1]/projected[0],(PF_DRAW/P_DRAW)*np.cos(np.deg2rad(EL)))
    assert np.isclose(np.dot(tangent,e_f)/np.linalg.norm(tangent),np.cos(THETA))
    assert np.isclose(np.cos(THETA),PF_DRAW/M_DRAW)
    # Same camera, same image, same aspect ratio: no flattening or stretching.
    side=950/ZOOM
    left=float(np.clip(q[0]-side*.50,0,W-side))
    top=float(np.clip(q[1]-side*.60,0,H-side))
    box=(left,top,left+side,top+side)
    crop=image.transform((950,950),Image.Transform.EXTENT,box,resample=Image.Resampling.BICUBIC)
    crop.save(R/'validation/opaque-torus-crop.png')
    assert np.isclose(950/(box[2]-box[0]),ZOOM)
    assert np.isclose(950/(box[3]-box[1]),ZOOM)
    fig=plt.figure(figsize=(11.8,4.9))
    a=fig.add_axes([.025,.18,.47,3.57/4.9]);a.imshow(image);a.axis('off')
    a.set_title('A section of the loop',fontsize=15,fontweight='bold',pad=14)
    a.add_patch(Rectangle((left,top),side,side,fill=False,edgecolor=AMBER,lw=.9,ls=':'))
    triangle(a,q,210,11,1.4)
    b=fig.add_axes([.54,.18,.42,3.57/4.9]);b.imshow(crop,extent=(0,side,side,0));b.axis('off')
    b.set_title('The same geometry, enlarged',fontsize=15,fontweight='bold',pad=14)
    triangle(b,q-np.array([left,top]),210,16,2.2)
    fig.add_artist(ConnectionPatch(xyA=(left+side,top+side*.72),coordsA=a.transData,
        xyB=(0,side*.72),coordsB=b.transData,color=AMBER,lw=1.,ls=':',alpha=.7))
    fig.text(.29,.067,r'$M^2=p^2+p_f^2$',ha='center',fontsize=17,color=INK)
    fig.text(.75,.112,'Fermic cycling',ha='center',fontsize=12,color=AMBER)
    fig.text(.75,.039,r'$f=f_0\,p_f/M=f_0\cos\theta$',ha='center',fontsize=17,color=AMBER)
    (R/'validation/projection-checks.json').write_text(json.dumps(dict(
        theta_measured_from_fermic_direction=True,
        selected_p=P_DRAW,selected_p_f=PF_DRAW,selected_M=float(M_DRAW),
        theta_radians=float(THETA),tangent_alignment_verified=True,
        common_tangent_plane_scale=True,perspective_foreshortening_retained=True,
        lower_speed_panels_removed=True,shared_origin_pf_and_M=True,
        theta_at_origin=True,frequency_explanation_in_text=True,
        frequency_relation_in_figure=True,clock_law_inherited_from_foundations=True,
        manifold_picture_uses_fixed_speed='c',
        fermic_component='c*cos(theta)',bosic_component='c*sin(theta)',
        rate_fraction='cos(theta)=p_f/M',frequency_relation='f=f0*p_f/M=f0*cos(theta)',
        clock_frequency_inferred_from_drawn_arclength=False,
        microscopic_derivation_claimed=False,external_wave_strip_removed=True),indent=2)+'\n')
    fig.savefig(R/'assets/momentum-wave.png',dpi=220,bbox_inches='tight');plt.close(fig)
    (R/'validation/opaque-closeup-checks.json').write_text(json.dumps(dict(
        backend='existing geometry3d/pyvista3d',mesh=[48,24],opaque=True,
        full_image_pixels=[W,H],crop_box=box,q_pixels=q.tolist(),
        right_panel_zoom_relative_to_v11=ZOOM,overview_camera_unchanged=True,
        loop_start_azimuth_degrees=AZ,loop_start_fermic_phase=V_START,
        loop_start_front_centre=True,loop_start_outer_position=True,
        uniform_crop_resampling=True,
        literal_same_camera_crop=True,momentum_triangle_screen_overlay=False,
        momentum_triangle_projected_tangent=True,
        selected_bosic_turns=N_B,selected_fermic_turns=N_F,
        surface_metric_identified_with_momentum=False,
        internal_propagation_law_added=False,new_dependencies=[]),indent=2)+'\n')
    # The geometry displays directions; Foundations supplies the clock law.
    print('Opaque overview and literal close-up rendered:',box)

if __name__=='__main__':main()
