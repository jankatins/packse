import pytest
from packse import __development_base_path__

from .common import snapshot_command


def test_list_no_target_finds_all_valid_scenarios(snapshot):
    assert snapshot_command(["list"]) == snapshot


def test_list_no_versions(snapshot):
    assert snapshot_command(["list", "--no-versions"]) == snapshot


def test_list_short_names(snapshot):
    assert snapshot_command(["list", "--short-names"]) == snapshot


def test_list_no_sources(snapshot):
    assert snapshot_command(["list", "--no-sources"]) == snapshot


def test_list_target_does_not_exist(snapshot):
    assert snapshot_command(["list", "foo"]) == snapshot


@pytest.mark.usefixtures("tmpcwd")
def test_list_one_target_does_not_exist(snapshot):
    target = __development_base_path__ / "scenarios" / "example.json"
    assert snapshot_command(["list", str(target), "foo"]) == snapshot


def test_list_invalid_target(snapshot, tmpcwd):
    bad_target = tmpcwd / "test.json"
    bad_target.touch()
    good_target = __development_base_path__ / "scenarios" / "example.json"
    assert snapshot_command(["list", str(bad_target), str(good_target)]) == snapshot


def test_list_invalid_target_skip_invalid(snapshot, tmpcwd):
    bad_target = tmpcwd / "test.json"
    bad_target.touch()
    good_target = __development_base_path__ / "scenarios" / "example.json"
    assert (
        snapshot_command(["list", str(bad_target), str(good_target), "--skip-invalid"])
        == snapshot
    )


def test_list_example(snapshot):
    target = __development_base_path__ / "scenarios" / "example.json"
    assert snapshot_command(["list", str(target)]) == snapshot
