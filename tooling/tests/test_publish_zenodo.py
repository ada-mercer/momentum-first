from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tooling" / "scripts" / "publish_zenodo.py"
SPEC = importlib.util.spec_from_file_location("publish_zenodo", SCRIPT)
assert SPEC and SPEC.loader
zenodo = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = zenodo
SPEC.loader.exec_module(zenodo)


def make_pdf(tmp_path: Path) -> zenodo.Artifact:
    path = tmp_path / zenodo.PDF_NAME
    path.write_bytes(b"%PDF-1.7\nsmall test artifact\n")
    return zenodo.inspect_pdf(path)


def public_record(
    artifact: zenodo.Artifact,
    *,
    version: str = "0.3.8",
    record_id: int = 102,
    concept_id: str = "101",
) -> dict:
    return {
        "id": record_id,
        "conceptrecid": concept_id,
        "doi": f"10.5281/zenodo.{record_id}",
        "conceptdoi": f"10.5281/zenodo.{concept_id}",
        "metadata": {"version": version},
        "files": [
            {
                "key": zenodo.PDF_NAME,
                "checksum": f"md5:{artifact.md5}",
            }
        ],
    }


class FakeClient:
    def __init__(self, depositions: list[dict], record: dict):
        self.depositions = depositions
        self.record = record
        self.calls: list[tuple] = []

    def list_family_depositions(self, concept_record_id: str) -> list[dict]:
        self.calls.append(("list", concept_record_id))
        return self.depositions

    def public_record(self, record_id: int) -> dict:
        self.calls.append(("public", record_id))
        return self.record

    def wait_for_public_record(self, record_id: int) -> dict:
        self.calls.append(("wait-public", record_id))
        return self.record

    def create_new_version(self, latest_id: int) -> dict:
        self.calls.append(("new-version", latest_id))
        return {
            "id": 103,
            "submitted": False,
            "metadata": {},
            "files": [{"id": "old-file"}],
        }

    def delete_file(self, draft_id: int, file_id: str) -> None:
        self.calls.append(("delete", draft_id, file_id))

    def update_metadata(self, draft_id: int, metadata: dict) -> dict:
        self.calls.append(("metadata", draft_id, metadata["version"]))
        return {"links": {"bucket": "https://zenodo.org/api/files/bucket"}}

    def upload_pdf(self, bucket_url: str, artifact: zenodo.Artifact) -> dict:
        self.calls.append(("upload", bucket_url, artifact.sha256))
        return {}

    def publish(self, draft_id: int) -> dict:
        self.calls.append(("publish", draft_id))
        return {"record_id": self.record["id"]}


def metadata(version: str = "0.3.8") -> dict:
    template = zenodo.load_metadata_template(zenodo.DEFAULT_METADATA)
    return zenodo.build_metadata(
        template,
        version=version,
        publication_date="2026-08-01",
        github_release_url=(
            f"https://github.com/ada-mercer/momentum-first/releases/tag/v{version}"
        ),
    )


def test_metadata_has_one_human_creator_and_exact_license() -> None:
    result = metadata()
    assert result["creators"] == [
        {
            "name": "Klaveness, Arne",
            "orcid": "0009-0004-1536-3055",
        }
    ]
    assert result["license"] == "cc-by-nc-sa-4.0"
    assert result["upload_type"] == "publication"
    assert result["publication_type"] == "book"
    assert result["related_identifiers"] == [
        {
            "identifier": "https://github.com/ada-mercer/momentum-first/releases/download/v0.3.8/Momentum-First.pdf",
            "relation": "isIdenticalTo",
            "resource_type": "publication-book",
        },
        {
            "identifier": "https://github.com/ada-mercer/momentum-first/releases/tag/v0.3.8",
            "relation": "isSupplementedBy",
            "resource_type": "software",
        },
        {
            "identifier": "10.5281/zenodo.21775704",
            "relation": "isSupplementedBy",
            "resource_type": "software",
        },
    ]


