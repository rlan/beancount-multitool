from beancount_multitool.get_beancount_config import get_beancount_config


def test_get_beancount_config():
    # OK
    x = {"beancount": 123}
    assert get_beancount_config(x) == 123

    # section does not exist
    try:
        x = {"bean": 123}
        get_beancount_config(x)
    except KeyError as e:
        print(e)
        assert True
    else:
        assert AssertionError
