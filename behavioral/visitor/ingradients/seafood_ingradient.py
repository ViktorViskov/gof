from visitor.abstract_visitor import AbstractVisitor
from .abstract_ingradient import AbstractIngradient


class SeafoodIngradient(AbstractIngradient):
    def accept(self, visitor: AbstractVisitor) -> None:
        visitor.visit_seafood()