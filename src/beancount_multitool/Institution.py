from abc import ABC, abstractmethod


class Institution(ABC):
    @abstractmethod
    def convert(self, csv_file: str, bean_file: str):
        raise NotImplementedError  # abstract
