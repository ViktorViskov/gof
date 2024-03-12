from visitor.abstract_visitor import AbstractVisitor
from .abstract_ingradient import AbstractIngradient


class MashroomsIngradient(AbstractIngradient):
    def accept(self, visitor: AbstractVisitor) -> None:
        visitor.visit_mashrooms()