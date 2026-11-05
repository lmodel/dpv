#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Check the DPV Community Group's repository against the edition the schema renders.

The schema renders DPV at the release pinned below, and upstream/ holds that release's
files unchanged. Three things can change without any change in this repository:

- the Community Group publishes another release;
- the pinned tag moves, or a pinned file changes or goes;
- the licence file on the default branch changes.

The script lists the repository's trees through GitHub's API and compares git object
hashes, so it downloads no file. scripts/upstream_pins.tsv holds each file's hash. The
script prints a Markdown report and exits 1 on any of the above, or when a check could not
finish. A Turtle file added beside the pinned vocabularies, or a machine-readable file in
a mapping folder that holds only a web page today, is reported for information.

Text a server chose is quoted as code on one line in the report, so the issue the workflow
opens from it cannot mention anyone. A redirect is followed only to an https address on
api.github.com. Set ``GITHUB_TOKEN`` to raise the API's rate limit. Usage::

    python scripts/check_upstream_release.py [--report FILE]
"""

from __future__ import annotations

import argparse
import http.client
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PINS = ROOT / "scripts" / "upstream_pins.tsv"
USER_AGENT = "lmodel-dpv-upstream-check"
API = "https://api.github.com/repos/w3c-cg/dpv"
HOST = "api.github.com"

# The most the script reads of one answer. A recursive listing of the edition's folder is
# about 300 kB.
MAX_BYTES = 20_000_000

# The release the schema renders, the commit its tag names and the edition's address.
# tests/test_upstream.py holds the schema headers and these pins equal. Move them together,
# with upstream/ and scripts/upstream_pins.tsv, for another release.
PINNED_EDITION = "2.3"
PINNED_TAG = "dpv-2.3"
PINNED_DATE = "2026-02-28"
PINNED_COMMIT = "cbcd21567808812677eeb3bb0f05b2ff2c2211a5"
PINNED_SOURCE = "https://w3id.org/dpv/2.3"

# The folders a pinned file sits under, and the licence at the root.
FOLDERS = (PINNED_EDITION, "examples", "mappings")
LICENCE = "LICENSE.md"

# A serialisation or a module copy repeats a vocabulary, so the copy leaves them out.
LEFT_OUT = ("-owl.ttl", "/modules/")


class _ApiRedirect(urllib.request.HTTPRedirectHandler):
    """Follow a redirect only to an https address on the API's host."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        parts = urllib.parse.urlsplit(newurl)
        if parts.scheme != "https" or parts.hostname != HOST:
            raise ValueError(f"a redirect leads off {HOST}, to {newurl}")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


# An opener in place of urlopen's, whose redirect handler follows any address.
_open = urllib.request.build_opener(_ApiRedirect).open


