# JA Bank ＪＡネットバンク

[https://www.jabank.jp/](https://www.jabank.jp/)

## How to download transactions

TODO

## CSV file

Header row:

```csv
"番号","明細区分","取扱日付","起算日","お支払金額","お預り金額","取引区分","残高","摘要"
```

In English:

```python
column_names = {
    "番号": "Number",
    "明細区分": "Detail Classification",
    "取扱日付": "Handling Date",
    "起算日": "Starting Date",
    "お支払金額": "Debit",
    "お預り金額": "Credit",
    "取引区分": "Transaction Classification",
    "残高": "Balance",
    "摘要": "Description",
}
```

Note on dates. On inspection of the CSV file, there are no year in dates, e.g. 4月30日. Thus, the tool uses the current year during conversion. So if you are converting data from last year, edit the generate bean file after conversion.

The following two columns are concatentated then passed to regular expressions for matching: `Transaction Classification` and `Description`.

## Example: label all transactions as default

[One](https://github.com/rlan/beancount-multitool/tree/main/tests/data/ja_bank) of the automated tests does exactly this. Let's download and run it locally.

```sh
mkdir ja_bank
cd ja_bank
wget https://raw.githubusercontent.com/rlan/beancount-multitool/main/tests/data/ja_bank/config.toml
wget https://raw.githubusercontent.com/rlan/beancount-multitool/main/tests/data/ja_bank/credit_mapping.toml
wget https://raw.githubusercontent.com/rlan/beancount-multitool/main/tests/data/ja_bank/debit_mapping.toml
wget https://raw.githubusercontent.com/rlan/beancount-multitool/main/tests/data/ja_bank/test.bean
wget https://raw.githubusercontent.com/rlan/beancount-multitool/main/tests/data/ja_bank/test.csv
bean-mt ja_bank config.toml test.csv --output out.bean
```
