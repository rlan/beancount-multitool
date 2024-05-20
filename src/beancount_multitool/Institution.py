from abc import ABC, abstractmethod


class Institution(ABC):
    @abstractmethod
    def convert(self):
        raise NotImplementedError  # abstract
