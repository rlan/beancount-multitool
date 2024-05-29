# Rakuten Card 楽天カード

[https://www.rakuten-card.co.jp/](https://www.rakuten-card.co.jp/)

## How to download transactions

TODO

## CSV file

Header row:

```csv
"利用日","利用店名・商品名","利用者","支払方法","利用金額","支払手数料","支払総額","10月支払金額","11月繰越残高","新規サイン"
```

### Regular expressions

Regular expressions uses `利用店名・商品名` for matching.

## Example: label all transactions as default

[One](https://github.com/rlan/beancount-multitool/tree/main/tests/data/rakuten_card) of the automated tests does exactly this. Let's download and run it locally.

```sh
wget https://raw.githubusercontent.com/rlan/beancount-multitool/main/tests/data/rakuten_card/config.toml
wget https://raw.githubusercontent.com/rlan/beancount-multitool/main/tests/data/rakuten_card/credit_mapping.toml
wget https://raw.githubusercontent.com/rlan/beancount-multitool/main/tests/data/rakuten_card/debit_mapping.toml
wget https://raw.githubusercontent.com/rlan/beancount-multitool/main/tests/data/rakuten_card/test.bean
wget https://raw.githubusercontent.com/rlan/beancount-multitool/main/tests/data/rakuten_card/test.csv
bean-mt rakuten_card config.toml test.csv --output out.bean
```
