# Workflow

A typical workflow using the CLI tool with a Beancount ledger:

1. Download the raw CSV file from a financial institution.
2. Run `bean-mt` CLI tool on the CSV file.
3. Inspect the resulting `output.bean` file for uncategorized transactions.
4. Edit [configurations](configs.md) (i.e. regular expressions and etc) and repeat previous step.
5. Include `output.bean` in the Beancount ledger.

## What to do next?

* For quick start, choose [one](../institutions/index.md) of the financial institutions. Then modify the label-all-as-default example to suit your needs.
* Learn about [configurations](configs.md) of `bean-mt` CLI tool.
* Here are some [examples](examples.md) of common usage.
