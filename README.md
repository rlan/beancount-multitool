# Beancount Multitool

![Tests badge](https://github.com/rlan/beancount-multitool/actions/workflows/tests.yml/badge.svg)
![pypi version](https://img.shields.io/pypi/v/beancount-multitool
)
![python version required](https://img.shields.io/pypi/pyversions/beancount-multitool
)
![static coverage badge](https://img.shields.io/badge/Coverage-97%25-blue)

Beancount Multitool is a command-line-interface (CLI) tool that converts financial data from financial institutions to Beancount files.

The following institutions are supported:

* Japan
  * [JA Bank ＪＡネットバンク](https://www.jabank.jp/)
  * [Rakuten Card 楽天カード](https://www.rakuten-card.co.jp/)
  * [Rakuten Bank 楽天銀行](https://www.rakuten-bank.co.jp/)
  * [SBI Shinsei Bank 新生銀行](https://www.sbishinseibank.co.jp/)

What these scripts __can__ do:

* Read raw CSV files downloaded from each institution's website.
* Label debit and credit transactions to respective account types.
  * Debit: `Expenses:JP:Unknown:NameOfInstitution`
  * Credit: `Income:JP:Unknown:NameOfInstitution`

What these scripts __can not__ (yet) do:

* Label transactions with different sub-accounts, e.g., `Expenses:JP:Food:Grocery` or `Expenses:JP:Food:Restaurant`.

Installation:

```sh
pip install beancount-multitool
```

Usage:

```sh
bean-mt --help
```

```txt
Usage: bean-mt [OPTIONS] NAME CONFIG DATA

  Read financial data and output a Beancount file.

  NAME is the name of the financial institution. See Note below for a list of
  supported names.

  CONFIG is a .toml file with run-time configurations, e.g. config.toml.

  DATA is the raw financial data downloaded from NAME, e.g. input.csv.

Options:
  --output PATH  Resulting Beancount file
  --version      Show the version and exit.
  --help         Show this message and exit.

  Note: supported names of financial institutions: ['ja_bank', 'rakuten_bank',
  'rakuten_card', 'shinsei_bank']
```

Example:

```sh
bean-mt rakuten_bank config.toml 2024-01.csv --output 2024-01.bean
```

Workflow:

1. Download the raw CSV files from a financial institutions.
2. Run `bean-mt`.
3. Include the `output.bean` file in my ledger.
4. Manually edit that Beancount file to my needs.

config.toml:

There is a default config.toml per financial institutions. Examples are in the test [data folder](./tests/data/).

## Requirements

* Python 3.9 or higher.

## More

* [Todo](./todo.md)
* [Changelog](./changelog.md)
* [Development](./development.md)

## License

MIT License
