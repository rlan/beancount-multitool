# Introduction

## What is it?

Beancount Multitool is a collection of tools for the end users of [Beancount](https://github.com/beancount/beancount). There is a command-line-interface (CLI) tool that converts financial data from financial institutions to Beancount files.

## Why do I want it?

There is no importers for Japan financial institutions on Beancount's [contribution list](https://beancount.github.io/docs/external_contributions.html). So I created this tool.

[Here](institutions/index.md) is a list of supported financial institutions.

### What is it good for?

* The CLI tool saves the user from typing transaction from statements. The tool reads the raw CSV files downloaded from supported financial institutions. It converts the transactions in a CSV file to an importable Beancount file.
    * For example, it can label all debit transactions as `Expenses:JP:Unknown:NameOfInstitution`.
    * and all credit transaction as `Income:JP:Unknown:NameOfInstitution`.
* The CLI tool uses regular expressions to find recurring expenses. Once found, they are labeled by user-defined account and hashtags, e.g. `Expenses:JP:Food:Grocery` or `Expenses:JP:Food:Restaurant`.
* Outgoing money transfers can be found via regular expressions and be labeled with a reserved hashtag (`#reconcile`). Then an unique UUID string is generated and appended to that Beancount transaction. This UUID can be used on the receiving Beancount transaction to "link" them for reconcilation.

### What is it not good for?

* The regular expressions are manually added or modified by the user. The CLI tool does not make predictions from them. In other words, there is no machine learning.
* The duplicate transactions for a money transfer between two bank account still exist. The CLI tool does not reconcile them. The user is expected to do so.

### What is it *not yet* good for?

* TBD.
