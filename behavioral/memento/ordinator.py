from abc import (
    ABC,
    abstractmethod
)
from memento import Memento


class Ordinator(ABC):
    @abstractmethod
    def get_state(self) -> Memento:
        pass

    @abstractmethod
    def restore_state(self, state: Memento) -> None:
        pass