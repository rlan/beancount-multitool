# SBI Shinsei Bank SBI 新生銀行

## Homepage

[https://www.sbishinseibank.co.jp/](https://www.sbishinseibank.co.jp/)

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

The raw CSV file does not contain the sender memo that one enters during outgoing money transfers. This info is recorded in the bank's PDF files, instead. My current workaround is manually copying that text from the PDF to the "出金金額" or "Description" column in the CSV.
