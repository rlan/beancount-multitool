import pandas as pd

from .Institution import Institution
from .read_config import read_config
from .as_transaction import as_transaction


class RakutenCard(Institution):
    NAME = "rakuten_card"  # used in cli.py and in tests

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

        # Rename column names to English.
        column_names = {
            "利用日": "Date",
            "利用店名・商品名": "Description",
            # "利用者": "User",
            # "支払方法": "Payment method",
            # "利用金額": "Amount",
            # "支払手数料": "Commission paid",
            "支払総額": "Total",
            # "新規サイン": "New sign",
        }
        df.rename(columns=column_names, inplace=True)

        df["Date"] = pd.to_datetime(df["Date"], format="%Y/%m/%d")

        # Remove rows with empty 支払総額 cell.
        # These are extra info such as name of ETC gate or currency exchange rate.
        # TODO record as metadata
        extra = df.loc[pd.isnull(df["Total"])]
        df.drop(extra.index, inplace=True)
        # Convert to int type because currency is JPY
        df = df.astype({"Total": int})

        # Remove rows with zero 支払総額. These are refunds.
        # TODO record as metadata.
        refund = df.loc[df["Total"] == 0]
        df.drop(refund.index, inplace=True)

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
        target_account = self.config["default"]["account"]
        narration = self.config["default"]["narration"]
        tag = self.config["default"]["tag"]
        flag = self.config["default"]["flag"]

        with open(file_name, "w", encoding="utf-8") as f:
            for row in df.index:
                date = df["Date"][row]
                amount = df["Total"][row]
                payee = df["Description"][row]
                output = as_transaction(
                    date,
                    payee,
                    narration,
                    tag,
                    source_account,
                    target_account,
                    amount,
                    currency,
                    flag,
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
