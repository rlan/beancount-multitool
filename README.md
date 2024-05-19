# Beancount Multitool

![Tests badge](https://github.com/rlan/beancount-multitool/actions/workflows/tests.yml/badge.svg)
![python version required](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Frlan%2Fbeancount-multitool%2Fmain%2Fpyproject.toml)
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

Usage:

```txt
$ bean-mt --help
Usage: bean-mt [OPTIONS] NAME CONFIG DATA

  Read financial data and output a Beancount file.

  NAME is the name of the financial institution, e.g. RakutenBank.

  CONFIG is a .toml file with run-time configurations, e.g. config.toml.

  DATA is the raw financial data downloaded from NAME, e.g. input.csv.

Options:
  --output PATH  Resulting Beancount file
  --version      Show the version and exit.
  --help         Show this message and exit.
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

## Installation

```sh
pip install beancount-multitool
```

## Requirements

* Python 3.9 or higher.

## More

* [Todo](./todo.md)
* [Changelog](./changelog.md)
* [Development](./development.md)

## License

MIT License
