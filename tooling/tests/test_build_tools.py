"""Regressions for Quarto path semantics and non-destructive build maintenance."""
from pathlib import Path
import subprocess
import sys
from types import SimpleNamespace

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import check_crossrefs as refs
import build_manuscript_status as status
import sync_ci_image as images
import validate
import check_figure_reproducibility as figures


def put(root, name, text=""):
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    return path


def test_quarto_root_and_local_paths_are_not_host_absolute(tmp_path, monkeypatch):
    monkeypatch.setattr(refs, "ROOT", tmp_path)
    source = put(tmp_path, "chapters/section.qmd")
    image = put(tmp_path, "figures/a figure.png")
    assert refs.resolve_relative('/figures/a%20figure.png?raw=1#view', source) == image
    assert refs.resolve_relative('../figures/a%20figure.png', source) == image
    assert refs.resolve_relative('<../figures/a figure.png> "title"', source) == image
    for external in ('https://example.org/a', '//example.org/a', 'data:image/png;base64,AA', '#sec-local'):
        assert refs.resolve_relative(external, source) is None


def test_bad_include_reports_error_without_root_fallback_or_crash(tmp_path, monkeypatch):
    monkeypatch.setattr(refs, "ROOT", tmp_path)
    source = put(tmp_path, "chapter/index.qmd", '{{< include absent.qmd >}}\n{{< include ../../escape.qmd >}}')
    put(tmp_path, "absent.qmd", 'Wrong directory must not hide a bad include')
    files, errors = refs.collect_qmd_tree([source])
    assert tmp_path / 'absent.qmd' not in files
    assert any('missing' in e and 'chapter/absent.qmd' in e for e in errors)
    assert any('escapes project root' in e for e in errors)
    assert refs.check_refs(files) == []


def test_literal_examples_do_not_create_dependencies(tmp_path, monkeypatch):
    monkeypatch.setattr(refs, "ROOT", tmp_path)
    source = put(tmp_path, 'index.qmd', '''# Book
<!-- ![draft](missing.png) {{< include draft.qmd >}} -->
```markdown
{{< include example.qmd >}}
@eq-example
```
$$ x=1 $$ {#eq-real}
See @eq-real.
''')
    files, errors = refs.collect_qmd_tree([source])
    assert files == {source}
    assert not errors + refs.check_assets(files) + refs.check_refs(files)


def test_missing_and_unrendered_links_and_duplicate_ids_are_detected(tmp_path, monkeypatch):
    monkeypatch.setattr(refs, "ROOT", tmp_path)
    source = put(tmp_path, 'index.qmd', '''# Book {#sec-same}
[missing](/absent.qmd)
[unadopted](/_candidates/draft.qmd)
[bad anchor](/appendix.qmd#sec-wrong)
''')
    appendix = put(tmp_path, 'appendix.qmd', '# Appendix {#sec-same}')
    put(tmp_path, '_candidates/draft.qmd')
    files = {source, appendix}
    errors = refs.check_links(files)
    assert any('missing/outside-project' in e for e in errors)
    assert any('not in the book' in e for e in errors)
    assert any('missing explicit link anchor' in e for e in errors)
    assert any('duplicate explicit ID' in e for e in refs.check_refs(files))


def test_book_order_does_not_promote_unlisted_qmds(tmp_path, monkeypatch):
    monkeypatch.setattr(refs, 'ROOT', tmp_path)
    put(tmp_path, '_candidates/unadopted.qmd')
    config = {'book': {'chapters': ['index.qmd', {'part': 'part.qmd', 'chapters': ['ch.qmd']}],
                       'references': 'references.qmd', 'appendices': ['app.qmd']}}
    assert refs.declared_files(config) == [tmp_path/p for p in
        ['index.qmd', 'part.qmd', 'ch.qmd', 'references.qmd', 'app.qmd']]


def test_wrapper_link_anchors_expand_only_the_targets_nested_includes(tmp_path, monkeypatch):
    monkeypatch.setattr(refs, 'ROOT', tmp_path)
    source = put(tmp_path, 'appendix.qmd', '[valid](/chapter/index.qmd#sec-deep)\n'
                 '[wrong page](/chapter/index.qmd#sec-unrelated)')
    wrapper = put(tmp_path, 'chapter/index.qmd', '{{< include section.qmd >}}')
    put(tmp_path, 'chapter/section.qmd', '{{< include nested/deep.qmd >}}')
    put(tmp_path, 'chapter/nested/deep.qmd', '# Deep {#sec-deep}')
    other = put(tmp_path, 'other.qmd', '# Unrelated {#sec-unrelated}')
    files, errors = refs.collect_qmd_tree([source, wrapper, other])
    assert not errors
    assert refs.check_links(files) == [
        'missing explicit link anchor in appendix.qmd: /chapter/index.qmd#sec-unrelated']


def test_anchor_include_closure_is_bounded_and_reports_missing_inputs(tmp_path, monkeypatch):
    monkeypatch.setattr(refs, 'ROOT', tmp_path)
    source = put(tmp_path, 'index.qmd', '[link](wrapper.qmd#sec-child)')
    wrapper = put(tmp_path, 'wrapper.qmd', '{{< include child.qmd >}}')
    child = put(tmp_path, 'child.qmd', '# Child {#sec-child}\n'
                '{{< include wrapper.qmd >}}\n{{< include missing.qmd >}}')
    errors = refs.check_links({source, wrapper, child})
    assert errors == ['missing declared/include file: missing.qmd']


