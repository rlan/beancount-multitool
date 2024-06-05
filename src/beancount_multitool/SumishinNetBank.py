from decimal import Decimal
from pathlib import Path

import pandas as pd

from .Institution import Institution
from .MappingDatabase import MappingDatabase
from .read_config import read_config
from .as_transaction import as_transaction
from .get_value import get_value
from .get_beancount_config import get_beancount_config


class SumishinNetBank(Institution):
    NAME = "sumishin_net_bank"  # used in cli.py and in tests

    def __init__(self, config_file: str):
        # params
        self.config_file = config_file
        # attributes
        self.config = read_config(config_file)
        self.beancount_config = get_beancount_config(self.config)
        # Use basedir of config_file to read mapping database files
        base_dir = Path(config_file).parent
        credit_file = get_value(self.config, "database", "credit_mapping")
        self.credit_file = str(base_dir / credit_file)
        debit_file = get_value(self.config, "database", "debit_mapping")
        self.debit_file = str(base_dir / debit_file)
        self.credit_db = MappingDatabase(self.credit_file)
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
            "日付": pd.to_datetime,
            "出金金額(円)": str,
            "入金金額(円)": str,
            "残高(円)": str,
        }
        df = pd.read_csv(file_name, encoding="shift_jis", converters=converters)
        print(f"Found {len(df.index)} data transactions")
        # Rename column names to English.
        # "日付","内容","出金金額(円)","入金金額(円)","残高(円)","メモ"
        # "Date","Description","Debit","Credit","Balance","Memo"
        # Lowercase names will be keyword arguments later.
        columns = {
            "日付": "date",
            "内容": "Description",
            "出金金額(円)": "Debit",
            "入金金額(円)": "Credit",
            "残高(円)": "Balance",
            "メモ": "Memo",
        }
        df.rename(columns=columns, inplace=True)

        df.replace(
            to_replace="",
            value={"Debit": "0", "Credit": "0", "Balance": "0"},
            inplace=True,
        )
        df.replace(
            to_replace=",",
            value={"Debit": "", "Credit": "", "Balance": ""},
            inplace=True,
            regex=True,
        )
        df["Debit"] = df["Debit"].apply(Decimal)
        df["Credit"] = df["Credit"].apply(Decimal)
        df["Balance"] = df["Balance"].apply(Decimal)

        df["memo"] = df["Description"] + df["Memo"]

        df["amount"] = df["Credit"] - df["Debit"]

        # Reverse row order because the oldest transaction is on the bottom
        # Note: the index column is also reversed
        df = df[::-1]
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
                    metadata = {"memo": memo}

                    if amount < 0:  # a debit
                        accounts = self.debit_db.match(memo)
                    else:  # a credit
                        accounts = self.credit_db.match(memo)

                    account_metadata = {}
                    for x in range(1, len(accounts)):
                        account_metadata[f"match{x+1}"] = str(accounts[x])

                    output = as_transaction(
                        date=date,
                        amount=-amount,
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
