# SBI Sumishin Net Bank 住信SBIネット銀行

[https://www.netbk.co.jp/](https://www.netbk.co.jp/)

## How to download transactions

TODO

## CSV file

Header row:

```csv
"日付","内容","出金金額(円)","入金金額(円)","残高(円)","メモ"
```

The following two columns are concatentated then passed to regular expressions for matching: `内容` and `メモ`.

## Example: label all transactions as default

[One](https://github.com/rlan/beancount-multitool/tree/main/tests/data/sumishin_net_bank) of the automated tests does exactly this. Let's download and run it locally.

```sh
wget https://raw.githubusercontent.com/rlan/beancount-multitool/main/tests/data/sumishin_net_bank/config.toml
wget https://raw.githubusercontent.com/rlan/beancount-multitool/main/tests/data/sumishin_net_bank/credit_mapping.toml
wget https://raw.githubusercontent.com/rlan/beancount-multitool/main/tests/data/sumishin_net_bank/debit_mapping.toml
wget https://raw.githubusercontent.com/rlan/beancount-multitool/main/tests/data/sumishin_net_bank/test.bean
wget https://raw.githubusercontent.com/rlan/beancount-multitool/main/tests/data/sumishin_net_bank/test.csv
bean-mt sumishin_net_bank config.toml test.csv --output out.bean
```
