#!/usr/bin/env python3
"""Static and optional API checks for a data-case submission package."""

from __future__ import annotations

import argparse
import json
import sys
import urllib.request
import zipfile
from pathlib import Path


FORBIDDEN_PARTS = (
    "__pycache__",
    "node_modules/",
    "archive/",
)

FORBIDDEN_NAMES = (
    "ProblemDataPage",
)

SUSPICIOUS_DOC_TERMS = (
    "Problem Data",
    "soft-only",
    "Streamlit",
    "localhost:18501",
    "localhost:18502",
)

REQUIRED_FILES = (
    "README.md",
    "MANIFEST.txt",
)


def normalize(path: str) -> str:
    return path.replace("\\", "/").lstrip("./")


def load_entries(path: Path) -> tuple[dict[str, bytes], str]:
    if path.is_dir():
        entries: dict[str, bytes] = {}
        for file_path in path.rglob("*"):
            if file_path.is_file():
                rel = normalize(str(file_path.relative_to(path)))
                entries[rel] = file_path.read_bytes()
        return entries, ""

    if zipfile.is_zipfile(path):
        entries = {}
        with zipfile.ZipFile(path) as zf:
            names = [name for name in zf.namelist() if not name.endswith("/")]
            prefix = ""
            if names and all("/" in name for name in names):
                first = names[0].split("/", 1)[0] + "/"
                if all(name.startswith(first) for name in names):
                    prefix = first
            for name in names:
                rel = normalize(name[len(prefix) :] if prefix and name.startswith(prefix) else name)
                entries[rel] = zf.read(name)
        return entries, prefix

    raise SystemExit(f"Not a folder or zip file: {path}")


def decode_text(blob: bytes) -> str:
    return blob.decode("utf-8", errors="replace")


def check_static(path: Path) -> int:
    entries, prefix = load_entries(path)
    failures: list[str] = []

    for required in REQUIRED_FILES:
        if required not in entries:
            failures.append(f"Missing required file: {required}")

    for name in entries:
        lower = normalize(name).lower()
        if lower.endswith(".zip"):
            failures.append(f"Nested zip detected: {name}")
        for part in FORBIDDEN_PARTS:
            if part.lower() in lower:
                failures.append(f"Forbidden package path: {name}")
        for token in FORBIDDEN_NAMES:
            if token.lower() in lower:
                failures.append(f"Forbidden stale filename: {name}")

    if "MANIFEST.txt" in entries:
        manifest = decode_text(entries["MANIFEST.txt"]).splitlines()
        if "Package contents:" in manifest:
            listed = {normalize(line.strip()) for line in manifest[manifest.index("Package contents:") + 1 :] if line.strip()}
            actual = {normalize(name) for name in entries}
            missing_from_manifest = sorted(actual - listed)
            missing_from_package = sorted(listed - actual)
            if missing_from_manifest:
                failures.append(f"Manifest missing package files: {missing_from_manifest[:10]}")
            if missing_from_package:
                failures.append(f"Manifest lists absent files: {missing_from_package[:10]}")

    for doc_name in ("README.md", "docs/中文操作手冊.md", "docs/strategy_document.md"):
        if doc_name not in entries:
            continue
        text = decode_text(entries[doc_name])
        for term in SUSPICIOUS_DOC_TERMS:
            if term in text:
                failures.append(f"Suspicious stale term in {doc_name}: {term}")

    print(json.dumps({
        "path": str(path),
        "zip_prefix": prefix,
        "entry_count": len(entries),
        "failures": failures,
    }, ensure_ascii=False, indent=2))
    return 1 if failures else 0


def check_api(base_url: str, endpoints: list[str]) -> int:
    failures = []
    for endpoint in endpoints:
        url = base_url.rstrip("/") + "/" + endpoint.lstrip("/")
        try:
            with urllib.request.urlopen(url, timeout=10) as response:
                status = response.status
                if status != 200:
                    failures.append(f"{status} {url}")
        except Exception as exc:  # pragma: no cover - diagnostic path
            failures.append(f"{url}: {exc}")

    print(json.dumps({"base_url": base_url, "api_failures": failures}, ensure_ascii=False, indent=2))
    return 1 if failures else 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path, help="Submission folder or zip path")
    parser.add_argument("--base-url", help="Optional running dashboard base URL for API checks")
    parser.add_argument(
        "--endpoint",
        action="append",
        default=[],
        help="API endpoint to check. May be repeated.",
    )
    args = parser.parse_args()

    rc = check_static(args.path)
    if args.base_url:
        endpoints = args.endpoint or [
            "/api/status",
            "/api/overview",
            "/api/filter-options",
        ]
        rc = max(rc, check_api(args.base_url, endpoints))
    return rc


if __name__ == "__main__":
    sys.exit(main())
