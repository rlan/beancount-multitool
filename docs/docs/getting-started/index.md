---
title: Getting Started
---

## Prerequisites

Python 3.9, 3.10, 3.11 or 3.12.

These versions are tested via CI/CD. Prior versions of Python may work, just untested.

## Installation

First, update `pip`:

```sh
pip install -U pip
```

Then install:

```sh
pip install beancount-multitool
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

  Note: supported names of financial institutions: ['ja_bank', 'rakuten_bank',
  'rakuten_card', 'shinsei_bank']
```