def test_sidebar_cannot_link_an_unrendered_document(tmp_path, monkeypatch):
    monkeypatch.setattr(refs, 'ROOT', tmp_path)
    config = put(tmp_path, '_quarto.yml', 'book:\n  chapters: [index.qmd]\n')
    monkeypatch.setattr(refs, 'QUARTO', config)
    put(tmp_path, '_quarto-html.yml', 'book:\n  sidebar:\n    contents:\n    - href: orphan.qmd\n')
    source = put(tmp_path, 'index.qmd')
    put(tmp_path, 'orphan.qmd')
    assert refs.check_sidebar({source})


def test_status_check_reports_drift_without_overwriting(tmp_path, monkeypatch):
    ledger = put(tmp_path, 'ledger.yml', 'chapters: []\n')
    output = put(tmp_path, 'table.md', 'valuable existing bytes\n')
    monkeypatch.setattr(status, 'LEDGER', ledger)
    monkeypatch.setattr(status, 'OUTPUT', output)
    monkeypatch.setattr(sys, 'argv', ['build_manuscript_status.py', '--check'])
    assert status.main() == 1
    assert output.read_text() == 'valuable existing bytes\n'


def image_fixture(root):
    old = 'ghcr.io/ada-mercer/momentum-first-build@sha256:' + 'a'*64
    put(root, str(images.REFERENCE), old+'\n')
    for name in images.WORKFLOWS:
        put(root, '.github/workflows/'+name, 'container:\n  image: '+old+'\n# Keep this comment\n')
    return old


def test_image_update_validates_all_consumers_before_writing(tmp_path):
    old = image_fixture(tmp_path)
    before = (tmp_path / '.github/workflows' / images.WORKFLOWS[0]).read_bytes()
    put(tmp_path, '.github/workflows/'+images.WORKFLOWS[-1], 'image: unexpected\n')
    new = 'ghcr.io/ada-mercer/momentum-first-build@sha256:' + 'b'*64
    with pytest.raises(ValueError, match='unexpected'):
        images.synchronize(tmp_path, new)
    assert (tmp_path / images.REFERENCE).read_text().strip() == old
    assert (tmp_path / '.github/workflows' / images.WORKFLOWS[0]).read_bytes() == before


def test_image_update_preserves_other_workflow_content_and_rejects_tags(tmp_path):
    image_fixture(tmp_path)
    with pytest.raises(ValueError, match='pinned'):
        images.synchronize(tmp_path, 'ghcr.io/ada-mercer/momentum-first-build:latest')
    new = 'ghcr.io/ada-mercer/momentum-first-build@sha256:' + 'b'*64
    assert len(images.synchronize(tmp_path, new)) == 4
    assert images.synchronize(tmp_path) == []
    for name in images.WORKFLOWS:
        assert (tmp_path / '.github/workflows' / name).read_text().endswith('# Keep this comment\n')


def test_publication_never_builds_figures_after_failed_source_checks(monkeypatch):
    called=[]
    def run(*args):
        called.append(args)
        return int(args[0] == 'tooling/scripts/check_crossrefs.py')
    monkeypatch.setattr(validate, 'run_python', run)
    monkeypatch.setattr(sys, 'argv', ['validate.py', '--publication'])
    assert validate.main() == 1
    assert len(called) == 4
    assert all('build_figures.py' not in arg for args in called for arg in args)


def test_publication_preserves_dirty_figure_outputs(monkeypatch):
    called = []
    monkeypatch.setattr(validate, 'run_python', lambda *args: called.append(args) or 0)
    monkeypatch.setattr(validate.subprocess, 'run', lambda *a, **kw:
        SimpleNamespace(returncode=0, stdout=' M figures/build/valuable.png\n'))
    monkeypatch.setattr(sys, 'argv', ['validate.py', '--publication'])
    assert validate.main() == 1
    assert len(called) == 4


def test_geometry_metadata_and_routing_do_not_load_numpy():
    library = Path(__file__).resolve().parents[2] / 'figures/lib'
    code = '''
import importlib.abc
import sys
class NoNumpy(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname == 'numpy' or fullname.startswith('numpy.'):
            raise ImportError('Lightweight geometry routing must not import NumPy')
sys.meta_path.insert(0, NoNumpy())
sys.path.insert(0, sys.argv[1])
from geometry3d import SceneSpec, OutputTarget, render_scene
from geometry3d.exporters import build_output_path
from pathlib import Path
assert build_output_path(Path('build'), 'example', OutputTarget('x', 'canonical_png', 'x')).name == 'x.png'
assert 'numpy' not in sys.modules
'''
    result = subprocess.run([sys.executable, '-c', code, str(library)], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr


def test_figure_drift_catches_deleted_and_untracked_outputs(tmp_path, monkeypatch):
    monkeypatch.setattr(figures, 'ROOT', tmp_path)
    def git(*args):
        return subprocess.run(['git', *args], cwd=tmp_path, check=True, capture_output=True)
    git('init', '-q')
    put(tmp_path, '.gitignore', 'figures/build/**/*.svg\n')
    output = put(tmp_path, 'figures/build/example/registered.png', 'baseline')
    git('add', '.')
    git('-c', 'user.name=Test', '-c', 'user.email=test@localhost', 'commit', '-qm', 'baseline')
    output.unlink()
    put(tmp_path, 'figures/build/example/unexpected.png', 'new')
    put(tmp_path, 'figures/build/example/companion.svg', 'ignored companion')
    assert figures._changed_build_paths() == [
        'figures/build/example/registered.png', 'figures/build/example/unexpected.png']
    assert figures.main() == 1
