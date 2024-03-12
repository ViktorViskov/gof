from abc import ABC
from abc import abstractmethod


class AbstractOven(ABC):
    @abstractmethod
    def bake(self) -> None:
        pass