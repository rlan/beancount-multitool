def get_value(config: dict, section: str, variable: str) -> str:
    """Validate and return value

    Expected TOML data:

        [section]
        variable = value

    Parameters
    ----------
    config : dict
    section : str
    variable : str

    Returns
    -------
    str
        value

    Raises
    ------
    KeyError
        if "section" key or "variable" key does not exist.
    """
    if section in config:
        if variable in config[section]:
            return config[section][variable]
        else:
            raise KeyError(f"Expects variable: {variable}")
    else:
        raise KeyError(f"Expects section: {section}")
