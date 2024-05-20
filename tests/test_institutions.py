import pytest

from pathlib import Path
import beancount_multitool as bcmt


@pytest.fixture(params=bcmt.__INSTITUTIONS__)
def assets(tmp_path, request):
    name = request.param
    base_dir = Path("./tests/data")
    assert base_dir.is_dir(), f"Expected folder missing: {str(base_dir.resolve())}"
    data_dir = base_dir / name
    assert data_dir.is_dir(), f"Expected folder missing: {str(data_dir.resolve())}"
    in_file = data_dir / "test.csv"
    assert in_file.is_file(), f"Expected file missing: {str(in_file.resolve())}"
    config_file = data_dir / "config.toml"
    assert config_file.is_file(), f"Expected file missing: {str(config_file.resolve())}"
    ref_file = data_dir / "test.bean"
    assert ref_file.is_file(), f"Expected file missing: {str(ref_file.resolve())}"
    data = {
        "name": name,
        "in_file": str(in_file),
        "config_file": str(config_file),
        "ref_file": str(ref_file),
        "out_file": str(tmp_path / "out.bean"),
    }
    yield data


"""
def test_assets(assets):
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(assets)

"""


def test_institutions(assets):
    if assets["name"] == bcmt.JABank.NAME:
        app = bcmt.JABank(assets["config_file"])
    elif assets["name"] == bcmt.RakutenBank.NAME:
        app = bcmt.RakutenBank(assets["config_file"])
    elif assets["name"] == bcmt.RakutenCard.NAME:
        app = bcmt.RakutenCard(assets["config_file"])
    elif assets["name"] == bcmt.ShinseiBank.NAME:
        app = bcmt.ShinseiBank(assets["config_file"])

    app.convert(assets["in_file"], assets["out_file"])
    out = Path(assets["out_file"])
    ref = Path(assets["ref_file"])
    data_out = out.read_text(encoding="utf-8")
    data_ref = ref.read_text(encoding="utf-8")
    assert data_ref == data_out
