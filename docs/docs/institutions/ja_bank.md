# JA Bank ＪＡネットバンク

## Homepage

[https://www.jabank.jp/](https://www.jabank.jp/)


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
    "取扱日付": "Handling Date",  # full name "Handling Date"
    "起算日": "Starting Date",
    "お支払金額": "Debit",  # full name = "Debit Amount"
    "お預り金額": "Credit",  # full name = "Credit Amount"
    "取引区分": "Transaction Classification",
    "残高": "Balance",
    "摘要": "Description",
}
```

The following two columns are concatentated then passed to regular expressions for matching: `Transaction Classification` and `Description`.
