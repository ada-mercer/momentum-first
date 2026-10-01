"""Regression checks for family-owned composites without a native 3D runtime."""
from pathlib import Path
from types import SimpleNamespace
import sys

import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'figures/lib'))
from geometry3d import runtime
from geometry3d.manifest import FamilyManifest, SceneManifest
from geometry3d.scene_spec import SceneSpec, OutputTarget


def setup_runtime(monkeypatch, tmp_path, composite, module):
    entry=SceneManifest('example','build_example')
    family=FamilyManifest('test-family','test','src','build','manuscript-3q',
        default_backend='pyvista3d',default_style='light-manuscript',scenes=(entry,))
    manifest=SimpleNamespace(build_root=tmp_path,get_family=lambda _:family)
    scene=SceneSpec('test-family','example','manuscript-3q','light-manuscript',
        outputs=[OutputTarget('canonical_png','canonical_png','example.png')],
        metadata={'composite':composite})
    monkeypatch.setattr(runtime,'load_manifest',lambda _:manifest)
    monkeypatch.setattr(runtime,'_build_scene',lambda *_:(scene,module,entry))
    return scene


@pytest.mark.parametrize('composite',[False,True])
def test_ordinary_and_composite_render_paths_stay_distinct(monkeypatch,tmp_path,composite):
    calls=[]
    def write(kind,**kwargs):
        calls.append((kind,kwargs))
        p=kwargs['output_path']; p.parent.mkdir(parents=True,exist_ok=True)
        p.write_bytes(kind.encode())
    module=SimpleNamespace(render_composite=lambda **kw:write('composite',**kw))
    setup_runtime(monkeypatch,tmp_path,composite,module)
    monkeypatch.setattr(runtime,'render_scene_with_backend',lambda backend,**kw:write('ordinary',backend_name=backend,**kw))
    path=runtime.render_scene('test.yml','test-family','example',backend_name='pyvista3d')
    expected='composite' if composite else 'ordinary'
    assert [name for name,_ in calls]==[expected]
    assert path.read_bytes()==expected.encode()
    assert calls[0][1]['camera_name']=='manuscript-3q'
    assert calls[0][1]['style_name']=='light-manuscript'
    assert calls[0][1]['backend_name']=='pyvista3d'


def test_missing_compositor_is_an_error_not_a_blank_canonical_render(monkeypatch,tmp_path):
    setup_runtime(monkeypatch,tmp_path,True,SimpleNamespace())
    monkeypatch.setattr(runtime,'render_scene_with_backend',lambda *a,**k:pytest.fail('Must not silently render a composite as an ordinary scene'))
    with pytest.raises(ValueError,match='without render_composite'):
        runtime.render_scene('test.yml','test-family','example')
    assert not list(tmp_path.rglob('*.png'))
