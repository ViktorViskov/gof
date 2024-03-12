from abc import ABC
from abc import abstractmethod

from models.idish import IDish


class AbstractFactory(ABC):
    @abstractmethod
    def create_first(self) -> IDish:
        raise NotImplementedError()

    @abstractmethod
    def create_second(self) -> IDish:
        raise NotImplementedError()