import pandas as pd

from .Institution import Institution
from .read_config import read_config
from .as_transaction import as_transaction


class ShinseiBank(Institution):
    NAME = "shinsei_bank" # used in cli.py and in tests

    def __init__(self, config_file: str):
        # params
        self.config_file = config_file
        
        self.config = read_config(config_file)


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
        df = pd.read_csv(file_name)
        print(f"Found {len(df.index)} transactions in {file_name}")

        # Column names can be English or Japanese
        # "取引日","摘要","出金金額","入金金額","残高"
        # "Value Date","Description","Debit","Credit","Balance"
        # Rename column names
        column_names = {
            "取引日": "Date",
            "摘要": "Description",
            "出金金額": "Debit",
            "入金金額": "Credit",
            "残高": "Balance",
            "Value Date": "Date",
            # "Description": "Description",
            # "Debit": "Debit",
            # "Credit": "Credit",
            # "Balance": "Balance",
        }
        df.rename(columns=column_names, inplace=True)

        # Convert date column to a datetime object
        df["Date"] = pd.to_datetime(df["Date"], format="%Y/%m/%d")
        # Fill empty cells with zeros
        df.fillna(0, inplace=True)
        # Convert float to int
        df["Debit"] = df["Debit"].astype(int)
        df["Credit"] = df["Credit"].astype(int)

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

        currency = self.config["currency"]
        source_account = self.config["source_account"]
        credit_target_account = self.config["default"]["credit"]["account"]
        credit_narration = self.config["default"]["credit"]["narration"]
        credit_tag = self.config["default"]["credit"]["tag"]
        credit_flag = self.config["default"]["credit"]["flag"]
        debit_target_account = self.config["default"]["debit"]["account"]
        debit_narration = self.config["default"]["debit"]["narration"]
        debit_tag = self.config["default"]["debit"]["tag"]
        debit_flag = self.config["default"]["debit"]["flag"]

        with open(file_name, "w", encoding="utf-8") as f:
            for row in df.index:
                date = df["Date"][row]
                description = df["Description"][row]
                debit = df["Debit"][row]
                credit = df["Credit"][row]

                if credit == 0:  # a debit
                    output = as_transaction(
                        date,
                        description,
                        debit_narration,
                        debit_tag,
                        source_account,
                        debit_target_account,
                        debit,
                        currency,
                        debit_flag,
                    )
                else:  # a credit
                    output = as_transaction(
                        date,
                        description,
                        credit_narration,
                        credit_tag,
                        source_account,
                        credit_target_account,
                        -credit,
                        currency,
                        credit_flag,
                    )

                # print(output) # debug
                f.write(output)
            print(f"Written {file_name}")


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