def _get(path: str):
    """The JSON answer to one API path, read up to the cap."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(f"{API}{path}", headers=headers)
    with _open(req, timeout=60) as resp:
        body = resp.read(MAX_BYTES + 1)
    if len(body) > MAX_BYTES:
        raise ValueError(f"the answer to {path} is larger than {MAX_BYTES} bytes")
    return json.loads(body)


def _code(text: object) -> str:
    """Text a server chose, as a code span on one line, so it cannot mention a person or
    add a link in the issue. A blank line would end the span, so every run of spaces and
    line breaks is one space."""
    return "`" + " ".join(str(text).replace("`", "'").split()) + "`"


def pins() -> dict[str, str]:
    """Each pinned path and its git object hash."""
    rows = (line.split("\t") for line in PINS.read_text(encoding="utf-8").splitlines())
    return {path: sha for path, sha in rows}


def _tree(sha: str, recursive: bool = False) -> list[dict]:
    """The entries of one tree. A listing GitHub cuts short cannot be compared."""
    answer = _get(f"/git/trees/{sha}" + ("?recursive=1" if recursive else ""))
    if answer.get("truncated"):
        raise ValueError(f"GitHub cut short the listing of tree {sha}")
    return answer["tree"]


def listing(commit: str) -> dict[str, str]:
    """Each file under the pinned folders at a commit, and the licence, by path."""
    root = {entry["path"]: entry for entry in _tree(commit)}
    found = {LICENCE: root[LICENCE]["sha"]} if LICENCE in root else {}
    for folder in FOLDERS:
        if folder not in root:
            continue
        for entry in _tree(root[folder]["sha"], recursive=True):
            if entry["type"] == "blob":
                found[f"{folder}/{entry['path']}"] = entry["sha"]
    return found


def check_release() -> tuple[list[str], bool]:
    """Report whether the latest release is the pinned one."""
    tag = _get("/releases/latest")["tag_name"]
    if tag != PINNED_TAG:
        return [
            f"- **The latest DPV release is {_code(tag)}; the schema renders "
            f"{PINNED_TAG}.** Read what changed, decide whether the schema moves to it, "
            "and move upstream/, the pins and the schema headers together."
        ], True
    return [f"- The latest DPV release is the pinned one, {PINNED_TAG}."], False


def check_tag() -> tuple[list[str], bool]:
    """Report whether the tag names the pinned commit and holds the pinned files."""
    commit = _get(f"/git/ref/tags/{PINNED_TAG}")["object"]["sha"]
    lines = []
    attention = False
    if commit != PINNED_COMMIT:
        attention = True
        lines.append(
            f"- **The tag {PINNED_TAG} moved to {_code(commit)}.** Find out why a "
            "published release moved before trusting the copy in upstream/."
        )
    found = listing(commit)
    pinned = pins()
    gone = sorted(path for path in pinned if path not in found)
    changed = sorted(
        path for path, sha in pinned.items() if path in found and found[path] != sha
    )
    for label, paths in (("gone", gone), ("changed", changed)):
        if paths:
            attention = True
            shown = ", ".join(_code(path) for path in paths[:10])
            lines.append(f"- **{len(paths)} pinned files {label}:** {shown}.")
    if not gone and not changed:
        lines.append(f"- All {len(pinned)} pinned files are unchanged.")
    added = sorted(
        path
        for path in found
        if path not in pinned
        and (
            path.endswith(".ttl")
            or path.startswith("mappings/")
            and path.endswith(".csv")
        )
        and not any(part in path for part in LEFT_OUT)
    )
    if added:
        shown = ", ".join(_code(path) for path in added[:10])
        lines.append(
            f"- For information, {len(added)} files sit beside the pins: {shown}."
        )
    return lines, attention


def check_licence() -> tuple[list[str], bool]:
    """Report whether the licence on the default branch is the pinned file."""
    root = {entry["path"]: entry["sha"] for entry in _tree("master")}
    if root.get(LICENCE) != pins()[LICENCE]:
        return [
            f"- **{LICENCE} on the default branch changed.** Read what changed, and "
            "update NOTICE if the licence moved."
        ], True
    return ["- The licence on the default branch is the pinned file."], False


# Each check, by the name the report gives it when it cannot finish.
CHECKS = (
    ("latest release", check_release),
    ("pinned tag and files", check_tag),
    ("licence", check_licence),
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--report", type=Path, help="Also write the Markdown report to this file"
    )
    args = parser.parse_args(argv)
    lines = [
        f"- Pinned edition: DPV {PINNED_EDITION} of {PINNED_DATE}, {PINNED_SOURCE}."
    ]
    attention = False
    for label, check in CHECKS:
        try:
            found, needs = check()
        # OSError covers a refused or failed request and a timeout, HTTPException and
        # EOFError a connection cut off mid-answer, LookupError and ValueError an answer
        # of another shape or too large.
        except (
            OSError,
            http.client.HTTPException,
            EOFError,
            LookupError,
            ValueError,
        ) as err:
            found = [f"- **The {label} check could not finish: {_code(err)}.**"]
            needs = True
        lines += found
        attention = attention or needs
    text = "\n".join(lines) + "\n"
    print(text, end="")
    if args.report:
        args.report.write_text(text, encoding="utf-8")
    return 1 if attention else 0


if __name__ == "__main__":
    sys.exit(main())
