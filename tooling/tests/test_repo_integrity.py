from __future__ import annotations

import re
from datetime import date
from pathlib import Path
from urllib.parse import unquote

import yaml

ROOT = Path(__file__).resolve().parents[2]


def _load_quarto_config() -> dict:
    return yaml.safe_load((ROOT / "_quarto.yml").read_text(encoding="utf-8"))


def _walk_book_entries(entries: list[object]) -> list[str]:
    paths: list[str] = []
    for entry in entries:
        if isinstance(entry, str):
            paths.append(entry)
        elif isinstance(entry, dict):
            paths.extend(_walk_book_entries(entry.get("chapters", [])))
    return paths


def test_quarto_render_paths_exist() -> None:
    config = _load_quarto_config()
    render_paths = config["project"]["render"]
    missing = [path for path in render_paths if not (ROOT / path).exists()]
    assert not missing


def test_quarto_book_chapter_paths_exist() -> None:
    config = _load_quarto_config()
    chapter_paths = _walk_book_entries(config["book"]["chapters"])
    missing = [path for path in chapter_paths if not (ROOT / path).exists()]
    assert not missing


def test_default_quarto_render_pipeline_is_configured() -> None:
    config = _load_quarto_config()
    default_profile = config.get("profile", {}).get("default")
    assert default_profile == "pdf"
    assert (ROOT / f"_quarto-{default_profile}.yml").is_file()

    pre_render = config["project"].get("pre-render", [])
    assert pre_render == [".venv/bin/python tooling/scripts/build_manuscript_status.py"]
    required_paths = [".venv/bin/python", "tooling/scripts/build_manuscript_status.py"]
    missing = [path for path in required_paths if not (ROOT / path).is_file()]
    assert not missing


def test_quarto_downloads_match_supported_release_assets() -> None:
    config = _load_quarto_config()
    assert config["book"].get("downloads") == ["pdf"]


def test_pages_workflow_watches_root_book_homepage() -> None:
    workflow = yaml.load(
        (ROOT / ".github" / "workflows" / "deploy-book-site.yml").read_text(
            encoding="utf-8"
        ),
        Loader=yaml.BaseLoader,
    )
    watched_paths = workflow["on"]["push"]["paths"]
    assert "index.qmd" in watched_paths


def test_figure_registry_paths_and_ids_are_valid() -> None:
    registry = yaml.safe_load((ROOT / "figures" / "figures.yml").read_text(encoding="utf-8"))
    figures = registry.get("figures", [])
    assert figures

    seen_ids: set[str] = set()
    missing: list[str] = []
    for figure in figures:
        assert {"id", "source", "output", "chapter"} <= figure.keys()
        assert figure["id"] not in seen_ids
        seen_ids.add(figure["id"])
        assert str(figure["output"]).startswith("figures/build/")
        assert Path(str(figure["output"])).suffix in {".png", ".pdf", ".svg"}
        for key in ("source", "chapter"):
            if not (ROOT / figure[key]).exists():
                missing.append(f"{figure['id']}:{key}:{figure[key]}")
    assert not missing


def test_documentation_entrypoints_exist() -> None:
    entrypoints = [
        "README.md",
        "docs/README.md",
        "manuscript/README.md",
        "figures/README.md",
        "rendering/README.md",
        "tooling/README.md",
        ".github/README.md",
    ]
    missing = [path for path in entrypoints if not (ROOT / path).is_file()]
    assert not missing


def test_root_readme_routes_readers_and_contributors() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "https://ada-mercer.github.io/momentum-first/" in readme
    assert "releases/latest/download/Momentum-First.pdf" in readme
    assert "(docs/README.md)" in readme


def test_readme_internal_links_resolve() -> None:
    excluded_parts = {".git", ".local-review", ".pytest_cache", ".quarto", ".venv", "_book"}
    readmes = [
        path
        for path in ROOT.rglob("README.md")
        if excluded_parts.isdisjoint(path.relative_to(ROOT).parts)
    ]
    link_pattern = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
    broken: list[str] = []

    for readme in readmes:
        for raw_target in link_pattern.findall(readme.read_text(encoding="utf-8")):
            target = raw_target.strip().strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not target:
                continue
            resolved = (readme.parent / target).resolve()
            if not resolved.exists():
                broken.append(f"{readme.relative_to(ROOT)} -> {raw_target}")

    assert not broken


def test_citation_metadata_is_present_for_doi_workflow() -> None:
    citation = yaml.safe_load((ROOT / "CITATION.cff").read_text(encoding="utf-8"))
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    assert citation["cff-version"] == "1.2.0"
    assert citation["title"] == "Momentum First"
    # CITATION version must track VERSION (the release workflow enforces tag == VERSION).
    assert citation["version"] == version
    assert citation["authors"] == [{"family-names": "Klaveness", "given-names": "Arne"}]
    assert citation["repository-code"] == "https://github.com/ada-mercer/momentum-first"
    assert date.fromisoformat(str(citation["date-released"]))
    assert "AI-assisted" in citation["message"]
    assert (ROOT / "docs" / "doi" / "zenodo-v0.3.2.md").exists()
