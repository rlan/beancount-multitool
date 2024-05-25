import pytest

from pathlib import Path
import beancount_multitool as bcmt


@pytest.fixture
def base_dir():
    dir = Path("./tests/data2")
    assert dir.is_dir(), f"Expected folder missing: {str(dir.resolve())}"
    yield dir


@pytest.fixture(params=["ja_bank"])
def data_dir(base_dir, request):
    name = request.param
    dir = base_dir / name
    assert dir.is_dir(), f"Expected folder missing: {str(dir.resolve())}"
    yield name, dir


@pytest.fixture
def in_file(data_dir):
    _, dir = data_dir
    file = dir / "test.csv"
    assert file.is_file(), f"Expected file missing: {str(file.resolve())}"
    yield file


@pytest.fixture
def config_file(data_dir):
    name, dir = data_dir
    file = dir / "config.toml"
    assert file.is_file(), f"Expected file missing: {str(file.resolve())}"
    yield name, file


@pytest.fixture
def app(config_file):
    name, file = config_file
    if name == bcmt.JABank.NAME:
        yield bcmt.JABank(str(file))
    elif name == bcmt.RakutenBank.NAME:
        yield bcmt.RakutenBank(str(file))
    elif name == bcmt.RakutenCard.NAME:
        yield bcmt.RakutenCard(str(file))
    elif name == bcmt.ShinseiBank.NAME:
        yield bcmt.ShinseiBank(str(file))
    else:
        raise AssertionError(f"Unknown institution name: {name}")


@pytest.fixture
def ref_file(data_dir):
    _, dir = data_dir
    file = dir / "test.bean"
    assert file.is_file(), f"Expected file missing: {str(file.resolve())}"
    yield file


@pytest.fixture
def out_file(tmp_path):
    yield tmp_path / "out.bean"


@pytest.fixture
def run(app, in_file, out_file):
    app.convert(str(in_file), str(out_file))
    yield out_file


def test_data2(run, ref_file):
    data_out = run.read_text(encoding="utf-8")
    data_ref = ref_file.read_text(encoding="utf-8")
    assert data_ref == data_out
