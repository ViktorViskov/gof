from abc import ABC
from abc import abstractmethod

from visitor.abstract_visitor import AbstractVisitor


class AbstractIngradient(ABC):
    @abstractmethod
    def accept(self, visitor: AbstractVisitor) -> None:
        pass