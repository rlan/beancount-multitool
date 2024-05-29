# SBI Shinsei Bank SBI 新生銀行

[https://www.sbishinseibank.co.jp/](https://www.sbishinseibank.co.jp/)

## How to download transactions

TODO

## CSV file

The header row can be in English or in Japanese.
Japanese header row:

```csv
"取引日","摘要","出金金額","入金金額","残高"
```

English header row:

```csv
"Value Date","Description","Debit","Credit","Balance"
```

### Regular expressions

Regular expressions uses `摘要` (or `Description`) for matching.

### On sender memo

The raw CSV file does not contain the sender memo that one enters during outgoing money transfers. This info is recorded in the bank's PDF files, instead. My current workaround is manually copying that text from the PDF to the `摘要` (or `Description`) column in the CSV.

## Example: label all transactions as default

[One](https://github.com/rlan/beancount-multitool/tree/main/tests/data/shinsei_bank) of the automated tests does exactly this. Let's download and run it locally.

```sh
wget https://raw.githubusercontent.com/rlan/beancount-multitool/main/tests/data/shinsei_bank/config.toml
wget https://raw.githubusercontent.com/rlan/beancount-multitool/main/tests/data/shinsei_bank/credit_mapping.toml
wget https://raw.githubusercontent.com/rlan/beancount-multitool/main/tests/data/shinsei_bank/debit_mapping.toml
wget https://raw.githubusercontent.com/rlan/beancount-multitool/main/tests/data/shinsei_bank/test.bean
wget https://raw.githubusercontent.com/rlan/beancount-multitool/main/tests/data/shinsei_bank/test.csv
bean-mt shinsei_bank config.toml test.csv --output out.bean
```
