from decimal import Decimal
from pathlib import Path

import pandas as pd

from .Institution import Institution
from .MappingDatabase import MappingDatabase
from .read_config import read_config
from .as_transaction import as_transaction
from .get_value import get_value
from .get_beancount_config import get_beancount_config


class RakutenCard(Institution):
    NAME = "rakuten_card"  # used in cli.py and in tests

    def __init__(self, config_file: str):
        # params
        self.config_file = config_file
        # attributes
        self.config = read_config(config_file)
        self.beancount_config = get_beancount_config(self.config)
        # Use basedir of config_file to read mapping database files
        base_dir = Path(config_file).parent
        debit_file = get_value(self.config, "database", "debit_mapping")
        self.debit_file = str(base_dir / debit_file)
        self.debit_db = MappingDatabase(self.debit_file)

    def read_transaction(self, file_name: str) -> pd.DataFrame:
        """Read financial transactions into a Pandas DataFrame.

        Parameters
        ----------
        file_name : str
            Input file name.

        Returns
        -------
        pd.DataFrame
            A dataframe after pre-processing.
        """
        converters = {
            "利用日": pd.to_datetime,
            "利用店名・商品名": str,
            "利用者": str,
            # "支払方法": "Payment method",
            # "利用金額": "Amount",
            # "支払手数料": "Commission paid",
            "支払総額": str,
        }
        df = pd.read_csv(file_name, converters=converters)
        print(f"Found {len(df.index)} transactions in {file_name}")

        # Rename column names to English.
        # "利用日","利用店名・商品名","利用者","支払方法","利用金額","支払手数料","支払総額","10月支払金額","11月繰越残高","新規サイン"
        # Lowercase names will be keyword arguments later.
        column_names = {
            "利用日": "date",
            "利用店名・商品名": "memo",
            "利用者": "user",
            # "支払方法": "Payment method",
            # "利用金額": "Amount",
            # "支払手数料": "Commission paid",
            "支払総額": "amount",
            # "新規サイン": "New sign",
        }
        df.rename(columns=column_names, inplace=True)

        # ETC transaction has a second row.
        # Update firsts to be concatenation of the two memos.
        # Then delete the seconds.
        etc_index = df.loc[df["user"] == "ETC"].index
        df.loc[etc_index, "memo"] = (
            df.loc[etc_index, "memo"].values
            + " "
            + df.loc[etc_index + 1, "memo"].values
        )
        df.drop(df.loc[df["user"] == ""].index, inplace=True)

        # Remove rows with zero 支払総額. These are refunds.
        # Also currency exchange rate(?)
        # TODO record as metadata.
        # refund = df.loc[df["amount"] == 0]
        # df.drop(refund.index, inplace=True)

        # TODO this will fail if the refund rows are not removed
        df["amount"] = df["amount"].apply(Decimal)

        # Reverse row order because the oldest transaction is on the bottom
        # Note: the index column is also reversed
        df = df[::-1]

        # print(df.dtypes) # debug
        # print(df) # debug
        return df

    def write_bean(self, df: pd.DataFrame, file_name: str) -> None:
        """Write Beancount transactions to file

        Parameters
        ----------
        df : pd.DataFrame
            Transaction dataframe.
        file_name : str
            Output file name.

        Returns
        -------
        None
        """
        try:
            with open(file_name, "w", encoding="utf-8") as f:
                for row in df.index:
                    date = df["date"][row]
                    amount = df["amount"][row]
                    memo = df["memo"][row]
                    metadata = {
                        "memo": memo,
                        "user": df["user"][row],
                    }

                    accounts = self.debit_db.match(memo)

                    account_metadata = {}
                    for x in range(1, len(accounts)):
                        account_metadata[f"match{x+1}"] = str(accounts[x])

                    output = as_transaction(
                        date=date,
                        amount=amount,
                        metadata=metadata,
                        account_metadata=account_metadata,
                        **accounts[0],
                        **self.beancount_config,
                    )
                    # print(output) # debug
                    f.write(output)
                print(f"Written {file_name}")
        except IOError as e:
            print(f"Error encountered while writing to: {file_name}")
            print(e)

    def convert(self, csv_file: str, bean_file: str):
        """Convert transactions in a CSV file to a Beancount file

        Parameters
        ----------
        csv_file : str
            Input CSV file name.

        bean_file : str
            Output Beancount file name.

        Returns
        -------
        None
        """
        df = self.read_transaction(csv_file)
        self.write_bean(df, bean_file)
