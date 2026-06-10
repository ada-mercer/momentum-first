from __future__ import annotations

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


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


def test_quarto_downloads_match_supported_release_assets() -> None:
    config = _load_quarto_config()
    assert config["book"].get("downloads") == ["pdf"]


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


def test_readme_reflects_current_release_posture() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "As of `v0.3.2`" in readme
    assert "will be added later" not in readme
    assert "https://ada-mercer.github.io/momentum-first/" in readme
    assert "releases/latest/download/Momentum-First.pdf" in readme
    assert "actions/workflows/deploy-book-site.yml" in readme
    assert "CITATION.cff" in readme
    assert "docs/doi/" in readme
    assert "--mode minimal" in readme


def test_citation_metadata_is_present_for_doi_workflow() -> None:
    citation = yaml.safe_load((ROOT / "CITATION.cff").read_text(encoding="utf-8"))
    assert citation["cff-version"] == "1.2.0"
    assert citation["title"] == "Momentum First"
    assert citation["version"] == "0.3.2"
    assert citation["authors"] == [{"family-names": "Klaveness", "given-names": "Arne"}]
    assert citation["repository-code"] == "https://github.com/ada-mercer/momentum-first"
    assert "AI-assisted" in citation["message"]
    assert (ROOT / "docs" / "doi" / "zenodo-v0.3.2.md").exists()
