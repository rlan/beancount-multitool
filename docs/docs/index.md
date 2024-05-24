# Introduction

## What is it?

Beancount Multitool is a collection of tools for the end users of [Beancount](https://github.com/beancount/beancount).

## Why do I want it?

There is a command-line-interface (CLI) tool that converts financial data from financial institutions to Beancount files.

### What is it good for?

* The CLI tool saves me from typing transaction from statements. It tool can read raw CSV files downloaded from supported financial institutions. It converts the transactions in a CSV file to an importable Beancount file.
* For recurring expenses, the tool supports using regular expression to find them. Once found, they are labeled by the given account and/or hashtags.
* For outgoing money transfers, I can find them with regular expressions and label them with a reserved hashtag. An unique UUID string is generated and appended to the Beancount transaction. I can use this UUID to on the receiving end to "link" the two transactions.

### What is it not good for?

* The regular expressions are manually added or modified. The CLI tool does not make predictions from them. In other words, there is no machine learning.
* The duplicate transaction for a money transfer between two bank account still exist. The CLI tool does not reconcile them. I would have to.

### What is it *not yet* good for?

* TBD.
