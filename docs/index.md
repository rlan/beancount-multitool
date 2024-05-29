# Introduction

## What is it?

Beancount Multitool is a collection of tools for the end users of [Beancount](https://github.com/beancount/beancount). Currenly, the entry point is a command-line-interface (CLI) tool that converts financial data from financial institutions to Beancount files.

## Why do I want it?

There is no importers for Japan financial institutions on Beancount's [contribution list](https://beancount.github.io/docs/external_contributions.html). So I created this tool. [Here](institutions/index.md) is a list of supported financial institutions.

The target audience is someone who is quite hands-on with their tools, in the same way a Beancount user is.

### What is it good for?

* The CLI tool saves the user from typing transaction from statements. The tool reads the raw CSV files downloaded from supported financial institutions. It converts the transactions in a CSV file to an importable Beancount file.
    * For example, it can label all debit transactions as `Expenses:JP:Unknown:NameOfInstitution`.
    * and all credit transaction as `Income:JP:Unknown:NameOfInstitution`.
* The CLI tool uses regular expressions to find recurring expenses. Once found, they are labeled by user-defined account and tags, e.g. `Expenses:JP:Food:Grocery` or `Expenses:JP:Food:Restaurant`.
* Outgoing money transfers can be found via regular expressions and be labeled with a reserved tag (`#reconcile`). Then an unique UUID string is generated and appended to that Beancount transaction. This UUID can be used on the receiving Beancount transaction to "link" them for reconcilation.

### What is it not good for?

* The regular expressions are manually added and maintained by the user. The CLI tool does not make predictions from them. In other words, there is no machine learning.
* The regular expressions helps the user to mark potentional duplicates. However, duplicate transactions for a money transfer between two bank account will exist. The CLI tool does not reconcile them. Same as Beancount, the user is expected to do so.

### What is it *not yet* good for?

* The tool supports only transactions with one source account and one target account. It does not support [splitting expenses][] as described in Beancount's documentation. For example, if there is a hotel bill that combines lodging, food and entertainment costs in one charge, this tool can not help with splitting that expense into three different expense accounts.
* The tool does not support transactions with currency exchanges.

## What does success look like for this project?

If I can only list 3 requirements:

1. Data ingest. I plan to query my ledger like a database. The financial data files must be ingested correctly.
2. Reusability. Every month, I import data from 10+ accounts.
3. Automated tests. As I add more importers and features, I will break things. Automated tests helps with shipping working code.


[splitting expenses]: https://beancount.github.io/docs/sharing_expenses_with_beancount.html#splitting-expenses

## What are the innovations?

* Parsing the CSV file from each financial instituation to standard data structure, [Pandas Dataframe](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html).
* [Reserved words](usage/tags.md) in tags injects additional metadata to a Beancount transaction.
    * I didn't do a survey of tools out there, just a gut feeling.
