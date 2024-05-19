import datetime
import decimal


def as_transaction(
    date: datetime.datetime,
    payee: str,
    narration: str,
    tags: list[str],
    source_account: str,
    target_account: str,
    amount: decimal.Decimal,
    currency: str,
    flag: str = "",
) -> str:
    """
    Given transaction details, returns a beancount transaction entry.

    Returns
    -------
    str
        A beancount transaction entry:

        {date} * "{payee}" "{narration}" {" ".join(tags)}
          {source_account}
          {flag}{target_account}  {amount} {currency}
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
    output += f"  {source_account}\n"
    output += f"  {flag_str}{target_account}  {amount} {currency}\n"
    return output
