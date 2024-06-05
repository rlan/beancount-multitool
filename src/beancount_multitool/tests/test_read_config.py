from beancount_multitool.read_config import read_config


def test_read_config_no_such_file(tmp_path):
    file = tmp_path / "no_such_file.toml"
    config = read_config(file)
    assert config == {}


def test_read_config_empty_file(tmp_path):
    file = tmp_path / "empty.toml"
    file.write_text("")
    config = read_config(file)
    assert config == {}
