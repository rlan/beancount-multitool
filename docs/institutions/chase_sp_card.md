# Chase Sappire Preferred VISA Card

[https://www.chase.com/](https://www.chase.com/)

## How to download transactions

TODO

## CSV file

Header row:

```csv
Transaction Date,Post Date,Description,Category,Type,Amount,Memo
```

### Regular expressions

Regular expressions uses `Description` for matching.

## Example: label all transactions as default

[One](https://github.com/rlan/beancount-multitool/tree/main/tests/data/chase_sp_card) of the automated tests does exactly this. Let's download and run it locally.

```sh
wget https://raw.githubusercontent.com/rlan/beancount-multitool/main/tests/data/chase_sp_card/config.toml
wget https://raw.githubusercontent.com/rlan/beancount-multitool/main/tests/data/chase_sp_card/credit_mapping.toml
wget https://raw.githubusercontent.com/rlan/beancount-multitool/main/tests/data/chase_sp_card/debit_mapping.toml
wget https://raw.githubusercontent.com/rlan/beancount-multitool/main/tests/data/chase_sp_card/test.bean
wget https://raw.githubusercontent.com/rlan/beancount-multitool/main/tests/data/chase_sp_card/test.csv
bean-mt chase_sp_card config.toml test.csv --output out.bean
```
