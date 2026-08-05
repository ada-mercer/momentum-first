#!/usr/bin/env python3
"""Create and update the canonical Zenodo manuscript DOI family.

The script deliberately never creates a DOI family during ``publish``. A human
must first run ``bootstrap`` and configure the returned concept record ID. This
keeps a rerun or a configuration mistake from creating a competing family.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlparse
from urllib.request import Request, urlopen


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_METADATA = REPO_ROOT / "docs" / "doi" / "zenodo-manuscript.json"
PRODUCTION_API = "https://zenodo.org/api"
SANDBOX_API = "https://sandbox.zenodo.org/api"
ALLOWED_API_URLS = {PRODUCTION_API, SANDBOX_API}
PDF_NAME = "Momentum-First.pdf"
SOURCE_CONCEPT_DOI = "10.5281/zenodo.21775704"
VERSION_RE = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")


class ZenodoError(RuntimeError):
    """A safe, user-facing Zenodo workflow failure."""


@dataclass(frozen=True)
class Artifact:
    path: Path
    size: int
    md5: str
    sha256: str


def file_digest(path: Path, algorithm: str) -> str:
    digest = hashlib.new(algorithm)
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def inspect_pdf(path: Path) -> Artifact:
    resolved = path.resolve()
    if not resolved.is_file():
        raise ZenodoError(f"PDF does not exist: {path}")
    if resolved.name != PDF_NAME:
        raise ZenodoError(f"PDF must use the release filename {PDF_NAME}")
    if resolved.stat().st_size == 0:
        raise ZenodoError("PDF is empty")
    with resolved.open("rb") as handle:
        if handle.read(5) != b"%PDF-":
            raise ZenodoError("Artifact does not start with a PDF signature")
    return Artifact(
        path=resolved,
        size=resolved.stat().st_size,
        md5=file_digest(resolved, "md5"),
        sha256=file_digest(resolved, "sha256"),
    )


def load_metadata_template(path: Path) -> dict[str, Any]:
    try:
        metadata = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ZenodoError(f"Cannot load metadata template {path}: {exc}") from exc

    expected_creator = [
        {
            "name": "Klaveness, Arne",
            "orcid": "0009-0004-1536-3055",
        }
    ]
    required = {
        "title": "Momentum First",
        "upload_type": "publication",
        "publication_type": "book",
        "creators": expected_creator,
        "access_right": "open",
        "license": "cc-by-nc-sa-4.0",
    }
    for key, expected in required.items():
        if metadata.get(key) != expected:
            raise ZenodoError(
                f"Metadata field {key!r} must equal {expected!r}; "
                f"found {metadata.get(key)!r}"
            )
    if not metadata.get("description") or not metadata.get("notes"):
        raise ZenodoError("Metadata description and acknowledgement notes are required")
    return metadata


def validate_version(value: str) -> str:
    if not VERSION_RE.fullmatch(value):
        raise ZenodoError("Version must be a formal X.Y.Z release without a v prefix")
    return value


def validate_publication_date(value: str) -> str:
    try:
        date.fromisoformat(value)
    except ValueError as exc:
        raise ZenodoError("Publication date must use YYYY-MM-DD") from exc
    return value


def validate_release_url(value: str, version: str) -> str:
    parsed = urlparse(value)
    if parsed.scheme != "https" or parsed.netloc != "github.com":
        raise ZenodoError("GitHub release URL must be an https://github.com URL")
    expected_suffix = f"/releases/tag/v{version}"
    if not parsed.path.endswith(expected_suffix):
        raise ZenodoError(
            f"GitHub release URL must end with {expected_suffix}"
        )
    return value.rstrip("/")


def build_metadata(
    template: dict[str, Any],
    *,
    version: str,
    publication_date: str,
    github_release_url: str,
) -> dict[str, Any]:
    metadata = dict(template)
    metadata["version"] = validate_version(version)
    metadata["publication_date"] = validate_publication_date(publication_date)
    release_url = validate_release_url(github_release_url, version)
    metadata["related_identifiers"] = [
        {
            "identifier": f"{release_url.rsplit('/tag/', 1)[0]}/download/v{version}/{PDF_NAME}",
            "relation": "isIdenticalTo",
            "resource_type": "publication-book",
        },
        {
            "identifier": release_url,
            "relation": "isSupplementedBy",
            "resource_type": "software",
        },
        {
            "identifier": SOURCE_CONCEPT_DOI,
            "relation": "isSupplementedBy",
            "resource_type": "software",
        },
    ]
    return metadata


def normalize_checksum(value: str) -> str:
    return value.split(":", 1)[-1].lower()


def version_tuple(value: str) -> tuple[int, int, int] | None:
    if not VERSION_RE.fullmatch(value):
        return None
    return tuple(int(part) for part in value.split("."))  # type: ignore[return-value]


class ZenodoClient:
    def __init__(self, api_url: str, token: str):
        api_url = api_url.rstrip("/")
        if api_url not in ALLOWED_API_URLS:
            raise ZenodoError(
                "API URL must be the official Zenodo production or sandbox endpoint"
            )
        if not token:
            raise ZenodoError("ZENODO_TOKEN is required")
        self.api_url = api_url
        self.token = token
        self.allowed_host = urlparse(api_url).netloc

    def _url(self, path_or_url: str, query: dict[str, str] | None = None) -> str:
        if path_or_url.startswith("https://"):
            url = path_or_url
        else:
            url = f"{self.api_url}/{path_or_url.lstrip('/')}"
        parsed = urlparse(url)
        if parsed.scheme != "https" or parsed.netloc != self.allowed_host:
            raise ZenodoError("Refusing to send a Zenodo token to another host")
        if query:
            url = f"{url}?{urlencode(query)}"
        return url

    def request(
        self,
        method: str,
        path_or_url: str,
        *,
        payload: Any | None = None,
        data: bytes | None = None,
        content_type: str | None = None,
        query: dict[str, str] | None = None,
    ) -> Any:
        if payload is not None and data is not None:
            raise ZenodoError("Internal error: request cannot use payload and data")
        headers = {
            "Authorization": f"Bearer {self.token}",
            "User-Agent": "momentum-first-doi-workflow/1",
            "Accept": "application/json",
        }
        body = data
        if payload is not None:
            body = json.dumps(payload).encode("utf-8")
            headers["Content-Type"] = "application/json"
        elif content_type:
            headers["Content-Type"] = content_type
        request = Request(
            self._url(path_or_url, query),
            data=body,
            headers=headers,
            method=method,
        )
        try:
            with urlopen(request, timeout=120) as response:
                raw = response.read()
        except HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")[:2000]
            raise ZenodoError(
                f"Zenodo API {method} failed with HTTP {exc.code}: {detail}"
            ) from exc
        except URLError as exc:
            raise ZenodoError(f"Zenodo API {method} failed: {exc.reason}") from exc
        if not raw:
            return None
        try:
            return json.loads(raw)
        except json.JSONDecodeError as exc:
            raise ZenodoError("Zenodo returned a non-JSON response") from exc

    def create_empty_draft(self) -> dict[str, Any]:
        return self.request("POST", "deposit/depositions", payload={})

    def list_family_depositions(self, concept_record_id: str) -> list[dict[str, Any]]:
        result = self.request(
            "GET",
            "deposit/depositions",
            query={
                "q": f"conceptrecid:{concept_record_id}",
                "sort": "mostrecent",
                "size": "100",
            },
        )
        if not isinstance(result, list):
            raise ZenodoError("Zenodo returned an unexpected deposition list")
        return result

    def get(self, url: str) -> dict[str, Any]:
        result = self.request("GET", url)
        if not isinstance(result, dict):
            raise ZenodoError("Zenodo returned an unexpected record")
        return result

    def create_new_version(self, latest_id: int) -> dict[str, Any]:
        original = self.request(
            "POST", f"deposit/depositions/{latest_id}/actions/newversion"
        )
        latest_draft = original.get("links", {}).get("latest_draft")
        if not latest_draft:
            raise ZenodoError("Zenodo did not return the new-version draft link")
        return self.get(latest_draft)

    def delete_file(self, draft_id: int, file_id: str) -> None:
        self.request("DELETE", f"deposit/depositions/{draft_id}/files/{file_id}")

    def update_metadata(self, draft_id: int, metadata: dict[str, Any]) -> dict[str, Any]:
        return self.request(
            "PUT",
            f"deposit/depositions/{draft_id}",
            payload={"metadata": metadata},
        )

    def upload_pdf(self, bucket_url: str, artifact: Artifact) -> dict[str, Any]:
        return self.request(
            "PUT",
            f"{bucket_url.rstrip('/')}/{PDF_NAME}",
            data=artifact.path.read_bytes(),
            # Zenodo's bucket API accepts raw bytes only and rejects media-type
            # specific headers with HTTP 415.
            content_type="application/octet-stream",
        )

    def publish(self, draft_id: int) -> dict[str, Any]:
        return self.request(
            "POST", f"deposit/depositions/{draft_id}/actions/publish"
        )

    def public_record(self, record_id: int) -> dict[str, Any]:
        return self.get(f"records/{record_id}")

    def wait_for_public_record(
        self, record_id: int, *, attempts: int = 10, delay_seconds: int = 3
    ) -> dict[str, Any]:
        last_error: ZenodoError | None = None
        for attempt in range(attempts):
            try:
                return self.public_record(record_id)
            except ZenodoError as exc:
                last_error = exc
                if attempt + 1 < attempts:
                    time.sleep(delay_seconds)
        raise ZenodoError(
            f"Published record {record_id} was not readable after {attempts} attempts: "
            f"{last_error}"
        )


def select_draft_and_latest(
    depositions: list[dict[str, Any]],
) -> tuple[dict[str, Any] | None, dict[str, Any] | None]:
    drafts = [item for item in depositions if not item.get("submitted", False)]
    published = [item for item in depositions if item.get("submitted", False)]
    if len(drafts) > 1:
        raise ZenodoError("More than one unpublished draft exists in the DOI family")
    published.sort(key=lambda item: str(item.get("modified", "")), reverse=True)
    return (drafts[0] if drafts else None, published[0] if published else None)


def verify_record_artifact(record: dict[str, Any], artifact: Artifact) -> None:
    files = [item for item in record.get("files", []) if item.get("key") == PDF_NAME]
    if not files:
        files = [
            item
            for item in record.get("files", [])
            if item.get("filename") == PDF_NAME
        ]
    if len(files) != 1:
        raise ZenodoError("Published record does not contain exactly one release PDF")
    checksum = files[0].get("checksum", "")
    if normalize_checksum(str(checksum)) != artifact.md5:
        raise ZenodoError("Published Zenodo PDF checksum differs from the release PDF")


def result_from_record(
    record: dict[str, Any], artifact: Artifact, status: str
) -> dict[str, Any]:
    concept_record_id = str(record.get("conceptrecid", ""))
    record_id = int(record.get("id") or record.get("record_id"))
    doi = record.get("doi") or record.get("metadata", {}).get("doi")
    concept_doi = record.get("conceptdoi")
    if not doi:
        raise ZenodoError("Published Zenodo record has no DOI")
    return {
        "status": status,
        "record_id": record_id,
        "concept_record_id": concept_record_id,
        "doi": doi,
        "concept_doi": concept_doi,
        "record_url": f"https://doi.org/{doi}",
        "concept_url": f"https://doi.org/{concept_doi}" if concept_doi else None,
        "filename": PDF_NAME,
        "bytes": artifact.size,
        "md5": artifact.md5,
        "sha256": artifact.sha256,
    }


def publish_version(
    client: ZenodoClient,
    *,
    concept_record_id: str,
    artifact: Artifact,
    metadata: dict[str, Any],
) -> dict[str, Any]:
    if not concept_record_id.isdigit():
        raise ZenodoError("Concept record ID must be numeric")
    depositions = client.list_family_depositions(concept_record_id)
    if not depositions:
        raise ZenodoError(
            "No bootstrapped DOI family found; run the explicit bootstrap step first"
        )
    draft, latest = select_draft_and_latest(depositions)
    target_version = str(metadata["version"])

    if draft is None and latest is not None:
        latest_version = str(latest.get("metadata", {}).get("version", ""))
        if latest_version == target_version:
            record = client.public_record(int(latest.get("record_id") or latest["id"]))
            verify_record_artifact(record, artifact)
            return result_from_record(record, artifact, "already-published")
        old_tuple = version_tuple(latest_version)
        new_tuple = version_tuple(target_version)
        if old_tuple and new_tuple and new_tuple <= old_tuple:
            raise ZenodoError(
                f"Refusing non-increasing DOI version {target_version}; "
                f"latest is {latest_version}"
            )
        draft = client.create_new_version(int(latest.get("record_id") or latest["id"]))

    if draft is None:
        raise ZenodoError("DOI family has neither an initial draft nor a published version")

    draft_version = str(draft.get("metadata", {}).get("version", ""))
    if draft_version and draft_version != target_version:
        raise ZenodoError(
            f"Existing draft targets version {draft_version}, not {target_version}"
        )
    draft_id = int(draft["id"])
    for existing in draft.get("files", []):
        file_id = existing.get("id")
        if not file_id:
            raise ZenodoError("Existing draft file has no deletable ID")
        client.delete_file(draft_id, str(file_id))

    updated = client.update_metadata(draft_id, metadata)
    bucket_url = updated.get("links", {}).get("bucket")
    if not bucket_url:
        raise ZenodoError("Zenodo draft has no upload bucket")
    client.upload_pdf(bucket_url, artifact)
    published = client.publish(draft_id)
    record_id = int(published.get("record_id") or published.get("id"))
    record = client.wait_for_public_record(record_id)
    verify_record_artifact(record, artifact)
    return result_from_record(record, artifact, "published")


def write_result(result: dict[str, Any], output: Path | None) -> None:
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if output:
        output.write_text(rendered, encoding="utf-8")
    sys.stdout.write(rendered)


def append_github_summary(result: dict[str, Any], path: Path | None) -> None:
    if not path:
        return
    lines = [
        "## Zenodo manuscript DOI",
        "",
        f"- Status: `{result['status']}`",
        f"- Version DOI: [{result['doi']}]({result['record_url']})",
    ]
    if result.get("concept_doi"):
        lines.append(
            f"- Concept DOI: [{result['concept_doi']}]({result['concept_url']})"
        )
    lines.extend(
        [
            f"- PDF SHA-256: `{result['sha256']}`",
            "",
        ]
    )
    with path.open("a", encoding="utf-8") as handle:
        handle.write("\n".join(lines))


def token_from_environment() -> str:
    return os.environ.get("ZENODO_TOKEN", "")


def add_api_argument(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--api-url",
        choices=sorted(ALLOWED_API_URLS),
        default=PRODUCTION_API,
        help="Official Zenodo API endpoint (production by default)",
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    bootstrap = subparsers.add_parser(
        "bootstrap", help="Create one empty concept-family draft"
    )
    add_api_argument(bootstrap)
    bootstrap.add_argument("--output", type=Path)

    publish = subparsers.add_parser(
        "publish", help="Publish or verify one formal manuscript release"
    )
    add_api_argument(publish)
    publish.add_argument("--pdf", type=Path, required=True)
    publish.add_argument("--version", required=True)
    publish.add_argument("--publication-date", required=True)
    publish.add_argument("--github-release-url", required=True)
    publish.add_argument("--concept-record-id", required=True)
    publish.add_argument("--metadata-template", type=Path, default=DEFAULT_METADATA)
    publish.add_argument("--output", type=Path)
    publish.add_argument("--github-step-summary", type=Path)
    publish.add_argument(
        "--dry-run", action="store_true", help="Validate and print the planned deposit"
    )
    publish.add_argument(
        "--confirm-publication",
        action="store_true",
        help="Required acknowledgement that Zenodo publication is permanent",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "bootstrap":
            client = ZenodoClient(args.api_url, token_from_environment())
            draft = client.create_empty_draft()
            result = {
                "status": "draft-created",
                "api_url": args.api_url,
                "deposit_id": draft.get("id"),
                "concept_record_id": str(draft.get("conceptrecid", "")),
                "reserved_version_doi": draft.get("metadata", {})
                .get("prereserve_doi", {})
                .get("doi"),
                "draft_url": draft.get("links", {}).get("html"),
            }
            if not result["concept_record_id"]:
                raise ZenodoError("Zenodo bootstrap response has no concept record ID")
            write_result(result, args.output)
            return 0

        artifact = inspect_pdf(args.pdf)
        template = load_metadata_template(args.metadata_template)
        metadata = build_metadata(
            template,
            version=args.version,
            publication_date=args.publication_date,
            github_release_url=args.github_release_url,
        )
        if args.dry_run:
            write_result(
                {
                    "status": "dry-run",
                    "concept_record_id": args.concept_record_id,
                    "metadata": metadata,
                    "filename": PDF_NAME,
                    "bytes": artifact.size,
                    "md5": artifact.md5,
                    "sha256": artifact.sha256,
                },
                args.output,
            )
            return 0
        if not args.confirm_publication:
            raise ZenodoError(
                "Publication is permanent; pass --confirm-publication explicitly"
            )
        client = ZenodoClient(args.api_url, token_from_environment())
        result = publish_version(
            client,
            concept_record_id=args.concept_record_id,
            artifact=artifact,
            metadata=metadata,
        )
        write_result(result, args.output)
        append_github_summary(result, args.github_step_summary)
        return 0
    except ZenodoError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
