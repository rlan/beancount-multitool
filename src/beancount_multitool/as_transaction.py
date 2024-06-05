from datetime import datetime
from decimal import Decimal
import sys
from typing import Optional
import uuid


def make_hashtags(func):
    """Add # prefix if missing from any tags."""

    def add_hash(*args, **kwargs):
        hashtags = []
        for x in kwargs["tags"]:
            if len(x):
                if x.startswith("#"):
                    hashtags.append(x)
                else:
                    hashtags.append("#" + x)
        kwargs["tags"] = hashtags

        result = func(*args, **kwargs)
        return result

    return add_hash


def reconcile(func):
    """Add an UUID field if #reconcile tag exists"""

    def add_uuid(*args, **kwargs):
        # Add UUID for manual transactions reconcilation between accounts
        if "#reconcile" in kwargs["tags"]:
            if kwargs["amount"] < 0:  # a credit
                kwargs["metadata"]["uuid"] = ""
            else:  # a debit
                if hasattr(sys, "_called_from_pytest"):
                    # remove randomness during pytest
                    kwargs["metadata"]["uuid"] = "_called_from_pytest"
                else:
                    kwargs["metadata"]["uuid"] = str(uuid.uuid4())

        result = func(*args, **kwargs)
        return result

    return add_uuid


@reconcile
@make_hashtags
def as_transaction(
    date: Optional[datetime] = None,
    payee: str = "",
    narration: str = "",
    tags: Optional[list[str]] = None,
    source_account: str = "",
    account: str = "",
    amount: Decimal = Decimal(0),
    currency: str = "",
    flag: str = "",
    metadata: Optional[dict] = None,
    account_metadata: Optional[dict] = None,
    **kwargs,
) -> str:
    """
    Given transaction details, returns a beancount transaction entry.

    Returns
    -------
    str
        A beancount transaction entry:

        {date} * "{payee}" "{narration}" {" ".join({tags})}
          for key, value in {metadata}:
            {key}: "{value}"
          {source_account}
          {flag}{account}  {amount} {currency}
            for key, value in {account_metadata}:
              {key}: "{value}"
    """
    # Initialize None. Ref: https://docs.astral.sh/ruff/rules/mutable-argument-default/
    if date is None:
        date = datetime.today()
    if tags is None:
        tags = []
    if metadata is None:
        metadata = {}
    if account_metadata is None:
        account_metadata = {}

    if len(tags):
        tags_str = "  " + " ".join(tags)
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
    for key, value in account_metadata.items():
        output += f'    {key}: "{value}"\n'
    return output
