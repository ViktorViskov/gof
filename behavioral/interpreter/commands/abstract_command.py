from abc import ABC
from abc import abstractmethod
from models.pizza import Pizza


class AbstractCommand(ABC):
    @abstractmethod
    def invoke(self, pizza: Pizza) -> None:
        pass

    @abstractmethod
    def undo(self, pizza: Pizza) -> None:
        pass