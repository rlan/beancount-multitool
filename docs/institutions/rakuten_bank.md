# Rakuten Bank 楽天銀行

[https://www.rakuten-bank.co.jp/](https://www.rakuten-bank.co.jp/)

## How to download transactions

TODO

## CSV file

Header row:

```csv
取引日,入出金(円),取引後残高(円),入出金内容
```

Regular expressions uses `入出金内容` for matching.

## Example: label all transactions as default

One of the automated tests does exactly this. Let's download it and run it locally.

```sh
mkdir rakuten_bank
cd rakuten_bank
wget https://raw.githubusercontent.com/rlan/beancount-multitool/main/tests/data/rakuten_bank/config.toml
wget https://raw.githubusercontent.com/rlan/beancount-multitool/main/tests/data/rakuten_bank/credit_mapping.toml
wget https://raw.githubusercontent.com/rlan/beancount-multitool/main/tests/data/rakuten_bank/debit_mapping.toml
wget https://raw.githubusercontent.com/rlan/beancount-multitool/main/tests/data/rakuten_bank/test.bean
wget https://raw.githubusercontent.com/rlan/beancount-multitool/main/tests/data/rakuten_bank/test.csv
bean-mt rakuten_bank config.toml test.csv --output out.bean
```
