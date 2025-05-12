from abc import ABC, abstractmethod


class DBConnectionURLBuilder(ABC):
    @abstractmethod
    def build(self, settings) -> str:
        pass
