from abc import ABC
from abc import abstractmethod


class AbstractVisitor(ABC):
    @abstractmethod
    def visit_ananas(self) -> None:
        pass

    @abstractmethod
    def visit_bacon(self) -> None:
        pass

    @abstractmethod
    def visit_chease(self) -> None:
        pass

    @abstractmethod
    def visit_mashrooms(self) -> None:
        pass

    @abstractmethod
    def visit_seafood(self) -> None:
        pass

    @abstractmethod
    def visit_tomato(self) -> None:
        pass