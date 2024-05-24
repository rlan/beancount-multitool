from beancount_multitool.get_value import get_value


def test_get_value():
    x = {"section": {"variable": "value"}}

    # okay
    assert get_value(x, "section", "variable") == "value"

    # variable does not exist
    try:
        get_value(x, "section", "unknown")
    except KeyError as e:
        print(e)
        assert True
    else:
        assert AssertionError

    # section does not exist
    try:
        get_value(x, "unknown", "")
    except KeyError as e:
        print(e)
        assert True
    else:
        assert AssertionError
