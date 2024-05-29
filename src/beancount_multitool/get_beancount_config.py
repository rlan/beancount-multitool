def get_beancount_config(config: dict) -> dict:
    """Validate beancount config

    Expects TOML data:

        [beacount]

    Parameters
    ----------
    config : dict
        Beancount configuration.

    Returns
    -------
    dict
        config["beancount"]

    Raises
    ------
    KeyError
        if "beancount" key does not exist.
    """
    if "beancount" in config:
        return config["beancount"]
    else:
        raise KeyError("Expects section in TOML file: [beancount]")
