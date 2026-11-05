"""Checks the upstream watch's decisions against stubbed answers.

scripts/check_upstream_release.py lists the repository through GitHub's API. These tests
replace its one network call, `_get`, with a table of answers, so they run offline. They show
what the report says in each case the watch knows.
"""

import http.client
import importlib.util
import urllib.error
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "check_upstream_release.py"


@pytest.fixture
def watch():
    """A fresh copy of the script, so no test sees another's stub."""
    spec = importlib.util.spec_from_file_location("watch_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _answers(watch, pins=None):
    """The answers of an unchanged upstream, built from the pins."""
    pins = pins if pins is not None else watch.pins()
    trees = {}
    for path, sha in pins.items():
        head, _, tail = path.partition("/")
        if tail:
            trees.setdefault(head, []).append(
                {"path": tail, "type": "blob", "sha": sha}
            )
    root = [
        {"path": name, "type": "tree", "sha": f"tree-{name}"} for name in trees
    ] + [{"path": "LICENSE.md", "type": "blob", "sha": pins["LICENSE.md"]}]
    answers = {
        "/releases/latest": {"tag_name": watch.PINNED_TAG},
        f"/git/ref/tags/{watch.PINNED_TAG}": {"object": {"sha": watch.PINNED_COMMIT}},
        f"/git/trees/{watch.PINNED_COMMIT}": {"tree": root},
        "/git/trees/master": {"tree": root},
    }
    for name, tree in trees.items():
        answers[f"/git/trees/tree-{name}?recursive=1"] = {"tree": tree}
    return answers


def _run(watch, answers, capsys, argv=()):
    def fake_get(path):
        answer = answers[path]
        if isinstance(answer, Exception):
            raise answer
        return answer

    watch._get = fake_get
    code = watch.main(list(argv))
    return code, capsys.readouterr().out


def test_an_unchanged_upstream_reports_nothing(watch, capsys):
    code, report = _run(watch, _answers(watch), capsys)
    assert code == 0, report
    assert "**" not in report


def test_another_release_is_reported_and_quoted(watch, capsys):
    answers = _answers(watch)
    answers["/releases/latest"] = {"tag_name": "dpv-2.4"}
    code, report = _run(watch, answers, capsys)
    assert code == 1
    assert "The latest DPV release is `dpv-2.4`" in report


def test_a_moved_tag_is_reported(watch, capsys):
    answers = _answers(watch)
    answers[f"/git/ref/tags/{watch.PINNED_TAG}"] = {"object": {"sha": "abc123"}}
    answers["/git/trees/abc123"] = answers[f"/git/trees/{watch.PINNED_COMMIT}"]
    code, report = _run(watch, answers, capsys)
    assert code == 1
    assert "moved to `abc123`" in report


def test_a_changed_file_is_reported_by_path(watch, capsys):
    pins = watch.pins()
    changed = dict(pins, **{"2.3/dpv/dpv.ttl": "0" * 40})
    answers = _answers(watch, changed)
    code, report = _run(watch, answers, capsys)
    assert code == 1
    assert "1 pinned files changed" in report
    assert "`2.3/dpv/dpv.ttl`" in report


def test_a_file_gone_is_reported_by_path(watch, capsys):
    pins = dict(watch.pins())
    del pins["examples/E0001.ttl"]
    code, report = _run(watch, _answers(watch, pins), capsys)
    assert code == 1
    assert "1 pinned files gone" in report


def test_a_new_turtle_file_is_for_information_only(watch, capsys):
    pins = dict(watch.pins(), **{"2.3/new/new.ttl": "1" * 40})
    code, report = _run(watch, _answers(watch, pins), capsys)
    assert code == 0
    assert "For information" in report
    assert "`2.3/new/new.ttl`" in report


def test_a_serialisation_beside_the_pins_stays_quiet(watch, capsys):
    pins = dict(watch.pins(), **{"2.3/dpv/dpv-owl.ttl": "1" * 40, "2.3/dpv/dpv.csv": "2" * 40})
    code, report = _run(watch, _answers(watch, pins), capsys)
    assert code == 0
    assert "For information" not in report


def test_a_changed_licence_is_reported(watch, capsys):
    answers = _answers(watch)
    root = [dict(e) for e in answers["/git/trees/master"]["tree"]]
    for entry in root:
        if entry["path"] == "LICENSE.md":
            entry["sha"] = "2" * 40
    answers["/git/trees/master"] = {"tree": root}
    code, report = _run(watch, answers, capsys)
    assert code == 1
    assert "LICENSE.md on the default branch changed" in report


def test_a_truncated_listing_cannot_finish(watch, capsys):
    answers = _answers(watch)
    answers["/git/trees/tree-2.3?recursive=1"]["truncated"] = True
    code, report = _run(watch, answers, capsys)
    assert code == 1
    assert "could not finish" in report


@pytest.mark.parametrize(
    "error",
    [
        urllib.error.URLError("refused"),
        http.client.IncompleteRead(b""),
        EOFError("cut off"),
        ValueError("too large"),
    ],
    ids=["refused", "incomplete", "eof", "too-large"],
)
def test_a_failed_check_is_reported_and_quoted(watch, capsys, error):
    answers = _answers(watch)
    answers["/releases/latest"] = error
    code, report = _run(watch, answers, capsys)
    assert code == 1
    assert "The latest release check could not finish" in report


def test_server_text_cannot_mention_anyone(watch, capsys):
    answers = _answers(watch)
    answers["/releases/latest"] = {"tag_name": "@someone `x`\n\nsecond"}
    code, report = _run(watch, answers, capsys)
    assert code == 1
    assert "`@someone 'x' second`" in report


def test_a_redirect_off_the_api_is_refused(watch):
    handler = watch._ApiRedirect()
    with pytest.raises(ValueError, match="off api.github.com"):
        handler.redirect_request(None, None, 302, "Found", {}, "https://example.com/x")
    with pytest.raises(ValueError, match="off api.github.com"):
        handler.redirect_request(None, None, 302, "Found", {}, "http://api.github.com/x")


def test_the_report_file_holds_what_is_printed(watch, capsys, tmp_path):
    target = tmp_path / "report.md"
    code, report = _run(watch, _answers(watch), capsys, ["--report", str(target)])
    assert code == 0
    assert target.read_text(encoding="utf-8") == report
