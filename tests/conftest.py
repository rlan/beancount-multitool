# content of conftest.py

# Ref: https://stackoverflow.com/a/25188424
def pytest_configure(config):
    import sys
    sys._called_from_pytest = True

def pytest_unconfigure(config):
    import sys
    if hasattr(sys, "_called_from_pytest"):
        del sys._called_from_pytest
