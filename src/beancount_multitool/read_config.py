import sys

if sys.version_info >= (3, 11):
    import tomllib
else:
    try:
        import tomli as tomllib
    except ImportError:
        raise ImportError("Is tomli module installed?")


def read_config(file_name: str) -> dict:
    """Reads a TOML config file

    Parameters
    ----------
    file_name : str
        File name to the input TOML file.

    Returns
    -------
    dict
        TOML file content
    """
    with open(file_name, "rb") as f:
        config = tomllib.load(f)
        # print(config) # debug
        # print(type(config)) # debug
        return config
