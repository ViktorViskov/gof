from abc import ABC
from abc import abstractmethod

from models.idish import IDish


class AbstractFactory(ABC):
    @abstractmethod
    def create_dish(self) -> IDish:
        pass