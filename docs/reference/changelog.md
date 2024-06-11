# Changelog

0.7.0

* Supports Chase Sapphire Preferred Card.

0.6.1

* Typing errors in Python 3.9.

0.6.0

* All currency values use decimal.Decimal.
* Handle Rakuten ETC card charges in Rakuten Card.

0.5.0

* Add support for SBI Sumishin Net Bank.

0.4.1

* Bug fix. Multiple account matches were not written to Beancount transactions.

0.4.0

* Identify and label transactions to user-defined sub-accounts. Documentation is incoming.
  * __Breaking change__: Structure of `config.toml` has changed.

0.3.0

* Fix a hard-coded year bug in JABank.py.
* Add ruff. Run formatter and linter.

0.2.1

* Update README for PyPi project page.
* Add sys.exit to calls of cli.py:main.

0.2.0

* Show a list of supported financial institutions in --help.

0.1.0

* Initial version.
