import datetime
import decimal


def as_transaction(
    date: datetime.datetime,
    payee: str,
    narration: str,
    tags: list[str],
    source_account: str,
    account: str,
    amount: decimal.Decimal,
    currency: str,
    flag: str,
    metadata: dict,
    account_metadata: dict,
    **kwargs,
) -> str:
    """
    Given transaction details, returns a beancount transaction entry.

    Returns
    -------
    str
        A beancount transaction entry:

        {date} * "{payee}" "{narration}" {" ".join(tags)}
          for key, value in metadata:
            {key}: "{value}"
          {source_account}
          {flag}{account}  {amount} {currency}
            for key, value in metadata:
              {key}: "{value}"
    """
    # Add "#" prefix if does not exist
    hashtags = []
    for x in tags:
        if len(x):
            if x.startswith("#"):
                hashtags.append(x)
            else:
                hashtags.append("#" + x)
    if len(hashtags):
        tags_str = "  " + " ".join(hashtags)
    else:
        tags_str = ""

    # prepare flag
    flag_str = flag.strip()
    if len(flag_str):
        flag_str = flag_str + "  "

    output = "\n"
    output += f'{date.strftime("%Y-%m-%d")} * "{payee}" "{narration}"{tags_str}\n'
    for key, value in metadata.items():
        output += f'  {key}: "{value}"\n'
    output += f"  {source_account}\n"
    output += f"  {flag_str}{account}  {amount} {currency}\n"
    return output
