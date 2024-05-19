from datetime import datetime
import pandas as pd

from .Institution import Institution
from .read_config import read_config
from .as_transaction import as_transaction


class JABank(Institution):
    NAME = "ja_bank"  # used in cli.py and in tests

    def __init__(self, config_file: str):
        # params
        self.config_file = config_file

        self.config = read_config(config_file)

    def read_transaction(self, file_name: str, year: int) -> pd.DataFrame:
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
        df = pd.read_csv(file_name, encoding="shift_jis_2004")
        print(f"Found {len(df.index)} transactions in {file_name}")

        # Rename column names to English
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
        df.rename(columns=column_names, inplace=True)

        # Convert date column to a datetime object
        df["Date"] = pd.to_datetime(
            str(year) + "." + df["Handling Date"], format="%Y.%m月%d日"
        )

        cols = ["Debit", "Credit", "Balance"]
        df[cols] = df[cols].replace({"\¥": "", ",": ""}, regex=True)
        df.fillna({"Debit": 0, "Credit": 0}, inplace=True)
        # Convert float to int
        df[cols] = df[cols].astype(int)
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
                classification = df["Transaction Classification"][row]
                description = df["Description"][row]
                payee = classification + description
                debit = df["Debit"][row]
                credit = df["Credit"][row]

                if credit == 0:  # a debit
                    output = as_transaction(
                        date,
                        payee,
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
                        payee,
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
        year = datetime.now().year
        df = self.read_transaction(csv_file, 2024)
        self.write_bean(df, bean_file)