def test_bucket_upload_uses_octet_stream(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    artifact = make_pdf(tmp_path)
    client = zenodo.ZenodoClient(zenodo.SANDBOX_API, "test-token")
    captured: dict = {}

    def fake_request(method: str, path_or_url: str, **kwargs: object) -> dict:
        captured.update(method=method, path_or_url=path_or_url, **kwargs)
        return {}

    monkeypatch.setattr(client, "request", fake_request)
    client.upload_pdf("https://sandbox.zenodo.org/api/files/bucket", artifact)

    assert captured["method"] == "PUT"
    assert captured["content_type"] == "application/octet-stream"
    assert captured["data"] == artifact.path.read_bytes()


def test_existing_published_version_is_idempotent(tmp_path: Path) -> None:
    artifact = make_pdf(tmp_path)
    record = public_record(artifact)
    client = FakeClient(
        [
            {
                "id": record["id"],
                "record_id": record["id"],
                "submitted": True,
                "modified": "2026-08-01T00:00:00Z",
                "metadata": {"version": "0.3.8"},
            }
        ],
        record,
    )
    result = zenodo.publish_version(
        client,
        concept_record_id="101",
        artifact=artifact,
        metadata=metadata(),
    )
    assert result["status"] == "already-published"
    assert result["doi"] == "10.5281/zenodo.102"
    assert not any(call[0] in {"new-version", "upload", "publish"} for call in client.calls)


def test_bootstrap_draft_is_filled_and_published(tmp_path: Path) -> None:
    artifact = make_pdf(tmp_path)
    record = public_record(artifact)
    client = FakeClient(
        [
            {
                "id": 102,
                "submitted": False,
                "metadata": {},
                "files": [{"id": "placeholder"}],
            }
        ],
        record,
    )
    result = zenodo.publish_version(
        client,
        concept_record_id="101",
        artifact=artifact,
        metadata=metadata(),
    )
    assert result["status"] == "published"
    assert ("delete", 102, "placeholder") in client.calls
    assert ("metadata", 102, "0.3.8") in client.calls
    assert ("publish", 102) in client.calls
    assert not any(call[0] == "new-version" for call in client.calls)


def test_later_release_uses_new_version_action(tmp_path: Path) -> None:
    artifact = make_pdf(tmp_path)
    record = public_record(artifact, version="0.3.9", record_id=104)
    client = FakeClient(
        [
            {
                "id": 102,
                "record_id": 102,
                "submitted": True,
                "modified": "2026-08-01T00:00:00Z",
                "metadata": {"version": "0.3.8"},
            }
        ],
        record,
    )
    result = zenodo.publish_version(
        client,
        concept_record_id="101",
        artifact=artifact,
        metadata=metadata("0.3.9"),
    )
    assert result["status"] == "published"
    assert ("new-version", 102) in client.calls
    assert ("delete", 103, "old-file") in client.calls
    assert ("publish", 103) in client.calls


def test_non_increasing_version_is_rejected(tmp_path: Path) -> None:
    artifact = make_pdf(tmp_path)
    client = FakeClient(
        [
            {
                "id": 104,
                "record_id": 104,
                "submitted": True,
                "modified": "2026-08-02T00:00:00Z",
                "metadata": {"version": "0.3.9"},
            }
        ],
        public_record(artifact, version="0.3.9", record_id=104),
    )
    with pytest.raises(zenodo.ZenodoError, match="non-increasing"):
        zenodo.publish_version(
            client,
            concept_record_id="101",
            artifact=artifact,
            metadata=metadata("0.3.8"),
        )


def test_multiple_drafts_are_rejected() -> None:
    with pytest.raises(zenodo.ZenodoError, match="More than one"):
        zenodo.select_draft_and_latest(
            [
                {"id": 1, "submitted": False},
                {"id": 2, "submitted": False},
            ]
        )


def test_checksum_mismatch_is_rejected(tmp_path: Path) -> None:
    artifact = make_pdf(tmp_path)
    record = public_record(artifact)
    record["files"][0]["checksum"] = "md5:" + ("0" * 32)
    with pytest.raises(zenodo.ZenodoError, match="checksum differs"):
        zenodo.verify_record_artifact(record, artifact)


def test_client_refuses_non_zenodo_token_destination() -> None:
    with pytest.raises(zenodo.ZenodoError, match="official Zenodo"):
        zenodo.ZenodoClient("https://example.com/api", "secret-token")


def test_dry_run_needs_no_token_and_writes_plan(tmp_path: Path) -> None:
    artifact = make_pdf(tmp_path)
    output = tmp_path / "result.json"
    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "publish",
            "--pdf",
            str(artifact.path),
            "--version",
            "0.3.8",
            "--publication-date",
            "2026-08-01",
            "--github-release-url",
            "https://github.com/ada-mercer/momentum-first/releases/tag/v0.3.8",
            "--concept-record-id",
            "101",
            "--dry-run",
            "--output",
            str(output),
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        env={key: value for key, value in os.environ.items() if key != "ZENODO_TOKEN"},
    )
    assert result.returncode == 0, result.stderr
    planned = json.loads(output.read_text(encoding="utf-8"))
    assert planned["status"] == "dry-run"
    assert planned["sha256"] == artifact.sha256


def test_live_publish_requires_explicit_confirmation(tmp_path: Path) -> None:
    artifact = make_pdf(tmp_path)
    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "publish",
            "--pdf",
            str(artifact.path),
            "--version",
            "0.3.8",
            "--publication-date",
            "2026-08-01",
            "--github-release-url",
            "https://github.com/ada-mercer/momentum-first/releases/tag/v0.3.8",
            "--concept-record-id",
            "101",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        env={key: value for key, value in os.environ.items() if key != "ZENODO_TOKEN"},
    )
    assert result.returncode == 2
    assert "--confirm-publication" in result.stderr
