import sys

if sys.version_info >= (3, 11):
    import tomllib
else:
    try:
        import tomli as tomllib
    except ImportError as e:
        raise ImportError("Is tomli module installed?") from e


def read_config(file_name: str) -> dict:
    """Reads a TOML config file

    Parameters
    ----------
    file_name : str
        File name to the input TOML file.

    Returns
    -------
    dict
        TOML file content. Returns an empty dict if file not found
        or error decoding TOML data.
    """
    try:
        with open(file_name, "rb") as f:
            try:
                config = tomllib.load(f)
            except tomllib.TOMLDecodeError as e:
                print(f"Has invalid TOML data: {file_name}")
                print(e)
                config = {}
            else:
                if len(config) == 0:  # Empty file
                    print(f"Has no TOML data: {file_name}")

    except FileNotFoundError as e:
        print(f"File not found: {file_name}")
        print(e)
        config = {}

    # print(config) # debug
    # print(type(config)) # debug
    return config
