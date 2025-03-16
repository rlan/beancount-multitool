# Getting Started

## Prerequisites

Python 3.9, 3.10, 3.11, 3.12 or 3.13.

All of these versions are tested via [CI/CD]. Due to use of [removeprefix()], not compatible with previous versions of Python.

## Installation

First, install [pipx] (not pip):

Then:

```sh
pipx install beancount-multitool
```

## Try it out!

Let's see if installation was successful:

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

  Note: supported financial institutions are ['ja_bank', 'rakuten_bank',
  'rakuten_card', 'shinsei_bank', 'sumishin_net_bank']
```

## Update to a new version

```sh
pipx upgrade beancount-multitool
```

## Uninstallation

```sh
pipx uninstall beancount-multitool
```

[removeprefix()]: https://docs.python.org/3/library/stdtypes.html#str.removeprefix
[CI/CD]: https://github.com/rlan/beancount-multitool/actions/workflows/tests.yml
[pipx]: https://github.com/pypa/pipx
