#!/usr/bin/env python3
"""Upload a local file to an Agent Body document-upload URL."""

from __future__ import annotations

import argparse
import json
import mimetypes
import sys
from http.client import HTTPSConnection
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit


CHUNK_SIZE = 1024 * 1024


def parse_headers(args: argparse.Namespace) -> dict[str, str]:
    if args.headers_json and args.headers_file:
        raise ValueError("use only one of --headers-json and --headers-file")
    raw = args.headers_json
    if args.headers_file:
        raw = args.headers_file.read_text(encoding="utf-8")
    if not raw:
        return {}
    value = json.loads(raw)
    if not isinstance(value, dict):
        raise ValueError("headers must be a JSON object")
    headers = {}
    for key, item in value.items():
        if not isinstance(key, str) or not isinstance(item, str):
            raise ValueError("header names and values must be strings")
        if "\r" in key or "\n" in key or "\r" in item or "\n" in item:
            raise ValueError("headers must not contain newlines")
        headers[key] = item
    return headers


def upload(args: argparse.Namespace) -> dict[str, object]:
    file_path = args.file.resolve()
    if not file_path.is_file():
        raise ValueError(f"file does not exist: {file_path}")

    parsed = urlsplit(args.upload_url)
    if parsed.scheme != "https" or not parsed.netloc:
        raise ValueError("upload URL must use https")

    headers = parse_headers(args)
    headers.setdefault(
        "Content-Type",
        mimetypes.guess_type(file_path.name)[0] or "application/octet-stream",
    )
    size_bytes = file_path.stat().st_size
    max_bytes = getattr(args, "max_bytes", None)
    if max_bytes is not None and size_bytes > max_bytes:
        raise ValueError(f"file exceeds maxBytes: {size_bytes} > {max_bytes}")
    headers["Content-Length"] = str(size_bytes)
    path = urlunsplit(("", "", parsed.path or "/", parsed.query, ""))

    connection = HTTPSConnection(parsed.netloc, timeout=args.timeout)
    try:
        connection.putrequest(args.method, path)
        for key, value in headers.items():
            connection.putheader(key, value)
        connection.endheaders()
        with file_path.open("rb") as source:
            while chunk := source.read(CHUNK_SIZE):
                connection.send(chunk)
        response = connection.getresponse()
        response.read(512)
        if not 200 <= response.status < 300:
            raise RuntimeError(f"upload failed with HTTP {response.status} {response.reason}")
        result = {
            "uploaded": True,
            "status": response.status,
            "bytes": size_bytes,
            "file": file_path.name,
        }
        if response.getheader("ETag"):
            result["etag"] = response.getheader("ETag")
        return result
    finally:
        connection.close()


def main() -> int:
    parser = argparse.ArgumentParser(description="Upload a local document to a temporary MCP upload URL")
    parser.add_argument("--file", type=Path, required=True, help="local file to upload")
    parser.add_argument("--upload-url", required=True, help="temporary URL returned by document-upload")
    parser.add_argument("--method", choices=("PUT",), default="PUT")
    parser.add_argument("--headers-json", help="JSON object of signed upload headers")
    parser.add_argument("--headers-file", type=Path, help="file containing the signed upload headers as JSON")
    parser.add_argument("--max-bytes", type=int, help="maximum size returned by document-upload")
    parser.add_argument("--timeout", type=float, default=120.0)
    args = parser.parse_args()
    try:
        print(json.dumps(upload(args), ensure_ascii=True))
    except (OSError, ValueError, RuntimeError, json.JSONDecodeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
