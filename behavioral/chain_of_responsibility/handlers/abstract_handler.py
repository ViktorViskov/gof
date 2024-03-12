from abc import ABC
from abc import abstractmethod


class AbstractHandler(ABC):
    @abstractmethod
    def can_do(self) -> bool:
        pass

    @abstractmethod
    def do(self):
        pass