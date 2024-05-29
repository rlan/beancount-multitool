# Tags

A generic Beancount transaction looks like this:

```txt
{date} * "{payee}" "{narration}" {" ".join({tags})}
  for key, value in {metadata}:  # aka transaction metadata
    {key}: "{value}"
  {source_account}
  {flag}{account}  {amount} {currency}
    for key, value in {account_metadata}:  # aka account metadata
      {key}: "{value}"
```

Tags are user input. Here we define a list of reserved words for tags that injects additional metadata.

* `#reconcile`
    * Adds a (random) uuid string to a `uuid` key to transaction metadata of a debit transaction (amount is negative). Example:

    ```txt
    uuid: "603cd901-a734-45d0-a100-dc01c22b5b4b"
    ```

    * Adds a empty string to a `uuid` key to transaction metadata of a credit transaction (amount is positive). Example:

    ```txt
    uuid: ""
    ```

    This is to reconcile duplicate transactions for a money transfer between two accounts. My personal convention is to keep the debit one, copy the UUID, paste the UUID to the credit one and comment the credit one.
